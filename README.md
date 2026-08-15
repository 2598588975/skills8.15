# skills8.15

Zz 个人导演、编剧、分镜、视觉资产与 AI 视频生产 Skill 集合。

本版完成了通用工作流收敛：删除重复入口，把仍有价值的方法吸收到核心 Skill，同时原样保留图片、海报、视觉资产和线稿故事板类 Skill。

## 推荐主工作流

1. `zz-screenwriting-master`（Zz超级编剧大师）：唯一通用编剧入口，从灵感、大纲、人物、会诊和台词推进到可执行剧本。
2. `zz-director-master`（Zz超级导演大师）：唯一通用导演入口，负责导演定调、节奏、调度、轴线、分镜、AI 视频执行、声音剪辑交接和成片质检。
3. `seedance-storyboard`：把剧本或导演稿转换成按秒分镜、分场统一规则和可投喂视频提示词。
4. `seedance-20`：Seedance 专项总包；28 个功能模块统一保留在 `seedance-20/skills/`，不再安装顶层重复副本。
5. `emotion-performance-director`：哭戏、泪线、微表情、对白口型等情绪特写专项。

综合 AI 短剧、角色场景资产与九宫格工作流统一使用 `zz-ai-drama`。

动作场面按需调用 `script-to-shot-engine`、`fight-line-storyboard` 或 `epic-action-storyboard`；非打斗线稿故事板使用 `storyboard-image-sheet`。

## 本版整理原则

- 先吸收后停用：原通用导演、直接视频、情绪对白和剪辑代理中的有效规则已并入对应核心 Skill。
- 删除无效重复：Vidu 旧入口、低频旧视频工作流和 28 个顶层 Seedance 重复目录不进入本仓库。
- 图片类不改动：电影视觉、海报、视觉资产、构图、焦段、色卡、图像反推和故事板图片 Skill 均按原目录保留。
- 不包含 Codex 自带的 `.system` Skill，也不包含任何嵌套 Git 仓库元数据。
- 运行身份统一：旧作者昵称、旧调用名和强制署名输出已从当前安装版与上传版移除；Zz 系列统一使用 `$zz-screenwriting-master`、`$zz-director-master` 和 `$zz-ai-drama`。

## 使用

把需要的 Skill 目录复制到 `C:/Users/codex/.codex/skills/`，或使用 Codex 的 Skill 安装功能从本仓库选择对应目录安装。

每个 Skill 的详细触发条件和执行规则以其目录内的 `SKILL.md` 为准。

## 版本

- 整理日期：2026-08-15
- 顶层个人 Skill：42 个
- 仓库：`2598588975/skills8.15`
