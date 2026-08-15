---
name: storyboard-image-sheet
description: Create or refine non-combat line-art storyboard sheets from scene scripts, character identity boards, shot notes, or Chinese prompts. Use when the user asks for 线稿故事板、普通分镜图、对白分镜、悬疑/校园/生活场景分镜、AI视频故事板、手绘线稿分镜, one storyboard image, panel-by-panel visual planning, captions under each frame, or a prompt that clearly shows character positions, shot size, actions, camera movement, arrows, continuity, and visual focus without making a polished poster. Do not use for fight choreography, martial-arts boards, attack-defense blocking, or combat rhythm analysis; route those requests to fight-line-storyboard.
---

# Storyboard Image Sheet

## Core Use

Turn a non-combat scene script and one or more character identity boards into a single storyboard sheet for AI video planning. Prefer a clean hand-drawn line-art storyboard, not a finished poster, key visual, cinematic still, or polished comic page.

If the user asks for an actual image, build a complete image-generation prompt and use the available image generation tool. If the storyboard is meant to support AI video generation, also provide a detailed shot-note table outside the image. If the user only asks for a prompt, return the image prompt, the panel caption list, and the video shot-note table.

## Scope Boundary

- Use this skill for dialogue, suspense, campus life, romance, family, workplace, comedy, investigation, atmosphere, reaction, reveal, and ordinary movement.
- If the scene's main design problem is attack/defense, martial arts, weapon exchange, chase combat, impact rhythm, or force/footwork analysis, use `fight-line-storyboard` instead.
- Never add the fight skill's 15-panel tactical layout, attack-defense diagrams, force points, or combat rhythm band to an ordinary line-art storyboard unless the user explicitly requests a hybrid.
- Keep both skills independent; do not modify or inherit rules from `fight-line-storyboard` during ordinary storyboard work.

## Workflow

1. Extract the input:
   - Character A/B identity: age, gender presentation, role, costume, hairstyle, key props, facial features, posture, and relationship.
   - Scene goal: what changes from start to end, who leads the action, who reacts, and the emotional turn.
   - Location and time: interior/exterior, weather, light source, key background elements, moving environment elements.
   - Delivery target: duration, aspect ratio, whether the board is for director review or clean AI-video reference, and whether exact timecodes are required.

2. Choose panel count:
   - Use 4 panels in a 2×2 grid for a short beat or four key moments.
   - Default to 6 panels in a 2×3 grid for a normal 5–10 second scene, dialogue exchange, or reveal.
   - Use 9 panels in a 3×3 grid for a dense 10–15 second non-combat scene or montage.
   - Use 12 panels in a 3×4 grid or 16 panels in a 4×4 grid only for a contact-sheet overview or when the user explicitly asks for high density.
   - Split material longer than 15 seconds into multiple boards. Carry the last pose, prop state, screen direction, and scene state into the next board.

3. Lock visual DNA and geography before writing panels:
   - Lock character identity anchors, costume, body proportions, key prop ownership, scene architecture, time of day, line weight, gray-wash level, and accent-color policy.
   - Establish the A–B axis, camera side, screen direction, entrances/exits, foreground/background order, and important prop locations.
   - Use a neutral frontal/overhead shot or a visible continuous camera move when an intentional axis change is required.

4. Write a compact shot card for every panel:
   - Include shot number/timecode, narrative purpose, shot size/angle, start state, one visible action or reaction, end state, next-shot connection, camera movement, and prohibited continuity changes.
   - Make adjacent timecodes continuous with no gaps or overlaps.
   - Make each panel add information, establish space, advance an action, show a reaction, or create an edit point.
   - Match action across cuts, preserve eyelines, and preserve left-to-right/right-to-left screen direction unless a turn is visibly shown.

5. Structure each panel:
   - Show character positions clearly: left/right, foreground/background, distance, orientation, eyeline.
   - Specify shot size: 远景, 全景, 中景, 近景, 特写, 过肩, 俯拍, 仰拍.
   - Specify action: body movement, hand action, expression, object interaction.
   - Specify camera movement: 推, 拉, 摇, 移, 跟拍, 环绕, 固定镜头, 手持轻晃.
   - Add arrows for motion: solid arrows for character movement, dashed arrows for camera movement, small repeated arrows for environment movement.
   - Mark the visual focus: use simple circles, frame boxes, or focus marks around faces, hands, props, or impact points.

6. Require captions:
   - Add a short Chinese caption below every panel.
   - Format each caption as: `景别｜人物动作｜镜头运动`.
   - Keep captions concise so they fit inside the panel footer.
   - Also provide the caption list outside the image prompt when text legibility matters.
   - Do not place dialogue balloons, speech bubbles, subtitles, or floating text inside the image area when the storyboard may be used as an AI video reference. Put dialogue in the external shot notes instead.
   - Keep the image footer short; put richer text in the external shot notes, not inside the generated image.

7. Reduce anatomy risk:
   - For hand or ring close-ups, prefer clear simplified storyboard hands over detailed photorealistic fingers.
   - Avoid multiple overlapping hands, tangled fingers, hidden thumbs, or extreme cropped hand piles.
   - Show one controlling hand and one wrist/hand in a readable side view when depicting force.
   - Keep the ring separated from the fingers enough to remain readable; circle it as a prop focus if needed.

Read [references/continuity-and-qa.md](references/continuity-and-qa.md) before generating a multi-panel board or repairing continuity problems.

## Image Prompt Template

Use this template and replace bracketed fields:

```text
根据以下剧情脚本和人物身份板，生成一张 AI 视频故事板分镜图。画面是一张完整的 storyboard sheet，白纸背景，黑色和灰色铅笔手绘线稿，清晰分格，不是精修海报，不是电影剧照，不是漫画成稿。

画幅：[横版16:9 / A3分镜纸 / 竖版按用户要求]，布局：[默认2行3列，共6格；或4格/9格/12格/16格]。每一格都有清楚边框、分镜编号、可选时间码、简短中文说明栏。每格下方中文说明格式为“景别｜人物动作｜镜头运动”。

分镜性质：普通非打斗线稿故事板，不使用打斗故事板的15格战术板、攻防走位图、受力分析或战斗节奏底栏。

全局视觉DNA：[线稿介质、线条粗细、灰阶方式、允许的强调色、固定光线方向、人物与场景一致性规则]
空间连续性：[A-B轴线、摄影机所在侧、人物屏幕方向、出入口、关键道具初始位置]

人物身份保持一致：
角色A：[身份、外貌、服装、关键道具、性格状态]
角色B：[身份、外貌、服装、关键道具、性格状态]

剧情核心：[一句话概括场景冲突或情绪转折]
场景环境：[地点、时间、光线、天气、关键物件]

每格内容：
1. [编号与时间码] [景别/角度]：起始状态[具体状态]；角色位置[左/右/前/后]；角色完成[一个具体动作或反应]；结束状态[可衔接下一格的姿态/道具/视线]；镜头[运动方式]；画面重点[脸/手/道具/空间关系]；用箭头标注[人物/镜头/环境运动]。说明：[景别｜人物动作｜镜头运动]
2. [景别]：...
3. [景别]：...
4. [景别]：...
5. [景别]：...
6. [景别]：...

视觉要求：专业导演分镜草图，线条干净，人物比例简化但可辨认，空间透视清楚，动作姿态明确，镜头运动箭头清楚，环境运动箭头清楚，重要道具用圈线标注。画面重点是调度、动作和镜头，不追求精修质感。

避免：精修海报、厚涂插画、彩色商业KV、复杂背景压过人物、无分格、无说明栏、人物身份混乱、服装或道具状态重置、无因越轴、左右方向反转、时间码断裂、动作无法衔接、文字过长、中文乱码、镜头运动缺失、箭头缺失、每格构图重复、画面内对话框、气泡对白、字幕漂浮在分镜画面里、异常手、额外手指、手指粘连、手部交叠过多、打斗战术分析底栏。
```

## Panel Writing Rules

Before generating the final prompt, create a compact panel plan:

```text
1. 全景｜A从门口进入，B在桌旁回头｜镜头缓慢推入
2. 过肩中景｜A看向B手中的道具，B微微后退｜镜头向右横移
3. 特写｜B握紧道具，手指发抖｜固定镜头
4. 双人中景｜A伸手制止，B躲开｜手持跟拍
5. 近景｜两人对视，情绪僵住｜镜头轻推
6. 远景｜B转身离开，A停在原地｜镜头缓慢拉远
```

Use concrete visual verbs. Avoid vague words like “电影感很强” unless tied to a visible action, shot, or lighting choice.

## Video-Reference Cleanups

If a generated storyboard will be fed into an AI video model, make the image itself clean:

- Keep dialogue, voiceover, sound design, and exact lines outside the image as separate shot notes.
- Remove speech bubbles, dialogue boxes, floating subtitles, and long text inside panels.
- Keep only panel numbers, arrows, simple focus circles, and optional footer captions.
- For difficult anatomy beats such as grabbing a wrist or putting on a ring, use a medium close-up or prop insert with simplified hands instead of a dense interlocked-finger macro.

For live-action video references:

- Treat hand-drawn storyboard sheets as blocking/camera references, not style references.
- Treat photoreal reference boards as look-development documents for humans; avoid feeding dense collage boards directly to video models.
- Prefer separate clean inputs: one high-resolution character identity image, one environment/style reference, one clean storyboard panel, and one detailed text prompt per shot.
- If only one image reference is allowed, use a clean single-shot keyframe or a clean storyboard panel; avoid all-in-one boards with maps, icons, labels, palettes, tiny photos, and UI lines.
- Add this instruction to video prompts: `参考图只用于构图、人物站位和运镜，不继承分镜线稿、箭头、边框、文字、拼贴版式或低清噪点。`

## Continuity and Visual QA

Before generation, verify that every shot card has one purpose, one visible action/reaction, a start state, an end state, and a next-shot connection. After generation, inspect the entire sheet rather than judging attractive panels in isolation.

Block acceptance when the result has a missing/extra panel, wrong order, identity drift, costume/prop reset, broken geography, unexplained axis crossing, reversed screen direction, inconsistent line style, repeated composition without purpose, unreadable action, or analysis graphics from the fight-board format. Repair the smallest failing scope; regenerate the whole board only when the shared visual DNA or geography is wrong across multiple panels.

## External Video Shot Notes

For AI video generation, output a separate detailed note for each panel after the image or prompt. Use this structure:

```text
05｜15-19s
画面：断崖礼台中全景，诺亚从左后方把莉娅推到仪式中央，宾客半圆围住她，长桌和银烛形成压迫中心。
人物：莉娅踉跄、抗拒、低头稳住身体；诺亚靠近她肩后，动作克制但强硬；宾客静默注视。
运镜：镜头从左向右轻摇，同时缓慢拉远，露出宾客包围和悬崖边缘。
动态：海风吹动长裙、斗篷和烛火，远处海浪闪光。
声音/对白：诺亚低声“微笑。今晚之后，我家的债就清了。”对白只写在这里，不进入画面。
负面：不要气泡对白，不要画内字幕，不要现代婚礼，不要过度精修。
```

Keep these notes concrete enough to become video prompts. Include:

- Timecode and shot number
- Scene/framing
- Character blocking and action
- Camera movement
- Environmental motion
- Sound/dialogue/voiceover
- Continuity constraints and negative prompts
- Start state, end state, and next-shot connection
- Stable screen direction, eyeline, prop state, and any prohibited change

## Output Shape

When answering the user, keep the response practical:

1. Provide the finished image-generation prompt.
2. Provide the panel caption list.
3. Provide a compact continuity note: axis/camera side, screen direction, prop state, and the last pose/state used by the next board.
4. Provide external detailed video shot notes when the storyboard is intended for AI video generation.
5. If an image was generated, show the image and mention that image text should stay short; use the external shot notes for exact dialogue and detailed video prompting.
