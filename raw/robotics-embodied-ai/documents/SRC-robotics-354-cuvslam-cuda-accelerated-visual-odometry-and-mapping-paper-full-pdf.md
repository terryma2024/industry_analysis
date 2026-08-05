---
source_id: "SRC-robotics-354"
title: "cuVSLAM CUDA accelerated visual odometry and mapping paper full PDF"
source_type: "research_paper"
publisher: "NVIDIA"
source_date: "2025-07-08"
url: "https://arxiv.org/pdf/2506.04359.pdf"
evidence_grade: "S"
capture_method: "pdf-extract-pdftotext"
captured_at: "2026-08-05T06:50:30+00:00"
pdf_file: "raw/robotics-embodied-ai/documents/SRC-robotics-354-cuvslam-cuda-accelerated-visual-odometry-and-mapping-paper-full-pdf.pdf"
page_count: "23"
tags:
  - raw/source
  - raw/pdf
  - source-type/research-paper
  - evidence/s
aliases:
  - SRC-robotics-354
---
# cuVSLAM CUDA accelerated visual odometry and mapping paper full PDF

## Page 1

2025-7-9



                                        cuVSLAM: CUDA accelerated visual odometry and
                                        mapping
                                        Alexander Korovko1 , Dmitry Slepichev1 , Alexander Efitorov1 , Aigul Dzhumamuratova1 , Viktor Kuznetsov1 ,
                                        Joydeep Biswas1 , Hesam Rabeti1 and Soha Pouya1
                                        1 NVIDIA , {akorovko,   dslepichev, aefitorov, adzhumamurat, vkuznetsov, jbiswas, hrabeti, spouya}@nvidia.com




                                        Abstract
                                        Accurate and robust pose estimation is a key requirement for any autonomous robot. We present
                                        cuVSLAM, a state-of-the-art solution for visual simultaneous localization and mapping, which can




arXiv:2506.04359v3 [cs.RO] 8 Jul 2025
                                        operate with a variety of visual-inertial sensor suites, including multiple RGB and depth cameras,
                                        and inertial measurement units. cuVSLAM supports operation with as few as one RGB camera to as
                                        many as 32 cameras, in arbitrary geometric configurations, thus supporting a wide range of robotic
                                        setups. cuVSLAM is specifically optimized using CUDA to deploy in real-time applications with minimal
                                        computational overhead on edge-computing devices such as the NVIDIA Jetson. We present the design
                                        and implementation of cuVSLAM, example use cases, and empirical results on several state-of-the-art
                                        benchmarks demonstrating the best-in-class performance of cuVSLAM.


                                         Acknowledgements
                                        We would like to extend our heartfelt acknowledgment to Eugene Vendrovskiy, Stanislav Volodarskiy, and
                                        Dmitry Robustov for their invaluable contributions to this project. Their profound expertise, exceptional skills,
                                        and commitment to excellence have been pivotal in shaping the outcomes of this work.

                                        1. Introduction
                                        Visual Simultaneous Localization and Mapping (VSLAM) is a fundamental capability for autonomous robots,
                                        enabling them to build a metric map of their environment while simultaneously determining their location
                                        within it. The increasing deployment of autonomous robots across diverse applications, from warehouse
                                        automation to last-mile delivery, has created a pressing need for robust, real-time VSLAM solutions that can
                                        operate efficiently across diverse settings, while being able to run on energy-efficient edge computing devices.

                                        Traditional VSLAM systems face several key challenges: they often struggle with real-time performance on
                                        resource-constrained platforms, have limited flexibility in sensor configurations, and may not fully utilize
                                        available hardware acceleration capabilities. Additionally, many existing solutions are optimized for specific
                                        sensor configurations, making them less adaptable to diverse robotic platforms with varying sensor requirements.

                                        We evaluate cuVSLAM on standard benchmarks, demonstrating state-of-the-art accuracy while maintaining real-
                                        time performance on edge computing platforms. Our results show that cuVSLAM achieves average trajectory
                                        errors below 1% on the KITTI odometry benchmark and position errors under 5cm on the EuRoC dataset,
                                        while processing frames in real-time on NVIDIA Jetson platforms. Multi-Stereo mode significantly improves
                                        accuracy and robustness on challenging sequences compared to single stereo cameras, as validated through
                                        both simulated and real-world dataset evaluations.

                                        We present cuVSLAM, a CUDA-accelerated visual SLAM system designed to address these challenges. cuVSLAM
                                        offers several key innovations:

                                           • Flexible sensor suite support, accommodating configurations from a single RGB camera to complex arrays
                                             of up to 32 cameras with arbitrary geometric arrangements


                                         © 2025 NVIDIA. All rights reserved.

## Page 2

cuVSLAM: CUDA accelerated visual odometry and mapping



   • Support for optional IMU and depth sensors
   • Efficient CUDA implementation enabling real-time performance on edge devices like NVIDIA Jetson
   • A modular architecture separating frontend pose estimation from backend map refinement
   • Robust feature tracking and mapping capabilities that maintain accuracy across diverse environments

Our technical approach combines classical SLAM techniques with modern GPU acceleration. The frontend
module performs real-time pose estimation using feature detection, tracking, and local mapping, while the
backend handles global map consistency through pose graph optimization and loop closure. By leveraging
CUDA acceleration throughout the pipeline, from feature detection to bundle adjustment, cuVSLAM achieves
superior performance while maintaining high accuracy.

The rest of this technical report is organized as follows: Section 2 describes the system architecture and design,
Section 3 presents experimental results and benchmarks, and Section 4 concludes with discussion and future
work.


2. System Architecture and Design




                                        Figure 1: cuVSLAM architecture

The cuVSLAM library implements a general approach to camera pose estimation, where the architecture
consists of two major blocks: the frontend, responsible for online pose estimation with minimal latency and
maximum throughput, and the backend, focusing on asynchronous and potentially resource-demanding map
refinement, loop closing, and pose graph optimization.

The design of the frontend pipeline prioritizes local pose estimation accuracy over global consistency, focusing
on delivering smooth trajectories without the bumps introduced by loop closure mechanisms or PGO (Pose
Graph Optimization). To achieve this, it maintains a local odometry map consisting of the last 𝑁 6DOF camera
poses (at keyframes) along with visible 3D landmarks and their observations. Besides the map, the frontend
consists of the 2D module, responsible for feature selection, 2D feature tracking, and keyframe selection, and
the 3D module, which performs pose estimation based on the local map, 2D information, and other data sources
(e.g., IMU or depth measurements).

In contrast to the frontend, cuVSLAM backend focuses on global map and pose consistency. It processes frontend
outputs and builds a globally consistent map that integrates camera poses, 2D observations, 3D landmarks,
pose deltas, and visual features. The backend maintains global consistency in the map through asynchronous
refinement using pose graph optimization and loop closing.

2.1. 2D module
cuVSLAM implements a set of algorithms operating on the 2D level, which include keypoint selection and
feature extraction, keypoint tracking, and keyframe selection.



                                                                                                                2

## Page 3

cuVSLAM: CUDA accelerated visual odometry and mapping




           Figure 2: 2D module implements keyframe selection, feature selection and 2D tracking.


The pipeline begins with keypoint selection, which is designed to identify high-contrast features and ensure
an approximately uniform distribution of keypoints across the image. The image is first divided into non-
overlapping patches, forming an 𝑁 × 𝑀 grid. In each patch, the algorithm selects the top 𝑘 keypoints based
on the "Good Features to Track" measure (Shi and Tomasi (1993)), where 𝑘 is calculated such that the total
number of keypoints across the entire image exceeds a predefined threshold, 𝐾𝐼 .

                                                          ⌊︂          ⌋︂
                                                                𝐾𝐼
                                                     𝑘>                                                          (1)
                                                               𝑁 *𝑀

For 2D tracking, cuVSLAM implements a modified version of the Lucas-Kanade algorithm (Lucas and Kanade
(1981), Bouguet (2000)) for feature tracking that: 1) performs tracking in a coarse-to-fine manner, continuously
refining track positions at each image pyramid level, and 2) performs a normalized cross-correlation (NCC)
check at each optimization step for each keypoint to filter out unreliable tracks.

If the number of successfully tracked keypoints falls below a threshold, the 2D module creates a new keyframe,
which triggers local and global map updates and asynchronous refinement. In stereo and multicamera modes,
cuVSLAM launches cross-camera feature tracking to obtain multi-view observations for subsequent landmark
triangulation.

2.2. 3D module
When a keyframe is created, the 3D module collects multi-view observations from the 2D module and performs
landmark triangulation. The created landmarks, along with their observations, are saved in the local map.
After pose estimation, an asynchronous local sparse bundle adjustment (SBA) is initiated for refinement. Given
the poses 𝑇𝑖 , landmarks 𝑝𝑗 , and 2D observations 𝑜𝑖𝑗 , SBA solves the following optimization task:

                                           𝑟𝑒𝑝𝑟
                                          𝑟𝑖𝑗𝑘  = 𝜋(𝑇𝑘𝑐𝑏 𝑇𝑖𝑏𝑤 𝑝𝑤
                                                               𝑗 ) − 𝑜𝑗,𝑘                                        (2)


                                                      ∑︁        ∑︁         ∑︁
                  𝑇ˆ1:𝑁
                    𝑏𝑤
                        , 𝑝ˆ𝑤
                            1:𝑀 = arg𝑇1:𝑁
                                      𝑏𝑤 ,𝑝𝑤
                                           1:𝑀
                                               min                               ||𝜋(𝑇𝑘𝑐𝑏 𝑇𝑖𝑏𝑤 𝑝𝑤            2
                                                                                                𝑗 ) − 𝑜𝑗,𝑘 ||Σ   (3)
                                                     𝑖∈[1,𝑁 ] 𝑗∈[1,𝑀 ] 𝑘∈[1,𝐶]

where 𝑟𝑟𝑒𝑝𝑟 represents reprojection error, 𝑇𝑘𝑐𝑏 refers to the k-th camera-from-base transformation, 𝑇𝑖𝑏𝑤 denotes
the base-from-world transformation, 𝑝𝑤 is the 3D landmark in the world frame, and 𝑜𝑗,𝑘 represents the
observation of landmark 𝑗 by the k-th camera.

Following the common approach, we use the Schur complement to solve for poses 𝑇𝑖 first and solve for points 𝑝𝑗
afterward. To enhance the efficiency of SBA further, we implement it in CUDA, which is particularly useful for
edge devices and/or in multicamera setups. cuVSLAM supports mono, stereo, multicamera, and visual-inertial
modes, each of which corresponds to a dedicated 3D solver.




                                                                                                                  3

## Page 4

cuVSLAM: CUDA accelerated visual odometry and mapping



2.2.1. Stereo
Stereo mode is the default mode in cuVSLAM. It utilizes PnP algorithm for pose estimation, that relies on 𝑜𝑗 ,
2D observation, and 𝑝𝑖 , 3D landmarks, acquired from the local map.
                                                          ∑︁      ∑︁          𝑟𝑒𝑝𝑟 2
                                   𝑇ˆ𝑏𝑤 = arg𝑇 𝑏𝑤 min                      ||𝑟𝑗𝑘  ||Σ                         (4)
                                                        𝑗∈[1,𝑀 ] 𝑘∈[1,2]



On regular frames, we perform tracking only for the left camera for the tracks that are still active. We query
the local map for the corresponding 3D landmarks and use them for pose estimation. When the number of
successfully tracked keypoints falls below a threshold, a keyframe is created. After feature selection, we perform
cross-camera (left-to-right) tracking to obtain landmark stereo observations and conduct point triangulation.
Finally, we add the current camera pose, along with the created landmarks and their observations, into the
local map and launch asynchronous SBA for refinement.

2.2.2. Multi-Stereo
When a robot operates in environments where it is likely to face a featureless surface from one direction, e.g.,
narrow corridors or elevators, it becomes vital to use multiple cameras for pose estimation.

cuVSLAM extends the approach introduced in 2.2.1 to a multicamera setup by treating an arbitrary multiple-
camera configuration as a number of stereo pairs.

At startup, we build a Frustum Intersection Graph (FIG)—a directed graph (𝑉, 𝐸), where vertices 𝑉 represent a
set of optical sensors, and edges 𝐸 connect cameras that share a common field of view. Edge direction describes
the cross-camera tracking between adjacent cameras, i.e., if 𝑒𝑖𝑗 exists, cuVSLAM performs 2D tracking from
camera 𝑐𝑖 to 𝑐𝑗 .

The FIG is built automatically at cuVSLAM startup. Provided with a list of camera extrinsics/intrinsics, cuVSLAM
iterates over each pair of cameras and creates a new edge in the graph when cameras have overlapping fields
of view (FoV). To detect this, cuVSLAM places a virtual plane in front of the first camera. It selects uniformly
distributed pixels in the image 𝐼1 , lifts them onto the plane, and backprojects them to the image 𝐼2 . When the
ratio of successfully projected points to the total number of sampled points exceeds a threshold, cuVSLAM
detects the shared FoV and creates an edge.




Figure 3: Randomly selected pixels on left picture are lifted on a virtual plane in front of the camera. Pixels
               that can be successfully projected onto second images are shown in green.

Cameras that correspond to the source of some edge are used for feature tracking/selection over time on each
incoming frame. A keyframe is still treated as a global event, while feature selection happens independently


                                                                                                                4

## Page 5

cuVSLAM: CUDA accelerated visual odometry and mapping



for each camera.

Let 𝑆𝑐𝑢𝑟𝑟 be a set of all currently observed points from all the cameras and 𝑆𝑘𝑓 is the set of points observed in
the previous keyframe. Then if:

                                                  |𝑆𝑐𝑢𝑟𝑟 ∩ 𝑆𝑘𝑓 |
                                                                 < 𝑇;                                             (5)
                                                      |𝑆𝑘𝑓 |
a keyframe is created and cross-camera tracking is done. Similar to stereo mode we then perform landmark
triangulation and refine the map with SBA.

After 2D tracking both on regular frames and keyframes, we collect all the available observations along with
the corresponding 3D landmarks for pose estimation.

                                                            ∑︁      ∑︁          𝑟𝑒𝑝𝑟 2
                                     𝑇ˆ𝑏𝑤 = arg𝑇 𝑏𝑤 min                      ||𝑟𝑗𝑘  ||Σ                           (6)
                                                          𝑗∈[1,𝑀 ] 𝑘∈[1,𝐶]


where 𝑟𝑟𝑒𝑝𝑟 denotes a reprojection error for j-th landmark observed from k-th camera in the rig Barfoot (2017).

Since observations from multiple cameras contribute to pose estimation, cuVSLAM requires images to be syn-
chronized. This is a minor restriction, as many modern cameras provide hardware synchronization capabilities,
such as Intel RealSense Grunnet-Jepsen et al. (2018).

2.2.3. Visual-Inertial




                                      Figure 4: Factor graphs for VIO pipeline.

Visual-Inertial (VI) mode is inspired by Forster et al. (2017) and Campos et al. (2021). Following their approach
cuVSLAM defines robot‘s state as a combination of 6 DoF pose, linear velocity, accelerometer and gyroscope
biases forming a 15 DoF state vector 𝑆 = [𝑇 ∈ 𝑆𝐸(3), 𝑣 ∈ R3 , 𝑏𝑎 ∈ R3 , 𝑏𝑤 ∈ R3 ]. Robot states along with IMU
(𝑟𝑖𝑚𝑢 ) and visual (𝑟𝑟𝑒𝑝𝑟 ) factors are used to build a factor-graph for a list of crucial subproblems, which are:

   • Purely visual pose estimation is used for the initialization of VI pipeline. It consists of the PnP and
     the asynchronous SBA as it was described in section 2.2.1 and needed to build a pose history for the
     subsequent gravity estimation.
   • Gravity estimation. Gravity is a key parameter needed for the IMU preintegration and IMU-aided pose
     estimation. Assuming the poses predicted by the visual-only part are fixed, the algorithm estimates
     velocities 𝑣𝑖 , accelerometer and gyroscope biases 𝑏𝑎 , 𝑏𝑤 and a rotation matrix 𝑅𝑔 , s.t. 𝑔 = 𝑅𝑔 [0, 0, 9.81]𝑇 .
                                                     [︃             𝑘−1
                                                                                                    ]︃
                                                         2
                                                                    ∑︁                      ⃦2
                              𝑔
                                                                                                                  (7)
                                                                          ⃦ 𝑖𝑚𝑢
                            𝑅 , b, 𝑣0:𝑘 = 𝑎𝑟𝑔𝑚𝑖𝑛      ‖𝑏‖Σ𝑝𝑟𝑖𝑜𝑟 +         ⃦𝑟    (𝑆𝑖 , 𝑆𝑖+1 )⃦Σ
                                                                                             𝐼𝑀 𝑈
                                                                    𝑖=0




                                                                                                                    5

## Page 6

cuVSLAM: CUDA accelerated visual odometry and mapping



   • Visual-inertial pose estimation is used every frame. It constrains two consecutive robot states 𝑆𝑖−1 and 𝑆𝑖
     with IMU and visual factors. In addition 𝑆𝑖−1 is also constrained by the prior factor.
                                 ⎡                                                                                ⎤
                                                                    1
                                                    ⃦2             ∑︁                   2                      2
              𝑆𝑖−1 , 𝑆𝑖 = 𝑎𝑟𝑔𝑚𝑖𝑛 ⎣⃦𝑟𝑖𝑚𝑢 (𝑆𝑖−1 , 𝑆𝑖 )⃦Σ                   ‖𝑟𝑟𝑒𝑝𝑟 (𝑆𝑖−𝑗 )‖Σ𝑣𝑖𝑠 + ⃦𝑟𝑝𝑟𝑖𝑜𝑟 (𝑆𝑖−1 )⃦Σ𝑝 ⎦      (8)
                                  ⃦                                                            ⃦              ⃦
                                                               +
                                                        𝐼𝑀 𝑈
                                                                   𝑗=0


   • Visual-inertial sparse bundle adjustment is used for local map refinement when IMU data along with gravity
     and bias estimations are available. Following prior works, we perform relinearization of the IMU factors
     based on the variable update norm or once per number of iterations.
                                        [︃ 𝑘                                         𝑘
                                                                                                                   ]︃
                                             ⃦𝑟𝑖𝑚𝑢 (𝑆𝑖−1 , 𝑆𝑖 )⃦2
                                          ∑︁ ⃦                                      ∑︁                      2
                                                                                               𝑟𝑒𝑝𝑟
                                                                                                                         (9)
                                                               ⃦
                          𝑆0:𝑘 = 𝑎𝑟𝑔𝑚𝑖𝑛                         Σ
                                                                                +         ‖𝑟          (𝑆𝑖 )‖Σ𝑣𝑖𝑠
                                                                         𝐼𝑀 𝑈
                                            𝑖=1                                     𝑖=0


2.2.4. Mono-Depth




                                          Figure 5: RGBD factor graph.

cuVSLAM supports mono RGBD-based dense frame-to-frame pose estimation. Following Kerl et al. (2013) it
considers two consecutive intensity images 𝐼1,2 along with pixel-aligned depth images 𝑍1,2 and estimates a
relative 6 DoF transformation between corresponding frames.

It defines a list of factors, that constrain frame positions w.r.t each other:

   • Visual factor used to constrain poses w.r.t the local map by means of reprojection error 𝑟𝑟𝑒𝑝𝑟 described
     earlier.
   • Dense intensity and depth factors define constraints for each pixel location 𝑥, introducing the following
     error functions:                             [︃                        ]︃
                                                     𝐼2 (𝜏 (𝑇21 , 𝑥)) − 𝐼 1
                                            𝑟𝐼 =             −1                                           (10)
                                                    𝐼1 (𝜏 (𝑇21   , 𝑥)) − 𝐼2
                                       [︃                                            ]︃
                                          𝑍2 (𝜏 (𝑇21 , 𝑥)) − [𝑇21 𝜋 −1 (𝑥, 𝑍1 (𝑥))]𝑧
                                   𝑍
                                  𝑟 =             −1              −1 −1                                   (11)
                                         𝑍1 (𝜏 (𝑇21  , 𝑥)) − [𝑇21    𝜋 (𝑥, 𝑍2 (𝑥))]𝑧

     where 𝑇21 is the relative pose; 𝜏 (𝑇, 𝑥) is a warping function, that lifts the pixel location 𝑥 to 3D, applies
     transformation 𝑇 and projects the point back to image plane; [.]𝑧 returns Z coordinate of a point.
   • Point-to-point factor. Provided with the 2D-2D matches (𝑥, 𝑦)1:𝑁 obtained in 2D module, we define the
     point-to-point error:

                                        𝑟𝑝 = 𝜋 −1 (𝑦, 𝑍2 (𝑦)) − 𝑇21 𝜋 −1 (𝑥, 𝑍1 (𝑥))                                    (12)

All together these factors form the combined optimization problem, which we solve using a Levenberg-Marquardt




                                                                                                                          6

## Page 7

cuVSLAM: CUDA accelerated visual odometry and mapping



solver implemented on GPU:
                        ∑︁                            ∑︁                                           ∑︁
   𝑇ˆ21 = arg𝑇21 min(           ||𝑟𝑟𝑒𝑝𝑟 (𝑝)||2Σ +           (||𝑟𝐼 (𝑥)||2 + ||𝑟𝑍 (𝑥)||2𝜎𝑧 ) +                   ||𝑟𝑝 (𝑥, 𝑦)||2 )   (13)
                    𝑝∈𝑃 𝑜𝑖𝑛𝑡𝑠                       𝑥∈𝑃 𝑖𝑥𝑒𝑙𝑠                                  (𝑥,𝑦)∈𝑇 𝑟𝑎𝑐𝑘𝑠



2.2.5. Mono
Mono camera mode shares the same common approach as 2D feature tracking, with subsequent point triangu-
lation and pose estimation. A key difference is that triangulation is performed using observations obtained
from different camera poses, which we estimate using the same PnP algorithm as described in 2.2.1, given the
current observations of previously obtained landmarks.

For the first frame pair, when no 3D landmarks are available, cuVSLAM estimates the relative transformation
through the fundamental matrix. Specifically, given a set of 2D tracks (𝑥, 𝑦)1:𝑁 , we estimate the fundamental
matrix 𝐹 using RANSAC. With the calibration matrix 𝐾, we then retrieve the up-to-scale relative pose.

The relative pose is subsequently used to triangulate the first set of landmarks and update the local map,
followed by asynchronous SBA refinement.

2.3. Loop closing and global map refinement




                                      Figure 6: Factor graphs for VIO pipeline.

cuVSLAM loop closing and global map refinement module helps limit global drift by enforcing global consistency
of the map. It consists of 6 DoF keyframe poses, landmarks and their observations, pose deltas, and sparse
image features. Pose deltas are obtained through the integration of intra-keyframe frontend pose predictions.
For image features, we use a list of 9 × 9 image patches taken from each level of the image pyramid.

We perform the following steps to detect loop closures and refine the map to enforce global consistency:

   • Integrate latest data. When a new keyframe is created, cuVSLAM extracts visual features, integrates
     intra-keyframe pose predictions, collects currently visible landmarks along with their observations and
     updates the global map using an asynchronous data queue.
   • Query nearest neighbors. After the map update, cuVSLAM performs a pose search of robot poses within
     a sphere of fixed radius. We use a kd-tree for fast and efficient spatial search.
   • Landmark selection. After collecting all the landmarks related to the found poses, we: 1) filter them by
     geometric visibility, 2) track landmark visual features onto the currently observed image, and 3) filter
     out landmarks with unsuccessful tracking. Finally, when landmarks from multiple poses are observed,
     we split the landmarks into sets with respect to connected poses and pick the largest set.
   • Relative pose estimation. At this step, we estimate a pose delta 𝐷 between the pose from the map and
     the current robot’s position. Let 𝑇 𝑚𝑤 denote a pose in the map, connecting the world and map frames.


                                                                                                                                    7

## Page 8

cuVSLAM: CUDA accelerated visual odometry and mapping



     Then, after shifting landmarks into the map frame, we solve for the relative pose estimate:
                                                 ∑︁       ∑︁
                           𝑇ˆ𝑏𝑚 = arg𝑇 𝑏𝑚 min                      ||𝜋(𝑇𝑘𝑐𝑏 𝑇 𝑏𝑚 𝑇 𝑚𝑤 𝑝𝑤            2
                                                                                       𝑗 ) − 𝑜𝑗,𝑘 ||Σ     (14)
                                                𝑗∈[1,𝑀 ] 𝑘∈[1,𝐶]


   • Pose graph optimization. Provided with the pose deltas between poses either by the frontend or the
     loop closure mechanism, cuVSLAM refines the map by minimizing the following sum across pose graph
     edges 𝐸:                                      ∑︁
                                                               −1 −1
                                𝑇1:𝑁 = arg𝑇1:𝑁 min     ||𝐿𝑜𝑔(𝐷𝑖𝑗 𝑇𝑖 𝑇𝑗 )||2                        (15)
                                                          𝑖,𝑗∈𝐸



3. Experiments
This section demonstrates the capabilities of the cuVSLAM library in robotics applications across diverse real-
world environments and camera configurations. We also compare our solution with established classical and
deep learning libraries that provide camera pose estimation for long-distance trajectories.

3.1. System Performance and Hardware Utilization
We evaluated cuVSLAM performance through two complementary approaches: real-time execution on em-
bedded hardware to measure resource utilization and single-frame processing time, and offline processing of
warehouse environment recordings on workstation hardware. The test scenarios involved processing feature-
rich images captured from either a wheeled robot navigating a warehouse environment or handheld camera
movements. To ensure accurate measurements, all experiments were conducted on systems dedicated solely to
cuVSLAM execution, without concurrent resource-intensive operations such as visualization, complex image
processing, or data recording that could potentially skew the results.

Table 1 summarizes the key performance metrics, with comprehensive results provided in Appendix A.2.
The left portion of Table 1 presents execution times for cuVSLAM visual tracking function, excluding image
acquisition and post-processing overhead. These measurements were obtained using recorded color images at
768×480 resolution (with the exception of mono-depth mode at 640×480 resolution) on two distinct hardware
configurations: a desktop workstation featuring an Intel i7-14700 CPU with NVIDIA RTX 4090 GPU, and an
embedded Jetson Orin AGX 64GB single-board computer operating in MAXN power mode.

Table 1: cuVSLAM Performance Evaluation. Left: Per-call processing times measured on RTX 4090 (Desktop)
and Jetson AGX Orin (64 GB) using datasets with image resolution 768×480 (except mono-depth mode at
640×480). Right: CPU and GPU utilization on Jetson AGX Orin during live operation with RealSense cameras
at 640×480 resolution and 60 FPS (except stereo-inertial mode at 30 FPS).

                                                 Track call time, ms          Jetson HW utilization
                     Configuration
                                                 Desktop      Jetson          CPU %     GPU %
                     Mono                          0.9          2.7             NA         NA
                     Mono-Depth                    5.9         15.1             2.6       55.0
                 .   Stereo-Inertial               1.3          3.8             1.3        2.2
                     Stereo                        0.4          1.8             5.5        1.7
                     Multicamera (2-stereo)        0.8          2.0             8.3        9.0
                     Multicamera (3-stereo)        1.4          2.3             8.3       11.0
                     Multicamera (4-stereo)        2.1          NA              NA         NA

The right portion of Table 1 details CPU and GPU utilization percentages for cuVSLAM visual odometry executed
through ISAAC ROS 3.2 with RealSense D435/D455 stereo cameras. All live tests utilized cameras configured
at 640×480 resolution and 60 FPS, except for Stereo-Inertial mode, which ran at 30 FPS with IMU data at
200 Hz. The reduced framerate was necessary to ensure valid IMU-based integration, providing 6-7 IMU
measurements between each stereo image pair. To accurately isolate cuVSLAM hardware requirements, we


                                                                                                             8

## Page 9

cuVSLAM: CUDA accelerated visual odometry and mapping



employed a controlled experimental methodology: we first established baseline system utilization with the
RealSense camera in motion but without cuVSLAM processing, then repeated the similar camera movement
pattern with cuVSLAM visual tracking active. Resource utilization metrics were sampled at 15 ms intervals for
equal durations in both experiments. The net resource consumption attributable to cuVSLAM was calculated by
subtracting baseline measurements from total utilization values and averaging the results. This methodology
provides an accurate assessment of the computational overhead introduced by the library. Additional details on
evaluation and an exploration of hardware utilization across different resolutions and modes on Jetson devices
are provided in Appendix A.2.

3.2. Benchmarking
We evaluated cuVSLAM different operation modes using several publicly available datasets. The Mono-Depth
mode was validated on the AR-table Chen et al. (2023), ICL-NUIM Handa et al. (2014) and TUM RGB-D Sturm
et al. (2012) datasets. The Stereo mode was tested on the EuRoC Burri et al. (2016) and KITTI Geiger
et al. (2013) datasets. The Stereo-Inertial mode was assessed using the EuRoC Burri et al. (2016) and TUM-
VI Schubert et al. (2018) datasets. The Multi-Stereo mode was evaluated on simulated TartanAir V2 Wang
et al. (2023) and TartanGround Patel et al. (2025) datasets and our proprietary R2B real-world dataset.

Table 2: Evaluation results for cuVSLAM Visual Odometry and SLAM across various operating modes

       Mode              Dataset             Method                avgRTE, %      avgRE, deg   RMSE APE
                                             ORBSLAM3                   -              -           -
                                             DPVO                     4.42           1.65        0.77
                         AR table
                                             cuVSLAM Odom             0.34           3.59        0.09
                                             cuVSLAM SLAM             0.19           1.68       0.025
                                             ORBSLAM3                   -              -           -
                                             DPVO                    10.28           0.77        0.61
       Mono-Depth        ICL-Nuim
                                             cuVSLAM Odom             0.41           0.99       0.026
                                             cuVSLAM SLAM             0.44           0.97       0.026
                                             ORBSLAM3                 0.50           2.98        0.067
                                             DPVO                    13.56           1.98        0.80
                         TUM RGB-D
                                             cuVSLAM Odom             1.35           5.52        0.11
                                             cuVSLAM SLAM             0.99           4.13       0.065
                                             ORBSLAM3                 0.21           1.41        0.068
                                             DPVO                     0.21           0.96        0.10
                         EuroC*
                                             cuVSLAM Odom             0.29           1.96        0.13
                                             cuVSLAM SLAM             0.17           1.12       0.054
       Stereo
                                             ORBSLAM3                 0.31           1.20        2.98
                                             DPVO                    21.69           1.14       195.05
                         Kitti
                                             cuVSLAM Odom             0.33           1.14        3.00
                                             cuVSLAM SLAM             0.27           0.93        1.98
                                             ORBSLAM3                 5.70          72.23       0.066
                                             DPVO                       -              -           -
                         EuroC
                                             cuVSLAM Odom             0.39           2.69        0.19
                                             cuVSLAM SLAM             0.29           2.27        0.13
       Stereo-Inertial
                                             ORBSLAM3                 2.17           1.37       0.077
                                             DPVO                       -              -           -
                         TUM-VI Room
                                             cuVSLAM Odom             0.20           3.85        0.18
                                             cuVSLAM SLAM             0.12           3.00        0.12

To quantify visual tracking accuracy, we employed standard metrics: Average Relative Translation (avgRTE) and
Rotation (avgRE) Errors Geiger et al. (2013), and Absolute Pose Error (RMSE APE) with trajectory alignment
and scale correction Sturm et al. (2012) using the EVO library Grupp (2017).

Table 2 presents comprehensive benchmarking results across popular datasets from various domains. For


                                                                                                            9

## Page 10

cuVSLAM: CUDA accelerated visual odometry and mapping



comparative analysis, we include performance metrics for the classical computer vision-based ORB-SLAM3
and the deep learning-based DPVO alongside cuVSLAM. Each library was configured according to the dataset
characteristics: ORB-SLAM3 and cuVSLAM operated in their corresponding specialized modes (monocular-
depth, stereo, or stereo-inertial), while DPVO consistently used monocular mode across all evaluations, utilizing
the front-left camera for stereo datasets. Since scale corrections were applied to final trajectories rather than
successive pose estimations, translation results may not be meaningful for some datasets; therefore, relative
rotation error should be considered the primary metric.




 Figure 7: Sample camera views from the R2B dataset captured across diverse environments including large
office spaces, industrial warehouses, and narrow corridors in both office and storage areas. The images show
     simultaneous captures from 4 stereo cameras (displaying only the left image from each stereo pair).

To ensure accurate and representative comparisons, we excluded clearly identified outlier and corrupted
sequences. For instance, the EuRoC V203 sequence was included only in Stereo-Inertial evaluations, and only a
subset of TUM RGB-D sequences were used (see Table 6). For TartanGround datasets, not all sequences provide
the full complement of cameras or are available for download. Additionally, many sequences lack overlapping
trajectories, preventing loop closure detection—a critical component for evaluating SLAM performance versus
odometry. Consequently, we validated SLAM mode on selected subsets of TartanGround (see Table 9) and
TartanAir V2 (see Tables 10 and 11) datasets.

While the new Tartan datasets provide free camera and quadruped robot movements in diverse simulated
environments, rigorous validation of cuVSLAM multi-camera capabilities in real-world scenarios was required.
Therefore, a proprietary Multi-Stereo R2B dataset was collected in office and warehouse environments using
the Nova Carter wheeled robot equipped with four stereo cameras. The example views from the R2B dataset
are shown in Fig. 7. This was our only available option for validating this cuVSLAM mode on real data, as
publicly available real-world multi-camera datasets either lack hardware-synchronized cameras suitable for
stereo pair arrangements Carlevaris-Bianco et al. (2015); Nair et al. (2024) or employ software synchronization
that cannot ensure simultaneous image capture Yin et al. (2021); Zhang (2023).

Table 3 presents cuVSLAM results in Multi-Stereo Mode. Notably, results achieved on the real R2B dataset
closely match those from similar domains in the TartanGround dataset, confirming the validity of both datasets
and results. For TartanAir V2, we performed detailed validation only on the Hard dataset, which presents
greater challenges due to fast six-degrees-of-freedom motion and higher translational and angular velocities.


                                                                                                              10

## Page 11

cuVSLAM: CUDA accelerated visual odometry and mapping


Table 3: Evaluation results for cuVSLAM Multi-Stereo Visual Odometry and SLAM on multi-camera datasets

            Dataset                  Method                avgRTE, %       avgRE, deg   RMSE APE
                                     cuVSLAM Odom             0.18            1.15        0.28
            R2B
                                     cuVSLAM SLAM             0.11            0.70        0.18
                                     cuVSLAM Odom*            0.54            0.95        0.14
            TartanGround             cuVSLAM Odom             0.21            0.48        0.09
                                     cuVSLAM SLAM             0.17            0.37        0.07
                                     cuVSLAM Odom*            2.56           13.97        5.20
            TartanAir V2 (Hard)      cuVSLAM Odom             2.44           13.98        5.24
                                     cuVSLAM SLAM             2.26           12.76        4.99


Results for the Easy mode are comparable to those for TartanGround, with a detailed comparison available in
Table 8. While TartanAir V2 results indicate room for improvement, they also demonstrate the importance
of multi-camera mode for robust tracking in most environments, with some showing 2–4× improvement in
multi-camera SLAM mode.

We anticipate that the recent growth in availability and adoption of synchronized multi-stereo camera systems
from various vendors will encourage the creation of new public multi-camera datasets, facilitating further
development, testing, and implementation of multi-camera SLAM systems in robotic applications.


4. Discussion
We advocate for the wider adoption of multi-camera visual tracking in robotics based on two principal advantages
observed in our experiments: enhanced trajectory reliability in feature-poor environments when operating in
odometry mode, and increased loop closure detection rates in SLAM mode.

4.1. Trajectory Reliability Under Visual Occlusion
Figure 8 demonstrates the system’s trajectory reliability through a practical robustness test. We equipped a
Carter robot with 4 stereo cameras and subjected it to challenging visual conditions during continuous motion.
Cameras were randomly occluded with opaque film for intervals of 20–60 seconds, with the constraint that at
least one stereo pair remained unobstructed at a given moment.




 Figure 8: Occlusion resilience test using the Carter robot. cuVSLAM maintains continuous trajectory despite
random camera occlusions. Numbered rows show instantaneous views from the robot’s 4 stereo cameras (left
                              images only) at corresponding trajectory locations


                                                                                                             11

## Page 12

cuVSLAM: CUDA accelerated visual odometry and mapping



Despite these severe visual constraints, the odometry trajectory maintained stability without exhibiting jumps
or discontinuities, validating the system’s robustness to partial visual obstruction. This capability represents a
significant advancement for visual tracking systems. While single-camera configurations can maintain tracking
in feature-poor environments only briefly—typically relying on IMU or depth sensor fusion—our multi-camera
approach preserves stable and reliable visual tracking over extended periods even with degraded visual input.

4.2. Enhanced Loop Closure Detection
The expanded collective field of view afforded by multiple cameras directly translates to increased loop closure
detection rates. Figure 9 presents a comparative analysis of loop closure events between single-stereo and four-
stereo camera configurations along identical trajectories. The multi-camera setup demonstrates a substantially
higher frequency of successful loop closures, enabling more frequent pose graph optimization. This increased
loop closure rate yields quantitative improvements in localization accuracy. As shown in Table 3, evaluation on
the Multi-Stereo R2B dataset reveals approximately 40% improvement in SLAM accuracy metrics compared to
pure odometry mode, underscoring the practical benefits of the multi-camera approach for robust localization.




Figure 9: Comparison of loop closure detection events between single-camera and multi-camera (four stereo
pairs) SLAM configurations on identical trajectories. The multi-camera setup demonstrates improved mapping
                           consistency due to its wider cumulative field-of-view.


5. Conclusions
This technical report demonstrates the robust real-time performance of the cuVSLAM visual tracking library
across diverse robotic platforms, including automotive vehicles, aerial drones, wheeled robots, and handheld
camera systems. Our comprehensive evaluation encompasses both real-world deployments and synthetic
datasets, validating the system’s capabilities under varied operational conditions.

The cuVSLAM library offers several key advantages that position it as a production-ready solution for modern
robotics applications:

   • Accessibility and Integration: The library is readily available through both ISAAC ROS1 and Python2
     APIs, supporting deployment on both desktop and embedded NVIDIA platforms. This dual-API approach
     ensures flexibility for developers working across different software ecosystems.
  1 https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam
  2 https://github.com/NVlabs/PyCuVSLAM




                                                                                                               12

## Page 13

cuVSLAM: CUDA accelerated visual odometry and mapping



   • Computational Efficiency: The system maintains low computational overhead while delivering high-
     accuracy localization, enabling seamless integration into complex robotic stacks such as NVIDIA Isaac
     Perceptor3 , which incorporates NVBLOX Millane et al. (2024) for 3D reconstruction and Nav2 Macenski
     et al. (2020) for autonomous navigation.
   • Minimal Configuration Overhead: Unlike many SLAM systems that require extensive parameter tuning
     for different scenarios, cuVSLAM provides robust out-of-the-box performance across diverse environments
     and sensor configurations, significantly reducing deployment time and complexity.

Looking forward, the demonstrated multi-camera capabilities and robust performance characteristics of cu-
VSLAM establish a strong foundation for next-generation autonomous systems that demand reliable visual
localization in challenging real-world environments. The library’s proven versatility across platforms and
scenarios, combined with its efficient GPU-accelerated implementation, makes it a compelling choice for both
research prototypes and production robotic systems.




  3 https://developer.nvidia.com/isaac/perceptor




                                                                                                         13

## Page 14

cuVSLAM: CUDA accelerated visual odometry and mapping



 References
 [1] Kitti visual odometry / slam evaluation 2012. URL https://www.cvlibs.net/datasets/kitti/eval_
     odometry.php. Accessed: 2025-06. 15

 [2] Tartanair: A python package for the tartanair-v2 dataset.           URL https://github.com/castacks/
     tartanairpy. Accessed: 2025-06. 17

 [3] Timothy Barfoot. State Estimation for Robotics. 08 2017. ISBN 9781107159396. doi: 10.1017/
     9781316671528. 5

 [4] J. Y. Bouguet. Pyramidal implementation of the affine lucas kanade feature tracker description of the
     algorithm. Microprocessor Research Labs, 2000. URL https://robots.stanford.edu/cs223b04/algo_
     tracking.pdf. 3

 [5] Michael Burri, Janosch Nikolic, Pascal Gohl, Thomas Schneider, Joern Rehder, Sammy Omari, Markus W
     Achtelik, and Roland Siegwart. The euroc micro aerial vehicle datasets. The International Journal of
     Robotics Research, 35(10):1157–1163, 2016. doi: 10.1177/0278364915620033. 9

 [6] Carlos Campos, Richard Elvira, Juan J. Gomez Rodriguez, Jose M. M. Montiel, and Juan D. Tardos. Orb-
     slam3: An accurate open-source library for visual, visual–inertial, and multimap slam. IEEE Transactions
     on Robotics, 37(6):1874–1890, December 2021. ISSN 1941-0468. doi: 10.1109/tro.2021.3075644. URL
     http://dx.doi.org/10.1109/TRO.2021.3075644. 5

 [7] Nicholas Carlevaris-Bianco, Arash K. Ushani, and Ryan M. Eustice. University of Michigan North Campus
     long-term vision and lidar dataset. International Journal of Robotics Research, 35(9):1023–1035, 2015. 10

 [8] Chuchu Chen, Patrick Geneva, Yuxiang Peng, Woosik Lee, and Guoquan Huang. Monocular visual-inertial
     odometry with planar regularities. In 2023 IEEE International Conference on Robotics and Automation
     (ICRA), pages 6224–6231, 2023. doi: 10.1109/ICRA48891.2023.10160620. 9, 16

 [9] Christian Forster, Luca Carlone, Frank Dellaert, and Davide Scaramuzza. On-manifold preintegration
     for real-time visual–inertial odometry. IEEE Transactions on Robotics, 33(1):1–21, February 2017. ISSN
     1941-0468. doi: 10.1109/tro.2016.2597321. URL http://dx.doi.org/10.1109/TRO.2016.2597321.
     5

[10] Andreas Geiger, Philip Lenz, Christoph Stiller, and Raquel Urtasun. Vision meets robotics: The KITTI
     dataset. The International Journal of Robotics Research, 32(11):1231–1237, 2013. doi: 10.1177/
     0278364913491297. 9

[11] Anders Grunnet-Jepsen, Paul Winer, Aki Takagi, John Sweetser, Kevin Zhao, Tri Khuong, Dan Nie,
     and John Woodfill. Using the intel® realsense™ d400 series depth cameras in multi-camera config-
     urations. Technical report, Intel Corporation, 2018. URL https://dev.intelrealsense.com/docs/
     multiple-depth-cameras-configuration. Rev 1.2. 5

[12] Michael Grupp. evo: Python package for the evaluation of odometry and slam. https://github.com/
     MichaelGrupp/evo, 2017. Accessed: 2025. 9

[13] Ankur Handa, Thomas Whelan, John B. McDonald, and Andrew J. Davison. A benchmark for RGB-D visual
     odometry, 3D reconstruction and SLAM. In 2014 IEEE International Conference on Robotics and Automation
     (ICRA), pages 1524–1531, Hong Kong, China, May 2014. IEEE. doi: 10.1109/ICRA.2014.6907054. 9

[14] Christian Kerl, Jürgen Sturm, and Daniel Cremers. Dense visual slam for rgb-d cameras. pages 2100–2106,
     2013. doi: 10.1109/IROS.2013.6696650. 6



                                                                                                           14

## Page 15

cuVSLAM: CUDA accelerated visual odometry and mapping



[15] B. D. Lucas and T. Kanade. An iterative image registration technique with an application to stereo
     vision. Proceedings of Imaging Understanding Workshop, 1981. URL https://www.ri.cmu.edu/pub_
     files/pub3/lucas_bruce_d_1981_1/lucas_bruce_d_1981_1.pdf. 3

[16] Steven Macenski, Francisco Martin, Ruffin White, and Juan Ginés Clavero. The marathon 2: A navigation
     system. In 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages
     2718–2725. IEEE, 2020. 13

[17] Alexander Millane, Helen Oleynikova, Emilie Wirbel, Remo Steiner, Vikram Ramasamy, David Tingdahl,
     and Roland Siegwart. nvblox: Gpu-accelerated incremental signed distance field mapping. 2024. URL
     https://arxiv.org/abs/2311.00626. 13

[18] Ashish Devadas Nair, Julien Kindle, Plamen Levchev, and Davide Scaramuzza. Hilti slam challenge
     2023: Benchmarking single + multi-session slam across sensor constellations in construction, 2024. URL
     https://arxiv.org/abs/2404.09765. 10

[19] Manthan Patel, Fan Yang, Yuheng Qiu, Cesar Cadena, Sebastian Scherer, Marco Hutter, and Wenshan
     Wang. Tartanground: A large-scale dataset for ground robot perception and navigation, 2025. URL
     https://arxiv.org/abs/2505.10696. 9, 17

[20] David Schubert, Thore Goll, Nikolaus Demmel, Vladyslav Usenko, Jörg Stückler, and Daniel Cremers.
     The TUM VI benchmark for evaluating visual-inertial odometry. CoRR, abs/1804.06120, 2018. URL
     http://arxiv.org/abs/1804.06120. 9, 16

[21] Jianbo Shi and Carlo Tomasi. Good features to track. 1994 Proceedings of IEEE Conference on Computer
     Vision and Pattern Recognition, 37(6), December 1993. ISSN 1063-6919. doi: 10.1109/CVPR.1994.
     323794. URL https://ieeexplore.ieee.org/document/323794. 3

[22] Jürgen Sturm, Nikolas Engelhard, Felix Endres, Wolfram Burgard, and Daniel Cremers. A benchmark for
     the evaluation of rgb-d slam systems. In 2012 IEEE/RSJ International Conference on Intelligent Robots and
     Systems (IROS), pages 573–580. IEEE, Oct 2012. doi: 10.1109/IROS.2012.6385773. 9

[23] Wenshan Wang, Yaoyu Hu, Yuheng Qiu, Shihao Shen, and Yorai Shaoul. Tartanair-v2 dataset, 2023. URL
     https://tartanair.org. Accessed: 2025-06. 9, 17

[24] Jie Yin, Ang Li, Tao Li, Wenxian Yu, and Danping Zou. M2dgr: A multi-sensor and multi-scenario slam
     dataset for ground robots. IEEE Robotics and Automation Letters, 7(2):2266–2273, 2021. 10

[25] Chaitanya; Zhang Christina; Hong Raymond; Kalyani Pranav; Kalyanaraman Lochana; Gamare Arsh;
     Bagad Arnav; Esteva Maria; Biswas Joydeep Zhang, Arthur; Eranki. Ut campus object dataset (coda),
     2023. URL https://doi.org/10.18738/T8/BBOQMV. 10


A. Appendix
A.1. Appendix A. Detailed Description of Dataset Validation
A.1.1. KITTI Dataset
We evaluated our method on sequences 0-10 of the KITTI dataset, for which ground truth trajectories are
available. For comparison with the conventional KITTI leaderboard (1), Figure 10 presents relative translation
(avgRTE) and rotation (avgRE) errors calculated on trajectory segments of lengths 100, 200, 300, 400, 500,
600, 700, and 800 meters. In contrast Table 2 presents results calculated without trajectory segmentation to
maintain metric comparability across different datasets.




                                                                                                           15

## Page 16

cuVSLAM: CUDA accelerated visual odometry and mapping




  Figure 10: cuVSLAM evaluation results on KITTI odometry benchmark sequences 00-10. Translation and
rotation errors are calculated on segments of 100-800m following the KITTI public leaderboard methodology,
                     averaged metrics: Translation: 0.85%, Rotation: 0.0025 [deg/m].


A.1.2. TUM-VI Room Dataset
To validate the stereo-inertial tracking mode on real hardware under aggressive camera motions, we evaluated
cuVSLAM on the Room sequences of the TUM-VI dataset (20). These sequences were selected because they
provide complete ground truth trajectories. We used undistorted images with a resolution of 512x512 pixels and
applied a 50-pixel mask along each frame edge to mitigate significant fisheye lens distortion, which negatively
affects tracking performance. To facilitate comparison with other visual tracking methods, we followed the
evaluation protocol described in the original TUM-VI paper (20), computing the average RMSE of the Relative
Pose Error (RPE) in meters/degrees over 1-second segments. Detailed results are provided in Table 4.

Table 4: cuVSLAM Stereo Inertial tracking validation results on TUM-VI Room dataset RMSE RPE (m / deg) on
1 second segments

                                   Sequence         ODOM             SLAM
                                   room1         0.023 / 0.89     0.025 / 0.90
                                   room2         0.048 / 2.28     0.048 / 2.29
                                   room3         0.047 / 1.93     0.048 / 1.95
                                   room4         0.015 / 0.54     0.015 / 0.55
                                   room5         0.019 / 0.56     0.021 / 0.57
                                   room6         0.021 / 0.57     0.021 / 0.58


A.1.3. AR-table Dataset
This dataset contains sequences captured using an Intel RealSense D455 depth camera, providing image
and depth data at a resolution of 848x480 pixels. The enhanced image and depth quality allows achieving
performance on this real-world camera close to that obtained on the ideal simulated ICL-NUIM dataset, as
shown in Table 2.

However, consistent gaps in depth values were observed along the sides and bottom edges of the depth
images. To mitigate this issue, we applied static masking of 24 pixels on each side and 10 pixels at the bottom.
Additionally, several prolonged depth-image dropouts (lasting more than one second) occurred in sequences 3,
4, 5, and 8. To address these interruptions, we segmented the affected sequences into continuous portions,
executed tracking independently on each segment, and subsequently merged the results.

To facilitate comparison with other visual tracking methods, we followed the evaluation methodology described
in the original AR-table dataset paper (8). Specifically, we computed Absolute Trajectory Error (ATE), reporting
translation errors in centimeters and rotation errors in degrees. The obtained results are summarized in Table 5.


                                                                                                              16

## Page 17

cuVSLAM: CUDA accelerated visual odometry and mapping




Table 5: cuVSLAM Mono-Depth Odometry and SLAM validation results on AR table dataset ATE (degree / cm)

 Mode       table_01      table_02      table_03      table_04      table_05      table_06        table_07      table_08
 ODOM      3.77 / 2.03   9.36 / 5.41   6.09 / 2.28   3.13 / 2.21   2.27 / 1.97   3.43 / 3.39     18.5 / 6.17   13.2 / 8.18
 SLAM      2.98 / 1.76   2.23 / 1.77   2.11 / 0.87   2.12 / 1.64   1.24 / 1.22   1.93 / 1.23     8.88 / 3.82   4.83 / 3.69



A.1.4. TUM RGB-D Dataset
To validate the Mono-Depth mode on this dataset, a subset of 10 sequences from the Freiburg3 collection
was used. These sequences were selected as they provide rectified images, which are required by cuVSLAM
Mono-Depth mode. Minimal preprocessing was performed, consisting only of depth-image pair synchronization
without further image or depth processing. The complete list of evaluated sequences is provided in Table 6.

Table 6: Results of cuVSLAM Mono-Depth Odometry and SLAM evaluation on TUM RGB-D dataset

                Sequence                                  Mode      avgRTE       avgRE         RMSE APE
                                                          ODOM       1.74         2.08           0.12
                large cabinet validation
                                                          SLAM       1.53         1.60           0.11
                                                          ODOM       1.27         7.89           0.20
                long office household
                                                          SLAM       0.96         5.94           0.06
                                                          ODOM       1.29         1.66           0.07
                nostructure texture far
                                                          SLAM       1.44         1.63           0.06
                                                          ODOM       1.23         4.62           0.10
                nostructure texture near withloop
                                                          SLAM       1.25         4.71           0.04
                                                          ODOM       2.07         3.67           0.12
                sitting halfsphere
                                                          SLAM       0.61         1.42           0.05
                                                          ODOM       1.03         1.21           0.05
                sitting xyz
                                                          SLAM       0.65         0.86           0.03
                                                          ODOM       0.90         1.42           0.05
                sitting xyz validation
                                                          SLAM       0.44         0.67           0.03
                                                          ODOM       1.11         1.46           0.04
                structure texture far
                                                          SLAM       0.55         0.69           0.02
                                                          ODOM       1.45         2.15           0.03
                structure texture near
                                                          SLAM       1.45         2.09           0.03
                                                          ODOM       1.38        29.04           0.31
                teddy
                                                          SLAM       1.04        21.70           0.22

A.1.5. TartanGround and TartanAir V2
Odometry Mode. We validated cuVSLAM using 216 sequences from TartanGround (19) and 539 sequences
from TartanAir V2 (23) Hard datasets. Complete sequence lists are provided in Tables 7 and 10, respectively.
All results were obtained using a four stereo-camera configuration (front, back, left, and right) with 640×640
undistorted images. While the TartanAir V2 dataset supports two additional cameras (top and bottom), their
inclusion yielded minimal metric improvement (less than 5%). For the TartanGround dataset, we observed slight
performance degradation when using these additional cameras, attributed to meaningless feature selection
from sky regions and repetitive floor textures in planar robot navigation areas.

To facilitate comparison with other visual tracking libraries, we computed additional metrics—relative transla-
tion (𝑡rel ) and rotation (𝑟rel ) per frame—using scripts from the official TartanAir GitHub repository (2). Since
not all environments from the original TartanGround paper were available, we present environment-averaged
results in Table 7 to enable future comparative studies.

TartanAir V2 Easy sequences were excluded from our analysis as they present minimal challenge for cuVSLAM,
yielding consistently high tracking quality similar to the TartanGround dataset. To support this decision, Table 8


                                                                                                                         17

## Page 18

cuVSLAM: CUDA accelerated visual odometry and mapping


Table 7: Odometry evaluation results for cuVSLAM Multi-Stereo configuration (4 stereo cameras) on Tartan-
Ground dataset. Values represent averages computed per environment.

     Environment                Sequences             avgRTE      avgRE     RMSE APE      𝑡rel      𝑟rel
     Downtown                   P0-P17                 0.30        0.41       0.11      0.0019   0.00013
     ForestEnv                  P0-P22                 0.45        0.72       0.19      0.0024   0.00036
     Gascola                    P0-P21                 0.24        0.46       0.09      0.0012   0.00018
     GreatMarsh                 P1-P19, P21-P29        2.34        4.21       0.45      0.0037   0.00126
     ModernCityDowntown         P1-P10                 0.19        0.39       0.08      0.0012   0.00014
     ModularNeighborhood        P0-P29                 0.42        0.65       0.12      0.0014   0.00016
     NordicHarbor               P0-P27                 0.23        0.41       0.06      0.0010   0.00015
     OldTownFall                P0-P7                  0.15        0.34       0.04      0.0011   0.00013
     OldTownSummer              P0-P7                  0.15        0.34       0.05      0.0011   0.00013
     SeasonalForestAutumn       P0-P19                 0.27        0.42       0.11      0.0017   0.00022
     SeasonalForestSpring       P0-P19                 0.23        0.49       0.12      0.0016   0.00024
     SeasonalForestWinter       P0-P21                 0.27        0.51       0.08      0.0011   0.00018
     Average                                           0.54        0.95       0.14      0.0017   0.00032


presents a comparison of averaged four-stereo-camera odometry results between Easy and Hard subsets of
TartanAir V2, with example trajectory estimates shown in Figure 11.

Table 8: Comparative odometry evaluation of cuVSLAM Multi-Stereo (4 stereo cameras) on TartanAir V2 Easy
and Hard sequences. Results show average performance metrics for selected environments.

                     Environment              Difficulty    avgRTE      avgRE      RMSE APE
                                                 easy        0.05        0.56        0.26
                     AbandonedCable
                                                hard         1.93        14.5        8.65
                                                 easy        0.02        0.13        0.02
                     AbandonedFactory2
                                                hard         0.27        1.41        0.34
                                                 easy        0.03        0.16        0.02
                     CoalMine
                                                hard         0.37        1.25        0.56
                                                 easy        0.08        0.58        0.17
                     GothicIsland
                                                hard         1.73       13.44        4.48
                                                 easy        0.04        0.60        0.06
                     Hospital
                                                hard         1.50       16.17        3.25
                                                 easy        0.06        0.34        0.06
                     JapaneseAlley
                                                hard         0.97        5.45        0.50
                                                 easy        0.06        0.54        0.04
                     OldBrickHouseDay
                                                hard         1.74       11.15        1.48

SLAM Mode. To evaluate the impact of SLAM mode on trajectory estimation, we analyzed only sequences
containing loop closures. This resulted in a subset of 32 sequences for TartanGround and 506 sequences for
TartanAir V2 Hard. Complete tracking results are provided in Tables 9 and 10, with all results averaged across
environments.

For the TartanAir V2 dataset, most environments utilized all available sequences. Sequences excluded from
SLAM validation are marked with an asterisk (P*), while their corresponding visual odometry results are
labeled ODOM*, indicating performance metrics computed across all available sequences for those specific
environments, including the excluded sequences.

A.1.6. Mutli-Stereo R2B Dataset
The Multi-Stereo R2B dataset was acquired using a wheeled Carter robot platform equipped with four stereo
Hawk cameras, each capturing RGB images at a resolution of 1920×1200 pixels and 30 frames per second. The
stereo camera pairs are hardware-synchronized to ensure temporal coherence, with synchronization precision


                                                                                                           18

## Page 19

cuVSLAM: CUDA accelerated visual odometry and mapping




Figure 11: Example trajectories predicted by cuVSLAM (4 Multi-Stereo Odometry) on TartanAir V2 (Easy and
Hard). Black lines represent ground truth, green lines represent odometry predictions. Columns correspond to
                      the same environment and sequence label at different difficulties.


maintained within 0.1 ms for each 8-image batch. Data integrity validation confirmed minimal frame loss
across all recordings, with the maximum batch loss rate remaining below 0.04%. Figure 12 illustrates the
complete set of recorded trajectories, along with corresponding trajectory lengths and synchronized image
batch counts for each sequence.




 Figure 12: Trajectories predicted by cuVSLAM (4 Multi-Stereo Odometry) on the proprietary R2B wheeled
robot dataset. Black lines represent ground truth; green lines represent odometry predictions. Attached table
 lists trajectory distances, number of 8-image batches, and trajectory index for environments (left to right).


A.2. Appendix B: Hardware Scalability on Embedded Platforms
This appendix presents an analysis of hardware utilization and visual tracking performance for cuVSLAM on
embedded platforms, comparing Multi-Stereo and Mono-Depth modes as representative examples of sparse
and dense feature-based approaches, respectively.

Experimental Setup. The primary hardware configuration consisted of an NVIDIA Jetson Orin AGX operating


                                                                                                           19

## Page 20

cuVSLAM: CUDA accelerated visual odometry and mapping



in MAXN mode with 3 Intel RealSense D435 stereo cameras connected via USB and hardware-synchronized.
Different resolutions were obtained directly from the cameras by modifying their configuration during the
initialization step of each experiment. For Full HD resolution testing, we employed a set of 3 RGB Hawk stereo
cameras connected via FAKRA2 connectors with hardware synchronization. All experiments were conducted
in real-time with live camera feeds connected directly to the Jetson boards, and cuVSLAM calculations were
performed on the same board in real-time. The system operated in Performance mode, utilizing the Isaac ROS
(ROS2) stack for image acquisition and Multi-Stereo visual tracking, while the Python stack was employed for
Mono-Depth visual tracking and processing.

Methodology. Resource utilization was measured through a two-phase experimental protocol designed to
isolate the computational overhead of cuVSLAM. In the first phase, system utilization was logged while receiving
frames from freely moving cameras without invoking visual tracking, establishing a baseline measurement. In
the second phase, the identical setup was used with cuVSLAM visual tracking enabled. CPU and GPU utilization
metrics were sampled at 15ms intervals, and the time spent on cuVSLAM frame processing was logged for each
frame and subsequently averaged. The net computational resource utilization of cuVSLAM was calculated by
subtracting the baseline measurements from the active tracking measurements.

Jetson Orin AGX Performance. Figure 13 illustrates the significant computational efficiency advantage of the
sparse feature-based approach for tracking, demonstrating 3-7× faster processing times for 6-image batches
compared to single image-depth pairs. The phenomenon where the 3-stereo camera visual tracking in Full
HD configuration exhibited lower hardware utilization than HD configuration is attributed to differences in
the camera field-of-view, with Hawk cameras provided 121.5° × 73.5° FOV in FHD mode versus RealSense
D435 cameras provided 87° × 58° FOV in HD mode. The wider field-of-view affects the lifetime of keypoints as
described in Section 2.1, triggering more frequent keyframe creation and consequently invoking computation-
ally intensive operations including 3D landmark triangulation and sparse bundle adjustment, as detailed in
Sections 2.1 and 2.2.




Figure 13: cuVSLAM realtime network hardware utilization and callback time per input image on Jetson AGX
Orin as a function of resolution for 3-Stereo Camera Visual Odometry (left) and Mono-Depth Visual Odometry
                          (right) at 30 FPS. For further details, refer to Appendix A.2

For Mono-Depth mode, the average callback time for 720p resolution reached 37.7ms, which exceeds the
33.3ms frame interval required for 30 FPS operation. This timing constraint indicates GPU overload on the
Orin AGX platform in this configuration, and according to our measurements, resulted in the system skipping
approximately half of the incoming frames. Consequently, for HD resolution applications, we recommend
either reducing the frame rate to 15 FPS or decreasing the resolution to VGA, as our experiments revealed no
significant difference in cuVSLAM visual tracking quality between VGA and HD resolutions.

Jetson Orin Nano Performance. To evaluate the feasibility of deploying cuVSLAM on entry-level hardware,
we conducted experiments replacing the Jetson Orin AGX with a Jetson Orin Nano Super operating in 25W
mode and utilizing exclusively the Python stack. The experiments explore possibility of using multi-stereo


                                                                                                             20

## Page 21

cuVSLAM: CUDA accelerated visual odometry and mapping



odometry mode for 640x360 resolution and 30 FPS followed the methodology described above with free camera
movement.




 Figure 14: Hardware utilization and callback time on Jetson Orin Nano for Multi-Stereo Visual Odometry
 using RealSense cameras at 640×360 resolution and 30 FPS. Results are presented for varying numbers of
   cameras, showing total utilization (faded color bars) and net cuVSLAM utilization (normal color bars).

The results of average net cuVSLAM resource utilization, total system load, and average processing time are
presented in Figure 14. The findings demonstrate substantial resource headroom, enabling the use of higher
frame rates for configurations with one or 2 stereo cameras. For Mono-Depth processing at 30 FPS, stable
operation was achieved only at the minimum resolution of 424×240 pixels. Although the average GPU load
remained below 40%, the observed average cuVSLAM call time of 31ms approached the critical 33ms frame
interval at 30 FPS. When combined with additional operations in the image acquisition loop, this resulted in
exceeding the frame interval and consequently dropping approximately 30% of incoming frames.

It is important to note that for scenarios involving ground robots, the observed computational load will be lower
than our free-movement test scenarios due to the reduced number of keyframes generated during predominantly
inertial movements. However, for systems involving freely moving cameras with rapid scene changes, such as
handheld cameras or unmanned aerial vehicles, we recommend increasing frame rates to 60 FPS when using
RealSense cameras to ensure robust tracking performance. The selection of appropriate resolution and frame
rate parameters should be carefully balanced based on the available computational resources and specific
application requirements.




                                                                                                              21

## Page 22

cuVSLAM: CUDA accelerated visual odometry and mapping




Table 9: Comparative evaluation of odometry and SLAM performance for cuVSLAM Multi-Stereo (4 stereo
cameras) on the TartanGround dataset. To assess the impact of SLAM mode, a subset of sequences containing
looped trajectories with observable loop closures was selected. Reported values are averages computed per
environment.

          Environment              Sequences               Mode      avgRTE      avgRE   RMSE APE
                                                           ODOM       0.35        0.59     0.09
          Downtown                 P7
                                                           SLAM       0.25        0.41     0.09
                                                           ODOM       0.42        0.78     0.16
          ForestEnv                P1, P14, P17, P21
                                                           SLAM       0.38        0.61     0.17
                                                           ODOM       0.17        0.41     0.08
          Gascola                  P0, P3-P6, P9
                                                           SLAM       0.13        0.31     0.06
                                                           ODOM       0.17        0.32     0.08
          ModernCityDowntown       P2, P5-P7
                                                           SLAM       0.12        0.24     0.06
                                                           ODOM       0.42        1.17     0.14
          ModularNeighborhood      P12, P20
                                                           SLAM       0.35        1.02     0.05
                                   P1, P11, P17-P19        ODOM       0.17        0.41     0.08
          NordicHarbor                 P23, P27            SLAM       0.10        0.26     0.04
                                                           ODOM       0.07        0.31     0.05
          OldTownFall              P2
                                                           SLAM       0.12        0.26     0.06
                                                           ODOM       0.09        0.29     0.06
          OldTownSummer            P2-P4
                                                           SLAM       0.06        0.25     0.03
                                                           ODOM       0.20        0.32     0.07
          SeasonalForestAutumn     P5, P8, P17
                                                           SLAM       0.19        0.33     0.07
                                                           ODOM       0.15        0.49     0.05
          SeasonalForestSpring     P9
                                                           SLAM       0.11        0.39     0.02
                                                           ODOM       0.21        0.48    0.088
          Average
                                                           SLAM       0.17        0.37    0.065




                                                                                                      22

## Page 23

cuVSLAM: CUDA accelerated visual odometry and mapping


Table 10: TartanAir V2 Hard cuVSLAM evaluation                   Table 11: TartanAir V2 Hard cuVSLAM evaluation
results (Envs 1–35, see Appendix A.1.5 for details)              results (Envs 36–71, see Appendix A.1.5 for details)
      Env            Seq          Mode    RTE     RRE     APE          Env               Seq          Mode    RTE     RRE      APE
      Abandoned-                  ODOM    1.90   13.77   8.97          ModernCity                     ODOM    2.34   11.70     4.01
 1                   P0-P7                                        36                     P0-P8
         Cable                    SLAM    1.54   11.47   7.15          Downtown                       SLAM    2.08   11.34     3.60
      Abandoned-     P1-P6        ODOM    1.07    4.89   1.06            Modular-                     ODOM    4.14   22.48    17.10
 2                                                                37                     P0-P10
        Factory      P8-P9        SLAM    0.77    3.70   0.95          Neighborhood                   SLAM    3.60   21.04    13.85
      Abandoned-                  ODOM    0.27    1.41   0.34          ModularNeigh      P1-P5        ODOM    2.64   15.80     4.74
 3                   P0-P5                                        38                     P7-P8
       Factory2                   SLAM    0.19    0.84   0.24          borhoodIntExt                  SLAM    2.62   13.93     5.13
      Abandoned-                  ODOM    3.59   33.78   5.41                                         ODOM    2.07   14.37     6.04
 4                   P0-P9                                        39   NordicHarbor      P0-P7
        School                    SLAM    3.31   31.42   5.12                                         SLAM    1.97   15.04     5.77
                                  ODOM*   5.53   13.27   1.25                            P1-P3        ODOM*   1.76    8.13     1.99
      American-      P0, P2*
 5                                ODOM    5.21   11.12   1.05     40   Ocean              P4*         ODOM    1.65    8.66     2.36
       Diner          P3-P4
                                  SLAM    4.98   10.94   0.93                            P5-P7        SLAM    1.47    7.12     2.22
                      P0, P1*     ODOM*   1.15    3.74   1.53                                         ODOM*   3.51   16.02     2.71
      Amusement-                                                  41   Office            P0-P6
 6                   P2-P3, P4*   ODOM    1.36    5.15   1.71                                         SLAM    3.36   14.84     2.49
         Park
                       P5-P7      SLAM    1.36    5.49   1.71                            P1-P2        ODOM*   1.74   11.15     1.48
                                                                       OldBrick-
      Ancient-                    ODOM    2.86   10.98   2.52     42                      P3*         ODOM    1.54   11.80     1.25
 7                   P0-P6                                             HouseDay
       Towns                      SLAM    2.50    8.93   2.23                            P4-P7        SLAM    1.29    7.76     1.10
                     P1-P5, P6*   ODOM*   2.30   17.90   4.05                            P1*, P2      ODOM*   1.83   16.07     1.53
                                                                        OldBrick-
 8    Antiquity3D                 ODOM    1.95   16.53   3.69     43                                  ODOM    1.68   16.35     1.56
                     P7, P8*,P9                                        HouseNight         P4-P7
                                  SLAM    1.84   15.23   3.55                                         SLAM    1.59   13.05     1.50
                                  ODOM    0.92    4.25   1.25              Old-                       ODOM    2.25    8.60     4.33
 9    Apocalyptic    P0-P4                                        44                     P0-P9
                                  SLAM    0.66    2.81   0.98          IndustrialCity                 SLAM    1.58    7.20     3.76
                      P0, P1*     ODOM*   3.75    4.02   0.37             Old-                        ODOM*   2.22   11.68     8.90
      ArchVizTiny-                                                45                     P1-P6
 10                  P2-P3,P4*    ODOM    2.69    3.48   0.27          Scandinavia                    SLAM    2.15   11.47     8.38
       HouseDay
                       P5-P6      SLAM    2.44    3.14   0.25                            P0*,P1*      ODOM*   1.62    6.44     1.53
                     P0*, P1      ODOM*   5.37    6.23   0.47     46   OldTownFall                    ODOM    1.25    4.09     0.11
      ArchVizTiny-                                                                         P2
 11                  P5, P6*      ODOM    4.19    5.64   0.39                                         SLAM    0.75    2.47     0.28
      HouseNight                  SLAM    4.15    5.91   0.36
                     P2-P4*                                                                           ODOM    0.83    4.74     1.24
                                                                  47   OldTownNight      P0-P2
      Brushify-                   ODOM    5.64   40.15   44.55                                        SLAM    0.61    3.49     0.95
 12                  P1-P5
       Moon                       SLAM    6.23   41.28   45.50         OldTown-                       ODOM    2.42   11.90     1.57
                                                                  48                     P0-P2
                                  ODOM    1.14    5.74   1.34          Summer                         SLAM    2.41   11.84     1.54
 13   CarWelding     P0-P8
                                  SLAM    0.94    4.51   1.27          OldTown-                       ODOM    0.60    2.14     0.72
                                                                  49                     P0-P2
      Castle-                     ODOM    0.93    7.33   2.65           Winter                        SLAM    0.53    2.33     0.75
 14                  P0-P11
      Fortress                    SLAM    0.90    6.41   2.50                                         ODOM    2.76   12.74     2.19
                                                                  50   PolarSciFi        P0-P8
                                  ODOM    0.34    1.42   0.51                                         SLAM    2.68   12.34     2.18
 15   CoalMine       P0-P5
                                  SLAM    0.20    0.67   0.38                                         ODOM    4.14   21.37     4.59
                                                                  51   Prison            P0-P11
                     P1, P3*      ODOM*   2.80    8.81   3.15                                         SLAM    4.12   20.78     4.68
      Construct-
 16                   P5*         ODOM    2.90    9.23   3.31                                         ODOM    1.51   10.99     0.97
        Site                                                      52   Restaurant        P1-P8
                     P6-P11       SLAM    2.80    8.74   3.14                                         SLAM    1.03    8.00     0.70
      Country-                    ODOM    0.87    2.69   0.20                                         ODOM    1.14    3.11     0.10
 17                  P0-P5                                        53   RetroOffice       P0-P5
       House                      SLAM    0.16    0.62   0.05                                         SLAM    0.94    2.85     0.09
      CyberPunk-                  ODOM    1.19    7.27   4.01                            P1-P6        ODOM    3.07   16.68     9.43
 18                  P0-P6                                        54   Ruins
      Downtown                    SLAM    1.27    8.22   3.98                            P8-P9        SLAM    3.05   17.07     9.09
                                  ODOM    1.13    4.65   3.38                                         ODOM    0.67    1.79     0.56
 19   Cyberpunk      P0-P7                                        55   SeasideTown       P0-P7
                                  SLAM    1.13    5.43   4.23                                         SLAM    0.61    1.58     0.44
       Desert-                    ODOM    2.44    7.11   2.53          SeasonForest-                  ODOM    5.41   35.20    21.38
 20                  P0-P4                                        56                     P0-P2
      GasStation                  SLAM    2.31    6.78   2.43            Autumn                       SLAM    5.10   31.76    18.73
                                  ODOM    1.20    5.66   3.59          SeasonForest-                  ODOM    4.09   25.14    15.03
 21   Downtown       P0-P8                                        57                     P0-P3
                                  SLAM    1.21    5.52   3.35             Spring                      SLAM    3.93   28.30    15.02
      Factory-                    ODOM*   6.23   39.06   22.37         SeasonForest-                  ODOM    3.65   21.45    25.05
                     P1-P7, P8*                                   58                     P0-P1
 22                               ODOM    6.31   40.09   22.64         SummerNight                    SLAM    3.45   19.42    23.00
      Weather         P9-P12
                                  SLAM    6.17   37.40   22.22         SeasonForest-                  ODOM    6.73   30.59    15.47
                                                                  59                     P0-P2
                                  ODOM    1.01    4.16   1.45             Winter                      SLAM    7.53   32.61    19.11
 23   Fantasy        P0-P6
                                  SLAM    1.01    4.70   1.87          SeasonForest-                  ODOM    4.77   30.45    27.40
                     P0, P2-P5                                    60                     P0-P2
                                  ODOM*   3.67   21.93   13.76          WinterNight                   SLAM    5.14   30.09    26.31
 24   ForestEnv       P7, P9      ODOM    3.55   21.75   14.42                                        ODOM    3.94   30.11     6.74
                                  SLAM    3.62   23.64   15.47    61   Sewerage          P1-P11
                     P10*, P11                                                                        SLAM    3.87   27.64     5.92
                                  ODOM    2.36   14.83   5.47                                         ODOM    1.86    7.56     3.41
 25   Gascola        P0-P9                                        62   ShoreCaves        P1-P8
                                  SLAM    2.49   14.56   6.13                                         SLAM    1.77    7.20     3.00
      Gothic-                     ODOM    1.68   13.19   4.00                            P0, P1*      ODOM*   4.52   26.89     6.04
 26                  P0-P10
      Island                      SLAM    1.44   11.60   3.54     63   Slaughter         P2-P10       ODOM    3.97   27.19     5.53
      HQWestern-                  ODOM    2.67   16.93   2.01                             P11*        SLAM    3.80   24.49     5.34
 27                  P0-P7
         Saloon                   SLAM    1.96    8.81   1.60                            P0*,P1,P2*   ODOM*   5.22   32.59     7.30
                     P0, P1*      ODOM*   5.26   18.85   5.02     64   SoulCity          P3-P4, P5*   ODOM    4.74   28.79     7.96
 28   HongKong                    ODOM    4.81   18.85   3.99                              P6, P7     SLAM    4.82   29.27     8.10
                      P2-P4
                                  SLAM    4.75   17.78   3.89                                         ODOM*   4.70   23.19     3.69
                                                                                         P0*,P1,P2
                                  ODOM    1.50   16.17   3.25     65   Supermarket                    ODOM    4.82   22.64     3.66
 29   Hospital       P0-P10                                                              P3*, P4-P6
                                  SLAM    1.30   14.85   2.93                                         SLAM    4.73   23.38     3.60
                                  ODOM    1.47    9.80   0.47          Terrain-                       ODOM    0.45    1.65     1.31
 30   House          P0-P7                                        66                     P1, P3-P4
                                  SLAM    0.98    6.43   0.26          Blending                       SLAM    0.55    1.90     1.55
      Industrial-                 ODOM    3.43   19.61   8.21             Urban-                      ODOM    0.35    1.76     1.30
 31                                                               67                     P0-P4
        Hangar       P0-P6        SLAM    3.48   19.86   8.03          Construction                   SLAM    0.31    1.50     1.24
      Japanese-                   ODOM    0.94    5.27   0.48                                         ODOM    0.99    4.67     0.43
 32                  P0-P6                                        68   VictorianStreet   P0-P7
         Alley                    SLAM    0.34    1.87   0.39                                         SLAM    0.72    3.17     0.25
      Japanese-                   ODOM    1.81    7.89   2.08                                         ODOM    0.48    2.54     0.74
 33                  P0-P10                                       69   WaterMillDay      P1-P3, P6
         City                     SLAM    1.74    7.80   2.03                                         SLAM    0.30    1.12     0.59
                                  ODOM    2.96   13.18   2.64                                         ODOM    0.34    0.94     0.78
 34   MiddleEast     P0-P10                                       70   WaterMillNight    P0-P6
                                  SLAM    2.65   11.34   2.47                                         SLAM    0.29    0.92     0.72
        Mod-                      ODOM    3.65   23.51   5.74           Western-         P1-P7, P9    ODOM    1.89   13.77     8.09
 35                  P0-P11                                       71
      UrbanCity                   SLAM    3.70   23.22   5.60          DesertTown        P11, P13     SLAM    1.78   12.97     7.32

                                                                                                                             23
