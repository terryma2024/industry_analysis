---
title: "CoRL 李飞飞 × 苏姿丰：Atlas、算力与机器人｜要点入库"
type: news-summary
date_created: 2026-11-12
last_updated: 2026-11-12
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-773-corl-fei-fei-li-and-lisa-su-atlas-world-models-compute-and-robotics-wechat-trans.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-774-atlas-a-world-model-for-spatial-intelligence.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-775-frameboy-atlas-in-real-time.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-776-amd-to-acquire-world-labs-to-advance-the-future-of-ai-compute.md
tags: [industry/robotics-embodied-ai, world-model, spatial-intelligence, atlas, compute, corl]
status: active
---

# CoRL 李飞飞 × 苏姿丰：Atlas、算力与机器人

> [!summary]
> 最值得保留的主线是：世界模型连接环境表示、动作预测和仿真数据；Atlas 用相机条件把生成与重建放入同一模型，但展示画面一致性与可靠机器人闭环之间仍有距离。对谈强调模型、硬件、软件和系统协同，以及研究者的领域直觉、好奇心与求真能力。

## 来源与入库状态

- 原文：[现场｜CoRL现场李飞飞 × 苏姿丰：世界模型、算力与机器人的下一步](https://mp.weixin.qq.com/s/CuhnoPBcC_F9qPmhXPoC7w)。微信公众号：具身纪元；署名：Marilyn Liu。
- 文章发布日期：**待验证**，Defuddle 元数据的 `published` 为空；2026-11-12 是入库日期。原文自述为 CoRL 现场演讲及对谈整理，未据此补写会议具体日期。
- 提取方式：Defuddle Markdown 正文及 JSON 元信息，读取 §01–16；另归档三份官方材料。配图保留链接，未逐图 OCR；没有观看原始现场视频，译文、删节和专名未逐句听校。curl 返回的页面未用于判断标题或日期。
- 证据等级：会议演讲的中文整理 B；公司技术博客 A；AMD 收购公告 S（仅对公告内容）。四项新来源 `SRC-robotics-773`–`776` 均抽取 `ok`；抓取脚本退出 1 来自合并清单中的历史失败项。
- 范围：**文章要点入库与关键口径核查，非独立深度研究**；没有运行模型、评测或机器人。

## 原文八个要点

以下归纳来自 [SRC-robotics-773](../../raw/robotics-embodied-ai/documents/SRC-robotics-773-corl-fei-fei-li-and-lisa-su-atlas-world-models-compute-and-robotics-wechat-trans.md)，保留为讲者观点或现场展示主张。

1. **世界模型对应机器人三个问题**（§03）：理解并表示环境、预测动作后果并规划、补齐真实数据长尾，分别联系渲染、规划与仿真；三者可以相互贯通。
2. **生成与重建是一条连续谱**（§04–05）：同一 Atlas 模型可从文本生成、单图/少图补全，走到多图重建。输入越少，未观测部分越依赖生成先验。斯坦福庭院的 2/8/33 张照片例子说明：看似合理，不等于恢复了真实缺失结构。
3. **关键是显式相机约束与下一视角预测**（§06）：多模态自回归扩散 Transformer 接收文本、图像、视频、深度、灰盒等条件，沿相机轨迹生成新视角；Atlas 本体不必采用 3DGS，3DGS 可以是后续显式表示。
4. **展示覆盖静态、动态和实时场景**（§07–10）：长于 60 秒的视频、8 图公寓重建、单图生成空间、三部 iPhone 拍摄后的子弹时间，以及蒸馏后 15 FPS 交互。均需保留演示条件，不能作为所有场景的质量保证。
5. **机器人价值首先落在仿真场景与数据**（§10）：生成/重建环境，丰富导航训练及评测，探索与 real-to-sim-to-real 操作研究结合。原文未给出可归因于 Atlas 的完整真机成功率、样本量和对照实验。
6. **机器人进展取决于系统协同**（§12）：VLM/LLM 可能发挥更大作用，但 System 2 及物理 AI 问题尚未解决；不同应用可能需要不同模型，需同时优化云端训练、边缘功耗、内存、延迟与软件。
7. **公共算力与团队科学影响研究机会**（§12–13）：大学、非营利机构承担探索研究、人才培养和 AI 评估；模型与计算互相影响，需要跨机构合作。产业资源支持的意愿不能等同已落实的资源承诺。
8. **个人长期优势来自深入探索与判断力**（§14–16）：博士不是唯一创新道路，其价值在于受保护的好奇心与领域直觉；坚持正直、求真、主动解决难题。效率研究也重要，但大脑运行功耗与模型训练总能耗不能直接比较。

## 关键事实与口径核查

| 项目 | 本次核查结果 | 使用边界 |
|---|---|---|
| Atlas 架构与任务 | 公司发布页支持多模态自回归扩散 Transformer、生成/重建/时空模拟的定位 | 技术路线的一手自述；不等于独立复现，见 [774](../../raw/robotics-embodied-ai/documents/SRC-robotics-774-atlas-a-world-model-for-spatial-intelligence.md) |
| 15 FPS | Frameboy 官方页说明由云 GPU 向浏览器串流，最高 15 fps；Viewfinder 当页仍为封闭测试 | 不能当成本地部署速度或机器人控制频率；云成本与访问条件需另验，见 [775](../../raw/robotics-embodied-ai/documents/SRC-robotics-775-frameboy-atlas-in-real-time.md) |
| AMD 收购与任职 | 2026-09-28 公告为签订收购协议，任职安排与交易交割相关 | 未取得交割完成证据，不能写成收购/任职已完成，见 [776](../../raw/robotics-embodied-ai/documents/SRC-robotics-776-amd-to-acquire-world-labs-to-advance-the-future-of-ai-compute.md) |
| 相机控制排名、约 50 万次人评及深度/重建优势 | 原文 §07–08 的展示主张 | 未取得 Rapidata 原始完整评测或重算图表，暂不当作可复用的领先幅度 |
| “数千亿美元机会” | 原文 §12 中苏姿丰的前瞻判断 | 缺市场边界、测算和实现路径，不能当已实现收入或确定市场规模 |

## 知识冲突与版本差异

- **视频长度**：9 月发布页写最长 1 分钟；此次现场整理称已远超 60 秒。可能是版本进展，但尚未取得对应新版规格，不静默覆盖任一记录。[773 §07](../../raw/robotics-embodied-ai/documents/SRC-robotics-773-corl-fei-fei-li-and-lisa-su-atlas-world-models-compute-and-robotics-wechat-trans.md)、[774](../../raw/robotics-embodied-ai/documents/SRC-robotics-774-atlas-a-world-model-for-spatial-intelligence.md)。
- **开放状态**：现场称“很快开放”；11 月 5 日官方已有 Frameboy 研究预览，而自建场景入口仍有限制。“可体验演示”与“可将自有房间导出为仿真资产”分别核验。[775](../../raw/robotics-embodied-ai/documents/SRC-robotics-775-frameboy-atlas-in-real-time.md)。

## 对本仓库的判断

**判断，非原文实验结论**：对中国机器人团队，先把这条路线作为场景外观、视觉扰动和评测覆盖的候选。现有 [[robotics-embodied-ai/research-notes/interactive-room-sim-reconstruction-alternatives-2026-11-10|可交互房间重建路线]]要求对象分件、碰撞、门轴/滑轨、限位与复位；本文没有提供可直接接入该流程的完整交付证据，暂不改变实测分件与显式关节的主线。

## 商业应用可能性

**待验证的应用假设**：场景预览、影视/设计镜头探索可先验证交互效率；机器人研发可验证场景准备和视觉评测的节省。潜在使用者是创作、仿真与算法团队，付款者和预算尚未访谈确认。中国项目需另验访问、商用授权、数据处理条件、成本及资产格式；本文不支持已有客户付费或规模盈利的结论。

## 中小型创业者的机会

**判断/待验证**：比训练通用基础模型更适合小团队的切口，是垂直场景采集、资产清洗/质检、仿真格式转换和回归评测服务。下一步先找一个具体工位的潜在客户，交付可量测、可编辑的场景，并比较传统重建与模型辅助流程的工时、误差和维护成本；没有付费意愿及可重复验收前，不写成已成立的商业机会。

## 后续问题

- [ ] 取得原文发布日期、现场原视频与幻灯片，听校中文整理和性能数字。
- [ ] 查 Rapidata 完整评测：模型版本、相机输入差异、样本及人评协议。
- [ ] 核验自有场景接入、价格、许可、导出格式，以及门/抽屉对象化与物理属性支持。
- [ ] 对零样本真机演示追溯具体项目、基线、样本量及 Atlas 实际承担的环节。

## 关联连接

- [[_sources/wechat-corl-atlas-feifei-li-lisa-su|文章来源卡与四项证据]]
- [[_syntheses/bilibili-world-labs-spatial-intelligence-deep-dive-2026-08-14|既有 World Labs 空间智能研究]]
- [[robotics-embodied-ai/research-notes/door-drawer-interactive-reconstruction-code-audit-2026-11-10|门与抽屉代码核查]]
- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
- [[news/00-index|新闻速记]]

## 2026-11-12 落地调研跟进

已完成 [[robotics-embodied-ai/research-notes/atlas-3d-reconstruction-robot-simulation-deployment-2026-11-12|Atlas 3D重建与机器人仿真落地方案]]，补入 [[_sources/atlas-reconstruction-simulation-source-set-2026-11-12|25项官方资料与1项有限核查]]。新证据把资产链细化到posed RGBD→SPZ→GLB/碰撞盒；仍不等于分件、门轴/滑轨、物性或机器人闭环。保留原摘要的日期范围；API文档被发现不代表今日才上线，账号调用与场景精度未验证。
