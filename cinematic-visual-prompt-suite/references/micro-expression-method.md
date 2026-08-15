来源：https://acnqrreajo27.feishu.cn/wiki/ExnwwzV6Ii7KStkeaMLc2wgFnth

# AI 视频 Prompt 的“减法哲学”：微表情写法总结

来源：网页完整截图内容 + 已整理的微表情词库文档

## 1. 核心结论

做 AI 视频时，不要让 AI “全力表演情绪”。  
越是直接写大情绪，越容易生成假笑、僵脸、油腻表演、提线木偶感。

真正好用的原则是：

```text
少即是多，动即是稳。
```

具体来说：

- 控制强度：不要让 AI 把情绪拉满，要限制它的发挥幅度。
- 动作归因：不要直接“摆出表情”，要用身体动作和视线变化“带出表情”。
- 时间顺序：不要只写一个结果，要写情绪如何发生、变化、结束。

## 2. 为什么 AI 表情容易假

现在的视频模型已经很少出现明显的面部崩坏，但它们常见的问题是：

- 笑容太完美，像广告模特。
- 表情从第 1 秒到第 5 秒强度不变。
- 嘴角、眼睛、眉毛像被锁死在一个固定角度。
- 人物虽然有表情，但缺少呼吸、犹豫、停顿和回落。
- 情绪像被“摆”出来，而不是被动作自然带出来。

比如写：

```text
A girl laughing loudly.
```

AI 可能会生成一个非常完整、强度 100% 的笑容，但笑容会维持太久，纹丝不动。真实的大笑会有呼吸起伏、胸腔变化、笑容回落、眼睛弯度变化。缺少这些变化，观众会立刻觉得这是 AI 视频。

因此，AI 默认的“最大值”不等于真实感，反而会带来廉价的摆拍感。

## 3. 方法一：控制情绪强度

### 3.1 原理

不要写满格情绪，要用“克制感”替代“稳定性”。

错误写法：

```text
Beautiful woman smiling happily at the camera.
```

问题：

AI 会理解为“漂亮女人对着镜头开心地笑”，结果容易像拍广告的模特：笑容固定、没有变化、没有生活气息。

正确写法：

```text
A relaxed woman, faint smile playing on lips, soft gaze, facial muscles relaxed, not posing.
```

中文理解：

一个放松的女人，嘴角带着淡淡笑意，目光柔和，面部肌肉放松，没有摆拍感。

### 3.2 可复制公式

```text
[人物描述], 脸上带着[微弱程度词]的[情绪], 嘴角[肌肉微动], 眼神[眼神状态], 面部肌肉放松，没有摆拍感，呼吸感，真实自然。
```

英文公式：

```text
[Character description], with a [faint/subtle/barely visible/suppressed] [emotion], [mouth detail], [eye detail], facial muscles relaxed, not posing, breathing naturally, realistic and candid.
```

### 3.3 推荐词库

微弱程度词：

- faint：微弱的
- subtle：微妙的
- barely visible：几乎看不见的
- suppressed：克制的

情绪词：

- smile：笑
- frown：皱眉
- smirk：得意笑
- worry：担忧

肌肉细节：

- slightly turned up：轻微上扬
- twitching：轻微抽动
- softened：变柔和

松弛感：

- relaxed：放松
- breathing naturally：自然呼吸
- candid：抓拍感
- not posing：没有摆拍感

### 3.4 适用场景

用于防止表情油腻、僵硬、太像广告片。  
尤其适合口播、生活感镜头、人物特写、情绪氛围片。

## 4. 方法二：给微表情一个发生原因

### 4.1 原理

真实人类的表情通常不是独立存在的，而是身体动作的副产品。

如果只写：

```text
Shy woman.
```

AI 容易生成一个直勾勾盯着镜头、脸红、扭捏的人物。这个结果会很像被线牵着脸皮动，因为“害羞”没有动作来源。

在视频生成中：

```text
身体微动 + 视线转移 = 真实微表情
```

### 4.2 错误写法

```text
The woman is shy and looking directly at the camera. She smiles shyly at the viewer. She maintains eye contact the whole time. Static head, just facial expression changing.
```

问题：

虽然写了 shy，但又要求一直看镜头、头部静止、只有面部表情变化。AI 会把“害羞”理解成静态扭捏，人物会像机械一样对着观众挤表情。

### 4.3 正确写法

```text
She feels shy. She immediately lowers her head to avoid eye contact. Her eyes look down and dart to the side nervously. She tucks her chin in and bites her lower lip gently. She cannot look at the camera.
```

中文理解：

她感到害羞，立刻低头避开视线。眼睛向下看，又紧张地瞥向旁边。她收下巴，轻轻咬下唇，不敢看镜头。

### 4.4 为什么这样更好

这里不是只写“害羞”，而是给害羞安排了身体动作：

- lowers her head：低头
- avoids eye contact：避开视线
- eyes look down：眼睛向下看
- dart to the side：眼神向旁边游移
- tucks her chin in：收下巴
- bites her lower lip：咬下唇

AI 会知道人物为什么低头、为什么躲闪。这样生成的动作更羞怯、更柔和，而不是机械地低头。

### 4.5 可复制公式

```text
人物感到[情绪]。她/他立刻[身体动作]，以[动作目的]。眼神[视线变化]，同时[嘴部/头部/手部动作]。最终，脸上自然浮现出[微表情]。
```

英文公式：

```text
The character feels [emotion]. They immediately [body action] to [reason/purpose]. Their eyes [gaze movement], while [mouth/head/hand action]. As a result, a subtle [expression] appears naturally.
```

### 4.6 填空词库

手部/头部动作：

- scratching back of head：挠后脑勺
- tucking hair behind ear：挽头发
- rubbing eyes：揉眼睛
- looking down at phone：低头看手机
- lowering head：低头
- tucking chin in：收下巴

视线移动：

- avoiding eye contact：避开视线
- eyes darting sideways：眼神游移
- looking down shyly：害羞地低头
- glancing sideways：向旁边瞥
- shifting gaze：转移视线

引发的表情：

- nervous smile：紧张的笑
- relieved look：释然的表情
- confused frown：困惑的皱眉
- faint smile：淡淡的笑
- subtle worry：轻微担忧

### 4.7 适用场景

用于防止“提线木偶感”。  
让人物不再直勾勾盯着镜头，而是拥有肢体语言和动作动机。

核心逻辑：

```text
动作在前，表情在后。
```

## 5. 方法三：给情绪加入时间顺序

### 5.1 原理

图片是静态的，视频是流动的。  
如果只给视频 AI 一个静态描述，比如“他很伤心”，AI 不知道第 1 秒和第 5 秒有什么区别，于是只能让人物循环保持同一个表情。

微表情的本质是：

```text
Change（变化）
```

所以，视频 Prompt 必须写入时间轴。

### 5.2 通用时序公式

```text
Start（起始状态） -> Transition（变化动作） -> End（最终微表情）
```

中文填空公式：

```text
视频开始时，人物处于[起始状态：平静/发呆/严肃]。然后，[发生了触发动作/变化]，眼神[产生了反应]。最后，脸上慢慢浮现出[结束状态：情绪]。
```

英文填空公式：

```text
The video starts with the character in a [starting state]. Then, [trigger/action happens], and the eyes [reaction]. Finally, a [final expression] slowly forms on the face.
```

### 5.3 示例：从严肃到释然

```text
The video starts with the man maintaining a serious, stoic expression, gazing into the distance. Then, he closes his eyes slowly and takes a deep visible breath, shoulders dropping. Finally, as he opens his eyes again, a faint, relieved smile slowly forms on his lips. Subtle movement of hair in the wind.
```

中文理解：

视频开始时，男人保持严肃、坚忍的表情，望向远处。然后，他慢慢闭上眼，深深吸了一口可见的气，肩膀下沉。最后，当他再次睁开眼时，一个微弱、释然的笑慢慢出现在嘴角。头发在风中轻微飘动。

### 5.4 这个例子的三段结构

第一阶段 Start：

```text
serious, stoic expression, gazing into the distance
```

人物严肃、坚忍、望向远处，建立起始情绪。

第二阶段 Transition：

```text
closes his eyes slowly and takes a deep visible breath, shoulders dropping
```

闭眼、深呼吸、肩膀下沉是关键动作，它切断了严肃情绪，为转变做铺垫。

第三阶段 End：

```text
a faint, relieved smile slowly forms on his lips
```

最后的微笑经过前面的深呼吸才显得有血有肉，不像假笑。

### 5.5 填空词库

状态 A：

- neutral expression：平静表情
- sleeping face：睡脸
- bored look：无聊
- serious expression：严肃表情
- stoic expression：坚忍克制的表情
- absent-minded look：心不在焉

触发动作：

- eyebrows suddenly raise：眉毛突然上挑
- pupils dilate：瞳孔放大
- takes a deep breath：深呼吸
- closes eyes slowly：慢慢闭眼
- shoulders dropping：肩膀下沉
- gaze shifts away：视线移开
- lowers head：低头

状态 B：

- warm smile：温暖微笑
- shocked expression：震惊
- tear falling：眼泪落下
- relieved smile：释然微笑
- faint smile：微弱的笑
- confused frown：困惑皱眉

### 5.6 适用场景

用于生成有剧情感的视频片段，防止画面静止不动。  
特别适合：

- 情绪转折
- 回忆片段
- 人物特写
- 电影感镜头
- 从悲伤到释然
- 从平静到惊讶
- 从期待到失落

核心逻辑：

```text
起始状态 -> 触发动作 -> 最终结果
```

## 6. 三个方法的合并写法

最稳的写法不是单独使用某一个方法，而是把三者合在一起：

```text
强度控制 + 动作归因 + 时间顺序
```

完整公式：

```text
视频开始时，人物处于[起始状态]，面部肌肉[松弛/克制]。然后，因为[触发原因]，人物做出[身体动作]，眼神[视线变化]，嘴部[微动作]。最后，一个[微弱程度词]的[最终情绪]慢慢浮现在脸上。整体动作克制、真实、自然，没有摆拍感。
```

英文完整公式：

```text
The video starts with the character in a [starting state], facial muscles relaxed and restrained. Then, because of [trigger/reason], the character [body action], eyes [gaze movement], and mouth [subtle mouth movement]. Finally, a [faint/subtle/barely visible/suppressed] [final emotion] slowly forms on the face. The movement is restrained, realistic, natural, and not posed.
```

示例：

```text
The video starts with the woman sitting quietly by the window, facial muscles relaxed and not posing. Then, after hearing something unexpected off-camera, she lowers her head slightly and avoids eye contact. Her eyes look down and dart to the side, while she gently bites her lower lip. Finally, a barely visible nervous smile slowly forms on her lips. The movement is restrained, realistic, natural, and breathing softly.
```

中文理解：

视频开始时，女人安静地坐在窗边，面部肌肉放松，没有摆拍感。然后，听到镜头外某个意外声音后，她轻轻低头并避开视线。眼睛向下看，又向旁边游移，同时轻咬下唇。最后，一个几乎看不见的紧张微笑慢慢出现在嘴角。整体动作克制、真实、自然，有轻微呼吸感。

## 7. 错误写法改写对照

### 7.1 开心

错误写法：

```text
The woman is drinking coffee and smiling happily. She is enjoying the morning.
```

问题：

“smiling happily” 是结论，AI 找不到动作着力点，只能让人物对镜头傻笑或僵硬地拿杯子。

改写：

```text
Subtle motion. The woman lifts the cup slightly to smell the aroma. Her eyes close gently for a second. Then she blows on the steam. She does not drink yet. The steam moves naturally. Her facial muscles relax, showing a sense of comfort.
```

核心：

```text
smell the aroma -> eyes close -> blows on steam -> comfort appears
```

### 7.2 害羞

错误写法：

```text
The woman is shy and looking directly at the camera. She smiles shyly at the viewer.
```

问题：

害羞却一直看镜头，动作逻辑冲突，容易生成僵硬扭捏。

改写：

```text
She feels shy. She immediately lowers her head to avoid eye contact. Her eyes look down and dart to the side nervously. She tucks her chin in and bites her lower lip gently. She cannot look at the camera.
```

核心：

```text
shy -> lowers head -> avoids eye contact -> bites lower lip
```

### 7.3 释然

错误写法：

```text
The man smiles with relief.
```

问题：

只写最终表情，没有过程，微笑会显得像假笑。

改写：

```text
The video starts with the man maintaining a serious, stoic expression, gazing into the distance. Then, he closes his eyes slowly and takes a deep visible breath, shoulders dropping. Finally, as he opens his eyes again, a faint, relieved smile slowly forms on his lips.
```

核心：

```text
serious -> closes eyes -> deep breath -> shoulders drop -> relieved smile
```

## 8. 直接可复制的 Prompt 模板

### 8.1 中文模板

```text
视频开始时，人物处于[起始状态：平静/发呆/严肃/疲惫]，面部肌肉放松，没有摆拍感。然后，因为[触发原因]，人物[身体微动作]，眼神[视线变化]，嘴部[细微动作]。最后，一个[微弱程度词]的[最终情绪]慢慢浮现在脸上。整体动作克制、真实、自然，有轻微呼吸感，避免夸张表情和僵硬假笑。
```

### 8.2 英文模板

```text
The video starts with the character in a [neutral/absent-minded/serious/tired] state, facial muscles relaxed and not posing. Then, because of [trigger], the character [body micro-action], eyes [gaze movement], and mouth [subtle mouth movement]. Finally, a [faint/subtle/barely visible/suppressed] [final emotion] slowly forms on the face. The movement is restrained, realistic, natural, with soft breathing, avoiding exaggerated expressions and stiff fake smiles.
```

## 9. 最终检查清单

写完视频 Prompt 后，用这 9 个问题检查：

- 我是不是只写了 happy、sad、shy、angry 这种大情绪？
- 有没有用 faint、subtle、barely visible、suppressed 控制强度？
- 有没有避免让表情从第 1 秒到第 5 秒一成不变？
- 有没有写出起始状态、变化动作、最终结果？
- 有没有给表情安排发生原因？
- 有没有用身体动作带出表情，而不是直接摆表情？
- 有没有写眼神变化，而不是一直盯着镜头？
- 有没有加入呼吸、肩膀、低头、闭眼、咬唇等物理动作？
- 有没有避免 exaggerated expression、forced smile、stiff face、not posing？

## 10. 一句话记忆

```text
不要写“他很开心”，要写“他为什么开心、身体先怎么动、眼神怎么变、笑意如何慢慢出现”。
```

视频 Prompt 的关键不是堆情绪词，而是做导演：

```text
少给情绪结论，多给动作过程。
```

