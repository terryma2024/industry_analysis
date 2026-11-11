---
source_id: SRC-robotics-685
title: SceneBot fixed source and VLK website inspection snapshot
source_type: source_code
publisher: Ericcsr / VLK authors
source_date: 2026-11-10
url: https://github.com/Ericcsr/scenebot/tree/430c29c1801aceb813506d86f3a8cffeba250df3
evidence_grade: S
capture_method: github-connector-fixed-commit
captured_at: 2026-11-10
tags: [raw/source, source-code, sim2real]
---

# SceneBot source inspection snapshot

Retrieved via connected GitHub tools. Code and model metadata only inspected; no inference, demo rollout, training or hardware execution performed.

## Fixed revisions and inventories

- SceneBot author demo: 430c29c1801aceb813506d86f3a8cffeba250df3
- VLK static website: fa01dab376d81f1c361c203822437b6a2d8efe42
- CHOIS: 8ec585aa0200fd2a890ffb12897bcf69ae719463
- Website tree (full list):

  - .DS_Store
  - README.md
  - css
  - css/style.css
  - images
  - images/hero_poster.jpg
  - images/method_data.png
  - images/method_full.png
  - images/method_policy.png
  - images/poster_highlight.jpg
  - images/poster_method_data.jpg
  - images/poster_method_policy.jpg
  - images/poster_mode_pick_floor.jpg
  - images/poster_mode_pick_surface.jpg
  - images/poster_mode_put_floor.jpg
  - images/poster_mode_put_surface.jpg
  - images/poster_mode_turn_around.jpg
  - images/poster_mode_walk_to.jpg
  - images/poster_sim_apartment.jpg
  - images/poster_sim_lab.jpg
  - images/poster_task1_nav4.jpg
  - images/poster_task1_walkrand.jpg
  - images/poster_task2_box.jpg
  - images/poster_task3_multi.jpg
  - images/poster_task4_disco.jpg
  - images/poster_task4_dynamic.jpg
  - images/poster_task5_lh1.jpg
  - images/poster_task5_lh2.jpg
  - index.html
  - js
  - js/main.js
  - videos
  - videos/hero_bg.mp4
  - videos/highlight.mp4
  - videos/method_data.mp4
  - videos/method_policy.mp4
  - videos/mode_pick_floor.mp4
  - videos/mode_pick_surface.mp4
  - videos/mode_put_floor.mp4
  - videos/mode_put_surface.mp4
  - videos/mode_turn_around.mp4
  - videos/mode_walk_to.mp4
  - videos/sim_apartment.mp4
  - videos/sim_lab.mp4
  - videos/task1_nav4.mp4
  - videos/task1_walkrand.mp4
  - videos/task2_box.mp4
  - videos/task3_multi.mp4
  - videos/task4_disco.mp4
  - videos/task4_dynamic.mp4
  - videos/task5_lh1.mp4
  - videos/task5_lh2.mp4

## SceneBot selected inventory

- README.md | git blob 7665c8f2f9e2312ab68bc2086efe558ac57b6afe | size 14470
- assets/scenebot_policy_bundle.zip | git blob cdeb65c40837662efb0535a4f778faac130dc561 | size 31943492
- mujoco_wasm/LICENSE | git blob 5168a93fd8f663a169177efcabc189bb1c8d5d1f | size 1078
- mujoco_wasm/README.md | git blob 4edf7643bc654cb5da658cd0be4bd1f63cf66fe3 | size 3243
- mujoco_wasm/assets/scenes/agility_cassie/LICENSE | git blob ed6132511f964d16a641a880c5fbfc9e0707d38f | size 1060
- mujoco_wasm/assets/scenes/agility_cassie/README.md | git blob 80ac5b63ca7588abe704ea170d576f80e84bdf24 | size 904
- mujoco_wasm/assets/scenes/shadow_hand/LICENSE | git blob 34e408254ab138d12c7b224dc263df8792225304 | size 11355
- mujoco_wasm/assets/scenes/shadow_hand/README.md | git blob 962c157416bea12f447b54a1c6e51026712015d5 | size 1719
- mujoco_wasm/dist-desktop/scenebot/contact_labels.bin | git blob 4dac68213386b3faec129151dca9f31b6a2521f1 | size 48204
- mujoco_wasm/dist-desktop/scenebot/contact_labels_index.json | git blob 0fc95cadbe22eec0e52099f8d7534acd7390f819 | size 1873
- mujoco_wasm/dist-desktop/scenebot/policy.onnx | git blob ad67e7ebcf601b820fddb444f67797adf353986a | size 33910590
- mujoco_wasm/dist-desktop/scenebot/policy_meta.json | git blob e580e8d9029e37fe28a06de4a81ec7dcb37aaf46 | size 4204
- mujoco_wasm/src/scenebot/contact_utils.js | git blob 0142307368dc8dd3b8cf065fc026329e14a46a81 | size 4750
- mujoco_wasm/src/scenebot/loader.js | git blob 2d270ec8cc07c22766f89ef763ef4c850df30037 | size 3364
- mujoco_wasm/src/scenebot/policy_runtime.js | git blob e778865b42f7591ff07589333317ef7a8332bdb0 | size 10154
- patches/robot_motion_stitching.patch | git blob 9d37d2deaaf37bf6cb0fe711789139e0740db32e | size 7304
- patches/tml_humanoid_deploy.patch | git blob 10db744356593c2545283ed927bf3a572c06e6fa | size 17674

## mujoco_wasm/src/scenebot/policy_runtime.js

Source: https://github.com/Ericcsr/scenebot/blob/430c29c1801aceb813506d86f3a8cffeba250df3/mujoco_wasm/src/scenebot/policy_runtime.js

```javascript
// Direct port of tml_humanoid_deploy/rl_policy.py:RLStreamingContactPolicy runtime path
// (constructor + prepare_control_signals + prepare_obs + get_action), driven by
// onnxruntime-web in place of onnxruntime CPU.
//
// Observation construction follows obs_names from policy_meta.json (the YAML config),
// not the ONNX metadata's training-time observation_names. The Python code does the same
// in RLBasePolicy.prepare_obs (rl_policy.py:347-358).

import * as ort from "onnxruntime-web";
import {
  applyQuat, multQuat, invQuat, quatAsMatrix, wxyzToXyzw,
} from "./quat_utils.js";
import { normalizeContactForPolicy } from "./contact_utils.js";

/**
 * @param {Float32Array} dst         output flat array
 * @param {Float32Array|number[]} src
 * @param {number} offset            starting position in dst
 * @returns {number}                 new offset (offset + src.length)
 */
function copyInto(dst, src, offset) {
  for (let i = 0; i < src.length; i++) dst[offset + i] = src[i];
  return offset + src.length;
}

export class PolicyRuntime {
  /**
   * @param {ort.InferenceSession} session
   * @param {object} meta            content of policy_meta.json
   */
  constructor(session, meta) {
    this.session = session;
    this.meta = meta;
    this.obsDim = meta.obs_dim;
    this.actionDim = meta.action_dim;
    this.obsNames = meta.obs_names;
    this.ISAAC_TO_MUJOCO = Int32Array.from(meta.ISAAC_TO_MUJOCO);
    this.MUJOCO_TO_ISAAC = Int32Array.from(meta.MUJOCO_TO_ISAAC);
    this.actionScaleMujoco = Float32Array.from(meta.action_scale_mujoco);
    this.defaultQIsaac = Float32Array.from(meta.default_q_isaac);

    // Default contact mask: expanded to policy contact_dim (e.g. 5-way -> 10-way).
    this.contactDim = meta.contact_dim;
    this.latestContactMask = normalizeContactForPolicy(
      meta.default_contact_label || [],
      meta,
    );

    // Latest streaming inputs (defaults; over-written each tick from MotionGraphRuntime packet).
    this.latestLowerCmd = new Float32Array(meta.lower_cmd_dim);
    this.latestVrPos = new Float32Array(meta.vr_pos_dim);
    this.latestVrOrn = new Float32Array(meta.vr_orn_dim);
    // Identity rotations for VR orn default (3 quats, wxyz).
    this.latestVrOrn[0] = 1; this.latestVrOrn[4] = 1; this.latestVrOrn[8] = 1;
    this.latestMotionAnchorPosW = new Float32Array(3);
    this.latestMotionAnchorOrnW = new Float32Array([0, 0, 0, 1]); // xyzw

    // Persistent state.
    this.lastAction = new Float32Array(this.actionDim);

    // Pre-allocated obs buffer to avoid per-tick allocs.
    this._obsBuf = new Float32Array(this.obsDim);
    // session may be null during parity tests that exercise prepareObs only.
    this._inputName = session?.inputNames?.[0] ?? "obs";
    this._outputName = session?.outputNames?.[0] ?? "actions";
  }

  reset() {
    this.lastAction.fill(0);
    this.latestLowerCmd.fill(0);
    this.latestVrPos.fill(0);
    this.latestVrOrn.fill(0);
    this.latestVrOrn[0] = 1;
    this.latestVrOrn[4] = 1;
    this.latestVrOrn[8] = 1;
    this.latestMotionAnchorPosW.fill(0);
    this.latestMotionAnchorOrnW[0] = 0;
    this.latestMotionAnchorOrnW[1] = 0;
    this.latestMotionAnchorOrnW[2] = 0;
    this.latestMotionAnchorOrnW[3] = 1;
    this.latestContactMask = normalizeContactForPolicy(
      this.meta.default_contact_label || [],
      this.meta,
    );
  }

  static async create(modelUrl, meta) {
    // Point ort-web at jsdelivr for its .wasm backend files (Vite dev/prod don't auto-bundle them).
    // Mirrors what scenebot/mujoco_wasm/src/policy/policyController.js does.
    ort.env.wasm.wasmPaths = "https://cdn.jsdelivr.net/npm/onnxruntime-web/dist/";
    ort.env.wasm.numThreads = Math.min(4, (typeof navigator !== "undefined" && navigator.hardwareConcurrency) || 1);
    const session = await ort.InferenceSession.create(modelUrl, {
      executionProviders: ["wasm"],
      graphOptimizationLevel: "all",
    });
    return new PolicyRuntime(session, meta);
  }

  /** Pull values from a MotionGraphRuntime packet into the cached `latest*` fields. */
  ingestStreamPacket(packet) {
    if (packet.lower_cmd) this.latestLowerCmd = packet.lower_cmd;
    if (packet.vr_3point_pos_l) this.latestVrPos = packet.vr_3point_pos_l;
    if (packet.vr_3point_orn_l) this.latestVrOrn = packet.vr_3point_orn_l;
    if (packet.contact_mask) {
      this.latestContactMask = normalizeContactForPolicy(packet.contact_mask, this.meta);
    }
    if (packet.motion_anchor_pos_w) {
      this.latestMotionAnchorPosW[0] = packet.motion_anchor_pos_w[0];
      this.latestMotionAnchorPosW[1] = packet.motion_anchor_pos_w[1];
      this.latestMotionAnchorPosW[2] = packet.motion_anchor_pos_w[2];
    }
    if (packet.motion_anchor_orn_w) {
      // motion_anchor_orn_w is xyzw (Python publishes that — see _build_stream_packet line 1842).
      this.latestMotionAnchorOrnW[0] = packet.motion_anchor_orn_w[0];
      this.latestMotionAnchorOrnW[1] = packet.motion_anchor_orn_w[1];
      this.latestMotionAnchorOrnW[2] = packet.motion_anchor_orn_w[2];
      this.latestMotionAnchorOrnW[3] = packet.motion_anchor_orn_w[3];
    }
  }

  /**
   * Build the per-tick "control signals" dictionary, matching prepare_control_signals
   * (rl_policy.py:1400-1426). robotState is the live MuJoCo state.
   *
   * @param {object} robotState
   *   { q: Float32Array(29) [Mujoco-order],
   *     dq: Float32Array(29),
   *     omega: Float32Array(3),
   *     imu_quat: Float32Array(4) (wxyz),
   *     root_pos: Float32Array(3),
   *     root_orn: Float32Array(4) (xyzw),
   *     root_vel: Float32Array(3) }
   */
  prepareControlSignals(robotState) {
    // anchor_rot_inv = Rotation.from_quat(root_orn).inv()
    const anchorRotInv = invQuat(robotState.root_orn);
    // target_anchor_rot = Rotation.from_quat(latest_motion_anchor_orn_w)
    const targetAnchorRot = this.latestMotionAnchorOrnW;
    const error = new Float64Array(3);
    error[0] = this.latestMotionAnchorPosW[0] - robotState.root_pos[0];
    error[1] = this.latestMotionAnchorPosW[1] - robotState.root_pos[1];
    error[2] = this.latestMotionAnchorPosW[2] - robotState.root_pos[2];
    // motion_anchor_pos_b = anchor_rot_inv.apply(error)
    const anchorPosB = applyQuat(anchorRotInv, error);
    // motion_anchor_ori_b = (anchor_rot_inv * target_anchor_rot).as_matrix()[:, :2].reshape(-1)
    // numpy default reshape(-1) is C-order (row-major). For a 3x2 slice that means
    // flat = (M[0,0], M[0,1], M[1,0], M[1,1], M[2,0], M[2,1]).
    const composed = multQuat(anchorRotInv, targetAnchorRot);
    const M = quatAsMatrix(composed); // row-major 3x3 stored flat as M[r*3+c]
    const anchorOriB = new Float32Array([
      M[0], M[1],  // row 0, cols 0..1
      M[3], M[4],  // row 1
      M[6], M[7],  // row 2
    ]);
    // projected_gravity = anchor_rot_inv.apply([0, 0, -1])
    const gravWorld = new Float64Array([0, 0, -1]);
    const projectedGravity = applyQuat(anchorRotInv, gravWorld);
    return {
      lower_command: this.latestLowerCmd,
      vr_3point_pos: this.latestVrPos,
      vr_3point_ori: this.latestVrOrn,
      contact_mask: this.latestContactMask,
      motion_anchor_pos_b: new Float32Array([anchorPosB[0], anchorPosB[1], anchorPosB[2]]),
      motion_anchor_ori_b: anchorOriB,
      projected_gravity: new Float32Array([projectedGravity[0], projectedGravity[1], projectedGravity[2]]),
    };
  }

  /**
   * Concatenate obs fields per `obs_names` order. Matches RLStreamingContactPolicy.prepare_obs
   * (rl_policy.py:1428-1443). For q/dq, subtracts default_q (Isaac order) — i.e.
   *   item = robot_state[key][MUJOCO_TO_ISAAC] - default_q_isaac
   */
  prepareObs(robotState, controlSignals) {
    const buf = this._obsBuf;
    let off = 0;

    for (const key of this.obsNames) {
      let item;
      if (key === "q") {
        // robot_state.q is MuJoCo-order (29). Reindex to Isaac via MUJOCO_TO_ISAAC, then subtract default.
        const tmp = new Float32Array(29);
        for (let i = 0; i < 29; i++) tmp[i] = robotState.q[this.MUJOCO_TO_ISAAC[i]] - this.defaultQIsaac[i];
        item = tmp;
      } else if (key === "dq") {
        const tmp = new Float32Array(29);
        // default_value["dq"] = zeros, so subtraction is a no-op (matches rl_policy.py:1132).
        for (let i = 0; i < 29; i++) tmp[i] = robotState.dq[this.MUJOCO_TO_ISAAC[i]];
        item = tmp;
      } else if (key === "last_action") {
        item = this.lastAction;
      } else if (key === "root_vel") {
        item = robotState.root_vel;
      } else if (key === "omega") {
        item = robotState.omega;
      } else if (key in controlSignals) {
        item = controlSignals[key];
      } else {
        // robot_state introspection — fall through any names we haven't special-cased yet.
        if (key in robotState) item = robotState[key];
        else throw new Error(`Unknown obs field "${key}"`);
      }
      off = copyInto(buf, item, off);
    }
    if (off !== this.obsDim) {
      throw new Error(`obs assembly mismatch: built ${off} floats, expected ${this.obsDim}`);
    }
    return buf;
  }

  /**
   * Run ONNX inference and return the raw action vector (Isaac order, length actionDim).
   * @param {Float32Array} obs   length obsDim
   */
  async getAction(obs) {
    const tensor = new ort.Tensor("float32", obs, [1, this.obsDim]);
    const out = await this.session.run({ [this._inputName]: tensor });
    const raw = out[this._outputName].data; // Float32Array of length actionDim
    // Cache for next-tick last_action.
    for (let i = 0; i < this.actionDim; i++) this.lastAction[i] = raw[i];
    return raw;
  }

  /**
   * Map raw policy output (Isaac order) to MuJoCo-order target joint angles.
   *   target_q_mujoco = action[ISAAC_TO_MUJOCO] * action_scale + default_q[ISAAC_TO_MUJOCO]
   * (Python at run_controller.py:198 + rl_policy.py:1138.)
   */
  applyControl(rawAction) {
    const target = new Float32Array(this.actionDim);
    for (let i = 0; i < this.actionDim; i++) {
      const idx = this.ISAAC_TO_MUJOCO[i];
      target[i] = rawAction[idx] * this.actionScaleMujoco[i] + this.defaultQIsaac[idx];
    }
    return target;
  }
}

```


## mujoco_wasm/src/scenebot/contact_utils.js

Source: https://github.com/Ericcsr/scenebot/blob/430c29c1801aceb813506d86f3a8cffeba250df3/mujoco_wasm/src/scenebot/contact_utils.js

```javascript
// Mirrors tml_humanoid_deploy/rl_policy.py contact-mask expansion helpers.

/** 4-way [Lfoot, Rfoot, Lwrist, Rwrist] -> 8-way env/obj split. */
export function expand4wayContactTo8(m4) {
  const src = m4 instanceof Float32Array ? m4 : Float32Array.from(m4);
  if (src.length !== 4) {
    throw new Error(`expand4wayContactTo8: expected 4 channels, got ${src.length}`);
  }
  const out = new Float32Array(8);
  out[0] = src[0];
  out[2] = src[1];
  out[5] = src[2];
  out[7] = src[3];
  return out;
}

/** 5-way stored labels -> 10-way policy obs. */
export function expand5wayContactTo10(m5) {
  const src = m5 instanceof Float32Array ? m5 : Float32Array.from(m5);
  if (src.length !== 5) {
    throw new Error(`expand5wayContactTo10: expected 5 channels, got ${src.length}`);
  }
  const m8 = expand4wayContactTo8(src.subarray(0, 4));
  const out = new Float32Array(10);
  out.set(m8, 0);
  out[8] = src[4];
  out[9] = 0.0;
  return out;
}

/** 4-way limbs -> 10-way with zero pelvis/seat channels. */
export function expand4wayLimbTo10wayWithZeroSeat(m4) {
  const m8 = expand4wayContactTo8(m4);
  const out = new Float32Array(10);
  out.set(m8, 0);
  return out;
}

/** 8-way -> 4-way by max(env, obj) per limb. */
export function reduce8wayContactTo4(m8) {
  const src = m8 instanceof Float32Array ? m8 : Float32Array.from(m8);
  if (src.length !== 8) {
    throw new Error(`reduce8wayContactTo4: expected 8 channels, got ${src.length}`);
  }
  return Float32Array.from([
    Math.max(src[0], src[1]),
    Math.max(src[2], src[3]),
    Math.max(src[4], src[5]),
    Math.max(src[6], src[7]),
  ]);
}

/** Append zero pelvis/seat column: 4 -> 5. */
export function pad4wayContactTo5(m4) {
  const src = m4 instanceof Float32Array ? m4 : Float32Array.from(m4);
  if (src.length !== 4) {
    throw new Error(`pad4wayContactTo5: expected 4 channels, got ${src.length}`);
  }
  const out = new Float32Array(5);
  out.set(src, 0);
  return out;
}

/**
 * Pad/truncate a motion-graph stream mask to the resolver's stream width (max label dim, usually 5).
 * Mirrors ContactLabelResolver padding 4-dim clip labels up to contact_dim.
 */
export function padContactMaskToStreamDim(raw, streamDim) {
  const src = raw instanceof Float32Array ? raw : Float32Array.from(raw);
  const out = new Float32Array(streamDim);
  const n = Math.min(src.length, streamDim);
  for (let i = 0; i < n; i++) out[i] = src[i];
  return out;
}

/**
 * Expand a motion-graph contact_mask payload to policy.contact_dim.
 * Mirrors RLStreamingContactPolicy stream decode (rl_policy.py:1352-1396) and default-label init.
 */
export function normalizeContactForPolicy(raw, meta, { limbContactFileIs8way = false } = {}) {
  const contactDim = meta.contact_dim;
  let arr = raw instanceof Float32Array ? Float32Array.from(raw) : Float32Array.from(raw);
  const use10 = !!meta.use_10way_contact;
  const use5from4 = !!meta.use_5dim_contact_from_4dim;
  const use8 = !!meta.use_8way_contact;

  if (use10 && use5from4) {
    const n = arr.length;
    if (n === 4) {
      arr = expand4wayLimbTo10wayWithZeroSeat(arr);
    } else if (n === 5) {
      arr = expand4wayLimbTo10wayWithZeroSeat(arr.subarray(0, 4));
    } else if (n === 8) {
      arr = limbContactFileIs8way
        ? (() => { const o = new Float32Array(10); o.set(arr, 0); return o; })()
        : expand4wayLimbTo10wayWithZeroSeat(reduce8wayContactTo4(arr));
    } else if (n === 10) {
      arr = (() => { const o = new Float32Array(10); o.set(arr.subarray(0, 8), 0); return o; })();
    } else {
      throw new Error(
        `contact stream: use_10way + use_5dim_from_4dim expected 4,5,8,10 values, got ${n}`,
      );
    }
  } else if (use10) {
    if (arr.length === 5) arr = expand5wayContactTo10(arr);
    if (arr.length !== contactDim) {
      throw new Error(`contact stream: use_10way expected 5 or ${contactDim} values, got ${arr.length}`);
    }
  } else if (use5from4) {
    if (arr.length === 4) arr = pad4wayContactTo5(arr);
    else if (arr.length === 5) {
      arr = Float32Array.from(arr);
      arr[4] = 0.0;
    }
    if (arr.length !== contactDim) {
      throw new Error(`contact stream: use_5dim_from_4dim expected 4 or ${contactDim} values, got ${arr.length}`);
    }
  } else if (use8) {
    if (arr.length === 4) arr = expand4wayContactTo8(arr);
    if (arr.length !== contactDim) {
      throw new Error(`contact stream: use_8way expected 4 or ${contactDim} values, got ${arr.length}`);
    }
  } else if (arr.length !== contactDim) {
    throw new Error(`contact stream: expected ${contactDim} values, got ${arr.length}`);
  }

  if (arr.length !== contactDim) {
    throw new Error(`contact stream: expected ${contactDim} values after normalize, got ${arr.length}`);
  }
  return arr;
}

```


## mujoco_wasm/src/scenebot/loader.js

Source: https://github.com/Ericcsr/scenebot/blob/430c29c1801aceb813506d86f3a8cffeba250df3/mujoco_wasm/src/scenebot/loader.js

```javascript
// Boot-time asset loader for the fully-browser scenebot demo.
//
// Also exports a small post-load helper to hide leftover debug geoms (red sphere/cylinder
// at world origin) that mujoco_wasm's loader inserts for some scene types.
// Fetches all artifacts in parallel from /scenebot/* (paths produced by tools/build_browser_assets.py).

import { ClipBundle, ContactLabels } from "./motion_clips.js";

// Vite sets BASE_URL to "/" in dev (vite serve) and "./" in production builds
// (because vite.config.* sets base: './'). Both work as fetch path prefixes —
// "/scenebot/..." resolves at the dev-server root; "./scenebot/..." resolves
// relative to the iframe's HTML document, which is what we want for the Pages
// build at .../mujoco_wasm/dist-desktop/index.html.
const BASE = `${import.meta.env.BASE_URL}scenebot`.replace(/\/+/g, "/").replace(/\/$/, "");

export async function loadScenebotAssets({ onProgress } = {}) {
  const status = (msg) => onProgress?.(msg);

  status("loading clip bundle…");
  const clipBundlePromise = ClipBundle.load(`${BASE}/clips.bin`, `${BASE}/clips_index.json`);
  status("loading contact labels…");
  const contactPromise = ContactLabels.load(`${BASE}/contact_labels.bin`, `${BASE}/contact_labels_index.json`);
  status("loading motion graph…");
  const motionGraphPromise = fetch(`${BASE}/motion_graph.json`).then((r) => {
    if (!r.ok) throw new Error(`fetch motion_graph.json ${r.status}`);
    return r.json();
  });
  status("loading policy meta…");
  const policyMetaPromise = fetch(`${BASE}/policy_meta.json`).then((r) => {
    if (!r.ok) throw new Error(`fetch policy_meta.json ${r.status}`);
    return r.json();
  });
  // Scene XML is staged into mujoco_wasm's MEMFS by main.js's stageSceneIntoMemfs() before
  // we get here, so by the time loadScenebotAssets() runs the XML has already been fetched.
  // We don't need to re-validate it.

  const [clipBundle, contactLabels, motionGraph, policyMeta] = await Promise.all([
    clipBundlePromise, contactPromise, motionGraphPromise, policyMetaPromise,
  ]);

  status("ready");
  return {
    clipBundle,
    contactLabels,
    motionGraph,
    policyMeta,
    policyOnnxUrl: `${BASE}/policy.onnx`,
    sceneXmlUrl: `${BASE}/scene_29dof_flat_hand.xml`,
    g1XmlUrl: `${BASE}/assets/g1/g1_29dof_flat_hand.xml`,
    meshesBaseUrl: `${BASE}/assets/g1/meshes`,
  };
}

/**
 * Hide leftover red debug geoms that mujoco_wasm's scene loader can attach to the
 * MuJoCo Root group at world origin (cylinder + sphere with color ~(0.8,0.3,0.3)).
 * These come from PHP demo defaults; they are not part of our scene XML and have no
 * parent body, so we identify them by parent name == "MuJoCo Root" and hide them.
 *
 * Pass the THREE scene root.
 */
export function hideDebugGeoms(scene) {
  const isReddish = (c) => c && c.r > 0.7 && c.g < 0.4 && c.b < 0.4;
  let hidden = 0;
  scene.traverse((o) => {
    if (!o.isMesh || !o.material?.color) return;
    const parentName = o.parent?.name || "";
    // Hide reddish meshes whose direct parent is "MuJoCo Root" (i.e. orphaned —
    // not under any named body). These are mujoco_wasm renderer artifacts.
    if (parentName === "MuJoCo Root" && isReddish(o.material.color)) {
      o.visible = false;
      hidden++;
    }
  });
  if (hidden > 0) console.log(`[scenebot] hid ${hidden} orphan debug geoms`);
}

```


## mujoco_wasm/dist-desktop/scenebot/policy_meta.json

Source: https://github.com/Ericcsr/scenebot/blob/430c29c1801aceb813506d86f3a8cffeba250df3/mujoco_wasm/dist-desktop/scenebot/policy_meta.json

```json
{
  "ISAAC_TO_MUJOCO": [
    0,
    3,
    6,
    9,
    13,
    17,
    1,
    4,
    7,
    10,
    14,
    18,
    2,
    5,
    8,
    11,
    15,
    19,
    21,
    23,
    25,
    27,
    12,
    16,
    20,
    22,
    24,
    26,
    28
  ],
  "MUJOCO_TO_ISAAC": [
    0,
    6,
    12,
    1,
    7,
    13,
    2,
    8,
    14,
    3,
    9,
    15,
    22,
    4,
    10,
    16,
    23,
    5,
    11,
    17,
    24,
    18,
    25,
    19,
    26,
    20,
    27,
    21,
    28
  ],
  "action_dim": 29,
  "action_scale_mujoco": [
    0.548,
    0.351,
    0.548,
    0.351,
    0.439,
    0.439,
    0.548,
    0.351,
    0.548,
    0.351,
    0.439,
    0.439,
    0.548,
    0.439,
    0.439,
    0.439,
    0.439,
    0.439,
    0.439,
    0.439,
    0.075,
    0.075,
    0.439,
    0.439,
    0.439,
    0.439,
    0.439,
    0.075,
    0.075
  ],
  "contact_dim": 10,
  "control_dt": 0.02,
  "default_contact_label": [
    0.0,
    0.0,
    0.0,
    0.0,
    0.0
  ],
  "default_q_isaac": [
    -0.312,
    -0.312,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.669,
    0.669,
    0.2,
    0.2,
    -0.363,
    -0.363,
    0.2,
    -0.2,
    0.0,
    0.0,
    0.0,
    0.0,
    0.6,
    0.6,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0
  ],
  "history_length": 1,
  "history_names": [
    "projected_gravity",
    "omega",
    "q",
    "dq",
    "last_action"
  ],
  "init_qpos_36": [
    -0.30971550941467285,
    -0.008524656295776367,
    0.7877424955368042,
    0.9987926812752704,
    -0.012486211622452519,
    -0.0459210711388165,
    0.01218727105381441,
    0.15753258764743805,
    -0.024858469143509865,
    0.014001104980707169,
    0.06524167209863663,
    -0.12364169210195541,
    0.033786576241254807,
    0.08075591176748276,
    0.028745979070663452,
    0.02062559500336647,
    0.18026025593280792,
    -0.13116876780986786,
    -0.03476269543170929,
    0.017560729756951332,
    -0.0013427719241008162,
    0.06848049908876419,
    -0.16282321512699127,
    0.2483399361371994,
    0.030629048123955727,
    0.9379460215568542,
    0.07211852073669434,
    0.17955879867076874,
    -0.010753108188509941,
    0.040171798318624496,
    -0.2165953665971756,
    -0.0063589769415557384,
    1.0054144859313965,
    -0.03225891664624214,
    0.14640237390995026,
    0.008325225673615932
  ],
  "joint_damping": [
    2.5579,
    6.3088,
    2.5579,
    6.3088,
    1.8144,
    1.8144,
    2.5579,
    6.3088,
    2.5579,
    6.3088,
    1.8144,
    1.8144,
    2.5579,
    1.8144,
    1.8144,
    0.9072,
    0.9072,
    0.9072,
    0.9072,
    0.9072,
    1.0681,
    1.0681,
    0.9072,
    0.9072,
    0.9072,
    0.9072,
    0.9072,
    1.0681,
    1.0681
  ],
  "joint_stiffness": [
    40.1792,
    99.0984,
    40.1792,
    99.0984,
    28.5012,
    28.5012,
    40.1792,
    99.0984,
    40.1792,
    99.0984,
    28.5012,
    28.5012,
    40.1792,
    28.5012,
    28.5012,
    14.2506,
    14.2506,
    14.2506,
    14.2506,
    14.2506,
    16.7783,
    16.7783,
    14.2506,
    14.2506,
    14.2506,
    14.2506,
    14.2506,
    16.7783,
    16.7783
  ],
  "lower_cmd_dim": 24,
  "motion_anchor_ori_b_dim": 6,
  "motion_anchor_pos_b_dim": 3,
  "obs_dim": 160,
  "obs_names": [
    "lower_command",
    "vr_3point_pos",
    "vr_3point_ori",
    "motion_anchor_pos_b",
    "motion_anchor_ori_b",
    "root_vel",
    "projected_gravity",
    "omega",
    "q",
    "dq",
    "last_action",
    "contact_mask"
  ],
  "onnx_sha256": "c0a3caf00809d1ccb26aad6358f2b107098462deccac755e406e522134103d04",
  "ref_motion_start_index": 0,
  "simulation_dt": 0.005,
  "torque_limit": [
    88,
    139,
    88,
    139,
    50,
    50,
    88,
    139,
    88,
    139,
    50,
    50,
    88,
    50,
    50,
    25,
    25,
    25,
    25,
    25,
    5,
    5,
    25,
    25,
    25,
    25,
    25,
    5,
    5
  ],
  "use_10way_contact": true,
  "use_5dim_contact_from_4dim": false,
  "use_8way_contact": false,
  "vr_3point_offsets": [
    [
      0.18,
      -0.025,
      0.0
    ],
    [
      0.18,
      0.025,
      0.0
    ],
    [
      0.0,
      0.0,
      0.35
    ]
  ],
  "vr_orn_dim": 12,
  "vr_pos_dim": 9
}
```


## mujoco_wasm/LICENSE

Source: https://github.com/Ericcsr/scenebot/blob/430c29c1801aceb813506d86f3a8cffeba250df3/mujoco_wasm/LICENSE

```text
MIT License

Copyright (c) 2017 Konstantin Gredeskoul

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

