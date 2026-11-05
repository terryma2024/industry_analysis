---
title: 集成电路 Source Capture Index
type: index
date_created: 2026-09-21
last_updated: 2026-11-05
sources:
  - integrated-circuits/sources.csv
  - raw/integrated-circuits/documents/source_capture_manifest.csv
status: active
tags:
  - industry/integrated-circuits
  - source-capture
---

# 集成电路 Source Capture Index

> [!summary]
> 2026-09-21 为忆阻器存算一体企业与上市公司调研捕获 `SRC-ic-036` 至 `SRC-ic-054`：14 条 `ok`、3 条 `fallback_html`、2 条 `failed`。市场数据 `SRC-ic-055` 至 `057` 记录在账本和机器可读 CSV 中。2026-09-22 新增论文 `SRC-ic-058` 至 `067`，并为中国 GPU/AI 芯片公司调研捕获 `SRC-ic-068` 至 `092`：后者 21 条 `ok`、4 条行情 API `fallback_html`；定期报告 PDF 已用 `pdftotext` 生成可检索 Markdown。

## 2026-09-22 技术原理与大模型扩展来源

| 来源 | 状态 | 主要用途 |
| --- | --- | --- |
| [`SRC-ic-058`](../../raw/integrated-circuits/documents/SRC-ic-058-memristor-based-hardware-accelerators-for-artificial-intelligence.md) | ok | 器件、阵列、外围、架构与商业化跨层综述。 |
| [`SRC-ic-059`](../../raw/integrated-circuits/documents/SRC-ic-059-hardware-implementation-of-memristor-based-artificial-neural-networks.md) | ok | VMM、写入、训练、ADC/DAC 与非理想性。 |
| [`SRC-ic-060`](../../raw/integrated-circuits/documents/SRC-ic-060-a-full-stack-memristor-based-computation-in-memory-system-with-software-hardware.md) | ok | 清华 8 芯片全栈系统、编译器和模型规模边界。 |
| [`SRC-ic-061`](../../raw/integrated-circuits/documents/SRC-ic-061-a-64-core-mixed-signal-in-memory-compute-chip-based-on-phase-change-memory.md) | ok | IBM 64 核 PCM 芯片与片上数字/通信。 |
| [`SRC-ic-062`](../../raw/integrated-circuits/documents/SRC-ic-062-hardware-aware-training-for-large-scale-and-diverse-deep-learning-inference-work.md) | ok | 硬件感知训练、非理想性模型和 AIHWKit。 |
| [`SRC-ic-063`](../../raw/integrated-circuits/documents/SRC-ic-063-toward-software-equivalent-accuracy-on-transformer-based-neural-networks-with-an.md) | ok | BERT、噪声感知训练和数字 attention 边界。 |
| [`SRC-ic-064`](../../raw/integrated-circuits/documents/SRC-ic-064-efficient-scaling-of-large-language-models-with-mixture-of-experts-and-3d-analog.md) | ok | 3D AIMC + MoE 模拟路线；非物理硬件证明。 |
| [`SRC-ic-065`](../../raw/integrated-circuits/documents/SRC-ic-065-analog-foundation-models.md) | ok | Phi-3/Llama-1B 模拟硬件适配及代码。 |
| [`SRC-ic-066`](../../raw/integrated-circuits/documents/SRC-ic-066-memristor-based-adaptive-analog-to-digital-conversion-for-efficient-and-accurate.md) | ok | ADC 面积/能耗瓶颈与自适应转换。 |
| [`SRC-ic-067`](../../raw/integrated-circuits/documents/SRC-ic-067-memory-is-all-you-need-compute-in-memory-architectures-for-llm-inference.md) | ok | Transformer 算子、LLM memory wall 与 CIM 映射综述。 |

## 忆阻器存算一体来源集

| 来源 | 状态 | 主要用途 |
| --- | --- | --- |
| [`SRC-ic-036`](../../raw/integrated-circuits/documents/SRC-ic-036-neurram-compute-in-memory-chip.md) | ok | NeuRRAM 多核 RRAM-CIM 研究芯片。 |
| [`SRC-ic-037`](../../raw/integrated-circuits/documents/SRC-ic-037-stellar-fully-integrated-memristor-chip-with-on-chip-learning.md) | ok | 清华 STELLAR 片上学习成果。 |
| [`SRC-ic-038`](../../raw/integrated-circuits/documents/SRC-ic-038-yizhu-all-digital-3d-dram-cim-tapeout-update.md) | ok | 亿铸最新 3D-DRAM 路线及流片宣称。 |
| [`SRC-ic-039`](../../raw/integrated-circuits/documents/SRC-ic-039-yizhu-reram-poc-chip-update.md) | ok | 亿铸早期 ReRAM POC，对照路线变化。 |
| [`SRC-ic-040`](../../raw/integrated-circuits/documents/SRC-ic-040-innomem-rram-products-and-company-profile.md) | fallback_html | 新忆 RRAM 存储与 AI 芯片定位；需手工复核页面正文。 |
| [`SRC-ic-041`](../../raw/integrated-circuits/documents/SRC-ic-041-innostar-semiconductor-reram-business-profile.md) | ok | 昕原 ReRAM IP、存储和 CIM 业务。 |
| [`SRC-ic-042`](../../raw/integrated-circuits/documents/SRC-ic-042-tetramem-mlx200-memristor-ai-accelerator.md) | fallback_html | TetraMem MLX200/EVK 路线；正文由 HTML sidecar 保留。 |
| [`SRC-ic-043`](../../raw/integrated-circuits/documents/SRC-ic-043-tetramem-and-sk-hynix-memristor-imc-soc-paper.md) | fallback_html | TetraMem 与 SK hynix 联合研究；正文由 HTML sidecar 保留。 |
| [`SRC-ic-044`](../../raw/integrated-circuits/documents/SRC-ic-044-ibm-analog-ai-chip-for-speech-recognition-and-transcription.md) | ok | IBM PCM 模拟 AI 芯片。 |
| [`SRC-ic-045`](../../raw/integrated-circuits/documents/SRC-ic-045-mixed-precision-memristor-and-sram-edge-ai-processor.md) | ok | TSMC 混合精度忆阻器/SRAM 边缘芯片。 |
| [`SRC-ic-046`](../../raw/integrated-circuits/documents/SRC-ic-046-samsung-mram-in-memory-computing-demonstration.md) | ok | Samsung MRAM-CIM 相邻路线。 |
| [`SRC-ic-047`](../../raw/integrated-circuits/documents/SRC-ic-047-weebit-nano-selected-for-korean-analog-cim-program.md) | ok | Weebit Nano 韩国模拟 CIM 项目。 |
| `SRC-ic-048` | failed | 盛视投资亿铸公告；CNINFO 拒绝自动下载，账本保留 URL。 |
| [`SRC-ic-049`](../../raw/integrated-circuits/documents/SRC-ic-049-biwin-investment-and-commissioned-r-d-with-zhongke-zhicu.md) | ok | 佰维对中科智存投资与委托研发。 |
| [`SRC-ic-050`](../../raw/integrated-circuits/documents/SRC-ic-050-challenges-for-memristive-neural-network-hardware.md) | ok | 可制造性、良率、可靠性与规模化障碍。 |
| [`SRC-ic-051`](../../raw/integrated-circuits/documents/SRC-ic-051-tsmc-artificial-intelligence-research-publications.md) | ok | TSMC RRAM-CIM 宏单元研究。 |
| `SRC-ic-052` | failed | Crossbar 白皮书服务器拒绝自动下载；搜索索引可读，仍需手工归档。 |
| [`SRC-ic-053`](../../raw/integrated-circuits/documents/SRC-ic-053-rain-ai-digital-in-memory-computing-approach.md) | ok | Rain AI 当前 SRAM 数字 IMC，用作路线切换反证。 |
| [`SRC-ic-054`](../../raw/integrated-circuits/documents/SRC-ic-054-china-policy-support-for-compute-in-memory.md) | ok | 中国存算一体政策方向。 |

## 中国 GPU 与 AI 芯片公司来源集

| 来源 | 状态 | 主要用途 |
| --- | --- | --- |
| [`SRC-ic-068`](../../raw/integrated-circuits/documents/SRC-ic-068-huawei-2025-annual-report.md) | ok | 华为集团 2025 财务、研发和业务分部；昇腾收入未单列。 |
| [`SRC-ic-069`](../../raw/integrated-circuits/documents/SRC-ic-069-open-cann-and-ascend-superpod-roadmap.md) | ok | 昇腾 SuperPoD、CANN 和后续芯片路线；厂商宣称。 |
| [`SRC-ic-070`](../../raw/integrated-circuits/documents/SRC-ic-070-moore-threads-2025-audit-report-and-financial-statements.md) | ok | 摩尔线程 2025 审计财务数据。 |
| [`SRC-ic-071`](../../raw/integrated-circuits/documents/SRC-ic-071-moore-threads-mtt-s5000-product-page.md) | ok | MTT S5000 与全功能 GPU/MUSA 路线。 |
| [`SRC-ic-072`](../../raw/integrated-circuits/documents/SRC-ic-072-moore-threads-2026-half-year-report.md) | ok | 摩尔线程 2026H1 财务与现金流。 |
| [`SRC-ic-073`](../../raw/integrated-circuits/documents/SRC-ic-073-muxi-2025-annual-report.md) | ok | 沐曦 2025 财务、产品收入和客户集中度。 |
| [`SRC-ic-074`](../../raw/integrated-circuits/documents/SRC-ic-074-muxi-company-and-product-family-overview.md) | ok | 沐曦 N/C/G/X 产品族与 MXMACA。 |
| [`SRC-ic-075`](../../raw/integrated-circuits/documents/SRC-ic-075-muxi-c500-product-page.md) | ok | 沐曦 C500 规格；厂商材料。 |
| [`SRC-ic-076`](../../raw/integrated-circuits/documents/SRC-ic-076-muxi-2026-half-year-report.md) | ok | 沐曦 2026H1 财务、公允价值收益和现金流。 |
| [`SRC-ic-077`](../../raw/integrated-circuits/documents/SRC-ic-077-cambricon-2025-annual-report.md) | ok | 寒武纪 2025 财务、云产品收入和客户集中度。 |
| [`SRC-ic-078`](../../raw/integrated-circuits/documents/SRC-ic-078-cambricon-2026-half-year-report.md) | ok | 寒武纪 2026H1 财务与现金流。 |
| [`SRC-ic-079`](../../raw/integrated-circuits/documents/SRC-ic-079-cambricon-mlu370-x8-product-page.md) | ok | MLU370-X8 公开规格；页面年代限制已标注。 |
| [`SRC-ic-080`](../../raw/integrated-circuits/documents/SRC-ic-080-hygon-2025-annual-report.md) | ok | 海光 2025 财务、CPU/DCU 路线与客户集中度。 |
| [`SRC-ic-081`](../../raw/integrated-circuits/documents/SRC-ic-081-hygon-2026-half-year-report.md) | ok | 海光 2026H1 财务、研发和现金流。 |
| [`SRC-ic-082`](../../raw/integrated-circuits/documents/SRC-ic-082-moore-threads-star-market-listing-announcement.md) | ok | 摩尔线程上市日期与总股本。 |
| [`SRC-ic-083`](../../raw/integrated-circuits/documents/SRC-ic-083-muxi-star-market-listing-announcement.md) | ok | 沐曦上市日期与总股本。 |
| `SRC-ic-084`–`087` | ok | 可变行情页，仅作交叉检查，不用于固定日期估值。 |
| [`SRC-ic-088`](../../raw/integrated-circuits/documents/SRC-ic-088-cambricon-2026-09-21-unadjusted-daily-quote.md)–[`SRC-ic-091`](../../raw/integrated-circuits/documents/SRC-ic-091-muxi-2026-09-21-unadjusted-daily-quote.md) | fallback_html | 东方财富 2026-09-21 不复权收盘价 API；原始 JSON 保存在 HTML sidecar。 |
| [`SRC-ic-092`](../../raw/integrated-circuits/documents/SRC-ic-092-moore-threads-2025-annual-report.md) | ok | 摩尔线程 2025 年报全文，补足产品结构、毛利率与客户集中度。 |

## 关联连接

- [[00-index|集成电路 - 研究入口]]
- [[research-notes/memristor-compute-in-memory-companies-and-stock-screen-2026-09-21|国内外忆阻器存算一体企业、研发成果与上市公司半年股价调研]]
- [[research-notes/china-gpu-ai-chip-providers-investment-comparison-2026-09-22|中国 GPU 与 AI 芯片提供商投资比较]]
- [[sources.csv|集成电路 sources.csv]]

## 五类核心资源跨市场研究（2026-11-05）

- [[_syntheses/future-core-resources-listed-companies-2026-11-05|50家上市公司筛选与财务反证]]
- [[_sources/future-core-resources-source-set-2026-11-05|来源集、原始材料与抓取状态]]

## 核心资源估值跟进（2026-11-05）

- [[_syntheses/future-core-resources-valuation-2026-11-05|21家公司估值与10家候选]]：统一2026-11-04收盘价、正常化盈利、三情景与买入区间；与前轮产业质量筛选分开。
- [[_sources/future-core-resources-valuation-source-set-2026-11-05|估值来源集与归档限制]]：41条增补记录，部分下载失败或正文过薄，另有网页核阅摘记。
