---
source_id: "SRC-robotics-379"
title: "Lightwheel NVIDIA customer story and Geely factory deployment"
source_type: "customer_case"
publisher: "NVIDIA"
source_date: "2026-08-06"
url: "https://www.nvidia.com/en-us/case-studies/lightwheel/"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-08-06T02:05:23+00:00"
tags:
  - raw/source
  - source-type/customer-case
  - evidence/a
aliases:
  - SRC-robotics-379
---
# Lightwheel NVIDIA customer story and Geely factory deployment

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=)

#### Manufacturing

## Lightwheel Accelerates Physical AI Development With NVIDIA Simulation and Foundation Models

## Objective

Lightwheel, a simulation-first robotics solutions provider, addresses two critical [physical AI](https://www.nvidia.com/en-us/glossary/generative-physical-ai/) barriers: data scarcity from expensive real-world data collection and the sim-to-real gap, where policies trained in simulation fail to translate to physical hardware. To help robot makers overcome these challenges, Lightwheel leveraged [NVIDIA Isaac Sim™](https://developer.nvidia.com/isaac/sim) and [Isaac™ Lab](https://developer.nvidia.com/isaac/lab), [NVIDIA Omniverse™](https://www.nvidia.com/en-us/omniverse/) libraries, and the [Isaac GR00T N1.5](https://developer.nvidia.com/isaac/gr00t) vision-language-action foundation model to create the Lightwheel Simulation Platform—a simulation-first workflow that bridges the gap between research and real-world robotic deployment.

## Customer

AgiBot  
BYD  
ByteDance  
Figure  
Fourier  
Galbot  
Geely  
Google Deepmind  
Zordi

## Partner

Lightwheel

## Use Case

Robotics

## Products

[NVIDIA Isaac](https://developer.nvidia.com/isaac)  
[NVIDIA Omniverse](https://www.nvidia.com/en-us/omniverse/)

#### Key Takeaways

- Accelerated development cycles, reducing robotic training from weeks or months to rapid, iterative loops through simulation-first workflows
- 100:1 simulated-to-real data ratio, eliminating expensive real-world data collection while maintaining physically realistic training environments

- Successful automotive factory deployment of GR00T N1.5 foundation models in Geely's live production environment with Unitree H1 humanoid robots
- Scalable multi-industry solutions serving major customers, including AgiBot, ByteDance, and Figure across robotics and automation applications

- Powered by OpenUSD, the Lightwheel Simulation Platform delivers a complete embodied AI pipeline, from SimReady asset generation to cloud-based simulation and collection of teleoperation data in virtual reality.

## Data Scarcity and the Sim-To-Real Gap

The embodied AI and robotics industry faces two fundamental barriers: data scarcity and the sim-to-real gap. Real-world data collection remains slow and expensive, constraining development speed and limiting the training datasets needed for intelligent autonomous systems. The sim-to-real gap presents an equally significant challenge, where AI policies trained in simulation environments fail to translate to reliable performance on physical hardware.

For [robotics researchers](https://www.nvidia.com/en-us/research/robotics/), developers, and industries deploying autonomous systems in manufacturing, healthcare, logistics, and agriculture, these challenges create substantial operational limitations. Traditional approaches require extensive physical prototyping, costly real-world testing, and time-intensive data collection—severely limiting innovation speed and increasing development costs while constraining the deployment of advanced AI systems in practical applications.

![Humanoid robot working in a warehouse environment](https://www.nvidia.com/content/nvidiaGDC/us/en_US/case-studies/lightwheel/_jcr_content/root/responsivegrid/nv_container_copy_co_568068830/nv_container_1324314/nv_image.coreimg.jpeg/1767338910268/data-scarcity-and-the-sim-to-real-gap-ari-1.jpeg "Humanoid robot working in a warehouse environment")

Lightwheel

![Lightwheel](https://www.nvidia.com/content/nvidiaGDC/us/en_US/case-studies/lightwheel/_jcr_content/root/responsivegrid/nv_container_copy_co_568068830/nv_image_copy_copy.coreimg.jpeg/1767338911566/lightwheel-simulation-platform-ari-1.jpeg "Lightwheel")

Lightwheel

## Building a Simulation-First Platform

To overcome these challenges, Lightwheel developed the Lightwheel Simulation Platform—a comprehensive solution built on [Isaac Sim](https://developer.nvidia.com/isaac/sim), [Isaac Lab](https://developer.nvidia.com/isaac/lab), and [NVIDIA Omniverse](https://www.nvidia.com/en-us/omniverse/) libraries,that addresses embodied AI development through three core components.

### Lightwheel SimReady Assets and Simulation Foundation

Lightwheel’s SimReady assets are engineered for real-world physics, designed with precise geometry and validated physical properties. These assets enable users to quickly assemble accurate digital twins, accelerating workflows for teleoperation data collection and [reinforcement learning](https://www.nvidia.com/en-us/glossary/reinforcement-learning/). With built-in support for Universal Scene Description (USD) format and MJCF, teams can seamlessly integrate assets into Isaac Sim, unlocking robust, interoperable simulation environments.

Leveraging OpenUSD, Lightwheel creates high-quality, physically accurate simulations to drive modern physical AI at scale. Lightwheel uses [NVIDIA USD Search](https://docs.omniverse.nvidia.com/services/latest/services/usd-search/overview.html) to streamline asset discovery, making it easy to locate the right SimReady assets for each simulation task and assemble scenes in minutes. This flexibility allows teams to accelerate development in their preferred simulation environment. Underpinning this asset library is Lightwheel’s simulation framework, which seamlessly integrates Isaac Sim.

![Simulated robot doing household task](https://www.nvidia.com/content/nvidiaGDC/us/en_US/case-studies/lightwheel/_jcr_content/root/responsivegrid/nv_container_copy_18/nv_container/nv_container_copy/nv_image.coreimg.jpeg/1767338913052/building-a-simulation-first-platform-ari.jpeg "Simulated robot doing household task") <video controls="" aria-label="External Video"><source src="https://images.nvidia.com/aem-dam/Solutions/customer-stories/lightwheel/deformable-cloth-folding-in-newton.mp4" type="video/mp4"></video>

### Advanced Teleoperation and Data Generation

Lightwheel enables high-quality teleoperation data collection through VR headsets (Apple Vision Pro, Meta Quest), Space Mouse, and exoskeleton solutions with robust quality assurance. The platform combines [MimicGen](https://mimicgen.github.io/) and [DexMimicGen](https://dexmimicgen.github.io/) with Lightwheel’s SimReady assets, environments, and Isaac Sim to generalize teleoperated simulation data, scaling the value of [synthetic data](https://www.nvidia.com/en-us/glossary/synthetic-data-generation/) by 100 to 1000 times.

To generate this diverse training dataset, operators control simulated Unitree H1 [humanoid robots](https://www.nvidia.com/en-us/glossary/humanoid-robot/) through complex industrial tasks, including cylindrical component manipulation with Dex Hand and dual-arm coordination for heavy tray lifting in automotive environments.

### GR00T N1.5 Integration and Quality Assurance

By leveraging the [GR00T N1.5](https://research.nvidia.com/labs/gear/gr00t-n1_5/) visual-language-action (VLA) foundation model, Lightwheel fine-tuned the model using simulation-generated synthetic data from its SimReady environments. This data included RGB images, joint states, GPT-generated task descriptions, and scene metadata. This robust training process resulted in impressive downstream performance, validating the effectiveness of simulation-based pipelines for embodied AI.

The Lightwheel Simulation Platform applies rigorous two-phase quality assurance: automated validation for visual realism and annotation completeness, followed by manual review for realistic behavior under physical constraints.

For the Geely automotive deployment, the team further tailored GR00T N1.5 to the Unitree H1 robot’s specific morphology, customizing the vision-language planner with factory-optimized prompts. Using Isaac Sim and DexMimicGen data augmentation techniques, they expanded training diversity across varied lighting, materials, and object placements, enabling reliable performance in dynamic factory conditions.

During prototyping, the system runs on [NVIDIA GeForce RTX™ 4090 GPUs](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/), providing compute capacity for embodiment adaptation and task optimization before deployment.

![Simulated robot doing household task](https://www.nvidia.com/content/nvidiaGDC/us/en_US/case-studies/lightwheel/_jcr_content/root/responsivegrid/nv_container_copy_18/nv_container/nv_container/nv_image.coreimg.jpeg/1767338914336/building-a-simulation-first-platform-ari-1.jpeg "Simulated robot doing household task")

Lightwheel

## Delivering Embodied AI to Industry

[Lightwheel's NVIDIA-powered simulation platform](https://www.lightwheel.ai/) delivers transformative improvements across development speed, deployment success, and real-world performance, establishing new benchmarks for embodied AI development in industrial applications.

### Accelerated Development and Cost Efficiency

The simulation-first approach reduced development cycles from months to weeks by enabling rapid iteration in virtual environments. The 100:1 simulated-to-real data ratio eliminated expensive real-world data collection while maintaining the physical accuracy necessary for reliable sim-to-real transfer, generating scalable, high-quality synthetic data with minimal manual intervention.

### Real-World Industrial Deployment

Lightwheel successfully deployed GR00T N1.5 foundation models in Unitree H1 humanoid robots at Geely's live automotive factory. The robots autonomously perform component transportation between workstations, precise part placement on inspection trays, and coordinated dual-arm manipulation for heavy components while maintaining balance in dynamic environments with human workers. These deployments demonstrate meaningful progress toward robust, factory-grade autonomy capable of scaling across diverse workflows.

 <video controls="" aria-label="External Video"><source src="https://images.nvidia.com/aem-dam/Solutions/customer-stories/lightwheel/h1-car-plant-task-simulation.mp4" type="video/mp4"> </video>![Simulated robot doing household task](https://www.nvidia.com/content/nvidiaGDC/us/en_US/case-studies/lightwheel/_jcr_content/root/responsivegrid/nv_container_copy_81/nv_container/nv_container_copy/nv_image.coreimg.jpeg/1773640282169/siggraph25-robotics-web-lightwheel-chimera.jpeg "Simulated robot doing household task")

### Multi-Industry Impact and Future Development

Major technology partners including Google DeepMind, Figure, AgiBot, ByteDance, Geely, and BYD leverage the Lightwheel Simulation Platform assets and synthetic datasets to improve embodied AI performance across robotics and automation applications. The platform's integration with NVIDIA's broader ecosystem completes the end-to-end service chain for synthetic data generation while opening new revenue streams from the robotics industry.

Ongoing development focuses on expanding platform capabilities for deformable object modeling, building SimReady Assets for general-purpose tasks, and scaling data generation pipelines by leveraging GR00T N1.5 as a semi-autonomous demonstrator for initial task demonstrations at scale.

## Turning Advanced Research Into Deployable Solutions

Lightwheel's collaboration with NVIDIA demonstrates how advanced simulation platforms and foundation models can transform embodied AI development, turning theoretical research into practical, deployable robotic solutions. Their successful deployment of GR00T N1.5-powered humanoid robots in live automotive manufacturing environments showcases how simulation-first strategies can deliver robust, scalable automation to the factory floor.

This comprehensive approach showcases how companies can leverage NVIDIA's AI ecosystem to overcome traditional barriers in robotics development, achieving unprecedented speed, cost efficiency, and deployment success across industries from automotive manufacturing to next-generation robot development.

“By leveraging NVIDIA AI technologies, we successfully fine-tuned our vision-language-action foundation model with our own high-quality synthetic and real-world data and deployed it on real robots. Using GR00T N1.5, we enabled robots to understand complex instructions and perform versatile tasks in dynamic, real-world environments—capabilities that were not possible before.”

**Jay Yang**  
Chief Architect

Learn how NVIDIA Isaac Sim can accelerate your own sim-to-real robotics development with photorealistic simulation environments.
