#!/usr/bin/env bash
# 同步 workspace + 发布 0.4.3。前提：先跑过 finalize-github.sh
# 用法：bash tools/publish-0.4.3.sh
set -eu

SRC="$(cd "$(dirname "$0")/.." && pwd)"
DST=~/.openclaw/workspace/skills/libtv-skills

echo "═══ Sync workspace ═══"
cp "$SRC/SKILL.md" "$DST/SKILL.md"
cp "$SRC/README.md" "$DST/README.md"
cp "$SRC/LICENSE" "$DST/LICENSE"
rm -rf "$DST/scripts"; mkdir -p "$DST/scripts"; cp "$SRC/scripts"/*.py "$DST/scripts/"
rm -rf "$DST/examples"; mkdir -p "$DST/examples"; cp "$SRC/examples"/*.md "$DST/examples/"
rm -rf "$DST/.clawhub" "$DST/_meta.json"
echo "  ok ($(find "$DST" -type f | wc -l) files)"

echo ""
echo "═══ Patch publish.js (acceptLicenseTerms) ═══"
PUB_JS=/opt/homebrew/lib/node_modules/clawhub/dist/cli/commands/publish.js
cp "$PUB_JS" /tmp/publish.js.before-0.4.3
python3 - <<PYEOF
src = open("$PUB_JS").read()
old = """        form.set('payload', JSON.stringify({
            slug,
            displayName,
            version,
            changelog,
            tags,
            ...(forkOf ? { forkOf } : {}),
        }));"""
new = """        form.set('payload', JSON.stringify({
            slug,
            displayName,
            version,
            changelog,
            tags,
            acceptLicenseTerms: true,
            ...(forkOf ? { forkOf } : {}),
        }));"""
if old in src:
    open("$PUB_JS", "w").write(src.replace(old, new))
    print("  patched")
elif "acceptLicenseTerms" in src:
    print("  already patched (skipping)")
else:
    print("  WARNING: patch target not found - publish may fail")
PYEOF

echo ""
echo "═══ Publish 0.4.3 ═══"
clawhub publish "$DST" \
  --slug libtv-skill-pro \
  --name "LibTV Skill Pro" \
  --version 0.4.3 \
  --fork-of libtv-skill@1.0.3 \
  --tags "latest,libtv,liblib,aigc,video,image-gen,agent-skill,text-to-video,text-to-image,chinese-ai" \
  --changelog "$(cat <<'EOF'
0.4.3 — GitHub repo + 透明版本记录

新增：
- GitHub 公开仓库（含 tests/ / CHANGELOG / INTEGRATIONS.md / cursor rule 等开发者文件，不发布到 ClawHub）
- README.md 顶部加 GitHub stars / issues badges
- SKILL.md fork-of 段加 Source / Issues 链接

版本记录（透明）：
- 0.4.1：尝试在 CLI publish 时发送 icon 字段，服务端 schema 拒收。无功能变更。
- 0.4.2：再试一种 icon 格式，同样被拒。无功能变更。
- 结论：ClawHub CLI 不支持设 icon；只有 web 表单支持。
EOF
)"

echo ""
echo "═══ Revert patch ═══"
cp /tmp/publish.js.before-0.4.3 "$PUB_JS"
echo "  reverted"

echo ""
echo "═══ Verify ═══"
clawhub inspect libtv-skill-pro 2>&1 | head -8
