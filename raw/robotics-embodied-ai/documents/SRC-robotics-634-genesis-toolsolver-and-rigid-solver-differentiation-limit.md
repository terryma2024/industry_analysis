---
source_id: "SRC-robotics-634"
title: "Genesis ToolSolver and rigid solver differentiation limit"
source_type: "documentation"
publisher: "Genesis AI"
source_date: "待验证"
url: "https://genesis-world.readthedocs.io/en/latest/api_reference/engine/solvers/tool_solver.html"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:35:43+00:00"
tags:
  - raw/source
  - source-type/documentation
  - evidence/s
aliases:
  - SRC-robotics-634
---
# Genesis ToolSolver and rigid solver differentiation limit

## ToolSolver

The `ToolSolver` handles kinematic tools and end-effectors that drive other entities through one-way coupling into the soft solvers (MPM, FEM, PBD, SPH). A `ToolEntity` carries no internal dynamics and comes from a single mesh. It is a temporary workaround for differentiable rigid-soft interaction and will be removed once the `RigidSolver` supports differentiability directly.

## Options

*class* genesis.options.solvers.ToolOptions(*\**, *dt: float | None = None*, *floor\_height: float | None = None*) → None [\[source\]](https://genesis-world.readthedocs.io/en/latest/_modules/genesis/options/solvers.html#ToolOptions) [#](#genesis.options.solvers.ToolOptions "Permalink to this definition")

Options configuring the ToolSolver.

> [!note] Note
> ToolEntity is a simplified form of RigidEntity. It supports one way tool->other coupling, but has *no* internal dynamics and can only be created from a single mesh. This is a temporal workaround for differentiable rigid-soft interaction. This solver will be removed once differentiable mode is supported by the RigidSolver.

Parameters:

**floor\_height** (*float**,* *optional*) – Height of the floor in meters. Defaults to 0.0.

## ToolSolver

*class* genesis.engine.solvers.tool\_solver.ToolSolver(*scene*, *sim*, *options*) [\[source\]](https://genesis-world.readthedocs.io/en/latest/_modules/genesis/engine/solvers/tool_solver.html#ToolSolver) [#](#genesis.engine.solvers.tool_solver.ToolSolver "Permalink to this definition")

Bases: `TimeBasedMixin`, `Solver`

> [!note] Note
> !! This class will be removed once we added differntiability to the RigidSolver. This is just a temporary solution to obtain rigid->soft one-way differeitable coupling.

material\_cls [#](#genesis.engine.solvers.tool_solver.ToolSolver.material_cls "Permalink to this definition")

alias of [`Tool`](https://genesis-world.readthedocs.io/en/latest/api_reference/engine/material/tool.html#genesis.engine.materials.tool.Tool "genesis.engine.materials.tool.Tool")

build() [\[source\]](https://genesis-world.readthedocs.io/en/latest/_modules/genesis/engine/solvers/tool_solver.html#ToolSolver.build) [#](#genesis.engine.solvers.tool_solver.ToolSolver.build "Permalink to this definition")

*property* is\_active [#](#genesis.engine.solvers.tool_solver.ToolSolver.is_active "Permalink to this definition")

setup\_boundary() [\[source\]](https://genesis-world.readthedocs.io/en/latest/_modules/genesis/engine/solvers/tool_solver.html#ToolSolver.setup_boundary) [#](#genesis.engine.solvers.tool_solver.ToolSolver.setup_boundary "Permalink to this definition")

add\_entity(*idx*, *material*, *morph*, *surface*, *visualize\_contact=False*, *name: str | None = None*, *desc=None*) → [ToolEntity](https://genesis-world.readthedocs.io/en/latest/api_reference/engine/entity/tool_entity.html#genesis.engine.entities.tool_entity.tool_entity.ToolEntity "genesis.engine.entities.tool_entity.tool_entity.ToolEntity") [\[source\]](https://genesis-world.readthedocs.io/en/latest/_modules/genesis/engine/solvers/tool_solver.html#ToolSolver.add_entity) [#](#genesis.engine.solvers.tool_solver.ToolSolver.add_entity "Permalink to this definition")

reset\_grad() [\[source\]](https://genesis-world.readthedocs.io/en/latest/_modules/genesis/engine/solvers/tool_solver.html#ToolSolver.reset_grad) [#](#genesis.engine.solvers.tool_solver.ToolSolver.reset_grad "Permalink to this definition")

## See also

- [Tool](https://genesis-world.readthedocs.io/en/latest/api_reference/engine/material/tool.html): the tool material and its parameters.
- [Couplers](https://genesis-world.readthedocs.io/en/latest/api_reference/engine/couplers/index.html): coupling with other solvers.
