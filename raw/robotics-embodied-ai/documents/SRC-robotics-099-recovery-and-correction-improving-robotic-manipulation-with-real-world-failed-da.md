---
source_id: "SRC-robotics-099"
title: "Recovery and Correction: Improving Robotic Manipulation with Real-World Failed Data"
source_type: "paper"
publisher: "arXiv"
source_date: "2025-09-09"
url: "https://arxiv.org/abs/2509.07953"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-05-27T02:22:12+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-099
---
# Recovery and Correction: Improving Robotic Manipulation with Real-World Failed Data

## Title:RaC: Robot Learning for Long-Horizon Tasks by Scaling Recovery and Correction

Authors:[Zheyuan Hu](https://arxiv.org/search/cs?searchtype=author&query=Hu,+Z), [Robyn Wu](https://arxiv.org/search/cs?searchtype=author&query=Wu,+R), [Naveen Enock](https://arxiv.org/search/cs?searchtype=author&query=Enock,+N), [Jasmine Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+J), [Riya Kadakia](https://arxiv.org/search/cs?searchtype=author&query=Kadakia,+R), [Zackory Erickson](https://arxiv.org/search/cs?searchtype=author&query=Erickson,+Z), [Aviral Kumar](https://arxiv.org/search/cs?searchtype=author&query=Kumar,+A)

[View PDF](https://arxiv.org/pdf/2509.07953) [HTML (experimental)](https://arxiv.org/html/2509.07953v1)

> Abstract:Modern paradigms for robot imitation train expressive policy architectures on large amounts of human demonstration data. Yet performance on contact-rich, deformable-object, and long-horizon tasks plateau far below perfect execution, even with thousands of expert demonstrations. This is due to the inefficiency of existing \`\`expert'' data collection procedures based on human teleoperation. To address this issue, we introduce RaC, a new phase of training on human-in-the-loop rollouts after imitation learning pre-training. In RaC, we fine-tune a robotic policy on human intervention trajectories that illustrate recovery and correction behaviors. Specifically, during a policy rollout, human operators intervene when failure appears imminent, first rewinding the robot back to a familiar, in-distribution state and then providing a corrective segment that completes the current sub-task. Training on this data composition expands the robotic skill repertoire to include retry and adaptation behaviors, which we show are crucial for boosting both efficiency and robustness on long-horizon tasks. Across three real-world bimanual control tasks: shirt hanging, airtight container lid sealing, takeout box packing, and a simulated assembly task, RaC outperforms the prior state-of-the-art using 10 $\times$ less data collection time and samples. We also show that RaC enables test-time scaling: the performance of the trained RaC policy scales linearly in the number of recovery maneuvers it exhibits. Videos of the learned policy are available at [this https URL](https://rac-scaling-robot.github.io/).

| Subjects: | Robotics (cs.RO); Machine Learning (cs.LG) |
| --- | --- |
| Cite as: | [arXiv:2509.07953](https://arxiv.org/abs/2509.07953) \[cs.RO\] |
|  | (or [arXiv:2509.07953v1](https://arxiv.org/abs/2509.07953v1) \[cs.RO\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2509.07953](https://doi.org/10.48550/arXiv.2509.07953) |

## Submission history

From: Zheyuan Hu \[[view email](https://arxiv.org/show-email/d88aba55/2509.07953)\]  
**\[v1\]** Tue, 9 Sep 2025 17:41:29 UTC (26,134 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2509.07953) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
