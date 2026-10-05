# Ludo Atlas · Engine Internals Path

> How to read engine source code: methodology, three routes (Godot / Bevy / small-engine starter), a reading list, and weekly plans.
> Companions: Programming Handbook · Open Source Picks & Book Recommendations · AI Workflows Handbook (having AI read the source code with you).
> Who it's for: developers who have written one or two games and want to move toward engine / tools / technical art / graphics roles.

---

## 1. Why Read Source Code

- **Breaking the illusion**: engines are not magic. Once you can read them, "black-magic bugs" become "I know roughly which layer it lives in."
- **Learning industrial practice**: the architecture, memory management, toolchains and automated testing of large C++/Rust projects are not things you can learn from books.
- **Pinpointing**: the answers you can't find in the docs are in the source. People who read source code debug on another level.
- **Career payoff**: for engine, tools, graphics and TA roles, one "I've actually read the engine" project in your portfolio beats ten lines of "familiar with the engine."

## 2. Five Rules of Methodology

1. **Read with a question**: don't start reciting from the first line. Pick a concrete question ("from pressing a button to a picture appearing on screen, what happens in between?"), then chase it.
2. **Follow the call chain**: trace from user-visible behavior down to the core implementation. Fully digesting one chain beats skimming ten modules.
3. **Build it, then change it**: get a working build first, then set breakpoints, add logs, and change code to see what happens. Building an engine from source is itself a milestone.
4. **Draw diagrams, take notes**: draw your own module diagrams and sequence diagrams. Wherever you can't draw it is wherever you don't understand it.
5. **Guess, then verify**: before reading, guess the implementation ("how would I write this if I were the author?"), then go check. Far more memorable than passive reading.

## 3. Route A: Godot (recommended first stop, modern C++ practice)

Repository: https://github.com/godotengine/godot

Rough structure (walk the top-level directories once before reading):

| Directory | Contents | Reading value |
| --- | --- | --- |
| `main/` | Entry point and main loop | The starting point; look at main.cpp first |
| `core/` | Base types, math, memory, containers | Learn how C++ infrastructure is built |
| `scene/` | Nodes, the scene system, 2D/3D nodes | The core of the engine's object model |
| `servers/` | Service layers for rendering, physics, audio | How abstraction layers are designed |
| `drivers/` | Low-level graphics and audio drivers | Vulkan/GL practice in the field |
| `modules/` | Optional modules (language bindings, etc.) | The modular plug-in mechanism |
| `platform/` | Per-platform release layers | How cross-platform engineering is done |

Six-stage reading plan (2-3 hours a week, about 8 weeks):

1. Build from source (the build chapter in the official docs, the scons flow), run it, and learn to change a line of code and recompile.
2. `main/main.cpp`: startup flow, main loop, frame scheduling.
3. `core/object/`: Object, RefCounted, the class registration system (ClassDB) — understand the foundation of "everything is an object."
4. `scene/`: SceneTree and node lifecycle, the signal mechanism.
5. `servers/rendering/`: the rendering server and the RID resource-handle system — understand "why the rendering layer needed abstraction."
6. Pick one point that interests you and go deep (physics, navigation, GDExtension bindings), then write an explainer article.

## 4. Route B: Bevy (Rust, an ECS architecture course)

Repository: https://github.com/bevyengine/bevy

- **Start from the examples**: the `examples/` directory is the best official teaching material; run a few before entering the source.
- **A crate is a module**: `bevy_app` (application framework) → `bevy_ecs` (entity-component system) → `bevy_render` (rendering) → `bevy_asset` (assets) → `bevy_pbr`/`bevy_sprite`/`bevy_ui` (feature layers). Rust's workspace structure makes module boundaries obvious at a glance — this is where it reads more easily than C++ engines.
- **Main line 1**: how an App is built (the plugin system); how systems get scheduled (the schedule).
- **Main line 2**: the implementation of ECS queries and change detection.
- **Main line 3**: how the render graph organizes a frame.
- Mental preparation: compile times are long — read in snapshots with cargo check; read doc comments before implementations.
- Pacing reference: 6-8 weeks.

## 5. Route C: Small-Engine Crash Course (read a small one cover to cover first)

If you want the "cover-to-cover" experience first, pick one whose code volume is manageable:

- **raylib** (https://github.com/raysan5/raylib ): C, with an extremely clear structure (rcore main loop, rshapes primitives, rtextures textures, rmodels models, rtext text, raudio audio). Good for your first "read a whole engine cover to cover."
- **Quake 1** (https://github.com/id-Software/Quake ): a living-fossil textbook of the 3D FPS, in C, with plenty of community guides and videos. Focus on the separation of engine and game logic (QuakeC), the networking layer, and the rendering pipeline. Reading alongside a guide doubles your efficiency.

Goal: within 8 weeks, complete full-chain notes on "from entry point to drawing one frame," plus an architecture diagram you drew yourself.

## 6. General Toolbox

- **Debugger**: conditional breakpoints, call stacks, memory inspection. When reading source, code is the documentation and the debugger is the microscope.
- **Build first**: get the project compiling before reading code. Reading source with a broken build halves your efficiency.
- **Notes repo**: record each stage in your own notes repo (structure diagrams, confusions, answers) — this is future interview material.
- **The right way to use AI assistance** (see the AI Workflows Handbook): have coding agents explain code, draw flowcharts, and pose comprehension questions; but their answers must be verified against the source — models will fabricate call relationships with a straight face. Recommended game: have the AI quiz you, you answer, it grades.
- **Performance tools**: learn the profiler while reading rendering code; the two reinforce each other.

## 7. Reading List (pick one main line, don't be greedy)

| Goal | Recommended route | Milestone |
| --- | --- | --- |
| Build a solid C++ engine foundation | Godot six stages | Write an explainer on "startup to first frame" |
| Understand ECS and modern architecture | Bevy | Write an explainer on "system scheduling" |
| Read one engine cover to cover | raylib | Read the whole repo through + an architecture diagram |
| Understand FPS and networking | Quake 1 | Write an explainer on "movement and network sync" |

## 8. Common Pitfalls

1. Wandering without a goal — looking everywhere, understanding nowhere.
2. Chasing a "full read" and losing confidence in front of millions of lines of code.
3. Reading without running, never changing anything by hand.
4. No notes; forgotten the moment you finish.
5. Opening several engines at once and crossing the wires.
6. Getting stuck on details and abandoning the main line (know "what" first, then study "why").
7. Ignoring the build step; giving up when stuck at environment setup.
8. Trusting AI explanations completely, never verifying against the source.
9. No output (explainer articles / diagrams); the learning process never gets a wrap-up.
10. Expecting a crash course: this route is measured in months, and the payoff in years.

## 9. Suggested Output

After finishing a route, leave behind at least one piece of work: an explainer article, an architecture diagram, or a small change based on your understanding of the source (a merged PR is even better). Learning outcomes must be visible — that is what separates this from "casually flipping through."
