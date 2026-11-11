---
source_id: SRC-robotics-752
title: SimFoundry固定INSTALL.md路径失败记录
source_type: capture_failure
date: 2026-11-10
capture_method: analyst-failure-note
status: failed
url: https://raw.githubusercontent.com/NVlabs/SimFoundry/9e34ebefcd020583fbb755a8b57268dce78eca26/INSTALL.md
---

# 失败记录

固定README指向INSTALL.md，但该固定提交路径的直接请求返回HTTP 404。通用捕获工具也记录failed；未生成官方正文。本文件仅为失败说明，不是安装文档替代品。

安装／服务需求根据同提交README（SRC-robotics-747）及THIRD_PARTY_LICENSES.md（SRC-robotics-757）核查。以后应检索官方正确安装路径，不能因本路径失效断言全部项目无法安装。
