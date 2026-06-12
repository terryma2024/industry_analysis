---
title: 集成电路 - 产业链地图
type: industry
date_created: 2026-05-29
last_updated: 2026-06-11
status: draft
tags:
  - industry/integrated-circuits
sources:
  - integrated-circuits/sources.csv
---

# 集成电路 - 产业链地图

## 产业链总览

| 环节 | 核心价值 | 代表公司/机构 | 关键壁垒 | 证据 |
| --- | --- | --- | --- | --- |
| EDA/IP | 提高芯片设计效率，降低验证失败风险 | Synopsys, Cadence, Arm | 软件生态、IP库、客户粘性、出口管制 | SRC-ic-016 |
| AI 芯片设计 | 直接承接训练/推理算力预算 | NVIDIA, AMD, Broadcom, Marvell, Intel, 寒武纪, 海光信息 | 架构、软件生态、客户验证、供应链绑定 | SRC-ic-001, SRC-ic-004, SRC-ic-005 |
| 晶圆代工 | 把设计转化为可量产芯片 | TSMC, Samsung, Intel Foundry, SMIC | 先进节点、良率、先进封装、资本开支 | SRC-ic-002, SRC-ic-006 |
| 存储/HBM | 决定 AI 加速器带宽和容量 | SK hynix, Micron, Samsung | TSV/堆叠、良率、客户认证、产能 | SRC-ic-012, SRC-ic-013 |
| 半导体设备 | 决定制程可达性和扩产速度 | ASML, AMAT, LRCX, KLAC, TEL, Advantest, Teradyne, 北方华创, 中微公司 | 光刻、刻蚀、沉积、检测、测试、服务网络 | SRC-ic-007, SRC-ic-016 |
| 材料/硅片/化学品 | 影响良率、可靠性和成本 | Entegris, Shin-Etsu, SUMCO, GlobalWafers | 纯度、认证周期、客户切换成本 | SRC-ic-016 |
| 先进封装/测试 | 把 GPU/ASIC 与 HBM 集成为系统级算力 | Amkor, ASE, JCET, Tongfu, Huatian | 2.5D/3D封装、测试复杂度、良率 | SRC-ic-010, SRC-ic-016 |
| PCB/载板/服务器硬件 | 承载高速互连、电力和系统集成 | Ibiden, Unimicron, Shennan, Victory Giant | 高速材料、良率、客户认证、产能 | SRC-ic-033, SRC-ic-034 |

## 价值流

- 谁付钱：云厂商、AI 模型公司、主权 AI/政府项目、企业数据中心、服务器 OEM/ODM、边缘终端厂商。
- 谁获益：短期集中在 NVIDIA、HBM、TSMC、ASML、先进封装和测试；中期可能扩散到 AMD、Broadcom/Marvell 定制 ASIC、光互连、PCB/载板和国产替代。
- 成本主要在哪里：先进 GPU/ASIC、HBM、先进节点晶圆、CoWoS/2.5D 封装、AI 服务器电力和散热。
- 利润池集中在哪里：设计生态和瓶颈设备最高；代工和 HBM 受供需紧张放大利润；封测/PCB 弹性强但议价弱。

## 关键瓶颈

- 供给瓶颈：HBM、先进封装、先进节点产能、测试能力、电力和液冷基础设施。
- 技术瓶颈：EUV/先进光刻、HBM 堆叠良率、CoWoS 类封装、GPU 软件生态、国产 EDA/IP。
- 监管瓶颈：美国出口管制、荷兰/日本设备出口限制、中国实体清单和先进算力进口限制。
- 渠道瓶颈：AI 加速器客户认证周期长，云厂商和模型公司的大订单高度集中。
- 人才瓶颈：芯片架构、编译器、EDA、先进封装工艺、良率工程、AI 系统软硬协同。

## 关联连接

- [[integrated-circuits/00-index|集成电路 - 研究入口]]
- [[integrated-circuits/07-ai-chip-global-supply-chain-and-stock-screen-2026-06-11|AI 芯片全球上市公司、供应链关系与股票初筛]]
