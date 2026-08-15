#!/usr/bin/env python3
"""Build a complete Chinese movie-poster prompt from a project JSON file."""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRESETS = json.loads((ROOT / "data" / "genre-presets.json").read_text(encoding="utf-8"))

def as_text(value, sep="、"):
    if isinstance(value, list):
        return sep.join(str(x) for x in value if str(x).strip())
    return str(value or "").strip()

def choose_preset(genre: str):
    if genre in PRESETS:
        return PRESETS[genre]
    for key, value in PRESETS.items():
        if key in genre or genre in key:
            return value
    return {"composition":"电影静帧型","typography":"清晰可读的中文标题系统","palette":["一个主色","一个辅助色","一个强调色"],"texture":"克制电影胶片质感","avoid":["广告感","模板感","剧照拼贴"]}

def build(data: dict) -> str:
    genre = as_text(data.get("genre")) or "作者电影"
    preset = choose_preset(genre)
    title = as_text(data.get("title")) or "未命名电影"
    english_title = as_text(data.get("english_title")) or "可生成简短虚拟英文副题，弱于中文主标题"
    logline = as_text(data.get("logline")) or as_text(data.get("synopsis")) or "根据输入内容建立原创叙事。"
    era_location = "，".join(x for x in [as_text(data.get("era")), as_text(data.get("location"))] if x) or "根据剧情判断"
    relationship = as_text(data.get("relationship")) or "根据剧情判断人物关系"
    motif = as_text(data.get("primary_motif")) or "从剧情中选择一个一级视觉母题"
    supporting = as_text(data.get("supporting_clues")) or "最多两个辅助线索"
    composition = as_text(data.get("composition"))
    if not composition or composition == "auto": composition = preset["composition"]
    typography = as_text(data.get("typography"))
    if not typography or typography == "auto": typography = preset["typography"]
    palette = as_text(data.get("palette")) or as_text(preset["palette"])
    texture = as_text(data.get("texture")) or preset["texture"]
    reference_dna = as_text(data.get("reference_dna")) or "只吸收构图、光线、色彩或字图关系中的单一维度"
    avoid_items = list(preset.get("avoid", [])) + list(data.get("avoid", []) or [])
    avoid = as_text(list(dict.fromkeys(avoid_items)))
    ensemble = "使用有关系逻辑的群像构图" if data.get("ensemble") else "不强制群像，按一级视觉母题决定人物数量"
    return f"""生成一张原创电影海报，竖版 9:16，单张独立输出，不做拼图。

片名：《{title}》
英文副题：{english_title}
题材：{genre}
剧情：{logline}
时代与地点：{era_location}
人物关系：{relationship}
一级视觉母题：{motif}
辅助线索：{supporting}
构成模型：{composition}
人物策略：{ensemble}
字体系统：{typography}
色彩系统：{palette}
影像质感：{texture}
参考图学习范围：{reference_dna}

海报先建立明确的空间、人物或物件叙事，再安排文字。主标题清晰可读，英文副题退为辅助；底部只放少量虚拟制作信息。导演、编剧、制片、摄影、美术、视觉设计、剪辑、音乐、出品等署名全部统一为“梵想美学”。不要出现电影节、奖项、桂冠、官方入选、真实片商、真实导演、真实品牌或密集无意义小字。不要复制参考中的人物动作、场景骨架、道具组合、标题字形、标题位置和完整配色。

避免：{avoid}。"""

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: build_prompt.py <project.json>", file=sys.stderr); return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"Failed to read JSON: {exc}", file=sys.stderr); return 1
    print(build(data)); return 0

if __name__ == "__main__": raise SystemExit(main())
