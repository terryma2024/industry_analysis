---
title: LeRobot Dataset Schema
type: concept
date_created: 2026-05-29
last_updated: 2026-05-29
tags:
  - robotics
  - dataset-schema
  - lerobot
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-053-lerobotdataset-v3-0-documentation.md
  - robotics-embodied-ai/research-notes/lerobot-beginner-guide-2026-05-28.md
---

# LeRobot Dataset Schema

LeRobot Dataset Schema 是机器人数据工程中的一种标准化组织方式，通常把视觉数据、低维状态/动作、任务文本、episode 元数据和统计信息拆分存储，使数据能被统一 loader、训练脚本和评测流程复用。

## 本仓库使用方式

- 作为 UMI-like 数据包的默认客户交付格式之一。
- 与 HDF5/Zarr/RLDS/MCAP 并存，避免锁死客户训练栈。
- 初学者入口：[[robotics-embodied-ai/research-notes/lerobot-beginner-guide-2026-05-28|LeRobot 初学者教学]]。

## 关联连接

- [[robot-training-data]]
- [[universal-manipulation-interface]]
- [[_entities/HuggingFaceLeRobot|Hugging Face LeRobot]]
