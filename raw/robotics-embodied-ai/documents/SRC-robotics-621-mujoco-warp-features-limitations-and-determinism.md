---
source_id: "SRC-robotics-621"
title: "MuJoCo Warp features limitations and determinism"
source_type: "documentation"
publisher: "Google DeepMind"
source_date: "待验证"
url: "https://mujoco.readthedocs.io/en/stable/mjwarp/"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:35:43+00:00"
tags:
  - raw/source
  - source-type/documentation
  - evidence/s
aliases:
  - SRC-robotics-621
---
# MuJoCo Warp features limitations and determinism

MuJoCo Warp (MJWarp) is an implementation of MuJoCo written in [Warp](https://nvidia.github.io/warp/) and optimized for [NVIDIA](https://nvidia.com/) hardware and parallel simulation. MJWarp lives in the [google-deepmind/mujoco\_warp](https://github.com/google-deepmind/mujoco_warp) GitHub repository.

MJWarp is developed and maintained as a joint effort by [NVIDIA](https://nvidia.com/) and [Google DeepMind](https://deepmind.google/).

## Tutorial notebook

The MJWarp basics are covered in a tutorial [\[notebook\]](https://github.com/google-deepmind/mujoco_warp/blob/main/notebooks/tutorial.ipynb) [\[open in colab\]](https://colab.research.google.com/github/google-deepmind/mujoco_warp/blob/main/notebooks/tutorial.ipynb).

## When To Use MJWarp?

### High throughput

The MuJoCo ecosystem offers multiple options for batched simulation.

- [mujoco.rollout](https://mujoco.readthedocs.io/en/stable/python.html#pyrollout): Python API for multi-threaded calls to [mj\_step](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-step) on CPU. High throughput can be achieved with hardware that has fast cores and large thread counts, but overall performance of applications requiring frequent host<>device transfers (e.g., reinforcement learning with simulation on CPU and learning on GPU) may be bottlenecked by transfer overhead.
- [mjx.step](https://mujoco.readthedocs.io/en/stable/mjx.html#mjxfunctions): `jax.vmap` and `jax.pmap` enable multi-threaded and multi-device simulation with JAX on CPUs, GPUs, or TPUs.
- [`mujoco_warp.step`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.step "mujoco_warp.step"): Python API for high throughput simulation targeting NVIDIA GPUs. Scales better than MJX on nearly every workload, in particular complex simulation scenes. Works well with PyTorch.

### Low latency

MJWarp is optimized for throughput: the total number of simulation steps per unit time whereas MuJoCo is optimized for latency: time for one simulation step. It is expected that a simulation step with MJWarp will be less performant than a step with MuJoCo for the same simulation.

As a result, MJWarp is well suited for applications where large numbers of samples are required, like reinforcement learning, while MuJoCo is likely more useful for real-time applications like online control (e.g., model predictive control) or interactive graphical interfaces (e.g., simulation-based teleoperation).

### Complex scenes

MJWarp scales better than MJX for scenes with many geoms or degrees of freedom, but not as well as MuJoCo for single large kinematic trees. MJWarp can scale to scenes with hundreds of degrees of freedom as long as [sleeping](https://mujoco.readthedocs.io/en/stable/computation/index.html#sleeping) is enabled and the scene can be partitioned into independent islands with dormant bodies. Improving performance for single connected mechanisms beyond ~60 DoFs remains an active priority.

### Differentiability

The dynamics API in MJX is automatically differentiable via JAX. We are considering whether to support this in MJWarp via Warp - if this feature is important to you, please chime in on this issue [here](https://github.com/google-deepmind/mujoco_warp/issues/500).

## Installation

**From PyPI:**

```shell
pip install mujoco-warp
```

**From source:**

```shell
git clone https://github.com/google-deepmind/mujoco_warp.git
cd mujoco_warp
uv sync --all-extras
```

To make sure everything is working:

```shell
uv run pytest -n 8
```

## Basic Usage

Once installed, the package can be imported via `import mujoco_warp as mjw`. Structs, functions, and enums are available directly from the top-level [`mjw`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#module-mujoco_warp "mujoco_warp") module.

### Structs

Before running MJWarp functions on an NVIDIA GPU, structs must be copied onto the device via [`mjw.put_model`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.put_model "mujoco_warp.put_model") and [`mjw.make_data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.make_data "mujoco_warp.make_data") or [`mjw.put_data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.put_data "mujoco_warp.put_data") functions. Placing an [mjModel](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjmodel) on device yields an [`mjw.Model`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Model "mujoco_warp.Model"). Placing an [mjData](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjdata) on device yields an [`mjw.Data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Data "mujoco_warp.Data").

```python
mjm = mujoco.MjModel.from_xml_string("...")
mjd = mujoco.MjData(mjm)
m = mjw.put_model(mjm)
d = mjw.put_data(mjm, mjd)
```

These MJWarp variants mirror their MuJoCo counterparts but have a few key differences:

1. [`mjw.Model`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Model "mujoco_warp.Model") and [`mjw.Data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Data "mujoco_warp.Data") contain Warp arrays that are copied onto device.
2. Some fields are missing from [`mjw.Model`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Model "mujoco_warp.Model") and [`mjw.Data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Data "mujoco_warp.Data") for features that are unsupported.

### Batch sizes

MJWarp is optimized for parallel simulation. A batch of simulations can be specified with three parameters:

- [`nworld`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Data.nworld "mujoco_warp.Data.nworld"): Number of worlds to simulate.
- nconmax: Expected number of contacts per world. The maximum number of contacts for all worlds is `nconmax * nworld`.
- naconmax: Alternative to, maximum number of contacts over all worlds. If and are both set then is ignored.
- njmax: Maximum number of constraints per world.

> [!note] Semantic difference for nconmax and njmax.
> It is possible for the number of contacts per world to exceed if the total number of contacts for all worlds does not exceed `nworld x nconmax`. However, the number of constraints per world is strictly limited by.

> [!note] XML parsing
> Values for and are not parsed from [size/nconmax](https://mujoco.readthedocs.io/en/stable/XMLreference.html#size-nconmax) and [size/njmax](https://mujoco.readthedocs.io/en/stable/XMLreference.html#size-njmax) (these parameters are deprecated). Values for these parameters must be provided to [`mjw.make_data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.make_data "mujoco_warp.make_data") or [`mjw.put_data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.put_data "mujoco_warp.put_data").

### Functions

MuJoCo functions are exposed as MJWarp functions of the same name, but following [PEP 8](https://peps.python.org/pep-0008/) -compliant names. Most of the [main simulation](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mainsimulation) and some of the [sub-components](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#subcomponents) for forward simulation are available from the top-level [`mjw`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#module-mujoco_warp "mujoco_warp") module.

### Minimal example

```python
# Throw a ball at 100 different velocities.

import mujoco
import mujoco_warp as mjw
import warp as wp

_MJCF=r"""
<mujoco>
  <worldbody>
    <body>
      <freejoint/>
      <geom size=".15" mass="1" type="sphere"/>
    </body>
  </worldbody>
</mujoco>
"""

mjm = mujoco.MjModel.from_xml_string(_MJCF)
m = mjw.put_model(mjm)
d = mjw.make_data(mjm, nworld=100)

# initialize velocities
wp.copy(d.qvel, wp.array([[float(i) / 100, 0, 0, 0, 0, 0] for i in range(100)], dtype=float))

# simulate physics
mjw.step(m, d)

print(f'qpos:\n{d.qpos.numpy()}')
```

### Command line scripts

Benchmark an environment with testspeed

```shell
mjwarp-testspeed benchmark/humanoid/humanoid.xml
```

Interactive environment simulation with MJWarp

```shell
mjwarp-viewer benchmark/humanoid/humanoid.xml
```

## Feature Parity

MJWarp supports most of the main simulation features of MuJoCo, with a few exceptions. MJWarp will raise an exception if asked to copy to device an [mjModel](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjmodel) with field values referencing unsupported features. For the most up-to-date feature availability, please see [MuJoCo API Compatibility](https://github.com/google-deepmind/mujoco_warp#mujoco-api-compatibility).

## Performance Tuning

The following are considerations for optimizing the performance of MJWarp.

### Graph capture

MJWarp functions, for example [`mjw.step`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.step "mujoco_warp.step"), often comprise a collection of kernel launches. Warp will launch these kernels individually if the function is called directly. To improve performance, especially if the function will be called multiple times, it is recommended to capture the operations that comprise the function as a CUDA graph

```python
with wp.ScopedCapture() as capture:
  mjw.step(m, d)
```

The graph can then be launched or re-launched

```python
wp.capture_launch(capture.graph)
```

and will typically be significantly faster compared to calling the function directly. Please see the [Warp Graph API reference](https://nvidia.github.io/warp/stable/user_guide/execution_and_performance/concurrency.html#graph-launches) for details.

### Batch sizes

The maximum numbers of contacts and constraints, / and respectively, are specified when creating [`mjw.Data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Data "mujoco_warp.Data") with [`mjw.make_data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.make_data "mujoco_warp.make_data") or [`mjw.put_data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.put_data "mujoco_warp.put_data"). Memory and computation scales with the values of these parameters. For best performance, the values of these parameters should be set as small as possible while ensuring the simulation does not exceed these limits.

It is expected that good values for these limits will be environment specific. In practice, selecting good values typically involves trial-and-error. `mjwarp-testspeed` with the flag `--measure_alloc` for printing the number of contacts and constraints at each simulation step, `--overflow_behavior=error` (default) for detecting overflows, and programmatic inspection via can all be useful techniques for iteratively testing values for these parameters.

### Solver iterations

MuJoCo’s default solver settings for the maximum numbers of [solver iterations](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-iterations) and [linesearch iterations](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-ls-iterations) are expected to provide reasonable performance. Reducing MJWarp’s settings [`Option.iterations`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Option.iterations "mujoco_warp.Option.iterations") and/or [`Option.ls_iterations`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Option.ls_iterations "mujoco_warp.Option.ls_iterations") limits may improve performance and should be secondary considerations after tuning / and.

Reducing these limits too much may prevent the constraint solver from converging and can lead to inaccurate or unstable simulation.

> [!note] Impact on Performance: MJX (JAX) and MJWarp
> In [MJX](https://mujoco.readthedocs.io/en/stable/mjx.html#mjx) these solver parameters are key for controlling simulation performance. With MJWarp, in contrast, once all worlds have converged the solver can early exit and avoid unnecessary computation. As a result, the values of these settings have comparatively less impact on performance.

### Contact sensor matching

Scenes that include [contact sensors](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-contact) have a parameter that specifies the maximum number of matched contacts per sensor `Option.contact_sensor_max_match`. For best performance, the value of this parameter should be as small as possible while ensuring the simulation does not exceed the limit. Matched contacts that exceed this limit will be ignored.

The value of this parameter can be set directly, for example `model.opt.contact_sensor_maxmatch = 16`, or via an XML custom numeric field

```xml
<custom>
  <numeric name="contact_sensor_maxmatch" data="16"/>
</custom>
```

Similar to the maximum numbers of contacts and constraints, a good value for this setting is expected to be environment specific. `mjwarp-testspeed` and `mjwarp-viewer` may be useful for tuning the value of this parameter.

### Memory

Simulation throughput is often limited by memory requirements for large numbers of worlds. Considerations for optimizing memory utilization include:

- CCD colliders require more memory than primitive colliders, see the for information about colliders.
- [multiccd](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-multiccd) requires more memory than CCD.
- CCD memory requirements scale linearly with [Option.ccd\_iterations](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-ccd-iterations).
- A scene with at least one mesh geom and using [multiccd](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-multiccd) will have memory requirements that scale linearly with the maximum number of vertices per face and with the maximum number of edges per vertex, computed over all meshes.

provides the flag `--memory` for reporting a simulation’s total memory utilization and information about [`mjw.Model`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Model "mujoco_warp.Model") and [`mjw.Data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Data "mujoco_warp.Data") fields that require significant memory. Memory allocated inline, including for CCD and the constraint solver, can also be significant and is reported as `Other memory`.

> [!note] Maximum number of contacts per collider
> Some MJWarp colliders have a different maximum number of contacts compared to MuJoCo (see the ):
> 
> - `PLANE<>MESH`: 4 versus 3
> - `HFieldCCD`: 4 versus `mjMAXCONPAIR`

Sparse Jacobians (e.g., `efc.J`, `ten_J`, `flexedge_J`, and `actuator_moment`) store only potentially non-zero entries, reducing memory and skipping zero arithmetic. For high-DoF scenes ($n_v > 60$), sparsity enables simulations that are unsupported in dense mode. For example, in the Aloha clutter benchmark ($n_v = 136$, 2048 worlds, `njmax = 384`), the sparse representation of `efc.J` and its column indices `efc.J_colind` requires ~84 MB combined (~42 MB each) compared to ~408 MB for dense `efc.J`, a +4x reduction in memory.

The [`mjw.make_data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.make_data "mujoco_warp.make_data") or [`mjw.put_data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.put_data "mujoco_warp.put_data") argument `nccdmax` / `naccdmax` can be set to a value less than / in order to reduce the memory requirements for CCD. The value for this parameter should be the maximum number of contacts generated by a CCD collider, per world or for all worlds, respectively. For example, a batched simulation with 10 worlds that generates 80 total contacts with per-collider contacts: mesh-mesh: 30 (CCD), ellipsoid-ellipsoid: 10 (CCD), and sphere-sphere: 40 (primitive) should set / to at least 8 / 80 (may require more for broadphase) and `nccdmax` / `naccdmax` to 3 / 30.

### Large scenes

Simulating scenes with many DoFs (i.e., `nv`) can be computationally expensive. However, in many scenarios, a significant portion of the scene may be stationary. MJWarp can put stationary objects to *sleep* (see [Sleeping islands](https://mujoco.readthedocs.io/en/stable/computation/index.html#sleeping)), excluding them from the working set of many of its calculations. Furthermore, MJWarp groups bodies into independent [islands](https://mujoco.readthedocs.io/en/stable/computation/index.html#soisland); if all bodies in an island are stationary, the entire island is put to sleep. Currently, both the collision pipeline and the constraint solver benefit from sleeping, and more sleeping-aware components may be added in the future.

#### Compact solver

To optimize performance in scenes with many total DoFs but a relatively small number of active DoFs (typically fewer than 64, such as two robot arms with grippers (16 DoFs) and 8 active objects (48 DoFs)), MJWarp provides a **compact solver** that leverages this sleeping mechanism:

1. Identifies the set of active DOFs for each world, determined from the active islands.
2. **Compacts** these active DOFs into a single, contiguous dense workspace of a known maximum size (`nvmax`).
3. Executes the constraint solver (Newton) using GPU-optimized tile operations (such as blocked Cholesky factorization) of fixed size on this compacted space.
4. Scatters the results back to the global state, freezing the inactive DOFs.

By using a fixed-size compacted workspace, the solver avoids GPU thread divergence and leverages high-performance tensor/matrix operations optimized for fixed tile sizes.

Enabling the compact solver

1. Enable the Newton solver:
	- Via XML:
		```xml
		<option solver="Newton"/>
		```
		- Via Python `MjSpec`:
		```python
		spec = mujoco.MjSpec()
		spec.option.solver = mujoco.mjtSolver.mjSOL_NEWTON
		```
2. Enable sleep:
	- Via XML:
		```xml
		<option>
		  <flag sleep="enable"/>
		</option>
		```
		- Via Python `MjSpec`:
		```python
		spec = mujoco.MjSpec()
		spec.option.enableflags |= mujoco.mjtEnableBit.mjENBL_SLEEP
		```
3. Specify the maximum expected active DOFs for any world (`nvmax`) when allocating data. This sizes the compacted workspace.
	- In Python:
		```python
		# Allocate data with a maximum of 64 active DOFs per world
		d = mjw.make_data(mjm, nworld=2048, nvmax=64)
		```
		- Via the command line:
		```shell
		mjwarp-testspeed scene.xml --nvmax=64
		```
	If `nvmax` is not specified, it defaults to the full number of DOFs (`nv`). Sizing `nvmax` to a tight upper bound of the expected active DOFs significantly reduces GPU memory usage and improves throughput.
4. When setting `nvmax < nv` it is recommended to initialize all trees to asleep in order to avoid initial dof overflow.
	```python
	d.tree_asleep.assign(np.array(np.arange(mjm.ntree, dtype=np.int32)), dtype=np.int32)
	```

> [!note] Note
> Consider increasing the sleep tolerance setting (e.g., `sleep_tolerance="0.01"` in XML options or `spec.option.sleep_tolerance = 0.01` in Python) from its default value (0.001) to more quickly sleep objects.

### Overflow detection

MJWarp relies on fixed-size buffer allocations ( /,, `nccdmax` / `naccdmax`, `nvmax`, [`Option.contact_sensor_maxmatch`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Option.contact_sensor_maxmatch "mujoco_warp.Option.contact_sensor_maxmatch")) for high-throughput GPU execution. When simulation demands exceed these pre-allocated limits, an overflow occurs, leading to undefined behavior.

MJWarp tracks overflows per world in [`Data.overflow`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Data.overflow "mujoco_warp.Data.overflow"), a 1D Warp array of shape `(nworld,)` storing bitmasks of [`mjw.OverflowType`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.OverflowType "mujoco_warp.OverflowType").

[`Data.overflow`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Data.overflow "mujoco_warp.Data.overflow") is initialized to zero upon creation and cleared on [`mjw.reset_data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.reset_data "mujoco_warp.reset_data").

Checking for overflows programmatically

```python
mjw.step(m, d)

# device-to-host transfer
overflow = d.overflow.numpy()

# check worlds for any overflow
any_overflow = np.any(overflow != 0)

# check for each world for (narrowphase) contact overflow
has_contact_overflow = (overflow & mjw.OverflowType.NARROWPHASE) != 0
```

Controlling warnings

By default, [`Option.warn_overflow`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Option.warn_overflow "mujoco_warp.Option.warn_overflow") is `True`, causing kernels to print warning messages to stdout via `wp.printf` when an overflow occurs. Setting `m.opt.warn_overflow = False` suppresses these GPU-side warning prints while still recording the overflow bitmasks in [`Data.overflow`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Data.overflow "mujoco_warp.Data.overflow").

In, the command-line flag `--overflow_behavior=error` (default) automatically checks [`Data.overflow`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Data.overflow "mujoco_warp.Data.overflow") and aborts with a diagnostic error if any world overflows, while `--overflow_behavior=continue` allows execution to proceed with warnings enabled.

Performance implications

- **Device printf overhead**: Printing warnings from GPU kernels (`m.opt.warn_overflow = True`) serializes execution across threads, introduces CUDA device synchronizations, and can severely degrade simulation throughput when many parallel worlds overflow. Disabling warnings (`m.opt.warn_overflow = False`) eliminates this GPU I/O overhead.
- **Host-device synchronization**: Reading [`Data.overflow`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Data.overflow "mujoco_warp.Data.overflow") on CPU via `d.overflow.numpy()` requires a device-to-host memory copy and pipeline synchronization. In high-throughput reinforcement learning pipelines, avoid synchronizing on every simulation step; instead, check [`Data.overflow`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Data.overflow "mujoco_warp.Data.overflow") periodically (e.g., at environment reset or rollout boundaries) or inspect the tensor directly on device.
- **Simulation fidelity**: If warnings are disabled and [`Data.overflow`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Data.overflow "mujoco_warp.Data.overflow") is not checked, overflows will lead to undefined behavior.

## Batched Model Fields

To enable batched simulation with different model parameter values, many [`mjw.Model`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Model "mujoco_warp.Model") fields have a leading batch dimension. By default, the leading dimension is 1 (i.e., `field.shape[0] == 1`) and the same value(s) will be applied to all worlds. It is possible to set batch sizes per field

```python
m = mjw.put_model(mjm, batch_sizes={"dof_damping": 2})
m.dof_damping.assign(np.array([[0.1], [0.2]], dtype=float))
```

and then override the default values. Batched fields will be indexed with a modulo operation of the world id and batch dimension: `field[worldid % field.shape[0]]`.

### Modifying fields

The recommended workflow for modifying an [mjModel](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjmodel) field is to first modify the corresponding [mjSpec](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjspec) and then compile to create a new [mjModel](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjmodel) with the updated field. However, compilation currently requires a host call: 1 call per new field instance, i.e., `nworld` host calls for `nworld` instances.

Certain fields are safe to modify directly without compilation, enabling on-device updates. Please see [mjModel changes](https://mujoco.readthedocs.io/en/stable/programming/simulation.html#sichange) for details about specific fields. Additionally, [GitHub issue 893](https://github.com/google-deepmind/mujoco_warp/issues/893) tracks adding on-device updates for a subset of fields.

### Per-world assets

Per-world assets enable heterogeneous worlds where different worlds simulate different [assets](https://mujoco.readthedocs.io/en/latest/XMLreference.html#asset) including meshes, height fields, materials, and textures. The general workflow is:

1. Create an [mjSpec](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjspec) with **all** assets.
2. Compile each variant by mutating the spec and calling `spec.compile()`.
3. Compile a **base** model and create [`mjw.Model`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Model "mujoco_warp.Model") from it.
4. Override the relevant [`mjw.Model`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Model "mujoco_warp.Model") fields with per-world arrays built from the compiled variants.

Per-world meshes

**Example 1 — Per-world meshes: Geom-level** randomization (1 body, 1 geom, 2 mesh assets):

The base scene includes all mesh assets. The geom references one mesh (`mesh_a`); a second mesh (`mesh_b`) is available for per-world substitution.

```xml
<mujoco>
  <asset>
    <mesh name="mesh_a" vertex="0 0 0 1 0 0 0 1 0 0 0 1"/>
    <mesh name="mesh_b" vertex="0 0 0 2 0 0 0 2 0 0 0 2"/>
  </asset>
  <worldbody>
    <body pos="0 0 1">
      <freejoint/>
      <geom name="obj" type="mesh" mesh="mesh_a"/>
    </body>
  </worldbody>
</mujoco>
```

```python
nworld = 4

# base spec: 1 body with 1 mesh geom, all mesh assets
spec = mujoco.MjSpec()
mesh_a = spec.add_mesh()
mesh_a.name = "mesh_a"
mesh_a.uservert = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]

mesh_b = spec.add_mesh()
mesh_b.name = "mesh_b"
mesh_b.uservert = [0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2]

body = spec.worldbody.add_body()
body.pos = [0, 0, 1]
body.add_freejoint()
geom = body.add_geom()
geom.name = "obj"
geom.type = mujoco.mjtGeom.mjGEOM_MESH
geom.meshname = "mesh_a"

# compile each variant
geom.meshname = "mesh_a"
mjm_a = spec.compile()
geom.meshname = "mesh_b"
mjm_b = spec.compile()

# restore and compile base
geom.meshname = "mesh_a"
mjm = spec.compile()

m = mjw.put_model(mjm)
d = mjw.make_data(mjm, nworld=nworld)

# build per-world arrays: worlds 0-1 use mesh_a, worlds 2-3 use mesh_b
geom_id = mujoco.mj_name2id(mjm, mujoco.mjtObj.mjOBJ_GEOM, "obj")
variants = [mjm_a, mjm_b]
assignment = [0, 0, 1, 1]  # variant index per world

# build per-world arrays
dataid = np.tile(mjm.geom_dataid, (nworld, 1))
geom_size = np.zeros((nworld, mjm.ngeom, 3))
geom_aabb = np.zeros((nworld, mjm.ngeom, 2, 3))
geom_rbound = np.zeros((nworld, mjm.ngeom))
geom_pos = np.zeros((nworld, mjm.ngeom, 3))
body_mass = np.zeros((nworld, mjm.nbody))
body_subtreemass = np.zeros((nworld, mjm.nbody))
body_inertia = np.zeros((nworld, mjm.nbody, 3))
body_invweight0 = np.zeros((nworld, mjm.nbody, 2))
body_ipos = np.zeros((nworld, mjm.nbody, 3))
body_iquat = np.zeros((nworld, mjm.nbody, 4))

for w in range(nworld):
  ref = variants[assignment[w]]
  dataid[w, geom_id] = ref.geom_dataid[geom_id]
  geom_size[w] = ref.geom_size
  geom_aabb[w] = ref.geom_aabb.reshape(mjm.ngeom, 2, 3)
  geom_rbound[w] = ref.geom_rbound
  geom_pos[w] = ref.geom_pos
  body_mass[w] = ref.body_mass
  body_subtreemass[w] = ref.body_subtreemass
  body_inertia[w] = ref.body_inertia
  body_invweight0[w] = ref.body_invweight0
  body_ipos[w] = ref.body_ipos
  body_iquat[w] = ref.body_iquat

m.geom_dataid = wp.array(dataid, dtype=int)
m.geom_size = wp.array(geom_size, dtype=wp.vec3)
m.geom_aabb = wp.array(geom_aabb, dtype=wp.vec3)
m.geom_rbound = wp.array(geom_rbound, dtype=float)
m.geom_pos = wp.array(geom_pos, dtype=wp.vec3)
m.body_mass = wp.array(body_mass, dtype=float)
m.body_subtreemass = wp.array(body_subtreemass, dtype=float)
m.body_inertia = wp.array(body_inertia, dtype=wp.vec3)
m.body_invweight0 = wp.array(body_invweight0, dtype=wp.vec2)
m.body_ipos = wp.array(body_ipos, dtype=wp.vec3)
m.body_iquat = wp.array(body_iquat, dtype=wp.quat)
```

**Example 2 — Per-world meshes: Body-level** randomization (1 body, 1 or 2 geoms, 3 mesh assets):

> [!important] Maximum geom count
> For body-level randomization, the base `mjModel` provided to `mjw.put_model` should specify the **maximum number of geoms** required across all variants. Geom slots that are unused in a particular variant can be disabled (e.g., `contype=0`, `conaffinity=0`, `dataid=-1`), but they should still be present as part of the body in the base model.

```xml
<mujoco>
  <asset>
    <mesh name="mA" vertex="0 0 0 1 0 0 0 1 0 0 0 1"/>
    <mesh name="mB" vertex="0 0 0 2 0 0 0 2 0 0 0 2"/>
    <mesh name="mC" vertex="0 0 0 3 0 0 0 3 0 0 0 3"/>
  </asset>
  <worldbody>
    <body name="obj" pos="0 0 1">
      <freejoint/>
      <geom name="obj_0" type="mesh" mesh="mA"/>
      <geom name="obj_1" size=".001" contype="0" conaffinity="0" mass="0"/>
    </body>
  </worldbody>
</mujoco>
```

```python
nworld = 6

# base spec: body with 2 geom slots (max across variants), all mesh assets
spec = mujoco.MjSpec()
for name, scale in [("mA", 1), ("mB", 2), ("mC", 3)]:
  mesh = spec.add_mesh()
  mesh.name = name
  mesh.uservert = [0, 0, 0, scale, 0, 0, 0, scale, 0, 0, 0, scale]

body = spec.worldbody.add_body()
body.name = "obj"
body.pos = [0, 0, 1]
body.add_freejoint()

g0 = body.add_geom()
g0.name = "obj_0"
g0.type = mujoco.mjtGeom.mjGEOM_MESH
g0.meshname = "mA"

# null geom slot: disabled collision, no mesh
g1 = body.add_geom()
g1.name = "obj_1"
g1.size = [0.001, 0, 0]
g1.contype = 0
g1.conaffinity = 0
g1.mass = 0

# variant A: 1 geom (mesh mA), g1 stays null
mjm_a = spec.compile()

# variant B: 2 geoms (mesh mB + mC)
g0.meshname = "mB"
g1.type = mujoco.mjtGeom.mjGEOM_MESH
g1.meshname = "mC"
g1.contype = 1
g1.conaffinity = 1
mjm_b = spec.compile()

# restore base and compile
g0.meshname = "mA"
g1.type = mujoco.mjtGeom.mjGEOM_SPHERE
g1.contype = 0
g1.conaffinity = 0
mjm = spec.compile()

m = mjw.put_model(mjm)
d = mjw.make_data(mjm, nworld=nworld)

# worlds 0-2: variant A (1 active geom), worlds 3-5: variant B (2 active geoms)
variants = [mjm_a, mjm_b]
assignment = [0, 0, 0, 1, 1, 1]

geom0_id = mujoco.mj_name2id(mjm, mujoco.mjtObj.mjOBJ_GEOM, "obj_0")
geom1_id = mujoco.mj_name2id(mjm, mujoco.mjtObj.mjOBJ_GEOM, "obj_1")
body_id = mjm.geom_bodyid[geom0_id]

# build per-world arrays
dataid = np.tile(mjm.geom_dataid, (nworld, 1))
geom_size = np.zeros((nworld, mjm.ngeom, 3))
geom_rbound = np.zeros((nworld, mjm.ngeom))
geom_aabb = np.zeros((nworld, mjm.ngeom, 2, 3))
geom_pos = np.zeros((nworld, mjm.ngeom, 3))
body_mass = np.zeros((nworld, mjm.nbody))
body_subtreemass = np.zeros((nworld, mjm.nbody))
body_inertia = np.zeros((nworld, mjm.nbody, 3))
body_invweight0 = np.zeros((nworld, mjm.nbody, 2))
body_ipos = np.zeros((nworld, mjm.nbody, 3))
body_iquat = np.zeros((nworld, mjm.nbody, 4))

for w in range(nworld):
  ref = variants[assignment[w]]
  dataid[w] = ref.geom_dataid
  # disable unused geom slot for variant A
  if assignment[w] == 0:
    dataid[w, geom1_id] = -1
  geom_size[w] = ref.geom_size
  geom_rbound[w] = ref.geom_rbound
  geom_aabb[w] = ref.geom_aabb.reshape(mjm.ngeom, 2, 3)
  geom_pos[w] = ref.geom_pos
  body_mass[w] = ref.body_mass
  body_subtreemass[w] = ref.body_subtreemass
  body_inertia[w] = ref.body_inertia
  body_invweight0[w] = ref.body_invweight0
  body_ipos[w] = ref.body_ipos
  body_iquat[w] = ref.body_iquat

m.geom_dataid = wp.array(dataid, dtype=int)
m.geom_size = wp.array(geom_size, dtype=wp.vec3)
m.geom_rbound = wp.array(geom_rbound, dtype=float)
m.geom_aabb = wp.array(geom_aabb, dtype=wp.vec3)
m.geom_pos = wp.array(geom_pos, dtype=wp.vec3)
m.body_mass = wp.array(body_mass, dtype=float)
m.body_subtreemass = wp.array(body_subtreemass, dtype=float)
m.body_inertia = wp.array(body_inertia, dtype=wp.vec3)
m.body_invweight0 = wp.array(body_invweight0, dtype=wp.vec2)
m.body_ipos = wp.array(body_ipos, dtype=wp.vec3)
m.body_iquat = wp.array(body_iquat, dtype=wp.quat)
```

**Batched fields** — fields that must be overridden for per-world meshes:

| Field | dtype | Shape |
| --- | --- | --- |
| `geom_dataid` | `int` | `(nworld, ngeom)` |
| `geom_size` | `wp.vec3` | `(nworld, ngeom)` |
| `geom_aabb` | `wp.vec3` | `(nworld, ngeom, 2)` |
| `geom_rbound` | `float` | `(nworld, ngeom)` |
| `geom_pos` | `wp.vec3` | `(nworld, ngeom)` |
| `body_mass` | `float` | `(nworld, nbody)` |
| `body_subtreemass` | `float` | `(nworld, nbody)` |
| `body_inertia` | `wp.vec3` | `(nworld, nbody)` |
| `body_invweight0` | `wp.vec2` | `(nworld, nbody)` |
| `body_ipos` | `wp.vec3` | `(nworld, nbody)` |
| `body_iquat` | `wp.quat` | `(nworld, nbody)` |

Per-world height fields, materials, and textures can be similarly formulated.

> [!note] Per-world asset dependent field construction
> MJWarp enables per-world asset functionality but does not provide utilities for construction of dependent per-world field variants. Construction is left to the user or environment authoring frameworks.

## Batch Rendering

MJWarp provides a batch renderer for high-throughput ray tracing built on [Warp’s accelerated BVHs](https://nvidia.github.io/warp/stable/api_reference/_generated/warp.Bvh.html) for rendering worlds with multiple cameras in parallel.

Key features:

- **Mesh rendering with textures**: BVH-accelerated mesh rendering with full texture support.
- **Heightfield rendering**: Optimized rendering for heightfields.
- **Flex rendering**: Render [flex](https://mujoco.readthedocs.io/en/stable/XMLreference.html#deformable-flex) objects.
- **3D Gaussian Splatting (3DGS)**: BVH-accelerated ray tracing and alpha compositing of 3D Gaussian splats with per-world grouping and bidirectional physical occlusion.
- **Lighting and shadows**: Dynamic lighting with configurable shadows; domain randomizable: `light_active`, `light_type`, `light_castshadow`, `light_xpos`, `light_xdir`.
- **Heterogeneous multi-camera**: Multiple cameras per world and each camera can have a different resolution (`cam_resolution`), field of view (`cam_fovy`, `cam_sensorsize`, `cam_intrinsic`), and output mode (`cam_output`).
- **Domain Randomization**: Per-world [`mjw.Model`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Model "mujoco_warp.Model") fields (see above): `geom_matid`, `geom_size`, `geom_rgba`, `mat_texid`, `mat_texrepeat`, `mat_rgba`.
- **BVH-accelerated ray/rays API**: Ray casting: Accelerated [`mjw.ray`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.ray "mujoco_warp.ray"), [`mjw.rays`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.rays "mujoco_warp.rays"), and [rangefinder sensors](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-rangefinder) via [Warp’s BVHs](https://nvidia.github.io/warp/stable/api_reference/_generated/warp.Bvh.html).

### Basic Usage

Rendering or raycasting requires a [`mjw.RenderContext`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.RenderContext "mujoco_warp.RenderContext") which contains BVH structures, rendering specific fields, and output buffers.

```python
rc = mjw.create_render_context(
    mjm,
    nworld=1,
    cam_res=(256, 256),           # Override camera resolution (or per-camera list)
    render_rgb=True,              # Enable RGB output (or per-camera list)
    render_depth=True,            # Enable depth output (or per-camera list)
    use_textures=True,            # Apply material textures
    use_shadows=False,            # Enable shadow casting (slower)
    enabled_geom_groups=[0, 1],   # Only render geoms in groups 0 and 1
    cam_active=[True, False],     # Selectively enable/disable cameras
    flex_render_smooth=True,      # Smooth shading for soft bodies
    splat_position=pos,           # Optional (nsplat, 3) 3DGS centers
    splat_rotation=rot,           # Optional (nsplat, 4) 3DGS quaternions (w, x, y, z)
    splat_scale=scale,            # Optional (nsplat, 3) 3DGS standard deviations
    splat_rgba=rgba,              # Optional (nsplat, 4) 3DGS RGB color and opacity
    splat_adr=adr,                # Optional (ngroup+1,) group offsets for per-world splats
    splat_group_id=group_id,      # Optional (nworld,) splat group index per world
)
```

Each [`mjw.RenderContext`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.RenderContext "mujoco_warp.RenderContext") parameter can be applied globally or per camera. Additionally, values for [`mjw.RenderContext`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.RenderContext "mujoco_warp.RenderContext") parameters can be parsed from XML:

```xml
<camera name="front_camera" pos="3 0 2" xyaxes="0 1 0 -0.6 0 0.8" resolution="64 64" output="rgb depth"/>
```

or set via [mjSpec](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjspec) for camera customization.

To render, first call [`mjw.refit_bvh`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.refit_bvh "mujoco_warp.refit_bvh") to update the BVH trees, followed by [`mjw.render`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.render "mujoco_warp.render") to write to output buffers.

```python
mjw.refit_bvh(m, d, rc)
mjw.render(m, d, rc)
```

The output buffers contain stacked pixels for all cameras with shape `(nworld, npixel)` and RGB data is packed into one `uint32` variable. `RenderContext.rgb_adr` and `RenderContext.depth_adr` provide per-camera indexing. For convenience, [`mjw.get_rgb`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.get_rgb "mujoco_warp.get_rgb") and [`mjw.get_depth`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.get_depth "mujoco_warp.get_depth") return processed and reshaped RGB and depth data for a given camera batched for all worlds.

```python
nworld = 1
cam_index = 0
resolution = rc.cam_res.numpy()[cam_index]
rgb_data = wp.zeros((nworld, resolution[1], resolution[0]), dtype=wp.vec3)
mjw.get_rgb(rc, rgb_data=rgb_data, cam_id=cam_index)
```

A complete example can be found in the MJWarp tutorial [\[notebook\]](https://github.com/google-deepmind/mujoco_warp/blob/main/notebooks/tutorial.ipynb) [\[open in colab\]](https://colab.research.google.com/github/google-deepmind/mujoco_warp/blob/main/notebooks/tutorial.ipynb).

### Benchmarks

Rendering can be benchmarked using:

```shell
mjwarp-testspeed benchmarks/primitives.xml --function=render
```

For benchmark results across a variety of scenes, see the [released benchmarks](https://github.com/google-deepmind/mujoco_warp/pull/1113).

### 3D Gaussian Splatting (3DGS)

MJWarp supports rendering 3D Gaussian Splatting (3DGS) scenes composited with simulated physical MuJoCo objects. Splats are raytraced via a dedicated SAH-constructed BVH (`build_splat_bvh`) and evaluated using a single-hit planar slice approximation along each ray.

#### Physical Occlusion

Splats are raytraced and alpha-composited *prior* to solid MuJoCo geometry intersection. If a camera ray hits a physical body (such as a mesh, primitive, or flex), splats located behind the hit distance (`dist`) are occluded by the physical object, while splats in front of the hit distance are blended over the physical object’s surface color.

#### Loading PLY Files

Standard binary little-endian 3DGS `.ply` files can be loaded using the helper in `contrib/render.py` or prepared manually as NumPy arrays:

- `splat_position`: Splat centers in world coordinates `(nsplat, 3)` (`float32`).
- `splat_rotation`: Splat unit quaternions in MuJoCo convention `(w, x, y, z)` `(nsplat, 4)` (`float32`).
- `splat_scale`: Splat standard deviations in each local axis `(nsplat, 3)` (`float32`), exponentiated from log-scale PLY properties.
- `splat_rgba`: Diffuse RGB color (converted from degree-0 spherical harmonics `f_dc_0..2`) and sigmoid-activated opacity `(nsplat, 4)` (`float32`).

```python
import mujoco_warp as mjw
import numpy as np

# Example defining a single splat
splat_pos = np.array([[0.0, 0.0, 0.5]], dtype=np.float32)
splat_rot = np.array([[1.0, 0.0, 0.0, 0.0]], dtype=np.float32)  # w, x, y, z
splat_scale = np.array([[0.1, 0.1, 0.1]], dtype=np.float32)
splat_rgba = np.array([[1.0, 0.2, 0.2, 0.9]], dtype=np.float32)

rc = mjw.create_render_context(
    mjm,
    nworld=1,
    render_rgb=True,
    splat_position=splat_pos,
    splat_rotation=splat_rot,
    splat_scale=splat_scale,
    splat_rgba=splat_rgba,
)
```

#### Per-World Splat Groups

Similar to per-world meshes, MJWarp supports heterogeneous per-world 3DGS scenes. Multiple splat scenes can be concatenated into single attribute arrays with group offsets specified by `splat_adr` `(ngroup + 1,)` and assigned to each world via `splat_group_id` `(nworld,)`.

```python
# Group 0 has 100 splats (indices 0..99), Group 1 has 250 splats (indices 100..349)
splat_adr = np.array([0, 100, 350], dtype=np.int32)
# Assign Group 0 to World 0 and Group 1 to World 1
splat_group_id = np.array([0, 1], dtype=np.int32)
```

#### Dynamic Splat Refitting

If splat positions, rotations, or scales change dynamically during simulation (e.g., splats attached to moving rigid bodies), call [`mjw.refit_splat_bvh`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.refit_splat_bvh "mujoco_warp.refit_splat_bvh") before rendering:

```python
# Update splat positions on device
wp.copy(rc.splat_position, updated_positions)
mjw.refit_splat_bvh(rc)
mjw.render(m, d, rc)
```

#### Performance & Raycasting Thresholds

- **BVH Response Cutoff**: Splat bounding boxes are sized to contain density responses down to `SPLAT_MIN_RESPONSE = 0.01`.
- **Bounded Compositing**: Raycasting accumulates up to the first `_MAX_SPLAT_HITS = 32` BVH intersections per ray ordered by depth.
- **Early Termination**: Compositing stops early once remaining ray transmittance drops below `0.005` or individual splat alpha is below 8-bit quantization (`1 / 255`).

#### CLI Previewer & Camera Orbits

The command-line tool `mjwarp-render` supports rendering 3DGS PLY scenes and generating camera orbit animations:

```shell
# Render single frame with 3DGS PLY
mjwarp-render scene.xml --splat=my_scene.ply --width=512 --height=512

# Render a 128-frame circular camera orbit video around a target
mjwarp-render scene.xml --splat=my_scene.ply --orbit --orbit_center="0,0,1" --orbit_radius=4.0 --output_video=orbit.gif
```

### Notes

- **Meshes**: Rendering computation scales with mesh complexity, specifically the number of vertices and faces. A primitive is expected to have better performance (i.e., higher throughput) compared to a similar-sized [mesh](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-mesh) or [heightfield](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-hfield).
- **Scaling**: Rendering scales linearly with resolution (total pixel count) and camera count.

## Frequently Asked Questions

### Learning frameworks

**Does MJWarp work with JAX?**

Yes. MJWarp is interoperable with [JAX](https://jax.readthedocs.io/). Please see the [Warp Interoperability](https://nvidia.github.io/warp/stable/user_guide/interoperability/jax.html) documentation for details.

Additionally, [MJX](https://mujoco.readthedocs.io/en/stable/mjx.html#mjx) provides a JAX API for a subset of MJWarp’s [API](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html). The implementation is specified with `impl='warp'`.

**Does MJWarp work with PyTorch?**

Yes. MJWarp is interoperable with [PyTorch](https://pytorch.org/). Please see the [Warp Interoperability](https://nvidia.github.io/warp/stable/user_guide/interoperability/pytorch.html) documentation for details.

**How to train policies with MJWarp physics?**

For examples that train policies with MJWarp physics, please see:

- [Isaac Lab](https://github.com/isaac-sim/IsaacLab): Train via [Newton API](https://github.com/newton-physics/newton).
- [mjlab](https://github.com/mujocolab/mjlab): Train directly with MJWarp using PyTorch.
- [MuJoCo Playground](https://github.com/google-deepmind/mujoco_playground): Train via [MJX API](https://mujoco.readthedocs.io/en/stable/mjx.html#mjx).

### Features

**Is MJWarp differentiable?**

No. MJWarp is not currently differentiable via Warp’s [automatic differentiation](https://nvidia.github.io/warp/stable/user_guide/differentiability.html) functionality. Updates from the team related to enabling automatic differentiation for MJWarp are tracked in this [GitHub issue](https://github.com/google-deepmind/mujoco_warp/issues/500).

**Does MJWarp work with multiple GPUs?**

Yes. Warp’s `wp.ScopedDevice` enables multi-GPU computation

```python
# create a graph for each device
graph = {}
for device in wp.get_cuda_devices():
  with wp.ScopedDevice(device):
    m = mjw.put_model(mjm)
    d = mjw.make_data(mjm)
    with wp.ScopedCapture(device) as capture:
      mjw.step(m, d)
    graph[device] = capture.graph

# launch a graph on each device
for device in wp.get_cuda_devices():
  wp.capture_launch(graph[device])
```

Please see the [Warp documentation](https://nvidia.github.io/warp/stable/user_guide/execution_and_performance/concurrency.html) for details and [mjlab distributed training](https://mujocolab.github.io/mjlab/main/source/training/distributed_training.html) for a reinforcement learning example.

**Is MJWarp on GPU deterministic?**

No. There may be ordering or *small* numerical differences between results computed by different executions of the same code. This is characteristic of non-deterministic atomic operations on GPU. Set device to CPU with `wp.set_device("cpu")` for deterministic results.

Developments for deterministic results on GPU are tracked in this [GitHub issue](https://github.com/google-deepmind/mujoco_warp/issues/562).

**How are orientations represented?**

Orientations are represented as unit quaternions and follow [MuJoCo’s conventions](https://mujoco.readthedocs.io/en/stable/programming/simulation.html#silayout): `w, x, y, z` or `scalar, vector`.

> [!note] wp.quat
> MJWarp utilizes Warp’s [built-in type](https://nvidia.github.io/warp/stable/api_reference/_generated/warp.quat.html) `wp.quat`. Importantly however, MJWarp does not utilize Warp’s `x, y, z, w` quaternion convention or operations and instead implements quaternion routines that follow MuJoCo’s conventions. Please see [math.py](https://github.com/google-deepmind/mujoco_warp/blob/main/mujoco_warp/_src/math.py) for the implementations.

**Does MJWarp have a named access API / bind?**

No. Updates for this feature are tracked in this [GitHub issue](https://github.com/google-deepmind/mujoco_warp/issues/884).

**Why are contacts reported when there are no collisions?**

1 contact will be reported for each unique geom pair that contributes to any collision sensor, even if this geom pair is not in collision. Unlike MuJoCo or MJX where [collision sensors](https://mujoco.readthedocs.io/en/stable/XMLreference.html#collision-sensors) make separate calls to collision routines while computing sensor data, MJWarp computes and stores the data for these sensors in contacts while running its main collision pipeline.

[Contact sensors](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-contact) will report the correct information for contacts affecting the physics.

**Why do some arrays have different shapes compared to mjModel or mjData?**

By default for batched simulation, many [`mjw.Data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Data "mujoco_warp.Data") fields having a leading batch dimension of size `Data.nworld`. Some [`mjw.Model`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Model "mujoco_warp.Model") fields having a leading batch dimension with size `1`, indicating that this.

Additionally, certain fields including `Model.M`, `Data.efc.J`, and `Data.efc.D` are padded to enable fast loading on GPU.

**Why are numerical results from MJWarp and MuJoCo different?**

MJWarp utilizes single precision [float32](https://nvidia.github.io/warp/stable/api_reference/_generated/warp.float32.html) in contrast to MuJoCo’s default double precision (float64) representation for [mjtNum](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtnum). Solver settings, including iterations, collision detection, and small friction values may be sensitive to differences in floating point representation.

If you encounter unexpected results, including NaNs, please open a GitHub issue.

**How to fix simulation runtime warnings?**

Warnings are provided when memory requirements exceed existing allocations during simulation:

- /: The maximum number of contacts / constraints has been exceeded. Increase the value of the setting by updating the relevant argument to [`mjw.make_data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.make_data "mujoco_warp.make_data") or [`mjw.put_data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.put_data "mujoco_warp.put_data").
- `mjw.Option.ccd_iterations`: The convex collision detection algorithm has exceeded the maximum number of iterations. Increase the value of this setting in the XML / [mjSpec](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjspec) / [mjModel](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjmodel). Importantly, this change must be made to the [mjModel](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjmodel) instance that is provided to [`mjw.put_model`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.put_model "mujoco_warp.put_model") and [`mjw.make_data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.make_data "mujoco_warp.make_data") / [`mjw.put_data`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.put_data "mujoco_warp.put_data").
- `mjw.Option.contact_sensor_maxmatch`: The maximum number of contact matches for a [contact sensor](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-contact) ’s matching criteria has been exceeded. Increase the value of this MJWarp-only setting `m.opt.contact_sensor_maxmatch`. Alternatively, refactor the contact sensor matching criteria, for example if the 2 geoms of interest are known, specify `geom1` and `geom2`.
- `height field collision overflow`: The number of potential contacts generated by a height field exceeds [mjMAXCONPAIR](https://mujoco.readthedocs.io/en/stable/APIreference/APIglobals.html#glnumericengine) and some contacts are ignored. To resolve this warning, reduce the height field resolution or reduce the size of the geom interacting with the height field.

For programmatic inspection of these overflow conditions, check [`Data.overflow`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Data.overflow "mujoco_warp.Data.overflow") and [`mjw.OverflowType`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.OverflowType "mujoco_warp.OverflowType"). To suppress stdout warning prints during high-throughput runs, set [`Option.warn_overflow`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Option.warn_overflow "mujoco_warp.Option.warn_overflow") to `False`. See for details.

### Compilation

**How can compilation time be improved?**

Limit the number of unique colliders that require the general convex collision pipeline. These colliders are listed as `CONVEX` in `MJ_COLLISION_TABLE` in [collision\_driver.py](https://github.com/google-deepmind/mujoco_warp/blob/e357e88b6b47166d325b564c805d9ecbae659a64/mujoco_warp/_src/collision_driver.py#L45) (and marked as `CCD` in the ).

**Why are the physics not working as expected after upgrading MJWarp?**

The Warp cache may be incompatible with the current code and should be cleared as part of the debugging process. This can be accomplished by deleting the directory `~/.cache/warp` or via Python

```python
import warp as wp
wp.clear_kernel_cache()
```

**Is it possible to compile MJWarp ahead of time instead of at runtime?**

Yes. Please see Warp’s [Ahead-of-Time Compilation Workflows](https://nvidia.github.io/warp/stable/user_guide/programming_model/code_generation.html#ahead-of-time-compilation-workflows) documentation for details.

## Differences from MuJoCo

This section notes differences between MJWarp and MuJoCo.

### Warmstart

If warmstarts are not [disabled](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-warmstart), the MJWarp solver warmstart always initializes the acceleration with `qacc_warmstart`. In contrast, MuJoCo performs a comparison between `qacc_smooth` and `qacc_warmstart` to determine which one is utilized for the initialization.

### Inertia matrix factorization

MJWarp performs a per-tree factorization of the inertia matrix that is stored in `qLD` where the size of the tree determines if Warp’s `U'U` Cholesky factorization [wp.tile\_cholesky](https://nvidia.github.io/warp/stable/language_reference/_generated/warp.tile_cholesky.html), MuJoCo’s sparse reverse-mode `L'DL` routine, or a simple diagonal inverse routine is employed.

### Options

[`mjw.Option`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Option "mujoco_warp.Option") fields correspond to their [mjOption](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjoption) counterparts with the following exceptions:

- [impratio](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-impratio) is stored as its inverse square root `impratio_invsqrt`.
- The constraint solver setting [tolerance](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-tolerance) is clamped to a minimum value of `1e-6`.
- Contact [override](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-override) parameters [o\_margin](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-o-margin), [o\_solref](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-o-solref), [o\_solimp](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-o-solimp), and [o\_friction](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-o-friction) are not available.

[disableflags](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag) has the following differences:

- [mjDSBL\_MIDPHASE](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtdisablebit) is not available.
- [mjDSBL\_AUTORESET](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtdisablebit) is not available.
- [mjDSBL\_NATIVECCD](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtdisablebit) changes the default box-box collider from CCD to a primitive collider.

[enableflags](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag) has the following differences:

- [mjENBL\_OVERRIDE](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtenablebit) is not available.
- [mjENBL\_FWDINV](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtenablebit) is not available.

Additional MJWarp-only options are available:

- `broadphase`: type of broadphase algorithm ([`mjw.BroadphaseType`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.BroadphaseType "mujoco_warp.BroadphaseType"))
- `broadphase_filter`: type of filtering utilized by broadphase ([`mjw.BroadphaseFilter`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.BroadphaseFilter "mujoco_warp.BroadphaseFilter"))
- `graph_conditional`: use CUDA graph conditional
- `run_collision_detection`: use collision detection routine
- `contact_sensor_maxmatch`: maximum number of contacts for contact sensor matching criteria
- `warn_overflow`: warn if simulation overflow is encountered

> [!note] Fluid model
> Modifying fluid model parameters: `density`, `viscosity`, or `wind` may require updating `Model.has_fluid`.

> [!note] Graph capture
> A new may be necessary after modifying an [`mjw.Option`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Option "mujoco_warp.Option") field in order for the updated setting to take effect.

### SDF plugins

SDF collisions support plugins. The following example for [plugin/sdf/bowl.xml](https://github.com/google-deepmind/mujoco/blob/main/model/plugin/sdf/bowl.xml) illustrates how to implement the SDF plugin implementation in [bowl.cc](https://github.com/google-deepmind/mujoco/blob/main/plugin/sdf/bowl.cc):

```python
import mujoco_warp as mjw
import warp as wp

# distance function
@wp.func
def bowl(p: wp.vec3, attr: wp.vec3) -> float:
  """Signed distance function for a bowl shape.

  attr[0] = height
  attr[1] = radius
  attr[2] = thickness
  """
  height = attr[0]
  radius = attr[1]
  thick = attr[2]
  width = wp.sqrt(radius * radius - height * height)

  # q = (norm_xy(p), p.z)
  q0 = wp.sqrt(p[0] * p[0] + p[1] * p[1])
  q1 = p[2]

  # qdiff = q - (width, height)
  qdiff0 = q0 - width
  qdiff1 = q1 - height

  if height * q0 < width * q1:
    dist = wp.sqrt(qdiff0 * qdiff0 + qdiff1 * qdiff1)
  else:
    q_norm = wp.sqrt(q0 * q0 + q1 * q1)
    dist = wp.abs(q_norm - radius)

  return dist - thick

# gradient of distance function
@wp.func
def bowl_sdf_grad(p: wp.vec3, attr: wp.vec3) -> wp.vec3:
  """Gradient of bowl SDF via finite differences."""
  eps = float(1e-6)
  f0 = bowl(p, attr)

  px = wp.vec3(p[0] + eps, p[1], p[2])
  py = wp.vec3(p[0], p[1] + eps, p[2])
  pz = wp.vec3(p[0], p[1], p[2] + eps)

  grad = wp.vec3(
    (bowl(px, attr) - f0) / eps,
    (bowl(py, attr) - f0) / eps,
    (bowl(pz, attr) - f0) / eps,
  )
  return grad

# register the bowl SDF plugin
@wp.func
def user_sdf(p: wp.vec3, attr: wp.vec3, sdf_type: int) -> float:
  return bowl(p, attr)

@wp.func
def user_sdf_grad(p: wp.vec3, attr: wp.vec3, sdf_type: int) -> wp.vec3:
  return bowl_sdf_grad(p, attr)

# override the module-level hooks
mjw._src.collision_sdf.user_sdf = user_sdf
mjw._src.collision_sdf.user_sdf_grad = user_sdf_grad
```

### Physics callbacks

MuJoCo provides global [physics callbacks](https://mujoco.readthedocs.io/en/latest/APIreference/APIglobals.html#physics-callbacks) that allow users to inject custom logic into the simulation pipeline. MJWarp supports a similar mechanism, but callbacks are Python functions set per-model on the [`mjw.Model`](https://mujoco.readthedocs.io/en/stable/mjwarp/api.html#mujoco_warp.Model "mujoco_warp.Model") instance via `Model.callback` rather than as global function pointers.

The following callbacks are available:

| Callback | Description |
| --- | --- |
| `control` | Custom control laws, writes to `Data.ctrl` |
| `passive` | Custom passive forces, writes to `Data.qfrc_passive` |
| `act_dyn` | Custom actuator dynamics, writes to `Data.act_dot` |
| `act_gain` | Custom actuator gains, writes to `Data.actuator_force` |
| `act_bias` | Custom actuator biases, writes to `Data.actuator_force` |
| `sensor` | Custom sensors, writes to `Data.sensordata`; receives an additional `stage` argument |
| `contactfilter` | Custom contact filtering, writes to `Data.contact` |

```python
import mujoco
import mujoco_warp as mjw
import warp as wp

_MJCF = r"""
<mujoco>
  <worldbody>
    <body>
      <geom size=".1"/>
      <joint name="hinge"/>
    </body>
  </worldbody>
  <actuator>
    <motor joint="hinge"/>
  </actuator>
</mujoco>
"""

@wp.kernel
def _ctrl_callback(ctrl_out: wp.array2d(dtype=float)):
  worldid = wp.tid()
  ctrl_out[worldid, 0] = 2.0

def ctrl_callback(m, d):
  wp.launch(_ctrl_callback, dim=(d.nworld,), outputs=[d.ctrl])

mjm = mujoco.MjModel.from_xml_string(_MJCF)
m = mjw.put_model(mjm)
d = mjw.make_data(mjm)

m.callback.control = ctrl_callback
mjw.step(m, d)
assert d.ctrl.numpy()[0, 0] == 2.0
```

### Pair-wise colliders

The table below provides information about the colliders and maximum number of contacts generated for different geom pairs in MJWarp. Use the toggles to see the maximum number of contacts with the options [nativeccd](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-nativeccd) and [multiccd](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-multiccd).

nativeccd

multiccd

|  | Sphere | Capsule | Ellipsoid | Cylinder | Box | Mesh | SDF |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Plane | primitive  **1** | primitive  **2** | primitive  **1** | primitive  **4** | primitive  **4** | primitive  **4** | primitive  **1** |
| HField | HFieldCCD  **4** | HFieldCCD  **4** | HFieldCCD  **4** | HFieldCCD  **4** | HFieldCCD  **4** | HFieldCCD  **4** | HFieldSDF  [sdf\_initpoints](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-sdf-initpoints) |
| Sphere | primitive  **1** | primitive  **1** | CCD  **1** | primitive  **1** | primitive  **1** | CCD  **1** | SDF  [sdf\_initpoints](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-sdf-initpoints) |
| Capsule |  | primitive  **2** | CCD  **1** | CCD  **2** | primitive  **2** | CCD  **2** | SDF  [sdf\_initpoints](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-sdf-initpoints) |
| Ellipsoid |  |  | CCD  **1** | CCD  **1** | CCD  **1** | CCD  **1** | SDF  [sdf\_initpoints](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-sdf-initpoints) |
| Cylinder |  |  |  | CCD  **4** | CCD  **4** | CCD  **4** | SDF  [sdf\_initpoints](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-sdf-initpoints) |
| Box |  |  |  |  | CCD  **4** | CCD  **4** | SDF  [sdf\_initpoints](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-sdf-initpoints) |
| Mesh |  |  |  |  |  | CCD  **4** | MeshSDF  [sdf\_initpoints](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-sdf-initpoints) |
| SDF |  |  |  |  |  |  | SDF  [sdf\_initpoints](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-sdf-initpoints) |

### Box-box collisions

By default, box-box collisions use the general-purpose convex collision pipeline (GJK/EPA). A specialized primitive collider based on [engine\_collision\_box.c](https://github.com/google-deepmind/mujoco/blob/main/src/engine/engine_collision_box.c) is available by setting the `NATIVECCD` disable flag:

```python
m.opt.disableflags |= mjw.DisableBit.NATIVECCD
```

The specialized collider generates up to 8 contact points, compared to up to 4 for the convex pipeline, and may improve contact stability for tasks involving box stacking or manipulation.

### Rendering

The batch renderer included in MJWarp serves a different purpose than MuJoCo’s renderer. The MJWarp batch renderer is a single hit raycaster optimized for high throughput and low fidelity.

It supports:

- Simple lambertian diffuse shading
- Basic point lights and directional lights
- Textures
- Shadows
- 3D Gaussian Splatting (3DGS) diffuse rendering with physical occlusion

It does not support:

- Advanced lighting effects such as global illumination
- Physically based material properties
- View-dependent spherical harmonics (higher degree SH > 0) for 3DGS
