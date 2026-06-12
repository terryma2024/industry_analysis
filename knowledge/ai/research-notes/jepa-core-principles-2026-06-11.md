---
title: JEPA 核心原理快速调研
type: synthesis
date_created: 2026-06-11
last_updated: 2026-06-11
sources:
  - ai/sources.csv
  - https://openreview.net/forum?id=BZ5a1r-kVsf
  - https://ai.meta.com/blog/yann-lecun-ai-model-i-jepa/
  - https://ai.meta.com/blog/v-jepa-yann-lecun-ai-model-video-joint-embedding-predictive-architecture/
  - https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/
  - https://arxiv.org/abs/2301.08243
  - https://arxiv.org/abs/2404.08471
  - https://arxiv.org/abs/2506.09985
  - https://arxiv.org/abs/2603.19312
tags:
  - industry/ai
  - self-supervised-learning
  - world-model
  - embodied-ai
status: active
---

# JEPA 核心原理快速调研

## 30 秒版本

JEPA，全称 [[_concepts/joint-embedding-predictive-architecture|Joint-Embedding Predictive Architecture]]，是 Yann LeCun 推动的“非生成式世界模型”路线。它不训练模型补全像素、patch 或 token，而是把输入压成 latent representation，然后让模型用可见上下文的 representation 去预测被遮挡部分、未来状态或动作后果的 representation。

如果用一句类比：**生成式模型像是在画出未来画面，JEPA 像是在预测未来画面的“状态摘要”。** 这会牺牲直接生成能力，但换来更高效的表征学习，并让模型更关注物体、动作、空间关系、可预测变化这些对理解和规划更有用的信息。

## LeCun 为什么提出 JEPA

LeCun 2022 年的 AMI 位置论文把问题设定为：机器如何像人和动物一样，通过观察学到世界模型，并用它进行推理、规划和少样本适应。论文给出的智能体框架包含 perception、world model、actor、critic、cost、short-term memory 和 configurator；其中 world model 的任务是补全当前未观测状态，并预测未来状态。

JEPA 是这个 world model 的候选训练范式。LeCun 反对把“预测世界”直接理解为“生成全部像素”，因为真实世界有大量不可预测或对任务无关的细节。JEPA 因此把预测目标转移到 latent space：只预测被编码器保留下来的抽象状态。

## 架构拆解

最小 JEPA 有三个核心部件：

| 部件 | 作用 | 直觉 |
|---|---|---|
| context encoder | 把可见输入 `x` 编成 `s_x` | “我现在看到什么” |
| target encoder | 把目标 `y` 编成 `s_y` | “被遮挡/未来部分的真实状态摘要” |
| predictor | 从 `s_x` 预测 `s_y` | “根据上下文，那里/未来应该是什么状态” |

训练目标是让预测表示接近目标表示。为了避免所有输入都变成同一个向量，需要 anti-collapse 机制：I-JEPA/V-JEPA 系列常用 EMA target encoder 与 masking 设计；其他 JEPA 后续工作会使用方差/协方差正则、Gaussian latent regularizer 等。

## JEPA 和生成式模型的关键差异

| 问题 | 生成式路线 | JEPA 路线 |
|---|---|---|
| 预测对象 | 像素、token、patch、波形等观测空间 | latent representation |
| 是否生成内容 | 是 | 默认不是 |
| 对不确定性的处理 | 要给出具体细节或分布 | 可由表示不变性和潜变量忽略/表达多种可能 |
| 学到的重点 | 全部可重建信息 | 对任务/语义/动态有用且可预测的信息 |
| 主要风险 | 算力高、被无关细节拖累 | 表示坍塌、丢失任务所需细节、难解释 |

一个关键判断：JEPA 不是“比生成式模型全面更强”，而是在**表征学习、物理世界理解、机器人规划**这些场景里，用“预测抽象状态”替代“重建全部观测”的路线选择。

## 发展脉络

| 时间 | 里程碑 | 说明 |
|---:|---|---|
| 2022 | LeCun AMI / H-JEPA 愿景 | 提出 JEPA、分层世界模型、内在代价和可微规划框架 |
| 2023 | I-JEPA | 图像自监督；从 context block 预测 target block 表示；CVPR 2023 |
| 2024 | V-JEPA | 视频自监督；大块时空 masking；冻结 backbone 后可迁移到动作识别等任务 |
| 2025 | V-JEPA 2 | 百万小时级视频/图像预训练，结合少量机器人视频，展示 latent world model + MPC 的 zero-shot pick/place |
| 2026 | LeWorldModel | 研究性探索：从像素端到端稳定训练小型 JEPA 式世界模型，用于控制与物理异常检测 |

## 快速理解 V-JEPA 2 的机器人规划

V-JEPA 2 的路线可以压缩为四步：

1. 用海量无标签视频训练视觉 encoder，让模型理解物体、运动和交互。
2. 用少量机器人视频训练 action-conditioned predictor：输入当前 latent state 和动作，预测下一步 latent state。
3. 给机器人一个目标图像，用 encoder 得到 goal embedding。
4. 通过 model-predictive control 试算候选动作，选择预测后最接近 goal embedding 的动作，边执行边重规划。

重要边界：这不是“机器人已经能任意理解和执行自然语言任务”。更准确地说，它证明了一个方向：**大规模视频自监督表征 + 少量机器人动作数据，可以形成可用于短程视觉目标规划的世界模型雏形。**

## 对 AI/具身智能产业的含义

- 对基础模型：JEPA 代表“世界模型”路线中非生成式、自监督、预测 latent state 的一支，和 LLM/扩散视频生成不是同一个优化目标。
- 对机器人：它提供了从互联网视频迁移到机器人规划的技术想象空间，尤其适合和 [[robot-training-data|机器人训练数据]]、DROID/OXE/LeRobot 类数据生态结合。
- 对中国创业/职业观察：短期更值得关注的不是“复刻 Meta 级 V-JEPA 2”，而是围绕数据闭环、视频/机器人轨迹清洗、world model evaluation、MPC/仿真评测平台、动作条件数据集格式转换等工程化环节形成能力。
- 对学习路径：先理解自监督表示学习、masked modeling、ViT/video transformer，再看世界模型、model-predictive control 和机器人数据集，会比直接啃“AGI 世界模型”叙事更稳。

## 待验证问题

- JEPA 与 diffusion/LLM/VLA 融合后，哪种 objective 在真实机器人长程任务上更可扩展。
- V-JEPA 2 的 zero-shot pick/place 是否能在更多机器人本体、更多任务和更高干扰环境中稳定复现。
- 物理推理 benchmark 是否能预测真实机器人任务成功率，还是会出现新的 benchmark gaming。
- 中国公司是否会优先采用 JEPA 式 latent world model，还是继续沿 VLA、扩散策略、生成式仿真路线推进。

## 来源

- Yann LeCun, `A Path Towards Autonomous Machine Intelligence`, 2022-06-27, OpenReview.
- Meta AI, `I-JEPA: The first AI model based on Yann LeCun's vision for more human-like AI`, 2023-06-13.
- Assran et al., `Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture`, arXiv:2301.08243, 2023.
- Meta AI, `V-JEPA: The next step toward Yann LeCun's vision of advanced machine intelligence`, 2024-02-15.
- Bardes et al., `Revisiting Feature Prediction for Learning Visual Representations from Video`, arXiv:2404.08471, 2024.
- Meta AI, `Introducing the V-JEPA 2 world model and new benchmarks for physical reasoning`, 2025-06-11.
- Assran et al., `V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning`, arXiv:2506.09985, 2025.
- Maes et al., `LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels`, arXiv:2603.19312, 2026.

## 关联连接

- [[_concepts/joint-embedding-predictive-architecture|Joint-Embedding Predictive Architecture]]
- [[_concepts/embodied-ai|Embodied AI]]
- [[_concepts/robot-training-data|Robot Training Data]]
- [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]
- [[robotics-embodied-ai/research-notes/open-embodied-ai-datasets-comparison-2026-06-11|开源具身智能训练与评估数据集横向调研]]
