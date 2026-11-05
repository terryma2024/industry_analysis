---
title: 接触模型、物理解算误差与 Sim2Real 差距
type: concept
date_created: 2026-10-26
last_updated: 2026-10-26
sources:
  - knowledge/_sources/robot-physics-engines-sim2real-source-set-2026-10-26.md
tags:
  - physics-simulation
  - contact-dynamics
  - sim2real
status: active
---

# 接触模型、物理解算误差与 Sim2Real 差距

**模型精度、数值精度、梯度正确性和策略迁移效果是四个不同的评价对象。**把它们都叫“物理更真实”，会导致错误归因。

| 对象 | 核心问题 | 典型验证 |
|---|---|---|
| 物理模型 | 接触、摩擦、执行器和材料定律能否表达目标工况 | 实测受力、滑移、变形、接触事件与多工况留出 |
| 几何/离散化 | collider、法向、接触面、步长和控制采样是否合理 | 几何公差、事件对齐、网格与步长敏感性 |
| 数值求解 | 给定离散模型是否在计算预算内求得足够准确 | 残差、迭代敏感性、容量、守恒/耗散一致性 |
| 梯度 | 算法导数是否正确，以及是否对优化有用 | 解析/方向导数、接触切换、优化与真机效果 |
| 策略迁移 | 闭环行为是否对真实不确定性足够稳健 | 真机holdout、力/损伤/成功率与恢复行为 |

P02说明接触模型松弛与有限迭代是不同误差源；P12/P13说明程序可微不保证碰撞梯度正确；P08/P21提醒真实力迁移依赖执行器与replay初始化。[SRC-robotics-649](../../raw/robotics-embodied-ai/documents/SRC-robotics-649-contact-models-in-robotics-a-comparative-analysis.md) [SRC-robotics-658](../../raw/robotics-embodied-ai/documents/SRC-robotics-658-differentiable-physics-simulations-with-contacts-do-they-have-correct-gradients.md) [SRC-robotics-659](../../raw/robotics-embodied-ai/documents/SRC-robotics-659-differentiable-simulation-of-hard-contacts-with-soft-gradients-for-learning-and.md) [SRC-robotics-654](../../raw/robotics-embodied-ai/documents/SRC-robotics-654-learning-agile-and-dynamic-motor-skills-for-legged-robots.md) [SRC-robotics-671](../../raw/robotics-embodied-ai/documents/SRC-robotics-671-contact-uan-unsupervised-actuator-networks-as-a-residual-world-model-for-humanoi.md)

## 常见误区

- 接触残差很低，只能说明更接近该模型的解，不能证明模型适合真实材料。
- 面接触模型能产生分布压力/力矩，但不因此具备完整软体内部状态和材料历史。
- 自动微分、可微接触、可微多物理耦合、梯度对优化有用是逐层附加条件。
- Sim2Sim是发现引擎特有漏洞的诊断方法；共享资产或理想驱动错误可能在多个引擎同时存在。
- 参数随机化处理模型族内的不确定性；缺失孔洞、机械结构或接触模式通常需要修模型。

以上误区校正包含方法判断；没有本文独立实测支持的通用引擎排名。

## 关联连接

- [[robotics-embodied-ai/research-notes/robot-physics-engines-sim2real-2026-10-26|完整技术调研]]
- [[_sources/robot-physics-engines-sim2real-source-set-2026-10-26|论文和官方资料]]
- [[robotics-embodied-ai/research-notes/3d-simulation-asset-production-pipelines-comparison-2026-08-06|外观与物理资产分离]]
