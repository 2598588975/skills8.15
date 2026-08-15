# 分层封面工作流

用于电影封面、海报封面、系列影片封面，尤其是用户提供参考图、剧照或三联画时。

## 核心原则

- 先保底图内容，再做字体设计。
- 底图和文字都必须是图像设计产物；本地程序只做裁剪、缩放、混合和定位。
- 若原参考图二次裁剪即可成立，直接裁剪原图作为底图层，不再生成新底图。
- 字体图层必须单独输出，便于用户复用。

## 标准产物

每张封面输出四类文件：

1. `base`：无文字底图层，9:16。
2. `type`：字体设计图层，9:16 或透明/黑底/白底字体图。
3. `composite`：按网格合成后的最终封面。
4. `grid`：JSON 配置，记录画布、底图裁剪、字体图层位置、缩放、混合模式和透明度。

默认放在 `D:\Codex_Outputs\images` 的任务子目录中。

## 底图层

优先级：

1. 直接裁剪原图：内容、人物、场景和影调最稳定。
2. 基于参考图编辑生成：当三联图无法直接裁成单张封面时使用。
3. 文生图重建：仅当没有可用参考图时使用。

底图提示词要强调：

- 保留原片内容一致性：人物关系、场景、道具、时代、空间秩序。
- 低到中等对比，暗部有细节。
- 不要焦黑、脏污、重 HDR、强暗角、恐怖片质感。
- 不要文字、logo、奖项、桂冠、媒体引语。

## 字体图层

字体图层由图像模型生成，不由本地绘字。优先生成整张 9:16 的字体设计层，包含准确的：

- 中文主标题
- 英文副题
- 宣传语
- 日期
- 统一署名：`导演 / 编剧 / 摄影 / 美术 / 剪辑 / 音乐 / 出品  梵想美学`

推荐两种图层格式：

- 白字/浅色字在纯黑背景：合成时用 `screen` 混合。
- 黑字/深色字在纯白背景：合成时用 `multiply` 混合。

提示词必须写明：

- 只生成字体设计层，不生成电影画面。
- 背景必须纯黑或纯白，不能有纹理、人物、场景、边框。
- 只允许出现指定文字；禁止桂冠、奖项、媒体引语、随机小字、乱码和重复英文。
- 字体可以有质感和字图关系暗示，但要可读。

## 网格合成

使用 9:16 画布，推荐 `1080x1920` 或 `1024x1792`。

建议网格：

- 顶部宣传语：x 8%–92%，y 5%–14%。
- 主标题：x 8%–92%，y 58%–78%，可横排；东方题材可放右侧竖排 x 62%–92%，y 10%–45%。
- 英文副题：紧随主标题，字号弱于中文。
- 日期：y 80%–88%。
- 署名：y 92%–96%。

本地合成只允许：

- 裁剪底图。
- 缩放字体图层。
- 移动字体图层。
- `screen`、`multiply`、`normal` 混合。
- 调整整体透明度。

禁止在本地新建文本对象、重新打字或修字。

## 质检

- 底图是否保留参考图核心内容。
- 字体层是否可单独复用。
- 字体层是否由图像模型生成。
- 合成图是否没有文字遮挡关键人物、物件和叙事动作。
- 是否没有桂冠、奖项、媒体引语、真实片商和随机小字。
- 是否比一体生成更稳定：底图不漂、文字风格独立、最终封面有电影宣传完成度。

## Poster-effect and title-scale rules

When references show strong poster craft, extract the relationship between effect, surface, and typography, not only the depicted subject.

- The base layer should create a physical surface for typography: frosted glass, fogged window, reflection, translucent curtain, wet floor, paper field, wall texture, projection haze, large shadow, or a quiet color block.
- Frosted glass and soft obstruction are especially suitable for literary drama, suspense, memory, romance, and psychological subjects. Use them to create a milky area where text can sit, partially disappear, or be reflected.
- Do not overuse high contrast, dirty blacks, HDR, heavy grain, or random debris. If a prop is dark or messy, keep it as one controlled narrative clue instead of scattered texture.
- Chinese title design may intentionally become the main composition. For bold poster directions, let the Chinese title occupy roughly 30%-60% of the poster width or height.
- The title may overlap or partially cover people, objects, glass, doors, horizon lines, or color fields when the overlap strengthens the story. Avoid polite floating captions that feel pasted on.
- Large handwritten Chinese, heavy Song/Ming serif, compressed sans, or calligraphic marks should be chosen according to genre. Tiny English text is secondary rhythm, not the visual center.
- A strong title composition can use asymmetry, broken strokes, oversized single characters, vertical stacking, red accent letters, or scattered English letters, but the Chinese title must remain readable.
- Before generating the base, decide where the title can physically live: sky/salt plane, glass panel, curtain edge, wall, floor reflection, door opening, body shadow, or object surface.

Useful title-layout archetypes:

- Literary vertical title: tall Song/Ming Chinese title on the left third, large negative space, tiny English subtitle nearby, restrained top tagline.
- Suspense surface title: oversized serif title printed on frosted glass, mirror, door, table, or wall, with image details blurred behind it.
- Epic calligraphy title: one or two large black brush characters in the sky or central axis, with small vertical side text and seal-like red accents.
- Institutional drama title: title locked to a table, courtroom, corridor, or vanishing-point axis; the table or corridor becomes the title base.
- Object-key poster: room key, cup, box, helmet, mirror, or other prop anchors the lower third; title can be large above it, but the prop remains readable.
- Sports or pressure poster: face or helmet may fill the top half, action line in the lower half, title heavy and low like field paint or stamped lettering.

## Mandatory LLM pre-analysis gate

Before generating any base layer from reference triptychs or keyword-only tests, do an explicit movie-poster analysis pass. Do not jump straight from reference image to image prompt.

The analysis must decide:

- genre and subgenre
- likely audience and rating mood: child/family, teen, art-house adult, thriller, sports, epic, etc.
- emotional temperature: playful, warm, suspenseful, solemn, absurd, bleak, romantic, etc.
- whether the reference has recognizable IP-adjacent qualities such as Pixar-like animals, mascot animation, toy-like characters, theme-park fantasy, or brand-like sports imagery
- what must be preserved as the story core
- what must not be distorted because it would violate the film type
- suitable poster lane: family animation key art, prestige animated feature, art-house drama, suspense object poster, sports pressure poster, epic landscape, etc.
- title naming direction before any image generation
- base-layer concept and title-surface concept

Hard rule: if the reference looks like a child/family animated film or Pixar-like animal IP, do not convert it into a gloomy empty art-house scene unless the user explicitly asks for a dark reinterpretation. Keep warmth, character charm, performance energy, readable faces, and family-audience accessibility. The poster may become more sophisticated, but it must not betray the movie's genre promise.

Hard rule: if a reference cannot be reproduced exactly, either make a clearly original thematic diffraction or preserve only a small number of abstract visual DNA traits. Avoid the weak middle ground where the result looks like an inaccurate copy.
