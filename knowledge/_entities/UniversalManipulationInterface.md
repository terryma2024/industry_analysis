---
title: Universal Manipulation Interface
type: entity
date_created: 2026-06-02
last_updated: 2026-06-02
aliases:
  - UMI
  - Universal Manipulation Interface
  - 通用操作示教接口
sources:
  - knowledge/robotics-embodied-ai/08-umi-gripper-research-and-business-plan.md
tags:
  - entity/project
  - industry/robotics-embodied-ai
  - umi
status: active
---

# Universal Manipulation Interface

## 初学者解释

UMI 是 Universal Manipulation Interface 的缩写，可以理解为“通用操作示教接口”。

它的基本思路是：不用每次都拿真实机器人遥操作，而是让人拿一个像机器人夹爪的手持设备去真实环境做任务，再把这个过程转成机器人可训练的数据。

在 UMI 报告中，它代表一条低成本、可移动、真实场景采集路线。

容易误解：UMI 不是一个普通夹爪硬件。夹爪只是入口，核心是“硬件 + 轨迹恢复 + 数据格式 + 训练接口”这一整套流程。

## 补充说明

补充：UMI 的产业价值不在单个夹爪，而在把人类示教、传感器标定、轨迹恢复、数据 schema、训练 recipe 和真机验证连成低成本闭环。它适合早期机器人公司快速积累操作数据，但不自动解决跨本体迁移。

## 在 UMI 数据闭环中的位置

- **采集侧：** 判断它是否影响传感器选择、操作者 SOP、标定、时间同步或原始数据质量。
- **处理侧：** 判断它是否影响轨迹恢复、字段设计、数据格式、episode 切分和质量等级。
- **训练/部署侧：** 判断它是否影响 policy 输入输出、机器人可执行性、rollout 成功率和跨本体迁移。

## 易错边界

- 不要只按字面翻译理解；在机器人数据里，它通常和坐标系、时间轴、动作表示、数据 schema 共同起作用。
- 不要把“能记录”误认为“可训练”；只有经过标定、同步、质检并能被训练代码读取的数据，才有稳定商业价值。
- 如果用于 ToB 交付，应明确记录字段定义、单位、采样率、质量等级和失败口径。

## 关联连接

- [[Gripper]]
- [[SLAM]]
- [[HuggingFaceLeRobot|LeRobot]]
- [[DiffusionPolicy]]
- [[DataPackage]]
- [[robotics-embodied-ai/08-umi-gripper-research-and-business-plan|UMI Gripper 研究与业务计划]]
- [[_entities/README|UMI 技术术语实体索引]]
