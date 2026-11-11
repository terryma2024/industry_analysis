---
source_id: "SRC-robotics-683"
title: "SceneBot author project and demo availability"
source_type: "research_project"
publisher: "Sirui Chen et al."
source_date: "待验证"
url: "https://ericcsr.github.io/scenebot/"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-11-10T01:34:53+00:00"
tags:
  - raw/source
  - source-type/research-project
  - evidence/s
aliases:
  - SRC-robotics-683
---
# SceneBot author project and demo availability

Controlled with single policy.

Motion and contact tracking in real-time.

## Interactive Demo

Control a G1 humanoid in a real-time MuJoCo simulation running fully in your browser.

The demo may take a few seconds to load as models and assets are streamed. For the best experience, use a laptop or desktop.

[Open the interactive demo page](https://ericcsr.github.io/scenebot/demo.html)

**💡 Tip:** Press the next key when the previous motion is finished.  
**Example sequence:** Q - L - L - E - W - N - G - W - Z - P

<iframe src="https://ericcsr.github.io/scenebot/mujoco_wasm/dist-desktop/index.html" title="Scenebot MuJoCo Web Demo">Your browser does not support iframes.</iframe>

💡 **Press the next key when the previous motion is finished.**

Example: Q - L - L - E - W - N - G - W - Z - P

### 🎮 How to Play

Controls

W A S D Walk forward / back, turn left / right Q / E Spin in place left / right N / Z Step on box / come down G / P Pick up / put down box L Sit down / stand up (toggle) K Kicking Enter Run example sequence automatically Backspace Reset scene

## Abstract

Current humanoid reinforcement-learning policies excel at free-space motions but struggle with contact-rich tasks, as pure kinematic tracking cannot resolve the physical ambiguities of interacting with objects and uneven terrain. To address this, we introduce SceneBot, a unified motion-tracking framework capable of handling freespace locomotion, terrain traversal, and whole-body manipulation. SceneBot conditions a single policy on both reference motions and per-link contact labels, explicitly defining expected environmental interactions. To overcome the lack of annotated interaction data, we propose a hindsight scene reconstruction approach that infers scene-interaction graphs from retargeted human motion. Trained on 7.5 hours of this reconstructed, contact-rich data, SceneBot successfully generalizes to unseen motions and environments. Our results demonstrate that SceneBot is the first general framework to seamlessly unify free-space and contact-rich behaviors—executing complex, long-horizon tasks like carrying a box upstairs and establishing contact conditioning as a powerful interface for humanoid control.

![](https://ericcsr.github.io/scenebot/static/images/method_v6.png)
