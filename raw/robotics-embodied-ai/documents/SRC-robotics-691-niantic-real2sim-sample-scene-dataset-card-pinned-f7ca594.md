---
source_id: "SRC-robotics-691"
title: "Niantic Real2Sim sample scene dataset card pinned f7ca594"
source_type: "dataset_card"
publisher: "Niantic Spatial"
source_date: "2026-08-01"
url: "https://huggingface.co/datasets/NianticSpatial/real2sim-sample-usdz-scenes/raw/f7ca59406bf15cdaf28e9c95bb99a317ebd7c83c/README.md"
evidence_grade: "S"
capture_method: "direct-download"
captured_at: "2026-11-10T02:02:05+00:00"
tags:
  - raw/source
  - source-type/dataset-card
  - evidence/s
aliases:
  - SRC-robotics-691
---
# Niantic Real2Sim sample scene dataset card pinned f7ca594

---
license: cc-by-4.0
pretty_name: Niantic Spatial Real2Sim Sample USDZ Scenes
tags:
- robotics
- physical-ai
- simulation
- real-to-sim
- isaac-sim
- isaac-lab
- 3d-reconstruction
- usdz
- usd
---

# Niantic Spatial Real2Sim Sample USDZ Scenes

Sample real-world USDZ scenes and particle-field variants from Niantic Spatial for robotics simulation and physical AI workflows.

## Why this exists

The real world is the best simulation.

This repository contains sample scene assets from Niantic Spatial to help developers evaluate real-to-sim robotics and physical AI workflows in NVIDIA Isaac Sim and Isaac Lab.

## What's included

This repository includes two representations of the same four sample scenes:

* **NuRec Volume Schema**
  * Four packaged USDZ sample scenes intended as the primary simulation-ready assets.
* **Particle Field Schema**
  * Four companion sample scenes representing the same environments in a particle-field format.

## NuRec vs. Particle Field

Both representations come from the same underlying real-world captures, but they are packaged differently.

* **NuRec Volume Schema** is the packaged, NVIDIA-oriented simulation format and the simplest place to start for real-to-sim evaluation in Isaac Sim and Isaac Lab.
* **Particle Field Schema** is the companion particle-field representation of the same scenes for developers who want to work with an alternate, more native open 3D scene format.

## License

This dataset is published under the **CC-BY-4.0** license.

## About Niantic Spatial

Niantic Spatial builds real-world foundation models for physical AI.

Our technology helps robots, agents, and people understand and operate in physical environments through geometrically accurate 3D reconstruction, precise localization, and spatial understanding. Built on 30+ billion posed real-world images and 25 years of planet-scale mapping and 3D reconstruction leadership, Niantic Spatial serves enterprise use cases across robotics, defense, and oil and gas.

In robotics, we help close the sim-to-real gap with a real-to-sim-to-real workflow: turning fast real-world captures into simulation-ready digital twins for physical AI workflows, including NVIDIA Isaac Sim and Isaac Lab. We also provide precise visual positioning for robotic assets operating indoors, outdoors, and in GPS-denied environments.

Learn more at [nianticspatial.com](https://www.nianticspatial.com).
