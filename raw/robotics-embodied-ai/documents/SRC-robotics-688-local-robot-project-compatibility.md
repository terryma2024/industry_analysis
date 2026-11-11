---
source_id: SRC-robotics-688
title: Local Microduck and SO101 compatibility inspection
source_type: local_source_inspection
publisher: 本地项目源码与设计文件
source_date: 2026-11-10
evidence_grade: S
capture_method: read-only-local-lines-and-sha256
captured_at: 2026-11-10
tags: [raw/source, project-compatibility]
---

# Local compatibility evidence

Read-only inspection; no robot or simulator launched, no training, no remote host access, no changes to either robot project. Design documents prove planned interfaces, not runtime acceptance. Local untracked guide was read for orientation but not used as proof of implemented ACT collection. Microduck uv.lock has local changes; SO101 has untracked guide/handoff documents, so HEAD alone does not identify every working-tree file. All cited files below carry their own SHA256.

- Project `/Users/matianyi/Projects/microduck/microduck_rl` HEAD `29e887ecfbf5d37144759e5a9f8a176dfb83d547`
- Project `/Users/matianyi/Projects/robot_demo_001/moveit-demo` HEAD `49119c1531c20a0928b5af0713738a729e629ae6`

## AGENTS.md

Project: `/Users/matianyi/Projects/microduck/microduck_rl`

SHA256: `f7d4ae83ee740816f30f13312cc4d646f7396bc531c7980680627108abc8de1a`

### Lines 1–90

```text
1: # AGENTS.md
2: 
3: RL training environments for Microduck — a ~800 g, ~25 cm tall bipedal
4: robot with 14 Dynamixel XL330 servos — built on [mjlab](https://github.com/mujocolab/mjlab)
5: (MuJoCo Warp) with PPO (rsl_rl). Policies are trained here at 50 Hz, exported to
6: ONNX, and deployed by the runtime in the `pollen-robotics/microduck` repo on
7: the real robot. Sim2real transfer
8: is the whole point: every convention below exists because breaking it produced a
9: policy that worked in the viewer and failed on hardware.
10: 
11: ## Commands
12: 
13: ```bash
14: uv run list-envs                                    # live task registry
15: uv run train <TASK_ID> --env.scene.num-envs 4096    # train (add --hf-jobs for Hugging Face Jobs)
16: uv run train <TASK_ID> --env.scene.num-envs 64 --agent.max_iterations 5   # SMOKE TEST — always run first
17: uv run play <TASK_ID> --wandb-run-path <entity/project/run_id>
18: uv run scripts/export.py <TASK_ID> --wandb-run-path <...>   # → ONNX (bakes obs normalizer — mandatory path)
19: uv run publish --task <TASK_ID> --wandb-run-path <...> --checkpoint N --repo <user>/microduck-<name> --kind episodic --duration-s 4.0
20:                                                     # → HF Hub repo (policy.onnx + schema-2 manifest.json + README) the daemon loads via `robotctl policy add`
21: uv run scripts/infer_policy.py --walking out.onnx   # CPU MuJoCo deployment rehearsal (BAM M6 actuators as in training; --no-bam = XML PD)
22: uv run --with pytest pytest tests/
23: ```
24: 
25: A 5-iteration smoke test at 64 envs catches ~95% of config errors for cents.
26: Never launch a long run without one.
27: 
28: ## Repo map
29: 
30: - `src/mjlab_microduck/tasks/mdp.py` — ALL custom MDP functions (rewards, events,
31:   observations, commands, curricula). Add new functions here, grouped by task.
32: - `src/mjlab_microduck/tasks/microduck_*_env_cfg.py` — one cfg module per task
33:   family. `microduck_velocity_env_cfg.py` is the main walking recipe AND the
34:   shared base (robot, DR, obs, commands) other envs build on or mirror.
35: - `src/mjlab_microduck/tasks/__init__.py` — task registration (base + `-Backlash-` variants).
36: - `src/mjlab_microduck/tasks/backlash.py` — wraps any env cfg into its backlash twin.
37: - `src/mjlab_microduck/robot/microduck_constants.py` — robot cfgs, HOME frame, BAM actuator cfg.
38: - `src/mjlab_microduck/robot/microduck/` — MJCF exports from Onshape
39:   (onshape-to-robot, one `config_mjcf_*.json` per model) + scenes + `add_backlash.py`.
40: - `src/mjlab_microduck/actuator/friction_dr_bam.py` — BAM actuator + friction DR + backlash encoder.
41: - `src/mjlab_microduck/export.py` — the ONNX export (normalizer baked in); `scripts/export.py` wraps it.
42: - `src/mjlab_microduck/publish/` — `uv run publish`: schema-2 manifest builder + ONNX shape/smoke
43:   gate + Hub upload. Contract = `docs/policy-manifest.md` in the `microduck` repo; only
44:   constant-command episodic/perpetual policies are publishable (phase/posture-flag are the set's).
45: - `scripts/` — export wrapper, infer, sim2real comparison, wandb helpers.
46: - `tests/` — cfg-invariant and mdp-function regression tests (CPU, no GPU needed).
47: 
48: ## Invariants — do not break these
49: 
50: - **Obs layout is 61D (actor) and shared across the whole policy family** so
51:   policies are hot-swappable in the runtime: 48 base proprioception +
52:   13D command block `[twist(3), head_pose(4), body_pose(6)]`, in that order.
53:   An env that doesn't use a command slot ZERO-PADS it (keep the obs term,
54:   sample tiny ranges) — never delete a slot.
55: - **Joint layout** (14 servos, ctrl idx = joint idx on walk/groundcontact
56:   models): 0–4 left leg (hip_yaw, hip_roll, hip_pitch, knee, ankle), 5–8
57:   neck/head (neck_pitch, head_pitch, head_yaw, head_roll), 9–13 right leg.
58:   On roller/backlash models, passive joints INTERLEAVE — never hardcode joint
59:   indices in mdp functions; use the `_servo_joint_ids` / `_servo_joint_pos`
60:   helpers in mdp.py (identity on plain models, correct everywhere else).
61: - **Unactuated joints are all named `passive_*`** (wheels, backlash hinges).
62:   Every actuator/obs/reward selector uses `^(?!passive_).*` — keep the prefix
63:   convention when adding joints, and new `passive_` regexes must not
64:   accidentally match backlash joints (`^passive_.*wheel`, not `^passive_.*`).
65: - **Actuators are BAM** (voltage-controlled XL330 model, friction computed by
66:   the actuator). Two consequences: any STANDALONE env cfg must register the
67:   `expand_bam_friction_fields` startup event, and joint-friction DR must scale
68:   the actuator's `friction_scale` — `dof_frictionloss` is zeroed under BAM, so
69:   randomizing it is a silent no-op.
70: - **Obs normalization is ON** → the normalizer must be baked into the ONNX.
71:   `scripts/export.py` does this; in-sim play hides the bug (it applies the
72:   normalizer anyway), so never hand-convert a checkpoint.
73: - **Policies are UNFILTERED** (no action low-pass in training). Don't add EMA
74:   filtering without a matched runtime flag and a transfer test — trained-with /
75:   deployed-without (either direction) breaks transfer.
76: - **Domain randomization must not accumulate across resets.** mjlab 1.3.0's
77:   `dr.*` ops with `operation="add"/"scale"` are natively non-accumulating (they
78:   re-read compile-time defaults); custom DR functions must restore-then-apply.
79:   An accumulating CoM randomizer once degraded every long run for months.
80: - If an obs is remapped to a sensor view (backlash encoder, bias), any tracking
81:   REWARD on the same quantity must measure the same view — otherwise the policy
82:   is punished for correcting what it sees.
83: - `-Backlash-` task variants must mirror their base task's robot model
84:   (walk / groundcontact / rollers) so backlash A/B comparisons are unconfounded.
85: 
86: ## Building a new env — the workflow
87: 
88: 1. **Pick the closest template** and build on it, don't start from scratch:
89:    locomotion → the velocity recipe; episodic trick ending in a pose →
90:    standup; commanded two-state → sitstand; dynamic maneuver → roulade
```

## pyproject.toml

Project: `/Users/matianyi/Projects/microduck/microduck_rl`

SHA256: `e4f73a9f9aff14826463aee558f53900307ba973a287fb3bfc27a8954a131026`

### Lines 1–45

```text
1: [build-system]
2: requires = ["uv_build>=0.8.19,<0.9.0"]
3: build-backend = "uv_build"
4: 
5: [project]
6: name = "mjlab-microduck"
7: version = "0.1.0"
8: description = "RL training environments for the Microduck robot, built on mjlab"
9: readme = "README.md"
10: license = "Apache-2.0"
11: license-files = ["LICENSE"]
12: # <3.13: bam (better-actuator-models) pins requires-python <3.13, and jobs must
13: # run the same interpreter we test locally (3.12) — a floating upper bound let
14: # HF jobs pick 3.13.14 (2026-07-21).
15: requires-python = ">=3.12, <3.13"
16: dependencies = [
17:     "mjlab==1.3.0",
18:     "warp-lang==1.12.0",
19:     # BAM distribution name is `better-actuator-models`; the import stays `bam`.
20:     "better-actuator-models",
21:     "onnxruntime>=1.24.4",
22:     "rustypot>=1.4.2",
23:     "huggingface_hub>=0.27.0",
24:     "matplotlib>=3.10.9",
25:     # mjlab 1.3.0 imports scipy (terrains/heightfield_terrains.py) but forgets
26:     # to declare it — without this line a fresh `uv sync` (e.g. on HF jobs)
27:     # can't even `import mjlab_microduck` (found 2026-07-21).
28:     "scipy>=1.16",
29:     # Direct dep ONLY so [tool.uv.sources] can bind torch to the CUDA index on
30:     # aarch64 (see the torch source below) — uv applies sources to DIRECT
31:     # dependencies only, so as a purely transitive dep (mjlab, rsl_rl) the
32:     # source entry is silently ignored.
33:     # Pinned to the exact version uv.lock already resolved from PyPI so this
34:     # changes only the SOURCE of the wheel on aarch64, not the version: a
35:     # floating `>=` lets the CUDA index (which carries newer builds than the
36:     # PyPI pin) drag torch 2.9.1 -> 2.13.0, an unvetted bump for mjlab/rsl_rl.
37:     "torch==2.9.1",
38: ]
39: 
40: [project.entry-points."mjlab.tasks"]
41: mjlab_microduck = "mjlab_microduck.tasks"
42: 
43: [project.scripts]
44: # This name collides with mjlab's `train` ON PURPOSE and must stay declared.
45: # Same-name console scripts are last-writer-wins and both dist-info RECORDs
```

## src/mjlab_microduck/tasks/microduck_velocity_env_cfg.py

Project: `/Users/matianyi/Projects/microduck/microduck_rl`

SHA256: `75a0430b814ac7495eb237ab806fbd4dd10309b9fd3027ac3eee3c2e3c5a944a`

### Lines 1–58

```text
1: """Microduck velocity (walking) environment.
2: 
3: The main locomotion task: velocity-command tracking + head-pose commands.
4: The reward/regularization recipe is locomotion-focused (lean tracking +
5: gait/feet terms, curriculum-ramped action-rate smoothing), with:
6: 
7:   - foot_slip kept at -0.1 (deliberately weak — stronger was too restrictive
8:     for this robot's pivot-heavy turning)
9:   - fixed, modest command ranges (ang ±1.0 makes turning learnable) instead of
10:     a widening curriculum that outpaced the robot's capability
11:   - turn-in-place: 15% of envs get lin=0 + |ang| ∈ [0.4, 1.0] (2026-07 audit:
12:     independent uniform sampling makes spin-on-the-spot ~2% of data → untrained)
13:   - head_pose_tracking as a primary objective, plus an EMA-based head_pose_bias
14:     penalty that prices only the escapable DC head droop (see below)
15:   - body_pose tracking infra kept intact but DISABLED (weight 0) so the obs
16:     slot stays alive for envs that use it
17: """
18: 
19: import math
20: from copy import deepcopy
21: 
22: NUM_STEPS_PER_ENV = 24
23: 
24: # Fraction of envs commanded to spin on the spot (lin=0, |ang| ∈ [0.4·max, max]).
25: TURN_IN_PLACE_FRACTION = 0.15
26: 
27: # Symmetry
28: ENABLE_SYMMETRY = False
29: 
30: # Domain randomization toggles
31: ENABLE_COM_RANDOMIZATION = True
32: ENABLE_HEAD_COM_RANDOMIZATION = True  # Randomize CoM of the head assembly bodies
33: ENABLE_KP_RANDOMIZATION = False # Was True
34: ENABLE_KD_RANDOMIZATION = False # Was True
35: ENABLE_MASS_INERTIA_RANDOMIZATION = True  # Can enable once walking is stable
36: ENABLE_JOINT_FRICTION_RANDOMIZATION = True  # Scales BAM's friction budget per-env via FrictionDRBamActuator.friction_scale
37: ENABLE_JOINT_DAMPING_RANDOMIZATION = False
38: ENABLE_ARMATURE_RANDOMIZATION = True  # Reflected rotor inertia (microban-style). DOES affect BAM (armature is set, not zeroed).
39: ENABLE_VELOCITY_PUSHES = True  # Velocity-based pushes for robustness training
40: ENABLE_IMU_ORIENTATION_RANDOMIZATION = True  # Simulates mounting errors
41: ENABLE_ENCODER_BIAS = True  # Per-env joint encoder calibration offset (actor obs sees joint_pos + bias)
42: ENABLE_BASE_ORIENTATION_RANDOMIZATION = False  # Randomize initial tilt to force reactive behavior
43: 
44: # Head/body pose command tracking (replaces the old neck-offset disturbance scheme).
45: # Head pose: 4D deltas-from-HOME on neck/head joints; vel env tracks these as a
46: # primary objective. Body pose: 6D delta in [x, y, z, roll, pitch, yaw]; vel env
47: # samples small ranges + tiny reward weight so input neurons stay alive but
48: # tracking isn't the priority (standup env raises the weight).
49: HEAD_POSE_CMD_RESAMPLE_S = (2.0, 5.0)
50: BODY_POSE_CMD_RESAMPLE_S = (2.0, 5.0)
51: 
52: # Observation configuration
53: USE_PROJECTED_GRAVITY = True  # If True, use projected gravity instead of raw accelerometer
54: 
55: # Domain randomization ranges (adjust as needed)
56: # Conservative ranges proven to be stable - can increase gradually if needed
57: COM_RANDOMIZATION_RANGE = 0.003  # ±3mm initial, ramped to ±8mm via curriculum
58: # Head CoM randomization: applied per-episode to every body of the head assembly
```

### Lines 550–580

```text
550:         # Remove projected_gravity and add raw_accelerometer
551:         del cfg.observations["actor"].terms["projected_gravity"]
552:         cfg.observations["actor"].terms["raw_accelerometer"] = ObservationTermCfg(
553:             func=microduck_mdp.raw_accelerometer,
554:             scale=1.0,
555:         )
556: 
557:     cfg.observations["actor"].terms[gravity_term_name] = deepcopy(
558:         cfg.observations["actor"].terms[gravity_term_name]
559:     )
560:     cfg.observations["actor"].terms["base_ang_vel"] = deepcopy(
561:         cfg.observations["actor"].terms["base_ang_vel"]
562:     )
563: 
564:     cfg.observations["actor"].terms["base_ang_vel"].delay_min_lag = 0
565:     cfg.observations["actor"].terms["base_ang_vel"].delay_max_lag = 1  # was 3 (=60 ms worst case); real dxl IMU path is fast — ±20 ms envelope (2026-07 audit)
566:     cfg.observations["actor"].terms["base_ang_vel"].delay_update_period = 64
567: 
568:     cfg.observations["actor"].terms[gravity_term_name].delay_min_lag = 0
569:     cfg.observations["actor"].terms[gravity_term_name].delay_max_lag = 1  # was 3 (=60 ms worst case); real dxl IMU path is fast — ±20 ms envelope (2026-07 audit)
570:     cfg.observations["actor"].terms[gravity_term_name].delay_update_period = 64
571: 
572:     # The critic's sensor-derived terms are the one obs path `nan_state` cannot
573:     # protect (it checks joint + root state; these read raycast/contact sensor
574:     # data, which MuJoCo can return non-finite for while the state is still
575:     # clean). A single NaN here kills the whole run via rsl_rl's check_nan —
576:     # that is the 2026-08-21 Velocity2-Rough-Backlash crash. Critic-only, so
577:     # sanitizing costs the policy nothing.
578:     for _term, _safe in (
579:         ("foot_contact_forces", microduck_mdp.foot_contact_forces_safe),
580:         ("foot_height", microduck_mdp.foot_height_safe),
```

### Lines 635–705

```text
635:         cfg.events.pop("encoder_bias", None)
636: 
637:     # Commands — deepcopy to avoid shared-state corruption from other env cfgs
638:     # (make_velocity_env_cfg() returns objects with shared mutable references;
639:     # standup/ground_pick envs mutate commands["twist"] in place, zeroing ranges)
640:     command: UniformVelocityCommandCfg = deepcopy(cfg.commands["twist"])
641:     cfg.commands["twist"] = command
642:     command.rel_standing_envs = 0.02  # small but non-zero from the start, ramped up by curriculum
643:     command.rel_heading_envs = 0.0
644:     # Modest, FIXED command ranges (no widening curriculum): a ramp to
645:     # lin ±0.4 / ang ±2.0 outpaced the robot's capability and tracked a
646:     # post-iter-1000 reward/episode-length decline. ang ±1.0 is the big
647:     # change — it makes turning learnable.
648:     command.ranges.lin_vel_x = (-0.4, 0.4)
649:     command.ranges.lin_vel_y = (-0.3, 0.3)
650:     command.ranges.ang_vel_z = (-1.0, 1.0)
651:     command.viz.z_offset = 0.5
652:     cfg.commands["twist"] = microduck_mdp.VelocityCommandCommandOnlyCfg(**vars(command))
653:     # Explicit turn-in-place bucket (see TURN_IN_PLACE_FRACTION above).
654:     cfg.commands["twist"].rel_turn_in_place_envs = TURN_IN_PLACE_FRACTION
655: 
656:     # Head pose command (4D deltas from HOME, in joint order:
657:     #   neck_pitch, head_pitch, head_yaw, head_roll). Tracked as a primary
658:     # reward — see "head_pose_tracking" added below. Initial ranges are small
659:     # non-zero so input neurons stay alive from step 0; curriculum widens them.
660:     # Per-joint final caps reflect each joint's mechanically reachable delta
661:     # from HOME (XML limits minus HOME offset, with ~10% safety margin):
662:     #   neck_pitch / head_pitch: ±1.10 rad (limit ±π/2 with HOME=±20°)
663:     #   head_yaw                : ±1.40 rad (limit ±π/2 with HOME=0)
664:     #   head_roll               : ±0.31 rad (limit ±20°)
665:     # Initial ranges are small non-zero so input neurons stay alive from step 0.
666:     cfg.commands["head_pose"] = microduck_mdp.UniformPoseCommandCfg(
667:         resampling_time_range=HEAD_POSE_CMD_RESAMPLE_S,
668:         ranges=(
669:             (-0.05, 0.05),    # neck_pitch
670:             (-0.05, 0.05),    # head_pitch
671:             (-0.07, 0.07),    # head_yaw
672:             (-0.015, 0.015),  # head_roll (tighter — much smaller mechanical range)
673:         ),
674:     )
675:     # Body pose command (6D delta from nominal standing: [x, y, z, roll, pitch, yaw]).
676:     # Vel env carries this slot for runtime obs-shape parity; tracked at a tiny
677:     # weight to keep the input neurons alive but not steer the policy. The
678:     # standup env raises the weight + widens the ranges.
679:     cfg.commands["body_pose"] = microduck_mdp.UniformPoseCommandCfg(
680:         resampling_time_range=BODY_POSE_CMD_RESAMPLE_S,
681:         ranges=(
682:             (-0.005, 0.005),  # x (m)
683:             (-0.005, 0.005),  # y (m)
684:             (-0.005, 0.005),  # z (m)
685:             (-0.05, 0.05),    # roll (rad)
686:             (-0.05, 0.05),    # pitch (rad)
687:             (-0.05, 0.05),    # yaw (rad)
688:         ),
689:     )
690: 
691:     # Append head + body command obs terms to both policy and critic groups.
692:     # Order matters for the runtime obs layout: [twist(3), head_pose(4), body_pose(6)].
693:     for group in ("actor", "critic"):
694:         cfg.observations[group].terms["head_command"] = ObservationTermCfg(
695:             func=mdp.generated_commands,
696:             params={"command_name": "head_pose"},
697:         )
698:         cfg.observations[group].terms["body_command"] = ObservationTermCfg(
699:             func=mdp.generated_commands,
700:             params={"command_name": "body_pose"},
701:         )
702: 
703:     # === Pose tracking rewards ===
704:     # head_pose: primary objective in vel env — the whole point of the rewrite.
705:     # std=0.5 with per-joint Gaussian (see head_pose_tracking in mdp.py): at the
```

## docs/superpowers/specs/2026-09-10-so101-act-head-wrist-rgb-design.md

Project: `/Users/matianyi/Projects/robot_demo_001/moveit-demo`

SHA256: `f9efa395ecc88606dd674e16a8222a29b36b3555f8218fec0b3b69c186a7f660`

### Lines 1–82

```text
1: # SO-101 双 RGB 视角 ACT、颈部搜索与随机示教设计
2: 
3: 2026-10-05 优先修订：[Teacher 执行与 ACT 数据验证分离](2026-10-05-so101-teacher-act-decoupling-amendment.md)。Teacher 按起终点杯子 Pose 和最终直立结果判定任务；过程质量项以审计为主，保留真正的执行保护。ACT 采集/QC 故障不得阻断或撤销 Teacher 运动，数据标准和用途隔离不放宽。下文冲突条款以该修订为准；用户已授权现有 ai-station Claude 更新计划、清理旧逻辑/测试并执行，尚未形成新运行验收。
4: 
5: 日期：2026-09-10
6: 
7: 2026-10-01 验收修订：[共用端点 Pose 验收](2026-10-01-so101-act-endpoint-pose-acceptance-design.md) 按用户要求替代本文的物体过程质量成功条件，覆盖正式采集、并行资格和 ACT rollout。经验阈值运行前冻结；动作安全、Head 搜索、数据 QC 和用途门禁保持独立。本次文档修订不表示代码或资格已更新。
8: 
9: 更新：2026-09-24，按 `main` 的 fixed exact-N v3 shared queue、统一 Web 全局仲裁和八 Worker 测试门重写并行采集与训练边界；ACT 单次运行上限仍为 2 分钟。
10: 
11: 补充设计：[Task 8 live 与正式采集设计](2026-09-24-so101-act-task8-live-formal-collection-design.md) 收紧 Task 7A 至 Task 11A。仿真后端仅支持 MuJoCo；资源绑定只在 campaign 启动入口校验；W2 通过后直接测试独立 40 场景 W8，不再测试 W4/W6。相关内容与本文冲突时，以补充设计为准。
12: 
13: 状态：已确认方案的设计汇总，供实现与审阅使用。本文不代表相机、控制器、数据集或 ACT 已完成运行验收。
14: 
15: ## 1. 目标与课程范围
16: 
17: 在 MuJoCo 中为 SO-101 增加 head 与 wrist 两台普通 RGB 相机。独立搜索状态机控制单轴颈部 yaw，发现杯子后锁定头部；ACT（Action Chunking with Transformers）根据双相机 RGB、机械臂状态和头部朝向控制手臂与夹爪。MoveIt 2 提供示教动作，杯子在经过验证的可抓取区域内连续随机分布。
18: 
19: 保留 V5-T001～V5-T005 的 Agent、感知与几何规划链路。本文对应 V5-T006～V5-T010 的 ACT 支线，后续实现属于 `src/so101_demo_py`，Teleop 集成属于 `src/so101_teleop`。实体机械臂迁移属于 V6，仿真验收不能替代实机验收。
20: 
21: 课程当前“至少 50 个有效 episode、至少 3 个位置”是原始最低要求。本设计采用更严格的数据方案：至少 50 个训练、10 个离线验证、10 个离线测试 episode，另设至少 10 个可重复使用的闭环验证初始条件，以及至少 10 个无专家示教的封存闭环测试初始条件。本文更新设计口径；公共课程条目与个人进度不随本文自动修改。
22: 
23: ## 2. 已确认决策
24: 
25: | 项目 | 决策 |
26: | --- | --- |
27: | ACT 图像输入 | 仅 `head_camera` 与 `wrist_camera` 的 RGB |
28: | ACT 深度输入 | 不使用 Depth，也不使用由 Depth 派生的目标坐标 |
29: | task_camera | 保留既有 RGB-D 教师链路，不进入 ACT 输入 |
30: | 头部安装 | 机械臂上方固定支架，单个 yaw 电机，固定斜向下俯角 |
31: | 颈部运动 | 仿真支持 360°；有限速、加速度限制、超时和单次扫描预算 |
32: | 默认朝向 | 朝向预先配置的默认杯子区域，不随杯子真值自动转向 |
33: | neck 控制权 | 独立搜索状态机 |
34: | 搜索策略 | 固定角度步进扫描、轻量物体检测、水平居中；不使用 ACT |
35: | 搜索输出 | 锁定结果、杯子视线方位、neck 实测角及时间戳；不输出三维位置 |
36: | ACT 控制权 | SO-101 五个手臂关节与夹爪，不包含 neck |
37: | ACT 运行上限 | 单次 attempt 最长 120 s（2 分钟），按单调墙钟计时；包含推理等待、抓放、撤离与最终检查 |
38: | 执行时头部 | 搜索完成后锁定，ACT 运行中不追踪转头 |
39: | 抓取前目标丢失 | 停止 ACT，确认可恢复后回观察姿态并重新搜索 |
40: | 抓取确认后遮挡 | 不因检测框消失重新搜索，交由持物监督 |
41: | 示教来源 | MoveIt 教师完整 pick-place 的实际执行命令 |
42: | 杯子位置 | 可抓取区域内分层、连续随机采样；空间隔离数据划分 |
43: | 并行范围 | 首版只并行 MoveIt 专家示教采集；ACT 闭环验证和封存测试保持单场景独立执行 |
44: | 并行实现 | Linux 新执行复用 `ParallelRuntimeConfigV3`、`BatchRequestV3`、fixed exact-N shared queue、lease、终态提交、start guard 与精确清理；新增 ACT collection workload，不复用点位验证证据 schema |
45: | 并发策略 | W1 冒烟并建立语义基线；W1/W2 完成八场景功能资格后，直接以独立 40 场景测试 W8；不测试 W4/W6，也不在运行中自动降档 |
46: | 运行所有权 | Web 与 headless CLI 通过同一启动入口完成一次 admission；campaign owner 从 admission 持有 reservation 到终态与 cleanup，内部组件不复验资源 binding |
47: | GPU 所有权 | 采集、共享教师 Broker 与训练共同使用按稳定 host identity + 解析后的物理 GPU UUID 持久化的 `ActGpuWorkloadArbiter`；原 selector/可见性映射留审计，别名或映射漂移不能产生第二把锁 |
48: | 丢失数据 | `/data/work/so101-evidence/act-data/0917a` 已不可用；Git 分支只能恢复源码，不能恢复 episode、QC 或训练资格。后续采集使用新的 dataset/run ID 与新 evidence root |
49: | 训练执行 | 训练只消费 journal commit 引用且 verifier 通过的正式 episode；与采集/感知 GPU 负载串行，使用独立 Python 环境、不可变导出和独立 run root |
50: 
51: ## 3. 系统分工与信息边界
52: 
53: ```text
54: head RGB → 轻量杯子检测器 → HeadSearchController → neck controller
55:                    │
56:                    └→ TARGET_LOCKED + 方位结果 → neck 保持
57: 
58: head RGB + wrist RGB + q1…q6 + neck 朝向
59:                    ↓
60:         RgbObservationSynchronizer
61:                    ↓
62:               ActPolicyRunner
63:                    ↓
64:              ActSupervisor
65:                    ↓
66:           ActExecutionAdapter
67:                    ↓
68:        arm/gripper controllers → MuJoCo
69: 
70: 示教时：task_camera RGB-D → 感知/tf2 → MoveIt 教师
71:                                       ↓
72:                                执行命令记录
73:                                       ↓
74: 双 RGB 与实测关节 → EpisodeRecorder → ACT 数据集
75: 
76: 冻结的示教候选清单 → FixedActCollectionCampaign
77:                               ├→ BatchRequestV3 + exact-N shared queue
78:                               ├→ Worker 1：独立 ROS Domain + 完整 MuJoCo/MoveIt stack + Recorder
79:                               ├→ Worker 2：独立 ROS Domain + 完整 MuJoCo/MoveIt stack + Recorder
80:                               └→ …；共享的仅是身份隔离的教师感知 Broker 与持久调度状态
81: 
82: 统一 Web / headless authority → startup admission → AdmittedCampaignContext
```

## docs/superpowers/specs/2026-10-05-so101-teacher-act-decoupling-amendment.md

Project: `/Users/matianyi/Projects/robot_demo_001/moveit-demo`

SHA256: `0473db52c3915cbd87775ce1836f57681b48bf3a5ad228f2a05fa971cf5ce8e4`

### Lines 1–57

```text
1: # SO-101 Teacher 执行与 ACT 数据验证分离修订
2: 
3: 日期：2026-10-05
4: 状态：用户已确认两个原则，并授权 ai-station 的现有 Claude 修订执行计划、清理旧实现和测试、按新计划执行。本文经过编写者 inline self review；未宣称代码、集成或运行验收通过。
5: 
6: ## 1. 适用范围与优先级
7: 
8: 本修订适用于完整 ACT 方案中的 MoveIt Teacher 示教执行与数据采集，也适用于当前非 Head 首条采集闭环。它不是诊断模式专用的宽松规则。发生冲突时，本文优先于下列文档及其执行计划中的 Teacher/Recorder/QC 耦合、过程质量成功条件和数据故障停机条款：
9: 
10: - `2026-09-10-so101-act-head-wrist-rgb-design.md`
11: - `2026-09-24-so101-act-task8-live-formal-collection-design.md`
12: - `2026-09-28-so101-act-task8-artifact-preparation-design.md`
13: - `2026-09-29-so101-act-task8-measurement-protocol-design.md`
14: - `2026-09-30-so101-act-containerized-campaign-design.md`
15: - `2026-09-30-so101-act-nonhead-first-episode-design.md`
16: - `2026-10-01-so101-act-endpoint-pose-acceptance-design.md`
17: 
18: Head Search、ACT 模型闭环控制策略和算法不在本次实施范围。ACT rollout 的停止规则不从 Teacher 的旁路采集规则自动推导。W2 后直接独立 40 场景 exact-W8、不跑 W4/W6、正式/诊断用途隔离、CUDA/no CPU fallback 和 MuJoCo-only 保持不变；本次不启动并行资格、训练、第二套 stack 或真实硬件。
19: 
20: ## 2. 两个原则
21: 
22: Teacher 独立负责执行、运动安全和任务结果。Recorder、ACT 同步器、数据 QC 和导出筛选是旁路消费者，不是运动许可的签发者。关闭、缺失或故障的采集侧不能改变 Teacher 的规划、轨迹、动作顺序、重试策略或执行结果。
23: 
24: Teacher 的任务成功以同一杯子的起点和最终 Pose 为主要判据：杯子实际从配置的 start 区域转移到 end 区域，最终位置和高度满足容差，杯轴保持竖直、没有倾倒。过程物理检查尽量减少；抓稳、抬升高度、持续双侧接触、阶段间的物理质量窗口不再独立决定任务成功。
25: 
26: ## 3. 组件权限和数据流
27: 
28: Teacher 使用自己执行所需的 MuJoCo/ROS 状态、MoveIt 规划、controller action 和必要安全输入。其控制通道、控制租约和停止确认独立于采集结果租约、Recorder 状态、数据 seal 和 Coordinator 提交。复用已有控制器和必要的控制所有权机制，不因分离而绕过关节限制或允许多个运动所有者。
29: 
30: Teacher/仿真只向采集侧提供观测、已接受的 controller reference 和执行事件。采集侧没有 Teacher command、cancel、revoke、pause、reset 或自动业务重试权限。独立 QC 只读取已保留的文件，不连接运动控制入口。数据 finalization 超时、提交失败或采集 lease 过期不能取消仍在其独立执行期限内的 Teacher。
31: 
32: CPU/GPU/RAM/磁盘资源在启动入口按现有规则绑定一次；不能在内部组件重新申请资源。Teacher 的输入校验不再以 RGB 齐备、Recorder READY、首行成功、数据 hash/seal 或采集队列排空为运动 prerequisite。真正的执行安全配置缺失仍拒绝运动；不能把旧质量报告改名为安全报告以保留耦合。
33: 
34: ## 4. Teacher 的最小检查和结果判定
35: 
36: ### 4.1 必须保留的执行保护
37: 
38: 保留有效机器人/场景身份、合法控制所有权、关节位置/速度/加速度限制、必要的规划碰撞约束、明确危险碰撞/接触力保护、controller 失效和必要状态长期不可用的停止机制。保留用户停止、独立执行 deadline、停止后的反馈确认；控制消息不得跨 session/reset 使用。
39: 
40: Planning Scene attachment 仍只是规划 shadow，不得通过 MuJoCo 物体瞬移、人工 physics attachment 或隐藏 reset 制造成功。释放与错误处理保留真正的安全要求；无支撑且被持有的杯子出错时，不通过自动开爪来清理。必要的执行保护可以停止 Teacher，但必须记录明确的安全/控制原因，而不是数据 QC 原因。
41: 
42: 逐项审查双侧接触丢失、提前碰桌、夹取前杯子移动、微抬升验证、释放接触和阶段稳定窗口：一般过程质量项改为 audit-only，不再取消轨迹或阻止 `DONE`。只有能够说明具体危险、独立于采集也需要的条件才归入执行保护。不能把所有旧过程断言都标为“安全”保留下来，也不能把所有接触保护一并删除。计划须列出每项的去留、消费者和测试。
43: 
44: ### 4.2 起点与终点
45: 
46: Teacher 在 reset 完成后、本次首条 arm/gripper 运动前独立读取起点 Pose，不等待采集启动、相机齐备、首行或 phase-channel 的数据绑定。终点在获准动作序列结束、释放动作完成并确认 controller 停止后读取；可使用配置的短暂落稳等待，默认取 `0.5 s` 经验值，允许非负有限值覆盖。它不是速度、接触或精确连续采样门禁；可选的多帧终态观察只留诊断，不新增过程质量成功条件。
47: 
48: 起点和终点均来自实际执行世界、同一个 `object_id/body_name`、`world` frame 和本次 session/reset。目标在运行前冻结，不从实际终点反推目标。不择优选择历史帧；缺少有效终态给出 `UNCONFIRMED`，不能因证据缺失报成功。Teacher 的必要状态新鲜度按执行策略定义，不能直接继承 ACT 的 10 Hz/100 ms 数据合同，也不能要求两个不同时间的快照数值完全相同。
49: 
50: 沿用五个可配置经验容差：初始位置 `0.010 m`、初始轴 `0.15 rad`、最终 XY `0.020 m`、最终 Z `0.010 m`、最终轴 `0.15 rad`。最终杯轴是 body 局部 `+Z` 旋转到 world 后与 world `+Z` 的夹角；终点目标姿态也必须符合直立要求，不能通过冻结倾倒目标取得 PASS。不限制绕杯轴的 yaw，四元数须有效。
51: 
52: 使用版本化的新结果规则和配置，不能在旧 closed schema 偷加字段并继续声称 `endpoint_pose_v1`。现有位置/角度字段可复用，新增落稳参数由计划定义显式版本。配置在 episode/attempt 开始前冻结，记录完整生效值和 hash，不在运行后调阈值重判同一次结果。
53: 
54: start/end recipe 必须定义实际搬运任务，不能把起终目标配置为重合，然后宣称杯子被转移；不要求另一个经测量批准的最小位移阈值。端点口径不证明全程夹持或标准抓取方式，报告如实写明“杯子转移与最终直立结果通过”。
55: 
56: ## 5. ACT 采集故障只影响数据
57: 
```

## docs/superpowers/specs/2026-10-09-so101-mujoco-domain-randomization-act-design.md

Project: `/Users/matianyi/Projects/robot_demo_001/moveit-demo`

SHA256: `56c0a6de77436294019fe66a1e8613fbcba969955cc9a43f5e2a6798dbb27d48`

### Lines 1–34

```text
1: # SO-101 MuJoCo 环境随机化与 ACT 示教采集设计草案
2: 
3: 日期：2026-10-09。状态：供用户审阅，未批准实施。目标已确认：优先迁移到当前 SO-101 实机，兼顾仿真泛化。“关机阻尼”按“关节阻尼”理解。
4: 
5: 本文基于本地源码和现有设计进行静态分析，经过编写者 inline self review；未启动仿真、采集、训练或硬件动作。参数范围是试验起点，不是实机标定结果。远端 ACT 实现与运行资格未在本轮核验。
6: 
7: ## 1. 推荐路线与取舍
8: 
9: 采用“实机基线校准 → 单因素随机化 → 组合随机化 → 分层采集 → 冻结场景评估”。先把当前相机、机械臂、杯子和桌面的主要特性建对，再覆盖测量误差、安装变化、光照变化及舵机响应波动。
10: 
11: | 路线 | 收益与代价 | 本次选择 |
12: | --- | --- | --- |
13: | 实机校准后的 MuJoCo 分层随机化 | 可复用现有 MoveIt Teacher、ROS controller、Recorder；参数与失败原因可追溯 | 推荐 |
14: | 仅对已有 RGB 做颜色/背景增强 | 成本低，但不能生成新的接触响应、相机视差和受扰后的专家动作 | 作为训练侧补充 |
15: | 接入另一套写实渲染或仿真平台 | 可能改善特定成像效果，但增加资产、同步、控制和数据链路验证成本 | 暂不纳入首版 |
16: 
17: 首版保留当前杯形、机器人运动学、抓取任务和固定放置目标。杯子尺寸、可碰撞杂物及目标位置变化分别后置；它们会同时影响规划、可达域或任务可观测性，不能当作纯视觉随机化。
18: 
19: ## 2. 本地现状与设计前提
20: 
21: 本地基线为 `main@7a62d8e88f4b04fa5f20359649013a16bae909b0`，依赖子模块为 `5a590b22770b270b71ba6a1c3443d4e67edc7f4b`。已有 ACT 文档的未提交修订是本轮读取的设计输入；本文不覆盖这些文件。
22: 
23: | 已核对的源码事实 | 对设计的影响 |
24: | --- | --- |
25: | [scene.xml](../../../src/so101_demo_py/assets/mujoco/scene.xml) 有单盏主光、task_camera、固定桌面和橙色杯；杯质量 `0.020 kg`，自由关节 `damping=1.0` | 先审计杯子阻尼与落体/滑移行为，不围绕未经测量的数值盲目扩大分布 |
26: | [so101.xml](../../../src/so101_demo_py/assets/mujoco/so101.xml) 默认关节 `damping=0.60`、`frictionloss=0.052`、`armature=0.028`；指垫滑动摩擦 `3.0`；位置执行器配置 `kp`、`kv` 和力限幅 | 分别建模被动阻尼、干摩擦、伺服响应和饱和，不用一个“电机噪声”参数代替 |
27: | [ResetWorld 实现](../../../third_party/mujoco_ros2_control/mujoco_ros2_control/src/mujoco_simulation.cpp) 支持 joint/free-joint state overrides | 可复用状态重置；环境模型参数事务还需设计实现 |
28: | [CameraPlugin](../../../third_party/mujoco_ros2_control/mujoco_ros2_control_plugins/src/camera_plugin.cpp) 由 `fovy` 推导等焦距、居中主点，畸变系数为零 | 内参随机化必须同时验证实际投影和 CameraInfo，不能只改消息或 XML |
29: | [控制接口](../../../third_party/mujoco_ros2_control/mujoco_ros2_control/src/mujoco_system_interface.cpp) 将位置目标写入 `ctrl`，随后允许插件更新控制快照 | 可评估在 plant 输入边界增加延迟/偏置模型；线程、更新周期和最终生效点仍需运行验证 |
30: 
31: head/wrist RGB、8D state 和 6D action 是[现有 ACT 设计合同](2026-09-10-so101-act-head-wrist-rgb-design.md)，不是本轮确认已运行的本地功能。实施前须核对执行机实际 checkout、安装产物及当前采集资格。
32: 
33: Teacher 与采集侧的权限以[2026-10-05 分离修订](2026-10-05-so101-teacher-act-decoupling-amendment.md)为准。Recorder、QC、数据提交失败不能取消、暂停、重置 Teacher。新随机化方案也不重新引入过程质量停机条件。
34: 
```

### Lines 83–132

```text
83: ## 6. 接入现有流程
84: 
85: 新增概念组件放入现有领域/应用/adapter 分层，名称待实施计划冻结，不在本轮创建代码：
86: 
87: | 组件 | 职责 |
88: | --- | --- |
89: | RandomizationProfile | 版本化参数、单位、分布、相关性、范围、资产白名单与校准来源 |
90: | ScenarioSampler | 按冻结 split 和种子生成候选；先分配场景族，再生成变体 |
91: | SceneRealizer | 从 nominal 模型构建本次环境，管理模型/渲染/控制配置应用及读回 |
92: | AppliedSceneManifest | 保存请求值、实际生效值、模型/资产哈希、软件版本、种子和 reset generation |
93: | 现有 Teacher / Recorder / QC | Teacher 执行；Recorder 旁路记录；独立 QC 筛选数据，沿用现有封存和提交链 |
94: 
95: ```mermaid
96: flowchart TD
97:     P[校准基线与随机化 profile] --> S[冻结 split 与候选场景清单]
98:     S --> R[构建场景 / reset / 生效读回]
99:     R --> T[Teacher 独立执行]
100:     T --> E[任务端点结果]
101:     R -. 场景身份 .-> D[旁路 Recorder]
102:     T -. 观测与 accepted reference .-> D
103:     D --> Q[封存与独立 QC]
104:     E --> X[成功示教选择]
105:     Q --> X
106:     X --> I[Coordinator commit / campaign-index]
107:     I --> A[ACT 训练视图]
108: ```
109: 
110: 首轮优先以完整模型构建和 `FULL_RESTART` 建立正确性基准，测出成本后再增加 `RESET_WORLD` 快路径。不得直接声称现有 reset 服务支持完整随机化。快路径须在仿真停止、控制所有权明确时恢复 nominal，再应用新配置；禁止在上一 episode 已随机化的数值上继续乘系数。
111: 
112: 生效确认包含模型值、相机首个新 generation 的有效图像及标定、实际初始姿态。跨 reset 的相机缓存、controller reference 和扰动队列全部失效。失败发生在启动运动之前时拒绝该场景；一旦 Teacher 已执行，纯数据问题只能标为数据无效。Recorder readiness 不能成为 Teacher 运动许可。
113: 
114: 纯视觉参数变化通常不要求修改运动规划；任何几何变化都需同步规划碰撞体。候选预检只覆盖合法配置、可达性与必要碰撞安全，不要求提前成功抓放来筛掉困难样本。真实失败保留并按参数分桶，防止采集分布只剩“容易成功”的场景。
115: 
116: 物理光照、材质和背景变化也会影响 Teacher 的 task_camera 感知。分别记录 Teacher 感知失败与执行失败；不能暗中给 Teacher 保留另一套理想世界图像。若以后引入真值 Teacher，必须单独标记来源并评估示教分布变化，不与当前相机 Teacher 无标记混用。
117: 
118: ## 7. ACT 数据与采样策略
119: 
120: 沿用当前约定：head/wrist RGB `640×480`、10 Hz 仿真时间网格；state 为 `[q1..q6, sin(neck_yaw), cos(neck_yaw)]`；action 是 6D 绝对关节目标。`action[k]` 对齐 `t_k + 0.1 s` 的 accepted/executing controller reference。相机、状态以因果方式对齐，不能使用未来反馈补当前输入。搜索阶段与手臂 ACT episode 的边界遵循现有设计。
121: 
122: 随机化参数、CameraInfo、真值、接触、Teacher 阶段、实际 plant 输入只存审计侧，不进入 ACT observation。训练归一化仅使用 Train。保留原始无损 PNG/JSONL；训练侧颜色增强另存配置和种子，不覆盖原始图像。若模拟物理成像效应，其输出作为策略观测，同时保留生成配方；不能以人为制造缺帧来绕过当前连续性合同。
123: 
124: 每个 episode 绑定 `scenario_id`、`scene_family_id`、split、master seed/子种子、profile 版本与 hash、实际参数、资产 hash、base/model hash、控制及相机配置、软件版本、reset generation、Teacher 来源、执行结果及 QC 结果。随机流按几何/视觉/动力学/传感器分开派生，线程调度和 worker 数不能改变场景。支持按 manifest 重建；跨平台不承诺图像或浮点轨迹逐字节相同。
125: 
126: 五集合继续为 Train、Validation、Offline Test、Rollout Validation、封存 Rollout Test。按空间区块、底层场景族、背景资产身份及相机安装 profile 分组；同一轨迹的重渲染/增强变体必须留在同一 split。测试另外留出未见参数组合和较宽包络，分别报告插值泛化与域外泛化。
127: 
128: 第一轮建议约 100 条候选做数据链路和覆盖率检查；通过后以约 1,000 条合格训练示教为预算起点，按约 `20% nominal / 30% visual / 20% dynamics / 30% combined` 分层。具体候选配额在实测 Teacher 产出率后冻结，数量不构成训练充分性的保证。Validation 和 Offline Test 独立配额，rollout 集不进入专家采集队列。
129: 
130: 新增数据仍从真实 Coordinator journal/index 导出，不能扫描目录自动拼接。若困难桶配额不足，报告 `QUOTA_UNSATISFIED` 和失败分布；不能复制数据、扩大阈值或悄悄缩窄随机范围补齐。补采使用新清单/数据身份。分别报告合法候选数、开始执行数、Teacher 成功数、QC 合格数与可提交数。
131: 
132: 两个 RGB 相机每帧对的原始像素量为 `640×480×3×2 = 1,843,200 bytes`。按 10 Hz、60 s 估算，每条 episode 未压缩约 `1.11 GB`，1,000 条约 `1.11 TB`，尚未计其他证据。PNG 实际大小与吞吐须实测；不能用示意压缩比做磁盘准入依据。资产按 hash 复用，单条保存完整解析配置。
```

### Lines 150–160

```text
150: 实现测试重点是：seed/manifest 确定性、split 无泄漏、nominal 恢复、实际接触参数生效、投影一致性、action 标签未被 plant 扰动污染、停止/reset 清队列、Recorder 故障无反向控制。完整普通测试按各包 xdist 门禁执行；本任务不触发 perception benchmark suite。可见变化须取 fresh sensor 图像，不能只看 XML 或 viewer。
151: 
152: ## 9. 实施范围、审阅与证据
153: 
154: 拟修改范围为 `so101_demo_py` 的场景/profile、采样与 manifest、现有采集 adapter；CameraPlugin 投影/标定与控制扰动接入可能涉及 `third_party/mujoco_ros2_control`。依赖改动须独立记录来源并更新 lock。实施前在执行机核对 ACT 当前代码归属，避免凭本地设计文件创建第二套采集系统。
155: 
156: 本轮 self review 已检查：Teacher/Recorder 权限边界、未来 reference 与 observation 因果性、有效摩擦而非单个 geom 值、固定目标的可观测性、模型更新与 reset 生命周期、训练/测试隔离、未校准范围的标记。尚无运行资格结论。
157: 
158: 当前设计取证唯一根为 `/tmp/so101-debug-domain-randomization-design-20261009-01a11f59/`，登记在其 `manifest.md`。retained：本设计及该根；archived：无；deletion candidates：无。未删除证据。未来执行任务须另行登记其唯一持久根：ai-station 为 `/data/work/so101-evidence/<task-family>/<run-id>/`，macOS 为 `/opt/data/work/so101-evidence/<task-family>/<run-id>/`。
159: 
160: 下一步是审阅此草案并冻结实机配置、首版参数集合和采集预算，然后编写实施计划。执行计划仍按 AGENTS.md 取得明确确认后，由 tmux 中的 `dst` 执行；本轮未启动执行器、未 commit/push。
```

## src/so101_demo_py/src/backends/mujoco/client.py

Project: `/Users/matianyi/Projects/robot_demo_001/moveit-demo`

SHA256: `901ac2fbedc36b45b3ef79c782fc43cb335f720e9bda2b8e54233b3462114c6c`

### Lines 1–22

```text
1: """Pinned ROS 2 service and joint-state client for MuJoCo reset transactions."""
2: 
3: from __future__ import annotations
4: 
5: import math
6: import threading
7: import time
8: from dataclasses import dataclass
9: from typing import Any
10: 
11: import rclpy
12: from controller_manager_msgs.srv import ListControllers, SwitchController
13: from mujoco_ros2_control_msgs.msg import FreeJointState
14: from mujoco_ros2_control_msgs.srv import ResetWorld, SetPause
15: from rclpy.qos import qos_profile_sensor_data
16: from sensor_msgs.msg import JointState
17: 
18: 
19: class MujocoServiceError(RuntimeError):
20:     """Raised when a pinned ROS interface is unavailable or returns failure."""
21: 
22: 
```

### Lines 95–124

```text
95:         if not math.isfinite(service_timeout_s) or service_timeout_s <= 0.0:
96:             raise ValueError("service_timeout_s must be finite and positive")
97:         self._service_node = service_node
98:         self._joint_state_node = joint_state_node
99:         self._timeout_s = service_timeout_s
100:         self._pause = service_node.create_client(SetPause, "/mujoco_ros2_control_node/set_pause")
101:         self._reset = service_node.create_client(
102:             ResetWorld, "/mujoco_ros2_control_node/reset_world"
103:         )
104:         self._switch = service_node.create_client(
105:             SwitchController, "/controller_manager/switch_controller"
106:         )
107:         self._list = service_node.create_client(
108:             ListControllers, "/controller_manager/list_controllers"
109:         )
110:         self._joint_lock = threading.Lock()
111:         self._joint_positions: dict[str, float] = {}
112:         self._joint_callback_count = 0
113:         self._joint_subscription = joint_state_node.create_subscription(
114:             JointState, "/joint_states", self._joint_callback, qos_profile_sensor_data
115:         )
116: 
117:     def _joint_callback(self, message: JointState) -> None:
118:         if len(message.name) != len(message.position):
119:             return
120:         positions = {}
121:         for name, position in zip(message.name, message.position, strict=True):
122:             value = float(position)
123:             if not math.isfinite(value):
124:                 return
```

## src/so101_demo_py/src/backends/mujoco/qualified_phases/contact_hold.py

Project: `/Users/matianyi/Projects/robot_demo_001/moveit-demo`

SHA256: `acfbd4dee37483d5d221fce2d92b00957bcbe53f698ce6ad3d18fabd5b2b3029`

### Lines 1–25

```text
1: #!/usr/bin/env python3
2: """Qualified MuJoCo phase: bounded bilateral preload under the Noslip model."""
3: 
4: from __future__ import annotations
5: 
6: import json
7: import math
8: import os
9: import time
10: from pathlib import Path
11: 
12: import rclpy
13: from control_msgs.action import FollowJointTrajectory
14: from rclpy.action import ActionClient
15: from rclpy.qos import qos_profile_sensor_data
16: from sensor_msgs.msg import JointState
17: from so101_demo.application.phases.grasp_strategy import seating_preload_target
18: from so101_demo.application.pick_place import load_live_task_policy
19: from so101_demo.application.staged_approach import maximum_joint_error
20: from so101_demo.backends.mujoco.observer import EvidenceStale, MujocoWorldObserver
21: from so101_demo.control.gripper.client import GripperClient
22: 
23: SESSION_ID = os.environ["SO101_SIMULATION_SESSION_ID"]
24: EXPECTED_EPOCH = int(os.environ["SO101_EXPECTED_RESET_EPOCH"])
25: EVIDENCE_PATH = Path(os.environ["SO101_EVIDENCE_ROOT"]) / "contact-hold.json"
```
