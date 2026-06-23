---
title: Diffusion Policy
type: entity
date_created: 2026-06-02
last_updated: 2026-06-02
aliases:
  - Diffusion Policy
  - 扩散策略
sources:
  - knowledge/robotics-embodied-ai/08-umi-gripper-research-and-business-plan.md
tags:
  - entity/model
  - industry/robotics-embodied-ai
  - umi
status: active
---

# Diffusion Policy

## 初学者解释

Diffusion Policy 是一种机器人模仿学习方法，使用扩散模型生成一段连续动作。

初学可以把它理解成：模型不是只预测下一步，而是预测接下来一小段平滑动作。

UMI 原文主要使用 Diffusion Policy 做训练。

## 补充说明

补充：Diffusion Policy 更适合把连续、平滑、多峰的操作动作建模成一段 action trajectory，但训练质量高度依赖 episode 切分、动作频率、图像质量和 rollout 评测。

## 在 UMI 数据闭环中的位置

- **采集侧：** 判断它是否影响传感器选择、操作者 SOP、标定、时间同步或原始数据质量。
- **处理侧：** 判断它是否影响轨迹恢复、字段设计、数据格式、episode 切分和质量等级。
- **训练/部署侧：** 判断它是否影响 policy 输入输出、机器人可执行性、rollout 成功率和跨本体迁移。

## 易错边界

- 不要只按字面翻译理解；在机器人数据里，它通常和坐标系、时间轴、动作表示、数据 schema 共同起作用。
- 不要把“能记录”误认为“可训练”；只有经过标定、同步、质检并能被训练代码读取的数据，才有稳定商业价值。
- 如果用于 ToB 交付，应明确记录字段定义、单位、采样率、质量等级和失败口径。

## 关联连接

- [[ImitationLearning]]
- [[PolicyModel]]
- [[Rollout]]
- [[robotics-embodied-ai/08-umi-gripper-research-and-business-plan|UMI Gripper 研究与业务计划]]
- [[_entities/README|UMI 技术术语实体索引]]
