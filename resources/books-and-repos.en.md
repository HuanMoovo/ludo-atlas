# Ludo Atlas · Open Source Picks & Book Recommendations

> Positioning: two handy lists: (1) curated GitHub projects (ordered by learning value; every repository's existence has been verified); (2) game development book recommendations (ordered by area, with free / Chinese-translation status noted).
> Companions: Resources (the full tool list with official links) · Programming Handbook · Indie Developers & Companies · About This Repo (where each handbook lands in the repo).
> Star counts change at any time; this list is ordered by learning value rather than popularity. All repository URLs have been verified (verification records in `link-check-results.json` / `repo-check-results.json`).

---

## 1. GitHub Picks: Engines & Frameworks

| Repo | Language | Why it's worth a look |
| --- | --- | --- |
| [godotengine/godot](https://github.com/godotengine/godot) | C++ | The flagship open-source engine: complete engine source plus editor, the best textbook for learning engine architecture |
| [bevyengine/bevy](https://github.com/bevyengine/bevy) | Rust | A modern textbook of ECS architecture, with an active plugin ecosystem |
| [raysan5/raylib](https://github.com/raysan5/raylib) | C | A minimalist game programming library: the core source reads in an hour |
| [love2d/love](https://github.com/love2d/love) | C++ | A Lua 2D framework; clean architecture, well suited to learning engines by editing the source |
| [libgdx/libgdx](https://github.com/libgdx/libgdx) | Java | A model of engineering for cross-platform frameworks |
| [MonoGame/MonoGame](https://github.com/MonoGame/MonoGame) | C# | XNA lineage; the de facto standard for C# game frameworks |
| [FNA-XNA/FNA](https://github.com/FNA-XNA/FNA) | C# | A sample compatibility layer for modernizing an old project |
| [stride3d/stride](https://github.com/stride3d/stride) | C# | A complete C# engine with editor and rendering pipeline |
| [defold/defold](https://github.com/defold/defold) | C++ | An industrial-grade lightweight engine; a complete toolchain |
| [o3de/o3de](https://github.com/o3de/o3de) | C++ | A big-tech-grade open-source 3D engine (Amazon) |
| [FlaxEngine/FlaxEngine](https://github.com/FlaxEngine/FlaxEngine) | C++/C# | A modern engine that gives equal weight to visual quality and tooling |
| [cocos/cocos-engine](https://github.com/cocos/cocos-engine) | TypeScript/C++ | An engine from the Chinese ecosystem; at the core of the mini-game ecosystem |
| [HaxeFlixel/flixel](https://github.com/HaxeFlixel/flixel) | Haxe | A 2D framework that takes the "batteries included" route |
| [heapsio/heaps](https://github.com/heapsio/heaps) | Haxe | A high-performance cross-platform engine (by the creator of Haxe) |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | JS | The de facto standard for Web 3D; the example library is a tutorial library |
| [BabylonJS/Babylon.js](https://github.com/BabylonJS/Babylon.js) | TS | A strongly typed Web 3D engine; exceptionally complete documentation |
| [pixijs/pixijs](https://github.com/pixijs/pixijs) | TS | The king of Web 2D rendering |
| [phaserjs/phaser](https://github.com/phaserjs/phaser) | JS | An HTML5 2D game framework; mini-game friendly |
| [hajimehoshi/ebiten](https://github.com/hajimehoshi/ebiten) | Go | A 2D engine in the Go ecosystem; a clean API |
| [panda3d/panda3d](https://github.com/panda3d/panda3d) | C++/Python | The veteran Python 3D engine |

## 2. GitHub Picks: Libraries & Middleware

| Repo | Area | Why it's worth a look |
| --- | --- | --- |
| [skypjack/entt](https://github.com/skypjack/entt) | ECS | The industry-standard C++ ECS implementation |
| [SanderMertens/flecs](https://github.com/SanderMertens/flecs) | ECS | Fast ECS with rich queries; excellent documentation |
| [erincatto/box2d](https://github.com/erincatto/box2d) | 2D physics | The textbook of 2D physics (by Erin Catto) |
| [jrouwe/JoltPhysics](https://github.com/jrouwe/JoltPhysics) | 3D physics | A new-generation high-performance physics engine |
| [dimforge/rapier](https://github.com/dimforge/rapier) | Physics | A Rust physics engine (2D/3D) |
| [bulletphysics/bullet3](https://github.com/bulletphysics/bullet3) | Physics | A veteran physics engine, with a collection of examples |
| [gfx-rs/wgpu](https://github.com/gfx-rs/wgpu) | Rendering | A Rust graphics abstraction (a WebGPU implementation) |
| [bkaradzic/bgfx](https://github.com/bkaradzic/bgfx) | Rendering | The classic cross-API rendering abstraction layer |
| [floooh/sokol](https://github.com/floooh/sokol) | Rendering | Single-file cross-platform graphics libraries |
| [google/filament](https://github.com/google/filament) | Rendering | A PBR rendering engine for mobile |
| [DiligentGraphics/DiligentEngine](https://github.com/DiligentGraphics/DiligentEngine) | Rendering | A modern graphics API abstraction engine |
| [mas-bandwidth/yojimbo](https://github.com/mas-bandwidth/yojimbo) | Networking | A game networking protocol library (by Gaffer) |
| [ValveSoftware/GameNetworkingSockets](https://github.com/ValveSoftware/GameNetworkingSockets) | Networking | Valve's reliable UDP transport |
| [MirrorNetworking/Mirror](https://github.com/MirrorNetworking/Mirror) | Networking | An open-source Unity networking library |
| [heroiclabs/nakama](https://github.com/heroiclabs/nakama) | Backend | An open-source game backend (accounts / matchmaking / leaderboards) |
| [colyseus/colyseus](https://github.com/colyseus/colyseus) | Backend | A Node multiplayer game server framework |
| [mackron/miniaudio](https://github.com/mackron/miniaudio) | Audio | A single-file audio library |
| [jarikomppa/soloud](https://github.com/jarikomppa/soloud) | Audio | A cross-platform audio engine |
| [Auburn/FastNoiseLite](https://github.com/Auburn/FastNoiseLite) | Procedural generation | Noise libraries with implementations in many languages |
| [recastnavigation/recastnavigation](https://github.com/recastnavigation/recastnavigation) | Pathfinding | The industry-standard navmesh solution |
| [ocornut/imgui](https://github.com/ocornut/imgui) | Tool UI | The de facto standard for debug and editor UI |
| [mikke89/RmlUi](https://github.com/mikke89/RmlUi) | Game UI | An HTML/CSS-style game interface library |
| [mxgmn/WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse) | Procedural generation | The original WFC algorithm implementation, with examples |
| [inkle/ink](https://github.com/inkle/ink) | Narrative | A scripting language for branching narrative |
| [YarnSpinnerTool/YarnSpinner](https://github.com/YarnSpinnerTool/YarnSpinner) | Narrative | A dialogue system for Unity/Godot |
| [renpy/renpy](https://github.com/renpy/renpy) | Visual novel | Complete VN engine source |
| [dialogic-godot/dialogic](https://github.com/dialogic-godot/dialogic) | Dialogue | A Godot dialogue plugin |

## 3. GitHub Picks: Editors & Tools

| Repo | Area | Why it's worth a look |
| --- | --- | --- |
| [mapeditor/tiled](https://github.com/mapeditor/tiled) | Level editing | The veteran tile map editor |
| [deepnight/ldtk](https://github.com/deepnight/ldtk) | Level editing | A modern 2D level editor |
| [Orama-Interactive/Pixelorama](https://github.com/Orama-Interactive/Pixelorama) | Pixel art | A pixel editor written in Godot; learn Godot by modifying the engine |
| [LibreSprite/LibreSprite](https://github.com/LibreSprite/LibreSprite) | Pixel art | An open-source fork of Aseprite |
| [JannisX11/blockbench](https://github.com/JannisX11/blockbench) | 3D modeling | A blocky / low-poly model editor |
| [RodZill4/material-maker](https://github.com/RodZill4/material-maker) | Materials | Procedural material generation |
| [DragonBones/DragonBonesJS](https://github.com/DragonBones/DragonBonesJS) | Skeletal animation | A free 2D skeletal animation solution (JS implementation) |
| [audacity/audacity](https://github.com/audacity/audacity) | Audio | An open-source audio editor |
| [LMMS/lmms](https://github.com/LMMS/lmms) | Music | An open-source DAW |
| [Ardour/ardour](https://github.com/Ardour/ardour) | Music | A professional-grade open-source DAW |
| [OpenMPT/openmpt](https://github.com/OpenMPT/openmpt) | Music | Module music production |
| [chr15m/jsfxr](https://github.com/chr15m/jsfxr) | Sound effects | Source for a web sound-effect generator |
| [itchio/butler](https://github.com/itchio/butler) | Publishing | The itch.io command-line publishing tool |
| [game-ci/unity-actions](https://github.com/game-ci/unity-actions) | CI | An open-source CI solution for Unity |
| [godot-gdunit-labs/gdUnit4](https://github.com/godot-gdunit-labs/gdUnit4) | Testing | A unit testing framework for Godot |
| [bitwes/Gut](https://github.com/bitwes/Gut) | Testing | A Godot testing framework (the veteran) |
| [baldurk/renderdoc](https://github.com/baldurk/renderdoc) | Debugging | A graphics frame-capture debugger |

## 4. GitHub Picks: Open-Source Games (Readable Source)

> Reading source code is a shortcut to the next level; start with projects close to your own genre and moderate in code size.

| Repo | Language | Why it's worth reading |
| --- | --- | --- |
| [00-Evan/shattered-pixel-dungeon](https://github.com/00-Evan/shattered-pixel-dungeon) | Java | Complete source for a classic roguelike; the author keeps a long-running dev log |
| [CleverRaven/Cataclysm-DDA](https://github.com/CleverRaven/Cataclysm-DDA) | C++ | A very large survival simulation; a living textbook of data-driven design |
| [endless-sky/endless-sky](https://github.com/endless-sky/endless-sky) | C++ | Space exploration; clear gameplay code |
| [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | Java | Tower defense + automation; the performance and multiplayer work is worth studying |
| [OpenRA/OpenRA](https://github.com/OpenRA/OpenRA) | C# | A rebuilt RTS engine; networking and AI included in full |
| [wesnoth/wesnoth](https://github.com/wesnoth/wesnoth) | C++ | The evergreen turn-based strategy game; a model of separating content from engine |
| [OpenRCT2/OpenRCT2](https://github.com/OpenRCT2/OpenRCT2) | C++ | A reverse-engineered remake of a classic; multiplayer implementation included |
| [OpenTTD/OpenTTD](https://github.com/OpenTTD/OpenTTD) | C++ | A management simulation textbook; a plugin ecosystem |
| [supertuxkart/stk-code](https://github.com/supertuxkart/stk-code) | C++ | A 3D kart racer; complete pipeline and multiplayer |
| [Revolutionary-Games/Thrive](https://github.com/Revolutionary-Games/Thrive) | C# | An evolution simulation; ECS combined with scientific models |
| [Warzone2100/warzone2100](https://github.com/Warzone2100/warzone2100) | C++ | A veteran of open-source RTS |
| [OpenMW/OpenMW](https://github.com/OpenMW/OpenMW) | C++ | An engine reimplementation: physics / rendering / scripting all covered |
| [scummvm/scummvm](https://github.com/scummvm/scummvm) | C++ | The classic multi-engine virtual machine architecture |
| [chocolate-doom/chocolate-doom](https://github.com/chocolate-doom/chocolate-doom) | C | A DOOM source port: a study in inherited code |
| [id-Software/DOOM](https://github.com/id-Software/DOOM) | C | The 1997 original, open-sourced; a living fossil of graphics history |
| [id-Software/Quake](https://github.com/id-Software/Quake) | C | Quake engine source (a textbook of the 3D pipeline) |
| [diasurgical/devilutionX](https://github.com/diasurgical/devilutionX) | C++ | A Diablo port; bringing an old game up to date |

## 5. GitHub Picks: Learning & List Repos

| Repo | Why it's worth starring |
| --- | --- |
| [munificent/game-programming-patterns](https://github.com/munificent/game-programming-patterns) | Full source for Game Programming Patterns |
| [JoeyDeVries/LearnOpenGL](https://github.com/JoeyDeVries/LearnOpenGL) | Companion code for LearnOpenGL |
| [patriciogonzalezvivo/thebookofshaders](https://github.com/patriciogonzalezvivo/thebookofshaders) | Source for The Book of Shaders |
| [ssloy/tinyrenderer](https://github.com/ssloy/tinyrenderer) | A software renderer in 500 lines: a graphics pipeline crash course |
| [lettier/3d-game-shaders-for-beginners](https://github.com/lettier/3d-game-shaders-for-beginners) | A step-by-step game shader tutorial |
| [RayTracing/raytracing.github.io](https://github.com/RayTracing/raytracing.github.io) | The Ray Tracing in One Weekend series |
| [OneLoneCoder/olcPixelGameEngine](https://github.com/OneLoneCoder/olcPixelGameEngine) | A single-file engine plus hundreds of video episodes |
| [godotengine/godot-demo-projects](https://github.com/godotengine/godot-demo-projects) | Godot's official demo project library |
| [UnityTechnologies/open-project-1](https://github.com/UnityTechnologies/open-project-1) | An official open-source Unity project (archived; a complete case study) |
| [ellisonleao/magictools](https://github.com/ellisonleao/magictools) | A directory of classic game development tools (this repo cross-links to it) |
| [dawdle-deer/awesome-learn-gamedev](https://github.com/dawdle-deer/awesome-learn-gamedev) | A mega-list of learning resources |
| [FronkonGames/Awesome-Gamedev](https://github.com/FronkonGames/Awesome-Gamedev) | A categorized resource list |
| [utilForever/game-developer-roadmap](https://github.com/utilForever/game-developer-roadmap) | A learning roadmap for game developers |
| [miloyip/game-programmer](https://github.com/miloyip/game-programmer) | The game programmer's learning path (Chinese-friendly) |
| [0xFA11/MultiplayerNetworkingResources](https://github.com/0xFA11/MultiplayerNetworkingResources) | A comprehensive list of network programming resources |
| [Trilarion/opensourcegames](https://github.com/Trilarion/opensourcegames) | A master catalog of open-source games |
| [mattdesl/graphics-resources](https://github.com/mattdesl/graphics-resources) | A graphics programming resource list |

## 6. GitHub Picks: AI & Generative Tools

| Repo | Why it's worth a look |
| --- | --- |
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Node-based generative workflows; central to game asset pipelines |
| [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | The starting point of the Stable Diffusion ecosystem |
| [ollama/ollama](https://github.com/ollama/ollama) | Local LLMs, running with a single command |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | A local inference engine |
| [facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft) | MusicGen / AudioGen audio generation |

---

## 7. Book Recommendations: Game Design

| Title | Author | Notes | Why read it |
| --- | --- | --- | --- |
| The Art of Game Design | Jesse Schell | Chinese translation available | A lens-based toolbox; the first choice for getting into design and for self-review |
| A Theory of Fun for Game Design | Raph Koster | Chinese translation available | The essential argument that "games are learning"; slim but deep |
| Game Design Workshop | Tracy Fullerton | Chinese translation available | An exercise-driven textbook, good for systematic study |
| Level Up! | Scott Rogers | Chinese translation available | A humorous, practical guide to the full design process |
| Rules of Play | Salen & Zimmerman | English | The academic cornerstone of design theory (thick) |
| Game Feel | Steve Swink | English | The only dedicated book on game feel |
| Game Mechanics: Advanced Game Design | Adams & Dormans | Chinese translation available | Systems and mechanics modeling (the Machinations methodology) |
| The Gamer's Brain | Celia Hodent | English | UX and cognitive science; experience design before launch |
| Procedural Generation in Game Design | edited by Short & Adams | English | A collection on procedural generation design |
| Characteristics of Games | Elias, Garfield, Gutschera | English | A foundational analysis of multiplayer, competition and balance |
| Reality Is Broken | Jane McGonigal | Chinese translation available | The value of games and a big-picture design perspective |

## 8. Book Recommendations: Programming, Architecture & Math

| Title | Author | Notes | Why read it |
| --- | --- | --- | --- |
| Game Programming Patterns | Robert Nystrom | Chinese translation available; free online | Design patterns in a game context; the whole book is free online |
| Game Engine Architecture | Jason Gregory | Chinese translation available | The panoramic engine authority; works as a reference book |
| Game Coding Complete | Mike McShaffry | English | Engineering practice and project management |
| Foundations of Game Engine Development | Eric Lengyel | English | A series on engine math and low-level rendering |
| 3D Math Primer for Graphics and Game Development | Dunn & Parberry | Free online | Graphics and game math (companion site: gamemath.com) |
| Mathematics for 3D Game Programming and Computer Graphics | Eric Lengyel | English | Advanced math (pairs with the engine books) |
| Essential Mathematics for Games and Interactive Applications | Van Verth & Bishop | English | A systematic textbook on game math |
| Effective Modern C++ | Scott Meyers | Chinese translation available | Modern C++ (aimed at engines and tools) |
| C# in Depth | Jon Skeet | Chinese translation available | A deeper understanding of C# (for Unity work) |
| Programming Game AI by Example | Mat Buckland | English | The classic hands-on book on game AI |
| AI for Games | Ian Millington | English | An AI systems textbook (broad coverage) |
| Multiplayer Game Programming | Glazer & Madhav | English | A textbook on network synchronization and architecture |
| Physics for Game Developers | David Bourg | English | An introduction to physics programming |

## 9. Book Recommendations: Graphics, Rendering & Shaders

| Title | Author | Notes | Why read it |
| --- | --- | --- | --- |
| Real-Time Rendering (4th) | Akenine-Möller et al. | English | The real-time rendering bible (companion site: realtimerendering.com) |
| Physically Based Rendering (PBRT) | Pharr, Jakob, Humphreys | Free online | The offline rendering authority, with complete companion code |
| Ray Tracing in One Weekend series | Peter Shirley et al. | Free online | A hands-on introduction to ray tracing in three parts |
| The Book of Shaders | Gonzalez-Vivo & Lowe | Free online | An interactive introduction to shaders |
| LearnOpenGL | Joey de Vries | Free online | The complete modern OpenGL pipeline |
| Unity Shader Essentials | Feng Lele | Chinese | A shader classic in Chinese-language circles |
| GPU Gems 1–3 | edited by Nvidia | Free online | A graphics techniques collection (a classic worth rereading) |
| GPU Pro series | edited by Wolfgang Engel | English | An advanced graphics collection |
| Real-Time Shadows | Eisemann et al. | English | A book devoted to shadow techniques |
| Computer Graphics: Principles and Practice | Hughes et al. | English | The encyclopedia of computer graphics |

## 10. Book Recommendations: Art & Audio

| Title | Author | Notes | Why read it |
| --- | --- | --- | --- |
| Color and Light | James Gurney | English | The bible of color and light, from a painter's perspective |
| Framed Ink | Marcos Mateu-Mestre | English | Composition and storyboarding (visual storytelling) |
| The Animator's Survival Kit | Richard Williams | Chinese translation available | The bible of animation principles |
| How to Draw | Scott Robertson | English | Perspective and industrial design drawing |
| Art Fundamentals | 3DTotal | English | A comprehensive grounding in art basics (color / light / composition) |
| Pixel Art for Game Developers | Daniel Silber | English | An introduction to pixel art |
| The Complete Guide to Game Audio | Aaron Marks | English | The full game audio pipeline |
| Game Audio Implementation | Richard Stevens | English | Hands-on audio implementation inside engines |
| The Sound Effects Bible | Ric Viers | English | A methodology for creating sound effects |
| Mastering Audio | Bob Katz | English | The standard on mixing and mastering |
| This Is Your Brain on Music | Daniel Levitin | Chinese translation available | Music cognition (why music moves us) |

## 11. Book Recommendations: Production, Business & Industry Accounts

| Title | Author | Notes | Why read it |
| --- | --- | --- | --- |
| A Playful Production Process | Richard Lemarchand | English | The full production process from idea to launch (a production bible) |
| Blood, Sweat, and Pixels | Jason Schreier | Chinese translation available | A record of AAA development; a collection of project-management cautionary tales |
| Press Reset | Jason Schreier | English | A sequel on studios rising and falling, and the fates of the people in them |
| Masters of Doom | David Kushner | Chinese translation available (titled DOOM Qishilu) | The id Software legend; a dual history of technology and business |
| Console Wars | Blake Harris | English | An account of the Sega vs. Nintendo console war |
| Spelunky | Derek Yu | English (Boss Fight Books) | An indie developer's design diary |
| The Making of Prince of Persia | Jordan Mechner | English | A 1980s development diary (of archaeological value) |
| Significant Zero | Walt Williams | English | A AAA narrative designer's memoir |
| How To Market A Game series | Chris Zukowski | Blog / e-books | A practical knowledge base for Steam marketing (not a traditional book; highly recommended) |

## 12. Free Online Books & Resource Sites (Roundup)

| Name | Link | Contents |
| --- | --- | --- |
| Game Programming Patterns | https://gameprogrammingpatterns.com/ | Design patterns (free online) |
| The Book of Shaders | https://thebookofshaders.com/ | A shader primer |
| LearnOpenGL | https://learnopengl.com/ | Modern OpenGL |
| 3D Math Primer | https://gamemath.com/ | The online edition of the graphics math book |
| Ray Tracing in One Weekend | https://raytracing.github.io/ | The ray tracing trilogy |
| PBRT (4th edition, online) | https://pbr-book.org/ | The offline rendering authority |
| Game AI Pro (chapters free) | http://www.gameaipro.com/ | A game AI collection |
| GPU Gems | https://developer.nvidia.com/gpugems | A graphics techniques collection |
| The Nature of Code | https://natureofcode.com/ | Systems, physics and generative art, all through code |

## 13. How to Use This List

1. **How to choose books**: for each area, take "one main textbook + one reference manual" — for example: design = The Art of Game Design + Game Feel; graphics = Real-Time Rendering + GPU Gems.
2. **Free first**: the list in §12 is more than a year of reading on its own; start free, then print, and read online before you buy.
3. **Pair books with repos**: back each theoretical point with source code from a repo in §1–§6 and the payoff doubles (e.g. ECS theory → the flecs source).
4. **Build your own reading list**: maintain your own version in `resources/books.md` (inside this repo), tracking "read or not / worth it or not". This list is a seed, not the finish line.
