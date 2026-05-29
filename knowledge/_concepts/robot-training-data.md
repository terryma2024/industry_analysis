---
title: Robot Training Data
type: concept
date_created: 2026-05-29
last_updated: 2026-05-29
tags:
  - robotics
  - training-data
  - dataset-schema
sources:
  - robotics-embodied-ai/07-training-data.md
  - robotics-embodied-ai/09-training-data-deep-dive.md
---

# Robot Training Data

Robot Training Data 指用于训练、评测和改进机器人策略的数据资产，包括成功示教、失败轨迹、人工接管、恢复动作、任务文本、状态/动作序列、多模态观测和元数据。

## 当前判断

- 数据价值不只在 episode 数量，而在 schema、质检、失败/接管标注、格式转换、baseline 复现和客户训练栈适配。
- 国内 ToB 数据服务的早期收入可能来自“有效 episode + 标注/QC + baseline 结果 + 复采服务”。
- 深度调研入口：[[robotics-embodied-ai/09-training-data-deep-dive|机器人训练数据深度调研]]。

## 关联连接

- [[embodied-ai]]
- [[lerobot-dataset-schema]]
- [[universal-manipulation-interface]]
- [[_entities/HuggingFaceLeRobot|Hugging Face LeRobot]]
- [[_entities/IOAI|IO-AI]]
