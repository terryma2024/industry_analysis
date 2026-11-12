---
source_id: SRC-robotics-802
title: Atlas schema inspection and public health check
source_type: local_probe
publisher: Analyst
source_date: 2026-11-12
evidence_grade: S
capture_method: local-schema-parse-and-unauthenticated-http-get
tags: [raw/source, evidence/s]
---

# Atlas schema 与公开健康路由有限核查

配套 [JSON 完整记录](SRC-robotics-802-atlas-schema-health-audit.json)。

- 对 790–793 四份已归档 OpenAPI 文档解析，请求字段、required、版本与源文件 SHA256 见 JSON。
- `PosedImages2SplatsRequest` 没有 `refine`，且 `additionalProperties=false`；教程 draft 字段与 schema 不一致。未调用该任务，不把静态不相容当成已实测 HTTP 拒绝。
- 对生产域 `/api/v2/health` 做一次无认证 GET，HTTP 200、返回 status=ok。执行时间与原始响应见 JSON；只证明当前执行环境该路由可达。
- 没有登录、安装、上传素材、生成、扣费、仿真、训练或控制机器人。
- 5m/512=9.765625mm 是示例离散格距，非几何精度实测；$10/$30 仅为2次/6次 refined splat 文档单价的算术。
