---
title: Hugging Face LeRobot
type: entity
date_created: 2026-06-02
last_updated: 2026-06-02
aliases:
  - LeRobot
  - Hugging Face LeRobot
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-052-lerobot-github-repository.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-053-lerobotdataset-v3-0-documentation.md
  - knowledge/robotics-embodied-ai/08-umi-gripper-research-and-business-plan.md
tags:
  - entity/tool
  - industry/robotics-embodied-ai
  - umi
status: active
---

# Hugging Face LeRobot

## 初学者解释

LeRobot 是 Hugging Face 推出的机器人学习工具链，包含数据格式、数据集、训练、评测和部署相关工具。

它的重要性在于降低机器人数据和模型训练的工程门槛。

UMI 报告建议支持 LeRobot，是因为客户可能希望直接用开源工具加载和训练数据。

入门教学见 [[robotics-embodied-ai/research-notes/lerobot-beginner-guide-2026-05-28]]。

## 补充说明

补充：LeRobot 的价值是把机器人数据从“私有脚本可读”推向“社区工具可加载、可训练、可复现”。数据服务商若支持 LeRobot，可以降低客户验收和二次训练成本。

## 在 UMI 数据闭环中的位置

- **采集侧：** 判断它是否影响传感器选择、操作者 SOP、标定、时间同步或原始数据质量。
- **处理侧：** 判断它是否影响轨迹恢复、字段设计、数据格式、episode 切分和质量等级。
- **训练/部署侧：** 判断它是否影响 policy 输入输出、机器人可执行性、rollout 成功率和跨本体迁移。

## 易错边界

- 不要只按字面翻译理解；在机器人数据里，它通常和坐标系、时间轴、动作表示、数据 schema 共同起作用。
- 不要把“能记录”误认为“可训练”；只有经过标定、同步、质检并能被训练代码读取的数据，才有稳定商业价值。
- 如果用于 ToB 交付，应明确记录字段定义、单位、采样率、质量等级和失败口径。

## 关联连接

- [[DatasetSchema]]
- [[Zarr]]
- [[DataPackage]]
- [[robotics-embodied-ai/08-umi-gripper-research-and-business-plan|UMI Gripper 研究与业务计划]]
- [[_entities/README|UMI 技术术语实体索引]]
