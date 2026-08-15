#!/usr/bin/env bash
# 一键准备发邮件给 Frank Wang (haofanwang.ai@gmail.com)
# 1. 把中文邮件正文放剪贴板
# 2. 打开 Gmail 撰写界面（to + subject 已填好）
# 你需要做：到浏览器里 Cmd+V 粘贴正文 → Send

BODY_FILE=/tmp/haofanwang-email-body.txt

# 如果文件不存在，从 git repo 重新生成
if [ ! -s "$BODY_FILE" ]; then
    /bin/cat > "$BODY_FILE" <<'BODYEOF'
Frank 你好，

我是 ClawHub 上的 Qiuxiangxiang。基于你的 libtv-skill fork 了一个 Pro 版（ClawHub slug: libtv-skill-pro，GitHub: github.com/Qiuxiangxiang/libtv-skill-pro），想提前告诉你一下，而不是让你从别处发现。

保留你的工作（byte 级一致，已署名）：
- download_results.py / query_session.py / upload_file.py 三个脚本
- _common.py API client 结构
- SKILL.md 描述基础

新增（~17 个脚本）：
- 7 个高级工作流脚本：batch / monitor / poll / templates / export / history / project
- 4 个 LibTV 功能矩阵脚本：flow / node / edit / model —— 显式调用首页 4 个预设、7 个节点动作、5 个修饰器、9 个模型路由（含 --ratio --resolution --duration 参数）
- 体验增强：libtv.py 统一入口、--dry-run 预览、结构化 APIError JSON

详见：
- https://github.com/Qiuxiangxiang/libtv-skill-pro/blob/main/CHANGELOG.md
- https://github.com/Qiuxiangxiang/libtv-skill-pro/blob/main/INTEGRATIONS.md

三个问题想问你：

1. 你 OK 这个 fork 吗？想加更强署名 / 调整定位都可以告诉我。

2. 要不要把新脚本合并回你的原版？我可以发 clean PR。Pro 版继续作为「实验场」独立维护。

3. 命名协调？当前生态：
   - 你的：libtv-skill（单数）
   - 我的：libtv-skill-pro（单数）
   - 另有 316530790 的 libtv-skills（复数，疑似无意 fork），跟我无关
   希望避免用户混淆。

顺便自我介绍：我目前也在探索 AI 时代下硬件侧方案整合、算法后训练、以及智能体 / Skill 层级建设这几个方向，在 ToB 行业有一些落地经验。如果你或 Lovart AI 有合作交集，欢迎进一步交流。

最后说一下设计宗旨——我做 Pro 版的初心是创作平权（democratize creation）：让 AI 创作不再是 prompt 工程师的特权。任何用户哪怕只会说一句话，后端 Agent 也应该能替他把活干漂亮。

你写的「用户侧不做创作，只做传话」正是这一愿景的工程化基石——把「创作智慧」从用户身上转移到后端 Agent，用户只需表达意图。Pro 版扩展的 dry-run / 结构化错误 / 模型路由，本质上都只是让「传话」这一步更稳、更可控。同一个方向，多一层护栏。

祝好
Qiuxiangxiang
https://github.com/Qiuxiangxiang
BODYEOF
fi

# 1. 邮件正文 → 剪贴板
pbcopy < "$BODY_FILE"
echo "✓ 邮件正文已复制到剪贴板（$(wc -c < "$BODY_FILE" | tr -d ' ') 字节）"

# 2. 打开 Gmail compose（subject 已 URL 编码）
SUBJECT="关于 fork 你的 libtv-skill 为 libtv-skill-pro 的通知"
ENCODED_SUBJECT=$(python3 -c "import urllib.parse, sys; print(urllib.parse.quote(sys.argv[1]))" "$SUBJECT")
GMAIL_URL="https://mail.google.com/mail/?view=cm&fs=1&to=haofanwang.ai@gmail.com&su=${ENCODED_SUBJECT}"

echo ""
echo "✓ 即将打开 Gmail 撰写界面..."
sleep 1
open "$GMAIL_URL"

echo ""
echo "════════════════════════════════════"
echo "现在在浏览器里："
echo "  1. 检查 To 是 haofanwang.ai@gmail.com"
echo "  2. 检查 Subject 已自动填好"
echo "  3. 点击 body 区域，Cmd+V 粘贴正文"
echo "  4. 检查链接是否能点（CHANGELOG / INTEGRATIONS）"
echo "  5. Send"
echo ""
echo "如果你想用别的邮箱客户端发，正文文件在："
echo "  $BODY_FILE"
