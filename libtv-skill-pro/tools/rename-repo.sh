#!/usr/bin/env bash
# 用户在 GitHub 网页把 libtv-skill-pro 重命名为 libtv-skill-pro 后跑这个脚本
# 一键完成本地 + ClawHub plugin + 文档全局同步
set -eu

OLD=libtv-skill-pro
NEW=libtv-skill-pro
OWNER=Qiuxiangxiang

echo "═══ Rename: $OLD → $NEW ═══"
echo ""

# ─── 1. 验证 GitHub 网页已改名 ───
echo "▸ 验证新 URL 是否可访问..."
HTTP_CODE=$(/usr/bin/curl -s -o /dev/null -w "%{http_code}" "https://github.com/$OWNER/$NEW")
if [ "$HTTP_CODE" != "200" ]; then
    echo "  ✗ https://github.com/$OWNER/$NEW 返回 HTTP $HTTP_CODE"
    echo "  请先到 https://github.com/$OWNER/$OLD/settings 把 repo 改名为 $NEW"
    exit 1
fi
echo "  ✓ 新 URL 可访问"

# ─── 2. 更新 git remote ───
SKILL_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$SKILL_ROOT"
echo ""
echo "▸ 更新本地 git remote..."
git remote set-url origin "git@github.com:$OWNER/$NEW.git"
echo "  $(git remote get-url origin)"

# ─── 3. 全局替换文档里的 repo URL ───
echo ""
echo "▸ 全局替换文档里的 $OLD → $NEW..."
FILES=(README.md SKILL.md CHANGELOG.md INTEGRATIONS.md)
for f in "${FILES[@]}"; do
    if [ -f "$f" ] && /usr/bin/grep -q "$OLD" "$f"; then
        /usr/bin/sed -i.bak "s|$OLD|$NEW|g" "$f"
        rm -f "$f.bak"
        echo "  ✓ $f"
    fi
done
# examples / cursor / tools 目录
for d in examples cursor tools; do
    if [ -d "$d" ]; then
        for f in "$d"/*.md "$d"/*.mdc "$d"/*.sh; do
            if [ -f "$f" ] && /usr/bin/grep -q "$OLD" "$f"; then
                /usr/bin/sed -i.bak "s|$OLD|$NEW|g" "$f"
                rm -f "$f.bak"
                echo "  ✓ $f"
            fi
        done
    fi
done

# ─── 4. Claude Code plugin/marketplace ───
echo ""
echo "▸ 更新 Claude Code marketplace homepage..."
MKT=~/.claude/libtv-marketplace/.claude-plugin/marketplace.json
PLG=~/.claude/libtv-marketplace/plugins/libtv-skill-pro/.claude-plugin/plugin.json
for cf in "$MKT" "$PLG"; do
    if [ -f "$cf" ] && /usr/bin/grep -q "$OLD" "$cf"; then
        /usr/bin/sed -i.bak "s|$OLD|$NEW|g" "$cf"
        rm -f "$cf.bak"
        echo "  ✓ $cf"
    fi
done

# ─── 5. CHANGELOG 加 0.4.4 entry ───
echo ""
echo "▸ CHANGELOG 加 0.4.4 entry..."
python3 - <<PYEOF
import re
content = open("CHANGELOG.md").read()
new_entry = """## [0.4.4] - 2026-05-14

**Renamed GitHub repo: libtv-skill-pro → libtv-skill-pro**

跟 ClawHub slug 保持一致，避免跨平台搜索割裂。GitHub 自带 redirect，旧 URL 仍可访问。

### Updated
- 文档里所有 \`github.com/Qiuxiangxiang/libtv-skill-pro\` → \`github.com/Qiuxiangxiang/libtv-skill-pro\`
- README.md 顶部 GitHub badges 链接更新
- Claude Code plugin/marketplace homepage 更新

---

"""
content = re.sub(r"(## \[0\.4\.3\])", new_entry + r"\1", content, count=1)
open("CHANGELOG.md", "w").write(content)
print("  ✓ CHANGELOG 0.4.4 entry inserted")
PYEOF

# ─── 6. commit + push GitHub ───
echo ""
echo "▸ commit + push GitHub..."
git add -A
git diff --cached --stat
git -c user.email=qiuxiangxiang@users.noreply.github.com \
    -c user.name=Qiuxiangxiang \
    commit -m "chore: rename repo libtv-skill-pro → libtv-skill-pro

Align GitHub repo name with ClawHub slug. GitHub redirect keeps old URLs working." 2>&1 | tail -3
git push 2>&1 | tail -3

# ─── 7. 同步 workspace + publish 0.4.4 ───
echo ""
echo "▸ Sync workspace..."
DST=~/.openclaw/workspace/skills/libtv-skills
cp "$SKILL_ROOT/SKILL.md" "$DST/SKILL.md"
cp "$SKILL_ROOT/README.md" "$DST/README.md"
rm -rf "$DST/examples"; mkdir -p "$DST/examples"; cp "$SKILL_ROOT/examples"/*.md "$DST/examples/"

echo ""
echo "▸ Patch publish.js + Publish 0.4.4..."
PUB_JS=/opt/homebrew/lib/node_modules/clawhub/dist/cli/commands/publish.js
cp "$PUB_JS" /tmp/publish.js.before-0.4.4
python3 -c "
src = open('$PUB_JS').read()
old = '''        form.set(\\'payload\\', JSON.stringify({
            slug,
            displayName,
            version,
            changelog,
            tags,
            ...(forkOf ? { forkOf } : {}),
        }));'''
new = '''        form.set(\\'payload\\', JSON.stringify({
            slug,
            displayName,
            version,
            changelog,
            tags,
            acceptLicenseTerms: true,
            ...(forkOf ? { forkOf } : {}),
        }));'''
if old in src:
    open('$PUB_JS', 'w').write(src.replace(old, new))
    print('  patched')
elif 'acceptLicenseTerms' in src:
    print('  already patched')
"

clawhub publish "$DST" \
    --slug libtv-skill-pro \
    --name "LibTV Skill Pro" \
    --version 0.4.4 \
    --fork-of libtv-skill@1.0.3 \
    --tags "latest,libtv,liblib,aigc,video,image-gen,agent-skill,text-to-video,text-to-image,chinese-ai" \
    --changelog "0.4.4 — GitHub repo 重命名为 libtv-skill-pro（与 ClawHub slug 对齐）。GitHub 自带 redirect，旧 link 仍可用。无功能变更。"

cp /tmp/publish.js.before-0.4.4 "$PUB_JS"

# ─── 8. Claude Code plugin 重装让 version 同步 ───
echo ""
echo "▸ Bump Claude Code plugin version..."
/usr/bin/sed -i.bak 's/"version": "0\.4\.3"/"version": "0.4.4"/' "$PLG"
rm -f "$PLG.bak"
claude plugin marketplace update libtv-marketplace 2>&1 | tail -1
claude plugin uninstall libtv-skill-pro 2>&1 | tail -1
claude plugin install libtv-skill-pro@libtv-marketplace 2>&1 | tail -1

echo ""
echo "═══ 完成 ═══"
echo ""
echo "GitHub:     https://github.com/$OWNER/$NEW"
echo "ClawHub:    https://clawhub.ai/qiuxiangxiang/libtv-skill-pro (0.4.4)"
echo "Claude Code plugin: 0.4.4"
echo ""
clawhub plugin list 2>&1 | /usr/bin/grep -A3 libtv 2>/dev/null || claude plugin list 2>&1 | /usr/bin/grep -A3 libtv | head -5
