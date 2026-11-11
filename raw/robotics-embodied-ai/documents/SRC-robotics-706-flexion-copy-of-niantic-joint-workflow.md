---
source_id: "SRC-robotics-706"
title: "Flexion copy of Niantic joint workflow"
source_type: "company_blog"
publisher: "Flexion / Niantic Spatial"
source_date: "2026-07-20"
url: "https://flexion.ai/news/niantic-spatial-flexion-and-nvidia-closing-the-sim2real-gap-for-humanoids"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-11-10T02:02:05+00:00"
tags:
  - raw/source
  - source-type/company-blog
  - evidence/a
aliases:
  - SRC-robotics-706
---
# Flexion copy of Niantic joint workflow

![](https://framerusercontent.com/images/P6hYFXttoeRBYbTlPAXBZrUVY.jpeg?width=264&height=2956)

Niantic Spatial, Flexion, and NVIDIA: Closing the Sim2RealGap for Humanoids

Niantic Spatial, Flexion, and NVIDIA: Closing the Sim2RealGap for Humanoids

Niantic Spatial, Flexion, and NVIDIA: Closing the Sim2RealGap for Humanoids

Niantic Spatial, Flexion, and NVIDIA: Closing the Sim2RealGap for Humanoids

The most scalable way to teach a humanoid fundamental skills like locomotion and navigation is reinforcement learning (RL). Running RL in the real world is hard, because robots do not get many second chances. A misjudged gap or a collision with a glass door is expensive, slow to reset, and can damage hardware. So most learning happens in simulation instead.

The question every company should ask: how do you know a policy trained in sim will hold up at a deployment site before a robot ever sets foot there? The answer is to train, test, and evaluate it in a digital twin of that exact site, which also makes it fast to adapt skills for each new location.

Here is the vision. A team scans the intended deployment site with a standard RGB camera. Niantic Spatial reconstructs a high-fidelity digital twin. Developers then simulate and train their robots using NVIDIA Isaac Sim and Isaac Lab open source simulation and learning frameworks. Flexion delivers policies and deployment software tuned to the specific hardware that transfers zero-shot to the real world.

Niantic Spatial and Flexion jointly present that pipeline end to end: an RGB-only local navigation policy, trained entirely in simulation using photorealistic rendering from Gaussian splatting, that transfers zero-shot to a real office. The results highlight that the speed and quality of the rendering are sufficient to train RL-based policies in hours, and hold promise for training full vertical systems, including reasoning and manipulation, in the future.

![](https://www.youtube.com/watch?v=qZR0RMP2_5w)

## Robots have to fail in simulation in order to learn

Simulation is where a robot can afford to fail. In reinforcement learning, a policy improves through trial and error: taking an action, observing the reward, and adjusting across millions of attempts, most of which go wrong before the behavior works reliably. While a real robot would never survive that, simulation offers a fast, safe, and massively parallel environment for robots to train, enabling thousands of virtual robots to practice at once, faster than real time, without a single scratch. But simulation training only creates real value if that behavior transfers back to the physical world – the core challenge of sim2real robotics.

### The path to today’s simulation-first robot training

Modern reinforcement learning for robotics depends on GPU-accelerated simulation, which lets physics engines and training loops scale across thousands of parallel environments \[[Rudin et al., 2022](https://proceedings.mlr.press/v164/rudin22a.html)\]. Platforms such as NVIDIA Isaac Sim and Isaac Lab provide the core infrastructure for this kind of large-scale robot training.

Within these simulation environments, robot policies have advanced as sensor inputs have become richer. Early reinforcement learning systems relied mainly on proprioception, using joint feedback and contact forces to traverse terrain \[[Lee et al., 2020](https://www.science.org/doi/abs/10.1126/scirobotics.abc5986)\].

The next wave added exteroceptive sensing – height scans, depth maps, and LiDAR – so policies could anticipate terrain before contact. That shift enabled robust locomotion on irregular terrain \[[Miki et al., 2022](https://www.science.org/doi/abs/10.1126/scirobotics.abk2822)\], high-speed agile maneuvers \[[Hoeller et al., 2024](https://journals.sagepub.com/doi/abs/10.1177/02783649261455067)\], and end-to-end navigation in simulation \[[Yang et al., 2025](https://journals.sagepub.com/doi/abs/10.1177/02783649251401926)\].

![](https://framerusercontent.com/images/YuKQPRPDJJePwbyMQSRtKQIyeM.webp?width=2908&height=1620)

> A typical massively parallel training environment for humanoid navigation from raw depth information. The navigation goal location is visualized with a red arrow. The simulation relies entirely on randomized untextured structures.

RGB is the next step, and it is what humanoids already carry. Cameras are cost-efficient, ubiquitous, have a wide field of view, and they implicitly encode both geometry and semantics with fewer hard failure cases than stereo depth. That extra information is the headroom to scale.

The limitation is that these training worlds are still built from randomized, untextured geometric scenes. That remains the standard because depth is relatively straightforward to simulate accurately. But it also restricts the robot to structural contours, leaving it blind to materials, semantics, and what objects actually are. That is why RGB is the next step in perceptive robot policies: it gives humanoid navigation systems access to both geometry and scene meaning, provided the simulated imagery is realistic enough to transfer to the real world.

### The solution in two parts

**The first is real2sim:** faithfully bringing reality into the simulator, both how the world looks and how it physically behaves. Niantic Spatial's strength is turning captures of a real place into a high-fidelity, renderable, simulatable copy.

**The second is sim2real:** taking a policy trained in that imperfect simulated environment and getting it to run robustly on a physical robot. Bridging that gap is Flexion's strength.

Vision is the hardest part of both real2sim and sim2real. Depth has historically been easier to simulate because a depth image looks broadly similar whether it is rendered or measured, and its noise can be modeled directly. RGB is more demanding: small errors in color, lighting, or texture can make a scene look like a different place altogether, which makes both realistic simulation and robust policy transfer harder.

So why train an RGB robot policy inside a reconstructed scene? First, RGB is what robots increasingly carry. Cameras are low-cost, widely available, often offer a wider field of view than stereo depth sensors, and RGB implicitly encodes both geometry and semantics. That gives RGB-based robot policies more room to scale than depth alone, especially in real-world environments where semantics matter as much as shape.

Second, specialization unlocks capability. Training a policy inside a digital twin of the actual deployment site allows it to adapt to the visual structure, materials, and constraints of the environment where it will run, enabling behaviors that are difficult for a general-purpose policy to achieve.

But for sim2real transfer to work, the training imagery has to look real. In practice, that means either photorealistic synthetic assets or, more directly, a faithful reconstruction of the real scene. That is what makes a reconstruction the natural home for an RGB policy. It also defines the problem in two parts: building a training world faithful enough to learn from, and training a policy robust enough to transfer out of it. The rest of this blog walks through both, using local navigation as a concrete example: starting with the world Niantic Spatial builds, then how Flexion trains and deploys an RGB navigation policy inside it.

## Part 1: Niantic Spatial's real2sim – one walkthrough to a world worth training in

A policy is only as good as the observations obtained from the world in which it learns. For a sim2real transfer to work, the reconstructed scene has to be faithful on two fronts at once: it has to look like the real place (geometry, materials, lighting) and it has to behave like it under physics. Satisfying both requirements usually means a photorealistic rendering layer and a collision mesh for physics, and the quality of the reconstruction depends on how well they agree. If the rendered wall and the collision wall disagree by a few centimeters, a vision policy learns to brush through obstacles it can see, or steer around obstacles that are not there, and it carries that miscalibration onto the real robot. Niantic Spatial’s pipeline derives both layers from the same reconstruction, so they agree by construction.

### Capture a real site with a single walkthrough

A few minutes of video from an off-the-shelf 360° camera are enough to create a training-ready digital twin of a real deployment site. The operator simply walks the space once, with no LiDAR, tripod stations, or specialized capture workflow. From that video, the pipeline reconstructs the scene at metric scale so the robot learns distances and velocities in meters, avoiding scale errors that would otherwise propagate into every action.

The same capture then becomes the visual layer for simulation. Niantic Spatial estimates camera poses and trains a 3D Gaussian splat that provides photorealistic RGB views from arbitrary viewpoints, preserving the lighting, materials, and clutter of the real environment as it appeared at capture time. That matters for RGB robot training: unlike a generic synthetic asset, a faithful scene reconstruction gives the policy the visual realism it needs for sim2real transfer. It also scales operationally, because capturing a real warehouse or office is far more repeatable than hand-building a high-fidelity synthetic model for every new site.

### Deriving geometry from the same reconstruction

From that same reconstruction, Niantic Spatial also derives the physics layer. Instead of building geometry in a separate pipeline, it uses the reconstruction itself to generate the collision mesh, including depth estimated with [MVSAnywhere](https://nianticlabs.github.io/mvsanywhere/), a zero-shot multi-view stereo model designed to generalize across domains and depth ranges. This produces flatter, cleaner surfaces than photometric reconstruction alone, especially on white walls and other low-texture regions where conventional multi-view methods often leave gaps, noisy geometry, or even lose camera poses entirely.

Because the visual layer and collision mesh come from the same reconstruction, they stay aligned by construction. There is no separate cross-registration step between what the robot sees and what it collides with in simulation, which removes a major source of sim2real error. Even a small mismatch between a rendered wall and a collision wall can teach a humanoid to slide through obstacles it can see or avoid obstacles that are not really there. The single-reconstruction design minimizes that failure mode instead of trying to correct for it later.

<video controls="" src="https://framerusercontent.com/images/On4I0HkbNZGR6tvlriDHaxW73hg.mp4"></video>

> Comparing NerfStudio splats (left) to Niantic Spatial splats (right).

### Exporting a USDZ ready for NVIDIA Isaac Sim

The splat and mesh are packaged into a single [USDZ](https://www.nianticspatial.com/blog/usdz-scaniverse) that matches NVIDIA’s [NuRec](https://developer.nvidia.com/omniverse/nurec) volume specification and loads directly into NVIDIA [Isaac Sim](https://developer.nvidia.com/isaac/sim) and [Isaac Lab](https://developer.nvidia.com/isaac/lab). In that workflow, the splat renders through the RTX pipeline as the visual scene, while the mesh serves as the invisible physics proxy the robot stands on and collides with. The export arrives gravity-aligned, metric-scale, and collider-ready, so training can start without manual conversion, reorientation, or collider authoring.

### The end-to-end workflow: from 360° capture to a training-ready digital twin for robot simulation

1. **Capture:** Walk the real deployment site once with an off-the-shelf 360° camera to collect the visual data needed for reconstruction.
2. **Reconstruct:** The pipeline estimates camera poses, trains a photorealistic 3D Gaussian splat, and derives an aligned collision mesh to create a faithful digital twin of the environment.
3. **Export:** The visual splat and physics mesh are packaged into a single NuRec-volume USDZ that is gravity-aligned, metric-scale, and ready for simulation with collider settings applied.
4. **Train:** The USDZ loads directly into NVIDIA Isaac Sim and Isaac Lab, where it can be used as a stage for large-scale robot training in simulation.

### What the reconstruction captures – and what it doesn’t

Like any reconstruction, this one has limits that are important to understand before training. It captures a moment in time, so lighting, reflections, and object placement are baked in as observed during capture. It also captures a static scene: people, robots, and other dynamic agents are added later in simulation. And its fidelity depends on coverage, which means areas skipped during the walkthrough will reconstruct less reliably. In practice, though, those limits have not prevented zero-shot transfer to the real robot in the results that follow.

## Part 2: Flexion's sim2real recipe – from pixels in sim to a robot that works

With a world worth training in, the door opens to a wide range of robot tasks. In this blog, Flexion focuses on local robot navigation: the short-horizon skill of moving from the robot’s current pose to a nearby goal while avoiding obstacles, without relying on a prebuilt global map. The policy takes the robot’s onboard camera view, proprioceptive sensor data, and the goal expressed in its own coordinate frame, and outputs a velocity command. A separate, in-the-loop pre-trained locomotion policy then converts that command into motion. Because the policy acts directly on what the camera sees, visual realism in simulation matters. Most camera-based robot policies today still use depth as their primary input, but Flexion takes a different approach: train an RGB policy inside a reconstruction of the specific deployment site, so the policy specializes in the real environment where it will actually run.

### Massively parallel robot training inside the digital twin

Loaded into Isaac Lab as a NuRec volume, the reconstruction renders RGB efficiently enough to support massively parallel robot training inside the same digital twin on a single GPU. Each robot begins from a sampled spawn pose and is assigned a random target pose. From there, the navigation policy learns through reinforcement learning: reaching the goal while avoiding obstacles is rewarded, while collisions and falls are penalized.

To bridge the sim2real gap, Flexion combines domain randomization across simulation parameters with large-scale, offline-trained image encoders that produce robust features on real imagery. Those encoders are designed to run both across many parallel training environments and onboard the robot at deployment time. Together, this setup enables millions of rollouts inside the target site’s digital twin, giving the policy enough experience to learn deployment-specific robot navigation behavior.

The following two videos show policies trained directly inside reconstructions of the Niantic Spatial office in London and the Flexion office in Zurich.

![](https://www.youtube.com/watch?v=kvefIcaQqg4)

> Video of the training process inside a reconstruction of a Niantic Spatial office. Robots navigate towards their red goal pose markers.

![](https://www.youtube.com/watch?v=AE--3vNOAdw)

> Visualization of the training process inside the Flexion Office reconstruction. Robots navigate towards their red goal pose markers.

### On the real robot: the reconstruction-trained RGB policy transfers zero-shot

The policy does not stay in simulation. The RGB network trained entirely inside the reconstruction transfers to the physical robot and navigates the real office, holding up to scene changes such as rearranged furniture and other differences from the captured world. During nominal navigation through the test area, it performs on par with a depth-based policy, highlighting that an RGB-only policy trained solely in simulation can extract the spatial understanding required for successful navigation.

![](https://www.youtube.com/watch?v=s3LghqmCSrc)

> RGB-only policy purely trained in simulation, navigating the real office toward three commanded target poses.

### Comparing alternative approaches in simulation

We compare four local-navigation policies on the same task in simulation across two reconstructed scenes: areas from Flexion’s and Niantic Spatial’s offices. The setups vary by both sensor modality and training environment: a depth policy trained in a generated, untextured navigation mesh as the conventional baseline; an RGB policy trained in that same generated mesh; an RGB policy trained in a synthetic, textured office mesh; and an RGB policy trained in the 3DGS reconstruction of the actual site.

The plots below report three simulation metrics across all four policies: success rate, time-out rate after 120 seconds, and fall rate. Each policy is evaluated over 1,024 rollouts, with the same spawn and target poses reused across conditions so that the comparison isolates the effect of sensor modality and training environment.

Across both simulated scenes, RGB trained in the 3DGS reconstruction is the only RGB setup that matches or exceeds the conventional depth baseline: 97.8% versus 93.8% in the easier Flexion office, and 75.0% versus 70.9% in the harder Niantic Spatial office. The other RGB training environments – the synthetic office and the generated mesh – trail depth in both scenes, with the gap widening as scene difficulty increases. In simulation, the reconstruction is what allows an RGB policy to reach depth-level reliability rather than fall well short of it.

### RGB handles common stereo depth failure cases

In our experiments, the depth stream comes from a ZED X camera in neural mode. It is a capable sensor, but some scenarios remain difficult for stereo depth or lose important information in the depth-conversion step.

Three representative hard cases are shown below:

#### Non-geometric cues

<video controls="" src="https://framerusercontent.com/images/XAhK9OWQfScnEwRD4mJsipuGCg.mp4"></video>

> Hazards defined more by semantics than geometry. In this example, a blue mat is obvious in RGB but barely registers on the depth stream, even though its raised edge is enough to trip a non-perceptive locomotion policy.

#### Thin structures

<video controls="" src="https://framerusercontent.com/images/9yKXEuEzirfoQIazWVbJTLZHA.mp4"></video>

> Tripods, railings, and cables are especially challenging for depth-based methods, which can miss them entirely or blur their edges. This issue can be mitigated, but doing so typically requires significant scene engineering and a realistic model of depth noise.

#### Transparent surfaces

<video controls="" src="https://framerusercontent.com/images/kz3CXjb14pc4gkDWTIoC6MPb4.mp4"></video>

> Glass doors and windows, where depth sensors routinely struggle.

None of these exact scene configurations – the blue mat, the tripod, or the sheet of glass in the locations shown here – were present during scene reconstruction, so the policy did not encounter them in that form during training.

Why, then, does the reconstruction-trained RGB policy still handle them in real-world robot navigation?

During simulation training, the policy repeatedly collided with semantically related objects and learned to associate those interactions with failure. It never saw this exact glass barrier, for example, but the reconstruction did contain windows. Failing against those transparent surfaces in simulation taught the policy to treat framed, glass-like surfaces as obstacles, including ones it had not encountered before.

That same mechanism is also the limit of the approach. RGB is not magic: the policy generalizes well to objects that are semantically similar to what it saw during training, but less well to objects that are too far outside that experience.

That is why the longer-term path for training RGB policies pairs broad, massively parallel perceptual pretraining with fine-tuning inside the reconstruction, so the policy can both generalize broadly and specialize to its deployment site for stronger sim2real transfer.

## Closing the loop – and what comes next

A perfect reconstruction with no way to ship a policy is a compelling demo. A strong sim2real recipe with no faithful world to train in has limited information to learn from. Together, real2sim and sim2real turn a real place into a training ground – and a trained policy back into a robot that works in that environment.

Where this goes next:

- **Scaling data collection:** expanding capture with off-the-shelf hardware such as iPhones and fisheye cameras would make it possible to build larger datasets from real-world environments, creating broader training grounds for future robot policies.
- **Semantic scene understanding:** attaching open-vocabulary labels to surfaces and objects in a reconstruction would make the digital twin queryable, not just visible.
- **Scene transformation:** generating controlled variants of a captured scene – in appearance, such as lighting or time of day, and in state, such as doors open or closed or furniture moved – would let policies train against a wider range of conditions and interactions.
- **End-to-end evaluation in simulation:** extending evaluation from local navigation to full-task performance inside the reconstructed world. Flexion’s [Reflect v1.0](https://flexion.ai/news/flexion-reflect-v1.0) is a concrete example of that broader direction toward long-horizon autonomy, combining navigation, interaction, planning, and recovery in one system.
- **VLM and agent training:** pushing beyond navigation toward richer, language-conditioned behavior grounded in the same reconstructed scenes.

The broader implication is commercial. Deploying a robot policy to a new environment has traditionally required months of on-site adaptation. Together, real2sim and sim2real compress that timeline to days, making it possible to deploy policies that are both faster to develop and more robust in practice. For operators seeking to scale autonomous robots across multiple plants or facilities, this pipeline offers a clear, repeatable path forward.

## About Niantic Spatial

Niantic Spatial is building the real-world model for physical AI, giving robots, AI agents, and people an accurate, shared understanding of physical spaces. Its [reconstruction](https://www.nianticspatial.com/products/reconstruct) technology captures environments with geometric accuracy and fine detail from any standard camera, and its [Visual Positioning System](https://www.nianticspatial.com/products/localize) delivers precise positioning almost anywhere in the world. Learn more at [nianticspatial.com](http://nianticspatial.com/).

## About Flexion

Flexion is building the autonomy stack for humanoid robots: from command to control, from manipulation to locomotion. By leveraging simulation and reinforcement learning, the stack is designed to generalize and scale across environments and hardware platforms with minimal human involvement.
