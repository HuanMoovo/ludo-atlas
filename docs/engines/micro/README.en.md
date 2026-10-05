# Ludo Atlas · Engine Tracks · Lightweight Frameworks

> **Engine Tracks**. Positioning: a route with no editor as a safety net — you organize the main loop, assets and tooling yourself, trading that effort for full control and a tech stack you can read end to end.
> Companions: Programming Handbook · Production Handbook · Indie Survival.

---

## 1. Positioning and Choice

"Code-first" is a concrete technical route: there is no scene editor, or only a minimal one. The programmer faces the main loop directly — input, update and draw are organized frame by frame; assets, levels and tooling are organized through code and data files. Nothing falls back to "drag it into the scene and it runs": every job an engine would do for you comes back to you as "build it yourself."

When to pick it:

1. **Learning the fundamentals**: if you want to know what happens inside the engine black box each frame, implementing it by hand is the shortest path. It complements the Engine Internals Path — one reads other people's code, the other has you write your own.
2. **Small finished games**: focused-mechanics 2D games, experiences from a few to a dozen-plus hours, where the framework's small footprint translates directly into delivery speed.
3. **Prototypes and experiments**: fast startup, no editor overhead — good for validating gameplay hypotheses and doing game jams.
4. **Tools and non-game programs**: parameter panels, map viewers, graphics demos, teaching examples — programs that "do not look like games" are actually lighter with a framework.

When this route does not fit: content-heavy projects, teams where artists and designers need to edit content directly, productions that depend on a visual level pipeline, and heavy 3D projects. If you tick two or more, go back to the Engine Selection Guide and re-evaluate — do not force a framework to carry it.

The trade-offs between the two routes:

| Dimension | Engine route | Lightweight framework route |
| --- | --- | --- |
| Editor | Scene and prefab editors | None or minimal; code is the project |
| Systems provided | Built into the engine | You assemble them; pull in libraries as needed |
| Iteration | Play-test inside the editor | Running is play-testing; hot reload is yours to build |
| What you learn | How to use the engine | How things work, plus the language |
| Customization ceiling | Bounded by the engine's extension model | No ceiling; engineering effort is the only cost |
| Collaboration | Designers and artists edit content directly | Content lives in data files; tools are yours to write |
| Cost profile | Fast early; later you wrestle the engine | Slow early; fully your own from then on |

One-line positioning for five frameworks:

| Framework | Language | In one line | Common pick for |
| --- | --- | --- | --- |
| raylib | C (bindings for many languages) | The light C-family route: minimal API, no external dependencies at the core, quick to start | Learners who read source as they go; C-family small projects and tools |
| LÖVE | Lua | A Lua 2D framework: the directory is the project, and the feedback loop is short | Fast iteration with a scripting language; small 2D and game jams |
| Pygame | Python | The classic Python 2D starter: a huge tutorial and example ecosystem | Python learners, teaching demos, 2D where logic matters more than engine features |
| SDL | C | Low-level multimedia abstraction: the minimal set of window, input, audio and rendering | Projects that want full control and are willing to build from the bottom up |
| SFML | C++ | An object-oriented C++ mid-layer: clean modules, mostly 2D | People who want C++ without touching system APIs directly |

Selection depends on three variables only: the language you are willing to write long-term (this matters more than performance differences); how much you enjoy building systems from scratch (SDL and SFML are the lowest level, while raylib, LÖVE and Pygame produce results faster); and target scope (once you outgrow small, any framework becomes running with weights on). Of the three, let language and scope decide.

A self-check question: once the editor is taken away, whose workflow besides yours breaks? The more people who break, the less this route suits you.

## 2. Ecosystem and Project Structure

A framework is not a shrunken engine — the project shape differs a lot from engine projects: there is no editor-generated skeleton, so structure is yours to define, and the build approach depends on the language.

| Framework | Project shape | Build and dependencies |
| --- | --- | --- |
| raylib | Linked into the project as a library; code structure is free | Build system of your choice; the core has no external dependencies |
| LÖVE | Convention over configuration: an entry file plus a config file; the directory is the project | Hand the directory to the runtime; modules go in the project directory |
| Pygame | A Python package plus a virtual environment | Dependency manifest; the entry script is the program |
| SDL | A system-level library: headers plus link libraries | Managed by the build system; link per platform |
| SFML | Like SDL, linked module by module | Like SDL; static or dynamic linking, pick one |

With no editor, the directory structure is the project structure. Fix conventions from the start and write them into the project docs:

- `src/`: all game code, split by system (main loop, input, rendering, world, UI) — avoid one file that keeps swelling.
- `assets/`: art and audio, keeping source files separate from runtime formats; naming rules enforced from day one.
- `tools/`: your own editors and conversion scripts (§3.2); tool outputs go into version control too.
- `scripts/`: build, packaging and release scripts, so "one command to run it" is the baseline for collaboration.

Think dependency management through per language: with C and C++, either bring everything with you, or once you choose a build system and dependency approach, stop churning; Lua modules are simplest dropped straight into the project directory; Python demands a virtual environment and a dependency manifest, or unreproducible environments are only a matter of time.

Rules of thumb on ecosystem size: SDL sits at the bottom, and almost every layer above it has ready-made options; raylib has rich official examples and a strong template community, with a mature read-the-source path; LÖVE's module ecosystem is community-organized — quality varies and you must filter it yourself; Pygame has the most tutorials, but the main project moves slowly and community forks are more active (entry points in Resources).

One discipline: the framework route has no editor recording project knowledge for you — any convention (naming, directories, build commands, asset formats) that is not written into docs does not exist.

## 3. Core Workflows

### 3.1 Owning the main loop

What these frameworks share: they hand you "one frame." The typical structure is a single chain of responsibilities:

`collect events and input → update logic (fixed or variable step) → draw → frame pacing and wait for the next frame`

In an engine this sentence is hidden; here it is your daily routine. Two disciplines:

- Update logic on a fixed step and decouple rendering from it, or game feel and physics drift with machine performance (reasoning in the Programming Handbook §2.9).
- Build three debug facilities from day one: a frame timer display, a state overlay panel, and runtime output of key parameters. Tuning must not require editing code and restarting.

The iteration loop is this route's biggest asset: change code, run, observe, change again. Compress that loop to seconds and you outpace most engine projects; treat startup and run time as first-priority engineering metrics to push down.

### 3.2 Building your own tools: the hidden workload

Every editor an engine project gets for free is a to-do item on the framework route. List them separately when estimating:

| Tool | If you skip it | Common approach |
| --- | --- | --- |
| Level editor | Levels live in code; moving one wall means editing code | A runtime debug mode that places objects and exports data; or a small standalone tool reading and writing the same format |
| Tuning panel | Every value needs a code edit and a restart | A runtime overlay panel that reads and writes a config file |
| Data tables and conversion scripts | Values scatter across the codebase | Tables or text formats plus conversion scripts, generated at build time |
| Asset packaging tools | Directories maintained by hand; package size out of control | Scripted atlas packing, audio conversion and naming checks |

Rule of thumb: tool cost is counted in hours; hand-maintained content cost is counted in hours multiplied by iterations. Level editing and tuning panels pay off the earlier you build them; past ten levels or a few dozen values, content iteration without tools will drag the schedule down.

### 3.3 Asset pipeline

With no asset importer, your code is the importer. The pipeline is usually: DCC export (agreed formats and sizes) → naming and directory conventions → conversion scripts (atlases, compression, audio formats) → in-game loading code. Two disciplines: keep source files and runtime files in separate directories; script every manual step, or "it won't come out on another machine" will happen again and again.

### 3.4 Packaging and distribution

Distribution is the most underrated stretch of this route, and the difficulty differs by language:

| Route | Main difficulty | Response |
| --- | --- | --- |
| C and C++ (raylib, SDL, SFML) | Each platform builds separately; dynamic libraries add runtime dependencies | Use a build matrix to produce per-platform versions; prefer static linking to cut dependencies |
| Lua (LÖVE) | Players need the runtime unless you fuse project and runtime | Fuse into a single executable; produce it per platform |
| Python (Pygame) | Large packaged artifacts; occasional antivirus false positives | Use a packaging tool to build the executable; handle signing and false-positive appeals for real releases |
| Common | Store requirements, update mechanisms and crash collection are all yours to wire up | Schedule backwards from release and give it an engine-grade budget |

## 4. Idioms for Key Systems

Frameworks do not define your architecture, but every "standard system" an engine offers has a counterpart here — you just implement all of them:

| Engine concept | Framework counterpart |
| --- | --- |
| Scenes and scene switching | Write your own state stack: enter, exit and pause each clean up their resources |
| Prefabs and entities | Data tables plus constructors; entity fields driven by data files |
| Visual editor | Runtime debug mode plus small self-built tools (§3.2) |
| Asset importer | Convention directories plus loader code, with a single loading entry point |
| Events and signals | Callback registries or a message queue; limit propagation depth to prevent chains |
| Save system | A custom format with version numbers and migration functions; store state, never object references |
| Camera | Implement follow, dead zone, look-ahead and screen shake yourself (key points in the Programming Handbook §2.3) |
| Object pool | Pool everything created and destroyed at high frequency; the more managed the language, the earlier you should do it |

Some idioms: keep game state in one top-level object and split files by system — no scattered globals; route input through an action-mapping layer distinguishing pressed, held and released, with input buffering; keep a single loading entry point for assets to leave room for hot reload; UI has no built-in — build in-game UI and debug UI separately, or adopt a mature third-party UI library; call the framework directly for audio, but manage channels, concurrency limits and streaming playback yourself.

For every system you finish, leave a switch: a runtime toggle that shows its visual state on its own. It is both a debug tool and the foundation for future editor UI and self-built tools.

## 5. Performance and Optimization

Performance boundaries are set by the language — know your lane first:

| Route | Performance class | Scope intuition |
| --- | --- | --- |
| C and C++ (raylib, SDL, SFML) | Native speed, the most headroom | Thousands of on-screen objects and complex 2D are no strain |
| Lua (LÖVE) | Slower at the script layer; hot spots can drop to native | Conventional 2D; hundreds of active objects are comfortable |
| Python (Pygame) | Clearly a class slower; keep per-object updates restrained | Small 2D, tools and teaching demos; keep entity counts low |

The classes only answer "can this route carry my idea"; real numbers count only when measured on your game and target machines.

Common optimization points:

- Drawing: fewer draw calls and texture switches — atlases and batching; text rendering is expensive, cache rendered results and do not re-layout every frame.
- Update: managed languages avoid per-frame allocations; pool and pre-warm high-frequency objects; hoist lookups out of per-entity loops to load time.
- Structure: decouple logic and rendering; cap catch-up steps per frame when logic backs up, so a stutter does not pile up.
- Dropping down: only after a hot spot is confirmed, consider native code, third-party libraries or parallelism; measure first, replace second.

Measurement discipline per the Programming Handbook §3: no optimization without measurement; confirm which layer the hot spot is in (rendering, update or asset loading); trust real-device data, and keep records before and after.

## 6. Learning Path

Follow it in order; every stage has observable output:

1. **The language** (weeks): get comfortable writing the target language — file I/O, data structures, error handling, the debugger. Frameworks cannot save someone who does not know the language.
2. **Run every official example** (days): frameworks ship example collections; run through the list, tweak a parameter or two in each to see the response, and build a feel for the boundary of "what the framework owns vs. what you own."
3. **Recreate a small-game trio** (weeks): Pong, Breakout, and a scrolling platformer. Each adds a system over the last: input buffering, collision and state machines, cameras and level data files.
4. **Hand-write a minimal kit** (weeks): a fixed-step main loop, a state stack, saves, and a runtime tuning panel — implement them all once. After this step, any engine architecture diagram stops being a mystery.
5. **Finish and ship a small game** (one to three months): including a self-built tool, packaging scripts and one real distribution. The pitfalls of shipping disappear only after you walk the whole path once.

Acceptance criteria (all observable):

- Without a tutorial, you can go from an empty project to "it draws, it takes input, it switches states."
- You can explain the execution order within one frame, and when it stutters, locate which layer is the bottleneck.
- Your recreation-stage games contain at least one mechanic you added yourself, with a rationale for the implementation choice.
- The packaged build runs on someone else's clean machine, with no on-site coaching from you to install or start it.

## 7. Common Pitfalls

1. **Scope creep**: you picked a framework for "something a bit bigger," and as content grows, every missing editor and tool shows up; the framework route suits small scope — when scope grows, face the route change.
2. **Tool debt**: remembering level editors and tuning panels only at mass-production time, when content iteration is already collapsing (§3.2).
3. **Reinventing wheels**: hand-rolling UI, audio and physics from zero, burning schedule on engineering unrelated to gameplay; the opposite extreme is outsourcing everything while the core loop stays unclear.
4. **Runaway manual asset management**: load without release, release while still in use, asset paths scattered as magic strings; solve it with one loading entry point plus reference management.
5. **Underestimating distribution**: packaging, signing, store materials and update mechanisms are all real engineering; starting two weeks before release guarantees delays.
6. **Misjudging performance**: the wrong language at the wrong scope (Python straining under an entity swarm); or the opposite — early complex optimization on a tiny project.
7. **Iteration speed unfulfilled**: no hot reload, no runtime tuning, still editing code and restarting to change a value — this route's biggest advantage wasted.
8. **Unreproducible environments**: C++ build matrices and Python dependency differences yield "it runs on my machine"; script the environment and build, and containerize where possible.
9. **Adaptation postponed**: gamepads, resolutions, system fonts, save paths — handled only at the end of testing, with a large rework bill.
10. **Copying without understanding**: every number in tutorials and example code should be explainable; the whole benefit of the framework route is that every line can be understood — do not use it as a black box.

## Further Reading

- [Engine Tracks overview](../README.md): the list and plan for all 12 tracks — this page is the "lightweight frameworks" one.
- [Engine Internals Path](../../fundamentals/engine-internals/README.md): reading raylib through is a great first full source-reading exercise; complementary to this page.
- [Programming Handbook](../../fundamentals/programming/README.md): the general version of core-system checklists, performance methodology and engineering infrastructure.
- [Engine Selection Guide](../../start/engine-choice.md): confirm the lightweight framework route is yours before coming back to this page.
- [Pitfalls & Anti-patterns](../../pitfalls/README.md): read against section 7 here.
- [Resources](../../../resources/README.md): official entry points and tutorial indexes for each framework.
