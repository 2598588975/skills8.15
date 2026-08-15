---
name: micro-expression-control
description: Control subtle facial expression arcs in AI image/video prompts. Use when the user asks for 微表情控制, 表情细节, 眼神变化, natural acting, non-posed facial performance, faint/subtle/suppressed emotions, or when rewriting video prompts so facial emotion changes over time instead of staying as a fixed happy/sad/shy/angry label.
---

# Micro Expression Control

## Core Pattern

When describing a face, use this structure:

`[人物描述], 脸上带着[微弱程度词]的[具体情绪], 嘴角[肌肉微动], 眼神[眼神状态与方向变化], 面部肌肉放松，没有摆拍感，呼吸感，真实自然。`

Prefer intensity words that keep the acting small:

- 中文: 很淡的, 轻微的, 几乎看不出的, 被压住的, 短暂闪过的, 克制的, 未完全展开的.
- English: faint, subtle, barely visible, suppressed, restrained, a brief flicker of.

## Write Expression As An Arc

For each shot or time range, include:

1. 起始状态: what the face is doing before the emotion changes.
2. 触发原因: what causes the expression to shift, usually dialogue, another person's action, or a body movement.
3. 变化动作: mouth corner, eyelid, brow, jaw, lip, breath, shoulder, head angle, blink, gaze direction.
4. 最终结果: where the expression settles by the end of the beat.

Use body action to create the expression. Do not command a frozen face. Useful physical cues:

- breathing catches, exhales, or becomes steadier;
- shoulders drop, close inward, or open;
- head lowers, turns away, lifts, or tilts;
- eyes avoid, return, soften, close, or become wet;
- lips press, part, tremble slightly, bite, or release;
- jaw tightens then loosens;
- smile begins from one corner before reaching the eyes.

## Avoid

- Only writing big labels such as happy, sad, shy, angry.
- Keeping one expression unchanged from the first second to the last.
- Exaggerated expression, forced smile, stiff face, dead stare, over-posed beauty acting.
- Asking the character to stare at the camera unless the shot requires it.

## Nine-Question Check

After writing a video prompt, check:

1. Did I only write happy, sad, shy, angry instead of specific emotional texture?
2. Did I use faint, subtle, barely visible, suppressed, or similar words to control intensity?
3. Did I avoid a fixed expression from second 1 to second 5?
4. Did I write the starting state, change action, and final result?
5. Did I give the expression a visible or dramatic cause?
6. Did I use body action to bring out the expression instead of directly posing the face?
7. Did I write eye movement changes instead of constant camera staring?
8. Did I include breathing, shoulders, lowering the head, closing eyes, biting lips, or similar physical details when appropriate?
9. Did I avoid exaggerated expression, forced smile, stiff face, and posed acting while keeping the performance natural?

## Output Integration

When combining with shot-by-shot video prompts, add one compact micro-expression clause inside each shot after the main action. Keep it visible and playable: one to three facial/physical changes per beat is usually enough.
