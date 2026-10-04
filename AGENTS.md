# AGENTS.md — 给 AI 编码代理的仓库约定

本仓库是中文游戏开发知识库。AI 代理在此工作须遵循：

## 结构地图

- `docs/` 手册正文；`docs/meta/design.md` 是顶层设计（改结构前必读）。
- `catalog/` 机器可读条目（YAML，`schema.json` 校验）。
- `resources/` 链接目录；`playbooks/` 实战手册；`templates/` 模板；`scripts/` 工具。

## 写作规则

- 简体中文；术语保留英文；不写空洞铺垫与套话式收尾；不虚构事实与链接。
- 新增链接必须真实可达；日期与数字要有来源。

## 修改规则

- 大改（结构、删并章节）先开 Issue。
- 提交前跑 markdownlint；新增链接跑 `scripts/check_links.py` 或 lychee。
- 不要改动机器可读文件（`catalog/*.yml`）的字段名，schema 需保持稳定。
