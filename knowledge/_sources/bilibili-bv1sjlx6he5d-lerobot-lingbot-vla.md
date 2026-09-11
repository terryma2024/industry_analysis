---
title: "速通具身智能毕业论文！LeRobot+LingBot-VLA训推全流程"
type: source
date_created: 2026-09-11
last_updated: 2026-09-11
source_urls:
  - https://www.bilibili.com/video/BV1sjLx6HE5D
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-09-11-bilibili-bv1sjlx6he5d-lerobot-lingbot-vla.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# 速通具身智能毕业论文！LeRobot+LingBot-VLA训推全流程

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1sjLx6HE5D |
| BV / video id | `BV1sjLx6HE5D` |
| Author | 同济子豪兄 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-09-11-bilibili-bv1sjlx6he5d-lerobot-lingbot-vla.json` |

## Transcript Excerpt

大家好，我是同济子豪兄。这期视频是具身智能 VLA 的保姆级教程。我将用 SORM 101开源机械臂和 LeapRobot 框架，结合蚂蚁凌波最新开源的具身智能基座大模型 Lingbot VLA。 带大家实现一个最简单的 VLA 样例场景，机械臂主动和人握手，碳硅之握。人类伸手它就伸手，人类抽手它也抽手，还会和你优雅的挽留贴贴。我和刘月写了一个详细的，The Robot 保姆级飞书知识库，涵盖模仿学习和 VLA 的全部流程，包括购买机械臂套件、组装、校准机械臂。获取端口号、连接摄像头、摇操作、录制视教数据集、选择 VOA 模型、后训练微调、仿真验证、开环验证、真机推理。你可以用 Mac 电脑、4090主机。英伟达 Jetson Soar。 英伟达 DGL Spark 这些端侧算力，本地推理 VLA 模型，让机械臂真的动起来干活。全套流程使用了 Robot 框架，兼容 ACT Small VLA派零，Linkbot VLA 这些主流 VLA 模型。这个飞书知识库也被了 Robert 官方 GitHub 推荐。那我们现在开始吧！最近，Figer AI 人形机器人分拣快递的直播火爆全网。机器人的任务是把所有传送带上的包裹整理成标签朝下。它在30多个小时自主整理了几万件包裹，没有任何遥控和远程操作。就算遇到包裹堵塞、重叠、干扰，它也能像人一样从容丝滑完成任务，仿佛注入了灵魂。我最近两年也见过不少机器人自主干活的案例。从简单的抓取放置、收纳物品、夹小龙虾下锅，到柔性物体操作，比如叠毛巾。叠衣服、把笔收纳到笔筒里、再擦一擦桌子。再到双臂协作的长序列任务。这些 demo 虽然仍然有点简陋，甚至智障，但它们全都是机器人自主推理运行，而且具备主动纠错、抵抗干扰的能力。具身智能解锁了 AI 接管物理世界，机器人操作万物的无限想象。具身智能分为小脑和大脑两个流派。运动控制小脑掌管机器人的下半身，也就是双腿。比如宇树春晚的节目，机器人做出各种酷炫动作，还能自主稳定平衡。机器人马拉松速度打破人类半马记录，这些都是小脑。可以看我之前做的宇树春晚和亦庄马拉松的几期视频。操作物体的大脑掌管机器人的上半身，也就是双臂。比如我们现在说的机器人干活，大脑又分为两个流派，视觉语言动作大模型 VLA。和世界模型 world model 两派的研究者都在疯狂烧钱。VLA 似乎更成熟一些，刚刚那些干活的 demo 都是用 VLA 实现的。输入文字指令和摄像头画面，VLA 模型实时输出机器人每个关节下一步的位置。各大具身智能厂商都开源了自己的 VLA 大模型。代表算法有 ACT Small VLA 派零、 Lingbot VLA 世界模型今年新出了一个世界行动模型，World Action Model。 大有一统天下的趋势。代表算法是蚂蚁凌波的 Lingbot AA 和英伟达的 DreamZero 所以像蚂蚁凌波这样的具身智能公司，同时压住了 VRA 和世界模型。 VLA 和大语言模型一样，也同样出现了 scaling law 智能涌现的现象。Lingbot VLA 官网有一张图反映了预训练数据越多，基座 VLA 模型就越智能，后训练微调之后，下游任务的成功率就越高，而且尚未达到饱和瓶颈。预训练就好比 K12 基础教育，告诉 AI 物理世界的鲜艳知识和基本规律。预训练的数据越多，质量越高，基座模型的地基就越稳固。这就是为什么具身本体公司都在砸巨资建数采基地。后训练微调就好比大学和职业教育，告诉 AI 每种活具体该怎么干。灵猫特 VLA 的预训练基座模型就是用9种本体，2万个小时的高质量真机数据训练而成的。乐聚夸父4 Pro 北京国际中心开源的青龙、星海图轮式双臂 R1 Pro 瑞尔曼双臂升降机器人 RS2、智元精灵 G1。松灵 AGLX 方舟无限 Lift 2、星海图 R1 Lite 和双臂弗兰卡。我们之前参加黑客松巅峰赛做的吹米机械臂就是用的松灵的臂。叠衣服用的是星海图的笔，都是非常常见的本体。但作为一个穷学生，我只能买得起三 d 打印开源机械臂，SORM101。我和刘月在同济 FabLab 创客空间组装了一下午。包含一条主臂和一条从臂，每条臂有5个关节自由度和一个夹爪自由度。从臂有一台腕部相机，总成本2000多块钱，非常便宜。跟西地科技的客服说是子豪兄粉丝，还能薅到代金券。按照...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-09-11-bilibili-bv1sjlx6he5d-lerobot-lingbot-vla.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
