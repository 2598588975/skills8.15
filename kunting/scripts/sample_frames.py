#!/usr/bin/env python3
"""Select a visually diverse, deterministic subset without interpreting identities."""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def dhash(path: Path) -> int:
    from PIL import Image
    with Image.open(path) as im:
        gray = im.convert("L").resize((9, 8))
        px = list(gray.getdata())
    bits = [px[y * 9 + x] > px[y * 9 + x + 1] for y in range(8) for x in range(8)]
    return sum(int(bit) << i for i, bit in enumerate(bits))


def distance(a: int, b: int) -> int:
    return (a ^ b).bit_count()


def information(path: Path) -> float:
    from PIL import Image, ImageStat
    with Image.open(path) as im:
        stat = ImageStat.Stat(im.convert("L").resize((128, 128)))
    return stat.stddev[0]


def main() -> int:
    root = repo_root()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=root / "dataset/manifests/media.jsonl")
    parser.add_argument("--output", type=Path, default=root / "dataset/selected_frames")
    parser.add_argument("--max-frames", type=int, default=12)
    args = parser.parse_args()
    try:
        import PIL  # noqa: F401
    except ImportError:
        parser.error("缺少 Pillow；请运行 python3 -m pip install -e .")
    rows = [json.loads(line) for line in args.manifest.read_text(encoding="utf-8").splitlines() if line]
    candidates = []
    for row in rows:
        path = root / row["source_file"]
        score = information(path)
        if score >= 10:
            candidates.append((row, path, dhash(path), score))
    candidates.sort(key=lambda item: (-item[3], item[1].name))
    selected = []
    if candidates:
        selected.append(candidates.pop(0))
    while candidates and len(selected) < args.max_frames:
        best = max(candidates, key=lambda item: min(distance(item[2], chosen[2]) for chosen in selected))
        selected.append(best)
        candidates.remove(best)
    args.output.mkdir(parents=True, exist_ok=True)
    for old in args.output.iterdir():
        if old.is_file():
            old.unlink()
    selected_ids = {item[0]["id"] for item in selected}
    for index, (row, path, _, _) in enumerate(selected, 1):
        shutil.copy2(path, args.output / f"selected-{index:03d}__{row['id']}{path.suffix.lower()}")
    for row in rows:
        row["selected"] = row["id"] in selected_ids
        if row["selected"]:
            row["analysis_status"] = "selected_pending_annotation"
    with args.manifest.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"selected {len(selected)} of {len(rows)} records into {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
