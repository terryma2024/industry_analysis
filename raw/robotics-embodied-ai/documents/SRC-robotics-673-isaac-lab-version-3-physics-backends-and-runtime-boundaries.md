---
source_id: "SRC-robotics-673"
title: "Isaac Lab version 3 physics backends and runtime boundaries"
source_type: "documentation"
publisher: "NVIDIA"
source_date: "待验证"
url: "https://isaac-sim.github.io/IsaacLab/v3.0.0/source/concepts/physics_backends.html"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:38:59+00:00"
tags:
  - raw/source
  - source-type/documentation
  - evidence/s
aliases:
  - SRC-robotics-673
---
# Isaac Lab version 3 physics backends and runtime boundaries

## Physics Backends

Isaac Lab supports PhysX, Newton, and OvPhysX through shared asset, sensor, and scene APIs. Choose a backend for the runtime and solvers you need, then select a preset supported by your task. See [Backends and Presets](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/concepts/backends_and_presets.html#backends-and-presets) for launch commands.

## Choose a backend

IsaacSim PhysX

[IsaacSim PhysX](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/concepts/physics-backends/physx.html)

Newton

[Newton](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/concepts/physics-backends/newton.html)

OvPhysX

[OvPhysX](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/concepts/physics-backends/ovphysx.html)

Follow [Installation](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/isaaclab/installation.html#isaaclab-installation-root) for the supported installation paths and current optional extras. Do not combine OvPhysX with a Kit runtime in the same process.

For the general PhysX–Newton policy validation workflow, see [Transfer Policies Between PhysX and Newton](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/how-to/transfer_policies_between_physx_and_newton.html). When a checkpoint’s joint or body ordering differs from the target backend, use the [articulation ordering guide](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/how-to/transfer_policies_between_physx_and_newton.html#joint-and-body-ordering).

## IsaacSim PhysX

IsaacSim PhysX runs through Isaac Sim and Omniverse Kit. It uses the Temporal Gauss-Seidel (TGS) solver by default, with Projective Gauss-Seidel (PGS) also available. Configure scene settings through [`PhysxCfg`](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/api/lab_physx/isaaclab_physx.physics.html#isaaclab_physx.physics.PhysxCfg "isaaclab_physx.physics.PhysxCfg") and asset properties through [Physics Schemas](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/concepts/schema_cfgs.html). Large or contact-rich scenes may need additional GPU buffer capacity.

See [the IsaacSim PhysX guide](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/concepts/physics-backends/physx.html) for runtime details and [Tune the PhysX Solver](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/how-to/solver_tuning_physx.html#physx-solver-tuning) for solver and buffer settings.

## Newton

Newton runs on Warp without requiring Isaac Sim. Its solvers cover different simulation needs: MJWarp and Kamino for rigid robots, VBD for cloth and soft bodies, and MPM for particle materials. Configure the backend with [`NewtonCfg`](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/api/lab_newton/isaaclab_newton.physics.html#isaaclab_newton.physics.NewtonCfg "isaaclab_newton.physics.NewtonCfg") and select a solver through `solver_cfg`. Native Warp arrays are available for custom simulation code.

See [the Newton guide](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/concepts/physics-backends/newton.html) for solver choices, tuning guides, and native data access.

## OvPhysX

OvPhysX runs PhysX without Isaac Sim or Omniverse Kit. It supports rigid objects, articulations, contact and motion sensors, and CUDA-based deformables, and can pair with OVRTX for rendering. Scene-level solver settings come primarily from USD’s `PhysicsScene`; [`OvPhysxCfg`](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/api/lab_ov/isaaclab_ov.physics.html#isaaclab_ov.physics.OvPhysxCfg "isaaclab_ov.physics.OvPhysxCfg") holds additional settings such as GPU buffer capacities. It cannot share a process with Kit.

See [the OvPhysX guide](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/concepts/physics-backends/ovphysx.html) for installation, supported features, and their configuration limits.

## Find supported tasks and APIs

Backend support is task-specific. Use [Environments](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/isaaclab/environments.html) to browse registered environments and presets, or ask a task for its current choices:

```bash
uv run isaaclab train --rl_library rsl_rl \
   --task Isaac-Cartpole-Direct --help
```

The help output is the source of truth for that task’s `physics=` choices. For native solver data and views, see the [PhysX](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/concepts/physics-backends/physx.html#physx-native-access), [Newton](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/concepts/physics-backends/newton.html#newton-native-access), and [OvPhysX](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/concepts/physics-backends/ovphysx.html#ovphysx-native-access) access guides. For field-level configuration, follow the generated API links for [`PhysxCfg`](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/api/lab_physx/isaaclab_physx.physics.html#isaaclab_physx.physics.PhysxCfg "isaaclab_physx.physics.PhysxCfg"), [`NewtonCfg`](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/api/lab_newton/isaaclab_newton.physics.html#isaaclab_newton.physics.NewtonCfg "isaaclab_newton.physics.NewtonCfg"), its solver configurations, and [`OvPhysxCfg`](https://isaac-sim.github.io/IsaacLab/v3.0.0/source/api/lab_ov/isaaclab_ov.physics.html#isaaclab_ov.physics.OvPhysxCfg "isaaclab_ov.physics.OvPhysxCfg").
