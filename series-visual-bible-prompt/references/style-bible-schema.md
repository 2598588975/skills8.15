# Style Bible Schema

Use this reference when producing structured visual bibles or scene-by-scene style cards.

## Fast Style Lock Template

```markdown
**一句话视觉定位**
[一句话说明这部短剧/广告片看起来像什么真实拍摄体系，而不是堆风格词。]

**整体风格**
[画幅、成像介质、现实拍摄感、整体空间与人物关系。]

**色彩系统**
- 主色域:
- 次色域:
- 强调色:
- 色彩来源:
- 禁止色彩:

**光线系统**
- 主光源:
- 方向:
- 色温:
- 阴影:
- 变化:

**镜头语言**
- 焦段范围:
- 机位高度:
- 运镜纪律:
- 构图压力:

**材质与肤色**
- 皮肤:
- 服装:
- 金属/玻璃/木/纸/湿地:
- 高光和暗部:

**人物一致性**
- 稳定身份:
- 当前造型:
- 表演状态:

**全局负面约束**
[3-6 条，只针对当前项目。]

**可复制全局提示词**
[一段可粘贴到图片或视频模型前半段的中文/英文提示词。]
```

## Production Visual Bible Template

```markdown
**项目视觉命题**
- 项目类型:
- 观众第一感觉:
- 视觉核心冲突:
- 统一风格句:

**Capture Profile**
- 画幅:
- 成像基底:
- 清晰度:
- 颗粒/噪点:
- 曝光哲学:
- 胶片/数字质感:

**Color Bible**
- 主色域:
- 次色域:
- 强调色:
- 色彩比例:
- 色彩来源:
- 场景变化规则:
- 禁用色:

**Lighting Bible**
- 日景:
- 夜景:
- 室内:
- 外景:
- 人脸受光规则:
- 材质高光规则:
- 光线变化规则:

**Camera Bible**
- 常用焦段:
- 禁用焦段/机位:
- 机位高度:
- 运镜:
- 轴线:
- 正反打规则:
- 运动/慢动作规则:

**Composition Bible**
- 主要构图压力:
- 视线入口:
- 视线阻断:
- 背景信息:
- 留白/遮挡:

**Character Bible**
| role_id | stable identity | hair/costume | body baseline | gaze habit | performance arc | do-not-change |
|---|---|---|---|---|---|---|

**Environment Bible**
| env_id | geography | key anchors | light source | color source | material response | allowed angles | do-not-change |
|---|---|---|---|---|---|---|---|

**Scene Style Cards**
| scene_id | story function | env_id | characters | color/light | camera | continuity anchors | image prompt | video prompt |
|---|---|---|---|---|---|---|---|---|

**Global Prompt Block**
[项目级可复制提示词。]

**Negative Constraints**
[最小负面约束。]
```

## Scene Style Card Detail

Use this card when the user needs each scene or shot to stay visually consistent.

```markdown
### SCENE [ID] - [Name]

**剧情职责**
[这场戏推动什么关系、信息或转折。]

**场景锁定**
- 地点:
- 时间:
- 空间轴线:
- 背景锚点:
- 可见道具:
- 不允许变化:

**人物锁定**
- 出场角色:
- 稳定外貌:
- 当前服装:
- 当前身体状态:
- 视线目标:
- 微表情强度:

**色彩和光线**
- 主色:
- 强调色:
- 主光源:
- 方向/色温:
- 阴影:
- 材质响应:

**镜头和构图**
- 景别:
- 焦段:
- 机位:
- 运镜:
- 构图压力:
- 背景层次:

**图片提示词**
[单帧图像 prompt，只描述一个冻结瞬间。]

**视频提示词**
[视频 prompt，描述起始状态、动作过程、结束状态、镜头运动和声音。]

**负面约束**
[3-6 条。]
```

## Ad Film Add-On

For ads, append:

```markdown
**Brand/Product Priority**
- Product hero angle:
- Material highlight:
- Hand/product interaction:
- Logo or text safe area:
- End-frame rule:
- Conversion emotion:
```

Keep ads visually specific without turning them into generic glossy commercials.
