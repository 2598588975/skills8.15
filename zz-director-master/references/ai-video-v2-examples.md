# 视频提示词生成工作流 V2.0（示例库）

本文件只作为 `video-prompt-v2-workflow.md` 的参考库。

## 阅读导航

- 风格词过于抽象：查“风格解析种子”。
- 镜头、光影或专业词选择不确定：查“专业视觉锚点示例”“镜头字段写法示例”“光线字段示例”。
- 需要生成角色文本音色：查“角色音色示例”。
- 需要处理剧情摘要、资产状态、镜头密度或台词标点：读取对应同名示例章节。
- 只提取可复用的写法规律，不复制示例中的具体内容。

调用原则：
- 主文件能独立执行；本文件只在风格、专业视听锚点、角色音色或写法不确定时调用。
- 本文件示例不是封闭词库，不得机械照抄。
- 示例库不得覆盖主文件规则；冲突时以主文件为准。
- 示例只提供选择方向，最终必须根据剧本、资产、视频类型、画幅比例、视觉风格和连续性动态生成。

---

## 风格解析种子

当用户只给一个风格词时，先内部解析，再输出可执行的全局风格锁定词。

真人写实：
- 媒介来源：电影摄影 / 电视剧摄影 / 纪录片摄影 / 平台短视频实拍。
- 渲染方式：实拍 / naturalistic cinematography / handheld realism / practical lighting。
- 角色质感：真人演员 / natural skin tone / real skin texture。
- 运动质感：真实摄影运动 / restrained camera movement / handheld micro-shake。
- 材质语言：真实皮肤 / 布料纹理 / 旧墙肌理 / 雨水反光 / 胶片颗粒。
- 光影色彩：低饱和 / 冷暖对比 / 暗调 / 柔光 / 高反差。

3DCG：
- 媒介来源：游戏过场 / 动画电影 / 实时渲染 / 虚拟制片。
- 渲染方式：UE5 / PBR / physically based rendering / global illumination。
- 角色质感：数字人 / 动捕角色 / stylized 3D character。
- 运动质感：virtual camera / motion capture / cinematic motion blur。
- 材质语言：PBR材质 / subsurface scattering / ray-traced reflections。
- 光影色彩：volumetric lighting / controlled rim light / high dynamic range。

2D：
- 媒介来源：动画 / 漫画 / 插画 / 分镜动画。
- 渲染方式：手绘 / 平涂 / 赛璐璐 / 水墨 / 厚涂。
- 角色质感：漫画人物 / 卡通角色 / 手绘角色。
- 运动质感：limited animation / anime-style timing / parallax camera move。
- 材质语言：clean line art / paper texture / painterly brushwork / comic halftone。
- 光影色彩：color script / flat color blocks / stylized shadow / high saturation。

特殊风格化触发词：
- 回忆：slightly faded color, soft contrast, memory-like diffusion。
- 梦境：surreal lighting, soft focus, floating camera movement。
- 监控：fixed surveillance angle, low-resolution security footage, timestamp framing。
- 手机直播：vertical video framing, creator-style handheld, mobile video realism。
- 新闻画面：broadcast news framing, compressed video texture, documentary lighting。
- 游戏 UI：game interface overlay, virtual camera, HUD-like composition。

---

## 专业视觉锚点示例

以下只是方向，不是封闭词库。

低照度问题：
```text
low light cinematography
available light
natural shadow detail
controlled highlights
low noise shadows
filmic dynamic range
```

湿雨环境：
```text
wet pavement reflections
rain diffusion
soft specular highlights
backlit rain
moody overcast night
```

实景光源：
```text
practical light
warm spill light
ambient bounce light
mixed color temperature
soft key light
```

人物反应：
```text
50mm standard lens
85mm portrait lens
shallow depth of field
natural skin tone
real skin texture
```

道具文字：
```text
macro lens
extreme close-up
legible text
controlled reflections
```

色彩与质感：
```text
desaturated color grading
cool blue-gray palette
muted contrast
naturalistic cinematography
restrained realism
```

短视频平台影像：
```text
vertical video framing
creator-style handheld
mobile video realism
fast hook
jump cut rhythm
reaction shot timing
on-screen text readability
```

短漫剧节奏：
```text
fast-paced coverage
dramatic close-up
reaction shot timing
cliffhanger framing
phone screen insert
high information density
```

广告产品镜头：
```text
product hero shot
clean commercial lighting
macro product detail
packshot framing
call-to-action framing
crisp product texture
```

3DCG 视听语言：
```text
virtual camera
physically based rendering
global illumination
volumetric lighting
ray-traced reflections
motion blur
depth of field
```

2D 视听语言：
```text
clean line art
color script
limited animation
2D compositing
parallax camera move
cel shading
anime-style timing
```

强风格词。会改变作品气质，只有当用户明确指定或资产库已有风格时才使用：
```text
Blade Runner inspired
neon noir
teal and orange color grading
Cinestill 800T
Kodak Portra 400
Denis Villeneuve cinematography
Impressionist oil painting
cyberpunk aesthetic
```

---

## 角色音色示例

通用格式：

```text
@角色名：{年龄感}，{声线质感}，{语速}，{气息状态}，{情绪底色}，{禁止项}。
```

年轻女性，克制现实文戏：
```text
@艾莉：年轻女性声线，音色偏清但不甜腻，语速正常偏慢，气息轻、尾音短，情绪底色克制紧绷，禁止夸张哭腔和动漫化撒娇。
```

中年母亲，生活流亲情文戏：
```text
@母亲：中年女性声线，音色偏低而疲惫，语速正常，气息稳但略压住情绪，情绪底色隐忍和试探，禁止戏剧化喊叫和过度哭诉。
```

年轻男性，悬疑或压抑情绪：
```text
@阿远：年轻男性声线，音色偏低哑，语速正常偏慢，气息略紧，情绪底色警惕和迟疑，禁止英雄化怒吼和夸张喘息。
```

儿童或少年角色：
```text
@小孩：儿童声线，音色清亮但不过度可爱化，语速略快，气息短，情绪底色直接和不设防，禁止尖叫式童声和卡通化尾音。
```

旁白或说明角色：
```text
@旁白：成熟中性声线，语速稳定，咬字清楚，气息平稳，情绪底色克制客观，禁止播音腔过重和煽情拖腔。
```

---

## 本组剧情写法示例

推荐：
```text
本组剧情：@阿远 到达 @青槐路旧墙 后发现导航指向的门并不存在，他对照 16 号与 18 号，确认中间只有一面无门旧墙。
```

生活文戏推荐：
```text
本组剧情：@母亲 端着 @汤碗 出现在厨房门口，@女儿 先拒绝又尝试接过，两人隔着饭桌短暂停住，关系变得更僵。
```

不推荐：
```text
本组剧情：本组制造悬疑，推动人物情绪，形成反转。
```

原因：它只有编剧功能，没有可见事件和明确动作。

---

## 全局风格与本组环境写法示例

推荐：
```text
全局风格提示词：
风格锁定：真人写实电影质感，低照度现实主义摄影，低饱和冷灰蓝色调，雨夜湿润反光，实用光源冷暖对比，克制悬疑影像。
特殊风格化：不启用。全片保持普通风格锁定，不额外叠加梦境、回忆、监控、漫画化、游戏 UI 等局部风格。
```

本组环境推荐（一行格式，含持续声音）：

```text
【本组环境】
深夜，雨夜街道，小雨。持续光源：路灯冷光+店铺暖光。持续声音：细雨声、远处车辆经过声、手机导航提示音。氛围：潮湿、压抑、低饱和。
```

火场环境推荐：

```text
【本组环境】
夜晚，火场内部，浓烟遮挡。持续光源：火海橙红主光，黑烟削弱远景。持续声音：火焰燃烧轰鸣、结构坍塌声、远处爆炸余响。氛围：灼热、窒息、混乱。
```

室内科幻环境推荐：

```text
【本组环境】
深夜，温室舱内部，室内封闭。持续光源：控制台红色故障灯脉冲+休眠舱绿色状态灯。持续声音：低频电流嗡鸣、远处警报余音。氛围：压抑、窒息、暗红笼罩。
```

不推荐：
```text
每组重复输出电影质感、基础光影、基础色调。
本组环境拆成 5 行分字段写（字数浪费）；应压为“环境：时间，地点；光：...；声：...；氛围：...”。
漏写持续声音导致环境声在镜头声音字段中反复出现。
```

---

---

---

## 状态资产引用示例

### 有视觉资产库：正式状态资产

推荐：
```text
@赵无极_破败 穿过 @天阴门广场_白日练武，众弟子让开一条路。
@卢光_倒地受伤 撞在 @大殿门前_冲突后 的台阶上。
@古琴_震落 从琴案边缘滑落，琴声戛然而止。
@山神庙_毒烟弥漫 中，@武松 闭气追向 @庙门。
```

不推荐：
```text
@赵无极_愤怒 抬眼。
@林雪_惊讶 起身。
@孟凡_玩味消失 看向赵无极。
@卢光_嘲讽 走近。
```

原因：愤怒、惊讶、玩味、嘲讽是短暂表演或情绪，不是静态视觉状态。

### 无视觉资产库：临时状态引用

允许建立：
```text
@赵无极_破败：衣衫破损、尘土明显、外来者状态。
@卢光_倒地受伤：被拳击飞后倒在台阶上。
@古琴_震落：被真气震动后从琴板滑落。
@山神庙_毒烟弥漫：黑烟持续影响空间识别。
```

禁止建立：
```text
@赵无极_出拳
@林雪_冷漠
@周执事_厉声
@弟子_围观
```

原因：出拳、厉声、围观是动作或行为；冷漠是表演气质，不是需要复用的静态视觉差异。

### 镜头字段中的状态引用

动作字段推荐：
```text
动作：@赵无极_破败 穿过 @练武方阵，肩背不缩，手指压住破袖边缘。
动作：@卢光_倒地受伤 撞上台阶后滑落，胸口衣料塌陷，手臂失力垂下。
```

画面字段推荐：
```text
画面：竖屏中景，正面平视机位，@山神庙_毒烟弥漫 中黑烟压住庙门，火光变浑。
```

光线字段注意：
```text
光线：手机屏幕蓝光短暂照亮下巴。
```

说明：短暂手机光只写光线事实，不建立 `@场景_手机蓝光` 状态；只有烟雾、火场、雨中、战后等持续改变场景识别时，才建立场景状态。

### 最终报告示例

有正式资产库：
```text
状态资产引用：
使用正式状态资产：@赵无极_破败、@卢光_倒地受伤、@古琴_震落
使用临时状态引用：无
建议补做状态资产：@天阴门广场_冲突后
```

无视觉资产库：
```text
当前为临时资产引用版。
使用临时状态引用：@赵无极_破败、@卢光_倒地受伤、@古琴_震落
建议后续使用视觉资产 skill 补做正式多状态资产库。
```
## 镜头密度判断示例

电影故事片文戏：
```text
视听功能：文戏反应 / 对话拉扯。
传播功能：沉浸、可信表演、情绪余味。
镜头策略：1-3 镜；优先固定镜头和克制反打，不为每句台词切镜。
记忆点：一个眼神、手部动作、道具触感或台词后的停顿。
```

电影故事片动作：
```text
视听功能：动作推进 / 复杂打斗。
传播功能：动作因果清楚、受击结果有重量。
镜头策略：3-5 镜；按攻击发起 -> 闪避/防守 -> 接触点 -> 受击结果 -> 反应或下一动作方向拆。
记忆点：一次命中、兵器折断、人物位置反转或杀招结果。
```

短漫剧反转：
```text
视听功能：信息揭示 / 反转爽点。
传播功能：强情绪、强反应、信息推进。
镜头策略：4-7 镜；铺垫、揭示、主角反应、对手反应、结尾钩子不能糊在一镜里。
记忆点：身份揭示、打脸反应、强台词或关系反转。
```

短视频生活流：
```text
视听功能：开头钩子 / 口播推进 / 视觉反馈。
传播功能：前3秒留人，移动端可读，每几秒有新信息。
镜头策略：开头 hook 独立成镜；生活流可 1-2 镜，不强行快切；口播超过 8 秒必须给视觉变化。
记忆点：一个可截图动作、反应、道具或金句。
```

广告宣传片：
```text
视听功能：产品展示 / 使用过程 / 结果反馈。
传播功能：产品识别、卖点记忆、使用欲望、品牌收束。
镜头策略：产品首次出现独立成镜；每个卖点 1-2 镜；品牌收束 1 镜。
记忆点：产品外观、卖点动作、结果画面或品牌符号。
```
## 镜头字段写法示例

推荐（6 个镜头字段 + 组约束）：

```text
镜头1（0-5秒）
画面：中景，正面略低机位，人物在画面左侧，16号和18号形成左右对照，中间旧墙留出空缺感，墙面潮湿起皮。
镜头：35mm（35mm cinematic lens），中浅景深，焦点从手机导航切到门牌。
运镜：缓慢前推到墙面。
动作：@阿远 站在 @青槐路旧墙 前，对照门牌号，视线从 16 号移到 18 号，手指停在手机屏幕上，肩膀微微僵住。
台词：无。停顿 1 秒，呼吸变浅，眉心收紧。
光线：街灯冷光照出墙面潮湿纹理，远处店铺暖光只落在地面边缘。
```

有台词示例：

```text
镜头3（7-11秒）
画面：近景，正面略低机位，人物居中，背景控制台红光虚化。
镜头：50mm（50mm standard lens），浅景深，焦点锁定在眼睛。
运镜：固定。
动作：@艾莉 身体前倾，双手撑在 @操作台 边缘，指关节发白。
台词：艾莉（声音发哑）："……你他妈倒是给个信号啊。"；省略号处停 0.5 秒，喉咙干涩吞咽；尾音咬字用力但气息不足，嘴唇微颤。
光线：@培养皿 蓝光短暂亮起又熄灭，照亮艾莉下巴后消失。
```

不推荐（旧版拆分格式——禁止使用）：

```text
镜头目的：确认空间异常。
视角/景别：中景，保留人物、16 号、18 号和中间旧墙的空间关系。
机位：人物正前方略低机位，墙面占据画面后半部。
焦段/光圈：35mm 自然电影镜头（35mm cinematic lens），中浅景深。
运镜：缓慢前推到墙面。
主体动作：@阿远 站在 @青槐路旧墙 前……（台词和标点混入动作）
环境细节：墙面潮湿起皮，门牌边缘有雨水滑落。
构图/取景：人物在画面左侧，16 号和18号形成左右对照，中间旧墙留出空缺感。
焦点/景深：焦点从手机导航切到墙面门牌，中浅景深保留空间关系。（景深与焦段/光圈字段重复）
台词：无。
标点节奏重点：无台词，停顿 1 秒，呼吸变浅。
微表情/身体锚点：眉心收紧；手指停在手机屏幕上；肩膀微微僵住。
声音：细雨声、远处车辆经过声、手机导航提示音停止。
光线：街灯冷光照出墙面潮湿纹理，远处店铺暖光只落在地面边缘。
【关键约束】
有音效，无音乐，无字幕。
```

原因：字段过多，景深在两处重复，台词与动作混在一起不利于语音合成。常见错误：画面字段漏写“机位”二字；应写“正面平视机位”“侧面略低机位”，不要只写“正面平视”。
## 光线字段示例

推荐：
```text
光线：@手机 屏幕亮起蓝光，只照亮手指、屏幕边缘雨点和阿远下巴。
```

推荐：
```text
光线：@黑伞手电 的冷白光扫过墙面，短暂照亮 @钥匙 和半截 @17号旧门牌。
```

推荐：
```text
光线：404 门缝暖光变宽，铺到 @热粥碗 和门口冷地砖上。
```

不推荐：
```text
光线：本镜头新增手机蓝光，偏离全局光线。
```

原因：这是技术说明，不是画面事实。

---

## 标点节奏转译示例

逗号：
```text
短暂停顿或换气，表现为吸气、嘴唇微停、眼神轻微偏移。
```

句号：
```text
说完后停住，嘴唇闭合，下颌轻收，眼神停留。
```

问号：
```text
说完后看向对方或门缝，眼神寻找反应，停半秒。
```

省略号：
```text
中间停 0.5 秒，喉咙吞咽，呼吸卡住，嘴唇微张。
```

破折号：
```text
前半句中断，角色换气、动作停住或眼神突然断开。
```

感叹号：
```text
只允许表现为音量、呼吸或身体紧绷变化，禁止默认失控喊叫。
```

禁止只写：
```text
句号落地。
尾音压低。
问号上扬。
情绪落地。
声音发虚。
```
