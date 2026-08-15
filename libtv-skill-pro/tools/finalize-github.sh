#!/usr/bin/env bash
# 一键替换所有 GitHub URL 占位符 + 加 badges
# 用法：bash tools/finalize-github.sh https://github.com/Qiuxiangxiang/libtv-skill-pro
set -eu

if [ "$#" -lt 1 ]; then
    echo "用法：bash tools/finalize-github.sh <GitHub repo URL>"
    echo "示例：bash tools/finalize-github.sh https://github.com/Qiuxiangxiang/libtv-skill-pro"
    exit 1
fi

REPO_URL="$1"
# 提取 owner/repo 部分（如 Qiuxiangxiang/libtv-skill-pro）
REPO_PATH=$(echo "$REPO_URL" | sed -E 's|https?://github\.com/||' | sed 's|\.git$||')
REPO_OWNER=$(echo "$REPO_PATH" | cut -d/ -f1)

echo "═══ Finalize GitHub URL → $REPO_URL ═══"
echo "Owner: $REPO_OWNER | Path: $REPO_PATH"
echo ""

SKILL_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$SKILL_ROOT"

# 1. README.md: 替换 YOUR_HANDLE
echo "▸ README.md: 替换 YOUR_HANDLE"
sed -i.bak "s|github.com/YOUR_HANDLE/libtv-skill-pro|github.com/${REPO_PATH}|g" README.md
rm -f README.md.bak

# 2. README.md: 在顶部 badges 行追加 GitHub badges
echo "▸ README.md: 加 GitHub badges"
python3 - <<PYEOF
import re
content = open("README.md").read()
old_badges = """[![ClawHub](https://img.shields.io/badge/ClawHub-libtv--skill--pro-orange)](https://clawhub.ai/qiuxiangxiang/libtv-skill-pro)
[![License](https://img.shields.io/badge/license-MIT--0-blue)](LICENSE)"""
new_badges = f"""[![ClawHub](https://img.shields.io/badge/ClawHub-libtv--skill--pro-orange)](https://clawhub.ai/qiuxiangxiang/libtv-skill-pro)
[![GitHub stars](https://img.shields.io/github/stars/${REPO_PATH}?style=social)]($REPO_URL)
[![GitHub issues](https://img.shields.io/github/issues/${REPO_PATH})]($REPO_URL/issues)
[![License](https://img.shields.io/badge/license-MIT--0-blue)](LICENSE)"""
content = content.replace(old_badges, new_badges)
open("README.md", "w").write(content)
PYEOF

# 3. SKILL.md: 把 "Source / Issues: 见包内 README.md。" 换成 GitHub link
echo "▸ SKILL.md: 加 GitHub Source / Issues 链接"
sed -i.bak "s|Source / Issues: 见包内 README.md。|Source / Issues: $REPO_URL|g" SKILL.md
rm -f SKILL.md.bak

# 4. examples/README.md / 04-character-to-video.md（如果有 github 引用）
#    （目前 grep 显示无，留 hook）

# 5. ClawHub marketplace.json + plugin.json: homepage 加 GitHub
echo "▸ Claude Code marketplace homepage → GitHub"
MKT_FILE=~/.claude/libtv-marketplace/.claude-plugin/marketplace.json
PLG_FILE=~/.claude/libtv-marketplace/plugins/libtv-skill-pro/.claude-plugin/plugin.json
if [ -f "$MKT_FILE" ]; then
    python3 -c "
import json
p = '$MKT_FILE'
d = json.load(open(p))
for plugin in d.get('plugins', []):
    plugin['homepage'] = '$REPO_URL'
json.dump(d, open(p, 'w'), ensure_ascii=False, indent=2)
print(f'  updated {p}')
"
fi
if [ -f "$PLG_FILE" ]; then
    python3 -c "
import json
p = '$PLG_FILE'
d = json.load(open(p))
d['homepage'] = '$REPO_URL'
json.dump(d, open(p, 'w'), ensure_ascii=False, indent=2)
print(f'  updated {p}')
"
fi

# 6. CHANGELOG.md: 把已有 [0.4.0] 段前面加 0.4.3
echo "▸ CHANGELOG.md: 加 0.4.3 entry"
python3 - <<PYEOF
content = open("CHANGELOG.md").read()
new_entry = """## [0.4.3] - 2026-05-14

**主题：GitHub repo 上线 + 0.4.1/0.4.2 试错版本说明**

### Added
- GitHub 公开仓库：[$REPO_URL]($REPO_URL)
- README.md 顶部加 GitHub stars / issues badges
- SKILL.md fork-of 段加 Source / Issues 链接
- ClawHub marketplace homepage 指向 GitHub

### Notes（透明记录）
- **0.4.1**：尝试在 CLI publish 时发送 \`icon: {kind: "lucide", name: "film"}\` 字段，服务端 schema 直接丢弃。**无功能变更**。
- **0.4.2**：再试 \`icon: "lucide:film"\` 字符串，同样被丢弃。**无功能变更**。
- 结论：ClawHub CLI publish endpoint 不支持设 icon；只有 web publish 表单支持。
- 用户若想看 film 图标，需要 owner 在 \`https://clawhub.ai/skills/publish?updateSlug=libtv-skill-pro\` 网页表单手动设置一次。

---

"""
# 插入到 [0.4.0] 之前
import re
content = re.sub(r"(## \[0\.4\.0\])", new_entry + r"\1", content, count=1)
open("CHANGELOG.md", "w").write(content)
PYEOF

echo ""
echo "═══ Done. Diff 预览 ═══"
git diff --stat 2>/dev/null || echo "（非 git repo，跳过 diff stat）"
echo ""
echo "下一步："
echo "  1. cd $SKILL_ROOT && git add -A && git commit -m 'docs: link GitHub repo + add 0.4.3 changelog'"
echo "  2. git push"
echo "  3. cd to workspace, sync, publish 0.4.3:"
echo "     bash tools/publish-0.4.3.sh"
