# GameDev Atlas · 开源精选与书籍推荐

> **迭代第 ⑯ 轮**（收官轮）。定位：两份"趁手清单"——① GitHub 精选项目（按学习价值编排，全部经仓库存在性核查）；② 游戏开发书籍推荐（按方向编排，标注免费/中译情况）。
> 配套：《资源大全》（工具全量清单与官网链接）·《技术实现手册》（⑩）·《人物与厂商谱》（⑮）· 设计文档 §17（仓库落点）。
> 星标数随时变化，本清单以"学习价值"排序而非热度；仓库地址均已核查（核查记录见 `link-check-results.json` / `repo-check-results.json`）。

---

## 1. GitHub 精选：引擎与框架

| 仓库 | 语言 | 为什么值得看 |
| --- | --- | --- |
| [godotengine/godot](https://github.com/godotengine/godot) | C++ | 开源引擎旗舰：完整引擎源码 + 编辑器，学习引擎架构的最佳教材 |
| [bevyengine/bevy](https://github.com/bevyengine/bevy) | Rust | ECS 架构的现代教科书，插件生态活跃 |
| [raysan5/raylib](https://github.com/raysan5/raylib) | C | 极简游戏编程库：1 小时读完核心源码 |
| [love2d/love](https://github.com/love2d/love) | C++ | Lua 2D 框架；架构清晰、适合改源码学引擎 |
| [libgdx/libgdx](https://github.com/libgdx/libgdx) | Java | 跨平台框架工程化典范 |
| [MonoGame/MonoGame](https://github.com/MonoGame/MonoGame) | C# | XNA 血脉；C# 游戏框架事实标准 |
| [FNA-XNA/FNA](https://github.com/FNA-XNA/FNA) | C# | 老项目现代化移植的兼容层样本 |
| [stride3d/stride](https://github.com/stride3d/stride) | C# | 带编辑器与渲染管线的完整 C# 引擎 |
| [defold/defold](https://github.com/defold/defold) | C++ | 工业级轻量引擎；工具链完整 |
| [o3de/o3de](https://github.com/o3de/o3de) | C++ | 大厂级开源 3D 引擎（亚马逊） |
| [FlaxEngine/FlaxEngine](https://github.com/FlaxEngine/FlaxEngine) | C++/C# | 画质与工具并重的现代引擎 |
| [cocos/cocos-engine](https://github.com/cocos/cocos-engine) | TypeScript/C++ | 国产引擎；小游戏生态核心 |
| [HaxeFlixel/flixel](https://github.com/HaxeFlixel/flixel) | Haxe | 2D 框架的"电池全包"路线 |
| [heapsio/heaps](https://github.com/heapsio/heaps) | Haxe | 高性能跨平台引擎（作者：Haxe 之父） |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | JS | Web 3D 事实标准；示例库即教程库 |
| [BabylonJS/Babylon.js](https://github.com/BabylonJS/Babylon.js) | TS | 强类型 Web 3D 引擎；文档极全 |
| [pixijs/pixijs](https://github.com/pixijs/pixijs) | TS | Web 2D 渲染王者 |
| [phaserjs/phaser](https://github.com/phaserjs/phaser) | JS | HTML5 2D 游戏框架；小游戏友好 |
| [hajimehoshi/ebiten](https://github.com/hajimehoshi/ebiten) | Go | Go 生态 2D 引擎；API 简洁 |
| [panda3d/panda3d](https://github.com/panda3d/panda3d) | C++/Python | Python 3D 引擎老将 |

## 2. GitHub 精选：库与中间件

| 仓库 | 领域 | 为什么值得看 |
| --- | --- | --- |
| [skypjack/entt](https://github.com/skypjack/entt) | ECS | C++ ECS 的工业标准实现 |
| [SanderMertens/flecs](https://github.com/SanderMertens/flecs) | ECS | 快速 ECS + 丰富查询；文档优秀 |
| [erincatto/box2d](https://github.com/erincatto/box2d) | 2D 物理 | 2D 物理教科书（作者 Erin Catto） |
| [jrouwe/JoltPhysics](https://github.com/jrouwe/JoltPhysics) | 3D 物理 | 新一代高性能物理引擎 |
| [dimforge/rapier](https://github.com/dimforge/rapier) | 物理 | Rust 物理引擎（2D/3D） |
| [bulletphysics/bullet3](https://github.com/bulletphysics/bullet3) | 物理 | 老牌物理引擎与示例集 |
| [gfx-rs/wgpu](https://github.com/gfx-rs/wgpu) | 渲染 | Rust 图形抽象（WebGPU 实现） |
| [bkaradzic/bgfx](https://github.com/bkaradzic/bgfx) | 渲染 | 跨 API 渲染抽象层经典 |
| [floooh/sokol](https://github.com/floooh/sokol) | 渲染 | 单文件跨平台图形库 |
| [google/filament](https://github.com/google/filament) | 渲染 | 移动端 PBR 渲染引擎 |
| [DiligentGraphics/DiligentEngine](https://github.com/DiligentGraphics/DiligentEngine) | 渲染 | 现代图形 API 抽象引擎 |
| [mas-bandwidth/yojimbo](https://github.com/mas-bandwidth/yojimbo) | 网络 | 游戏网络协议库（Gaffer 出品） |
| [ValveSoftware/GameNetworkingSockets](https://github.com/ValveSoftware/GameNetworkingSockets) | 网络 | Valve 的可靠 UDP 传输 |
| [MirrorNetworking/Mirror](https://github.com/MirrorNetworking/Mirror) | 网络 | Unity 开源网络库 |
| [heroiclabs/nakama](https://github.com/heroiclabs/nakama) | 后端 | 开源游戏后端（账号/匹配/排行） |
| [colyseus/colyseus](https://github.com/colyseus/colyseus) | 后端 | Node 多人游戏服务器框架 |
| [mackron/miniaudio](https://github.com/mackron/miniaudio) | 音频 | 单文件音频库 |
| [jarikomppa/soloud](https://github.com/jarikomppa/soloud) | 音频 | 跨平台音频引擎 |
| [Auburn/FastNoiseLite](https://github.com/Auburn/FastNoiseLite) | 程序生成 | 噪声库多语言实现 |
| [recastnavigation/recastnavigation](https://github.com/recastnavigation/recastnavigation) | 寻路 | 行业标准导航网格方案 |
| [ocornut/imgui](https://github.com/ocornut/imgui) | 工具 UI | 调试/编辑器 UI 事实标准 |
| [mikke89/RmlUi](https://github.com/mikke89/RmlUi) | 游戏 UI | HTML/CSS 式游戏界面库 |
| [mxgmn/WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse) | 程序生成 | WFC 算法原始实现与示例 |
| [inkle/ink](https://github.com/inkle/ink) | 叙事 | 分支叙事脚本语言 |
| [YarnSpinnerTool/YarnSpinner](https://github.com/YarnSpinnerTool/YarnSpinner) | 叙事 | Unity/Godot 对话系统 |
| [renpy/renpy](https://github.com/renpy/renpy) | 视觉小说 | 完整 VN 引擎源码 |
| [dialogic-godot/dialogic](https://github.com/dialogic-godot/dialogic) | 对话 | Godot 对话插件 |

## 3. GitHub 精选：编辑器与工具

| 仓库 | 领域 | 为什么值得看 |
| --- | --- | --- |
| [mapeditor/tiled](https://github.com/mapeditor/tiled) | 关卡编辑 | 老牌瓦片地图编辑器 |
| [deepnight/ldtk](https://github.com/deepnight/ldtk) | 关卡编辑 | 现代 2D 关卡编辑器 |
| [Orama-Interactive/Pixelorama](https://github.com/Orama-Interactive/Pixelorama) | 像素美术 | Godot 写的像素编辑器；改引擎学 Godot |
| [LibreSprite/LibreSprite](https://github.com/LibreSprite/LibreSprite) | 像素美术 | Aseprite 开源分支 |
| [JannisX11/blockbench](https://github.com/JannisX11/blockbench) | 3D 建模 | 方块/低模编辑器 |
| [RodZill4/material-maker](https://github.com/RodZill4/material-maker) | 材质 | 程序化材质生成 |
| [DragonBones/DragonBonesJS](https://github.com/DragonBones/DragonBonesJS) | 骨骼动画 | 免费 2D 骨骼动画方案（JS 实现） |
| [audacity/audacity](https://github.com/audacity/audacity) | 音频 | 开源音频编辑器 |
| [LMMS/lmms](https://github.com/LMMS/lmms) | 音乐 | 开源 DAW |
| [Ardour/ardour](https://github.com/Ardour/ardour) | 音乐 | 专业级开源 DAW |
| [OpenMPT/openmpt](https://github.com/OpenMPT/openmpt) | 音乐 | 模块音乐制作 |
| [chr15m/jsfxr](https://github.com/chr15m/jsfxr) | 音效 | 网页音效生成器源码 |
| [itchio/butler](https://github.com/itchio/butler) | 发布 | itch.io 命令行发布工具 |
| [game-ci/unity-actions](https://github.com/game-ci/unity-actions) | CI | Unity 开源 CI 方案 |
| [godot-gdunit-labs/gdUnit4](https://github.com/godot-gdunit-labs/gdUnit4) | 测试 | Godot 单元测试框架 |
| [bitwes/Gut](https://github.com/bitwes/Gut) | 测试 | Godot 测试框架（老牌） |
| [baldurk/renderdoc](https://github.com/baldurk/renderdoc) | 调试 | 图形抓帧调试器 |

## 4. GitHub 精选：开源游戏（可读源码）

> 读源码是进阶捷径；从"与你类型相近、代码规模适中"的项目开始。

| 仓库 | 语言 | 为什么值得读 |
| --- | --- | --- |
| [00-Evan/shattered-pixel-dungeon](https://github.com/00-Evan/shattered-pixel-dungeon) | Java | 经典 Roguelike 全源码；作者长期写开发日志 |
| [CleverRaven/Cataclysm-DDA](https://github.com/CleverRaven/Cataclysm-DDA) | C++ | 超大型生存模拟；数据驱动设计的活教材 |
| [endless-sky/endless-sky](https://github.com/endless-sky/endless-sky) | C++ | 太空探索；游戏性代码清晰 |
| [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | Java | 塔防+自动化；性能与联机实现值得学 |
| [OpenRA/OpenRA](https://github.com/OpenRA/OpenRA) | C# | RTS 引擎重制；网络与 AI 完整 |
| [wesnoth/wesnoth](https://github.com/wesnoth/wesnoth) | C++ | 战棋常青树；内容与引擎分离范式 |
| [OpenRCT2/OpenRCT2](https://github.com/OpenRCT2/OpenRCT2) | C++ | 经典游戏逆向重制；多人联机实现 |
| [OpenTTD/OpenTTD](https://github.com/OpenTTD/OpenTTD) | C++ | 模拟经营教科书；插件生态 |
| [supertuxkart/stk-code](https://github.com/supertuxkart/stk-code) | C++ | 3D 卡丁车；完整管线与联机 |
| [Revolutionary-Games/Thrive](https://github.com/Revolutionary-Games/Thrive) | C# | 演化模拟；ECS 与科学模型结合 |
| [Warzone2100/warzone2100](https://github.com/Warzone2100/warzone2100) | C++ | 开源 RTS 老将 |
| [OpenMW/OpenMW](https://github.com/OpenMW/OpenMW) | C++ | 引擎重实现：物理/渲染/脚本全覆盖 |
| [scummvm/scummvm](https://github.com/scummvm/scummvm) | C++ | 多引擎虚拟机架构经典 |
| [chocolate-doom/chocolate-doom](https://github.com/chocolate-doom/chocolate-doom) | C | DOOM 源码移植：祖传代码学习 |
| [id-Software/DOOM](https://github.com/id-Software/DOOM) | C | 1997 年原版开源；图形史活化石 |
| [id-Software/Quake](https://github.com/id-Software/Quake) | C | Quake 引擎源码（3D 管线教科书） |
| [diasurgical/devilutionX](https://github.com/diasurgical/devilutionX) | C++ | 暗黑破坏神移植；老游戏现代化 |

## 5. GitHub 精选：学习与清单仓库

| 仓库 | 为什么值得 star |
| --- | --- |
| [munificent/game-programming-patterns](https://github.com/munificent/game-programming-patterns) | 《游戏编程模式》全书源码 |
| [JoeyDeVries/LearnOpenGL](https://github.com/JoeyDeVries/LearnOpenGL) | LearnOpenGL 配套代码 |
| [patriciogonzalezvivo/thebookofshaders](https://github.com/patriciogonzalezvivo/thebookofshaders) | 着色器之书源码 |
| [ssloy/tinyrenderer](https://github.com/ssloy/tinyrenderer) | 500 行软渲染器：图形管线扫盲 |
| [lettier/3d-game-shaders-for-beginners](https://github.com/lettier/3d-game-shaders-for-beginners) | 游戏着色器渐进教程 |
| [RayTracing/raytracing.github.io](https://github.com/RayTracing/raytracing.github.io) | 《Ray Tracing in One Weekend》系列 |
| [OneLoneCoder/olcPixelGameEngine](https://github.com/OneLoneCoder/olcPixelGameEngine) | 单文件引擎 + 数百集视频教程 |
| [godotengine/godot-demo-projects](https://github.com/godotengine/godot-demo-projects) | Godot 官方示例工程库 |
| [UnityTechnologies/open-project-1](https://github.com/UnityTechnologies/open-project-1) | Unity 官方开源项目（已归档，完整案例） |
| [ellisonleao/magictools](https://github.com/ellisonleao/magictools) | 经典游戏开发工具大全（本仓库互链） |
| [dawdle-deer/awesome-learn-gamedev](https://github.com/dawdle-deer/awesome-learn-gamedev) | 学习资源 mega-list |
| [FronkonGames/Awesome-Gamedev](https://github.com/FronkonGames/Awesome-Gamedev) | 分类资源清单 |
| [utilForever/game-developer-roadmap](https://github.com/utilForever/game-developer-roadmap) | 游戏开发者学习路线图 |
| [miloyip/game-programmer](https://github.com/miloyip/game-programmer) | 游戏程序员学习之路（中文友好） |
| [0xFA11/MultiplayerNetworkingResources](https://github.com/0xFA11/MultiplayerNetworkingResources) | 网络编程资源大全 |
| [Trilarion/opensourcegames](https://github.com/Trilarion/opensourcegames) | 开源游戏总目录 |
| [mattdesl/graphics-resources](https://github.com/mattdesl/graphics-resources) | 图形编程资源清单 |

## 6. GitHub 精选：AI 与生成工具

| 仓库 | 为什么值得看 |
| --- | --- |
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 节点式生成工作流；游戏资产管线核心 |
| [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | SD 生态起点 |
| [ollama/ollama](https://github.com/ollama/ollama) | 本地 LLM 一键运行 |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 本地推理引擎 |
| [facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft) | MusicGen/AudioGen 音频生成 |

---

## 7. 书籍推荐：游戏设计

| 书名 | 作者 | 备注 | 为什么读 |
| --- | --- | --- | --- |
| 《游戏设计艺术》(The Art of Game Design) | Jesse Schell | 有中译 | 透镜式工具箱；设计入门与自查首选 |
| 《快乐之道》(A Theory of Fun for Game Design) | Raph Koster | 有中译 | "游戏=学习"的本质论述，薄而深刻 |
| 《游戏设计梦工厂》(Game Design Workshop) | Tracy Fullerton | 有中译 | 练习驱动的教材，适合成体系学习 |
| 《通关！游戏设计之道》(Level Up!) | Scott Rogers | 有中译 | 幽默且实用的全流程设计指南 |
| 《游戏设计要则探秘》(Rules of Play) | Salen & Zimmerman | 英文 | 学术化设计理论基石（厚） |
| 《Game Feel》 | Steve Swink | 英文 | 手感（游戏感）设计唯一专著 |
| 《游戏机制：高级游戏设计技术》 | Adams & Dormans | 有中译 | 系统与机制建模（Machinations 方法论） |
| 《The Gamer's Brain》 | Celia Hodent | 英文 | UX 与认知科学；上线前体验设计 |
| 《Procedural Generation in Game Design》 | Short & Adams 编 | 英文 | 程序生成设计文集 |
| 《Characteristics of Games》 | Elias, Garfield, Gutschera | 英文 | 多人/竞技/平衡的底层分析 |
| 《游戏改变世界》(Reality Is Broken) | Jane McGonigal | 有中译 | 游戏价值与大设计视角 |

## 8. 书籍推荐：编程、架构与数学

| 书名 | 作者 | 备注 | 为什么读 |
| --- | --- | --- | --- |
| 《游戏编程模式》(Game Programming Patterns) | Robert Nystrom | 有中译；在线免费 | 设计模式的游戏语境；全书免费在线 |
| 《游戏引擎架构》(Game Engine Architecture) | Jason Gregory | 有中译 | 引擎全景权威，工具书属性 |
| 《Game Coding Complete》 | Mike McShaffry | 英文 | 工程实践与项目管理 |
| 《Foundations of Game Engine Development》 | Eric Lengyel | 英文 | 引擎数学/渲染底层系列 |
| 《3D Math Primer for Graphics and Game Development》 | Dunn & Parberry | 在线免费 | 图形与游戏数学（配套 gamemath.com） |
| 《Mathematics for 3D Game Programming and Computer Graphics》 | Eric Lengyel | 英文 | 数学进阶（与引擎书配套） |
| 《Essential Mathematics for Games and Interactive Applications》 | Van Verth & Bishop | 英文 | 游戏数学系统教材 |
| 《Effective Modern C++》 | Scott Meyers | 有中译 | C++ 现代化（引擎/工具向） |
| 《深入理解 C#》 | Jon Skeet | 有中译 | C# 深入（Unity 向） |
| 《Programming Game AI by Example》 | Mat Buckland | 英文 | 游戏 AI 实操经典 |
| 《AI for Games》 | Ian Millington | 英文 | AI 系统教材（覆盖广） |
| 《Multiplayer Game Programming》 | Glazer & Madhav | 英文 | 网络同步与架构教材 |
| 《Physics for Game Developers》 | David Bourg | 英文 | 物理编程入门 |

## 9. 书籍推荐：图形、渲染与着色器

| 书名 | 作者 | 备注 | 为什么读 |
| --- | --- | --- | --- |
| 《Real-Time Rendering》(4th) | Akenine-Möller 等 | 英文 | 实时渲染圣经（配 realtimerendering.com） |
| 《Physically Based Rendering》(PBRT) | Pharr, Jakob, Humphreys | 在线免费 | 离线渲染权威，配套完整代码 |
| 《Ray Tracing in One Weekend》系列 | Peter Shirley 等 | 在线免费 | 手写光追入门三部曲 |
| 《The Book of Shaders》 | Gonzalez-Vivo & Lowe | 在线免费 | 着色器交互入门 |
| 《LearnOpenGL》 | Joey de Vries | 在线免费 | 现代 OpenGL 全管线 |
| 《Unity Shader 入门精要》 | 冯乐乐 | 中文 | 中文圈 Shader 经典 |
| 《GPU Gems》1-3 | Nvidia 编 | 在线免费 | 图形技术文集（经典常读） |
| 《GPU Pro》系列 | Wolfgang Engel 编 | 英文 | 进阶图形文集 |
| 《Real-Time Shadows》 | Eisemann 等 | 英文 | 阴影技术专门书 |
| 《Computer Graphics: Principles and Practice》 | Hughes 等 | 英文 | 图形学大百科 |

## 10. 书籍推荐：美术与音频

| 书名 | 作者 | 备注 | 为什么读 |
| --- | --- | --- | --- |
| 《Color and Light》 | James Gurney | 英文 | 色彩与光影圣经（画家视角） |
| 《Framed Ink》 | Marcos Mateu-Mestre | 英文 | 构图与分镜（视觉叙事） |
| 《动画师生存手册》(The Animator's Survival Kit) | Richard Williams | 有中译 | 动画原理圣经 |
| 《How to Draw》 | Scott Robertson | 英文 | 透视与工业设计绘图 |
| 《Art Fundamentals》 | 3DTotal | 英文 | 美术基础综合（色彩/光/构图） |
| 《Pixel Art for Game Developers》 | Daniel Silber | 英文 | 像素美术入门 |
| 《The Complete Guide to Game Audio》 | Aaron Marks | 英文 | 游戏音频全流程 |
| 《Game Audio Implementation》 | Richard Stevens | 英文 | 引擎内音频实现实操 |
| 《The Sound Effects Bible》 | Ric Viers | 英文 | 音效制作方法论 |
| 《Mastering Audio》 | Bob Katz | 英文 | 混音与母带标准 |
| 《This Is Your Brain on Music》 | Daniel Levitin | 有中译 | 音乐认知（为什么音乐动人） |

## 11. 书籍推荐：生产、商业与行业纪实

| 书名 | 作者 | 备注 | 为什么读 |
| --- | --- | --- | --- |
| 《A Playful Production Process》 | Richard Lemarchand | 英文 | 从创意到发布的生产全流程（制作圣经） |
| 《Blood, Sweat, and Pixels》 | Jason Schreier | 有中译 | 3A 开发实录；项目管理反面教材合集 |
| 《Press Reset》 | Jason Schreier | 英文 | 工作室兴衰与从业者命运续作 |
| 《Masters of Doom》 | David Kushner | 中译《DOOM 启世录》 | id Software 传奇；技术与商业的双线史 |
| 《Console Wars》 | Blake Harris | 英文 | 世嘉 vs 任天堂主机大战纪实 |
| 《Spelunky》 | Derek Yu | 英文（Boss Fight Books） | 独立开发者设计日记 |
| 《The Making of Prince of Persia》 | Jordan Mechner | 英文 | 80 年代开发日记（考古价值） |
| 《Significant Zero》 | Walt Williams | 英文 | 3A 叙事设计师回忆录 |
| How To Market A Game 系列 | Chris Zukowski | 博客/电子书 | Steam 营销的实战知识库（非传统书，强烈推荐） |

## 12. 免费在线书与资源站（汇总）

| 名称 | 链接 | 内容 |
| --- | --- | --- |
| Game Programming Patterns | https://gameprogrammingpatterns.com/ | 设计模式（免费在线） |
| The Book of Shaders | https://thebookofshaders.com/ | 着色器入门 |
| LearnOpenGL | https://learnopengl.com/ | 现代 OpenGL |
| 3D Math Primer | https://gamemath.com/ | 图形数学在线版 |
| Ray Tracing in One Weekend | https://raytracing.github.io/ | 光追三部曲 |
| PBRT（第 4 版在线） | https://pbr-book.org/ | 离线渲染权威 |
| Game AI Pro（章节免费） | http://www.gameaipro.com/ | 游戏 AI 文集 |
| GPU Gems | https://developer.nvidia.com/gpugems | 图形技术文集 |
| The Nature of Code | https://natureofcode.com/ | 用代码玩系统/物理/生成 |

## 13. 使用建议

1. **选书原则**：每个方向"1 本主教材 + 1 本手册"——例：设计 =《游戏设计艺术》+《Game Feel》；图形 =《Real-Time Rendering》+《GPU Gems》。
2. **免费优先**：§12 的清单一整年都读不完；先免费后纸质，先在线后买断。
3. **书与仓库配对**：每个理论点配合一个 §1-§6 的仓库读源码，效果翻倍（如 ECS 理论 → flecs 源码）。
4. **建立个人书单**：在 `resources/books.md`（仓库内）按"读没读/值不值"维护你自己的版本——本清单是种子，不是终点。
