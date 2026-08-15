---
name: series-visual-bible-prompt
description: Create reusable visual style bible prompts for short dramas, commercials, music videos, trailers, AI video projects, and image-to-video pipelines. Use when the user asks for 整体风格描述提示词, 短剧视觉规范, 广告片风格, 剧集风格 Bible, 场景统一规范, 人物画面一致性, 色彩风格, 镜头风格, 光线风格, 材质质感, prompt bible, style bible, visual bible, or scene-by-scene style locks for image/video generation.
---

# Series Visual Bible Prompt

## Purpose

Build a reusable visual bible before writing individual image or video prompts. The output should make a short drama, commercial, trailer, or AI-video sequence look authored by one visual system across scenes, characters, props, lighting, color, camera language, and material response.

Do not treat this as a one-off image prompt or poster prompt. The skill's job is to define the project's stable visual contract, then derive scene-level prompt blocks from it.

## Resource Routing

- Read `references/style-bible-schema.md` when the user needs a full style bible, a structured output, or scene-by-scene cards.
- Read `references/prompt-contracts.md` when the user needs image prompts, video prompts, reference-image role maps, continuity locks, or negative constraints.

Use existing specialist skills after the bible is formed when useful:

- Use `cinema-dna-21x9x3` thinking for cinematic composition pressure, color proposition, and anti-CG discipline.
- Use `direct-ai-video` or `seedance-storyboard` after this skill when converting the bible into timed video shots.
- Use `image-prompt-director` after this skill when converting one scene card into a polished single-image prompt.

## Output Modes

Choose the smallest mode that satisfies the request.

### Fast Style Lock

Use when the user only asks for an overall style description, a short style prompt, or a quick visual direction.

Return:

1. One-sentence visual positioning.
2. Global style paragraph.
3. Color system.
4. Light system.
5. Camera and lens language.
6. Material and texture language.
7. Character consistency locks.
8. Negative constraints.
9. Copy-ready global prompt block.

### Production Visual Bible

Use when the user has a short drama, ad film, trailer, script, scene list, storyboard, or recurring characters.

Return:

1. Project visual thesis.
2. Genre and capture profile.
3. Global color system.
4. Global lighting system.
5. Lens and camera behavior.
6. Composition pressure.
7. Character visual bible.
8. Environment visual bible.
9. Costume, props, and material response.
10. Scene-by-scene style cards.
11. Image prompt contract.
12. Video prompt contract.
13. Continuity and negative constraints.
14. Final consistency checklist.

### Scene Style Cards

Use when the user already has characters and scene images, and needs each scene or shot to stay consistent.

For each scene, define:

- `scene_id`
- location and time
- story function
- visible subject priority
- color source and accent color
- key light source, direction, temperature, and shadow behavior
- lens, camera height, shot distance, and movement discipline
- background geography and continuity anchors
- character state, costume, and micro-performance constraints
- still-image prompt
- video prompt
- do-not-change list

### Commercial / Ad Film Variant

Use when the project is an advertisement, brand film, product spot, or campaign.

Keep the visual bible story-led but prioritize:

- product hierarchy
- brand color restraint
- hero material response
- packshot or logo-safe space
- practical light that reveals the product
- hand/product interaction physics
- one conversion emotion
- clear end-frame design notes

## Core Rules

### Style Must Be Physical

Translate style words into visible causes:

- Color comes from wardrobe, wall, sky, practical lamps, screens, rain, dust, product material, or signage.
- Light comes from a named source with direction, color temperature, hardness, and shadow behavior.
- Texture comes from material response: skin, cloth, metal, glass, wet floor, paper, plastic, stone, screen glare.
- Camera language comes from position, lens, distance, height, axis, and movement trigger.

Avoid empty phrases such as `高级感`, `氛围感`, `电影感`, `大片感`, `梦幻`, `好看`, `精致`, `震撼`, unless each is translated into physical visual facts.

### One Project, One Visual Spine

Every scene may vary, but the project must keep one spine:

- one capture profile
- one dominant color logic
- one lens family
- one exposure philosophy
- one skin/material response
- one rule for highlights and shadows
- one rule for how backgrounds are allowed to blur or reveal information

Do not let each scene invent a different art direction.

### Separate Stable Identity From Temporary State

For characters, split:

- stable identity: face structure, hair, body baseline, age range, core costume silhouette, recurring accessories
- current styling: makeup, wetness, dirt, damage, fatigue, jacket on/off
- performance state: posture, gaze target, breath, micro-expression, current emotional pressure

Never let a temporary expression or outfit overwrite the character's stable identity.

### Scene Continuity Comes Before Decorative Style

For every recurring location, lock:

- main axis and entrances/exits
- dominant background shapes
- windows, lamps, signs, furniture, props, and practical light positions
- wet/dry state, damage state, time of day, and crowd density
- whether the camera sees toward or away from the main light

If a reverse shot is needed, describe how the background changes logically from the same geography.

### Camera Must Have a Reason

Define why the camera is there:

- observing through a barrier
- following a movement path
- trapped in a narrow space
- waiting on an object or empty chair
- revealing a power imbalance
- staying close to a hand, face, or product because the action depends on it

Each scene gets one main camera behavior. Avoid stacking push-in, orbit, handheld shake, rack focus, drone move, and slow motion in the same prompt.

### Light Must Be Motivated

For each scene, specify:

- source: window, streetlight, practical lamp, monitor, neon sign, helicopter spotlight, fire, overcast sky, softbox-like shop window, product light
- direction: left, right, back, overhead, low front, bounced from wall/floor
- temperature: warm tungsten, cool daylight, green fluorescent, blue screen spill, amber streetlight
- shadow: hard-edged, soft falloff, broken by blinds, reflected on wet floor, low contrast, deep but readable
- change: stable, flickering, moving, dimming, passing across face

Do not add rim light unless there is a real source.

## Prompt Writing Discipline

Write reusable prompt blocks in this order:

1. Project/capture style.
2. Scene and subject priority.
3. Character identity and current state.
4. Action or pose with a visible end state.
5. Camera relationship.
6. Background geography.
7. Light source and material response.
8. Color system.
9. Continuity locks.
10. Minimal negative constraints.

For video prompts, add timing, movement trigger, physical action path, and final state. For image prompts, stop at one frozen moment and do not describe a time process.

## Reference Image Handling

When the user provides images, assign each image one primary role:

- character identity
- current costume
- environment
- color/light reference
- composition reference
- product/prop reference
- storyboard/blocking reference

Do not let one reference image control everything. Do not average multiple faces. If a reference is a storyboard sheet, inherit camera, position, and action only; exclude borders, arrows, captions, grid lines, and low-fidelity drawing style.

## Final Check

Before delivery, verify:

- The style can be reused across multiple scenes, not just one pretty frame.
- Every color has a source.
- Every light has a source and direction.
- The camera position can exist physically.
- Character identity, costume, and performance state are separated.
- Recurring locations have stable geography.
- Scene-level prompts inherit the global bible without repeating it mechanically.
- Negative constraints target only current risks.
- The output includes copy-ready prompt blocks if the user requested prompt text.
