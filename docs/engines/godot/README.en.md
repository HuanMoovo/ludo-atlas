# Ludo Atlas · Engine Tracks · Godot

> **Engine Tracks**. Positioning: a fully open-source all-rounder — one node-and-scene system covers 2D and mid-scale 3D, making it one of the default choices for indie developers.
> Companions: Programming Handbook · Multi-platform Launch Playbook · Mini-Game Development · Indie Survival.

---

## 1. Positioning and Choice

Godot is a fully open-source, community-driven game engine under the MIT license: games made with it need not be open-sourced, carry no license fees and no revenue share, with no strings attached for commercial use; use of the engine name and logo follows its trademark guidelines.

Three bedrock strengths on the engineering side:

- The editor is light and starts fast, runs on Windows, macOS and Linux, and one editor covers both 2D and 3D;
- The scripting language GDScript is close to Python — readable means writable — and the official docs and examples are high quality;
- The scene system is built on a node tree: characters, levels, UI, popup menus — all assembled with the same "node plus scene" model.

### Who it fits

- Indie developers and small teams: zero license cost, light projects, one person can carry both logic and content.
- 2D projects: the 2D workflow is a built-in first-class citizen covering both pixel and high-resolution art — one of the default candidates for small-scope 2D.
- Projects that need fast prototyping and frequent iteration: change it in the editor and run, save a script and it takes effect — a short feedback loop.
- People with programming basics who are willing to read docs: GDScript has a low learning cost, and when you are stuck there is source to consult.
- Teams that value open source and control: the engine source is readable and editable, with no commercial terms holding you back.

### Who it does not fit

- Photoreal visuals and large-team industrial pipelines: rendering ceilings and content tooling show a gap against the big commercial engines.
- Projects depending heavily on commercial plugins and middleware: official and third-party SDK coverage is smaller than mainstream commercial engines — check item by item before choosing.
- People who do not want to write any code: there is no established visual-scripting mainline; scripting is unavoidable.
- Commercial projects centered on console launch: mainstream consoles have no official export template and require third-party porting — cost and schedule are a separate calculation.
- Projects that need mature commercial support contracts: the support ecosystem is growing, and coverage remains a weak spot.

## 2. Ecosystem and Project Structure

A Godot project is just a directory: a single `project.godot` at the root marks its identity, and everything else is yours to define. No enforced structure means you must set your own conventions, or a mid-sized project quickly grows into a junk room.

### 2.1 Directories and naming

Split folders by function, not one big directory each for scenes, scripts and assets. A skeleton that survives scale:

| Location | What goes here |
| --- | --- |
| Feature directories (e.g. `player/`, `ui/`) | Scenes, scripts and their dedicated resources, kept together |
| `assets/` | Globally shared source assets: textures, audio, fonts, models |
| `resources/` | Custom data resources (values, configs, definitions) |
| `addons/` | Third-party and in-house plugins |
| Project root | Project config and export presets — no content |

Name everything in lowercase with underscores, avoiding spaces; all-lowercase sidesteps the Git weirdness of cross-system case sensitivity. Rename and move through the editor where possible so references update along.

### 2.2 Asset organization

- Scenes (`.tscn`) and resources (`.tres`) save as text formats — readable diffs, made for version control from the start.
- External assets keep their original formats inside the project tree; import parameters live in configs beside the source files, and import products in a cache directory that rebuilds at any time.
- Large files (textures, audio, models) go through Git LFS, with rules and ignore configs written early in the project.

### 2.3 Plugin ecosystem

- Official asset library: search and install from inside the editor; plugins land in `addons/` and are enabled per project.
- Common categories: testing (GUT, gdUnit4), dialogue and narrative (such as Dialogic), state machines, terrain, character controllers, UI themes.
- Plugin discipline: check maintenance status and license before installing; before upgrading the engine, verify plugin compatibility on a branch first.
- The engine itself is open source with rich official example projects; for a source-reading route, see the Engine Internals Path.

## 3. Core Workflows

From an empty folder to a first shippable build, the mainline runs as follows; each step carries the caution you will pay for ignoring.

### 3.1 From zero to running

1. Create the project: new from the project manager; settle the renderer tier first. If Web or low-end mobile is among the targets, pick the Compatibility tier; keep the project on a short English path, away from cloud-sync folders.
2. Lay the skeleton: stand up three scenes first — the main scene (entry point), the player, the UI; everything afterwards grows from these three.
3. Write scripts, run it: scripts attach to nodes and run right inside the editor; read errors in the built-in debugger, and use remote debugging to chase real-device problems.
4. Wire up version control: generate the version-control metadata from the project manager; the `.godot/` cache directory is ignored automatically (see §3.2).
5. Configure export presets: download export templates that match the editor version exactly, then set up a preset each for desktop, Android, iOS and Web.
6. Ship a build: exporting supports the command line and headless mode, ready to wire straight into CI for daily builds (infrastructure checklist in the Programming Handbook §6).

### 3.2 Version control notes

- Ignore `.godot/`: editor cache and import products live inside, all regenerable — committing them only slows the team down.
- Commit import configs: the import-parameter files beside source assets record how each asset is processed; without them, imports differ across machines.
- Scenes and resources are text formats, diff- and merge-friendly; but when two people edit one scene at once, conflicts still resist merging. Team law: one scene belongs to one person at a time.
- Binary assets go through Git LFS to keep the repository from ballooning.
- Before committing, run the editor through once to confirm no broken references; rename and move through the editor wherever possible.

### 3.3 Export and multi-platform

- Export templates are the precondition: template and editor versions must match strictly — a mismatch is the most common cause of export failure.
- Desktop (Windows, macOS, Linux): the smoothest pipeline; signing and distribution follow your store or self-publishing channel (details in Multi-platform Launch Playbook).
- Mobile (Android, iOS): Android needs a signing key and package name; iOS final signing depends on the macOS toolchain — non-Mac teams should plan ahead.
- Web: it runs, but the browser environment imposes plenty of limits — bundle size, memory and audio strategy all need real-device verification; do not try it for the first time the week before launch (deeper coverage in Mini-Game Development).
- Consoles: no official out-of-the-box export template; real console hardware goes through third-party porting services — ask for quotes and schedules early; handheld-class devices (such as the Steam Deck) are covered by the Linux build.
- Automation: wire command-line exports into CI; one downloadable build per day is the minimum bar.

## 4. Idioms for Key Systems

This section is Godot's way of thinking: accept its worldview first, then build — it saves a lot of rework.

### 4.1 Nodes and scenes: composition over inheritance

Godot has no separate "component" concept — nodes themselves are the unit of composition:

- Each node does one thing (display, collide, time, play); behavior comes from scripts attached to nodes;
- A scene is a reusable subtree of nodes, the equivalent of other engines' prefabs; characters, levels and UI are all scenes;
- You add capability by attaching child nodes: want health, add a health node — not code in the base class;
- Reserve inheritance for true variants of one kind (a regular enemy and a boss sharing base behavior), never as a reuse mechanism. A base class that grows fatter with every change is a signal you are heading the wrong way;
- Nodes reach each other through unique names within a scene or through references fetched once at ready time — do not scatter fragile long paths.

### 4.2 GDScript vs C#: settle it with one table

| Dimension | GDScript | C# |
| --- | --- | --- |
| Getting started | Close to Python; write it once you can read the docs | Needs C# and .NET basics |
| Fit with the engine | First-class; the default language of docs and examples | Officially supported; fewer example coverings |
| Language power | Mostly dynamic; static type hints speed it up | Strong typing, generics, mature toolchain |
| Performance | Sufficient; mind how you write hot paths | Steadier for compute-heavy and complex systems |
| Ecosystem compatibility | The vast majority of community code and plugins just work | Some plugins ship only the GDScript version |
| Platform coverage | All target platforms | Certain export platforms lag — check first |

Selection rules:

- Solo and small-team projects, prototyping: GDScript — iteration speed is productivity.
- Teams whose native language is C#, or compute-heavy core systems: choose C#, and use the .NET editor build.
- Keep one primary language per project; mixing needs a clear boundary (tooling scripts in one, a simulation kernel in the other) — do not hop back and forth inside one system.
- The default when unsure: GDScript. The performance difference rarely earns first-variable status — measure before switching.

### 4.3 Signals: the default decoupling tool

- Signals are a node's broadcasts: emitters announce "this happened" without caring who listens; listeners connect themselves.
- Typical use is cross-module notification: health changes refresh UI, pickups trigger audio, an achievement system eavesdrops on global events.
- Connection lifecycle: connections are cleaned up when the node is freed; guard against duplicates when wiring dynamically — doubled connections fire twice.
- Moderation: signals suit notification, not heavy data requests; keep cross-layer chains within two hops — forwarding through layers turns debugging into archaeology.
- The editor shows which connections hang on a node; start there when chasing "who triggered what."

### 4.4 Autoloads: keep global singletons restrained

- An autoload is a global node that lives as long as the game — right for whole-lifetime services: scene transitions, audio buses, save read/write, global settings.
- The anti-pattern: stuffing game rules, player data or scene-object references in; dependencies go hidden, load order becomes implicit coupling, and testing and refactoring both get harder.
- Discipline: keep the total in single digits, and write one line of responsibility per autoload; if nodes plus signals can solve it, do not go global.
- Pair with signals: global services broadcast (e.g. "scene changed") and scenes subscribe and react, rather than everyone grabbing global state.

### 4.5 Resources and the import pipeline

- Resources are savable data objects; custom types enable data-driven design: weapons, cards and enemy configs as resource files — tune values without touching code.
- Import pipeline: external assets are processed by the import system on entry; processing parameters live beside the source files, products go to the cache directory and rebuild automatically — never edit the cache by hand.
- Shared references are the biggest trap: resources are shared by default, and changing properties at runtime affects every referrer; before editing, make a local copy first, then edit the copy.
- Division of labor: data in resources, behavior in scripts, structure in scenes. Value-tuners tune values; logic-changers change logic.

### 4.6 Scene instancing and composition

- Instancing is one scene embedded in another (dragged in via the editor or spawned at runtime) — where Godot's composition actually lands.
- Make reusable units into sub-scenes: health bars, pickups, hitboxes, camera arms, AI sensors; the main scene only assembles and wires.
- Variants use scene inheritance (a regular enemy to an elite), organization uses instancing — each does its job.
- Beware the "god scene": past a few hundred nodes, split it; break sub-scenes out by function and pick up on-demand loading along the way (see §5).

## 5. Performance and Optimization

General rule: measure before optimizing — smooth in the editor does not count; target devices do (methodology in the Programming Handbook §3).

### 5.1 CPU

- Per-frame callbacks are the most expensive resource: turn off what need not run every frame, and stop them promptly when a state ends.
- Avoid per-frame allocations: string concatenation, temporary arrays, object churn — eliminate them one by one on hot paths.
- Do not look up nodes every frame; fetch frequently used references once at ready time and keep them.
- Add static type hints to hot GDScript variables — a clear speedup, far cheaper than changing languages.

### 5.2 Rendering

- 2D: share textures and materials across the screen so batching works; atlases are the basic tool — constantly switching textures throws that away.
- 3D: get distance culling and occlusion culling right first; multi-instance rendering for heavy repeats (grass, bullets, trees); toggle shadows and post-processing per device tier.
- Keep two things in view on mobile: draw calls and overdraw — the usual suspects for dropped frames and heat.

### 5.3 Physics and loading

- Collision shapes should be simplified shapes that are good enough, not art-shaped; give no rigid body to objects that need no physics.
- The physics backend is pluggable (Jolt); for large-scale physics scenes, decide after comparative measurement.
- Split big scenes, load on demand, instance over frames; loading everything in one go at a door is a common source of stutter.
- Choose texture compression per platform; short sound effects resident in memory, long music streamed.

### 5.4 Mobile and Web specifics

- Test on the lowest-end devices as the floor: mid-to-low-end Android phones and target browsers — not your dev machine.
- Set budgets before building: one number each for memory, bundle size and framerate — over budget, cut content.
- Get the Web export running end to end early: browser compatibility, bundle size, memory and audio strategy verified early in the project.

## 6. Learning Path

A straight line; every step is accepted by something you made:

1. The official docs' getting-started chapters: walk the four-piece set — editor, nodes, scenes, scripts — and follow along to build the official starter project. The docs have multiple languages (including Simplified Chinese); when unsure about a term, cross-check the English original.
2. The language: finish the official GDScript tutorials (variables, functions, signals, classes) — enough to write your first small game.
3. First game: one small but complete game playable to an ending, covering movement, collision, UI, saves and audio (process in the Getting Started section's Your First Game).
4. Toolchain: use the debugger, profiler, export flow and a test plugin (GUT or gdUnit4) one by one.
5. Community: ask in the official forums and chat communities, join game jams; Chinese tutorials are plentiful but uneven — keep the official docs as the mainline.
6. Advanced: read official example projects and engine source (route in the Engine Internals Path), learn plugin development as needed.

## 7. Common Pitfalls

1. **Building features with inheritance**: three-deep base-class trees, overrides everywhere, "add a method to the base" as reflex. Think composition first (attach child nodes, embed sub-scenes); keep inheritance for true variants.
2. **Autoloads as the global variable bucket**: everything stuffed in, dependencies invisible, tests impossible. Hold the count down and write responsibilities clearly.
3. **Runaway signal chains**: notifications crossing five or six nodes, and when something breaks you cannot find who sent it. Cross-module communication needs a clear wiring layer.
4. **Editing shared resources at runtime**: change one property and the whole project follows. To change a copy, make it local first.
5. **Cache directory not ignored**: `.godot/` slips into version control, the repository fills with regenerable files, and teammates overwrite each other.
6. **Force-merging scene conflicts**: two people edit one scene and merge the text by feel — broken node references surface as errors only later. One scene, one person; or let the editor redo the change.
7. **Mismatched export templates**: exporting someone else's project and hitting a missing-template error. Align template and editor versions first.
8. **Mistaking editor performance for the device**: smooth on a dev machine, dropping frames on mid-range Android and in browsers. Performance conclusions only count on target devices.
9. **Heavy work per frame**: node lookups, string building and object creation inside per-frame callbacks quietly eat the framerate.
10. **Sticking with old tutorials**: tutorials lag engine iterations as a rule — when they do not line up, the official docs are the arbiter.

## Further Reading

- Programming Handbook: architecture choices, core systems, performance methodology and engine-concept comparisons — the base document cited throughout this page.
- Multi-platform Launch Playbook: desktop, mobile and Web release flows and store integration details.
- Mini-Game Development: the Web route expanded — engineering constraints and platform capabilities for mini-game platforms.
- Indie Survival: scope control and scheduling, complementing the audience positioning of §1.
- Engine Internals Path: the roadmap and weekly plan for when you want to read the engine's internals.
