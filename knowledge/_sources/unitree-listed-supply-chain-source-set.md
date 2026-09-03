---
title: 宇树科技上市供应链公司来源集
type: source
date_created: 2026-09-02
last_updated: 2026-09-02
sources:
  - knowledge/robotics-embodied-ai/sources.csv
  - raw/robotics-embodied-ai/documents/SRC-robotics-541-2025.pdf
  - raw/robotics-embodied-ai/documents/SRC-robotics-542-2024.pdf
  - raw/robotics-embodied-ai/documents/SRC-robotics-543-2025-3-2.pdf
  - raw/robotics-embodied-ai/documents/SRC-robotics-544-2025-a.pdf
  - raw/robotics-embodied-ai/documents/SRC-robotics-545-source.md
  - raw/robotics-embodied-ai/data/unitree-public-supply-chain-market-snapshot-2026-08-31.csv
tags:
  - industry/robotics-embodied-ai
  - company/unitree
  - supply-chain
  - public-companies
status: active
---

# 宇树科技上市供应链公司来源集

## 来源集结论

截至 2026-09-02，本来源集只把有上市公司公告、年度报告或官方投资者互动直接确认的企业列入“核心名单”。共有 5 家：蔚蓝锂芯、新洁能、创世纪、丰立智能、长盛轴承。五家公司均未披露来自宇树的收入、毛利或订单占比，因此本来源集证明的是**供应关系或验证关系**，不是投资收益弹性。

## 供应关系一级证据

| 来源 ID | 公司 | 一级来源确认内容 | 证据边界 | 本地归档 |
|---|---|---|---|---|
| `SRC-robotics-541` | 新洁能 | 多款产品进入机器人关节电机驱动、BMS，并对宇树多款机型批量供货 | 未披露宇树收入和具体器件型号 | [PDF](../../raw/robotics-embodied-ai/documents/SRC-robotics-541-2025.pdf) |
| `SRC-robotics-542` | 蔚蓝锂芯 | 公司自称宇树重要锂电池供应商，向其销售锂电池产品；宇树只是客户、公司未持股 | 未披露供货量、单价和客户收入占比 | [PDF](../../raw/robotics-embodied-ai/documents/SRC-robotics-542-2024.pdf) |
| `SRC-robotics-543` | 创世纪 | 自 2022 年至今持续向宇树供货，并称其为人形机器人领域重要长期客户之一 | 未披露具体产品；该客户类别占公司收入较小 | [PDF](../../raw/robotics-embodied-ai/documents/SRC-robotics-543-2025-3-2.pdf) |
| `SRC-robotics-544` | 丰立智能 | 精密减速器已向宇树、三花智控、禾川科技“验证导入或小批量供货” | 合并表述不能证明已对宇树量产或形成重要收入 | [PDF](../../raw/robotics-embodied-ai/documents/SRC-robotics-544-2025-a.pdf) |
| `SRC-robotics-545` | 长盛轴承 | 公司确认与宇树合作产品为自润滑轴承 | 机器人零部件整体收入占比不足 1%；宇树特定供货量未披露 | [网页归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-545-source.md) |

## 宇树采购结构证据

- `SRC-robotics-536`：上交所上市交易公告，确认宇树于 2026-08-19 在科创板上市，代码 `688836`。
- `SRC-robotics-537`：宇树招股书。2025 年原材料采购总额 79,378.00 万元，其中机械件 40,255.54 万元（50.71%）、电子元器件 17,782.18 万元（22.40%）、电气材料 17,642.58 万元（22.23%）。
- 招股书所列 2025 年前五大供应商采购占比合计 22.54%，单一供应商不存在超过 50% 的情形；前五大中多数匿名，具名的上海曜励也不是本报告核心 A 股名单。
- 宇树同时强调电机、减速器、灵巧手、激光雷达等核心部件的自研自产能力。因此“机器人 BOM 需要该部件”不自动推出“外部供应商将按整机销量同比例受益”。

## 二级市场数据口径

统一使用 2026-08-31 收盘作为快照日，用 2026-08-03 至 2026-08-31 的前复权收盘价计算近一个月涨跌幅；市值为 2026-08-31 总市值。原始整理表见 [CSV](../../raw/robotics-embodied-ai/data/unitree-public-supply-chain-market-snapshot-2026-08-31.csv)。

| 来源 ID | 标的 | 用途 | 限制 |
|---|---|---|---|
| `SRC-robotics-546` | 蔚蓝锂芯 | 历史收盘价与总市值 | B 级聚合行情，交易前需用券商终端复核 |
| `SRC-robotics-547` | 新洁能 | 历史收盘价与总市值 | B 级聚合行情，已保存网页正文 |
| `SRC-robotics-548` | 创世纪 | 历史收盘价与总市值 | B 级聚合行情，动态页未形成完整 raw 正文 |
| `SRC-robotics-549` | 丰立智能 | 历史收盘价与总市值 | B 级聚合行情，动态页未形成完整 raw 正文 |
| `SRC-robotics-550` | 长盛轴承 | 历史收盘价与总市值 | B 级聚合行情，动态页未形成完整 raw 正文 |

> [!warning]
> 行情与市值会持续变化。本来源集选择共同可比的 2026-08-31 快照，不把 2026-09-01 的零散最新价与 8 月 31 日市值混用。用于真实交易前，应重新拉取交易所或券商终端数据。

## 未列入核心名单的常见传闻股

| 公司 | 未纳入原因 |
|---|---|
| 拓邦股份 | 面对宇树供货提问只表示客户信息保密，未直接确认关系 |
| 兆威机电 | 公开回复未确认具体客户，不能由微型传动业务反推出宇树供货 |
| 卧龙电驱 | 与宇树共建联合实验室属于合作/研发证据，不等于供应关系 |
| 奥比中光 | 具备机器人视觉业务，但本轮未找到直接确认宇树采购的一级证据 |
| 双一科技 | 公司对人形机器人关节业务表示暂无新进展，不构成宇树供应证明 |

## 关联连接

- [[robotics-embodied-ai/research-notes/unitree-listed-supply-chain-public-companies-2026-09-02|宇树科技上市供应链 A 股公司调研]]
- [[_syntheses/bilibili-unitree-commercialization-and-valuation-deep-dive-2026-09-02|宇树上市与机器人商业化视频深度调研]]
- [[_entities/UnitreeRobotics|宇树科技]]

