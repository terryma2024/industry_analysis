---
title: AI 芯片全球上市公司、供应链关系与股票初筛
type: synthesis
date_created: 2026-06-11
last_updated: 2026-06-11
sources:
  - integrated-circuits/sources.csv
  - raw/integrated-circuits/data/ai_chip_listed_company_universe_2026-06-11.csv
tags:
  - industry/integrated-circuits
  - topic/ai-chip
  - investing
status: draft
---

# AI 芯片全球上市公司、供应链关系与股票初筛

> 本页是第一版可复用研究资产，不构成投资建议。所有“供应链关系”只记录公开财报、公司公告或公开报道中明确出现的关系；未披露客户不做猜测。市值数据优先采用 StockAnalysis 截至 2026-06-09/10 的 market-cap 页面；StockAnalysis 未覆盖的部分日韩台港股使用 CompaniesMarketCap 的 2026-06 页面；仍未完成统一抓取的 A/H 股标为 `needs_local_quote`。

## 数据资产

- 可筛选 CSV: `raw/integrated-circuits/data/ai_chip_listed_company_universe_2026-06-11.csv`，已包含 `pe_ttm`、`forward_pe`、`pe_data_date`、`pe_source`、`pe_notes`。
- 来源表: [[integrated-circuits/sources|integrated-circuits/sources.csv]]
- 本页和 `04-companies.md` 使用相同口径：`AI 直接暴露`、`供应链瓶颈`、`财报兑现`、`估值/周期风险` 分开看。

## 研究边界

### 包含

- 数据中心 AI 训练/推理芯片：GPU、ASIC/XPU、AI CPU、AI 加速卡。
- 上游关键环节：EDA/IP、晶圆代工、HBM/DRAM、设备、材料、先进封装、测试、PCB/载板。
- 中国国产替代链：AI 芯片设计、国产设备、封测、PCB/载板、存储接口。

### 不包含

- 只做 AI 应用或云服务、但没有芯片/硬件供应链上市暴露的公司。
- 没有上市主体的 AI 芯片创业公司；只在需要解释竞争格局时备注。
- 未经公开确认的客户关系，例如“某芯片一定由某代工厂生产”但没有公开来源支撑的说法。

## 产业链分层

| 层级 | AI 芯片价值 | 全球代表上市公司 | 中国代表上市公司 | 关键判断 |
| --- | --- | --- | --- | --- |
| 架构/IP/EDA | 决定芯片设计效率和生态入口 | Arm, Synopsys, Cadence | 概伦电子、华大九天等待补 | 软件/IP 高毛利，直接收入弹性小于 GPU/HBM，但质量更稳。 |
| AI 芯片设计 | 直接吃训练/推理算力预算 | NVIDIA, AMD, Broadcom, Marvell, Intel | 寒武纪、海光信息、澜起科技 | NVIDIA 已财报兑现；AMD/Broadcom 是第二供给和定制 ASIC 弹性；中国公司更偏政策与国产替代弹性。 |
| 晶圆代工 | 先进节点与 CoWoS/先进封装产能 | TSMC, Samsung, Intel Foundry, GlobalFoundries | SMIC | TSMC 是当前 AI 芯片制造瓶颈核心；中国先进节点受设备和制裁约束。 |
| HBM/存储 | AI 加速器的带宽和容量瓶颈 | SK hynix, Micron, Samsung | 兆易创新/长鑫相关上市映射待补 | HBM 是 2025-2026 最强利润池之一，但强周期属性必须单独折价。 |
| 设备 | 扩产 capex 入口 | ASML, AMAT, LRCX, KLAC, TEL, Advantest, Teradyne | 北方华创、中微公司、拓荆科技、华海清科 | ASML/EUV 是稀缺瓶颈；刻蚀、沉积、检测、测试受先进节点/HBM扩产拉动。 |
| 材料 | 消耗品和良率基础 | Entegris, Shin-Etsu, SUMCO, GlobalWafers | 沪硅产业、安集科技、鼎龙股份等待补 | 复购属性强，但多数不是纯 AI。 |
| 先进封装/测试 | GPU+HBM 集成瓶颈 | Amkor, ASE, Ibiden, Shinko, BESI | 长电科技、通富微电、华天科技 | CoWoS/2.5D/测试复杂度提升；毛利和客户议价低于设计/设备。 |
| PCB/载板/服务器链 | AI server/rack 信号和电力连接 | Ibiden, Unimicron, Nan Ya PCB | 深南电路、胜宏科技、生益科技 | 弹性强但更周期，需跟踪订单和扩产兑现。 |

## 已公开确认的供应链/客户关系

| 关系 | 证据等级 | 来源 | 投资含义 | 不写的内容 |
| --- | --- | --- | --- | --- |
| NVIDIA FY2026 收入 $215.9B，Q4 Data Center 收入 $62.3B | S | NVIDIA FY2026 results | AI GPU 需求已体现在财报，不只是概念 | 不推断未披露客户名称。 |
| TSMC Q1 2026 HPC 收入占比 61%，先进节点 7nm 及以下占 74% wafer revenue | A/B | IBD/Tom's Hardware 转述 TSMC 财报/电话会 | AI/HPC 已成为 TSMC 核心增量，先进节点产能紧张 | 不把所有 HPC 都等同于 AI。 |
| TSMC 为 AMD、Apple、Broadcom、NVIDIA 等 fabless 客户生产芯片 | B | IBD 公开报道 | TSMC 是 AI 芯片设计公司的关键制造共因子 | 不推断具体产品节点。 |
| Micron HBM3E 用于 NVIDIA H200 | B | Investopedia 转述 Micron 公告 | HBM 与 NVIDIA 平台绑定，提高存储厂 AI 纯度 | 不推断 Micron 在全部 NVIDIA 平台份额。 |
| NVIDIA 与 SK hynix 签署多年存储共同开发/供应协议 | B | Tom's Hardware/MarketWatch | SK hynix 对 NVIDIA 平台的可见度增强 | 不推断协议金额和份额。 |
| AMD 与 OpenAI 公布多代 Instinct GPU、最高 6GW 合作 | B | 多家公开报道 | AMD 从“备选”走向核心供应商的可验证节点 | 不假设全部 6GW 一定落地。 |
| OpenAI 与 Broadcom 公布 10GW 定制 AI 加速器/机架系统合作 | B | BI/Tom's Hardware/WSJ 报道 | 定制 ASIC 成为 GPU 之外的大额预算路径 | 不把未披露财务条款填成收入。 |
| NVIDIA 供应链公开报道提到 TSMC、SK hynix、Samsung、Foxconn、Quanta、Amkor、SPIL 等 | B | Tom's Hardware 转述 Bloomberg | 说明 AI 系统价值流横跨晶圆、HBM、组装、封装 | 对未在公司财报点名的关系标记为二级公开信息。 |

## 市值变化快照

> 完整表见 CSV。这里列出第一批已取得同源市值数据的公司。

| 公司 | 角色 | 市值 | 近一年市值变化 | 数据日 | 备注 |
| --- | --- | ---: | ---: | --- | --- |
| NVIDIA | AI GPU/系统 | $4.85T | +46.82% | 2026-06-10 | 绝对龙头，估值仍需用收入增速和 capex 可持续性检验。 |
| TSMC | 先进代工/封装 | $1.85T | +116.56% | 2026-06-10 | 先进节点共因子。 |
| Broadcom | 定制 ASIC/网络 | $1.77T | +59.77% | 2026-06-10 | 定制 ASIC + 网络。 |
| Samsung Electronics | HBM/DRAM/NAND/Foundry | $1.285T | +353.63% | 2026-06 | 存储+晶圆代工综合暴露，AI纯度低于纯 HBM/代工。 |
| Micron | HBM/存储 | $1.01T | +833.79% | 2026-06-10 | 强周期高弹性，需防峰值估值。 |
| SK hynix | HBM/存储 | $967.76B | +707.85% | 2026-06 | HBM 直接暴露高，需防存储周期。 |
| AMD | AI GPU/CPU | $737.68B | +312.44% | 2026-06-10 | 份额提升预期强。 |
| ASML | EUV/光刻 | $670.10B | +125.71% | 2026-06-10 | 稀缺设备瓶颈。 |
| Intel | CPU/Foundry | $537.98B | +515.13% | 2026-06-10 | 复苏和本土制造可选项。 |
| Lam Research | 刻蚀/沉积设备 | $402.43B | +288.13% | 2026-06-10 | 存储和先进制程 capex 弹性。 |
| Applied Materials | 综合设备 | $394.61B | +212.18% | 2026-06-10 | WFE 平台型公司。 |
| KLA | 检测/量测 | $278.97B | +178.61% | 2026-06-10 | 良率控制刚需。 |
| Marvell | 定制 ASIC/互连 | $220.97B | +299.76% | 2026-06-10 | 光互连和定制芯片弹性。 |
| MediaTek | 端侧 AI SoC | $204.11B | +191.98% | 2026-06 | 边缘 AI 暴露，非数据中心主线。 |
| Qualcomm | 端侧 AI SoC | $201.52B | +23.49% | 2026-06-10 | 数据中心 AI 暴露低。 |
| Tokyo Electron | 半导体设备 | $181.62B | +142.57% | 2026-06 | 亚洲设备龙头。 |
| Advantest | 测试设备 | $114.01B | +174.16% | 2026-06 | AI/HBM 测试弹性。 |
| Cadence | EDA | $107.82B | +24.71% | 2026-06-09 | 高质量软件资产。 |
| Synopsys | EDA/IP | $89.09B | +15.50% | 2026-06-09 | 高质量软件资产。 |
| SMIC | 中国晶圆代工 | $74.04B | +75.00% | 2026-06 | 国产替代核心，但先进制程透明度有限。 |
| Teradyne | 测试设备 | $54.41B | +314.96% | 2026-06-10 | AI/HBM 测试弹性。 |
| Amkor | 封装测试 | $17.25B | +269.52% | 2026-06-10 | 美国先进封装本土化弹性。 |
| Entegris | 材料/过滤 | $19.65B | +79.45% | 2026-06-10 | 耗材属性。 |

## 股票筛选框架

### 评分维度

| 维度 | 高分标准 | 低分信号 |
| --- | --- | --- |
| AI 收入兑现 | 财报已显示 AI/HPC/数据中心收入大幅增长 | 只有叙事，没有收入分项或订单证据 |
| 供应链瓶颈 | EUV、HBM、先进封装、先进节点、测试/良率控制 | 可替代供应商多、议价弱 |
| 客户/订单证据 | 公告、年报、电话会明确提到客户或平台 | 仅市场传闻 |
| 财务质量 | 高毛利、高 ROIC、现金流强、负债可控 | 强 capex 但现金回收慢 |
| 估值消化能力 | 增速、订单和利润率能支撑估值 | 市值涨幅远超盈利兑现 |
| 周期风险 | 收入来自长期供给约束和结构升级 | 存储/设备/PCB 价格周期接近峰值 |
| 地缘风险 | 可在多区域供应/客户分散 | 单一区域、出口管制、制裁清单 |

## PE 补充口径

- `pe_ttm`: trailing PE，基于过去 12 个月盈利；周期股在盈利低点/高点会失真。
- `forward_pe`: forward PE，基于市场预期；只对 StockAnalysis 覆盖的公司补入，CompaniesMarketCap 页面暂只记录 TTM PE。
- Intel 的 TTM PE 为空，因为 StockAnalysis 显示 TTM 亏损，不能用正 PE 比较。
- A/H 股和部分台股封测/国产设备公司暂标 `needs_pe_source`，下一轮需用交易所、Wind/同花顺/东方财富或公司年报统一口径补齐。

| 公司 | 环节 | TTM PE | Forward PE | 估值解读 |
| --- | --- | ---: | ---: | --- |
| NVIDIA | AI GPU/系统 | 30.69 | 20.17 | 估值相对其利润兑现不算最夸张，但高度依赖 AI capex 延续。 |
| TSMC | 先进代工/封装 | 30.95 | 21.68 | 先进节点共因子，估值低于多数设备/EDA/ASIC 弹性股。 |
| Broadcom | 定制 ASIC/网络 | 61.93 | 23.64 | Forward PE 明显低于 TTM，市场押注 AI 订单兑现。 |
| AMD | AI GPU/CPU | 150.86 | 51.92 | 估值主要买份额提升和 OpenAI/大客户兑现。 |
| Micron | HBM/存储 | 41.96 | 9.21 | 典型强周期：forward PE 很低但要防盈利峰值。 |
| SK hynix | HBM/存储 | 39.46 |  | HBM 纯度高，但缺 forward PE，需要补韩股一致预期。 |
| Samsung | HBM/DRAM/NAND/Foundry | 52.39 |  | 估值反映存储复苏和 AI 预期，AI 纯度低于 SK hynix/Micron。 |
| ASML | EUV/光刻 | 58.10 | 44.50 | 垄断稀缺但估值不便宜，订单周期是关键。 |
| AMAT | 综合设备 | 46.74 | 33.75 | WFE 平台型，估值低于 ASML/部分测试股。 |
| Lam Research | 刻蚀/沉积 | 60.78 | 42.88 | 存储和先进制程弹性，周期风险更强。 |
| KLA | 检测/量测 | 60.46 | 44.87 | 质量高但估值已高。 |
| Advantest | 测试设备 | 243.82 |  | TTM PE 极高，需核对盈利周期和 forward 预期。 |
| Arm | CPU IP | 363.23 | 141.68 | 估值高度依赖长期 royalty 和 AI server/edge 叙事。 |
| Cadence | EDA | 89.77 | 47.33 | 高质量软件，但估值仍高。 |
| Synopsys | EDA/IP | 109.08 | 29.03 | TTM 受并购/利润节奏影响，forward 更有参考性。 |
| SMIC | 中国晶圆代工 | 113.35 |  | 国产替代溢价明显，需结合盈利质量和制裁风险看。 |

### 初筛结论

- **第一梯队：高质量但估值敏感**：NVIDIA、TSMC、ASML、Broadcom。共同点是瓶颈或生态强；NVIDIA/TSMC 的 forward PE 低于多数设备和 EDA 弹性股，但仍要看 AI capex 延续。
- **第二梯队：高弹性兑现中**：AMD、Micron、SK hynix、Marvell、Lam Research、Applied Materials、KLA、Teradyne。共同点是 AI 订单或 capex 传导强；Micron 的 forward PE 很低但可能是周期峰值信号，AMD/Marvell 仍需要收入兑现来消化高 PE。
- **第三梯队：质量稳但弹性较低**：Cadence、Synopsys、Arm、Entegris。适合用作“AI 芯片复杂度上升”的低波动映射，但 Arm/Cadence 的估值已经很吃增长。
- **中国政策弹性池**：寒武纪、海光信息、澜起科技、北方华创、中微公司、拓荆科技、华海清科、长电科技、通富微电、深南电路、胜宏科技。优点是国产替代和十五五政策方向明确；缺点是估值、先进制程、出口管制和客户/订单透明度。

## 当前最值得继续深挖的问题

1. HBM：SK hynix、Micron、Samsung 的 2026-2027 HBM 产能、长期协议、价格条款和客户集中度。
2. 先进封装：TSMC CoWoS、Amkor/ASE、长电/通富/华天的真实先进封装收入占比，而不是只看封测总收入。
3. 定制 ASIC：Broadcom、Marvell 的客户数量、订单金额、量产节点和毛利率变化。
4. 中国 AI 芯片：寒武纪/海光的收入质量、毛利、现金流、客户集中度、制程/封装供给约束。
5. 估值：将近一年市值涨幅拆成 EPS 上调、估值扩张和汇率/股本变化，避免只因涨幅大就判断泡沫或优质。

## 关联连接

- [[integrated-circuits/00-index|集成电路 - 研究入口]]
- [[integrated-circuits/01-industry-map|集成电路 - 产业链地图]]
- [[integrated-circuits/04-companies|集成电路 - 公司与竞争]]
- [[integrated-circuits/05-investment-view|集成电路 - 投资视角]]
- [[ai/00-index|AI 相关 - 研究入口]]
