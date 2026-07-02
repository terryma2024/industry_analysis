---
title: "具身智能必备！TensorRT深度学习部署居然被计算机大佬用大白话讲明白了，比刷剧还爽！"
type: source
date_created: 2026-07-02
last_updated: 2026-07-02
source_urls:
  - https://www.bilibili.com/video/BV1N8Kd6QEBE
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-02-bilibili-bv1n8kd6qebe-tensorrt.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: draft
---

# 具身智能必备！TensorRT深度学习部署居然被计算机大佬用大白话讲明白了，比刷剧还爽！

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1N8Kd6QEBE |
| BV / video id | `BV1N8Kd6QEBE` |
| Author | 大模型微调 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-02-bilibili-bv1n8kd6qebe-tensorrt.json` |

## Transcript Excerpt

真心希望各位观众老爷们不要白嫖，你的三连是我更新的动力！本期课程我们从零学习算法部署，TensorRT 篇。接下来我们了解本课程提供的内容以及学习方法。说在前面，本课程以 TensorRT 和 PyTorch 为主，不涉及模型训练，仅以工程角度考虑如何导出模型，让模型尽可能的高性能，以及如何上线交付。这里主要指的是多线程和封装。部署的优化思想，导出方式，解决问题流程，可以借鉴到其他算法场景，比如嵌入式的3399安卓 jetson 等等。这里我们抛砖引玉。算法部署学什么？这里我们列出三大块。第一块，精简的 CUDA 编程。第二块，TensorRT 基础。第三块，项目实战。那，CUDA 编程是一个相对复杂的一个技术。在这里我们主要强调的是精简。我们只求够用，能写图像处理、后处理，理解索引计算就够够了。它是我们 TensorRT 高性能的一个基础，所以必学的东西。第二个，TensorRT 基础这块，我们主要学习如何编译模型，TensorRT 就是推理模型，ONNX 如何控制，插件怎么写，解析器怎么配，深入理解 TensorRT 这个东西。第三个，我们拿真实的项目实际操作，并在 TensorRT 上以高性能推理起来，学习拿到项目过后如何分析问题，如何解决。本课程我们还开发了自动环境配置的 Python 包，解决环境配置的困扰。那为什么说环境配置的困扰？因为了解过 cuda tensorrt 的人应该会知道。学习库的测试题的第一步通常是配环境，那配环境呢又对初学者来讲是一个高门槛的事情。通常学了一两个月，可能都在解决环境上的一些问题，造成了造成了学习效率非常低下。因此我们才开发了这个自动环境配置的 Python 包。那使得初，零基础的初学者能够更友好的学习教程，并进行实验。然后力求更好的学习效率和更好的学习体验。同时我们还提供了52个学习案例，从浅到深，逐步递进的学习。这个是我们自动环境配置的一个演示。如果我们装好了 T R T P Y 这个库的话，就可以通着，通过 Git Even 这个指令，然后自动下载到对应的环境。比如这里 T R T 八，库到11.2，库定8。那它会根据你系统的驱动程序，自动选择一个合适的版本，然后自行下载并且解压。那这个解压的过程是解压到你的Anaconda Python set packages 里面，T R T P Y 里面。所以它不会影响到你系统的任何的环境。如果你想删掉它，你只需要把这个目录删除，那整个过程全部都不存在，所以不会干扰你的系统。我们安装完过后发现，CUDA 是11.2，cuDNN 是8.2，cuTensorRT 是8.0。那这是我们提供的案例的一个拉取的方法。我们通过 get template CPPTRTMinist 能拉取到 CPPTRTMinist 这个案例底下。然后它的代码会解到当前目录。我们 cd 到案例里面去，就可以立即 make run 运行起来。为什么？因为我们在拉取过后，它就已经为你配置好了环境，所以你可以立即进行运行。那这是运行后的一个输出的效果。那这是一个 minis 分类的一个演示，用 tensorrt 做minis 分类。这是一个图像五，它的分类的结果是五，然后 confidence 是0.9997。然后这是一个六。我们可以看到 MixFeel 里面，它的环境的路径全是依赖自 T R T P Y 里面，它不会依赖自你的依依赖你的系统里面的任何东西，所以它是一个相当于是绿色版。干净的东西。我们就可以打开闷点 c p p 然后学习并修改这里面代码，自己去尝试运行，尝试运行，来实现一个高效率的一个学习的过程。那这是一个系列，因为刚才的案例的组织形式相当于是一个独立的一个，独立的一个工程。那系列是相当于是一堆工程组在一起，比如说我们学习 cuda 我们就有123456789，每一个步骤学习不同的内容。那系列就是描述这个东西的。我们通过 T R D P Y Service Detail 来查看一个系列的一个详细信息。那 T R D P Y Service Detail 然后 CUDA Runtime API 查看它的详细信息。我们发现 CUDA Runtime API 里面有14个篇章，每个篇章讲的内容是不一样的。我们通过 c r d p y get service 然后 cuda...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-02-bilibili-bv1n8kd6qebe-tensorrt.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
