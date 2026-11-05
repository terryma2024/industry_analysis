---
source_id: "SRC-robotics-671"
title: "Contact-UAN Unsupervised Actuator Networks as a Residual World Model for Humanoid Control"
source_type: "paper"
publisher: "Fey et al."
source_date: "2026-10-13"
url: "https://arxiv.org/abs/2610.18991"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:38:59+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-671
---
# Contact-UAN Unsupervised Actuator Networks as a Residual World Model for Humanoid Control

## Computer Science > Robotics

## Title:Contact-UAN: Unsupervised Actuator Networks as a Residual World Model for Humanoid Control

Authors:[Nolan Fey](https://arxiv.org/search/cs?searchtype=author&query=Fey,+N), [Khai Nguyen](https://arxiv.org/search/cs?searchtype=author&query=Nguyen,+K), [Yash Prabhu](https://arxiv.org/search/cs?searchtype=author&query=Prabhu,+Y), [Gabriel B. Margolis](https://arxiv.org/search/cs?searchtype=author&query=Margolis,+G+B), [Pulkit Agrawal](https://arxiv.org/search/cs?searchtype=author&query=Agrawal,+P)

[View PDF](https://arxiv.org/pdf/2610.18991) [HTML (experimental)](https://arxiv.org/html/2610.18991v1)

> Abstract:Humanoid policies trained in simulation can transfer qualitatively to hardware while failing to transfer the force interactions learned during training, compromising torque efficiency, load regulation, and robustness to impacts. This failure can arise from actuator sim-to-real gaps because forces depend on actuator torques. We introduce Contact-UAN, a residual world model that preserves a simulator's physics priors while correcting actuator dynamics to align simulated rollouts with recorded hardware rollouts. For humanoid motion with contact, this requires contact-consistent replay: if hardware playback in simulation begins with misaligned contact wrenches, the residual model learns to correct reset artifacts rather than actuator discrepancies. Using only onboard proprioception, Contact-UAN infers the simulator-side stance-foot pose needed to initialize replay with consistent contact forces. We show that a UAN trained on 6.5 minutes of real-world walking data generalizes to tasks that benefit from accurate force and impulse regulation and produces policies that transfer seamlessly to the real world, yielding 20% lower running torque, 43% lower force-tracking error, extreme compliance, accurate impedance control, and dynamic, robust jumps.

| Comments: |  |
| --- | --- |
| Subjects: | Robotics (cs.RO) |
| Cite as: | [arXiv:2610.18991](https://arxiv.org/abs/2610.18991) \[cs.RO\] |
|  | (or [arXiv:2610.18991v1](https://arxiv.org/abs/2610.18991v1) \[cs.RO\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2610.18991](https://doi.org/10.48550/arXiv.2610.18991) |

## Submission history

From: Nolan Fey \[[view email](https://arxiv.org/show-email/2a0003a1/2610.18991)\]  
**\[v1\]** Tue, 13 Oct 2026 18:00:52 UTC (18,384 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2610.18991) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
