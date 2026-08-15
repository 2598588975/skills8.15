#!/usr/bin/env python3
import argparse
import json
import math
import shutil
import subprocess
import sys
from pathlib import Path


def run_json(cmd):
    try:
        proc = subprocess.run(cmd, check=True, capture_output=True, text=True)
    except (OSError, subprocess.CalledProcessError):
        return None
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return None


def ffprobe_metadata(video):
    if not shutil.which("ffprobe"):
        return None
    data = run_json([
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=width,height,r_frame_rate,avg_frame_rate,duration,nb_frames:format=duration",
        "-of",
        "json",
        str(video),
    ])
    if not data:
        return None
    stream = (data.get("streams") or [{}])[0]
    fmt = data.get("format") or {}
    duration = stream.get("duration") or fmt.get("duration")
    return {
        "width": int(stream["width"]) if stream.get("width") else None,
        "height": int(stream["height"]) if stream.get("height") else None,
        "fps": parse_rate(stream.get("avg_frame_rate") or stream.get("r_frame_rate")),
        "duration": float(duration) if duration else None,
        "frames": int(stream["nb_frames"]) if str(stream.get("nb_frames", "")).isdigit() else None,
        "backend": "ffprobe",
    }


def parse_rate(value):
    if not value or value == "0/0":
        return None
    if "/" in value:
        a, b = value.split("/", 1)
        try:
            return float(a) / float(b)
        except ZeroDivisionError:
            return None
    try:
        return float(value)
    except ValueError:
        return None


def cv2_metadata(video):
    try:
        import cv2
    except Exception:
        return None
    cap = cv2.VideoCapture(str(video))
    if not cap.isOpened():
        return None
    fps = cap.get(cv2.CAP_PROP_FPS) or None
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT) or None
    duration = (frames / fps) if fps and frames else None
    meta = {
        "width": int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 0) or None,
        "height": int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 0) or None,
        "fps": float(fps) if fps else None,
        "duration": float(duration) if duration else None,
        "frames": int(frames) if frames else None,
        "backend": "opencv",
    }
    cap.release()
    return meta


def timestamps(duration, count):
    if not duration or duration <= 0:
        return [0.0]
    if count <= 1:
        return [min(duration * 0.5, max(duration - 0.05, 0.0))]
    start = min(0.2, duration * 0.05)
    end = max(duration - min(0.2, duration * 0.05), start)
    return [start + (end - start) * i / (count - 1) for i in range(count)]


def ffmpeg_extract(video, out_dir, times, max_width):
    if not shutil.which("ffmpeg"):
        return None
    out_files = []
    scale = f"scale='min({max_width},iw)':-2"
    for idx, t in enumerate(times, 1):
        dest = out_dir / f"frame_{idx:03d}_{t:.2f}s.jpg"
        cmd = [
            "ffmpeg",
            "-y",
            "-ss",
            f"{t:.3f}",
            "-i",
            str(video),
            "-frames:v",
            "1",
            "-vf",
            scale,
            "-q:v",
            "2",
            str(dest),
        ]
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            out_files.append(str(dest))
        except (OSError, subprocess.CalledProcessError):
            return None
    return out_files


def cv2_extract(video, out_dir, times, max_width):
    try:
        import cv2
    except Exception as exc:
        raise RuntimeError("Neither ffmpeg nor OpenCV is available for frame extraction.") from exc
    cap = cv2.VideoCapture(str(video))
    if not cap.isOpened():
        raise RuntimeError(f"Could not open video: {video}")
    out_files = []
    for idx, t in enumerate(times, 1):
        cap.set(cv2.CAP_PROP_POS_MSEC, max(t, 0.0) * 1000.0)
        ok, frame = cap.read()
        if not ok:
            continue
        h, w = frame.shape[:2]
        if w > max_width:
            scale = max_width / float(w)
            frame = cv2.resize(frame, (max_width, max(1, int(math.floor(h * scale)))))
        dest = out_dir / f"frame_{idx:03d}_{t:.2f}s.jpg"
        cv2.imwrite(str(dest), frame, [int(cv2.IMWRITE_JPEG_QUALITY), 92])
        out_files.append(str(dest))
    cap.release()
    return out_files


def main():
    parser = argparse.ArgumentParser(description="Extract video metadata and evidence frames.")
    parser.add_argument("video")
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--frames", type=int, default=12)
    parser.add_argument("--max-width", type=int, default=960)
    args = parser.parse_args()

    video = Path(args.video).expanduser().resolve()
    out_dir = Path(args.out_dir).expanduser().resolve()
    if not video.exists():
        raise SystemExit(f"Video not found: {video}")
    out_dir.mkdir(parents=True, exist_ok=True)

    meta = ffprobe_metadata(video) or cv2_metadata(video)
    if not meta:
        meta = {"width": None, "height": None, "fps": None, "duration": None, "frames": None, "backend": None}
    times = timestamps(meta.get("duration"), max(args.frames, 1))
    files = ffmpeg_extract(video, out_dir, times, args.max_width)
    if files is None:
        files = cv2_extract(video, out_dir, times, args.max_width)

    print(json.dumps({
        "video": str(video),
        "metadata": meta,
        "timestamps": times,
        "frames": files,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
