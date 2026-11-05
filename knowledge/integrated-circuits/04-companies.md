---
title: 集成电路 - 公司与竞争
type: industry
date_created: 2026-05-29
last_updated: 2026-09-22
status: draft
tags:
  - industry/integrated-circuits
sources:
  - integrated-circuits/sources.csv
  - raw/integrated-circuits/data/ai_chip_listed_company_universe_2026-06-11.csv
  - raw/integrated-circuits/data/china-gpu-ai-chip-investment-comparison-2026-09-22.csv
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
| 华为昇腾 | 中国 AI 芯片/系统 | NPU、整机、SuperPoD、CANN | 数据中心、政企、运营商 | 系统工程、交付与生态 | 非上市；昇腾分部财务不披露 | SRC-ic-068, SRC-ic-069 |
| 寒武纪 | 中国 AI 加速器 | MLU、NeuWare、云端产品 | 中国数据中心/政企 | AI 专注、收入利润快速兑现 | 产品和客户集中、估值 | SRC-ic-077 至 SRC-ic-079 |
| 海光信息 | 中国 CPU/DCU | x86 兼容 CPU、DCU、DTK | 数据中心、政企、科研 | CPU+DCU 组合、规模与利润 | 关联客户集中、分部透明度 | SRC-ic-080, SRC-ic-081 |
| 摩尔线程 | 中国全功能 GPU | MUSA、GPU、集群 | AI、图形、HPC、云桌面 | 通用生态期权 | 扣非与现金流待验证 | SRC-ic-070 至 SRC-ic-072 |
| 沐曦股份 | 中国 GPGPU | N/C/G/X 产品族、MXMACA | AI、图形、HPC | 产品族清晰、收入增长 | 核心盈利与现金流待验证 | SRC-ic-073 至 SRC-ic-076 |
| 北方华创/中微公司/拓荆/华海清科 | 中国设备 | 设备销售和服务 | 国内晶圆厂 | 国产替代核心 | 技术差距、订单周期 | SRC-ic-026 至 SRC-ic-029 |

## 竞争格局

- 集中度：AI GPU 高度集中在 NVIDIA；先进代工集中在 TSMC；EUV 集中在 ASML；HBM 集中在 SK hynix/Micron/Samsung；EDA 集中在 Synopsys/Cadence/Siemens EDA。
- 进入壁垒：软件生态、客户认证、先进制程产能、HBM/封装良率、设备工艺 know-how。
- 价格/成本趋势：HBM 和先进封装短期供需紧张；设备和 PCB 更受 capex 周期影响；GPU/ASIC 长期看单位算力成本下降但总量上升。
- 新进入者：云厂商自研 ASIC、OpenAI 等模型公司定制芯片、中国国产 AI 芯片公司。
- 替代者：ASIC 替代部分 GPU 推理负载；国产芯片替代受限进口芯片；端侧 AI 分流部分云端推理需求。

## 需要跟踪的公司

- 上市公司：见 `raw/integrated-circuits/data/ai_chip_listed_company_universe_2026-06-11.csv`。
- 已上市国产算力：寒武纪、海光信息、摩尔线程、沐曦股份；详见公司投资比较报告。
- 未上市公司：Huawei Ascend/海思、壁仞科技、天数智芯、燧原科技、曦智科技等需单独建立观察表；华为为非上市集团，不应使用公开市值口径横比。
- 海外公司：NVIDIA、AMD、Broadcom、Marvell、TSMC、ASML、SK hynix、Micron、Samsung、AMAT、LRCX、KLAC、TEL、Advantest、Teradyne。
- 产业链关键供应商：HBM、先进封装、EUV、测试、光互连、PCB/载板。

## 关联连接

- [[integrated-circuits/07-ai-chip-global-supply-chain-and-stock-screen-2026-06-11|AI 芯片全球上市公司、供应链关系与股票初筛]]
- [[integrated-circuits/research-notes/china-gpu-ai-chip-providers-investment-comparison-2026-09-22|中国 GPU 与 AI 芯片提供商投资比较]]
- [[integrated-circuits/05-investment-view|集成电路 - 投资视角]]
