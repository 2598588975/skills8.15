# White-Clay Storyboard Prompt System

## Contents

1. Visual definition
2. Global locks
3. Shot construction
4. Continuity method
5. Grid workflows
6. Failure repair
7. QA checklist

## Visual Definition

Treat the image as a cinematic previsualization built from physical-looking, unpainted clay maquettes. The board should communicate staging, lens choice, light direction, spatial depth, and emotional emphasis without relying on color or finished textures.

The desired result sits between a sculptor's maquette and a film previs frame:

- Uniform warm-white or neutral-white matte clay.
- Untextured surfaces with fine hand-shaped irregularity.
- Neutral-gray value range created by lighting, ambient occlusion, and contact shadows.
- Realistic human scale and anatomy unless the source explicitly requests stylization.
- Film-set composition rather than product-icon or toy-diorama composition.

## Global Locks

### Material Lock

Use this wording consistently:

```text
Every visible subject and surface is built from the same unpainted matte warm-white clay: skin, hair, eyes, clothing, props, furniture, architecture, ground, and background forms. No applied color and no finished material maps. Softly sculpted edges, faint tool marks and small hand-shaped irregularities remain visible. Form is separated only by shape, neutral value, soft global illumination, contact shadows, and restrained ambient occlusion. Highlights retain detail and never clip to pure white.
```

### Cinematic Lock

```text
Cinematic physical-maquette previsualization, realistic scale and anatomy, readable silhouette, grounded contact, coherent eyelines, physically plausible lens perspective, controlled depth of field, one motivated key-light direction, soft fill, restrained rim separation, monochrome white-and-neutral-gray value structure.
```

### Negative Lock

```text
No color accents, no realistic skin tone, no painted eyes, no fabric weave, no wood grain, no metal shader, no glass shader, no glossy plastic, no porcelain glaze, no translucent wax, no subsurface skin, no cute toy style, no chibi proportions, no oversized head or eyes, no polished commercial CGI, no finished textures, no text inside the scene, no duplicate characters, no extra limbs or fingers, no floating objects, no melted anatomy, no overexposed white surfaces.
```

Use the negative lock as constraints in prose when a model does not support a separate negative prompt field.

## Shot Construction

Build each prompt in this order:

1. Shot identity and narrative purpose.
2. Exact character and environment anchors.
3. Blocking and action at one readable instant.
4. Camera position, shot size, lens, height, and angle.
5. Camera movement only if the output is for video or animatic planning.
6. Key-light direction and tonal separation.
7. Material and cinematic locks.
8. Negative lock.

### Individual Frame Template

```text
SHOT {NN}, {NARRATIVE PURPOSE}. {ASPECT RATIO} cinematic storyboard frame.

SUBJECT AND LOCATION: {EXACT CHARACTER LOCK}. {EXACT ENVIRONMENT LOCK}.

BLOCKING AND ACTION: {WHO IS WHERE, FACING WHICH DIRECTION, DOING ONE CLEAR ACTION}. Preserve {SCREEN DIRECTION OR EYELINE}. The frame captures {DECISIVE INSTANT}.

CAMERA: {SHOT SIZE}, {LENS} lens feel, camera at {HEIGHT}, viewed from {ANGLE}; {COMPOSITION AND FOREGROUND/MIDGROUND/BACKGROUND}. {OPTIONAL CAMERA MOVE}.

LIGHT: motivated key light from {FIXED DIRECTION}, {SOFT/HARD} quality, {FILL LEVEL}, clear contact shadows and controlled ambient occlusion; preserve detail in all white surfaces.

MATERIAL: {MATERIAL LOCK}

STYLE: {CINEMATIC LOCK}

CONSTRAINTS: {NEGATIVE LOCK}
```

### Focal-Length Guide

- 18-24mm: spatial geography, pronounced foreground depth, use sparingly near faces.
- 28-35mm: active master shots, two-shots, environmental proximity.
- 40-50mm: neutral dialogue coverage and balanced human perspective.
- 65-85mm: reactions, emotional compression, clean close-ups.
- 100mm or longer: inserts and distant observation, only when compression serves the beat.

Keep neighboring shots visually distinct through purpose, scale, or angle. Do not change all three at once without narrative motivation.

## Continuity Method

Create exact text locks before the first frame:

```text
CHARACTER A: {age/build}, {face silhouette}, {hair mass}, {costume silhouette}, {distinctive feature}.
CHARACTER B: ...
SET: {architecture}, {fixed entrances}, {hero furniture}, {hero props}.
AXIS: A remains screen-left looking right; B remains screen-right looking left.
MOVEMENT: principal travel direction is left-to-right until {defined reversal}.
LIGHT: key light always enters from camera-left / geographic east.
```

Copy these phrases unchanged into every relevant prompt. For sequential generation:

1. Generate the establishing or master frame first.
2. Inspect and approve character silhouette, spatial layout, and light direction.
3. Feed the approved frame as the visual reference for the next frame when supported.
4. Carry the latest approved identity frame forward. Use the master frame again whenever the location geometry drifts.
5. Regenerate a failed frame from the last good anchor instead of referencing the failed frame.

## Grid Workflows

### Fast One-Pass Grid

Use only for ideation. Ask for a clean 3x3 or 4x3 contact sheet with equal panels, thin neutral borders, consistent aspect ratios, and no in-scene labels. Explicitly assign one shot to each panel from top-left to bottom-right. Expect weaker identity and geometry consistency than sequential generation.

### Production Grid

Generate frames individually, then assemble them in order. Add shot numbers, duration, and notes outside image content with deterministic layout software. This avoids malformed text and lets one frame be replaced without disturbing the others.

### Master Grid Prompt

```text
A {ROWS} by {COLUMNS} cinematic storyboard contact sheet, {TOTAL} equal panels in reading order, thin neutral-gray panel borders, no captions inside the scenes. Every panel depicts the same locked cast and set as a monochrome unpainted matte white-clay physical maquette. Maintain exact character proportions, costume silhouettes, set geography, screen direction, and key-light direction across all panels. Vary shot size and camera position only according to the numbered shot plan. Each panel must show a distinct narrative beat; no duplicate compositions and no repeated action.
```

Append a short panel map after the master prompt:

```text
Panel 1: {shot summary}
Panel 2: {shot summary}
...
```

## Failure Repair

- Colored or realistic materials: repeat that every visible surface shares one unpainted matte clay shader; name troublesome objects explicitly.
- Flat unreadable white shapes: strengthen side light, contact shadows, ambient occlusion, foreground overlap, and neutral-gray separation. Do not add color.
- Glossy plastic or porcelain: request high roughness, broad diffused highlights, no clearcoat, no glaze, and no ray-traced sparkle.
- Cute toy appearance: restore realistic proportions, adult facial structure, restrained eyes, film-set scale, and natural posture.
- Identity drift: return to the last approved identity anchor and repeat the exact character lock.
- Set drift: reference the master frame and restate doors, windows, furniture, and geographic positions.
- Repetitive board: label the purpose of each shot and remove any frame that adds no new action, information, emotion, or spatial orientation.
- Broken axis: restore screen-left/screen-right positions or insert a neutral frontal/master shot that re-establishes geography.
- Broken hands or object contact: simplify to one hand action and one contact point at the decisive instant.
- Overexposed white model: lower exposure, protect highlights, use a neutral-gray background value, and add soft negative fill.

## QA Checklist

Verify before delivery:

- Every frame adds a distinct story beat.
- Character count, identity, proportions, costume silhouette, and hair mass remain stable.
- Set entrances, furniture, and hero props remain in fixed positions.
- Screen direction, eyelines, and movement axis are coherent.
- Lens and camera height serve the shot purpose.
- The complete image is monochrome white clay with no accidental colored or finished materials.
- White surfaces retain detail through neutral values and contact shadows.
- Anatomy, feet, hands, and object contacts are believable.
- No frame is blank, duplicated, melted, or cropped unintentionally.
- Grid panels have stable dimensions and do not contain malformed generated labels.
