#!/usr/bin/env python3
"""Extract interval, scene-cut, or start/middle/end shot frames with ffmpeg."""
from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
import sys
from pathlib import Path

VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".avi", ".m4v", ".webm"}
PTS_RE = re.compile(r"pts_time:([0-9.]+)")


def require_tools() -> None:
    missing = [name for name in ("ffmpeg", "ffprobe") if shutil.which(name) is None]
    if missing:
        raise RuntimeError(f"缺少视频工具：{', '.join(missing)}。请先安装 ffmpeg（其中应包含 ffprobe），再重新运行。")


def probe(path: Path) -> dict:
    command = ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height:format=duration", "-of", "json", str(path)]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    data = json.loads(result.stdout)
    stream = data["streams"][0]
    return {"duration": float(data["format"]["duration"]), "width": int(stream["width"]), "height": int(stream["height"])}


def scene_cuts(path: Path, threshold: float) -> list[float]:
    vf = f"select='gt(scene,{threshold})',showinfo"
    command = ["ffmpeg", "-hide_banner", "-i", str(path), "-vf", vf, "-an", "-f", "null", "-"]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode not in (0, 255):
        raise RuntimeError(result.stderr.strip() or "ffmpeg 场景检测失败")
    return sorted({float(match.group(1)) for match in PTS_RE.finditer(result.stderr)})


def timecode(seconds: float) -> str:
    seconds = max(0.0, seconds)
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h:02d}h{m:02d}m{s:06.3f}s"


def safe_stem(path: Path) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", path.stem).strip("-") or "source"


def extract_one(video: Path, timestamp: float, output: Path, quality: int) -> None:
    command = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", f"{timestamp:.3f}", "-i", str(video), "-frames:v", "1", "-q:v", str(quality), "-y", str(output)]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0 or not output.exists():
        raise RuntimeError(result.stderr.strip() or f"无法在 {timestamp:.3f}s 抽帧")


def dhash(path: Path) -> int:
    from PIL import Image
    with Image.open(path) as im:
        px = list(im.convert("L").resize((9, 8)).getdata())
    return sum(int(px[y * 9 + x] > px[y * 9 + x + 1]) << (y * 8 + x) for y in range(8) for x in range(8))


def reject_reason(path: Path, previous: list[int], duplicate_distance: int) -> str | None:
    from PIL import Image, ImageFilter, ImageStat
    with Image.open(path) as im:
        gray = im.convert("L").resize((160, 90))
        stats = ImageStat.Stat(gray)
        edge_std = ImageStat.Stat(gray.filter(ImageFilter.FIND_EDGES)).stddev[0]
    if stats.mean[0] < 8 and stats.stddev[0] < 8:
        return "black_frame"
    if stats.stddev[0] < 4 or edge_std < 2:
        return "low_information_transition"
    fingerprint = dhash(path)
    if any((fingerprint ^ old).bit_count() <= duplicate_distance for old in previous):
        return "near_duplicate"
    previous.append(fingerprint)
    return None


def samples_for(mode: str, duration: float, cuts: list[float], interval: float) -> list[tuple[float, int, str]]:
    if mode == "interval":
        return [(t, index + 1, "interval") for index, t in enumerate(frange(0.0, duration, interval))]
    boundaries = sorted({0.0, *[c for c in cuts if 0 < c < duration], duration})
    shots = list(zip(boundaries, boundaries[1:]))
    if mode == "scene":
        return [((start + end) / 2, index + 1, "scene") for index, (start, end) in enumerate(shots)]
    result = []
    for index, (start, end) in enumerate(shots, 1):
        length = end - start
        margin = min(0.15, max(0.01, length * 0.05))
        points = [(start + margin, "start"), ((start + end) / 2, "middle"), (max(start + margin, end - margin), "end")]
        for timestamp, label in points:
            result.append((min(timestamp, max(0.0, duration - 0.001)), index, label))
    return result


def frange(start: float, stop: float, step: float):
    value = start
    while value < stop:
        yield value
        value += step


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="视频文件或包含视频的目录")
    parser.add_argument("--output", type=Path, required=True, help="派生帧输出目录")
    parser.add_argument("--mode", choices=("interval", "scene", "shot-triplets"), default="shot-triplets")
    parser.add_argument("--interval", type=float, default=5.0, help="固定间隔秒数")
    parser.add_argument("--scene-threshold", type=float, default=0.35, help="ffmpeg scene 分数阈值")
    parser.add_argument("--duplicate-distance", type=int, default=4, help="dHash 汉明距离小于等于此值视为重复")
    parser.add_argument("--jpeg-quality", type=int, default=2, help="ffmpeg JPEG qscale，2 为高质量")
    parser.add_argument("--manifest", type=Path, help="抽帧 JSONL；默认写入输出目录")
    args = parser.parse_args()
    try:
        import PIL  # noqa: F401
    except ImportError:
        parser.error("缺少 Pillow；请运行 python3 -m pip install -e .")
    if args.interval <= 0:
        parser.error("--interval 必须大于 0")
    if not 0 <= args.scene_threshold <= 1:
        parser.error("--scene-threshold 必须在 0 到 1 之间")
    try:
        require_tools()
        videos = [args.input] if args.input.is_file() else sorted(p for p in args.input.rglob("*") if p.suffix.lower() in VIDEO_EXTS)
        if not videos:
            raise RuntimeError(f"未在 {args.input} 找到支持的视频文件")
        args.output.mkdir(parents=True, exist_ok=True)
        records, fingerprints = [], []
        for video in videos:
            info = probe(video)
            cuts = scene_cuts(video, args.scene_threshold) if args.mode != "interval" else []
            for timestamp, shot, label in samples_for(args.mode, info["duration"], cuts, args.interval):
                filename = f"{safe_stem(video)}__{timecode(timestamp)}__shot-{shot:03d}__{label}.jpg"
                target = args.output / filename
                extract_one(video, timestamp, target, args.jpeg_quality)
                reason = reject_reason(target, fingerprints, args.duplicate_distance)
                record = {"source_video": str(video), "timestamp": round(timestamp, 3), "timecode": timecode(timestamp), "shot_id": f"shot-{shot:03d}", "extraction_method": args.mode, "representative_position": label, "width": info["width"], "height": info["height"], "output_file": str(target), "selected": reason is None, "rejection_reason": reason}
                if reason:
                    target.unlink(missing_ok=True)
                records.append(record)
        manifest = args.manifest or args.output / "extraction_manifest.jsonl"
        with manifest.open("w", encoding="utf-8") as handle:
            for record in records:
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        kept = sum(record["selected"] for record in records)
        print(f"processed {len(videos)} videos; kept {kept}/{len(records)} frames; manifest: {manifest}")
        return 0
    except (RuntimeError, subprocess.SubprocessError, OSError, KeyError, ValueError) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
