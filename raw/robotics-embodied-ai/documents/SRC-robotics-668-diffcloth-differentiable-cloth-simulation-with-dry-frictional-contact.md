---
source_id: "SRC-robotics-668"
title: "DiffCloth Differentiable Cloth Simulation with Dry Frictional Contact"
source_type: "paper"
publisher: "Li et al."
source_date: "待验证"
url: "https://people.csail.mit.edu/liyifei/publication/diffcloth/"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:35:43+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-668
---
# DiffCloth Differentiable Cloth Simulation with Dry Frictional Contact

### Abstract

Cloth simulation has wide applications in computer animation, garment design, and robot-assisted dressing. This work presents a differentiable cloth simulator whose additional gradient information facilitates cloth-related applications. Our differentiable simulator extends a state-of-the-art cloth simulator based on Projective Dynamics (PD) and with dry frictional contact. We draw inspiration from previous work to propose a fast and novel method for deriving gradients in PD-based cloth simulation with dry frictional contact. Furthermore, we conduct a comprehensive analysis and evaluation of the usefulness of gradients in contact-rich cloth simulation. Finally, we demonstrate the efficacy of our simulator in a number of downstream applications, including system identification, trajectory optimization for assisted dressing, closed-loop control, inverse design, and real-to-sim transfer. We observe a substantial speedup obtained from using our gradient information in solving most of these applications.

### Keywords

diffcloth, projective dynamics, jacobi solver, cloth simulation, differentiable simulation, physics simulation, inverse problems

### Code 💻

Follow our Github repository [Diffcloth](https://github.com/omegaiota/DiffCloth)<iframe src="https://ghbtns.com/github-btn.html?user=omegaiota&amp;repo=DiffCloth&amp;type=star&amp;count=true&amp;size=large" frameborder="0" width="170" height="30" title="GitHub"></iframe>

[![omegaiota/diffcloth - GitHub](https://gh-card.dev/repos/omegaiota/diffcloth.svg?fullname=)](https://github.com/omegaiota/diffcloth)

### Demos

For details refer to the paper Sec 6. Applications.

#### Hat: Trajectory Optimization

Optimize manipulator end effector trajectories to move the hat onto the head.  
1737 Dof, h=1/100s, 400 Timesteps, 18 Design Parameters

![](https://people.csail.mit.edu/liyifei/publication/diffcloth/hat.gif#paper_image)

#### Sock: Trajectory Optimization

Optimize manipulator end effector trajectories to put on the sock.  
3165 Dof, h=1/160s, 400 Timesteps, 36 Design Parameters

![](https://people.csail.mit.edu/liyifei/publication/diffcloth/sock.gif#paper_image)

#### Hat-Controller: Closed-Loop Control

We train a *generalizable* closed-loop controller that can put on the hat from different initial positions.  
1737 Dof, h=1/100s, 400 Timesteps, 117126 Design Parameters

![](https://people.csail.mit.edu/liyifei/publication/diffcloth/hatcontroller.gif#paper_image)

#### Dress: Inverse Design

Optimize dress material parameters so that the spinning angle of the dress is 50 degrees.  
10902 Dof, h=1/120s, 125 Timesteps, 2 Design Parameters

![](https://people.csail.mit.edu/liyifei/publication/diffcloth/dress.gif#paper_image)

#### Sphere: System Identification

Optimize the fricitonal coefficient between the sphere and the cloth to match target trajectory.  
1875 Dof, h=1/180s, 350 Timesteps, 1 Design Parameters

![](https://people.csail.mit.edu/liyifei/publication/diffcloth/sphere.gif#paper_image)

#### T-shirt: System Identification

Optimize wind model and cloth material parameters to match target trajectory.  
4278 Dof, h=1/90s, 250 Timesteps, 6 Design Parameters

![](https://people.csail.mit.edu/liyifei/publication/diffcloth/tshirt.gif#paper_image)

### Demo

![](https://www.youtube.com/watch?v=WWmWuhJcPYY)

### Presentation

![](https://www.youtube.com/watch?v=GH8jLG7UIYQ)

### Citation

```
@article{li2022diffcloth,
    author = {Li, Yifei and Du, Tao and Wu, Kui and Xu, Jie and Matusik, Wojciech},
    title = {DiffCloth: Differentiable Cloth Simulation with Dry Frictional Contact},
    year = {2022},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    issn = {0730-0301},
    url = {https://doi.org/10.1145/3527660},
    doi = {10.1145/3527660},
    abstract = {Cloth simulation has wide applications in computer animation, garment design, and robot-assisted dressing. This work presents a differentiable cloth simulator whose additional gradient information facilitates cloth-related applications. Our differentiable simulator extends a state-of-the-art cloth simulator based on Projective Dynamics (PD) and with dry frictional contact&nbsp;[Ly et&nbsp;al. 2020]},
    note = {Just Accepted},
    journal = {ACM Trans. Graph.},
    month = {mar},
    keywords = {cloth simulation, differentiable simulation, Projective Dynamics}
}
```

### Acknowledgement

We thank Marco Renedo for his helpful discussions on the preconditioners, Junbang Liang for his help with running the baseline comparison code, and the anonymous reviewers for their helpful comments. This work was supported in part by the Defense Advanced Research Projects Agency (DARPA) under grant No. FA8750-20-C-0075.

### Related

- [DiffAvatar: Simulation-Ready Garment Optimization with Differentiable Simulation](https://people.csail.mit.edu/liyifei/publication/diffavatar/)
- [Fluidic Topology Optimization with an Anisotropic Mixture Model](https://people.csail.mit.edu/liyifei/publication/anisotropicstokes/)
- [NeuralFluid: Nueral Fluidic System Design and Control with Differentiable Simulation](https://people.csail.mit.edu/liyifei/publication/neuralfluid/)
- [A Method for Automatically Animating Children’s Drawings of the Human Figure](https://people.csail.mit.edu/liyifei/publication/animateddrawings/)
- [JoinABLe: Learning Bottom-up Assembly of Parametric CAD Joints](https://people.csail.mit.edu/liyifei/publication/joinable-learning-bottom-up-assembly-of-parametric-cad-joints/)
