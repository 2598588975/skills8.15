#!/usr/bin/env python3
"""Build a neutral JSONL manifest for screenshots and extracted frames."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}
FRAME_RE = re.compile(r"__(\d{2})h(\d{2})m(\d{2}(?:\.\d+)?)s__shot-(\d+)__(\w+)")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def item_id(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def metadata(path: Path, root: Path) -> dict:
    from PIL import Image
    with Image.open(path) as image:
        width, height = image.size
    match = FRAME_RE.search(path.stem)
    timestamp = None
    shot_id = None
    method = None
    if match:
        h, m, s, shot, method = match.groups()
        timestamp = round(int(h) * 3600 + int(m) * 60 + float(s), 3)
        shot_id = f"shot-{int(shot):03d}"
    source_type = "video_frame" if "extracted_frames" in path.parts else "screenshot"
    category = method if source_type == "video_frame" else "unclassified"
    return {
        "id": item_id(path),
        "source_file": str(path.relative_to(root)),
        "source_type": source_type,
        "timestamp": timestamp,
        "shot_id": shot_id,
        "width": width,
        "height": height,
        "aspect_ratio": round(width / height, 4),
        "category": category,
        "selected": False,
        "notes": "",
        "analysis_status": "pending",
        "extraction_method": method,
    }


def main() -> int:
    root = repo_root()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--screenshots", type=Path, default=root / "input/screenshots")
    parser.add_argument("--frames", type=Path, default=root / "dataset/extracted_frames")
    parser.add_argument("--output", type=Path, default=root / "dataset/manifests/media.jsonl")
    args = parser.parse_args()
    try:
        import PIL  # noqa: F401
    except ImportError:
        parser.error("缺少 Pillow；请运行 python3 -m pip install -e .")

    paths = []
    for directory in (args.screenshots, args.frames):
        if directory.exists():
            paths.extend(p for p in directory.rglob("*") if p.suffix.lower() in IMAGE_EXTS)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        for path in sorted(paths):
            handle.write(json.dumps(metadata(path.resolve(), root), ensure_ascii=False) + "\n")
    print(f"wrote {len(paths)} records to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
