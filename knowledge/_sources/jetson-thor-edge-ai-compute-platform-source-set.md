---
title: Jetson Thor 与边缘 AI 计算平台来源集
type: source
date_created: 2026-08-05
last_updated: 2026-08-05
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-363-nvidia-jetson-thor-official-product-specifications.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-364-nvidia-jetson-faq-current-pricing-and-lifecycle.md
  - knowledge/robotics-embodied-ai/sources.csv
tags:
  - industry/robotics-embodied-ai
  - edge-ai
  - jetson
status: active
---

# Jetson Thor 与边缘 AI 计算平台来源集

> [!summary]
> 本来源集服务于 [[robotics-embodied-ai/research-notes/jetson-thor-and-alternatives-spec-price-comparison-2026-08-05|Jetson Thor 与替代平台规格、价格及选型调研]]。关键规格与美元定价优先使用厂商官网、开发文档和官方商城；中国渠道价、库存与交期是动态采购线索，不升级为永久事实。

## 核心来源

| SRC | 证据 | 用途与边界 |
|---|---|---|
| [`SRC-robotics-363`](../../raw/robotics-embodied-ai/documents/SRC-robotics-363-nvidia-jetson-thor-official-product-specifications.md) | NVIDIA Thor 官方规格 | T5000/T4000、开发套件、内存、功耗、I/O；FP4 sparse 指标不能与 INT8 dense 直接比较。 |
| [`SRC-robotics-364`](../../raw/robotics-embodied-ai/documents/SRC-robotics-364-nvidia-jetson-faq-current-pricing-and-lifecycle.md) | NVIDIA 当前 FAQ | 2026-08-05 当前 MSRP、1KU+ 模组建议价、开发套件和量产模组边界。 |
| `SRC-robotics-365` | NVIDIA Marketplace | Thor 开发套件 5,499 美元及抓取时缺货状态；库存会变化。 |
| `SRC-robotics-366` | JetPack 7 | Ubuntu 24.04、Kernel 6.8、CUDA 13、SBSA、MIG、实时内核和 HSB。 |
| `SRC-robotics-367` | NVIDIA Jetson benchmark | Thor 在指定 JetPack/TensorRT/vLLM 设置下的 LLM/VLM 吞吐；不是跨厂商独立测试。 |
| `SRC-robotics-368`–`369` | Qualcomm IQ-9075 / EVK | 50/100 INT8 Dense TOPS、36GB ECC、工业温度、10+ 年生命周期及 EVK；价格仅询价。 |
| `SRC-robotics-370`–`371` | AMD / MINISFORUM | Ryzen AI Max+ 395 的 CPU/NPU 边界及 128GB 完整系统当前售价。 |
| `SRC-robotics-372` | NVIDIA DGX Spark | 128GB CUDA 桌面开发系统的规格与当前 4,699 美元 MSRP。 |
| `SRC-robotics-373` | Hailo-10H | 低功耗 M.2 加速器规格；不是独立计算机。 |
| `SRC-robotics-374` | 华为 Atlas 200I DK A2 | 国产低阶边缘推理对照，不是 Thor 同档替代。 |
| `SRC-robotics-375` | 地平线征程 6 | 车规 10–560 Effective TOPS 对照；非通用机器人采购路径。 |
| [`SRC-robotics-376`](../../raw/robotics-embodied-ai/documents/SRC-robotics-376-jetson-agx-thor-china-channel-listing.md) | iCEasy 中国渠道页（B 级） | 约 ¥40,999 含税动态报价与库存线索；采购前必须取得书面报价。 |

## 数据表

- [候选规格与价格 CSV](../../raw/robotics-embodied-ai/data/jetson-thor-alternatives-spec-price-2026-08-05.csv)

## 证据冲突

- 2025 年发布博客仍显示 Thor 开发套件 `US$3,499`；NVIDIA 当前 FAQ 和 Marketplace 已显示 `US$5,499`。报告以 2026-08-05 当前页面为准，并保留旧价作为历史价格。
- NVIDIA FAQ 页面局部问答仍残留旧 Orin 价格，而同页当前统一价格表和 Marketplace 已更新。采购应以结算页和书面报价单为准。

## 关联连接

- [[robotics-embodied-ai/00-index|机器人（具身智能）研究入口]]
- [[robotics-embodied-ai/research-notes/jetson-thor-and-alternatives-spec-price-comparison-2026-08-05|Jetson Thor 选型调研]]
- [[_concepts/embodied-ai|Embodied AI]]
