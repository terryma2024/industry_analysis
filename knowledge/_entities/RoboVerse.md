---
title: RoboVerse
type: entity
date_created: 2026-07-28
last_updated: 2026-07-28
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-336-roboverse-rss-2025-paper-full-pdf.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-328-roboverse-repository-readme-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-329-roboverse-scope-and-architecture-documentation-at-audited-commit.md
tags:
  - entity/project
  - industry/robotics-embodied-ai
  - simulation
  - benchmark
  - robot-learning
status: active
aliases:
  - RoboVerseOrg/RoboVerse
  - RoboVerse robot learning platform
---

# RoboVerse

> [!summary]
> RoboVerse 是一个面向可扩展、可泛化机器人学习的开源任务、资产、数据集、基准和学习工作流层，底层依赖独立的 [MetaSim](https://github.com/RoboVerseOrg/MetaSim) 多仿真器抽象。它可以用于迁移/构建任务、生成和增强仿真轨迹、训练并评测 IL/VLA/RL 策略、Real2Sim 和 sim-to-real 研究，但它本身不是机器人基础模型，也不是现成的企业级真机数据湖。

## 实体属性

| 字段 | 内容 |
|---|---|
| 类型 | 开源机器人学习平台、合成数据集与 benchmark |
| 论文 | RSS 2025；arXiv `2504.18904` |
| 代码 | [RoboVerseOrg/RoboVerse](https://github.com/RoboVerseOrg/RoboVerse) |
| 底层 | [RoboVerseOrg/MetaSim](https://github.com/RoboVerseOrg/MetaSim) |
| 审阅提交 | `e9b5c6e`（2026-06-28） |
| 根代码许可证 | Apache-2.0；第三方资产/数据许可需逐项确认 |
| 学习路线 | Diffusion Policy、ACT、OpenVLA、SmolVLA、RDT、Octo；PPO、FastTD3、SAC、TD3 等 |
| 数据/任务来源 | ManiSkill、RLBench、CALVIN、MetaWorld、robosuite、LIBERO、GraspNet、RoboTwin 等 |
| 核心格式 | task/scene/asset config；robot-keyed `*_v2.pkl` 轨迹；训练侧 Zarr、LeRobot、RLDS 等 |

## 稳定判断

- 核心差异化是“多 simulator、多任务来源统一”，不是某一个物理引擎的极致速度或一款通用 VLA。
- 真实数据最有价值的入口是：Real2Sim 资产/场景、物理参数校准、源示范轨迹、真实失败 benchmark 和真实+合成混训。
- arbitrary real data 不能直接倒入后自动变强；必须先完成本体、坐标系、控制语义、时间同步、资产和成功判据对齐。
- 适合研究/工程 PoC；生产采用前必须验证安装、任务成功、跨后端一致性、许可、真机相关性和维护成本。

## 关联连接

- [[_sources/roboverse-platform-dataset-benchmark-source-set|RoboVerse 来源集]]
- [[robotics-embodied-ai/research-notes/roboverse-platform-and-real-data-deep-dive-2026-07-28|RoboVerse 深度调研]]
- [[robotics-embodied-ai/research-notes/vla-world-model-data-infrastructure-platform-design-2026-07-06|VLA 与世界模型数据基建平台]]
- [[robotics-embodied-ai/research-notes/open-embodied-ai-datasets-comparison-2026-06-11|开源具身数据集对比]]
