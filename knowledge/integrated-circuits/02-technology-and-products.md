---
title: 集成电路 - 技术和产品
type: industry
date_created: 2026-05-29
last_updated: 2026-06-11
status: draft
tags:
  - industry/integrated-circuits
sources:
  - integrated-circuits/sources.csv
---

# 集成电路 - 技术和产品

## AI 芯片技术栈

| 技术/产品 | 解决的问题 | 代表公司 | 投资观察 |
| --- | --- | --- | --- |
| GPU | 通用训练/推理加速，生态成熟 | NVIDIA, AMD | NVIDIA 生态和规模领先；AMD 通过大客户协议证明替代价值。 |
| 定制 ASIC/XPU | 为特定模型/推理负载优化成本和能耗 | Broadcom, Marvell, Google/TPU 生态 | 适合超大客户自研；订单大但客户集中、项目制强。 |
| CPU/DPU/NIC/交换芯片 | AI 集群调度、数据移动、网络互连 | Intel, AMD, NVIDIA, Broadcom, Marvell | AI 不只需要 GPU，网络和CPU逐步成为系统瓶颈。 |
| HBM | 给 GPU/ASIC 提供高带宽内存 | SK hynix, Micron, Samsung | 当前最紧缺环节之一，强周期属性明显。 |
| 先进节点 | 提升能效和晶体管密度 | TSMC, Samsung, Intel Foundry, SMIC | TSMC 先进节点是全球 AI 设计公司的共因子。 |
| 先进封装 | 集成 GPU/ASIC、HBM、chiplet | TSMC, Amkor, ASE, JCET, Tongfu | CoWoS/2.5D/3D 是 AI 系统产能瓶颈。 |
| EDA/IP | 支撑复杂芯片设计和验证 | Synopsys, Cadence, Arm | 软件/IP 质量高，但短期弹性较硬件小。 |
| 测试/量测 | 提升良率和出货可靠性 | KLA, Advantest, Teradyne | 芯片越大、封装越复杂，测试/量测越重要。 |

## 中国技术位置

- 相对强项：封装测试、PCB、成熟制程、部分刻蚀/沉积/CMP设备、AI 芯片应用侧适配。
- 相对短板：先进光刻、先进 GPU 生态、HBM、先进封装高端产能、EDA/IP、先进制程良率。
- 可行路径：先围绕“可获得算力”做系统级优化，包括国产 AI 芯片、模型压缩、推理优化、集群网络、国产设备和先进封装补链。

## 关联连接

- [[integrated-circuits/00-index|集成电路 - 研究入口]]
- [[integrated-circuits/01-industry-map|集成电路 - 产业链地图]]
