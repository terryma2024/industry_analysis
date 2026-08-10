---
source_id: "SRC-robotics-502"
title: "DexCap project page"
source_type: "project_page"
publisher: "Stanford University"
source_date: "2024-07-04"
url: "https://dex-cap.github.io/"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-08-09T08:25:07+00:00"
tags:
  - raw/source
  - source-type/project-page
  - evidence/s
aliases:
  - SRC-robotics-502
---
# DexCap project page

## DexCap: Scalable and Portable Mocap DataCollection System for Dexterous Manipulation

![](https://dex-cap.github.io/assets/logos/SUSig-red.png)

## Abstract

Imitation learning from human hand motion data presents a promising avenue for imbuing robots with human-like dexterity in real-world manipulation tasks. Despite this potential, substantial challenges persist, particularly with the portability of existing hand motion capture (mocap) systems and the difficulty of translating mocap data into effective control policies. To tackle these issues, we introduce DexCap, a portable hand motion capture system, alongside DexIL, a novel imitation algorithm for training dexterous robot skills directly from human hand mocap data. DexCap offers precise, occlusion-resistant tracking of wrist and finger motions based on SLAM and electromagnetic field together with 3D observations of the environment. Utilizing this rich dataset, DexIL employs inverse kinematics and point cloud-based imitation learning to replicate human actions with robot hands. Beyond learning from human motion, DexCap also offers an optional human-in-the-loop correction mechanism to refine and further improve robot performance. Through extensive evaluation across six dexterous manipulation tasks, our approach not only demonstrates superior performance but also showcases the system's capability to effectively learn from in-the-wild mocap data, paving the way for future data collection methods for dexterous manipulation.

---

## DexCap: A Portable Hand Motion Capture System

Overview of the DexCap system:  
**Front design:** A camera rack on the chest is equipped with an RGB-D LiDAR camera and three SLAM tracking cameras.  
**Back design:** A mini-PC and power bank in the backpack power the system for approximately 40 minutes of data collection.  
**Data collection process:** The tracking cameras, initially placed in the camera rack for calibration, are relocated to hand mounts during data collection to consistently track the palm positions. Finger motions are captured by motion capture gloves.

**Data visualization:** 3D hand motion capture data in point cloud observation.

**Data collection throughput:** DexCap is about three times faster than teleoperation in data collection throughput and is close to the level of natural human motion.

**Compare to vision-based method:** In this example, human is holding the mug handle with a fixed gesture. The vision-based hand tracking method used by the VR headset fails to accurately track finger positions due to heavy occlusion. DexCap is more capable of collecting hand-object interaction data.

## From Human to Robot

**Observation retargeting:** To simplify the process of switching the camera system between the human and robot, a quick-release buckle has been integrated into the back of the camera rack, allowing for swift camera swaps – in less than 20 seconds. In this way, the robot utilizes the same observation camera employed during human data collection.

**Action retargeting:** To transfer human finger motion to the LEAP robot hand, we use fingertip inverse kinematics (IK) to compute the 16-dimensional joint positions. Human finger motions are tracked using a pair of motion capture gloves, which measure the 3D positions of the fingers relative to the palm based on electromagnetic field (EMF).

**Visual gap:** To further bridge the visual gap between human hand and robot hand, we use forward kinematics to genrate a point cloud mesh of the robot hand and add it to the pointcloud observation as is shown in this video.

---

## Method: Data Retargeting and Imitation Learning

We first retarget the DexCap data to the robot embodiment by constructing 3D point clouds from RGB-D observations and transforming it into robot operation space. Meanwhile, the hand motion capture data is retargeted to the dexterous hand and robot arm with fingertip IK. Based on the data, a Diffusion Policy is learned to take the point cloud as input and outputs a sequence of future goal positions as the robot actions.

## Results

## Bimanual Manipulation Task

---

## In-the-wild Data Collection with DexCap

## Policy learned with In-the-wild DexCap Data

---

## Human-in-the-loop correction with DexCap

DexCap supports two types of human-in-the-loop correction during the policy rollouts:  
**(1). Residual correction** measures the 3D delta position changes of the human wrist and incorporates them as residual actions to the robot's wrist movements. This mode enables minimal movement but requiring more precise control.  
**(2). Teleoperation** directly translates full human hand motions to the robot end-effector actions based on inverse kinematics. This mode enables the full control over the robot but requiring more effort.  
Users can switch between the two modes by stepping on the foot pedal during the rollouts.

![Description of Image](https://dex-cap.github.io/assets/HIL_method.png)

The corrections are stored in a new dataset and uniformly sampled with the original dataset for fine-tuning the robot policy

## Results after finetuning - Tea preparing

## Results after finetuning - Scissor cutting

---

## Acknowledgments

This research was supported by National Science Foundation NSF-FRR-2153854 and Stanford Institute for Human-Centered Artificial Intelligence, SUHAI. This work is partially supported by ONR MURI N00014-21-1-2801. We would like to thank Yunfan Jiang, Albert Wu, Paul de La Sayette, Ruocheng Wang, Sirui Chen, Josiah Wong, Wenlong Huang, Yanjie Ze, Christopher Agia, Jingyun Yang and the SVL PAIR group for providing help and feedback. We also thank Zhenjia Xu, Cheng Chi, Yifeng Zhu for their suggestions in tuning the robot controller. We especially thank Kenneth Shaw, Ananye Agrawal, Deepak Pathak for open-sourcing the LEAP Hand.

---

## BibTeX

@article{wang2024dexcap,  
title = {DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation},  
author = {Wang, Chen and Shi, Haochen and Wang, Weizhuo and Zhang, Ruohan and Fei-Fei, Li and Liu, C. Karen},  
journal = {arXiv preprint arXiv:2403.07788},  
year = {2024}  
}
