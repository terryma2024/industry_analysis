---
title: "Kimodo，全新且免费的生成式动画工具，人人可用！"
type: source
date_created: 2026-07-12
last_updated: 2026-07-12
source_urls:
  - https://www.bilibili.com/video/BV17UD6BzEQc
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-12-bilibili-bv17ud6bzeqc-kimodo.json
tags:
  - bilibili
  - video
  - ai-research
  - ai
status: draft
---

# Kimodo，全新且免费的生成式动画工具，人人可用！

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV17UD6BzEQc |
| BV / video id | `BV17UD6BzEQc` |
| Author | 海盗CG |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-12-bilibili-bv17ud6bzeqc-kimodo.json` |

## Transcript Excerpt

本视频由 RenderHog 赞助，来看他们的高品质三 D 模型与游戏资源。众所周知， NVIDIA 一直处于技术前沿，拥有深层次和智能工具。长期以来，它一直是现代计算机图形领域的核心推动者。无论是在硬件加速还是基础研究方面，现在看到他们最新的成果确实非常有趣。事实上，在神经网络用于生成噪声到图像爆发之前，英伟达就已经涉足这一领域，比如 this person does not exist。com 这样的网站，以及利用这种分段技术生成令人惊叹图像的 GAN 等。而在高斯点云 gaussian splatting 被广泛接受之前， NVIDIA 也曾率先推出神经辐射场 NeRF。如今这种技术已被广泛应用于电影和其他创意艺术领域。从字面意义上来说，英伟达一直走在前沿，并且是计算机图形以及各个领域新兴技术的重要推动者。而今天我们要介绍的是 nvidia 特别智能实验室的团队打造的一款有趣工具。这款工具用于生成动力学动作，可以应用于多个领域。现在为大家介绍 Kimodori。那么 key model 是什么？ nvidia key model 是一种动力学动作扩散模型，基于大规模光学动作数据进行训练。它通过文本和约束进行控制，以生成高质量的三维人类和机器人动作。这与我们之前讨论过的各种工具类似，这些工具只需使用清晰的提示输入就能制作动画。当然还有我们提到过的其他一些工具，有些工具不仅结合了提示词，还结合了视频素材来制作动画，而 Kimodo 则更进一步。顺便说一下，如果你对我们之前在这个类别中讨论过的那些工具感兴趣，相关链接会放在视频描述中，同时这个视频中也会有一些卡片。帮助你探索所有这些内容。那么这个工具的基本理念到底是什么呢？它的理念其实非常简单，高质量的动作数据在机器人、仿真和娱乐等应用中变得越来越重要。而拥有一个用户可以灵活操作并加以控制的工具也变得尤为关键。Kinetic Motion 将为创作者提供更多专注于创作本身的机会，而不是一开始就被制作动作的技术细节所困扰。这正是这个工具真正发挥作用的地方。也许你会觉得这和你常见的文本生成动作工具没什么区别，但实际上这个工具不仅能接收输入生成动作。还能对姿势进行动力学约束控制，使其更加具有交互性。因此，你实际上可以通过使用姿势或该工具提供的动力学约束控制，稍微调整你想要的动作效果。根据论文， KeyModel 旨在生成高质量的动作。同时，它可以通过文本和一整套全面的运动学约束轻松控制，包括全身关键帧。稀疏关节位置与旋转、二维路径点以及密集的二维路径。这意味着模型可以根据你作为创作者的需求进行条件设定。因此，我们可以轻松地从稀疏关键帧过渡到中间帧，以及与环境的交互。它还提供末端执行器约束，这是一种将手和脚的位置与旋转锁定结合起来的方式，这在各种动画或类人动作中都非常实用。此外，它还提供了合适的根部约束，因为角色的全局移动可以通过二维路径点和舞蹈部分来控制。拥有这些二维路径点，让你可以非常轻松地实际控制内容，并将物体定位在你想要的位置。这为你创造了一个可以有效控制动作的游乐场。有趣的是，这些动作可以导出为与 Promotions 和 mojoco 兼容的格式。这些也可以用于与机器人技术一起训练基于物理的策略。现在，K-Model 模型家族包括了在不同骨骼和数据集上训练的模型。它基本上是英伟达一项大型研究工作的组成部分，旨在通过开发模型和工具支持类人机器人和物理人工智能的三维类人动作。当然，对于喜欢深入了解的朋友，你可以直接去查阅相关内容。我会把相关链接放在描述栏里，你可以在那里看到他们整理的一些精彩事例。英伟达的团队对这个项目非常认真。实际上，他们投入了大量精力，让这个东西看起来极其实用。所以从这里，你实际上可以看看这些示例。比如我们有文本到动作的生成，这是用于行走动作的。我们还有这个，也是组合式的行走动作。所以你实际上可以更灵活的混合提示词。物体交互也是一个非常不错的功能，这也是你可以在这里找到的示例之一。我们还有典型的舞蹈动作，这里还有一些特技动作和手势。你还可以看到其他一些示例，比如风格化动作，更像是僵尸的动作。我们还有展示动作，还有按键示例和提示词序列。这意味着你实际上可以添加各种提示词。把这些内容混合在一起，动作就会按照计划进行。角色会根据这些提示被驱动。当然我们还有全身约束，这涉及...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-12-bilibili-bv17ud6bzeqc-kimodo.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[ai/00-index|AI]]
