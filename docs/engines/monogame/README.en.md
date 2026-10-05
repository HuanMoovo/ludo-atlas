# Ludo Atlas · Engine Tracks · MonoGame / FNA

> **Engine Tracks**. Positioning: a code-first C# framework line descended from XNA — MonoGame carries it forward into the modern day, FNA reproduces it faithfully; the main loop, architecture and toolchain are all yours to organize.
> Companions: Programming Handbook · Game Design Handbook · Indie Survival · Engine Internals Path.

---

## 1. Positioning and Choice

MonoGame and FNA are two open-source continuations of Microsoft's discontinued XNA framework, sharing one worldview: C# code-first, no scene editor — you get a window, a main loop, and a set of drawing, input and audio interfaces; everything else you organize yourself. Plenty of commercial work has been built with this plain toolchain — Stardew Valley and Celeste among them — and it can carry a full project, provided you accept its worldview.

The two differ in "attitude toward the original":

| Dimension | MonoGame | FNA |
| --- | --- | --- |
| Positioning | An XNA-style modern framework; interfaces and behavior allowed to evolve step by step | A faithful reproduction targeting complete compatibility with the original; fidelity first |
| Who it is for | New projects; people who want the modern .NET toolchain | Porting existing XNA projects; people who need frame-for-frame identical behavior |
| Content pipeline | Ships MGCB; assets compiled as part of the build | No content pipeline; the official stance encourages building your own light conversion tools |
| Project shape | One project per target platform | One project covers every platform it supports |
| Ecosystem | Community libraries mostly target it | Plainer; most tooling is yours to wire up |
| Platforms | Desktop, mobile, consoles (consoles via registered-developer channels) | Mainly desktop and consoles; mobile via community forks |

Selection rule: new projects default to MonoGame; if you hold a working old XNA codebase that needs a fidelity port, go FNA; do not mix the two in one project, and do not expect a painless migration between them.

### 1.1 Who it fits

- C# programmers: the language is your working language, and the whole .NET ecosystem (dependency management, testing, CI) applies — the skills you invest are the same ones your career uses.
- Learner-oriented developers: what happens each frame is fully transparent, making it direct material for understanding what an engine does for you; complements the Engine Internals Path.
- Porters: existing XNA projects moving to modern platforms — FNA minimizes the migration.
- Authors who want control: render order, memory, threads and platform integration all stay in your hands; no engine black box to wrestle.
- Small, focused-mechanics 2D games: tooling gaps have a limited blast radius, and code-first buys extremely fast iteration.

### 1.2 Who it does not fit

- Projects with heavy content where designers and artists need to build levels in an editor: no visual scene tooling, and no one else will fill that workflow gap.
- Projects that depend on off-the-shelf systems: navigation, animation state machines, UI kits — mostly write your own or assemble one by one.
- Teams aiming for consoles at launch without a publisher or porting resources: console platforms carry qualification thresholds and confidentiality requirements — budget them through registered-developer channels.
- People who want things to work out of the box: window dragging, resolution strategy, save paths — none of it exists by default.

### 1.3 Against Unity and Godot (C#)

| Dimension | MonoGame / FNA | Unity | Godot C# |
| --- | --- | --- | --- |
| Way of working | Code is the project; no editor | Editor-first; code attaches to objects | Editor-first; nodes plus scripts |
| What you learn | C# and graphics fundamentals; no engine jargon to memorize | The whole Unity system | Godot's node and scene model |
| Off-the-shelf systems | Almost none; build or pull in libraries | The most, with uneven quality | Moderate; a batch built in officially |
| Platform coverage | Desktop and mobile smooth; consoles via developer channels | All platforms, consoles mature | Desktop and mobile good; consoles via third parties |
| Licensing and control | Open source; runtime fully controllable | Commercial engine; terms need tracking | Open source, permissive license |
| Content collaboration | Content in data files; tools are yours to write | Artists and designers work directly | Artists and designers work directly |

In one line: want off-the-shelf systems and content collaboration — choose Unity or Godot; want native C#, full control, and a tech stack you can read through — choose MonoGame or FNA.

## 2. Ecosystem and Project Structure

### 2.1 Toolchain

The workbench is the .NET toolchain itself; the editor provides only completion and debugging:

| Tool | What it handles |
| --- | --- |
| .NET SDK and the dotnet CLI | Templates, dependencies, build, run, publish |
| IDE (Rider, Visual Studio or VS Code) | Coding, debugging, profiling |
| MGCB (content builder) | Compiles raw assets into runtime formats as part of the build |
| Template commands | Generate per-platform project skeletons; desktop, mobile and other targets each have templates |

One discipline: compress the "edit code to see a frame" loop into seconds. Code-first's whole advantage rests on this.

### 2.2 Directories and project shape

A single solution with per-platform launcher projects is the common shape:

```text
game/
├── Game.Core/            # All game code, platform-agnostic
├── Game.Desktop/         # Desktop launcher project, references Core
├── Game.Mobile/          # Mobile launcher project, references Core
├── Content/              # Source assets and content pipeline config
└── tools/                # Self-built editors and conversion scripts
```

- Put all logic in the platform-agnostic Core project; launcher projects keep only the entry point and a bit of adaptation — the most economical way to handle platform differences.
- `Content/` holds both source assets and pipeline configuration; outputs go to separate per-platform directories and stay out of version control.
- Build `tools/` from day one: level editors, tuning panels and conversion scripts are first-class citizens of the project.

Drift from this convention and, a month later, a second copy of the game grows inside the platform branches.

### 2.3 Version control

- Ignore generated output directories (compiled output and content artifacts) — they all rebuild automatically.
- Commit content pipeline configs and asset source files so builds are identical on any machine.
- Large files — images, audio — go through Git LFS, with the rules written early.
- Keep levels and data in text formats where possible so diffs stay readable; binary formats need a separate review approach.

### 2.4 Ecosystem and common libraries

The framework gives only the foundation; the upper layers you assemble. Common needs and established options:

| Need | Common approach |
| --- | --- |
| Tile maps and levels | The Tiled editor with community loaders, or your own format and editor |
| In-game UI | UI libraries such as Gum, or a hand-rolled minimal widget set |
| Font rendering | Community font libraries reading font files directly, or baking through the content pipeline |
| Physics | An off-the-shelf 2D physics library, wired in as needed |
| Debug panel | .NET bindings for Dear ImGui for runtime overlays |
| Extension kits | Community extension libraries (cameras, pixel art, particles) picked as needed |

Library discipline: check recent commits and issue responsiveness first, then license and target framework. The XNA era left a vast pile of old libraries — compiling is not the same as working.

## 3. Core Workflows

### 3.1 From zero to running

1. Environment: install the .NET SDK and an IDE, generate a target-platform project from the template, and get the bundled empty-window example running first.
2. Skeleton: split the template into Core plus launcher projects; write the first game class — a minimal loop of window, clear, exit.
3. Set the rules: wire up version control, write ignore rules and editor configs, and create `tools/` right now.
4. First pixels: draw one sprite, add input and a camera, and complete the minimal loop of "a character stands on a level and moves."
5. Content pipeline: get one minimal pipeline through first (one font or one audio file); for assets that need no conversion, reading raw files directly is less trouble.
6. Ship something: do a desktop release first, script "one command produces the build," and reuse that script for every platform afterwards.

### 3.2 Owning the main loop

The framework hands you the game class; the loop has only two entry points: update and draw. Four disciplines:

- Logic on a fixed step (the default), decoupled from rendering; before changing step strategy, think through the effects on physics and feel.
- Cap single-frame catch-up, or a stutter snowballs into worse stutters.
- Make frame-time distribution visible: build a frame-timer display and a state overlay from day one.
- Define loop behavior clearly for pause, scene switches and focus loss — the three states where bugs take up residence.

### 3.3 No editor, so build your own tools

This is the route's biggest hidden workload; list it separately when estimating:

| Gap | If unfilled | Common approach |
| --- | --- | --- |
| Level editing | Levels live in code; moving one wall means recompiling | A runtime debug mode placing objects and exporting data, or a small standalone tool reading and writing the same format |
| Asset conversion | Manual handling every time assets change; mistakes eventually | Scripted batch conversion wired into the build |
| Tuning panel | Every value needs a code edit and restart | A runtime overlay panel reading and writing config files |
| Data tables | Values scattered through the codebase | Tables or text plus conversion scripts, generated at build time |

Rule of thumb: tool cost counts in hours; hand-maintenance cost counts in hours times iterations. Before levels pass ten or values pass a few dozen, the tools must be in place.

### 3.4 Packaging and distribution

| Target | Key points |
| --- | --- |
| Desktop | Self-contained publish plus installers and store integration; hold the line that players need no preinstalled runtime, and mind runtime-library dependencies for platform-native backends |
| Mobile | Android needs toolchain and signing setup; iOS final signing depends on a Mac environment; package size, memory and input forms all need separate adaptation |
| Consoles | Registered-developer channels; SDKs and docs under NDA; without a channel, plan a third-party porting route early |
| Browser | Not officially supported; community forks such as KNI offer experimental ports — verify maturity yourself |
| Common | Updaters, crash collection and log reporting are all yours to wire up; schedule backwards from the release date and budget at engine-project scale |

Desktop graphics backends each carry trade-offs (different window systems, audio libraries and driver dependencies); before release, run the chosen backend through the full path on target machines.

## 4. Idioms for Key Systems

### 4.1 Architecture: state machine plus services

- No built-in scene system; the mainstream approach is a self-built state stack: main menu, match, pause each a layer, each responsible for its own resource loading and cleanup.
- Pass global services (saves, audio, settings, input mapping) down through one explicit service object — no scattered static classes.
- One class per system, one responsibility, a clear interface; directories split by system.
- State must be serializable and restorable at any moment — the shared foundation of saves and debugging.

### 4.2 Input

- Input is a polling model: read keyboard, mouse, gamepad and touch state actively each frame; maintain pressed, held, released and input buffering yourself.
- Keys and actions must be separated by a mapping layer, so runtime rebinding and device switching do not touch everything at once.
- Handle gamepad dead zones, touch virtual buttons and keyboard focus loss from day one — retrofitting is expensive.

### 4.3 Rendering

- Start 2D with SpriteBatch: keep one texture and one set of state within a batch — atlases are the foundation of batch efficiency.
- Cameras via transform matrices: follow, dead zone, look-ahead and screen shake are all matrix math.
- Decide resolution and pixel-alignment strategy (integer scaling, letterboxing, high-DPI scrolling) up front — do not change it after the art is done.
- Custom shaders compile to different outputs per graphics backend; verify each one before cross-backend release.

### 4.4 Audio and assets

- Short sound effects resident in memory, long music streamed; plan capacity and formats together with platforms.
- Asset lifecycle is the managed-language trap: hand-created resources such as textures must be released by you; pool everything created at high frequency.
- Keep a single asset loading entry (a unified resource manager) to leave room for hot reload, fallback assets and reference counting.
- The FNA route has no content pipeline — reading raw files directly is more natural, or build conversion scripts as needed.

### 4.5 Debug facilities

- The trio — frame timing, state overlay, parameter panel — before the first playable version.
- A runtime console suits tuning gameplay parameters better than breakpoints.
- Build tool UI and game UI separately; do not let debug widgets creep into the player's screen.

## 5. Performance and Optimization

General rule: measure before optimizing, and trust target devices (methodology in the Programming Handbook §3).

### 5.1 CPU and managed memory

- Managed bottlenecks usually sit in two places: per-frame allocations and virtual calls; in hot paths avoid string concatenation, boxing, LINQ and temporary collections.
- Pool and pre-warm high-frequency objects to remove garbage spikes during play.
- Find hot spots with a profiler and keep records before and after; smooth on desktop is not smooth on mobile.

### 5.2 Drawing

- Draw calls and texture switches are the primary metrics: look at atlases, sorting and batching together.
- Every batch break each frame should be explainable; an unexplainable break is performance thrown away.
- Overdraw is especially expensive with large textures and particles; on mobile, squeeze this first.

### 5.3 Content and memory

- Choose texture compression per target platform; unify audio into stream-friendly formats before launch.
- Load large assets on demand with prefetch; avoid pressing everything in at once on scene switches.
- On mobile, consider trimming and ahead-of-time compilation settings, and run the build through the full path on real devices.

## 6. Learning Path

Follow it in order; every step needs a runnable artifact:

1. C# and .NET fundamentals: solidify the language, generics, collections, async and the debugger first — the framework cannot save someone who does not know the language.
2. Official docs and template projects: walk the getting-started tutorials and get four things running — empty window, sprite, sound, gamepad.
3. Reuse XNA-era knowledge: that body of tutorials and books still applies at the interface level; where it diverges from the current implementation, trust what you measure.
4. Three small games: Pong, Breakout, a scrolling platformer — adding a state machine, a camera and level data in turn.
5. Toolchain focus: the content pipeline, the tile-map workflow, a self-built tuning panel — write each once and distill them into your own project template.
6. Ship one small game: walk the full path from build scripts to store page; to go deeper, read the implementation against FNA (path in the Engine Internals Path).

Acceptance criteria (observable): without tutorials, build from an empty project to "input, state switching, levels"; explain the execution order of each frame; the released artifact runs directly on a clean machine.

## 7. Common Pitfalls

1. **Content pipeline black hole**: assets like fonts and shaders stuck in conversion with unreadable build errors. Get one minimal pipeline through first; for the rest, prefer reading raw files directly.
2. **Scattered documentation**: official docs cover the basics; deeper questions live in source, issues and community chats. Reading source is a basic skill on this route.
3. **Fragmented ecosystem**: libraries either long unmaintained or compatible with only one of the two. Check maintenance status and target framework before choosing; do not bet core systems on abandoned libraries.
4. **Scope creep**: without engine guardrails, you want to build every system yourself and half a year later you are still building an engine. Set hard caps on self-built systems in the milestones.
5. **Misconfigured main loop**: variable step used as fixed step, physics and feel drifting with framerate; or uncapped catch-up causing stutter avalanches.
6. **Per-frame allocations**: strings, boxing, closures quietly making garbage in update and draw; framerate eaten by the GC.
7. **Load without release**: high-frequency objects and hand-created textures are the usual leak suspects; manage them through the single entry point from day one.
8. **Platform differences postponed**: resolution, scaling, path case, save directories — handled at the end of testing with a large rework bill.
9. **Wrong lineage**: new projects copying FNA's old ways, or forcing MonoGame into a port that demands frame-identical behavior. Choose per the rules in §1.
10. **Treating the template as the product**: a template is a starting point; platform branches, build scripts and the content flow all get rebuilt for the project.

## Further Reading

- [Engine Tracks overview](../README.md): the list and plan for all 12 tracks — this page is the "MonoGame / FNA" one.
- [Programming Handbook](../../fundamentals/programming/README.md): the general version of core systems, performance methodology and engineering infrastructure; echoes §3 and §4 throughout.
- [Engine Internals Path](../../fundamentals/engine-internals/README.md): reading MonoGame's source through as a first full source-reading exercise.
- [Indie Survival](../../../playbooks/indie-survival/README.md): scope control, scheduling and cash flow; complements the audience positioning of §1.
- [Pitfalls & Anti-patterns](../../pitfalls/README.md): read against section 7 here.
- [Resources](../../../resources/README.md): official entry points, community libraries and tutorial indexes for both lineages.
