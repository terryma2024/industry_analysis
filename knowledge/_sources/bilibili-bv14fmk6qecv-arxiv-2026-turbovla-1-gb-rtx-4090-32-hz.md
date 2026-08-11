---
title: "【arXiv 2026】🥇TurboVLA：<1 GB 显存、RTX 4090 上 32 Hz 实时运行的视觉-语言-动作模型"
type: source
date_created: 2026-08-11
last_updated: 2026-08-11
source_urls:
  - https://www.bilibili.com/video/BV14FMk6QECv
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-08-11-bilibili-bv14fmk6qecv-arxiv-2026-turbovla-1-gb-rtx-4090-32-hz.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# 【arXiv 2026】🥇TurboVLA：<1 GB 显存、RTX 4090 上 32 Hz 实时运行的视觉-语言-动作模型

> [!summary]
> Synthesized in [[_syntheses/bilibili-turbovla-real-time-vla-deep-dive-2026-08-11|TurboVLA 实时 VLA 视频深度调研]].

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV14FMk6QECv |
| BV / video id | `BV14FMk6QECv` |
| Author | 白拾的物理AI组会 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-08-11-bilibili-bv14fmk6qecv-arxiv-2026-turbovla-1-gb-rtx-4090-32-hz.json` |

## Transcript Excerpt

大家好，欢迎收看本期论文分享。今天介绍的是华中科技大学与华为联合提出的 Turbo VLA，发表于2026年 AR 14预印本。论文标题是 Turbo VLA 在 RTX 4090上，以不到1G 显存、32赫兹频率实时运行的视觉语言动作模型。它的核心主张非常大胆，执行及机器人控制，其实不需要大语言模型作为感知与动作之间的中央桥梁。本期分享按9个部分展开。作者介绍、研究背景与动机、相关工作、方法、实验设计、实验结果、局限性，最后是要点总结与参考文献。附录里还准备了 Liberal 全量对比、消融细节、 ORO 信号分析与 VLA 范式历史视角。核心观察。Turbo VLA 用0.2B参数在 LibriSpeech 上拿到97.7%的平均成功率，端到端延迟只有31.2毫秒，推理显存不到1GB，追平甚至超过十亿级参数的 VLA 模型。接下来进入第一部分，作者介绍。这是一个高校与工业界深度合作的团队，华中科技大学与华为技术有限公司联合研发。第一作者谢恒毅是华中科技大学博士生，具身智能方向，是 Turbo VLA 的项目负责人。共同一作姚晨飞同样来自华科。华为团队的三位成员参与了联合研发。通讯作者阵容非常豪华，朱颖颖教授深耕计算机视觉与具身智能，梁定康助理教授师从白翔教授，在具身智能、三维视觉与世界模型方向成果颇丰。白翔教授是 IEEE 与 IAPR 双 Fellow，国家杰出青年基金获得者，场景文字识别领域的领军学者。丁汉教授则是中国科学院院士、华中科技大学学术委员会主任、机器人学与智能制造的奠基人之一。研究脉络可以概括为，从感知到具身执行，再到制造装备。团队把轻量实时策略作为落地突破口。第二部分，研究背景与动机。核心论点是现有 VLA 的 LLM 中心化设计是实时机器人执行的主要瓶颈。现有视觉语言动作模型普遍遵循视觉到语言再到动作的通路，视觉观测被投影进大语言模型的表示空间，与指令一起经过十亿级参数的语言模型处理后，再解码成动作。这个设计在每次策略调用时都要付出巨大的计算和显存开销。TurboVLA 的关键观察是，指令已经明确了操作技能时，执行策略并不需要开放式语言生成。它只需要用指令来决定当前的视觉证据如何指导动作。因此，论文提出直接做视觉加语言到动作的映射，只用0.2B参数和不到1G显存，就在 RTX4090上实现了32赫兹的实时闭环操作，Liberal 平均成功率97.7%。这张图对比了两种范式。上半部分，LLM 中心化的 VLA 从视觉编码器出发，把视觉特征投影进语言模型空间，由大语言模型完成跨模态融合后再解码动作。Turbo VLA 则让视觉编码器与轻量文本编码器各自独立编码，通过双向交互直接构造控制导向的表示。下半部分展示性能与延迟的散点。TurboVLA 位于左上角，Libra 成功率接近98%，而端到端延迟只有31毫秒左右，远优于其他所有模型。第三部分相关工作。已有工作从动作侧或骨干侧提效，但都保留了 LLM 这个中央表示桥梁。相关工作分三条线。第一条是 LLM 中心化的 VLA 主线，从 RT 一、 RT 二到 OpenVLA 派零和派零点五，模型越来越大。但执行路径始终以大语言模型为核心。第二条是轻量与加速方向，TinyVLA、 RoboMamba、 SmallVLA、EvoE压缩模型规模、BLIP等做并行解码。但无论怎么改，动作解码器仍然作用在语言模型产生的特征上。第三条是语言条件化操作策略，比如 CLIPort CalvinPERAT TurboVLA 的直接交互机制借鉴了视觉接地模型 grounding DINO 的双向交叉注意力，但把它用于控制导向的表示构造。关键差异在于，所有加速工作都在保留 LLM 中心的前提下修修补补。TurboVLA 直接把大语言模型从执行路径中移除。第四部分，方法。紧凑编码器，双向视觉语言交互与并行动作快解码，构成完整的 V 加 L 到 A 执行通路。TurboVLA 的总体结构非常简洁。视觉观测用 DINOV 三编码，任务指令用轻量级的 BERT 编码，两者投影到共享的256维空间。六层双向交叉注意力模块在视觉流和指令流之间直接交换信息。最后，一个 Act 式的 Transformer 解码器用 H 个可学习的动作查询，并行预测整段连续动作，单次前向完成全部推理。训练只用行为克隆加 L...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-08-11-bilibili-bv14fmk6qecv-arxiv-2026-turbovla-1-gb-rtx-4090-32-hz.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
