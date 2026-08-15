# Ordinary line-art storyboard continuity and QA

Use this reference for multi-panel non-combat boards. Route fight choreography and tactical combat boards to `fight-line-storyboard`.

## Shot-card contract

Plan every panel with these fields before generating the sheet:

```text
镜号/时间码：
叙事功能：建立空间 / 推进动作 / 反应 / 线索 / 揭示 / 转场
景别与角度：
起始状态：人物位置、朝向、视线、手部、道具、环境状态
可见动作：一个明确动作或反应
结束状态：动作完成后的姿态、视线、道具和空间关系
下一镜连接：动作匹配 / 视线匹配 / 声音桥 / 空间切换 / 情绪匹配
运镜：固定 / 推 / 拉 / 摇 / 移 / 跟拍 / 升降 / 环绕
禁止变化：脸、发型、服装、体型、道具归属、屏幕方向等
```

Keep the image footer shorter than the shot card. Use `景别｜人物动作｜镜头运动` inside the sheet and keep exact dialogue, sound, and continuity notes outside.

## Continuity invariants

Treat these as blockers:

- Stable identity: face, hair, costume, body proportions, age, temperament.
- Stable geography: doors, windows, furniture, foreground/background order, entrances, exits.
- Stable prop state: owner, hand, open/closed, intact/damaged, visible/hidden.
- Stable screen direction: preserve left-to-right or right-to-left movement until the turn is shown.
- Stable eyeline: the look direction and the following object/POV shot must agree.
- Match on action: continue the same movement at the same physical point across a cut.
- 180-degree rule: keep the camera on one side of the A–B axis; justify a change through a neutral frontal/overhead shot or a visible crossing move.
- Continuous timecodes: no gaps, overlaps, duplicated ranges, or backward time.

## Visual DNA lock

Write one shared lock before panel prompts:

- medium: graphite, pencil, charcoal, ink, marker, or mixed line art;
- line weight: clean thin line, rough construction line, or bold brush line;
- shading: none, hatch, gray wash, or restrained value blocks;
- paper: pure white, warm white, or light gray;
- accents: none or one restrained color for arrows/focus only;
- perspective and anatomy simplification level;
- fixed character and scene anchors;
- aspect ratio and grid geometry.

Repeat only the shortest necessary identity/style anchors in every panel prompt. Avoid adjective-heavy repetition.

## Layout routing

| Layout | Use |
|---|---|
| 2×2 / 4 panels | Four key moments, pitch review, simple reveal |
| 2×3 / 6 panels | Default dialogue, suspense, campus, daily-life scene |
| 3×3 / 9 panels | Dense non-combat movement, montage, 10–15 second sequence |
| 3×4 / 12 panels | Director contact-sheet overview |
| 4×4 / 16 panels | High-density overview only when explicitly requested |

Split scenes longer than 15 seconds into multiple sheets. End each sheet with a continuation state and start the next sheet from exactly that state.

## Two delivery modes

**Director-review board**

- Keep panel number, timecode, short footer, arrows, focus marks, and optional short technical notes.
- Put dialogue and full sound notes outside the drawing area.

**Clean AI-video reference board**

- Keep only panel numbers, minimal arrows, and necessary focus marks.
- Remove long captions, speech bubbles, subtitles, dense UI, palettes, maps, and explanatory blocks.
- Tell the video model to use the board only for composition, blocking, action paths, eyelines, and camera movement.

## Visual QA gate

Inspect the full sheet after generation.

1. **Structure** — exact requested panel count, correct grid, sequential numbers and timecodes.
2. **Narrative** — every panel adds information or an edit point; no missing cause/reaction/result.
3. **Identity** — characters remain recognizable; no swapped costume, age, body, or temperament.
4. **Geography** — stable room layout, axis, screen direction, eyelines, entrances, and exits.
5. **Props** — no unexplained appearance, disappearance, ownership change, or reset.
6. **Drawing** — coherent line weight and gray wash; readable silhouettes, hands, and object contact.
7. **Camera** — varied only when motivated; arrows agree with the written movement.
8. **Text** — short readable labels; provide an exact external caption list when generated Chinese is imperfect.
9. **Scope** — no combat tactical band, attack-defense diagram, force-point legend, or fight-rhythm graph.

Repair the smallest failing scope. Regenerate a single panel when only that panel fails. Regenerate the complete board when shared identity, visual DNA, grid geometry, or scene geography drifts across multiple panels.
