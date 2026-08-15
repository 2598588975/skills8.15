#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_project.py <project.json>", file=sys.stderr); return 2
    try: data=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except Exception as exc: print(f"INVALID: {exc}"); return 1
    errors=[]
    if not isinstance(data,dict): errors.append("root must be an object")
    if not any(str(data.get(k," ")).strip() for k in ("title","genre","logline","synopsis")): errors.append("provide title, genre, logline or synopsis")
    if data.get("aspect_ratio","9:16")!="9:16": errors.append("aspect_ratio must be 9:16")
    if data.get("credits_name","梵想美学")!="梵想美学": errors.append("credits_name must be 梵想美学")
    if len(data.get("supporting_clues",[]) or [])>2: errors.append("supporting_clues must contain at most 2 items")
    if errors:
        print("INVALID"); [print(f"- {e}") for e in errors]; return 1
    print("VALID"); return 0
if __name__ == "__main__": raise SystemExit(main())
