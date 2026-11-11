---
source_id: "SRC-robotics-690"
title: "Niantic embodied AI product availability and delivery"
source_type: "product_page"
publisher: "Niantic Spatial"
source_date: "待验证"
url: "https://www.nianticspatial.com/embodied-ai"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-11-10T02:02:05+00:00"
tags:
  - raw/source
  - source-type/product-page
  - evidence/a
aliases:
  - SRC-robotics-690
---
# Niantic embodied AI product availability and delivery

## Make real places simulatable.

Our real-to-sim stack turns inexpensive camera footage into photorealistic, metric-scale, collider-ready environments.

Train where you'll deploy and evaluate against the real site's edge cases, from one capture with a commodity camera.

Hours, not weeks

One walkthrough with an off-the-shelf camera takes you from capture to a simulation-ready environment your policies can train in – hours, not weeks.

A few hundred dollars

A deployment environment starts at a few hundred dollars vs. tens of thousands to professionally survey or hand-build synthetic twins of the same environment from scratch.

Proven policy transfer improvement

Trained on the reconstruction, ran zero-shot on the real robot. Across 1024 simulation runs, an RGB navigation policy trained only on our reconstruction fell 13 times less often than the same architecture trained on a hand-built synthetic office. On the real robot in the real site, it handled cases where a depth-input policy failed.

RUNS IN YOUR STACK

Runs in: Isaac Sim · Isaac Lab · any OpenUSD-compatible simulatorDelivered as: Gaussian splat + collision mesh from the same reconstruction, in one USDZ

## Hallucination is a luxury physical AI can't afford.

Embodied AI policies trained only in synthetic environments struggle when they encounter the details of a real deployment environment: uneven floors, clutter, changing layouts, and transparent surfaces. Closing that sim-to-real gap costs time, money, and customer trust, throttling deployment.

The answer: combine the scale of synthetic data with the accuracy of real-world environments. Niantic Spatial’s real-to-sim pipeline turns captures of deployment environments into simulation-ready digital twins – faster and cheaper than has been possible before – to let embodied AI teams train and evaluate policies in the real places and scenarios their policies will operate in.

Humanoids

Humanoid robots need RGB-based navigation and whole-body control to handle the geometry and visual complexity of real environments. Train and evaluate humanoid policies in a digital twin of those environments.

Warehouse AMRs

Every warehouse is different – from aisles and loading areas to storage zones and changing layouts. Reconstruct the environment at true metric scale. Then, train and evaluate policies in a simulation-ready digital twin.

Drones

Use aerial imagery to build a digital twin of the environment. Then, train and evaluate autonomous flight policies against the real skyline, terrain, and surrounding structures.

## How it works

Create custom scenes from your own environments, or get a head start with our [Places Library](https://www.nianticspatial.com/embodied-ai/places-library-usdz). Follow the steps we have outlined to build your scene.

Delivered as:

one USDZ per place

Contains:

Gaussian splat + aligned collision mesh

Alignment:

gravity-aligned, metric-scale

Capture input:

360 camera, drone

Runs in:

Isaac Sim, Isaac Lab, any USDZ-compatible simulator

Metering:

capture minutes, rolling over

1. 01
	### Walk or fly the site
	Five minutes with an off-the-shelf 360 camera or a drone pass for larger outdoor environments.
2. 02
	### Upload
	Drag and drop into a secure GCS bucket. Enterprise APIs coming soon.
3. 03
	### Reconstruct
	We estimate camera poses, train the splat, and derive the aligned collision mesh from the same reconstruction.
4. 04
	### Train against it
	Lands in your bucket, collider-ready. Training rights attached. You captured it; you own it.

## Enabling visual-spatial intelligence.

Teams building with us today help prioritize what we build tomorrow – join us.

01Available

### Ground.

Start simulation from a metric-scale 3D reconstruction of the real environment, not a synthetic approximation. Delivered as one USDZ with a Gaussian splat and aligned collision mesh.

02Available

### Train and evaluate.

Use the tools you already run: import a USDZ directly into NVIDIA Isaac Sim or Isaac Lab to train and evaluate policies against the real-world environments they need to perform in.

03IN BETA

### Vary.

Turn your sim-ready scenes into domain randomization substrates through generative variation features. Partners get first access.

04Roadmap

### Deploy and feed the loop.

Fleets trained in these environments go live and continuously observe, enabling rapid simulation updates as site conditions change or failure modes emerge, while keeping sensitive operational data private.

## What the policy sees is what it collides with.

The visual scene and the collision mesh come from the same reconstruction, so the environment looks and behaves consistently in simulation. There is no manual cross-registration and no drift between what a policy sees and the surfaces it can hit. Photometric reconstruction can struggle with white walls, glass, and other low-texture surfaces. [MVSAnywhere](https://nianticlabs.github.io/mvsanywhere/) adds zero-shot multi-view depth to produce cleaner, more consistent geometry in those areas.

![](https://lh3.googleusercontent.com/QSGfVWUQdLGULMorMakQPThf7_EvFA9DbcrJcRrVMxvaY23nnuI4Mx8brYpxWfRNLgTJuOyZJMDkUpb1mRPHo6TLwlrgCOnEDLTAzYD5ZjGvPA=s0-e365)

Gaussian Splat

![](https://lh3.googleusercontent.com/AFScHCFtHdq_azGu6AEbZEMFypbWackovPWFwmyDPd5udr7n8SlK9zG41_oLKzzVk0fNLRz_dgNaMQ6kTOyB94N-Si3e2K7hG72LHljGysXe2Q=s0-e365)

Aligned Mesh

## Proven in simulation: Reconstruction-trained RGB policy transfers zero-shot.

[In a comparison conducted by Niantic Spatial and Flexion](https://www.nianticspatial.com/blog/flexion-humanoid-real2sim-sim2real) in collaboration with NVIDIA, an RGB policy trained on a Niantic Spatial 3DGS reconstruction exceeded the conventional depth baseline across two simulated scenes.

92.3%

Reduction vs. synthetic office

27.1%2.1% fall rate

66.1%

Reduction vs. generated mesh

6.2%2.1% fall rate

The reconstruction-trained RGB policy ran zero-shot on a humanoid in the Flexion office and outperformed the depth-based policy. Watch the livestream to learn more.

## Policies trained against real environments are cheaper to ship and easier to trust.

[Explore Plans](https://www.nianticspatial.com/embodied-ai/plans)

DimensionToday, without usWith usThe measure

Speed2

Engineering time

Months hand-building synthetic twins that still transfer badly to the real environment.

Fine-tune in days, on places that already match the environment.

Engineering weeks per environment.

Time to deploy

Tuning cannot start until hardware is onsite. POCs run six to twelve months.

The environment is simulatable before anyone travels. Robots arrive with most of their environment-specific training already complete.

Weeks from POC to production.

Money2

Cost avoided

Edge cases surface in the customer’s operation, where each one costs an incident and weeks of engineering.

Rehearse the environment's failure modes before anything is live.

Incident and clean-up costs avoided.

Revenue won

Deals stall on doubt that the policy will hold in a particular environment.

Arrive with evidence it already works in that exact environment.

Win rate and deal cycle length.

Model quality1

Policy transfer

Policies perceive mesh artifacts as real obstacles and carry those phantom obstacles onto hardware.

The visual layer and the physics layer come from the same reconstruction, ensuring consistency.

Sim-to-real transfer rate.

Flywheel2

Your environment becomes an asset

Every vendor rebuilds the same environment from scratch, each one paid for separately.

One model of the environment that you own and hand to any vendor you choose.

Vendors served per model. Duplicate scanning cut.

Your fleet becomes an asset

Nothing the fleet sees flows back into the environment it trains against.

Each deployment feeds the next, so the model sharpens on the environments your robots actually work in.

Model gain per deployment cycle.

## Build with the most advanced embodied AI teams in the world.

### Explore the Places Library

Use the Places Library to build breadth across real-world scenes that reflect the messy reality of the environments you'll deploy into – helping your policy generalize before it reaches your site.

[Discover Places](https://www.nianticspatial.com/embodied-ai/places-library-usdz)

### Talk to us

Whether you’re running POCs and need to add diversity to your dataset, or are deploying and need to fine-tune your policy for customer environments or edge-case scenarios, we’ll help define the right terms and engagement model for you.

## Frequently Asked Questions

What hardware do I need to capture a real environment?

You can capture the environment with an off-the-shelf 360 camera. Larger outdoor environments can be captured with a drone. The workflow does not require LiDAR, tripod stations, or a specialized capture crew.

Can I import the digital twin into NVIDIA Isaac Sim or Isaac Lab?

Yes. The environment is delivered as a USDZ package that loads directly into NVIDIA Isaac Sim and Isaac Lab (and compatible OpenUSD simulators).

How realistic and metrically accurate is the reconstructed environment?

Without any calibration target, a 360-camera capture reconstructs to within 1% of true scale. With a printed calibration board in the capture, scale is set from a known dimension rather than estimated from camera geometry, and the error drops well below that.

What types of robots can use these simulation environments?

Any. As our real-to-sim stack is optimized for reconstructing places, we find that teams training and deployed mobile embodiments benefit from it most.

What is included in the simulation-ready USDZ package?

Each package includes a photorealistic 3D Gaussian splat and an aligned collision mesh derived from the same reconstruction. The asset is gravity-aligned, metric-scale, and collider-ready for robot simulation and policy training.

Does real-to-sim improve sim-to-real transfer?

[In a comparison conducted by Niantic Spatial and Flexion](https://www.nianticspatial.com/blog/flexion-humanoid-real2sim-sim2real), an RGB navigation policy trained in a reconstructed environment transferred zero-shot to a robot. In simulation, the reconstruction-trained policy matched or exceeded the reported conventional depth baseline across the evaluated scenes.
