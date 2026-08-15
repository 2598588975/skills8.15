---
name: fight-line-storyboard
description: Convert fight scripts, action beats, martial-arts scenes, superpower battles, chases, or weapon confrontations into professional second-by-second line-art storyboard sheets with attack-defense causality, screen direction, 180-degree axis control, character blocking, motion arrows, impact beats, camera rhythm, and bottom-row tactical analysis. Use when the user asks for 打斗线稿故事板、动作分镜、逐秒打戏、武打预演、攻防走位图、战斗节奏板、fight storyboard、action previs, or wants an image matching a dense 15-panel production-board standard.
---

# Fight Line Storyboard

Turn a fight scene into a readable production board, not a collection of unrelated heroic poses. Make every beat follow from the previous beat and expose enough spatial information for performers, camera planning, and image-to-video generation.

## Required reference

Before composing or rendering a board, read [references/layout-standard.md](references/layout-standard.md). Use [assets/reference-fight-storyboard-standard.png](assets/reference-fight-storyboard-standard.png) as the layout and information-density reference when the image tool accepts local references. Treat it only as a board-format reference; never copy its characters, costumes, setting, poses, or exact choreography.

## Defaults

- Use 16:9 landscape, white paper, monochrome pencil/ink line art.
- Use 15 seconds and 15 numbered panels by default: three rows of five, one second per panel.
- Reserve a full-width bottom band for three analysis modules: blocking, action links, and rhythm/camera timeline.
- Use black/gray for drawing, restrained cyan-blue for motion paths, and restrained red for impact or force points.
- Keep dialogue outside the image. Keep panel text short and production-oriented.
- Use fictional screen choreography. Prefer readable action and consequences over graphic injury detail.

## Workflow

### 1. Normalize the scene

Extract or infer:

- Fighters: stable label, identity, body type, costume silhouette, dominant side, skill level, weapon/power, current injury or fatigue.
- Space: floor plan, obstacles, entrances, height changes, breakable props, hazards, and initial distance.
- Dramatic turn: who appears dominant at the start, what changes, and who controls the final beat.
- Duration and format: default to 15 seconds, 15 panels, 16:9 if absent.
- Physical register: realistic, heightened live action, wuxia, superhero, anime, game cinematic, or abstract energy combat.

Ask only when a missing fact would change the combatants or the ending. Otherwise choose conservative defaults and continue.

### 2. Lock continuity before drawing

Create a compact continuity card for each fighter and prop. Keep face, hair, costume, body proportions, handedness, weapon ownership, damage state, and power color unchanged unless the script explicitly changes them.

Define the initial map:

- A and B positions and facing.
- Connecting action axis.
- Screen direction for each fighter.
- Camera side of the 180-degree line.
- Key obstacles and safe movement lanes.

Do not cross the axis accidentally. Cross only through a neutral frontal/overhead shot or a visibly continuous camera move across the line.

### 3. Build an attack-defense causal chain

Plan the fight as linked beats:

`intent → preparation → attack → perception → defense/evade → counter → contact or miss → recoil/recovery → changed advantage`

For every major action, show cause, reaction, and result. Never repeat an attack merely to fill panels. Preserve momentum, weight transfer, balance, and the last pose of the previous panel.

Use quiet beats deliberately: a stare, breath reset, stance change, distance check, or environmental reaction can separate high-energy bursts.

### 4. Assign panels and timecodes

Start panel 1 at `00:00`. Keep adjacent timecodes continuous with no gaps or overlaps. For the 15-second default, use `00:00–00:01` through `00:14–00:15`.

Give every panel:

1. Panel number and timecode.
2. A distinct, readable action state.
3. Shot size and angle.
4. Fighter positions, facing, eyelines, and contact point.
5. Camera movement or `固定`.
6. A concise two-line footer: action result, then `镜头：景别（运镜）`.

Cut on action where possible. Use inserts only for tactically important feet, hands, weapons, eyes, or impact points. Vary shot scale to improve readability, not for random spectacle.

### 5. Enforce physical readability

- Show preparation, contact/miss, and recovery as different states.
- Keep the planted foot, center of gravity, torso rotation, and force direction believable.
- Make silhouettes readable; avoid overlapping both fighters into one knot.
- Show only limbs required by the action; prevent extra fingers, duplicated arms, fused hands, broken joints, and inconsistent weapons.
- Use a wider shot for complex exchanges and a close shot for one clear detail.
- Keep VFX subordinate to bodies and contact geometry.

### 6. Design the three analysis modules

Place these below the 15 panels:

1. **角色走位示意（俯视简图）** — five time windows, A/B markers, starting position, direct movement, circular movement, axis, and camera side.
2. **动作衔接分析** — simplified stick-figure sequence for the decisive attack/defense chain; mark red force points, blue defense direction, dashed stepping paths, and curved force paths.
3. **视觉节奏与运镜分析** — 0–15 second timeline with rhythm waveform, camera-activity row, shot-scale row, and event/VFX markers.

The analysis band must describe the same choreography as the panels. Do not invent a second version of the fight.

### 7. Compose the image prompt

Use the exact layout grammar and prompt skeleton in [references/layout-standard.md](references/layout-standard.md). If character or environment references are supplied, state their roles explicitly:

- identity reference: face, hair, costume, proportions;
- environment reference: architecture and geography;
- layout reference: grid, notation, information density only.

Explicitly instruct the image model not to inherit photorealism, reference characters, embedded captions, watermarks, or prior choreography from the layout reference.

### 8. Generate and inspect

When the user asks for an actual storyboard image, use the available image-generation tool. Generate one complete board per scene or per 15-second segment. Inspect the result for:

- all panels present and numbered in order;
- continuous timecodes;
- stable character identity and weapon ownership;
- axis and screen direction continuity;
- attack-defense causality;
- legible silhouettes, hands, feet, and contact points;
- agreement between panels and bottom analysis;
- short, readable Chinese captions.

Regenerate or edit when a failure changes choreography or continuity. Minor text imperfections may be corrected by delivering an exact external caption list.

## Camera rules

- Establish geography with an opening wide or overhead shot before tight coverage.
- Maintain the A–B axis and each fighter's screen direction across cuts.
- Use a neutral shot, overhead shot, or continuous arc move to justify an axis change.
- Use low angle for threat or power, high angle for vulnerability or spatial clarification, and close-up only for a single decisive detail.
- Distinguish character motion from camera motion: solid arrow for body/weapon path, dashed arrow for camera path, thin line for eyeline, concentric/impact marks for contact.
- Use slow motion only around anticipation, decisive contact, or aftermath; return to real-time so the rhythm has contrast.
- Avoid constant orbiting, constant shake, and a new camera trick in every panel.

## Output

For an image request, deliver:

1. The completed board image.
2. A short panel list with exact timecodes and action outcomes.
3. A continuity note covering axis, screen direction, character/weapon state, and the final pose used to continue the next segment.
4. If requested for AI video, a separate per-shot prompt set; tell the video model to use the board only for composition, blocking, action paths, and camera movement, not to reproduce line art, arrows, borders, labels, or paper texture.

For a prompt-only request, deliver the complete image prompt plus the panel list and analysis-module data.

## Hard constraints

- Do not make a polished poster, colored comic, contact sheet of still portraits, or random montage.
- Do not omit the bottom analysis band when the user asks for this standard.
- Do not use long prose inside panels, speech bubbles, subtitles, or floating dialogue.
- Do not change identity, costume, weapon, dominant hand, injury, time of day, or environment without cause.
- Do not teleport fighters, reverse left/right, cross the axis without motivation, or reset poses between panels.
- Do not let effects hide the action, impact point, or body mechanics.
- Do not describe a hit without showing its reaction and resulting spatial change.
