# Prompt Contracts

Use this reference when delivering copy-ready image or video prompts from a visual bible.

## Global Prompt Contract

A global prompt block should be reusable. It must lock style but avoid locking scene-specific action.

Include:

1. project type and visual thesis
2. capture profile
3. color system with physical sources
4. light system with source/direction/temperature
5. lens and camera behavior
6. material and skin response
7. continuity locks
8. negative constraints

Avoid:

- scene-specific gestures that would pollute every shot
- too many adjectives
- named directors, exact film titles, or copied IP style
- contradictory lighting
- incompatible camera moves

## Image Prompt Contract

Image prompts describe one frozen moment.

Order:

```text
[project style/capture profile], [scene/location/time], [main subject and stable identity], [current costume/state], [one visible action or pose frozen at a specific point], [camera position/lens/composition], [background geography and continuity anchors], [light source/direction/material response], [color system], [do-not-change + negative constraints].
```

Rules:

- Do not describe before/after timing in still prompts.
- Do not ask for text unless the user explicitly needs text in the image.
- Use one main composition decision.
- Keep reference-image role boundaries clear.

## Video Prompt Contract

Video prompts describe a change over time.

Order:

```text
[project style/capture profile], [scene/location/time], [starting state], [main subject identity and current state], [action trigger -> physical path -> visible result], [camera movement triggered by action], [background continuity anchors], [light behavior and material response], [audio if needed], [final frame state], [negative constraints].
```

Rules:

- Write start, process, and end state.
- Each clip gets one main action and one main camera behavior.
- Add motion only where time allows.
- Preserve axis, eyeline, and screen direction for dialogue or reverse shots.
- If using reference images, state exactly what each reference controls.

## Reference Role Map

Use this table when the user provides multiple references.

```markdown
| ref | role | must inherit | must not inherit |
|---|---|---|---|
| Image 1 | character identity | face, hair, body baseline | background, pose, lighting unless specified |
| Image 2 | environment | geography, light source, material | people, text, random objects |
| Image 3 | costume | silhouette, fabric, color | face, pose, background |
| Image 4 | storyboard | blocking, camera, action path | borders, arrows, captions, line-art style |
```

## Continuity Locks

Use concise locks. Do not write the entire bible into every shot.

Good locks:

- "Keep the same left-side window as the only cool key source."
- "Keep her black bob haircut with blue front streak and green eyes; do not change face structure."
- "The corridor remains wet, narrow, and copper-green, with red vertical light only on frame right."
- "Reverse shot keeps the window between the two characters and preserves screen direction."

Weak locks:

- "keep cinematic style"
- "same atmosphere"
- "high quality"
- "make it beautiful"

## Negative Constraints

Use 3-6 constraints aimed at likely failure modes.

Common options:

- no extra characters
- no duplicate faces
- no changing costume
- no changing room layout
- no unrelated text, logo, subtitle, watermark
- no glossy AI skin
- no random neon color shift
- no impossible rim light
- no game key art
- no poster composition unless poster is requested

Do not overuse negative prompts. A long negative list can introduce the very objects it tries to avoid.

## Final Prompt Check

Before returning a prompt:

- Can this prompt be used without reading the analysis?
- Is the style physical, not decorative?
- Does it preserve global consistency but still describe this scene's unique job?
- Is identity separated from current state?
- Are light direction and color source clear?
- Is camera behavior compatible with the shot duration?
- Are negative constraints minimal and relevant?
