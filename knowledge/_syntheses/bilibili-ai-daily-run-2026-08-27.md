---
title: Bilibili AI Daily Run 2026-08-27
type: synthesis
date_created: 2026-08-27
last_updated: 2026-08-27
sources:
  - raw/_inbox/transcripts/
tags:
  - operations
  - bilibili
  - ai
  - embodied-ai
status: active
---

# Bilibili AI Daily Run 2026-08-27

## Run Summary

- Candidate videos: 0
- Selected for transcript extraction: 0
- Duplicate skipped: 0
- Needs model review: 0
- Processed: 0
- Failed: 0

## OpenCLI / Fetch Notes

- bilibili favorite failed: (node:36674) [UNDICI-EHPA] Warning: EnvHttpProxyAgent is experimental, expect them to change at any time.
(Use `node --trace-warnings ...` to show where the warning was created)
ok: false
error:
  code: BROWSER_CONNECT
  message: Browser Bridge extension not connected
  help: |-
    Make sure Chrome/Chromium is open and the OpenCLI extension is enabled.
    If not installed:
      1. Download: https://github.com/jackwener/opencli/releases
      2. Open chrome://extensions → Developer Mode → Load unpacked
  exitCode: 69
- bilibili comment failed: error: missing required argument 'bvid'
- bilibili comments failed: error: missing required argument 'bvid'
- bilibili download failed: error: missing required argument 'bvid'
- bilibili hot failed: (node:36748) [UNDICI-EHPA] Warning: EnvHttpProxyAgent is experimental, expect them to change at any time.
(Use `node --trace-warnings ...` to show where the warning was created)
ok: false
error:
  code: BROWSER_CONNECT
  message: Browser Bridge extension not connected
  help: |-
    Make sure Chrome/Chromium is open and the OpenCLI extension is enabled.
    If not installed:
      1. Download: https://github.com/jackwener/opencli/releases
      2. Open chrome://extensions → Developer Mode → Load unpacked
  exitCode: 69

## TOS Audio Check

- Check enabled: True
- Prefix: `asr-audio/2026/08/27`
- Objects found: 0

## Candidate Decisions

| Status | Title | Video ID | Score | Reason |
|---|---|---:|---:|---|
| none | none | `-` | 0 | no candidates |

## Processing Results

- No videos processed.

## Codex Research Handoff

- Read each new `knowledge/_sources/bilibili-*.md` source card and the corresponding raw transcript JSON.
- For durable value, update relevant pages under `knowledge/ai/`, `knowledge/robotics-embodied-ai/`, `knowledge/_entities/`, `knowledge/_concepts/`, `knowledge/_claims/`, or `knowledge/_syntheses/`.
- Cross-check important company, policy, market-size, and product claims against primary sources before promoting them into industry pages.

## Related Links

- [[ai/00-index|AI]]
- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[_sources/README|Sources Layer]]
