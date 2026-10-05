# Ludo Atlas · Engine Tracks · Defold

> **Engine Tracks**. Positioning: a free, source-available lightweight engine — Lua scripting plus a component-and-message working model, with small-scope 2D, mobile and HTML5 projects as home ground.
> Companions: Programming Handbook · Multi-platform Launch Playbook · Indie Survival · Pitfalls & Anti-patterns.

---

## 1. Positioning and Choice

Defold is a free cross-platform game engine maintained by an independent foundation, with public source you can read and modify; commercial games pay no license fees and no revenue share. It grew up on mobile and web games — a small footprint and fast startup are design goals written into its genes.

Three bedrock strengths on the engineering side:

- Lua is the only scripting language: small syntax, quick to learn, no second official language to choose from.
- An all-in-one workbench: scenes, particles, tile maps, the GUI and code editors, the debugger and the profiler all live in the editor — install and go.
- 2D first: sprites, atlases, tile maps, particles, frame sequences and Spine skeletal animation are out of the box; 3D runs, but the toolchain is not deep.

### Who it fits

- Indie developers and small teams: zero-cost start, light projects, one project covering desktop, mobile and Web.
- Small-scope 2D and casual gameplay: with controllable content volume, the lightweight advantage turns directly into delivery speed.
- HTML5 and web platforms: where bundle size and startup are hard metrics, exports and platform SDK extensions are ready-made.
- Mobile-first lightweight projects: Android and iOS exports are mature, with a smooth real-device debugging chain.
- People who know or want to learn Lua: a low language threshold and straightforward engine APIs.

### Who it does not fit

- Projects with heavy content and deep designer-artist collaboration: the editor's tool surface is narrower than mainstream engines — collaboration leans on conventions.
- Heavy 3D and photoreal visuals: not its battlefield.
- Teams leaning heavily on commercial plugins and middleware: the ecosystem is small — many capabilities are built in-house or found in community libraries.
- Projects planning rapid team growth: few people know Defold and hiring is hard (see §7).
- Learners relying only on Chinese materials: Chinese content is scarce — the mainline docs are English-first.

### Against Godot and Cocos

| Scenario | Defold | Godot | Cocos |
| --- | --- | --- | --- |
| Lightweight 2D, small-scope finished work | First choice: small footprint, fast builds | Usable, heavier engineering | Usable, 2D mature |
| HTML5 and international web platforms | First choice: tiny exports, platform SDK extensions ready | Heavier exports, needs testing | Usable; home ground is China |
| WeChat/Douyin mini-games | Weak chain | Weaker | First choice |
| Mid-scale-and-up 2D | Usable, accepting the narrower editor and ecosystem | Steadier | Steadier |
| 3D projects | Lightweight stylized only | Usable at mid-scale | Usable light-to-mid |
| Ecosystem, tutorials, hiring | The smallest | Thick | Thick in China |
| License | Free, source available | Free, fully open source | Editor free, runtime open source |

The trade-off asks three questions only: does the target platform list include HTML5 or lightweight mobile; is the project small-scope; can the team accept a small ecosystem. Three yeses make Defold an efficient choice; one no sends you back to the [Engine Tracks index](../README.md) to re-evaluate.

## 2. Ecosystem and Project Structure

Set expectations first: the official docs are good and frequently updated, with the official team present in the forum; the third-party scale is small — plugins, assets, finished-goods solutions and tutorials all trail Godot and Unity by a distance, Chinese content especially. There is no central package repository; dependencies hang on the project config as archive URLs. Editor extensions are written in Lua, and platform SDK integration and performance surgery go through C/C++ native extensions.

The project spine is small — no elaborate skeleton:

| Location | What goes here |
| --- | --- |
| `game.project` | Project config: display, physics, input bindings, asset packing, dependency list; plain text, committed |
| Collections (`.collection`) | Scene units and the startup entry; a project has at least one main collection (see §4.3) |
| Game objects (`.go`) and scripts (`.script`) | Characters, components and logic, split by feature and kept nearby |
| Atlases, fonts, materials, particles, GUI and other assets | The content itself; 2D sprites usually go into an atlas before use |
| `.internal/` and `build/` | Editor cache and build output — both stay out of version control |

Three habits for the asset pipeline:

- The build only collects what is reachable by reference from the main collection; unreferenced files do not ship — dynamically loaded assets must sit on the reference chain too (see §7).
- Rename and move assets through the editor where references sync automatically; moving files by hand breaks the chain.
- Dependency upgrades and platform SDK updates each need a regression checklist — replaced by hand, verified by hand.

Version control: Defold works well with Git — project files are text and diffable; the editor shows a file-changes panel for status and diffs, while commits and pushes still go through an external Git client. Structured files like collections and game objects leave essentially no room for manual merging of edit conflicts — sidestep them with the rule "one file, one person at a time" (see §7).

## 3. Core Workflows

### 3.1 From zero to running

1. Install the editor (Windows, macOS and Linux all have builds) and create a project; the editor bundles code editing and debugging — get the bundled sample running first.
2. Stand up the main collection: make the entry scene the main collection, assembling the minimal runnable content from "background, player, camera".
3. Attach scripts, add input: scripts mount on game objects as components; declare actions in the input bindings first, then have scripts respond by action name (see §4.5).
4. Run it: run straight from the editor with hot-reloaded script changes; read errors in the console and attach real-device debugging for device problems.
5. Enter version control: ignore editor caches and build output, and after the first commit confirm the project rebuilds in a clean environment.
6. Produce the first build: one each for desktop, Android and HTML5, then walk the release checklist (details in the Multi-platform Launch Playbook).

### 3.2 Builds, packaging and live updates

- Desktop (Windows, macOS, Linux): the smoothest flow — signing and distribution per channel requirements.
- Mobile (Android, iOS): Android needs a signing key and package name; iOS packaging and signing depend on the macOS toolchain — non-Mac teams should plan ahead.
- HTML5: produces a static site ready to host directly; web game platforms (Poki, CrazyGames and the like) have ready SDK extensions.
- Consoles (Switch, PlayStation): through platform-approved developer channels; there is no public self-service flow.
- Live Update: exclude non-first-screen assets from the build and download them at runtime; not supported in editor runs — verify in packaged builds.
- Automation: the command-line build tool (bob, requiring a Java environment) runs builds headlessly, suited to CI daily builds (infrastructure checklist in the Programming Handbook §6).

## 4. Idioms for Key Systems

Accept the working model before building: objects assemble from components, and components talk in messages.

### 4.1 Game objects and components: assembly first

- The engine's smallest unit is the game object: position, rotation, scale — with no behavior of its own.
- All behavior comes from components: sprite, label, collision object, sound, particles, tile map, model, camera, script; whichever component you mount, that capability you get.
- Game objects cannot nest inside game objects; hierarchy and reuse go through collections (see §4.3). To add capability, mount a component — avoid growing one all-purpose script.
- Numeric parameters live in component properties: scripts declare properties and expose them in the editor, so tuning needs no code changes.

### 4.2 Message passing: components talk in messages

- Components do not call each other directly; communication goes through message passing: the sender names a receiving address ("which component of which object"), attaches a message name and data, and the receiver responds in a callback.
- Name the lifecycle callbacks: initialization, per-frame update, fixed-step (physics) update, message received, input received, hot reload, destroy cleanup.
- Messages are asynchronous: right for event notification (getting hit, pickup, state change), wrong for high-frequency per-frame data queries; couple per-frame reads and writes through properties directly.
- Centralize address strings into constants: typos surface only at runtime, and building them on hot paths costs performance too.

### 4.3 Collections, factories and loading

- Collections are the reuse and organization unit: levels, gameplay modules and whole UI sets can each split into sub-collections — the main collection is just the entry.
- Factories spawn game objects at runtime, and collection factories instantiate whole collections; the engine provides no object pool, so high-frequency spawns (bullets, effects, floating text) must be pooled yourself (see the Programming Handbook §2.5).
- Sub-collections load and unload dynamically through collection proxies — the standard tool for level switching and streaming; keep the main collection slim.
- Discipline: loading everything in at startup is a classic source of stutter and memory bloat; split by scene and load on demand.

### 4.4 Scripts and Lua discipline

- Lua is the only official scripting language; scripts organize as "one per component", all callback-driven.
- Globals are shared across all scripts — omitting `local` pollutes between them and buries hidden dependencies; default to local and put shared logic in modules.
- Hot reload covers scripts; structural changes like collections, atlases and properties wait for a build.
- Lua's temporary tables and string concatenation all land on the GC's ledger — write hot paths allocation-free (see §5).

### 4.5 GUI and input

- UI runs through the separate GUI system (gui resources plus scripts), apart from the world's game-object system; build interfaces separately from scenes — do not assemble UI inside scenes.
- Input declares actions in the input bindings first (keyboard, touch, gamepad each bound), and scripts respond by action name rather than polling keys.
- Animation: frame sequences work out of the box; skeletal animation imports via Spine; presentation niceties like tweening are not in the core — community libraries or your own.

## 5. Performance and Optimization

Know the cost structure first: lightweight means fewer engine safety nets, and optimization concentrates in three places — render batching, Lua memory and platform differences.

| Direction | Key points |
| --- | --- |
| Rendering | 2D bottlenecks are texture switches and draw calls: batching needs one atlas, so split atlases by usage; GUI runs its own channel — optimize separately; control translucent layers and particle counts — overdraw is the main heat source on mobile |
| Scripting and memory | Fewer per-frame allocations: temporary tables, string concatenation and closures all land on the GC; cache addresses and references ahead; pool high-frequency objects |
| Physics | Physics only happens on objects with collision objects mounted; use simplified collision shapes; if the gameplay needs no physics, switch it off |
| Loading and bundle | Only referenced assets ship (see §2); Live Update moves non-first-screen assets out of the initial package; on HTML5 watch first-package size and runtime memory |
| Target platforms | Conclusions count only on real devices and target browsers: HTML5 varies widely in audio, input and memory; low-end Android is the mid-low budget baseline |

One line of method: measure before optimizing (methodology in the Programming Handbook §3) — smooth in the editor does not count.

## 6. Learning Path

A straight line; every step is accepted by something made:

1. Official onboarding tutorials: walk editor operations, collections, game objects, components and messages, following the official from-scratch tutorial project; Chinese content is scarce — read the English docs directly, cross-referencing terms against the API reference.
2. Lua catch-up: if new to the language, learn it first (tables, closures, local vs. global scope) — enough to read and write scripts; no need to finish it before starting.
3. First work: a small-scope 2D piece covering input, collision, GUI, audio and saves; once it runs on desktop, produce an HTML5 and an Android build each.
4. Toolchain: use the profiler, real-device debugging, command-line builds and dependency management one by one, treating "one runnable build per day" as the minimum bar.
5. Community: the official forum and chat communities are the main asking grounds (English); third-party libraries and extensions turn up on GitHub — check maintenance status before adopting.
6. Advanced: read the engine source (route in the Engine Internals Path); touch native extensions only when integrating platform SDKs or performing performance surgery.

## 7. Common Pitfalls

1. **Editor dependence**: collections, components and properties are basically maintained through the editor only — hand-editing project files is unrealistic; external scripting can do only so much, and the team must accept "content changes go through the editor".
2. **Force-merging scene files**: two people editing one collection or game object is essentially unmergeable by hand; one file, one person — whoever edits, closes it out.
3. **Unreferenced assets never ship**: builds collect only what is reachable from the main collection — a missing reference surfaces only at runtime; confirm new assets sit on the reference chain.
4. **Sparse community resources**: tutorials, examples, plugins and assets run an order of magnitude below mainstream engines; set expectations and solve many things in-house or by reading source — and check the freshness of old video tutorials.
5. **Hard to hire for**: few developers know Defold, making growth, outsourcing and handovers hard to staff; the team's foundation is best built on Lua veterans.
6. **Forcing heavy 3D onto it**: 3D components are complete but the toolchain is shallow — do not bet on photoreal projects; for lightweight stylized 3D, build a technical slice first.
7. **Message address strings scattered**: typos blow up only at runtime; centralize into constants, and split modules once cross-module messaging passes two layers.
8. **Per-frame allocations dragging down mobile**: Lua GC jitter shows as periodic stutter on low-end devices; run an allocation-free pass over hot paths.
9. **Dependencies and platform SDKs unattended**: dependencies come in by URL and upgrade by manual replacement plus regression; platform SDKs update often — leave schedule room for maintenance.
10. **Mistaking editor performance for the device**: smooth in the editor is not smooth in a release; HTML5 and mobile differ most — conclusions count only on target devices.

## Further Reading

- [Programming Handbook](../../fundamentals/programming/README.md): architecture, core systems and performance methodology — the base document cited throughout this page.
- [Multi-platform Launch Playbook](../../../playbooks/platform-launch/README.md): release flows for desktop, mobile, Web and web platforms.
- [Indie Survival](../../../playbooks/indie-survival/README.md): scope control and scheduling discipline — the upstream decision for a small-scope route.
- [Pitfalls & Anti-patterns](../../pitfalls/README.md): read against section 7 here.
- [Engine Internals Path](../../fundamentals/engine-internals/README.md): a public, readable source is one of its long-term values — start here when you want to read the engine's internals.
- [Engine Tracks index](../README.md): all 12 tracks at a glance and what comes first.
