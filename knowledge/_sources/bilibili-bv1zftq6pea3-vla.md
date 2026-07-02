---
title: "VLA&世界模型数据基建：从原始传感器信号到可用训练资产"
type: source
date_created: 2026-07-02
last_updated: 2026-07-02
source_urls:
  - https://www.bilibili.com/video/BV1ZFTq6pEA3
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-02-bilibili-bv1zftq6pea3-vla.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: draft
---

# VLA&世界模型数据基建：从原始传感器信号到可用训练资产

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1ZFTq6pEA3 |
| BV / video id | `BV1ZFTq6pEA3` |
| Author | 失控的PM |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-02-bilibili-bv1zftq6pea3-vla.json` |

## Transcript Excerpt

哈喽，大家好，我是司马。今天呢，我将详细拆解一下，Ego 多模态巨声数据采集与训练数据生成链路的一个 sop。 这份 sop 的核心宗旨非常的明确。巨神智能数据的本质啊，不仅仅是说拍下多视角的这个视频就够了，更是要建立从 observation 到 action 的严格映射。啊，接下来呢，我会分15个阶段。啊，就是一部高标准的工业化数据生产线。我们来探讨一下将如何把原始的信号转化为 VLA 和世界模型真正可用的。数据资产。第一个阶段呢，也就是链路的一个起点。定义输入和输出的空间。我们绝对不能仅仅满足于采集视频。这对于 VOA 或者说模仿学习来说是不够的。我们必须要明确 observation 的这个空间。就是模型看到了什么。和这个 action 空间，模型该怎么做？那 action 空间包括了关节角、末端位姿以及夹爪的状态。同时呢，还需要定义 language 的空间和能判定采集是否合格的这个质量标准，对吧？也就是 quality 啊。第二步呢是设备初始化。大家都知道啊，传感器在运转或者说颠簸后啊，容易出现微小的定位漂移。因此呢，我们在这个硬件设计的时候，正式录制的时候呢，要加一道在线健康检查的一个机制。除了加载静态的这个参数啊，我们必须要实时的去检测 camera 和 imu 的时间戳偏移啊。是否在安全的一个阈值以内？同投影的误差呢？是否达标？一旦检测到这个 VIO 残差过大呀，系统呢就要立即去报警。这极大避免了，采了一天以后啊，你会发现这个数据全部是废掉的，灾难性后果。所以我们要提前去干预。第三步呢，是采集数据阶段的核心动作啊。就是同步流。我们经常会看到一些团队收到一堆清晰的视频，但 action 数据频率对不上的时候，或者说压根就没有存在要操作的具体控制量。但在这套 sop 下呢，就 vision 啊、 m u r audio 啊、action 啊、command 啊，和这个 robot state 啊，必须汇总到同一个 sink buffer。之中。左边的多模态呢，和右边的控制量啊，是同等重要的。不要丢掉操作员踩下的任何一个按键事件。这些都是后处理的长序列分割点。第四步是现场操作员的这个视角。我们在监控面板上，不仅要能确定这个画面和流啊，有没有断啊。左流右流，更引入了非常有价值的触发式保护这个机制。就像这个行车记录仪的这个碰撞锁存，对吧？系统在后台呢，保持滚动的一个缓存。只有当人操作完一段漂亮的轨迹啊，觉得这次任务呢非常的完美，按下这个保存键，系统呢才将过去几分钟的 buffer 呢。固化在这个落盘。这一招呢，能够剔除掉海量的无效发呆数据和试错的一个数据，可以大幅度降低后续的带宽和标注的一个成本。所以这一个是我们一定要去做的一个机制。第五步呢，就是数据落盘。落盘呢，绝对不是说简单粗暴的去保存一个 MP4的一个文件啊。那 mp4的文件对大模型其实是没用的。每一个采集任务呢，都必须结构化归档为一个 episode 的目录啊，就这个目录。左边呢是我们推荐的一个目录树。这里面呢不仅有原始的观察数据，还单独剥离了这个 action 机器人状态和当时的这个 calibration 也就是个这个标定文件。这一步呢，是把一次物理的交互呢，封印成了一个具备溯源能力的一个数据资产。那阶段六呢，就是落盘以后啊，数据即刻进入并行的机器质检的这个阶段。这不能靠人工的肉眼去查啊。我们从左到右呢，设计了这个三大核心质检的一个维度。一是纯视觉的 RGB 清晰度与。曝光啊。二是呢，这个左右目的与这个 imu 之间的微秒级同步的一个验证。三是呢，最容易被忽略的 action 连贯性。也就是动作的连贯性。如果机械臂数据跳变了，视频再清晰呢，其实也没有用。这三条线的结果呢，最终汇聚成了一份结构化的。质量报告。第七步呢，就是深度的计算。一般实施的深度呢，只会用于现场的一个预览。那真正的预练啊，深度必须放在离线集群去计算。在这条管线里面，最核心的一环呢，不是说算出深度的一个矩阵，而是生成这个 confidence mask 啊，就是置信度的这个掩码。因为抓东西的时候呢，经常遇到金属的反光啊，透明的玻璃啊，立体匹配在这些地方算出来的深度或者说距离呢，它是错的。那大模型如果学会了这些错误的数据啊，机械臂呢就会把杯子给捏碎掉。所以呢，我们不仅要深度啊，更要知道哪个区域的深度呢...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-02-bilibili-bv1zftq6pea3-vla.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
