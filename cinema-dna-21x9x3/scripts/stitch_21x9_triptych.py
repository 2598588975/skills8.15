#!/usr/bin/env python3
"""Crop images to 21:9 and vertically stitch them into one triptych."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


RATIO_W = 21
RATIO_H = 9


def crop_to_ratio(image: Image.Image, anchor_x: float = 0.5, anchor_y: float = 0.5) -> Image.Image:
    width, height = image.size
    if width * RATIO_H > height * RATIO_W:
        target_height = height
        target_width = int(round(height * RATIO_W / RATIO_H))
    else:
        target_width = width
        target_height = int(round(width * RATIO_H / RATIO_W))

    left = int(round((width - target_width) * max(0.0, min(1.0, anchor_x))))
    top = int(round((height - target_height) * max(0.0, min(1.0, anchor_y))))
    return image.crop((left, top, left + target_width, top + target_height))


def resize_to_width(image: Image.Image, width: int) -> Image.Image:
    if image.width == width:
        return image
    height = int(round(image.height * width / image.width))
    return image.resize((width, height), Image.Resampling.LANCZOS)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a vertical 21:9 x 3 triptych.")
    parser.add_argument("images", nargs=3, type=Path, help="Three source images.")
    parser.add_argument("--out", required=True, type=Path, help="Output image path.")
    parser.add_argument("--width", type=int, default=1920, help="Output width for each frame.")
    parser.add_argument("--gap", type=int, default=10, help="Black gap between frames in pixels.")
    parser.add_argument("--anchor-x", type=float, default=0.5)
    parser.add_argument("--anchor-y", type=float, default=0.5)
    args = parser.parse_args()

    frames: list[Image.Image] = []
    for path in args.images:
        with Image.open(path) as source:
            image = ImageOps.exif_transpose(source).convert("RGB")
            frames.append(resize_to_width(crop_to_ratio(image, args.anchor_x, args.anchor_y), args.width))

    total_height = sum(frame.height for frame in frames) + args.gap * (len(frames) - 1)
    canvas = Image.new("RGB", (args.width, total_height), (0, 0, 0))
    y = 0
    for frame in frames:
        canvas.paste(frame, (0, y))
        y += frame.height + args.gap

    args.out.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.out)
    print(f"Saved {args.out} ({canvas.width}x{canvas.height})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
