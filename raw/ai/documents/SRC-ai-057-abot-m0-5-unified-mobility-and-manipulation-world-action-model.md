---
source_id: "SRC-ai-057"
title: "ABot-M0.5 Unified Mobility-and-Manipulation World Action Model"
source_type: "paper"
publisher: "arXiv"
source_date: "2026-07-01"
url: "https://arxiv.org/html/2607.00678"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-07-07T01:22:36+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-ai-057
---
# ABot-M0.5 Unified Mobility-and-Manipulation World Action Model

See [Contributions](#S7 "7 Contributions ‣ 6 Conclusion and Future Work ‣ Experimental Results ‣ 5.5 Real-World Experiments ‣ Summary ‣ 5.4 Ablation Studies ‣ Generalization beyond mobile manipulation ‣ 5.3 Results on Manipulation Benchmarks ‣ Qualitative Analysis ‣ Discussion ‣ Main Comparison ‣ 5.2 Main Results on Mobile Manipulation ‣ 5 Experiments ‣ ABot-M0.5: Unified Mobility-and-Manipulation World Action Model") section for a full author list.

AMAP CV Lab

###### Abstract

Mobile manipulation is a key capability for general-purpose robots, yet remains challenging for current embodied learning methods. VLA policies are typically reactive and lack explicit world modeling, while existing World Action Models (WAMs) are still poorly aligned with the structure of mobile manipulation: they operate on coarse video chunks, model entangled navigation-manipulation actions, and train inverse dynamics under supervision that does not match autoregressive inference. As a result, they often miss fine-grained contact dynamics, suffer from action-distribution conflicts, and accumulate errors over long-horizon rollouts.

We propose ABot-M0.5, a new WAM built on the insight that mobile manipulation requires alignment at three levels: temporal granularity, action space, and train-test consistency. To align temporal granularity, we introduce intermediate latent actions that capture local visual state transitions and serve as an bridging action space between video latents and embodiment-specific controls. To align action space, we design a dual-level Mixture-of-Transformers architecture that disentangles both modality representations and heterogeneous action subspaces such as base movement and arm manipulation. To align inference conditions, we propose the dream-forcing training strategy that progressively trains inverse dynamics on model-predicted videos, improving train-test alignment and robustness during autoregressive prediction.

Experiments on challenging mobile and fine-grained manipulation benchmarks demonstrate that ABot-M0.5 achieves state-of-the-art performance in both long-horizon task success and fine-grained control accuracy. These results highlight the critical importance of granularity-aligned, action-disentangled, and inference-consistent world-action modeling.

Date: July 1, 2026

Code: [https://github.com/amap-cvlab/ABot-Manipulation](https://github.com/amap-cvlab/ABot-Manipulation)

![[Uncaptioned image]](https://arxiv.org/html/2607.00678v1/figure/ABot-M0.5-7.png)

\[Uncaptioned image\]

## 1 Introduction

![Refer to caption](https://arxiv.org/html/2607.00678v1/x1.png)

Figure 1: Overview of ABot-M0.5. ABot-M0.5 is a granularity-aligned, action-disentangled, and train-test-consistent world-action model for mobile manipulation. Top: The 3-stage training pipeline (Pretrain, SFT1, SFT2 ) progressively improves the model. The final Dream-Forcing stage (SFT2) uses model-predicted videos to train inverse dynamics, significantly boosting robustness. Left & Center: To solve structural mismatches, we design a Video → \\rightarrow Latent Action Action pipeline for temporal alignment, and use a dual-level architecture to decouple different action spaces (e.g., base movement and arm manipulation), making the framework adaptable to diverse robot embodiments. Right: ABot-M0.5 achieves state-of-the-art performance on both simulation benchmarks (radar chart) and real-world mobile manipulation tasks (bar charts). Bottom: Real-world execution sequences (e.g., Arrange Flower, Find Toaster) show successful long-horizon mobile manipulation, where blue and green colors distinguish the navigation and manipulation phases.

Mobile manipulation is a defining capability for general-purpose robots: a capable embodied agent must not only manipulate objects, but also navigate through cluttered environments, maintain long-horizon task context, and execute precise interactions under changing viewpoints and scene dynamics \[szot2022habitat20traininghome, yenamandra2024homerobotopenvocabularymobilemanipulation, li2024behavior1khumancenteredembodiedai, huo2026abot\]. Despite rapid recent progress in embodied AI, current embodied learning paradigms still fall short of this goal. Reactive Vision-Language-Action (VLA) policies lack explicit world modeling and long-horizon memory \[brohan2023rt2, kim2024openvla, black2026pi0visionlanguageactionflowmodel, intelligence2025pi05visionlanguageactionmodelopenworld, intelligence2026pi07steerablegeneralistrobotic\], while emerging world-model-based methods, though promising, are still not structured in a way that matches the demands of mobile manipulation \[ye2026worldactionmodelszeroshot, bi2025motusunifiedlatentaction, ha2018worldmodels, hafner2024dreamerv3\].

The central limitation is not merely insufficient model scale, but a structural mismatch between current world-action learning methods and the requirements of mobile manipulation. Effective mobile manipulation requires alignment at three levels. First, temporal granularity must be aligned, since coarse video prediction must ultimately support fine-grained, step-level control; otherwise, subtle but crucial dynamics such as contact onset, grasp closure, and alignment correction are easily blurred or lost \[hafner2024dreamerv3\]. Second, action space must be aligned, since navigation and manipulation follow fundamentally different dynamics—for example, low-frequency global base motion versus high-frequency local arm control—yet are often optimized within a single entangled action space, leading to interference and suboptimal specialization \[brohan2023rt1, brohan2023rt2\]. Third, train-test consistency must be aligned, since actions at deployment time are conditioned on the model’s own predicted future observations rather than ground-truth futures, creating train-test mismatch and compounding errors over long autoregressive rollouts \[ye2026worldactionmodelszeroshot, li2026causalworldmodelingrobot, ha2018worldmodels, hafner2024dreamerv3\].

ABot-M0.5 is designed around this alignment principle. Rather than addressing these issues as isolated patches, it provides a unified framework for alignment-aware world-action learning in mobile manipulation. To align temporal granularity, ABot-M0.5 introduces frame-level latent actions between video latents and robot actions, forming a fine-grained intermediate action space that captures local visual state transitions and is less tied to any specific embodiment. This factorizes the direct video-to-action mapping into a video-to-latent-action-to-action pipeline, allowing the model to recover motion intent from coarse visual dynamics and translate it into executable low-level control. To align action structure, ABot-M0.5 adopts a dual-level Mixture-of-Transformers architecture that disentangles both modality-specific representations and heterogeneous action subspaces, enabling base motion and arm manipulation to be modeled separately within a unified system. To align inference conditions, ABot-M0.5 further employs a Dream Forcing training strategy that exposes inverse dynamics learning to self-dreamed videos, directly aligning the conditioning context of training with that of inference, thus improving robustness to prediction errors.

Extensive experiments on challenging mobile manipulation and manipulation benchmarks show that ABot-M0.5 achieves strong performance in both long-horizon and fine-grained manipulation tasks. These results indicate that progress in mobile manipulation depends not only on scaling model capacity or data volume, but also on aligning world modeling, action abstraction, and deployment-time behavior within a single coherent framework \[ma2026vla\_survey\]. More broadly, they point to a practical path for extending WAMs from stationary manipulation to mobile manipulation.

Our main contributions are as follows:

- We identify three core structural bottlenecks that limit existing WAMs in mobile manipulation: temporal granularity mismatch between coarse video prediction and fine-grained control, action structure mismatch between heterogeneous mobility and manipulation behaviors, and context mismatch between training and autoregressive inference.
- We propose ABot-M0.5, a new WAM architecture for mobile manipulation that addresses these bottlenecks through intermediate latent actions, a dual-level Mixture-of-Transformers design, and Dream Forcing, enabling fine-grained motion abstraction, structured action decoupling, and train-test consistent inverse dynamics learning.
- We demonstrate strong results on challenging mobile manipulation and manipulation benchmarks, with clear gains in long-horizon task success and fine-grained manipulation accuracy, and validate the contribution of each component through extensive ablations.

## 2 Alignment-Aware World-Action Learning

This section formalizes mobile manipulation as an alignment-aware world-action learning problem. Rather than treating mobile manipulation as a simple long-horizon extension of stationary manipulation, we view it as a setting in which world modeling, action modeling, and deployment-time rollout must be jointly aligned. This perspective provides a unified explanation for why current embodied learning methods struggle in mobile manipulation, and motivates the design of ABot-M0.5 in the next section.

### 2.1 Problem Setting

We consider language-conditioned mobile manipulation tasks in which a robot must execute long-horizon behaviors by jointly performing navigation and object interaction in visually complex environments \[szot2022habitat20traininghome, yenamandra2024homerobotopenvocabularymobilemanipulation, li2024behavior1khumancenteredembodiedai\]. At each time step $t$, the agent receives a language instruction $l$, a multi-view visual observation $o_{t}$, and optionally a history of past observations and actions. The goal is to generate low-level executable actions $a_{t}$ that complete the task over an extended horizon while remaining consistent with future world evolution.

Formally, let $o_{t}=\{I_{t}^{(1)},\dots,I_{t}^{(N_{c})}\}$ denote the multi-view observation at time $t$, where $N_{c}$ is the number of cameras and $I_{t}^{(i)}$ is the image captured by the $i$ -th camera. Given an observation history $o_{\leq t}$, an action history $a_{<t}$, and a language instruction $l$, the policy aims to predict future behavior over a horizon $H$. In reactive policies, this is often formulated as a direct conditional mapping over a chunk size $H$ \[brohan2023rt1, kim2024openvla, black2026pi0visionlanguageactionflowmodel, Diffusionpolicy\]:

$$
a_{t:t+H-1}\sim\pi(\cdot\mid o_{\leq t},a_{<t},l).
$$

Such a formulation is effective when the required action mainly depends on the current observation and the temporal horizon is short. However, it becomes increasingly brittle in mobile manipulation, where future decisions depend not only on the current state, but also on how the environment is expected to evolve under the robot’s own future actions.

World Action Models (WAMs) address this limitation by jointly modeling future observations and future actions \[ye2026worldactionmodelszeroshot, bi2025motusunifiedlatentaction, yuan2026fastwamworldactionmodels, ye2026gigaworldpolicyefficientactioncenteredworldaction, li2026causalworldmodelingrobot\]. Let $z_{t+1:t+H}$ denote the compressed video latent of the future observations over the time horizon $t+1:t+H$. Instead of directly predicting actions from the current observation, a WAM models a structured future trajectory:

$$
(z_{t+1:t+H},a_{t:t+H-1})\sim p(\cdot\mid o_{\leq t},a_{<t},l).
$$

This formulation introduces explicit future world modeling and provides a natural interface for long-horizon rollout, since future prediction and action prediction are embedded in the same autoregressive process.

However, directly applying existing WAM formulations to mobile manipulation remains insufficient. Mobile manipulation differs from stationary manipulation in at least three ways. First, future world evolution spans larger viewpoint changes and more diverse scene transitions due to robot movement. Second, the action space becomes heterogeneous, since both mobility and manipulation must be generated within a single policy. Third, rollout robustness becomes more important, because long-horizon mobile tasks amplify small prediction errors over time.

These differences suggest that mobile manipulation should not be viewed merely as a larger version of stationary manipulation. Instead, it should be treated as a world-action learning problem with stricter structural requirements on representation, control, and rollout.

To make this explicit, the core challenge in mobile manipulation lies in bridging two fundamentally different spaces: the coarse, long-term future video latents $z_{t+1:t+H}$ that capture global world evolution, and the fine-grained, heterogeneous executable robot actions $a_{t:t+H-1}$. Directly mapping the video latent to executable robot action is notoriously difficult due to the severe granularity and semantic gaps between them. For notational simplicity in the following text, we will abstract away the explicit horizon $H$ and denote $z_{t+1{:}t+H}$ and $a_{t{:}t+H-1}$ simply as $z_{t+1}$ and $a_{t}$, respectively.

Ideally, a successful mobile manipulation policy should learn a coherent hierarchical process: it must first anticipate how the visual world will evolve ($z_{t+1}$), then distill this macroscopic evolution into frame-level intermediate motion intents that capture local visual state transitions, and finally ground these intents into embodiment-specific low-level controls ($a_{t}$). Formally, this desired hierarchy can be conceptualized as:

$$
\text{Video Latent }z_{t+1}\rightarrow\underbrace{\text{Frame-level Motion Intents}}_{\text{Bridging Space}}\rightarrow\text{Robot Action }a_{t},
$$

where the intermediate bridging space serves as the crucial link connecting future world dynamics with fine-grained physical execution. However, how to effectively define, learn, and align this intermediate space remains an open question. In the next section, we will address this by introducing latent actions to instantiate this bridging space, along with tailored architectures and training strategies to achieve full alignment.

### 2.2 Core Bottlenecks in Mobile Manipulation

Under the formulation above, the key limitation of existing methods is not merely insufficient model scale, but a structural mismatch between how current WAMs are trained and the requirements of mobile manipulation \[ye2026worldactionmodelszeroshot, bi2025motusunifiedlatentaction, yuan2026fastwamworldactionmodels\]. We identify three core bottlenecks.

#### Temporal Granularity Mismatch

Existing WAMs typically model future observations in temporally compressed chunks. This design is computationally efficient and suitable for long-horizon video prediction, but it creates a mismatch between the temporal granularity of world modeling and that of control generation. In practice, future video latents may summarize multiple frames within a chunk, whereas robot actions must often be generated at every frame or control step.

This mismatch is especially problematic in mobile manipulation, where fine-grained interactions determine success. Behaviors such as grasp closure, contact onset, object release, fine alignment, and local collision avoidance often unfold over very short temporal windows. When world modeling is performed only at a coarse chunk level, these local transitions may be smoothed out or omitted, making it difficult for the policy to recover the precise motion intent required for execution.

#### Action Structure Mismatch

Mobile manipulation introduces a heterogeneous action space that differs substantially from the action space of stationary manipulation. The robot must control both global mobility and local manipulation, and these two forms of behavior obey very different dynamics. Base movement tends to be low-frequency, smooth, and globally oriented. Arm manipulation, by contrast, is higher-frequency, local, and sensitive to contact-rich dynamics. Treating them as a single entangled action space forces the model to optimize over conflicting patterns within one shared representation.

This mismatch has two consequences. First, it increases optimization difficulty. Gradients from mobility-dominated trajectories and manipulation-dominated trajectories may interfere, preventing the model from specializing to either mode effectively. Second, it weakens compositionality. In many mobile manipulation tasks, base control and arm control must coordinate while remaining structurally distinct.

#### Rollout Condition Mismatch

A third bottleneck arises from the discrepancy between how inverse dynamics is trained and how actions are actually generated at inference time. During training, inverse dynamics is usually conditioned on ground-truth future observations or their latent representations. During inference, however, such ground-truth futures are unavailable. The model must instead act based on its own predicted visual rollouts, which inevitably contain noise, uncertainty, and sometimes severe errors such as blurring, object drift, or hallucinated content.

This train-test mismatch creates a form of exposure bias in world-action learning, related to the distribution-shift studied in sequence prediction and imitation learning \[bengio2015scheduledsamplingsequenceprediction, ross2011reductionimitationlearningstructured\]. The inverse dynamics model is optimized under ideal future conditions, but deployed under imperfect self-generated futures. In long-horizon mobile manipulation, the discrepancy compounds over time and can eventually derail execution.

#### Summary

These three bottlenecks reveal a shared pattern: current methods are insufficiently aligned with the structure of mobile manipulation. Coarse visual prediction is misaligned with fine control, entangled action learning is misaligned with heterogeneous robot behavior, and ground-truth-conditioned training is misaligned with autoregressive deployment. ABot-M0.5 is designed around this observation. The next section presents the full model, including latent actions for temporal alignment, a dual-level Mixture-of-Transformers for structured action modeling, and Dream-Forcing for rollout-aligned inverse dynamics learning.

## 3 The ABot-M0.5 Model

This section details the architecture of ABot-M0.5. Guided by the alignment perspective introduced in Section˜2, our model directly addresses the three structural bottlenecks in mobile manipulation: temporal granularity mismatch, action structure mismatch, and train-test condition mismatch. At a high level, ABot-M0.5 factorizes world-action learning into a hierarchical cascade: it first predicts future visual dynamics, refines them into frame-level motion intents, and finally generates embodiment-specific executable actions.

### 3.1 Overall Architecture and Notation

ABot-M0.5 is a video-action World Action Model built upon the Wan2.2 video diffusion backbone \[wan2025wanopenadvancedlargescale\]. Given a language instruction $l$ and a sequence of multi-view observations, it jointly models future video latents, frame-level latent actions, and executable robot actions within a unified generative framework.

At the perception stage, a 3D VAE compresses continuous video observations $o_{t}=\{I_{t}^{(1)},\dots,I_{t}^{(N_{c})}\}$ into compact spatiotemporal video latents $z_{t}$, while a text encoder (e.g., UMT5) maps $l$ into conditional features. Crucially, we introduce a frame-level latent action $m_{t}$ to capture local visual state transitions, serving as a bridging representation between coarse video latents and fine-grained control. The generation process follows a structured cascade over clean (noise-free) variables:

$$
z_{t+1}\rightarrow m_{t}\rightarrow a_{t},
$$

where $z_{t+1}$, $m_{t}$, and $a_{t}$ denote the clean future video latent, clean latent action, and clean executable action, respectively. This factorization decomposes direct video-to-action prediction into three distinct stages: world modeling, motion abstraction, and control generation.

Table 1: Main notation used in ABot-M0.5.

| Symbol | Meaning | Symbol | Meaning |
| --- | --- | --- | --- |
| $t$ | Time step | $o_{t}$ | Raw multi-view observation |
| $I_{t}$ | Raw frame | $z_{t+1}$ | Video latent |
| $m_{t}$ | Frame-level latent action | $a_{t}$ | Executable robot action |
| $a_{t}^{\mathrm{move}}$ | Mobility action | $a_{t}^{\mathrm{manip}}$ | Manipulation action |
| $H$ | Prediction horizon | $N_{c}$ | Number of cameras |
| $X_{t}$ | Token | $\hat{z}_{t+1}$, $\hat{m}_{t}$,$\hat{a}_{t}$ | Dreamed latents |
| $l$ | Language instruction | $\tilde{z}_{t+1}$, $\tilde{m}_{t}$, $\tilde{a}_{t}$ | Noisy latents |
| $\tau$ | Diffusion time step ($\tau\in[0,1]$) | $p_{z},p_{m},p_{a}$ | Latent distributions |

To optimize this hierarchical cascade, we employ Conditional Flow Matching (CFM) as the unified generative objective across all stages. Taking the first stage (world modeling) as an example, given the ground-truth clean video latent $z_{t+1}$ and standard Gaussian noise $\epsilon\sim\mathcal{N}(0,I)$, we construct a conditional probability path at time step $\tau\sim\mathcal{U}(0,1)$. The video prediction objective is defined as:

$$
\mathcal{L}_{\mathrm{z}}=\mathbb{E}_{z_{t+1},\epsilon,\tau}\left[\left\|v_{\theta}^{z}\big(z_{t+1}^{\tau};z_{<t+1},m_{<t},a_{<t},\tau,l\big)-(z_{t+1}-\epsilon)\right\|_{2}^{2}\right],
$$

where $z_{t+1}^{\tau}=\tau z_{t+1}+(1-\tau)\epsilon$ is the interpolated state, and $v_{\theta}^{z}$ is the network regressing the target velocity field. Crucially, the conditioning context for $z_{t+1}$ strictly includes only historical states ($z_{\leq t},m_{<t},a_{<t}$) and the language instruction $l$. The subsequent stages (predicting $m_{t}$ and $a_{t}$) follow analogous CFM objectives, but with progressively expanded receptive fields conditioned on the previously generated variables in the cascade (e.g., conditioning $m_{t}$ on the predicted $z_{t+1}$). This mathematically guarantees that the training-time information flow perfectly mirrors the autoregressive generation order used at inference.

Architecturally, the model processes three parallel token streams:

$$
X_{t}=[X_{t+1}^{z},X_{t}^{m},X_{t}^{a}],
$$

where $X_{t+1}^{z}$, $X_{t}^{m}$, and $X_{t}^{a}$ correspond to video latent tokens, latent action tokens, and action tokens. To reflect the causal dependencies dictated by the above conditional objectives, we enforce an asymmetric information flow: video latent tokens ($X_{t+1}^{z}$) are masked from attending to latent action tokens ($X_{t}^{m}$), as future motions are inherently unknown during video prediction. Conversely, action tokens ($X_{t}^{a}$) explicitly attend to $X_{t}^{m}$, ensuring that final control is grounded in fine-grained motion intentions.

To realize this alignment, the architecture integrates three key mechanisms, which are detailed in the subsequent subsections: (1) an Intermediate Latent Action Modeling module that bridges the temporal granularity gap; (2) a Dual-level Mixture-of-Transformers (D-MoT) that structurally decouples heterogeneous action subspaces (e.g., base mobility vs. arm manipulation) while maintaining modality-specific optimization; and (3) a Dream Forcing Mechanism that exposes the action stream to self-generated visual predictions, fundamentally resolving the train-test distribution shift.

Figure˜2 illustrates the overall architecture of ABot-M0.5 and Table˜1 summarizes the core notation. The remainder of this section elaborates on the design and implementation of these three core components.

![Refer to caption](https://arxiv.org/html/2607.00678v1/x2.png)

Figure 2: Overall architecture of ABot-M0.5. The model jointly predicts future video latents, frame-level latent actions, and executable actions through a structured, asymmetric cascade design of a dual-level MoT. The Action-Decoupled MoT disentangled action into mobile and manipulation and predict together.

### 3.2 Intermediate Latent Action Modeling

As established in Section˜2.2, directly mapping coarse video latents to low-level actions creates severe temporal and structural mismatches. To resolve this, ABot-M0.5 introduces frame-level latent actions ($m_{0,t}$) as an intermediate, embodiment-agnostic representation. This design factorizes the generation process into a structured three-stage cascade:

$$
\text{Context}\xrightarrow{\text{World Modeling}}z_{t+1}\xrightarrow{\text{Motion Abstraction}}m_{t}\xrightarrow{\text{Control Decoding}}a_{t}.
$$

Specifically, the model first predicts future video latents $z_{t+1}$ to capture macroscopic environmental evolution (Stage 1). It then refines these coarse dynamics into frame-level latent actions $m_{t}$ to represent fine-grained motion intents (Stage 2). Finally, it translates these intents into embodiment-specific executable actions $a_{t}$ (Stage 3). By explicitly modeling this hierarchy, the system decouples embodiment-agnostic physical priors from hardware-specific kinematics, enabling robust generalization across heterogeneous robot platforms.

#### Latent Action Extraction and Alignment

A key advantage of latent actions is that they depend solely on visual state transitions, enabling extraction from large-scale, action-free video datasets without requiring robot kinematic labels \[ye2025latentactionpretrainingvideos, liang2025clamcontinuouslatentaction, tang2026alam\]. Given consecutive frames $(I_{t},I_{t+1})$, we utilize a frozen, pretrained latent action encoder $E_{m}$ to extract local motion representations:

$$
m_{t}=E_{m}(I_{t},I_{t+1})\in\mathbb{R}^{d_{m}},
$$

where $d_{m}$ is the feature dimension. In multi-camera setups, we extract latent actions from each view and organize them into a unified spatiotemporal tensor. For a chunk with $H$ control steps and $N_{c}$ camera views, the aggregated latent action tensor is structured as $M=\{m_{t}^{view}\}\in\mathbb{R}^{H\times N_{c}\times d_{m}}$.

Under this formulation, similar physical interactions (e.g., grasping an object) are mapped to proximate regions in the shared latent action space $\mathcal{M}$, regardless of the underlying robot morphology. This alignment is crucial for transferring physical priors across diverse embodiments.

#### Conditional Flow Matching for Latent Actions

We formulate the generation of latent actions as a Conditional Flow Matching (CFM) problem, a simulation-free objective increasingly adopted in continuous-action robot policies \[lipman2023flowmatchinggenerativemodeling, black2026pi0visionlanguageactionflowmodel, pertsch2025fastefficientactiontokenization, intelligence2025pi05visionlanguageactionmodelopenworld\].

Given the ground-truth clean latent action $m_{t}$ and standard Gaussian noise $\epsilon\sim\mathcal{N}(0,I)$, we construct a conditional probability path at time step $\tau\sim\mathcal{U}(0,1)$. The objective is defined as:

$$
\mathcal{L}_{\mathrm{m}}=\mathbb{E}_{m_{t},\epsilon,\tau}\left[\left\|v_{\theta}\big(m_{t}^{\tau};z_{\leq t+1},m_{<t},a_{<t},\tau,\,l\big)-(m_{t}-\epsilon)\right\|_{2}^{2}\right],
$$

where $m_{t}^{\tau}=\tau m_{t}+(1-\tau)\epsilon$ is the interpolated state, and $v_{\theta}$ is the neural network regressing the target velocity field.

This loss supervises the model to synthesize high-fidelity latent actions through iterative denoising. By training exclusively on visual transitions conditioned on anticipated world dynamics, the model captures fine-grained, embodiment-agnostic motion intents that robustly guide the downstream control decoder.

### 3.3 Dual-Level Mixture-of-Transformers

While latent actions address the temporal granularity mismatch between world modeling and control, mobile manipulation also requires structured handling of heterogeneous action dynamics. To this end, ABot-M0.5 introduces a Dual-level Mixture-of-Transformers (D-MoT) architecture that disentangles heterogeneity at both the modality level and the action level.

#### Modality-Level Disentanglement

The first level of D-MoT operates across the three parallel token streams: video latents ($X^{z}$), latent actions ($X^{m}$), and executable actions ($X^{a}$). Although these streams share the same Transformer trunk for cross-modal reasoning, they differ fundamentally in semantics and temporal roles. To prevent representational collapse, each modality is equipped with its own dedicated input projection, timestep embedding, and output head. This design ensures that the model maintains distinct representational spaces for world dynamics, motion intents, and hardware control, while still enabling flexible information exchange through shared self-attention layers.

#### Action-Level Disentanglement

The second level of D-MoT operates strictly within the executable action stream ($X^{a}$). In mobile manipulation, the action vector $a_{t}$ inherently contains both mobility and manipulation dimensions, which exhibit distinct temporal frequencies and physical loss landscapes. Jointly predicting them with a single homogeneous head often leads to gradient interference, where the high-frequency manipulation signals dominate or destabilize the low-frequency mobility predictions.

To address this challenge, we explicitly decouple the action space $a_{t}$ into two distinct subspaces: manipulation $a_{t}^{manip}$ and mobility $a_{t}^{move}$. Specifically, as shown in Figure˜3, we enforce a strict channel-to-subtower assignment, where each sub-tower is equipped with its own dedicated feed-forward network (FFN) and prediction head. This design enables each sub-tower to specialize in its dedicated action space, ensuring strictly decoupled learning dynamics between base mobility and arm manipulation.

#### Structured Joint Attention

Despite the strict decoupling in the feed-forward layers, the model must still support coordinated reasoning between movement and manipulation (e.g., base repositioning directly affects grasp feasibility). To achieve this, D-MoT employs joint self-attention over the concatenated token streams at each layer. Under carefully designed causal and conditional masks, latent-action, mobility-action, and manipulation-action tokens participate in unified attention computation, while their subsequent FFN transformations remain branch-specific. This provides structured specialization without sacrificing cross-subspace coordination.

#### Subspace-Aware CFM Supervision

We supervise the final action generation stage via conditional flow matching (CFM). To stabilize learning and prevent error accumulation across the cascade, we adopt a teacher-forced upstream conditioning protocol during training, where the action decoder receives ground-truth video latents $z_{\leq k+1}$ and latent actions $m_{\leq k}$. Furthermore, we make the noisy actions within the same chunk mutually visible to enable cross-subspace coordination. To maintain train-test consistency and improve inference efficiency, both subspaces share a single denoising timestep, aligning with the parallel joint denoising procedure at inference time and eliminating the need for separate noise schedules.

Formally, at time $t$, the model predicts executable actions conditioned on the teacher-forced upstream representations and clean historical actions $a_{<t}=\{a_{j}^{\mathrm{move}},a_{j}^{\mathrm{manip}}\}_{j<t}$. We sample a shared denoising timestep $\tau\in[0,1]$ for both action subspaces and independently draw Gaussian noises $\epsilon^{\mathrm{move}},\epsilon^{\mathrm{manip}}\sim\mathcal{N}(0,I)$. The noisy mobility and manipulation actions are constructed as:

$$
a_{t}^{\mathrm{move},\tau}=\tau a_{t}^{\mathrm{move}}+(1-\tau)\epsilon^{\mathrm{move}},\quad a_{t}^{\mathrm{manip},\tau}=\tau a_{t}^{\mathrm{manip}}+(1-\tau)\epsilon^{\mathrm{manip}}.
$$

The CFM objectives for the two branches are then defined as:

$$
\mathcal{L}_{\mathrm{a}}^{\mathrm{move}}=\mathbb{E}_{a_{t}^{\mathrm{move}},\epsilon^{\mathrm{move}},\tau}\left[\left\|v_{\theta}^{\mathrm{move}}\left(a_{t}^{\mathrm{move},\tau};z_{\leq t+1},m_{\leq t},a_{<t},a_{t}^{\mathrm{manip},\tau},\tau,l\right)-\left(a_{t}^{\mathrm{move}}-\epsilon^{\mathrm{move}}\right)\right\|_{2}^{2}\right],
$$

$$
\mathcal{L}_{\mathrm{a}}^{\mathrm{manip}}=\mathbb{E}_{a_{t}^{\mathrm{manip}},\epsilon^{\mathrm{manip}},\tau}\left[\left\|v_{\theta}^{\mathrm{manip}}\left(a_{t}^{\mathrm{manip},\tau};z_{\leq t+1},m_{\leq t},a_{<t},a_{t}^{\mathrm{move},\tau},\tau,l\right)-\left(a_{t}^{\mathrm{manip}}-\epsilon^{\mathrm{manip}}\right)\right\|_{2}^{2}\right],
$$

where each branch takes the noisy action of the other branch as input, enabling cross-subspace coordination. The overall action objective is a weighted sum:

$$
\mathcal{L}_{\mathrm{a}}=\lambda_{\mathrm{move}}\mathcal{L}_{\mathrm{a}}^{\mathrm{move}}+\lambda_{\mathrm{manip}}\mathcal{L}_{\mathrm{a}}^{\mathrm{manip}},
$$

where $\lambda_{\mathrm{move}}$ and $\lambda_{\mathrm{manip}}$ balance the contributions of the two subspaces. Together, this subspace-aware CFM supervision closes the final stage of the $z_{t+1}\rightarrow m_{t}\rightarrow a_{t}$ cascade. By grounding action denoising in both anticipated world dynamics and fine-grained motion intents while maintaining cross-subspace information flow, the model is encouraged to produce temporally coherent and physically plausible action chunks.

![Refer to caption](https://arxiv.org/html/2607.00678v1/x3.png)

Figure 3: Dual-level Mixture-of-Transformers. The architecture disentangles modality-specific representations and heterogeneous action subspaces while preserving coordinated reasoning through shared attention. We omit the video and latent action expert for clarity.

### 3.4 Dream Forcing for Train-Test Aligned Action Prediction

![Refer to caption](https://arxiv.org/html/2607.00678v1/x4.png)

Figure 4: Training paradigms for World Action Models. Existing WAM training paradigms (a) and (b) suffer from train-test mismatch, as they condition on data distributions absent during inference. (a) In Teacher Forcing, the model is trained to denoise actions conditioned on clean, ground-truth future videos. (b) In Diffusion Forcing, the model jointly denoises future videos and actions with varying timesteps. Although the joint denoising scheme can be adapted for inference, it is difficult to mirror the exact timestep compositions used during training, thereby increasing the learning complexity and exacerbating the distribution gap. (c) Our Dream Forcing conditions action prediction on self-dreamed videos generated by the model itself. This paradigm closely mirrors the inference process, achieving faithful train-test alignment and bridging the distribution gap inherent in prior methods.

#### Train–Test Gap in Action Prediction

Existing world action models (WAMs) mainly follow two training paradigms. The first is teacher-forcing paradigm \[li2026causalworldmodelingrobot, pai2025mimic, feng2025vidar\], where action tokens are denoised conditioned on ground-truth video tokens. The second is diffusion forcing \[ye2026worldactionmodelszeroshot, ye2026gigaworldpolicyefficientactioncenteredworldaction, bi2025motusunifiedlatentaction\], where video and action tokens are jointly denoised within a unified diffusion process.

Despite their effectiveness, we identify a fundamental train-test gap in both paradigms, particularly for action prediction, as illustrated in Figure˜4. In Teacher Forcing (Figure˜4(a)), the action model is trained with access to clean GT video latents \[li2026causalworldmodelingrobot, pai2025mimic, feng2025vidar\]. However, such GT latents are unavailable at inference time; the model must instead condition on self-generated video latents that inevitably contain prediction errors and visual artifacts. This mismatch leads to severe exposure bias \[ning2024elucidating, schmidt2019generalization, huang2026self\], where the action predictor has never been trained to interpret or compensate for its own dreamed visual states, leading to substantially degradation in action generation.

Diffusion forcing (Figure˜4(b)) partially mitigates this issue by exposing action prediction to noisy video latents during training \[ye2026worldactionmodelszeroshot, ye2026gigaworldpolicyefficientactioncenteredworldaction, bi2025motusunifiedlatentaction\]. However, it introduces another form of discrepancy. During training, video and action tokens may appear under diverse and independently sampled noise timesteps, whereas inference follows a specific denoising trajectory whose exact timestep composition is difficult to reproduce. As a result, the model must learn action prediction under a broad set of artificial noise configurations, increasing optimization complexity and still leaving a mismatch between the training distribution and the actual inference-time conditioning context.

To address these limitations, we propose Dream Forcing, a novel training paradigm that directly aligns the conditioning context of training with that of inference. Instead of conditioning action tokens on GT video latents or arbitrarily noised latents, Dream Forcing trains the action predictor on self-dreamed video latents produced by the model itself, as shown in Figure˜4(c). This design exposes the action model to the same type of imperfect visual states it will encounter at inference time, enabling it to learn robust action generation under model-induced prediction errors and thereby substantially reducing the train-test gap.

#### Two-Phase Forwarding Strategy

To implement the Dream Forcing training paradigm, we depart from the conventional approach of jointly optimizing multimodal tokens in a single forward pass. Instead, we introduce a two-phase forward pass strategy that decouples the generation of dreamed latents (Phase A) from the optimization of action prediction (Phase B).

The goal of Phase A is to synthesize the dreamed conditioning latents. Unlike autoregressive forcing methods in video generation \[huang2026self, liu2025rolling, zhu2026causal, cui2025self\] that must sequentially roll out multiple future chunks, our closed-loop robotic setting only requires dreaming the latest future chunk. This is because historical chunks are continually grounded in real-world ground-truth (GT) observations during deployment \[li2026causalworldmodelingrobot\]. Consequently, rather than relying on a time-consuming sequential rollout, we employ a parallel generation strategy that produces all required dreamed latents for a batch in a single forward pass. Furthermore, since standard multi-step diffusion sampling remains computationally prohibitive for on-the-fly latent generation during training, we follow Self Forcing \[huang2026self\] and adopt a few-step denoising procedure to ensure training efficiency.

In Phase B, the model executes a second forward pass to predict actions conditioned on the dreamed latents synthesized in Phase A. Specifically, this shifts the action predictive distribution from the standard Teacher Forcing formulation:

$$
a_{t}\sim p_{a}(\cdot\mid z_{\leq t+1},m_{\leq t},a_{<t},l),
$$

to our Dream Forcing formulation:

$$
a_{t}\sim p_{a}(\cdot\mid\hat{z}_{t+1},z{\leq t},\hat{m}_{t},m{<t},a_{<t},l),
$$

where only the future conditioning latents $z_{t+1},m_{t}$ are replaced with their self-dreamed counterparts $\hat{z}_{t+1},\hat{m}_{t}$. By exposing the action prediction model to imperfect, dreamed visual contexts, Dream Forcing effectively eliminates the train-test distributional gap.

![Refer to caption](https://arxiv.org/html/2607.00678v1/x5.png)

Figure 5: Illustration of two-phase training strategy in Dream Forcing. In Phase A, the model performs a standard forward pass to predict the velocity field, yielding clean dreamed latents z ^ t + 1, m \\hat{z}\_{t+1},\\hat{m}\_{t}, which are sent to Phase B as conditions to conduct a second forward pass to predict the final action a \\hat{a}\_{t}.

Taken together, these components form the core model design of ABot-M0.5. Intermediate Latent Action Modeling address the temporal gap between world modeling and control, dual-level MoT addresses heterogeneity in modality and action structure, and Dream Forcing aligns inverse dynamics learning with autoregressive rollout. The next section describes how these components are trained progressively from large-scale pretraining to inference-aligned fine-tuning.

## 4 Training Paradigm

To fully realize the representational and generative potential of ABot-M0.5, we adopt a progressive training paradigm that moves from large-scale world modeling to rollout-consistent action learning. The overall strategy is motivated by the structure of the model itself. Since ABot-M0.5 jointly relies on future video prediction, frame-level latent action abstraction, and executable action generation, effective training must establish these capabilities in stages rather than optimizing them all from scratch under the most difficult rollout setting. We therefore organize training into three phases: large-scale pretraining for world modeling, self-supervised pretraining for latent action extraction, and progressive supervised fine-tuning for inverse dynamics learning. In addition, we introduce system-level optimizations to support efficient long-sequence video-action training.

### 4.1 Pretraining Data

The pretraining corpus of ABot-M0.5 is constructed by combining large-scale public robot datasets with synthetic robotic data. The objective is to provide broad coverage over embodiments, environments, task structures, and manipulation dynamics, so that the model can acquire transferable priors before downstream fine-tuning.

All datasets are standardized into a unified data format for consistent processing, training, and evaluation. Following the data pipeline established in prior ABot work, we aggregate data from the following sources:

- OXE \[embodimentcollaboration2025openxembodimentroboticlearning\]: a large-scale multi-embodiment robotic dataset covering diverse scenes, tasks, and platforms. It provides broad visual and behavioral diversity and serves as a foundational source of embodied experience.
- OXE-AugE \[ji2025oxeauge\]: an augmented extension of OXE designed to improve embodiment diversity, especially for single-arm morphologies.
- Agibot-Beta \[agibotworldcontributors2025agibotworldcolosseolargescale\]: a high-quality dataset with structured task design, coherent action sequences, and long-horizon manipulation trajectories.
- RoboCOIN \[wu2026robocoinopensourcedbimanualrobotic\]: a cross-embodiment dataset emphasizing dual-arm manipulation and hierarchical task structure.
- RoboMind \[wu2025robomindbenchmarkmultiembodimentintelligence\]: a long-horizon manipulation dataset spanning both single-arm and dual-arm platforms, with strong cross-platform diversity.
- Galaxea \[jiang2025galaxeaopenworlddatasetg0\]: a dataset with rich sensor signals and fine-grained sub-task annotations for complex, long-horizon manipulation.
- InternData-A1 \[tian2025interndataa1pioneeringhighfidelitysynthetic\]: a large-scale synthetic robotic dataset constructed in simulation, covering diverse embodiments, manipulation skills, and scene configurations.

These datasets complement one another along several axes. OXE and OXE-AugE provide scale and embodiment diversity, Agibot-Beta and Galaxea provide higher-quality long-horizon task structure, RoboCOIN and RoboMind enrich cross-embodiment and dual-arm coverage, and InternData-A1 introduces synthetic scale and broader scene variation. Galaxea also goes beyond arm-only operations by incorporating diverse base mobility tasks, where both are coordinated to complete long-horizon mobile manipulation. Taken together, they enable ABot-M0.5 to learn robust visual dynamics and transferable motion priors before exposure to task-specific action supervision. We additionally include large-scale public robot corpora for diversity and robustness, including RoboNet \[dasari2020robonetlargescalemultirobotlearning\], BridgeData V2 \[walke2024bridgedatav2datasetrobot\], and DROID \[khazatsky2025droidlargescaleinthewildrobot\].

The same data infrastructure also supports latent action pretraining. Because frame-level latent actions depend only on visual frame pairs rather than control labels, large amounts of unlabeled or weakly labeled video can still contribute to motion abstraction learning. This broadens the effective supervision available to the model beyond standard action-annotated robotic datasets.

### 4.2 World Model Pretraining

The first phase of training focuses on pretraining the visual world model component of our framework. Initialized from the pretrained Wan2.2 5B weights \[wan2025wanopenadvancedlargescale\], the model is trained as an action-unconditioned future video predictor in an autoregressive (AR) manner. We perform full-parameter fine-tuning to adapt the Internet-scale spatiotemporal priors to robotic environments. This stage serves several critical purposes: it equips the model with robust scene and object representations, improves the quality of future latent predictions (which later serve as conditioning signals for action generation), and decouples visual world modeling from inverse dynamics learning, thereby significantly reducing the burden on downstream fine-tuning.

A key challenge in training on heterogeneous embodiment data is the significant semantic gap introduced by diverse camera configurations across different robot platforms and datasets, making it difficult for the video generation model to learn a consistent spatial representation when camera semantics are entangled. To address this, we introduce a fixed semantic slot allocation strategy. Specifically, we define four canonical video slots with predefined semantic roles: the first two slots are reserved for third-person views that capture the global scene and robot body configuration, while the last two slots are reserved for wrist-mounted views that provide fine-grained hand-object interaction details. For datasets that contain more than four camera views, we randomly sample a subset to fill the available slots, thereby introducing view-level data augmentation and preventing the model from overfitting to any particular camera arrangement. For datasets with fewer views than available slots, we apply zero padding to the unused slots.

To prevent zero-padded views from interfering with computation, missing views are represented as all-zero latent tensors and masked out in the self-attention layers, making them invisible to all valid views. The training objective is computed exclusively over valid views. Specifically, we optimize the visual world model using the conditional flow matching loss in the latent space, formulated as:

$$
\mathcal{L}_{\mathrm{z}}^{\mathrm{pretrain}}=\mathbb{E}_{z_{t},\epsilon,\tau}\left[\left\|v_{\theta}^{z}\big(z_{t}^{\tau};z_{<t},\tau,l\big)-(z_{t}-\epsilon)\right\|_{2}^{2}\right],
$$

where $v_{\theta}^{z}$ denotes the parameterized velocity field, $z_{t}^{\tau}$ is the interpolated latent at noise level $\tau$, $z_{<t}$ represents the autoregressive historical context, and $l$ is the conditioning input. We mask out this loss on padded regions so that no gradient propagates from artificial padding. This ensures the optimization is driven entirely by real visual observations and allows the model to seamlessly ingest multi-view data from heterogeneous robot embodiments with varying camera setups.

The pretrained world model is especially important in mobile manipulation. Compared with stationary manipulation, mobile tasks exhibit larger visual changes due to base movement, scene relocation, and changing camera viewpoints. A weak world model would therefore provide unstable or low-quality future predictions, severely limiting the effectiveness of downstream action learning. By pretraining world dynamics at scale, ABot-M0.5 starts fine-tuning from a much stronger representation of embodied future evolution.

![Refer to caption](https://arxiv.org/html/2607.00678v1/x6.png)

Figure 6: Model structure of ALAM.

### 4.3 Latent Action Model Pretraining

The second phase pretrains the latent action encoder used to construct frame-level motion supervision. Unlike executable robot actions, latent actions are defined in terms of visual transitions between consecutive frames. This makes them suitable for self-supervised training on large-scale video data.

To obtain the latent action encoder $E_{m}$, we adopt the training framework proposed in ALAM \[tang2026alam\], shown in Figure˜6. Given a triplet of temporally ordered observations $(o_{i},o_{j},o_{k})$ with $i<j<k$, the latent action model learns transition embeddings that capture how the observation changes over time. To encourage these embeddings to form a structured motion space, we impose algebraic consistency constraints over the learned transitions.

Specifically, let $m_{i}^{j}$ denote the latent action from $o_{i}$ to $o_{j}$. We enforce additive consistency:

$$
\mathcal{L}_{\mathrm{add}}=\left\|m_{i}^{k}-(m_{i}^{j}+m_{j}^{k})\right\|_{2}^{2},
$$

which encourages longer temporal transitions to be approximately decomposable into shorter ones. We also enforce reversal consistency:

$$
\mathcal{L}_{\mathrm{rev}}=\left\|m_{i}^{j}+m_{j}^{i}\right\|_{2}^{2},
$$

which encourages the transition from $o_{i}$ to $o_{j}$ to be the inverse of the transition from $o_{j}$ to $o_{i}$.

In addition to these relational constraints, the model is trained with reconstruction and vector-quantization objectives to ensure that the latent code remains informative and compact. The full pretraining objective is motivated by structured latent-action learning and flow-based policy generation \[tang2026alam, lipman2023flowmatchinggenerativemodeling, tang2026one\]:

$$
\mathcal{L}_{\mathrm{LAM}}=\lambda_{\mathrm{vq}}\mathcal{L}_{\mathrm{vq}}+\lambda_{\mathrm{rec}}\mathcal{L}_{\mathrm{rec}}+\lambda_{\mathrm{perc}}\mathcal{L}_{\mathrm{perc}}+\lambda_{\mathrm{add}}\mathcal{L}_{\mathrm{add}}+\lambda_{\mathrm{rev}}\mathcal{L}_{\mathrm{rev}}.
$$

After pretraining, we retain only the latent action encoder $E_{m}$ and discard the decoder and vector-quantization modules. The encoder is then frozen and used as an offline feature extractor to generate latent action labels for robot trajectories. In this way, the latent action supervision used by ABot-M0.5 is learned from large-scale visual motion rather than handcrafted from robot control signals.

This stage is crucial for two reasons. First, it provides a fine-grained intermediate representation that compensates for the temporal coarseness of future video latents. Second, it allows motion knowledge from unlabeled videos to be transferred into robotic action learning, thereby expanding the effective scope of pretraining beyond purely action-annotated robotic datasets.

### 4.4 Progressive Supervised Fine-Tuning

After world model pretraining and latent action pretraining, ABot-M0.5 enters supervised fine-tuning on downstream robotic data. This stage introduces explicit action supervision and aligns the model with task-specific control distributions. Rather than directly training under the final rollout regime, we use a progressive strategy that first stabilizes world-action learning under clean future conditions and then gradually transitions to rollout-consistent conditioning.

#### Stage I: Joint World Model and Inverse Dynamics Fine-Tuning

At the beginning of supervised fine-tuning, the pretrained world model still exhibits domain shift relative to the target datasets. Although it already encodes useful spatiotemporal priors, its future predictions are not yet sufficiently accurate to serve as reliable conditions for downstream action learning. If the inverse dynamics model were trained immediately on predicted futures, visual prediction errors would interfere with action learning before the model has adapted to the new data distribution.

We therefore begin with a stabilized fine-tuning stage in which latent action prediction and executable action prediction are conditioned on ground-truth future video latents. Under this setting, the model jointly predicts future video latents, latent actions, and executable actions:

$$
\displaystyle z_{t+1}
$$

$$
\displaystyle\sim p_{z}(\cdot\mid z_{\leq t},m_{<t},a_{<t},l),
$$
$$
\displaystyle m_{t}
$$

$$
\displaystyle\sim p_{m}(\cdot\mid z_{\leq t+1},m_{<t},a_{<t},l),
$$
$$
\displaystyle a_{t}
$$

$$
\displaystyle\sim p_{a}(\cdot\mid z_{\leq t+1},m_{\leq t},a_{<t},l).
$$

By aggregating Equations˜9, 5 and 13, the total training loss is

$$
\mathcal{L}_{\mathrm{SFT1}}=\lambda_{z}\mathcal{L}_{\mathrm{z}}+\lambda_{m}\mathcal{L}_{\mathrm{m}}+\lambda_{a}\mathcal{L}_{\mathrm{a}}.
$$

This stage provides a stable environment for action learning. Since future visual conditioning is clean, the inverse dynamics model can focus on learning the mapping from future world evolution and latent motion intention to executable control, rather than compensating for noisy or inaccurate predictions. In effect, Stage I initializes the interaction between the world model and the action model under controlled conditions.

#### Stage II: Dream Forcing for Inference-Aligned Fine-Tuning

Once the model reaches an initially converged regime, we transition to inference-aligned fine-tuning. At inference time, the model does not have access to ground-truth future video latents; instead, it must rely entirely on its own predicted future latents. To reduce this train-test discrepancy, we replace ground-truth future conditioning $z_{t+1}$ and $m_{t}$ with model-predicted future conditioning $\hat{z}_{t+1}$ and $\hat{m}_{t}$ when predicting action:

$$
\displaystyle a_{t}
$$

$$
\displaystyle\sim p_{a}(\cdot\mid\hat{z}_{t+1},z_{\leq t},\hat{m}_{t},m_{<t},a_{<t},l).
$$

And the Equations˜11 and 12 are modified as:

$$
\tilde{\mathcal{L}}_{\mathrm{a}}^{\mathrm{move}}=\mathbb{E}_{a_{t}^{\mathrm{move}},\epsilon,\tau}\left[\left\|v_{\theta}^{\mathrm{move}}\big(a_{t}^{\mathrm{move},\tau};\hat{z}_{\leq t+1},\hat{m}_{\leq t},a_{<t},a_{t}^{\mathrm{manip},\tau},\tau,l\big)-(a_{t}^{\mathrm{move}}-\epsilon)\right\|_{2}^{2}\right],
$$

and

$$
\tilde{\mathcal{L}}_{\mathrm{a}}^{\mathrm{manip}}=\mathbb{E}_{a_{t}^{\mathrm{manip}},\epsilon,\tau}\left[\left\|v_{\theta}^{\mathrm{manip}}\big(a_{t}^{\mathrm{manip},\tau};\hat{z}_{\leq t+1},\hat{m}_{\leq t},a_{<t},a_{t}^{\mathrm{move},\tau},\tau,l\big)-(a_{t}^{\mathrm{manip}}-\epsilon)\right\|_{2}^{2}\right].
$$

Then the overall loss becomes:

$$
\displaystyle\mathcal{L}_{\mathrm{SFT2}}
$$

$$
\displaystyle=\lambda_{z}\mathcal{L}_{\mathrm{z}}+\lambda_{m}\mathcal{L}_{\mathrm{m}}+\lambda_{a}\tilde{\mathcal{L}}_{\mathrm{a}}
$$

$$
\displaystyle=\lambda_{z}\mathcal{L}_{\mathrm{z}}+\lambda_{m}\mathcal{L}_{\mathrm{m}}+\lambda_{a}(\lambda_{a}^{\mathrm{move}}\tilde{\mathcal{L}}_{\mathrm{a}}^{\mathrm{move}}+\lambda_{a}^{\mathrm{manip}}\tilde{\mathcal{L}}_{\mathrm{a}}^{\mathrm{manip}})
$$

This stage implements the dream-forcing mechanism introduced in Section 3.4. Future latent actions and executable actions are now predicted under model-generated futures rather than perfect future observations. As a result, the inverse dynamics model learns to tolerate video prediction noise, slight object drift, and imperfect future rollout conditions.

![Refer to caption](https://arxiv.org/html/2607.00678v1/x7.png)

Figure 7: Attention masks of different training stages.

#### Training Rationale

The full fine-tuning strategy can be understood as a progressive alignment process. Stage I aligns the world model and action model on the downstream domain while shielding the inverse dynamics model from early prediction noise. Stage II then aligns the conditioning regime of action learning with the deployment regime of autoregressive rollout. In this way, the model is not merely optimized for one-step prediction accuracy, but for stable long-horizon performance under its own generated futures.

### 4.5 Efficient Structured Attention and Latent Augmentation

The training pipeline described above requires long-sequence joint modeling over multiple token streams and multiple modalities. Without additional optimization, such training would be prohibitively expensive. We therefore introduce two practical techniques that improve efficiency and data utilization while preserving the intended semantics of the model.

#### Efficient Structured Attention

ABot-M0.5 uses a structured sparse self-attention pattern to encode causal order, modality separation, and conditional visibility between token streams. A naive implementation with explicit block masks over the full attention matrix incurs substantial computational waste, especially for long sequences.

To address this, we reformulate the structured attention pattern as a set of dense sub-problems and implement them with variable-length FlashAttention \[dao2022flashattentionfastmemoryefficientexact\]. Concretely, for each sample, frame, and token category, we precompute the valid ranges of query and key indices implied by the structured attention mask. These valid ranges are then packed into contiguous query-key-value segments, and multiple attention sub-problems are executed within a single variable-length FlashAttention kernel. This yields an implementation that is mathematically equivalent to the original structured attention pattern but much more GPU-efficient.

Compared with a FlexAttention-style baseline, this design substantially reduces kernel overhead, avoids unnecessary block padding, and lowers memory consumption. In practice, it provides approximately a $5\times$ speedup in the combined forward-backward pass for long-sequence video-action modeling.

#### Offset-Based Latent Augmentation

To reduce the computational cost of repeatedly encoding raw video during training, we precompute video latent features at a fixed temporal stride $H$. A conventional implementation partitions a video starting from the first frame and always maps frames $[tH,(t+1)H]$ to the $t$ -th latent feature. While simple, this rigid alignment effectively underutilizes the raw video and limits the diversity of latent segmentations seen during training.

We therefore introduce an offset-based indexing strategy. Instead of always starting from the first frame, we allow the starting offset $s$ to vary within

$$
s\in\{0,1,\dots,H-1\}.
$$

Under a given offset $s$, frames $[s+tH,...,s+(t+1)H]$ are mapped to the $t$ -th latent feature. Since there are $H$ possible offsets, this increases the number of valid latent segmentations by a factor of $H$. The resulting augmentation improves temporal diversity and empirically enhances robustness to small timing variations.

#### Role in the Full Training Pipeline

These optimizations are not isolated engineering details. Efficient structured attention makes large-scale joint video-action training feasible under the multi-stream architecture of ABot-M0.5, while offset-based latent augmentation improves data efficiency and temporal robustness. Together, they enable the progressive training pipeline to scale to long-horizon mobile manipulation without compromising the structural design of the model.

Taken together, the training paradigm of ABot-M0.5 combines large-scale world modeling, self-supervised motion abstraction, progressive action alignment, and efficient system-level optimization. This combination is critical to translating the architectural advantages of the model into practical performance on mobile manipulation benchmarks and real-world deployment. The next section evaluates this training strategy and the resulting model across a broad range of simulated and real-world tasks.

## 5 Experiments

![Refer to caption](https://arxiv.org/html/2607.00678v1/x8.png)

Figure 8: Visualization of some results on RoboCasa365. We show video frames of both real camera observations and model-dreamed scenarios for each sample. Here we decompose the task into several subtasks, using yellow and green to distinguish between mobility and manipulation, respectively.

We evaluate ABot-M0.5 on a diverse set of mobile manipulation, manipulation, and real-world benchmarks to answer four questions. First, does the proposed framework improve long-horizon mobile manipulation performance over strong VLA and WAM baselines? Second, do the proposed architectural and training designs also benefit fine-grained manipulation beyond the mobile setting? Third, which components are responsible for the gains? Fourth, can the resulting model be deployed reliably in real-world scenarios? To answer these questions, we conduct experiments on RoboCasa365, RoboTwin 2.0, LIBERO / LIBERO-Plus, and real-world robotic tasks, together with detailed ablations and efficiency analysis.

### 5.1 Experimental Setup

#### Benchmarks

We evaluate ABot-M0.5 on the following benchmarks.

- RoboCasa365 \[nasiriany2026robocasa365largescalesimulationframework\]: a challenging mobile manipulation benchmark involving household tasks with both atomic and composite subtasks. It is the primary benchmark used to evaluate long-horizon mobile manipulation.
- RoboTwin 2.0 \[chen2025robotwin20scalabledata\]: a multi-task bimanual manipulation benchmark with both clean and randomized settings, used to evaluate generalization under scene variation.
- LIBERO / LIBERO-Plus \[liu2023libero, fei25libero-plus\]: compositional manipulation benchmarks that evaluate multi-task and long-horizon tabletop manipulation.
- Real-World Tasks: a set of real robotic tasks designed to test whether the learned world-action policy transfers beyond simulation.

Benchmark implementations follow the official setups of RoboCasa365, RoboTwin 2.0, and LIBERO/LIBERO-Plus.

#### Baselines

We compare our method with prior Video-Language-Action (VLA) and World Action Models (WAMs). To ensure a comprehensive and objective evaluation, we carefully select baselines that encompass the most widely adopted, state-of-the-art, and most recent works, as well as those most closely related to our approach. Specifically, on the LIBERO-Plus benchmark, we extend our comparison beyond standard VLA models to include hybrid VLA+WM and pure WAM architectures, with a particular focus on highlighting the distinct advantages of our method over existing WAMs.

#### Metrics

For each benchmark, we follow the official protocol and report benchmark-standard metrics. The primary evaluation metric is task success rate. For RoboCasa365, we additionally report performance across atomic seen, composite seen, and composite unseen task categories. For RoboTwin 2.0, we report average success rate under clean and randomized scenes across 50 tasks. For LIBERO and LIBERO-Plus, we report the standard benchmark success rate metric averaged across tasks. For real-world experiments, we evaluate on 5 tasks and report both success rate and process score.

#### Implementation Details

Unless otherwise specified, ABot-M0.5 is trained using the progressive pipeline described in Section 4. The video latent backbone, latent action encoder, and inverse dynamics components are jointly fine-tuned under the proposed training paradigm. For mobile manipulation, the action head models both mobility and manipulation controls. For non-mobile manipulation benchmarks, the same overall architecture is retained, with action routing specialized to the corresponding embodiment and control dimensions.

### 5.2 Main Results on Mobile Manipulation

We first evaluate ABot-M0.5 on RoboCasa365, which serves as the primary benchmark for mobile manipulation. RoboCasa365 is particularly suitable for evaluating the proposed framework because many tasks require both long-horizon planning and precise manipulation, and because the benchmark contains diverse atomic and composite tasks under realistic household layouts.

#### Benchmark Protocol

We follow the standard RoboCasa365 evaluation setup and report average performance together with category-specific results on atomic seen, composite seen, and composite unseen tasks. These categories capture increasingly challenging settings, from relatively localized interactions to longer task chains and unseen task compositions.

#### Main Comparison

Section˜5.2 summarizes the comparison between ABot-M0.5 and representative baselines. ABot-M0.5 achieves strong overall performance, with particularly clear gains on long-horizon composite tasks. This is consistent with the design goals of the model: temporal alignment helps preserve fine-grained control-relevant dynamics, action decoupling improves structured coordination between mobility and manipulation, and Dream-Forcing improves robustness under long rollout.

![Refer to caption](https://arxiv.org/html/2607.00678v1/x9.png)

Table 2: Evaluation results on RoboCasa365 Benchmark (pretraining). ABot-M0.5 outperforms prior methods, achieving state-of-the-art performance. Furthermore, we introduce an enhanced condensed memory mechanism, which yields further performance gains and sets a new record. A detailed discussion of this extension will be presented in our future work.
