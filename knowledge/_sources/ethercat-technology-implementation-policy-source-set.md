---
title: EtherCAT 技术、实现、生态与政策来源集
type: source
date_created: 2026-08-09
last_updated: 2026-08-09
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-505-ethercat-technology-overview.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-506-ethercat-technology-group-organisation-and-standardization.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-507-ethercat-faq-licensing-and-implementation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-509-ethercat-g-technology-overview.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-510-ethercat-and-tsn.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-511-soem-official-repository.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-512-igh-ethercat-master-1-6-documentation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-513-cip-motion-official-overview.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-514-source.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-515-2026-2028.md
tags:
  - industry/robotics-embodied-ai
  - industrial-ethernet
  - ethercat
status: active
---

# EtherCAT 技术、实现、生态与政策来源集

> [!summary]
> 本来源集以 ETG 官方技术、标准化、许可、实现、EtherCAT G/TSN 文档为主，以 SOEM、IgH 官方代码资料和 ODVA CIP Motion 官方页作实现与竞品对照，并用工信部文件限定中国政策表述。稳定结论是：EtherCAT 是开放标准化、受专利和兼容性许可治理的实时工业以太网技术；它并不等于“协议开源”，也不能仅凭总线性能推导整机控制实时性。

## 核心来源

| SRC | 主要用途 | 等级 | 限制 |
|---|---|---:|---|
| [`SRC-robotics-505`](../../raw/robotics-embodied-ai/documents/SRC-robotics-505-ethercat-technology-overview.md) | on-the-fly、FMMU、DC、拓扑、诊断 | S | ETG 自述性能不是独立 benchmark |
| [`SRC-robotics-506`](../../raw/robotics-embodied-ai/documents/SRC-robotics-506-ethercat-technology-group-organisation-and-standardization.md) | IEC 61158/61784、ETG、CTT/Plug Fest | S | 会员数不等于装机份额 |
| [`SRC-robotics-507`](../../raw/robotics-embodied-ai/documents/SRC-robotics-507-ethercat-faq-licensing-and-implementation.md) | 开放、专利、MainDevice/ESC 许可、一致性 | S | 不是法律意见 |
| `SRC-robotics-508` | 从站实现、状态机、ESI、同步与测试 | S | 官方 PDF 本轮自动抽取未产出 raw，需后续补采并按版本冻结 |
| [`SRC-robotics-509`](../../raw/robotics-embodied-ai/documents/SRC-robotics-509-ethercat-g-technology-overview.md) | Gigabit 分支与兼容性 | S | 不代表普通应用需要升级 |
| [`SRC-robotics-510`](../../raw/robotics-embodied-ai/documents/SRC-robotics-510-ethercat-and-tsn.md) | EtherCAT 与 TSN 的互补边界 | S | ETG 立场，需用目标网络 PoC |
| [`SRC-robotics-511`](../../raw/robotics-embodied-ai/documents/SRC-robotics-511-soem-official-repository.md) | 轻量 C MainDevice 库 | S | 库本身不提供整机实时保证 |
| [`SRC-robotics-512`](../../raw/robotics-embodied-ai/documents/SRC-robotics-512-igh-ethercat-master-1-6-documentation.md) | Linux 内核 MainDevice、GPLv2 | S | 内核/驱动/发行版适配成本需实测 |
| [`SRC-robotics-513`](../../raw/robotics-embodied-ai/documents/SRC-robotics-513-cip-motion-official-overview.md) | EtherNet/IP + CIP Motion/CIP Sync 对照 | S | 未做统一硬件横评 |
| [`SRC-robotics-514`](../../raw/robotics-embodied-ai/documents/SRC-robotics-514-source.md) | 人形机器人实时可靠控制政策背景 | S | 未点名 EtherCAT |
| [`SRC-robotics-515`](../../raw/robotics-embodied-ai/documents/SRC-robotics-515-2026-2028.md) | 十五五工业互联网平台政策背景 | S | 偏平台层，不是现场总线补贴政策 |

## 证据纪律

- 报告中的 `≤100 µs` 周期目标、`<1 µs` 同步抖动等数字只作为 ETG 官方设计目标/测量口径，不当作任意设备组合的 SLA。
- “最大现场总线组织”“大量中国会员”只证明生态广度信号，不能推出市场份额、收入或国产化率。
- 开源 MainDevice 项目证明可实现性，不证明满足功能安全、长期维护和目标系统最坏时延。
- 中国政策支持工业互联网、机器人实时可靠控制、标准与测试能力，但没有证据表明政府偏好单一 EtherCAT 协议。

## 关联连接

- [[robotics-embodied-ai/research-notes/ethercat-technology-ecosystem-engineering-deep-dive-2026-08-09|EtherCAT 深度调研]]
- [[embodied-ai|具身智能]]
- [[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]]
