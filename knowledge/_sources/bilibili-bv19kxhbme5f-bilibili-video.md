---
title: "耗时两年半，我们做了一个让机器人“摸得到”的开源触觉系统"
type: source
date_created: 2026-08-11
last_updated: 2026-08-11
source_urls:
  - https://www.bilibili.com/video/BV19kXHBmE5F
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-08-11-bilibili-bv19kxhbme5f-bilibili-video.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# 耗时两年半，我们做了一个让机器人“摸得到”的开源触觉系统

> [!summary]
> Synthesized in [[_syntheses/bilibili-flexitac-open-tactile-system-deep-dive-2026-08-11|FlexiTac 开源触觉系统视频深度调研]].

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV19kXHBmE5F |
| BV / video id | `BV19kXHBmE5F` |
| Author | Mango-Man |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-08-11-bilibili-bv19kxhbme5f-bilibili-video.json` |

## Transcript Excerpt

Hello, everyone. Today, I will introduce FlexiTac, a low cost, open source, scalable tactile sensing solution for robot systems. About a year ago, we introduced 3D VITAC, a low cost, piezo resistive tactile sensor. Designed for robot manipulation. Since then, it's been adopted by research labs and industry teams around the world. Over the past year, we upgraded the design using flexible PCBs, which makes the sensor more consistent. Easier to manufacture, and much easier to integrate onto robots with different shapes and form factors. We've used this sensor for in the wild tactile data collection. And also in simulation as part of a sim to real to sim pipeline. In this video, I'll show you how to assemble a FlexiTec sensor in about 3 minutes using four simple steps. Attach the FPC to the lamination sheet, stack the Velostat layer, seal the edges with polyimide tape, connect to the readout board. Step one, attach the FPC to the lamination sheet and align. Take a pre cut lamination sheet and place the top FPC onto it. Do the same for the bottom FPC. Make sure the corners are aligned exactly like this. Step two, stack Velostat with the FPCs. Place the Velostat layer in the middle between the two prepared layers. Once it's centered, the sensor stack is already functional. Step three, seal edges with polyimide tape. Now, we make it more robust for long term robot experiments. Seal the border with polyimide tape. This protects the edges and helps prevent delamination over time. Step four, connect to the readout board. Now, let's connect the sensor to the electronics. Insert the sensor's gold fingers into the connector, then connect the connector to the readout board using an FFC cable. Once the board is connected to your computer, the sensor is ready. In our demo software, you...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-08-11-bilibili-bv19kxhbme5f-bilibili-video.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
