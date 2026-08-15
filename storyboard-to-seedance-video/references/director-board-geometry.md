# Director-Board Geometry

Read this reference when a storyboard contains two or more characters, directional movement, entrances/exits, fights, chases, prop exchange, or any cut whose spatial continuity matters.

## 1. Establish the scene coordinate system

Before designing panels, record internally:

- Fixed spatial anchors: doors, windows, table edges, stairs, vehicles and important props.
- Character world positions: start position, facing direction, reachable objects and exit route.
- Primary axis: character-to-character line for dialogue, line of travel for movement, or subject-to-object line for discovery/action.
- Approved camera zone: the side of the axis used by the scene's coverage.
- Screen projection: who appears screen-left/right, who faces left/right, and which direction movement reads on screen.

Use world position for geography and screen position for the current composition. A camera cut can change screen projection but cannot teleport a character in world space.

## 2. Build a blocking ledger

For each panel, track:

| Field | Required content |
|---|---|
| Start | Character position, posture, facing, eyeline and held prop |
| Motion | One readable path or action with direction and contact point |
| End | Stable pose/location that can become the next panel's start |
| Camera | Camera side of axis, height, angle, shot size and movement |
| Screen | Subject screen-left/center/right and travel direction |
| Continuity | Wardrobe, light direction, prop state and environment anchors |

Enforce `panel N end state = panel N+1 start state` unless a visible time/location transition is explicitly designed.

## 3. Control the axis

- Keep all coverage on the approved side of the 180-degree line by default.
- Preserve screen direction: a character moving left-to-right continues left-to-right until a visible turn, neutral shot or axis change establishes otherwise.
- Preserve eyelines: opposite speakers look toward complementary off-screen directions and compatible vertical targets.
- Apply the 30-degree rule when cutting around the same subject; change angle or shot size enough to avoid a visual jump.
- Do not cross the axis merely to create variety.

Allow an axis change only through one of these visible mechanisms:

1. The camera moves across the line within a continuous shot.
2. A neutral shot sits on the axis and re-establishes geography.
3. A character visibly moves so the relationship line reforms.
4. A clear establishing shot resets the scene after an intentional temporal/spatial break.

## 4. Encode geometry into the generated board

Every storyboard panel prompt must state observable geometry, not abstract continuity language. Use phrases such as:

- `Character A remains screen-left facing right; Character B remains screen-right facing left.`
- `Camera stays inside the south-side camera zone established by the master shot.`
- `The runner continues left-to-right; the exit remains ahead on screen-right.`
- `The key begins in A's right hand and ends visibly resting in B's open left palm.`

Use arrows and small annotations on the planning board for body path, camera path, eyeline and light direction. These marks belong only to the storyboard artifact; Stage 2 must explicitly exclude arrows, labels and guide marks from the final video.

## 5. Image-to-video handoff

Treat approved storyboard panels as spatial evidence. The Seedance prompt must preserve:

- Identity reference from `image1`.
- Shot order and geometry from `image2`.
- Start/end body positions and prop states.
- Screen direction, eyelines, axis side and camera path.
- Room-coordinate light source and stable environment anchors.

If a generated panel violates the ledger, regenerate the still before generating video. Do not ask motion text to repair a wrong axis, mirrored character placement or impossible prop ownership already baked into the reference image.

## 6. Pre-video gate

Approve a panel only when:

- The number and identity of characters are correct.
- World position and screen position are both plausible.
- Axis side, facing direction and eyelines agree with adjacent panels.
- Start and end poses support the intended motion.
- Hands contact the correct props and ownership is unambiguous.
- Entrances, exits and camera paths are physically reachable.
- Light direction and fixed set anchors remain consistent.
- No planning arrows, labels, grids or annotations are intended to survive into the video.
