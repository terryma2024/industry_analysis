---
title: "智谱入局具身智能，26亿参数VLA模型ZR-0，用'思维链'打通跨实体迁移，单臂/双臂/人形一键通用"
type: source
date_created: 2026-07-02
last_updated: 2026-07-02
source_urls:
  - https://www.bilibili.com/video/BV1orTv62E2j
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-02-bilibili-bv1ortv62e2j-26-vla-zr-0.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: draft
---

# 智谱入局具身智能，26亿参数VLA模型ZR-0，用"思维链"打通跨实体迁移，单臂/双臂/人形一键通用

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1orTv62E2j |
| BV / video id | `BV1orTv62E2j` |
| Author | 类人实验室 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-02-bilibili-bv1ortv62e2j-26-vla-zr-0.json` |

## Transcript Excerpt

大家好，这里是类人实验室。今天这篇我读完有点东西，一起拆一遍。你的机器人策略，换个机械臂就废？现有 VLA 全靠对齐动作空间硬扛。换个平台就瘫，根本学不到任务内在推理。这篇给 VLM 灌了密集思维练当教练，推理时却一刀切掉，让动作专家自己上跨。实体迁移大幅跃升，看完你会懂，多数对齐方案其实在绕远路。具体涉及哪些方向呢？我们可以按这个框架来拆，先理清研究背景，摸清问题出在哪，之后看系统架构，了解 Z20的双流设计和推理时跳过一思维链的巧思。接着深度拆解核心创新点，包括密集 e 思维链监督、 ProCoPus 60M数据、混合 VL 协同训练这些关键设计。然后看 sota 对比分析，用实验数据验证性能边界。再通过消融实验，量化 e 思维链到底带来了多少增益。最后坦诚讨论局限性和未来怎么规模化。好，我们先从研究背景切入。请看这页上四个真实机器人任务。清理桌子要把所有物体放进抽屉顶层。挂杯子需要识别白色杯子并精确挂到最远挂钩。推积木要用字母拼读引导推动，拾取放置则考验空间关系和指称理解。这些任务覆盖了指令遵循、颜色理解、长时序规划、OCR 推理等关键能力维度。正好暴露出 VLA 模型在跨实体迁移上的核心痛点。不同机器人平台的状态空间和动作空间有根本差异，过去靠零填充或统一动作空间。只是在格式层面对齐，并没有真正学到共享的语义表征。但是场景感知、任务规划、子任务分解这些高层认知过程。在不同实体间是天然共享的。Z20就从这个观察出发，用密集 e 思维链监督，在预训练时把 VLM 的表示强行拉齐。让模型先学会怎么想，再适配怎么做。顺着刚才的思路，我们直接看这张架构图。Z20把系统分成了两层，左侧的 VLM 作为系统二，处理全局和腕部图像以及任务指令。输出最后一层隐藏状态。右侧基于 DIT 的动作专家作为系统一，接收机器人状态和带噪声的动作快。通过流匹配去噪生成连续动作。中间那个 embodied chain of thought 在训练时提供结构化推理文本，但注意这根线在推理时是断开的。因为架构里有一个关键的交叉注意力 mask 限制动作专家只关注输入提示词特征，完全绕开了易思维链 token。这就做到了训练时用一思维链的丰富梯度去塑造表征。推理时，VLM 只需要单次前馈，直接出动作所需的特征。整个过程在 A6000 上大约90毫秒一帧。这种设计从根本上解决了推理延迟和强表征之间的矛盾。 Z20能学到跨实体对齐的表征，核心就靠这个秘籍e 思维链监督。论文里给每一帧图像都标注了一个结构化的 e 思维链序列。包含6个组件。场景描述提升物体识别，进度评估让模型感知任务完成状态。未来计划做长期持续推理。待办动作把计划拆成动词加宾语的原子子任务。目标物体用边界框提供空间定位，离散动作则作为与动作专家衔接的桥梁。这些组件全部采用与实体无关的格式表达，不论换机械臂还是人形机器人，子任务分解的那套逻辑是通用的。关键是这种监督在训练时给 VLM 注入了大量跨实体共享的认知梯度，但它只存在训练阶段，推理时完全不占用任何额外 token。算是一个相当聪明的信息注入方式。接续刚才讲的，为什么亿思维链能在训练时提供强力监督，却又不在推理时产生开销呢？这就得看架构里的交叉注意力 mask。ZR0在动作专家的交叉注意力层上做了一个限制，让状态和动作 token 作为 query 时，只能关注输入提示词对应的 VLM 特征。也就是任务文本和图像特征，而不去碰伊思维链 token 这就在架构层面把伊思维链生成和动作预测解耦了。推理的时候， VLM 只需要单次前馈跳过自回归文本解码，直接输出隐含状态给动作专家生成一个动作块，差不多100毫秒，完全满足实时控制要求。这个设计很妙，它保留一思维链训练带来的场景理解、进度估计、目标定位这些表征收益，却把推理成本降到几乎为零，是一种训练和推理非对称的优雅解法。要实现秘籍一思维链监督，数据得先跟上。ZR0用的 ProCorpus 6 0 M 聚合了超过40万条轨迹、约6000万帧数据。涵盖多种实体和任务，而且96.8%的帧都有易思维链标注。这里面的待办动作尤其值得注意，它把未来计划细化为一系列祈使句形式的动词加宾语原子子任务。比如从毛巾上抓起蓝色盘子。这种与实体无关的子目标分解正是跨实体对齐的关键机制。另外，目标物体组件直接用边界框给出空间定位...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-02-bilibili-bv1ortv62e2j-26-vla-zr-0.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
