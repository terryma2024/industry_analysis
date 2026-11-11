---
source_id: "SRC-robotics-681"
title: "VLK paper v1 PDF supplementary extraction"
source_type: "paper"
publisher: "Wang et al."
source_date: "2026-06-29"
url: "https://arxiv.org/pdf/2606.30645v1"
evidence_grade: "S"
capture_method: "pdf-extract-pdftotext"
captured_at: "2026-11-10T01:36:22+00:00"
pdf_file: "raw/robotics-embodied-ai/documents/SRC-robotics-681-vlk-paper-v1.pdf"
page_count: "19"
tags:
  - raw/source
  - raw/pdf
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-681
---
# VLK paper v1 PDF supplementary extraction

## Page 1

VLK: Learning Humanoid Loco-Manipulation from
                                            Synthetic Interactions in Reconstructed Scenes
                                                   Yen-Jen Wang∗,1,2 , Jiaman Li∗,‡,1 , Sirui Chen§,1,3 , Takara E. Truong§,1,3 , Pei Xu§,1
                                                    Pieter Abbeel†,1,2 , Rocky Duan†,1 , Koushil Sreenath†,1,2 , Angjoo Kanazawa†,1,2
                                                               Carmelo Sferrazza†,1 , Guanya Shi†,1,4 , C. Karen Liu†,1,3
                                                   1                                2                           3                                           4
                                                       Amazon FAR                       UC Berkeley                 Stanford University                         Carnegie Mellon University

                                                                Large-Scale Synthetic Data Generation                                                   Zero-Shot Real-World Deployment




arXiv:2606.30645v1 [cs.RO] 29 Jun 2026
                                                                                A        B                  C                                                       A                     C




                                                                                                                                                                        B




                                          A Pick up the box from the desk                                                    A Walk toward the white desk
                                          B Walk toward the white sofa                                                       B Pick up the box from the floor
                                          C Carry the box while walking                                                      C Put down the box on the table


                                                                                          Real-Time Interactive Language Prompt for Real-World Deployment




                                                                                                                                                       4




                                                                                                        3                                                       5



                                                                                             2
                                                                            1                                                              6




                                         Figure 1:      Synthetic interactions in reconstructed scenes enable real-world perception-based loco-
                                         manipulation. Synthetic data generation produces paired egocentric observations, task instructions, and G1
                                         kinematic trajectories for VLK training. Top: A–C show atomic prompt-conditioned skills generated in re-
                                         constructed scenes (left) and executed on the physical G1 in the real world (right). Bottom: long-horizon
                                         real-world behavior is produced by chaining atomic prompts; markers 1–6 indicate successive stages for pick-
                                         ing, placing, and navigation. Project Website: https://vision-language-kinematics.github.io.
                                                           Abstract: Perception-based humanoid loco-manipulation requires connecting
                                                           egocentric observations and task instructions to whole-body motion. Learning
                                                           this mapping requires synchronized egocentric images, language commands, and
                                                           robot-compatible kinematic trajectories, yet no existing data source provides this
                                                           complete tuple at scale. We address this bottleneck by generating vision-language-
                                                           kinematics (VLK) supervision synthetically in reconstructed scenes. Our pipeline
                                                           leverages 3D Gaussian Splatting to reconstruct metric-scale indoor environments,
                                                           synthesizes navigation and object-interaction trajectories using privileged scene
                                                           information, and renders paired egocentric observations after the fact. We pro-
                                                           duce 48,000 paired trajectories with no human intervention and train a VLK pol-
                                                           icy that predicts short-horizon whole-body kinematic trajectories. A whole-body
                                                           tracker converts these predictions into actions on the physical humanoid. We eval-
                                               ∗
                                                   Co-first authors. ‡ Project lead. § Equal contribution. † Amazon FAR Team Co-Lead.

## Page 2

uate on the physical Unitree G1 performing navigation and single-object transport,
         demonstrating that synthesized interactions in reconstructed scenes provide effec-
         tive supervision for sim-to-real perception-based humanoid loco-manipulation.

         Keywords: Vision-Language-Kinematics, Humanoid Loco-Manipulation, Scene-
         Grounded Synthetic Data, Sim-to-Real Transfer

1   Introduction
Connecting egocentric observations to whole-body action is a fundamental challenge for humanoid
robots operating in human-centered environments. A humanoid must perceive the world from its
own viewpoint, identify task-relevant objects, navigate toward them, and physically interact with
them through coordinated full-body motion. This perception-to-action loop, which humans exe-
cute effortlessly in everyday settings, requires a policy that maps high-dimensional visual input and
language instructions to whole-body kinematic behavior.
Learning such a policy requires paired data: synchronized egocentric observations, task instructions,
and robot-compatible whole-body trajectories. Prior work has explored several paths to obtain this
supervision, each with significant limitations. Real-world teleoperation systems [1, 2] can produce
high-quality paired demonstrations, but collecting full-body data remains expensive and difficult to
scale across diverse scenes, objects, and interaction types. Human motion-capture datasets offer
rich whole-body references that can be retargeted to humanoid morphologies, but they lack the
corresponding robot egocentric observations. Egocentric video datasets provide abundant visual
experience, but are not paired with robot-compatible kinematics or actions. No single existing source
provides the complete tuple — vision, language, and whole-body kinematics — needed for scalable
policy learning.
Can we overcome this data bottleneck by generating paired supervision synthetically? Doing so
requires two ingredients: synthetic world assets that are visually realistic and diverse, and synthetic
robot behaviors that produce valid whole-body trajectories within those worlds. Each ingredient
poses a distinct challenge. On the Real2Sim side, creating environments with sufficient realism,
diversity, and geometric detail at scale has traditionally been prohibitive. On the Sim2Real side,
policies trained entirely on synthetic renderings must transfer back to physical hardware under real-
world visual and dynamic variation. Recent progress, however, suggests that these barriers are
beginning to weaken. 3D Gaussian Splatting (3DGS) [3] can efficiently reconstruct indoor environ-
ments with photorealistic detail and metric scale, providing a partial Real2Sim solution for world
assets. Whole-body motion tracking trained in simulation [4] can produce real-world robot policies
that faithfully execute kinematic reference trajectories, providing a partial Sim2Real solution for be-
haviors. From this maturing but still fragmented technical landscape, we ask: can we connect these
partial solutions into a real-to-sim-to-real pipeline for both scene assets and humanoid behaviors?
We show that the missing link is a data-generation system that synthesizes paired visual observa-
tions within 3DGS worlds and corresponding robot kinematic behaviors suitable for whole-body
motion tracking. The key advantage of such a system is the decoupling it enables. We can pre-
scribe the language commands, leverage privileged information in the simulated world (e.g., object
poses, collision geometry, walkable regions) to ease the challenge of behavior generation, and ren-
der the corresponding egocentric observations as RGB images after the fact. By exploiting targeted
annotation, oracle-conditioned motion synthesis, and hindsight rendering, we can scale up data pro-
duction by orders of magnitude to generate synchronized language instructions, egocentric visual
observations, and whole-body kinematic trajectories without any human demonstration effort.
Using this system, we synthesize 48,000 trajectories automatically within 600 GPU-hours in metric-
scale indoor environments reconstructed by 3DGS. We then train a Vision-Language-Kinematics
(VLK) policy that takes an egocentric image, a task instruction, and the current robot state as in-
put, and predicts a short-horizon whole-body kinematic trajectory together with binary wrist-object
contact labels. We treat these contact labels as auxiliary components of the kinematic state: they
indicate whether each wrist should be in contact with the manipulated object and are readily avail-


                                                  2

## Page 3

able from our synthetic data. During deployment, a contact-aware whole-body tracker [5] uses the
predicted kinematics and contact labels to produce robot actions on the physical humanoid.
We evaluate the system on two fundamental task categories, navigation and object transport. Navi-
gation requires the robot to move itself to a commanded location; object transport requires it to move
an object to a commanded location. Together, they exercise the full perception-to-action loop: vi-
sual grounding, locomotion, picking up, carrying, and placing objects. Experiments in closed-loop
simulation and on the physical G1 demonstrate that our synthesized interactions in reconstructed
scenes provide effective supervision for sim-to-real perception-based humanoid loco-manipulation.

2   Related Work
Vision-language and perception-based policies for humanoids. Vision-language-action (VLA)
policies map visual observations and language instructions to robot actions and have become
a promising paradigm for robot policy learning [6, 7, 8]. Recent work extends this direction
to humanoid robots, where policies must connect perception, language, and whole-body con-
trol [9, 10, 11, 12, 13, 14, 15, 16, 17]. WholeBodyVLA [11] and Ψ0 [13] train humanoid loco-
manipulation policies using egocentric video data together with real humanoid teleoperation data.
Our work is complementary: instead of relying on existing robot demonstrations or human videos
as the primary supervision source, we generate paired vision-language-kinematics supervision in
reconstructed scenes, enabling a VLK policy to predict explicit future G1 whole-body kinematic
trajectories for tracker-based execution.

Synthetic data and reconstructed scenes for robot learning. Synthetic data can reduce real-
world data-collection cost and expose policies to controlled variation in appearance, geometry, and
task configuration. Recent work uses digital twins and reconstructed scene representations, such as
3D Gaussian Splatting, to build realistic synthetic environments for robot manipulation, locomotion,
demonstration synthesis, and evaluation [18, 19, 20, 21, 22]. In this work, we also use 3DGS-
reconstructed scenes to generate synthetic robot-learning data. Our focus, however, is humanoid
loco-manipulation, where data generation must provide both realistic egocentric observations and
valid whole-body interaction behaviors. We therefore combine reconstructed scenes with humanoid
motion synthesis to generate paired vision-language-kinematics supervision.

Humanoid motion synthesis and whole-body tracking. Human motion, retargeting pipelines,
and whole-body tracking controllers provide a practical route for generating and executing hu-
manoid kinematic references. Retargeting methods map human motions to humanoid embodi-
ments [23, 24], and whole-body tracking methods train controllers to execute such references on
hardware [25, 26, 27, 28, 29]. Recent work further generates text-conditioned humanoid motion
references for whole-body control [30, 31, 16, 15, 32]. For humanoid loco-manipulation, however,
synthetic behaviors must include object interaction. We therefore adapt human-object interaction
synthesis methods [33, 34] from SMPL-based human motion to a Unitree G1 kinematic representa-
tion, and use the synthesized G1-object trajectories as supervision paired with egocentric renderings
and language instructions.

3   Method
Our goal is to enable a Unitree G1 humanoid to perform perception-based loco-manipulation, in-
cluding object-directed navigation and box interaction, from egocentric observations and task in-
structions. We formulate the problem as kinematic prediction followed by whole-body tracking:
given the current egocentric view, instruction, and robot kinematic state, a high-level policy predicts
a short-horizon G1 whole-body kinematic trajectory, and a whole-body tracker converts the pre-
dicted trajectory into executable robot actions. This decomposition makes whole-body kinematics
the learning target for the perception policy, and shifts the central data requirement to paired ego-
centric observations, task instructions, and G1 kinematics. We obtain this supervision synthetically
in reconstructed scenes, avoiding the need to collect full-body teleoperation data for the target tasks.
Figure 2 illustrates the overall pipeline. The following sections describe synthetic data generation
(Sec 3.1), VLK policy training (Sec 3.2), whole-body tracking (Sec 3.3), and deployment (Sec 3.4).

                                                   3

## Page 4

Synthetic Data Generation

        1. Scene Reconstruction             2. Waypoint Generation           3. Robot Motion Synthesis                   4. Egocentric View Rendering




              …

      Captured Images   3DGS Scene              Waypoints                                                              Robot Asset      Rendered Images
                                                                               “Put the box down on the stool.”



                                                               Vision-Language-Kinematics Policy
                                                                              Future Kinematic Trajectory                            Physical Execution
                          Input
           Egocentric           Task        Current
             Image           Instruction    G1 State
                                                                                                                  Whole-Body
                                                                    VLK
                                                                                                                   Tracking
                             "Pick up box
                             from floor.”
                                            Wrist contact
                                            No wrist contact                   Wrist contact
                                                                               No wrist contact




Figure 2: Method overview. Top: we reconstruct 3D scenes, generate task waypoints, synthe-
size G1 motions, and render egocentric observations to produce paired vision-language-kinematics
supervision. Bottom: the paired data train a VLK policy to predict short-horizon G1 kinematic tra-
jectories from egocentric observations, task instructions, and the current G1 state; at deployment, a
whole-body tracker converts the predicted trajectories into robot actions for physical execution.
3.1       Synthetic Data Generation in Reconstructed Scenes
We generate training data by synthesizing Unitree G1 motions in metric-scale reconstructed scenes
and rendering the corresponding egocentric observations. The pipeline has three stages: scene re-
construction and annotation, G1 motion synthesis in the annotated scenes, and egocentric rendering.
Together, these stages produce paired vision-language-kinematics data.
Scene Reconstruction and Annotation. We reconstruct indoor environments from Polycam scans
captured with an iPhone 14 Pro. The scans combine RGB imagery with LiDAR-based depth, en-
abling metric-scale scene reconstruction. For each scene, we optimize a 3DGS representation that
preserves the visual appearance and spatial layout of the real environment for egocentric rendering.
For motion synthesis, we extract a scene point cloud and annotate task-relevant semantic and ge-
ometric information. Specifically, we annotate semantic 3D bounding boxes for objects and mark
walkable regions (see Appendix A.1). These annotations define the scene constraints used by the
motion synthesis stage: for each task, we sample task-relevant objects, feasible initial robot poses,
and sparse waypoints according to task-specific rules. We also use semantic object labels from the
3D bounding boxes to instantiate task instructions with simple templates, e.g., “walk toward the
[object]” for navigation and task-specific templates such as “pick up the box from the floor” or “put
down the box on the [surface]” for interaction. Additional details are provided in Appendix A.2.
Interaction Synthesis in Reconstructed Scenes. Using the scene-derived waypoints, we synthe-
size Unitree G1 trajectories for two task families: object-directed navigation and object interaction.
The navigation model is trained on G1 motions from BONES-SEED [35], while the interaction
model is trained from OMOMO [36] sequences retargeted to G1 with OmniRetarget [23].
We represent a G1 motion sequence of length T as X = [p, R, sin(q), cos(q)], where p ∈ RT ×J×3
and R ∈ RT ×J×6 denote global joint positions and 6D joint rotations [37] for J joints, and
q ∈ RT ×D denotes the G1 joint angles. We encode joint angles using (sin(q), cos(q)) to avoid
discontinuities from angle wrap-around. For object-interaction sequences, we additionally repre-
sent the object trajectory as Xobj = [o, Robj ], where o ∈ RT ×3 is the global object position and
Robj ∈ RT ×6 is the object rotation relative to the input object geometry.
We build on the conditional diffusion formulation of prior human-object interaction synthesis meth-
ods [33, 34], and adapt it to the Unitree G1 representation. The navigation model generates G1
trajectories for object-directed walking from task instructions, initial G1 states, and sparse scene-
grounded waypoints. The interaction model generates coupled G1-object trajectories and addition-


                                                                              4

## Page 5

Egocentric           2                                           Egocentric
           2                                    View                                           1                 View
                                                           1                                                                1
                                     1


                                                           2                                                                2




            Pick up the box from the floor                             Pick up the box from the coffee table

           1                                  Egocentric                                                       Egocentric
                                                View               1                                             View
                                                           1                                              2                 1

                        2

                                                           2                                                                2




            Put down the box on the floor                              Put down the box on the coffee table

Figure 3: Examples of generated VLK supervision. Each sequence pairs an egocentric RGB
observation and language instruction with the corresponding G1 whole-body kinematic trajectory.
ally conditions on the initial object state, object geometry features [38], desired relative wrist poses,
and wrist contact labels. These conditions specify interaction constraints such as wrist placement,
and contact timing. Additional details are provided in Appendix A.3 and A.4.
Egocentric View Rendering. We render egocentric observations by replaying the synthesized G1
trajectories in Isaac Sim. For each sequence, we load the reconstructed 3DGS scene and place
the Unitree G1 model in the scene. The robot is equipped with a virtual ZED 2i camera mounted
on the head, with extrinsics calibrated to match the physical camera setup on the real robot. This
alignment ensures that the rendered observations closely match the deployment viewpoint. To im-
prove robustness to visual differences between rendered and real observations, we apply domain
randomization during rendering, including lighting variation and perturbations to camera extrinsics
and focal length. Details are provided in Appendix A.5.
Overall, the pipeline produces paired VLK sequences consisting of egocentric observations, task
instructions, and G1 whole-body trajectories. Examples of the resulting data are shown in Figure 3.
For more examples, please see Appendix A.6.
3.2 Vision-Language-Kinematics Policy
The generated vision-language-kinematics sequences provide paired supervision for learning a pol-
icy that maps robot-view observations and task instruction to future whole-body motion.
Kinematic State Representation. We represent each per-frame G1 kinematic state at frame τ
as xτ = [∆xτ , ∆yτ , ∆ψτ , hτ , Rroot τ   , sin(qτ ), cos(qτ ), cτ ], where (∆xτ , ∆yτ ) is the heading-
normalized root planar displacement, ∆ψτ is the yaw change, hτ is the root height, Rroot       τ    is the
heading-normalized 6D root orientation, and qτ denotes the G1 joint angles. We denote the contact
vector as cτ = [cL    R           L R
                 τ , cτ ], where cτ , cτ ∈ {0, 1} indicate the left and right wrist-object contact labels.
VLK Policy Formulation. At timestep t, the VLK policy takes the current egocentric RGB obser-
vation ot , task instruction ℓ, and current G1 kinematic state xt as input 1 , and predicts an H-frame
future trajectory x̂t+1:t+H = πθ (ot , ℓ, xt ), where H = 30 corresponds to one second at 30 Hz. The
instruction ℓ is fixed for each task execution, and the predicted trajectory serves as the high-level
motion target for the downstream whole-body tracker.
Training Objective. We initialize the VLK policy from a pretrained π0.5 [39] and fine-tune the
full model on our generated vision-language-kinematics dataset. We adapt the action space to our
G1 kinematic representation. We train the policy with an x0 -prediction objective in a flow-matching
formulation. Given a ground-truth future trajectory xt+1:t+H , Gaussian noise ϵ, and interpolation
coefficient α, we construct the noisy trajectory xαt+1:t+H = αϵ + (1 − α)xt+1:t+H . The pol-
icy predicts the clean trajectory as x̂t+1:t+H = πθ (xαt+1:t+H , α, ot , ℓ, xt ) and is trained with the
reconstruction loss Ltraj = ∥x̂t+1:t+H − xt+1:t+H ∥22 . We additionally apply auxiliary losses for
   1
       During deployment, the contact label in xt is auto-regressively predicted rather than directly observed.


                                                               5

## Page 6

foot-floor contact prediction, accumulated root-trajectory consistency, forward-kinematics accuracy,
and foot-sliding regularization to improve motion quality. Details are provided in Appendix B.1.

3.3   Whole-Body Motion Tracking
The VLK policy predicts high-level reference states x̂t , which are executed on the physical hu-
manoid by a contact-aware whole-body tracker based on SceneBot [5]. The tracker is blind to ego-
centric observations and language instructions: it only receives converted reference targets and cur-
rent robot proprioception, while VLK handles perception-conditioned replanning. At each control
step, we convert the predicted VLK state x̂t into the tracker reference format, including lower-body
joint targets, upper-body head and wrist target 6D poses, root target pose, and binary wrist-object
contact labels. The tracker takes this converted reference x̄t and the current low-level robot state st
as input, and outputs joint-level PD targets for all actuated joints: ut = πtrack (x̄t , st ). Similar to
prior whole-body tracking controllers [40, 5], the tracker follows the reference motion while using
the predicted contact labels to stabilize object transport. When wrist contact is active, the tracker
activates contact-aware wrist behavior to maintain contact with the manipulated object.

3.4   Deployment
During real-world deployment, we implement a real-time VLA [41] system with Triton as the opti-
mized inference backend. On an RTX 5090, the end-to-end VLK inference latency remains stable
at 31 ms. To reduce discontinuities between predicted chunks, we adapt the client-side real-time
chunking idea from Ψ0 [13] to our kinematic trajectory setting. In our case, there will be 10 time-
frame overlap between two adjacent action chunks. In addition, motion blur in egocentric observa-
tions can degrade VLK prediction quality during real-world operation, especially during fast bend-
ing motions. To improve robustness, we use sharpness-based frame selection during deployment.
Details are provided in Appendix B.3.

4     Experiments
In this section, we introduce our hardware setup (Sec. 4.1) and then answer four research questions:
(i) How efficiently can the proposed pipeline generate diverse paired VLK data? (Sec. 4.2) (ii) Can
a VLK policy trained on synthesized data transfer to the physical humanoid? (Sec. 4.3) (iii) How
does the amount of synthesized training data affect performance across different tasks? (Sec. 4.4)
(iv) How does visual domain randomization help bridge the visual sim-to-real gap? (Sec. 4.5)

4.1   Experimental Setup
We use two physical environments: a lab-style scene and an apartment-style scene. For each envi-
ronment, we create multiple physical layouts by changing the positions and orientations of selected
furniture items, then scan each layout using the Polycam app on an iPhone 14 Pro and reconstruct it
with 3D Gaussian Splatting (3DGS) [3, 22]. This produces 4 lab and 4 apartment layouts, which are
used for synthetic data generation and simulation evaluation. Real-world deployment is conducted
in the same two physical environments, with furniture layouts manually varied across trials.
We deploy our system on a Unitree G1 on a custom 3D-printed head bracket to obtain a wider field
of view and use the left RGB image at 672×376 resolution, resized to the VLK input resolution of
224×224. During deployment, VLK model inference runs on an RTX 5090, while the whole-body
tracking policy runs on an RTX 5000 Ada. A detailed system overview and profiling results are
provided in Appendix B.4.

4.2   Synthetic Data Generation
How efficiently can the proposed pipeline generate diverse paired VLK data? Given a re-
constructed scene with semantic 3D bounding boxes and walkable-region annotations, the pipeline
samples task-relevant objects, feasible initial poses, waypoints, and task instructions; synthesizes
G1-compatible trajectories; filters trajectories with scene penetrations; and renders paired egocentric
observations. Each sequence contains synchronized egocentric observations, language instructions,
and G1 whole-body kinematic trajectories.


                                                   6

## Page 7

Table 1: Full-system evaluation in MuJoCo simulation (with IsaacSim rendering) and real-world
deployment. We report the number of successful trials over the total number of trials for each mode.
 Setting      Scene             Walk To    Turn Around   Pick (Floor)       Put (Floor)   Pick (Surface)   Put (Surface)
              Lab Scene          20/20        20/20                16/20      20/20           11/20           8/20
 Real-World
              Apartment Scene    19/20        18/20                18/20      20/20           13/20           15/20
              Lab Scene         994/1000    843/1000         731/1000        991/1000       458/1000         569/1000
 Simulation
              Apartment Scene   948/1000    813/1000         749/1000        987/1000       521/1000         722/1000
Each environment contains 4 reconstructed layouts and 12 data-generation modes: six evaluated
modes—Walk To, Turn Around, Pick (Floor), Put (Floor), Pick (Surface), and Put (Surface)—plus
auxiliary modes for random walking, turning, carrying, and carry-turning. These auxiliary modes
improve state coverage by exposing the policy to diverse walking and object-transport behaviors.
We synthesize 1000 trajectories per layout and mode, yielding 48,000 trajectories per environment.
On a single NVIDIA L40S GPU, synthesizing 1000 trajectories for one mode in one layout takes
approximately 4 hours, while rendering the corresponding egocentric observations takes approxi-
mately 8.3 hours. These results show that, after scene reconstruction and annotation, the pipeline
can automatically generate large volumes of paired VLK supervision, with generation parallelized
across layouts and modes.
4.3 Evaluation of Complete System
Can a VLK policy trained on synthesized data transfer to the physical humanoid? We test the
full closed-loop system in MuJoCo simulation (with IsaacSim rendering) and on the physical Unitree
G1. In both settings, the VLK policy predicts short-horizon whole-body kinematic trajectories from
egocentric observations, task instructions, and robot kinematic state, while the whole-body tracker
converts the predicted kinematics into robot actions.
For real-world evaluation, we conduct trials in both the lab and apartment environments while vary-
ing the scene layout across trials. We evaluate the six task modes shown in Table 1, with 20 trials per
mode, resulting in 120 real-world trials in total. In addition, we also evaluate “Pick (Floor)” without
a contact label, and the success rates in both the Lab Scene and the Apartment Scene are 0 out of
5 trials in real-world evaluation. For simulation evaluation, we use Isaac Sim to render egocentric
RGB observations from the reconstructed 3DGS scenes. At each replanning step, the VLK policy
takes the rendered egocentric image and task instruction as input and predicts future G1 kinematics.
The predicted kinematics are then executed by the whole-body tracker in MuJoCo, where we evalu-
ate closed-loop task success. We use a held-out validation set comprising 10% of the generated data.
We evaluate 1000 rollouts for each task mode, using the initial pose from each validation sequence
as the test initial condition. Success is determined by task-specific heuristic rules for each mode,
with details provided in Appendix B.2. Table 1 reports the resulting success rates.
As shown in Table 1, the system achieves high success rates on object-directed navigation and
floor-level box manipulation in both simulation and the real world. Surface-level interactions are
more challenging, partly because the retargeted interaction data provides limited coverage of box
manipulation at different support-surface heights, leading to less reliable grasps and placements.
4.4 Effect of Synthesized Data Volume                             Walk To     Pick (Floor)     Pick (Surface)
                                                        100%                                                99%
How does the amount of synthesized train-
ing data affect performance across different             80%




                                                             Success rate
                                                                                                            73%
tasks? For each layout in the lab scene, our de-         60%
                                                                                                            46%
fault setting generates 1000 trajectories per mode.      40%
To study the effect of synthesized training-data         20%
volume, we train VLK policies using different                         scales with data
                                                          0%
fractions of the full dataset and evaluate each              100   250          500         750         1000
                                                            (10%) (25%)       (50%)        (75%)       (100%)
policy in closed-loop MuJoCo simulation (with
                                                                         Training data volume
IsaacSim rendering) on the lab-scene validation
set. The per-mode success rates are reported in Figure 4: Ablation of training-data volume in
Figure 4. As shown in the figure, increasing the lab scene. We vary the number of synthe-
the amount of synthesized training data consis- sized trajectories per mode per layout and report
tently improves performance across the evaluated success rates on the lab-scene validation set.


                                                         7

## Page 8

Pick up the box from the floor.                                                       Walk toward the black chair. Turn around.
                                                             Pick up the box from the black chair.
               Put down the box on the floor.                                                              Walk toward the white chair.

    1. Light                                     2. Layout                        3. Layout                  4. Layout




                                Walk toward the grey office chair (Under Light and Layout Disturbance)

Figure 5: Real-world deployment in lab and apartment scenes. The VLK system executes
language-conditioned navigation and box manipulation under different layouts and visual variations.
Top: sequential lab-scene executions for manipulation and navigation. Bottom: apartment-scene de-
ployments under lighting (disco light) and layout variations.

modes. Object-directed navigation achieves high success rates even with limited data, suggesting
that navigation is easier to learn from synthetic supervision. In contrast, manipulation tasks ben-
efit substantially from additional trajectories, with Pick (Surface) improving from 0% success at
10% data to 46% success using the full dataset. These results indicate that contact-rich, perception-
conditioned manipulation requires more scene-grounded supervision than navigation, highlighting
the value of increasing synthesized data volume.

4.5       Effect of Visual Domain Randomization
How does visual domain randomization help Table 2: Effect of visual domain randomiza-
bridge the visual sim-to-real gap? We evaluate tion on walking-mode success. Evaluation is con-
whether visual domain randomization during ren- ducted in the lab scene under visual perturbations,
                                                        including lighting and camera variation.
dering improves robustness to visual perturbations
in MuJoCo simulation (with IsaacSim rendering).           Configuration             Success Rate (%) ↑
Specifically, we evaluate walking-mode success in         No randomization                    41
the lab scene under randomized lighting and cam-          Camera randomization                48
era conditions, and compare four training configu-        Lighting randomization              87
rations: no randomization, lighting randomization         Full randomization                  90
only, camera randomization only, and full random-
ization. The full setting combines lighting variation and camera variation.
As shown in Table 2, removing visual domain randomization substantially reduces walking suc-
cess from 90% to 41%, indicating that visual variation is important for transferring policies trained
on rendered egocentric observations to the real robot. The lighting-only and camera-only settings
provide a coarse ablation of appearance variation and viewpoint/calibration robustness. Additional
real-world deployment examples are shown in Figure 5, illustrating the system operating under dif-
ferent lighting conditions and scene layouts.

5       Conclusion
We presented a perception-based humanoid loco-manipulation system trained from synthesized in-
teractions in reconstructed 3D scenes. Our pipeline generates Unitree G1-compatible navigation
and box-manipulation trajectories, renders paired egocentric observations, and trains a VLK policy
to predict whole-body kinematic trajectories for tracker-based execution. Experiments in simulation
and on the physical Unitree G1 demonstrate object-directed navigation and box manipulation, show-
ing that scene-grounded synthetic supervision can support sim-to-real humanoid loco-manipulation.
These results suggest that synthesizing robot-compatible interactions in reconstructed scenes is a
promising path toward scalable perception-conditioned humanoid control.


                                                                              8

## Page 9

Limitations. Our current interaction synthesis is limited by the coverage of OMOMO, which con-
tains interactions with a limited set of large objects. As a result, the generated behaviors are better
suited to bimanual transport of box-like objects than to grasping small objects such as cups or tools.
Similarly, the contact-aware tracker stabilizes large-object manipulation through wrist-object con-
tact, but does not address precise object grasping. Extending VLK to small-object manipulation
would require richer interaction data and a low-level controller designed for precise object grasping.

Acknowledgments
We thank Xiaoyu Huang for preparing a clean retargeted OMOMO dataset, Alejandro Escontrela
for guidance on 3DGS training, Jenny Zhang and Hunter Liu for providing realistic box assets for
rendering, and Eric Lalumiere for providing the camera mount. We also thank Zhen Wu, Shibo
Zhao, and Yunsheng Tian for valuable discussions on motion synthesis and Real2Sim pipelines. We
are grateful to Haozhi Qi, Linda Shih, Youjian Huang, and Roberto Ceja for their support with the
experimental hardware, and to Shuying Deng, Zihan Wang, and Charlie Cheng for their valuable
feedback on the design and visual presentation of the paper figures and video.

References
 [1] Y. Ze, S. Zhao, W. Wang, A. Kanazawa, R. Duan, P. Abbeel, G. Shi, J. Wu, and C. K. Liu.
     Twist2: Scalable, portable, and holistic humanoid data collection system. arXiv preprint
     arXiv:2511.02832, 2025. URL https://arxiv.org/abs/2511.02832.

 [2] Y. Li, Y. Lin, J. Cui, T. Liu, W. Liang, Y. Zhu, and S. Huang. Clone: Closed-loop whole-body
     humanoid teleoperation for long-horizon tasks. arXiv preprint arXiv:2506.08931, 2025. URL
     https://arxiv.org/abs/2506.08931.

 [3] B. Kerbl, G. Kopanas, T. Leimkühler, G. Drettakis, et al. 3d gaussian splatting for real-time
     radiance field rendering. ACM Trans. Graph., 42(4):139–1, 2023.

 [4] Q. Liao, T. E. Truong, X. Huang, Y. Gao, G. Tevet, K. Sreenath, and C. K. Liu. Beyondmimic:
     From motion tracking to versatile humanoid control via guided diffusion, 2025. URL https:
     //arxiv.org/abs/2508.08241.

 [5] S. Chen, S. Zhao, Z. Wu, J. Li, G. Shi, and C. K. Liu. Scenebot: Contact-prompted general
     humanoid whole body tracking with scene-interaction, 2026. URL https://arxiv.org/
     abs/2606.27581.

 [6] B. Zitkovich, T. Yu, S. Xu, P. Xu, T. Xiao, F. Xia, J. Wu, P. Wohlhart, S. Welker, A. Wahid,
     Q. Vuong, V. Vanhoucke, H. Tran, R. Soricut, A. Singh, J. Singh, P. Sermanet, P. R. San-
     keti, G. Salazar, M. S. Ryoo, K. Reymann, K. Rao, K. Pertsch, I. Mordatch, H. Michalewski,
     Y. Lu, S. Levine, L. Lee, T.-W. E. Lee, I. Leal, Y. Kuang, D. Kalashnikov, R. Julian, N. J.
     Joshi, A. Irpan, B. Ichter, J. Hsu, A. Herzog, K. Hausman, K. Gopalakrishnan, C. Fu, P. Flo-
     rence, C. Finn, K. A. Dubey, D. Driess, T. Ding, K. M. Choromanski, X. Chen, Y. Chebotar,
     J. Carbajal, N. Brown, A. Brohan, M. G. Arenas, and K. Han. RT-2: Vision-language-action
     models transfer web knowledge to robotic control. In Proceedings of The 7th Conference on
     Robot Learning, volume 229 of Proceedings of Machine Learning Research, pages 2165–2183.
     PMLR, 2023.

 [7] M. J. Kim, K. Pertsch, S. Karamcheti, T. Xiao, A. Balakrishna, S. Nair, R. Rafailov, E. P. Foster,
     P. R. Sanketi, Q. Vuong, T. Kollar, B. Burchfiel, R. Tedrake, D. Sadigh, S. Levine, P. Liang, and
     C. Finn. OpenVLA: An open-source vision-language-action model. In Proceedings of The 8th
     Conference on Robot Learning, volume 270 of Proceedings of Machine Learning Research,
     pages 2679–2713. PMLR, 2025.

 [8] K. Black, N. Brown, D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, L. Groom, K. Haus-
     man, B. Ichter, S. Jakubczak, T. Jones, L. Ke, S. Levine, A. Li-Bell, M. Mothukuri, S. Nair,


                                                  9

## Page 10

K. Pertsch, L. X. Shi, J. Tanner, Q. Vuong, A. Walling, H. Wang, and U. Zhilinsky. π0 : A
     vision-language-action flow model for general robot control. In Robotics: Science and Sys-
     tems, 2025.

 [9] NVIDIA, J. Bjorck, F. Castañeda, N. Cherniadev, X. Da, R. Ding, L. Fan, Y. Fang, D. Fox,
     F. Hu, et al. GR00T N1: An open foundation model for generalist humanoid robots. arXiv
     preprint arXiv:2503.14734, 2025.

[10] H. Xue, X. Huang, D. Niu, Q. Liao, T. Kragerud, J. T. Gravdahl, X. B. Peng, G. Shi, T. Dar-
     rell, K. Sreenath, and S. Sastry. LeVERB: Humanoid whole-body control with latent vision-
     language instruction. arXiv preprint arXiv:2506.13751, 2025.

[11] H. Jiang, J. Chen, Q. Bu, L. Chen, M. Shi, Y. Zhang, D. Li, C. Suo, C. Wang, Z. Peng,
     and H. Li. WholeBodyVLA: Towards unified latent VLA for whole-body loco-manipulation
     control. In International Conference on Learning Representations, 2026.

[12] P. Ding, J. Ma, X. Tong, B. Zou, X. Luo, Y. Fan, T. Wang, H. Lu, P. Mo, J. Liu, et al.
     Humanoid-vla: Towards universal humanoid control with visual integration. arXiv preprint
     arXiv:2502.14795, 2025.

[13] S. Wei, H. Jing, B. Li, Z. Zhao, J. Mao, Z. Ni, S. He, J. Liu, X. Liu, K. Kang, S. Zang, W. Yuan,
     M. Pavone, D. Huang, and Y. Wang. Ψ0 : An open foundation model towards universal hu-
     manoid loco-manipulation. In Robotics: Science and Systems, 2026.

[14] S. Chen, Y. Ye, Z.-A. Cao, J. Lew, P. Xu, and C. K. Liu. Hand-eye autonomous delivery:
     Learning humanoid navigation, locomotion and reaching. arXiv preprint arXiv:2508.03068,
     2025.

[15] Y. Shao, X. Huang, B. Zhang, Q. Liao, Y. Gao, Y. Chi, Z. Li, S. Shao, and K. Sreenath. Lang-
     WBC: Language-directed humanoid whole-body control via end-to-end learning. In Robotics:
     Science and Systems, 2025.

[16] P. Li, Z. Zhuang, Y. Gao, Y. Dong, S. Li, C. Jiang, S. Dou, Z. Xi, E. Zhou, J. Huang, H. Li,
     J. Gong, X. Ma, T. Gui, Z. Wu, Q. Zhang, X. Huang, Y.-G. Jiang, and X. Qiu. FRoM-W1:
     Towards general humanoid whole-body control with language instructions. arXiv preprint
     arXiv:2601.12799, 2026.

[17] D. Kalaria, S. S. Harithas, P. Katara, S. Kwak, S. Bhagat, S. Sastry, S. Sridhar, S. Vemprala,
     A. Kapoor, and J. C.-K. Huang. Dreamcontrol: Human-inspired whole-body humanoid control
     for scene interaction via guided diffusion. arXiv preprint arXiv:2509.14353, 2025.

[18] Y. Mu, T. Chen, Z. Chen, S. Peng, Z. Lan, Z. Gao, Z. Liang, Q. Yu, Y. Zou, M. Xu, L. Lin,
     Z. Xie, M. Ding, and P. Luo. RoboTwin: Dual-arm robot benchmark with generative digital
     twins. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recogni-
     tion, 2025.

[19] M. N. Qureshi, S. Garg, F. Yandun, D. Held, G. Kantor, and A. Silwal. SplatSim: Zero-
     shot sim2real transfer of RGB manipulation policies using gaussian splatting. arXiv preprint
     arXiv:2409.10161, 2024.

[20] X. Li, J. Li, Z. Zhang, R. Zhang, F. Jia, T. Wang, H. Fan, K.-K. Tseng, and
     R. Wang. RoboGSim: A real2sim2real robotic gaussian splatting simulator. arXiv preprint
     arXiv:2411.11839, 2024.

[21] Y. Wu, L. Pan, W. Wu, G. Wang, Y. Miao, and H. Wang. RL-GSBridge: 3d gaussian splatting
     based real2sim2real method for robotic manipulation learning. In IEEE International Confer-
     ence on Robotics and Automation, 2025.


                                                 10

## Page 11

[22] A. Escontrela, J. Kerr, A. Allshire, J. Frey, R. Duan, C. Sferrazza, and P. Abbeel. GaussGym:
     An open-source real-to-sim framework for learning locomotion from pixels. In International
     Conference on Learning Representations, 2026.

[23] L. Yang, X. Huang, Z. Wu, A. Kanazawa, P. Abbeel, C. Sferrazza, C. K. Liu, R. Duan, and
     G. Shi. OmniRetarget: Interaction-preserving data generation for humanoid whole-body loco-
     manipulation and scene interaction. In IEEE International Conference on Robotics and Au-
     tomation, 2026.

[24] J. P. Araujo, Y. Ze, P. Xu, J. Wu, and C. K. Liu. Retargeting matters: General motion retargeting
     for humanoid motion tracking. In IEEE International Conference on Robotics and Automation,
     2026.

[25] T. He, Z. Luo, X. He, W. Xiao, C. Zhang, W. Zhang, K. Kitani, C. Liu, and G. Shi. Om-
     niH2O: Universal and dexterous human-to-humanoid whole-body teleoperation and learning.
     In Proceedings of The 8th Conference on Robot Learning, Proceedings of Machine Learning
     Research. PMLR, 2024.

[26] Z. Chen, M. Ji, X. Cheng, X. Peng, X. B. Peng, and X. Wang. GMT: General motion tracking
     for humanoid whole-body control. arXiv preprint arXiv:2506.14770, 2025.

[27] Q. Liao, T. E. Truong, X. Huang, G. Tevet, K. Sreenath, and C. K. Liu. BeyondMimic:
     From motion tracking to versatile humanoid control via guided diffusion. arXiv preprint
     arXiv:2508.08241, 2025.

[28] S. Zhao, Y. Ze, Y. Wang, C. K. Liu, P. Abbeel, G. Shi, and R. Duan. Resmimic: From gen-
     eral motion tracking to humanoid whole-body loco-manipulation via residual learning. arXiv
     preprint arXiv:2510.05070, 2025.

[29] Z. Luo, Y. Yuan, T. Wang, C. Li, S. Chen, F. Castañeda, Z.-A. Cao, J. Li, D. Minor, Q. Ben,
     X. Da, R. Ding, C. Hogg, L. Song, E. Lim, E. Jeong, T. He, H. Xue, W. Xiao, Z. Wang,
     S. Yuen, J. Kautz, Y. Chang, U. Iqbal, L. Fan, and Y. Zhu. Sonic: Supersizing motion tracking
     for natural humanoid whole-body control. arXiv preprint arXiv:2511.07820, 2025.

[30] D. Kalaria, S. S. Harithas, P. Katara, S. Kwak, S. Bhagat, S. Sastry, S. Sridhar, S. Vemprala,
     A. Kapoor, and J. C.-K. Huang. DreamControl: Human-inspired whole-body humanoid con-
     trol for scene interaction via guided diffusion. arXiv preprint arXiv:2509.14353, 2025.

[31] Z. Zhang, K. Wen, M. Xu, J. He, C. Li, T. Miki, C. Schwarke, C. Zhang, X. B. Peng, and
     M. Hutter. Learning whole-body humanoid locomotion via motion generation and motion
     tracking. arXiv preprint arXiv:2604.17335, 2026.

[32] D. Rempe, M. Zanfir, Y.-T. Hu, R. Li, C. Li, J. Tseng, L. Liu, T. Darrell, A. Kanazawa,
     J. Kautz, C. K. Liu, S. Fidler, L. Guibas, S. Saito, O. Litany, G. Shafir, T.-Y. Lin, S. Tulsiani,
     A. A. Efros, et al. Kimodo: Scaling controllable human motion generation. arXiv preprint
     arXiv:2603.15546, 2026. URL https://arxiv.org/abs/2603.15546.

[33] J. Li, A. Clegg, R. Mottaghi, J. Wu, X. Puig, and C. K. Liu. Controllable human-object
     interaction synthesis. In European Conference on Computer Vision, 2024.

[34] Z. Wu, J. Li, P. Xu, and C. K. Liu. Human-object interaction from human-level instructions.
     In Proceedings of the IEEE/CVF International Conference on Computer Vision, 2025.

[35] Bones Studio.  BONES-SEED: Skeletal everyday embodiment dataset.      https://
     huggingface.co/datasets/bones-studio/seed, 2025. Hugging Face dataset. Accessed:
     2026-05-22.

[36] J. Li, J. Wu, and C. K. Liu. Object motion guided human motion synthesis. ACM Transactions
     on Graphics, 42(6):225:1–225:11, 2023. doi:10.1145/3618333.


                                                  11

## Page 12

[37] Y. Zhou, C. Barnes, J. Lu, J. Yang, and H. Li. On the continuity of rotation representations in
     neural networks. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
     Recognition (CVPR), pages 5745–5753, 2019.
[38] S. Prokudin, C. Lassner, and J. Romero. Efficient learning on point clouds with basis point
     sets. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pages
     4332–4341, 2019.
[39] P. Intelligence, K. Black, N. Brown, J. Darpinian, K. Dhabalia, D. Driess, A. Esmail, M. Equi,
     C. Finn, N. Fusai, et al. π0 .5: a vision-language-action model with open-world generalization.
     arXiv preprint arXiv:2504.16054, 2025.

[40] S. Chen, Z. ang Cao, Z. Luo, F. Castañeda, C. Li, T. Wang, Y. Yuan, L. J. Fan, C. K. Liu,
     and Y. Zhu. Chip: Adaptive compliance for humanoid control through hindsight perturbation,
     2026. URL https://arxiv.org/abs/2512.14689.
[41] Y. Ma, Y. Zhou, Y. Yang, T. Wang, and H. Fan. Running vlas at real-time speed. arXiv preprint
     arXiv:2510.26742, 2025.

[42] Z. Wu, J. Li, P. Xu, and C. K. Liu. Human-object interaction from human-level instructions.
     In Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 11176–
     11186, 2025.
[43] B. Yi, V. Ye, M. Zheng, Y. Li, L. Müller, G. Pavlakos, Y. Ma, J. Malik, and A. Kanazawa.
     Estimating body and hand motion in an ego-sensed world. In Proceedings of the IEEE/CVF
     Conference on Computer Vision and Pattern Recognition (CVPR), 2025.
[44] M. Mittal, P. Roth, J. Tigue, A. Richard, O. Zhang, P. Du, A. Serrano-Muñoz, X. Yao,
     R. Zürbrügg, N. Rudin, L. Wawrzyniak, M. Rakhsha, A. Denzler, E. Heiden, A. Borovicka,
     O. Ahmed, I. Akinola, A. Anwar, M. T. Carlson, J. Y. Feng, A. Garg, R. Gasoto, L. Gulich,
     Y. Guo, M. Gussert, A. Hansen, M. Kulkarni, C. Li, W. Liu, V. Makoviychuk, G. Malczyk,
     H. Mazhar, M. Moghani, A. Murali, M. Noseworthy, A. Poddubny, N. Ratliff, W. Rehberg,
     C. Schwarke, R. Singh, J. L. Smith, B. Tang, R. Thaker, M. Trepte, K. Van Wyk, F. Yu,
     A. Millane, V. Ramasamy, R. Steiner, S. Subramanian, C. Volk, C. Chen, N. Jawale, A. V. Ku-
     ruttukulam, M. A. Lin, A. Mandlekar, K. Patzwaldt, J. Welsh, H. Zhao, F. Anes, J.-F. Lafleche,
     N. Moënne-Loccoz, S. Park, R. Stepinski, D. Van Gelder, C. Amevor, J. Carius, J. Chang,
     A. H. Chen, P. de Heras Ciechomski, G. Daviet, M. Mohajerani, J. von Muralt, V. Reutskyy,
     M. Sauter, S. Schirm, E. L. Shi, P. Terdiman, K. Vilella, T. Widmer, G. Yeoman, T. Chen,
     S. Grizan, C. Li, L. Li, C. Smith, R. Wiltz, K. Alexis, Y. Chang, D. Chu, L. Fan, F. Farshidian,
     A. Handa, S. Huang, M. Hutter, Y. Narang, S. Pouya, S. Sheng, Y. Zhu, M. Macklin, A. Mora-
     vanszky, P. Reist, Y. Guo, D. Hoeller, and G. State. Isaac lab: A gpu-accelerated simulation
     framework for multi-modal robot learning. arXiv preprint arXiv:2511.04831, 2025. URL
     https://arxiv.org/abs/2511.04831.




                                                 12

## Page 13

Appendix Contents

A Synthetic Data Generation Details                                                                13
      A.1 Scene Annotation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   13
      A.2 Waypoint, Language Generation in 3D Scenes . . . . . . . . . . . . . . . . . . . .       13
      A.3 Interaction Synthesis Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   14
      A.4 Post-Processing for Generated Motion . . . . . . . . . . . . . . . . . . . . . . . .     15
      A.5 Domain Randomization in Rendering . . . . . . . . . . . . . . . . . . . . . . . .        15
      A.6 Dataset Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   15

B Experiment Details                                                                               15
      B.1 VLK Training Loss Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    16
      B.2 Metric for Evaluation in Simulation . . . . . . . . . . . . . . . . . . . . . . . . .    17
      B.3 Motion Blur Handling During Deployment . . . . . . . . . . . . . . . . . . . . .         18
      B.4 System Overview and Profiling . . . . . . . . . . . . . . . . . . . . . . . . . . . .    18

A      Synthetic Data Generation Details
This appendix provides additional details on the synthetic data generation pipeline and experimental
setup. Additional simulation and real-world results are shown in the supplementary video.

A.1     Scene Annotation

We annotate each reconstructed scene to support scene-aware motion synthesis. Since the 3DGS
representation does not provide an explicit mesh or semantic labels, we first extract a point cloud
from the reconstructed scene and use it as the geometric reference for annotation. We implement
an interactive annotation tool using viser, which allows users to load the reconstructed 3D scene,
inspect it in 3D, and add task-relevant annotations.
For semantic object annotation, we manually place oriented 3D bounding boxes around objects of
interest and assign each box a semantic label, such as chair, table, or box. The annotation interface
supports translating, scaling, and rotating each box to align it with the corresponding object in the
scene. These semantic 3D boxes are used to sample target objects for navigation tasks and define
task-relevant object locations for interaction synthesis.
We also annotate walkable regions in each scene. Users specify a set of points on the floor plane,
and the tool connects these points to form polygonal regions. These regions define feasible areas
for sampling humanoid initial poses and navigation waypoints. Together, the semantic object boxes
and walkable regions provide the geometric and semantic structure needed for scene-aware motion
generation.

A.2     Waypoint, Language Generation in 3D Scenes

Waypoint Generation. We generate sparse waypoints from the annotated 3D scenes according to
task-specific rules. For navigation tasks, we first sample a target object from the annotated semantic
3D bounding boxes. We then sample the initial humanoid pose and intermediate waypoints from the
annotated walkable regions. The sampled poses are constrained to be collision-free and compatible
with the task objective.
For walk-toward-object tasks, we additionally require the target object to be visible from the initial
egocentric viewpoint. This constraint ensures that the rendered observation contains visual evidence


                                                  13

## Page 14

of the task target, making the resulting training sample visually grounded. In practice, after sampling
a candidate initial pose, we check whether the target object lies within the camera field of view and
is not occluded by major scene structures. If the visibility constraint is not satisfied, we resample the
initial pose. The distance between consecutive waypoints is selected heuristically to ensure that the
generated walking motion remains natural. For turn-around tasks, we randomly sample an initial
position that is collision-free with respect to the 3D scene and set all waypoints to the initial position,
producing in-place turning motions.
For box-interaction tasks, we generate waypoints and contact timing according to the object state
and the height of the supporting surface. For picking motions, the waypoints guide the humanoid to
approach the box, establish wrist-object contact, and lift the box from either the floor or a support
surface. For placing motions, the waypoints guide the humanoid to carry the box toward the target
support surface and release it at the desired location. Since lifting from the floor, lifting from a
table, and placing onto surfaces require different arm heights and contact phases, we design the
wrist contact frames and desired relative wrist poses based on the surface height. This task-specific
design helps the synthesized motion maintain realistic contact timing, avoid abrupt vertical motion,
and align the robot wrists with the box during lifting and placement.
The final waypoint sequence provides sparse spatial guidance for the motion synthesis model. These
waypoints encourage the generated humanoid motion to follow feasible paths in the reconstructed
scene.


Language Generation. Language annotations are generated automatically from task metadata.
Since the task type, target object, and waypoint structure are known during data generation, we use
template-based rules to assign language instructions to each trajectory.
For navigation trajectories, the instruction is instantiated from the semantic label of the sampled
target object. For example, if the target object is annotated as a chair, the corresponding instruction
is “walk toward the chair”. This produces language labels that are directly grounded in the scene
annotations.
For object-interaction trajectories, we use task-level templates defined for each motion type. For
example, box-lifting trajectories are annotated with instructions such as “lift the box from the floor”.
When the interaction target or placement location varies, the template can be instantiated with the
corresponding object or support surface label, such as “place the box on the table”. These template-
based annotations provide consistent supervision for the VLK policy while avoiding the need for
manual language labeling.


A.3   Interaction Synthesis Module

We synthesize humanoid-object interaction trajectories directly in the Unitree G1 kinematic rep-
resentation. Our interaction synthesis module follows the conditional DDPM formulation of
CHOIS [33], which generates coupled human-object motion conditioned on language instructions,
initial states, sparse waypoints, and object geometry. We retain the Transformer-based denoising
architecture, but adapt the motion representation from SMPL-based human motion to the Unitree
G1 humanoid. We also introduce a G1-specific forward-kinematics loss to improve end-effector
position accuracy.
For a sequence of length T with J G1 joints, the humanoid motion is represented as xg1 =
[p, R, sin(q), cos(q)], where p ∈ RT ×J×3 denotes global joint positions, R ∈ RT ×J×6 denotes
global joint rotations in the 6D rotation representation, and q ∈ RT ×D denotes the G1 joint angles.
We encode joint angles as (sin(q), cos(q)) rather than raw angles to avoid discontinuities from an-
gle wrap-around. The object trajectory is represented as xobj = [o, Robj ], where o ∈ RT ×3 is the
global object position and Robj ∈ RT ×6 is the object rotation relative to the canonical pose of the
input object geometry. The full interaction trajectory is x = [xg1 , xobj ].


                                                    14

## Page 15

The model is trained as a conditional denoising diffusion model. During training, Gaussian noise
is added to the clean interaction trajectory x at a sampled diffusion timestep, and the Transformer
denoising network predicts the clean motion or denoising target conditioned on the task context.
The conditioning inputs include the language instruction, initial humanoid and object states, sparse
scene-derived waypoints, object geometry, desired relative wrist poses, and wrist-object contact la-
bels. Language instructions are encoded using CLIP text features, and object geometry is encoded
using a Basis Point Set (BPS) representation followed by an MLP projection. The sparse way-
points provide scene-level spatial guidance, while the wrist-pose and contact conditions specify the
intended object interaction. The desired relative wrist poses are defined in the object coordinate
frame. For box-lifting motions, for example, we specify the two wrists to approach opposite sides of
the box with downward-facing palms. The wrist-object contact labels indicate the expected contact
phase for each wrist. These interaction conditions help constrain the generated full-body motion so
that the wrists reach task-relevant contact regions while the object follows a consistent trajectory.
To adapt the CHOIS-style formulation to Unitree G1, we retarget OMOMO [36] motions from
SMPL to G1 using OmniRetarget [23] and train the interaction synthesis model on the resulting G1-
object trajectories. We additionally implement a differentiable G1 forward-kinematics layer, which
allows geometric losses to be applied to global body and end-effector positions. This encourages the
generated joint-angle trajectories to produce accurate whole-body geometry and wrist placements,
which is especially important for box-interaction motions.

A.4   Post-Processing for Generated Motion

Foot sliding and unrealistic hand-object contact are common artifacts in human motion synthesis
and human-object interaction synthesis. To improve the quality of the generated motions, we apply
lower-body post-processing following prior work [42]. The key idea is to use the predicted foot-
contact labels to identify contact onsets and contact phases. During each contact phase, we constrain
the corresponding robot foot to remain fixed at its contact position by solving inverse kinematics.
To correct hand-object contact artifacts, we adapt the optimization approach from EgoAllo [43] and
introduce a wrist-pose matching term that drives the position and rotation of each wrist toward the
input wrist pose expressed in the object’s local frame. This encourages more realistic two-hand
grasping contact during object interaction.

A.5   Domain Randomization in Rendering

To improve the real-world utility of the rendered data, we apply domain randomization during ego-
centric rendering. The randomization covers camera parameters, lighting, and image appearance.
Camera randomization perturbs the camera extrinsics and focal length to account for small calibra-
tion mismatches between the virtual and physical ZED 2i camera setups. Lighting randomization
changes the dome-light intensity and yaw rotation. We also apply image-space appearance augmen-
tations, including perturbations to brightness, contrast, saturation, and hue, as well as Gaussian noise
and Gaussian blur. We summarize the domain randomization ranges in Table 3.

A.6   Dataset Examples

Figure 6 shows additional representative examples from our synthetic dataset. Each example con-
tains a rendered egocentric RGB observation, a language instruction, and the corresponding G1
kinematic trajectory generated in an annotated 3D scene. Visualizations of more sequences are
provided in the supplementary video.

B     Experiment Details

This section presents supplementary details for model training, evaluation, and deployment. We
describe the objective functions used to fine-tune the VLK policy, the metrics adopted for simulation


                                                  15

## Page 16

Table 3: Domain randomization parameters used for egocentric rendering.
                                        Randomization                         Range
                                        Camera translation jitter             ±2 cm
                                        Camera rotation jitter                ±3◦
                                        Camera focal perturbation             ±2%
                                        Dome-light intensity                  [400, 1500]
                                        Dome-light yaw rotation               [−π, π]
                                        Brightness                            [0.8, 1.2]
                                        Contrast                              [0.8, 1.3]
                                        Saturation                            [0.7, 1.4]
                                        Hue                                   [−0.05, 0.05]
                                        Gaussian noise std.                   [0, 0.05]
                                        Gaussian blur sigma                   [0, 1.0]




       Walk towards the white desk            Walk towards the box on the coffee table        Walk towards the box on floor




      Turn around from the right side              Turn around from the left side             Turn around from the right side



Figure 6: Examples from the synthetic vision-language-kinematics dataset. Each example pairs an
egocentric RGB observation and language instruction with a G1 kinematic trajectory.


evaluation, and the practical considerations required for real-world deployment, including motion-
blur handling and system-level profiling.

B.1   VLK Training Loss Details

Training Objective. We initialize the VLK policy from a pretrained π0.5 [39] and fine-tune the
full model on our generated vision-language-kinematics dataset. We adapt the action space of the
pretrained model to our G1 kinematic representation.
We train the policy with an x0 -prediction objective in a flow-matching formulation. Given a ground-
truth future trajectory xt+1:t+H , Gaussian noise ϵ, and interpolation coefficient α, we construct the
noisy trajectory
                                 xαt+1:t+H = αϵ + (1 − α)xt+1:t+H .

The policy predicts the clean trajectory conditioned on the noisy trajectory, interpolation coefficient,
current egocentric observation, task instruction, and current G1 kinematic state:

                                        x̂t+1:t+H = πθ (xα
                                                         t+1:t+H , α, ot , ℓ, xt ).

The primary trajectory reconstruction loss is
                                                                                         2
                                          Ltraj = ∥x̂t+1:t+H − xt+1:t+H ∥2 .


                                                                 16

## Page 17

Auxiliary Losses. To improve physical consistency and execution quality, we introduce auxil-
iary objectives for foot-floor contact prediction, accumulated root-trajectory consistency, forward-
kinematics accuracy, and foot-skating regularization.
Foot-floor contact loss. We predict foot-floor contact labels to identify stance phases used by the
foot-skating regularizer. Since contact events are sparse, we supervise the predicted foot-contact
labels using a focal loss:
                                Lfoot-contact = FocalLoss(m̂, m),
where m̂ and m denote the predicted and ground-truth foot-contact labels.
Accumulated root-trajectory loss. The trajectory representation parameterizes root motion using
relative displacements. We integrate the predicted root displacements to recover the global root
trajectory and penalize accumulated drift:
                                                    H
                                                1 X root          2
                                  Lacc-root =       p̂t+k − proot
                                                             t+k 2 .
                                                H
                                                   k=1

Forward-kinematics loss. We apply forward kinematics to the predicted joint angles and supervise
the resulting ankle and wrist positions:
                                            Lfk = Lankle
                                                   fk    + Lwrist
                                                            fk    ,
where
                     H            2                                         H               2
               1 XX j                                                   1 XX
   Lankle
    fk    =         p̂t+k − pjt+k ,                         Lwrist
                                                             fk    =         p̂jt+k − pjt+k .
              H|A|                2                                    H|W|                 2
                    k=1 j∈A                                                k=1 j∈W
Here, A and W denote the ankle and wrist end-effectors, respectively.
Foot-skating regularization loss. To discourage unrealistic foot sliding during stance phases, we
penalize horizontal foot velocity when a foot is predicted to be in contact with the ground:
                                                   H          2
                                             1 XX j      j,xy
                                  Lfoot =         m̂t+k vt+k    ,
                                            H|F |             2
                                                  k=1 j∈F

where F denotes the foot end-effectors, m̂jt+k is the predicted foot-contact label for foot j, and vt+k
                                                                                                    j,xy

is the corresponding foot velocity projected onto the ground plane.
The final training objective is
   Ltotal = 1.0 Ltraj + 0.5 Lfoot-contact + 0.2 Lacc-root + 1.0 Lankle
                                                                 fk    + 1.0 Lwrist
                                                                              fk    + 0.05 Lfoot .

B.2   Metric for Evaluation in Simulation

While the RL tracking controller is trained in IsaacLab [44], we perform sim2sim evaluation in
MuJoCo. During evaluation, the simulator is paused while the VLK policy performs trajectory
inference at the end of each motion chunk, avoiding the need for real-time chunked execution. For
each task mode, we hold out 10% of the synthesized trajectories (1000 trajectories per mode) for
evaluation. The humanoid is initialized from the initial state of each held-out trajectory and evaluated
on whether it can successfully complete the corresponding language-conditioned task.
For “Walk To” tasks, a rollout is considered successful if the humanoid reaches the specified target
object or box, stops within 0.5 m of the target, and avoids colliding with or penetrating the target
geometry.
For “Turn Around” tasks, success requires the humanoid to perform a clear turning motion toward
the instructed direction, rather than remaining stationary or continuing forward motion.
For “Pick Up” tasks, the humanoid must successfully grasp a box placed either on the floor or on
top of an object and maintain stable holding for at least 20 consecutive frames.
For “Put Down” tasks, success is defined as the humanoid reaching the specified target object and
successfully placing the carried box onto the target surface or floor.


                                                       17

## Page 18

B.3   Motion Blur Handling During Deployment

During training.    We augment a subset of RGB observations with synthetic motion blur:
                                    I ′ = Bσ (I),          σ ∼ p(σ),
where I is the original image, Bσ denotes the blur operator with magnitude σ, and p(σ) is restricted
to a small range to preserve semantic scene content while improving robustness to mild blur artifacts.

During deployment.      We maintain an image buffer covering a 0.3 s window. Given buffered can-
didate frames                       n                         o
                                        (1) (2)          (N )
                                      It , It , . . . , It      ,
the system selects the sharpest frame according to the variance of the Laplacian:
                                        S(I) = Var ∇2 I ,
                                                          

where ∇2 I denotes the image Laplacian operator. The selected observation is
                                                     
                                                       (i)
                                   It∗ = arg max S It .
                                                     (i)
                                                    It

The resulting frame is then passed to the VLK policy for inference.

B.4   System Overview and Profiling

We deploy the VLK policy on the physical Unitree G1 with a multi-process runtime that decou-
ples high-rate whole-body control from lower-rate vision-language inference. Figure 7 shows the
architecture. Three concurrent processes run on a tethered laptop—a state estimator, a whole-body
tracker, and a VLK inference client—and communicate through shared memory and inter-process
queues. The inference client streams the latest egocentric image and robot kinematic state to an ex-
ternal GPU server, which performs the flow-matching trajectory sampling, and merges the returned
kinematic chunks into the tracker’s reference stream.

Whole-body tracking loop. The tracker runs at 50 Hz on an RTX 5000 Ada. Each tick reads robot
proprioception, fetches the latest root pose from the state estimator, splices any newly returned VLK
kinematic chunk into the active reference, runs the RL tracking policy, and sends joint-level PD
targets to the robot. Across our deployments, the per-tick computation averages 4.3 ms, with no
missed deadlines observed over a full task rollout.

VLK inference loop. A separate inference client maintains the most recent egocentric RGB frame
from the ZED 2i and the most recent robot state in shared memory. Each replan packs the obser-
vation, sends it to the external GPU server over a websocket, receives a predicted H = 30-frame
kinematic chunk (one second of future motion at 30 Hz), and converts the canonical-frame predic-
tion into world-frame motion references via forward kinematics. Predicted chunks overlap by 10
frames (Section 3.4) and are consumed by the 50 Hz tracker as a streaming reference rather than
re-predicted every control tick. On the RTX 5090, VLK inference itself takes 31 ms, and the end-to-
end replan—including websocket transport, input packing, and post-processing—averages ∼ 63 ms
(Table 4); since each chunk covers 1 s of motion, this leaves ample headroom and chunks do not
accumulate.

Asynchronous chunk merging. Because chunks are produced asynchronously while the tracker
runs at 50 Hz, a freshly arrived chunk is spliced into the active reference with a 10-frame overlap
(Section 3.4). The merge step contributes ∼ 3.4 ms to the tracker tick on which a new chunk lands
and early-returns otherwise, keeping the tracker comfortably within its 50 Hz schedule.




                                                    18

## Page 19

Unitree G1                                                ZED 2i Camera




                                                          proprioception            joint targets                                             RGB image

          Tethered Laptop
                                                                                                      robot state
                                                                 Whole-Body Tracker
                            State Estimator   root pose                                                                      VLK Inference Client
                                                                     RL tracking policy

                                                                                                    kinematic chunk

                                  50 Hz                           50 Hz • RTX 5000 Ada                                streams 1 s (30-frame) chunks to tracker



                                                                                                             image + state          websocket            predicted chunk




                                                                                                                             External GPU Server
                                                                                                                      VLK flow-matching sampling • 31 ms

                                                                                                                             RTX 5090 • Triton backend


     On-laptop CPU loop
     On-laptop inference client
     External GPU server
     Hardware



Figure 7: Deployment system overview. Three concurrent on-robot processes (blue: state estima-
tion and whole-body tracking; orange: VLK inference client) communicate through shared mem-
ory and inter-process queues. The client offloads flow-matching sampling to a remote VLK server
(green) over a websocket. The whole-body tracker runs at 50 Hz and emits joint-level PD targets,
while the inference loop replans at ∼ 1.8 Hz; predicted kinematic chunks are spliced into the active
reference with a 10-frame overlap.




Table 4: End-to-end VLK replan latency breakdown, averaged across one deployment. The total
of ∼ 63 ms is well below the ∼ 555 ms replan period, leaving ∼ 8.8× headroom against backlog
formation.
                           Stage                                                                      Latency (ms)                     Share
                           Image fetch from camera buffer                                                               5.4               9%
                           Observation packing (state norm. + image enc.)                                               7.5              12%
                           Server roundtrip + GPU flow-matching sampling                                               37.0              59%
                           Output denormalization                                                                       4.2               7%
                           World-frame transform + forward kinematics                                                   7.2              11%
                           Reference merge into tracker stream                                                          3.4               5%
                           Total                                                                                       63.0           100%




                                                                       19
