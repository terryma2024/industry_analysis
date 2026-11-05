---
source_id: "SRC-robotics-661"
title: "ConCent Contact-Centric Real-to-Sim-to-Real Learning from One Demonstration"
source_type: "paper"
publisher: "Kim et al."
source_date: "待验证"
url: "https://arxiv.org/abs/2606.30268"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:35:43+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-661
---
# ConCent Contact-Centric Real-to-Sim-to-Real Learning from One Demonstration

## Computer Science > Robotics

## Title:ConCent: Contact-Centric Real-to-Sim-to-Real Learning from One Demonstration

[View PDF](https://arxiv.org/pdf/2606.30268) [HTML (experimental)](https://arxiv.org/html/2606.30268v1)

> Abstract:Sim-to-real policy transfer -- deploying policies trained in simulation in the real world -- is a promising paradigm for scaling robot manipulation without large-scale real-world data. However, transferring simulation-trained policies remains challenging due to discrepancies in contact dynamics -- particularly in contact-rich tasks where subtle differences can alter task outcomes entirely. Because interaction between the manipulated object and the environment is mediated through contact, task success depends on accurately reproducing task-relevant contacts. Accordingly, in manipulation, contact-centric fidelity -- reproducing both the contact event sequence (when, where, and how contacts occur) and the local contact dynamics (how forces and motions evolve at each contact) -- is a necessary condition for task success. Based on this insight, we propose a contact-centric real-to-sim-to-real RL framework that uses task-relevant contact event sequences extracted from real demonstrations as the learning objective. We approximate objects as groups of primitives and optimize their contact geometry in simulation so that the resulting local contact dynamics explain the observed state transitions. The contact event sequence is automatically extracted by replaying the demonstration. This sequence serves as a structured reward signal, guiding the policy toward physically plausible contact regimes validated in reality and preventing exploitation of unrealistic simulator contacts. The signal is obtained automatically, requiring no per-task reward design. Experiments on contact-rich manipulation tasks demonstrate more stable and robust sim-to-real policy transfer compared to unconstrained RL baselines.

| Comments: |  |
| --- | --- |
| Subjects: | Robotics (cs.RO) |
| Cite as: | [arXiv:2606.30268](https://arxiv.org/abs/2606.30268) \[cs.RO\] |
|  | (or [arXiv:2606.30268v1](https://arxiv.org/abs/2606.30268v1) \[cs.RO\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2606.30268](https://doi.org/10.48550/arXiv.2606.30268) |

## Submission history

From: Heecheol Kim \[[view email](https://arxiv.org/show-email/57fd5752/2606.30268)\]  
**\[v1\]** Mon, 29 Jun 2026 13:16:33 UTC (1,130 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2606.30268) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
