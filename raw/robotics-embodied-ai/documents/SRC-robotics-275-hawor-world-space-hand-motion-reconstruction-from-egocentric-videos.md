---
source_id: "SRC-robotics-275"
title: "HaWoR World-Space Hand Motion Reconstruction from Egocentric Videos"
source_type: "paper"
publisher: "CVPR / Computer Vision Foundation"
source_date: "2025-06"
url: "https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_HaWoR_World-Space_Hand_Motion_Reconstruction_from_Egocentric_Videos_CVPR_2025_paper.html"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-07-14T02:34:29+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-275
---
# HaWoR World-Space Hand Motion Reconstruction from Egocentric Videos

HaWoR: World-Space Hand Motion Reconstruction from Egocentric Videos

***Jinglei Zhang, Jiankang Deng, Chao Ma, Rolandos Alexandros Potamias***; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2025, pp. 1805-1815

  
**Abstract**  
  

Despite the advent in 3D hand pose estimation, current methods predominantly focus on single-image 3D hand reconstruction in the camera frame, overlooking the world-space motion of the hands. Such limitation prohibits their direct use in egocentric video settings, where hands and camera are continuously in motion. In this work, we propose HaWoR, a high-fidelity method for hand motion reconstruction in world coordinates from egocentric videos. We propose to decouple the task by reconstructing the hand motion in the camera space and estimating the camera trajectory in the world coordinate system. To achieve precise camera trajectory estimation, we propose an adaptive egocentric SLAM framework that addresses the shortcomings of traditional SLAM methods, providing robust performance under challenging camera dynamics. To ensure robust hand motion trajectories, even when the hands move out of view frustum, we devise a novel motion infiller network that effectively completes the missing frames of the sequence. Through extensive quantitative and qualitative evaluations, we demonstrate that HaWoR achieves state-of-the-art performance on both hand motion reconstruction and world-frame camera trajectory estimation under different egocentric benchmark datasets. Code and models are available on \\href https://hawor-project.github.io/ https://hawor-project.github.io/.

  
**Related Material**  
  

\[[pdf](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhang_HaWoR_World-Space_Hand_Motion_Reconstruction_from_Egocentric_Videos_CVPR_2025_paper.pdf)\] \[[supp](https://openaccess.thecvf.com/content/CVPR2025/supplemental/Zhang_HaWoR_World-Space_Hand_CVPR_2025_supplemental.zip)\] \[[arXiv](http://arxiv.org/abs/2501.02973)\]

\[bibtex\]

@InProceedings{Zhang\_2025\_CVPR, author = {Zhang, Jinglei and Deng, Jiankang and Ma, Chao and Potamias, Rolandos Alexandros}, title = {HaWoR: World-Space Hand Motion Reconstruction from Egocentric Videos}, booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}, month = {June}, year = {2025}, pages = {1805-1815} }
