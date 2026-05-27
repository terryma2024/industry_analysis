---
title: 机器人（具身智能） - 来源抽取索引
date: 2026-05-27
tags:
  - industry/robotics-embodied-ai
  - sources
  - raw-capture
  - obsidian/moc
aliases:
  - 具身智能来源抽取索引
  - Robotics Source Capture Index
---

# 机器人（具身智能） - 来源抽取索引

> [!summary]
> 本页是 [[00-index|机器人（具身智能）]] 的来源抽取 MOC。来源编号仍以 [[sources.csv]] 为准；原文/清洗件保存在 `raw/robotics-embodied-ai/documents/`，抽取状态见 [source_capture_manifest.csv](../../raw/robotics-embodied-ai/documents/source_capture_manifest.csv)。

## 当前状态

| 状态 | 数量 | 含义 |
|---|---:|---|
| `exists` | 76 | 既有 Markdown/PDF raw artifact；其中 5 条是 fallback HTML sidecar。 |
| `ok` | 20 | 本轮新增并成功抽取的 raw artifact。 |
| `fallback_html` | 1 | 本轮新增但正文抽取失败，已保存 HTML sidecar。 |
| `failed` | 4 | defuddle 与 HTML fallback 都失败，需要浏览器、官方 PDF 或手工补采。 |

## 快速定位

- 来源总表：[[sources.csv]]
- 抽取 manifest：[source_capture_manifest.csv](../../raw/robotics-embodied-ai/documents/source_capture_manifest.csv)
- 示例：[`SRC-robotics-060`](../../raw/robotics-embodied-ai/documents/SRC-robotics-060-mimicgen-a-data-generation-system-for-scalable-robot-learning-using-human-demons.md) 的 raw extract 在 [SRC-robotics-060 MimicGen](../../raw/robotics-embodied-ai/documents/SRC-robotics-060-mimicgen-a-data-generation-system-for-scalable-robot-learning-using-human-demons.md)

## 需要补采的来源

> [!warning]
> 以下来源被站点限制、JS 渲染或 SSL/403 阻断。知识笔记可以暂用 `sources.csv` 的 URL，但关键结论需要后续补 raw 证据。

| SRC | 状态 | 原因 | 下一步 |
|---|---|---|---|
| `SRC-robotics-017` | `failed` | NVIDIA investor 页面 403，HTML fallback 也被拒。 | 寻找 NVIDIA 官方新闻镜像、开发者页或 PDF。 |
| `SRC-robotics-019` | `failed` | Tesla 页面 403，HTML fallback 也被拒。 | 用浏览器登录/手工保存，或改用 Tesla 官方可访问页面。 |
| `SRC-robotics-021` | `failed` | RobotEra 页面 defuddle 无正文，HTML fallback SSL 失败。 | 用浏览器手工保存官网关键页面或寻找官方新闻稿。 |
| `SRC-robotics-085` | `failed` | 深圳科创局页面 defuddle fetch failed，HTML fallback SSL BAD_ECPOINT。 | 用浏览器手工保存原文，或寻找深圳市政府/政策 PDF 镜像。 |

## 已保存 fallback HTML 的来源

| SRC | raw sidecar | 说明 |
|---|---|---|
| [`SRC-robotics-015`](../../raw/robotics-embodied-ai/documents/SRC-robotics-015-agibot-a2-product-page.md) | [AGIBOT A2](../../raw/robotics-embodied-ai/documents/SRC-robotics-015-agibot-a2-product-page.md) | defuddle 500，但已保存 HTML。 |
| [`SRC-robotics-016`](../../raw/robotics-embodied-ai/documents/SRC-robotics-016-agibot-products-page.md) | [AGIBOT products](../../raw/robotics-embodied-ai/documents/SRC-robotics-016-agibot-products-page.md) | defuddle 500，但已保存 HTML。 |
| [`SRC-robotics-044`](../../raw/robotics-embodied-ai/documents/SRC-robotics-044-agibot-open-agibot-world-2026.md) | [AGIBOT WORLD 2026](../../raw/robotics-embodied-ai/documents/SRC-robotics-044-agibot-open-agibot-world-2026.md) | defuddle 500，但已保存 HTML。 |
| [`SRC-robotics-048`](../../raw/robotics-embodied-ai/documents/SRC-robotics-048-firstmove-egocentric-data-engine-for-robotics.md) | [FirstMove](../../raw/robotics-embodied-ai/documents/SRC-robotics-048-firstmove-egocentric-data-engine-for-robotics.md) | JS 页面无正文，但已保存 HTML。 |
| [`SRC-robotics-049`](../../raw/robotics-embodied-ai/documents/SRC-robotics-049-source.md) | [ModelScope/BAAI](../../raw/robotics-embodied-ai/documents/SRC-robotics-049-source.md) | defuddle URL 解析失败，但已保存 HTML。 |
| [`SRC-robotics-087`](../../raw/robotics-embodied-ai/documents/SRC-robotics-087-source.md) | [杭州强链补链政策解读](../../raw/robotics-embodied-ai/documents/SRC-robotics-087-source.md) | defuddle 无正文，但已保存 HTML。 |

## 后续流程

- 新增来源后先更新 [[sources.csv]]，再运行 `uv run python tools/extract_sources_with_defuddle.py --industry robotics-embodied-ai`。
- 对知识笔记中的关键判断，使用 `SRC-*` 编号引用，并在需要时链接到 raw extract。
- 对 failed/fallback 来源，优先寻找官方 PDF、GitHub raw、论文 arXiv、监管/公告页等更稳定来源替换。
