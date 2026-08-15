# 给 Frank (Haofan) Wang 的 fork 通知邮件草稿

> 这是**未发出**的邮件草稿。你审阅后可以：
> - 复制到 Gmail/邮件客户端发出，或
> - 让 `mail` CLI 发，或
> - 让我用 `gh` 在他活跃 repo 留 issue（不推荐——污染他的公共 repo）

## 联系对象档案（已查证）

| 字段 | 内容 |
|---|---|
| Real name | Frank (Haofan) Wang |
| GitHub | [@haofanwang](https://github.com/haofanwang) (login 跟 ClawHub handle 一致) |
| Company | Lovart AI |
| Email（公开）| `haofanwang.ai@gmail.com` |
| Twitter | [@Haofan_Wang](https://twitter.com/Haofan_Wang) |
| Blog | https://haofanwang.github.io |
| 知名 repos | inswapper (★736), Lora-for-Diffusers (★822), Score-CAM (★438) |
| ClawHub repo | **不存在 GitHub 镜像** —— libtv-skill 是 ClawHub-only 分发 |

**结论**：他是知名 AI 研究员（SIGGRAPH/CVPR reviewer），通过 ClawHub 而不是 GitHub 维护 libtv-skill。最礼貌的通知渠道是 **email**。

---

## 邮件草稿

**To**: `haofanwang.ai@gmail.com`
**Cc**: （可空）
**Subject**: `Heads up: I forked your @haofanwang/libtv-skill as libtv-skill-pro on ClawHub`

---

Hi Frank,

I'm Qiuxiangxiang on ClawHub. I've published a fork of your excellent `libtv-skill` as [`libtv-skill-pro`](https://clawhub.ai/qiuxiangxiang/libtv-skill-pro), with GitHub mirror at https://github.com/Qiuxiangxiang/libtv-skill-pro. Wanted to give you a heads-up rather than have you discover it from a stranger.

**What I kept from your work** (byte-for-byte identical, properly credited):
- `download_results.py`, `query_session.py`, `upload_file.py`
- `_common.py` API client structure
- SKILL.md description as starting point

**What I added** (~17 scripts total):
- Advanced workflow layer: batch / monitor / poll / templates / export / history / project
- LibTV function-matrix layer: `flow / node / edit / model` — 4 canvas presets, 7 node actions, 5 modifiers, 9-model routing with explicit `--ratio --resolution --duration` params
- DX: unified `libtv.py` entrypoint, `--dry-run` preview, structured `APIError` JSON

Full design notes in [CHANGELOG.md](https://github.com/Qiuxiangxiang/libtv-skill-pro/blob/main/CHANGELOG.md) and [INTEGRATIONS.md](https://github.com/Qiuxiangxiang/libtv-skill-pro/blob/main/INTEGRATIONS.md).

I have three questions for you:

1. **Are you OK with this fork?** Happy to add stronger attribution or adjust framing if anything bothers you.

2. **Want any of the advanced layers merged back upstream?** If batch / monitor / workflow_template / model-router scripts would be useful in your own repo, I can split out clean PRs. Pro stays as a "superset" experimentation space.

3. **Coordinate on naming?** Current state in the ecosystem:
   - You: `libtv-skill` (singular)
   - Me: `libtv-skill-pro` (singular)
   - There's also `libtv-skills` (plural) by user `316530790` that looks like an unintentional duplicate fork. I have no relationship with that one.

   Happy to do whatever helps avoid user confusion.

A bit about me — I'm exploring integration of hardware-side stacks, post-training pipelines, and agent / skill layer architecture in the AI era, with some ToB enterprise experience. If there's ever a collaboration angle that makes sense (with you personally or at Lovart AI), I'd be glad to chat further.

One last note on design philosophy — my motivation for building Pro is **democratizing creation (创作平权)**: AI-assisted content generation shouldn't remain a privilege of prompt engineers. Anyone with a single-sentence intent should be able to let the backend Agent do the heavy lifting properly.

Your "用户侧不做创作，只做传话" principle is exactly the engineering foundation of that vision — moving creative judgment from the user side to the backend Agent so the user only expresses intent. Pro's additions (dry-run preview, structured errors, model routing) are all just ways to make that "传话" step more reliable and controllable. Same direction, more guardrails.

Best,
Qiuxiangxiang
https://github.com/Qiuxiangxiang

---

## 中文版（可附在英文邮件后或单独发）

```
Frank 你好，

我是 ClawHub 上的 Qiuxiangxiang。基于你的 libtv-skill fork 了一个 Pro 版
（ClawHub slug: libtv-skill-pro，GitHub: github.com/Qiuxiangxiang/libtv-skill-pro），
想提前告诉你一下，而不是让你从别处发现。

保留你的工作（byte 级一致，已署名）：
- download_results / query_session / upload_file 3 个脚本
- _common.py API client 结构
- SKILL.md 描述基础

新增：
- 7 个高级工作流脚本（batch / monitor / poll / templates / export / history / project）
- 4 个 LibTV 功能矩阵脚本（flow / node / edit / model）—— 显式调用首页 4 个预设、
  7 个节点动作、5 个修饰器、9 个模型路由（含 --ratio --resolution --duration 参数）
- 体验增强：libtv.py 统一入口、--dry-run 预览、结构化 APIError JSON

详见：CHANGELOG.md / INTEGRATIONS.md

3 个问题：

1. 你 OK 这个 fork 吗？想加更强署名 / 调整定位都可以。

2. 要不要把新脚本合并回你的原版？我可以发 clean PR。Pro 版继续作为"实验场"独立维护。

3. 命名协调？
   - 你的：libtv-skill（单数）
   - 我的：libtv-skill-pro（单数）
   - 另有 316530790 的 libtv-skills（复数，疑似无意 fork）
   希望避免用户混淆。

顺便自我介绍：我目前也在探索 AI 时代下硬件侧方案整合、算法后训练、
以及智能体 / Skill 层级建设这几个方向，在 ToB 行业有一些落地经验。
如果你或 Lovart AI 有合作交集，欢迎进一步交流。

最后说一下设计宗旨——我做 Pro 版的初心是**创作平权（democratize creation）**：
让 AI 创作不再是 prompt 工程师的特权。任何用户哪怕只会说一句话，
后端 Agent 也应该能替他把活干漂亮。

你写的"用户侧不做创作，只做传话"正是这一愿景的工程化基石——
把"创作智慧"从用户身上转移到后端 Agent，用户只需表达意图。
Pro 版扩展的 dry-run / 结构化错误 / 模型路由，本质上都只是让"传话"
这一步更稳、更可控。同一个方向，多一层护栏。

祝好
Qiuxiangxiang
```

---

## 发送命令（macOS）

```bash
# 方式 1：从默认邮件 client 打开新邮件（macOS Mail）
open "mailto:haofanwang.ai@gmail.com?subject=Heads%20up%3A%20I%20forked%20your%20%40haofanwang%2Flibtv-skill%20as%20libtv-skill-pro%20on%20ClawHub"

# 方式 2：直接 gmail web compose
open "https://mail.google.com/mail/?view=cm&to=haofanwang.ai@gmail.com&su=Heads%20up%3A%20libtv-skill-pro%20fork"
```

---

## 心态准备

- 知名研究员收 fork 通知是常事，他大概率会礼貌回复
- 他可能不回（80% 开源作者收邮件不回是常态）
- 极小概率会有冲突，但**先通知再说**比"被发现"主动得多
- 即便他完全不回，**你也已经尽到了 fork-of 礼仪**，将来任何人质疑都能拿出这封邮件
