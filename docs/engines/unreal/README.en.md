# Ludo Atlas · Engine Tracks · Unreal Engine

> **Engine Tracks**. Positioning: a commercial engine known for high-fidelity real-time rendering and a film-grade content pipeline; one of the default candidates for high-spec 3D projects.
> Companion handbooks: Programming Handbook · Art & Audio Handbook · Production Handbook · Multi-platform Launch Playbook.
> Principle: no API code and no version numbers on this page; interfaces and configuration details shift with engine iterations — defer to the official documentation and your profiling tools.

---

## 1. Positioning and Selection

Unreal is the commercial engine that makes high-fidelity rendering and a film-grade content pipeline its core selling point: real-time rendering quality that closes in on offline rendering, and an asset and toolchain that overlaps heavily with film and TV production workflows. Teams use it at every scale, from three- to five-person groups to hundred-person industrial pipelines, but the engine's complexity and content cost have to be spread across headcount — without enough people, it only pays off for projects where the visuals are the selling point.

- **Rendering and visuals**: high-spec techniques such as virtualized geometry, dynamic global illumination and temporal supersampling work out of the box; the visual starting line is the highest among engines of its kind.
- **Content pipeline**: models, materials, effects, animation and cutscenes share one editor, and the flow from art software import to real-time preview is designed for industrial-scale production.
- **Two languages**: C++ is the engine's native language and Blueprint is the visual scripting system; mixing the two is the standard way of working (§4.2).
- **Business model**: the engine is free to use; once product revenue crosses the agreed threshold, you pay the vendor a revenue share, with rates and thresholds per the official license agreement. Source is provided through official channels, so you can compile and modify it yourself.

Good fit:

- High-fidelity 3D projects: realistic visuals, large scenes, cinematic staging — the engine's default capabilities match these goals most closely.
- Mid-size and large teams: the character framework, asset pipeline and collaboration flows are designed around multi-discipline roles; the more complete the team, the better the engine's complexity is spread.
- Film and virtual production: real-time rendering and film production share one toolchain, so live-action and digital content can collaborate on the same assets.
- Teams with existing C++ depth that are willing to maintain a compile pipeline: the engine's ceiling sits on the C++ side.

Think twice:

- 2D and small-scale gameplay prototypes: the engine's complexity and content cost far outweigh the payoff; a lightweight engine is the better deal.
- Non-visual-driven projects from solo or two-to-three person teams: content output cannot feed the visual ceiling, and scope tends to collapse.
- Low-end devices and lightweight build targets: high-spec rendering has a cost, and scaling down needs dedicated effort (§5).

The cross-engine trade-off settles into four rows (other tracks live under `docs/engines/`):

| Project profile | Usual choice |
| --- | --- |
| High-fidelity 3D, film-grade pipeline, full content team | Unreal (this page) |
| General commercial project, wanting ecosystem and hiring pool | Unity (`docs/engines/unity/`) |
| Fully open source, light engineering, indie development | Godot (`docs/engines/godot/`) |
| Web-only delivery, page-level lightweight gameplay | Web stack (`docs/engines/web/`) |

Selection checklist:

- Is the project's first selling point visuals or gameplay? If visuals come first, Unreal is the smooth choice; if gameplay comes first, first weigh whether you can accept the engine's complexity (§7 item 4).
- Who on the team owns C++ compilation and builds? If no one clearly does, fill that gap before greenlighting.
- Are mobile and web among the target platforms? If so, pull build size and performance validation forward; don't assume "the engine can export it" means "it can ship".
- How much content capacity do you have? The visual ceiling has to be fed with content volume; estimate art and level capacity first, then set the visual spec.

## 2. Ecosystem and Project Structure

### 2.1 Project Structure

An Unreal project keeps source content and generated output fairly separate; the skeleton is made of a few kinds of directories:

| Location | Contents | In version control | Notes |
| --- | --- | --- | --- |
| `Content/` | Levels, Blueprints, materials, models, audio and video assets | Yes | The asset workspace; organization rules in §2.2 |
| `Source/` | C++ source, split by module | Yes | Module boundaries decide the reach of a compile (§3.3) |
| `Config/` | Project-level settings for rendering, input, default classes | Yes | Shared by the team; changes get reviewed |
| `Plugins/` | In-house and third-party plugins | As needed | Isolate and evaluate third-party plugins before they enter the main project |
| `Binaries/`, `Intermediate/`, `Saved/`, `DerivedDataCache/` | Build output, caches, logs and local settings | No | Regenerable; committing them only creates conflicts and bulk |

- The `.uproject` file marks project identity and records the engine association and the enabled-plugin list; it must be committed.
- Keep the engine and the project separate: the whole team runs one engine version, and upgrades get their own scheduled validation, so nobody runs their own build (§7 item 9).
- Official templates (First Person, Third Person and so on) ship a complete gameplay example; adapting a template beats reinventing wheels in an empty project. Clear out what you don't use, and read what you keep before changing it.
- Plugins are how capability is organized: many official features and third-party middleware ship as plugins, enabled as needed; before adopting one, evaluate its maintenance status, license and size.

### 2.2 Content Organization: Directories and Naming

In the Content Browser, the path is the asset reference path; letting directories and naming drift costs you across the whole project.

- Split directories by domain (characters, environment, effects, UI, core systems, levels), then by subsystem within each domain; keep depth within three or four levels — deeper means regrouping. Keep each domain's assets inside it and shared assets in a shared directory; don't file the same asset under both a type and a function.
- Use the community-standard prefixes for naming, fix them into a team reference table, and review against that table:

| Prefix | Asset type |
| --- | --- |
| `BP_` | Blueprint class |
| `WBP_` | Widget Blueprint |
| `M_` / `MI_` | Master material / material instance |
| `T_` | Texture |
| `SM_` / `SK_` | Static Mesh / Skeletal Mesh |
| `ABP_` | Animation Blueprint |
| `NS_` | Niagara effect system |
| `DT_` | Data Table |

- Rename and move inside the editor where possible so references follow automatically; clean up the Redirectors left by moves, or they pile up in the Content Browser.
- Levels are for placement and orchestration only; reusable logic belongs in Blueprint classes and components, not grown inside levels.

### 2.3 Version Control

The biggest difference between an Unreal project and an ordinary code repository: assets are binary by default (`.uasset`, `.umap`), so you can't see what changed and conflicts can't be merged by hand.

- Set up the ignore list on day one: `Binaries/`, `Intermediate/`, `Saved/`, `DerivedDataCache/` and all build output — all of it is regenerable.
- Binary assets and large files (video, audio, model sources) go through Git LFS, leaving only pointers in the repository; `.uasset` and `.umap` go on the LFS list too.
- Git LFS's tooling for file locking and collaboration workflows is weaker than centralized options; large teams and art mass-production scenarios more often use centralized version control with file locks, so one person edits an asset at a time. Beyond tools, agree on the rules: the same level or the same critical Blueprint is edited by one person at a time.
- Blueprints can't be reviewed by diff: agree on a review method (screenshots, screen recordings, a paired walkthrough) and leave intent behind in naming and comments.

## 3. Core Workflows

### 3.1 The Daily Loop in the Editor

The daily rhythm: build levels in the editor, assemble Actors, tune materials and effects, write logic in Blueprint or C++, then enter play mode (Play In Editor) to verify. Three disciplines:

- Changing content and changing C++ have different feedback costs: content iterates almost instantly, while C++ changes go through compilation — schedule the two kinds of work on separate rhythms (§3.3).
- Reproduce problems in a minimal level: strip out a test level containing only the relevant objects from the main level; don't debug on the full level.
- Turn repeated operations into tools: batch renaming, convention checks, asset processing — build them into editor tools and run them in one pass.

### 3.2 Asset Pipeline: From Art Software to the Engine

- External assets enter `Content/` through the engine's import flow: models, textures and animation each have import options (LODs, collision, material slots, compression); fix those options into a checklist per project conventions.
- Materials are built inside the engine (§4.3), and their interface to a model is the material slot; surfaces of the same kind share a master material, and variants go through instances.
- Post-import asset specs (resolution, poly count, LODs) are part of acceptance and go through review just like naming.

### 3.3 Compiling and Packaging

- The C++ compile loop sets the project's pace: the scope of a change decides the wait, and runaway header dependencies turn every small edit into a wide rebuild. The controls: split modules, converge dependencies, put stable systems in C++, and keep fast-iterating parts in Blueprint and data (§4.2).
- Hot reload covers only some changes; touching class structure or data layout usually needs a full rebuild and an editor restart — count that in when scheduling.
- Packaging produces artifacts per target platform, separating internal test builds from release builds; wire command-line packaging into CI and keep one downloadable, runnable build per day (see the infrastructure checklist in Programming Handbook §6).
- Console and mobile releases add platform-holder authorization, dev kits and a submission process — schedule them early (Multi-platform Launch Playbook).

## 4. Key System Idioms

### 4.1 Gameplay Framework: Rules, Will, Body

The engine ships a built-in framework of role division; sort it out, and most "where does this logic go" questions have an answer:

| Role | Responsibility | Key points |
| --- | --- | --- |
| GameMode | The rules for a match or level: assembling default classes, spawn and win/lose conditions | In multiplayer it runs only on the server; in single-player it is the one place rules are defined |
| PlayerController | The player's proxy: input routing, UI interaction, view direction | On death and respawn only the Pawn is swapped; the controller persists |
| Pawn | The body in the world: position, movement, collision, being controlled | Humanoid characters use a Character subclass with a movement component |
| GameState / PlayerState | Replicated state for the match and for individuals | Put scores and phase information here, not in the UI |
| GameInstance | A session object that persists across levels | Session-level data: login state, global settings |

- The mental model in one sentence: GameMode sets the rules, the PlayerController represents the will, the Pawn is the body. Respawn swaps the body, not the will — the fastest way to check whether the division of labor is set up right.
- AI is symmetric with players: an AI controller drives an AI Pawn, from the same source as the player side; when writing AI, keep to the same "controller plus body" framework.
- Don't write rules in the Level Blueprint: rules go in the GameMode and system classes, and the Level Blueprint only orchestrates this level, or the same rule set gets written once per level.

### 4.2 Blueprint and C++: Division of Labor and Mixing

| Dimension | Blueprint | C++ |
| --- | --- | --- |
| Ramp-up | Visual, no compilation, the engine's full capability exposed | Requires C++ and knowledge of the engine framework |
| Iteration speed | Change and run; fastest during prototyping | Every change goes through the compile pipeline |
| Performance | Good enough; per-frame heavy work pays the price | More solid for hot paths and large-batch logic |
| Review and merging | Asset form; diff and code review don't apply | Diffable, reviewable, revertible |
| Where it lands | Prototypes, content logic, presentation orchestration, self-serve tuning by designers | System internals, performance-sensitive paths, third-party integration, long-lived shared code |

Selection rules:

- Prototypes and gameplay validation: use Blueprint; speed is productivity.
- Performance-sensitive and system layers: use C++; settle the stable skeleton and expose tunable parameters and extension events to Blueprint.
- Mixing is the norm: C++ defines classes and parameters, Blueprint handles subclasses and configuration; change behavior in C++, tune numbers in Blueprint data.
- Write the boundary into team convention: per-frame logic and heavy work inside loops stay out of Blueprint; agree a separate review method for Blueprint assets (§2.3).

### 4.3 Materials and Niagara: Artist-Driven, Performance-Sensitive Assets

- The material system defines how a surface responds to lighting (base color, roughness, metalness and other PBR inputs) with a node graph; it is where the visual style is mainly implemented.
- Master materials and material instances divide the work: the master builds the skeleton and leaves parameter switches, while individual assets tune parameters through instances and share the compiled result; duplicating a master material per asset magnifies shader count and maintenance surface together.
- Niagara is the particle and effects system: node-based authoring, CPU or GPU simulation selectable, with parameters exposed for artists to tune directly on the asset.
- Both share one identity — "artist-driven, performance-sensitive assets": easy to build in the editor, and cost scales at runtime with count, area and complexity. Convention before tricks: instancing, per-platform effect quality tiers, material complexity on the budget (§5).

### 4.4 System Idioms Checklist

Against the cross-engine checklist in Programming Handbook §2, here is where each system lands in Unreal terms:

- **Input**: layer logical actions over physical keys; keep input buffering and state machines inside character logic; leave key remapping to the engine's input system (Programming Handbook §2.1).
- **UI**: use the engine's built-in widget system (UMG); separate data from view, and fast-changing elements from static ones.
- **Saves**: store state, not object references; version them with migrations; write to a temp file first, then replace (Programming Handbook §2.4).
- **Object pooling**: pool objects that spawn and die frequently (bullets, effects, pickups); don't rebuild pooling for types the engine already pools.
- **Camera**: follow and screen-shake parameters per (Programming Handbook §2.3); manage cutscene and gameplay cameras together so they don't fight for control.
- **Networking**: the engine ships a replication framework and a server-authoritative model; write single-player projects the same way and more of the work carries over to multiplayer (Programming Handbook §5).

## 5. Performance and Optimization

The methodology follows Programming Handbook §3: set budgets first, measure before changing, on-device beats in-editor. Hotspots in Unreal projects cluster in five places:

| Hotspot | Symptom | Countermeasure |
| --- | --- | --- |
| All rendering features on | High-spec features stack up and kill both frame rate and VRAM | Enable per target platform in tiers (virtualized geometry and dynamic global illumination each have their own cost model); control resolution and scene complexity |
| GPU submission and overdraw | Frame drops where transparency and particles stack | Control transparent area and particle density; instantiate materials to cut state changes |
| Blueprint per-frame overhead | Many Blueprint objects each executing every frame | Replace polling with event-driven logic, move heavy logic to C++, drive similar objects together |
| Shader compilation | Long waits after material edits; a bulk compile before packaging | Manage master materials with freeze periods, batch changes, count compile time in the CI budget |
| Memory and loading | High-resolution assets and big worlds drag loading down | Async loading and streaming; asset specs and compression per platform; VRAM on the budget sheet |

- Measurement toolchain: the engine's profiling suite (Insights) for frames and tasks, GPU capture tools to find the real culprit in the render pipeline, platform tools for on-device confirmation. Editor numbers often lie; conclusions come from packaged builds and target devices.
- Budget sheets: split the frame budget by target frame rate across logic, rendering, physics and UI; memory and VRAM budgets per platform; build size budgets per channel (Programming Handbook §3.1).
- Optimization discipline: change one variable at a time; record data from the same scene and the same path before and after; no optimization without measurement.

## 6. Learning Path

Four stages by output; each stage's milestone is something you have built:

1. **Engine fundamentals (on the order of 2-4 weeks)**: editor operations, levels and Actors, materials and Blueprint basics. Build two small things: a playable prototype adapted from an official template, and a small level with UI and saving.
2. **Gameplay and Blueprint (on the order of 1-2 months)**: use each role from §4.1 in turn (custom rules, respawn, match state), then complete a full gameplay prototype in Blueprint; implement the systems from §2 at minimal scale.
3. **C++ and hybrid mode (on the order of 1-2 months)**: start from a small system built as "a C++ base class plus Blueprint subclasses" and get familiar with the temper of compiling, debugging and hot reload; to go deeper into the engine afterwards, take the Engine Internals Path.
4. **A complete project**: enter the Production Handbook's process, take version control, CI builds and packaging all the way, and go through one full release.

Learning discipline: the official documentation and learning portal are the authority on concepts and behavior; tutorials lagging behind engine iterations is the norm, so the official source wins disagreements; demo-grade visuals are not project-grade content cost — judge your ability by finishing a vertical slice.

## 7. Common Pitfalls

1. **Blueprint bloat**: one Blueprint piles up hundreds of nodes until nobody dares to change it and no one can review it, while per-frame logic quietly eats frames. Draw the boundary between systems and content early (§4.2): logic goes into C++ and components, Blueprint does configuration and orchestration.
2. **Runaway C++ compile loops**: a change to one header triggers a wide rebuild, iteration degrades into "batch changes, then compile", and feedback slows down. Countermeasures in §3.3: split modules, converge dependencies, put stable systems in C++.
3. **Naming and directory drift**: without prefix and directory conventions, finding assets relies on memory; casual renames and moves create broken references and Redirector debris. Set the rules on day one (§2.2).
4. **The wrong engine for a personal project**: a two- or three-person, gameplay-driven project picks the engine with the heaviest content cost, and the schedule gets eaten by engine complexity and art specs. Choose by project profile (§1), not by visual demos.
5. **Importing marketplace assets wholesale**: you inherit unused dependencies, inconsistent specs and the pack's own directory structure. Isolate and evaluate first, take only what you need, and reformat imports to project conventions.
6. **Managing version control like a pure-code project**: binary assets treated as text, cache directories committed, large files pushed through ordinary commits — once size and conflicts explode, walking it back is hard (§2.3).
7. **Copying materials instead of instancing them**: duplicating the master material per asset multiplies shader count and maintenance surface (§4.3).
8. **Judging performance only in the editor**: the editor runs smooth while the packaged build and real device differ widely; performance conclusions come only from packaged builds and target devices (§5).
9. **Everyone on their own engine version**: assets become mutually incompatible and people overwrite each other on site; unify the version and schedule upgrades for separate validation (§2.1).

## Further Reading

- [Programming Handbook](../../fundamentals/programming/README.md): architecture choices, core systems, performance methodology and engineering infrastructure — the drafting base for §4 and §5 of this page.
- [Art & Audio Handbook](../../fundamentals/art-audio/README.md): asset specs and the art pipeline, connecting to §2.2 and §4.3 here.
- [Production Handbook](../../fundamentals/production/README.md): phase models and scope control; the entry point for the complete-project stage in §6.
- [Multi-platform Launch Playbook](../../../playbooks/platform-launch/README.md): release flows and platform integration details for PC and console.
- [Engine Internals Path](../../fundamentals/engine-internals/README.md): the roadmap for going deeper into the engine, connecting to the third stage of §6.
- [Engine Track Index](../README.md): an overview of all 12 tracks.
- Unreal official documentation and learning portal: the authority on concepts and behavior; this page's judgments evolve with engine iterations, so defer to the official docs and your profiling tools.
