---
source_id: "SRC-robotics-102"
title: "CoinFT force-torque fingertip sensor project"
source_type: "hardware_project"
publisher: "Stanford"
source_date: "2026"
url: "https://coin-ft.github.io/"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-05-27T02:22:12+00:00"
tags:
  - raw/source
  - source-type/hardware-project
  - evidence/a
aliases:
  - SRC-robotics-102
---
# CoinFT force-torque fingertip sensor project

## Abstract

We introduce CoinFT, a capacitive 6-axis force/torque (F/T) sensor that is compact, light, low-cost, and robust with an average mean-squared error of 0.11N for force and 0.84mNm for moment when the input ranges from 0∼10N and 0∼4N in normal and shear directions, respectively. CoinFT is a stack of two rigid PCBs with comb-shaped electrodes connected by an array of silicone rubber pillars. The microcontroller interrogates the electrodes in different subsets in order to enhance sensitivity for measuring 6-axis F/T. The combination of desirable features of CoinFT enables various contact-rich robot interactions at a scale, across different embodiment domains including drones, robot end-effectors, and wearable haptic devices. We demonstrate the utility of CoinFT on drones by performing an attitude-based force control to perform tasks that require careful contact force modulation.

## CoinFT Applications

### Dexterous Manipulation

### In-the-Wild Compliant Manipulation with UMI-FT

CoinFTs on each finger of a modified UMI device is used to collect multimodal data and perform compliance control on both external contact forces and internal grasp forces during manipulation.

[Project Website](https://umi-ft.github.io/)

---

### DexForce: Extracting Force-informed Actions from Kinesthetic Demonstrations for Dexterous Manipulation

CoinFTs are mounted on the fingers of a dexterous hand and are used to teach robots forceful dexterous manipulation through kinesthetic teaching.

[Project Website](https://clairelc.github.io/dexforce.github.io/)

### Drones

### Contact Force Control of Aerial Vehicles

A attitude-based force PID control enables aerial vehicles to regulate contact force using CoinFT, allowing drones to perform contact-based tasks reliably.

### Wearable Devices

![CoinFT on a wrist mounted device](https://coin-ft.github.io/static/images/coinft-wristDevice2.png)

CoinFT on a wrist mounted device

### Perceived Intensities of Normal and Shear Skin Stimuli using a Wearable Haptic Bracelet

CoinFT is used to compare intensity perception of normal and shear forces through a haptic bracelet.

[Paper](https://arxiv.org/abs/1911.02104)

### Design and Evaluation of a 3-DoF Haptic Device for Directional Shear Cues on the Forearm

A 3-DoF forearm-mounted haptic device can provide force-controlled haptic feedback using CoinFT.

[Paper](https://ieeexplore.ieee.org/document/10433850/)

### {Your Cool Project Here}

## CoinFT Maintenance and Support

![Seongheon Hong](https://coin-ft.github.io/static/images/seongheon.JPG)

Seongheon Hong

Seongheon Hong

![Mark Cutkosky](https://coin-ft.github.io/static/images/mark.jpg)

Mark Cutkosky

Mark Cutkosky

CoinFT continues to be researched and developed by [Hojung Choi](https://www.hojungchoi.com/), Seongheon Hong, and Mark Cutkosky at the [Biomimetics and Dexterous Manipulation Laboratory (BDML)](https://bdml.stanford.edu/) at [Stanford University](https://www.stanford.edu/).

For questions and feedback, please email Hojung (ilovehjb0520@gmail.com) and Seongheon (wbfprp@stanford.edu).

## BibTeX

```
@misc{choi2025coinftcoinsizedcapacitive6axis,
      title={CoinFT: A Coin-Sized, Capacitive 6-Axis Force Torque Sensor for Robotic Applications}, 
      author={Hojung Choi and Jun En Low and Tae Myung Huh and Gabriela A. Uribe and Seongheon Hong and Kenneth A. W. Hoffman and Julia Di and Tony G. Chen and Andrew A. Stanley and Mark R. Cutkosky},
      year={2025},
      eprint={2503.19225},
      archivePrefix={arXiv},
      url={https://arxiv.org/abs/2503.19225}}
```
