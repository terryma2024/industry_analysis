---
title: DexCap 论文、官网与代码来源集
type: source
date_created: 2026-08-09
last_updated: 2026-08-09
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-277-dexcap-scalable-and-portable-mocap-data-collection-system-for-dexterous-manipula.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-502-dexcap-project-page.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-504-dexcap-official-code-repository-at-commit-4b0bed0.md
tags:
  - source/paper
  - source/github
  - industry/robotics-embodied-ai
  - dexterous-manipulation
status: active
---

# DexCap 论文、官网与代码来源集

> [!summary]
> 本来源集用 RSS 2024/arXiv 论文核验方法与实验，用项目官网核验演示和数据流，用固定提交 `4b0bed0966c87368f3cde4476aadb7585c3b94b5` 核验代码、格式、依赖与 MIT 许可证。综合判断见 [[robotics-embodied-ai/research-notes/dexcap-dexterous-mocap-data-collection-deep-dive-2026-08-09|DexCap 深度调研]]。

| SRC | 等级 | 用途 | 边界 |
|---|---:|---|---|
| [`SRC-robotics-277`](../../raw/robotics-embodied-ai/documents/SRC-robotics-277-dexcap-scalable-and-portable-mocap-data-collection-system-for-dexterous-manipula.md) | S | 硬件、DexIL、六任务、成功率与限制 | 作者实验，未独立复现 |
| [`SRC-robotics-502`](../../raw/robotics-embodied-ai/documents/SRC-robotics-502-dexcap-project-page.md) | S | 系统演示、数据流、human-in-loop | 项目自述，不是商业客户证据 |
| [`SRC-robotics-504`](../../raw/robotics-embodied-ai/documents/SRC-robotics-504-dexcap-official-code-repository-at-commit-4b0bed0.md) | S | 采集/处理/HDF5/训练流程与许可 | 未编译；第三方硬件/软件/数据许可另审 |

## 审阅快照

- 论文版本：arXiv v2 / RSS 2024，2024-07-04。
- GitHub：2026-08-09 查询时未归档，387 stars、35 forks、12 open issues；默认分支 head 的提交日为 2024-08-18。动态计数不是采用量或维护 SLA。
- 原论文 raw 已在仓库中，因此复用 `SRC-robotics-277`，没有重复创建论文 source ID。
- 未运行双 Franka/LEAP 硬件，也未复现训练；商业订单、客户、回款和复购均无一手证据。

## 关联连接

- [[DexCap]]
- [[robotics-embodied-ai/research-notes/dexcap-dexterous-mocap-data-collection-deep-dive-2026-08-09|DexCap 深度调研]]
- [[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]]

