---
name: clay-white-model-storyboard
description: Turn scripts, prose, shot lists, or existing storyboards into coherent cinematic storyboards rendered as untextured matte white clay maquettes. Use for requests mentioning clay white-model storyboards, white clay previs, clay animatics, grayscale 3D blocking, "黏土白膜", "黏土白模", "白模故事板", "黏土分镜", or a 9-grid/12-grid storyboard that should preserve character, scene, screen direction, and camera continuity without color or finished materials.
---

# Clay White-Model Storyboard

Create a practical film-previsualization board in a uniform white-clay look. Preserve story clarity and shot continuity first; use the clay material as a neutral visual language, not as cute decoration.

## Required Reference

Read `references/prompt-system.md` before writing prompts or generating frames. It contains the material lock, shot templates, continuity rules, and QA checklist.

## Workflow

1. Parse the source into causal beats. Split when the action, information, emotional state, camera purpose, or location changes. Do not create several shots that communicate the same thing.
2. Establish a continuity bible before drafting frames:
   - Character identity: age range, build, facial silhouette, hair mass, costume silhouette, and distinguishing feature.
   - Environment: architecture, entrances, furniture, hero props, and fixed light direction.
   - Blocking: character positions, eyelines, movement direction, and screen axis.
   - Material: every visible surface uses the same matte white clay unless the user explicitly allows another neutral value.
3. Choose the board format from the request. Default to 9 frames, 16:9, landscape, with one decisive narrative beat per frame. Use 12 frames when the action needs setup, development, and consequence that cannot read clearly in 9.
4. Design coverage as a sequence, not a collection of attractive angles. Include an establishing or master shot, readable action coverage, reaction or insert shots only when they add information, and a final consequence image.
5. Keep screen direction and the 180-degree axis stable. Cross the axis only through a motivated neutral shot, visible camera move, or character movement that re-establishes orientation.
6. Write a global lock once, then one self-contained prompt per frame. Repeat exact identity, wardrobe silhouette, environment anchors, material wording, and light direction where consistency matters.
7. Generate frames sequentially when tools permit. Approve or inspect frame 1 as the identity and environment anchor, then reference the latest approved frame for the next shot. Generate a single grid only for fast ideation.
8. Run the QA checklist in the reference. Repair individual misses rather than rewriting the whole board.

## Defaults

Apply sensible defaults without stopping for questions when the source is clear:

- Aspect ratio: 16:9.
- Board size: 9 frames.
- Image treatment: monochrome off-white clay with neutral-gray shadows.
- Human form: realistic proportions and readable anatomy, slightly simplified surface detail.
- Lighting: soft global illumination, clear key direction, contact shadows, and ambient occlusion.
- Camera: restrained cinematic coverage, physically plausible focal lengths, no random lens changes.
- Text: place shot labels and notes outside generated imagery; avoid asking the image model to render captions.

Ask one concise question only when a missing decision would materially change the story, such as which ending to board or which character is the protagonist.

## Output Modes

### Prompt Board

Return:

1. Global continuity and style lock.
2. A compact beat list.
3. One shot block per frame containing shot number, duration if known, shot purpose, action, framing/lens, camera movement, light, continuity note, generation prompt, and negative prompt.
4. A final consistency checklist.

### Storyboard Sheet

For a requested 3x3 or 4x3 sheet, provide a master sheet prompt plus the individual frame prompts. Keep panel borders simple and consistent. Put labels below panels during deterministic layout or post-production, not inside the generated scene.

### Generated Images

When the user asks for actual images, use the available raster image-generation tool or skill. Prefer sequential individual frames for continuity, then assemble the approved frames into a grid if tooling supports it. Inspect the result for blank frames, repeated compositions, colored materials, identity drift, broken anatomy, and incoherent screen direction.

## Non-Negotiable Look

- Use one untextured matte white or warm off-white clay material across skin, hair, clothes, props, architecture, and landscape.
- Preserve form through light and shadow. White model does not mean flat lighting or blown highlights.
- Allow subtle sculpting seams and hand-shaped irregularity; keep them subordinate to anatomy and readability.
- Avoid colored accents, realistic skin, fabric weave, wood grain, metallic surfaces, glossy plastic, translucent skin, toy packaging, cute chibi proportions, polished CGI, and finished production textures.
- Keep eyes, teeth, and hair in the same material family. Define them through shape and value, not color.
- Favor readable silhouettes, grounded feet, correct contact, and believable object interaction.

## Delivery Rules

- Speak in the user's language.
- Keep prompts ready to paste into common image models.
- Preserve original dialogue and story facts unless the user asks for adaptation.
- State any inferred action briefly instead of inventing a new subplot.
- Do not use named studio or living-artist imitation as the style lock. Describe material, lighting, framing, and motion directly.
