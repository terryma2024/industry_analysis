---
title: 集成电路 - 公司与竞争
type: industry
date_created: 2026-05-29
last_updated: 2026-06-11
status: draft
tags:
  - industry/integrated-circuits
sources:
  - integrated-circuits/sources.csv
  - raw/integrated-circuits/data/ai_chip_listed_company_universe_2026-06-11.csv
---

# 集成电路 - 公司与竞争

## 公司分层

| 公司 | 环节 | 商业模式 | 客户 | 优势 | 风险 | 证据 |
| --- | --- | --- | --- | --- | --- | --- |
| NVIDIA | AI GPU/系统 | GPU、网络、系统、软件生态 | 云厂商、AI公司、企业、主权AI | 财报兑现最强，CUDA生态 | 客户集中、出口管制、估值 | SRC-ic-001 |
| TSMC | 晶圆代工/先进封装 | 按晶圆和封装产能收费 | AMD、Apple、Broadcom、NVIDIA 等公开报道客户 | 先进节点和产能稀缺 | 台湾地缘、capex周期 | SRC-ic-006 |
| ASML | 光刻设备 | 设备销售和服务 | 全球先进晶圆厂 | EUV 稀缺 | 出口管制、订单周期 | SRC-ic-007 |
| SK hynix | HBM/DRAM | 存储芯片销售 | NVIDIA 等 AI 平台客户 | HBM 领先，供需紧 | 存储周期、客户集中 | SRC-ic-012 |
| Micron | HBM/DRAM/NAND | 存储芯片销售 | NVIDIA H200 等 | 美国 HBM 暴露 | 存储周期 | SRC-ic-013 |
| Broadcom | 定制 ASIC/网络 | 定制芯片、网络芯片、软件 | OpenAI 等超大客户/未披露客户 | 定制 ASIC 和网络双暴露 | 客户集中、毛利结构 | SRC-ic-005 |
| AMD | AI GPU/CPU | GPU/CPU 销售 | OpenAI、Oracle 等公开报道客户 | 第二供给源，份额提升 | 软件生态和兑现节奏 | SRC-ic-004 |
| AMAT/LRCX/KLAC/TEL | 半导体设备 | 设备+服务 | 晶圆厂/存储厂 | 受益先进制程和存储扩产 | 设备周期、出口限制 | SRC-ic-016 |
| Cadence/Synopsys/Arm | EDA/IP | 软件授权、IP授权、版税 | 芯片设计公司 | 高毛利、高粘性 | 出口限制、估值 | SRC-ic-016 |
| Amkor/ASE/JCET/Tongfu/Huatian | 封装测试 | 封装和测试服务 | 芯片设计/IDM/代工生态 | 先进封装需求提升 | 毛利低、客户议价强 | SRC-ic-010 |
| 寒武纪/海光信息 | 中国 AI 芯片 | 加速器、CPU/DCU、软件栈 | 中国数据中心/政企客户待逐项核验 | 国产替代弹性 | 制程、生态、估值 | SRC-ic-023, SRC-ic-024 |
| 北方华创/中微公司/拓荆/华海清科 | 中国设备 | 设备销售和服务 | 国内晶圆厂 | 国产替代核心 | 技术差距、订单周期 | SRC-ic-026 至 SRC-ic-029 |

## 竞争格局

- 集中度：AI GPU 高度集中在 NVIDIA；先进代工集中在 TSMC；EUV 集中在 ASML；HBM 集中在 SK hynix/Micron/Samsung；EDA 集中在 Synopsys/Cadence/Siemens EDA。
- 进入壁垒：软件生态、客户认证、先进制程产能、HBM/封装良率、设备工艺 know-how。
- 价格/成本趋势：HBM 和先进封装短期供需紧张；设备和 PCB 更受 capex 周期影响；GPU/ASIC 长期看单位算力成本下降但总量上升。
- 新进入者：云厂商自研 ASIC、OpenAI 等模型公司定制芯片、中国国产 AI 芯片公司。
- 替代者：ASIC 替代部分 GPU 推理负载；国产芯片替代受限进口芯片；端侧 AI 分流部分云端推理需求。

## 需要跟踪的公司

- 上市公司：见 `raw/integrated-circuits/data/ai_chip_listed_company_universe_2026-06-11.csv`。
- 未上市公司：Huawei Ascend/海思、Biren、Moore Threads、Iluvatar、燧原、沐曦、曦智科技等需要另建未上市观察表。
- 海外公司：NVIDIA、AMD、Broadcom、Marvell、TSMC、ASML、SK hynix、Micron、Samsung、AMAT、LRCX、KLAC、TEL、Advantest、Teradyne。
- 产业链关键供应商：HBM、先进封装、EUV、测试、光互连、PCB/载板。

## 关联连接

- [[integrated-circuits/07-ai-chip-global-supply-chain-and-stock-screen-2026-06-11|AI 芯片全球上市公司、供应链关系与股票初筛]]
- [[integrated-circuits/05-investment-view|集成电路 - 投资视角]]
