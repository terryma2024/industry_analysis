---
source_id: "SRC-robotics-410"
title: "NVIDIA Isaac Sim current asset ingestion overview"
source_type: "product_documentation"
publisher: "NVIDIA"
source_date: "2026-08-06"
url: "https://developer.nvidia.com/isaac/sim"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-08-06T03:34:18+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/s
aliases:
  - SRC-robotics-410
---
# NVIDIA Isaac Sim current asset ingestion overview

## NVIDIA Isaac Sim

NVIDIA Isaac Sim™ is an open source reference framework built on [NVIDIA Omniverse](https://developer.nvidia.com/omniverse) ™ libraries for robotics simulation, testing, and synthetic data generation in physically based virtual environments.

Isaac Sim is fully extensible, so developers can build custom [OpenUSD](https://www.nvidia.com/en-us/glossary/openusd/) -based simulators or integrate framework capabilities into existing testing and validation pipelines.

Ready to get started?

---

## How Isaac Sim Works

Isaac Sim can ingest data from multiple sources—such as computer-aided design (CAD), Unified Robot Description Format (URDF), or real-world captures via [NVIDIA Omniverse NuRec](https://docs.nvidia.com/nurec/index.html) and Isaac TeleOp—and convert it into USD. Developers then assemble simulation scenes by assigning materials, enabling physics, and configuring robot and sensor models. From there, robots can be used with [NVIDIA Isaac Lab](https://developer.nvidia.com/isaac/lab) for [robot learning](https://www.nvidia.com/en-us/use-cases/robot-learning/) and simulated in Isaac Sim.

Isaac Sim also supports controllable synthetic data generation, letting developers build custom data pipelines that complement their existing data sources. That data can be further augmented with NVIDIA Cosmos™ world foundation models. Finally, developers can train perception and mobility stacks in simulation and evaluate the end-to-end system in Isaac Sim using software-in-the-loop or hardware-in-the-loop testing.

![A diagram showing how NVIDIA NeMo Retriever works from data ingestion to information retrieval.](https://developer.download.nvidia.com/images/isaac/sim/isaac-sim-main.png)

NVIDIA NeMo Retriever collection of NIM microservices are used to build optimized ingestion and retrieval pipelines for highly accurate information retrieval at scale.

### Isaac Sim Documentation

Browse documentation and learn how to get started on Isaac Sim.

### Robotics Simulation Overview

Learn how robotics simulation helps developers virtually train, test, and validate robots, and the advantages of a simulation-first approach.

### Isaac Sim Courses

Gain a foundational understanding of core robotics concepts and explore essential workflows in simulation and robot learning with hands-on training in Isaac Sim™ and Isaac Lab.

### Isaac Sim Office Hours

Stay informed with our [recurring Office Hours](https://addevent.com/calendar/ae483892) that cover in-depth topics with experts and customers using Isaac Sim.

---

## Starter Kits

### Neural Reconstruction and Rendering With NVIDIA Omniverse NuRec

Turn real world sensor data into interactive simulation [with NuRec](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nre/containers/nre-ga?version=latest) using 3D Gaussian Splatting-based rendering for enhanced efficiency and accuracy.  

- [Getting Started With Neural Rendering](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/neural-rendering.html)
- [How to Instantly Render Real-World Scenes in Interactive Simulation](https://developer.nvidia.com/blog/how-to-instantly-render-real-world-scenes-in-interactive-simulation/)
- [3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://research.nvidia.com/labs/toronto-ai/3DGUT/)
- [Reconstruct a Scene in NVIDIA Isaac Sim Using Only a Smartphone](https://developer.nvidia.com/blog/reconstruct-a-scene-in-nvidia-isaac-sim-using-only-a-smartphone/)
- [Simulate Robotic Environments Faster with NVIDIA Isaac Sim and World Labs Marble](https://developer.nvidia.com/blog/simulate-robotic-environments-faster-with-nvidia-isaac-sim-and-world-labs-marble)

### Realistic Physics Simulation

Model the physical behavior of objects and systems foundational to physical AI.  
  
Isaac Sim can simulate rigid body and vehicle dynamics, multi-joint articulation, SDF colliders, and more for realistic physics simulation  

- [Physics Simulation Fundamentals](https://docs.omniverse.nvidia.com/isaacsim/latest/simulation_fundamentals.html)
- [Getting Started Guides for Sensor Simulation](https://docs.omniverse.nvidia.com/isaacsim/latest/features/sensors_simulation/index.html)
- [NVIDIA® PhysX®](https://developer.nvidia.com/physx-sdk)
- [Newton](https://developer.nvidia.com/blog/announcing-newton-an-open-source-physics-engine-for-robotics-simulation)

### Scalable Synthetic Data Generation

Bootstrap AI model training with synthetic data.  
  
Generate training data by randomizing attributes like lighting, reflection, color, and position of scene and assets.  

- [Synthetic Data Generation Use Cases](https://www.nvidia.com/en-us/use-cases/synthetic-data/)
- [Omniverse Replicator Getting Started Guide](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/getting_started.html)
- [Scaling Action Recognition Models With Synthetic Data Blog](https://developer.nvidia.com/blog/scaling-action-recognition-models-with-synthetic-data/)

### ROS Support

Custom ROS2 messages and URDF/MJCF are now open-source.  
  
Get support for custom ROS messages that allow standalone scripting to manually control the simulation steps.  

- [URDF Importer Getting Started Guide](https://docs.isaacsim.omniverse.nvidia.com/latest/importer_exporter/ext_isaacsim_asset_importer_urdf.html)

### Robotics Learning

Virtually train, test, and validate robotics systems using NVIDIA Isaac Lab.  

- [Isaac Lab Whitepaper](https://research.nvidia.com/publication/2025-09_isaac-lab-gpu-accelerated-simulation-framework-multi-modal-robot-learning)
- [Isaac Lab Reference Architecture](https://isaac-sim.github.io/IsaacLab/main/source/refs/reference_architecture/index.html)
- [Isaac GR00T for Synthetic Manipulation Motion Generation](https://build.nvidia.com/nvidia/isaac-gr00t-synthetic-manipulation)

### Industrial Facility Digital Twin

Build intelligent factory, warehouse, and industrial facility solutions that enable comprehensive design, simulation, and optimization of industrial assets and processes.  

- [Mega NVIDIA Omniverse Blueprint for Multi-Robot Fleet Simulation](https://build.nvidia.com/nvidia/mega-multi-robot-fleets-for-industrial-automation)

---

#### Newton, the Next-Generation Open-Source Physics Simulation Engine

Newton is an open-source, GPU-accelerated, and extensible physics engine, co-developed by Google DeepMind and Disney Research, and [managed by the Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-contribution-of-newton-by-disney-research-google-deepmind-and-nvidia-to-accelerate-open-robot-learning). Built on NVIDIA Warp and OpenUSD, Newton is optimized for robotics and compatible with learning frameworks such as MuJoCo Playground or NVIDIA Isaac Lab. [Newton Beta](https://github.com/newton-physics) is now available to use.

![](https://developer.download.nvidia.com/images/isaac/newton-ari.jpg)
