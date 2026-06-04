---
source_id: "SRC-robotics-115"
title: "NVIDIA Isaac Lab developer page"
source_type: "technology_platform"
publisher: "NVIDIA Developer"
source_date: "2026"
url: "https://developer.nvidia.com/isaac/lab"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-06-04T06:08:12+00:00"
tags:
  - raw/source
  - source-type/technology-platform
  - evidence/a
aliases:
  - SRC-robotics-115
---
# NVIDIA Isaac Lab developer page

## NVIDIA Isaac Lab

NVIDIA Isaac™ Lab is an open-source, GPU-accelerated, agent-ready simulation framework for robot learning designed to train robot policies at scale.

It supports flexible integration across physics engines, renderers, and learning algorithms, including Newton and NVIDIA Omniverse™ libraries. This helps to accelerate vision and perception training for real-world robot applications, from desktop to cloud.

---

## How Isaac Lab Works

Isaac Lab’s modular architecture and NVIDIA GPU-based parallelization make it ideal for building robot policies that cover a wide range of embodiments, including [humanoid robots](https://www.nvidia.com/en-us/glossary/humanoid-robot/), manipulators, and autonomous mobile robots (AMRs).

This gives you a comprehensive framework for robot learning, covering everything from environment setup to policy training. It supports both [imitation](https://www.nvidia.com/en-us/glossary/imitation-learning/) and [reinforcement learning](https://www.nvidia.com/en-us/glossary/reinforcement-learning/) methods. Plus, you can further customize and extend Isaac Lab capabilities with a variety of physics engines, such as Newton, NVIDIA® PhysX®, [NVIDIA Warp](https://developer.nvidia.com/warp-python), and MuJoCo.

Isaac Lab is also the foundational robot learning framework of the [NVIDIA Isaac GR00T platform](https://developer.nvidia.com/isaac/gr00t).

![Isaac Lab’s comprehensive platform for robot learning and robot policy building](https://developer.download.nvidia.com/images/isaac/lab/how-nvidia-isaac-lab-works.jpg)

Isaac Lab’s comprehensive platform for robot learning and robot policy building

## Introductory Resources

### Isaac Lab Whitepaper

See how the combination of advanced simulation capabilities and data center scale execution unlock breakthroughs in [robotics research](https://www.nvidia.com/en-us/research/robotics/).

### NVIDIA Isaac Lab-Arena

Built on Isaac Lab, Isaac Lab-Arena is an open-source framework for scalable policy evaluation in simulation.

### Isaac Lab Courses

Explore the fundamentals of robot learning and Isaac Lab, a powerful tool for developing robotic applications.

### Isaac Lab Office Hours

Stay informed with our [recurring office hours](https://addevent.com/calendar/ae483892) that cover in-depth topics with experts answering questions about Isaac Lab.

---

## Starter Kits

View more tutorials and how-to guides in the [documentation](https://isaac-sim.github.io/IsaacLab/main/source/tutorials/index.html).

### Accelerate Robot Learning

Choose from reinforcement learning and imitation learning to train AI robots. Easily bring your custom libraries and use the direct agent-environment or hierarchical-manager development workflows.

- [Read Use Case: Robot Learning](https://www.nvidia.com/en-us/use-cases/robot-learning/?)
- [Isaac GR00T-Mimic Blueprint for Synthetic Manipulation Motion Generation](https://github.com/NVIDIA-Omniverse-blueprints/synthetic-manipulation-motion-generation)
- [Physical AI Dataset](https://huggingface.co/collections/nvidia/physicalai-67c643edbb024053dcbcd6d8)

### Enable Perception in the Loop

Tiled rendering reduces rendering time by consolidating input from multiple cameras into a single large image. With a streamlined API for handling vision data, the rendered output directly serves as observational data for simulation learning.

- [Read Guide: Tiled Rendering](https://isaac-sim.github.io/IsaacLab/main/source/overview/sensors/camera.html#tiled-rendering)

### Scale With Multi-GPU and Multi-Node Training

Scale up training of cross-embodied models for complex reinforcement learning environments across multiple GPUs and nodes. Deploy locally and on the cloud (AWS, GCP, Azure, and Alibaba Cloud) by integrating with NVIDIA OSMO.

- [Read Guide: Multi-GPU and Multi-Node Rendering](https://isaac-sim.github.io/IsaacLab/main/source/features/multi_gpu.html)

### Accurate High-Fidelity Physics Simulation and Rendering in Omniverse

Tap into the latest GPU-accelerated PhysX version through Isaac Lab, including support for deformables, ensuring quick and accurate physics simulations augmented by domain randomizations.

- [Read Guide: Mastering Omniverse for Robotics](https://isaac-sim.github.io/IsaacLab/main/source/how-to/master_omniverse.html#)

---

## Isaac Lab Learning Library

Research

A GPU Accelerated Simulation Framework For Multi-Modal Robot Learning

**NVIDIA Isaac Lab**

We present Isaac Lab, the natural successor to Isaac Gym, which extends the paradigm of GPU-native robotics simulation into the era of large-scale multi-modal learning.

Tech Blog

Streamline Robot Learning with Whole-Body Control and Enhanced Teleoperation in NVIDIA Isaac Lab 2.3

**NVIDIA Isaac Lab
**
The latest version of Isaac Lab 2.3, in early developer preview, improves humanoid robot capabilities with advanced whole-body control, enhanced imitation learning, and better locomotion.

Tech Blog

Quadruped Robot Locomotion and Multiphysics Simulation Using Newton in NVIDIA Isaac Lab

**NVIDIA Isaac Lab**

Walks through how to train a quadruped robot to move from one point to another and how to set up a multiphysics simulation with an industrial manipulator to fold clothes. This tutorial uses Newton within NVIDIA Isaac Lab.
