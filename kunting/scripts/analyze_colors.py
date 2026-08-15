#!/usr/bin/env python3
"""Compute auxiliary color statistics; never treats a palette as a complete style."""
from __future__ import annotations

import argparse
import colorsys
import json
import math
from pathlib import Path

try:
    from PIL import Image, ImageDraw
except ImportError:  # Allow --help before optional dependencies are installed.
    Image = None
    ImageDraw = None


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def rgb_to_lab(rgb: tuple[float, float, float]) -> list[float]:
    values = []
    for value in rgb:
        value /= 255.0
        values.append(value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4)
    r, g, b = values
    xyz = [(0.4124564*r + 0.3575761*g + 0.1804375*b) / 0.95047, 0.2126729*r + 0.7151522*g + 0.0721750*b, (0.0193339*r + 0.1191920*g + 0.9503041*b) / 1.08883]
    d = 6 / 29
    f = [v ** (1/3) if v > d**3 else v / (3*d*d) + 4/29 for v in xyz]
    return [round(116*f[1]-16, 3), round(500*(f[0]-f[1]), 3), round(200*(f[1]-f[2]), 3)]


def dominant_colors(im: Image.Image, count: int = 6) -> list[dict]:
    small = im.convert("RGB").resize((160, 160))
    quant = small.quantize(colors=count, method=Image.Quantize.MEDIANCUT)
    palette = quant.getpalette() or []
    total = small.width * small.height
    result = []
    for pixels, idx in sorted(quant.getcolors(total) or [], reverse=True):
        rgb = tuple(palette[idx * 3:idx * 3 + 3])
        hsv = colorsys.rgb_to_hsv(*(v / 255 for v in rgb))
        result.append({"rgb": rgb, "hsv": [round(hsv[0]*360, 2), round(hsv[1], 4), round(hsv[2], 4)], "lab": rgb_to_lab(rgb), "area_ratio": round(pixels/total, 4)})
    return result


def tint(pixels: list[tuple[int, int, int]]) -> dict:
    if not pixels:
        return {"rgb_mean": None, "lab_mean": None}
    mean = tuple(sum(pixel[i] for pixel in pixels) / len(pixels) for i in range(3))
    return {"rgb_mean": [round(v, 2) for v in mean], "lab_mean": [round(v, 2) for v in rgb_to_lab(mean)]}


def pixel_data(im: Image.Image) -> list[tuple[int, int, int]]:
    if hasattr(im, "get_flattened_data"):
        return list(im.get_flattened_data())
    return list(im.getdata())


def summarize_region(im: Image.Image) -> dict:
    pixels = pixel_data(im.convert("RGB"))
    luminances, saturations = [], []
    shadows = midtones = highlights = warm = cool = 0
    black_pixels, highlight_pixels = [], []
    for pixel in pixels:
        r, g, b = pixel
        lum = 0.2126*r + 0.7152*g + 0.0722*b
        hue, sat, _ = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        hue *= 360
        luminances.append(lum)
        saturations.append(sat)
        shadows += lum < 64
        midtones += 64 <= lum < 192
        highlights += lum >= 192
        warm += sat >= 0.15 and (hue < 75 or hue >= 330)
        cool += sat >= 0.15 and 150 <= hue < 300
        if lum < 32:
            black_pixels.append(pixel)
        if lum >= 224:
            highlight_pixels.append(pixel)
    total = len(pixels) or 1
    return {
        "dominant_colors": dominant_colors(im),
        "mean_luminance": round(sum(luminances)/total/255, 4),
        "tones": {"shadows": round(shadows/total, 4), "midtones": round(midtones/total, 4), "highlights": round(highlights/total, 4)},
        "saturation": {"mean": round(sum(saturations)/total, 4), "low": round(sum(v < .2 for v in saturations)/total, 4), "medium": round(sum(.2 <= v < .6 for v in saturations)/total, 4), "high": round(sum(v >= .6 for v in saturations)/total, 4)},
        "temperature_area": {"warm": round(warm/total, 4), "cool": round(cool/total, 4), "neutral_or_other": round((total-warm-cool)/total, 4)},
        "near_black_tint": tint(black_pixels),
        "highlight_tint": tint(highlight_pixels),
    }


def analyze(path: Path) -> dict:
    with Image.open(path) as image:
        im = image.convert("RGB")
        width, height = im.size
        im.thumbnail((512, 512))
    summary = summarize_region(im)
    thirds = {}
    labels = ("top", "middle", "bottom")
    for index, label in enumerate(labels):
        y0 = round(im.height * index / 3)
        y1 = round(im.height * (index + 1) / 3)
        thirds[label] = summarize_region(im.crop((0, y0, im.width, y1)))
    return {
        "file": str(path), "width": width, "height": height,
        **summary,
        "spatial_regions": {
            "method": "水平三等分；用于比较亮度拓扑与色彩落点，不能替代人物/布景/灯光/道具的人工语义标注。",
            "horizontal_thirds": thirds,
        },
        "interpretation_required": {"color_location": "人工标注：人物/服装/布景/灯光/道具", "narrative_emphasis": "人工判断", "repeated_across_samples": "跨样本报告确认", "warning": "色板仅为辅助数据，不能单独代表完整视觉风格。"},
    }


def palette_image(result: dict, output: Path) -> None:
    canvas = Image.new("RGB", (720, 120), "white")
    draw, x = ImageDraw.Draw(canvas), 0
    for item in result["dominant_colors"]:
        width = max(1, round(item["area_ratio"] * 720))
        draw.rectangle((x, 0, min(719, x + width), 119), fill=tuple(item["rgb"]))
        x += width
    canvas.save(output)


def main() -> int:
    root = repo_root()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path, default=root / "dataset/selected_frames")
    parser.add_argument("--output", type=Path, default=root / "analysis/color_palettes")
    parser.add_argument("--write-palettes", action="store_true")
    args = parser.parse_args()
    if Image is None:
        parser.error("缺少 Pillow；请运行 python3 -m pip install -e .")
    paths = [args.input] if args.input.is_file() else sorted(p for p in args.input.rglob("*") if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"})
    args.output.mkdir(parents=True, exist_ok=True)
    results = []
    for path in paths:
        result = analyze(path)
        try:
            result["file"] = str(path.relative_to(root))
        except ValueError:
            pass
        results.append(result)
        if args.write_palettes:
            palette_image(result, args.output / f"{path.stem}__palette.png")
    target = args.output / "color_analysis.json"
    target.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"analyzed {len(results)} images; auxiliary report: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
