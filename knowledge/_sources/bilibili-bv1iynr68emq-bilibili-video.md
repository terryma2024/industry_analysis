---
title: "“偷师”人类数据，机器人在光模块工位干活了！"
type: source
date_created: 2026-08-11
last_updated: 2026-08-11
source_urls:
  - https://www.bilibili.com/video/BV1iyNR68EMQ
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-08-11-bilibili-bv1iynr68emq-bilibili-video.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# “偷师”人类数据，机器人在光模块工位干活了！

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. Synthesized in [[_syntheses/bilibili-optical-module-robotic-workcell-commercial-validation-deep-dive-2026-08-11|光模块工位机器人与人类数据路线视频深度调研]].

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1iyNR68EMQ |
| BV / video id | `BV1iyNR68EMQ` |
| Author | 福爸说人形机器人 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-08-11-bilibili-bv1iynr68emq-bilibili-video.json` |

## Transcript Excerpt

你们一直好奇的真人数据采集，今天在现场带大家体验。这套外骨骼手套会记录我的手怎么动，怎么接触，怎么用力。摄像头同步拍下整个操作过程。把采集到的示范数据会传给旁边的，SAI W0，也就是今年很受关注的世界模型。因为咱们人手跟机器人手有差异，人的动作数据没法直接照搬，所以世界模型要在中间做一次翻译，把真人操作数据转换成机器人数据，再拿去训练迭代，SAI R。 2巨深策略模型，它负责理解任务、规划动作，让机器人把学到的本事给用出来。这就是我4月给大家讲过的灵初10万小时真人数据加双模型路线的现场版。那这些数据跟模型的真实能力怎么样？咱们继续看现场表现。看展台这几组是灵初和常飞共同打造的光模块自动化制造方案。光模块今年很火啊。 AI 服务器、数据中心和高速数据传输都离不了它。但这东西实际插拔并没有看着这么简单，尺寸小，接口和触点又很精密，抓偏了可能对不准，抓歪了还容易卡住。机器人要想把这个活给干好，先得看清楚光模块长什么样，摆在哪，再决定从哪抓，怎么调整方向，把对准、插入、检测、拔出这一整套动作规划好。真到插进去这一下，位置得很准，力也得控的很细，稍微歪一点卡一点，系统就得及时反馈，不能继续硬怼。而且做完插板检测还没有完，机器人接着把光模块送到防静电袋做真空封装，最后再进标准化装盒。现场几台机器人把检测、封装、装盒几道工序连续串起来，组成一套完整的光模块检测和包装流程。所以现在再看，一家巨人大模型公司为什么要自己下场做人类数据采集？是不是一下就清楚了？因为巨深模型要进场工作，离不开大规模高质量的人类数据。模型缺什么，哪些数据有用，都是在训练和任务里试出来的。所以他先用模型反推数据标准，自己定义采什么，怎么采，再拿这些数据持续训练迭代模型，最后放到真实产业场景里，把干活的一整套流程给跑起来。甚至他家最近还跟北大联合发布开源了 ego scale，把近半小时第一人称人手数据用到了灵巧手通用操作模型。所以我觉得这次零初真正值得看的是把人类数据、双模型和工业场景完整串成了一条线。最后你就记住一句话，机器人进厂干活，它的启蒙老师是人类。我是福爸，下期见！

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-08-11-bilibili-bv1iynr68emq-bilibili-video.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
