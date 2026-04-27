#!/usr/bin/env python3
"""Create the standard workspace folders and starter files for one industry."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


KNOWLEDGE_FILES = {
    "00-index.md": """# {name} - 研究入口

## 当前摘要

- 一句话理解：
- 当前判断：
- 关键不确定性：
- 下一步优先问题：

## 行业边界

- 包含：
- 不包含：
- 相邻行业：

## 中国十五五定位

- 国家重视原因：
- 对应战略方向：
- 中国产业链位置：
- 关键短板：
- 政策受益环节：
- 地方落地线索：

## 文件导航

- `01-industry-map.md`: 产业链和价值流。
- `02-technology-and-products.md`: 技术路线和产品形态。
- `03-market-and-policy.md`: 中国市场规模、十五五政策和监管。
- `04-companies.md`: 公司和竞争格局。
- `05-investment-view.md`: 投资逻辑和风险。
- `06-career-view.md`: 岗位地图和学习路径。
""",
    "01-industry-map.md": """# {name} - 产业链地图

## 产业链总览

| 环节 | 核心价值 | 代表公司/机构 | 关键壁垒 | 证据 |
| --- | --- | --- | --- | --- |
| 上游 |  |  |  |  |
| 中游 |  |  |  |  |
| 下游 |  |  |  |  |

## 价值流

- 谁付钱：
- 谁获益：
- 成本主要在哪里：
- 利润池集中在哪里：

## 关键瓶颈

- 供给瓶颈：
- 技术瓶颈：
- 监管瓶颈：
- 渠道瓶颈：
- 人才瓶颈：
""",
    "02-technology-and-products.md": """# {name} - 技术与产品

## 技术路线

| 路线 | 原理/特点 | 成熟度 | 优势 | 风险 | 代表玩家 |
| --- | --- | --- | --- | --- | --- |

## 产品形态

- 当前主流产品：
- 早期产品：
- 潜在替代产品：

## 成熟度与瓶颈

- 性能指标：
- 成本曲线：
- 标准化程度：
- 商业化障碍：
""",
    "03-market-and-policy.md": """# {name} - 市场与政策

## 中国市场

- 中国市场规模：
- 增长率：
- 渗透率：
- 地域分布：
- 客户结构：

## 十五五政策与监管

- 国家政策：
- 地方政策：
- 十五五相关线索：
- 监管约束：
- 采购/补贴/准入：
- 国际限制或出口管制：

## 数据口径

| 指标 | 数值 | 口径 | 时间 | 来源 |
| --- | --- | --- | --- | --- |
""",
    "04-companies.md": """# {name} - 公司与竞争

## 公司分层

| 公司 | 环节 | 商业模式 | 客户 | 优势 | 风险 | 证据 |
| --- | --- | --- | --- | --- | --- | --- |

## 竞争格局

- 集中度：
- 进入壁垒：
- 价格/成本趋势：
- 新进入者：
- 替代者：

## 需要跟踪的公司

- 上市公司：
- 未上市公司：
- 海外公司：
- 产业链关键供应商：
""",
    "05-investment-view.md": """# {name} - 投资视角

## 投资假设

- 核心 thesis：
- 时间 horizon：
- 中国政策催化：
- 关键催化剂：
- 估值锚：

## 风险

- 技术风险：
- 商业化风险：
- 政策风险：
- 竞争风险：
- 估值风险：

## 反证条件

- 什么事实会推翻当前判断：
- 哪些指标需要持续跟踪：

## 观察指标

| 指标 | 为什么重要 | 数据来源 | 更新频率 |
| --- | --- | --- | --- |
""",
    "06-career-view.md": """# {name} - 求职与学习视角

## 岗位地图

| 岗位族群 | 典型职位 | 核心能力 | 代表公司 | 证据 |
| --- | --- | --- | --- | --- |

## 学习路径

- 基础概念：
- 技术/业务能力：
- 推荐资料：
- 可做项目：

## 进入策略

- 适合背景：
- 入门岗位：
- 作品集建议：
- 面试准备：
- 招聘信号：
""",
}


def create_workspace(root: Path, slug: str, name: str) -> None:
    for subdir in [root / "raw" / slug / "documents", root / "raw" / slug / "data", root / "knowledge" / slug]:
        subdir.mkdir(parents=True, exist_ok=True)
        (subdir / ".gitkeep").touch(exist_ok=True)

    knowledge_dir = root / "knowledge" / slug
    for filename, template in KNOWLEDGE_FILES.items():
        path = knowledge_dir / filename
        if not path.exists():
            path.write_text(template.format(name=name).rstrip() + "\n", encoding="utf-8")

    sources = knowledge_dir / "sources.csv"
    if not sources.exists():
        with sources.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["id", "title", "source_type", "publisher", "date", "url_or_path", "evidence_grade", "notes"])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug", help="Stable English directory slug, e.g. robotics-embodied-ai")
    parser.add_argument("name", help="Human-readable industry name, e.g. 机器人（具身智能）")
    parser.add_argument("--root", default=".", help="Repository root")
    args = parser.parse_args()

    create_workspace(Path(args.root).resolve(), args.slug, args.name)


if __name__ == "__main__":
    main()
