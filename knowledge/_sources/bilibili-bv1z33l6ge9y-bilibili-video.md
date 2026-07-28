---
title: "开源机器人与机械臂成套方案选型调研"
type: source
date_created: 2026-07-28
last_updated: 2026-07-28
source_urls:
  - https://www.bilibili.com/video/BV1z33L6gE9y
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-28-bilibili-bv1z33l6ge9y-bilibili-video.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# 开源机器人与机械臂成套方案选型调研

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1z33L6gE9y |
| BV / video id | `BV1z33L6gE9y` |
| Author | 啥也不会的小黑黑 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-28-bilibili-bv1z33l6ge9y-bilibili-video.json` |

## Transcript Excerpt

好的，废话不多说，咱们直接进入今天的深度解析。今天我们来聊聊当下热度爆表的开源机器人领域。说实话，现在这个赛道里满天飞的都是各种新概念 PPT 还有铺天盖地的炒作。那么咱们今天就来拨开迷雾，实实在在的看一看。作为一名开发者或者创客，你现在到底能亲手造出个什么东西？或者说能买到什么靠谱的硬件？为了理清这个复杂的生态，今天咱们一步步来。首先重新定义一下什么叫完全开源，接着看看机器人的选型决策树，然后我们会一路从极具性价比的桌面机械臂，聊到移动双臂平台，再到最前沿的人形机器人。最后，当然还要揭秘驱动它们运转的隐形大脑，也就是软件与数据引擎。好的，第一部分咱们先来定义一下什么是真正的完全开源。说实话，咱们得先面对一个行业里挺残酷的现实。很多项目在代码库里贴个开源的标签，或者发篇特别酷炫的论文，对吧？但这绝对不意味着你真能在自己家里把它给造出来。一个真正靠谱，能让你完整复现的开源闭环系统，必须得在咱普通人或者小团队掏得起钱的预算内搞定这5个维度。你看，从最底层的硬件 bom 表，也就是明确告诉你该去买哪颗螺丝钉。一路干到最顶层的模型部署工具链，真的是缺一不可，少任何一环，你绝对会卡在半山腰。另外，咱们必须把纯粹的软件框架，或者那些用于测试的数据集，跟物理硬件严格区分开来。具身智能，重点在具身两个字。它得跟真实的物理世界去互动啊。要是你连个能跑代码的物理躯体都没有，那你哪怕下到了地球上最牛的 AI 基础模型，它也只不过是缸中之脑，完全没用。接下来进入第二部分，机器人选型决策树。既然弄懂了刚才说的成套标准，这就有意思了。根据你到底想干嘛，现在的开源生态其实给你画出了一条极其清晰的选择路线。而且这个跨度简直大的离谱。你看，从只要一两千块钱就能搞定的桌面级机械臂入门套件，一路狂飙到将近30万人民币的商业级人形机器人。这完全取决于你是想随便花点小钱验证的算法，还是硬核到需要工业级的极高可靠性。那么咱们进入第三部分，先来看看对普通人最友好的，极具性比的桌面机械臂。桌面级产品绝对是个人创客和学生党的地基，这就很有意思了，它衍生出了两种完全不一样的画风。一边呢，是预算大概1600块钱左右的 SO 101。你看它那种层层叠叠的3D打印件，散发着一股纯粹的 DIY 极客硬核风。而另一边呢，是大概要36000块的 AGLX PIPER，那种高度抛光、开箱即用的质感，一看就是商业成品。咱们重点聊聊这个简直称得上颠覆性的 SO 101。它是目前 Hugging Face 旗下 Lil' Robotic 生态疯狂打 call 的旗舰级低成本机械臂。这东西神在哪？您只需要花1600块钱就能拿到一个彻头彻尾的闭环系统。你自己买零件，打印，拼装，然后系统帮你自动标定。接着你用手里这个轻量级的主手柄去实时操控干活的机械臂，也就是 Leader 和 Follower 模式，用来采集数据。最后连模型训练软件都给你备齐了，真的一站式搞定！当然了，要是你对舵机的扭距性能或者对开源生态有那种比较传统的执念，那 Quadcopter One 一点绝对是个完美的备胎。它用了学术界老大哥级别的 Dynamixel 舵机，虽然这会让你的钱包多出几千块钱的血，但它能无缝插进传统 Robot Store 机器人科研工作流里，而且整体价格依然在咱们普通人咬咬牙能接受的范围内。还有一个相当棒的进阶选项，就是 Seeed 体系下的 Rebot Arm B61E。这玩意用料更猛，上了钣金件，所以能扛得起1.5~2.5公斤的重物。而且跟刚才说的一样，对 Leap Motion 框架也是开箱即用，原生态支持。好的，桌面上的小家伙聊完了。第四部分，咱们给这些机器人装上轮子，再加一条胳膊，看看移动与双臂平台。既然桌面方案都这么熟了，那咱们就别局限在桌子上了。xLife Robot 这个项目真的是 DIY 圈子里的一次大暴走。他脑洞大开的把咱们刚聊过的两台低成本 SO 1100机械臂，直接给安在了一个 Leqi 移动底盘上。你敢信吗？只要大概4500块钱，再加上你自己的这双手，你就能在客厅里整出一套能到处溜达、干家务的双臂移动机器人。咱们格局再打开一点，看看顶尖实验室都在玩什么？ALAHOR 项目绝对是目前静态上臂摇操作领域天花板级别的存在。不过先给大家泼盆冷水，为了追求那种变态级的精度，它要求你必须配上贵的吓人的 V...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-28-bilibili-bv1z33l6ge9y-bilibili-video.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.
- Completed synthesis: [[_syntheses/bilibili-open-robot-arm-platform-selection-deep-dive-2026-07-28|开源机器人与机械臂成套方案选型视频深度调研]].

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
