# Weisenandesen Skill

这是一个用于生成复古对称电影感图像提示词的 Codex skill。

## 用途

输入一句简短中文画面描述，例如：

```text
画面：一个沙漠里的加油站，9:16 比例
```

它会扩写成包含构图、完整提示词、色彩方案、人物动作、场景道具、氛围、反向限制和比例的完整中文图像生成提示词。

## 风格重点

- 正面平视、相机水平、地平线水平
- 严格中央对称或清晰左右平衡
- 1960s-1970s 明亮复古胶片色彩
- 手工搭建的电影布景感
- 安静、克制、轻微冷幽默
- 避免斜拍、荷兰角、歪地平线、建筑歪斜、AI 塑料感

## 安装

把整个 `weisenandesen` 文件夹复制到你的 Codex skills 目录：

```bash
~/.codex/skills/weisenandesen
```

然后在 Codex 里这样调用：

```text
[$weisenandesen](~/.codex/skills/weisenandesen/SKILL.md) 画面：一个男人在等公交
```

## 文件说明

- `SKILL.md`：skill 主入口和工作流
- `style_rules.md`：视觉风格规则
- `prompt_formula.md`：提示词结构和输出格式
- `negative_prompts.md`：反向限制
- `checklist.md`：生成前质量检查
- `examples.md`：示例提示词
- `agents/openai.yaml`：agent 配置
