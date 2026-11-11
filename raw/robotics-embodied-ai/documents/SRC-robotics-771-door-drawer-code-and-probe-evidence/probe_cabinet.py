from pathlib import Path
import xml.etree.ElementTree as ET,json,hashlib
import mujoco,numpy as np
p=Path('/tmp/joint-audit/discoverse-dev--DISCOVERSE--models--mjcf--object--toy_cabinet.xml')
r=ET.fromstring(p.read_text());xml='<mujoco model="upstream_toy_cabinet_probe"><compiler angle="radian"/><option timestep="0.002"/><worldbody>'+''.join(ET.tostring(x,encoding='unicode') for x in r)+'</worldbody></mujoco>'
model=mujoco.MjModel.from_xml_string(xml);d=mujoco.MjData(model)
records=[]
for j in range(model.njnt):records.append({'id':j,'type':int(model.jnt_type[j]),'limited':bool(model.jnt_limited[j]),'axis':model.jnt_axis[j].tolist(),'range':model.jnt_range[j].tolist(),'qposadr':int(model.jnt_qposadr[j])})
assert model.njnt==2
assert int(model.jnt_type[0])==int(mujoco.mjtJoint.mjJNT_HINGE)
assert int(model.jnt_type[1])==int(mujoco.mjtJoint.mjJNT_SLIDE)
assert model.jnt_limited.all()
mujoco.mj_forward(model,d);pos0=d.xpos[model.body('cabinet_drawer').id].copy();rot0=d.xmat[model.body('cabinet_door').id].copy()
d.qpos[:]=[0.5,0.10];mujoco.mj_forward(model,d)
delta=d.xpos[model.body('cabinet_drawer').id]-pos0
assert np.allclose(delta,[-.1,0,0]);assert not np.allclose(rot0,d.xmat[model.body('cabinet_door').id])
mujoco.mj_resetData(model,d);d.qpos[:]=[.3,.08];mujoco.mj_forward(model,d)
q0=d.qpos.copy();d.qfrc_applied[:]=[1,2]
for _ in range(100):mujoco.mj_step(model,d)
assert np.isfinite(d.qpos).all();assert np.linalg.norm(d.qpos-q0)>1e-6
result={'mujoco_version':mujoco.__version__,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'wrapper':'Unchanged upstream include bodies in standalone radian MJCF; no robot scene or graphics','model_njnt':model.njnt,'joints':records,'forward_drawer_delta_at_0_1m':delta.tolist(),'hinge_rotation_changed':True,'force_step_100_qpos_start':q0.tolist(),'force_step_100_qpos_end':d.qpos.tolist(),'finite':True,'limits_runtime_tested':False,'render_or_GS_tested':False,'full_DISCOVERSE_tested':False}
Path('/tmp/joint-audit/mujoco-cabinet-probe-result.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
