# Ludo Atlas · Engine Tracks · Unity

> **Engine Tracks**. Positioning: the Unity-track engineering handbook, covering the component mental model, script lifecycle, data assets, package ecosystem, version control and multi-platform builds.
> Companions: Programming Handbook · Art & Audio Handbook · Production Handbook · Mini-Game Development.

---

## 1. Positioning and Choice

In one line: Unity is the general-purpose engine that is **component-based, C#-scripted, and backed by the largest ecosystem**. It is not picky about game genres; it is picky about team engineering discipline: the editor presses assembly costs very low, and once a project grows, structure, performance and collaboration problems are all yours to hold up.

Fits:

- Small-to-mid teams and indie developers building a first commercial title: docs, Q&A and tutorials are the cheapest to search among engines of its class.
- Develop once, ship to many platforms: desktop, mobile, console and Web share one project and content set.
- 2D and low-to-mid-poly 3D projects: the 2D workflow and the 3D pipeline live in one editor; hybrid projects need no tool switch.
- Prototypes with frequent gameplay and balance iteration: change in the editor, verify immediately — a very short loop.

Think twice:

- High-fidelity 3D and enormous scenes: that is Unreal's home turf; do not carry an art gap on engineering grit.
- Ultralight 2D micro-projects: Godot or a Web stack has a smaller engineering surface.
- Deep engine surgery: Unity's core is closed source — the upper layers are customizable, the bottom is not.

Cross-engine trade-offs in four lines (other tracks in `docs/engines/`):

| Project profile | Usual choice |
| --- | --- |
| General commercial projects with hiring and outsourcing ecosystems | Unity (this page) |
| Full open source, willing to read and patch engine code | Godot or a self-built engine |
| High-fidelity 3D, large-team industrial pipelines | Unreal |
| Web-only delivery, page-level lightweight gameplay | A Web stack |

Selection checklist:

- Does the target list include Web or mini-games? If so, verify bundle size and loading first, then decide (§3.3).
- Who maintains the build and version control? With no dedicated owner, stand up the §2.4 conventions first.
- Is this a 2D or a 3D project? Once decided, unify camera, lighting and asset specs — do not mix the two approaches.
- What is the team's C# and architecture level? Most technical debt in Unity projects comes from code organization, not the engine.

## 2. Ecosystem and Project Structure

### 2.1 Project directories

| Directory | Content | In version control | Notes |
| --- | --- | --- | --- |
| `Assets/` | Scenes, scripts, prefabs, materials, models, audio — the project content | Yes | The workspace; all content is produced here |
| `Packages/` | Dependency manifest and locally embedded packages | Manifest and local packages yes | Declare dependencies in the manifest; never copy source in by hand as a "dependency" |
| `ProjectSettings/` | Project-level config: rendering, input, physics, quality | Yes | Part of team collaboration; changes deserve review |
| `Library/`, `Temp/`, `Logs/` | Import cache, temporary files and logs | No | Rebuilt per machine; committing only makes conflicts and noise |

### 2.2 The composition mental model

- **A GameObject is an empty container** with no function of its own; everything comes from attached components: rendering, collision, audio, custom scripts are all components.
- All composition is snapping parts onto a container: a character equals a transform, a collider, an animator plus a few behavior scripts. There is no inheritance tree, only assembly — so "where does this feature go" usually answers itself with "a new small component."
- A **scene** is the runtime stage for objects, doubling as placement sheet and wiring chart. Treat scenes as configuration and mounting tables; heavy logic does not grow inside them.
- A **prefab** is a reusable object template: build the prototype in a scene, save it as an asset, instantiate from it. Supports nesting (prefabs containing prefabs) and variants (derived configuration from a base prefab).
- The model in one line: **components are parts, prefabs are blueprints, scenes are the assembly floor.** Reusable behavior goes into components and prefabs; one-off placement stays in scenes.

### 2.3 Package management and tooling ecosystem

- Official capabilities ship modularized as packages: install what you use, and keep "which packages and why" answerable in one sentence per package; clean out the unused regularly.
- Packages come from four sources: the official registry, the Asset Store, Git URLs, local paths. Before a third-party package enters, assess five things: size, compile time, license, maintenance status, and whether you can take only the parts you need.
- Package pollution is Unity's most covert cost: one big all-in-one asset bundle raises import time, compile time and build size at once, and drags in its own directory structure, sample scenes and stale dependencies. The discipline: probe in isolation first; bring it into the main project only after review.
- Official cloud services (analytics, cloud saves, relay multiplayer, etc.) are wired in as needed; assess switching costs at selection time.
- Tooling ecosystem: IDE integration (completion and debugging), editor scripts (turn repeated operations into menu commands), unit and Play-mode tests, profilers (§5). Any process performed by hand three times deserves scripting.

### 2.4 Version control conventions

Unity projects differ from ordinary code repositories in two things: **assets are binary, and references rely on companion files.**

- **Text serialization**: set asset serialization to text so scenes and prefabs become readable, diffable, mergeable text files. This is the precondition of multi-person work — switch it on day one, not after the incident.
- **`.meta` files**: every asset and folder has a `.meta` recording its unique ID and import settings. Three rules: commit them with the assets; rename and move only through the editor (renames outside the editor sever references); never hand-edit or delete them.
- **Git LFS**: textures, audio, models, video and fonts go into large-file storage, leaving only pointers in the repository. Start the ignore list from the official template; `Library/`, `Temp/`, `Logs/` and build outputs never enter the repository.
- **Smart Merge**: the official merge tool performs structural merges of scene and prefab text conflicts on pull and merge. It only handles syntactic conflicts; semantic conflicts (two people changed different properties of one object) still need human judgment. The real fix is to reduce concurrent edits of the same file.
- Collaboration discipline: split scenes and prefabs by module to avoid multiple people on one big scene; commit messages state what behavior and assets changed.

## 3. Core Workflows

### 3.1 The daily loop in the editor

The daily rhythm: assemble in the scene → enter Play mode to verify → exit, change scripts and assets → enter Play mode again. Three disciplines:

- Changes made in Play mode are not kept: treat Play mode as a read-only observation window — note the problem, return to edit mode, and change the asset there.
- Reproduce problems in a minimal scene: strip a test scene with only the relevant objects out of the main scene; do not debug on the full level.
- Script repeated operations: batch import-setting changes, batch asset generation, batch naming checks — each as an editor script run in one go.

### 3.2 Scene and prefab workflow

The standard path: whitebox scene → identify repeated objects → extract into prefabs → manage differences with nesting and variants → the scene keeps only placement and a few deliberate overrides.

- Layer scenes: environment (static), gameplay objects (prefab instances) and systems (camera, managers, lights) under separate root nodes, so anyone can read the shape of the tree.
- When to extract a prefab: the second time the same object appears. A third copy-paste is debt you are burying for yourself.
- Keep instance overrides restrained: changing a prefab instance's properties in a scene creates overrides, and overridden properties stop following base-prefab updates. Allow a few deliberate overrides; forbid casual edits.
- Use variants for different configurations of one prototype: enemies with different stats, doors in different colors — express the difference as a variant, not a copied subtree.
- Signals to split a scene: people start blocking each other, a single scene gets slow to load, or one scene absorbs unrelated modules. At that point, split by area or gameplay and stitch with async loading.

### 3.3 Builds and multi-platform

Unity's build model is "pick a target platform, get its artifact"; the three platform families differ:

| Family | Artifact form | Main constraints |
| --- | --- | --- |
| Desktop | Executable and data directory | Storage-path and graphics-API differences; the loosest constraints |
| Mobile | Store-distributed app packages | Heat and memory the tightest; real-device testing mandatory; iOS requires AOT compilation |
| Web | Web artifacts loaded by the browser | First-load size and time are lifelines; the browser sandbox limits threads and capabilities; mobile browsers weaker still |

- Script compilation: targets without runtime compilation (iOS, Web) need AOT ahead of time — verify reflection and dynamic code generation early, not at release.
- Build as configuration: package name, icons, signing, scene list and quality tiers per target are project configs; freeze several sets at repository creation instead of hand-filling on release day.
- Automated builds: make the build a command-line task wired into CI, producing a playable version on every commit (Programming Handbook §6). Menu-clicked builds are for local debugging only.
- Web and mini-games: watch the first-load time on Web builds — asset splitting and lazy loading are standard tools; Chinese mini-game platforms have no native build target and convert from Web builds with adaptation layers, with stricter size and performance thresholds.
- Tick through platform differences: input methods, resolution and safe areas, platform lifecycle (background suspend and resume), permission dialogs, storage and cloud saves, fonts and localization (reuse the checklist in the Multi-platform Launch Playbook).

## 4. Idioms for Key Systems

### 4.1 Script lifecycle and execution order

Lifecycle callbacks are the skeleton of Unity programming. Memorizing them is not enough; understand two things: **who is called when, and that order among scripts in the same phase is not guaranteed.**

| Callback | Timing | Common duties |
| --- | --- | --- |
| Awake | Once when the object is loaded or instantiated (deferred if inactive) | Grab own component references, initialize internal state |
| OnEnable | Every time the object is enabled | Subscribe to events, register with managers |
| Start | Once after first enable, before the first frame update | Wiring that needs other objects ready |
| FixedUpdate | Called on a fixed time step; zero or more times per frame | Physics and force-related logic |
| Update | Once per frame | Input sampling, non-physics logic, presentation driving |
| LateUpdate | Once per frame, after all Updates | Camera follow, logic depending on other objects' positions this frame |
| OnDisable / OnDestroy | On disable and destroy | Unsubscribe, return to pools, release resources |

Execution-order awareness:

- Within a phase, there is no stable order between scripts by default. Two scripts grabbing each other's references in their own Awake leave success to luck — the symptom is random null references.
- Converge it two ways: fold coupled initialization into one explicit entry (one script initiates in order), or declare script execution order in the editor. The larger the project, the more you need the former; declared order suits only a few special cases.
- Cross-phase traps: reading in Awake a value another object only prepares in Start; reading physics results in Update while physics actually steps in FixedUpdate.
- Draw "who depends on whom" as a directed graph: acyclic, single entry, predictable order. Projects with a tangled graph crash randomly during startup, unreproducibly.

### 4.2 ScriptableObject: data assets

A ScriptableObject is a data object serialized inside the project; its job is to **pull data out of scene objects**: value tables, configs, enemy dossiers, event channels. It solves three things: sharing one copy of data across referrers, visual editing in the editor, and avoiding a copy per instance.

- Values and configs go into data assets: character parameters, level configs, economy tables. Values scattered across scenes and prefabs are the source of maintenance disasters.
- Decouple through data assets: the trigger side and the subscriber side each reference the same data asset (an event channel) without knowing each other — cross-module notification without hard references.
- Treat them as read-only at runtime: editing a data asset while running the game in the editor writes the change back into the asset — the most common way to shoot yourself; put mutable state in ordinary runtime objects.
- Data assets are ordinary assets: diffable, scriptable in batches, reviewable — value changes get a process and a history.

### 4.3 Systems idiom checklist

Against the cross-engine checklist in the Programming Handbook §2, the Unity landing spots for each system:

- **Input**: layer logical actions over physical keys, decouple input sampling from the fixed physics step, and account for short presses per frame (Programming Handbook §2.1).
- **Object pools**: pool high-frequency objects — bullets, effects, enemies — and pre-warm to peak counts; prefer the engine's pooling options over hand-rolled ones.
- **UI**: separate data from views; split interfaces into multiple canvas units, keep frequently changing elements apart from static ones, and control rebuild scope.
- **Saves**: store state, never object references; carry a version number and migration logic; write to a temporary file and swap, guarding against corrupt saves on interruption.
- **Camera**: follow parameters (look-ahead, dead zone, smoothing) and shake clamping per the checklist in the Programming Handbook §2.3; screen shake must be switchable off.
- **Localization**: externalize all visible text into keys; reserve text areas for multi-language lengths; font fallback chains covering CJK characters.

## 5. Performance and Optimization

Methodology inherited from the Programming Handbook §3: set budgets first, measure before changing, real devices over the editor. Unity projects concentrate hot spots in five places:

| Hot spot | Symptom | Countermeasure |
| --- | --- | --- |
| Total per-frame callbacks | Framerate keeps falling as object count rises | Merge driving into a few managers, replace polling with events, enable on demand |
| Managed allocations | Periodic stutters (GC pauses) | Eliminate hot-path allocations: string concatenation, boxing, closures, collection growth; object pools |
| Runtime lookups | Hot functions full of lookup calls | Fetch references once at initialization and cache them; prefer editor-wired references over code lookups |
| Render submission | GPU waiting, CPU busy submitting | Batching and atlases, fewer material switches and translucent areas; find the real culprit in the frame debugger |
| Physics and animation | Frame drops with many rigid bodies or dense skeletons | Layered collision filtering, simplified colliders, lower physics rate, limit skeleton and skinning layers |

- Measurement toolchain: the engine Profiler for frames and memory, the frame debugger for render submission, memory snapshots for resident assets, platform tools for real-device confirmation. Editor data often lies; conclusions stand on real devices.
- Budget sheets: split the frame budget by target framerate across logic, rendering, physics and UI; memory budgets per platform; bundle-size budgets per channel. Breaching a budget raises an alarm — better yet, in CI.
- Mobile specifics: thermal throttling (framerate after long sessions), memory waterline (the risk of the OS killing the process), bundle size and download conversion; Web specifics: first-load time, browser memory ceilings, the mobile-browser compatibility matrix.
- Optimization discipline: change one variable at a time and record numbers on the same scene and path before and after; no optimization without measurement.

## 6. Learning Path

Four stages by artifact; each milestone is something playable or usable, not a count of finished tutorials:

1. **Engine basics (on the order of 2–4 weeks)**: C# fundamentals, editor operations, the component model. Build three small games covering: 2D movement and collision, a UI flow, save read/write; ship a Web build of each to get the build chain working along the way.
2. **System implementations (on the order of 1–2 months)**: build minimal implementations of each item in the Programming Handbook §2 (input, object pools, camera, saves, UI, audio, localization), one small demo each. The output of this stage is a capability library to draw from in real projects.
3. **Engineering (throughout)**: version control conventions (§2.4), the build pipeline, performance budgets and measurement habits (§5), tests for critical logic. Pick a piece of your own code, find three hot spots with the Profiler, and optimize until the data proves it.
4. **A complete project**: follow the process in the Production Handbook, take the engineering infrastructure to full, and walk one full release.

Learning discipline: the official manual is the authoritative source for concepts and behavior; tutorials are for onboarding and building feel. The judgments on this page evolve with the ecosystem — when they diverge, defer to the official docs and your Profiler.

## 7. Common Pitfalls

1. **GetComponent abuse**: finding components in Update, finding components in loops — the cost goes straight into the frame budget. Fetch references once at initialization and cache; anything wireable in the editor should not be looked up at runtime.
2. **The full weight of Update**: hundreds or thousands of objects each holding per-frame callbacks, everyone doing their own thing. Drive homogeneous objects through managers, or by events and state changes — do not keep every object awake every frame.
3. **Third-party package pollution**: importing a whole asset bundle for one small feature, paying with tons of dead assets, compile time and dependency conflicts. Probe in isolation first, review, take only what you need, and clean samples and unused assets after import.
4. **Per-frame allocations causing stutter**: string concatenation, boxing, closure captures, collections created in loops — all build GC pressure. Not a single allocation on hot paths; pooling and caching are the standard tools.
5. **The version control trifecta**: committing `Library/`, hand-deleting or renaming `.meta` files, staying on binary serialization. Finish the §2.4 conventions on day one.
6. **Override chaos on scenes and prefabs**: casually editing prefab instance properties in scenes, inconsistent behavior when the base prefab changes, nobody able to say who changed what. Overrides must be conscious and recorded (§3.2).
7. **Implicit script execution order**: writing initialization that relies on "it should run first" — the symptom is random null references. Converge initialization to an explicit entry or order settings (§4.1).
8. **Verifying only in the editor**: editor framerate, input and memory all differ from devices, mobile especially. Real device, target model, target duration — miss one and it does not count as tested.
9. **Data scattered through scenes**: values written straight onto components, and changing one parameter means searching the whole scene. Data goes into data assets (§4.2); scenes keep only placement.

## Further Reading

- Programming Handbook: architecture choices, core systems, performance methodology and engineering infrastructure — §4 and §5 here are the full expansion.
- Art & Audio Handbook: asset specs, import settings and presentation feedback — consult when touching the art pipeline.
- Production Handbook: the phase model from prototype to release and scope control — the entry for the project stage in section 6.
- Mini-Game Development: the routes and bundle constraints for exporting mini-games from each engine — required reading before shipping to Web and mini-game platforms.
- The official Unity manual and scripting reference: the authoritative source for concepts and behavior; this page's judgments evolve with the ecosystem — defer to the official docs and your project's Profiler.
