---
source_id: "SRC-robotics-095"
title: "Oopsie Data manipulation failure dataset project"
source_type: "dataset_project"
publisher: "Oopsie Data contributors"
source_date: "2026"
url: "https://oopsie-data.com/"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-05-27T02:22:12+00:00"
tags:
  - raw/source
  - source-type/dataset-project
  - evidence/s
aliases:
  - SRC-robotics-095
---
# Oopsie Data manipulation failure dataset project

## Oopsie Data

> All successful robots are alike; each unsuccessful robot is unsuccessful in its own way.
> 
> L30 Tolstoy, Anna Kareni-Bot

![Logo](https://oopsie-data.com/assets/images/logo.png)

**[Oopsie Dataset](https://github.com/oopsie-data/oopsie-tools) project’s software toolkit for collecting, annotating, and managing robotic manipulation failures.**

This website explains the software tools for contributing failure data to the dataset: a multi-lab effort to build a large-scale dataset of robotic manipulation failures for offline RL, policy steering, and failure prediction.

The goal of this project is to enable research into how policy evaluation data, especially failures alongside successes, can improve robot policy training. Failed demonstrations are routinely collected during testing and evaluation, but immediately discarded as they provide no further use in common imitation learning pipelines. However, these failures contain crucial information about where current approaches break down, and can be used to train robots to recognize bottleneck states or request intervention from human operators.

To support research into how robotic failures can be used effectively, we need a varied dataset spanning different robot policies, tasks, and setups. Therefore, we share our tooling for collecting and annotating policy evaluation trajectories together with a **Call for Contributions**. Share your policy evaluation data with us, successes and failures, so that we can build datasets to enable the robotics community to investigate how to make full use of the data we produce every day.

---

## What this website provides

This website explains how to collect, annotate, and contribute data to our effort.

[Motivation](https://oopsie-data.com/motivation/) provides a more in-depth overview of the research vision.

[Quickstart](https://oopsie-data.com/quickstart/) provides an overview of the whole workflow with each individual step and links to detailed instructions for every step.

[Contributing](https://oopsie-data.com/contributing/) describes who can contribute and what benefits are available for contributing labs.

[Oopsie ToolKit](https://oopsie-data.com/tool/) describes the provided toolkit for recording and annotating robot manipulation failures.

[Frequently Asked Questions](https://oopsie-data.com/faq/) is a collection of frequent issues and questions that might arise during the use of our workflow. This is being continually expanded, and we invite you to open issues on github for any unanswered questions.

---

## An example of a common evaluation failure

Below are two example episodes from the initial dataset: one successful grasp and one failure on an Aloha robot using a diffusion policy. Recorded under similar conditions with the same policy, they highlight the fine-grained differences the dataset is designed to capture.

Even in a simple ball-grasping task, a slight gripper offset can cause failure. Capturing these nuances (and other common failure modes) is a core goal of this project.

<video controls=""><source src="https://oopsie-data.com/assets/videos/success_0.mp4" type="video/mp4"></video>

Successful episode

The robot is able to pick up the ball and place it in the bowl.

<video controls=""><source src="https://oopsie-data.com/assets/videos/failure_1.mp4" type="video/mp4"></video>

Failure episode

The robot fails to grasp the ball and instead pushes it to roll off the table.
