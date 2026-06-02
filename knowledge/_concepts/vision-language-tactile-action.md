---
title: Vision-Language-Tactile-Action
type: concept
date_created: 2026-06-02
last_updated: 2026-06-02
sources:
  - robotics-embodied-ai/11-embodied-ai-data-service-companies-2026-06-02.md
  - robotics-embodied-ai/07-training-data.md
tags:
  - robotics
  - embodied-ai
  - multimodal-model
  - tactile
status: draft
aliases:
  - VLTA
  - VTLA
  - Vision-Language-Tactile-Action Model
  - 视觉-语言-触觉-动作模型
---

# Vision-Language-Tactile-Action

Vision-Language-Tactile-Action 指一种面向机器人操作的多模态模型/数据范式：模型同时利用**视觉**、**语言指令**、**触觉/力觉反馈**和**动作轨迹**来理解任务并输出机器人可执行动作。按英文首字母更严格应写作 **VLTA**；部分公司或媒体也会写作 **VTLA**，本仓库把两者视为同一类“视觉/语言/触觉/动作”具身模型路线，但引用具体公司资料时保留原文写法。

## 四个组成部分

| 模态 | 含义 | 在机器人任务中的作用 |
|---|---|---|
| Vision | RGB、深度、多视角、点云、对象 mask、位姿等视觉观测 | 识别物体、场景、空间关系、可抓取区域和任务进展。 |
| Language | 人类指令、任务描述、步骤标注、推理链或语义标签 | 把开放任务转成可执行步骤，并支持泛化到新物体/新场景。 |
| Tactile | 触觉、力/力矩、接触状态、滑移、压力分布、灵巧手传感数据 | 补足视觉看不到的接触信息，尤其用于抓取、插接、柔性物体、擦拭、装配等接触丰富任务。 |
| Action | 末端位姿、关节角、夹爪开合、手指动作、底盘运动、控制频率和轨迹 | 作为模型输出或训练监督，让模型从“理解”进入“控制物理世界”。 |

## 和 VLA 的区别

VLA（Vision-Language-Action）通常用视觉和语言条件生成动作，适合很多抓取、移动和长程任务。VLTA/VTLA 在 VLA 的基础上加入 tactile/force feedback，更适合接触状态决定成败的任务：例如插拔线束、拧盖、整理柔性物体、按压、擦拭、双手协作和灵巧手操作。

一句话区分：

- **VLA**：主要回答“我看见什么、要做什么、下一步怎么动”。
- **VLTA/VTLA**：进一步回答“我碰到了什么、力度是否合适、是否滑移/卡住、需要如何微调动作”。

## 对数据采集公司的含义

VLTA/VTLA 抬高了具身数据服务的门槛。数据供应商不能只交付视频和文本标签，还需要处理传感器标定、时间同步、触觉/力觉噪声、接触事件切片、失败/恢复标签和跨本体动作重定向。拥有触觉传感器、灵巧手、手套、遥操作和真机评测能力的公司，会比纯视频采集公司更容易形成差异化。

## 当前判断

- 对中国具身智能数据公司来说，触觉数据可能是从“普通数据外包”升级到“高壁垒数据资产”的关键模态。
- VLTA/VTLA 是否真正有效，不能只看数据量或宣传口径，还要看加入触觉后对真实任务成功率、泛化、鲁棒性和失败恢复的提升。
- 帕西尼、它石、智元、简智等公司都在不同程度触及该路线，但公开资料中模型 benchmark、数据许可和可复现训练结果仍不足。

## 关联连接

- [[embodied-ai]]
- [[robot-training-data]]
- [[lerobot-dataset-schema]]
- [[robotics-embodied-ai/11-embodied-ai-data-service-companies-2026-06-02|具身智能数据采集和服务公司对比]]
