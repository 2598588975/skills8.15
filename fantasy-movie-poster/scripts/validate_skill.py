#!/usr/bin/env python3
from __future__ import annotations
import re, sys
from pathlib import Path
def main()->int:
    root=Path(sys.argv[1] if len(sys.argv)>1 else ".").resolve(); errors=[]
    skill_files=list(dict.fromkeys([p.resolve() for p in list(root.rglob("SKILL.md"))+list(root.rglob("skill.md"))]))
    if len(skill_files)!=1: errors.append(f"expected exactly one SKILL.md, found {len(skill_files)}")
    else:
        text=skill_files[0].read_text(encoding="utf-8"); m=re.match(r"^---\s*\n(.*?)\n---\s*\n",text,re.S)
        if not m: errors.append("SKILL.md must start with YAML frontmatter")
        else:
            for key in ("name","description"):
                if not re.search(rf"^{key}:\s*.+$",m.group(1),re.M): errors.append(f"frontmatter missing {key}")
    for rel in ["agents/openai.yaml","references/genre-presets.md","templates/project-brief.json","scripts/build_prompt.py","data/genre-presets.json"]:
        if not (root/rel).exists(): errors.append(f"missing: {rel}")
    if errors: print("INVALID"); [print(f"- {e}") for e in errors]; return 1
    print("VALID"); print(f"skill root: {root}"); return 0
if __name__=="__main__": raise SystemExit(main())
