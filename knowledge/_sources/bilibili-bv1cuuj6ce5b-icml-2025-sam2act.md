---
title: "【ICML 2025】🎓SAM2Act：视觉基础模型 × 记忆架构的机器人操作"
type: source
date_created: 2026-08-11
last_updated: 2026-08-11
source_urls:
  - https://www.bilibili.com/video/BV1Cuuj6CE5b
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-08-11-bilibili-bv1cuuj6ce5b-icml-2025-sam2act.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# 【ICML 2025】🎓SAM2Act：视觉基础模型 × 记忆架构的机器人操作

> [!summary]
> Synthesized in [[_syntheses/bilibili-sam2act-memory-robot-manipulation-deep-dive-2026-08-11|SAM2Act 记忆机器人操作视频深度调研]].

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1Cuuj6CE5b |
| BV / video id | `BV1Cuuj6CE5b` |
| Author | 白拾的物理AI组会 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-08-11-bilibili-bv1cuuj6ce5b-icml-2025-sam2act.json` |

## Transcript Excerpt

SAM R at 来自 ICLR 2025。作者把视觉基础模型 SAM R 的表示能力与记忆机制整体迁移到机器人操作策略中，让模仿学习在精度、泛化与空间记忆三个维度同时取得提升。团队来自华盛顿大学、 NVIDIA 与 AI 二。分享按六个部分展开，先介绍作者与研究动机，再看方法与核心设计，随后是实验设置与结果分析，最后讨论局限性与要点总结，并在附录补充任务设计、训练细节与历史脉络。第一站是作者与团队背景。这条研究主线从 PerAct 的三维关键真行为克隆出发，经 DeCalcium 泛化基准，一路推进到 SAM RAct，脉络非常清晰。一、做好全方，本科毕业于华盛顿大学，先后实习于 NVIDIA Cosmos Lab 与 AIR Robotics，现于斯坦福大学李飞飞团队攻读博士。本文中他负责模型设计与训练。合作者包括 Perceptron 二作者 Marcus Gross The Colosseum一作 Wilbert Pumpeck 等，构成 UW AIR 与 NVIDIA 之间的紧密合作。机器人操作当前的关键挑战是在多任务交互、环境变化与空间记忆之间同时保持稳定。现有行为克隆策略在环境扰动面前掉点严重，面对需要记忆的任务时几乎失效。SAM2 Act 基于 RVT2 的多视图 Transformer 骨干，把 SAM2 的多分辨率视觉嵌入与及连上采样引入六 DoF 三维模仿学习，进一步提出的 SAM2 Act 加把 SAM2 的记忆库、记忆编码器与记忆注意力整体迁移进粗粒度分支。赋予策略隐式的空间记忆。评测覆盖18个 RLBench 任务、20个 CalSim 扰动场景与4个真机任务，并新建了专门打破马尔可夫假设的 MemoryBench 基准。核心思路可以概括为语言指令驱动多视图行为克隆策略，用 SAM 二的视觉表示完成高精度操作，用记忆架构应对需要回忆场景状态的任务，比如记住钳子被存放的位置。相关工作沿三条线展开。三维操作 Transformer 机器人视觉表示与机器人记忆。SAM R X 的差异点在于，它不是简单把 SAM R 当做更强的编码器，而是首次把 SAM R 的流逝记忆机制搬进操作策略。三维操作 Transformer 这条线，从 PerAct 的体素表示，到 RVT 与 RVT2的2.5D 多视图，再到 PointNet、 M2TR 等点云重建方案。视觉表示方面，SAM、SAM2与 DINOV2常被用作预训练或冻结编码器。 SAM e 就是 R V T 乘上 SAM 编码器的代表。记忆方面，已有工作大多停留在给策略加循环网络或外部缓存，而 SAM R at 把分割模型中的记忆机制直接复用为操作记忆。方法部分的关键是让 SAM 二编码器产出多分辨率嵌入，再用级联上采样逐步精化热图。SAM 二 X 加则在粗粒度分支注入记忆三件套。具体流程是点云重建后渲染三个虚拟视角。 RGB 通道复制后送入 SAM 二编码器，得到以物体为中心的多分辨率嵌入，并用 Rank 16的 Lora 做预适配。多视图 Transformer 的粗粒度分支先生成缩放热图，定位感兴趣区域，细粒度分支再精化为精确动作热图。语言由 clip 编码后与空间坐标对齐。SAM 二 act 加载粗粒度分支注入记忆库，记忆编码器与记忆注意力，每个视角维护独立的 fifo 队列。架构上，预测出的平移热图扮演了 SAM 二中 object mask 的角色，这使得同一套记忆机制可以从视频分割无缝迁移到动作预测，这是本文最有代表性的设计直觉。多分辨率上采样由三个凸上采样器级联实现，每一级把分辨率翻倍，并与 SAM2的多分辨率嵌入做元素相加和 layer norm，最大限度减少信息损失。记忆编码器融合多视图 Transformer 特征与下采样后的平移热图，而不是直接使用 SAM2的图像嵌入。因此记忆表示天然包含多视图语义。训练采用冻结加微调的范式。SAM2 at 预训练完成后，冻结编码器，多视图 Transformer 与细粒度分支，只微调粗力度分支，让热图承载最丰富的记忆上下文。采样方面，按连续关键帧序列组织 batch。先标准预训练，再记忆微调，避免收敛缓慢。级联上采样，每一级都做两倍空间分辨率提升，配合 SAM 二各层的多分辨率嵌入注入，最终输出精确的平移热图...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-08-11-bilibili-bv1cuuj6ce5b-icml-2025-sam2act.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
