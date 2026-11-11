---
source_id: SRC-robotics-771
title: 门与抽屉场景重建代码核查与最小探针
source_type: source_code_inspection
date: 2026-11-10
capture_method: github-connector-fixed-files-api-tree-and-isolated-probe
evidence_grade: S
---

# 证据包

同名evidence目录保存固定源码、完整tree（truncated=false）、许可证与实际探针脚本／JSON；data/provenance给出文件hash。未运行训练、真机、图形界面、GS CUDA模型或完整候选系统。

## 两项有限验证

1. `probe_cabinet.py`：原始toy_cabinet.xml include各body不变，放入独立radian MJCF wrapper；MuJoCo4.0.0编译得到hinge和slide。drawer q=0.1时世界位移[-0.1,0,0]，door q=0.5改变朝向。施加广义力后100步，有限且状态改变。读取limited=true不等于端点受力验收，未测试极限／真实接触／渲染。
2. `probe_body_binding.py`：从固定GSRendererMuJoCo中AST提取init_renderer与update_gaussians原方法；真实MuJoCo模型／状态，替身仅截获传给GPU更新函数的pose。门／抽屉均映射成功，hinge改变四元数，slide改变位置。替身不是GPU，未测试Gaussian点变换或像素渲染。

隔离环境uv解析到mujoco4.0.0，并非现有机器人项目环境；不能据此声称原项目依赖已兼容或已有完整运行验收。

## 静态关键点

- DISCOVERSE toy_cabinet：hinge默认类型，range0..3.1416，axis0,0,-1；drawer slide range0..0.22，axis-1,0,0。父场景明确angle=radian。
- cabinet_door_open.py默认GS=false；drawer_open.py默认false但提供--use_gs。示例入口仍是机器人任务／数据循环，本轮不执行；抽离资产不等于已做独立房间编辑器。
- 当前GaussianRenderer0.2.0 MIT，pyproject依赖gsplat；模型按body名称映射，用mj_data.xpos/xquat更新，不仅支持freejoint。update_gaussian_properties显式.cuda()，不能当作CPU renderer。
- DISCOVERSE-Real2Sim中原始diff-gaussian-rasterization是研究／非商业许可；不把它外推成当前MIT＋gsplat运行时的许可。
- PhiRIE导出路径逐对象freejoint，未见该路径产生门轴／滑轨；不推断MuJoCo自身不支持关节。完整交互构建后台访问问题按官方750文档保留。
- RialToGUI SceneInit确实生成RevoluteJoint／PrismaticJoint描述，USDZExporter写local帧、axis、limit、friction、mass与碰撞字段；浏览器标注／导出不是内置物理验证。package.json无license，private=true只控制npm发布，不是许可声明。
