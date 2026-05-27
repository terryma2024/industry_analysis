---
source_id: "SRC-robotics-065"
title: "Universal Manipulation Interface project page"
source_type: "project_page"
publisher: "Stanford/Columbia/Toyota Research Institute"
source_date: "2024"
url: "https://umi-gripper.github.io/"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-05-27T01:34:04+00:00"
tags:
  - raw/source
  - source-type/project-page
  - evidence/a
aliases:
  - SRC-robotics-065
---
# Universal Manipulation Interface project page

![](https://umi-gripper.github.io/images/stanford_logo.png) ![](https://umi-gripper.github.io/images/columbia_engineering_logo.svg) ![](https://umi-gripper.github.io/images/tri_logo_landscape.svg)

## Universal Manipulation Interface

## In-The-Wild Robot Teaching Without In-The-Wild Robots

We present Universal Manipulation Interface (UMI) -- a data collection and policy learning framework that allows direct skill transfer from in-the-wild human demonstrations to deployable robot policies. UMI employs hand-held grippers coupled with careful interface design to enable portable, low-cost, and information-rich data collection for challenging bimanual and dynamic manipulation demonstrations. To facilitate deployable policy learning, UMI incorporates a carefully designed policy interface with inference-time latency matching and a relative-trajectory action representation. The resulting learned policies are hardware-agnostic and deployable across multiple robot platforms. Equipped with these features, UMI framework unlocks new robot manipulation capabilities, allowing zero-shot generalizable dynamic, bimanual, precise, and long-horizon behaviors, by only changing the training data for each task. We demonstrate UMI’s versatility and efficacy with comprehensive real-world experiments, where policies learned via UMI zero-shot generalize to novel environments and objects when trained on diverse human demonstrations.

---

### Paper

Latest version: [arXiv](https://arxiv.org/abs/2402.10329) or [here](https://umi-gripper.github.io/umi.pdf).  
Robotics: Science and Systems (RSS) 2024

★ Best Systems Paper Award Finalist, RSS ★

[![](https://umi-gripper.github.io/images/umi_thumbnail.png)](https://umi-gripper.github.io/umi.pdf)

### Code and Tutorial

 [![](https://umi-gripper.github.io/images/github_logo.svg) Codebase](https://github.com/real-stanford/universal_manipulation_interface)

 [![](https://umi-gripper.github.io/images/build.svg) Hardware Guide](https://docs.google.com/document/d/1TPYwV9sNVPAi0ZlAupDMkXZ4CA1hsZx7YDMSmcEy6EU/edit?usp=sharing)

 [![](https://umi-gripper.github.io/images/documentation.svg) Data Collection Instruction](https://swanky-sphere-ad1.notion.site/UMI-Data-Collection-Tutorial-4db1a1f0f2aa4a2e84d9742720428b4c?pvs=4)

![](https://www.youtube.com/watch?v=EJmAg1Bnp-k)
  
[3D Printing Tutorial](https://youtu.be/EJmAg1Bnp-k?si=24dVkyAtTY2MHnLp)

![](https://www.youtube.com/watch?v=x3ko0v_xwpg)
  
[Assembly Tutorial](https://youtu.be/x3ko0v_xwpg?si=cQnTKZEktMx3oPpf)

---

UMI’s data collection hardware takes the form of a hand-held parallel jaw gripper, mounted with a GoPro camera ①. To gather policy-deployable observations, UMI needs to capture sufficient visual context to infer action ② and critical information like depth ③. To obtain action data leading to deployable policies, UMI needs to capture precise robot action under fast human motion ④, fine adjustments on griping width ⑤, and automatically check whether each demonstration is valid under the specific robot kinematic constraints ⑥. ·
