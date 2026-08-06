---
source_id: "SRC-robotics-387"
title: "Lightwheel Newton partnership and deformable-terrain asset pipeline"
source_type: "technical_blog"
publisher: "Lightwheel"
source_date: "2025-09-29"
url: "https://lightwheel.ai/media/lightwheel-newton"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-08-06T02:05:23+00:00"
tags:
  - raw/source
  - source-type/technical-blog
  - evidence/a
aliases:
  - SRC-robotics-387
---
# Lightwheel Newton partnership and deformable-terrain asset pipeline

Blogs

Lightwheel-Newton Partnership on Development of High-Quality Locomotion Assets for the Newton Physics Engine

## Lightwheel-Newton Partnership on Development of High-Quality Locomotion Assets for the Newton Physics Engine

The robotics simulation landscape is evolving beyond the capabilities of mature, rigid-body-only simulators like [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim) and MuJoCo. To address the next frontier of simulation—encompassing complex material interactions, granular media, and deformable objects—industry leaders including [NVIDIA](https://nvidianews.nvidia.com/news/nvidia-accelerates-robotics-research-and-development-with-new-open-models-and-simulation-libraries), Google DeepMind, and Disney Research are pioneering the development of [Newton](https://github.com/newton-physics) an open-source, GPU-accelerated and extensible physics engine for robot learning.

Lightwheel has joined this collaborative consortium as a core contributor, driven by a shared vision to bridge the sim2real gap for increasingly complex robotic tasks. Our collaboration is direct and focused: to develop and provide the highest-quality simulation assets, thereby accelerating both the adoption of Newton and its utility for the broader research and industrial communities.

This collaboration is a natural extension of Lightwheel's position as a market leader in simulation-ready ("SimReady") assets. Our expertise spans the creation of rigid, articulated, rigid-articulated, deformable, and fluid assets for diverse applications, including robotic and medical simulations. Our recent launch of [simready.com](https://simready.com/) —the largest open source library of SimReady assets for Isaac Sim and robotics—and our work on upgrading the foundational YCB benchmark to be cross-platform (supporting both Isaac Sim.usd and MuJoCo.mjcf formats) exemplify our commitment to universal accessibility and physical realism. These assets are now teleoperation-ready and reinforcemnet learning-ready for the two largest simulators on the market.

This article details our specific contribution to Newton: the creation of a comprehensive asset pipeline and simulation environment for legged robot locomotion training over granular materials.

<video src="https://lw-cdn.lightwheel.net/web-assets/lightwheel_v1/lightwheel-newton-view.mp4" controls=""></video>

A demonstration of the ANYmal robot walking across different physical materials

## Project Overview: Newton for Robot Locomotion Training

Solver Selection: The Implicit Material Point Method (MPM)

The Newton engine supports multiple solvers. For this project, we selected the Material Point Method (MPM) solver for three key reasons:

**Stability and Maturity**: The MPM implementation in [Newton](https://github.com/newton-physics/newton/tree/main) has demonstrated superior stability for large-scale simulations. This MPM method itself is a well-established technique for simulating continuum materials. This implementation of implicit MPM solver in Newton is from SIGGRAPH 2016 paper by Gilles Daviet and team (at the time CPU- based), for reference, please visit the [paper](https://dl.acm.org/doi/10.1145/2897824.2925877).

**Intuitive Real-World Interactions**: MPM is uniquely suited for simulating the complex dynamics of deformable materials like sand, soil, and snow. This allows for highly realistic and physically accurate interactions between a locomoting robot and its environment, a critical requirement for effective sim2real transfer.

**Validation Use-Case**: This project serves as an ambitious and practical test case to rigorously validate, stress-test, and iteratively improve both the Newton engine and its Implicit MPM solver in collaboration with the Newton development team.

## Asset Pipeline and Created Assets

To ensure a scalable and artist-driven workflow, we developed a pipeline that extends Universal Scene Description (OpenUSD) assets with Newton-specific attributes. Since both Lightwheel and Newton are based on OpenUSD, the assets and composition engine are designed to scale the aggregation of data needed to describe robots and their environments. A dedicated scene parsing pipeline within Newton automatically assembles all physical properties and collisions from these assets. The created assets fall into two categories:

### 1\. Mesh Assets:

**Description**: A 12m × 12m terrain with various obstacles (rocks, tree stumps) was created to form a challenging sandbox environment for humanoid locomotion.

**Pipeline**: All assets include high-fidelity collisions and materials/textures, which are automatically set up in DCC (Digital Content Creation) tools like Houdini and rendered correctly in Isaac Sim.

**Dual Solver Support**: To accommodate both the Implicit MPM and MuJoCo Warp solvers, collision meshes were processed differently:

For Implicit MPM Solver: Collisions directly use the original, high-detail triangle meshes.

For MuJoCo Warp Solver: Complex meshes were pre-processed with convex decomposition to ensure stable collision handling, with the results cached for performance.

### 2\. Particle Assets (MPM):

**Description**: Particle systems for sand, soil, and snow were authored in a DCC tool and saved as OpenUSD assets.

**Newton Integration**: Each particle system is annotated with Newton-specific attributes, enabling full support for multiple physical material constraints within the MPM solver.

**Material Properties**: Distinct material parameters (e.g., cohesion, friction, elasticity) were assigned to each particle type (sand, soil, snow) to accurately model their unique physical behaviors.

The linked video provides a close-up demonstration highlighting the differences between various physical materials.

We found that starting from Newton’s initial recommended settings was a solid baseline. In subsequent experiments, we made targeted adjustments — for example, modifying particle radius and friction — to better capture certain specific behavioral characteristics and achieve more realistic results. (Optional) Here is a comparison between the particle settings before and after:

## Experimental Setup & Initial Results

### Robot Platform:

The initial experiments utilized the ANYmal quadruped robot, as provided in the Newton examples.

[Reference](https://github.com/newton-physics/newton-assets.git)

Future work will transition to a humanoid robot to more effectively demonstrate bipedal locomotion in complex terrains.

### Robot Performance:

Using a pre-trained locomotion policy designed for flat terrain, the ANYmal robot struggled significantly on the uneven and deformable terrain. Even moderate slopes and obstacles prevented stable walking, highlighting the need for policies trained specifically in these complex environments—a primary goal this asset suite is designed to enable.

## Technical Challenges & Solutions

### The development process presented several key challenges:

**Material Constraints**: Implementing and validating different physical parameters for distinct particle groups (sand vs. snow) within the MPM framework required close collaboration with the Newton team to ensure solver stability for the Newton Beta release.

**Collision Handling**:

The requirement for convex decomposition in MuJoCo Warp, versus support for complex triangle meshes in Newton's Implicit MPM solver, necessitated a flexible asset pipeline. We added solver-specific asset attributes so our parsing pipeline could automatically provide the correct collision geometry to each solver. At this stage, we are using a custom schema to add these asset attributes, but in the future we plan to adopt the Newton USD schema for importing such attributes.

A significant early issue was particles leaking through collision meshes. Through iterative asset refinement and direct collaboration with Newton developers, this issue has been nearly completely resolved.

**DCC Pipeline Integration (Houdini):**

Initial USD interoperability issues within Houdini were resolved, resulting in a robust and efficient pipeline.

The team can now rapidly author and edit Newton-specific attributes on all assets, enabling quick iteration on terrain and particle setups.

The assembly of textured USD assets into a final scene is now efficient and straightforward.

The figure shows the process of terrain generation

The figure shows the process of particles generation

## Long-Term Goal & Current Performance

Our ultimate objective is to enable fully asset-driven simulation scenes in Newton in order to build an embodied simulation training platform with Newton as the core simulation backend.

Looking ahead, we plan to develop and contribute more Newton-based simulation assets within [NVIDIA Isaac Lab](https://developer.nvidia.com/isaac/lab).

## Current performance is promising:

On a Windows system with an NVIDIA RTX 4090, the simulation runs at 8-12 FPS with approximately 1.5 million implicit MPM particles. It is important to contextualize FPS in terms of real-time factor or offline. The simulation is synchronized, with rigid body dynamics and the MPM solver operating on their respective time steps, which enables meaningful real-time interaction despite the current frame rate. We anticipate further optimization of the scene and deployment rather than running on the Linux platform with a more powerful GPU, will achieve rates of 20 FPS or higher, making real-time demonstration and reinforcement learning training a tangible reality.

We anticipate further optimization of the scene and deployment rather than running on the Linux platform with a more powerful GPU, will achieve rates of 20 FPS or higher, making real-time demonstration and reinforcement learning training a tangible reality.

## Conclusion

This collaboration between Lightwheel and the Newton development team has produced a powerful, open-source asset pipeline and a high-quality simulation environment for legged locomotion over deformable terrains composed of diverse materials (e.g.: sand, soil, and snow..) By providing these resources, we aim to empower the community to tackle harder simulation problems and accelerate progress in robotics. The assets and environments are available on our GitHub repository [(Newton-LightWheel)](https://github.com/LightwheelAI/Newton-Lightwheel) to support further research and development.

**Newton**: Lightwheel and NVIDIA push simulation forward with high-quality assets for Newton, enabling locomotion training on deformable terrains

**USD Search**: Lightwheel integrates NVIDIA USD Search API to make 2,000+ curated robotics assets instantly discoverable by text or image queries.

**Benchmarks**: Lightwheel enhances LIBERO & RoboCasa on NVIDIA Isaac Lab–Arena with higher-quality assets, multi-robot support, and unified evaluation.

## Upcoming Livestream

**Closing the Sim2Real Gap with SimReady and AI**

**Date**: Oct 8, 2025 — 9:00 AM (PT)

**Speakers**: Madison Huang (NVIDIA), Steve Xie (Lightwheel), Akhil Docca (NVIDIA)

**Host**: Edmar Mendizabal (NVIDIA)

The future of robotics and [embodied AI](https://lightwheel.ai/egosuite) depends on solving the **Sim2Real gap** — making sure robots trained in simulation succeed in the real world. In this OpenUSD Insiders livestream, NVIDIA and Lightwheel will discuss how **SimReady assets, advanced simulation pipelines, and AI-driven training** are transforming robot development.

**Join the stream**:
