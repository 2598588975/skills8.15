# Fight line storyboard layout standard

Use this reference whenever the requested output is a dense fight-storyboard sheet matching the bundled visual standard.

## 1. Canvas and hierarchy

- Canvas: 16:9 landscape, high resolution, white or warm-white storyboard paper.
- Main board: three equal rows × five equal columns = 15 panels.
- Bottom analysis band: approximately 22–28% of canvas height, split into three modules.
- Outer border and panel borders: clean black line, consistent weight.
- Reading order: left to right, top to bottom.
- Every panel header: black number box at upper left plus timecode.
- Every panel footer: maximum two compact Chinese lines.

## 2. Line-art language

- Black and gray pencil/ink storyboard rendering with visible construction strokes.
- Light gray wash for depth and separation; preserve white space.
- Cyan-blue only for body paths, weapon arcs, camera paths, or energy direction.
- Red only for decisive impact/force points.
- Bodies and contact geometry remain clearer than particles, speed lines, debris, or VFX.
- Keep character designs simplified but consistently recognizable.

## 3. Panel footer schema

Use:

```text
[visible action and outcome; include A/B positions if needed]
镜头：[景别/角度]（[固定/推/拉/摇/移/跟/环绕/变速]）
```

Examples:

```text
A前压直拳，B侧身格挡，拳路被引向画外。
镜头：近景侧拍（轻跟）
```

```text
B借格挡完成转髋反击，A后脚失衡退半步。
镜头：中近景（横移）
```

## 4. Bottom analysis band

### A. 角色走位示意（俯视简图）

Show five chronological windows. Use stable A/B markers, start dots, a thin A–B axis, and camera position. Mark:

- direct movement: solid arrow;
- circular/evading movement: cyan curved arrow;
- camera move: dashed arrow;
- axis: thin gray line.

### B. 动作衔接分析

Draw 6–10 simplified body diagrams representing the decisive causal chain. Annotate:

- attack setup;
- attack path;
- defense/contact;
- footwork and weight transfer;
- counter or reversal;
- recoil and recovery.

Legend:

- force point: red dot;
- defense direction: blue arrow;
- stepping path: dashed line;
- force path: curved wave/arc.

### C. 视觉节奏与运镜分析

Align all rows to the same time ruler:

- rhythm waveform: quiet → build → burst → pause → peak → release;
- camera activity: fixed, push, follow, lateral move, orbit, high-speed move, slow motion;
- shot scale: wide, full, medium, close, insert, overhead;
- event/VFX markers: launch, evade, contact, block, break, energy peak, freeze, recovery.

## 5. Timing density

- 10 seconds: normally 10 panels; use 12 only for a very dense exchange.
- 15 seconds: default 15 panels, one second each.
- 20–30 seconds: split into multiple 10–15 second boards unless the user explicitly wants one oversized sheet.
- A panel is an action state, not necessarily a new attack. Use anticipation, reaction, and recovery panels to maintain causality.

## 6. Image-generation prompt skeleton

```text
Create a professional 16:9 fight line-art storyboard production sheet. Use the supplied layout reference only for the 3×5 grid, panel headers, compact footers, line-art notation, and three-module analysis band. Do not copy its characters, setting, poses, costumes, text, or choreography.

Visual form: white storyboard paper, black/gray pencil and ink lines, restrained gray wash, crisp readable silhouettes, cyan-blue motion arrows, tiny red impact accents, no photorealism, no finished comic coloring, no poster layout.

Continuity anchors:
A: [identity, costume, body type, dominant side, weapon/power]
B: [identity, costume, body type, dominant side, weapon/power]
Space: [location, obstacle map, start positions, A–B axis, camera side]

Produce exactly 15 panels in three rows of five. Number 1–15. Put continuous timecodes from 00:00–00:01 through 00:14–00:15. Each panel must show one readable action state and a short two-line Chinese footer: action/result, then 镜头：景别（运镜）.

Panel plan:
01 [shot, blocking, preparation, camera]
02 [shot, attack initiation, camera]
03 [shot, defense or evade, camera]
04 [shot, changed distance, camera]
05 [shot, contact/miss and recovery, camera]
06 [...]
...
15 [decisive result and continuation pose]

Bottom band:
left — five-stage overhead A/B blocking diagrams with axis and camera side;
middle — simplified attack/defense/action-link diagrams with red force points, blue defense arrows, dashed stepping paths, and curved force paths;
right — aligned 0–15s rhythm waveform, camera activity, shot scale, and event/VFX markers.

Maintain identity, costume, handedness, weapon ownership, screen direction, damage state, and spatial continuity. Show cause → reaction → result. Keep hands, feet, joints, contact points, and weapon paths anatomically readable. Do not use speech bubbles, subtitles, watermarks, duplicated limbs, fused bodies, random teleporting, unexplained axis reversal, or effects that obscure action.
```

## 7. AI-video handoff line

Append this instruction when using a board as an image-to-video reference:

```text
参考图只用于构图、人物站位、动作路径、视线与运镜；不得继承线稿风格、纸张底色、分格边框、编号、箭头、分析图、文字或水印。人物身份、服装、武器归属和动作起止姿态必须连续。
```
