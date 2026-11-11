---
source_id: "SRC-robotics-693"
title: "MVSAnywhere official method and pose scale"
source_type: "research_project"
publisher: "Niantic et al."
source_date: "2025"
url: "https://nianticlabs.github.io/mvsanywhere/"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-11-10T02:02:05+00:00"
tags:
  - raw/source
  - source-type/research-project
  - evidence/s
aliases:
  - SRC-robotics-693
---
# MVSAnywhere official method and pose scale

![teaser.jpg](https://nianticlabs.github.io/mvsanywhere/resources/teaser.jpg)

### Abstract

---

Computing accurate depth from multiple views is a fundamental and longstanding challenge in computer vision. However, most existing approaches do not generalize well across different domains and scene types (e.g. indoor vs. outdoor). Training a general-purpose multi-view stereo model is challenging and raises several questions, e.g. how to best make use of transformer-based architectures, how to incorporate additional metadata when there is a variable number of input views, and how to estimate the range of valid depths which can vary considerably across different scenes and is typically not known a priori? To address these issues, we introduce MVSA, a novel and versatile Multi-View Stereo architecture that aims to work Anywhere by generalizing across diverse domains and depth ranges. MVSA combines monocular and multi-view cues with an adaptive cost volume to deal with scale-related issues. We demonstrate state-of-the-art zero-shot depth estimation on the Robust Multi-View Depth Benchmark, surpassing existing multi-view stereo and monocular baselines.

  
  
<video controls="" width="95%"><source src="https://nianticlabs.github.io/mvsanywhere/resources/videos/dron_mtb_both.mp4" type="video/mp4"></video>

Our model produces depth maps in the input camera pose scale. Here we show it estimating view consistent depths for a drone video.

### Approach

---

  
![method](https://nianticlabs.github.io/mvsanywhere/resources/images/method.jpg)

We construct a general-purpose multi-view depth estimation model. We start with a cost-volume based architecture, which matches deep features between views at different hypothesized depths. Key for performance are our Cost Volume Patchifier and Mono/Multi Cue Combiner. These also fuse single-view information coming from the Reference Image Encoder and source views.

#### Cost Volume Patchifier

![patchifier.jpg](https://nianticlabs.github.io/mvsanywhere/resources/images/patchifier.jpg)  

Our cost volume patchifier enables high-quality infor- mation to be extracted from a |D| × H/4 × W/4 cost volume, ready for input to the Mono/Multi Cue Combiner ViT. (a) Shows the naive approach to patchification. (b) Our approach makes better use of the reference image features.

### Results

---

#### Tanks and Temples - "Barn"

<video controls="" width="95%"><source src="https://nianticlabs.github.io/mvsanywhere/resources/videos/merged_barn.mp4" type="video/mp4"></video>  

#### Mesh Reconstruction via Depth TSDF Fusion

<video controls="" width="95%"><source src="https://nianticlabs.github.io/mvsanywhere/resources/videos/mesh_compare.mp4" type="video/mp4"></video>  
  

#### 3D Gaussian Splatting Depth Regularization - Mesh

#### 3DGS

<iframe width="95%" height="500em" src="https://sketchfab.com/models/5c6137a7d5d54c09918278a3722e53f1/embed" title="MVSAnywhere Regularized 3DGS Mesh" frameborder="0" allowfullscreen="" allow="autoplay; fullscreen; xr-spatial-tracking"></iframe>

#### 3DGS w/ MVSAnywhere

<iframe width="95%" height="500em" src="https://sketchfab.com/models/7c818e2b6a114a828bb52ea0d58ad614/embed" title="MVSAnywhere Regularized 3DGS Mesh" frameborder="0" allowfullscreen="" allow="autoplay; fullscreen; xr-spatial-tracking"></iframe>

#### 3DGS w/ Metric3D

<iframe width="95%" height="500em" src="https://sketchfab.com/models/83702776dda04ff4bdb55b823a70a462/embed" title="MVSAnywhere Regularized 3DGS Mesh" frameborder="0" allowfullscreen="" allow="autoplay; fullscreen; xr-spatial-tracking"></iframe>  
  

### Resources

---

#### Paper and Supplemental

[![Paper](https://nianticlabs.github.io/mvsanywhere/resources/paper_thumb.jpg)](https://nianticlabs.github.io/mvsanywhere/resources/MVSAnywhere.pdf)

#### Code

[![github_repo.jpg](https://nianticlabs.github.io/mvsanywhere/resources/github_repo.jpg)](https://github.com/nianticlabs/MVSAnywhere)

If you find this work useful for your research, please cite:

```
@inproceedings{izquierdo2025mvsanywhere,
  title={{MVSAnywhere}: Zero Shot Multi-View Stereo},
  author={Izquierdo, Sergio and Sayed, Mohamed and Firman, Michael and Garcia-Hernando, Guillermo and Turmukhambetov, Daniyar and Civera, Javier and Mac Aodha, Oisin and Brostow, Gabriel J. and Watson, Jamie},
  booktitle={CVPR},
  year={2025}
}
```

© This webpage was in part inspired from this [template](https://github.com/monniert/project-webpage).
