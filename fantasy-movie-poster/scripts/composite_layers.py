#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from PIL import Image


def parse_size(value: str) -> tuple[int, int]:
    w, h = value.lower().split("x", 1)
    return int(w), int(h)


def parse_box(value: str, canvas: tuple[int, int]) -> tuple[int, int, int, int]:
    parts = [float(x.strip()) for x in value.split(",")]
    if len(parts) != 4:
        raise ValueError("box must be x,y,w,h")
    cw, ch = canvas
    if all(0 <= x <= 1 for x in parts):
        x, y, w, h = parts
        return int(x * cw), int(y * ch), int(w * cw), int(h * ch)
    return tuple(int(x) for x in parts)  # type: ignore[return-value]


def cover(im: Image.Image, size: tuple[int, int]) -> Image.Image:
    w, h = size
    iw, ih = im.size
    scale = max(w / iw, h / ih)
    nw, nh = int(iw * scale), int(ih * scale)
    im = im.resize((nw, nh), Image.Resampling.LANCZOS)
    return im.crop(((nw - w) // 2, (nh - h) // 2, (nw + w) // 2, (nh + h) // 2))


def fit(im: Image.Image, box: tuple[int, int, int, int]) -> Image.Image:
    _, _, bw, bh = box
    iw, ih = im.size
    scale = min(bw / iw, bh / ih)
    nw, nh = int(iw * scale), int(ih * scale)
    return im.resize((nw, nh), Image.Resampling.LANCZOS)


def blend(base: Image.Image, layer: Image.Image, mode: str, opacity: float) -> Image.Image:
    base = base.convert("RGBA")
    layer = layer.convert("RGBA")
    if opacity < 1:
        alpha = layer.getchannel("A").point(lambda v: int(v * opacity))
        layer.putalpha(alpha)
    if mode == "normal":
        return Image.alpha_composite(base, layer)
    b = base.convert("RGB")
    l = layer.convert("RGB")
    if mode == "screen":
        out = Image.new("RGB", b.size)
        bp, lp, op = b.load(), l.load(), out.load()
        for y in range(b.size[1]):
            for x in range(b.size[0]):
                br, bg, bb = bp[x, y]
                lr, lg, lb = lp[x, y]
                sr = 255 - (255 - br) * (255 - lr) // 255
                sg = 255 - (255 - bg) * (255 - lg) // 255
                sb = 255 - (255 - bb) * (255 - lb) // 255
                op[x, y] = (
                    int(br * (1 - opacity) + sr * opacity),
                    int(bg * (1 - opacity) + sg * opacity),
                    int(bb * (1 - opacity) + sb * opacity),
                )
        return out.convert("RGBA")
    if mode == "multiply":
        out = Image.new("RGB", b.size)
        bp, lp, op = b.load(), l.load(), out.load()
        for y in range(b.size[1]):
            for x in range(b.size[0]):
                br, bg, bb = bp[x, y]
                lr, lg, lb = lp[x, y]
                mr, mg, mb = br * lr // 255, bg * lg // 255, bb * lb // 255
                op[x, y] = (
                    int(br * (1 - opacity) + mr * opacity),
                    int(bg * (1 - opacity) + mg * opacity),
                    int(bb * (1 - opacity) + mb * opacity),
                )
        return out.convert("RGBA")
    raise ValueError(f"unsupported blend mode: {mode}")


def main() -> int:
    p = argparse.ArgumentParser(description="Composite image-designed poster layers by grid.")
    p.add_argument("--base", required=True)
    p.add_argument("--type", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--grid-out", required=True)
    p.add_argument("--canvas", default="1080x1920")
    p.add_argument("--type-box", default="0,0,1,1", help="x,y,w,h in pixels or 0-1 ratios")
    p.add_argument("--mode", choices=["screen", "multiply", "normal"], default="screen")
    p.add_argument("--opacity", type=float, default=1.0)
    args = p.parse_args()

    canvas = parse_size(args.canvas)
    base = cover(Image.open(args.base), canvas)
    layer_src = Image.open(args.type)
    box = parse_box(args.type_box, canvas)
    layer_fit = fit(layer_src, box)
    layer = Image.new("RGBA", canvas, (0, 0, 0, 0))
    x, y, bw, bh = box
    layer.alpha_composite(layer_fit.convert("RGBA"), (x + (bw - layer_fit.width) // 2, y + (bh - layer_fit.height) // 2))
    result = blend(base, layer, args.mode, max(0, min(1, args.opacity)))

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    result.convert("RGB").save(out, quality=95)
    grid = {
        "canvas": f"{canvas[0]}x{canvas[1]}",
        "base": str(Path(args.base).resolve()),
        "type": str(Path(args.type).resolve()),
        "type_box": box,
        "mode": args.mode,
        "opacity": args.opacity,
        "output": str(out.resolve()),
    }
    Path(args.grid_out).write_text(json.dumps(grid, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(grid, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
