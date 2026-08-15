#!/usr/bin/env python3
from __future__ import annotations
import re, sys
from pathlib import Path
FORBIDDEN=["电影节","影展","金棕榈","Palme d'Or","Sundance","Cannes","official selection","award winner","桂冠"]
ROLE_PATTERN=re.compile(r"(导演|编剧|制片|摄影|美术|视觉设计|剪辑|音乐|出品)\s*[/：:]?\s*([^\n/，,]+)")
def main()->int:
    if len(sys.argv)!=2: print("Usage: validate_poster_text.py <text-file>",file=sys.stderr); return 2
    text=Path(sys.argv[1]).read_text(encoding="utf-8"); errors=[]
    for term in FORBIDDEN:
        if term.lower() in text.lower(): errors.append(f"forbidden term: {term}")
    for role,name in ROLE_PATTERN.findall(text):
        if "梵想美学" not in name: errors.append(f"{role} credit must use 梵想美学")
    if errors: print("INVALID"); [print(f"- {e}") for e in errors]; return 1
    print("VALID"); return 0
if __name__=="__main__": raise SystemExit(main())
