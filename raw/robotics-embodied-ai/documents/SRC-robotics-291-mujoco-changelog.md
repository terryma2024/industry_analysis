---
source_id: "SRC-robotics-291"
title: "MuJoCo changelog"
source_type: "product_documentation"
publisher: "Google DeepMind"
source_date: "2026-07-14"
url: "https://mujoco.readthedocs.io/en/stable/changelog.html"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-07-14T03:30:40+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/a
aliases:
  - SRC-robotics-291
---
# MuJoCo changelog

## Changelog

## Version 3.10.0 (June 22, 2026)

### General

1. Added [mju\_threadpool](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-threadpool), a new function for creating a thread pool on an `mjData` instance. When a thread pool is initialized, parts of the simulation pipeline, such as collision detection and constraint solving across islands, are parallelized. The thread pool is automatically destroyed when the `mjData` is freed.
2. Added a unified [logging API](https://mujoco.readthedocs.io/en/stable/programming/simulation.html#sierror):
	- All errors, warnings, and informational messages are now routed through a single [mjfLogHandler](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjfloghandler) callback receiving a structured [mjLogMessage](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjlogmessage).
		- Users can install a custom handler via [mju\_setLogHandler](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-setloghandler), configure the default handler’s behavior (console/file output, topic filtering) via [mju\_setLogConfig](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-setlogconfig).
		- Messages can be emitted via [mju\_info](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-info) and [mju\_message](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-message).
		- New types: [mjtLogLevel](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtloglevel), [mjtLogTopic](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtlogtopic), [mjLogMessage](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjlogmessage), [mjLogConfig](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjlogconfig).
		- The legacy callbacks [mju\_user\_error](https://mujoco.readthedocs.io/en/stable/APIreference/APIglobals.html#mju-user-error) and [mju\_user\_warning](https://mujoco.readthedocs.io/en/stable/APIreference/APIglobals.html#mju-user-warning) are deprecated but remain functional.
3. Added [mjs\_numWarnings](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjs-numwarnings) and [mjs\_getWarning](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjs-getwarning) for retrieving all warnings accumulated during model compilation and attachment. Deprecated [mjs\_isWarning](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjs-iswarning) in favor of `mjs_numWarnings(s) > 0`.
4. Added the [compiler/conflict](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-conflict) attribute for controlling how conflicting global attributes are resolved during [attachment](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjs-attach). Possible values are “warning” (default: parent values take precedence, warnings emitted on conflicts), “merge” (per-field min/max/error strategy), and “error” (any conflict raises an error). See [Attribute Merging](https://mujoco.readthedocs.io/en/stable/programming/modeledit.html#meattributemerging) for details.
	> [!warning] Future breaking API changes
	> The current default conflict resolution policy “warn” (ignore the child model) is backward compatible. However, the default policy will change to “merge” in a future release.
5. Improved primal solver convergence under float32. Improvements initially proposed by **[@n3b](https://github.com/n3b)** in [issue #2313](https://github.com/google-deepmind/mujoco/issues/2313) and **[@adenzler-nvidia](https://github.com/adenzler-nvidia)** in [MJWarp](https://mujoco.readthedocs.io/en/stable/mjwarp/index.html) pull request [1374](https://github.com/google-deepmind/mujoco_warp/pull/1374).
6. The [CG solver](https://mujoco.readthedocs.io/en/stable/computation/index.html#soalgorithms) now uses the Hager-Zhang conjugate direction update instead of the Polak-Ribiere-Plus formula. This improves convergence and leads to a significant speedup under float32.
7. Added [mjs\_makeFlex](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjs-makeflex), a new C API function equivalent to the [flexcomp](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp) element for programmatically creating flex objects with auto-generated bodies, joints, and equality constraints. Exposed as `body.make_flex()` in Python.
8. Added support for loading 1D flex components from OBJ line segments
9. Significantly improved the quality of coarse convex hulls produced by the [maxhullvert](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-mesh-maxhullvert) attribute by invoking Qhull’s [Q9](http://www.qhull.org/html/qh-optq.htm#Q9) option.
	> [!note] Breaking API changes
	> - The header file `mjthread.h` was removed along with the old engine threading API.  
	> 	**Migration:** Use [mju\_threadpool](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-threadpool) to set number of worker threads for the engine.
	> - Moved island sparse matrix construction from [mj\_island](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-island) (single threaded) into [mj\_fwdConstraint](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-fwdconstraint) (multi-threaded). The island-specific matrices `iM, iLD, iefc_J` were removed from the arena and are now allocated on the stack.
	> - Following the introduction of the [diagexact](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-diagexact) flag, the `mjData` field `efc_diagApprox` was renamed to `efc_diagA`, as it can now be either the exact or approximate diagonal of the $A$ (“Delassus”) matrix.
	> - The deprecated functions `mju_{error,warning}_{i,s}` have been removed.
	> - Changed the signature of [mj\_fullM](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-fullm) from `mj_fullM(m, dst, M)` to `mj_fullM(m, d, dst)` as part of the planned deprecation of `mjData.qM` in favor of the CSR-format `mjData.M`.
	> 	**Migration:** For inertia matrix conversion, replace `mj_fullM(m, dst, d->qM)` with `mj_fullM(m, d, dst)` or `mju_sym2dense(dst, d->M, m->nv, m->M_rownnz, m->M_rowadr, m->M_colind)`.

### Bug fixes

10. Fixed a vulnerability in the System Identification toolbox where loading a trajectory or time series called `np.load` with `allow_pickle=True`, allowing arbitrary code execution from a malicious `.npz` file. Signal metadata is now serialized as JSON and loaded with `allow_pickle=False`.
11. Fixed a bug in the `mjz` [decoder](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjpdecoder) where unnormalized paths would fail to be read.
12. Fixed a bug where the mesh compiler would produce non-unit convex hull polygon normals.

## Version 3.9.0 (May 27, 2026)

### General

1. Added `mjData.efc_Y`, the whitened constraint Jacobian $Y = J M^{-1/2}$, allocated in the arena when dual solvers (PGS or NoSlip) are used or when [diagexact](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-diagexact) is enabled.
2. Added the [diagexact](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-diagexact) enable flag, which computes the exact diagonal of the constraint-space inertia matrix at the current configuration, replacing the default compile-time approximation. This improves solver quality for models with anisotropic inertias or complex kinematic coupling. See [Exact diagonal](https://mujoco.readthedocs.io/en/stable/computation/index.html#soexactdiag) for details.
3. The pseudo-random constraint visitation order in the [PGS solver](https://mujoco.readthedocs.io/en/stable/computation/index.html#soalgorithms), introduced in the previous release, now uses a fixed seed. The previous implementation seeded with `mjData.time`, which introduced subtle yet undesirable time dependence.
4. Flexes are now allowed to sleep, with the exception of completely passive (constraint-free) flexes.
5. Added compiler timing diagnostics via the new [mjtCTimer](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtctimer) enum and the [mjs\_getTimer](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjs-gettimer) C API. After [mj\_compile](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-compile), per-category timings (total, assets, mesh loading, convex hull, normals, inertia, BVH, octree, textures) are available via `mjs_getTimer(spec)`. The [compile](https://mujoco.readthedocs.io/en/stable/programming/samples.html#sacompile) sample prints a detailed timing breakdown when run without an output file.
6. Added [mjtBool](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtbool) to represent boolean variables, replacing [mjtByte](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtbyte) across all boolean fields in [mjModel](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjmodel), [mjData](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjdata), and public C API function signatures.

> [!note] Breaking API changes
> 7. The semantics of the contact `margin` and `gap` parameters have been redesigned for conceptual clarity and consistency with [Newton](https://github.com/newton-physics/newton). See the new [margin and gap](https://mujoco.readthedocs.io/en/stable/computation/index.html#comargingap) documentation section for details.
> 	Previously, `margin` controlled the *detection threshold* (contacts exist when `dist < margin`) and `gap` was subtracted from it to produce the *force threshold* (forces generated when `dist < margin - gap`). This was unintuitive: users expected `margin` to mean geometric inflation and `gap` to mean a spatial gap.
> 	Under the new semantics, `margin` is the geometric inflation of the geom surface and `gap` is an additional detection buffer beyond the inflated surface:
> 	- **Detection**: contacts are created when `dist < margin + gap`.
> 		- **Force generation**: constraint forces are applied when `dist < margin`.
> 		- **Inactive contacts**: contacts with `margin < dist ≤ margin + gap` are included in `mjData.contact` but generate no force (`efc_address = -1`). This is useful for [adhesion](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-adhesion) actuators and custom callbacks.
> 	With the default values `margin = 0`, `gap = 0`, the behavior is unchanged.
> 	 [![_images/margin_gap_light.svg](https://mujoco.readthedocs.io/en/stable/_images/margin_gap_light.svg)](https://mujoco.readthedocs.io/en/stable/_images/margin_gap_light.svg)[![_images/margin_gap_dark.svg](https://mujoco.readthedocs.io/en/stable/_images/margin_gap_dark.svg)](https://mujoco.readthedocs.io/en/stable/_images/margin_gap_dark.svg)
> 	**Migration:** Models that use the default `gap="0"` (the vast majority) require no changes. For models with `gap > 0`, apply the following transformation to preserve identical behavior:
> 	```
> 	margin_new = margin_old - gap_old
> 	gap_new    = gap_old
> 	```
> 	For example, a geom with the old attributes `margin="0.1" gap="0.1"` should be changed to `margin="0" gap="0.1"`.
> 	Negative `margin` values are now permitted (corresponding to `gap > margin` under the old semantics). The constraint `margin + gap >= 0` should be maintained to ensure valid collision detection.
> 8. The [mjfCollision](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjfcollision) functions now populate the [mjPreContact](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjprecontact) struct instead of the [mjContact](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjcontact) struct. The [mjPreContact](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjprecontact) only contains the necessary fields needed for the narrowphase collision detection.
> 9. The header file `mjtnum.h` was renamed to `mjtype.h <https://github.com/google-deepmind/mujoco/blob/main/include/mujoco/mjtype.h>` and now includes all enum type definitions.
> 10. The [tactile](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-tactile) sensor now reports raw depth instead of an estimated pressure.
> 11. MJX: Removed the deprecated `nconmax` argument from `mjx.make_data` and `mjx.put_data` in favor of `naconmax`.
> 12. Maybe-breaking: Added [mjassert.h](https://github.com/google-deepmind/mujoco/blob/main/include/mujoco/mjassert.h), a new header containing compile-time assertions that verify the sizes of MuJoCo’s public types for ABI stability. This is a first step towards replacing `int` with strongly-typed enums in the public API. If these assertions fail on your compiler or platform, please report the issue on GitHub.

## Version 3.8.1 (May 11, 2026)

### General

1. Added island support for the [PGS solver](https://mujoco.readthedocs.io/en/stable/computation/index.html#soalgorithms).
2. The [PGS solver](https://mujoco.readthedocs.io/en/stable/computation/index.html#soalgorithms) now iterates over constraints in pseudo-random order, improving performance by ~20%.
3. Added support for [elastic2d](https://mujoco.readthedocs.io/en/stable/XMLreference.html#flex-elasticity-elastic2d) for trilinear and quadratic flex [dofs](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp-dof).
4. [Midpoint integration](https://mujoco.readthedocs.io/en/stable/computation/index.html#gemidpoint) is now restricted to the `implicitfast` [integrator](https://mujoco.readthedocs.io/en/stable/computation/index.html#geintegrators) and is disabled when fluid forces are active (nonzero [density](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-density) or [viscosity](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-viscosity)). Midpoint integration treats external forces as zero-order-hold constants, which causes energy gain in the presence of contacts and in fluid media.
5. Added [mjs\_getOriginSpec](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjs-getoriginspec), returning the spec that originally defined an element, prior to attachment. This is in contrast to [mjs\_getSpec](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjs-getspec) which returns the spec currently owning the element. If the element is not the result of an attach operation, the functions are identical.
6. Added [mju\_sym2dense](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-sym2dense), converting a lower-triangular, implicitly symmetric CSR matrix to a dense symmetric matrix. The inertia matrix `mjData.M` is an example of such a matrix.

> [!warning] Future breaking API changes
> 7. The introduction of [mju\_sym2dense](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-sym2dense) is a step towards the removal of the legacy-format `mjData.qM` in favor of the CSR-format `mjData.M`. This removal will involve a future breaking change to [mj\_fullM](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-fullm) (which currently accepts a `qM` -like matrix as an argument). To prevent a future breakage, replace `mj_fullM(m, dst, d->qM)` with  
> 	`mju_sym2dense(dst, d->M, m->nv, m->M_rownnz, m->M_rowadr, m->M_colind)`.

### Bug fixes

8. Fixed default for multiccd in [mjcPhysics](https://mujoco.readthedocs.io/en/stable/OpenUSD/mjcPhysics.html).

### Python

9. Added `MjSpec.encode` method, wrapping [mj\_encode](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-encode).
10. Added `mujoco.MjVfs` Python binding to interact with the Virtual File System directly from Python. See [Virtual File System](https://mujoco.readthedocs.io/en/stable/python.html#pyvfs) for usage details.
	> [!warning] Warning
	> The previous way of passing assets via a dictionary mapping asset names to bytes is **deprecated** and will be removed in an upcoming release. You cannot specify both the `assets` dictionary and the `vfs` argument at the same time. `MjVfs` should be used as a drop-in replacement.

## Version 3.8.0 (April 24, 2026)

### General

1. Added support for Python 3.14.
2. Added [multi-cell support](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp-cellcount) for trilinear and quadratic flexes. Note that the implicit integrator uses a dense solver for the flex degrees of freedom, which can be slow for multi-cell flexes.
3. Refactored `strain` flex [equality constraints](https://mujoco.readthedocs.io/en/stable/XMLreference.html#flexcomp-edge-equality) to be instantiated per cell instead of per flex object, reducing the number of degrees of freedom per constraint row. The equality can be associated with a specific cell with the new attribute [cell](https://mujoco.readthedocs.io/en/stable/XMLreference.html#equality-flexstrain-cell)
4. Added new [mj\_maxContact](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-maxcontact) function to get the maximum number of possible contacts returned by colliding two geoms.
5. Added `mj_containsBufferVFS` and `mj_containsFileVFS` to check for existence of buffers and files in VFS.

> [!note] Breaking API changes
> 6. The [multiccd](https://mujoco.readthedocs.io/en/stable/computation/index.html#comulticcd) option (multiple contacts returned from the convex collision detection pipeline) is now enabled by default. The new implementation (as opposed to the legacy pipeline) has little performance overhead and improves stability.
> 	**Migration:** Disable [multiccd](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-multiccd) to recover the previous behavior.

### Documentation

7. Added [documentation](https://mujoco.readthedocs.io/en/stable/programming/extension.html#exdecoder) for [mjpDecoder](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjpdecoder) plugins.

### Bug fixes

8. Asset paths in attached child specs are now resolved relative to the model file directory of the child spec, rather than the parent spec. This prevents the origin of the parent spec to affect the resolution of asset paths in the child spec.

## Version 3.7.0 (April 14, 2026)

### General

1. Added the [dcmotor](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-dcmotor) actuator for modeling DC motors. Supports optional electrical dynamics (inductance), cogging torque, thermal resistance variation, and LuGre friction. See the [technical note](https://mujoco.readthedocs.io/en/stable/_static/dcmotor.pdf) for more details.
2. Actuators with joint or tendon transmissions can now contribute [damping](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-damping) and [armature](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-armature) to their transmission target. These are applied during the passive force and inertia computations, respectively, and are scaled by gear <sup>2</sup> (“reflected” damping/inertia).
![](https://www.youtube.com/watch?v=aKa3ZlEF9_Y)
3. Stiffness in [joints](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint-stiffness) and [tendons](https://mujoco.readthedocs.io/en/stable/XMLreference.html#tendon-spatial-stiffness) and damping in [joints](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint-damping) and [tendons](https://mujoco.readthedocs.io/en/stable/XMLreference.html#tendon-spatial-damping) now support nonlinear polynomial [force profiles](https://mujoco.readthedocs.io/en/stable/computation/index.html#gepolynomial). New `mjModel` arrays (`jnt_stiffnesspoly`, `tendon_stiffnesspoly`, `dof_dampingpoly`, `tendon_dampingpoly`) hold higher-order coefficients. The existing scalar arrays (`jnt_stiffness`, `dof_damping`, etc.) continue to hold the linear coefficient and are unchanged. The polynomial order is defined by the new constant [mjNPOLY](https://mujoco.readthedocs.io/en/stable/APIreference/APIglobals.html#glnumericsizes). A future breaking C-API change may unify the linear and higher-order coefficients into a single array.
4. Added [midpoint integration](https://mujoco.readthedocs.io/en/stable/computation/index.html#gemidpoint) for standalone free bodies in `implicit` and `implicitfast` [integrators](https://mujoco.readthedocs.io/en/stable/computation/index.html#geintegrators). This applies the implicit midpoint rule to the rotational dynamics of free bodies with no children, conserving kinetic energy to machine precision in the absence of external torques. The [invdiscrete](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-invdiscrete) flag now also disables midpoint integration, providing an opt-out mechanism.
5. Added the centripetal/Coriolis acceleration term $\dot{J}v$ to the constraint solver bias for [connect](https://mujoco.readthedocs.io/en/stable/XMLreference.html#equality-connect) and [weld](https://mujoco.readthedocs.io/en/stable/XMLreference.html#equality-weld) equality constaints. This significantly improves the stability of constrained mechanisms like four-bar linkages. See [Dual problem](https://mujoco.readthedocs.io/en/stable/computation/index.html#sodual) for details.
6. Introduced [mjpEncoder](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjpencoder), the counterpart to [mjpDecoder](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjpdecoder) for encoding of [mjSpec](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjspec) and [mjModel](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjmodel) into [mjResource](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjresource).
7. Added [mj\_encode](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-encode), [mjp\_registerEncoder](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjp-registerencoder), [mjp\_defaultEncoder](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjp-defaultencoder), and [mjp\_findEncoder](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjp-findencoder).

> [!note] Breaking API changes
> 8. The `mjs` layer fields `stiffness` and `damping` in [mjsJoint](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjsjoint) and [mjsTendon](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjstendon) have been widened from `mjtNum` scalars to `mjtNum[mjNPOLY+1]` arrays. The first element is the linear coefficient (previously the scalar), and subsequent elements are the higher-order [polynomial](https://mujoco.readthedocs.io/en/stable/computation/index.html#gepolynomial) coefficients.
> 	**Migration:** Replace assignments like `joint.stiffness = val` with `joint.stiffness[0] = val`.
> 9. `.obj` and `.stl` decoders are now included as source when building MuJoCo with CMake. This fixes the behaviour from the previous release where it required downstream code to load these plugins explicitly.
> 10. The `vertcollide` field in [mjsFlex](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjsflex) has been removed. It is no longer required since [MuJoCo Warp](https://mujoco.readthedocs.io/en/stable/mjwarp/index.html) supports native flex collisions.
> 11. [mjPLUGIN\_LIB\_INIT](https://mujoco.readthedocs.io/en/stable/APIreference/APIglobals.html#mjplugin-lib-init) macro now requires a name argument to avoid initialization function name collisions. When building with MSVC, we now use the C runtime initialization section to initialize plugins instead of `DllMain`. See [plugin registration](https://mujoco.readthedocs.io/en/stable/programming/extension.html#exregistration) for more details.
> 12. The [mjtWarning](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtwarning) enum value `mjWARN_VGEOMFULL` is removed. Exhaustion of visual geoms is now handled internally by the [mjvScene](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjvscene).
> 13. URDF parsing no longer hardcodes [strippath](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-strippath) to “true”. The setting is now respected and the default is “false”. Setting this is attribute is now the responsibility of the user.
> 	**Migration:** Set [strippath](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-strippath) to “true” in MJCF or programmatically using
> 	```python
> 	spec = mujoco.MjSpec.from_file("path/to/model.urdf")
> 	spec.compiler.strippath = True
> 	```

### Bug fixes

14. The compiler now correctly accounts for negative scaling when loading user specified mesh data.

## Version 3.6.0 (March 10, 2026)

### General

> [!note] Breaking API changes
> 1. The tendon Jacobian `ten_J` is now always sparse. The fields `ten_J_rownnz`, `ten_J_rowadr`, and `ten_J_colind` have been moved from [mjData](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjdata) to [mjModel](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjmodel) and are no longer computed at run time by `mj_tendon` but at compile time.

2. Added [mjs\_getCompiler](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjs-getcompiler) C API function and a `compiler` read-only property to all Python spec element types. This allows querying the compiler settings (e.g., `meshdir`) from any element, with the correct originating spec’s compiler preserved after attachment.
3. Added a new `strain` [equality constraint](https://mujoco.readthedocs.io/en/stable/XMLreference.html#flexcomp-edge-equality) type for trilinear and quadratic [dofs](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp-dof).
4. Flexes now support collisions with SDF geoms.
5. Improved memory requirements for `ten_J` and `ten_J_colind` by reducing the upper bound for the number of non-zeros `nJten`.
6. Improved memory requirements for `actuator_moment` and `moment_colind` by reducing the upper bound for the number of non-zeros `nJmom`.

### MJX

7. Add batch rendering support for MJX-Warp. See the [MJX-Warp batch rendering](https://mujoco.readthedocs.io/en/stable/mjx.html#mjxwarpbatchrendering) section for details.

## Version 3.5.0 (February 12, 2026)

### Significant new features

1. [MuJoCo Warp](https://mujoco.readthedocs.io/en/stable/mjwarp/index.html) is now officially released.
2. Added a new **System Identification** toolbox (Python), see [README](https://github.com/google-deepmind/mujoco/blob/main/python/mujoco/sysid/README.md) for details.  
	A Colab notebook demonstrating the toolbox is available here: [![sysid_colab](https://colab.research.google.com/assets/colab-badge.png)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/python/mujoco/sysid/sysid.ipynb)  
	Contribution by **[@kevinzakka](https://github.com/kevinzakka)**, **[@aftersomemath](https://github.com/aftersomemath)**, **[@jonathanembleyriches](https://github.com/jonathanembleyriches)**, **[@qiayuanl](https://github.com/qiayuanl)**, **[@spjardim](https://github.com/spjardim)** and **[@gizemozd](https://github.com/gizemozd)**.
3. Actuators and sensors now support arbitrary delays via history buffers, and sensor values can be computed at intervals larger than the simulation timestep. Using a delay or interval introduces a new `mjData.history` variable to the [Physics state](https://mujoco.readthedocs.io/en/stable/programming/simulation.html#siphysicsstate). See [Delays](https://mujoco.readthedocs.io/en/stable/modeling.html#cdelay) for details.
[![_images/poncho.png](https://mujoco.readthedocs.io/en/stable/_images/poncho.png)](https://github.com/google-deepmind/mujoco/blob/main/model/flex/poncho.xml)
4. Added new [flexvert](https://mujoco.readthedocs.io/en/stable/XMLreference.html#equality-flexvert) equality constraints that enable cloth simulations with coarser meshes. This adds a new attribute value `vert` to flexcomp edge [equality](https://mujoco.readthedocs.io/en/stable/XMLreference.html#flexcomp-edge-equality) and the new equality type [flexvert](https://mujoco.readthedocs.io/en/stable/XMLreference.html#equality-flexvert). Uses the method described in [Chen, Kry and Vouga, 2019](https://arxiv.org/abs/1911.05204).
5. Added implicit integration support for deformable objects (flex) in `implicit` and `implicitfast` [integrators](https://mujoco.readthedocs.io/en/stable/computation/index.html#geintegration). This method extracts the flex degrees of freedom and solves them as a dense block, enabling increased stability for stiff flex objects without reducing the timestep. It is compatible with the `trilinear` and `quadratic` [dof](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp-dof) types.
[![_images/rfcamera.png](https://mujoco.readthedocs.io/en/stable/_images/rfcamera.png)](https://github.com/google-deepmind/mujoco/blob/main/test/engine/testdata/sensor/rfcamera.xml)
6. Rangefinder sensors can now be attached to a camera using the [rangefinder/camera](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-rangefinder-camera) attribute. In this case, the sensor respects the [camera/resolution](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-resolution) attribute and casts multiple rays, one for each pixel.
7. [Rangefinders](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-rangefinder) can now report various kinds of information besides ray distances, including surface normals and intersection points.

### General

> [!note] Breaking API changes
> 8. Ray-cast functions now optionally compute the surface normal at the ray intersection. This is a breaking change due to the addition of the `mjtNum normal[3]` argument. The modified functions are [mj\_ray](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-ray), [mj\_multiRay](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-multiray), [mju\_rayGeom](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-raygeom), [mj\_rayFlex](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-rayflex), [mj\_rayHfield](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-rayhfield) and [mj\_rayMesh](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-raymesh).
> 	**Migration:** In C/C++, pass `NULL` to the `normal` argument. In Python, in all functions except [mj\_multiRay](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-multiray), it defaults to `None`, so no action is required.
> 9. `mju_rayFlex` has been renamed to [mj\_rayFlex](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-rayflex) for consistency with other functions that take `mjModel*` and `mjData*` arguments.
> 10. The `mjModel.cam_orthographic` field has been renamed to `cam_projection`, with the semantic of a new enum type [mjtProjection](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtprojection). This will allow for more projection types in the future like fisheye cameras. Relatedly, the `camera/orthographic` MJCF attribute for cameras has been renamed to [camera/projection](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-projection) and now accepts the values `orthographic` and `perspective`.
> 	**Migration:** Replace `orthographic = "false/true"` with `projection="perspective/orthographic"`, respectively.
> 11. Removed `getdir` from the `mjpResourceProvider` struct. All Resource Providers now use the same shared implementation.
> 12. When combining the `margin` or `gap` [parameters](https://mujoco.readthedocs.io/en/stable/modeling.html#ccontact) of two geoms to obtain the parameters of a contact, the respective values are now **summed** rather than taking the maximum. This allows geom margins to be a proper “inflation” of the geom.

13. Camera frustum visualization is now triggered by setting [resolution](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-resolution) to values larger than 1. Relatedly, frustum visualization also works for [orthographic](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-projection) cameras. See [rangefinder](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-rangefinder) for details.
14. Cameras now have an [output](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-output) attribute, parsed into the `mjModel.cam_output` bitfield. Unused by the renderer, it serves as a convenient location to store a camera’s supported output types.
15. Added [mj\_mountVFS](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-mountvfs) and [mj\_unmountVFS](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-unmountvfs) functions for mounting a custom VFS provider. Mounting allows providers to be used to open/read/close resources dynamically at arbitrary paths.
16. The optimization whereby sequential [collision sensors](https://mujoco.readthedocs.io/en/stable/XMLreference.html#collision-sensors) with identical attributes shared computation has been removed. This results in a (likely minor) performance regression for models which exploited this optimization. To recover the performance, use the [fromto](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-fromto) and compute the other values manually. If `from = fromto[0:3]` and `to = fromto[3:6]` then `distance = norm(to-from)` and `normal = normalize(to-from)`.
17. [OpenUSD](https://mujoco.readthedocs.io/en/stable/OpenUSD/index.html):
	- Parsing has been moved out of experimental into a mjpDecoder plugin. (documentation pending)
		- OpenUSD can now be built with the [third\_party\_deps/openusd](https://github.com/google-deepmind/mujoco/tree/main/cmake/third_party_deps/openusd) CMake utility project.
		- `USD_DIR` is no longer used by the MuJoCo CMake project, instead use `pxr_DIR` if you have a pre-built USD library.
		- Users no longer have to set `PXR_PLUGINPATH_NAME` environment variable, MuJoCo should load USD plugins automatically.
18. Non-breaking ABI changes:
	- The type of the `sig` (signature) argument of [mj\_stateSize](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-statesize) and related functions has been changed from `unsigned int` to `int`. Before this change, invalid negative arguments passed to this function would result in a silent implicit cast; now, negativity will trigger an error.
		- Added a [depth](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtrndflag) rendering flag.
		- Allocation sizes in [mjModel](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjmodel) now use 64-bit rather than 32-bit integers to accommodate larger scenes.

### MJX

19. Added `actuator_length`, `cdof` and `cdof_dof` fields to `mjx.Data`.
20. Add `graph_mode` argument to `put_model` to support multiple Warp graph capture modes.

### Documentation

21. General improvements to the [Programming/Simulation](https://mujoco.readthedocs.io/en/stable/programming/simulation.html#simulation) chapter. Notably, the main discussion of [state](https://mujoco.readthedocs.io/en/stable/programming/simulation.html#sistatecontrol) has been moved there, and the section on [mjModel changes](https://mujoco.readthedocs.io/en/stable/programming/simulation.html#sichange) has been expanded.
22. The usability of the [MJCF schema](https://mujoco.readthedocs.io/en/stable/XMLreference.html#cschema) is improved with a collapsible dropdown menu with links to elements and attributes.
23. MuJoCo version numbering is now based on Semantic Versioning, see [VERSIONING.md](https://github.com/google-deepmind/mujoco/blob/main/VERSIONING.md).

### Bug fixes

24. Fixed a bug in [implicit integrator](https://mujoco.readthedocs.io/en/stable/computation/index.html#geintegrators) derivatives where actuator velocity derivatives were incorrectly computed when the force was clamped by [forcerange](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-forcerange).
25. Fixed a bug in [implicit integrator](https://mujoco.readthedocs.io/en/stable/computation/index.html#geintegrators) derivatives where actuator velocity derivatives did not account for the [actearly](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-actearly) flag.
26. Multi-threaded mesh processing, enabled by the [usethread](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-usethread) compiler flag (on by default), was in fact disabled by the flag. Fixing this bug speeds up compilation of mesh-heavy models by (up to) the number of available cores.
27. The `vertid` argument of [mj\_rayFlex](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-rayflex) and [mju\_raySkin](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-rayskin) was marked as nullable but was not; it is now nullable.
28. Fixed [gravcomp](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-gravcomp) being ignored for bodies with no joints nested inside jointed parent bodies ([issue #3066](https://github.com/google-deepmind/mujoco/issues/3066), reported by **[@Alex108306](https://github.com/Alex108306)**).

## Version 3.4.0 (December 5, 2025)

### General

![](https://www.youtube.com/watch?v=aKa3ZlEF9_Y)
1. Introduced a major new feature: [sleeping islands](https://mujoco.readthedocs.io/en/stable/computation/index.html#sleeping). Preliminary release for early testing, see documentation for details.
2. Added “quadratic” option to [flexcomp/dof](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp-dof). This type of fast [deformable](https://mujoco.readthedocs.io/en/stable/modeling.html#cdeformable) flex object is similar to the “trilinear” option, but it includes curved deformations.
3. Raise an error if there are name collisions also during parsing.
4. Increase Windows stack size to 16MB to enable models with deep nested body hierarchies.
5. Added a new pipeline component function [mj\_fwdKinematics](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-fwdkinematics) that combines all kinematics-like sub-components. Relatedly, added a clarifying table at the top of the [Simulation Pipeline](https://mujoco.readthedocs.io/en/stable/computation/index.html#pipeline) chapter.
6. Added a new [mj\_extractState](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-extractstate) function that allows a subset of a state that was previously returned by [mj\_getState](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-getstate) to be extracted without having to be written back into `mjData` first.
7. Added a new [mj\_copyState](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-copystate) function that copies state components from one `mjData` to another.
8. Tendon paths can now be queried from Python via `MjsTendon.path`, the returned object is iterable and indexing it will give the `MjsWrap` at the given index in the path.
9. `MjsWrap` now exposes:
	- `type -> mujoco.mjtWrap`
		- `target -> MjsSite|MjsJoint|MjsGeom|None`
		- `sidesite -> MjsSite|None`
		- `coef -> real`
		- `divisor -> real`
10. Non-breaking ABI changes:
	- [mjtSize](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtsize) is now defined as `int64_t` rather than `uint64_t` to avoid future type-promotion bugs.
		- [mj\_sizeModel](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-sizemodel) now returns an [mjtSize](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtsize) rather than an `int`.

### MJX

11. `warp-lang` optional dependency is updated to 1.10.0. `pmap` now works with MuJoCo Warp from MJX.

> [!note] Breaking ABI changes
> - `mjx.Model.tex_data` is now a numpy ndarray instead of a jax.Array, to avoid vmapping over this potentially large array. This may break certain use-cases with Madrona MJX, but we are no longer supporting this codepath. We will be migrating users to a Warp-based batch renderer.

### Bug fixes

12. Fixed a bug in the box-box distance computation. Reported by **[@nvtw](https://github.com/nvtw)**.

## Version 3.3.7 (October 13, 2025)

### General

> [!note] Breaking API changes
> 1. The mjSpec C API fields [meshdir](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-meshdir) and [texturedir](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-texturedir) have been moved to [compiler.meshdir](https://github.com/google-deepmind/mujoco/blob/0baac589993220095cf09e153f194f35ca0f0738/include/mujoco/mjspec.h#L154) and [compiler.texturedir](https://github.com/google-deepmind/mujoco/blob/0baac589993220095cf09e153f194f35ca0f0738/include/mujoco/mjspec.h#L155) respectively. For backwards compatibility, the old fields are still available in the Python API but will be removed in a future release.
> 	**Migration:** Replace `meshdir` and `texturedir` with `compiler.meshdir` and `compiler.texturedir`.
> 2. Remove `_full_compat` from `mjx.put_data` and `mjx.put_model`.
> 3. `nconmax` and `njmax` fields in `mjx.make_data` now default to `None` instead of -1. `nconmax` will be deprecated in favor of `naconmax` in a future release.

3. Joint decorators and spatial tendons which have limits defined and whose current value (angle or length) exceeds the limit, are recolored by using the [constraint impedance](https://mujoco.readthedocs.io/en/stable/computation/index.html#soparameters) $d$ to mix the existing color with [visual/rgba/constraint](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual-rgba-constraint). For spatial tendons, this visualization aid is active only if no [material](https://mujoco.readthedocs.io/en/stable/XMLreference.html#tendon-spatial-material) is set and [rgba](https://mujoco.readthedocs.io/en/stable/XMLreference.html#tendon-spatial-rgba) is default.
4. Added [mju\_getXMLDependencies](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-getxmldependencies) for computing a list of unique asset dependencies from an MJCF file.
5. Added the code sample `dependencies` which provides command line utility for printing the result of [mju\_getXMLDependencies](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-getxmldependencies).
6. The minimum C++ standard required to compile MuJoCo is now C++20, this has been the case within Google since 2023 but the CMake update was forgotten.

> [!note] Breaking ABI changes
> 7. The attribute `mjOption.apirate` was unused and has been removed.
> 8. MJX `nconmax` and `njmax` fields in `mjx.make_data` now default to `None` instead of -1.

### MJX

9. Fix [issue #2508](https://github.com/google-deepmind/mujoco/issues/2508), `qLD` shapes mismatched mjModel during `get_data_into`.
10. Pull in MuJoCo Warp update to `io.py`, and use `naconmax` instead of `nconmax` to set the maximum number of contacts over all environments.

### Bug fixes

11. Fix [issue #2881](https://github.com/google-deepmind/mujoco/issues/2881), fitaabb was adding an offset to the mesh and applying an incorrect frame transformation. Also, unify the meaning of fitting a geom to a mesh AABB: it now means to find the smallest geom such that its AABB contains the mesh AABB.

## Version 3.3.6 (September 15, 2025)

### General

1. Constraint island discovery and construction, previously an experimental feature, is now [documented](https://mujoco.readthedocs.io/en/stable/computation/index.html#soisland) and promoted to default; disable it with [option/flag/island](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-island). We expect islanding to be a strict improvement over the monolithic constraint solver, please let us know if you experience any issues.
2. [Contact sensor](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-contact) subtree1/subtree2 specification is now available for any body, not just direct children of the world.

> [!note] Breaking API changes
> 3. The update of `mjData.qacc_warmstart` was moved from the end of the solver call ([mj\_fwdConstraint](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-fwdconstraint)) to the end of [mj\_step](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-step), and is now updated with all other state variables. This change makes [mj\_forward](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-forward) fully idempotent.
> 	Before this change, calling [mj\_forward](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-forward) repeatedly would make the constraint solver converge, since each subsequent call would start from the previously updated `qacc_warmstart` value. Indeed, this is precisely what happened in the viewer, which calls [mj\_forward](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-forward) repeatedly in PAUSE mode.
> 	**Migration:** If your code depended on this behavior, you can recover it by updating manually after each [mj\_forward](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-forward): `qacc_warmstart ← qacc`. The behavior is available in [simulate](https://mujoco.readthedocs.io/en/stable/programming/samples.html#sasimulate) by clicking the “Pause update” toggle (off by default).
> 	Furthermore, this change has a numerical impact on the output of the [RK4](https://mujoco.readthedocs.io/en/stable/computation/index.html#geintegrators) integrator. Before this change, due to the `qacc_warmstart` update occurring after each of the four Runge-Kutta substeps, the solver convergence of RK4 was faster, at the cost of unprincipled integration. This change makes the RK4 integration principled and well-defined. Since this change to RK4 is effectively a bug fix, migration to the previous behavior is not provided.
> 4. The `mjDSBL_PASSIVE` flag for disabling passive forces was removed and replaced by [mjDSBL\_SPRING](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtdisablebit) and [mjDSBL\_DAMPER](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtdisablebit) with corresponding [mjcf](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-spring) [attributes](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-damper). Each flag disables only joint and tendon springs or dampers, respectively. When both flags are set, **all** passive forces are disabled, including gravity compensation, fluid forces, forces computed by the [mjcb\_passive](https://mujoco.readthedocs.io/en/stable/APIreference/APIglobals.html#mjcb-passive) callback, and forces computed by [plugins](https://mujoco.readthedocs.io/en/stable/programming/extension.html#explugin) when passed the [mjPLUGIN\_PASSIVE](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtplugincapabilitybit) capability flag.
> 	**Migration:** Set both flags to recover the behavior of the previous flag.

> [!note] Breaking ABI changes
> 5. Removed `mjMOUSE_SELECT` flag for [mjtMouse](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtmouse) as it is no longer in use.
> 6. The promotion of islanding to default involved removing the enable flag `mjENBL_ISLAND` and converting it to a disable flag [mjDSBL\_ISLAND](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtdisablebit).

7. Added support for shells with a curved reference configuration. See this [example](https://github.com/google-deepmind/mujoco/blob/main/model/flex/basket.xml).
8. Added experimental option for [passive](https://mujoco.readthedocs.io/en/stable/XMLreference.html#flex-contact-passive) contacts involving flexes.
9. Added support for assigning a default material to a mesh asset using the [mesh/material](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-mesh-material) attribute.

### MJX

10. Promote `ten_length` to the public MJX API. Add Warp support for `mjx.tendon`.

> [!note] Breaking API changes
> 11. `ten_length` was moved from `mjx.Data._impl.ten_length` to a public field `mjx.Data.ten_length`.

### Bug fixes

12. Fixed a latent bug where MjData objects were not serialized correctly by the Python bindings when islanding was enabled.

## Version 3.3.5 (August 8, 2025)

### General

1. Added the [insidesite](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-insidesite) sensor, for checking if an object is inside the volume of a site. It is useful for triggering events in surrounding environment logic.
2. Added the [contact](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-contact) sensor, for reporting contact information according to user-defined criteria. The purpose of the contact sensor is to report contact-related information in a fixed-size array. This is useful as input to learning-based agents and in environment logic.
3. Added the [tactile](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-tactile) sensor, for measuring the penetration depth between two objects at given points and the sliding velocities in the tangent frame. The sensor reports tactile data only when colliding with SDFs.
4. Removed the SdfLib plugin and the dependency on [SdfLib](https://github.com/UPC-ViRVIG/SdfLib). SDFs are now supported natively in mjModel.
5. Removed `oct_depth` from [mjvOption](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjvoption) (unused).
6. Added the functionality to create a builtin meshes, see [mesh/builtin](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-mesh-builtin).
7. Inertia computation in MuJoCo C is now performed by a new [pipeline](https://mujoco.readthedocs.io/en/stable/computation/index.html#pistages) function [mj\_makeM](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-makem), which combines the Composite Rigid Body algorithm in [mj\_crb](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-crb) and additional terms related to [tendon armature](https://mujoco.readthedocs.io/en/stable/XMLreference.html#tendon-spatial-armature). Code that uses [mj\_crb](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-crb) to compute the inertia should now use [mj\_makeM](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-makem) instead.

> [!note] Breaking API changes
> 8. Removed the `mjVIS_FLEXBVH` enum value, its functionality is now provided by [mjVIS\_MESHBVH](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtvisflag).

### Bug fixes

9. Fixed a bug that caused object lists in the child to have missing elements after attaching an mjSpec. This was caused by adding to the lists only the objects that belong to the tree of the requested body, but this causes to skip objects that were attached, since they belong to the tree of the parent.
10. Fixed a bug where the convex hull of a collision mesh was not being computed if the mesh could only collide via a [contact pair](https://mujoco.readthedocs.io/en/stable/XMLreference.html#contact-pair).

### Python

11. On Linux, built distribution packages (wheels) now target the `manylinux_2_28` platform tag. Previously MuJoCo wheels targeted `manylinux2014` based on CentOS 7, which reached end-of-life in June 2024.

### MJX

12. Add Warp as a backend implementation for MJX. The implementation can be specified via `mjx.put_model(m, impl='warp')` and `mjx.make_data(m, impl='warp')`. The warp implementation requires a CUDA device and `warp-lang` to be installed (`pip install mujoco-mjx[warp]`). This feature is available in “beta” and some bugs are expected.

## Version 3.3.4 (July 8, 2025)

> [!note] Breaking API changes
> 1. The functions `mjs_detachBody` and `mjs_detachDefault` have been replaced by [mjs\_delete](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjs-delete).
> 2. The Python functions `element.delete` have been replaced by `spec.delete(element)`.
> 3. In the mjSpec C API, directly setting an element’s name using [mjs\_setString](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjs-setstring) has been replaced with a new function [mjs\_setName](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjs-setname) which allows checking for naming collisions at set-time rather than compile-time, for earlier catching of errors. Relatedly, the `name` attribute has been removed from all mjs elements. Known issue: the error is not raised during parsing.
> 4. For MJX, the `mjx.Option` dataclass now has private and public fields similar to `mjx.Model` and `mjx.Data`. Some fields are no longer publicly available due to differences in the underlying implementations of this data structure.

### General

4. Added support for setting the initial camera in the viewer using [visual/global/cameraid](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual-global-cameraid).
5. Added support to only sync the state in the Python [passive viewer](https://mujoco.readthedocs.io/en/stable/python.html#pyviewerpassive) ’s `Sync` method, this is useful to improve performance. The default behavior is unchanged and copies the entire model and data.

### Bug fixes

6. Inverse dynamics were not being computed correctly when [tendon armature](https://mujoco.readthedocs.io/en/stable/XMLreference.html#tendon-spatial-armature) was present, now fixed.
7. Fix bug in `mjx.put_data` where `actuator_moment` was not being copied correctly for the C implementation.

### Documentation

8. Added missing item documentation and clarified the nature of breaking changes in the 3.3.3 changelog. See items 3 and 4 below.

## Version 3.3.3 (June 10, 2025)

### General

1. Refactored island implementation so that island data is memory-contiguous. This speeds up island processing in the solver and clears the way for the addition of the Newton and PGS solvers (currently only CG is supported).
2. Removed the shell plugin. This is now supported by [flexcomp](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp) and is active depending on the [elastic2d](https://mujoco.readthedocs.io/en/stable/XMLreference.html#flexcomp-elasticity-elastic2d) attribute (off by default).

> [!note] Breaking API changes
> 3. Replaced the [directional](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-light-directional) (boolean) field for lights with a [type](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-light-type) field (of type [mjtLightType](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtlighttype)) to allow for additional lighting types.
> 	**Migration:** Replace light/directional=”false/true” with light/type=”spot/directional”, respectively.
> 4. Added [mjtColorSpace](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtcolorspace) enum and associated [colorspace](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-texture-colorspace) attribute that allows to specify the color space of textures (either linear or [sRGB](https://en.wikipedia.org/wiki/SRGB)). Since this property is now read correctly from PNG files, textures files which use sRGB will now be rendered differently.
> 	**Migration:** Set [colorspace](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-texture-colorspace) to “linear” for all textures that should look like they did before this change.

5. Added new sub-component [mj\_makeM](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-makem) which combines the [mj\_crb](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-crb) call with additional logic to support the introduction in 3.3.1 of [tendon armature](https://mujoco.readthedocs.io/en/stable/XMLreference.html#tendon-spatial-armature). In addition to the traditional `mjData.qM`, [mj\_makeM](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-makem) also computes `mjData.M`, a CSR representation of the same matrix.
6. Added a new function [mj\_copyBack](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-copyback) to copy real-valued arrays in an mjModel to a compatible mjSpec.
7. Removed the limitation of [fusestatic](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-fusestatic) to models which contain no references. The fusestatic flag will now fuse all bodies which are not referenced and ignore bodies which are referenced.

### Simulate

8. The struct `mjv_sceneState` has been removed. This struct was used for partial synchronization of `mjModel` and `mjData` when the Python viewer is used in passive mode. This functionality is now provided by [mjv\_copyModel](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjv-copymodel) and [mjv\_copyData](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjv-copydata), which don’t copy arrays which are not required for visualization.
[![_images/procedural_terrain_generation.png](https://mujoco.readthedocs.io/en/stable/_images/procedural_terrain_generation.png)](https://mujoco.readthedocs.io/en/stable/_images/procedural_terrain_generation.png)

### Python bindings

9. Added examples of procedural terrain generation to the Model Editing tutorial: [![mjspec_colab](https://colab.research.google.com/assets/colab-badge.png)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/python/mjspec.ipynb)

### MJX

10. Added tendon armature.

## Version 3.3.2 (April 28, 2025)

### MJX

1. Added inverse dynamics.
2. Added tendon actuator force sensor.
3. Fix [issue #2606](https://github.com/google-deepmind/mujoco/issues/2606) such that `make_data` copies over `mocap_pos` and `mocap_quat` from `body_pos` and `body_quat`.

## Version 3.3.1 (Apr 9, 2025)

> [!note] Breaking API changes
> 1. The default value of the flag for toggling [internal flex contacts](https://mujoco.readthedocs.io/en/stable/XMLreference.html#flex-contact-internal) was changed from “true” to “false”. This feature has proven to be counterintuitive for users.
> 2. All of the attach functions (`mjs_attachBody`, `mjs_attachFrame`, `mjs_attachToSite`, `mjs_attachFrameToSite`) have been removed and replaced by a single function [mjs\_attach](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjs-attach).

### General

3. Added [tendon armature](https://mujoco.readthedocs.io/en/stable/XMLreference.html#tendon-spatial-armature): inertia associated with changes in tendon length.
4. Added the [compiler/saveinertial](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-saveinertial) flag, writing explicit inertial clauses for all bodies when saving to XML.
5. Added [orientation](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-composite-quat) attribute to [composite](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-composite). Moreover, allow the composite to be the direct child of a frame.
6. Added [tendon actuator force limits](https://mujoco.readthedocs.io/en/stable/XMLreference.html#tendon-spatial-actuatorfrclimited) and [tendon actuator force sensor](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-tendonactuatorfrc).

### MJX

7. Added tendon actuator force limits.

### Bug fixes

8. [mj\_jacDot](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-jacdot) was missing a term that accounts for the motion of the point with respect to which the Jacobian is computed, now fixed.
9. Fixed a bug that caused the parent frame of elements in the child worldbody to be incorrectly set when attaching an mjSpec to a frame or a site.
10. Fixed a bug that caused shadow rendering to flicker on platforms (e.g., MacOS) that do not support ARB\_clip\_control. Fixed in collaboration with **[@aftersomemath](https://github.com/aftersomemath)**.

## Version 3.3.0 (Feb 26, 2025)

### Feature promotion

![](https://www.youtube.com/watch?v=qJFbx-FR7Bc)
1. Introduced a new kind of **fast deformable body**, activated by setting [flexcomp/dof](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp-dof) to “trilinear”. This type of [deformable](https://mujoco.readthedocs.io/en/stable/modeling.html#cdeformable) flex object has the same collision geometry as a regular flex, but has far fewer degrees of freedom. Instead of 3 dofs per vertex, only the corners of the bounding box are free to move, with the positions of the interior vertices computed with trilinear interpolation of the 8 corners, for a total of 24 dofs for the entire flex object (or less, if some of the corners are pinned). This limits the types of deformation achievable by the flex, but allows for much faster simulation. For example, see the video on the right comparing [full](https://github.com/google-deepmind/mujoco/blob/main/model/flex/gripper.xml) and [trilinear](https://github.com/google-deepmind/mujoco/blob/main/model/flex/gripper_trilinear.xml) flexes for modeling deformable gripper pads.
2. The native convex collision detection pipeline introduced in 3.2.3 and enabled by the [nativeccd](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-nativeccd) flag, is now the default. See the section on [Convex Collision Detection](https://mujoco.readthedocs.io/en/stable/computation/index.html#coccd) for more details.
	**Migration:** If the new pipeline breaks your workflow, set [nativeccd](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-nativeccd) to “disable”.

### General

3. Add support for custom plots in the MuJoCo viewer by exposing a `viewport` property, a `set_figures` method, and a `clear_figures` method.
4. Separate collision and deformation meshes for [flex](https://mujoco.readthedocs.io/en/stable/XMLreference.html#deformable-flex). This enables a fixed cost for the soft body computations, while preserving the fidelity of high-resolution collisions.
5. Added [potential](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-e-potential) and [kinetic](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-e-kinetic) energy sensors.
6. Improved shadow rendering in the native renderer.
7. Moved `introspect` to `python/introspect`.

> [!note] Breaking API changes
> 8. As mentioned above, the native convex collision detection pipeline is now the default, which may break some workflows. In this case, set [nativeccd](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-nativeccd) to “disable” to restore the old behavior.
> 9. Added [mjs\_setDeepCopy](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjs-setdeepcopy) API function. When the deep copy flag is 0, attaching a model will not copy it to the parent, so the original references to the child can be used to modify the parent after attachment. The default behavior is to perform such a shallow copy. The old behavior of creating a deep copy of the child model while attaching can be restored by setting the deep copy flag to 1.
> 10. Changes to inertia inference from meshes:
> 	Previously, in order to specify that the mass lies on the surface, [geom/shellinertia](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-shellinertia) could be used for any geom type. Now this attribute is ignored if the geom is a mesh; instead, inertia inference for meshes is specified in the asset, using the [asset/mesh/inertia](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-mesh-inertia) attribute.
> 	Previously, if the volumetric inertia computation failed (for example due to a very flat mesh), the compiler would silently fall back to surface inertia computation. Now, the compiler will throw an informative error.
> 11. Removed the composite type `grid`. Users should instead use [flexcomp](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp).
> 12. Removed the `particle` composite type. It is recommended to use the more generic [replicate](https://mujoco.readthedocs.io/en/stable/XMLreference.html#replicate) instead, see for example [this model](https://github.com/google-deepmind/mujoco/blob/main/model/replicate/particle.xml).

### MJX

13. Added support for spatial tendons with internal sphere and cylinder wrapping.
14. Fix a bug with box-box collisions [issue #2356](https://github.com/google-deepmind/mujoco/issues/2356).

### Python bindings

15. Added a pedagogical colab notebook for `mujoco.rollout`, a Python module for multithreaded simulation rollouts. It is available here [![rollout_colab](https://colab.research.google.com/assets/colab-badge.png)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/python/rollout.ipynb).  
	Contribution by **[@aftersomemath](https://github.com/aftersomemath)**.

## Version 3.2.7 (Jan 14, 2025)

### Python bindings

1. [rollout](https://mujoco.readthedocs.io/en/stable/python.html#pyrollout) now features native multi-threading. If a sequence of `MjData` instances of length `nthread` is passed in, `rollout` will automatically create a thread pool and parallelize the computation. The thread pool can be reused across calls, but then the function cannot be called simultaneously from multiple threads. To run multiple threaded rollouts simultaneously, use the new class `Rollout` which encapsulates the thread pool. Contribution by **[@aftersomemath](https://github.com/aftersomemath)**.
2. Fix global namespace pollution when using `mjpython` ([issue #2265](https://github.com/google-deepmind/mujoco/issues/2265)).

### General

> [!note] Breaking API changes (minor)
> 3. The field `mjData.qLDiagSqrtInv` has been removed. This field is only required for the dual solvers. It is now computed as-needed rather than unconditionally. Relatedly, added the corresponding argument to [mj\_solveM2](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-solvem2).

4. Reduced the memory footprint of the PGS solver’s [A matrix](https://mujoco.readthedocs.io/en/stable/computation/index.html#sodual). This was the last remaining dense-memory allocation in MuJoCo, allowing for a significant reduction of the [dynamic memory allocation heuristic](https://mujoco.readthedocs.io/en/stable/modeling.html#csize).

### Bug fixes

5. Fixed a bug in the box-sphere collider, depth was incorrect for deep penetrations ([issue #2206](https://github.com/google-deepmind/mujoco/issues/2206)).
6. Fixed a bug in [mj\_mulM2](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-mulm2) and added a test.

## Version 3.2.6 (Dec 2, 2024)

### General

1. Removed rope and loop from [composite](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-composite). The user is encouraged to instead use the cable plugin or [flexcomp](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp), respectively.

### MJX

2. Added muscle actuators.

### Python bindings

3. Provide prebuilt wheels for Python 3.13.
4. Added `bind` method and removed id attribute from [mjSpec](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjspec) objects. Using ids is error prone in scenarios of repeated attachment and detachment. Python users are encouraged to use names for unique identification of model elements.
5. [rollout](https://mujoco.readthedocs.io/en/stable/python.html#pyrollout) can now accept sequences of MjModel of length `nroll`. Also removed the `nroll` argument because its value can always be inferred.

## Version 3.2.5 (Nov 4, 2024)

### Feature promotion

1. The [Model Editing](https://mujoco.readthedocs.io/en/stable/programming/modeledit.html) framework afforded by [mjSpec](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjspec), introduced in 3.2.0 as an in-development feature, is now stable and recommended for general use.
2. The native convex collision detection pipeline introduced in 3.2.3 and enabled by the [nativeccd](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-nativeccd) flag, is not yet the default but is already recommended for general use. Please try it when encountering collision-related problems and report any issues you encounter.

### General

3. The global compiler flag `exactmeshinertia` has been removed and replaced with the mesh-specific [inertia](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-mesh-inertia) attribute.
4. The not-useful `convexhull` compiler option (to disable computation of mesh convex hulls) has been removed.
5. Removed the deprecated `mju_rotVecMat`, `mju_rotVecMatT` and `mjv_makeConnector` functions.
6. Sorting now uses a faster, native sort function (fixes [issue #1638](https://github.com/google-deepmind/mujoco/issues/1638)).
7. The PBR texture layers introduced in 3.2.1 were refactored from separate sub-elements to a single [layer](https://mujoco.readthedocs.io/en/stable/XMLreference.html#material-layer) sub-element.
8. The composite types box, cylinder, and sphere have been removed. Users should instead use the equivalent types available in [flexcomp](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp).

### MJX

9. Added `apply_ft`, `jac`, and `xfrc_accumulate` as public functions.
10. Added `TOUCH` sensor.
11. Added support for `eq_active`. Fixes [issue #2173](https://github.com/google-deepmind/mujoco/issues/2173).
12. Added ray intersection with ellipsoid.

### Bug fixes

13. Fixed several bugs related to connect and weld constraints with site semantics (fixes [issue #2179](https://github.com/google-deepmind/mujoco/issues/2179), reported by **[@yinfanyi](https://github.com/yinfanyi)**). The introduction of site specification to connects and welds in 3.2.3 conditionally changed the semantics of `mjData.eq_obj1id` and `mjData.eq_obj2id`, but these changes were not properly propagated in several places leading to incorrect computations of constraint inertia, readings of affected force/torque sensors and runtime enabling/disabling of such constraints.
14. Fixed a bug in slider-crank [transmission](https://mujoco.readthedocs.io/en/stable/computation/index.html#getransmission). The bug was introduced in 3.0.0.
15. Fixed a bug in flex texture coordinates that prevented the correct allocation of textures in mjModel.

### Documentation

16. Function headers in the [API reference](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html) now link to their source definitions in GitHub.

## Version 3.2.4 (Oct 15, 2024)

### General

![](https://www.youtube.com/watch?v=e8lUuykQPGs)
1. The Newton solver no longer requires `nv*nv` memory allocation, allowing for much larger models. See e.g., [100\_humanoids.xml](https://github.com/google-deepmind/mujoco/blob/main/model/humanoid/100_humanoids.xml). Two quadratic-memory allocations still remain to be fully sparsified: `mjData.actuator_moment` and the matrices used by the PGS solver.
2. Removed the solid and membrane plugins and moved the associated computations into the engine. See [3D example model](https://github.com/google-deepmind/mujoco/blob/main/model/flex/floppy.xml) and [2D example model](https://github.com/google-deepmind/mujoco/blob/main/model/flex/trampoline.xml) for examples of flex objects that previously required these plugins.
3. Replaced the function `mjs_setActivePlugins` with [mjs\_activatePlugin](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjs-activateplugin).

### MJX

4. Added `mocap_pos` and `mocap_quat` in kinematics.
5. Added support for [spatial tendons](https://mujoco.readthedocs.io/en/stable/XMLreference.html#tendon-spatial) with pulleys and external sphere and cylinder wrapping.
6. Added sphere-cylinder and sphere-ellipsoid collision functions ([issue #2126](https://github.com/google-deepmind/mujoco/issues/2126)).
7. Fixed a bug with frictionloss constraints.
8. Added `TENDONPOS` and `TENDONVEL` sensors.
9. Fixed a bug with the computation of tangential contact forces in `_decode_pyramid`.
10. Added `JOINTINPARENT` actuator transmission type.

### Python bindings

11. Removed support for Python 3.8, now that it’s [deprecated upstream](https://devguide.python.org/versions).

### Bug fixes

12. Fixed a bug where `actuator_force` was not set in MJX ([issue #2068](https://github.com/google-deepmind/mujoco/issues/2068)).
13. Fixed bug where MJX data tendon fields were incorrect after calling `mjx.put_data`.
14. The compiler now returns an error if height fields are used with [collision sensors](https://mujoco.readthedocs.io/en/stable/XMLreference.html#collision-sensors) as they are not yet supported.

## Version 3.2.3 (Sep 16, 2024)

### General

> [!note] Breaking API changes
> 1. The runtime options `mpr_tolerance` and `mpr_iterations` were renamed to [ccd\_tolerance](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-ccd-tolerance) and [ccd\_iterations](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-ccd-iterations), both in XML and in the [mjOption](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjoption) struct. This is because the new convex collision detection pipeline (see below) does not use the MPR algorithm. The semantics of these options remain identical.
> 2. The functions `mjs_findMesh` and `mjs_findKeyframe` were replaced by `mjs_findElement`, which allows to look for any object type.
> 3. The experimental use of 2D/3D elasticity plugins with [composite](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-composite) has been removed. Users should instead use [flexcomp](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp), which provides the correct collision behavior.

4. Added the [nativeccd](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-nativeccd) flag. When this flag is enabled, general convex collision detection is handled with a new native code path, rather than [libccd](https://github.com/danfis/libccd). This feature is in early stages of testing, but users who’ve experienced issues related to collision detection are welcome to experiment with it and report any issues.
![](https://www.youtube.com/watch?v=kcM_oauk3ZA)
5. Added a new way of defining [connect](https://mujoco.readthedocs.io/en/stable/XMLreference.html#equality-connect) and [weld](https://mujoco.readthedocs.io/en/stable/XMLreference.html#equality-weld) equality constraints, using two sites. The new semantic is useful when the assumption that the constraint is satisfied in the base configuration does not hold. In this case the sites will “snap together” at the beginning of the simulation. Additionally, changing the site positions (`mjModel.site_pos`) and orientations ( `mjModel.site_quat`) at runtime will correctly modify the constraint definition. This [example model](https://github.com/google-deepmind/mujoco/blob/main/test/engine/testdata/equality_site.xml) using the new semantic is shown in the video on the right.
6. Introduced **free joint alignment**, an optimization that applies to bodies with a free joint and no child bodies (simple free-floating bodies): automatically aligning the body frame with the inertial frame. This feature can be toggled individually using the [freejoint/align](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-freejoint-align) attribute or globally using the compiler [alignfree](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-alignfree) attribute. The alignment diagonalizes the related 6x6 inertia sub-matrix, leading to both faster and more stable simulation of free bodies.
	While this optimization is a strict improvement, it changes the semantics of the joint’s degrees-of-freedom. Therefore, `qpos` and `qvel` values saved in older versions (for example, in [keyframes](https://mujoco.readthedocs.io/en/stable/XMLreference.html#keyframe)) will become invalid. The global compiler attribute currently defaults to “false” due to this potential breakage, but could be changed to “true” in a future release. Aligned free joints are recommended for all new models.
7. Added an [mjSpec](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjspec) option for creating a texture directly from a buffer.
8. [shell (surface) inertia](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-shellinertia) is now supported by all geom types.
9. When [attaching](https://mujoco.readthedocs.io/en/stable/programming/modeledit.html#meattachment) sub-models, [keyframes](https://mujoco.readthedocs.io/en/stable/XMLreference.html#keyframe) will now be correctly merged into the parent model, but only on the first attachment.
10. Added the [mjtSameFrame](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtsameframe) enum which contains the possible frame alignments of bodies and their children. These alignments are used for computation shortcuts in [mj\_kinematics](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-kinematics).
11. Added [mj\_jacDot](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-jacdot) for computing time-derivatives of kinematic Jacobians. Fixes [issue #411](https://github.com/google-deepmind/mujoco/issues/411).

### MJX

12. Added `efc_pos` to `mjx.Data` ([issue #1388](https://github.com/google-deepmind/mujoco/issues/1388)).
13. Added position-dependent sensors: `MAGNETOMETER`, `CAMPROJECTION`, `RANGEFINDER`, `JOINTPOS`, `ACTUATORPOS`, `BALLQUAT`, `FRAMEPOS`, `FRAMEXAXIS`, `FRAMEYAXIS`, `FRAMEZAXIS`, `FRAMEQUAT`, `SUBTREECOM`, `CLOCK`.
14. Added velocity-dependent sensors: `VELOCIMETER`, `GYRO`, `JOINTVEL`, `ACTUATORVEL`, `BALLANGVEL`, `FRAMELINVEL`, `FRAMEANGVEL`, `SUBTREELINVEL`, `SUBTREEANGMOM`.
15. Added acceleration/force-dependent sensors: `ACCELEROMETER`, `FORCE`, `TORQUE`, `ACTUATORFRC`, `JOINTACTFRC`, `FRAMELINACC`, `FRAMEANGACC`.
16. Changed default policy to avoid placing unused (MuJoCo-only) arrays on device.
17. Added `device` parameter to `mjx.make_data` to bring it to parity with `mjx.put_model` and `mjx.put_data`.
18. Added support for [implicitfast integration](https://mujoco.readthedocs.io/en/stable/computation/index.html#geintegration) for all cases except [fluid drag](https://mujoco.readthedocs.io/en/stable/computation/fluid.html).
19. Fixed a bug where `qLDiagInv` had the wrong size for sparse mass matrices.
20. Added support for joint and tendon [frictionloss](https://mujoco.readthedocs.io/en/stable/computation/index.html#cofriction).
21. Added support for [connect](https://mujoco.readthedocs.io/en/stable/XMLreference.html#equality-connect) equality constraints using two sites.
22. Added support for [spatial tendons](https://mujoco.readthedocs.io/en/stable/XMLreference.html#tendon-spatial) with site wrapping.

### Bug fixes

23. Fixed a performance regression introduced in 3.1.7 in mesh Bounding Volume Hierarchies ([issue #1875](https://github.com/google-deepmind/mujoco/issues/1875), contribution by **[@michael-ahn](https://github.com/michael-ahn)**).
24. Fixed a bug wherein, for models that have both muscles and stateless actuators and used one of the implicit integrators, wrong derivatives would be computed.
25. Fixed a bug in tendon wrapping around spheres. Before this fix, tendons that wrapped around spheres with an externally-placed [sidesite](https://mujoco.readthedocs.io/en/stable/XMLreference.html#spatial-geom-sidesite) could jump inside the sphere instead of wrapping around it.
26. Fixed a bug that caused meshdir and texturedir to be overwritten during model [attachment](https://mujoco.readthedocs.io/en/stable/programming/modeledit.html#meattachment), preventing model attachment for models with assets in different directories.

### Python bindings

27. Added support for engine plugins in [mjSpec](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjspec) ([issue #1903](https://github.com/google-deepmind/mujoco/issues/1903)).
28. Better error reporting for issues with the assets dictionary, when loading models.

## Version 3.2.2 (Aug 8, 2024)

### General

1. Increase texture and material limit back to 1000. 3.2.0 inadvertently reduced this limit to 100, breaking some existing models ([issue #1877](https://github.com/google-deepmind/mujoco/issues/1877)).

## Version 3.2.1 (Aug 5, 2024)

### General

1. Renamed `mjModel.tex_rgb` to `mjModel.tex_data`.
2. Added a new [autoreset](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-autoreset) flag to disable automatic reset when NaNs or infinities are detected.
3. Added sub-elements to the MJCF [material](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-material) element, to allow specification of multiple textures for rendering (e.g., `occlusion, roughness, metallic`). Note that the MuJoCo renderer doesn’t support these new features, and they are made available for use with external renderers.
4. Sorting (`mjQUICKSORT`) now calls `std::sort` when building with C++ ([issue #1638](https://github.com/google-deepmind/mujoco/issues/1638)).

### MJX

5. Added more fields to `mjx.Model` and `mjx.Data` for further compatibility with the corresponding MuJoCo structs.
6. Added support for [fixed tendons](https://mujoco.readthedocs.io/en/stable/XMLreference.html#tendon-fixed).
7. Added support for tendon length limits (`mjCNSTR_LIMIT_TENDON` in [mjtConstraint](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtconstraint)).
8. Added support for tendon equality constraints (`mjEQ_TENDON` in [mjtEq](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjteq)).
9. Added support for tendon actuator transmission (`mjTRN_TENDON` in [mjtTrn](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjttrn)).

### Python bindings

10. Added support for asset dictionary argument in `mujoco.spec.from_file`, `mujoco.spec.from_string` and `mujoco.spec.compile`.

### Bug fixes

11. Fixed a bug where implicit integrators did not take into account disabled actuators ([issue #1838](https://github.com/google-deepmind/mujoco/issues/1838)).

## Version 3.2.0 (Jul 15, 2024)

### New features

1. Introduced a major new feature: **procedural model creation and editing**, using a new top-level data-structure [mjSpec](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjspec). See the [Model Editing](https://mujoco.readthedocs.io/en/stable/programming/modeledit.html) chapter for details. Note that as of this release this feature is still in testing and subject to future breaking changes. Fixes [issue #364](https://github.com/google-deepmind/mujoco/issues/364).

### General

> [!note] Breaking API changes
> 2. Removed deprecated `mj_makeEmptyFileVFS` and `mj_findFileVFS` functions. The constants `mjMAXVFS` and `mjMAXVFSNAME` are also removed as they are no longer needed.
> 	**Migration:** Use [mj\_addBufferVFS](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-addbuffervfs) to copy a buffer into a VFS file directly.
> 3. Calls to [mj\_defaultVFS](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-defaultvfs) may allocate memory inside VFS, and the corresponding [mj\_deleteVFS](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-deletevfs) must be called to deallocate any internal allocated memory.
> 4. Deprecated `mju_rotVecMat` and `mju_rotVecMatT` in favor of [mju\_mulMatVec3](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-mulmatvec3) and [mju\_mulMatTVec3](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-mulmattvec3). These function names and argument order are more consistent with the rest of the API. The older functions have been removed from the Python bindings and will be removed from the C API in the next release.
> 5. Removed the `actuator_actdim` callback from actuator plugins. They now have the `actdim` attribute, which must be used with actuators that write state to the `act` array. This fixed a crash which happened when keyframes were used in a model with stateful actuator plugins. The PID plugin will give an error when the wrong value of actdim is provided.

6. Added [attach](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-attach) meta-element to MJCF, which allows [attaching](https://mujoco.readthedocs.io/en/stable/programming/modeledit.html#meattachment) a subtree from a different model to a body in the current model.
7. The [VFS](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#virtualfilesystem) implementation has been rewritten in C++ and is now considerably more efficient in speed and memory footprint.
![](https://www.youtube.com/watch?v=ZXBTEIDWHhs)
8. Added support for orthographic cameras. This is available for both fixed cameras and the free camera, using the `camera/orthographic` and [global/orthographic](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual-global-orthographic) attributes, respectively.
9. Added [maxhullvert](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-mesh-maxhullvert), the maximum number of vertices in a mesh’s convex hull.
10. Added [mj\_setKeyframe](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-setkeyframe) for saving the current state into a model keyframe.
11. Added support for `ball` joints in the URDF parser (“spherical” in URDF).
12. Replaced `mjUSEDOUBLE` which was previously hard-coded in [mjtnum.h](https://github.com/google-deepmind/mujoco/blob/3577e2cf8bf841475b489aefff52276a39f24d51/include/mjtnum.h) with the build-time flag `mjUSESINGLE`. If this symbol is not defined, MuJoCo will use double-precision floating point, as usual. If `mjUSESINGLE` is defined, MuJoCo will use single-precision floating point. See [mjtNum](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtnum).
	Relatedly, fixed various type errors that prevented building with single-precision.
13. Quaternions in `mjData.qpos` and `mjData.mocap_quat` are no longer normalized in-place by [mj\_kinematics](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-kinematics). Instead they are normalized when they are used. After the first step, quaternions in `mjData.qpos` will be normalized.
14. Mesh loading in the compiler, which is usually the slowest part of the loading process, is now multi-threaded.

#### MJX

15. Added support for [elliptic friction cones](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-cone).
16. Fixed a bug that resulted in less-optimal linesearch solutions for some difficult constraint settings.
17. Fixed a bug in the Newton solver that sometimes resulted in less-optimal gradients.
![](https://www.youtube.com/watch?v=P83tKA1iz2Y)

### Simulate

18. Added improved tutorial video.
19. Improved the Brownian noise generator.
20. Now displaying model load times if they are longer than 0.25 seconds.

### Python bindings

21. Fixed a memory leak when using `copy.deepcopy()` on a `mujoco.MjData` instance ([issue #1572](https://github.com/google-deepmind/mujoco/issues/1572)).

### Bug fixes

22. Fix an issue where `mj_copyData` (or `copy.copy()` in the Python bindings) was not copying contact information correctly ([issue #1710](https://github.com/google-deepmind/mujoco/issues/1710)).
23. Fix an issue with saving to XML that caused frames to be written multiple times ([issue #1802](https://github.com/google-deepmind/mujoco/issues/1802)).

## Version 3.1.6 (Jun 3, 2024)

### General

1. Added [mj\_geomDistance](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-geomdistance) for computing the shortest signed distance between two geoms and optionally a segment connecting them. Relatedly, added the 3 sensors: [distance](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-distance), [normal](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-normal), [fromto](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-fromto). See the function and sensor documentation for details. Fixes [issue #51](https://github.com/google-deepmind/mujoco/issues/51).
2. Improvements to position actuators:
	- Added [timeconst](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-position-timeconst) attribute to the [position actuator](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-position). When set to a positive value, the actuator is made stateful with filterexact dynamics.
		- Added [dampratio](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-position-dampratio) to both position and intvelocity actuators. An alternative to the kv attribute, it provides a convenient way to set actuator damping using natural units. See attribute documentation for details.

### MJX

3. Add height-field collision support. Fixes [issue #1491](https://github.com/google-deepmind/mujoco/issues/1491).
4. Add a pre-compiled field `mesh_convex` to `mjx.Model` so that mesh properties can be vmapped over. Fixes [issue #1655](https://github.com/google-deepmind/mujoco/issues/1655).
5. Fix a bug in convex mesh collisions, where erroneous edge contacts were being created even though face separating axes were found. Fixes [issue #1695](https://github.com/google-deepmind/mujoco/issues/1695).

### Bug fixes

6. Fixed a bug the could cause collisions to be missed when [fusestatic](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-fusestatic) is enabled, as is often the case for URDF imports. Fixes [issue #1069](https://github.com/google-deepmind/mujoco/issues/1069), [issue #1577](https://github.com/google-deepmind/mujoco/issues/1577).
7. Fixed a bug that was causing the visualization of SDF iterations to write outside the size of the vector storing them. Fixes [issue #1539](https://github.com/google-deepmind/mujoco/issues/1539).

## Version 3.1.5 (May 7, 2024)

### General

![](https://www.youtube.com/watch?v=5k0_wsIRAFc)
1. Added the [replicate](https://mujoco.readthedocs.io/en/stable/XMLreference.html#replicate) to MJCF, a [meta-element](https://mujoco.readthedocs.io/en/stable/XMLreference.html#meta-element) which permits to repeat a subtree with incremental translational and rotational offsets.
2. Enabled an internal cache in the MuJoCo compiler resulting in recompilation speedup. Currently, processed textures, hfields, and OBJ meshes are cached. Support for Unity environments is not yet available.
3. Added `mjModel.mesh_scale`: the scaling applied to asset vertices, as specified in the [scale](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-mesh-scale) attribute.
4. Added visual properties which are ignored by the native renderer, but can be used by external renderers:
	- [light/bulbradius](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-light-bulbradius) attribute and corresponding `mjModel.light_bulbradius` field.
		- [material/metallic](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-material-metallic) attribute and corresponding `mjModel.material_metallic` field.
		- [material/roughness](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-material-roughness) attribute and corresponding `mjModel.material_roughness` field.
5. The type of the `size` argument of [mj\_stackAllocNum](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-stackallocnum) and [mj\_stackAllocInt](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-stackallocint) was changed from `int` to `size_t`.
6. Added support for gmsh format version 2.2 surface meshes in [flexcomp](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp-file).

### MJX

> [!note] Breaking API changes
> 7. Removed deprecated `mjx.device_get_into` and `mjx.device_put` functions as they lack critical new functionality.
> 	**Migration:** Use `mjx.get_data_into` instead of `mjx.device_get_into`, and `mjx.put_data` instead of `mjx.device_put`.

8. Added cylinder plane collisions.
9. Added `efc_type` to `mjx.Data` and `dim`, `efc_address` to `mjx.Contact`.
10. Added `geom` to `mjx.Contact` and marked `geom1`, `geom2` deprecated.
11. Added `ne`, `nf`, `nl`, `nefc`, and `ncon` to `mjx.Data` to match `mujoco.MjData`.
12. Given the above added fields, removed `mjx.get_params`, `mjx.ncon`, and `mjx.count_constraints`.
13. Changed the way meshes are organized on device to speed up collision detection when a mesh is replicated for many geoms.
14. Fixed a bug where capsules might be ignored in broadphase colliision checking.
15. Added cylinder collisions using SDFs.
16. Added support for all [condim](https://mujoco.readthedocs.io/en/stable/computation/index.html#cocontact): 1, 3, 4, 6.
17. Add support functions for `id2name` and `name2id`, MJX versions of [mj\_id2name](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-id2name) and [mj\_name2id](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-name2id).
18. Added support for [gravcomp](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-gravcomp) and [actuatorgravcomp](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint-actuatorgravcomp).
19. Fixed a bug in `mjx.ray` for sometimes allowed negative distances for ray-mesh tests.
20. Added a new [differentiable physics tutorial](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/mjx/training_apg.ipynb) that demonstrates training locomotion policies with analytical gradients automatically derived from the MJX physics step. Contribution by **[@Andrew-Luo1](https://github.com/Andrew-Luo1)**.

### Bug fixes

21. Defaults of lights were not being saved, now fixed.
22. Prevent overwriting of frame names by body names when saving an XML. Bug introduced in 3.1.4.
23. Fixed bug in Python binding of [mj\_saveModel](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-savemodel): `buffer` argument was documented as optional but was actually not optional.
24. Fixed bug that prevented memory allocations larger than 2.15 GB. Fixes [issue #1606](https://github.com/google-deepmind/mujoco/issues/1606).

## Version 3.1.4 (April 10th, 2024)

### General

> [!note] Breaking API changes
> 1. Removed the ability to natively add noise to sensors. Note that the `mjModel.sensor_noise` field and [corresponding attribute](https://mujoco.readthedocs.io/en/stable/modeling.html#csensor) are kept and now function as a convenient location for the user to save standard-deviation information for their own use. This feature was removed because:
> 	- There was no mechanism to seed the random noise generator.
> 		- It was not thread-safe, even if seeding would have been provided, sampling on multiple threads would lead to non-reproducible results.
> 		- This feature was seen as overreach by the engine. Adding noise should be the user’s responsibility.
> 		- We are not aware of anyone who was actually using the feature.
> 	**Migration:** Add noise to sensor values yourself.

2. Added the [actuatorgravcomp](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint-actuatorgravcomp) joint attribute. When enabled, gravity compensation forces on the joint are treated as applied by actuators. See attribute documentation for more details. The example model [refsite.xml](https://github.com/google-deepmind/mujoco/blob/main/test/engine/testdata/actuation/refsite.xml), which demonstrates Cartesian actuation of an arm, has been updated to use this attribute.
3. Added support for gmsh format 2.2, tetrahedral mesh, as generated by e.g. [fTetwild](https://github.com/wildmeshing/fTetWild).
4. Added [mju\_euler2Quat](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-euler2quat) for converting an Euler-angle sequence to quaternion.

### MJX

5. Improved performance of SAT for convex collisions.
6. Fixed bug for sphere/capsule-convex deep penetration.
7. Fixed bug where `mjx.Data` produced by `mjx.put_data` had different treedef than `mjx.make_data`.
8. Throw an error for margin/gap for convex mesh collisions, since they are not supported.
9. Added ellipsoid plane collisions.
10. Added support for userdata.
11. Added ellipsoid-ellipsoid and ellipsoid-capsule collisions using signed distance functions (SDFs).

### Simulate

12. Fixed bug in order of enable flag strings. Before this change, using the simulate UI to toggle the [invdiscrete](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-invdiscrete) or the (now removed) `sensornoise` flags would actually toggle the other flag.

### Python bindings

![](https://www.youtube.com/watch?v=xHDS0n5DpqM)
13. Added the `mujoco.minimize` Python module for nonlinear least-squares, designed for System Identification (sysID). The sysID tutorial is work in progress, but a pedagogical colab notebook with examples, including Inverse Kinematics, is available here: [![ls_colab](https://colab.research.google.com/assets/colab-badge.png)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/python/least_squares.ipynb)  
	The video on the right shows example clips from the tutorial.

## Version 3.1.3 (March 5th, 2024)

### General

1. Added the inheritrange attribute to [position](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-position) and [intvelocity](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-intvelocity) actuators, allowing convenient setting of the actuator’s ctrlrange or actrange (respectively), according to the range of the transmission target (joint or tendon). See [position/inheritrange](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-position-inheritrange) for details.
2. Deprecated `mj_makeEmptyFileVFS` in favor of [mj\_addBufferVFS](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-addbuffervfs). [mjVFS](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjvfs) now computes checksums of its internal file buffers. [mj\_addBufferVFS](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-addbuffervfs) allocates an empty buffer with a given name in an mjVFS and copies the data buffer into it, combining and replacing the deprecated two-step process of calling `mj_makeEmptyFileVFS` followed by a direct copy into the given mjVFS internal file buffer.
3. Added [mj\_angmomMat](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-angmommat) which computes the `3 x nv` angular momentum matrix $H(q)$, providing the linear mapping from generalized velocities to subtree angular momentum $h = H \dot q$. Contribution by **[@v-r-a](https://github.com/v-r-a)**.

### MJX

4. Improved performance of getting and putting device data.
	- Use `tobytes()` for numpy array serialization, which is orders of magnitude faster than converting to tuples.
		- Avoid reallocating host `mjData` arrays when array shapes are unchanged.
		- Speed up calculation of `mjx.ncon` for models with many geoms.
		- Avoid calling `mjx.ncon` in `mjx.get_data_into` when `nc` can be derived from `mjx.Data`.
5. Fixed a bug in `mjx-viewer` that prevented it from running. Updated `mjx-viewer` to use newer `mjx.get_data_into` function call.
6. Fixed a bug in `mjx.euler` that applied incorrect damping when using dense mass matrices.
7. Fixed a bug in `mjx.solve` that was causing slow convergence when using `mjSOL_NEWTON` in [mjtSolver](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtsolver).
8. Added support for [mjOption.impratio](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjoption) to `mjx.Model`.
9. Added support for cameras in `mjx.Model` and `mjx.Data`. Fixes [issue #1422](https://github.com/google-deepmind/mujoco/issues/1422).
10. Added an implementation of broadphase using `top_k` and bounding spheres.

### Python bindings

11. Fixed incorrect data types in the bindings for the `geom`, `vert`, `elem`, and `flex` array members of the `mjContact` struct, and all array members of the `mjrContext` struct.

## Version 3.1.2 (February 05, 2024)

### General

1. Improved the [discardvisual](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-discardvisual) compiler flag, which now discards all visual-only assets. See [discardvisual](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-discardvisual) for details.
2. Removed the [timer](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjttimer) for midphase colllision detection, it is now folded in with the narrowphase timer. This is because timing the two phases separately required fine-grained timers inside the collision functions; these functions are so small and fast that the timer itself was incurring a measurable cost.
3. Added the flag [bvactive](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual-global-bvactive) to `visual/global`, allowing users to turn off visualisation of active bounding volumes (the red/green boxes in this ). For models with very high-resolution meshes, the computation required for this visualization can slow down simulation speed. Fixes [issue #1279](https://github.com/google-deepmind/mujoco/issues/1279).
	- Added color of [bounding volumes](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual-rgba-bv) and [active bounding volumes](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual-rgba-bvactive) to [visual/rgba](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual-rgba).
4. Height-field elevation data can now be specified directly in XML with the [elevation](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-hfield-elevation) attribute (and not only with PNG files). See [example model](https://github.com/google-deepmind/mujoco/blob/main/test/user/testdata/hfield_xml.xml).

### MJX

5. Added [dyntype](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-dyntype) `filterexact`.
6. Added site transmission.
7. Updated MJX colab tutorial with more stable quadruped environment.
8. Added `mjx.ray` which mirrors [mj\_ray](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-ray) for planes, spheres, capsules, boxes, and meshes.
9. Added `mjx.is_sparse` which mirrors [mj\_isSparse](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-issparse) and `mjx.full_m` which mirrors [mj\_fullM](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-fullm).
10. Added support for specifying sparse or dense mass matrices via [jacobian: \[dense, sparse, auto\], “auto”](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-jacobian).
11. Raise a not implemented error when nonzero frictionloss is present. Fixes [issue #1344](https://github.com/google-deepmind/mujoco/issues/1344).

### Python bindings

12. Improved the implementation of the [rollout](https://mujoco.readthedocs.io/en/stable/python.html#pyrollout) module. Note the changes below are breaking, dependent code will require modification.
	- Uses [mjSTATE\_FULLPHYSICS](https://mujoco.readthedocs.io/en/stable/programming/simulation.html#sifullphysics) as state spec, enabling divergence detection by inspecting time.
		- Allows user-defined control spec for any combination of [user input](https://mujoco.readthedocs.io/en/stable/programming/simulation.html#siinput) fields as controls.
		- Outputs are no longer squeezed and always have dim=3.
13. The `sync` function for the [passive viewer](https://mujoco.readthedocs.io/en/stable/python.html#pyviewerpassive) can now pick up changes to rendering flags in `user_scn`, as requested in [issue #1190](https://github.com/google-deepmind/mujoco/issues/1190).

### Bug fixes

14. Fixed a bug that prevented the use of pins with plugins if flexes are not in the worldbody. Fixes [issue #1270](https://github.com/google-deepmind/mujoco/issues/1270).
15. Fixed a bug in the [muscle model](https://mujoco.readthedocs.io/en/stable/modeling.html#cmuscle) that led to non-zero values outside the lower bound of the length range. Fixes [issue #1342](https://github.com/google-deepmind/mujoco/issues/1342).

## Version 3.1.1 (December 18, 2023)

### Bug fixes

1. Fixed a bug (introduced in 3.1.0) where box-box collisions produced no contacts if one box was deeply embedded in the other.
2. Fixed a bug in [simulate](https://mujoco.readthedocs.io/en/stable/programming/samples.html#sasimulate) where the “LOADING…” message was not showing correctly.
3. Fixed a crash in the Python [passive viewer](https://mujoco.readthedocs.io/en/stable/python.html#pyviewerpassive), when used with models containing Flex objects.
4. Fixed a bug in MJX where `site_xmat` was ignored in `get_data` and `put_data`
5. Fixed a bug in MJX where `efc_address` was sometimes incorrectly calculated in `get_data`.

## Version 3.1.0 (December 12, 2023)

### General

1. Improved convergence of Signed Distance Function (SDF) collisions by using line search and a new objective function for the optimization. This allows to decrease the number of initial points needed for finding the contacts and is more robust for very small or large geom sizes.
2. Added [frame](https://mujoco.readthedocs.io/en/stable/XMLreference.html#frame) to MJCF, a [meta-element](https://mujoco.readthedocs.io/en/stable/XMLreference.html#meta-element) which defines a pure coordinate transformation on its direct children, without requiring a [body](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body).
3. Added the kv attribute to the [position](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-position) and [intvelocity](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-intvelocity) actuators, for specifying actuator-applied damping. This can be used to implement a PD controller with 0 reference velocity. When using this attribute, it is recommended to use the implicitfast or implicit [integrators](https://mujoco.readthedocs.io/en/stable/computation/index.html#geintegration).

### Plugins

4. Allow actuator plugins to use activation variables in `mjData.act` as their internal state, rather than `mjData.plugin_state`. Actuator plugins can now specify [callbacks](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjpplugin) that compute activation variables, and they can be used with built-in [dyntype](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-plugin-dyntype) actuator dynamics.
5. Added the [pid](https://github.com/deepmind/mujoco/blob/main/plugin/actuator/README.md) actuator plugin, a configurable PID controller that implements the Integral term, which is not available with native MuJoCo actuators.

### MJX

6. Added `site_xpos` and `site_xmat` to MJX.
7. Added `put_data`, `put_model`, `get_data` to replace `device_put` and `device_get_into`, which will be deprecated. These new functions correctly translate fields that are the result of intermediate calculations such as `efc_J`.

### Bug fixes

8. Fix bug in Cartesian actuation with movable refsite, as when using body-centric Cartesian actuators on a quadruped. Before this fix such actuators could lead to non-conservation of momentum.
9. Fix bug that prevented using flex with [simulate](https://mujoco.readthedocs.io/en/stable/programming/samples.html#sasimulate).
10. Fix bug that prevented the use of elasticity plugins in combination with pinned flex vertices.
11. Release Python wheels targeting macOS 10.16 to support x86\_64 systems where `SYSTEM_VERSION_COMPAT` is set. The minimum supported version is still 11.0, but we release these wheels to fix compatibility for those users. See [issue #1213](https://github.com/google-deepmind/mujoco/issues/1213).
12. Fixed mass computation of meshes: Use the correct mesh volume instead of approximating it using the inertia box.

## Version 3.0.1 (November 15, 2023)

### General

1. Added sub-terms of total passive forces in `mjData.qfrc_passive` to [mjData](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjdata): `qfrc_{spring, damper, gravcomp, fluid}`. The sum of these vectors equals `qfrc_passive`.
![](https://www.youtube.com/watch?v=H9qG9Zf2W44)
2. Added [actuatorgroupdisable](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-actuatorgroupdisable) attribute and associated [mjOption.disableactuator](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjoption) integer bitfield, which can be used to disable sets of actuators at runtime according to their [group](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-group). Fixes [issue #1092](https://github.com/google-deepmind/mujoco/issues/1092). See [Group disable](https://mujoco.readthedocs.io/en/stable/modeling.html#cactdisable).
	- The first 6 actuator groups are toggleable in the [simulate](https://mujoco.readthedocs.io/en/stable/programming/samples.html#sasimulate) viewer. See [example model](https://github.com/google-deepmind/mujoco/blob/main/test/engine/testdata/actuation/actuator_group_disable.xml) and associated screen-capture on the right.
3. Increased `mjMAXUIITEM` (maximum number of UI elements per section in Simulate) to 200.

### MJX

4. Added support for Newton solver (`mjSOL_NEWTON` in [mjtSolver](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtsolver)). The Newton solver significantly speeds up simulation on GPU:
	| Model | CG | Newton | Speedup |
	| --- | --- | --- | --- |
	| [Humanoid](https://github.com/google-deepmind/mujoco/tree/56006355b29424658b56aedb48a4269bd4361c68/mjx/mujoco/mjx/benchmark/model/humanoid) | 640,000 | 1,020,000 | **1.6 x** |
	| [Barkour v0](https://github.com/google-deepmind/mujoco/tree/56006355b29424658b56aedb48a4269bd4361c68/mjx/mujoco/mjx/benchmark/model/barkour_v0) | 1,290,000 | 1,750,000 | **1.35 x** |
	| [Shadow Hand](https://github.com/google-deepmind/mujoco/tree/56006355b29424658b56aedb48a4269bd4361c68/mjx/mujoco/mjx/benchmark/model/shadow_hand) | 215,000 | 270,000 | **1.25 x** |
	Humanoid is the standard MuJoCo humanoid, [Google Barkour](https://blog.research.google/2023/05/barkour-benchmarking-animal-level.html) and the Shadow Hand are both available in the [MuJoCo Menagerie](https://mujoco.readthedocs.io/en/stable/models.html#menagerie).
5. Added support for joint equality constraints (`mjEQ_JOINT` in [mjtEq](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjteq)).
6. Fixed bug where mixed `jnt_limited` joints were not being constrained correctly.
7. Made `device_put` type validation more verbose (fixes [issue #1113](https://github.com/google-deepmind/mujoco/issues/1113)).
8. Removed empty EFC rows from `MJX`, for joints with no limits (fixes [issue #1117](https://github.com/google-deepmind/mujoco/issues/1117)).
9. Fixed bug in `scan.body_tree` that led to incorrect smooth dynamics for some kinematic tree layouts.

### Python bindings

10. Fix the macOS `mjpython` launcher to work with the Python interpreter from Apple Command Line Tools.
11. Fixed a crash when copying instances of `mujoco.MjData` for models that use plugins. Introduced a `model` attribute to `MjData` which is reference to the model that was used to create that `MjData` instance.

### Simulate

12. [simulate](https://mujoco.readthedocs.io/en/stable/programming/samples.html#sasimulate): correct handling of “Pause update”, “Fullscreen” and “VSync” buttons.

### Documentation

![](https://www.youtube.com/watch?v=cE3s_IfO4g4)
13. Added cell to the [tutorial colab](https://github.com/google-deepmind/mujoco#getting-started) providing an example of procedural camera control:
14. Added documentation for the [User Interface](https://mujoco.readthedocs.io/en/stable/programming/ui.html#ui) framework.
15. Fixed typos and supported fields in docs (fixes [issue #1105](https://github.com/google-deepmind/mujoco/issues/1105) and [issue #1106](https://github.com/google-deepmind/mujoco/issues/1106)).

### Bug fixes

16. Fixed bug relating to welds modified with [torquescale](https://mujoco.readthedocs.io/en/stable/XMLreference.html#equality-weld-torquescale).

## Version 3.0.0 (October 18, 2023)

### New features

1. Added simulation on GPU and TPU via the new [MuJoCo XLA (MJX)](https://mujoco.readthedocs.io/en/stable/mjx.html) (MJX) Python module. Python users can now natively run MuJoCo simulations at millions of steps per second on Google TPU or their own accelerator hardware.
	- MJX is designed to work with on-device reinforcement learning algorithms. This Colab notebook demonstrates using MJX along with reinforcement learning to train humanoid and quadruped robots to locomote: [![colab](https://colab.research.google.com/assets/colab-badge.png)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/mjx/tutorial.ipynb)
		- The MJX API is compatible with MuJoCo but is missing some features in this release. See the outline of [MJX feature parity](https://mujoco.readthedocs.io/en/stable/mjx.html#mjxfeatureparity) for more details.
![](https://www.youtube.com/watch?v=QewlEqIZi1o)
2. Added new signed distance field (SDF) collision primitive. SDFs can take any shape and are not constrained to be convex. Collision points are found by minimizing the maximum of the two colliding SDFs via gradient descent.
	- Added new SDF plugin for defining implicit geometries. The plugin must define methods computing an SDF and its gradient at query points. See the [documentation](https://mujoco.readthedocs.io/en/stable/programming/extension.html#exwriting) for more details.
![](https://www.youtube.com/watch?v=ra2bTiZHGlw)
3. Added new low-level model element called `flex`, used to define deformable objects. These [simplicial complexes](https://en.wikipedia.org/wiki/Simplicial_complex) can be of dimension 1, 2 or 3, corresponding to stretchable lines, triangles or tetrahedra. Two new MJCF elements are used to define flexes. The top-level [deformable](https://mujoco.readthedocs.io/en/stable/XMLreference.html#deformable) section contains the low-level flex definition. The [flexcomp](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp) element, similar to [composite](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-composite) is a convenience macro for creating deformables, and supports the GMSH tetrahedral file format.
	- Added [shell](https://github.com/deepmind/mujoco/blob/main/plugin/elasticity/shell.cc) passive force plugin, computing bending forces using a constant precomputed Hessian (cotangent operator).
	**Note**: This feature is still under development and subject to change. In particular, deformable object functionality is currently available both via [deformable](https://mujoco.readthedocs.io/en/stable/modeling.html#cdeformable) and [composite](https://mujoco.readthedocs.io/en/stable/modeling.html#ccomposite), and both are modifiable by the first-party [elasticity plugins](https://github.com/google-deepmind/mujoco/tree/main/plugin/elasticity). We expect some of this functionality to be unified in the future.
![](https://www.youtube.com/watch?v=Vc1tq0fFvQA)
4. Added constraint island discovery with [mj\_island](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-island). Constraint islands are disjoint sets of constraints and degrees-of-freedom that do not interact. The only solver which currently supports islands is [CG](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-solver). Island discovery can be activated using a new [enable flag](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-island). If island discovery is enabled, geoms, contacts and tendons will be colored according to the corresponding island, see video. Island discovery is currently disabled for models that have deformable objects (see previous item).
5. Added `mjThreadPool` and `mjTask` which allow for multi-threaded operations within the MuJoCo engine pipeline. If engine-internal threading is enabled, the following operations will be multi-threaded:
	- Island constraint resolution, if island discovery is [enabled](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-island) and the [CG solver](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-solver) is selected. The [22 humanoids](https://github.com/deepmind/mujoco/blob/main/model/humanoid/22_humanoids.xml) model shows a 3x speedup compared to the single threaded simulation.
		- Inertia-related computations and collision detection will happen in parallel.
	Engine-internal threading is a work in progress and currently only available in first-party code via the [testspeed](https://mujoco.readthedocs.io/en/stable/programming/samples.html#satestspeed) utility, exposed with the `npoolthread` flag.
6. Added capability to initialize [composite](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-composite) particles from OBJ files. Fixes [issue #642](https://github.com/google-deepmind/mujoco/issues/642) and [issue #674](https://github.com/google-deepmind/mujoco/issues/674).

### General

> [!note] Breaking API changes
> 7. Removed the macros `mjMARKSTACK` and `mjFREESTACK`.
> 	**Migration:** These macros have been replaced by new functions [mj\_markStack](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-markstack) and [mj\_freeStack](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-freestack). These functions manage the [mjData stack](https://mujoco.readthedocs.io/en/stable/programming/simulation.html#sistack) in a fully encapsulated way (i.e., without introducing a local variable at the call site).
> 8. Renamed `mj_stackAlloc` to [mj\_stackAllocNum](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-stackallocnum). The new function [mj\_stackAllocByte](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-stackallocbyte) allocates an arbitrary number of bytes and has an additional argument for specifying the alignment of the returned pointer.
> 	**Migration:** The functionality for allocating `mjtNum` arrays is now available via [mj\_stackAllocNum](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-stackallocnum).
> 9. Renamed the `nstack` field in [mjModel](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjmodel) and [mjData](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjdata) to `narena`. Changed `narena`, `pstack`, and `maxuse_stack` to count number of bytes rather than number of [mjtNum](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtnum) ⁠s.
> 10. Changed [mjData.solver](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjdata), the array used to collect solver diagnostic information. This array of [mjSolverStat](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjsolverstat) structs is now of length `mjNISLAND * mjNSOLVER`, interpreted as as a matrix. Each row of length `mjNSOLVER` contains separate solver statistics for each constraint island. If the solver does not use islands, only row 0 is filled.
> 	- The new constant [mjNISLAND](https://mujoco.readthedocs.io/en/stable/APIreference/APIglobals.html#glnumericsizes) was set to 20.
> 		- [mjNSOLVER](https://mujoco.readthedocs.io/en/stable/APIreference/APIglobals.html#glnumericsizes) was reduced from 1000 to 200.
> 		- Added [mjData.solver\_nisland](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjdata): the number of islands for which the solver ran.
> 		- Renamed `mjData.solver_iter` to `solver_niter`. Both this member and `mjData.solver_nnz` are now integer vectors of length `mjNISLAND`.
> 11. Removed `mjOption.collision` and the associated `option/collision` attribute.
> 	**Migration:**
> 	- For models which have `<option collision="all"/>`, delete the attribute.
> 		- For models which have `<option collision="dynamic"/>`, delete all [pair](https://mujoco.readthedocs.io/en/stable/XMLreference.html#contact-pair) elements.
> 		- For models which have `<option collision="predefined"/>`, disable all dynamic collisions (determined via contype/conaffinity) by first deleting all [contype](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-contype) and [conaffinity](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-conaffinity) attributes in the model and then setting them globally to `0` using  
> 		`<default> <geom contype="0" conaffinity="0"/> </default>`.
> 12. Removed the rope and cloth composite objects.
> 	**Migration:** Users should use the cable and shell elasticity plugins.
> 13. Added [mjData.eq\_active](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjdata) user input variable, for enabling/disabling the state of equality constraints. Renamed `mjModel.eq_active` to [mjModel.eq\_active0](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjmodel), which now has the semantic of “initial value of `mjData.eq_active` ”. Fixes [issue #876](https://github.com/google-deepmind/mujoco/issues/876).
> 	**Migration:** Replace uses of `mjModel.eq_active` with `mjData.eq_active`.
> 14. Changed the default of [autolimits](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-autolimits) from “false” to “true”. This is a minor breaking change. The potential breakage applies to models which have elements with “range” defined and “limited” not set. Such models cannot be loaded since version 2.2.2 (July 2022).

15. Added a new [dyntype](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-dyntype), `filterexact`, which updates first-order filter states with the exact formula rather than with Euler integration.
16. Added an actuator attribute, [actearly](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-actearly), which uses semi-implicit integration for actuator forces: using the next step’s actuator state to compute the current actuator forces.
17. Renamed `actuatorforcerange` and `actuatorforcelimited`, introduced in the previous version to [actuatorfrcrange](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint-actuatorfrcrange) and [actuatorfrclimited](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint-actuatorfrclimited), respectively.
18. Added the flag [eulerdamp](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-eulerdamp), which disables implicit integration of joint damping in the Euler integrator. See the [Numerical Integration](https://mujoco.readthedocs.io/en/stable/computation/index.html#geintegration) section for more details.
19. Added the flag [invdiscrete](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-invdiscrete), which enables discrete-time inverse dynamics for all [integrators](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-integrator) other than `RK4`. See the flag documentation for more details.
20. Added [ls\_iterations](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-ls-iterations) and [ls\_tolerance](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-ls-tolerance) options for adjusting linesearch stopping criteria in CG and Newton solvers. These can be useful for performance tuning.
21. Added `mesh_pos` and `mesh_quat` fields to [mjModel](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjmodel) to store the normalizing transformation applied to mesh assets. Fixes [issue #409](https://github.com/google-deepmind/mujoco/issues/409).
22. Added camera [resolution](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-resolution) attribute and [camprojection](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-camprojection) sensor. If camera resolution is set to positive values, the camera projection sensor will report the location of a target site, projected onto the camera image, in pixel coordinates.
23. Added [camera](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera) calibration attributes:
	- The new attributes are [resolution](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-resolution), [focal](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-focal), [focalpixel](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-focalpixel), [principal](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-principal), [principalpixel](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-principalpixel) and [sensorsize](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-sensorsize).
		- Visualize the calibrated frustum using the [mjVIS\_CAMERA](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtvisflag) visualization flag when these attributes are specified. See the following [example model](https://github.com/deepmind/mujoco/blob/main/test/engine/testdata/vis_visualize/frustum.xml).
		- Note that these attributes only take effect for offline rendering and do not affect interactive visualisation.
24. Implemented reversed Z rendering for better depth precision. An enum [mjtDepthMap](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtdepthmap) was added with values `mjDEPTH_ZERONEAR` and `mjDEPTH_ZEROFAR`, which can be used to set the new `readDepthMap` attribute in [mjrContext](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjrcontext) to control how the depth returned by [mjr\_readPixels](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjr-readpixels) is mapped from `znear` to `zfar`. Contribution [PR #978](https://github.com/google-deepmind/mujoco/pull/978) by [Levi Burner](https://github.com/aftersomemath).
25. Deleted the code sample `testxml`. The functionality provided by this utility is implemented in the [WriteReadCompare](https://github.com/google-deepmind/mujoco/blob/main/test/xml/xml_native_writer_test.cc) test.
26. Deleted the code sample `derivative`. Functionality provided by [mjd\_transitionFD](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjd-transitionfd).

### Python bindings

27. Fixed [issue #870](https://github.com/google-deepmind/mujoco/issues/870) where calling `update_scene` with an invalid camera name used the default camera.
28. Added `user_scn` to the [passive viewer](https://mujoco.readthedocs.io/en/stable/python.html#pyviewerpassive) handle, which allows users to add custom visualization geoms ([issue #1023](https://github.com/google-deepmind/mujoco/issues/1023)).
29. Added optional boolean keyword arguments `show_left_ui` and `show_right_ui` to the functions `viewer.launch` and `viewer.launch_passive`, which allow users to launch a viewer with UI panels hidden.

### Simulate

![](https://www.youtube.com/watch?v=YSvWn_poqWs)
30. Added **state history** mechanism to [simulate](https://mujoco.readthedocs.io/en/stable/programming/samples.html#sasimulate) and the managed [Python viewer](https://mujoco.readthedocs.io/en/stable/python.html#pyviewermanaged). State history can be viewed by scrubbing the History slider and (more precisely) with the left and right arrow keys. See screen capture:
31. The `LOADING...` label is now shown correctly. Contribution [PR #1070](https://github.com/google-deepmind/mujoco/pull/1070) by [Levi Burner](https://github.com/aftersomemath).

### Documentation

![](https://www.youtube.com/watch?v=nljr0X79vI0)
32. Added [detailed documentation](https://mujoco.readthedocs.io/en/stable/computation/fluid.html) of fluid force modeling, and an illustrative example model showing [tumbling cards](https://github.com/google-deepmind/mujoco/blob/main/model/cards/cards.xml) using the ellipsoid-based fluid model.

### Bug fixes

33. Fixed a bug that was causing [geom margin](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-margin) to be ignored during the construction of midphase collision trees.
34. Fixed a bug that was generating incorrect values in `efc_diagApprox` for weld equality constraints.

## Version 2.3.7 (July 20, 2023)

### General

1. Added primitive collider for sphere-cylinder contacts, previously this pair used the generic convex-convex collider.
2. Added [joint-actuatorforcerange](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint-actuatorfrcrange) for clamping total actuator force at joints and [sensor-jointactuatorfrc](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-jointactuatorfrc) for measuring total actuation force applied at a joint. The most important use case for joint-level actuator force clamping is to ensure that [Cartesian actuator](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-refsite) forces are realizable by individual motors at the joints. See [Force limits](https://mujoco.readthedocs.io/en/stable/modeling.html#cforcerange) for details.
3. Added an optional `content_type` attribute to hfield, texture, and mesh assets. This attribute supports a formatted [Media Type](https://www.iana.org/assignments/media-types/media-types.xhtml) (previously known as MIME type) string used to determine the type of the asset file without resorting to pulling the type from the file extension.
4. Added analytic derivatives for quaternion [subtraction](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjd-subquat) and [integration](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjd-quatintegrate) (rotation with an angular velocity). Derivatives are in the 3D tangent space.
5. Added [mjv\_connector](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjv-connector) which has identical functionality to `mjv_makeConnector`, but with more convenient “from-to” argument parametrization. `mjv_makeConnector` is now deprecated.
6. Bumped oldest supported MacOS from version 10.12 to 11. MacOS 11 is the oldest version still maintained by Apple.

### Python bindings

7. The [passive viewer](https://mujoco.readthedocs.io/en/stable/python.html#pyviewerpassive) handle now exposes `update_hfield`, `update_mesh`, and `update_texture` methods to allow users to update renderable assets. (Issues [issue #812](https://github.com/google-deepmind/mujoco/issues/812), [issue #958](https://github.com/google-deepmind/mujoco/issues/958), [issue #965](https://github.com/google-deepmind/mujoco/issues/965)).
8. Allow a custom keyboard event callback to be specified in the [passive viewer](https://mujoco.readthedocs.io/en/stable/python.html#pyviewerpassive) ([issue #766](https://github.com/google-deepmind/mujoco/issues/766)).
9. Fix GLFW crash when Python exits while the passive viewer is running ([issue #790](https://github.com/google-deepmind/mujoco/issues/790)).

### Models

10. Added simple [car](https://github.com/google-deepmind/mujoco/blob/main/model/car/car.xml) example model.

## Version 2.3.6 (June 20, 2023)

> [!note] Note
> MuJoCo 2.3.6 is the last version to officially support Python 3.7.

![](https://www.youtube.com/watch?v=ZppeDArq6AU)

### Models

1. Added [3x3x3 cube](https://github.com/google-deepmind/mujoco/blob/main/model/cube/cube_3x3x3.xml) example model. See [README](https://github.com/google-deepmind/mujoco/blob/main/model/cube/README.md) for details.

### Bug fixes

2. Fixed a bug that was causing an incorrect computation of the mesh bounding box and coordinate frame if the volume was invalid. In such case, now MuJoCo only accepts a non-watertight geometry if [shellinertia](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-shellinertia) is equal to `true`.
3. Fixed the sparse Jacobian multiplication logic that is used to compute derivatives for tendon damping and fluid force, which affects the behaviour of the [implicit and implicitfast integrators](https://mujoco.readthedocs.io/en/stable/computation/index.html#geintegration).
4. Fixes to [mj\_ray](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-ray), in line with geom visualisation conventions:
	- Planes and height-fields respect the `geom_group` and `flg_static` arguments. Before this change, rays would intersect planes and height-fields unconditionally.
		- `flg_static` now applies to all static geoms, not just those which are direct children of the world body.
![](https://www.youtube.com/watch?v=hqIMTNGaLF4)

### Simulate

![](https://www.youtube.com/watch?v=mXVPbppGk5I)
6. Added Visualization tab to simulate UI, corresponding to elements of the [visual](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual) MJCF element. After modifying values in the GUI, a saved XML will contain the new values. The modifiable members of [mjStatistic](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjstatistic) ([extent](https://mujoco.readthedocs.io/en/stable/XMLreference.html#statistic-extent), [meansize](https://mujoco.readthedocs.io/en/stable/XMLreference.html#statistic-meansize) and [center](https://mujoco.readthedocs.io/en/stable/XMLreference.html#statistic-center)) are computed by the compiler and therefore do not have defaults. In order for these attributes to appear in the saved XML, a value must be specified in the loaded XML.
[![Before / After](https://mujoco.readthedocs.io/en/stable/_images/simulate_text_width.png)](https://mujoco.readthedocs.io/en/stable/_images/simulate_text_width.png)
7. Increased text width for UI elements in the default spacing. \[before / after\]:

### General

8. Added [mj\_getState](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-getstate) and [mj\_setState](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-setstate) for getting and setting the simulation state as a concatenated vector of floating point numbers. See the [State](https://mujoco.readthedocs.io/en/stable/computation/index.html#gestate) section for details.
9. Added [mjContact.solreffriction](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjcontact), allowing different [solref](https://mujoco.readthedocs.io/en/stable/modeling.html#csolver) parameters for the normal and frictional axes of contacts when using [elliptic friction cones](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-cone). This attribute is required for elastic frictional collisions, see associated [example model](https://github.com/google-deepmind/mujoco/blob/main/test/engine/testdata/spin_recoil.xml) mimicking the spin-bounce recoil behaviour of [elastic rubber balls](https://www.youtube.com/watch?v=uFLJcRegIVQ&t=3s). This is an advanced option currently only supported by explicit [contact pairs](https://mujoco.readthedocs.io/en/stable/XMLreference.html#contact-pair), using the [solreffriction](https://mujoco.readthedocs.io/en/stable/XMLreference.html#contact-pair-solreffriction) attribute.
10. Added [mjd\_inverseFD](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjd-inversefd) for finite-differenced inverse-dynamics derivatives.
11. Added functions for operations on banded-then-dense “arrowhead” matrices. Such matrices are common when doing direct trajectory optimization. See [mju\_cholFactorBand](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-cholfactorband) documentation for details.
12. Added [mj\_multiRay](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-multiray) function for intersecting multiple rays emanating from a single point. This is significantly faster than calling [mj\_ray](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-ray) multiple times.
13. Ray-mesh collisions are now up to 10x faster, using a bounding volume hierarchy of mesh faces.
14. Increased `mjMAXUIITEM` (maximum number of UI elements per section in Simulate) to 100.
15. Added [documentation](https://mujoco.readthedocs.io/en/stable/programming/extension.html#exprovider) for resource providers.
16. Changed the formula for [mju\_sigmoid](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-sigmoid), a finite-support sigmoid $s \colon \mathbf R \rightarrow [0, 1]$. Previously, the smooth part consisted of two stitched quadratics, once continuously differentiable. It is now a single quintic, twice continuously differentiable:
	$$
	s(x) =
	\begin{cases}
	   0,                    &       & x \le 0  \\
	   6x^5 - 15x^4 + 10x^3, & 0 \lt & x \lt 1  \\
	   1,                    & 1 \le & x \qquad
	\end{cases}
	$$
17. Added optional [tausmooth](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-muscle-tausmooth) attribute to muscle actuators. When positive, the time-constant $\tau$ of muscle activation/deactivation uses [mju\_sigmoid](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-sigmoid) to transition smoothly between the two extremal values given by the [Millard et al. (2013)](https://doi.org/10.1115/1.4023390) muscle model, within a range of width tausmooth. See [Muscle actuators](https://mujoco.readthedocs.io/en/stable/modeling.html#cmuscle) for more details. Relatedly, [mju\_muscleDynamics](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-muscledynamics) now takes 3 parameters instead of 2, adding the new smoothing-width parameter.
18. Moved public C macro definitions out of mujoco.h into a new public header file called [mjmacro.h](https://github.com/google-deepmind/mujoco/blob/main/include/mujoco/mjmacro.h). The new file is included by mujoco.h so this change does not break existing user code.
19. Added instrumentation for the [Address Sanitizer (ASAN)](https://clang.llvm.org/docs/AddressSanitizer.html) and [Memory Sanitizer (MSAN)](https://clang.llvm.org/docs/MemorySanitizer.html) to detect memory bugs when allocating from the `mjData` stack and arena.
20. Removed `pstack` and `parena` from the output of `mj_printData`, since these are implementation details of the `mjData` allocators that are affected by diagnostic paddings in instrumented builds.
21. Removed the `mj_activate` and `mj_deactivate` functions. These had been kept around for compatibility with old user code from when MuJoCo was closed source, but have been no-op functions since open sourcing.

## Version 2.3.5 (April 25, 2023)

### Bug fixes

1. Fix asset loading bug that prevented OBJ and PNG files from being read from disk when [mjVFS](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjvfs) is used.
2. Fix occasional segmentation faults on macOS when mouse perturbations are applied in the Python passive viewer.

### Plugins

3. The `visualize` callback in [mjpPlugin](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjpplugin) now receives an [mjvOption](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjvoption) as an input argument.

## Version 2.3.4 (April 20, 2023)

> [!note] Note
> This version is affected by an asset loading bug that prevents OBJ and PNG files from being read from disk when `mjVFS` is used. Users are advised to skip to version 2.3.5 instead.

### General

1. Removed the “global” setting of the [compiler/coordinate](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-coordinate) attribute. This rarely-used setting complicates the compiler logic and is blocking future improvements. In order to convert older models which used this option, load and save them in MuJoCo 2.3.3 or older.
[![_images/ellipsoidinertia.gif](https://mujoco.readthedocs.io/en/stable/_images/ellipsoidinertia.gif)](https://mujoco.readthedocs.io/en/stable/_images/ellipsoidinertia.gif)
2. Added [visual-global](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual-global) flag [ellipsoidinertia](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual-global-ellipsoidinertia) to visualize equivalent body inertias with ellipsoids instead of the default boxes.
3. Added midphase and broadphase collision statistics to [mjData](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjdata).
4. Added documentation for [engine plugins](https://mujoco.readthedocs.io/en/stable/programming/extension.html#explugin).
5. Added struct information to the `introspect` module.
6. Added a new extension mechanism called [resource providers](https://mujoco.readthedocs.io/en/stable/programming/extension.html#exprovider). This extensible mechanism allows MuJoCo to read assets from data sources other than the local OS filesystem or the [Virtual file system](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#virtualfilesystem).

### Python bindings

7. Offscreen rendering on macOS is no longer restricted to the main thread. This is achieved by using the low-level Core OpenGL (CGL) API to create the OpenGL context, rather than going via GLFW which relies on Cocoa’s NSOpenGL. The resulting context is not tied to a Cocoa window, and is therefore not tied to the main thread.
8. Fixed a race condition in `viewer.launch_passive` and `viewer.launch_repl`. These functions could previously return before an internal call to `mj_forward`. This allows user code to continue and potentially modify physics state concurrently with the internal `mj_forward`, resulting in e.g. [MuJoCo stack overflow error](https://github.com/google-deepmind/mujoco/issues/783) or [segmentation fault](https://github.com/google-deepmind/mujoco/issues/790).
9. The `viewer.launch_passive` function now returns a handle which can be used to interact with the viewer. The passive viewer now also requires an explicit call to `sync` on its handle to pick up any update to the physics state. This is to avoid race conditions that can result in visual artifacts. See [documentation](https://mujoco.readthedocs.io/en/stable/python.html#pyviewerpassive) for details.
10. The `viewer.launch_repl` function has been removed since its functionality is superseded by `launch_passive`.
11. Added a small number of missing struct fields discovered through the new `introspect` metadata.

### Bug fixes

12. Fixed bug in the handling of ellipsoid-based fluid model forces in the new implicitfast integrator.
13. Removed spurious whole-arena copying in `mj_copyData`, which can considerably [slow down](https://github.com/google-deepmind/mujoco/issues/568) the copying operation.
14. Make [shellinertia](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-shellinertia) ignore `exactmeshinertia`, which is
	only used for legacy volume computations ([#759](https://github.com/google-deepmind/mujoco/issues/759)).

## Version 2.3.3 (March 20, 2023)

### General

1. Improvements to implicit integration:
	- The derivatives of the RNE algorithm are now computed using sparse math, leading to significant speed improvements for large models when using the [implicit integrator](https://mujoco.readthedocs.io/en/stable/computation/index.html#geintegration).
		- A new integrator called `implicitfast` was added. It is similar to the existing implicit integrator, but skips the derivatives of Coriolis and centripetal forces. See the [numerical integration](https://mujoco.readthedocs.io/en/stable/computation/index.html#geintegration) section for a detailed motivation and discussion. The implicitfast integrator is recommended for all new models and will become the default integrator in a future version.
	The table below shows the compute cost of the 627-DoF [humanoid100](https://github.com/google-deepmind/mujoco/blob/main/model/humanoid/humanoid100.xml) model using different integrators. “implicit (old)” uses dense RNE derivatives, “implicit (new)” is after the sparsification mentioned above. Timings were measured on a single core of an AMD 3995WX CPU.

| timing | Euler | implicitfast | implicit (new) | implicit (old) |
| --- | --- | --- | --- | --- |
| one step (ms) | 0.5 | 0.53 | 0.77 | 5.0 |
| steps/second | 2000 | 1900 | 1300 | 200 |

[![_images/midphase.gif](https://mujoco.readthedocs.io/en/stable/_images/midphase.gif)](https://mujoco.readthedocs.io/en/stable/_images/midphase.gif)
2. Added a collision mid-phase for pruning geoms in body pairs, see [documentation](https://mujoco.readthedocs.io/en/stable/computation/index.html#coselection) for more details. This is based on static AABB bounding volume hierarchy (a BVH binary tree) in the body inertial frame. The GIF on the right is cut from [this longer video](https://youtu.be/e0babIM8hBo).
3. The `mjd_transitionFD` function no longer triggers sensor calculation unless explicitly requested.
4. Corrected the spelling of the `inteval` attribute to `interval` in the [mjLROpt](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjlropt) struct.
5. Mesh texture and normal mappings are now 3-per-triangle rather than 1-per-vertex. Mesh vertices are no longer duplicated in order to circumvent this limitation as they previously were.
6. The non-zeros for the sparse constraint Jacobian matrix are now precounted and used for matrix memory allocation. For instance, the constraint Jacobian matrix from the [humanoid100](https://github.com/google-deepmind/mujoco/blob/main/model/humanoid/humanoid100.xml) model, which previously required ~500,000 `mjtNum` ’s, now only requires ~6000. Very large models can now load and run with the CG solver.
7. Modified [mju\_error](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-error) and [mju\_warning](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-warning) to be variadic functions (support for printf-like arguments). The functions `mju_error_i`, `mju_error_s`, `mju_warning_i`, and `mju_warning_s` are now deprecated.
8. Implemented a performant `mju_sqrMatTDSparse` function that doesn’t require dense memory allocation.
9. Added `mj_stackAllocInt` to get correct size for allocating ints on mjData stack. Reducing stack memory usage by 10% - 15%.

### Python bindings

10. Fixed IPython history corruption when using `viewer.launch_repl`. The `launch_repl` function now provides seamless continuation of an IPython interactive shell session, and is no longer considered experimental feature.
11. Added `viewer.launch_passive` which launches the interactive viewer in a passive, non-blocking mode. Calls to `launch_passive` return immediately, allowing user code to continue execution, with the viewer automatically reflecting any changes to the physics state. (Note that this functionality is currently in experimental/beta stage, and is not yet described in our [viewer documentation](https://mujoco.readthedocs.io/en/stable/python.html#pyviewer).)
12. Added the `mjpython` launcher for macOS, which is required for `viewer.launch_passive` to function there.
13. Removed `efc_` fields from joint indexers. Since the introduction of arena memory, these fields now have dynamic sizes that change between time steps depending on the number of active constraints, breaking strict correspondence between joints and `efc_` rows.
14. Added a number of missing fields to the bindings of `mjVisual` and `mjvPerturb` structs.

### Simulate

15. Implemented a workaround for [broken VSync](https://github.com/glfw/glfw/issues/2249) on macOS so that the frame rate is correctly capped when the Vertical Sync toggle is enabled.
[![_images/contactlabel.png](https://mujoco.readthedocs.io/en/stable/_images/contactlabel.png)](https://mujoco.readthedocs.io/en/stable/_images/contactlabel.png)
16. Added optional labels to contact visualization, indicating which two geoms are contacting (names if defined, ids otherwise). This can be useful in cluttered scenes.

## Version 2.3.2 (February 7, 2023)

### General

1. A more performant mju\_transposeSparse has been implemented that doesn’t require dense memory allocation. For a constraint Jacobian matrix from the [humanoid100.xml](https://github.com/google-deepmind/mujoco/blob/main/model/humanoid/humanoid100.xml) model, this function is 35% faster.
2. The function [mj\_name2id](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-name2id) is now implemented using a hash function instead of a linear search for better performance.
3. Geom names are now parsed from URDF. Any duplicate names are ignored. `mj_printData` output now contains contacting geom names.

### Bug fixes

4. Fixed a bug that for shellinertia equal to `true` caused the mesh orientation to be overwritten by the principal components of the shell inertia, while the vertex coordinates are rotated using the volumetric inertia. Now the volumetric inertia orientation is used also in the shell case.
5. Fixed misalignment bug in mesh-to-primitive fitting when using the bounding box fitting option fitaabb.
[![_images/meshfit.png](https://mujoco.readthedocs.io/en/stable/_images/meshfit.png)](https://mujoco.readthedocs.io/en/stable/_images/meshfit.png)
6. The `launch_repl` functionality in the Python viewer has been fixed.
7. Set `time` correctly in `mjd_transitionFD`, to support time-dependent user code.
8. Fixed sensor data dimension validation when `user` type sensors are present.
9. Fixed incorrect plugin error message when a null `nsensordata` callback is encountered during model compilation.
10. Correctly end the timer (`TM_END`) `mj_fwdConstraint` returns early.
11. Fixed an infinite loop in `mj_deleteFileVFS`.

### Simulate

12. Increased precision of simulate sensor plot y-axis by 1 digit ([#719](https://github.com/google-deepmind/mujoco/issues/719)).
13. Body labels are now drawn at the body frame rather than inertial frame, unless inertia is being visualised.

### Plugins

14. The `reset` callback now receives instance-specific `plugin_state` and `plugin_data` as arguments, rather than the entire `mjData`. Since `reset` is called inside `mj_resetData` before any physics forwarding call has been made, it is an error to read anything from `mjData` at this stage.
15. The `capabilities` field in `mjpPlugin` is renamed `capabilityflags` to more clearly indicate that this is a bit field.

## Version 2.3.1 (December 6, 2022)

### Python bindings

1. The `simulate` GUI is now available through the `mujoco` Python package as `mujoco.viewer`. See [documentation](https://mujoco.readthedocs.io/en/stable/python.html#pyviewer) for details. (Contribution by [Levi Burner](https://github.com/aftersomemath).)
2. The `Renderer` class from the MuJoCo tutorial Colab is now available directly in the native Python bindings.

### General

3. The tendon springlength attribute can now take two values. Given two non-decreasing values, `springlength` specifies a [deadband](https://en.wikipedia.org/wiki/Deadband) range for spring stiffness. If the tendon length is between the two values, the force is 0. If length is outside this range, the force behaves like a regular spring, with the spring resting length corresponding to the nearest springlength value. This can be used to create tendons whose limits are enforced by springs rather than constraints, which are cheaper and easier to analyse. See [tendon\_springlength.xml](https://github.com/google-deepmind/mujoco/blob/main/test/engine/testdata/tendon_springlength.xml) example model.
	> [!note] Attention
	> This is a minor breaking API change. `mjModel.tendon_lengthspring` now has size `ntendon x 2` rather than `ntendon x 1`.
	![](https://www.youtube.com/watch?v=-PJ6afdETUg)
4. Removed the requirement that stateless actuators come before stateful actuators.
5. Added [mju\_fill](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-fill), [mju\_symmetrize](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-symmetrize) and [mju\_eye](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-eye) utility functions.
6. Added gravcomp attribute to [body](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body), implementing gravity compensation and buoyancy. See [balloons.xml](https://github.com/google-deepmind/mujoco/blob/main/model/balloons/balloons.xml) example model.
7. Renamed the `cable` plugin library to `elasticity`.
8. Added actdim attribute to [general actuators](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general). Values greater than 1 are only allowed for dyntype user, as native activation dynamics are all scalar. Added example test implementing 2nd-order activation dynamics to [engine\_forward\_test.cc](https://github.com/google-deepmind/mujoco/blob/main/test/engine/engine_forward_test.cc).
9. Improved particle [composite](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-composite) type, which now permits a user-specified geometry and multiple joints. See the two new examples: [particle\_free.xml](https://github.com/google-deepmind/mujoco/blob/main/model/composite/particle_free.xml) and [particle\_free2d.xml](https://github.com/google-deepmind/mujoco/blob/main/model/composite/particle_free2d.xml).
10. Performance improvements for non-AVX configurations:
	- 14% faster `mj_solveLD` using [restrict](https://en.wikipedia.org/wiki/Restrict). See [engine\_core\_smooth\_benchmark\_test](https://github.com/google-deepmind/mujoco/blob/main/test/benchmark/engine_core_smooth_benchmark_test.cc).
		- 50% faster `mju_dotSparse` using manual loop unroll. See [engine\_util\_sparse\_benchmark\_test](https://github.com/google-deepmind/mujoco/blob/main/test/benchmark/engine_util_sparse_benchmark_test.cc).
11. Added new solid passive force plugin:
	![](https://www.youtube.com/watch?v=AGcTGHbbze4)
	- This is new force field compatible with the [composite](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-composite) particles.
		- Generates a tetrahedral mesh having particles with mass concentrated at vertices.
		- Uses a piecewise-constant strain model equivalent to finite elements but expressed in a coordinate-free formulation. This implies that all quantities can be precomputed except edge elongation, as in a mass-spring model.
		- Only suitable for small strains (large displacements but small deformations). Tetrahedra may invert if subject to large loads.
12. Added API functions `mj_loadPluginLibrary` and `mj_loadAllPluginLibraries`. The first function is identical to `dlopen` on a POSIX system, and to `LoadLibraryA` on Windows. The second function scans a specified directory for all dynamic libraries file and loads each library found. Dynamic libraries opened by these functions are assumed to register one or more MuJoCo plugins on load.
13. Added an optional `visualize` callback to plugins, which is called during `mjv_updateScene`. This callback allows custom plugin visualizations. Enable stress visualization for the Cable plugin as an example.
14. Sensors of type [user](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-user) no longer require objtype, objname and needstage. If unspecified, the objtype is now [mjOBJ\_UNKNOWN](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtobj). `user` sensors datatype default is now “real”, needstage default is now “acc”.
15. Added support for capsules in URDF import.
16. On macOS, issue an informative error message when run under [Rosetta 2](https://support.apple.com/en-gb/HT211861) translation on an Apple Silicon machine. Pre-built MuJoCo binaries make use of [AVX](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions) instructions on x86-64 machines, which is not supported by Rosetta 2. (Before this version, users only get a cryptic “Illegal instruction” message.)

### Bug fixes

17. Fixed bug in `mj_addFileVFS` that was causing the file path to be ignored (introduced in 2.1.4).

### Simulate

18. Renamed the directory in which the `simulate` application searches for plugins from `plugin` to `mujoco_plugin`.
19. Mouse force perturbations are now applied at the selection point rather than the body center of mass.

## Version 2.3.0 (October 18, 2022)

### General

1. The `contact` array and arrays prefixed with `efc_` in `mjData` were moved out of the `buffer` into a new `arena` memory space. These arrays are no longer allocated with fixed sizes when `mjData` is created. Instead, the exact memory requirement is determined during each call to [mj\_forward](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-forward) (specifically, in [mj\_collision](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-collision) and [mj\_makeConstraint](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-makeconstraint)) and the arrays are allocated from the `arena` space. The `stack` now also shares its available memory with `arena`. This change reduces the memory footprint of `mjData` in models that do not use the PGS solver, and will allow for significant memory reductions in the future. See the [Memory allocation](https://mujoco.readthedocs.io/en/stable/modeling.html#csize) section for details.
	![](https://www.youtube.com/watch?v=RHnXD6uO3Mg)
2. Added colab notebook tutorial showing how to balance the humanoid on one leg with a Linear Quadratic Regulator. The notebook uses MuJoCo’s native Python bindings, and includes a draft `Renderer` class, for easy rendering in Python.  
	Try it yourself: [![LQRopenincolab](https://colab.research.google.com/assets/colab-badge.png)](https://colab.research.google.com/github/deepmind/mujoco/blob/main/python/LQR.ipynb)
3. Updates to humanoid model: - Added two keyframes (stand-on-one-leg and squat). - Increased maximum hip flexion angle. - Added hamstring tendons which couple the hip and knee at high hip flexion angles. - General cosmetic improvements, including improved use of defaults and better naming scheme.
4. Added [mju\_boxQP](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-boxqp) and allocation function [mju\_boxQPmalloc](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-boxqpmalloc) for solving the box-constrained Quadratic Program:
	$$
	x^* = \text{argmin} \; \tfrac{1}{2} x^T H x + x^T g \quad \text{s.t.} \quad l \le x \le u
	$$
	The algorithm, introduced in [Tassa et al. 2014](https://doi.org/10.1109/ICRA.2014.6907001), converges after 2-5 Cholesky factorisations, independent of problem size.
5. Added [mju\_mulVecMatVec](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-mulvecmatvec) to multiply a square matrix $M$ with vectors $x$ and $y$ on both sides. The function returns $x^TMy$.
6. Added new plugin API. Plugins allow developers to extend MuJoCo’s capability without modifying core engine code. The plugin mechanism is intended to replace the existing callbacks, though these will remain for the time being as an option for simple use cases and backward compatibility. The new mechanism manages stateful plugins and supports multiple plugins from different sources, allowing MuJoCo extensions to be introduced in a modular fashion, rather than as global overrides. Note the new mechanism is currently undocumented except in code, as we test it internally. If you are interested in using the plugin mechanism, please get in touch first.
7. Added assetdir compiler option, which sets the values of both meshdir and texturedir. Values in the latter attributes take precedence over assetdir.
8. Added realtime option to [visual](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual) for starting a simulation at a slower speed.
9. Added new cable composite type:
	- Cable elements are connected with ball joints.
		- The `initial` parameter specifies the joint at the starting boundary: free, ball, or none.
		- The boundary bodies are exposed with the names B\_last and B\_first.
		- The vertex initial positions can be specified directly in the XML with the parameter vertex.
		- The orientation of the body frame **is** the orientation of the material frame of the curve.
10. Added new cable passive force plugin:
	- Twist and bending stiffness can be set separately with the parameters twist and bend.
		- The stress-free configuration can be set to be the initial one or flat with the flag flat.
		- New [cable.xml](https://github.com/google-deepmind/mujoco/blob/main/model/plugin/elasticity/cable.xml) example showing the formation of plectoneme.
		- New [coil.xml](https://github.com/google-deepmind/mujoco/blob/main/model/plugin/elasticity/coil.xml) example showing a curved equilibrium configuration.
		- New [belt.xml](https://github.com/google-deepmind/mujoco/blob/main/model/plugin/elasticity/belt.xml) example showing interaction between twist and anisotropy.
		- Added test using cantilever exact solution.
	| ![](https://www.youtube.com/watch?v=25kQP671fJE) | ![](https://www.youtube.com/watch?v=4DvGe-BodFU) | ![](https://www.youtube.com/watch?v=QcGdpUd5H0c) |
	| --- | --- | --- |

### Python bindings

11. Added `id` and `name` properties to [named accessor](https://mujoco.readthedocs.io/en/latest/python.html#named-access) objects. These provide more Pythonic API access to `mj_name2id` and `mj_id2name` respectively.
12. The length of `MjData.contact` is now `ncon` rather than `nconmax`, allowing it to be straightforwardly used as an iterator without needing to check `ncon`.
13. Fix a memory leak when a Python callable is installed as callback ([#527](https://github.com/google-deepmind/mujoco/issues/527)).

## Version 2.2.2 (September 7, 2022)

### General

![](https://www.youtube.com/watch?v=BcHZ5BFeTmU)
1. Added [adhesion actuators](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-adhesion) mimicking vacuum grippers and adhesive biomechanical appendages.
2. Added related [example model](https://github.com/google-deepmind/mujoco/tree/main/model/adhesion) and video:
3. Added [mj\_jacSubtreeCom](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-jacsubtreecom) for computing the translational Jacobian of the center-of-mass of a subtree.
4. Added torquescale and anchor attributes to weld constraints. torquescale sets the torque-to-force ratio exerted by the constraint, anchor sets the point at which the weld wrench is applied. See [weld](https://mujoco.readthedocs.io/en/stable/XMLreference.html#equality-weld) for more details.
5. Increased `mjNEQDATA`, the row length of equality constraint parameters in `mjModel.eq_data`, from 7 to 11.
6. Added visualisation of anchor points for both connect and weld constraints (activated by the ‘N’ key in `simulate`).
7. Added [weld.xml](https://github.com/google-deepmind/mujoco/blob/main/test/engine/testdata/weld.xml) showing different uses of new weld attributes.
	![](https://www.youtube.com/watch?v=s-0JHanqV1A)
8. Cartesian 6D end-effector control is now possible by adding a reference site to actuators with site transmission. See description of new refsite attribute in the [actuator](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general) documentation and [refsite.xml](https://github.com/google-deepmind/mujoco/blob/main/test/engine/testdata/actuation/refsite.xml) example model.
9. Added autolimits compiler option. If `true`, joint and tendon limited attributes and actuator ctrllimited, forcelimited and actlimited attributes will automatically be set to `true` if the corresponding range *is defined* and `false` otherwise.
	If `autolimits="false"` (the default) models where a range attribute is specified without the limited attribute will fail to compile. A future release will change the default of autolimits to `true`, and this compilation error allows users to catch this future change of behavior.
	> [!note] Attention
	> This is a breaking change. In models where a range was defined but limited was unspecified, explicitly set limited to `false` or remove the range to maintain the current behavior of your model.
10. Added moment of inertia computation for all well-formed meshes. This option is activated by setting the compiler flag exactmeshinertia to `true` (defaults to `false`). This default may change in the future.
11. Added parameter shellinertia to geom, for locating the inferred inertia on the boundary (shell). Currently only meshes are supported.
12. For meshes from which volumetric inertia is inferred, raise error if the orientation of mesh faces is not consistent. If this occurs, fix the mesh in e.g., MeshLab or Blender.
	![](https://www.youtube.com/watch?v=I2q7D0Vda-A)
13. Added catenary visualisation for hanging tendons. The model seen in the video can be found [here](https://github.com/google-deepmind/mujoco/blob/main/test/engine/testdata/catenary.xml).
14. Added `azimuth` and `elevation` attributes to [visual/global](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual-global), defining the initial orientation of the free camera at model load time.
15. Added `mjv_defaultFreeCamera` which sets the default free camera, respecting the above attributes.
16. `simulate` now supports taking a screenshot via a button in the File section or via `Ctrl-P`.
17. Improvements to time synchronisation in `simulate`, in particular report actual real-time factor if different from requested factor (if e.g., the timestep is so small that simulation cannot keep up with real-time).
18. Added a disable flag for sensors.
19. [mju\_mulQuat](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-mulquat) and [mju\_mulQuatAxis](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-mulquataxis) support in place computation. For example  
	`mju_mulQuat(a, a, b);` sets the quaternion `a` equal to the product of `a` and `b`.
20. Added sensor matrices to `mjd_transitionFD` (note this is an API change).

### Deleted/deprecated features

21. Removed `distance` constraints.

### Bug fixes

22. Fixed rendering of some transparent geoms in reflection.
23. Fixed `intvelocity` defaults parsing.

## Version 2.2.1 (July 18, 2022)

### General

1. Added `mjd_transitionFD` to compute efficient finite difference approximations of the state-transition and control-transition matrices, [see here](https://mujoco.readthedocs.io/en/stable/computation/index.html#derivatives) for more details.
2. Added derivatives for the ellipsoid fluid model.
3. Added `ctrl` attribute to [keyframes](https://mujoco.readthedocs.io/en/stable/XMLreference.html#keyframe).
4. Added `clock` sensor which [measures time](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-clock).
5. Added visualisation groups to skins.
6. Added actuator visualisation for `free` and `ball` joints and for actuators with `site` transmission.
7. Added visualisation for actuator activations.
8. Added `<actuator-intvelocity>` actuator shortcut for “integrated velocity” actuators, documented [here](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-intvelocity).
9. Added `<actuator-damper>` actuator shortcut for active-damping actuators, documented [here](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-damper).
10. `mju_rotVecMat` and `mju_rotVecMatT` now support in-place multiplication.
11. `mjData.ctrl` values are no longer clamped in-place, remain untouched by the engine.
12. Arrays in mjData’s buffer now align to 64-byte boundaries rather than 8-byte.
13. Added memory poisoning when building with [Address Sanitizer (ASAN)](https://clang.llvm.org/docs/AddressSanitizer.html) and [Memory Sanitizer (MSAN)](https://clang.llvm.org/docs/MemorySanitizer.html). This allows ASAN to detect reads and writes to regions in `mjModel.buffer` and `mjData.buffer` that do not lie within an array, and for MSAN to detect reads from uninitialised fields in `mjData` following `mj_resetData`.
14. Added a [slider-crank example model](https://github.com/google-deepmind/mujoco/tree/main/model/slider_crank).

### Bug fixes

15. [Activation clamping](https://mujoco.readthedocs.io/en/stable/modeling.html#cactrange) was not being applied in the [implicit integrator](https://mujoco.readthedocs.io/en/stable/computation/index.html#geintegration).
16. Stricter parsing of orientation specifiers. Before this change, a specification that included both `quat` and an [alternative specifier](https://mujoco.readthedocs.io/en/stable/modeling.html#corientation) e.g., `<geom ... quat=".1 .2 .3 .4" euler="10 20 30">`, would lead to the `quat` being ignored and only `euler` being used. After this change a parse error will be thrown.
17. Stricter parsing of XML attributes. Before this change an erroneous XML snippet like `<geom size="1/2 3 4">` would have been parsed as `size="1 0 0"` and no error would have been thrown. Now throws an error.
18. Trying to load a `NaN` via XML like `<geom size="1 NaN 4">`, while allowed for debugging purposes, will now print a warning.
19. Fixed null pointer dereference in `mj_loadModel`.
20. Fixed memory leaks when loading an invalid model from MJB.
21. Integer overflows are now avoided when computing `mjModel` buffer sizes.
22. Added missing warning string for `mjWARN_BADCTRL`.

### Packaging

23. Changed MacOS packaging so that the copy of `mujoco.framework` embedded in `MuJoCo.app` can be used to build applications externally.

## Version 2.2.0 (May 23, 2022)

### Open Sourcing

1. MuJoCo is now fully open-source software. Newly available top level directories are:
	a. `src/`: All source files. Subdirectories correspond to the modules described in the Programming chapter [introduction](https://mujoco.readthedocs.io/en/stable/programming/index.html#inintro):
	- `src/engine/`: Core engine.
		- `src/xml/`: XML parser.
		- `src/user/`: Model compiler.
		- `src/visualize/`: Abstract visualizer.
		- `src/ui/`: UI framework.
	2. `test/`: Tests and corresponding asset files.
		3. `dist/`: Files related to packaging and binary distribution.
2. Added [contributor’s guide](https://github.com/google-deepmind/mujoco/blob/main/CONTRIBUTING.md) and [style guide](https://github.com/google-deepmind/mujoco/blob/main/STYLEGUIDE.md).

### General

3. Added analytic derivatives of smooth (unconstrained) dynamics forces, with respect to velocities:
	- Centripetal and Coriolis forces computed by the Recursive Newton-Euler algorithm.
		- Damping and fluid-drag passive forces.
		- Actuation forces.
4. Added `implicit` integrator. Using the analytic derivatives above, a new implicit-in-velocity integrator was added. This integrator lies between the Euler and Runge Kutta integrators in terms of both stability and computational cost. It is most useful for models which use fluid drag (e.g. for flying or swimming) and for models which use [velocity actuators](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-velocity). For more details, see the [Numerical Integration](https://mujoco.readthedocs.io/en/stable/computation/index.html#geintegration) section.
5. Added actlimited and actrange attributes to [general actuators](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general), for clamping actuator internal states (activations). This clamping is useful for integrated-velocity actuators, see the [Activation clamping](https://mujoco.readthedocs.io/en/stable/modeling.html#cactrange) section for details.
6. `mjData` fields `qfrc_unc` (unconstrained forces) and `qacc_unc` (unconstrained accelerations) were renamed `qfrc_smooth` and `qacc_smooth`, respectively. While “unconstrained” is precise, “smooth” is more intelligible than “unc”.
7. Public headers have been moved from `/include` to `/include/mujoco/`, in line with the directory layout common in other open source projects. Developers are encouraged to include MuJoCo public headers in their own codebase via `#include <mujoco/filename.h>`.
8. The default shadow resolution specified by the [shadowsize](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual-quality) attribute was increased from 1024 to 4096.
9. Saved XMLs now use 2-space indents.

### Bug fixes

10. Antialiasing was disabled for segmentation rendering. Before this change, if the [offsamples](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual-quality) attribute was greater than 0 (the default value is 4), pixels that overlapped with multiple geoms would receive averaged segmentation IDs, leading to incorrect or non-existent IDs. After this change offsamples is ignored during segmentation rendering.
11. The value of the enable flag for the experimental multiCCD feature was made sequential with other enable flags. Sequentiality is assumed in the `simulate` UI and elsewhere.
12. Fix issue of duplicated meshes when saving models with OBJ meshes using mj\_saveLastXML.

## Version 2.1.5 (Apr. 13, 2022)

### General

1. Added an experimental feature: multi-contact convex collision detection, activated by an enable flag. See full description [here](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag).

### Bug fixes

2. GLAD initialization logic on Linux now calls `dlopen` to load a GL platform dynamic library if a `*GetProcAddress` function is not already present in the process’ global symbol table. In particular, processes that use GLFW to set up a rendering context that are not explicitly linked against `libGLX.so` (this applies to the Python interpreter, for example) will now work correctly rather than fail with a `gladLoadGL` error when `mjr_makeContext` is called.
3. In the Python bindings, named indexers for scalar fields (e.g. the `ctrl` field for actuators) now return a NumPy array of shape `(1,)` rather than `()`. This allows values to be assigned to these fields more straightforwardly.

## Version 2.1.4 (Apr. 4, 2022)

### General

1. MuJoCo now uses GLAD to manage OpenGL API access instead of GLEW. On Linux, there is no longer a need to link against different GL wrangling libraries depending on whether GLX, EGL, or OSMesa is being used. Instead, users can simply use GLX, EGL, or OSMesa to create a GL context and `mjr_makeContext` will detect which one is being used.
2. Added visualisation for contact frames. This is useful when writing or modifying collision functions, when the actual direction of the x and y axes of a contact can be important.

### Binary build

3. The `_nogl` dynamic library is no longer provided on Linux and Windows. The switch to GLAD allows us to resolve OpenGL symbols when `mjr_makeContext` is called rather than when the library is loaded. As a result, the MuJoCo library no longer has an explicit dynamic dependency on OpenGL, and can be used on system where OpenGL is not present.

### Simulate

4. Fixed a bug in simulate where pressing ‘\[’ or ‘\]’ when a model is not loaded causes a crash.
5. Contact frame visualisation was added to the Simulate GUI.
6. Renamed “set key”, “reset to key” to “save key” and “load key”, respectively.
7. Changed bindings of F6 and F7 from the not very useful “vertical sync” and “busy wait” to the more useful cycling of frames and labels.

### Bug fixes

8. `mj_resetData` zeroes out the `solver_nnz` field.
9. Removed a special branch in `mju_quat2mat` for unit quaternions. Previously, `mju_quat2mat` skipped all computation if the real part of the quaternion equals 1.0. For very small angles (e.g. when finite differencing), the cosine can evaluate to exactly 1.0 at double precision while the sine is still nonzero.

## Version 2.1.3 (Mar. 23, 2022)

### General

1. `simulate` now supports cycling through cameras (with the `[` and `]` keys).
2. `mjVIS_STATIC` toggles all static bodies, not just direct children of the world.

### Python bindings

3. Added a `free()` method to `MjrContext`.
4. Enums now support arithmetic and bitwise operations with numbers.

### Bug fixes

5. Fixed rendering bug for planes, introduced in 2.1.2. This broke maze environments in [dm\_control](https://github.com/google-deepmind/dm_control).

## Version 2.1.2 (Mar. 15, 2022)

### New modules

1. Added new [Python bindings](https://mujoco.readthedocs.io/en/stable/python.html), which can be installed via `pip install mujoco`, and imported as `import mujoco`.
2. Added new [Unity plug-in](https://mujoco.readthedocs.io/en/stable/unity.html).
3. Added a new `introspect` module, which provides reflection-like capability for MuJoCo’s public API, currently describing functions and enums. While implemented in Python, this module is expected to be generally useful for automatic code generation targeting multiple languages. (This is not shipped as part of the `mujoco` Python bindings package.)

### API changes

4. Moved definition of `mjtNum` floating point type into a new header [mjtnum.h](https://github.com/google-deepmind/mujoco/blob/3577e2cf8bf841475b489aefff52276a39f24d51/include/mjtnum.h).
5. Renamed header `mujoco_export.h` to [mjexport.h](https://mujoco.readthedocs.io/en/stable/programming/index.html#inheader).
6. Added `mj_printFormattedData`, which accepts a format string for floating point numbers, for example to increase precision.

### General

7. MuJoCo can load [OBJ](https://en.wikipedia.org/wiki/Wavefront_.obj_file) mesh files.
	1. Meshes containing polygons with more than 4 vertices are not supported.
		2. In OBJ files containing multiple object groups, any groups after the first one will be ignored.
		3. Added (post-release, not included in the 2.1.2 archive) textured [mug](https://github.com/google-deepmind/mujoco/blob/main/model/mug/mug.xml) example model:
		[![_images/mug.png](https://mujoco.readthedocs.io/en/stable/_images/mug.png)](https://mujoco.readthedocs.io/en/stable/_images/mug.png)
8. Added optional frame-of-reference specification to [framepos](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-framepos), [framequat](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-framequat), [framexaxis](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-framexaxis), [frameyaxis](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-frameyaxis), [framezaxis](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-framezaxis), [framelinvel](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-framelinvel), and [frameangvel](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-frameangvel) sensors. The frame-of-reference is specified by new reftype and refname attributes.
9. Sizes of [user parameters](https://mujoco.readthedocs.io/en/stable/modeling.html#cuser) are now automatically inferred.
	1. Declarations of user parameters in the top-level [size](https://mujoco.readthedocs.io/en/stable/XMLreference.html#size) clause (e.g. nuser\_body, nuser\_jnt, etc.) now accept a value of -1, which is the default. This will automatically set the value to the length of the maximum associated user attribute defined in the model.
		2. Setting a value smaller than -1 will lead to a compiler error (previously a segfault).
		3. Setting a value to a length smaller than some user attribute defined in the model will lead to an error (previously additional values were ignored).
10. Increased the maximum number of lights in an [mjvScene](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjvscene) from 8 to 100.
11. Saved XML files only contain explicit [inertial](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-inertial) elements if the original XML included them. Inertias that were automatically inferred by the compiler’s [inertiafromgeom](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler) mechanism remain unspecified.
12. User-selected geoms are always rendered as opaque. This is useful in interactive visualizers.
13. Static geoms now respect their [geom group](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom) for visualisation. Until this change rendering of static geoms could only be toggled using the [mjVIS\_STATIC](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjtvisflag) visualisation flag. After this change, both the geom group and the visualisation flag need to be enabled for the geom to be rendered.
14. Pointer parameters in function declarations in [mujoco.h](https://mujoco.readthedocs.io/en/stable/programming/index.html#inheader) that are supposed to represent fixed-length arrays are now spelled as arrays with extents, e.g. `mjtNum quat[4]` rather than `mjtNum* quat`. From the perspective of C and C++, this is a non-change since array types in function signatures decay to pointer types. However, it allows autogenerated code to be aware of expected input shapes.
15. Experimental stateless fluid interaction model. As described [here](https://mujoco.readthedocs.io/en/stable/computation/index.html#gepassive), fluid forces use sizes computed from body inertia. While sometimes convenient, this is very rarely a good approximation. In the new model forces act on geoms, rather than bodies, and have a several user-settable parameters. The model is activated by setting a new attribute: `<geom fluidshape="ellipsoid"/>`. The parameters are described succinctly [here](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom), but we leave a full description or the model and its parameters to when this feature leaves experimental status.

### Bug fixes

16. `mj_loadXML` and `mj_saveLastXML` are now locale-independent. The Unity plugin should now work correctly for users whose system locales use commas as decimal separators.
17. XML assets in VFS no longer need to end in a null character. Instead, the file size is determined by the size parameter of the corresponding VFS entry.
18. Fix a vertex buffer object memory leak in `mjrContext` when skins are used.
19. Camera quaternions are now normalized during XML compilation.

### Binary build

20. Windows binaries are now built with Clang.

## Version 2.1.1 (Dec. 16, 2021)

### API changes

1. Added `mj_printFormattedModel`, which accepts a format string for floating point numbers, for example to increase precision.
2. Added `mj_versionString`, which returns human-readable string that represents the version of the MuJoCo binary.
3. Converted leading underscores to trailing underscores in private instances of API struct definitions, to conform to reserved identifier directive, see [C standard: Section 7.1.3](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf).
	> [!note] Attention
	> This is a minor breaking change. Code which references private instances will break. To fix, replace leading underscores with trailing underscores, e.g. `_mjModel` → `mjModel_`.

### General

4. Safer string handling: replaced `strcat`, `strcpy`, and `sprintf` with `strncat`, `strncpy`, and `snprintf` respectively.
5. Changed indentation from 4 spaces to 2 spaces, K&R bracing style, added braces to one-line conditionals.

### Bug Fixes

6. Fixed reading from uninitialized memory in PGS solver.
7. Computed capsule inertias are now exact. Until this change, capsule masses and inertias computed by the [compiler](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler) ’s inertiafromgeom mechanism were approximated by a cylinder, formed by the capsule’s cylindrical middle section, extended on both ends by half the capsule radius. Capsule inertias are now computed with the [Parallel Axis theorem](https://en.wikipedia.org/wiki/Parallel_axis_theorem), applied to the two hemispherical end-caps.
	> [!note] Attention
	> This is a minor breaking change. Simulation of a model with automatically-computed capsule inertias will be numerically different, leading to, for example, breakage of golden-value tests.
8. Fixed bug related to [force](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-force) and [torque](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-torque) sensors. Until this change, forces and torques reported by F/T sensors ignored out-of-tree constraint wrenches except those produced by contacts. Force and torque sensors now correctly take into account the effects of [connect](https://mujoco.readthedocs.io/en/stable/XMLreference.html#equality-connect) and [weld](https://mujoco.readthedocs.io/en/stable/XMLreference.html#equality-weld) constraints.
	> [!note] Note
	> Forces generated by [spatial tendons](https://mujoco.readthedocs.io/en/stable/XMLreference.html#tendon-spatial) which are outside the kinematic tree (i.e., between bodies which have no ancestral relationship) are still not taken into account by force and torque sensors. This remains a future work item.

### Code samples

9. `testspeed`: Added injection of pseudo-random control noise, turned on by default. This is to avoid settling into some fixed contact configuration and providing an unrealistic timing measure.
10. `simulate`:
	1. Added slower-than-real-time functionality, which is controlled via the ‘+’ and ‘-’ keys.
		2. Added sliders for injecting Brownian noise into the controls.
		3. Added “Print Camera” button to print an MJCF clause with the pose of the current camera.
		4. The camera pose is not reset when reloading the same model file.

### Updated dependencies

11. `TinyXML` was replaced with `TinyXML2` 6.2.0.
12. `qhull` was upgraded to version 8.0.2.
13. `libCCD` was upgraded to version 1.4.
14. On Linux, `libstdc++` was replaced with `libc++`.

### Binary build

15. MacOS packaging. We now ship Universal binaries that natively support both Apple Silicon and Intel CPUs.
	1. MuJoCo library is now packaged as a [Framework Bundle](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Concepts/FrameworkAnatomy.html), allowing it to be incorporated more easily into Xcode projects (including Swift projects). Developers are encouraged to compile and link against MuJoCo using the `-framework mujoco` flag, however all header files and the `libmujoco.2.1.1.dylib` library can still be directly accessed inside the framework.
		2. Sample applications are now packaged into an Application Bundle called `MuJoCo.app`. When launched via GUI, the bundle launches the `simulate` executable. Other precompiled sample programs are shipped inside that bundle (in `MuJoCo.app/Contents/MacOS`) and can be launched via command line.
		3. Binaries are now signed and the disk image is notarized.
16. Windows binaries and libraries are now signed.
17. Link-time optimization is enabled on Linux and macOS, leading to an average of ~20% speedup when benchmarked on three test models (`cloth.xml`, `humanoid.xml`, and `humanoid100.xml`).
18. Linux binaries are now built with LLVM/Clang instead of GCC.
19. An AArch64 (aka ARM64) Linux build is also provided.
20. Private symbols are no longer stripped from shared libraries on Linux and MacOS.

### Sample models

21. Clean-up of the `model/` directory.
	1. Rearranged into subdirectories which include all dependencies.
		2. Added descriptions in XML comments, cleaned up XMLs.
		3. Deleted some composite models: `grid1`, `grid1pin`, `grid2`, `softcylinder`, `softellipsoid`.
22. Added descriptive animations in `docs/images/models/`:

[![humanoid](https://mujoco.readthedocs.io/en/stable/_images/humanoid.gif)](https://mujoco.readthedocs.io/en/stable/_images/humanoid.gif) [![particle](https://mujoco.readthedocs.io/en/stable/_images/particle.gif)](https://mujoco.readthedocs.io/en/stable/_images/particle.gif)

## Version 2.1.0 (Oct. 18, 2021)

### New features

1. Keyframes now have `mocap_pos` and `mocap_quat` fields (mpos and quat attributes in the XML) allowing mocap poses to be stored in keyframes.
2. New utility functions: `mju_insertionSortInt` (integer insertion sort) and `mju_sigmoid` (constructing a sigmoid from two half-quadratics).

### General

3. The preallocated sizes in the virtual file system (VFS) increased to 2000 and 1000, to allow for larger projects.
4. The C structs in the `mjuiItem` union are now named, for compatibility.
5. Fixed: `mjcb_contactfilter` type is `mjfConFilt` (was `mjfGeneric`).
6. Fixed: The array of sensors in `mjCModel` was not cleared.
7. Cleaned up cross-platform code (internal changes, not visible via the API).
8. Fixed a bug in parsing of XML `texcoord` data (related to number of vertices).
9. Fixed a bug in [simulate.cc](https://github.com/google-deepmind/mujoco/blob/main/simulate/simulate.cc) related to `nkey` (the number of keyframes).
10. Accelerated collision detection in the presence of large numbers of non-colliding geoms (with `contype==0 and conaffinity==0`).

### UI

11. Figure selection type changed from `int` to `float`.
12. Figures now show data coordinates, when selection and highlight are enabled.
13. Changed `mjMAXUIMULTI` to 35, `mjMAXUITEXT` to 300, `mjMAXUIRECT` to 25.
14. Added collapsible sub-sections, implemented as separators with state: `mjSEPCLOSED` collapsed, `mjSEPCLOSED+1` expanded.
15. Added `mjITEM_RADIOLINE` item type.
16. Added function `mjui_addToSection` to simplify UI section construction.
17. Added subplot titles to `mjvFigure`.

### Rendering

18. `render_gl2` guards against non-finite floating point data in the axis range computation.
19. `render_gl2` draws lines from back to front for better visibility.
20. Added function `mjr_label` (for text labels).
21. `mjr_render` exits immediately if `ngeom==0`, to avoid errors from uninitialized scenes (e.g. `frustrum==0`).
22. Added scissor box in `mjr_render`, so we don’t clear the entire window at every frame.

## Earlier versions

For changelogs of earlier versions please see [roboti.us](https://www.roboti.us/download.html).
