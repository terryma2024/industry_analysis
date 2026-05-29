---
title: Claims Index
type: index
date_created: 2026-05-29
last_updated: 2026-05-29
tags:
  - wiki
  - claims
  - evidence
---

# Claims Index

`_claims/` 用于存放原子化、可溯源的判断。当前先建立目录和规则，后续在行业研究深化时，把高价值判断从行业笔记、新闻摘要和 source 页面中逐条抽取出来。

## Claim 模板

```markdown
---
title:
type: claim
status: active | disputed | needs-review
date_created:
last_updated:
sources:
  - raw/...
tags:
---

# Claim

## Statement

一条可验证的事实、估计、判断或假设。

## Evidence

- 来源、页码、URL、表格或数据集。

## Confidence

- High / Medium / Low，并说明原因。

## 关联连接

- 相关概念、实体、来源和行业页面。
```
