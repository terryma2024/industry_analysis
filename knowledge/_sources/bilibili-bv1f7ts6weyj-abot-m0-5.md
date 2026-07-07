---
title: "高德杀进具身智能！ABot-M0.5：一个模型同时搞定导航+操作，还能自己'做梦'训练？"
type: source
date_created: 2026-07-07
last_updated: 2026-07-07
source_urls:
  - https://www.bilibili.com/video/BV1F7Ts6WEYj
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-07-bilibili-bv1f7ts6weyj-abot-m0-5.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: draft
---

# 高德杀进具身智能！ABot-M0.5：一个模型同时搞定导航+操作，还能自己"做梦"训练？

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. Synthesized in [[_syntheses/bilibili-abot-m05-world-action-model-deep-dive-2026-07-07|ABot-M0.5 世界动作模型视频深度调研]].

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1F7Ts6WEYj |
| BV / video id | `BV1F7Ts6WEYj` |
| Author | 类人实验室 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-07-bilibili-bv1f7ts6weyj-abot-m0-5.json` |

## Transcript Excerpt

大家好，这里是类人实验室。今天这篇论文我读完觉得有点东西，想跟你一起拆一遍。你的机器人想在杂乱厨房里一边走一边拧瓶盖。现有方案硬凑导航和操作，动作频率一乱，长序列就崩。这篇用 MOT 解耦两类动作，DreamForcing 强行对齐时间力度，长序列成功率暴增。看完你会发现很多模型都卡在动作解耦上，这套思路能直接套用。好，既然机器人学会了做梦，那这个梦境到底怎么编织的呢？今天我会沿着这条对齐主线，逐一拆解它的研究动机、架构设计、三大创新，再到 SOTA 对比、消融实验和真实世界的可视化表现。最后诚实地聊聊它的局限。我们先从为什么需要这样一个模型开始。移动操作一直是个硬骨头。现有的 VLA 策略是被动反应，缺乏对世界的显示建模，遇到长序列任务就容易断片。那世界动作模型 WAM 呢？明明引入了未来预测，却在时间力度、动作结构和训练测试一致性上卡了壳。嗯。粗力度的视频潜变量要嫁接到细力度的控制频率，天生就不匹配。导航和操作的动作纠缠在一起，互相拉扯。训练时看的是真实未来，推理时却只能用自己预测的模糊画面，误差越滚越大。A bot M 零五正是盯准这三个错位，提出了一整套对齐感知框架。顺着刚挖出的三个瓶颈，直接看这张架构全景图。顶部的三阶段训练流程一目了然。先在开放数据集上预训练世界模型，再通过监督微调以混合真实任务数据做联合微调。最后用监督微调二的 Dream Forcing 完成训练测试对齐。图的左侧是关键级联管道，从视频潜变量到潜在动作，再到可执行动作，层级解耦。中间的双层混合 Transformer 负责模态和动作空间的分离。右侧和底部的雷达图与执行序列则展示了仿真与真实环境下的 sota 性能。这个设计把时间桥接、空间拆解和推理一致性一次性打通了。先看第一个创新，中间潜在动作 mit 就是图中那条承上启下的胶水。没有它，粗力度的视频潜变量直接映射到控制信号。就会像用橡皮管去拧螺丝。但这里的做法很优雅，从连续帧中提取仅依赖视觉转换的潜在动作，不需要机器人运动学标签。用条件流匹配生成，再把整个管道做成视频潜在动作动作的三级级联。请注意这张对比图，三阶段分离架构在 drop 等于零时达到了94%的成功率。而通道拼接或两阶段方式都差了一截。本质上它保护了模态边界，不让视频和动作的信息提前泄露。解决完时间错位，动作空间内部的打架怎么解呢？A、BOT M Zero 五搬出了双层级混合 Transformer，也就是图三里这个 De-MoT。它的第一层是模态级解耦，为视频、潜在动作、可执行动作各分配独立的投影和输出头，防止表征坍塌。第二层更绝，把原本纠缠的动作空间硬核拆成 manipulation 和 mobility 两个子空间，各自拥有专属的 F F N 和预测头像，给胳膊和底盘开了独立车道。但联合自注意力又让它们能在关键时刻互相通风报信。前馈继续保持专精，减少梯度互扰，这样既能协调避碰，又不耽误精细抓取。最后一个创新点直指训练和推理的致命差异。图四把三种范式摆得很清楚。Teacher Forcing 看的是干净真值，Diffusion Forcing 在噪声上做文章。但推理时的条件分布始终对不齐。A bot M 零五的 Dream Forcing 则直接在训练时把动作预测建立在自生成的梦境视频上。嗯，具体实施是两阶段传播。Phase A 并行产生梦境潜变量，Phase B 再基于它预测动作。这样一来，模型从一开始就学会了容忍视频伪影和预测噪声。自回归展开时不再累积误差，这个对齐思路直接让训练和测试成为镜像。有设计也得有数据撑腰。看这张 RoboCat 365 Benchmark 的表，A Bot M05 在 average atomic scene composite scene 和 composite unseen 四个维度全线超车。特别是面对派零 IGR 零 T GigaWorld Policy 这些强基线，它在复合未见任务上的优势更加明显。说明对齐设计不仅管单步，更长程多阶段任务同样受益。另外，引入 Condensed Memory 增强后，性能再度拔高，验证了记忆机制和整体架构的协同。这种靠结构性改进而不是单纯堆参数量带来的提升才真正让人放心。光讲数值提升不够，组件到底多大贡献得拆开看。表七把潜在动作策略扒了个底朝天，直接映射只有87...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-07-bilibili-bv1f7ts6weyj-abot-m0-5.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
