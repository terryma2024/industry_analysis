---
title: 自变量机器人视频深度调研
type: synthesis
date_created: 2026-07-11
last_updated: 2026-07-11
sources:
  - knowledge/_sources/bilibili-bv1utnj6ge75-200.md
  - raw/_inbox/transcripts/2026-07-11-bilibili-bv1utnj6ge75-200.json
tags: [bilibili, embodied-ai, robotics, company-research]
status: active
---

# 自变量机器人视频深度调研

> [!warning] 证据边界
> 视频为 B 级线索。官网 `SRC-robotics-243` 确认公司 2023 年 12 月成立、端到端具身模型定位、WALL-A/WALL-B、四地布局与部分投资方；估值、融资、客户、收入、任务成功率和硬件参数仍未获一级证实。

## 视频主线

视频把公司叙事为“通用具身模型 + 自研本体 + 真实数据 + 场景交付”闭环。这个框架有研究价值，但不能把“模型方向存在”推导为“商业化已经成立”。

## 事实、估计、判断与假设

| 类型 | 内容 | 处理 |
|---|---|---|
| 事实 | 官网披露 WALL-A、WALL-B、端到端路线、量子系列与无本体数采入口。 | `SRC-robotics-243` |
| 视频线索 | 200 亿估值、多轮融资、汽车/物流/家庭客户、营收和模型成功率。 | 待融资公告、客户侧案例、模型卡/论文验证。 |
| 判断 | 真正的壁垒不是单一“机器人脑”，而是数据质量、本体接口、失败恢复和客户 ROI 的联合闭环。 | 研究判断。 |
| 假设 | 低成本采集、世界统一模型和家庭数据会持续改善跨场景任务。 | 用 held-out 真机任务、无人干预率和单位有效 episode 成本检验。 |

## 产业、投资与职业启发

- 产业：把现场失败、修正、回退动作沉淀为可版本化 episode，才可能形成数据壁垒。
- 投资：优先查客户公告、复购、无人干预成功率、毛利和现金消耗；只看融资新闻或 demo 不足以支撑高估值。
- 职业：数据工程、传感同步、VLA 评测、现场系统集成与安全验收是更稀缺的组合。

## 风险与后续验证

- 定位 WALL-B/WALL-OSS 的模型卡、训练数据许可、评测协议、权重和代码。
- 用投资方公告/工商变更核验融资与估值；用客户侧公告核验部署、订单与 ROI。
- 在家庭/工业场景记录故障率、人工接管、维护成本和安全边界。

## 关联连接

- [[_concepts/embodied-ai|Embodied AI]]
- [[_concepts/robot-training-data|Robot Training Data]]
- [[robotics-embodied-ai/04-companies|机器人公司与竞争格局]]
- [[robotics-embodied-ai/05-investment-view|机器人投资视角]]
