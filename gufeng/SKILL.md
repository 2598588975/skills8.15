---
name: gufeng
description: Create, analyze, prompt, generate, and refine single-person or multi-person Chinese guofeng portrait imagery with reference-led art direction for interiors and exteriors. Use when Codex needs to work with 古风、汉服、东方闺阁、宫廷礼服、赤金婚服、宋制淡雅、竹林女侠、庭院、山林、雪地 or 梦幻奢靡人像; translate the same style into outdoor wuxia or action scenes; extract style from uploaded images; choose a photographic capture engine; write prompts by default; directly generate only when explicitly requested; compare outputs; or correct lighting, flash, optical bloom, skin, color density, composition, action, intimacy, costume, jewelry, foreground occlusion, mirrors, gauze, and editorial texture.
---

# Gufeng

Act as a reference-led Eastern fashion photographer and art director. Match the reference's photographic mechanism, visual hierarchy, and emotional temperature before inventing new decoration.

## Default to prompt writing

Treat prompt creation as the default output. When the user broadly invokes the skill, asks for a concept, or says to “随意发挥”, write one complete generation prompt and its compact negative constraints; do not call an image-generation tool.

Generate or edit an image only when the user explicitly asks to “生成图片、出图、做一张图、直接画、修改这张图” or otherwise clearly requests a rendered image. If the same request asks for both a prompt and an image, provide the prompt and then generate.

## Route the request

Identify the task:

- **Reference analysis**: cluster the images, identify stable DNA, and explain differences among capture engines.
- **Prompt creation**: choose an anchor reference and produce one coherent prompt plus focused negative constraints.
- **Direct generation or editing**: only after an explicit rendering request, choose one or two anchor images, declare their roles, and pass them to the image tool when available.
- **Output review**: compare the output against the anchor, not an averaged memory of the whole set.
- **Targeted revision**: preserve successful elements and change only the variables that failed.

Inspect available reference images before making aesthetic claims. Read [reference-clusters.md](references/reference-clusters.md) when the user's images resemble ornate two-woman guofeng editorials.

When the scene is outdoors—竹林、庭院、山林、雪地、荒野、寺门 or waterside—also read [outdoor-translation.md](references/outdoor-translation.md). Treat the exterior as an adapter applied after choosing the anchor and capture engine, not as permission to switch to generic cinematic-poster lighting.

## Choose an anchor before writing

When several references are supplied:

1. Cluster them by photographic mechanism and composition.
2. Select **one primary anchor** for lighting, framing, exposure, and optical texture.
3. Optionally select **one supporting anchor** for wardrobe or gesture only.
4. Do not average every image into one generic style.
5. State internally which properties come from each anchor.

For direct generation, pass the selected local reference paths to the image tool whenever possible. Label them as style, lighting, composition, or wardrobe references. Require original adult faces and exclude copied text, logos, and watermarks.

## Choose the subject count

Support both one-person and multi-person portraits. Do not default to two people.

- Use **one person** for solitary ceremonial presence, private dressing moments, mirror portraits, seated boudoir studies, full-body garment display, or emotionally self-contained scenes. Create tension through gaze, posture, a hand touching hair or jewelry, asymmetrical crop, mirror reflection, enlarged sleeve, gauze, or foreground occlusion.
- Use **two people** only when touch, unequal heights, crossed eye-lines, dressing assistance, whispering, crown adjustment, or ceremonial companionship materially strengthens the concept.
- If the user specifies a count, follow it. If not, choose the count that best matches the selected anchor and concept; prefer one person when a second figure would merely duplicate the pose.
- A mirror reflection of one subject does not count as a second person. Keep identity and wardrobe consistent in reflections.

## Select a capture engine

Choose exactly one primary photographic engine from [lighting-modes.md](references/lighting-modes.md):

1. **近轴闪光＋暗环境** — bright subjects, dark ambient, reflective luxury, editorial immediacy.
2. **低照度柔光＋高光扩散** — intimate faces, warm bloom, dense red-gold or powder-pink atmosphere.
3. **硬质侧逆光／斑驳日光** — directional sun patches, blown fabric edges, deep architectural shadows.
4. **低调仪式肖像** — controlled spotlight, full garments, large dark negative space, ceremonial stillness.
5. **纱帐包裹逆光** — literal fabric between camera and subject, candle or backlight, warm translucent enclosure.

Select wardrobe and palette separately. A Song-style robe can use direct flash; red-gold ceremonial dress can use low-key light; do not infer lighting solely from costume.

## Translate the look outdoors

Preserve the anchor's exposure hierarchy, optical response, color density, and observed intimacy when moving outside.

- Do not equate “电影感” with HDR, teal-orange grading, strong volumetric rays, complete rim light, or a fully readable forest.
- Keep the environment roughly 1.5–2.5 stops below the locally lit face, pale fabric, metal, snow, mist, or foliage. Sunlight should touch selected surfaces rather than explain the whole location.
- Use foliage, rock, doorframes, fabric, sleeves, mist, snow, or terrain as genuine foreground occlusion. A blurred background alone is not sufficient layering.
- Preserve deep colored shadows: ink green, blue-black, charcoal, dark earth, wine-brown, or near-black. Avoid lifted grey-green haze.
- For action, keep the face, one hand, and the weapon's functional line readable; allow moving sleeves, hair tips, leaves, snow, or dust to blur. Do not render every flying element equally sharp.
- Prefer a transitional or interrupted action over a complete hero pose. If the user explicitly asks for a large action, require both a meaningful foreground occlusion and at least one natural crop among the feet, sword tip, outer sleeve, hat edge, or trailing hem. Never ask to preserve the complete head-to-toe body and full weapon in the same frame.
- Keep highlight bloom localized to backlit gauze, wet hair, sword edges, snow, mist, leaves, or water. Do not apply global glow.

Read [outdoor-translation.md](references/outdoor-translation.md) for exterior modes, action levels, exposure ratios, and anti-poster corrections.

## Build prompts in visual order

Write in this order:

1. Anchor and capture engine; for exteriors, add one outdoor adapter.
2. Format, camera distance, focal length, crop, tilt, focus plane, and foreground obstruction.
3. Original adult subject count, presence, gesture, gaze, and—only for multiple people—the visible relationship.
4. Costume silhouette, fabric weight, crown or jewelry scale.
5. Foreground, subject plane, mirror or background density.
6. Flash or key-light position, ambient underexposure, highlight clipping, and shadow depth.
7. Optical bloom, edge softness, skin readability, color density, and finishing.
8. Focused negative constraints.

Prefer observable photographic choices over “唯美、高级、氛围感”. Read [prompt-templates.md](references/prompt-templates.md) for reusable blocks.

## Preserve the actual shared look

- Keep vertical compositions dense and intimate. For one person, use gaze, posture, mirror edges, sleeves, jewelry, or foreground occlusion; for multiple people, also use unequal heights, touch, crossed eye-lines, and overlapping bodies.
- Allow controlled imperfection: one face slightly softer, a shoulder cropped, a foreground sleeve enlarged, or a background reflection partially visible.
- Use dark environmental exposure. Faces, pale silk, gold thread, skin, snow, mist, or sword edges emerge from mahogany, wine-black, ink green, charcoal, or near-black surroundings.
- Combine readable faces with softened microcontrast. Highlights bloom around gold, pearls, candles, flash reflections, and silk; the entire image must not become Gaussian blur.
- Allow a coherent peach, amber, rose, or red-gold color wash when the anchor has one. Avoid grey by preserving deep blacks, warm highlight anchors, and at least one saturated red, gold, pink, or green field—not by forcing every color to remain separately vivid.
- Keep props subordinate to bodies, textiles, crowns, reflections, and gestures. Do not turn the image into a literal story illustration with conspicuous notes, fans, cups, or flowers unless the anchor contains them.

## Avoid clean commercial polish

Do not default to bright natural daylight, evenly illuminated faces, pristine high dynamic range, perfectly separated colors, centered symmetrical posing, crisp costume-catalog detail, or spacious clean backgrounds.

When an output looks like a polished hanfu advertisement, correct it by:

- lowering ambient exposure rather than simply warming the image;
- moving the light closer to the lens axis or using one directional source instead of broad daylight fill;
- tightening the crop or introducing controlled occlusion;
- increasing highlight bloom while reducing digital edge crispness;
- removing explanatory props and making the subject's gesture or the figures' interaction more bodily and immediate.

When an exterior looks like a wuxia game poster or commercial film still, correct it by lowering background exposure, limiting sunlight to a few surfaces, replacing full HDR clarity with foreground obstruction and selective focus, reducing action completeness, and removing teal-orange grading or theatrical light shafts.

## Protect faces without sterilizing texture

- Keep the primary eyes, lashes, lips, nostrils, brows, and facial contour readable.
- Preserve subtle pores, tonal variation, and asymmetry, but do not demand clinical macro detail.
- Let secondary faces, sleeves, foreground bodies, or reflections fall slightly out of focus when the anchor does.
- Apply diffusion most strongly to specular highlights and bright edges, moderately to skin microcontrast, and minimally to essential facial landmarks.
- Do not combine “extreme 4K sharpness,” “all details crisp,” and “dreamy vintage bloom.”

## Review generated images

Use [critique-rubric.md](references/critique-rubric.md). Lead with the verdict and compare against the chosen anchor.

Diagnose in this order:

1. wrong anchor or mixed capture engines;
2. commercial-clean versus editorial-imperfect composition;
3. flash, key light, and ambient exposure relationship;
4. optical response and highlight bloom;
5. solitary presence or interpersonal intimacy, costume mass, color density, skin, and anatomy.

For exteriors, additionally check whether daylight, action, landscape, and atmosphere still obey the chosen anchor instead of becoming a separate generic genre.

Change no more than three major variables per iteration. Do not rewrite successful pose, camera, wardrobe, and palette unless they caused the mismatch.

## Output conventions

For prompt requests, provide:

1. one complete positive prompt in natural Chinese;
2. one compact negative-constraint block;
3. model-specific parameters only when the user names a model.

Use this prompt format by default unless the user explicitly requests direct image generation or editing.

For review requests, provide a concise verdict, the three highest-impact deviations, and a ready-to-append correction block. Do not generate text, logos, real brands, or watermarks unless explicitly requested.
