---
source_id: "SRC-robotics-380"
title: "Geely humanoid Real2Sim2Real deployment case"
source_type: "customer_case"
publisher: "Lightwheel"
source_date: "2026-08-06"
url: "https://lightwheel.ai/media/geely-humanoid-robots"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-08-06T02:05:23+00:00"
tags:
  - raw/source
  - source-type/customer-case
  - evidence/a
aliases:
  - SRC-robotics-380
---
# Geely humanoid Real2Sim2Real deployment case

Geely's self-developed humanoid robots are running on Geely Auto's production line — sorting and sequencing parts alongside human operators. Getting there meant solving two problems that have stalled humanoid deployment across manufacturing: collecting enough real-world training data without disrupting production, and closing the gap between simulated training and real-world performance.

Geely compressed that path from months per task to weeks by building on Lightwheel's Real2Sim2Real infrastructure, a closed loop that starts with how their own operators perform the work, trains policies in physics-grounded simulation, and keeps those policies improving once they're on the line.

Summary

- The Real2Sim2Real loop compressed the per-task training-and-iteration cycle from months to week-scale, with an order-of-magnitude reduction in training cost.
- Robots were trained from how Geely's own operators perform the work, captured as accurate, robot-ready human demonstration data.
- Simulation was grounded in measured physics — Geely's real production equipment was measured to calibrate the physics solver and the assets' physical properties.
- A continuous learning loop keeps deployed policies improving by directing new data collection to where they are weakest.

## The Challenge: Why Scaling Humanoids on Production Line Was Hard

Deploying humanoid robots into live production has been held back by two barriers. Real-world data is slow and costly to collect, which limits how quickly new tasks can be trained. And policies trained in simulation often fail to transfer to physical hardware, where lighting, materials, and contact dynamics differ from what the simulator assumed. For a manufacturer scaling humanoids across many tasks, a months-long cycle per task — and policies that degrade when conditions shift — does not scale.

Geely needed an approach that addressed both barriers: a way to capture how their operators actually perform the work, a simulation environment grounded in the real physics of their line, and a learning loop that keeps deployed policies improving rather than decaying. They built that approach on Lightwheel's Real2Sim2Real infrastructure.

![](https://lw-cdn.lightwheel.net/build/lightwheel/_next/static/media/image-3.138dc4d3.webp)

## Learning From the Operators on Geely's Line

Geely needed its robots to learn from the people already doing the job. Operators were captured first-person on the live line during normal production, not scripted, not on a stopped line, so demonstrations could be gathered at scale without disrupting output. Lightwheel's egocentric capture system (EgoSuite) runs as a single wearable rig: a head unit for RGB-D video paired with gloves and wrist cameras for fine hand detail, recording everything the operator does in one time-synchronized stream.

Each recording is annotated across three dimensions: hand pose, full-body pose, and action-level semantics, with tracking kept consistent frame to frame. Every sequence is validated against motion-capture ground truth, confirming the millimeter-level hand and centimeter-level body accuracy that contact-rich work like precise part placement and dual-arm handling depends on. The result is robot-ready demonstration data that reflects exactly how each task is performed on Geely's line.

## Simulation Grounded in Geely's Measured Physics

For simulation to replace real-world data collection and iteration, it has to behave like the real production line. Geely's actual production equipment and tooling were measured in Lightwheel's Physical Measurement Factory, where robotic rigs capture real contact, friction, and dynamics directly off the hardware. Those measurements calibrate the physics solver so the digital environment reproduces how Geely's equipment actually behaves. On Lightwheel's Real2Sim fidelity benchmark, simulated force response closely matches real measured response.

The validated digital twin of the line let Geely expand a focused set of human demonstrations into a large, varied training set spanning different lighting, materials, and object positions. The NVIDIA GR00T N1.7 foundation model was then fine-tuned to the humanoid robot and to each task entirely inside that twin, built on NVIDIA Isaac Sim and Isaac Lab.

## A Continuous Learning Loop From Evaluation to Deployment

At Geely, evaluation and deployment form a loop. Before a policy reaches the floor, it is tested against the line's real constraints and failure modes: cycle-time limits, varied lighting, occlusion, and contact edge cases. Policies that pass are deployed to physical robots.

The system then learns from what happens next. Tasks with low success rates in evaluation and on the robots deployed on the production line direct the next round of data collection. New egocentric demonstrations are captured with EgoSuite where a policy is weak, those scenarios are regenerated in simulation, and the model improves on the specific gap. Each cycle makes the next policy stronger, so Geely's deployed robots continue to improve over time.

![](https://lw-cdn.lightwheel.net/build/lightwheel/_next/static/media/image-2.46c7fa4e.webp)

## Results

Geely compressed the per-task training-and-iteration cycle from months to weeks, reducing it by 10x. A 100:1 simulated-to-real data ratio sharply reduced the need for real-world data collection, training costs fell by an order of magnitude, and no dedicated test lines were required.

Today, Geely's humanoid robots operate stably alongside workers in live production, performing component transport, part placement on inspection trays, and dual-arm manipulation of heavy components. Because the same loop powers every new task, Geely can bring on new workstations faster and keep deployed robots improving, the foundation for scaling humanoids across more lines and more sites.
