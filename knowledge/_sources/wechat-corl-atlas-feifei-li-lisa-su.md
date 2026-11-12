---
title: "CoRL 李飞飞 × 苏姿丰：Atlas 与机器人｜文章来源卡"
type: source
date_created: 2026-11-12
last_updated: 2026-11-12
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-773-corl-fei-fei-li-and-lisa-su-atlas-world-models-compute-and-robotics-wechat-trans.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-774-atlas-a-world-model-for-spatial-intelligence.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-775-frameboy-atlas-in-real-time.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-776-amd-to-acquire-world-labs-to-advance-the-future-of-ai-compute.md
tags: [industry/robotics-embodied-ai, world-model, atlas, source-set]
status: active
---

# CoRL 李飞飞 × 苏姿丰｜文章来源卡

> [!summary]
> 已编译为 [[news/2026-11-12-corl-atlas-feifei-li-lisa-su|八个要点、事实核查与后续问题]]。主题包括生成与重建统一、相机控制、仿真用途、系统协同、公共算力与研究者成长。保留现场整理的证据边界，不把演示外推为可靠物理仿真。

## 来源记录

| 编号 | 来源/日期/等级 | 本次用途与限制 |
|---|---|---|
| [773](../../raw/robotics-embodied-ai/documents/SRC-robotics-773-corl-fei-fei-li-and-lisa-su-atlas-world-models-compute-and-robotics-wechat-trans.md) | [微信原文](https://mp.weixin.qq.com/s/CuhnoPBcC_F9qPmhXPoC7w)，具身纪元 / Marilyn Liu；日期待验证；B | §01–16 中文演讲/对谈整理，未逐句听校原视频，图片未 OCR |
| [774](../../raw/robotics-embodied-ai/documents/SRC-robotics-774-atlas-a-world-model-for-spatial-intelligence.md) | [World Labs Atlas 发布页](https://worldlabs.ai/blog/atlas)，2026-09-01；A | 架构和任务定位、视频长度旧版本口径；公司自述 |
| [775](../../raw/robotics-embodied-ai/documents/SRC-robotics-775-frameboy-atlas-in-real-time.md) | [Frameboy 实时预览](https://worldlabs.ai/blog/atlas-realtime)，2026-11-05；A | 15 fps 的云端串流口径、访问限制和成本边界 |
| [776](../../raw/robotics-embodied-ai/documents/SRC-robotics-776-amd-to-acquire-world-labs-to-advance-the-future-of-ai-compute.md) | [AMD 拟收购公告](https://ir.amd.com/news-events/press-releases/detail/1299/amd-to-acquire-world-labs-to-advance-the-future-of-ai-compute)，2026-09-28；S | 仅核对协议、交割与任职的条件关系，不确认后续完成状态 |

四条均经 `tools/extract_sources_with_defuddle.py` 抽取为 `ok`；原文标题、作者与空发布日期字段另保存在 [Defuddle JSON](../../raw/robotics-embodied-ai/documents/SRC-robotics-773-defuddle-metadata.json)。公司技术博客属于一手披露，按 A 记录；S 级公告也不能证明其前瞻预期已实现。

## 原文主张定位

- §03–06：机器人三问题、生成—稀疏重建—稠密重建、相机条件与模型架构。
- §07–11：评测、长视频、重建、动态/实时演示、仿真探索和 BEHAVIOR 挑战赛。
- §12–13：AMD/World Labs 协同、模型路线、训练/边缘计算、公共资源与开放生态。
- §14–16：博士价值、领域直觉、计算效率与人脑比较、求真及面对难题。

## 知识冲突

现场与 9 月官方页的视频时长、现场“将开放”与 11 月研究预览存在版本/范围差异，详见 [[news/2026-11-12-corl-atlas-feifei-li-lisa-su#知识冲突与版本差异|差异记录]]。未取得足够证据前不将后来的展示数字写为通用产品承诺。

## 关联连接

- [[news/2026-11-12-corl-atlas-feifei-li-lisa-su|要点入库]]
- [[robotics-embodied-ai/00-source-capture-index|机器人来源索引]]
- [[robotics-embodied-ai/00-index|机器人研究入口]]
- [[_syntheses/bilibili-world-labs-spatial-intelligence-deep-dive-2026-08-14|World Labs 既有研究]]

## 2026-11-12 落地调研跟进

已完成 [[robotics-embodied-ai/research-notes/atlas-3d-reconstruction-robot-simulation-deployment-2026-11-12|Atlas 3D重建与机器人仿真落地方案]]，补入 [[_sources/atlas-reconstruction-simulation-source-set-2026-11-12|25项官方资料与1项有限核查]]。新证据把资产链细化到posed RGBD→SPZ→GLB/碰撞盒；仍不等于分件、门轴/滑轨、物性或机器人闭环。保留原摘要的日期范围；API文档被发现不代表今日才上线，账号调用与场景精度未验证。
