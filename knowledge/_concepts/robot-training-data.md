---
title: Robot Training Data
type: concept
date_created: 2026-05-29
last_updated: 2026-08-11
tags:
  - robotics
  - training-data
  - dataset-schema
sources:
  - robotics-embodied-ai/07-training-data.md
  - robotics-embodied-ai/09-training-data-deep-dive.md
  - robotics-embodied-ai/research-notes/embodied-ai-model-data-processing-pipeline-2026-08-11.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-529-50-vs-ego-roadmap.md
---

# Robot Training Data

Robot Training Data 指用于训练、评测和改进机器人策略的数据资产，包括成功示教、失败轨迹、人工接管、恢复动作、任务文本、状态/动作序列、多模态观测和元数据。

## 当前判断

- 数据价值不只在 episode 数量，而在 schema、质检、失败/接管标注、格式转换、baseline 复现和客户训练栈适配。
- 国内 ToB 数据服务的早期收入可能来自“有效 episode + 标注/QC + baseline 结果 + 复采服务”。
- 深度调研入口：[[robotics-embodied-ai/09-training-data-deep-dive|机器人训练数据深度调研]]。

## 数据处理闭环

具身数据的“处理”从采集前开始，最小闭环是：

1. 冻结任务、观测、动作、坐标/单位、时间基准、episode 与许可契约。
2. 保存不可覆盖的 raw，并记录传感器时间戳、标定、设备和软件版本。
3. 完成时间对齐、标定与自动质量门，再投入人工标注。
4. 切分 episode、技能阶段、成功/失败、接管与恢复事件。
5. 保留 robot-native action，同时编译 canonical action 和训练 schema。
6. 按场景、对象、操作者、设备和任务做无泄漏 split 与版本化 dataset recipe。
7. 用 baseline 和真实 holdout 验证数据能否提升任务，而不是只验证 loader 可读。
8. 把部署失败、低置信、接管和恢复回流为下一轮定向补采。

详细工程拆解见 [[robotics-embodied-ai/research-notes/embodied-ai-model-data-processing-pipeline-2026-08-11|具身智能模型数据处理闭环]]。

> [!warning]
> 不应把某个固定毫秒数当作所有任务的同步阈值，也不应把数据小时数、文件可读或训练 loss 下降当作任务价值。阈值必须来自目标运动速度、传感器机制和允许误差；最终证据是未参与调参的真实任务表现。

## 关联连接

- [[embodied-ai]]
- [[lerobot-dataset-schema]]
- [[robotics-embodied-ai/research-notes/embodied-ai-model-data-processing-pipeline-2026-08-11|具身智能模型数据处理闭环]]
- [[universal-manipulation-interface]]
- [[_entities/HuggingFaceLeRobot|Hugging Face LeRobot]]
- [[_entities/IOAI|IO-AI]]
