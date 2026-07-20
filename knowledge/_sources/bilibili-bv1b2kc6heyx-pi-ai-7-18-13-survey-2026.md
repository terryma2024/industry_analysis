---
title: "PI 机器人 AI 创业公司 · 7 位创始人 · 18 个月 · 13 项产出【Survey 2026】"
type: source
date_created: 2026-07-19
last_updated: 2026-07-19
source_urls:
  - https://www.bilibili.com/video/BV1B2Kc6HEyX
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-19-bilibili-bv1b2kc6heyx-pi-ai-7-18-13-survey-2026.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# PI 机器人 AI 创业公司 · 7 位创始人 · 18 个月 · 13 项产出【Survey 2026】

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1B2Kc6HEyX |
| BV / video id | `BV1B2Kc6HEyX` |
| Author | 白拾的物理AI组会 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-19-bilibili-bv1b2kc6heyx-pi-ai-7-18-13-survey-2026.json` |

## Transcript Excerpt

欢迎收看 Physical Intelligence 公司调研报告。Physical Intelligence，简称 PI，是一家2024年成立于旧金山的机器人 AI 创业公司。本调研系统梳理了 PI 成立18个月内的13项研究产出，涵盖5代 VLA 基础模型的完整演化，以及 Recap 经验闭环方法的诞生与验证。核心判断模型是共同起点，经验是新壁垒。转发关注不迷路，这里是白石的物理 AI 与智能体组会，每日更新。机器人竞争的底层逻辑正在发生根本性转变。过去两年，行业最热闹的词是大脑、 VLA 世界模型、 Foundation Model 但论文在公开，算法在扩散。任何公司迟早都能拿到差不多的模型，真正拉开差距的是让机器人进真实世界攒经验，越用越强的能力。Pi用18个月完成了证明。派零展示 VLA 可行，派0.5发现泛化瓶颈在经验多样性，派0.6证明了经验闭环能让模型超越人类数据收集员。 Hi 零是 PI 在2024年10月发布的首个通用 VLA 策略模型。基于 Flow Matching 架构，将视觉、语言和动作统一到一个流模型中，以50赫兹频率输出实时控制。模型在7种不同形态的机器人上训练了68个任务，实现了零样本跨距深迁移。图中展示了整体架构，视觉输入经过预训练 VLM 编码。语言指令通过文本编码器处理，两者融合后通过 flow matching 生成连续动作序列。 Physical Intelligence 于2024年在旧金山成立，是一家机器人 AI 创业公司，由7位联合创始人共同创立。核心三人是 CEO Carol Hausman，前 Google DeepMind 资深研究员。 Chief Scientist Sergey Levine UC Berkeley 副教授，Research Lead Chelsea Finn Stanford 助理教授。与学术实验室不同，PI 的所有产出都指向产品化。成立18个月，已完成 π0~π0.7四次重大迭代，6篇 AR 14论文和7篇技术博客。PI 的方法论不是凭空产生的。 Lavin 在 UC Berkeley 领导 RL 实验室，从 GPS、Sack、SQL 到 RT 系列，始终推动数据和规模是核心推动力的信念。Fein 在 Stanford 开创 MAML 元学习，被引超过8000次。 Hosmer 在 Google DeepMind 完成了 CKN 到 RTR 的完整路径。三人在 PI 成立之前已有深度合作，共同发表了 MPOut ROut 等论文。这三条知识谱系的汇聚并非偶然。Lavin 的 RL 基因催生了 PI 的经验闭环，从 Sack 到 Recap，始终相信数据和交互产生智能。 Finn 的泛化基因塑造了 PI 的 VLA 路线，从 MAML 到派0.5的100多个 Airbnb 测试，始终追问能否迁移。Hosmer 的落地基因驱动了 PI 的产品化。从 C 看到 P I layer 始终解决语言如何变成动作。 P I 的独特之处在三条基因的协同， R L 让模型进化，泛化让模型通用，落地让模型有用。 PI 的研究可以归纳为三条相互协同的主线。主线一，派系列 VLA 基础模型的演化，从派0到派0.75代模型，核心问题是模型能做什么？如何让它做得更好？主线二， RL 方法论，从 Hill slope 到 Recap 再到 RL token 核心问题是模型如何从经验中持续进化。主线三，系统与工程，包含 Action chunking MEM 记忆。 PI layer 平台和 OpenP 开源，核心问题是 VLA 如何真正落地部署。三条主线共13项产出。这三条主线不是三个独立项目。而是一个完整的技术栈。Pai 系列提供模型能力， RL 方法论让模型持续进化，系统工程让模型真正落地。三者缺一不可。Pai0证明了 VLA 可行。派0.5发现泛化瓶颈后，催生了 Recap。Recap 证明了经验闭环有效，RL token 将它工程化为可复用的方法论。Action chunking 让模型实时运行，MEM 处理长时间任务。 PI layer 将一切封装为平台。派零于2024年10月发布，是首个通用 VLA 策略模型。Flow Matching 架构统一视觉、语言和动作流，50赫兹...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-19-bilibili-bv1b2kc6heyx-pi-ai-7-18-13-survey-2026.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## 后续综合

- 已综合为 [[_syntheses/bilibili-physical-intelligence-vla-experience-loop-deep-dive-2026-07-19|Physical Intelligence VLA 与经验闭环视频深度调研]]；模型版本、论文、系统和实验效果以论文/官方项目页为准，视频中的公司史与未对应论文的主张仍待验证。

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
