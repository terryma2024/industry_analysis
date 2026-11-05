---
source_id: "SRC-robotics-662"
title: "Closing the Reality Gap Zero-Shot Sim-to-Real Dexterous Force-Based Grasping"
source_type: "paper"
publisher: "Dong et al."
source_date: "待验证"
url: "https://arxiv.org/abs/2601.02778"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:35:43+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-662
---
# Closing the Reality Gap Zero-Shot Sim-to-Real Dexterous Force-Based Grasping

## Computer Science > Robotics

## Title:Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation

Authors:[Zhe Zhao](https://arxiv.org/search/cs?searchtype=author&query=Zhao,+Z), [Haoyu Dong](https://arxiv.org/search/cs?searchtype=author&query=Dong,+H), [Zhengmao He](https://arxiv.org/search/cs?searchtype=author&query=He,+Z), [Yang Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+Y), [Xinyu Yi](https://arxiv.org/search/cs?searchtype=author&query=Yi,+X), [Zhibin Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+Z)

[View PDF](https://arxiv.org/pdf/2601.02778)

> Abstract:Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities, but training control policies that can directly deploy on real hardware remains difficult due to contact-rich physics and imperfect actuation. We close this gap with a practical sim-to-real reinforcement learning (RL) framework that utilizes dense tactile feedback combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer, we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii) a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current to joint torque; and (iii) actuator dynamics modeling to bridge the actuation gaps with randomization of non-ideal effects such as backlash, torque-speed saturation. Using an asymmetric actor-critic PPO pipeline trained entirely in simulation, our policies deploy directly to a five-finger hand. The resulting policies demonstrated two essential skills: (1) command-based, controllable grasp force tracking, and (2) reorientation of objects in the hand, both of which were robustly executed without fine-tuning on the robot. By combining tactile and torque in the observation space with effective sensing/actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge, this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation and transferred zero-shot on real hardware.

| Subjects: | Robotics (cs.RO); Artificial Intelligence (cs.AI) |
| --- | --- |
| Cite as: | [arXiv:2601.02778](https://arxiv.org/abs/2601.02778) \[cs.RO\] |
|  | (or [arXiv:2601.02778v2](https://arxiv.org/abs/2601.02778v2) \[cs.RO\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2601.02778](https://doi.org/10.48550/arXiv.2601.02778) |

## Submission history

From: Zhe Zhao \[[view email](https://arxiv.org/show-email/8918ad7c/2601.02778)\]  
**[\[v1\]](https://arxiv.org/abs/2601.02778v1)** Tue, 6 Jan 2026 07:26:39 UTC (4,032 KB)  
**\[v2\]** Fri, 9 Jan 2026 13:09:26 UTC (4,032 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2601.02778) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
