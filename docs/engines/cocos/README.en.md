# Ludo Atlas · Engine Tracks · Cocos

> **Engine Tracks**. Positioning: a cross-platform engine route from the Chinese ecosystem — TypeScript scripting and an integrated editor workflow, with its main battlefield in mobile games, WeChat/Douyin mini-games and the Web; 2D is its strength, 3D is being filled in.
> Companions: Programming Handbook · Mini-Game Development · Art & Audio Handbook · Multi-platform Launch Playbook.

---

## 1. Positioning and Choice

Cocos is a Chinese cross-platform engine; its active mainstay is Cocos Creator: one project exports Android, iOS, Web, WeChat/Douyin mini-games and hardware-channel quick games. Scripting is mainly TypeScript (officially recommended; JavaScript also compatible), and the workflow pivots on an integrated editor: scenes, assets, scripts and builds all happen inside it. The editor is free to use and the runtime is open source — when you hit an engine-level problem you can read the source and patch it.

The 2D and 3D situations should be read separately. 2D is home ground: rendering, atlases, UI, skeletal animation and tile maps are all mature, and the mini-game adaptation layer's accumulation lives on this line. 3D is usable and being filled in; stylized, light-to-mid and 2D/3D hybrid projects already run, but toolchain depth, tutorial density and high-end case studies show a clear gap against Unity — do not bet on it for heavy photoreal work. The earlier C++ engine line (Cocos2d-x) still sees maintenance on legacy projects, but new projects start from Creator.

The three patches where it works best:

| Patch | Why it fits |
| --- | --- |
| WeChat/Douyin mini-games | The largest share of the mini-game ecosystem: the build panel natively supports each platform's export; subpackaging, remote assets and platform debugging chains are mature |
| 2D mobile games and H5 | 2D productivity bought by long accumulation: rendering, atlases, UI, Spine and DragonBones animation, tile maps, all out of the box |
| Web and marketing interactives | Deep web lineage: small bundles, fast startup; campaign pages, interactive showcases and lightweight games are common landings |

Selection comparison (write down "what you need" and it settles):

| Scenario | Cocos | Godot | Unity |
| --- | --- | --- | --- |
| WeChat/Douyin mini-games | First choice: native export chain, most case studies | Weak support, few community solutions | Needs the official conversion path; evaluate bundle size and plugin compatibility item by item |
| 2D mobile games and Chinese channels | First choice: complete Chinese docs and community | Usable: light, open source | Thickest ecosystem, heavier engineering too |
| Light 3D (stylized, strategy, card) | Usable: 2D/3D integrated, enough for small-to-mid scale | Usable: 3D still catching up | Mature: most tooling and assets |
| Heavy 3D, photoreal open worlds, consoles | Not recommended | Not recommended | First choice (or Unreal) |
| Open source and customizable | Runtime open, editor closed | Fully open source | Closed source |
| Team with a C# background | Needs a move to TypeScript | C# available | No migration cost |

In one line: if mini-games are anywhere in your release targets, put Cocos in the first evaluation round; if the target is heavy 3D or consoles, look at the other tracks.

## 2. Ecosystem and Project Structure

The ecosystem has four parts: official docs (Chinese-first, promptly updated), official examples and templates, a plugin and asset store (Cocos Store), and community forums. Set expectations correctly: the store's scale and asset richness run a notch below Unity's, so many capabilities follow the order "check the store first, then community open-source projects, then build it yourself"; before adopting a third-party plugin, check its last update and issue status.

The spine of a standard project:

| Path | Content | Convention |
| --- | --- | --- |
| `assets/` | Scenes, prefabs, textures, audio, scripts | The content body, managed centrally by the editor's asset library |
| `extensions/` | Editor extensions (plugins) | Team-built tools live here |
| Local artifact directories | Asset import cache and build output | Kept out of version control; ignored by default in official templates |

Project organization idioms:

- Split directories by domain (gameplay, systems, UI as blocks) and keep scripts next to the assets they use — not one big pot by file type.
- Divide asset bundles by directory; granularity decided by load frequency and dependencies. Inside `resources`, assets load dynamically by path; everything else prefers serialized references.
- Scenes and prefabs are text-serialized assets — painful to diff and merge; for multi-person work, split prefabs small and avoid parallel edits to one file.
- Rename assets through the editor (references sync automatically); never rename or move them by hand in the filesystem, or reference chains break.

## 3. Core Workflows

### 3.1 Editor workflow

The daily motion: import assets in the asset manager, build the node tree in the hierarchy, tune parameters in the inspector, attach scripts as TypeScript components on nodes, and distill reusable parts into prefabs. Components expose parameters to the inspector so designers can tune directly; logic and presentation separate, UI and gameplay each modules.

- Editor preview answers "is it right"; real-device preview answers "is it smooth, does it respond" — run both.
- Change-then-preview is the source of efficiency; treat hot-reload-friendly practices (small modules, little global state) as discipline.
- Before release, run on a real device: touch, notch safe areas, low-end memory — the editor can test none of these.

### 3.2 Build and release chain (WeChat/Douyin mini-games)

From project to mini-game the chain is standardized:

1. In the build panel pick the platform (WeChat mini-game, Douyin mini-game, hardware-channel quick games, etc.) and set subpackaging and remote asset addresses.
2. The build emits a platform project directory (with platform config files and the open-data-domain project template); the editor can launch the corresponding developer tool, or open the build output manually with it.
3. Preview and real-device debug inside the developer tool, settle performance and memory; then upload the code.
4. Submit for review and release on the platform side (qualifications and review criteria in Mini-Game Development).

Build options worth understanding first:

| Option | Effect |
| --- | --- |
| Main package and subpackages | The main lever on first-package size: the main package keeps only what startup needs |
| Remote asset server | Low-priority assets on a CDN; the engine handles download and cache versioning |
| Engine native code subpackaging, engine plugins | Move the engine's own code later or switch to the platform's shared plugin, squeezing the first package further |
| Open-data-domain project template | The isolated runtime for relationship-chain gameplay (friend leaderboards, interactions), generated as needed |

Platform capabilities are not one mold; check them per target before shipping:

| Capability | WeChat mini-game | Douyin mini-game | Hardware-channel quick games |
| --- | --- | --- | --- |
| Login | Silent login with the platform account | Platform account login | Each channel's own account system |
| Relationship chain | Open data domain (friend leaderboards etc.) | Open data domain | Not applicable |
| Virality | Friend and group sharing | Short video, livestream attachment | Channel recommendation slots |
| Monetization | Ad components and virtual payments | Ad components and virtual payments | Ads and channel payments |

Two environmental differences to remember: the WeChat mini-game runtime is not equivalent to a browser and does not support WebView — check the platform's open interfaces for the rest; memory is the hardest constraint in mini-games, and exceeding it on low-end devices crashes instantly — watch the real-device memory curve more than framerate.

## 4. Idioms for Key Systems

### 4.1 Nodes, components and prefabs

- Everything is a node; capabilities assemble via components. Prefer composition; do not stretch inheritance chains into genealogies.
- Prefabs are the unit of reuse: UI modules, enemies, bullets — all prefabbed, so one edit applies project-wide.
- Configure in the editor whatever can be configured there; scripts carry only the changing logic; manage numeric parameters centrally — no scattered magic numbers.

### 4.2 Scripts, events and lifecycle

- Component lifecycle callbacks handle initialization, per-frame updates and destroy cleanup; put heavy logic on events rather than stuffing everything into per-frame update.
- Node events handle interactions (touch, click); a global event bus handles cross-module notifications (achievements, sound, UI refresh); keep event depth limited — past two layers, split modules.
- Build architecture pieces — state machines, object pools, data tables — yourself: the engine gives parts, not a finished framework (architecture practice in the Programming Handbook).

### 4.3 Assets and loading

- Dynamic loading goes through the `resources` directory or asset bundles; centralize path strings into constant tables rather than scattering them.
- The engine manages asset lifecycle by reference counting: whoever holds it, releases it; keep resident assets and scene-level assets managed separately, and check that memory falls back after scene switches.
- Tier your preloading: first-screen criticals first; secondary assets pulled in over frames in the background.

### 4.4 UI, animation and physics

- UI uses the 2D node tree plus components; set design resolution and adaptation strategy once in project settings; verify by safe areas across devices.
- Two main 2D animation routes: frame sequences (cheap, controllable) and skeletal animation (resource-light, expressive; Spine and DragonBones both import); tweened animation drives interface motion.
- 2D physics is built-in and out of the box; 3D physics is heavier (a WebAssembly module) — first ask whether the gameplay truly needs physics, then decide.

## 5. Performance and Optimization

Mini-games and low-end devices are the baseline scenario; the budget priority is fixed: memory first, rendering second, bundle size third.

| Direction | Key points |
| --- | --- |
| Memory | Watch the real-device curve; texture sizes and compression handled per platform; verify fallback after scene switches; object pools absorb peaks |
| Rendering | Batching needs one atlas and one material; control interrupts mid-batch; fewer translucent layers and full-screen particles; split atlases by usage |
| Scripting | Cache node references ahead; no per-frame lookups; fewer per-frame allocations and string concatenations to reduce GC jitter; register and remove event listeners in pairs |
| Startup | Slim the first scene; feature trimming (strip unused system modules in project settings); subpackaging and remote assets squeeze the first package under the limit |
| Physics | Enable on demand; collision group filtering; simplified shapes; drop physics frequency for smoothness if needed |

One line of methodology: measure before touching anything — editor numbers are reference only; conclusions come from real-device, tiered tests on target hardware (tool list in the Programming Handbook). Record a set of numbers before and after each optimization; no optimization without data.

## 6. Learning Path

Three stages, each with a deliverable:

| Stage | What to do | Deliverable |
| --- | --- | --- |
| Getting started | Official docs and example projects; make 2D mini-games covering movement, collision, UI, saves | Independently build a complete playable mini-game in the editor |
| Release | Walk the full mini-game chain: subpackaging, real-device debugging, review, launch | A real WeChat or Douyin mini-game live |
| Advanced | 3D basics, editor extensions, performance methodology; read engine source | A performance retrospective; small tools solving the team's repetitive work |

Coming from Unity or Godot: concepts map almost one-to-one (nodes to GameObjects, prefabs to Prefabs, components to MonoBehaviours), and architectural skills — object pools, state machines, events — transfer in full; what is new is TypeScript's type system, the details of the editor workflow, and the mini-game environment's constraint set.

Resource entry points: official docs and example projects first; video tutorials age fast — many teach old-generation APIs. Community and store entry points in [Resources](../../../resources/README.md).

## 7. Common Pitfalls

1. **Treating a major version change as a routine upgrade**: Creator major versions are refactor-grade — editor organization and script APIs both change, and third-party plugins often lag; freeze dependencies, build a regression checklist, walk the official migration guide item by item.
2. **Copying outdated tutorials**: the web is full of tutorials written against old-generation APIs; compiling is not behaving correctly. On version conflicts, trust only official docs.
3. **Treating the plugin store as a mature ecosystem**: smaller scale, uneven quality; have a self-build plan for critical capabilities, and check maintenance status before adopting.
4. **Looking for native capabilities in mini-games**: mini-games run in the platform's JS environment — SDKs and plugins with native code simply do not work; check the target platform's open interface list before deciding.
5. **Testing only in the editor and simulator**: memory crashes are a low-end-device specialty; run target devices for real before launch.
6. **Multiple people editing one prefab or scene in parallel**: text-serialized asset conflicts are essentially unresolvable; split prefabs, lock directories, stagger the work.
7. **Runaway first package**: the main-package limit is a hard constraint; ship without subpackaging and remote assets and rework is guaranteed before launch (criteria in Mini-Game Development).
8. **Loading without releasing**: reference counts never reach zero and memory does not fall back after scene switches; mark resident assets explicitly, release temporary assets by scope.
9. **Forcing it into heavy 3D**: 3D is catching up; heavy photoreal open worlds are not its battlefield — for 3D projects, validate with a slice before betting.
10. **Routing iOS payments around the old tutorials**: the virtual-payment channel is now open; historical workaround schemes are non-compliant — stop using them.

## Further Reading

- [Mini-Game Development](../../publishing/minigame/README.md): the full set of criteria on package size, platform capabilities and monetization — the parent handbook of section 3 here.
- [Programming Handbook](../../fundamentals/programming/README.md): cross-engine implementation points for characters, cameras, saves and performance methodology.
- [Art & Audio Handbook](../../fundamentals/art-audio/README.md): asset specs and 2D/3D pipelines, interfacing with this page's asset organization.
- [Multi-platform Launch Playbook](../../../playbooks/platform-launch/README.md): qualifications, anti-addiction and release flows beyond mini-game platforms.
- [Engine Internals Path](../../fundamentals/engine-internals/README.md): the starting point when you want to read Cocos runtime source.
- [Engine Tracks index](../README.md): all 12 tracks at a glance and what comes first.
