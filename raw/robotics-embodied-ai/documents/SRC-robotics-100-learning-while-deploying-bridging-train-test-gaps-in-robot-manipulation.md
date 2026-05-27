---
source_id: "SRC-robotics-100"
title: "Learning while Deploying: Bridging Train-Test Gaps in Robot Manipulation"
source_type: "paper"
publisher: "arXiv"
source_date: "2026-05-01"
url: "https://arxiv.org/abs/2605.00416"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-05-27T02:22:12+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-100
---
# Learning while Deploying: Bridging Train-Test Gaps in Robot Manipulation

## Title:Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies

Authors:[Yi Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+Y), [Xinchen Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+X), [Pengwei Xie](https://arxiv.org/search/cs?searchtype=author&query=Xie,+P), [Pu Yang](https://arxiv.org/search/cs?searchtype=author&query=Yang,+P), [Buqing Nie](https://arxiv.org/search/cs?searchtype=author&query=Nie,+B), [Yunuo Cai](https://arxiv.org/search/cs?searchtype=author&query=Cai,+Y), [Qinglin Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+Q), [Chendi Qu](https://arxiv.org/search/cs?searchtype=author&query=Qu,+C), [Jeffrey Wu](https://arxiv.org/search/cs?searchtype=author&query=Wu,+J), [Jianheng Song](https://arxiv.org/search/cs?searchtype=author&query=Song,+J), [Xinlin Ren](https://arxiv.org/search/cs?searchtype=author&query=Ren,+X), [Jingshun Huang](https://arxiv.org/search/cs?searchtype=author&query=Huang,+J), [Mingjie Pan](https://arxiv.org/search/cs?searchtype=author&query=Pan,+M), [Siyuan Feng](https://arxiv.org/search/cs?searchtype=author&query=Feng,+S), [Zhi Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+Z), [Jianlan Luo](https://arxiv.org/search/cs?searchtype=author&query=Luo,+J)

[View PDF](https://arxiv.org/pdf/2605.00416) [HTML (experimental)](https://arxiv.org/html/2605.00416v1)

> Abstract:Generalist robot policies increasingly benefit from large-scale pretraining, but offline data alone is insufficient for robust real-world deployment. Deployed robots encounter distribution shifts, long-tail failures, task variations, and human correction opportunities that fixed demonstration datasets cannot fully capture. We present Learning While Deploying (LWD), a fleet-scale offline-to-online reinforcement learning framework for continual post-training of generalist Vision-Language-Action (VLA) policies. Starting from a pretrained VLA policy, LWD closes the loop between deployment, shared physical experience, policy improvement, and redeployment by using autonomous rollouts and human interventions collected across a robot fleet. To stabilize learning from heterogeneous, sparse-reward fleet data, LWD combines Distributional Implicit Value Learning (DIVL) for robust value estimation with Q-learning via Adjoint Matching (QAM) for policy extraction in flow-based VLA action generators. We validate LWD on a fleet of 16 dual-arm robots across eight real-world manipulation tasks, including semantic grocery restocking and 3--5 minute long-horizon tasks. A single generalist policy improves as fleet experience accumulates, reaching an average success rate of 95%, with the largest gains on long-horizon tasks.

| Comments: |
| --- |
| Subjects: | Robotics (cs.RO) |
| Cite as: | [arXiv:2605.00416](https://arxiv.org/abs/2605.00416) \[cs.RO\] |
|  | (or [arXiv:2605.00416v1](https://arxiv.org/abs/2605.00416v1) \[cs.RO\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2605.00416](https://doi.org/10.48550/arXiv.2605.00416) |

## Submission history

From: Yi Wang \[[view email](https://arxiv.org/show-email/a494f9be/2605.00416)\]  
**\[v1\]** Fri, 1 May 2026 05:20:26 UTC (8,904 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2605.00416) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
