---
source_id: "SRC-robotics-705"
title: "MuJoCo modeling mesh collision semantics"
source_type: "documentation"
publisher: "MuJoCo"
source_date: "待验证"
url: "https://mujoco.readthedocs.io/en/stable/modeling.html"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-11-10T02:02:05+00:00"
tags:
  - raw/source
  - source-type/documentation
  - evidence/s
aliases:
  - SRC-robotics-705
---
# MuJoCo modeling mesh collision semantics

## Modeling

## Introduction

MuJoCo’s native model format is **MJCF**, an XML-based language designed to describe complex dynamical systems. This chapter is the primary MJCF modeling guide. The complete element and attribute reference manual is available in the [XML Reference](https://mujoco.readthedocs.io/en/stable/XMLreference.html) chapter. MuJoCo also supports loading models from other formats such as URDF (see ), MJZ Zip archives (see [MJZ Archives](https://mujoco.readthedocs.io/en/stable/programming/modeledit.html#mjzarchives)), and OpenUSD (see [OpenUSD](https://mujoco.readthedocs.io/en/stable/OpenUSD/index.html)).

MJCF models can represent complex dynamical systems with a wide range of features and model elements. Accessing all these features requires a rich modeling format, which can become cumbersome if it is not designed with usability in mind. Therefore we have made an effort to design MJCF as a scalable format, allowing users to start small and build more detailed models later. Particularly helpful in this regard is the extensive mechanism inspired by the idea of Cascading Style Sheets (CSS) inlined in HTML. It enables users to rapidly create new models and experiment with them. Experimentation is further aided by numerous [options](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option) which can be used to reconfigure the simulation pipeline, and by quick re-loading that makes model editing an interactive process.

One can think of MJCF as a hybrid between a modeling format and a programming language. There is a built-in compiler, which is a concept normally associated with programming languages. While MJCF does not have the power of a general-purpose programming language, a number of sophisticated compile-time computations are invoked automatically depending on how the model is designed.

### Procedural Modeling

This chapter covers high-level model design. For detailed documentation on programmatic modeling via the [mjSpec](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjspec) API—including loading, editing, compiling, and saving models in C/C++ or Python—see the [Model Editing](https://mujoco.readthedocs.io/en/stable/programming/modeledit.html) chapter.

## MJCF Mechanisms

MJCF uses several mechanisms for model creation which span multiple model elements. To avoid repetition we describe them in detail only once in this section. These mechanisms do not correspond to new simulation concepts beyond those introduced in the Computation chapter. Their role is to simplify the creation of MJCF models, and to enable the use of different data formats without need for manual conversion to a canonical format.

### Kinematic tree

The main part of the MJCF file is an XML tree created by nested [body](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body) elements. The top-level body is special and is called worldbody. This tree organization is in contrast with URDF where one creates a collection of links and then connects them with joints that specify a child and a parent link. In MJCF the child body is literally a child of the parent body, in the sense of XML.

When a [joint](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint) is defined inside a body, its function is not to connect the parent and child but rather to create motion degrees of freedom between them. If no joints are defined within a given body, that body is welded to its parent. A body in MJCF can contain multiple joints, thus there is no need to introduce dummy bodies for creating composite joints. Instead simply define all the primitive joints that form the desired composite joint within the same body. For example, two sliders and one hinge can be used to model a body moving in a plane.

Other MJCF elements can be defined within the tree created by nested body elements, in particular [joint](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint), [geom](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom), [site](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-site), [camera](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera), [light](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-light). When an element is defined within a body, it is fixed to the local frame of that body and always moves with it. Elements that refer to multiple bodies, or do not refer to bodies at all, are defined in separate sections outside the kinematic tree.

### Default settings

MJCF has an elaborate mechanism for setting default attribute values. This allows us to have a large number of elements and attributes needed to expose the rich functionality of the software, and at the same time write short and readable model files. This mechanism further enables the user to introduce a change in one place and have it propagate throughout the model. We start with an example.

```xml
<mujoco>
  <default class="main">
    <geom rgba="1 0 0 1"/>
    <default class="sub">
      <geom rgba="0 1 0 1"/>
    </default>
  </default>

  <worldbody>
    <geom type="box"/>
    <body childclass="sub">
      <geom type="ellipsoid"/>
      <geom type="sphere" rgba="0 0 1 1"/>
      <geom type="cylinder" class="main"/>
    </body>
  </worldbody>
</mujoco>
```

This example will not actually compile because some required information is missing, but here we are only interested in the setting of geom rgba values. The four geoms created above will end up with the following rgba values as a result of the default setting mechanism:

| geom type | geom rgba |
| --- | --- |
| box | 1 0 0 1 |
| ellipsoid | 0 1 0 1 |
| sphere | 0 0 1 1 |
| cylinder | 1 0 0 1 |

The box uses the top-level defaults class “main” to set the values of its undefined attributes, because no other class was specified. The body specifies childclass “sub”, causing all children of this body (and all their children etc.) to use class “sub” unless specified otherwise. So the ellipsoid uses class “sub”. The sphere has explicitly defined rgba which overrides the default settings. The cylinder specifies defaults class “main”, and so it uses “main” instead of “sub”, even though the latter was specified in the childclass attribute of the body containing the geom.

Now we describe the general rules. MuJoCo supports unlimited number of defaults classes, created by possibly nested [default](https://mujoco.readthedocs.io/en/stable/XMLreference.html#default) elements in the XML. Each class has a unique name – which is a required attribute except for the top-level class whose name is “main” if left undefined. Each class also has a complete collection of dummy model elements, with their attributes set as follows. When a defaults class is defined within another defaults class, the child automatically inherits all attribute values from the parent. It can then override some or all of them by defining the corresponding attributes. The top-level defaults class does not have a parent, and so its attributes are initialized to internal defaults which are shown in the [Reference chapter](https://mujoco.readthedocs.io/en/stable/XMLreference.html).

The dummy elements contained in the defaults classes are not part of the model; they are only used to initialize the attribute values of the actual model elements. When an actual element is first created, all its attributes are copied from the corresponding dummy element in the defaults class that is currently active. There is always an active defaults class, which can be determined in one of three ways. If no class is specified in the present element or any of its ancestor bodies, the top-level class is used (regardless of whether it is called “main” or something else). If no class is specified in the present element but one or more of its ancestor bodies specify a childclass, then the childclass from the nearest ancestor body is used. If the present element specifies a class, that class is used regardless of any childclass attributes in its ancestor bodies.

Some attributes, such as body inertia, can be in a special undefined state. This instructs the compiler to infer the corresponding value from other information, in this case the inertias of the geoms attached to the body. The undefined state cannot be entered in the XML file. Therefore once an attribute is defined in a given class, it cannot be undefined in that class or in any of its child classes. So if the goal is to leave a certain attribute undefined in a given model element, it must be undefined in the active defaults class.

A final twist here is actuators. They are different because some of the actuator-related elements are actually shortcuts, and shortcuts interact with the defaults setting mechanism in a non-obvious way. This is explained in the section below.

### Coordinate frames

The positions and orientations of all elements defined in the kinematic tree are expressed in local coordinates, relative to the parent body for bodies, and relative to the body that contains the element for geoms, joints, sites, cameras and lights.

A related attribute is [compiler/angle](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-angle). It specifies whether angles in the MJCF file are expressed in degrees or radians (after compilation, angles are always expressed in radians).

Positions are specified using

pos: real(3), “0 0 0”

Position relative to parent.

#### Frame orientations

Several model elements have right-handed spatial frames associated with them. These are all the elements defined in the kinematic tree except for joints. A spatial frame is defined by its position and orientation. Specifying 3D positions is straightforward, but specifying 3D orientations can be challenging. This is why MJCF provides several alternative mechanisms. No matter which mechanism the user chooses, the frame orientation is always converted internally to a unit quaternion. Recall that a 3D rotation by angle $a$ around axis given by the unit vector $(x, y, z)$ corresponds to the quaternion $(\cos(a/2), \: \sin(a/2) \cdot (x, y, z))$. Also recall that every 3D orientation can be uniquely specified by a single 3D rotation by some angle around some axis.

All MJCF elements that have spatial frames allow the five attributes listed below. The frame orientation is specified using at most one of these attributes. The quat attribute has a default value corresponding to the null rotation, while the others are initialized in the special undefined state. Thus if none of these attributes are specified by the user, the frame is not rotated.

quat: real(4), “1 0 0 0”

If the quaternion is known, this is the preferred was to specify the frame orientation because it does not involve conversions. Instead it is normalized to unit length and copied into mjModel during compilation. When a model is saved as MJCF in the canonical notation ([savecanonical](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-savecanonical)), or with the values which compilation made ([savecompiled](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-savecompiled)), all frame orientations are expressed as quaternions using this attribute; otherwise each is saved as it was written.

axisangle: real(4), optional

These are the quantities $(x, y, z, a)$ mentioned above. The last number is the angle of rotation, in degrees or radians as specified by the angle attribute of [compiler](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler). The first three numbers determine a 3D vector which is the rotation axis. This vector is normalized to unit length during compilation, so the user can specify a vector of any non-zero length. Keep in mind that the rotation is right-handed; if the direction of the vector $(x, y, z)$ is reversed this will result in the opposite rotation. Changing the sign of $a$ can also be used to specify the opposite rotation.

euler: real(3), optional

Rotation angles around three coordinate axes. The sequence of axes around which these rotations are applied is determined by the eulerseq attribute of [compiler](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler) and is the same for the entire model.

xyaxes: real(6), optional

The first 3 numbers are the X axis of the frame. The next 3 numbers are the Y axis of the frame, which is automatically made orthogonal to the X axis. The Z axis is then defined as the cross-product of the X and Y axes.

zaxis: real(3), optional

The Z axis of the frame. The compiler finds the minimal rotation that maps the vector $(0, 0, 1)$ into the vector specified here. This determines the X and Y axes of the frame implicitly. This is useful for geoms with rotational symmetry around the Z axis, as well as lights – which are oriented along the Z axis of their frame.

### Solver parameters

The constraint solver finds forces that satisfy soft constraints, parameterized by three quantities: the *impedance* $d$ (how strongly to enforce the constraint), *stiffness* $k$, and *damping* $b$ (how to respond to violations). These are described mathematically in the [Parameters](https://mujoco.readthedocs.io/en/stable/computation/index.html#soparameters) section of the Computation chapter. Here we explain how to set them. Setting is done indirectly, through the attributes solref and solimp which are available in all MJCF elements involving constraints. These parameters can be adjusted per constraint, or per defaults class, or left undefined – in which case MuJoCo uses the internal defaults shown below. Note also the override mechanism available in [option](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option); it can be used to change all contact-related solver parameters at runtime, so as to experiment interactively with parameter settings or implement continuation methods for numerical optimization.

Here we focus on a single scalar constraint. Using slightly different notation from the Computation chapter, let $\ac$ denote the acceleration, $v$ the velocity, $r$ the position or residual (defined as 0 in friction dimensions), $k$ and $b$ the stiffness and damping of the virtual spring used to define the reference acceleration $\ar = -b v - k r$ (see [(13)](https://mujoco.readthedocs.io/en/stable/computation/index.html#equation-eq-aref)). Let $d$ be the constraint impedance, and $\au$ the acceleration in the absence of constraint force. Our earlier analysis revealed that the dynamics in constraint space are approximately

(1) [#](#equation-eq-constraint "Permalink to this equation") $\ac + d \cdot (b v + k r) = (1 - d)\cdot \au$

Again, the parameters that are under the user’s control are $d, b, k$. The remaining quantities are functions of the system state and are computed automatically at each time step.

#### Impedance

We begin by explaining the constraint impedance $d$.

> [!note] Intuitive description of the impedance
> The *impedance* $d \in (0, 1)$ corresponds to a constraint’s **ability to generate force**. Small values of $d$ correspond to weak constraints while large values of $d$ correspond to strong constraints. The impedance affects the constraint at all times, in particular when the system is at rest. Impedance is set using the solimp attribute.

Recall that $d$ must lie between 0 and 1; internally MuJoCo clamps it to the range \[[mjMINIMP mjMAXIMP](https://mujoco.readthedocs.io/en/stable/APIreference/APIglobals.html#glnumericengine)\] which is currently set to \[0.0001 0.9999\]. It causes the solver to interpolate between the unforced acceleration $\au$ and reference acceleration $\ar$. The user can set $d$ to a constant, or take advantage of its interpolating property and make it position-dependent, i.e., a function of the constraint violation $r$. Position-dependent impedance can be used to model soft contact layers around objects, or define equality constraints that become stronger with larger violation (so as to approximate backlash, for example). The shape of the function $d(r)$ is determined by the element-specific parameter vector solimp.

**solimp:** real(5), “0.9 0.95 0.001 0.5 2”

The five numbers ($d_0$, $d_\mathrm{w}$, $\text{width}$, $\text{midpoint}$, $\text{power}$) parameterize $d(r)$ – the impedance $d$ as a function of the constraint violation $r$.

The first 3 values indicate that the impedance will vary smoothly as $r$ varies from $0$ to $\text{width}$:

$$
d(0) = d_0, \quad d(\text{width}) = d_\mathrm{w}
$$

The 4th and 5th values, $\text{midpoint}$ and $\text{power}$, control the shape of the sigmoidal function that interpolates between $d_0$ and $d_\mathrm{w}$, as shown in the plots below. The plots show two reflected sigmoids, because the impedance $d(r)$ depends on the absolute value of $r$. The $\text{power}$ (of the polynomial spline used to generate the function) must be 1 or greater. The $\text{midpoint}$ (specifying the inflection point) must be between 0 and 1, and is expressed in units of $\text{width}$. Note that when $\text{power}$ is 1, the function is linear regardless of the $\text{midpoint}$.

[![Impedance curves with midpoint 0.2, 0.5 and 0.8 by row and power 1, 2 and 6 by column. The negative-residual half is shaded; dotted lines mark midpoint times width.](https://mujoco.readthedocs.io/en/stable/_images/impedance.svg)](https://mujoco.readthedocs.io/en/stable/_images/impedance.svg)These plots show the impedance $d(r)$ as a function of the constraint violation $r$. For equality constraints, $r$ is the constraint violation itself. For limits, normal directions of elliptic cones and all directions of pyramidal cones, $r$ is the distance minus the margin at which the constraint becomes active (the [margin](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-margin) attribute for contacts). These unilateral constraints are active only when $r<0$, shown by the shaded region.

For frictional constraints, see.

> [!tip] Smoothness and differentiability
> For completely smooth (differentiable) dynamics, limits and contacts should have $d_0=0$ (`solimp[0]=0`). Specifically for contacts, the of geom-associated solver parameters should be kept in mind. See also discussion of derivatives in the [Computation chapter](https://mujoco.readthedocs.io/en/stable/computation/index.html#derivatives) and in the [mjd\_transitionFD](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjd-transitionfd) documentation.

#### Reference

Next we explain the setting of the stiffness $k$ and damping $b$ which control the reference acceleration $\ar$.

> [!note] Intuitive description of the reference acceleration
> The *reference acceleration* $\ar$ determines the **motion that constraint is trying to achieve** in order to rectify violation. Imagine a body dropped onto the plane. Upon impact the constraint will generate a normal force which attempts to rectify the penetration using a particular motion; this motion is the reference acceleration.
> 
> Another way of understanding the reference acceleration is to think of the unmodeled deformation variables described in the [Computation chapter](https://mujoco.readthedocs.io/en/stable/computation/index.html#soprimal). Imagine two bodies pressed together, leading to deformation at the contact. Now pull the bodies apart very quickly; the motion of the deformation as it settles into its undeformed state is the reference acceleration.
> 
> This acceleration is defined by two numbers, a stiffness $k$ and damping $b$ which can be set directly or re-parameterized as the time-constant and damping ratio of a mass-spring-damper system (a [harmonic oscillator](https://en.wikipedia.org/wiki/Harmonic_oscillator)). The reference acceleration is controlled by the solref attribute.

There are two formats for this attribute, determined by the sign of the numbers. If both numbers are positive the specification is considered to be in the $(\text{timeconst}, \text{dampratio})$ format. If negative it is in the “direct” $(-\text{stiffness}, -\text{damping})$ format.

For frictional constraints, the mass-spring-damper analysis below does not directly apply; see.

**solref:** real(2), “0.02 1”

We first describe the default, positive-value format where the two numbers are $(\text{timeconst}, \text{dampratio})$.

The idea here is to re-parameterize the model in terms of the time constant and damping ratio of a mass-spring-damper system. By “time constant” we mean the inverse of the natural frequency times the damping ratio. Now recall that the products $d \cdot k$ and $d \cdot b$ in [^1] are the effective stiffness and damping in constraint space. Because the impedance $d(r)$ varies with the position residual $r$, we cannot achieve constant mass-spring-damper properties; completely undoing the scaling by $d$ is undesirable because the limit $d = 0$ would no longer disable the constraint. Instead, we absorb one factor of $d(r)$ into $k$ (but not into $b$), so that the damping ratio remains constant while the time constant scales with $d(r)$. The formulas are

(2) [#](#equation-eq-solref-standard "Permalink to this equation") $\begin{aligned}
b &= 2 / (d_\mathrm{w}\cdot \text{timeconst}) \\
k &= d(r) / (d_\mathrm{w}^2 \cdot \text{timeconst}^2 \cdot \text{dampratio}^2) \\
\end{aligned}$

The timeconst parameter should be at least two times larger than the simulation time step, otherwise the system can become too stiff relative to the numerical integrator (especially when Euler integration is used) and the simulation can go unstable. This is enforced internally, unless the [refsafe](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-refsafe) attribute of [flag](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag) is set to false. The $\text{dampratio}$ parameter would normally be set to 1, corresponding to critical damping. Smaller values result in under-damped or bouncy constraints, while larger values result in over-damped constraints. Combining [^2] with [^1], we can derive the following If the reference acceleration is given using the positive number format and the impedance is constant $d = d_0 = d_\mathrm{w}$, then the penetration depth at rest is

$$
r = \au \cdot (1 - d) \cdot \text{timeconst}^2 \cdot \text{dampratio}^2
$$

Next we describe the direct format where the two numbers are $(-\text{stiffness}, -\text{damping})$. This allows direct control over restitution in particular. We still apply some scaling so that the same numbers can be used with different impedances, but the scaling no longer depends on $r$ and the two numbers no longer interact. The scaling formulas are

(3) [#](#equation-eq-solref-direct "Permalink to this equation") $\begin{aligned}
b &= \text{damping} / d_\mathrm{w} \\
k &= \text{stiffness} \cdot d(r) / d_\mathrm{w}^2 \\
\end{aligned}$

Similarly to the derivation following [^2], if the reference acceleration is given using the impedance is constant, then the penetration depth at rest is

$$
r = \frac{\au (1 - d)}{\text{stiffness}}
$$

> [!tip] Tip
> In the positive-value default format, the $\text{timeconst}$ parameter controls constraint **softness**. It is specified in units of time and means “how quickly is the constraint trying to resolve the violation”. Larger values correspond to softer constraints.
> 
> The negative-value “direct” format is more flexible, for example allowing for perfectly elastic collisions ($\text{damping} = 0$). It is the recommended format for system identification.
> 
> A $\text{dampratio}$ of 1 in the positive-value format is equivalent to $\text{damping} = 2 \sqrt{ \text{stiffness} }$ in the direct format.

#### Friction

Friction loss constraints (in joints and tendons) and friction dimensions of elliptic contact cones have zero position violation: $r \equiv 0$. This simplifies the constraint model (see also [Parameters](https://mujoco.readthedocs.io/en/stable/computation/index.html#soparameters)):

- The **impedance** is always $d_0$ (solimp\[0\]), since $d(r)$ is evaluated at $r=0$. The sigmoid shape parameters ($\text{width}$, $\text{midpoint}$, $\text{power}$) have no effect.
- The dynamics are **first-order** (exponential decay of constraint velocity, no spring): the stiffness $k$ is always 0.
- In the standard solref format, the time constant controls exponential velocity decay. The damping ratio is ignored (it only appears in the $k$ formula).
- In the direct solref format, the damping (second value) is used but the stiffness (first value) is ignored.
- $d_\mathrm{w}$ (solimp\[1\]) still affects the damping $b$ as a scaling denominator ([^2], [^3]), even though it does not affect the impedance.

See for the implications of this model for exact sticking and practical guidance.

### User parameters

A number of MJCF elements have the optional attribute user, which defines a custom element-specific parameter array. This interacts with the corresponding “nuser\_XXX” attribute of the [size](https://mujoco.readthedocs.io/en/stable/XMLreference.html#size) element. If for example we set nuser\_geom to 5, then every geom in mjModel will have a custom array of 5 real-valued parameters. These geom- specific parameters are either defined in the MJCF file via the user attribute of [geom](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom), or set to 0 by the compiler if this attribute is omitted. The default value of all “nuser\_XXX” attributes is -1, which instructs the compiler to automatically set this value to the length of the maximum associated user attribute defined in the model. MuJoCo does not use these parameters in any internal computations; instead they are available for custom computations. The parser allows arrays of arbitrary length in the XML, and the compiler later resizes them to length nuser\_XXX.

Some element-specific parameters that are normally used in internal computations can also be used in custom computations. This is done by installing user callbacks which override parts of the simulation pipeline. For example, the [general](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general) actuator element has attributes dyntype and dynprm. If dyntype is set to “user”, then MuJoCo will call [mjcb\_act\_dyn](https://mujoco.readthedocs.io/en/stable/APIreference/APIglobals.html#mjcb-act-dyn) to compute the actuator dynamics instead of calling its internal function. The user function pointed to by [mjcb\_act\_dyn](https://mujoco.readthedocs.io/en/stable/APIreference/APIglobals.html#mjcb-act-dyn) can interpret the parameters defined in dynprm however it wishes. However the length of this parameter array cannot be changed (unlike the custom arrays described earlier whose length is defined in the MJCF file). The same applies to other callbacks.

In addition to the element-specific user parameters described above, one can include global data in the model via [custom](https://mujoco.readthedocs.io/en/stable/XMLreference.html#custom) elements. For data that change in the course of the simulation, there is also the array mjData.userdata whose size is determined by the nuserdata attribute of the [size](https://mujoco.readthedocs.io/en/stable/XMLreference.html#size) element.

### Solver settings

The computation of constraint forces and constrained accelerations involves solving an optimization problem numerically. MuJoCo has three algorithms for solving this optimization problem: Newton, CG, PGS. Each of them can be applied to a pyramidal or elliptic model of the friction cones, and with dense or sparse constraint Jacobians. In addition, the user can specify the maximum number of iterations, and tolerance level which controls early termination. There is also a NoSlip solver, which is a post-processing step enabled by specifying a positive number of NoSlip iterations. All these algorithm settings can be specified in the [option](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option) element.

The default settings work well for most models, but in some cases it is necessary to tune the algorithm. The best way to do this is to experiment with the relevant settings and use the visual profiler in [simulate.cc](https://mujoco.readthedocs.io/en/stable/programming/samples.html#sasimulate), which shows the timing of different computations as well as solver statistics per iteration. We can offer the following general guidelines and observations:

- The constraint Jacobian should be dense for small models and sparse for large models. The default setting is ‘auto’; it resolves to dense when the number of degrees of freedom is up to 60, and sparse over 60. Note however that the threshold is better defined in terms of number of active constraints, which is model and behavior dependent.
- The choice between pyramidal and elliptic friction cones is a modeling choice rather than an algorithmic choice, i.e., it leads to a different optimization problem solved with the same algorithms. Elliptic cones correspond more closely to physical reality. However pyramidal cones can improve the performance of the algorithms – but not necessarily. While the default is pyramidal, we recommend trying the elliptic cones. When contact slip is a problem, the best way to suppress it is to use elliptic cones, large impratio, and the Newton algorithm with very small tolerance. If that is not sufficient, enable the Noslip solver.
- The Newton algorithm is the best choice for most models. It has quadratic convergence near the global minimum and gets there in surprisingly few iterations – usually around 5, and rarely more than 20. It should be used with aggressive tolerance values, say 1e-10, because it is capable of achieving high accuracy without added delay (due to quadratic convergence at the end). Sparse Newton folds elliptic friction cones into the Hessian, batches Cholesky updates, and automatically reorders flex DOFs, so slowdowns mainly occur in very large scenes where sparse Cholesky fill-in still dominates (for instance, un-reordered rigid hub bodies; see below) or under heavy active-set churn across many slipping contacts. Note that the number of non-zeros in the factorized Hessian can be monitored in the profiler.
- The CG algorithm can be faster in those very large or high-fill-in regimes. In general CG shows linear convergence with a good rate, though it requires many more iterations than Newton, especially when high accuracy is desired. However each iteration is cheap and unaffected by Cholesky fill-in or elliptic-cone Hessian updates, making CG a useful alternative when Hessian factorization dominates step time.
- The PGS solver is best when the number of degrees of freedom is larger than the number of constraints. PGS solves a constrained optimization problem and has sub-linear convergence in our experience, however it usually makes rapid progress on the first few iterations. So it is a good choice when inaccurate solutions can be tolerated. For systems with large mass ratios or other model properties causing poor conditioning, PGS convergence tends to be rather slow. Keep in mind that PGS performs sequential updates, and therefore breaks symmetry in systems where the physics should be symmetric. In contrast, CG and Newton perform parallel updates and preserve symmetry.
- The NoSlip solver is a modified PGS solver. It is executed as a post-processing step after the main solver (which can be Newton, CG or PGS). The main solver updates all unknowns. In contrast, the NoSlip solver updates only the constraint forces in friction dimensions, and ignores constraint regularization. This has the effect of suppressing the drift or slip caused by the soft-constraint model. However, this cascade of optimization steps is no longer solving a well-defined optimization problem (or any other problem); instead it is just an adhoc mechanism. While it usually does its job, we have seen some instabilities in models with more complex interactions among multiple contacts.
- PGS has a setup cost (in terms of CPU time) for computing the inverse inertia in constraint space. Similarly, Newton has a setup cost for the initial factorization of the Hessian, and incurs additional factorization costs depending on how many factorization updates are needed later. CG does not have any setup cost. Since the NoSlip solver is also a PGS solver, the PGS setup cost will be paid whenever NoSlip is enabled, even if the main solver is CG or Newton. The setup operation for the main PGS and NoSlip PGS is the same, thus the setup cost is paid only once when both are enabled.

#### Body ordering and fill-in

> [!tip] Tip
> Declare moving bodies with many contacts *before* the objects they interact with in worldbody, so they receive lower DOF indices and avoid dense Cholesky fill-in.

In sparse mode, the Newton solver factorizes the Hessian $H = \widehat{M} + J^T D J$ using reverse-order Cholesky, eliminating degrees of freedom from last to first ($\nv - 1$ down to $0$, i.e., from leaves to root). For the tree-structured matrix $\widehat{M}$ alone, this elimination order is [optimal and produces zero fill-in](https://link.springer.com/book/10.1007/978-1-4899-7560-7). Contacts, tendons, and equality constraints add off-tree couplings in $J^T D J$: when DOF $r$ is eliminated, it creates fill-in between **all lower-indexed DOFs** ($c < r$) currently coupled to $r$, forming a dense clique among them.

Consequently, the declaration order of bodies in worldbody can strongly affect solver speed without changing the physics. A moving “hub” body that simultaneously contacts many other bodies – such as an actuated tray, sieve, container, or platform – should be declared *before* the objects resting on or inside it. If a moving tray is declared first (low DOFs) and $N$ free bodies are declared after it (high DOFs), the free bodies are eliminated first and only fill into the tray’s DOFs, giving an arrowhead sparsity pattern with zero fill-in and $O(N)$ factorization cost. If the tray is declared *last*, it is eliminated first and couples all $N$ bodies into a single dense block with $O(N^3)$ cost. Static geoms attached directly to worldbody or to welded bodies have no DOFs and are unaffected by ordering. When a model contains flex elements, sparse `Newton` automatically computes a minimum-degree DOF permutation whenever it lowers factorization cost enough to amortize the reordering overhead, so manual XML ordering of flex bodies or vertices is unnecessary.

### Actuators

This section describes various aspects of using actuators in MuJoCo. See the [Actuation model](https://mujoco.readthedocs.io/en/stable/computation/index.html#geactuation) regarding the computational model.

#### Group disable

The [actuatorgroupdisable](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-actuatorgroupdisable) attribute, which can be changed at runtime by setting the [mjOption.disableactuator](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjoption) integer bitfield, allows the user to disable sets of actuators according to their [group](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-group). This feature is convenient when one would like to use multiple types of actuators for the same kinematic tree. For example consider a robot with firmware that supports multiple control modes e.g., torque-control and position-control. In this case, one can define both types of actuators in the same MJCF model, assigning one type of actuator to group 0 and the other to group 1.

![](https://www.youtube.com/watch?v=H9qG9Zf2W44)

The [actuatorgroupdisable](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-actuatorgroupdisable) MJCF attribute selects which groups are disabled by default, and [mjOption.disableactuator](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjoption) can be set at runtime to switch the active set. Note that the total number of actuators `mjModel.nu` remains unchanged, as do the actuator indices, so it is up to the user to know that the respective `mjData.ctrl` values of disabled actuators will be ignored and produce no force. [This example model](https://github.com/google-deepmind/mujoco/blob/main/test/engine/testdata/actuation/actuator_group_disable.xml) has three actuator groups which can be toggled at runtime in the [simulate](https://mujoco.readthedocs.io/en/stable/programming/samples.html#sasimulate) interactive viewer. See [example model](https://github.com/google-deepmind/mujoco/blob/main/test/engine/testdata/actuation/actuator_group_disable.xml) and associated screen-capture on the right.

#### Shortcuts

As explained in the [Actuation model](https://mujoco.readthedocs.io/en/stable/computation/index.html#geactuation) section of the Computation chapter, MuJoCo offers a flexible actuator model with transmission, activation dynamics and force generation components that can be specified independently. The full functionality can be accessed via the XML element [general](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general) which allows the user to create a variety of custom actuators. In addition, MJCF provides shortcuts for configuring common actuators. This is done via the XML elements [motor](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-motor), [position](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-position), [velocity](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-velocity), [intvelocity](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-intvelocity), [orientation](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-orientation), [pid](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-pid), [damper](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-damper), [cylinder](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-cylinder), [muscle](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-muscle), [adhesion](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-adhesion), and [dcmotor](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-dcmotor). These are *not* separate model elements. Internally MuJoCo supports only one actuator type. Shortcuts create general actuators implicitly, set their attributes to suitable values, and expose a subset of attributes with possibly different names. When a model is saved in the notation it was written in, an actuator is written with its shortcut if reading the shortcut back gives the same actuator, and as general otherwise; in the canonical notation every actuator is general. For example, position creates a position servo with attribute kp which is the servo gain. However general does not have an attribute kp. Instead the parser adjusts the gain and bias parameters of the general actuator in a coordinated way so as to mimic a position servo. The same effect could have been achieved by using general directly, and setting its attributes to certain values as described below.

Actuator shortcuts also interact with defaults. Recall that the mechanism involves classes, each of which has a complete collection of dummy elements (one of each element type) used to initialize the attributes of the actual model elements. In particular, each defaults class has a single actuator default, written with general or with one of the shortcuts. An actuator inherits all of its class’s actuator defaults, including mechanical attributes like ctrlrange and gear. Shortcut parameters (kp, kv, area, …) are inherited from a default written with the same shortcut, or from a general default with the shortcut’s gain type, whose raw gain and bias parameters are read as the shortcut’s; they are not inherited from a default written with another shortcut. In that case the nearest ancestor class whose default the shortcut can inherit from is used, and if there is none, the shortcut’s own documented defaults apply. So a motor in a class whose default is position is a plain motor with the class’s ctrlrange, not a position servo; a position in a class whose default is general with gainprm “400” has kp 400; and a position in a child class whose default is velocity has the kp of the parent class’s position default. general itself inherits the raw gain, bias and dynamics parameters of any default, so a general which omits these attributes in a class with a position default is a position servo. If several actuator elements are given in one class they are processed in order: each shortcut resets the gain, bias and dynamics parameters and the activation layout, while general sets only the attributes given explicitly.

#### Force limits

Actuator forces are usually limited between lower and upper bounds. These limits can be enforced in three ways:

Control clamping with [ctrlrange](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-ctrlrange):

If this actuator attribute is set, the input control value will be clamped. For simple [motors](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-motor), clamping the control input is equivalent to clamping the force output.

Force clamping at actuator output with [forcerange](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-forcerange):

If this actuator attribute is set, the actuator’s output force will be clamped. This attribute is useful for e.g. [position actuators](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-position), to keep the forces within bounds. Note that position actuators usually also require control range clamping to avoid hitting joint limits.

Force clamping at joint input with [joint/actuatorfrcrange](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint-actuatorfrcrange):

This joint attribute clamps the total force from all actuators acting on the joint, after passing through the [transmission](https://mujoco.readthedocs.io/en/stable/computation/index.html#getransmission). It dates from when every actuator had a single input, so that modeling one physical actuator with several commands (e.g., a position servo plus a velocity servo, or a motor plus velocity feedback) required stacking actuators on the joint and clamping their sum. Prefer a single multi-input actuator instead: a [pid](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-pid) or [dcmotor](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-dcmotor) with the required subset of `pos`, `vel` and `ff` [inputs](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-pid-input), its output bounded by [forcerange](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-forcerange). This keeps the limit on the actuator that produces the force, and the [actuatorfrc](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-actuatorfrc) sensor reports the force actually applied.

Joint clamping remains useful when the transmission combines actuator forces across joints, yet each joint is driven by a single torque-limited motor:

- In [this example model](https://github.com/google-deepmind/mujoco/blob/main/model/car/car.xml) (similar to a “Dubin’s Car”), two actuators act on two wheels via a [fixed tendon](https://mujoco.readthedocs.io/en/stable/XMLreference.html#tendon-fixed) transmission in order to apply symmetric (roll forward/back) and antisymmetric (turn right/left) torques.
- In [this example model](https://github.com/google-deepmind/mujoco/tree/main/test/engine/testdata/actuation/refsite.xml), a [site transmission](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-refsite) implements a Cartesian controller of an arm end-effector. In order for the computed torques to be realisable by individual, torque-limited joint motors, they need to be clamped at the joints.

Note that in this case, where forces/torques are combined by the transmission, one should use the [jointactuatorfrc](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-jointactuatorfrc) sensor to report the total actuator force acting on a joint. The standard [actuatorfrc](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-actuatorfrc) sensor will continue to report the pre-clamped actuator force.

Force clamping at tendon input with [tendon/actuatorfrcrange](https://mujoco.readthedocs.io/en/stable/XMLreference.html#tendon-spatial-actuatorfrcrange):

This tendon attribute clamps input forces from all actuators acting on the tendon. The same considerations as for joints apply: prefer a single multi-input actuator over clamping the sum of several.

The clamping options above are non-exclusive and can be combined as required. A saturated forcerange or tendon actuatorfrcrange contributes no implicit damping, since the clamped force does not depend on velocity.

#### Length range

The field `mjModel.actuator_lengthrange` contains the range of feasible actuator lengths (or more precisely, lengths of the actuator’s transmission). This is needed to simulate. Here we focus on what actuator\_lengthrange means and how to set it.

Unlike all other fields of mjModel which are exact physical or geometric quantities, actuator\_lengthrange is an approximation. Intuitively it corresponds to the minimum and maximum length that the actuator’s transmission can reach over all “feasible” configurations of the model. However MuJoCo constraints are soft, so in principle any configuration is feasible. Yet we need a well-defined range for muscle modeling. There are three ways to set this range: (1) provide it explicitly using the attribute lengthrange available in all actuators; (2) copy it from the limits of the joint or tendon to which the actuator is attached; (3) compute it automatically, as explained in the rest of this section. There are many options here, controlled with the XML element [lengthrange](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-lengthrange).

Automatic computation of actuator length ranges is done at compile time, and the results are stored in mjModel.actuator\_lengthrange of the compiled model. If the model is then saved as MJB, or as XML with the values which compilation made ([savecompiled](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-savecompiled)), the computation does not need to be repeated at the next load; saved as it is written, the model keeps the settings which compute the ranges, and computes them again. This is important because the computation can slow down the model compiler with large musculo-skeletal models. Indeed we have made the compiler multi-threaded just to speed up this operation (different actuators are processed in parallel in different threads).

Automatic computation relies on modified physics simulation. For each actuator we apply force (negative when computing the minimum, positive when computing the maximum) through the actuator’s transmission, advance the simulation in a damped regime avoiding instabilities, give it enough time to settle and record the result. This is related to gradient descent with momentum, and indeed we have experimented with explicit gradient-based optimization, but the problem is that it is not clear what objective we should be optimizing (given the mix of soft constraints). By using simulation, we are essentially letting the physics tell us what to optimize. Keep in mind though that this is still an optimization process, and as such it has parameters that may need to be adjusted. We provide conservative defaults which should work with most models, but if they don’t, use the attributes of [lengthrange](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-lengthrange) for fine-tuning.

It is important to keep in mind the geometry of the model when using this feature. The implicit assumption here is that feasible actuator lengths are indeed limited. Furthermore we do not consider contacts as limiting factors (in fact we disable contacts internally in this simulation, together with passive forces, gravity, friction loss and actuator forces). This is because models with contacts can tangle up and produce many local minima. So the actuator should be limited either because of joint or tendon limits defined in the model (which are enabled during this simulation) or due to geometry. To illustrate the latter, consider a tendon with one end attached to the world and the other end attached to an object spinning around a hinge joint attached to the world. In this case the minimum and maximum length of the tendon are well-defined and depend on the size of the circle that the attachment point traces in space, even though neither the joint nor the tendon have limits defined by the user. But if the actuator is attached to the joint, or to a fixed tendon equal to the joint, then it is unlimited. The compiler will return an error in this case, but it cannot tell if the error is due to lack of convergence or because the actuator length is unlimited. All of this sounds overly complicated, and it is in the sense that we are considering all possible corner cases here. In practice length ranges will almost always be used with muscle actuators attached to spatial tendons, and there will be joint limits defined in the model, effectively limiting the lengths of the muscle actuators. If you get a convergence error in such a model, the most likely explanation is that you forgot to include joint limits.

#### Stateful actuators

As described in the [Actuation model](https://mujoco.readthedocs.io/en/stable/computation/index.html#geactuation) section of the Computation chapter, MuJoCo supports actuators with internal dynamics whose states are called “activations”.

##### Activation limits

One useful application of stateful actuators is the “integrated-velocity” actuator, implemented by the [intvelocity](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-intvelocity) shortcut. Different from the [pure velocity](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-velocity) actuators, which implement direct feedback on transmission target’s velocity, *integrated-velocity* actuators couple an *integrator* with a *position-feedback* actuator. In this case the semantics of the activation state are “the setpoint of the position actuator”, and the semantics of the control signal are “the velocity of the setpoint of the position actuator”. Note that in real robotic systems this integrated-velocity actuator is the most common implementation of actuators with velocity semantics, rather than pure feedback on velocity which is often quite unstable (both in real life and in simulation).

In the case of integrated-velocity actuators, it is often desirable to *clamp* the activation state, since otherwise the position target would keep integrating beyond the joint limits, leading to loss of controllabillity. (On purely rotational transmissions, the setpoint wraps on the circle and stays bounded without clamping; see [gear](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-gear).) To see the effect of activation clamping, load the example model below:

Example model with activation limits

```xml
<mujoco>
<default>
   <joint axis="0 0 1" limited="true" range="-90 90" damping="0.3"/>
   <geom size=".1 .1 .1" type="box"/>
</default>

<worldbody>
   <body>
      <joint name="joint1"/>
      <geom/>
   </body>
   <body pos=".3 0 0">
      <joint name="joint2"/>
      <geom/>
   </body>
</worldbody>

<actuator>
   <intvelocity name="unclamped" joint="joint1"/>
   <intvelocity name="clamped" joint="joint2" actrange="-1.57 1.57"/>
</actuator>
</mujoco>
```

Note that the actrange attribute is always specified in native units (radians), even though the joint range can be either in degrees (the default) or radians, depending on the [compiler/angle](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler) attribute.

##### Muscles

We provide a set of tools for modeling biological muscles. Users who want to add muscles with minimum effort can do so with a single line of XML in the actuator section:

```xml
<actuator>
    <muscle name="mymuscle" tendon="mytendon">
</actuator>
```

Biological muscles look very different from each other, yet behave in remarkably similar ways once certain scaling is applied. Our default settings apply such scaling, which is why one can obtain a reasonable muscle model without adjusting any parameters. Constructing a more detailed model will of course require parameter adjustment, as explained in this section.

Keep in mind that even though the muscle model is quite elaborate, it is still a type of MuJoCo actuator and obeys the same conventions as all other actuators. A muscle can be defined using [general](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general), but the shortcut [muscle](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-muscle) is more convenient. As with all other actuators, the force production mechanism and the transmission are defined independently. Nevertheless, muscles only make (bio)physical sense when attached to tendon or joint transmissions. For concreteness we will assume a tendon transmission here.

First we discuss length and length scaling. The range of feasible lengths of the transmission (i.e., MuJoCo tendon) will play an important role; see section above. In biomechanics, a muscle and a tendon are attached in series and form a muscle-tendon actuator. Our convention is somewhat different: in MuJoCo the entity that has spatial properties (in particular length and velocity) is the tendon, while the muscle is an abstract force- generating mechanism that pulls on the tendon. Thus the tendon length in MuJoCo corresponds to the muscle+tendon length in biomechanics. We assume that the biological tendon is inelastic, with constant length $L_T$, while the biological muscle length $L_M$ varies over time. The MuJoCo tendon length is the sum of the biological muscle and tendon lengths:

$$
\texttt{actuator\_length} = L_T + L_M
$$

Another important constant is the optimal resting length of the muscle, denoted $L_0$. It equals the length $L_M$ at which the muscle generates maximum active force at zero velocity. We do not ask the user to specify $L_0$ and $L_T$ directly, because it is difficult to know their numeric values given the spatial complexity of the tendon routing and wrapping. Instead we compute $L_0$ and $L_T$ automatically as follows. The length range computation described above already provided the operating range for $L_T+L_M$. In addition, we ask the user to specify the operating range for the muscle length $L_M$ scaled by the (still unknown) constant $L_0$. This is done with the attribute range; the default scaled range is $(0.75, 1.05)$. Now we can compute the two constants, using the fact that the actual and scaled ranges have to map to each other:

$$
\begin{aligned}
(\texttt{actuator\_lengthrange[0]} - L_T) / L_0 &= \texttt{range[0]} \\
(\texttt{actuator\_lengthrange[1]} - L_T) / L_0 &= \texttt{range[1]} \\
\end{aligned}
$$

At runtime, we compute the scaled muscle length and velocity as:

$$
\begin{aligned}
L &= (\texttt{actuator\_length} - L_T) / L_0 \\
V &= \texttt{actuator\_velocity} / L_0 \\
\end{aligned}
$$

The advantage of the scaled quantities is that all muscles behave similarly in that representation. The behavior is captured by the Force-Length-Velocity ($\text{\small FLV}$) function measured in many experimental papers. We approximate this function as follows:

 [![_images/musclemodel.png](https://mujoco.readthedocs.io/en/stable/_images/musclemodel.png)](https://mujoco.readthedocs.io/en/stable/_images/musclemodel.png)[![_images/musclemodel_dark.png](https://mujoco.readthedocs.io/en/stable/_images/musclemodel_dark.png)](https://mujoco.readthedocs.io/en/stable/_images/musclemodel_dark.png)

The function is in the form:

$$
\text{\small FLV}(L, V, \texttt{act}) = F_L(L)\cdot F_V(V)\cdot \texttt{act} + F_P(L)
$$

Comparing to the general form of a MuJoCo actuator, we see that $F_L\cdot F_V$ is the actuator gain and $F_P$ is the actuator bias. $F_L$ is the active force as a function of length, while $F_V$ is the active force as a function of velocity. They are multiplied to obtain the overall active force (note the scaling by act which is the actuator activation). $F_P$ is the passive force which is always present regardless of activation. The output of the $\text{\small FLV}$ function is the scaled muscle force. We multiply the scaled force by a muscle-specific constant $F_0$ to obtain the actual force:

$$
\texttt{actuator\_force} = -\text{\small FLV}(L, V, \texttt{act}) \cdot F_0
$$

The negative sign is because positive muscle activation generates pulling force. The constant $F_0$ is the peak active force at zero velocity. It is related to the muscle thickness (i.e., physiological cross-sectional area or PCSA). If known, it can be set with the attribute force of element [muscle](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-muscle). If it is not known, we set it to $-1$ which is the default. In that case we rely on the fact that larger muscles tend to act on joints that move more weight. The attribute scale defines this relationship as:

$$
F_0 = \text{scale} / \texttt{actuator\_acc0}
$$

The quantity $\texttt{actuator\_acc0}$ is precomputed by the model compiler. It is the norm of the joint acceleration caused by unit force acting on the actuator transmission. Intuitively, $\text{scale}$ determines how strong the muscle is “on average” while its actual strength depends on the geometric and inertial properties of the entire model.

Thus far we encountered three constants that define the properties of an individual muscle: $L_T, L_0, F_0$. In addition, the function $\text{\small FLV}$ itself has several parameters illustrated in the above figure: $l_\text{min}, l_\text{max}, v_\text{max}, f_\text{pmax}, f_\text{vmax}$. These are supposed to be the same for all muscles, however different experimental papers suggest different shapes of the FLV function, thus users familiar with that literature may want to adjust them. We provide the MATLAB function [FLV.m](https://mujoco.readthedocs.io/en/stable/_static/FLV.m) which was used to generate the above figure and shows how we compute the $\text{\small FLV}$ function.

Before embarking on a mission to design more accurate $\text{\small FLV}$ functions, consider the fact that the operating range of the muscle has a bigger effect than the shape of the $\text{\small FLV}$ function, and in many cases this parameter is unknown. Below is a graphical illustration:

 [![_images/musclerange.png](https://mujoco.readthedocs.io/en/stable/_images/musclerange.png)](https://mujoco.readthedocs.io/en/stable/_images/musclerange.png)[![_images/musclerange_dark.png](https://mujoco.readthedocs.io/en/stable/_images/musclerange_dark.png)](https://mujoco.readthedocs.io/en/stable/_images/musclerange_dark.png)

This figure format is common in the biomechanics literature, showing the operating range of each muscle superimposed on the normalized $\text{FL}$ curve (ignore the vertical displacement). Our default range is shown in black. The blue curves are experimental data for two arm muscles. One can find muscles with small range, large range, range spanning the ascending portion of the $\text{FL}$ curve, or the descending portion, or some of both. Now suppose you have a model with 50 muscles. Do you believe that someone did careful experiments and measured the operating range for every muscle in your model, taking into account all the joints that the muscle spans? If not, then it is better to think of musculo-skeletal models as having the same general behavior as the biological system, while being different in various details – including details that are of great interest to some research community. For most muscle properties which modelers consider constant and known, there is an experimental paper showing that they vary under some conditions. This is not to discourage people from building accurate models, but rather to discourage people from believing too strongly in their models.

Coming back to our muscle model, there is the muscle activation `act`. This is the state of a first-order nonlinear filter whose input is the control signal. The filter dynamics are:

$$
\frac{\partial}{\partial t}\texttt{act} = \frac{\texttt{ctrl} - \texttt{act}}{\tau(\texttt{ctrl}, \texttt{act})}
$$

Internally the control signal is clamped to \[0, 1\] even if the actuator does not have a control range specified. There are two time constants specified with the attribute timeconst, namely $\text{timeconst} = (\tau_\text{act},
\tau_\text{deact})$ with defaults $(0.01, 0.04)$. Following [Millard et al. (2013)](https://doi.org/10.1115/1.4023390), the effective time constant $\tau$ is then computed at runtime as:

$$
\tau(\texttt{ctrl}, \texttt{act}) =
\begin{cases}
   \tau_\text{act} \cdot (0.5 + 1.5\cdot\texttt{act}) & \texttt{ctrl}-\texttt{act} \gt 0 \\
   \tau_\text{deact} / (0.5 + 1.5\cdot\texttt{act}) & \texttt{ctrl} - \texttt{act} \leq 0
\end{cases}
$$

Since the above equation describes discontinuous switching, which can be undesirable when using derivative-based optimization, we introduce the optional smoothing parameter [tausmooth](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-muscle-tausmooth). When greater than 0, the switching is replaced by [mju\_sigmoid](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-sigmoid), which will smoothly interpolate between the two values within the range $(\texttt{ctrl}-\texttt{act}) \pm \text{tausmooth}/2$.

Now we summarize the attributes of element [muscle](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-muscle) which users may want to adjust, depending on their familiarity with the biomechanics literature and availability of detailed measurements with regard to a particular model:

Defaults

Use the built-in defaults everywhere. All you have to do is attach a muscle to a tendon, as shown at the beginning of this section. This yields a generic yet reasonable model.

scale

If you do not know the strength of individual muscles but want to make all muscles stronger or weaker, adjust scale. This can be adjusted separately for each muscle, but it makes more sense to set it once in the [default](https://mujoco.readthedocs.io/en/stable/XMLreference.html#default) element.

force

If you know the peak active force $F_0$ of the individual muscles, enter it here. Many experimental papers contain this data.

range

The operating range of the muscle in scaled lengths is also available in some papers. It is not clear how reliable such measurements are (given that muscles act on many joints) but they do exist. Note that the range differs substantially between muscles.

timeconst

Muscles are composed of slow-twitch and fast-twitch fibers. The typical muscle is mixed, but some muscles have a higher proportion of one or the other fiber type, making them faster or slower. This can be modeled by adjusting the time constants. The vmax parameter of the $\text{\small FLV}$ function should also be adjusted accordingly.

tausmooth

When positive, smooths the transition between activation and de-activation time-constants. While a single [motor unit](https://en.wikipedia.org/wiki/Motor_unit) is either activating or de-activating, an entire muscle will have a mixture of many units, leading to a corresponding mixture of timescales.

lmin, lmax, vmax, fpmax, fvmax

These are the parameters controlling the shape of the $\text{\small FLV}$ function. Advanced users can experiment with them; see MATLAB function [FLV.m](https://mujoco.readthedocs.io/en/stable/_static/FLV.m). Similar to the scale setting, if you want to change the $\text{\small FLV}$ parameters for all muscles, do so in the [default](https://mujoco.readthedocs.io/en/stable/XMLreference.html#default) element.

Custom model

Instead of adjusting the parameters of our muscle model, users can implement a different model, by setting gaintype, biastype and dyntype of a [general](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general) actuator to “user” and providing callbacks at runtime. Or, leave some of these types set to “muscle” and use our model, while replacing the other components. Note that tendon geometry computations are still handled by the standard MuJoCo pipeline providing actuator\_length, actuator\_velocity and actuator\_lengthrange as inputs to the user’s muscle model. Custom callbacks could then simulate elastic tendons or any other detail we have chosen to omit.

**Relation to OpenSim**

The standard software used by researchers in biomechanics is OpenSim. We have designed our muscle model to be similar to the OpenSim model where possible, while making simplifications which result in significantly faster and more stable simulations. To help MuJoCo users convert OpenSim models, here we summarize the similarities and differences.

The activation dynamics model is identical to OpenSim, including the default time constants.

The $\text{\small FLV}$ function is not exactly the same, but both MuJoCo and OpenSim approximate the same experimental data, so they are very close. For a description of the OpenSim model and summary of relevant experimental data, see [Millard et al. (2013)](https://doi.org/10.1115/1.4023390).

We assume inelastic tendons while OpenSim can model tendon elasticity. We decided not to do that here, because tendon elasticity requires fast-equilibrium assumptions which in turn require various tweaks and are prone to simulation instability. In practice tendons are quite stiff, and their effect can be captured approximately by stretching the $\text{FL}$ curve corresponding to the inelastic case ([Zajac (1989)](https://pubmed.ncbi.nlm.nih.gov/2676342/)). This can be done in MuJoCo by shortening the muscle operating range.

Pennation angle (i.e., the angle between the muscle and the line of force) is not modeled in MuJoCo and is assumed to be 0. This effect can be approximated by scaling down the muscle force and also adjusting the operating range.

Tendon wrapping is also more limited in MuJoCo. We allow spheres and infinite cylinders as wrapping objects, and require two wrapping objects to be separated by a fixed site in the tendon path. This is to avoid the need for iterative computations of tendon paths. We also allow “side sites” to be placed inside the sphere or cylinder, which causes an inverse wrap: the tendon path is constrained to pass through the object instead of going around it. This can replace torus wrapping objects used in OpenSim to keep the tendon path within a given area. Overall, tendon wrapping is the most challenging part of converting an OpenSim model to a MuJoCo model, and requires some manual work. On the bright side, there is a small number of high-quality OpenSim models in use, so once they are converted we are done.

Below we illustrate the four types of tendon wrapping available, for which the geometry pipeline computes the curved paths, lengths, and moments analytically:

[![image3](https://mujoco.readthedocs.io/en/stable/_images/tendonwraps.png)](https://mujoco.readthedocs.io/en/stable/_images/tendonwraps.png)

### Sensors

MuJoCo can simulate a wide variety of sensors as described in the [sensor](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor) element below. User sensor types can also be defined, and are evaluated by the callback [mjcb\_sensor](https://mujoco.readthedocs.io/en/stable/APIreference/APIglobals.html#mjcb-sensor). Sensors do not affect the simulation. Instead their outputs are copied in the array mjData.sensordata and are available for user processing.

Here we describe the XML attributes common to all sensor types, so as to avoid repetition later.

name: string, optional

Name of the sensor.

noise: real, “0”

The standard deviation of the noise model of this sensor. This attribute does not affect the simulation; it serves as a convenient location for storing standard deviation information for later use.

cutoff: real, “0”

When this value is positive, it limits the absolute value of the sensor output. It is also used to normalize the sensor data plots in [simulate.cc](https://mujoco.readthedocs.io/en/stable/programming/samples.html#sasimulate). Note that cutoff has a different meaning for [collision sensors](https://mujoco.readthedocs.io/en/stable/XMLreference.html#collision-sensors).

nsample: int, “0”

If nsample is greater than 0, creates a time-indexed ring buffer with nsample slots of sensor data. During state advancement, the current sensor data is appended to the buffer with timestamp `time`, and the oldest sample is removed. Values in the history buffer can be read via [mj\_readSensor](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-readsensor). A positive nsample is required for both and features.

See for details.

interp: \[zoh, linear, cubic\], “zoh”

The interpolation method used when reading from the history buffer. Corresponds to the `interp` argument in [mj\_readSensor](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-readsensor).

- `zoh`: Zero-order hold (piecewise constant).
- `linear`: Piecewise linear interpolation.
- `cubic`: Cubic spline interpolation (Catmull-Rom).

The interp value is for advanced use-cases, see for details.

delay: real, “0”

If greater than 0, sensor values in `mjData.sensordata` are read from the history buffer at `time - delay` rather than computed directly. Requires positive, cannot be negative.

In the most common case, `delay = nsample * timestep`, see for details.

interval: real, “0 0”

This attribute controls how often sensor values are recomputed. It is useful for modeling sensors that have a larger sampling period than the simulation timestep. Requires a history buffer ( > 0).

This attribute is defined by two real-valued numbers, both in units of time, called interval = “period phase”. It is possible to only specify the period, in which case the phase is assumed to be 0.

The period specifies the interval period between recomputations. The default value of 0 has the special meaning “every simulation timestep”. Note that the period is not required to be an integer multiple of the timestep. For example, if the simulation timestep is 1.0, and period is 2.5, the sensor will be computed at times 0.0, 3.0, 5.0, 8.0, 10.0, 13.0, … with the actual interval alternating between 2 and 3 timesteps. period cannot be negative. Note that only `period > timestep` values make sense; values smaller than or equal to the timestep will not lead to an error but merely cause the sensor to be recomputed at every timestep.

The phase only takes effect during history buffer initialization in [mj\_resetData](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-resetdata). It specifies the last time that the sensor was computed “before the simulation started” in continuous time (i.e., disregarding the quantization of timesteps). It is useful for precisely controlling the *relative phase* of sensor computation and simulation time, when interval is used. The default value of 0 has the special meaning “-period”, i.e. specifying that the sensor should be computed at the first timestep of the simulation. Continuing our example from earlier, if the timestep is 1.0 and interval is “2.5 -1.5”, the sensor will be computed at times 1.0, 4.0, 6.0, 9.0, 11.0, 14.0, etc. phase must be in the range $(-\text{period}, 0]$.

user: real(nuser\_sensor), “0 0 …”

See.

### Delays

Both actuators and sensors support time delays via a ring buffer that stores timestamped samples. When the integer attribute nsample ([actuators](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-nsample), ) is positive, a buffer with nsample slots is included in the [physics state](https://mujoco.readthedocs.io/en/stable/programming/simulation.html#siphysicsstate) component `mjData.history` and the samples and current timestamps are written into the buffer upon state advancement.

If additionally the real-valued delay attribute ([actuators](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-delay), ) is positive, then during the forward dynamics the control or sensor values are read from the history buffer (instead of being read from `ctrl` or recomputed, respectively). Positive delay requires positive nsample.

Note that since reading happens before writing, the minimum positive delay is effectively one timestep, despite delay being real-valued.

Delayed reading in the engine is triggered by positive delay, and performed by the API functions [mj\_readCtrl](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-readctrl) and [mj\_readSensor](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-readsensor), which read from the buffer at `time - delay`, effectively implementing the requested delay. These functions take `time` as an argument and can be used whenever nsample is positive, allowing the user to inspect the contents of the history buffer at any time, including in a “history-only” mode (nsample > 0, delay = 0), where past values are accessible via the API but the simulation is unaffected.

**Sensor Modes**

Sensors support both and attributes. The combination determines behavior:

| delay | period | Write / Read behavior |
| --- | --- | --- |
| \= 0 | \= 0 | History-only: computed every step, written to `sensordata`, pushed into history buffer |
| \> 0 | \= 0 | Delayed: computed every step, `sensordata` contains delayed reading (read from buffer) |
| \= 0 | \> 0 | Periodic: computed on period, `sensordata` contains last computed value (no delay) |
| \> 0 | \> 0 | Periodic + Delayed: computed on period, `sensordata` contains delayed reading (read from buffer) |

**Initialization**

History buffers are initialized by [mj\_resetData](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-resetdata) as follows:

- **Values**: Always initialized to zero. For custom initialization after reset, call [mj\_initCtrlHistory](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-initctrlhistory) and [mj\_initSensorHistory](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-initsensorhistory).
- **Actuator timestamps**: `[..., -2*dt, -dt]`.
- **Sensor timestamps** without: `[..., -2*dt, -dt]`.
- **Sensor timestamps** with: Samples are spaced at `period` intervals rather than `dt`. The continuous-time timestamps `[..., phase-2*period, phase-period, phase]` are rounded up to the nearest multiple of `dt`, since that is when samples could have been computed. If `phase = 0` (the default), it is interpreted as `-period`, meaning the first sample will be computed at `t = 0`.

History buffers require a positive [timestep](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-timestep); models which violate this are rejected by the compiler. If the timestep is subsequently set to a non-positive value, [mj\_resetData](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-resetdata) issues a warning and the behavior of history buffers is undefined.

**Causality and interpolation**

The most common positive delay value is `delay = timestep * nsample`, which implements a simple history buffer, with no causality issues.

> [!warning] Warning
> If `delay > timestep * nsample`, then data will be read before the earliest buffer bound, resulting in non-causal extrapolation: using a value from before it was actually recorded. This scenario will not lead to a runtime error, so it is up to the user to avoid it.

Setting `delay < timestep * nsample` is not problematic and can be useful for [system identification](https://mujoco.readthedocs.io/en/stable/python.html#pysysid) and stochastic delays. In these use cases, one should choose a maximum possible `delay_max` and set `nsample = ceil(delay_max / timestep)`. Then at run-time or sysID-time, the [mjModel](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjmodel) fields `actuator_delay` or `sensor_delay` can be safely modified, so long as `delay_max` is not exceeded.

 [![_images/delay_buffer_light.svg](https://mujoco.readthedocs.io/en/stable/_images/delay_buffer_light.svg)](https://mujoco.readthedocs.io/en/stable/_images/delay_buffer_light.svg)[![_images/delay_buffer_dark.svg](https://mujoco.readthedocs.io/en/stable/_images/delay_buffer_dark.svg)](https://mujoco.readthedocs.io/en/stable/_images/delay_buffer_dark.svg)

These two use cases are the reason for including the interp attribute ([actuators](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-interp), ). While real-world exogenous delays are generally a zero-order-hold phenomenon, this implies discontinuity: a small change in the delay has no effect, until the timestep threshold is crossed. For example with `dt = 0.1` and `nsample = 2`, there is no functional difference between `delay = 0.2` and `delay = 0.101` (both read from the oldest sample), but stepping from `delay = 0.101` to `delay = 0.1` crosses a threshold and changes behavior. By allowing higher order interpolation, the effect of delays becomes continuous (`interp = linear`) and differentiable (`interp = cubic`).

Note that interpolation does not makes sense for some types of sensors, for example sensors that report integer values (e.g. [insidesite](https://mujoco.readthedocs.io/en/stable/XMLreference.html#sensor-insidesite)).

### Cameras

Besides the default, user-controllable, free camera, “fixed” cameras can be attached to the kinematic tree.

Extrinsics

By default, camera frames are attached to the containing body. The optional [mode](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-mode) and [target](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-target) attributes can be used to specify cameras that track (move with) or target (look at) a body or subtree. Cameras look towards the negative Z axis of the camera frame, while positive X and Y correspond to *right* and *up* in the image plane, respectively.

Projection

Cameras use [perspective](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-projection) projection by default. Setting [projection](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-projection) to `orthographic` switches to an orthographic projection, where the [fovy](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-fovy) attribute is interpreted as the vertical extent in length units rather than degrees.

Intrinsics

Camera intrinsics are specified using [ipd](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-ipd) (inter-pupilary distance, required for stereoscopic rendering and VR) and [fovy](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-fovy) (vertical field of view, in degrees).

The above specification implies a perfect point camera with no aberrations. However when calibrating real cameras, two types of linear aberration can be expressed using standard rendering pipelines. The first is different focal lengths in the vertical and horizontal directions (axis-aligned astigmatism). The second is a non-centered principal point. These can be specified using the [focal](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-focal) and [principal](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-principal) attributes. When these calibration-related attributes are used, the physical [sensor size](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-sensorsize) and camera [resolution](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-camera-resolution) must also be specified. In this case, the rendering frustum can be visualized.

### Deformable objects

In MuJoCo 3.0 we have introduced true deformable objects involving new model elements. The [skin](https://mujoco.readthedocs.io/en/stable/XMLreference.html#deformable-skin) described earlier was actually one such element, but it is merely used for visualization. We now have a related element [flex](https://mujoco.readthedocs.io/en/stable/XMLreference.html#deformable-flex) which generates contact forces, constraint forces and passive forces as needed to model a wide range of deformable entities. Both skins and flexes are now defined within a new grouping element in the XML called [deformable](https://mujoco.readthedocs.io/en/stable/XMLreference.html#deformable). A flex is a low-level element that specifies everything needed at runtime, but is difficult to design at modeling time. To aid with modeling, we have further introduced the element [flexcomp](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp) which automates the creation of the low-level flex.

A flex is a collection of MuJoCo bodies that are connected with massless stretchable elements. These elements can be capsules (1D flex), triangles (2D flex), or tetrahedra (3D flex). In all cases we allow a radius, which makes the elements smooth and also volumetric in 1D and 2D. The primitive elements are illustrated below:

[![_images/flexelem.png](https://mujoco.readthedocs.io/en/stable/_images/flexelem.png)](https://mujoco.readthedocs.io/en/stable/_images/flexelem.png)

Thus far these look like geoms. But the key difference is that they deform: as the bodies (vertices) move independently of each other, the shape of the elements changes in real time. Collisions and contact forces are now generalized to handle these deformable geometric elements. Note that when two such elements collide, the contact no longer involves just two bodies, but can involve up to 8 bodies (if both elements are tetrahedra). Contact forces are computed as before, given the contact frame and relevant quantities expressed in that frame. But then the contact force is distributed among all interacting bodies. The notion of contact Jacobian is complicated because the contact point cannot be considered fixed in any body frame. Instead we use a weighting scheme to “assign” each contact point to multiple bodies. It is also possible to create a rigid flex, by assigning all vertices to the same body. This is a way to re-purpose the new flex collision machinery to implement rigid non-convex mesh collisions (unlike mesh geoms which are convexified for collision purposes).

**Deformation model**.

In order to preserve the shape of the flex (in a soft sense), we need to generate passive or constraint forces. Prior to MuJoCo 3.0 this would involve a large number of tendons plus constraints on tendons and joints. This is still possible here, but inefficient both in terms of modeling and in terms of simulation when the flex is large. Instead, the design philosophy is to use a single set of parameters and provide two modeling choices: a new (soft) equality constraint type that applies to all edges of a given flex, which permits large time steps, or a discretized continuum representation, where each element is in a constant stress state, which is equivalent to piecewise linear finite elements and achieves improved realism and accuracy. The edge-based model could be seen as a “lumped” stiffness model, where the correct coupling of deformation modes (e.g. shear and volumetric) is averaged in a single quantity. The continuum model enables instead to specify shear and volumetric stiffnesses separately using the [Poisson’s ratio](https://en.wikipedia.org/wiki/Poisson%27s_ratio) of the material. For more details, see the [Saint Venant-Kirchhoff](https://en.wikipedia.org/wiki/Hyperelastic_material#Saint_Venant%E2%80%93Kirchhoff_model) hyperelastic model.

**Rods**.

For 1D flexes, [elasticity](https://mujoco.readthedocs.io/en/stable/XMLreference.html#flex-elasticity) implements the [discrete elastic rod](https://www.cs.columbia.edu/cg/pdfs/143-rods.pdf) (DER) model of bending and torsion. For open chains with at least two elements (both **circle** and **box** [sections](https://mujoco.readthedocs.io/en/stable/XMLreference.html#flex-elasticity-section)), [flexcomp](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp) creates per-edge twist bodies and hinge joints (`<name>_twist_0`, …, `<name>_twist`, omitting `<name>_twist_0` when the first edge is clamped to a body via `<pin id="0 1"/>`, and `<name>_twist` when the last two points of a rod with at least three elements are pinned). Each edge carries a material frame rotated by an angle $\theta_e$ about its tangent relative to a per-edge reference frame `(t_old, u_old)` that is parallel-transported in time and stored in `mjData.plastic` (`mjSTATE_PLASTIC`), together with the reference twist of each interior vertex, unwrapped across steps. A clamped end fixes that end’s material frame to the pinning body, which receives the reaction torque of the rod, while an unclamped `<name>_twist` controls or actuates the terminal material angle. Time-parallel transport keeps both torsion and curved reference bending continuous and drift-free as the rod coils, writhes, or tumbles in 3D (as in [cable.xml](https://github.com/google-deepmind/mujoco/blob/main/model/flex/cable.xml), [belt.xml](https://github.com/google-deepmind/mujoco/blob/main/model/flex/belt.xml), and [curved\_rods.xml](https://github.com/google-deepmind/mujoco/blob/main/model/flex/curved_rods.xml)), while frictional contact forces couple into the per-edge twist DOFs through their cross-sectional lever arm so circular cables roll on surfaces and twist in grippers and rectangular (**box**) ribbons couple anisotropic bending, torsion, and oriented-box contact.

For closed circular loops (such as the ring in [curved\_rods.xml](https://github.com/google-deepmind/mujoco/blob/main/model/flex/curved_rods.xml)) or raw `<flex dim="1">` elements without twist joints whose reference configuration `qpos0` has adjacent curved vertices (bent by more than $10^{-4}$ rad), adjacent curved vertices are paired across their shared edge: each vertex’s bending stiffness is split evenly among its pairs and the dihedral twist between their osculating planes around the shared edge is penalized relative to its reference value in `qpos0`, preserving 3D rest curvature and torsion.

**Parametrization types**.

While the default behavior of flexcomp produces a “full” flex where every node corresponds to a MuJoCo body, it also supports specialized [parametrizations](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp-dof) for volumetric objects: **trilinear** and **quadratic**. Instead of directly simulating all nodes, these options define a background grid of cells. The positions of the interior vertices are computed by interpolating the positions of the cell corners. Trilinear flexes use 8-node hexahedral cells with linear interpolation along each axis, while quadratic flexes use 27-node cells with quadratic interpolation, allowing for curved deformation modes. These grid-based parametrizations require fewer degrees of freedom than full flexes and can result in significantly faster simulation times, especially for large volumetric soft bodies.

**Creation and visualization**.

```xml
<option timestep=".001"/>

<worldbody>
   <flexcomp type="grid" count="24 4 4" spacing=".1 .1 .1" pos=".1 0 1.5"
             radius=".0" rgba="0 .7 .7 1" name="softbody" dim="3" mass="7">
      <contact condim="3" solref="0.01 1" solimp=".95 .99 .0001" selfcollide="none"/>
      <edge damping="1"/>
      <elasticity poisson="0.2" young="5e4">
   </flexcomp>
</worldbody>
```

Using the [flexcomp](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp) element, we can create flexes from meshes, including tetrahedral meshes, and automatically generate all the bodies/vertices and connect them with suitable elements. We can also create grids and other topologies automatically. This machinery makes it easy to create very large flexes, involving thousands or even tens of thousands of bodies, elements and edges. Obviously such simulations will not be fast. Even for medium-sized flexes, pruning of collision pairs is essential. This is why we have developed elaborate methods for pruning self-collisions; see XML reference.

In case of 3D flexes made of tetrahedra, it may be useful to examine how the flex is “triangulated” internally. We have a special visualization mode that peels off the outer layers. Below is an example with the Stanford Bunny. Note how it has smaller tetrahedra on the outside and larger ones on the inside. This mesh design makes sense, because we want the collision surface to be accurate, but on the inside we just need soft material properties – which require less spatial resolution. In order to convert a surface mesh to a tetrahedral mesh, we recommend open tools like the [fTetWild library](https://github.com/wildmeshing/fTetWild).

[![bunny1](https://mujoco.readthedocs.io/en/stable/_images/bunny1.png)](https://mujoco.readthedocs.io/en/stable/_images/bunny1.png) [![bunny2](https://mujoco.readthedocs.io/en/stable/_images/bunny2.png)](https://mujoco.readthedocs.io/en/stable/_images/bunny2.png)

### Including files

MJCF files can include other XML files using the [include](https://mujoco.readthedocs.io/en/stable/XMLreference.html#include) element. Mechanistically, the parser replaces the DOM node corresponding to the include element in the master file with the list of XML elements that are children of the top-level element in the included file. The top-level element itself is discarded, because it is a grouping element for XML purposes and would violate the MJCF format if included.

This functionality enables modular MJCF models; see the MPL family of models in the model library. One example of modularity is constructing a model of a robot (which tends to be elaborate) and then including it in multiple “scenes”, i.e., MJCF models defining the objects in the robot’s environment. Another example is creating a file with commonly used assets (say materials with carefully adjusted rgba values) and including it in multiple models which reference those assets.

The included files are not required to be valid MJCF files on their own, but they usually are. Indeed we have designed this mechanism to allow MJCF models to be included in other MJCF models. To make this possible, repeated MJCF sections are allowed even when that does not make sense semantically in the context of a single model. For example, we allow the kinematic tree to have multiple roots (i.e., multiple worldbody elements) which are merged automatically by the parser. Otherwise including robots into scenes would be impossible.

The flexibility of repeated MJCF sections comes at a price: global settings that apply to the entire model, such as the angle attribute of [compiler](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler) for example, can be defined multiple times. MuJoCo allows this, and uses the last definition encountered in the composite model, after all include elements have been processed. So if model A is defined in degrees and model B is defined in radians, and A is included in B after the compiler element in B, the entire composite model will be treated as if it was defined in degrees – leading to undesirable consequences in this case. The user has to make sure that models included in each other are compatible in this sense; local vs. global coordinates is another compatibility requirement.

Finally, as explained next, element names must be unique among all elements of the same type. So for example if the same geom name is used in two models, and one model is included in the other, this will result in compile error. Including the same XML file more than once is a parsing error. The reason for this restriction is that we want to avoid repeated element names as well as infinite recursion caused by inclusion.

### Naming elements

Most model elements in MJCF can have names. They are defined with the attribute name of the corresponding XML element. When a given model element is named, its name must be unique among all elements of the same type. Names are case-sensitive. They are used at compile time to reference the corresponding element, and are also saved in mjModel for user convenience at runtime.

The name is usually an optional attribute. We recommend leaving it undefined (so as to keep the model file shorter) unless there is a specific reason to define it. There can be several such reasons:

- Some model elements need to reference other elements as part of their creation. For example, a spatial tendon needs to reference sites in order to specify the via points it passes through. Referencing can only be done by name. Note that assets exist for the sole purpose of being referenced, so they must have a name, however it can be omitted and set implicitly from the corresponding file name.
- The visualizer offers the option to label all model elements of a given type. When a name is available, it is printed next to the object in the 3D view; otherwise a generic label in the format “body 7” is printed.
- The function [mj\_name2id](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-name2id) returns the index of the model element with given type and name. Conversely, the function [mj\_id2name](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-id2name) returns the name given the index. This is useful for custom computations involving a model element that is identified by its name in the XML (as opposed to relying on a fixed index which can change when the model is edited).
- The model file could in principle become more readable by naming certain elements. Keep in mind however that XML itself has a commenting mechanism, and that mechanism is more suitable for achieving readability – especially since most text editors provide syntax highlighting which detects XML comments.

### URDF extensions

The Unified Robot Description Format (URDF) is a popular XML file format in which many existing robots have been modeled. This is why we have implemented support for URDF even though it can only represent a subset of the model elements available in MuJoCo. In addition to standard URDF files, MuJoCo can load files that have a custom (from the viewpoint of URDF) mujoco element as a child of the top-level element robot. This custom element can have sub-elements [compiler](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler), [option](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option), [size](https://mujoco.readthedocs.io/en/stable/XMLreference.html#size) with the same functionality as in MJCF, except that the default compiler settings are modified so as to accommodate the URDF modeling convention. The [compiler](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler) extension in particular has proven very useful, and indeed several of its attributes were introduced because a number of existing URDF models have non-physical dynamics parameters which MuJoCo’s built-in compiler will reject if left unmodified. This extension is also needed to specify mesh directories. Also note that the compiler attributes [strippath](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-strippath), [angle](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-angle), [fusestatic](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-fusestatic) and [discardvisual](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-discardvisual) have different default values for URDF and MJCF.

URDF specifies effort limits on joints and has no actuator model, so a joint’s `<limit effort="...">` becomes its [actuatorfrcrange](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint-actuatorfrcrange). When adding actuators to the converted MJCF, either keep this joint-level clamp or move the limit to the actuators’ [forcerange](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-forcerange) (see ).

Note that the while MJCF models are checked against a custom XML schema by the parser, URDF models are not. Even the MuJoCo-specific elements embedded in the URDF file are not checked. As a result, mis-typed attribute names are silently ignored, which can result in major confusion if the typo remains unnoticed.

Here is an example extension section of a URDF model:

```xml
<robot name="darwin">
  <mujoco>
    <compiler meshdir="../mesh/darwin/" balanceinertia="true" discardvisual="false"/>
  </mujoco>
  <link name="MP_BODY">
    ...
</robot>
```

The above extensions make URDF more usable but still limited. If the user wants to build models taking full advantage of MuJoCo and at the same time maintain URDF compatibility, we recommend the following procedure. Introduce extensions in the URDF as needed, load it and save it as MJCF. Then add information to the MJCF using [include](https://mujoco.readthedocs.io/en/stable/XMLreference.html#include) elements whenever possible. In this way, if the URDF is modified, the corresponding MJCF can be easily re-created. In our experience though, URDF files tend to be static while MJCF files are often edited. Thus in practice it is usually sufficient to convert the URDF to MJCF once and after that only work with the MJCF.

### MoCap bodies

`mocap` bodies are static children of the world (i.e., have no joints) and their mocap attribute is set to “true”. They can be used to input a data stream from a motion capture device into a MuJoCo simulation. Suppose you are holding a VR controller, or an object instrumented with motion capture markers (e.g. Vicon), and want to have a simulated object moving in the same way but also interacting with other simulated objects. There is a dilemma here: virtual objects cannot push on your physical hand, so your hand (and thereby the object you are controlling) can violate the simulated physics. But at the same time we want the resulting simulation to be reasonable. How do we do this?

Mocap bodies and their dof-less descendants form their own *weld group*, rooted at the mocap body (`mjModel.body_weldid` equals the mocap body’s own id rather than 0, the world). This has several consequences: children of mocap bodies receive the standard parent-child collision exclusion; mocap bodies do not generate contacts with static geometry or with each other; and when [sleeping](https://mujoco.readthedocs.io/en/stable/computation/index.html#sleeping) is enabled, mocap bodies count as awake — contact with a mocap body, or an active equality constraint connecting to one, wakes sleeping objects, so dragging a mocap body through a pile of sleeping objects behaves as expected.

The first step is to define a mocap body in the MJCF model, and implement code that reads the data stream at runtime and sets [mjData.mocap\_pos](https://mujoco.readthedocs.io/en/stable/programming/simulation.html#simocap) and [mjData.mocap\_quat](https://mujoco.readthedocs.io/en/stable/programming/simulation.html#simocap) to the position and orientation received from the motion capture system. The [simulate.cc](https://mujoco.readthedocs.io/en/stable/programming/samples.html#sasimulate) code sample uses the mouse as a motion capture device, allowing the user to move mocap bodies around:

[![particle](https://mujoco.readthedocs.io/en/stable/_images/particle.gif)](https://mujoco.readthedocs.io/en/stable/_images/particle.gif)

The key thing to understand about mocap bodies is that the simulator treats them as being fixed. We are causing them to move from one simulation time step to the next by updating their position and orientation directly, but as far as the physics model is concerned their position and orientation are constant. So what happens if we make contact with a regular dynamic body, as in the particle examples provided with the MuJoCo distribution (recall that in those example we have a capsule probe which is a mocap body that we move with the mouse). A contact between two regular bodies will experience penetration as well as relative velocity, while contact with a mocap body is missing the relative velocity component because the simulator does not know that the mocap body itself is moving. So the resulting contact force is smaller and it takes longer for the contact to push the dynamic object away. Also, in more complex simulations the fact that we are doing something inconsistent with the physics can cause instabilities.

There is however a better-behaved alternative. In addition to the mocap body, we include a second regular body and connect it to the mocap body with a weld equality constraint. In the plots below, the pink box is the mocap body and it is connected to the base of the hand. In the absence of other constraints, the hand tracks the mocap body almost perfectly (and much better than a spring-damper would) because the constraints are handled implicitly and can produce large forces without destabilizing the simulation. But if the hand is forced to make contact with the table for example (right plot) it cannot simultaneously respect the contact constraint and track the mocap body. This is because the mocap body is free to go through the table. So which constraint wins? That depends on the softness of the weld constraint relative to the contact constraint. The corresponding solref and solimp parameters need to be adjusted so as to achieve the desired trade-off. See the Modular Prosthetic Limb (MPL) hand model available on the MuJoCo Forum for an example; the plots below are generated with that model.

[![image18](https://mujoco.readthedocs.io/en/stable/_images/mocap1.png)](https://mujoco.readthedocs.io/en/stable/_images/mocap1.png) [![image19](https://mujoco.readthedocs.io/en/stable/_images/mocap2.png)](https://mujoco.readthedocs.io/en/stable/_images/mocap2.png)

### Memory allocation

MuJoCo preallocates all the memory needed at runtime in [mjData](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjdata), and does not access the heap allocator after model creation. Memory in [mjData](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjdata) is allocated by [mj\_makeData](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-makedata) in two contiguous blocks:

- `mjData.buffer` contains fixed-size arrays.
- `mjData.arena` contains dynamically-sized arrays.

There are two types of dynamic arrays allocated in the `arena` memory space.

- contacts and constraint-related arrays are laid out from the beginning of the `arena`.
- [stack](https://mujoco.readthedocs.io/en/stable/programming/simulation.html#sistack) arrays are laid out from the end of the `arena`.

By allocating dynamic quantities from both sides of the `arena` space, variable-sized memory allocation is controlled by a single number: the memory attribute of the [size](https://mujoco.readthedocs.io/en/stable/XMLreference.html#size) MJCF element. Unlike the fixed-size arrays in the `buffer`, variable-sized arrays in the arena can be `NULL`, for example after a call to [mj\_resetData](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-resetdata). When `arena` memory runs out, one of four things will happen, depending on the type of memory requested:

- If memory runs out during contact allocation, a warning will be raised and subsequent contacts will not be added in this step, but simulation continues as usual.
- If memory runs out during constraint-related allocation, a warning will be raised and the constraint solver will be disabled in this step, but simulation continues as usual. Note that physics without the constraint solver will generally be very different, but allowing the simulation to continue can still be useful, e.g. during scene initialization when many bodies are temporarily overlapping.
- If memory runs out while the Newton solver is constructing or refactoring its Hessian/Cholesky factor (for example, under heavy contact fill-in on a deformable `flex`), `mjWARN_CNSTRFULL` will be raised and the solver will fall back to CG (or to incremental rank-1 cone updates) for that step. If this warning fires repeatedly, each step still incurs symbolic Hessian counting before falling back, so memory should be increased.
- If memory runs out during stack array allocation, a hard error will occur.

Unlike the size of the `buffer`, the size of the `arena` cannot be pre-computed, since the number of contacts and stack usage is not known in advance. So how should one choose it? The following heuristic is currently used: for rigid degrees of freedom, enough memory is allocated for 100 contacts and 500 scalar constraints under worst-case dense conditions; for deformable `flex` degrees of freedom, the sparse Newton Hessian and Cholesky factor are estimated from a symbolic reverse-Cholesky count on the static flex mesh topology (with a 1.5x safety margin) plus a bounded allowance for colliding flex contacts. If this heuristic is insufficient, we recommend the following procedure. Increase the `arena` memory significantly using the memory attribute, and inspect the actual memory used at runtime. `mjData.maxuse_arena` keeps track of the maximum `arena` memory utilization since the last reset. The [simulate](https://mujoco.readthedocs.io/en/stable/programming/samples.html#sasimulate) viewer shows this number as a fraction of the total arena space (in the info window in the lower-left corner). So one can start with a large number, simulate for a while, and if the fractions are small go back to the XML and reduce the allocation size. Keep in mind though that memory utilization can change dramatically in the course of the simulation, depending on how many constraints are active and which constraint solver is used. The CG solver is the most memory efficient, followed by the Newton solver, while the PGS solver is the most memory intensive. When we design models, we usually aim for 50% utilization in the worst-case scenario encountered while exploring the model. If you only intend to use the CG solver, you can get away with significantly smaller arena allocation.

### Assets by reference

An asset in [mjModel](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjmodel) is *embedded* when its payload is in the model buffer, which is the default, or *by reference* when the model holds a resolved path and the parameters a consumer needs to load it, and no payload. Textures are the first asset type which can be by reference; the compiler never reads a texture, so leaving it out of the model saves the decoding time and the memory of the pixels, which in texture-heavy scenes is most of the model. The mode is the [passthrough](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-passthrough) attribute of [compiler](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler), overridden per texture by [embed](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-texture-embed) (`mjsCompiler.passthrough` and `mjsTexture.embed` in the [mjSpec](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjspec)).

A texture `i` of [mjModel](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjmodel) is by reference when `tex_adr[i] == -1`. Then:

- `tex_width[i]` and `tex_height[i]` are 0, since the size is not known without reading the file. `tex_type`, `tex_colorspace` and `tex_nchannel` are as authored, except that a KTX has 1 channel, as when embedded; in particular a [colorspace](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-texture-colorspace) of “auto” stays `mjCOLORSPACE_AUTO`, to be resolved by whoever decodes the file. `ntexdata` excludes the texture.
- `paths + tex_pathadr[i]` is the resolved path of the file: the directory of the model file, the [texturedir](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-texturedir) and the [file](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-texture-file) attribute, after [strippath](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-strippath), unless the file is absolute or has a scheme (e.g. `https://`) handled by a [resource provider](https://mujoco.readthedocs.io/en/stable/programming/extension.html#exprovider). As for every asset, this holds whether or not the texture is by reference. `paths + tex_contenttypeadr[i]` is the authored [content\_type](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-texture-content-type), or `tex_contenttypeadr[i] == -1` to infer it from the extension.
- The bytes of the file are read with [mju\_openResource](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-openresource) and [mju\_readResource](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-readresource) on that path, with no virtual file system. The compiler does not check that the file exists or that it can decode it; a path which does not resolve is an error for whoever reads it. [mj\_loadTexture](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-loadtexture) decodes a texture into pixels, for both kinds of texture: for a by-reference texture it reads and decodes the file, resolving a colorspace of “auto”, and returns exactly the bytes compilation would have stored; for an embedded texture it returns a copy. The built-in renderer loads by-reference textures through it, in [mjr\_makeContext](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjr-makecontext) and [mjr\_uploadTexture](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mjr-uploadtexture), so a file which does not resolve or decode is a warning and an untextured material rather than an error. The Filament renderer loads them through [mj\_loadTexture](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-loadtexture) too, uploading the data as it would that of an embedded texture (a KTX file is its bytes, which Filament decodes), and uploads a file once for all textures that share it and its decode parameters.

A by-reference texture is always the file as a consumer would read it. Textures which the compiler would transform stay embedded, so that the model needs no fields describing the transformation: flipped textures, composite [grids](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-texture-gridsize), cubes from six [separate files](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-texture-fileright), [procedural](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-texture-builtin) textures and textures given as a buffer. A file served from memory by a [virtual file system](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#virtualfilesystem) also stays embedded, since the memory has no lifetime beyond compilation.

Compilation does not modify the [mjSpec](https://mujoco.readthedocs.io/en/stable/APIreference/APItypes.html#mjspec): the resolved path is computed when the model is written, the texture element keeps its file and embed attributes, and every spec texture has exactly one model texture, with the same id and name, whether or not it is by reference. Recompiling after changing the policy switches the representation. [mj\_saveModel](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-savemodel) writes the model as it is, so an MJB file keeps its by-reference textures as references, and loads wherever the paths resolve. [mj\_embedAssets](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-embedassets) makes a new model with every by-reference texture loaded into it, equal to the eager compile of the same spec; a hermetic MJB file is [mj\_embedAssets](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-embedassets), [mj\_saveModel](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-savemodel), [mj\_deleteModel](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mj-deletemodel).

## Tips and tricks

Here we provide guidance on how to accomplish some common modeling tasks. There is no new material here, in the sense that everything in this section can be inferred from the rest of the documentation. Nevertheless the inference process is not always obvious, so it may be useful to have it spelled out.

### Preventing slip

Below is a list of steps one can take in order to diagnose and solve contact slippage, which is especially problematic in manipulation tasks. In order to diagnose slippage, it is recommended to use the [simulate](https://mujoco.readthedocs.io/en/stable/programming/samples.html#sasimulate) utility’s built in visualization options to inspect contacts and contact forces. It is often helpful to tweak the visual size of contacts and forces (using the global [meansize](https://mujoco.readthedocs.io/en/stable/XMLreference.html#statistic-meansize) or the specific [contactwidth](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual-scale-contactwidth), [contactheight](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual-scale-contactheight) and [forcewidth](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual-scale-forcewidth) attributes) and the [force scaling](https://mujoco.readthedocs.io/en/stable/XMLreference.html#visual-map-force) attribute, to better visualize and understand the contact configuration and resulting forces.

**Slip-preventing contact forces are outside the friction cone**

This implies that the physics cannot prevent slip, even in principle. This occurs when:

1. *The normal force is too small.* Ensure that the maximum force that can be applied by the gripper multiplied by the sliding friction coefficient is significantly greater than the weight of the object.
2. *The sliding friction coefficient is too low.* Increase the sliding [friction](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-friction) coefficient.
3. *Torsional friction is insufficient to apply the required torques.* Increase [condim](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-condim) to 4 or 6 and choose appropriate friction coefficients. **condim 4** enables torsional friction, preventing rotation around the normal. **condim 6** also enables rolling friction, preventing rotation around the tangential directions. See the [Contact](https://mujoco.readthedocs.io/en/stable/computation/index.html#cocontact) section for details and the specific semantics of these coefficients.

**The geometry does not support the required forces or torques**

This is a common real-world problem, solved by improved design of grippers and handles.

1. Improve the geometry of the contacting geoms in order to add more contact points, possibly with non-flat geometry (e.g., bumps), so slippage is prevented by the normal force and not only frictional components.
2. If contacts are between flat surfaces, make sure that the flag [multiccd](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-multiccd) is not disabled (enabled by default), as it allows the detector to find more contacts than the single contact returned by the convex-convex collider.
3. Make sure that the flag [nativeccd](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-nativeccd) is not disabled (enabled by default), as NativeCCD is a more accurate and efficient convex collision detection algorithm.

**High-frequency vibration**

High-frequency, low-amplitude vibrations are also a real-world problem in many industrial settings, but unlike in simulation, in the real world they are audible. Such vibration is often caused by controllers with very high gains and sometimes by stick-slip feedback from contacts or joints, resonating with the eigen-modes of the mechanism. The easiest way to diagnose such vibration is to visualize contact forces in [simulate](https://mujoco.readthedocs.io/en/stable/programming/samples.html#sasimulate). The solution is usually to reduce the [timestep](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-timestep) and/or add some [armature](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint-armature) to the relevant joints. Another reason for vibration is feedback from explicit damping. Use the implicit or implicitfast integrators, as documented in the [Numerical Integration](https://mujoco.readthedocs.io/en/stable/computation/index.html#geintegration) section.

**Slow slippage**

Even when the tangential force required for static equilibrium lies strictly inside the contact friction cone, MuJoCo’s regularized soft-contact model does not guarantee an exact zero-velocity stick state. In the recommended elliptic contact model, friction dimensions have no position residual and are purely damped, so a persistent tangential load can produce a nonzero steady slip velocity. This is expected behavior; see and the [softness and slip](https://mujoco.readthedocs.io/en/stable/overview.html#soft) clarification.

After ruling out the faster failure modes above, slow slippage can be reduced in two ways.

1. Use [elliptic cones](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-cone) and increase [impratio](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-impratio). This makes the friction dimensions harder relative to the normal dimension without increasing the friction coefficient. It reduces slow slippage but does not guarantee exact sticking. The slip rate also depends on contact parameters, loading, geometry and dynamics, so `impratio` alone does not define a universal rate.
2. For stronger suppression, enable the NoSlip solver by setting [noslip\_iterations](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-noslip-iterations) to a positive integer. A small number (1, 2 or 3) is usually sufficient. In its friction-only post-processing sweep, NoSlip sets the regularizer to zero for the updated friction dimensions. The degree of suppression depends on solver convergence; the iteration limit caps the work, while [noslip\_tolerance](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-noslip-tolerance) is an early-termination threshold rather than a bound on residual slip. Exact zero slip is not guaranteed. NoSlip also adds computational cost, makes inverse dynamics ill-defined and can occasionally cause instabilities in complex multi-contact systems. See the [NoSlip solver](https://mujoco.readthedocs.io/en/stable/computation/index.html#sonoslip) for details.

### Preventing tunneling

Collision detection only inspects geom poses at discrete timesteps, so thin or fast-moving geoms (plates, walls, projectiles, swinging links) can pass through each other within a single step. Rather than shrinking the [timestep](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-timestep) or thickening geoms, enable the [speculative](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-speculative) flag, which adds contacts before impact at a collision cost that is often repaid by the larger timestep it allows. Height fields, SDFs and flexes are not supported. See [Speculative contacts](https://mujoco.readthedocs.io/en/stable/computation/index.html#cospeculative) for details and [model/speculative/](https://github.com/google-deepmind/mujoco/tree/main/model/speculative) for examples.

> [!note] New feature
> Speculative contacts were added in October 2026; their behavior may still change.

### Backlash

Backlash is present in many robotic joints. It is usually caused by small gaps between gears in the gearbox, but could also be caused by some sloppiness in the joint mechanism. The effect is that the motor can turn for a small angle before the joint turns, or vice versa (when external force is applied on the joint). Backlash can be modeled in MuJoCo as follows. Instead of having a single hinge joint within the body, define two hinge joints with identical position and orientation:

```xml
<body>
  <joint name="J1" type="hinge" pos="0 0 0" axis="0 0 1" armature="0.01"/>
  <joint name="J2" type="hinge" pos="0 0 0" axis="0 0 1" limited="true" range="-1 1"/>
</body>
```

Thus the overall rotation of the body relative to its parent is J1+J2. Now define an actuator acting only on J1. The small joint range on J2 keeps it near 0, yet allows it to move a bit in the direction of the force acting on it, producing a backlash effect. Note the armature attribute in J1. Without it the joint-space inertia matrix will be singular, because the two joints could accelerate in opposite directions without encountering any inertia. The physical gears responsible for the backlash actually have rotational inertia (which we call armature) so this is a realistic modeling approach. The numbers in this example should be adjusted to obtain the desired behavior. The solref and solimp parameters of the joint limit constraint could also be adjusted, to make the backlash rotation end at a softer or a harder limit.

Instead of specifying joint limits in J2, one can specify a soft equality constraint keeping J2=0. The constraint impedance function should then be adjusted so the constraint is weak near J2=0 and gets stronger away from 0. The new parameterization of impedance functions shown in enables this. Compared to joint limits, the equality constraint approach will generate a softer transition between the backlash regime and the limit regime. It will also be active all the time, which is convenient in user code that needs the constraint violation or constraint force as input.

### Restitution

Another mechanism exists for specifying solref, as explained in. When both numbers are non-positive, they are interpreted as (-stiffness, -damping) and scaled by the constraint impedance. To achieve perfect restitution for contacts and other constraints, set stiffness to some reasonably large value and damping to zero. Below is an example of a sphere bouncing on a plane with restitution coefficient of 1, so that the energy before and after contact is approximately preserved. It is not exactly preserved because the contact itself is soft and takes several time steps, and the (implicit) deformations during those time steps are not exactly energy-preserving. But the overall effect is that the ball bounces for a very long time without changing its peak height in a visible way, and the energy fluctuates around the initial value instead of drifting.

```xml
<worldbody>
  <geom type="plane" size="1 1 .1"/>

  <body pos="0 0 1">
    <freejoint/>
    <geom type="sphere" size="0.1" solref="-1000 0"/>
  </body>
</worldbody>
```

### Constraint accuracy

MuJoCo’s [constraint impedance](https://mujoco.readthedocs.io/en/stable/computation/index.html#soparameters) computation relies on an approximate diagonal of the constraint-space inertia matrix, computed once at compile time from the initial configuration `qpos0`.

In the vast majority of models this approximation is entirely adequate. However, in certain situations—such as models with highly anisotropic inertias, complex kinematic chains, or bodies operating far from `qpos0` —the approximation may become inaccurate. This can occasionally manifest as unexplained solver divergence (`badqacc` warnings), excessive penetration, unrealistic slip, or poor solver convergence. A useful diagnostic is the [fwdinv](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-fwdinv) flag: if the forward-inverse discrepancy is large, inaccurate constraint scaling may be a contributing factor.

If you suspect that the compile-time approximation is insufficient for your model, you can enable the [diagexact](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-diagexact) flag to compute the exact diagonal at runtime. See [Diagonal approximation](https://mujoco.readthedocs.io/en/stable/computation/index.html#soexactdiag) for details on the underlying mechanics and performance implications.

## Model tuning

Physical fidelity and simulation speed are two sides of the same coin: almost every change that improves accuracy costs compute, while relaxing accuracy buys throughput at the expense of realism. Model tuning is the process of choosing the right point on this speed–fidelity trade-off for a given task, while taking advantage of the few changes that improve *both*.

Before tuning parameters, load the model paused in [MuJoCo Studio](https://mujoco.readthedocs.io/en/stable/studio/native_viewers.html#studioapp) (or [simulate](https://mujoco.readthedocs.io/en/stable/programming/samples.html#sasimulate)) and rule out modeling bugs that masquerade as bad contacts: intersecting geoms at `t = 0` (toggle contact points/forces), visual/collision geom mismatches (toggle geom groups), concave collision meshes replaced by their [convex hulls](https://mujoco.readthedocs.io/en/stable/computation/index.html#cochecking) (toggle convex hulls; see [convex decomposition](https://mujoco.readthedocs.io/en/stable/computation/index.html#codecomposition)), implausible CAD/URDF inertias (toggle equivalent inertia boxes), millimeter/meter [unit or scale](https://mujoco.readthedocs.io/en/stable/overview.html#units) mismatches (check [mesh/scale](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-mesh-scale) and total mass), degree/radian or joint-axis mismatches (toggle joint axes; [compiler/angle](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-angle) defaults to `"degree"`), and position targets driving past joint limits or into surfaces. Stiffening contacts to mask these issues can cause chatter or divergence. Once the model is clean, tune interactively using the viewer’s contact-force and profiler overlays, and measure headless throughput with [testspeed](https://mujoco.readthedocs.io/en/stable/programming/samples.html#satestspeed) so changes target the stage dominating step time.

### Tuning defaults

**Unfortunate defaults**:

Several of MuJoCo’s internal defaults (e.g. `integrator="Euler"`, `cone="pyramidal"`, `solref="0.02 1"`) date back to early versions of the engine and are not what we recommend for new models today. Changing a physics default is difficult because it silently alters simulation trajectories across every existing model that omits the attribute. We may revise some of these defaults in a future release, but for now backwards compatibility keeps them fixed.

**Context-dependent defaults**:

Other defaults (e.g. `damping="0"`, `condim="3"`, `contype=conaffinity="1"`) are sensible baselines, but usually need to be overridden on real robots, so we note them in the table below.

Overriding these defaults at the start of a project, typically once in [option](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option) and the top-level class, avoids the most common modeling pitfalls:

| Setting | Internal default | Recommended initial value | Why? |
| --- | --- | --- | --- |
| [integrator](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-integrator) | `"Euler"` | `"implicitfast"` (`"discrete"` for flex elasticity or stiff springs/servos; see note below) | Cheap implicit integration of velocity-dependent forces. |
| [cone](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-cone), [impratio](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-impratio) | `"pyramidal"`, `"1"` | `"elliptic"`, `"10"` | Isotropic friction cones and stronger tangential resistance to slip. |
|  | `"0.02"` | `"0.004"` — `"0.01"` | Crisper rigid contacts and tighter equality constraints. |
|  | `"0.9"` | Keep, or `"0.95"` if needed | Halves rest penetration and creep, at the cost of more solver iterations. |
| [contype](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-contype), [conaffinity](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-conaffinity) | `"1"`, `"1"` | Separate visual / collision classes | Keeps detailed visual meshes out of collision detection. |
| [condim](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-condim) | `"3"` | `"4"` or `"6"` on grasp pads and rolling props | Adds torsional (and rolling) friction for stable pinch grasps and settling on flat surfaces. |
| [joint/armature](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint-armature), [damping](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint-damping) | `"0"`, `"0"` | Nonzero rotor inertia & light damping | Better mass-matrix conditioning and free implicit damping of chatter. |
| [actuator/position](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-position) | `kv="0"`, unlimited force | `dampratio="1"` (or `kv`) + forcerange | Critically damped servo response and bounded contact impulses. |

The lists below walk through global and model-level knobs in rough order of importance when tuning.

### Global options

**Timestep** ([timestep](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-timestep): `"0.002"`):

See note under [Numerical Integration](https://mujoco.readthedocs.io/en/stable/computation/index.html#gechoosingtimestepintegrator). The primary speed–fidelity knob: throughput scales linearly with timestep up to the stability limit where simulation diverges. `2 ms` is usually reasonable, or slightly high, for contact-rich manipulation (stiff grippers, high gains, or thin objects often prefer `0.5–2 ms`), whereas `5–15 ms` can work well for locomotion. When [refsafe](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-refsafe) is enabled, standard integrators clamp effective `solref[0]` to at least `2 * timestep` (under `discrete`, equality and friction rows stay unclamped while contact and limit springs that the step cannot resolve are clamped to the stiffest zero-restitution spring for timestep), so raising timestep past the clamp threshold also softens contacts. If thin or fast-moving geoms start tunneling through each other at the larger timestep, enable rather than shrinking it.

**Integrator** ([integrator](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-integrator): `"Euler"`):

See note under [Numerical Integration](https://mujoco.readthedocs.io/en/stable/computation/index.html#gechoosingtimestepintegrator). Use `implicitfast` for most models: it has nearly the same per-step cost as `Euler` (symmetric Cholesky factorization) while integrating actuator velocity feedback (kv, dampratio), tendon damping, and fluid viscosity implicitly, and applying exact [gyroscopic derivatives](https://mujoco.readthedocs.io/en/stable/computation/index.html#gefreebody) to standalone free bodies (`Euler` handles only joint damping implicitly). Use `RK4` (4x cost per step) for nearly energy-conserving or tumbling systems, and `implicit` (unsymmetric LU) for fast-spinning coupled multi-link chains where Coriolis derivatives matter. Models with flex [elasticity](https://mujoco.readthedocs.io/en/stable/XMLreference.html#flex-elasticity) or passive flex contact require `discrete` (they raise an error under `implicit` and `implicitfast`); see.

> [!note] Note
> We are currently trialling discrete as a candidate to replace `implicitfast` as the recommended integrator. `discrete` folds position stiffness (joint and tendon springs, flex elasticity, and actuator kp) jointly with the constraints into a single effective metric $\widehat{M} = M + hD + h^2K$, remaining stable at much larger timesteps when stiff servos or springs interact with contacts; see [Integrators](https://mujoco.readthedocs.io/en/stable/computation/index.html#geintegrators) for details and current limitations.

**Solver, iterations, and tolerance** ([solver](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-solver): `"Newton"`, [iterations](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-iterations): `"100"`, [tolerance](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-tolerance): `"1e-8"`):

See. `Newton` is the best choice for most models, converging quadratically in ~2–3 iterations. With [warmstart](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-warmstart) and early termination enabled by default, the `100` -iteration cap is rarely reached: tightening tolerance (e.g. `1e-10`) improves constraint accuracy cheaply, while capping iterations to `2–4` (or loosening tolerance) skips the final polishing step when maximizing speed. Switch to `CG` only when Hessian factorization dominates step time, such as on very large particle or high-fill-in scenes, or under heavy active-set churn across many slipping contacts. `PGS` is rarely warranted, with the exception of reduced-contact scenes (roughly `ncon < nv`) like legged locomotion.

**Friction cones, impratio, and NoSlip** ([cone](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-cone): `"pyramidal"`, [impratio](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-impratio): `"1"`, [noslip\_iterations](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-noslip-iterations): `"0"`):

`elliptic` cones model isotropic Coulomb friction and decouple tangential from normal impedance at modest extra cost over `pyramidal` cones. When grasp stability or foot slip on slopes matters (see ), set `cone="elliptic"` and raise impratio (`10` for manipulation, `10–100` for legged locomotion) to stiffen tangential resistance without raising the friction coefficient (avoid large impratio with `pyramidal` cones). For residual, `noslip_iterations` of `1–3` suppresses drift strongly, at roughly 2x step time, ill-defined inverse dynamics, and occasional chatter in overconstrained grasps.

**Jacobian sparsity** ([jacobian](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-jacobian): `"auto"`):

`dense` and `sparse` compute identical physics. The `auto` threshold (`nv = 60`) is usually fine, though medium-sized models are worth timing both ways. With `sparse` `Newton` on rigid scenes, declare moving bodies that contact many objects (such as a tray) *before* those objects in worldbody to avoid Cholesky fill-in (models with flex elements reorder DOFs automatically when beneficial); see.

**Situational flags and overrides**:

- [sleep](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-sleep) (`"disable"`): freezes settled kinematic trees below [sleep\_tolerance](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-sleep-tolerance), giving large speedups in scenes with resting clutter or piles.
- [diagexact](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-diagexact) (`"disable"`): computes the exact constraint-space inertia diagonal at runtime rather than the compile-time `qpos0` approximation; useful when bodies operate far from `qpos0` or have strongly anisotropic inertias (see ).
- ([override](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-override): `"disable"`, o\_solref, o\_solimp, o\_margin, o\_friction): globally replaces contact parameters at runtime, useful in [Studio](https://mujoco.readthedocs.io/en/stable/studio/native_viewers.html#studioapp) for sweeping contact softness interactively before editing defaults.

### Model parameters

**Solver parameters** (: `"0.02 1"`,: `"0.9 0.95 0.001 0.5 2"`):

- solref: the `20 ms` default time constant (`solref[0] = 0.02`) is 10x the default `2 ms` timestep, often too soft for rigid contacts and loop-closure equality constraints (roughly speaking, a hard rubber surface). Rigid contacts usually prefer lowering it to `0.004–0.01` and loop closures to `0.004–0.005`, keeping `solref[0] >= 2 * timestep`. Note that in `(timeconst, dampratio)` format, raising `dampratio` at fixed `timeconst` lowers stiffness ($k \propto 1/(\tau^2 \zeta^2)$) rather than adding damping; to tune stiffness and damping independently (e.g. for or [system identification](https://mujoco.readthedocs.io/en/stable/python.html#pysysid)), use the direct `-stiffness -damping` format.
- solimp: rest penetration and static-friction creep both scale with `1 - d_0` (static friction sees zero position residual and therefore uses only `solimp[0]`; see ), so raising `d_0` from `0.9` to `0.95` halves both, but costs solver iterations, especially with `CG` and `PGS`. Lowering solref and switching to `elliptic` cones are much stronger levers, so try those first. `d_w` (`solimp[1]`) only applies at penetrations approaching `width` (`solimp[2]`, default `1 mm`); scale `width` to the compliant layer or object size, and do not confuse solimp with solref (`solimp="0.01 1 ..."` sets `d_0 = 0.01`, nearly disabling the constraint).

**Collision detection and filtering** ([contype](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-contype): `"1"`, [conaffinity](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-conaffinity): `"1"`):

See [Collision detection](https://mujoco.readthedocs.io/en/stable/computation/index.html#collision). Every geom both renders and collides by default; put visual meshes in a class with `contype="0" conaffinity="0"` to keep them out of collision detection, and when inferring inertia from geoms, use [inertiagrouprange](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-inertiagrouprange) or `density="0"` to compute inertia from either the visual mesh or the collision geoms rather than counting both. Replacing collision meshes with primitives (`sphere`, `capsule`, `box`, `cylinder`) improves *both* speed and contact normals: dedicated pair functions (see [engine\_collision\_driver.c](https://github.com/google-deepmind/mujoco/blob/main/src/engine/engine_collision_driver.c)) are much cheaper than generic convex `mjc_Convex` CCD and far cheaper than `sdf` collisions. Where meshes are unavoidable, decimate or [convex-decompose](https://mujoco.readthedocs.io/en/stable/computation/index.html#codecomposition) them, cap [maxhullvert](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-mesh-maxhullvert), prune pairs via contype/conaffinity or [exclude](https://mujoco.readthedocs.io/en/stable/XMLreference.html#contact-exclude), and attach a thread pool with [mju\_threadpool](https://mujoco.readthedocs.io/en/stable/APIreference/APIfunctions.html#mju-threadpool) when narrowphase dominates. For fast-moving or thin convex geoms, the [speculative](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-speculative) flag (`"disable"`) adds contacts before impact to prevent tunneling, at a scene-dependent collision cost (see ).

**Contact dimension, friction, and mixing** ():

- [condim](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-condim) (`"3"`): `"3"` models sliding friction only. Set `"4"` (torsional) or `"6"` (torsional + rolling) on fingertips, grasp pads, and curved objects that should settle on flat surfaces rather than roll indefinitely (raising rolling `friction[2]` from its `0.0001` default when needed), keeping `"3"` elsewhere; note `friction[1]` and `friction[2]` have units of *length* (contact-patch radii). For frictionless contacts use `condim="1"` rather than near-zero `friction` (under `pyramidal` cones, facet regularization scales as $\mu^2$, severely ill-conditioning tiny-friction contacts; use `cone="elliptic"` if very low friction is needed).
- [priority](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-priority) (`"0"`) and mixing: equal-priority geoms average solref/solimp and take the **maximum** condim and element-wise friction (so a low-friction object on a `friction="1"` floor gets `"1"`). Set `priority="1"` on the geom whose parameters should govern.
- [margin](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-margin) and [gap](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-gap) (`"0"`): leave `margin="0"` unless paired with matching `gap`, otherwise contact forces activate at a distance and objects hover by `margin - gap`.

**Joints: armature, damping, and frictionloss** ([armature](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint-armature): `"0"`, [damping](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint-damping): `"0"`, [frictionloss](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint-frictionloss): `"0"`):

Geared actuators add reflected rotor inertia ($I_{\text{rotor}} N^2$) that often exceeds the link inertia of wrists, fingers, and ankles; adding realistic armature improves realism, mass-matrix conditioning, and timestep stability for free. Viscous joint damping likewise enters $M + hD$ implicitly (even under `Euler`) and damps chatter at no solver cost, whereas dry frictionloss adds an active constraint row per joint; reserve it for joints where Coulomb stiction matters.

**Actuator gains and force limits** ([position](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-position), [forcerange](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-general-forcerange)):

See. A position actuator defaults to `kv="0"` and unlimited force. Pair `dampratio="1"` (computed at `qpos0` from reflected inertia including armature, or set kv directly) with `implicitfast` and bound output via forcerange so large setpoint steps do not inject excessive contact impulses; for combined position, velocity or feedforward commands, use a single [pid](https://mujoco.readthedocs.io/en/stable/XMLreference.html#actuator-pid) rather than stacking actuators and clamping their sum at the joint (see ). While forcerange (or joint [actuatorfrcrange](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-joint-actuatorfrcrange)) is saturated the actuator adds no implicit damping, so a single step can accelerate a light link by up to `h * forcerange / M`; give such joints some armature and passive joint damping (which stays implicit during saturation), or use a smaller timestep. Keep ctrlrange within joint range so servos do not fight joint limits, except on grippers where extending slightly past pad contact lets a closed command generate grip force on thin objects.

**Masses and inertias** ([inertial](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-inertial), [mass](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-mass), [density](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-geom-density): `"1000"`):

When inertial and geom mass are omitted, MuJoCo infers mass and inertia from geom volume assuming water density (`1000 kg/m^3`), which can badly misestimate hollow shells or dense metal links (for thin 2D or non-watertight meshes, set [inertia](https://mujoco.readthedocs.io/en/stable/XMLreference.html#asset-mesh-inertia) `="shell"` on mesh so compile-time volume calculation does not fail). Mass or inertia ratios `> 1000:1` across contacts or joints (a heavy robot grasping a gram-scale object, or URDF dummy links with `1e-6` inertia) also degrade solver conditioning and accuracy; fix implausible CAD/URDF inertias at the source, or clamp messy imports at compile time with [boundmass](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-boundmass) and [boundinertia](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler-boundinertia).

### Deformables

**Parametrization** ([dof](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp-dof): `"full"`):

A deformable body approximates a continuum with infinitely many degrees of freedom, so its discretization is the sharpest form of the speed–fidelity trade-off: the same shape can be represented with a few dozen dofs or with tens of thousands, and cost grows quickly with their number. The default `full` gives every vertex three dofs, so cost scales with mesh resolution. Interpolated `trilinear` and `quadratic` flexes instead move the mesh with a coarse grid of nodes (refined with [cellcount](https://mujoco.readthedocs.io/en/stable/XMLreference.html#body-flexcomp-cellcount)), decoupling cost from mesh resolution while collisions still use the full mesh. Use `trilinear` unless the body is a true thin rod or plate, or undergoes extremely large deformations with a lot of bending; `quadratic` captures bending without shear locking at higher cost. Model thin rods as `dim="1"` flexes with an elasticity section and thin plates as `dim="2"` shells, which are far cheaper than 3D volumes. Flexes whose parent body has joints must [pin](https://mujoco.readthedocs.io/en/stable/XMLreference.html#flexcomp-pin) at least one vertex to it.

**Integrator and solver** ([integrator](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-integrator): `"discrete"`, [solver](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-solver): `"Newton"`):

Flex [elasticity](https://mujoco.readthedocs.io/en/stable/XMLreference.html#flex-elasticity) is usually the stiffest force in a deformable model, and only `discrete` integrates it implicitly in position. Under `implicit` and `implicitfast` it raises a runtime error, while `Euler` integrates it explicitly and needs sub-millisecond timesteps; with `discrete`, `1–4 ms` is typical. `Newton` (the default) is the best choice under `discrete` – especially for stiff rods, shells, cloth, and [ipc](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-ipc) contact – typically with tolerance `1e-6` (raising iterations to `150–400` only in very contact-rich scenes). Prefer `CG` (typically with tolerance `1e-5` – `1e-6`) in two cases: multi-cell `equality="strain"` grids (whose dense per-cell constraint blocks cause heavy Cholesky fill-in) and large but relatively soft 3D meshes (where `CG` converges in a few cheap matrix-free iterations without 3D fill-in). `PGS` and noslip\_iterations are not supported with flex; see [Integrators](https://mujoco.readthedocs.io/en/stable/computation/index.html#geintegrators) for current limitations.

**Stiffness and damping** ([elasticity](https://mujoco.readthedocs.io/en/stable/XMLreference.html#flex-elasticity), [edge](https://mujoco.readthedocs.io/en/stable/XMLreference.html#flexcomp-edge-equality)):

For quick but approximate simulations, edge equality constraints (`true`, or `strain` for interpolated flexes) work under `implicitfast` or `Euler`, but are typically softer than the material they stand for; they do not inherit the equality default, so set solref on edge explicitly. For accurate deformations, use continuum young/poisson (plus thickness and elastic2d for shells) with Rayleigh [damping](https://mujoco.readthedocs.io/en/stable/XMLreference.html#flex-elasticity-damping) (units of time, `0.002` – `0.05`) under `discrete`; since 1D elasticity is bending-only, rods combine it with edge equality for stretching. Avoid edge stiffness and damping, which are explicit and rejected by `discrete`.

**Contact** ([selfcollide](https://mujoco.readthedocs.io/en/stable/XMLreference.html#flex-contact-selfcollide): `"auto"`, [passive](https://mujoco.readthedocs.io/en/stable/XMLreference.html#flex-contact-passive): `"false"`):

Set `selfcollide="none"` unless the flex folds onto itself. `passive="true"` replaces flex-flex, self and static-geom contact rows with an implicit penalty force, cheaper and more stable in piled cloth, but frictionless, so keep it off where grip or resting friction matters. The experimental [ipc](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-ipc) flag gives intersection-free (but also frictionless) contact for thin 2D flexes, and requires `Newton`.

### System identification

Interactive tuning establishes numerical stability, throughput, and qualitative behavior, whereas matching a *specific physical system* (sim-to-real) is best cast as optimization against hardware logs. Rather than hand-tuning joint armature, damping, frictionloss, actuator gains (kp, kv), link inertias, or, the Python [mujoco.sysid](https://mujoco.readthedocs.io/en/stable/python.html#pysysid) toolbox fits these parameters directly to recorded control and sensor trajectories via box-constrained nonlinear least squares over batched parallel rollouts.

[^1]: (1) [#](#equation-eq-constraint "Permalink to this equation") $\ac + d \cdot (b v + k r) = (1 - d)\cdot \au$

Again, the parameters that are under the user’s control are $d, b, k$. The remaining quantities are functions of the system state and are computed automatically at each time step.

[^2]: (2) [#](#equation-eq-solref-standard "Permalink to this equation") $\begin{aligned}
b &= 2 / (d_\mathrm{w}\cdot \text{timeconst}) \\
k &= d(r) / (d_\mathrm{w}^2 \cdot \text{timeconst}^2 \cdot \text{dampratio}^2) \\
\end{aligned}$

The timeconst parameter should be at least two times larger than the simulation time step, otherwise the system can become too stiff relative to the numerical integrator (especially when Euler integration is used) and the simulation can go unstable. This is enforced internally, unless the [refsafe](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag-refsafe) attribute of [flag](https://mujoco.readthedocs.io/en/stable/XMLreference.html#option-flag) is set to false. The $\text{dampratio}$ parameter would normally be set to 1, corresponding to critical damping. Smaller values result in under-damped or bouncy constraints, while larger values result in over-damped constraints. Combining with, we can derive the following If the reference acceleration is given using the positive number format and the impedance is constant $d = d_0 = d_\mathrm{w}$, then the penetration depth at rest is

$$
r = \au \cdot (1 - d) \cdot \text{timeconst}^2 \cdot \text{dampratio}^2
$$

Next we describe the direct format where the two numbers are $(-\text{stiffness}, -\text{damping})$. This allows direct control over restitution in particular. We still apply some scaling so that the same numbers can be used with different impedances, but the scaling no longer depends on $r$ and the two numbers no longer interact. The scaling formulas are

[^3]: (3) [#](#equation-eq-solref-direct "Permalink to this equation") $\begin{aligned}
b &= \text{damping} / d_\mathrm{w} \\
k &= \text{stiffness} \cdot d(r) / d_\mathrm{w}^2 \\
\end{aligned}$

Similarly to the derivation following, if the reference acceleration is given using the impedance is constant, then the penetration depth at rest is 

$$
r = \frac{\au (1 - d)}{\text{stiffness}}
$$
