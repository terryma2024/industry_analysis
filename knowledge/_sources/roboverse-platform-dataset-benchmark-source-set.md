---
title: RoboVerse 平台、数据集与基准来源集
type: source
date_created: 2026-07-28
last_updated: 2026-07-28
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-327-roboverse-towards-a-unified-platform-dataset-and-benchmark-for-scalable-and-gene.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-328-roboverse-repository-readme-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-329-roboverse-scope-and-architecture-documentation-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-330-roboverse-multi-agent-trajectory-format-and-cross-simulator-replay-documentation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-331-roboverse-smolvla-and-lerobot-data-pipeline-documentation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-332-roboverse-github-repository-and-issue-audit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-336-roboverse-rss-2025-paper-full-pdf.md
tags:
  - source/github
  - source/paper
  - industry/robotics-embodied-ai
  - simulation
  - robot-learning
status: active
aliases:
  - RoboVerse 来源摘要
---

# RoboVerse 平台、数据集与基准来源集

> [!summary]
> 本来源集以 RSS 2025 论文、固定提交 `e9b5c6e` 的仓库/文档、2026-07-28 GitHub 元数据与官方对照平台文档为证据底座。稳定结论是：RoboVerse 是 MetaSim 之上的任务、资产、数据、基准和学习层，不是一个已训练的机器人基础模型，也不是开箱即用的真机数据管理平台。综合判断见 [[robotics-embodied-ai/research-notes/roboverse-platform-and-real-data-deep-dive-2026-07-28|RoboVerse 深度调研]]。

## 审阅范围与方法

- 论文：审阅 arXiv 摘要和 39 MB 完整 PDF；细节以 [`SRC-robotics-336`](../../raw/robotics-embodied-ai/documents/SRC-robotics-336-roboverse-rss-2025-paper-full-pdf.md) 为准。
- 代码/文档：浅克隆公开仓库并固定到审阅提交 `e9b5c6efeb665052edeb934fc3172df8b9d3c9d7`，静态检查 README、数据格式、学习工作流和示例；未安装 GPU 仿真后端或复现实验。
- 维护信号：2026-07-28 查询 GitHub API 和公开 issue；issue 仅作为工程摩擦信号，不作为性能证据。
- 横向对照：使用 Isaac Lab、LeRobotDataset v3、ManiSkill 官方文档；不做未经统一硬件实测的速度排名。

## 核心来源

| SRC | 内容 | 等级 | 关键用途 |
|---|---|---:|---|
| [`SRC-robotics-327`](../../raw/robotics-embodied-ai/documents/SRC-robotics-327-roboverse-towards-a-unified-platform-dataset-and-benchmark-for-scalable-and-gene.md) | arXiv 论文元数据/摘要 | S | 研究对象、发表时间、总定位。 |
| [`SRC-robotics-336`](../../raw/robotics-embodied-ai/documents/SRC-robotics-336-roboverse-rss-2025-paper-full-pdf.md) | RSS 2025 完整论文 | S | 数据构造、世界模型、Real2Sim、sim-to-real、限制。 |
| [`SRC-robotics-328`](../../raw/robotics-embodied-ai/documents/SRC-robotics-328-roboverse-repository-readme-at-audited-commit.md) | 固定提交 README | S | 当前安装入口、后端/来源集成、Apache-2.0、资产许可风险。 |
| [`SRC-robotics-329`](../../raw/robotics-embodied-ai/documents/SRC-robotics-329-roboverse-scope-and-architecture-documentation-at-audited-commit.md) | 范围与架构文档 | S | RoboVerse/MetaSim 边界、Pack/Dataset/Learn 三层。 |
| [`SRC-robotics-330`](../../raw/robotics-embodied-ai/documents/SRC-robotics-330-roboverse-multi-agent-trajectory-format-and-cross-simulator-replay-documentation.md) | 轨迹格式文档 | S | robot-keyed PKL、双臂数据、state replay 边界。 |
| [`SRC-robotics-331`](../../raw/robotics-embodied-ai/documents/SRC-robotics-331-roboverse-smolvla-and-lerobot-data-pipeline-documentation.md) | SmolVLA/LeRobot 工作流 | S | demo→LeRobot→训练→评测的现有出口。 |
| [`SRC-robotics-332`](../../raw/robotics-embodied-ai/documents/SRC-robotics-332-roboverse-github-repository-and-issue-audit.md) | GitHub 元数据/API fallback | S/B | 活跃维护与公开工程问题；自动抽取仅保存 HTML。 |
| [`SRC-robotics-333`](../../raw/robotics-embodied-ai/documents/SRC-robotics-333-isaac-lab-official-framework-overview.md) | Isaac Lab 官方概览 | S | 单一 PhysX/Isaac 生态对照。 |
| [`SRC-robotics-334`](../../raw/robotics-embodied-ai/documents/SRC-robotics-334-lerobotdataset-v3-official-specification.md) | LeRobotDataset v3 规范 | S | 真机数据格式/共享层对照。 |
| [`SRC-robotics-335`](../../raw/robotics-embodied-ai/documents/SRC-robotics-335-maniskill-official-framework-documentation.md) | ManiSkill 官方概览 | S | GPU 并行操作仿真对照。 |

## 可直接引用的事实边界

- 论文版本报告：数据集覆盖超过 1,000 个任务、超过 1,000 万 transitions；核心 manipulation 迁移表单独统计为 276 个 task categories、约 510.5k trajectories、约 5.5k assets。两个口径不是同一统计层级，不应互换。
- 论文把 50k DROID 与 50k RoboVerse episode 混合训练动作条件视频世界模型，作者报告物体几何保持改善；未给出足以证明下游真实任务成功率提升的统一数值指标。
- 论文 Real2Sim 抓取实验作者报告 80% 对 50% 基线；同时承认摩擦、质量、复杂材质与未见 mesh 难以仅由视觉估计。
- 当前文档提供 RoboVerse demo 向 LeRobot、RLDS、Zarr 等训练格式的工作流；这不等于已提供任意真机数据向 RoboVerse task/scene/dynamics 的通用导入器。
- 跨 simulator 的 state replay 能证明轨迹/画面桥接，不自动证明控制动力学等价或任务成功。

## 证据限制

- 本次未在 Linux/NVIDIA GPU 上安装并运行 RoboVerse；所有运行性能、后端一致性和目标硬件兼容性均待 PoC。
- 论文实验为作者报告，未做独立复现；直接 sim-to-real 任务数量和每任务试次有限。
- 仓库根代码是 Apache-2.0，但 README 明示资产许可证仍待补充；商业使用必须逐项做 dataset/asset/license lineage。
- GitHub API 自动抽取失败后仅留原始 HTML；具体 issue 标题来自本次只读 API 查询，不作为唯一关键证据。

## 关联连接

- [[RoboVerse|RoboVerse 实体页]]
- [[robotics-embodied-ai/research-notes/roboverse-platform-and-real-data-deep-dive-2026-07-28|RoboVerse 深度调研]]
- [[robotics-embodied-ai/research-notes/vla-world-model-data-infrastructure-platform-design-2026-07-06|VLA 与世界模型数据基建平台]]
- [[robotics-embodied-ai/research-notes/isaac-sim-vs-gazebo-vs-mujoco-2026-07-14|机器人仿真平台选型]]
- [[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]]
