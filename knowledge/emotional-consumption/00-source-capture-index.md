---
title: 情绪价值实体消费：来源与抓取状态
type: index
date_created: 2026-10-22
last_updated: 2026-10-22
sources:
  - knowledge/emotional-consumption/sources.csv
  - raw/emotional-consumption/documents/source_capture_manifest.csv
tags:
  - industry/emotional-consumption
  - research/R09
status: active
---

# 情绪价值实体消费：来源与抓取状态

18条记录：16条正常抓取/抽取，1条失败由新来源替代（004→018），1条动态IR页仅HTML回退（015）。有效的001—003、005—012及018财报为财务核验基础；016/017媒体仅作反方/上市线索。原始返回保留，不把下载成功视为正文有效。

| 来源 | 文件/内容 | 等级 | 抓取状态 |
|---|---|---|---|
| [SRC-emotion-001](../../raw/emotional-consumption/documents/SRC-emotion-001-pop-mart-2026-interim-results.md) | 泡泡玛特：Pop Mart 2026 interim results | S | 已抽取；原文核阅 |
| [SRC-emotion-002](../../raw/emotional-consumption/documents/SRC-emotion-002-bloks-2026-interim-report.md) | 布鲁可：Bloks 2026 interim report | S | 已抽取；原文核阅 |
| [SRC-emotion-003](../../raw/emotional-consumption/documents/SRC-emotion-003-miniso-2026-interim-report.md) | 名创优品：MINISO 2026 interim report | S | 已抽取；原文核阅 |
| [SRC-emotion-004](../../raw/emotional-consumption/documents/SRC-emotion-004-m-and-g-2026-half-year-report.md) | 晨光股份：M and G 2026 half year report | S | 失败：官网返回HTML，改用018 |
| [SRC-emotion-005](../../raw/emotional-consumption/documents/SRC-emotion-005-guangbo-2026-half-year-report.md) | 广博股份（新浪公告转载）：Guangbo 2026 half year report | S | 已抽取；第三方公告载体 |
| [SRC-emotion-006](../../raw/emotional-consumption/documents/SRC-emotion-006-alpha-group-2026-half-year-report.md) | 奥飞娱乐：Alpha Group 2026 half year report | S | 已抽取；原文核阅 |
| [SRC-emotion-007](../../raw/emotional-consumption/documents/SRC-emotion-007-shifeng-2026-half-year-report.md) | 实丰文化：Shifeng 2026 half year report | S | 已抽取；原文核阅 |
| [SRC-emotion-008](../../raw/emotional-consumption/documents/SRC-emotion-008-rastar-2026-half-year-report.md) | 星辉娱乐：Rastar 2026 half year report | S | 已抽取；原文核阅 |
| [SRC-emotion-009](../../raw/emotional-consumption/documents/SRC-emotion-009-cre8-2026-half-year-report.md) | 创源股份（新浪公告转载）：Cre8 2026 half year report | S | 已抽取；第三方公告载体 |
| [SRC-emotion-010](../../raw/emotional-consumption/documents/SRC-emotion-010-wahlap-2026-half-year-report.md) | 华立科技（新浪公告转载）：Wahlap 2026 half year report | S | 已抽取；第三方公告载体 |
| [SRC-emotion-011](../../raw/emotional-consumption/documents/SRC-emotion-011-laopu-gold-2026-interim-report.md) | 老铺黄金：Laopu Gold 2026 interim report | S | 已抽取；原文核阅 |
| [SRC-emotion-012](../../raw/emotional-consumption/documents/SRC-emotion-012-chj-2026-half-year-results-summary.md) | 潮宏基（东方财富公告转载）：CHJ 2026 half year results summary | S | 已抽取；第三方公告载体 |
| [SRC-emotion-013](../../raw/emotional-consumption/documents/SRC-emotion-013-china-consumption-action-plan-2025.md) | 中办国办/工信部转新华社：China consumption action plan 2025 | S | 已抽取；原文核阅 |
| [SRC-emotion-014](../../raw/emotional-consumption/documents/SRC-emotion-014-samr-blind-box-guidelines-2023.md) | 国家市场监管总局：SAMR blind box guidelines 2023 | S | 已抽取；原文核阅 |
| [SRC-emotion-015](../../raw/emotional-consumption/documents/SRC-emotion-015-pop-mart-investor-announcements-index.md) | 泡泡玛特：Pop Mart investor announcements index | S | HTML回退：动态目录正文未抽取 |
| [SRC-emotion-016](../../raw/emotional-consumption/documents/SRC-emotion-016-goldman-channel-tracker-reported-october-2026.md) | 观点网转述高盛：Goldman channel tracker reported October 2026 | B | 已抽取；原文核阅 |
| [SRC-emotion-017](../../raw/emotional-consumption/documents/SRC-emotion-017-kayou-ipo-progress-september-2026.md) | 财中社：Kayou IPO progress September 2026 | B | 已抽取；原文核阅 |
| [SRC-emotion-018](../../raw/emotional-consumption/documents/SRC-emotion-018-m-and-g-2026-half-year-report-official-disclosure.md) | 晨光股份/巨潮资讯：M and G 2026 half year report official disclosure | S | 已抽取；原文核阅 |

PDF提取用pdftotext，网页用Defuddle。005/009/010/012为公司公告的第三方载体。004保留失败返回，015不能用于证明公告完备。抓取工具因历史失败行返回非零，即使018替代抽取成功，也不把整组称为零错误。

## 关联连接

[[emotional-consumption/00-index|主题入口]] · [[_sources/emotional-consumption-listed-company-source-set-2026-10-22|编译来源卡]] · [[emotional-consumption/research-notes/china-emotional-value-physical-goods-stock-screen-2026-10-22|主报告]]
