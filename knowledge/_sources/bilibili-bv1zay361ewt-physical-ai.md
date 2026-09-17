---
title: "研讨会回放：Physical AI 助力下一次工业革命"
type: source
date_created: 2026-09-17
last_updated: 2026-09-17
source_urls:
  - https://www.bilibili.com/video/BV1zAY361EwT
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-09-17-bilibili-bv1zay361ewt-physical-ai.json
tags:
  - bilibili
  - video
  - ai-research
  - ai
status: draft
---

# 研讨会回放：Physical AI 助力下一次工业革命

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1zAY361EwT |
| BV / video id | `BV1zAY361EwT` |
| Author | NVIDIA英伟达 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-09-17-bilibili-bv1zay361ewt-physical-ai.json` |

## Transcript Excerpt

尊敬的各位来宾，大家下午好！欢迎参加 Physical AI 助力下一次工业革命在线研讨会。我是本次会议的主持人。在会议过程中，如果您有任何疑问，可以随时在屏幕右侧的聊天互动窗口中提出。讲师将在主题分享结束后为大家进行解答。下面我们首先有请 NVIDIA 解决方案架构师付少童老师带来他今天的主题分享，有请。好，大家好，我是英伟达的解决方案架构师 Scott 付少童，那主要负责 Physical AI 客户相关的技术支持。那我这边将向大家分享我们在 Physical AI 方向最新的策略。进展，然后以及我们最新的解决方案。 OK，那实际上大家对于 Physical AI 能够实现什么功能已经有了一个普遍的共识，就是说让我们的 AI 能够去理解我们的物理世界。那为了达到这样一个目的，首先我想介绍一下英伟达在实现 Physical AI 方面的硬件策略。那也就是我们的三台计算机理论。啊，首先我们有一台 GB 系列的啊计算机集群，用来去训练机器。啊，或者说用来训练 AI 的这个啊大脑，它是偏向于大模型的，具有自主感知和决策的能力。那同时的话，我们可以看到在右下角我们有一台 RTX Pro 啊，第二台计算机，它用来去构建一个虚拟的仿真环境，那用来去检验我们大模型的。去理解物理世界的这么一个效果。然后二者可以不断地进行反馈迭代，然后来提升我们自主大模型的这样一个。理解感知世界的效果。那最后的话，我们将会把这些模型啊，真正的去部署到我们真实的，这个端侧的设备当中，它可以是机器人，可以是工业机械臂，然后甚至说我们天上的卫星。那这个模型的话，将会由我们在设备内嵌的这个端侧芯片来去执行，也就是我们第三台负责部署执行的计算机，就是我们的 jetson orin 系列。 OK，那聊完了硬件基础，下面我和大家分享一下英伟达在软件侧啊所布局 Physical AI 的四个比较重要的方向。那首先第一个就是 CAE 也就是工程仿真领域。那因为我们要让 AI 去理解物理世界，那有一个高保真的物理求解器是必不可少的。啊，因为物理求解器，它能够为我们的虚拟场景，啊去注入现实世界的物理规律。啊，包括流体结构电磁，甚至多体动力学仿真等等等等。啊，从而让 AI 能够更好地去理解。啊，我们现实的世界。那第二部分我们会关注虚拟设施的集成，也就是工厂或者厂房的数字孪生。而第三部分我们会关注机器人行业，这也是我们的优势方向之一。那我们会提供完整的机器人虚拟仿真和强化学习训练框架。啊，如果您做机器人相关的啊，任何方向，实际上都可以找到。我们相应匹配的软件库。那最后我们会关注啊，在端侧等等的场景，比如说像端侧的视觉巡检等等，那为边缘场景去注入 AI 的能力。那每个方向我们都有相应的解决方案和软件站用来啊去加速您上述的工作流，或者更方便的啊，将我们的啊 library 去接入到您自己的工作流当中。啊，那下面我就从这四个方向分别来去展开分享。第一部分就是 CEA 的方向。那以往我们 CAE 工程仿真的工作流都是跑在 CPU 侧，那大概我们能够实现，几天运行完成一个算力，或者说一天完成。啊，几个啊算力这么一个量级。那我们一方面会支持啊，开发者啊，或者说相应的软件开发企业，帮助他们将啊，原本 c 在 CPU 侧的这个求解器向 GPU 上去迁移，从而利用 GPU 大规模并行的能力。进一步去提升啊，这种工程仿真的效率。那再往 CPU 切换，再往 GPU 切换完成之后，我们甚至可以达到在一天内能够完成数百个这种工程样例的仿真计算。那另一方面的话，我们会啊，进一步去注入 AI 的啊能力。啊，比如说我们会提供相应的 AI 训练框架，帮助啊开发者和企业在基于现有的工程仿真数据下去训练一个AI 代理模型，然后从而实现更快的这种实时预测。那我们管这种叫 AI Physics 那它就能够达到，甚至说我一天内可以实现几千个案例的这种。结果的预测啊，所以说来进一步提升我们相应工程仿真的效率。那么首先在求解器的 GPU 开发方面，那英伟达是不写工业级别的求解器的，但是我们为这个方向提供了非常便捷的扩大库的支持。那么开发者可以借助 NV 的加速库来实现 GPU 求解器的开发。那么 c a e 的核心实际上就是求解大规模的稀疏线性方程组。那我们这边专门提供了两个库，一个是库 d s s 一个是 a m g x。可以帮助开发者...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-09-17-bilibili-bv1zay361ewt-physical-ai.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[ai/00-index|AI]]
