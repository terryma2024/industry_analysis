---
source_id: "SRC-robotics-357"
title: "OpenVINS research platform for visual-inertial estimation paper full PDF"
source_type: "research_paper"
publisher: "Robot Perception and Navigation Group / University of Delaware"
source_date: "2020"
url: "https://pgeneva.com/downloads/papers/Geneva2020ICRA.pdf"
evidence_grade: "S"
capture_method: "pdf-key-info-draft"
captured_at: "2026-08-05T06:50:30+00:00"
source_markdown: "SRC-robotics-357-openvins-research-platform-for-visual-inertial-estimation-paper-full-pdf.md"
tags:
  - raw/source
  - raw/pdf
  - source-type/research-paper
  - evidence/s
aliases:
  - SRC-robotics-357
---
# OpenVINS research platform for visual-inertial estimation paper full PDF - Key Information Draft

> [!warning]
> This is an extraction draft for analyst review. Verify claims against the raw PDF/Markdown before using them in knowledge notes.

## Source Trace

- Source ID: `SRC-robotics-357`
- Raw Markdown: [SRC-robotics-357-openvins-research-platform-for-visual-inertial-estimation-paper-full-pdf.md](SRC-robotics-357-openvins-research-platform-for-visual-inertial-estimation-paper-full-pdf.md)
- Evidence grade: `S`

## Page-Level Leads

- [p. 1] OpenVINS: A Research Platform for Visual-Inertial Estimation Patrick Geneva, Kevin Eckenhoff, Woosik Lee, Yulin Yang, and Guoquan Huang Abstract— In this paper, we present an open platform, termed deep understanding, thus accelerating VINS research and OpenVINS, for visual-inertial estimation research for both the development in the field.
- [p. 1] Moreover, these systems have many academic community and practitioners from industry.
- [p. 2] ON-MANIFOLD MODULAR EKF where ˆ· denotes the estimated value and the subscript k|k −1 The state vector of our visual-inertial system consists of denotes the predicted estimate at time k given the mea- the current inertial navigation state, a set of c historical IMU surements up to time k − 1.
- [p. 2] The state covariance matrix pose clones, a set of m environmental landmarks, and a set is propagated typically by linearizing the nonlinear model at of w cameras’ extrinsic and intrinsic parameters.
- [p. 3] Landmark Update protected : / / Current best estimate We generalize the landmark measurement model as a E i g e n : : MatrixXd v a l u e ; series of nested functions to encompass different feature / / Index of error s t a t e in covariance parameterizations such as 3D position and inverse depth and i n t i d = −1; so on.
- [p. 3] Assuming a visual feature that has been tracked over / / Dimension o f e r r o r s t a t e the sliding window of stochastic clones [35], we can write i n t s i z e = −1; / / V e c t o r c o r r e c t i o n , how t o u p d a t e the visual-bearing measurements (i.e., pixel coordinates) as v o i d u p d a t e ( c o n s t E i g e n : : VectorXd dx ) ;
- [p. 4] visual-inertial estimation algorithms.
- [p. 4] To bridge this gap the our cubic B-spline.
- [p. 5] 2: Camera intrinsic projection and distortion along with extrinsic orientation and positions parameters error (blue-solid) and 3σ bounds (red-dashed) for a representative run.
- [p. 5] Note that we only plot the first sixty seconds of the dataset.
- [p. 6] TABLE II: Ten runs mean absolute trajectory error (ATE) for each algorithm in units of degree/meters.
- [p. 6] Note that V2 03 dataset is excluded due the inability for some algorithms to run on it.
- [p. 7] Mourikis, “Online temporal calibration for Camera- IMU systems: Theory and algorithms,” International Journal of [1] G.
- [p. 7] Huang, “Visual-inertial navigation: A concise review,” in Proc.

## Extracted Tables

### Table 1 (p. 2)

         h                                     i>                                 Pk|k−1 = Φk−1 Pk−1|k−1 Φ>

### Table 2 (p. 2)

with the vector space R12 (i.e. M = H × R12 ) and has 15                          zm,k = h(x̂k|k−1  x̃k|k−1 ) + nm,k             (11)
total degrees of freedom (DOF).                                                         = h(x̂k|k−1 ) + Hk x̃k|k−1 + nm,k         (12)

### Table 3 (p. 2)

quaternions, we define the quaternion boxplus operation as:                               ∂h(x̂k|k−1  x̃k|k−1 )

### Table 4 (p. 2)

                                                                            x̂k|k = x̂k|k−1  Kk (zm,k − h(x̂k|k−1 ))             (15)

### Table 5 (p. 2)

3D positions only for simplicity, while in practice we offer                Pk|k = Pk|k−1 − Kk Hk Pk|k−1                          (16)

### Table 6 (p. 2)

             x̂k|k−1 = f (x̂k−1|k−1 , I am , I ωm , 0)           (8)    and its manifold representation (i.e. the update function).


## Analyst Checklist

- Facts: extract numeric claims, dates, policy names, technical claims, and company disclosures.
- Estimates: mark market-size forecasts, CAGR, shipment forecasts, and assumptions.
- Judgments: separate source judgments from your own investment/career analysis.
- Traceability: cite page numbers or table numbers before moving claims into `knowledge/` notes.
