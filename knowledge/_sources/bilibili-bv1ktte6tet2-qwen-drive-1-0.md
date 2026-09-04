---
title: "Qwen-Drive-1.0正式发布 | 首个能'开车'的通用大模型"
type: source
date_created: 2026-09-04
last_updated: 2026-09-04
source_urls:
  - https://www.bilibili.com/video/BV1kTtE6tET2
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-09-04-bilibili-bv1ktte6tet2-qwen-drive-1-0.json
tags:
  - bilibili
  - video
  - ai-research
  - ai
status: active
---

# Qwen-Drive-1.0正式发布 | 首个能"开车"的通用大模型

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1kTtE6tET2 |
| BV / video id | `BV1kTtE6tET2` |
| Author | 类人实验室 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-09-04-bilibili-bv1ktte6tet2-qwen-drive-1-0.json` |

## Transcript Excerpt

大家好，欢迎来到类人实验室。今天和大家分享一篇很值得看的论文，相信会给你的工作或科研带来一些新的启发。这篇论文讨论了一个核心问题，能不能在同一个模型里同时完成3D感知、视觉问答和运动规划，而且不丢通用视觉语言能力。作者给出了肯定答案。他们提出千问 Drive 10。保留预训练 VLM 架构，外挂两个模块。这篇文章还验证了显示三 d 感知和通用语言能力可以共存，这个思路很务实。值得拆开看看。顺着这个目标，我们先看研究背景，再拆系统架构和三个核心创新点。接着是对比 SOTA 消融实验和可视化结果。最后讨论局限与展望。那好，我们先从背景切入。先看研究背景。图一给了一个全局印象，千问 Drive 10在驾驶 VQA 3D感知、运动规划和通用 VQA 上都保持领先位置。但问题不在性能，而在范式。自动驾驶正从模块化流水线转向统一的 VLA 模型。很多方法直接拿 VLM 做 VQA 适配。这有两个明显短板。第一，文本 vqa 目标不直接约束3D布局、深度或占用。即使预训练表示编码了空间线索。仅靠文本监督也无法要求显示三 D 预测，更无法直接评估。所以这些模型能生成流畅场景描述，但在三 D 空间中仍然不够精确。第二，大规模驾驶适配容易导致通用视觉世界知识灾难性遗忘。任何有限的驾驶数据集都无法穷尽部署中遇到的稀有和未见情况。而且量产车正向舱驾一体化发展，单一模型需要同时服务座舱与驾驶。这意味着保留通用能力是硬性部署要求，不是锦上添花。针对这些痛点作者提出统一3D感知、 VQA 与运动规划的视觉语言基础模型。有了背景铺垫，来看系统架构。请看这张架构图，输入有三类，驾驶视频、单视角或多视角驾驶图像、通用图像。它们先经过共享的 Vision Encoder，再进入 Quin 3 5 4 B 语言模型。注意，VLM 本身没有被改动。多视角输入会用视角标签和帧标签编码告诉 VLM 每张图来自哪个相机、哪个时间步。规划任务采用视图主序。让连续观测在 token 序列中相邻，便于捕捉动态变化。两个外挂模块分别接管3D 感知和规划。B BEV 感知头融合视觉编码器特征与 VLM 输出特征，构建自车坐标系的 BEV 表示。这个头联合执行3D检测。语义占用预测和 BEV 地图分割。它提供显示的、可检查的三 D 信息接口。Planning Expert 以缓存的 VLM Key Value 为条件，通过 flow matching 生成轨迹。它输出干净轨迹和噪声轨迹支持运动规划。最后，模型输出包含文本响应、干净轨迹与噪声轨迹。统一覆盖三大核心任务这一页聚焦第一个核心创新，统一多任务 VLA 框架。一个很容易想到的做法是修改 VLM 结构，强行塞入感知和规划。但作者选择保留预训练 VLM 架构不变，这带来两个好处。第一，集成和部署复杂度大幅降低。第二，可以继续利用预训练获得的通用视觉世界知识。在单模型内，3D 感知、驾驶 VQA 和运动规划被统一起来。BEV 感知头提供显示可检查的3D 场景信息接口。不再只是黑盒文本推理。Planning Expert 复用共享表示，无需修改语言模型结构就能生成轨迹。最终这套设计支持舱架一体化。一个模型同时覆盖座舱与驾驶场景接下来看 BEV 感知头是怎么工作的。从图3R可以看到，它读取两条特征流，视觉编码器的低层外观特征。和 VLM 输出后的语义特征。低层特征提供几何线索，语义特征提供场景上下文。基于深度的视图变换，将图像特征提升到 3D voxel 空间。这一步不需要特征金字塔，只靠单尺度特征预测、深度分布，再沿相机射线散布，然后 BEV Transformer 融合几何先验和多尺度上下文信息。它的 query 用高度压缩的 voxel 特征初始化，提供显示几何鲜艳。最后三个任务分支联合优化检测、占用和地图分割目标。在 New scenes 和 Open scene 上，这个头拿到了领先的3D 感知性能。说完了感知，再看规划。Planning Expert 是一个32层的 Diffusion Transformer，参数量约1.1B。它不修改 VLM 架构，而是以缓存的 VLM key value 作为轨迹 token 的条件。训练采用 flow matching 并用 X 预测参数化，直接估计干净轨迹端点。这种端点参数化降低了对跨数据集传...

## 已完成综合

- 已编译为 [[_syntheses/bilibili-qwen-drive-1-0-autonomous-driving-vlm-deep-dive-2026-09-04|Qwen-Drive-1.0 自动驾驶视觉语言基础模型视频深度调研]]。
- 视频中的技术叙事已用 Qwen 官方博客、官方仓库与技术报告交叉核验；所有 benchmark 仍限于论文/作者协议，不能外推为量产道路安全或商业订单。

## Related Links

- [[ai/00-index|AI]]
- [[_syntheses/bilibili-qwen-drive-1-0-autonomous-driving-vlm-deep-dive-2026-09-04|Qwen-Drive-1.0 深度调研]]
