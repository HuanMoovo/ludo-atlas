# genres/ — 分类型开发手册

按[设计文档 §11](../meta/design.md) 的 18 家族 / 112 类型推进（已落盘 71 类），每类一页，统一七节结构（定位与核心循环 / 体验目标与标杆作品 / 设计要点 / 技术要点 / 内容量与工作量 / 原型起步 / 常见坑）。

## P0 批次（已完成 · 10 类）

| 类型 | 一句话定位 |
| --- | --- |
| [平台跳跃](platformer/README.md) | 手感三要素、相机设计、教考变奏与跳跃半径度量。 |
| [银河城](metroidvania/README.md) | 锁-钥匙-回访三元组、连通地图与体量控制。 |
| [肉鸽（Roguelite）](roguelite/README.md) | 双循环、受控随机与 build 构筑多样性。 |
| [塔防](tower-defense/README.md) | 路径节点图、塔的克制矩阵、经济与波次曲线。 |
| [解谜](puzzle/README.md) | 机制克制、无文字教学与顿悟时刻设计。 |
| [视觉小说](visual-novel/README.md) | 分支治理、文本量估算与演出节奏。 |
| [生存建造](survival-craft/README.md) | 四阶段循环、压力源克制与解锁节奏。 |
| [农场经营](farming-sim/README.md) | 日程循环、作物矩阵与社交系统。 |
| [幸存者类](bullet-heaven/README.md) | 短局结构、构筑爆发与同屏密度工程。 |
| [放置增量](idle-incremental/README.md) | 离线收益、指数曲线与转生系统。 |

## P1 批次（已完成 · 15 类）

| 类型 | 一句话定位 |
| --- | --- |
| [动作 RPG](action-rpg/README.md) | 动作手感与成长系统双层循环、词条与掉落曲线。 |
| [JRPG](jrpg/README.md) | 回合制战斗、队伍成长与文本演出量级。 |
| [双摇杆射击](twin-stick/README.md) | 移动与瞄准分离、空间压迫与武器矩阵。 |
| [FPS](fps/README.md) | 射击手感四要素、遭遇设计与单人/多人工程分野。 |
| [弹幕射击](shmup/README.md) | 弹幕设计语言、擦弹判定与 Boss 模式库。 |
| [模拟经营](management/README.md) | 经营循环、数值经济与信息设计。 |
| [城市建造](city-builder/README.md) | 四层城市模拟、代理模型与负反馈。 |
| [殖民模拟](colony-sim/README.md) | 个体模拟、故事生成器与事件压力曲线。 |
| [卡牌构筑](deckbuilder/README.md) | 费用与效果曲线、构筑 combo 与平衡测试。 |
| [RTS](rts/README.md) | 克制矩阵、经济节奏与操作体验。 |
| [物理解谜](physics-puzzle/README.md) | 物理模拟作为机制、卡死防护与调参直觉。 |
| [点击式冒险](point-and-click/README.md) | 物品栏组合逻辑、防卡死引导与手绘美术量级。 |
| [文字冒险](interactive-fiction/README.md) | parser 与选择式两大流派、状态追踪与文本预算。 |
| [自走棋](auto-battler/README.md) | 经济利息、共享牌池与站位克制。 |
| [沙盒建造](sandbox-building/README.md) | 工具即游戏、规则组合与分享机制。 |

## P2 批次（已完成 · 26 类）

| 类型 | 一句话定位 |
| --- | --- |
| [竞速](racing/README.md) | 手感翻译、赛道弯道节奏与对手配速。 |
| [格斗](fighting/README.md) | 帧数据、连段资源与输入宽容。 |
| [清版动作](beat-em-up/README.md) | 群战结构、打击感三件套与波次设计。 |
| [音乐节奏](rhythm/README.md) | 判定系统、谱面流程与音频校准。 |
| [派对游戏](party/README.md) | 低门槛高混乱、小游戏合集与笑点设计。 |
| [合作闯关](co-op/README.md) | 互补设计、救援机制与沟通设计。 |
| [MMO](mmo/README.md) | 三重成本的现实核算、社交与经济治理。 |
| [社交推理](social-deduction/README.md) | 信息不对称、讨论节奏与反作弊。 |
| [叙事探索](walking-sim/README.md) | 环境叙事、玩家契约与演出成本。 |
| [密室逃脱](escape-room/README.md) | 谜题图、分级提示与多人协作。 |
| [大逃杀](battle-royale/README.md) | 缩圈节奏、物资经济与联机门槛的现实核算（俗称「吃鸡」）。 |
| [MOBA](moba/README.md) | 兵线经济、英雄克制与赛事生态。 |
| [潜行](stealth/README.md) | 感知系统、双路径设计与失败宽容。 |
| [恐怖](horror/README.md) | 恐惧资源模型、氛围与声音设计。 |
| [侦探推理](detective/README.md) | 线索冗余、推理交互与顿悟设计。 |
| [解谜平台](puzzle-platformer/README.md) | 机制耦合、教考变奏与防挫败。 |
| [4X](four-x/README.md) | 四环循环、迷雾探测与策略 AI。 |
| [体育游戏](sports/README.md) | 规则还原、判定简化与授权现实。 |
| [养成](raising-sim/README.md) | 培养循环、成长曲线与事件分支。 |
| [模拟驾驶](vehicle-sim/README.md) | 拟真分野、车辆物理与职业循环。 |
| [太空模拟](space-sim/README.md) | 飞行手感、尺度艺术与生成密度。 |
| [三消](match-3/README.md) | 连锁手感、数值骨架与无解检测。 |
| [桌游数字化](board-game/README.md) | 自动化分界、规则引擎与异步对局。 |
| [集换式卡牌](card-game-tcg/README.md) | 收集对战双循环与卡池管理。 |
| [文字游戏](word-game/README.md) | 词库工程、每日谜题与分享设计。 |
| [问答测验](trivia-quiz/README.md) | 题库工程、抽题公平与内容成本。 |

## P3 批次（已完成 · 20 类）

| 类型 | 一句话定位 |
| --- | --- |
| [开放世界](open-world/README.md) | 结构而非类型：密度、引导与「小开放世界」。 |
| [撤离射击](extraction-shooter/README.md) | 搜打撤四环、风险心理学与带出经济。 |
| [怪物收集（宝可梦类）](creature-collector/README.md) | 收集-培养-对战-交换四环与乘数成本。 |
| [动作冒险](action-adventure/README.md) | 探索-战斗-解谜三支柱与箱庭节奏。 |
| [沉浸模拟](immersive-sim/README.md) | 系统交互网络与关卡即沙盒。 |
| [生存恐怖](survival-horror/README.md) | 资源稀缺、箱庭回环与敌人分级。 |
| [英雄射击](hero-shooter/README.md) | 枪法×技能双维与英雄内容引擎。 |
| [大战略](grand-strategy/README.md) | 系统嵌套、历史事件与可读性管理。 |
| [割草无双](hack-and-slash/README.md) | 以一敌百的爽感公式与同屏工程。 |
| [恋爱模拟](dating-sim/README.md) | 好感度系统、日程管理与路线文本量。 |
| [工厂自动化](factory-automation/README.md) | 自动化四环、物流吞吐与蓝图工具。 |
| [抽卡养成](gacha-rpg/README.md) | 收集-养成-编队三环与长线运营节奏。 |
| [战术射击](tactical-shooter/README.md) | 低容错信息博弈与回合经济。 |
| [战棋（SRPG）](tactics-srpg/README.md) | 行动顺序、职业克制与永久死亡。 |
| [超休闲](hypercasual/README.md) | 一分钟上手公式与关卡速产流水线。 |
| [无尽跑酷](endless-runner/README.md) | 极简操作、程序生成与速度感。 |
| [教育游戏](educational/README.md) | 双重目标设计与学习效果评估。 |
| [钓鱼](fishing/README.md) | 拉扯博弈、图鉴收集与等待节奏。 |
| [生活模拟](life-sim/README.md) | 需求驱动日程与身份表达。 |
| [寻物找茬](hidden-object/README.md) | 找物机制、场景美术成本与叙事结合。 |

## 其余类型（持续扩充）

- 混合类型与长尾类型按批次继续补充，欢迎通过 Issue 提名。

先行阅读：

- [游戏设计手册](../fundamentals/game-design/README.md)（类型无关的设计基础）
- [关卡设计手册](../fundamentals/level-design/README.md)（十类玩法空间要点 + 经典拆解）
- [案例研究集](../postmortems/README.md)（各类型成功与失败案例）
