<p align="center"><img src="assets/logo.svg" alt="Ludo Atlas logo" width="150"></p>

# Ludo Atlas · 游戏开发全景手册

> **一个中文优先、结构化的开源游戏开发知识库。** 从学习、避坑、法务、上架，到设计、技术、美术、制作、运营与 AI 工作流：把"做游戏"拆成 **94 份文档（约 65.9 万字）**，全部外链逐条核查，可持续贡献。

**📖 在线阅读：https://huanmoovo.github.io/ludo-atlas/ （GitHub Pages，由 CI 自动部署）**

[![Lint](https://github.com/HuanMoovo/ludo-atlas/actions/workflows/lint.yml/badge.svg)](https://github.com/HuanMoovo/ludo-atlas/actions/workflows/lint.yml)
[![Link Check](https://github.com/HuanMoovo/ludo-atlas/actions/workflows/links.yml/badge.svg)](https://github.com/HuanMoovo/ludo-atlas/actions/workflows/links.yml)
[![License: CC BY-SA 4.0 + MIT](https://img.shields.io/badge/License-CC%20BY--SA%204.0%20%2B%20MIT-blue.svg)](LICENSE)

## 这是什么

一套覆盖游戏开发全流程的中文开源手册：

- **讲清楚"怎么做"和"为什么"**，不给空话；数据、政策与费率都给出可核实的来源，并标注核实时点。
- **全部外链逐条核查**（发布前逐条验证 + CI 每周自动复查），死链有一整套处理机制。
- **结构设计科学**：94 份文档各司其职、互相引用不重复；目录与长期规划见 [设计文档](docs/meta/design.md)。

## 内容地图

### 基础学科（docs/fundamentals/）

| 手册 | 说明 |
| --- | --- |
| [游戏设计手册](docs/fundamentals/game-design/README.md) | 流程、核心循环、系统、数值、手感、UX、叙事 |
| [技术实现手册](docs/fundamentals/programming/README.md) | 架构选型、核心系统、性能、多平台、网络、基建 |
| [美术与音频手册](docs/fundamentals/art-audio/README.md) | Art Bible、2D/3D、UI、技术美术、音频设计与交付 |
| [制作管理手册](docs/fundamentals/production/README.md) | 立项、估算、阶段模型、范围控制、QA、复盘 |
| [关卡设计手册](docs/fundamentals/level-design/README.md) | 度量、引导、节奏、白盒流程、十个经典拆解 |
| [引擎源码阅读路线](docs/fundamentals/engine-internals/README.md) | Godot / Bevy / 小引擎，方法论与周计划 |
| [从零写渲染器路线](docs/fundamentals/graphics/README.md) | 软光栅化 → 实时 API → 光追 |

### 风险与法务

| [避坑大全](docs/pitfalls/README.md) | 高频坑位合集（分领域、分级） |
| [法务、专利与竞争手册](docs/publishing/legal/README.md) | 版权、商标、专利、合同、出海合规、竞品分析 |

### 发行与平台（docs/publishing/）

- [全平台上架手册（含网络游戏专项）](playbooks/platform-launch/README.md)
- [运营与增长手册](docs/publishing/live-ops/README.md)
- [小游戏开发手册](docs/publishing/minigame/README.md)（微信/抖音/硬件渠道）
- [主机开发手册](docs/publishing/console/README.md)（ID@Xbox / PlayStation / Nintendo）
- [VR/AR 开发手册](docs/publishing/xr/README.md)
- [电竞与竞技设计手册](docs/publishing/esports/README.md)

### 管线与深入（docs/pipelines/）

- [Mod 与 UGC 手册](docs/pipelines/modding/README.md)
- [联机与后端深入手册](docs/pipelines/multiplayer-backend/README.md)

### AI 与案例

- [AI 工作流手册](docs/ai/README.md)：编码代理、引擎 MCP、美术音频管线、8 个端到端工作流、合规红线
- [案例研究集](docs/postmortems/README.md)：24 个公开案例的四段拆解

### 历史与人物（docs/meta/）

- [游戏简史](docs/meta/history/README.md)
- [独立开发者与厂商谱](docs/meta/people/README.md)
- [独立开发者深度谱](docs/meta/people/indie/README.md)（44 组档案）
- [设计文档](docs/meta/design.md)：仓库顶层设计与迭代记录

### 实战与资源

- [独立开发生存手册](playbooks/indie-survival/README.md)
- [游戏开发综合资源大全](resources/README.md)（521 条链接）
- [开源精选与书籍推荐](resources/books-and-repos.md)（103 个 GitHub 项目 + 60 余本书）

## 三条推荐阅读路线

- **零基础入门**：[资源大全](resources/README.md) → [游戏设计手册](docs/fundamentals/game-design/README.md) → [技术实现手册](docs/fundamentals/programming/README.md) → [AI 工作流手册](docs/ai/README.md)
- **准备做第一款作品**：[一页纸立项书](templates/gdd-mini.md) → [制作管理手册](docs/fundamentals/production/README.md) → [避坑大全](docs/pitfalls/README.md) → [独立开发生存手册](playbooks/indie-survival/README.md) → [全平台上架手册](playbooks/platform-launch/README.md)
- **进阶深挖**：[引擎源码阅读路线](docs/fundamentals/engine-internals/README.md) → [从零写渲染器路线](docs/fundamentals/graphics/README.md) → [联机与后端深入手册](docs/pipelines/multiplayer-backend/README.md)

## 仓库结构

```text
docs/           手册正文（按主题分区）
catalog/        机器可读条目（YAML + schema，单一事实来源）
resources/      链接目录与书单
playbooks/      端到端实战手册（上架、生存）
templates/      可复用模板（立项书、复盘）
scripts/        工具脚本（链接核查）
data/checks/    发布前核查记录归档
```

## 链接与事实核查

- 发布前对全部外链逐条验证（原始记录见 [data/checks/](data/checks/README.md)）；CI 每周自动复检。
- 政策、费率、平台规则类内容均标注核实时点；行动前请以官方最新文档为准。

## 参与贡献

勘误、新增内容、工程改进都欢迎，见 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [行为准则](CODE_OF_CONDUCT.md)。

## 许可

文档内容采用 [CC BY-SA 4.0](LICENSE)，代码采用 [MIT](LICENSE-CODE)。

## 说明

手册内容参考了大量公开资料、平台官方文档与开发者访谈，版权归各自作者；文中的数字与政策以行动时点的官方最新信息为准。
