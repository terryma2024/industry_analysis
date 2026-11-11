import ast,types,json
from pathlib import Path
import mujoco,numpy as np,xml.etree.ElementTree as ET
src=Path('/tmp/joint-audit/discoverse-dev--GaussianRenderer--src--gaussian_renderer--gs_renderer_mujoco.py')
t=ast.parse(src.read_text());cls=next(x for x in t.body if isinstance(x,ast.ClassDef) and x.name=='GSRendererMuJoCo')
methods=[x for x in cls.body if isinstance(x,ast.FunctionDef) and x.name in ['init_renderer','update_gaussians']]
class CaptureAdapter:
 def set_objects_mapping(self,info):self.mapping=info
 def update_gaussian_properties(self,p,q):self.captured=(p.copy(),q.copy())
ns={'mujoco':mujoco,'np':np}
for method in methods:
 code=ast.unparse(method);exec(compile(code,str(src),'exec'),ns);setattr(CaptureAdapter,method.name,ns[method.name])
r=ET.fromstring(Path('/tmp/joint-audit/discoverse-dev--DISCOVERSE--models--mjcf--object--toy_cabinet.xml').read_text());xml='<mujoco><compiler angle="radian"/><worldbody>'+''.join(ET.tostring(x,encoding='unicode') for x in r)+'</worldbody></mujoco>'
m=mujoco.MjModel.from_xml_string(xml);d=mujoco.MjData(m)
a=CaptureAdapter();a.gaussian_model_names=['cabinet_door','cabinet_drawer'];a.gaussian_start_indices={'cabinet_door':0,'cabinet_drawer':10};a.gaussian_end_indices={'cabinet_door':10,'cabinet_drawer':20};a.init_renderer(m)
mujoco.mj_forward(m,d);a.update_gaussians(d);p0,q0=a.captured
d.qpos[:]=[0.5,0.1];mujoco.mj_forward(m,d);a.update_gaussians(d);p1,q1=a.captured
assert a.mapping==[('cabinet_door',0,10),('cabinet_drawer',10,20)]
assert np.allclose(p1[1]-p0[1],[-.1,0,0]);assert not np.allclose(q0[0],q1[0]);assert np.allclose(p1,d.xpos[a.gs_body_ids]);assert np.allclose(q1,d.xquat[a.gs_body_ids])
res={'mujoco_version':mujoco.__version__,'renderer_commit':'577efdb50c3891f46db3971dc0b7c4129146dd16','method_source':'Exact AST-extracted init_renderer and update_gaussians; capture adapter replaces GPU model mutation','mapped_body_names':[x[0] for x in a.mapping],'drawer_translation':(p1[1]-p0[1]).tolist(),'hinge_quaternion_changed':True,'body_pose_binding_pass':True,'actual_gaussian_points_mutation_tested':False,'GPU_render_tested':False}
Path('/tmp/joint-audit/body-binding-probe-result.json').write_text(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
