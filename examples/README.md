# examples/ — 示例区路线图与贡献指南

手册讲清概念与取舍，示例把概念落成能跑起来的最小工程。本页是示例区的施工图：定位与边界、目录规范、规划中的示例清单，以及贡献一个新示例的完整流程。示例区目前处于首批落地前的筹备阶段，欢迎按本页规则提名与认领。

## 示例区是什么

- 每个示例是一个独立目录：引擎工程本体加一份说明页，目标是克隆即跑。
- 示例是教学材料，不是产品工程——一个示例只讲透一两个知识点，能删的都删，不引入与教学点无关的依赖。
- 示例与手册配套：手册讲清为什么这么做，示例给出最小可行怎么写；规划表中每个示例都标注了对应手册。
- 与 [templates/](../templates/README.md) 的分工：templates 是可复制的文档骨架，examples 是可运行的代码与素材。

## 目录结构规范

每个示例目录使用同一套骨架，只保留引擎运作必需的文件：

```text
examples/
├── README.md                       # 本页：路线图与贡献指南
└── <引擎>-<主题>/                  # 单个示例目录，命名见下
    ├── README.md                   # 说明页（必需）
    ├── <引擎工程文件>              # 如 project.godot、Assets/、package.json 等
    ├── src/                        # 代码与场景，按引擎惯例组织
    ├── assets/
    │   └── CREDITS.md              # 素材清单：逐条来源与许可（必需）
    ├── LICENSE                     # 许可说明：代码 MIT，素材见 CREDITS.md
    └── .gitignore                  # 屏蔽引擎缓存与构建产物（必需）
```

规则：

- **命名**：`<引擎>-<主题>`，全小写英文与短横线，不用空格与中文；引擎名以[引擎轨道](../docs/engines/README.md)中的写法为准（godot、unity、bevy、raylib、renpy 等）。
- **工程文件**：只保留能直接打开运行的最小配置；说明页写明引擎大版本，如 Godot 4.3、Unity 6。
- **代码**：组织到 src/ 或引擎惯用目录；总量以一个下午读完为准，规模克制。
- **素材**：统一放 assets/ 并在 CREDITS.md 逐条登记来源、作者、许可与是否改动；没有外部素材时也保留清单，写明情况。整个示例目录建议控制在 10 MB 以内，超出的用生成脚本或更小的替代素材。
- **许可**：代码默认 MIT（与根 [LICENSE-CODE](../LICENSE-CODE) 一致）；素材许可按清单逐条标注；说明页末节复述同一口径。
- **说明页**：固定五节，模板见下文。

## 示例规划表

下表是示例区的路线图：12 个示例覆盖 Godot、Unity、Web、raylib、Bevy、Ren'Py 六条引擎路线，其中五个标注为首批（对应[设计文档](../docs/meta/design.md) Phase 2 的示例名额），先在五条不同路线上打通克隆即跑链路，其余按认领顺序推进。目录名为规划占用名，实现前可在对应 Issue 里讨论调整。

| 示例 | 引擎 | 难度 | 状态 | 覆盖知识点 | 对应手册 |
| --- | --- | --- | --- | --- | --- |
| 平台手感演示 · `godot-platformer-feel` | Godot 4 | 入门 | 首批 | 移动与跳跃曲线、土狼时间（coyote time）、跳跃缓冲、可变跳跃高度、相机跟随 | [游戏设计手册](../docs/fundamentals/game-design/README.md)（手感）· [平台跳跃](../docs/genres/platformer/README.md) |
| 2D 控制器 · `unity-2d-controller` | Unity | 入门 | 首批 | 输入系统、刚体与自写移动、跳跃缓冲、单向平台 | [Unity 轨道](../docs/engines/unity/README.md) · [平台跳跃](../docs/genres/platformer/README.md) |
| Web 发布链路 · `phaser-web-pipeline` | Phaser 3 | 入门 | 首批 | 打包与首包体积、触摸与自适应、静态托管、版本与缓存 | [Web 游戏轨道](../docs/engines/web/README.md) · [小游戏开发手册](../docs/publishing/minigame/README.md) |
| 小游戏骨构 · `raylib-mini-game` | raylib | 入门 | 首批 | 主循环与固定步长、状态切换、碰撞与输入、跨平台构建 | [轻量框架轨道](../docs/engines/micro/README.md) · [构建发布管线](../docs/pipelines/build-release/README.md) |
| ECS 起步 · `bevy-ecs-starter` | Bevy（Rust） | 进阶 | 首批 | 组件与系统、查询与过滤、固定步长、状态与调度 | [Bevy 轨道](../docs/engines/bevy/README.md) · [引擎源码阅读路线](../docs/fundamentals/engine-internals/README.md) |
| 塔防骨构 · `godot-tower-defense-skeleton` | Godot 4 | 进阶 | 后续 | 路径与波次、塔表与经济、目标选择、数值 UI 绑定 | [塔防](../docs/genres/tower-defense/README.md) · [技术实现手册](../docs/fundamentals/programming/README.md) |
| 海量敌人对象池 · `godot-enemy-pool` | Godot 4 | 进阶 | 后续 | 对象池复用、同屏千级实体、批量绘制、物理裁剪 | [幸存者类](../docs/genres/bullet-heaven/README.md) · [技术实现手册](../docs/fundamentals/programming/README.md) |
| 着色器练习集 · `webgl-shader-exercises` | WebGL2 | 进阶 | 后续 | UV 与噪声、光照模型、溶解与扰动、屏幕空间后处理 | [从零写渲染器路线](../docs/fundamentals/graphics/README.md) · [美术与音频手册](../docs/fundamentals/art-audio/README.md) |
| 数据驱动数值表 · `unity-data-driven-stats` | Unity | 进阶 | 后续 | 数值与公式分离、ScriptableObject、热调参、公式自测 | [游戏设计手册](../docs/fundamentals/game-design/README.md)（数值）· [技术实现手册](../docs/fundamentals/programming/README.md) |
| 对话系统迷你版 · `godot-dialogue-mini` | Godot 4 | 进阶 | 后续 | 对话数据格式、条件与变量、打字机与选项、存档接驳 | [视觉小说](../docs/genres/visual-novel/README.md) · [游戏设计手册](../docs/fundamentals/game-design/README.md)（叙事） |
| 本地化示例 · `unity-localization` | Unity | 综合 | 后续 | 词条表与键命名、占位符与复数、字体回退、伪本地化验证 | [本地化管线](../docs/pipelines/localization/README.md) · [避坑大全](../docs/pitfalls/README.md) |
| 分支叙事最小示例 · `renpy-branching-story` | Ren'Py | 入门 | 后续 | 分支与跳转、变量与条件、立绘与转场、打包发布 | [Ren'Py 轨道](../docs/engines/renpy/README.md) · [视觉小说](../docs/genres/visual-novel/README.md) |

难度分三档：入门（熟悉引擎基础操作即可跟做）、进阶（需配合对应手册补一两个概念）、综合（多个系统拼装，规模接近小项目）。更多引擎（Cocos、Unreal、GameMaker、MonoGame、Defold 等）的示例欢迎在后续批次提名。

## 贡献一个新示例

流程五步；说明页模板与评审要点在下文。

1. **提名**。用「新增内容」模板提 Issue，标题为 `[示例] <引擎>-<主题>`，写明要讲清的教学点、目标引擎与版本、最小功能清单，以及与规划和现有示例的关系（重叠时说明增量）。确认后即可认领。
2. **搭骨架**。按目录规范建目录，先写说明页再写代码：说不出要教什么，就说明选题还太大。
3. **实现与自测**。在干净环境（重新 clone 一次）严格按说明页步骤跑通，记录引擎版本、命令与预期现象。三条红线：跑不起来、素材许可不明、说明缺节。
4. **提 PR**。一个示例一个 PR，描述附运行验证；按 [CONTRIBUTING.md](../CONTRIBUTING.md) 的约定通过 markdownlint 与链接检查。
5. **评审合入**。评审按验收标准清单逐项过；通过后合入，并把本页规划表的状态列更新为已合入。

### 说明页模板

```markdown
# <示例名>（<引擎与大版本>）

- 教学点：<一句话>
- 预计跑通时间：<x 分钟>
- 前置阅读：<对应手册的相对链接>

## 解决什么问题

<为什么要有这个示例；读者学完能做什么。>

## 运行方式

<引擎版本、逐条命令、预期现象；不依赖口头补充。>

## 关键文件导读

<文件与作用的对照，说明为什么这样组织。>

## 练习与改动建议

<两三个可以动手改一改的小任务。>

## 许可与素材

<代码 MIT（见仓库根 LICENSE-CODE）；素材来源与许可见 CREDITS.md。>
```

### 评审要点

- **能直接运行**：评审者在新环境按说明页跑通；命令与版本明确，不依赖口头补充。缺依赖、只在作者机器上能跑的直接退回。
- **无版权问题**：素材逐条可溯源、许可兼容；禁止从商业作品拆包；字体与音频同样登记；引用他人代码注明出处与许可。
- **说明完整**：五节齐备，讲清为什么这么写而不只是贴代码；行文简体中文，术语与全库一致。
- **克制与一致**：命名与目录符合规范，不引入与教学点无关的依赖，不提交缓存与构建产物。

## 示例的验收标准清单

合入前按此清单逐项检查；建议贡献者在提 PR 前自行过一遍。

- [ ] 目录名符合 `<引擎>-<主题>` 规范，全小写英文短横线
- [ ] 干净环境按说明页可跑通，引擎版本与命令明确
- [ ] 说明页五节齐备：解决什么问题 / 运行方式 / 关键文件导读 / 练习与改动建议 / 许可与素材
- [ ] 素材逐条登记在 CREDITS.md，来源与许可可核实
- [ ] 代码为 MIT 口径，素材许可单独标注，两者不冲突
- [ ] 未提交引擎缓存与构建产物，.gitignore 已按引擎配好
- [ ] 除教学点外无多余依赖；能删的都删，规模克制
- [ ] 站内引用使用相对链接，markdownlint 与链接检查通过
- [ ] PR 描述含运行验证记录（环境、命令、结果）
- [ ] 参考或移植自公开教程时，注明出处并确认许可兼容

## 相关

- [引擎轨道](../docs/engines/README.md)：12 条引擎路线，示例的引擎口径与工程习惯以此为准。
- [设计文档](../docs/meta/design.md)：示例区的定位原文与标准（第 10 节）。
- [templates/](../templates/README.md)：文档模板，与示例说明页互补。
- [CONTRIBUTING.md](../CONTRIBUTING.md)：提交约定与 CI（markdownlint、链接检查）。
- [ROADMAP.md](../ROADMAP.md)：示例区所在的版本批次与阶段目标。
