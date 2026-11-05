---
source_id: "SRC-robotics-663"
title: "PACE Zero-Shot Sim-to-Real Contact-Rich Assembly"
source_type: "paper"
publisher: "Wang et al."
source_date: "待验证"
url: "https://arxiv.org/abs/2609.07534"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:35:43+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-663
---
# PACE Zero-Shot Sim-to-Real Contact-Rich Assembly

## Computer Science > Robotics

## Title:Proprioception-Anchored Cross-Modal Pretraining for Zero-Shot Sim-to-Real Contact-Rich Assembly

Authors:[Yuhan Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+Y), [Yurou Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+Y), [Hongye Jiang](https://arxiv.org/search/cs?searchtype=author&query=Jiang,+H), [Gaojing Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+G), [Wenzhao Lian](https://arxiv.org/search/cs?searchtype=author&query=Lian,+W)

[View PDF](https://arxiv.org/pdf/2609.07534) [HTML (experimental)](https://arxiv.org/html/2609.07534v3)

> Abstract:Contact-rich assembly remains challenging because it requires submillimeter spatial accuracy and reliable interpretation of forces during sustained contact. Although simulation-based reinforcement learning offers a scalable training paradigm, discrepancies in visual observations, contact dynamics, and force/torque (F/T) measurements often limit policy transfer. We observe that proprioception is comparatively consistent across domains because joint positions are expressed in a shared calibrated coordinate system and joint velocities are computed consistently in simulation and on hardware. Based on this observation, we present PACE (Proprioception-Anchored Cross-Modal Encoder), which supervises temporal visual and F/T representations by predicting proprioceptive state transitions. Static domain-specific factors, including lighting, texture, and sensor bias, contain little information about joint motion; optimizing the proposed objective therefore suppresses their influence on the learned representation while retaining task-relevant motion cues. Policies trained on frozen PACE features are directly deployed on hardware without real-world fine-tuning or object-pose tracking. Across four contact-rich assembly tasks, PACE attains an average real-world success rate of 93.3\\% and only a 2.7-percentage-point sim-to-real drop, while remaining robust to perturbations that substantially degrade pose-based and learned-fusion baselines.

| Subjects: | Robotics (cs.RO); Artificial Intelligence (cs.AI) |
| --- | --- |
| Cite as: | [arXiv:2609.07534](https://arxiv.org/abs/2609.07534) \[cs.RO\] |
|  | (or [arXiv:2609.07534v3](https://arxiv.org/abs/2609.07534v3) \[cs.RO\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2609.07534](https://doi.org/10.48550/arXiv.2609.07534) |

## Submission history

From: Yuhan Wang \[[view email](https://arxiv.org/show-email/fdfc80ff/2609.07534)\]  
**[\[v1\]](https://arxiv.org/abs/2609.07534v1)** Mon, 7 Sep 2026 14:20:22 UTC (6,113 KB)  
**[\[v2\]](https://arxiv.org/abs/2609.07534v2)** Mon, 14 Sep 2026 04:13:47 UTC (6,352 KB)  
**\[v3\]** Wed, 16 Sep 2026 07:13:58 UTC (5,686 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2609.07534) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
