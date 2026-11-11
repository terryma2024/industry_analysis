---
title: "仿真数据采集技术深度解析｜微信文章来源卡"
type: source
date_created: 2026-11-09
last_updated: 2026-11-10
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-677-source.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-678-niantic-spatial-flexion-humanoid-real2sim-sim2real.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-679-vlk-learning-humanoid-loco-manipulation-official-project.md
tags:
  - industry/robotics-embodied-ai
  - real2sim
  - sim2real
  - 3dgs
  - synthetic-data
status: active
---

# 仿真数据采集技术深度解析｜文章来源卡

> [!summary]
> 微信技术解读，主张用 3DGS 重建、仿真强化学习与合成轨迹连接真实场景和机器人训练。已编译为 [[news/2026-11-09-3dgs-robot-simulation-data-real2sim-vlk|文章摘要与关键核验]]。保留原文，不静默修写；VLK 真机微调等冲突在摘要中明确记录。

## 来源记录

| 编号 | 来源与等级 | 抓取状态 |
|---|---|---|
| SRC-robotics-677 | 敢敢AUTOHUB／敢敢不敢写bug，微信公众号，C | Defuddle ok；发布日期待验证；部分公式缺失、配图未离线保存 |
| SRC-robotics-678 | Niantic Spatial/Flexion 官方实验博客，A | Defuddle ok；作者报告，无独立复现 |
| SRC-robotics-679 | VLK 作者项目页，S | Defuddle ok；原始研究披露，无独立复现 |

## 原文主张与证据指向

- 原文 §3–5：重建外观与碰撞几何、导航训练和零样本迁移，见 [SRC-robotics-677](../../raw/robotics-embodied-ai/documents/SRC-robotics-677-source.md)；核对 [SRC-robotics-678](../../raw/robotics-embodied-ai/documents/SRC-robotics-678-niantic-spatial-flexion-humanoid-real2sim-sim2real.md)。
- 原文 §6：VLK 合成视觉—语言—运动学轨迹，见 [SRC-robotics-677](../../raw/robotics-embodied-ai/documents/SRC-robotics-677-source.md)；核对 [SRC-robotics-679](../../raw/robotics-embodied-ai/documents/SRC-robotics-679-vlk-learning-humanoid-loco-manipulation-official-project.md)。
- 97.8% 属于仿真；真机只有定性结果。48k 是作者项目页每场景口径，不能直接当通用数据规模或收益指标。

## 知识冲突

原文 §6.3 将真机微调叙述为 VLK 实验路线，但作者项目页写零真机微调；采纳作者对本工作设定的披露，同时保留原文。详细比较、未核实代码参数、商业主张及下一步证据见 [[news/2026-11-09-3dgs-robot-simulation-data-real2sim-vlk#知识冲突|冲突记录]]。

## 关联连接

- [[news/2026-11-09-3dgs-robot-simulation-data-real2sim-vlk|文章核验摘要]]
- [[robotics-embodied-ai/00-source-capture-index|机器人来源抓取索引]]
- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[_sources/3dgs-ply-to-simready-source-set|3DGS 仿真资产来源集]]

## 2026-11-10 深研跟进

已完成 [[robotics-embodied-ai/research-notes/vlk-synthetic-data-zero-shot-project-fit-2026-11-10|VLK 全文、附录与公开实现深研]]。新增真机逐格表、120/240计数及验证split冲突；明确无真机微调仍依赖真实扫描、手工标注和预训练，场地内布局变化不等于未知场地泛化。SceneBot有公开推理demo，VLK主生成/训练代码仍未从作者入口取得。原文与前轮抽取保留。

## 2026-11-10 Niantic／Flexion 深研跟进

- [[robotics-embodied-ai/research-notes/niantic-flexion-real2sim-zero-shot-project-fit-2026-11-10|工作流、公开资产与迁移边界]]：已区分重建场景、RL交互经验和可导出ACT示教；补提取8个仿真条件及样例USD静态结构。未执行训练或真机；未取得合作导航完整代码/权重。
