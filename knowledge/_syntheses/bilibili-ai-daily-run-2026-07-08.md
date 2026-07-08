---
title: Bilibili AI Daily Run 2026-07-08
type: synthesis
date_created: 2026-07-08
last_updated: 2026-07-08
sources:
  - raw/_inbox/transcripts/
tags:
  - operations
  - bilibili
  - ai
  - embodied-ai
status: active
---

# Bilibili AI Daily Run 2026-07-08

## Run Summary

- Candidate videos: 2
- Selected for transcript extraction: 2
- Duplicate skipped: 0
- Needs model review: 0
- Processed: 2
- Failed: 0

## Retry Context

- This report was regenerated during the retry run for the two previously failed selected videos: `BV1q3TE6AE4b` and `BV1Z7jA6LE8s`.
- Earlier on 2026-07-08, `BV1mgja6CEbK` had already been processed and synthesized in [[_syntheses/bilibili-qianxun-intelligence-deep-dive-2026-07-08|千寻智能具身智能公司视频深度调研]].
- After this retry, all three model-selected 2026-07-08 videos have source packets and standalone deep-dive synthesis pages.
- Pipeline repair note: duplicate detection now ignores `knowledge/log.md` failure mentions, and TOS today-prefix checks use the Volcengine TOS SDK runner so missing/failed uploads are visible in candidate-stage diagnostics.

## OpenCLI / Fetch Notes

- No fetch errors recorded.

## TOS Audio Check

- Check enabled: True
- Prefix: `asr-audio/2026/07/08`
- Objects found: 3
- Recent keys:
  - `asr-audio/2026/07/08/022100-asr-audio.m4a`
  - `asr-audio/2026/07/08/035059-asr-audio.m4a`
  - `asr-audio/2026/07/08/040217-asr-audio.m4a`

## Candidate Decisions

| Status | Title | Video ID | Score | Reason |
|---|---|---:|---:|---|
| selected | 博登智能：估值超10亿，AI卖铲人闷声发大财 | `BV1q3TE6AE4b` | 0 | selected by model relevance judgment |
| selected | 成立两年半，估值200亿，千寻智能凭什么？ | `BV1Z7jA6LE8s` | 0 | selected by model relevance judgment |

## Processing Results

- `BV1q3TE6AE4b` 博登智能：估值超10亿，AI卖铲人闷声发大财: processed; transcript captured and source card written; raw=`raw/_inbox/transcripts/2026-07-08-bilibili-bv1q3te6ae4b-10-ai.json`; source=`knowledge/_sources/bilibili-bv1q3te6ae4b-10-ai.md`
- `BV1Z7jA6LE8s` 成立两年半，估值200亿，千寻智能凭什么？: processed; transcript captured and source card written; raw=`raw/_inbox/transcripts/2026-07-08-bilibili-bv1z7ja6le8s-200.json`; source=`knowledge/_sources/bilibili-bv1z7ja6le8s-200.md`

## Codex Research Handoff

- Read each new `knowledge/_sources/bilibili-*.md` source card and the corresponding raw transcript JSON.
- For durable value, update relevant pages under `knowledge/ai/`, `knowledge/robotics-embodied-ai/`, `knowledge/_entities/`, `knowledge/_concepts/`, `knowledge/_claims/`, or `knowledge/_syntheses/`.
- Cross-check important company, policy, market-size, and product claims against primary sources before promoting them into industry pages.

## Related Links

- [[ai/00-index|AI]]
- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[_sources/README|Sources Layer]]
