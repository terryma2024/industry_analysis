---
title: 具身智能大模型物理理解能力评估框架
type: synthesis
date_created: 2026-07-03
last_updated: 2026-07-03
aliases:
  - 具身大模型物理理解评估
  - Physical understanding evaluation for embodied models
sources:
  - knowledge/robotics-embodied-ai/sources.csv
  - knowledge/_sources/roboalign-r1-reward-aligned-robot-video-world-models.md
  - knowledge/news/2026-06-05-nvidia-cosmos-3-getting-started-plan.md
  - knowledge/ai/research-notes/jepa-core-principles-2026-06-11.md
  - https://arxiv.org/abs/2307.15818
  - https://openvla.github.io/
  - https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/
  - https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/
  - https://arxiv.org/abs/2505.09694
  - https://arxiv.org/abs/2605.12090
tags:
  - industry/robotics-embodied-ai
  - embodied-ai
  - world-model
  - vla
  - evaluation
status: draft
---

# 具身智能大模型物理理解能力评估框架

## 结论先行

评估具身智能大模型是否真正具备物理世界理解，不能只看它能不能从图像和指令生成动作。更强的判据是：

> 模型能否在未见过的物体、场景、扰动和动作条件下，预测“如果这样做，世界会怎样变化”，并用这个预测选择更安全、更有效的动作。

因此，评测应从单点任务成功率升级为 **动作条件世界模型能力**。一个模型如果只会 `observation + instruction -> action`，哪怕 demo 很漂亮，也可能只是高维行为克隆；如果它能稳定做 `state + candidate action -> future state / outcome / risk`，并在反事实、遮挡、接触、失败恢复和规划中带来收益，才更接近“理解物理规律”。

## 核心区分

| 能力层级 | 典型表现 | 评估重点 | 不足以证明的地方 |
|---|---|---|---|
| 动作生成 | 给定图像和指令，输出机械臂/机器人动作 | 任务成功率、动作误差、语言 grounding | 可能记住数据分布或学到 affordance shortcut |
| 语义理解 + 动作 | 能选对目标、理解“最大/最小/靠近/类别”等语义 | OOD 物体、语义组合、指令泛化 | 仍不一定知道接触、重力、支撑、摩擦后果 |
| 动作条件预测 | 给定候选动作，预测未来状态、接触、失败风险 | forward dynamics、counterfactual rollout、action-outcome consistency | 预测好看不等于闭环可控 |
| 规划可用世界模型 | 用预测进行 MPC/tree search/重规划，提升真实任务成功率 | 闭环控制收益、失败恢复、安全边界、长程任务 | 仍需验证跨本体、跨场景、长期可靠性 |

[[robotics-embodied-ai/research-notes/lidar-world-model-training-2026-06-29|LiDAR 世界模型调研]]里的经验也适用于这里：如果目标是规划安全，优先评估 occupancy、接触、碰撞、可通行空间和动作后果，而不是只评估生成画面是否像真。

## 证据基底

### VLA 路线的强项与边界

RT-2 把机器人动作表示成文本 token，与视觉语言任务共同训练，证明 web-scale VLM 的语义知识可以迁移到机器人控制；其论文和项目页强调了 novel objects、未见指令、符号/关系推理和 6000 次机器人评测。OpenVLA 进一步开源 7B VLA，基于 970k Open X-Embodiment 机器人 episode，展示跨平台 out-of-the-box 控制、语义泛化和 LoRA 微调。

但这类结果主要证明 **语义泛化 + 策略学习**，不自动证明物理规律理解。OpenVLA 项目页也显示：在窄任务精细操作上，从头训练的 Diffusion Policy 仍可能更强；在互联网概念泛化上，OpenVLA 也弱于更大规模 co-finetuned 的 RT-2-X。这提示我们，VLA 成功可能来自数据覆盖、视觉特征、语言 grounding 和动作先验，而不是显式/隐式学到了完整物理因果。

### 世界模型路线的判据更接近问题本身

[[ai/research-notes/jepa-core-principles-2026-06-11|JEPA 核心原理快速调研]]把世界模型问题拆为：在 latent space 预测被遮挡部分、未来状态或动作后果。Meta V-JEPA 2 官方说明强调物理推理 benchmark 与机器人规划，并指出未来仍要走多时间尺度、视觉/音频/触觉多模态 JEPA。

[[news/2026-06-05-nvidia-cosmos-3-getting-started-plan|NVIDIA Cosmos 3 上手调研]]中，Cosmos 3 的价值也不是“生成漂亮视频”，而是把世界理解、未来状态生成和动作预测接近合在一起。[[_sources/roboalign-r1-reward-aligned-robot-video-world-models|RoboAlign-R1]]则进一步把机器人视频世界模型评估从像素相似度推进到 instruction following、manipulation success、action-outcome consistency、temporal consistency、contact realism 和 physics adherence。

World Action Models 综述给出一个有用命名：VLA 偏 reactive observation-to-action mapping，而 WAM 要把预测性状态建模与动作生成统一起来，目标从“只生成动作”变成“联合建模未来状态和动作”。

## 评估框架

### 1. 反事实预测：测“如果做 A 而不是 B，会发生什么”

最小实验：

1. 固定初始状态，给模型多个候选动作。
2. 要求模型预测每个动作后的物体状态、接触事件、风险和成功概率。
3. 在仿真或真机中执行，比较预测和实际结果。

关键任务：

- 支撑关系：抽走底部物体，上方物体是否掉落。
- 容器/遮挡：物体放入盒子后不可见，模型是否保持 object permanence。
- 接触与摩擦：推、拉、滑、滚、夹取时，运动方向和失败模式是否合理。
- 形变与液体：布料、袋子、软物体、颗粒物和液体是否被当作刚体错误处理。
- 工具使用：同一工具不同接触点、角度、力矩是否导致不同结果。

指标：

- outcome accuracy：最终状态是否预测正确。
- contact event F1：接触发生、接触对象、接触时序是否预测正确。
- physical violation rate：穿模、悬浮、无支撑、质量/尺度不一致、瞬移。
- calibrated risk：模型给出的失败概率是否和真实失败率匹配。

### 2. 最小物理对照组：防止模型靠语义捷径答题

只改一个变量，其他保持相同：

| 对照变量 | 测什么 | 反捷径设计 |
|---|---|---|
| 质量 | 同形状不同重量，夹取/推动是否不同 | 外观相同，用历史交互或文字标签提示质量 |
| 摩擦 | 同物体在木桌/玻璃/布面上滑动差异 | 视觉纹理相近，动作完全相同 |
| 支撑 | 物体半悬空、完全支撑、被遮挡支撑 | 只改支撑面积或遮挡角度 |
| 容器 | 开口、封闭、透明、遮挡容器 | 目标物不可见时继续追踪 |
| 可达性 | 机器人末端可达/不可达/需绕障 | 单纯 VLM 可能只会说目标，不会算路径 |

这类 minimal pairs 比大杂烩 benchmark 更关键，因为它能逼出模型是否抓住因果变量。

### 3. Forward dynamics 与 inverse dynamics 双向测

只测动作生成容易误判。应同时测两类能力：

- Forward dynamics：`state_t + action_t -> state_{t+1:t+k}`。模型必须预测动作后果。
- Inverse dynamics：`state_t + state_{t+k} -> action / intervention`。模型必须解释什么动作造成了变化。

如果模型能生成可执行动作，却不能解释或预测动作造成的状态变化，说明它更可能是 policy prior，而不是可靠世界模型。反过来，如果模型能预测视频但不能输出可执行动作，它可能是生成式仿真器，还不是完整具身策略。

### 4. 闭环规划收益：世界模型必须让策略变好

最终判据不是离线问答，而是闭环任务：

1. 建立 policy-only baseline：VLA 或 Diffusion Policy 直接输出动作。
2. 建立 world-model-assisted policy：先生成/评分候选动作 rollout，再选择动作。
3. 在同一任务、同一机器人、同一扰动集上比较。

关键指标：

- success rate uplift：成功率是否显著提升。
- recovery rate：抓空、滑落、被人移动物体后是否能重规划。
- safety violation：碰撞、过力、掉落、越界是否降低。
- sample efficiency：新任务示教样本是否减少。
- long-horizon degradation：步数变长后性能下降是否更慢。

如果世界模型不能带来规划收益，它也许能“讲物理”，但还没证明“对行动有用”。

### 5. OOD 泛化：从分布内动作到物理规律

至少做四类 out-of-distribution：

- 物体 OOD：新形状、新材质、新重量、新尺寸。
- 场景 OOD：新背景、光照、遮挡、桌面材质、障碍布局。
- 本体 OOD：不同机械臂、夹爪、双臂/移动操作/人形。
- 任务 OOD：组合任务、长程任务、失败恢复任务。

VLA 在语义 OOD 上强，不代表物理 OOD 强。真正的物理理解应在新物体、新材质和新接触几何下仍能做合理预测。

### 6. 多模态约束：只看 RGB 容易高估

对物理规律，视觉不是唯一证据。应尽量加入：

- depth / stereo：空间关系、尺度、可达性。
- force / torque / tactile：接触、滑移、夹持稳定性。
- proprioception：关节、末端位姿、速度、负载。
- LiDAR / occupancy：移动机器人和自动驾驶中的 freespace、碰撞、动态障碍。
- audio：碰撞、掉落、破碎、摩擦等事件线索。

如果模型只在 RGB 视频上表现好，但一接入力觉/触觉后无法校准接触状态，说明物理理解仍停留在视觉常识层。

## 推荐评测组合

| 层级 | 可用 benchmark / 实验 | 用途 | 局限 |
|---|---|---|---|
| 视频物理理解 | V-JEPA 2 相关物理推理 benchmark、IntPhys / MVP 类 minimal video pairs | 测 object permanence、因果、物理异常检测 | 不等于机器人可执行 |
| Embodied world model | EWMBench、RobotWorldBench / RoboAlign-Judge | 测场景一致性、运动正确性、语义对齐、接触真实性、物理遵循 | judge 模型可能有偏差，需人评和真机交叉验证 |
| VLA 策略 | OpenVLA、RT-2 / RT-X 类真实机器人任务集 | 测语言 grounding、跨物体/跨场景动作泛化 | 任务成功率无法拆出物理理解来源 |
| 仿真闭环 | LIBERO、ManiSkill、RoboCasa、RoboTwin、Isaac / MuJoCo 自定义扰动 | 可控、可重复、可做 minimal pairs | sim2real gap，物理引擎本身也有偏差 |
| 真机闭环 | 同任务 policy-only vs world-model-assisted A/B | 证明世界模型是否真正提升行动 | 成本高、样本少、安全风险高 |

## 尽调问法

评估一家具身大模型公司，不要只看 demo，建议直接问：

1. 是否有 action-conditioned forward model？输入候选动作后，能输出未来状态、风险或评分吗？
2. 评测是否包含 minimal physical pairs，而不是只含自然语言任务成功率？
3. 有没有 policy-only vs world-model-assisted 的 A/B 结果？
4. 有没有失败恢复数据：滑落、抓空、遮挡、目标被移动、工具使用失败？
5. 物理评测维度是否覆盖 contact、support、collision、force、temporal consistency？
6. 训练数据是否标注动作前后状态、接触、失败/接管、力觉/触觉，而不仅是视频和动作？
7. 真实机器人评测是否跨物体、跨材质、跨场景、跨本体？
8. 模型是否输出不确定性，遇到高风险动作是否会降级、请求帮助或重规划？

## 红旗信号

- 只展示剪辑 demo，没有完整 rollout、失败样本和统计口径。
- 只报任务成功率，不报扰动集、置信区间、失败类型。
- 只在训练环境、训练物体或相近任务中评测。
- 只有 `observation -> action`，没有 `action -> outcome` 的预测或评分能力。
- 世界模型只用像素/视频画质指标，不测接触、碰撞、支撑、动作结果一致性。
- 用 VLM judge 评分但没有人类标注一致性、真机验证或 reward hacking 检查。
- 不披露数据分布、本体覆盖、任务覆盖和失败/接管数据比例。

## 中国产业启发

- 对整机公司：短期 demo 能证明工程整合和动作库，不能证明通用物理理解。投资或合作尽调要看扰动评测、失败恢复和真实复购场景。
- 对数据平台：高价值数据不只是更多 episode，而是带动作前后状态、接触、力觉、失败、接管、物体属性和环境变量的反事实可评测数据。可和 [[robotics-embodied-ai/research-notes/robot-training-data-value-evaluation-2026-06-29|训练数据价值评估框架]]合并使用。
- 对仿真/评测平台：商业机会可能在“物理 minimal pairs + 真机 A/B + judge/reward model + 数据回流”的闭环，而不只是提供仿真资产。
- 对个人学习/作品集：最有价值的项目不是复刻一个 VLA demo，而是做一个小而硬的评测 harness：同一机械臂/仿真环境中，构造支撑、摩擦、遮挡、接触扰动，比较 OpenVLA/Diffusion Policy/world-model-assisted policy 的预测和成功率。

## 一个最小可执行实验

目标：验证模型是“会动作”还是“懂后果”。

实验设置：

- 平台：LIBERO / ManiSkill / Isaac Sim 中一个桌面机械臂任务，后续可迁到真机。
- 任务：把目标物推入容器、从支撑物上取物、绕障抓取、轻推易滑物体。
- 变量：桌面摩擦、物体质量、支撑面积、遮挡程度、目标位置。
- 模型组：policy-only VLA / Diffusion Policy；world-model-assisted planner；人类规则 baseline。
- 输出：动作、预测未来状态、执行视频、接触事件、最终状态、失败原因。

验收：

- 如果模型只在固定变量下成功，扰动后失败，属于动作生成。
- 如果模型能预测扰动后的失败风险，但不能改善动作，属于物理感知或离线理解。
- 如果模型能因预测风险而改变动作，并显著降低失败率，才算具备规划可用的物理理解雏形。

## 待验证

- RoboAlign-R1 / RobotWorldBench 是否开放数据、代码和可商用许可证；若开放，应建立 source card 并复现实验评测脚本。
- V-JEPA 2 物理 benchmark 与真实机器人成功率的相关性仍需实证，不能把视频问答分数直接等同于具身能力。
- WAM 作为 2026 年综述定义仍是研究范式整理，产业产品是否已经稳定采用 joint world-action modeling 需要逐家公司验证。
- 国内具身智能公司公开 demo 多，系统评测少；后续应建立中国公司“物理理解评测披露表”。

## 关联连接

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]
- [[robotics-embodied-ai/research-notes/open-embodied-ai-datasets-comparison-2026-06-11|开源具身智能训练与评估数据集横向调研]]
- [[robotics-embodied-ai/research-notes/robot-training-data-value-evaluation-2026-06-29|具身智能训练数据价值评估框架]]
- [[robotics-embodied-ai/research-notes/lidar-world-model-training-2026-06-29|激光雷达数据融合进入世界模型训练论文与方案调研]]
- [[ai/research-notes/jepa-core-principles-2026-06-11|JEPA 核心原理快速调研]]
- [[_sources/roboalign-r1-reward-aligned-robot-video-world-models|RoboAlign-R1 - Reward-Aligned Robot Video World Models]]
