---
title: Microduck
type: entity
date_created: 2026-09-02
last_updated: 2026-09-02
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-559-microduck-official-press-kit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-560-microduck-runtime-official-repository-at-commit-2c61dcc.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-561-microduck-rl-official-repository-at-commit-badc4e7.md
tags:
  - entity/product
  - industry/robotics-embodied-ai
  - reinforcement-learning
  - biped-robot
  - sim-to-real
status: active
aliases:
  - Microduck 双足机器鸭
  - Pollen Robotics Microduck
---

# Microduck

> [!summary]
> Microduck 是 Pollen Robotics / Hugging Face 于 2026-08-27 开放预售的 25 cm 桌面双足机器人，定位是可玩、可编程的强化学习与 sim-to-real 教学平台。399 美元是税费和运费前的预售价；截至 2026-09-02 尚未完成首批交付，因此真实用户的可靠性、售后与课程价值仍待验证。

## 产品事实快照

| 字段 | 当前可核验内容 | 边界 |
|---|---|---|
| 厂商 | Pollen Robotics，Hugging Face 机器人团队 | 官方口径 |
| 状态 | 2026-08-27 开放预售，首批目标在 2026 年圣诞节前交付 | 交付目标不是交付事实 |
| 价格 | 399 美元，税费与运费另计 | 介绍价，可变 |
| 尺寸与重量 | 25 cm 高、14 cm 宽、不足 800 g | press kit；部分规格仍标为 provisional |
| 执行机构 | 15 个关节：左腿 5、头颈/嘴 5、右腿 5 | runtime 固定提交 |
| 策略接口 | 61 维观测、14 维动作；嘴由独立控制逻辑驱动 | runtime / RL 固定提交 |
| 计算 | Rockchip RK3566，1 GB RAM、32 GB 存储 | 官方 press kit |
| 传感 | 前置相机、8×8 ToF、头部与机身各一个 IMU、两个 NFC 天线、麦克风与扬声器 | 相机、无线与 SDK 细节仍可能变化 |
| 策略循环 | 50 Hz onboard policy loop | 当前实现目标，不等于全系统硬实时保证 |
| 电池 | 可拆 NP-F550，官方写 2600 mAh、约 1 小时 | 续航随动作而变 |

## 软件与许可

- `pollen-robotics/microduck` 是 Rust runtime：`robotd` 持有控制循环和舵机总线，其他 daemon 负责更新、配置、蓝牙、手柄、相机与 ToF；内部使用 Unix socket JSON-RPC。
- `pollen-robotics/microduck_rl` 使用 MuJoCo/mjlab 与 PPO 训练，导出 ONNX 后部署到实机；训练需要 CUDA GPU，也可转用 Hugging Face Jobs。
- 两个仓库代码均为 Apache-2.0；RL 仓库声明 3D model files 为 `CC BY-SA-NC`。
- 官方“开源”只覆盖软件。机械和电子设计文件不开放，不能把 Microduck 描述为开源硬件。

## 适用与不适用

### 适用

- 强化学习、MuJoCo、PPO、域随机化、执行器建模与 ONNX 部署教学。
- 小型双足运动、跌倒恢复、头部控制和策略热切换实验。
- 开源机器人 runtime、更新回滚、遥控与传感器服务的系统工程学习。

### 不适用

- 工业节拍、载荷、寿命或功能安全验证。
- 把官方仿真模型直接当作完整硬件制造包。
- 在首批交付前据此判断大规模售后、可靠性或二手生态。

## 购买与 DIY 决策

| 目标 | 更合理路径 | 原因 |
|---|---|---|
| 学 RL 与 sim-to-real | 等首批交付后购买整机，先用官方仿真栈学习 | 零售 15 个 XL330 的美国官网总价已高于整机预售价 |
| 学机械、电源与嵌入式 | 设计独立的功能相似平台 | 官方机械/电子设计不开放，复刻本身就是研发项目 |
| 做课程或研究平台 | 先用仿真验证课程，再采购小批量实机 | 降低预售、可靠性和售后不确定性 |
| 做商业硬件 | 重新设计机械电子并逐项审查许可、商标、专利与安全 | 仿真 3D 模型是非商业许可，官方也未开放硬件设计 |

## 待验证

- 最终量产相机、ToF 代次、无线版本、SDK 语言和年龄建议。
- 首批交付日期、真实续航、跌落/舵机寿命、备件供应、售后与中国购买总成本。
- 官方预训练策略在不同地面、电池状态、碰撞和长期连续运行下的成功率。

## 关联连接

- [[wechat-microduck-diy-replica-analysis|Microduck DIY 复刻文章来源卡]]
- [[robotics-embodied-ai/research-notes/microduck-diy-replication-feasibility-2026-09-02|Microduck DIY 复刻可行性与教学平台选型]]
- [[robotics-embodied-ai/02-technology-and-products|机器人技术与产品]]
- [[HuggingFaceLeRobot|Hugging Face LeRobot]]
- [[BillOfMaterials|BOM]]
- [[IMU]]
- [[LiDAR]]
