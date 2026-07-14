---
source_id: "SRC-ai-076"
title: "MediaPipe v0.10.35 release"
source_type: "release_notes"
publisher: "Google AI Edge"
source_date: "2026-04-28"
url: "https://github.com/google-ai-edge/mediapipe/releases/tag/v0.10.35"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-07-14T02:10:12+00:00"
tags:
  - raw/source
  - source-type/release-notes
  - evidence/s
aliases:
  - SRC-ai-076
---
# MediaPipe v0.10.35 release

### Framework and core calculator improvements

- Add histogram information to Tensor::DebugString.
- Bump MediaPipe version to 0.10.35.
- Add missing GL memory barrier in TensorsToSegmentationGlBufferConverter.
- Migrate FromImageCalculator to MediaPipe API3 and add test.
- Add api3::Packet::Share function.
- Remove util/analytics references from GitHub build
- Migrate ToImageCalculator to MediaPipe API3 and add tests.
- Fix -Wthread-safety-analysis warning.
- Allow MP Task files to be use in Vite's workers
- Add save-png-by-path test util function.
- Feat: Add configurable policy for handling empty landmarks in smoothing calculators
- #mediapipe Make GPU service optional in ImageToTensorCalculator for iOS.
- Add Host Platform Web and Host System iOS/Android to logging enums

### MediaPipe Tasks update

This section should highlight the changes that are done specifically for any platform and don't propagate to  
other platforms.

#### Android

- Allow users to use NPU acceleration with JIT compilation
- Drop unnecessary `tasks/core` deps

#### iOS

- Change MP Tasks CocoaPods types to Framework

#### Javascript

- Remove references to "subgroups-f16"
- Fix broken exports statement in package.json
- Update MP Tasks GenAI README

#### Python

- Small fixes to blockwise int4 compression calculations in LLM converter
- Allow for overriding apply\_srq in LLM Converter
- Small blockwise dequant helper for LLM Converter

### MediaPipe Dependencies

- Update Wasm file hashes and URLs in wasm\_files.bzl
