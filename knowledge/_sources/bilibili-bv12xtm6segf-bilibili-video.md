---
title: "机器触觉反馈，是不是就是一个伪命题？#机器触觉 #科技 #论文解读 #机器人 #科技改变生活"
type: source
date_created: 2026-07-05
last_updated: 2026-07-05
source_urls:
  - https://www.bilibili.com/video/BV12XTM6sEGF
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-05-bilibili-bv12xtm6segf-bilibili-video.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# 机器触觉反馈，是不是就是一个伪命题？#机器触觉 #科技 #论文解读 #机器人 #科技改变生活

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. Synthesized in [[_syntheses/bilibili-hapmorph-haptic-feedback-deep-dive-2026-07-05|HapMorph 触觉反馈视频深度调研]].

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV12XTM6sEGF |
| BV / video id | `BV12XTM6sEGF` |
| Author | 新达同学 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-05-bilibili-bv12xtm6segf-bilibili-video.json` |

## Transcript Excerpt

今天看到一篇名叫Hammer off的机器人触觉的研究。他们在尝试用两个互相拉扯的充气气枪，让可穿戴触觉设备在仅有21克的重量下，就能实现对物体大小和软硬的同时反馈。在聊这个研究之前，我们先把机器人触觉的地图摊开。很多人容易把两件方向完全相反的事混在一起说，他们硬件不同、目标不同、瓶颈更是天差地别。一条赛道叫触觉感知，传感器装在机器人手上，让机器学会摸东西。信息方向是从物理世界流向机器。这其中比较有代表的，GelSight 在指尖里塞摄像头和凝胶，物体按压的形变直接拍成 RGB 图像，分辨率做到微米级。Meta 的 Digits 360 更进一步，压力、形变、震动、温度甚至气味全能感知，指尖自带 AI 加速器。这条赛道现在的问题根本不是硬件不够强，而是这么多精细的触觉信号，怎么能真正融进机器人的闭环决策里？而另一条赛道叫触觉反馈，设备戴在人手上，让人感受到虚拟或者远端物体的物理属性。信息方向是从机器传回人体，这正是海莫夫所在的领域。他的难题和上面说的触觉感知赛道刚好是一对镜像，不是机器摸不摸得到，而是信号能不能准确传递到人的手指上，以及人到底能不能分辨的出来。一边是让机器人拥有人类级的触觉，另一边是让人类借机器获得跨时空的触感。理解了这层对称关系，下面我们来看看海莫夫这篇研究。回到触觉反馈这条赛道，现在主要有两派。一派是桌面型大型系统，会有机械臂末端、形状显示器等等，能精确渲染几何形状和力学特性，但大、重且贵。它们是实验室和工业场景里的好东西，不是普通用户能穿戴的。另一派是可穿戴方案，织物、软体执行器、微型外骨骼这些，轻便可穿戴，但代价是功能受限，通常只能反馈形状或软硬，很少能同时控制多个属性。所以目前的核心瓶颈显而易见，也就是多属性反馈和可穿戴之间不可兼得。而 hammock 的解法很简单，用两个对着较劲的充气气枪，充气后互相拉扯，最终平衡在固定尺寸。通过调整两边的气压配比，就能在完全相同的外形下，挑出不同的软硬质感，相当于从只有一个旋钮，变成了大小软硬各有一个独立开关，控制维度直接从一维升级到二维。最终的可穿戴原型仅重21克，大小能在50~104毫米之间连续变化，硬度最高能到4.7牛每毫米。人体测试中，整体识别准确率89.4%。不过这项研究最有价值的发现藏在数据细节里。极端软硬、极端大小的状态几乎不会认错，但中等尺寸加中等硬度的组合，准确率直接掉到78%，而且受试者越测越难分辨。这说明一个本质的问题，大小和软硬在机器端已经成功解耦，但人类的触觉神经系统其实并不能稳定分辨这么多独立维度。机器能渲染的触感可能会超过了人能感知的上限。最后一句话总结，Hammond 用一对互相拉扯的气枪给气动触觉反馈打开了多维度控制的新路径。但他也告诉我们，触觉反馈的下一道难关可能不在硬件里，而在我们自己的神经系统里。所以一定程度上，我认为机器触觉反馈可能就是一个伪命题。这里是辛达同学，如果你想及时了解最新科技、 ai 动态，关注我获取更多内容吧！

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-05-bilibili-bv12xtm6segf-bilibili-video.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
- [[_syntheses/bilibili-hapmorph-haptic-feedback-deep-dive-2026-07-05|HapMorph 触觉反馈视频深度调研]]
