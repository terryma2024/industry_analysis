---
source_id: "SRC-robotics-357"
title: "OpenVINS research platform for visual-inertial estimation paper full PDF"
source_type: "research_paper"
publisher: "Robot Perception and Navigation Group / University of Delaware"
source_date: "2020"
url: "https://pgeneva.com/downloads/papers/Geneva2020ICRA.pdf"
evidence_grade: "S"
capture_method: "pdf-extract-pdftotext"
captured_at: "2026-08-05T06:50:30+00:00"
pdf_file: "raw/robotics-embodied-ai/documents/SRC-robotics-357-openvins-research-platform-for-visual-inertial-estimation-paper-full-pdf.pdf"
page_count: "7"
tags:
  - raw/source
  - raw/pdf
  - source-type/research-paper
  - evidence/s
aliases:
  - SRC-robotics-357
---
# OpenVINS research platform for visual-inertial estimation paper full PDF

## Page 1

OpenVINS: A Research Platform for Visual-Inertial Estimation
                   Patrick Geneva, Kevin Eckenhoff, Woosik Lee, Yulin Yang, and Guoquan Huang

   Abstract— In this paper, we present an open platform, termed          deep understanding, thus accelerating VINS research and
OpenVINS, for visual-inertial estimation research for both the           development in the field. Moreover, these systems have many
academic community and practitioners from industry. The open             hard-coded assumptions or features that require an intricate
sourced codebase provides a foundation for researchers and
engineers to quickly start developing new capabilities for their         understanding of the codebases in order to adapt them to
visual-inertial systems. This codebase has out of the box support        the sensor systems at hand. This, along with inadequate
for commonly desired visual-inertial estimation features, which          documentation and support, limits their wide adoption in
include: (i) on-manifold sliding window Kalman filter, (ii)              different applications.
online camera intrinsic and extrinsic calibration, (iii) camera
to inertial sensor time offset calibration, (iv) SLAM landmarks             To fill the aforementioned void in the community and to
with different representations and consistent First-Estimates            promote the VINS research in robotics and beyond, in this
Jacobian (FEJ) treatments, (v) modular type system for state             paper, we present an extendable, open sourced codebase that
management, (vi) extendable visual-inertial system simulator,            is particularly designed for researchers and practitioners with
and (vii) extensive toolbox for algorithm evaluation. Moreover,          either limited or extensive background knowledge of state
we have also focused on detailed documentation and theoretical
derivations to support rapid development and research, which             estimation. We provide the necessary documentation, tools,
are greatly lacked in the current open sourced algorithms.               and theory for those who are even new to visual-inertial
Finally, we perform comprehensive validation of the proposed             estimation, and term this collection of utilities as OpenVINS
OpenVINS against state-of-the-art open sourced algorithms,               (OV). This codebase has been the foundation of many of
showing its competing estimation performance.                            the recent visual-inertial estimation projects in our group at
   • Open source:                                                        the University of Delaware, which include multi-camera [9],
      https://github.com/rpng/open_vins
                                                                         multi-IMU [10], visual-inertial moving object tracking [11],
   • Documentation:
                                                                         [12], Schmidt-based visual-inertial SLAM [13], [14], point-
      https://docs.openvins.com
                                                                         plane and point-line visual-inertial navigation [15], [16],
                     I. INTRODUCTION                                     among others [17]–[19]. We summarize the key functionality
                                                                         of the different components in OpenVINS as follows:
   Autonomous robots and consumer-grade mobile devices
such as drones and smartphones are becoming ubiquitous,                    • ov core – Contains 2D image sparse visual feature
in part due to a large increase in computing ability and                     tracking; linear and Gauss-Newton feature triangulation
a simultaneous reduction in power consumption and cost.                      methods; visual-inertial simulator for arbitrary number
To endow these robots and mobile devices with the ability                    of cameras and frequencies; and fundamental manifold
to perceive and understand their contextual locations within                 math operations and utilities.
                                                                           • ov eval – Contains trajectory alignment; plotting utili-
local environments, which is desired in many different ap-
plications from mobile AR/VR to autonomous navigation,                       ties for trajectory accuracy and consistency evaluation;
visual-inertial navigation systems (VINS) are often used to                  Monte-Carlo evaluation of different accuracy metrics;
provide accurate motion estimates by fusing the data from                    and utility for recording ROS topics to file.
                                                                           • ov msckf – Contains the extendable modular Extended
on-board camera and inertial sensors [1].
   Developing a working VINS algorithm from scratch has                      Kalman Filter (EKF)-based sliding window visual-
proven to be challenging, and in the robotics research                       inertial estimator with on-manifold type system for
community, this has shown to be a significant hurdle for                     flexible state representation. Features include: First-
researchers due to the lack of VINS codebases that have                      Estimates Jacobains (FEJ) [20]–[22], IMU-camera time
comprehensive documentation and detailed derivations for                     offset calibration [23], camera intrinsics and extrinsic
which even users with little background can learn and extend                 online calibration [24], standard MSCKF [25], and 3D
a current state-of-the-art work to address their problems at                 SLAM landmarks of different representations.
hand. While there are several open sourced visual-inertial                  In what follows we describe our generalized modular
codebases [2]–[8], they are not developed for extensibility              on-manifold EKF-based estimator which, in its simplest
and lack proper documentation and evaluation tools, which,               form, estimates the current state of a camera-IMU pair. We
in our experience, are crucial for rapid development and                 then introduce the implemented features that provide the
                                                                         foundation for researchers to quickly build and extend on.
  This work was partially supported by the University of Delaware (UD)   Note that what we present here is only a brief introduction
College of Engineering, the NSF (IIS-1924897), the ARL (W911NF-19-2-
0226, JWS 10-051-003), and Google ARCore. P. Geneva was also partially   to the feature set and readers are referred to our thorough
supported by the Delaware Space Grant College and Fellowship Program     documentation website. We also provide an evaluation of
(NASA Grant NNX15AI19H).                                                 the proposed EKF-based solution in simulations and then
  The authors are with the Robot Perception and Navigation
Group (RPNG), University of Delaware, Newark, DE 19716, USA.             on real-world datasets, clearly demonstrating its competing
{pgeneva,keck,woosik,yuyang,ghuang}@udel.edu                             performance against other open sourced algorithms.

## Page 2

II. ON-MANIFOLD MODULAR EKF                                    where ˆ· denotes the estimated value and the subscript k|k −1
   The state vector of our visual-inertial system consists of           denotes the predicted estimate at time k given the mea-
the current inertial navigation state, a set of c historical IMU        surements up to time k − 1. The state covariance matrix
pose clones, a set of m environmental landmarks, and a set              is propagated typically by linearizing the nonlinear model at
of w cameras’ extrinsic and intrinsic parameters.                       the current estimate:
         h                                     i>                                 Pk|k−1 = Φk−1 Pk−1|k−1 Φ>
                                                                                                          k−1 + Qk−1                (9)
   xk = x>   I     x>
                    C     x> M    x>W
                                         C
                                            tI                    (1)
         h                                           i>                 where Φk−1 and Qk−1 are respectively the system Jacobian
    xI = IGk q̄ > G p>         G >
                                  vIk b>         b>               (2)   and discrete noise covariance matrices [25]. The clones xC ,
                         Ik                ωk     ak
         h                                                  i>          environmental features xM , and calibration xW states do not
   xC = IGk−1 q̄ > G p>                  I
                                   · · · Gk−c q̄ > G p>           (3)   evolve with time and thus the corresponding state Jacobian
                            Ik−1                       Ik−c
         h                          i>                                  entries are identity with zero propagation noise and allow for
  xM = G p>         · · · G p>                                    (4)   exploitation of the sparsity for computational savings.
                f1               fm
         h                                                     i>       B. On-Manifold Update
  xW = IC1 q̄ > C1 p>     I    ζ>        I
                                 0 · · · Cw q̄
                                               > Cw >
                                                      pI ζ > w    (5)
                                                                          Consider the following nonlinear measurement function:
where IGk q̄ is the unit quaternion parameterizing the rotation                            zm,k = h(xk ) + nm,k                   (10)
R(IGk q̄) = IGk R from the global frame of reference {G} to
                                                                        where we have the measurement noise nm,k ∼ N (0, Rm,k ).
the IMU local frame {Ik } at time k [26], bω and ba are
                                                                        For the standard EKF update, one linearizes the above
the gyroscope and accelerometer biases, and G vIk and G pIk
                                                                        equation at the current state estimate. In our case, as in
are the velocity and position of the IMU expressed in the
                                                                        the indirect EKF [26], we linearize (10) with respect to the
global frame, respectively. The inertial state xI lies on the
                                                                        current zero-mean error state (i.e. x̃ = x x̂ ∼ N (0, P)):
manifold defined by the product of the unit quaternions H
with the vector space R12 (i.e. M = H × R12 ) and has 15                          zm,k = h(x̂k|k−1  x̃k|k−1 ) + nm,k             (11)
total degrees of freedom (DOF).                                                         = h(x̂k|k−1 ) + Hk x̃k|k−1 + nm,k         (12)
   For vector variables, the “boxplus” and “boxminus” opera-
                                                                                ⇒ z̃m,k = Hk x̃k|k−1 + nm,k                       (13)
tions, which map elements to and from a given manifold [27],
equate to simple addition and subtraction of their vectors. For         where Hk is the measurement Jacobian computed as follows:
quaternions, we define the quaternion boxplus operation as:                               ∂h(x̂k|k−1  x̃k|k−1 )
                              " #
                                 δθ                                                Hk =                                           (14)
                            ∆     2                                                             ∂ x̃k|k−1
                  q̄1  δθ =          ⊗ q̄1 ≃ q̄2                (6)                                               x̃k|k−1 =0
                                  1
                                                                        Using this linearized measurement model, we can now
Note that although we have defined the orientations using               perform the following standard EKF update to ensure the
the left quaternion error, it is not limited to this and any on-        updated states remain on-manifold:
manifold representation in practice can be used (e.g., [28]).
                                                                            x̂k|k = x̂k|k−1  Kk (zm,k − h(x̂k|k−1 ))             (15)
   The map of environmental landmarks xM contains global
3D positions only for simplicity, while in practice we offer                Pk|k = Pk|k−1 − Kk Hk Pk|k−1                          (16)
support for different representations (e.g. inverse MSCKF                     Kk = Pk|k−1 H>             >
                                                                                           k (Hk Pk|k−1 Hk + Rm,k )
                                                                                                                   −1
                                                                                                                                  (17)
[25], full inverse depth [29], and anchored 3D position [30]).
   The calibration vector xW contains the camera intrinsics                    III. OPENVINS RESEARCH PLATFORM
ζ, consisting of focal length, camera center, and distortion            A. Type-based Index System
parameters, and the camera-IMU extrinsics, i.e., the spatial               At the core of the OpenVINS library is the type-based
transformation (relative pose) from the IMU to each camera.             index system. Inspired by graph-based optimization frame-
Since we consider synchronized camera clocks, we include                works such as GTSAM [32], we abstract away from the user
a single time offset C tI between the IMU and the camera                the need to directly manipulate the covariance and instead
clock in the calibration vector.                                        provide the tools to automatically manage the state and
A. Propagation                                                          its covariance. This offers many benefits such as reduced
                                                                        implementation time and being less prone to development
   The inertial state xI is propagated forward using incoming           errors due to explicit state and covariance access.
IMU measurements of linear accelerations I am and angular                  Each state variable “type” has internally the location of
velocities I ωm based on the following generic nonlinear                where it is in the error state which is automatically updated
IMU kinematics propagating the state from timestep k − 1                during initialization, cloning, or marginalization operations
to k [31]:                                                              which affect variable ordering. A type is defined by its
                  xk = f (xk−1 , I am , I ωm , n)                (7)    covariance location, its current estimate and its error state
                                                                        size. The current value does not have to be a vector, but could
where n contains the zero-mean white Gaussian noise of the
                                                                        be a matrix in the case of an SO(3) rotation representation.
IMU measurements along with random walk bias noise. This
                                                                        The error state for all types is a vector and thus a type will
state estimate is evaluated at the current estimate:
                                                                        need to define the boxplus mapping between its error state
             x̂k|k−1 = f (x̂k−1|k−1 , I am , I ωm , 0)           (8)    and its manifold representation (i.e. the update function).

## Page 3

c l a s s Type {                                                           C. Landmark Update
protected :
    / / Current best estimate                                                 We generalize the landmark measurement model as a
    E i g e n : : MatrixXd v a l u e ;                                     series of nested functions to encompass different feature
    / / Index of error s t a t e in covariance                             parameterizations such as 3D position and inverse depth and
    i n t i d = −1;                                                        so on. Assuming a visual feature that has been tracked over
    / / Dimension o f e r r o r s t a t e                                  the sliding window of stochastic clones [35], we can write
    i n t s i z e = −1;
    / / V e c t o r c o r r e c t i o n , how t o u p d a t e              the visual-bearing measurements (i.e., pixel coordinates) as
    v o i d u p d a t e ( c o n s t E i g e n : : VectorXd dx ) ;          the following series of nested functions:
};
                                                                             zm,k = h(xk ) + nm,k                                        (23)
   One of the main advantages of this type system is that it                      = hd (zn,k , ζ) + nm,k                                 (24)
reduces the complexity of adding new features by allowing
                                                                                   = hd (hp (Ck pf ), ζ) + nm,k                          (25)
the user to construct sparse Jacobians. Instead of constructing
                                                                                                 G          Ck   G
a Jacobian for all state elements, the “sparse” Jacobian needs                     = hd (hp (ht ( pf ,      G R,   pCk )),   ζ) + nm,k   (26)
to only include the state elements that the measurement is a               where zm,k is the raw uv pixel coordinate; nm,k the raw pixel
function of. This both saves computation in the cases where                noise and typically assumed to be zero-mean white Gaussian;
a measurement is a function of only a few state elements                   zn,k is the normalized undistorted uv measurement; Ck pf is
and allows for measurement functions to be state agnostic                  the landmark position in the current camera frame; G pf is
as long as their involved state variables are present.                     the landmark position in the global frame and depending on
B. State Variable Initialization                                           its representation may also be a function of state elements;
                                                                           and {C      G
                                                                                 G R, pCk } denotes the current camera pose (position
                                                                                   k

   Based on a set of linearized measurement equations (13),                and orientation) in the global frame.
we aim to optimally compute the initial estimate of a new                     The measurement functions hd , hp , and ht correspond to
state variable and its covariance and correlations with the                the intrinsic distortion, projection, and transformation func-
existing state variables. As a motivating example, we here                 tions and the corresponding measurement Jacobians can be
describe how to initialize a new SLAM landmark G pf ,                      computed through a simple chain rule. Note that we compute
whose key logic can be used for any new state variable and                 the errors on the raw uv pixels to allow for calibration of the
is generalized to any type within the codebase. As in [33] we              camera intrinsics ζ and that the function hd can be changed
first perform QR decomposition (e.g., using computationally                to support any camera model (e.g., radial-tangential and
efficient in-place Givens rotations) to separate the linear                equidistant). We refer readers to the documentation website
system (13) into two subsystems: (i) one that depends on                   for the details of these measurement functions.
the new state (i.e., G pf ), and (ii) the other that does not.
                      h
                                   "
                                 i x̃
                                           #                               D. Online Calibration
                                        k
              z̃m,k = Hx Hf G                + nm,k         (18)              We perform online spatiotemporal calibration of the
                                       p̃f                                 camera-IMU time offset and extrinsic transformation, and
         "        # "               #"        # "      #
           z̃m1,k       Hx1 Hf 1         x̃k      nf 1                     camera intrinsics. Looking at the landmark measure-
      ⇒             =                   G
                                               +            (19)           ment (26), one can simply take the derivative with respect
           z̃m2,k       Hx2     0         p̃f     nf 2
                                                                           to the desired variables that they wish to calibrate online. In
where nf i ∼ N (0, Rf i ), i ∈ {1, 2}. Note that in the above              this case we will have additional Jacobians for the intrinsic ζ
                                                                                                     C
expression z̃m1,k and z̃m2,k are orthonormally transformed                 in function hd and {CI R, pI } extrinsics that the global pose
                                                                            Ck     G
measurement residuals, not the direct partitions of z̃m,k . With           {G R, pCk } is a function of. For derivations and Jacobian
the top transformed linearized measurement residual z̃m1,k                 results, we refer the reader to our documentation.
in (19), we now perform efficient EKF update to initialize                    We also co-estimate the time offset between the camera
the state estimate of G p̂f and its covariance and correlations            and IMU, which can commonly exist in low-cost devices due
to xk [see (15)], which will then be augmented to the current              to sensor latency, clock skew, or data transmission delays.
state and covariance matrix.                                               Consider the time C t as expressed in the camera clock is
                                                                           related to the same instant represented in the IMU clock, I t,
            G
                p̂f = G p̂f  H−1
                               f 1 z̃m1,k                           (20)   by a time offset C tI :
                              −>
            Pxf = −Pk H>  x1 Hf 1                                   (21)                             I
                                                                                                         t = C t + C tI                  (27)
            Pf f = H−1            >          −>
                    f 1 (Hx1 Pk Hx1 + Rf 1 )Hf 1                    (22)
                                                                           This offset is unknown and estimated online. We refer the
It should be noted that a full-rank Hf 1 is needed to perform              reader to [23] for further details.
the above initialization, which normally is the case if enough
measurements are collected (i.e., delayed initialization). Note            E. Codebase Documentation
also that to utilize all available measurement information,                   It is our belief that the documentation of this work in itself
we also perform EKF update using the bottom measurement                    is one of the main contributions to the research community.
residual z̃m2,k in (19), which essentially is equivalent to the            Both researchers and practitioners with little background in
Multi-State Constraint Kalman Filter (MSCKF) [25] update                   estimation may struggle to grasp the core theoretical concepts
with nullspace projection [34].                                            and important implementation details when it comes to

## Page 4

visual-inertial estimation algorithms. To bridge this gap the   our cubic B-spline. To obtain the true measurements from
documentation of this codebase takes as much of a priority as   our SE(3) B-spline we can do the following:
new features that could improve the estimation performance.                            
                                                                                                  >G
                                                                                                             
As compared to existing open sourced systems with limited
                                                                           I
                                                                             ω(t) = vee GI R(u(t)) I Ṙ(u(t))        (31)
documentation, we focus on providing additional dedicated                      I
                                                                                   a(t) = G         >G
                                                                                          I R(u(t))    p̈I (u(t))                       (32)
derivation pages on how different parts of the code are
derived and interact. The in-code and page documentation        where vee(·) returns the vector portion of the skew-
is automatically generated from the codebase using Doxygen      symmetric matrix. These are then corrupted using the random
[36] which is then post-processed using m.css [37] to provide   walk biases and corresponding white noises.
high quality search functionality and mobile friendly layout.   C. Visual-Bearing Measurement
This tight-coupling of our documentation and derivations
within the codebase also ensures that the documentation is         After creating the B-spline trajectory we generate envi-
up to date and that developers can easily find answers.         ronmental landmarks that can be later projected into the
                                                                synthetic camera frames. To generate these landmarks, we
        IV. VISUAL-INERTIAL SIMULATOR                           increment along the spline at a fixed interval and ensure that
                                                                all cameras see enough landmarks in the map. If there are not
  We now detail how our simulator generates visual-inertial
                                                                enough landmarks in the given camera frame, we generate
measurements. We note that this simulator can be easily
                                                                new landmarks by sending out random rays from the camera
extended to include other measurements besides the inertial
                                                                and assigning a random depth. Landmarks are then added to
and visual-bearing measurements presented below.
                                                                the map so that they can be projected into future frames. We
A. B-Spline Interpolation                                       generate landmarks’ visual measurements by projecting them
                                                                into the current frame. Projected landmarks are limited to
                                                                being within the field of view, in front, and close in distance
                            fSg   fi+1g
         fi-1g        fig                                       to the camera. Pixel noise can be directly added to the true
                                              fi+2g             pixel values.
                                                                                         V. BENCHMARKS
                 u           u            u
                                                                A. Simulation Results
Fig. 1: Illustrate the B-spline interpolation to a pose G
                                                        ST         With the proposed visual-inertial simulator, we evaluate
which is bounded by four control poses.                         the proposed online calibration and the consistency of our
   At the center of the simulator is an SE(3) B-spline          MSCKF estimator, which is implemented based on the First
which allows for the calculation of the pose, velocity, and     Estimate Jacobians (FEJ)-EKF [21], [22]. In particular, the
accelerations at any given timestep along a given trajectory.   system is run with a monocular camera, a window size
We follow the work of Patron-Perez et al. [38] and Mueggler     of 11, a maximum of 100 feature tracks per frame, and
et al. [39] in which given a series of temporally uniformly     a maximum of 50 SLAM landmarks kept in the state,1
distributed “control point” poses, the pose {S} at a given      along with VIO feature tracks that are processed by the
timestep ts can be interpolated by:                             MSCKF update. The camera is simulated at 10Hz while
                                                                the IMU is simulated at 400Hz. We inject one pixel noise
           G             G
           S T(u(ts )) = i−1 T A0 A1 A2                 (28)    and the IMU noise characteristics of an ADIS16448 MEMS
                                                                IMU. To simulate bad initial calibration values, we randomly
                                            
                   Aj = exp Bj (u(t)) i−1+j
                                        i+j Ω           (29)
                                                              initialize the calibration values using the prior distribution
                 i−1
                     Ω = log G     −1 G                         values of the estimator. This ensures that during Monte-Carlo
                 i            i−1 T   i T               (30)
                                                                simulation we have both different measurement noises and
where Bj (u(t)) are our spline interpolation constants,         initial calibration values for each run.
exp(·), log(·) are the SE(3) matrix exponential and log-           As summarized in Table I, the average Absolute Trajec-
arithm, and the frame notations are shown in Figure 1.          tory Error (ATE) and Normalized Estimation Error Squared
Equation (28) can be interpreted as compounding the fraction    (NEES) for each different scenario shows that when perform-
portions of the bounding poses to the first pose G  i−1 T. It
                                                                ing online calibration, estimation accuracy does not degrade
is then simple to take the time derivative to allow the         if we are given the true calibration; while in the case that we
computation of the velocity and acceleration at any point.      have bad initial guesses, the estimator remains consistent and
The only needed input into the simulator is a pose trajectory   is able to estimate with reasonable accuracy. A representative
which we uniformly sample to construct control points for       run with uncertainty bounds is shown in Figure 3. When
the B-spline. This B-spline is then used to both generate       calibration is disabled and a bad initial guess is used, the
the inertial measurements while also providing the pose         NEES becomes large due to not modeling the uncertainty
information needed to generate visual-bearing measurements.     that these calibration parameters have, and in many cases
                                                                the estimate diverges. We also plot the first ten and sixty
B. Inertial Measurements
                                                                   1 This is a little abuse of terminology. SLAM landmarks refer to the visual
  To incorporate inertial measurements from an IMU sensor,      features that can be tracked beyond the current window, kept in the state
we can leverage the continuous nature and C 2 -continuity of    vector, and marginalized out when lost [40].

## Page 5

Fig. 2: Camera intrinsic projection and distortion along with extrinsic orientation and positions parameters error (blue-solid)
and 3σ bounds (red-dashed) for a representative run. Note that we only plot the first sixty seconds of the dataset.
                                                                 TABLE I: Average ATE and NEES over twenty runs with
                                                                 true or bad calibration, with and without online calibration.

                                                                                   ATE (deg)   ATE (m)   Ori. NEES   Pos. NEES
                                                                   true w/ calib     0.212      0.134      2.203      1.880
                                                                  true w/o calib     0.200      0.128      2.265      1.909
                                                                   bad w/ calib      0.218      0.139      2.235      2.007
                                                                  bad w/o calib      5.432     508.719     9.159     1045.174




                                                                 uate the following state-of-the-art visual-inertial estimation
Fig. 3: IMU pose errors (blue-solid) and 3σ bounds (red-         algorithms:
dashed) for a representative run of the proposed method with
                                                                 OKVIS [2] – Keyframe-based fixed-lag smoother which
SLAM landmarks and online calibration.
                                                                   optimizes arbitrarily spaced keyframe poses connected
                                                                   with inertial measurement factors and environmental land-
                                                                   marks. A fixed window size was enforced to ensure com-
                                                                   putational feasibility with the focus on selective marginal-
                                                                   ization to allow for problem sparsity.
                                                                 VINS-Fusion VIO [3] – Extension of the original VINS-
                                                                   Mono [42] sliding optimization-based method that lever-
                                                                   ages IMU preintegration which is then loosely coupled
Fig. 4: Camera to IMU time offset error (blue-solid) and 3σ        with a secondary pose-graph optimization. VINS-Fusion
bounds (red-dashed) for a representative run.                      extends the original codebase to support stereo cameras.
                                                                 Basalt VIO [4] – Stereo keyframe-based fix-lag smoother
seconds of all calibration parameters of a representative run      with custom feature tracking frontend with focus on ex-
in Figures 2 and 4, showing that these parameters rapidly          tracting relevant information from the VIO for later offline
converge from their initially poor guesses.                        visual-inertial mapping.
                                                                 R-VIO [5] – Robocentric MSCKF-based algorithm which
B. Real-World Comparison                                           estimates in a local frame and updates the global frame
   We evaluate the proposed visual-inertial FEJ-MSCKF esti-        through a composition step. The direction of gravity is
mator with and without SLAM landmarks on the Vicon room            also estimated within the filter.
scenarios from the EurocMav dataset [41] which provides          ROVIO [6] – We use the ROVIO implementation within
both 20Hz stereo images, 200Hz ADIS16448 MEMS IMU                  maplab [43], which is a monocular iterative EKF-based
measurements, and optimized groundtruth trajectories. It           approach that performs minimization on the direct image
should be noted that we have recalculated the V1 01 easy           intensity patches allowing for tracking of non-corner fea-
groundtruth due to the original having incorrect orientation       tures such as high gradient lines.
values and have provided this corrected groundtruth trajec-      ICE-BA [7] – Stereo incremental bundle adjustment (BA)
tory to the community on our documentation website. All            method which optimizes both a local siding window and
methods were run with the configuration files from their open      global optimization problem in parallel. They exploited the
sourced repositories with each algorithm being run ten times       sparseness of their formulation and introduced a relative
on each dataset to compensate for some randomness inherent         marginalization procedure.
to the visual front-ends. In this benchmarking test, we eval-    S-MSCKF [8] – An open sourced implementation of original

## Page 6

TABLE II: Ten runs mean absolute trajectory error (ATE) for each algorithm in units of degree/meters. Note that V2 03
dataset is excluded due the inability for some algorithms to run on it. Green denotes the best, while blue is second best.

                                       V1 01 easy         V1 02 medium      V1 03 difficult    V2 01 easy     V2 02 medium           Average
               mono ov slam            0.699 / 0.058      1.675 / 0.076     2.542 / 0.063     0.773 / 0.124     1.538 / 0.074      1.445 / 0.079
                mono ov vio            0.642 / 0.076      1.766 / 0.096     2.391 / 0.344     1.164 / 0.121     1.248 / 0.106      1.442 / 0.148
                 mono okvis            0.823 / 0.090      2.082 / 0.146     4.122 / 0.222     0.826 / 0.117     1.704 / 0.197      1.911 / 0.154
                mono rovioli           2.249 / 0.153      1.635 / 0.131     3.253 / 0.158     1.455 / 0.106     1.678 / 0.153      2.054 / 0.140
                   mono rvio           0.994 / 0.094      2.288 / 0.129     1.757 / 0.147     1.735 / 0.144     1.690 / 0.233      1.693 / 0.149
          mono vinsfusion vio          1.199 / 0.064      3.542 / 0.103     5.934 / 0.202     1.585 / 0.073     2.370 / 0.079      2.926 / 0.104
                 stereo ov slam        0.856 / 0.061      1.813 / 0.047     2.764 / 0.059     1.037 / 0.056     1.292 / 0.047      1.552 / 0.054
                   stereo ov vio       0.905 / 0.061      1.767 / 0.056     2.339 / 0.057     1.106 / 0.053     1.151 / 0.048      1.454 / 0.055
                    stereo basalt      0.654 / 0.035      2.067 / 0.059     2.017 / 0.085     0.981 / 0.046     0.888 / 0.059      1.321 / 0.057
                     stereo iceba      0.909 / 0.059      2.574 / 0.120     3.206 / 0.137     1.819 / 0.128     1.212 / 0.116      1.944 / 0.112
                    stereo okvis       0.603 / 0.039      1.963 / 0.079     4.117 / 0.122     0.834 / 0.075     1.201 / 0.092      1.744 / 0.081
                  stereo smsckf        1.108 / 0.086      2.147 / 0.121     3.918 / 0.198     1.181 / 0.083     2.142 / 0.164      2.099 / 0.130
          stereo vinsfusion vio        1.073 / 0.054      2.695 / 0.089     3.643 / 0.132     2.499 / 0.071     2.006 / 0.074      2.383 / 0.084


TABLE III: Relative pose error (RPE) for different segment lengths for each algorithm variation over all datasets in units
of degree/meters. Note that V2 03 dataset is excluded due the inability for some algorithms to run on it.

                                               8m               16m              24m              32m             40m               48m
                  mono ov slam            0.661 / 0.074     0.802 / 0.086   0.979 / 0.097     1.061 / 0.105   1.145 / 0.120     1.289 / 0.122
                   mono ov vio            0.826 / 0.094     1.039 / 0.106   1.215 / 0.111     1.283 / 0.132   1.342 / 0.151     1.425 / 0.184
                    mono okvis            0.662 / 0.107     0.870 / 0.161   1.031 / 0.190     1.225 / 0.213   1.384 / 0.240     1.603 / 0.251
                   mono rovioli           1.136 / 0.095     1.585 / 0.135   1.847 / 0.184     2.078 / 0.226   2.218 / 0.263     2.402 / 0.295
                      mono rvio           0.705 / 0.130     0.902 / 0.160   1.029 / 0.183     1.074 / 0.213   0.991 / 0.227     1.077 / 0.232
             mono vinsfusion vio          0.940 / 0.070     1.298 / 0.103   1.680 / 0.118     1.822 / 0.146   1.833 / 0.153     1.860 / 0.171
                    stereo ov slam        0.685 / 0.069     0.876 / 0.080   1.064 / 0.087     1.169 / 0.087   1.275 / 0.098     1.488 / 0.105
                      stereo ov vio       0.722 / 0.068     0.892 / 0.077   1.089 / 0.087     1.218 / 0.088   1.342 / 0.101     1.489 / 0.106
                       stereo basalt      0.538 / 0.063     0.576 / 0.070   0.649 / 0.078     0.715 / 0.086   0.647 / 0.097     0.758 / 0.111
                        stereo iceba      0.955 / 0.096     1.227 / 0.114   1.415 / 0.120     1.658 / 0.152   1.856 / 0.173     1.803 / 0.180
                       stereo okvis       0.611 / 0.066     0.772 / 0.089   0.916 / 0.103     1.089 / 0.119   1.173 / 0.136     1.404 / 0.141
                     stereo smsckf        1.084 / 0.098     1.462 / 0.136   1.578 / 0.159     1.667 / 0.187   1.901 / 0.200     2.134 / 0.217
             stereo vinsfusion vio        0.946 / 0.057     1.357 / 0.079   1.721 / 0.097     1.928 / 0.111   1.935 / 0.125     1.805 / 0.132



  MSCKF [25] paper with stereo feature tracking and a                            for our monocular SLAM/VIO, and stereo SLAM/VIO,
  focus on high-speed motion scenarios.                                          respectively, on an Intel(R) Xeon(R) CPU E3-1505M v6 @
Note that we evaluate only the VIO portion of these code-                        3.00GHz processor in single threaded execution.
bases (i.e., not the non-realtime backend pose graph thread                             VI. CONCLUSION AND FUTURE WORK
output of VINS-Fusion [3] and visual-inertial mapping of
                                                                                    In this paper we have presented our OpenVINS (OV)
Basalt [4]), as one could simply append a pose graph
                                                                                 system as a platform for the research community. At the core
optimizer after any of these odometry methods to improve
                                                                                 we provide the visual processing frontend, full visual-inertial
long-term accuracy.
                                                                                 simulator, and modular on-manifold EKF. In particular, we
   Table II shows the average ATE of all methods for each
                                                                                 have implemented the FEJ-based MSCKF with and without
dataset. It is clear that the addition of SLAM landmarks in
                                                                                 SLAM landmarks and demonstrated the competing perfor-
our OpenVINS greatly reduces the drift in the monocular
                                                                                 mance of our estimator. We have heavily documented the
case, while it has a smaller impact on the stereo performance;
                                                                                 project to allow for researchers and practitioners to quickly
and more importantly, OpenVINS is able to perform com-
                                                                                 build on top of this work with minimal estimation theory
petitively to other methods. We additionally compared the
                                                                                 background. In the future we plan to expand our system
Relative Pose Error (RPE) of all methods. Shown in Table
                                                                                 to provide a sliding window optimization-based estimator
III, our monocular system clearly outperforms the current
                                                                                 leveraging our closed-form preintegration [45]. We are also
open sourced codebases, with our stereo system being able
                                                                                 interested in integrating visual-inertial mapping and percep-
to perform second to Basalt. While we did not evaluate per-
                                                                                 tion capabilities into OpenVINS.
frame timing rigorously, we found that Basalt outperformed
all other algorithms, with our proposed method being limited
by the visual-frontend implementation from OpenCV [44]
and SLAM feature update equally. On the first EurocMav
dataset we could process at 2.7x/4.3x and 1.2x/1.9x realtime

## Page 7

R EFERENCES                                        [23] M. Li and A. I. Mourikis, “Online temporal calibration for Camera-
                                                                                     IMU systems: Theory and algorithms,” International Journal of
 [1] G. Huang, “Visual-inertial navigation: A concise review,” in Proc.              Robotics Research, vol. 33, no. 7, pp. 947–964, June 2014.
     International Conference on Robotics and Automation, Montreal,             [24] M. Li, H. Yu, X. Zheng, and A. I. Mourikis, “High-fidelity sensor
     Canada, May 2019.                                                               modeling and self-calibration in vision-aided inertial navigation,” in
 [2] S. Leutenegger, S. Lynen, M. Bosse, R. Siegwart, and P. Furgale,                IEEE International Conference on Robotics and Automation (ICRA),
     “Keyframe-based visual-inertial odometry using nonlinear optimiza-              May 2014, pp. 409–416.
     tion,” International Journal of Robotics Research, vol. 34, no. 3, pp.     [25] A. I. Mourikis and S. I. Roumeliotis, “A multi-state constraint Kalman
     314–334, 2015.                                                                  filter for vision-aided inertial navigation,” in Proceedings of the IEEE
                                                                                     International Conference on Robotics and Automation, Rome, Italy,
 [3] T. Qin, J. Pan, S. Cao, and S. Shen, “A general optimization-based
                                                                                     Apr. 10–14, 2007, pp. 3565–3572.
     framework for local odometry estimation with multiple sensors,”
                                                                                [26] N. Trawny and S. I. Roumeliotis, “Indirect Kalman filter for 3D
     CoRR, vol. abs/1901.03638, 2019.
                                                                                     attitude estimation,” University of Minnesota, Dept. of Comp. Sci.
 [4] V. C. Usenko, N. Demmel, D. Schubert, J. Stückler, and D. Cremers,             & Eng., Tech. Rep., Mar. 2005.
     “Visual-inertial mapping with non-linear factor recovery,” CoRR, vol.      [27] C. Hertzberg, R. Wagner, U. Frese, and L. Schröder, “Integrating
     abs/1904.06504, 2019.                                                           generic sensor fusion algorithms with sound state representations
 [5] Z. Huai and G. Huang, “Robocentric visual-inertial odometry,” Inter-            through encapsulation of manifolds,” Information Fusion, vol. 14,
     national Journal of Robotics Research, Apr. 2019, (to appear).                  no. 1, pp. 57–77, 2013.
 [6] M. Bloesch, M. Burri, S. Omari, M. Hutter, and R. Siegwart, “Iterated      [28] K. Wu, T. Zhang, D. Su, S. Huang, and G. Dissanayake, “An
     extended kalman filter based visual-inertial odometry using direct pho-         invariant-ekf vins algorithm for improving consistency,” in Proc. of the
     tometric feedback,” The International Journal of Robotics Research,             IEEE/RSJ International Conference on Intelligent Robots and Systems,
     vol. 36, no. 10, pp. 1053–1072, 2017.                                           Sept 2017, pp. 1578–1585.
 [7] H. Liu, M. Chen, G. Zhang, H. Bao, and Y. Bao, “Ice-ba: Incremental,       [29] J. Civera, A. Davison, and J. Montiel, “Inverse depth parametrization
     consistent and efficient bundle adjustment for visual-inertial slam,” in        for monocular SLAM,” IEEE Transactions on Robotics, vol. 24, no. 5,
     Proceedings of the IEEE Conference on Computer Vision and Pattern               pp. 932–945, Oct. 2008.
     Recognition, 2018, pp. 1974–1982.                                          [30] M. K. Paul, K. Wu, J. A. Hesch, E. D. Nerurkar, and S. I. Roumeliotis,
 [8] K. Sun, K. Mohta, B. Pfrommer, M. Watterson, S. Liu, Y. Mulgaonkar,             “A comparative analysis of tightly-coupled monocular, binocular, and
     C. J. Taylor, and V. Kumar, “Robust stereo visual inertial odometry             stereo VINS,” in Proc. of the IEEE International Conference on
     for fast autonomous flight,” IEEE Robotics and Automation Letters,              Robotics and Automation, Singapore, July 2017, pp. 165–172.
     vol. 3, no. 2, pp. 965–972, April 2018.                                    [31] A. B. Chatfield, Fundamentals of High Accuracy Inertial Navigation.
 [9] K. Eckenhoff, P. Geneva, J. Bloecker, and G. Huang, “Multi-camera               AIAA, 1997.
     visual-inertial navigation with online intrinsic and extrinsic calibra-    [32] F. Dellaert, “Factor graphs and gtsam: A hands-on introduction,”
     tion,” in Proc. International Conference on Robotics and Automation,            Georgia Institute of Technology, Tech. Rep., 2012.
     Montreal, Canada, May 2019.                                                [33] M. Li, “Visual-inertial odometry on resource-constrained systems,”
[10] K. Eckenhoff, P. Geneva, and G. Huang, “Sensor-failure-resilient                Ph.D. dissertation, UC Riverside, 2014.
     multi-imu visual-inertial navigation,” in Proc. International Confer-      [34] Y. Yang, J. Maley, and G. Huang, “Null-space-based marginalization:
     ence on Robotics and Automation, Montreal, Canada, May 2019.                    Analysis and algorithm,” in Proc. IEEE/RSJ International Conference
[11] K. Eckenhoff, Y. Yang, P. Geneva, and G. Huang, “Tightly-coupled                on Intelligent Robots and Systems, Vancouver, Canada, Sept. 24-28,
     visual-inertial localization and 3D rigid-body target tracking,” IEEE           2017, pp. 6749–6755.
     Robotics and Automation Letters (RA-L), vol. 4, no. 2, pp. 1541–1548,      [35] S. I. Roumeliotis and J. W. Burdick, “Stochastic cloning: A generalized
     2019.                                                                           framework for processing relative state measurements,” in Proceedings
[12] K. Eckenhoff, P. Geneva, N. Merrill, and G. Huang, “Schmidt-ekf-                of the IEEE International Conference on Robotics and Automation,
     based visual-inertial moving object tracking,” in Proc. of the IEEE             Washington, DC, May 11-15, 2002, pp. 1788–1795.
     International Conference on Robotics and Automation, Paris, France,        [36] D. Van Heesch, “Doxygen: Source code documentation generator
     2020.                                                                           tool,” URL: http:// www.doxygen.org, 2008.
[13] P. Geneva, K. Eckenhoff, and G. Huang, “A linear-complexity EKF for        [37] V. Vondruš, “m.css: A no-nonsense, no-javascript css framework
     visual-inertial navigation with loop closures,” in Proc. International          and pelican theme for content-oriented websites,” URL: https:// mcss.
     Conference on Robotics and Automation, Montreal, Canada, May                    mosra.cz/ , 2018.
     2019.                                                                      [38] A. Patron-Perez, S. Lovegrove, and G. Sibley, “A spline-based tra-
[14] P. Geneva, J. Maley, and G. Huang, “An efficient schmidt-ekf for 3D             jectory representation for sensor fusion and rolling shutter cameras,”
     visual-inertial SLAM,” in Proc. Conference on Computer Vision and               International Journal of Computer Vision, vol. 113, no. 3, pp. 208–
     Pattern Recognition (CVPR), Long Beach, CA, June 2019, (accepted).              219, 2015.
[15] Y. Yang, P. Geneva, X. Zuo, K. Eckenhoff, Y. Liu, and G. Huang,            [39] E. Mueggler, G. Gallego, H. Rebecq, and D. Scaramuzza,
     “Tightly-coupled aided inertial navigation with point and plane fea-            “Continuous-time visual-inertial odometry for event cameras,” IEEE
     tures,” in Proc. International Conference on Robotics and Automation,           Transactions on Robotics, pp. 1–16, 2018.
     Montreal, Canada, May 2019.                                                [40] M. Li and A. I. Mourikis, “Optimization-based estimator design for
[16] Y. Yang, P. Geneva, K. Eckenhoff, and G. Huang, “Visual-inertial                vision-aided inertial navigation,” in Robotics: Science and Systems,
     navigation with point and line features,” Macau, China, Nov. 2019,              Berlin, Germany, June 2013, pp. 241–248.
     (accepted).                                                                [41] M. Burri, J. Nikolic, P. Gohl, T. Schneider, J. Rehder, S. Omari, M. W.
[17] X. Zuo, P. Geneva, W. Lee, Y. Liu, and G. Huang, “LIC-Fusion: Lidar-            Achtelik, and R. Siegwart, “The euroc micro aerial vehicle datasets,”
     inertial-camera odometry,” Macau, China, Nov. 2019, (accepted).                 The International Journal of Robotics Research, vol. 35, no. 10, pp.
                                                                                     1157–1163, 2016.
[18] X. Zuo, P. Geneva, Y. Yang, W. Ye, Y. Liu, and G. Huang, “Visual-
                                                                                [42] T. Qin, P. Li, and S. Shen, “VINS-Mono: A robust and versa-
     inertial localization with prior lidar map constraints,” IEEE Robotics
                                                                                     tile monocular visual-inertial state estimator,” IEEE Transactions on
     and Automation Letters (RA-L), 2019, (to appear).
                                                                                     Robotics, vol. 34, no. 4, pp. 1004–1020, 2018.
[19] Y. Yang, P. Geneva, K. Eckenhoff, and G. Huang, “Degenerate motion         [43] T. Schneider, M. Dymczyk, M. Fehr, K. Egger, S. Lynen, I. Gilitschen-
     analysis for aided INS with online spatial and temporal calibration,”           ski, and R. Siegwart, “Maplab: An open framework for research in
     IEEE Robotics and Automation Letters (RA-L), vol. 4, no. 2, pp. 2070–           visual-inertial mapping and localization,” IEEE Robotics and Automa-
     2077, 2019.                                                                     tion Letters, vol. 3, no. 3, pp. 1418–1425, July 2018.
[20] G. Huang, A. I. Mourikis, and S. I. Roumeliotis, “Analysis and             [44] OpenCV Developers Team, “Open source computer vision (OpenCV)
     improvement of the consistency of extended Kalman filter-based                  library,” Available: http://opencv.org.
     SLAM,” in Proc. of the IEEE International Conference on Robotics           [45] K. Eckenhoff, P. Geneva, and G. Huang, “Closed-form preintegra-
     and Automation, Pasadena, CA, May 19-23 2008, pp. 473–479.                      tion methods for graph-based visual-inertial navigation,” International
[21] ——, “A first-estimates Jacobian EKF for improving SLAM consis-                  Journal of Robotics Research, vol. 38, no. 5, pp. 563–586, 2019.
     tency,” in Proc. of the 11th International Symposium on Experimental
     Robotics, Athens, Greece, July 14–17, 2008.
[22] ——, “Observability-based rules for designing consistent EKF SLAM
     estimators,” International Journal of Robotics Research, vol. 29, no. 5,
     pp. 502–528, Apr. 2010.
