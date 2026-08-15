#!/usr/bin/env python3
"""Validate project structure, Skill integrity, references, CLI help, and regression format."""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def main() -> int:
    root = repo_root()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=root)
    parser.add_argument("--max-skill-lines", type=int, default=500)
    args = parser.parse_args()
    skill = args.root / "skill/kunting"
    required = [
        args.root / "AGENTS.md", args.root / "README.md", args.root / "pyproject.toml", skill / "SKILL.md",
        *[skill / "references" / name for name in ("visual-language.md", "color-system.md", "composition-system.md", "lighting-system.md", "light-color-architecture.md", "signature-color-response.md", "reference-color-transfer.md", "film-response.md", "casting-defaults.md", "character-system.md", "narrative-system.md", "prompt-template.md", "negative-constraints.md", "source-methodology.md", "output-calibration.md", "constraint-priority.md", "viewing-logic.md")],
        *[skill / "scripts" / name for name in ("extract_frames.py", "sample_frames.py", "build_manifest.py", "analyze_colors.py", "validate_skill.py", "run_tests.py")],
        skill / "assets/test_cases.json", args.root / "tests/inputs.json", args.root / "tests/expected_traits.json",
        args.root / "dataset/annotations/individual-template.json", args.root / "analysis/comparisons/cross-sample-rules.json"
    ]
    errors = []
    for path in required:
        if not path.exists():
            errors.append(f"缺少必要文件：{path.relative_to(args.root)}")
        elif path.is_file() and path.stat().st_size == 0:
            errors.append(f"空文件：{path.relative_to(args.root)}")
    skill_md = skill / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8") if skill_md.exists() else ""
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    expected_name = "name: kunting"
    expected_description = "description: 将用户的简单画面描述转化为复古犯罪类型片"
    if not match or expected_name not in match.group(1) or expected_description not in match.group(1):
        errors.append("SKILL.md frontmatter 缺失或与要求不符")
    if match:
        keys = [line.split(":", 1)[0].strip() for line in match.group(1).splitlines() if ":" in line]
        if keys != ["name", "description"]:
            errors.append(f"frontmatter 只能包含 name 和 description，当前为 {keys}")
    lines = text.splitlines()
    if len(lines) > args.max_skill_lines:
        errors.append(f"SKILL.md 过长：{len(lines)} 行 > {args.max_skill_lines}")
    for link in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        if not (skill / link).exists():
            errors.append(f"SKILL.md 内部引用无效：{link}")
    forbidden = ["Quentin Tarantino", "Tarantino", "Kill Bill", "Pulp Fiction", "昆汀", "杀死比尔", "低俗小说", "某导演风格"]
    for path in [skill_md, *(skill / "references").glob("*.md")]:
        body = path.read_text(encoding="utf-8")
        for term in forbidden:
            if term.lower() in body.lower():
                errors.append(f"禁止词出现在 {path.relative_to(args.root)}：{term}")
    image_only_forbidden = ["图像/视频媒介", "图像或视频提示词", "视频额外说明", "视频补充"]
    for path in [skill_md, skill / "references/prompt-template.md", skill / "references/visual-language.md"]:
        body = path.read_text(encoding="utf-8")
        for term in image_only_forbidden:
            if term in body:
                errors.append(f"图片 Skill 残留视频生成规则：{path.relative_to(args.root)}：{term}")
    for script in sorted((skill / "scripts").glob("*.py")):
        result = subprocess.run([sys.executable, str(script), "--help"], capture_output=True, text=True)
        if result.returncode != 0 or "usage:" not in result.stdout.lower():
            errors.append(f"脚本 --help 失败：{script.name}: {result.stderr.strip()}")
    regression = args.root / "tests/regression_results/latest.json"
    if regression.exists():
        body = regression.read_text(encoding="utf-8")
        if "【正向提示词】" not in body or "【负面约束】" not in body:
            errors.append("回归结果缺少要求的输出段落")
    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"VALIDATION PASSED: {len(required)} required files, {len(lines)} SKILL.md lines, all references and --help checks valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
