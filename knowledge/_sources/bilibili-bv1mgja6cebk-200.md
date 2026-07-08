---
title: "成立两年半，估值200亿，千寻智能凭什么？"
type: source
date_created: 2026-07-08
last_updated: 2026-07-08
source_urls:
  - https://www.bilibili.com/video/BV1mgja6CEbK
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-08-bilibili-bv1mgja6cebk-200.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# 成立两年半，估值200亿，千寻智能凭什么？

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. Synthesized in [[_syntheses/bilibili-qianxun-intelligence-deep-dive-2026-07-08|千寻智能具身智能公司视频深度调研]].

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1mgja6CEbK |
| BV / video id | `BV1mgja6CEbK` |
| Author | 小水_VC看具身智能 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-08-bilibili-bv1mgja6cebk-200.json` |

## Transcript Excerpt

进行核心技术的深度拆解。千寻智能的技术全景可以用一个三从对战来概括。最底层是硬件本体层，就是墨子一。这个层面不仅仅是造出机器人那么简单，它承担了两个角色。一个呢是作为交付载体，第二个是作为最重要的数据采集和物理交互平台。每个关节都集成了力传感器，支持细腻的力控和防倾覆机制，能够实现 S 弯行走、零空间二十六关节联动和低时延摇操作。自研的一体化关节是目前全球功率密度最高的方案之一，扭距大、体积小、成本可控。中间层呢是数据引擎，也就是全模态数据采集和预训练管线。这是千寻智能所有技术壁垒中最难以复制的一层。数据来源被分成了三个部分，大约70%来自互联网上的视频，包括 YouTube 上普通人拍的家务视频、烹饪视频、DIY 视频。这些视频包含了海量的物理交互场景，机器人从中学到的是世界模型层面的常识，比如水多了会溢，堆叠多个物体要小心平衡。那大约20%呢来自真实的遥操作数据。由专业的操作员远程操控机器人完成特定任务，把人类的高级操作经验转化成模型可以学习的样本。而大约10%呢来自强化学习中的自主探索。机器人在安全的沙盒环境中自己试错，自己找，自己找出最优策略。这当中最惊艳的是千寻自主研发的全套采集设备，主要包括三个系列，分别是 HRPI 外骨骼系统、乌米轻量化手持设备和 UDAS 系列。那 HRPI 3.0的成本可以降到传统真机遥采方案。那 HRPI 3.0的版本。那 HRPI 3.0的成本可以降到传统真机遥采集方案的5%。来数据精度可以达到95%。Omi 设备呢支持工人在正常作业的同时，边干活边采集，混合10%的真机遥采数据训练后，模型效果远远超过预期。那 UDAS 系列已经迭代到了3.0版本，脱离了外骨骼结构，适配全国的开放场景。公司已经在全国100多个城市建立了数据采集网络，近千台的设备持续运行。将人类操作过程转化为训练数据，公司累计获取了超过20万小时的多类型真实交互数据，预计2026年总量将突破100万小时。在成本效率上，通过自研设备把整体的采集成本降低了大约90%，人均有效采集时长呢提升了200%，专家干预频率降低了60%。形成了一个高吞吐低成本的数据飞轮。那这里有一个行业背景值得展开，巨深智能领域普遍面临异构数据难以互通、采集成本飙升的痛点。保守估计当前已经有数据量与所需数据量之间至少还差两个数量级。以智元机器人数据采集工厂使用的远征 AR 机器人为例。设备售价约20万元，年折旧约6.67万元，叠加人工费用、场地运维和专家干预成本，每小时有效数据采集成本高达了数百元甚至上千元。而千寻的 HRPI 3.0外骨骼采集系统呢，可以将硬件成本降到传统真机遥采集方案的5%以内。欧米设备甚至支持工人边干活边采集，把数据采集融合到日常工作中，几乎实现了零边际成本。这不仅大幅降低了数据飞轮的燃料成本，也为公司未来向中小企业提供低成本、标准化的预训练模型加按需微调服务打下了扎实的基础。这种数据策略背后呢，是一套非常反直觉的哲学，叫脏数据范式。传统的数据采集方法是怎么做的呢？工程师写好脚本，操作员按照精确的流程重复执行，质控人员把失败的尝试、歪斜的抓取、临时改变主意的操作通通过滤掉。保留干净的演示样本这种数据在实验室里效果很好，模型收敛的很快。但有一个致命的副作用，就是到了真实世界里，模型一旦遇到光线变化、物体偏移、意料之外的干扰，就立刻宕机。因为他从来没有在数据里见过这些情况，行业普遍陷入了干净数据泛化幻觉的陷阱。千寻智能反其道而行之，他们只给操作员一个高层目标，比如把厨房清理干净。我预设固定流程，甚至允许操作中有即兴发挥、失败和纠错。这样采集到的数据天然包含了真实世界中必然存在的杂乱和不确定性。团队在技术博客中甚至直言，干净的数据是伟大机器人基础模型的敌人。这个反直觉的实验结果是什么呢？千寻智能在开源的 Spirit V 1.5技术文档中展示了一个关键实验。相比于用干净脚本数据预训练的对照组，使用了更多样化更脏的数据预训练的模型，在新任务上的适配效率提升了大约40验证误差随着数据规模的扩大持续下降，完美契合了 Scaling Log。换句话就是说，多样性比纯净性更重要，真实比完美更重要。这种哲学深刻地影响着千寻智能整个技术路线的选择。也就是说，不是要过滤掉失败，而是要从失败中学习恢复机制和应对策略。不过高阳的策略是用更少的算力实现更多的泛化，尽...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-08-bilibili-bv1mgja6cebk-200.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[_syntheses/bilibili-qianxun-intelligence-deep-dive-2026-07-08|千寻智能具身智能公司视频深度调研]]
- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
