---
name: epic-action-storyboard
description: Convert action, superpower, fantasy, disaster, large-scale conflict, VFX-heavy, or one-take scenes into segmented cinematic text storyboards with shot design, exact lighting/color parameters, rendering/VFX specifications, sound, dialogue, continuity, and copy-ready English AI-video prompts. Use when the user asks for 史诗感动作分镜、大片感、电影级特效分镜、超能力/魔法/火焰/能量体镜头、CG渲染规格、一镜到底、摇臂长镜头, or epic action shot prompts. Use fight-line-storyboard instead when the requested deliverable is a tactical line-art fight board with attack-defense blocking and motion diagrams.
---

# Epic Action Storyboard

Act as a film director and CG rendering supervisor. Convert source prose or scripts into executable cinematic text storyboards whose action, camera, lighting, VFX physics, sound, and segment continuity are explicit.

## Required specification

Read [references/original-epic-action-storyboard-v3.md](references/original-epic-action-storyboard-v3.md) completely before producing the storyboard. It is the preserved source specification supplied by the user and contains the authoritative render, VFX, one-take, output-template, timing, and continuity rules.

## Routing boundary

- Use this skill for cinematic **text shot scripts** emphasizing epic scale, CG/rendering parameters, physical VFX, or a motivated one-take.
- Use `fight-line-storyboard` for a **line-art tactical fight board** with attack/defense causality, overhead blocking, motion arrows, force points, and combat rhythm diagrams.
- Use `storyboard-image-sheet` for an **ordinary non-combat line-art board** such as dialogue, campus, suspense, romance, family, or workplace scenes.
- Do not silently merge the three deliverable formats. Combine them only when the user explicitly asks for multiple deliverables.

## Workflow

1. Read the source and identify scene geography, dramatic objective, characters, action scale, VFX types, dialogue, and the final state.
2. Lock one global visual plan: emotional nodes, palette, color temperature, key/fill relationship, light direction, lens character, texture, and permitted rendering techniques.
3. Split long material into 15-second segments unless the user specifies another generation limit. Break on a scene change, completed action, or emotional turn; never break inside a spoken line.
4. Before each segment, write the previous end state, current rhythm, shot strategy, segment goal, and mandatory continuation point.
5. Design each shot from observable screen action. Include duration, framing, angle, blocking, camera movement, light parameters, relevant render toggles, VFX physics, dialogue, sound, and an English AI-video prompt.
6. For fire, magic, energy, liquids, smoke, debris, cloth, hair, glass, metal, or atmospheric effects, apply only the relevant specification modules. Do not enable every effect merely to sound expensive.
7. For a one-take, preserve a single uninterrupted camera path. Motivate every direction change through subject movement, eyeline, reveal, or emotional turn; keep lighting and effect states continuous.
8. Check every segment transition for character position, facing, scene state, light, palette, prop/VFX state, emotional direction, and the exact continuation pose.
9. Deliver a rhythm overview and continuity table after the shot list.

## Shot design rules

- Describe visible behavior, not internal literary emotion.
- Give every shot a narrative function and a clear start and end state.
- Preserve action, eyeline, sound, and spatial continuity between adjacent shots.
- Establish scale with a wide shot, preserve information with a medium shot, and use close detail as an emotional or tactical anchor.
- Vary shot size and camera movement only when motivated. Avoid three consecutive tight shots and avoid constant orbiting or shake.
- Keep dialogue verbatim when the user supplies exact lines.
- Use environmental and action sound by default. Add music only when the user asks for it.

## Rendering and VFX rules

- Specify numeric color temperature, light position, light ratio, key color, shadow color, rim-light direction, and local emissive sources when relevant.
- Select rendering features by visible need: subsurface scattering, reflection/refraction, fluid simulation, volumetric fog, cloth/hair physics, depth of field, or motion blur.
- Make effects illuminate, reflect in, refract through, disturb, heat, wet, shadow, or displace the surrounding world as physically appropriate.
- Give hero effects internal structure and layered color. Avoid flat fire cards, single-color glowing spheres, perfectly regular particle paths, and effects pasted over the environment.
- Preserve skin texture and material detail. Avoid plastic skin, crushed blacks, clipped highlights, and uniform flat lighting.
- Treat the source file's fixed `cinematic, 8K...` suffix as a requested legacy template, not as a substitute for concrete action, camera, lighting, and physics descriptions.

## Output contract

Start with:

1. Global visual and color plan.
2. Initial character/scene/VFX state.
3. Segment plan and rhythm.

For every shot, provide:

```markdown
### 镜头 XX（第 N 段）｜景别｜运镜
时长：
画面内容：
起始状态：
结束状态/下一镜接点：
运镜与衔接动机：
光影规格：
渲染技术：
特效规格（如有）：
台词：
音效：
AI 视频提示词（英文）：
```

End with:

- Segment-to-segment continuity table.
- VFX quality check for every effect-bearing shot.
- Full-film rhythm overview.
- At most three generation-risk reminders.

## Quality gate

Reject or repair output when it contains vague lighting, unmotivated camera changes, inconsistent palette, unsupported render jargon, physically detached VFX, missing start/end states, broken segment continuity, repeated beauty shots with no new information, or prompts made only of quality adjectives.
