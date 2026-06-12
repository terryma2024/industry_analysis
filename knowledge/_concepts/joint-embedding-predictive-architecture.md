---
title: Joint-Embedding Predictive Architecture
type: concept
date_created: 2026-06-11
last_updated: 2026-06-11
sources:
  - ai/sources.csv
  - https://openreview.net/forum?id=BZ5a1r-kVsf
  - https://arxiv.org/abs/2301.08243
  - https://arxiv.org/abs/2404.08471
  - https://arxiv.org/abs/2506.09985
tags:
  - ai
  - self-supervised-learning
  - world-model
  - embodied-ai
status: active
aliases:
  - JEPA
  - Joint Embedding Predictive Architecture
---

# Joint-Embedding Predictive Architecture

JEPA 是 Yann LeCun 在 2022 年 `A Path Towards Autonomous Machine Intelligence` 路线中提出的非生成式自监督学习架构。它的核心不是“生成缺失像素/词元”，而是在同一个潜在表示空间里，用上下文 `x` 的表示去预测目标 `y` 的表示。

一句话：**JEPA 学的是“世界中哪些高层状态可预测”，而不是把世界的每个低层细节都补出来。**

## 核心机制

给定上下文 `x` 和目标 `y`：

1. `x` 进入上下文编码器，得到 `s_x`。
2. `y` 进入目标编码器，得到 `s_y`。
3. predictor 用 `s_x`，有时再加潜变量 `z` 或动作 `a`，预测 `s_y`。
4. 损失函数度量 `pred(s_x, z)` 与 `s_y` 的距离，并用正则、EMA target encoder、variance/covariance 约束等机制避免表示坍塌。

这和三类常见方法的差别：

| 路线 | 训练目标 | JEPA 视角下的问题 |
|---|---|---|
| 生成式 masked modeling | 预测缺失像素、patch、token | 需要解释太多不可预测或无关细节，计算代价高 |
| 对比学习 / invariant JEA | 拉近正样本、推远负样本 | 依赖增强/负样本，可能丢失位置、运动等有用信息 |
| JEPA | 预测目标的抽象表示 | 直接学习可预测的语义、状态和动态，但不能天然生成可视输出 |

## 关键变体

| 变体 | 时间 | 输入 | 关键点 |
|---|---:|---|---|
| H-JEPA / AMI 路线 | 2022 | 通用感知与动作 | LeCun 的总体愿景：分层世界模型、内在代价、actor、critic、规划 |
| I-JEPA | 2023 | 图像 | 从单个 context block 预测多个 target block 的表示；依赖大块 masking 来逼出语义 |
| V-JEPA | 2024 | 视频 | 预测被遮挡的时空区域表示；重点是冻结 backbone 后的动作识别、物体交互理解 |
| V-JEPA 2 / V-JEPA 2-AC | 2025 | 视频 + 少量机器人轨迹 | 在百万小时级视频上预训练，再用少量 DROID 机器人视频训练 action-conditioned predictor，可用模型预测控制做短程抓取/放置 |
| LeWorldModel | 2026 | 像素到控制任务 | 研究性后续工作，尝试用更少损失项端到端稳定训练 JEPA 式世界模型 |

## 为什么它和世界模型有关

JEPA 的 predictor 可以被看成一个低配世界模型：给定当前表示，预测未来或缺失部分的表示。在机器人场景中，如果 predictor 进一步接收动作 `a`，就可以问：

> 如果机器人从当前状态执行这组动作，下一步 latent state 会更接近目标图像的 latent state 吗？

这让 JEPA 可以和 model-predictive control 结合：枚举或采样候选动作，用 predictor 在 latent space 里“想象”后果，选择最接近目标表示的动作。

## 当前限制

- JEPA 不直接生成像素，所以可解释性和调试通常要额外训练 decoder 或 probe。
- 表示坍塌仍是核心工程风险，需要 masking、target encoder、正则或分布约束。
- 当前强项更偏短时空、局部物理和表征学习；长程规划、分层时间尺度、真实世界可靠性仍未解决。
- V-JEPA 2 已展示机器人 zero-shot 规划信号，但仍主要是短程 pick/place，并依赖视觉子目标和 model-predictive control。
- 物理推理 benchmark 显示，人类与当前视频模型仍有明显差距，JEPA 不是已经完成的 AGI 路线，而是一个有实证进展的研究范式。

## 关联连接

- [[embodied-ai]]
- [[robot-training-data]]
- [[vision-language-tactile-action]]
- [[ai/research-notes/jepa-core-principles-2026-06-11|JEPA 核心原理快速调研]]
- [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]
