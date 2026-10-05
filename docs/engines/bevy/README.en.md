# Ludo Atlas · Engine Tracks · Bevy (Rust)

> **Engine Tracks**. Positioning: a data-driven ECS engine written in Rust; one of the best samples for learning modern architecture, with production readiness still growing.
> Companion handbooks: Programming Handbook (architecture choices and performance methodology) · Production Handbook (scope and scheduling) · Indie Survival (long-term technical investment) · AI Workflows (review boundaries for generated code).
> Principle: no code and no version numbers on this page; interfaces and configuration details change fast — defer to the official documentation, migration guides and your profiler.

---

## 1. Positioning and Selection

In one sentence: Bevy is an **open-source Rust game engine built on ECS (Entity-Component-System)**, with data-driven design as its first principle; Rust's type system and ownership model are its foundation.

Three reasons to pick it:

1. **Learning value**: ECS, data locality, scheduler parallelism, plugin architecture — the common themes of modern engines are the main path in Bevy, not an elective. Work through them once, and architecture questions turn transparent when you look back at other engines.
2. **Tool-oriented delivery**: Rust's reliability (no GC, memory and concurrency safety) suits simulations, visualizations, editor tools, and long-running simulations and services.
3. **Long-term technical investment**: language and engine share one capital base (type system, package management, testing), and the Rust you learn pays off outside the engine too.

The costs are just as clear:

| Dimension | Current state | What it means for you |
| --- | --- | --- |
| Engineering maturity | In a fast-iteration phase; APIs still evolving | Every upgrade may bring migration work — budget a slice for it up front |
| Toolchain experience | No mature all-in-one official editor | Scene building and tuning rely mainly on code and third-party tools |
| Ecosystem depth | The core is officially maintained; the rest comes from the community | Niche needs mean building it yourself or waiting; don't skip the evaluation period |
| Platform support | Desktop is fairly smooth; mobile and web lag in maturity | Run a small experiment before committing to a specific platform — don't find out right before release |

A fit for: people who want to learn modern engine architecture; small-scale projects with clear rules, simulation-oriented or tool-oriented; teams willing to treat keeping up with versions as daily homework. Not a fit for: large teams on hard deadlines; projects that lean heavily on visual editing and commercial middleware; projects with a hard console-certification deadline and no budget for trial and error.

Self-check: is the heaviest part of your project "many entities, dense rules" or "lots of content, heavy art"? The first is the comfort zone; for the second, check whether the ecosystem can catch it. One hard bar: someone on the team must be able to read compiler errors and find answers in English-language material.

## 2. Ecosystem and Project Structure

### 2.1 Toolchain: cargo Is the Workbench

Bevy is a library (crate) in the Rust ecosystem; the workbench is the Rust toolchain itself, and on the editor side rust-analyzer provides completions and error hints:

| Tool | What it handles | Where it sits in the dev loop |
| --- | --- | --- |
| cargo | Project setup, dependency fetching, building, testing, running | The entry point for everything |
| cargo check | Type checking only, no executable produced | The fast loop while writing code |
| cargo clippy, cargo fmt | Static checks and formatting | Run before committing; strictness carried into CI |

Suggested project layout (start as a single crate; split into a workspace once it grows):

```text
game/
├── Cargo.toml / Cargo.lock   # dependency config; commit the lockfile to the repo
├── assets/                   # runtime assets: textures, audio, scene data
└── src/                      # main.rs entry point; the rest split into plugins by domain
```

One easily overlooked configuration discipline: in the dev build, enable optimization for dependencies while keeping debug information for your own code. Otherwise ECS code runs slowly enough under a debug build to mislead your judgment, and you end up designing on false performance intuition.

### 2.2 The Plugin System

Plugins are this engine's unit of organization:

- One feature, one plugin. Rendering, input, audio, windowing and the rest come as official plugins, and the default plugin group assembles them into a working app out of the box; the plugins you write for gameplay, saves and UI sit alongside them.
- A plugin is the registration point: systems, resources, events, states and asset loaders all attach during plugin construction. Project organization therefore turns into a question of "which plugins, and who depends on whom" — the same source as the module-boundary heuristics in Programming Handbook §1.

### 2.3 crate Ecosystem Map

| Need | Representative options | Notes |
| --- | --- | --- |
| Physics | The Rapier integrations, the Avian family | 2D and 3D are separate; verify before integrating |
| Immediate-mode UI and debugging | The egui integrations, inspector-style crates | Great for tuning during development; production UI is a separate discussion |
| Networking | A number of community multiplayer crates | Maturity varies; start with a minimal latency experiment |
| Tilemaps and level data | Community crates plus your own parsing | Align with your editor's output format |

The ecosystem's true shape: the core (rendering, input, assets, UI, audio) is officially maintained and stable in quality; long-tail needs (platform-specific SDKs, commercial middleware, visual editors) come from the community or from you. When picking a crate, look at three things: whether it tracks the latest engine version, how fast issues get responses, and its license. At selection time, write down one sentence naming who will pick up the long-tail capability; if you can't write it, don't promise it.

### 2.4 Keeping Pace with Versions

Read the release notes (migration guides) before upgrading, then touch the dependency list; an upgrade is a separate, revertible commit; commit the lockfile so every machine and every CI build resolves the same dependency set:

- Third-party crates are tightly coupled to the engine version: before upgrading, confirm the key crates have followed; if not, wait, or accept the cost of maintaining them yourself.
- Suggested upgrade flow: separate branch → bump dependencies → fix compile errors one by one → run tests and smoke checks → watch for runtime behavior differences (rendering and scheduling changes don't necessarily fail compilation).

## 3. Core Workflows

### 3.1 The Birth of a Feature

`define data → write systems → register plugins → run and observe → tune and regression-test`

- Define data: which components does this feature need? Write "what it is" as data.
- Write systems: which logic reads which components and writes which ones? Write "how it changes" as functions.
- Register plugins: systems, resources and events are registered in a plugin, with ordering expressed through the scheduler.
- Run and tune: run it and watch the diagnostic numbers and the screen — don't guess; keep parameters in one place, and run the tests and smoke checklist after changes.

### 3.2 Commands in the Dev Loop

| Command | When | Notes |
| --- | --- | --- |
| cargo check | While writing code | Fast feedback; replaces a full compile |
| cargo run | Verifying behavior | Runs on the optimized dev profile |
| cargo test | Logic regression | Logic can run as headless tests |

### 3.3 From Prototype to Release

- Prototype phase: a single crate, the default plugin group, assets straight into `assets/` — validate the core loop first.
- Growth phase: split plugins and modules by domain; extract shared types into their own crate; manage multiple crates with a workspace.
- Release phase: release builds, platform packaging, CI daily builds (the fmt/clippy/test trio plus artifacts); see Programming Handbook §6 and the release-related handbooks.
- Saves and settings: decide the serialization format on day one (text or binary) and write the version-migration function from the first version.
- Testing and debugging: use a windowless app as a fixture to run logic regressions; use diagnostics panels and inspectors to see runtime state; wire up logging and crash reporting from the prototype phase.

## 4. Key System Idioms

### 4.1 The ECS Mental Model

| Concept | In one sentence | What to remember |
| --- | --- | --- |
| Entity | An ID | Lightweight and copyable; carries no data itself |
| Component | Data attached to an entity | Smaller is better; composition produces behavior |
| System | A function that processes data | An ordinary function; its parameters declare what it reads and writes |
| Resource | Global singleton data | Settings, handles and global managers live here |
| Query | How you iterate entities | Narrow the set with filters |
| Schedule | System execution order | Stages and dependencies decide order and parallelism |

Three points on scheduler thinking:

- Inter-system **parallelism** requires no conflict: read-only systems run together, while write-read and write-write pairs must queue. Half of performance design lives here.
- Neither order nor conditions rely on guesswork: lay out input collection → logic update → presentation refresh as stages, and express ordering with explicit dependencies; express "when it runs" with run conditions rather than writing if statements inside systems.

### 4.2 Three Disciplines of Data-Driven Design

1. Components are nouns and hold no logic; behavior lives entirely in systems.
2. Composition over inheritance: for "things that burn", add a component rather than building an inheritance tree.
3. Model state with state machines (the official state facilities or your own enums), not a scatter of boolean flags.

### 4.3 Layering Systems by Frequency

| Layer | Frequency | Typical contents |
| --- | --- | --- |
| Input layer | Every frame | Collect input, translate into intents |
| Logic layer | Fixed timestep | Physics, combat resolution, simulation; fixed timing is what makes it reproducible |
| Presentation layer | Every frame | Animation driving, UI refresh, audio triggering |
| Low-frequency layer | Timers | Autosave, statistics, pathfinding recalculation |

Running logic on a fixed timestep and presentation at a variable frame rate is the foundation of reproducibility: tests, replays and future multiplayer all depend on it.

### 4.4 Events, Assets and Data Flow

- Events broadcast "something happened": when damage resolution finishes, sound, effects and logs each respond without calling one another directly; limit forwarding depth, and keep events descriptive of facts, carrying no behavior.
- Name and group assets by scene and use, not by extension; hot reloading is a strength (edit a texture and see it immediately), while code hot reload needs extra solutions — don't assume it exists.
- Model loading as a state machine: enter scene = trigger load → progress indicator → swap on completion; never load everything synchronously on the first frame.

## 5. Performance and Optimization

### 5.1 Where the Performance Edge Applies

The ECS dividend comes from data locality and parallel scheduling, and its size depends on the shape of the scenario:

| Scenario shape | Dividend | Why |
| --- | --- | --- |
| Many entities, full iteration every frame (bullet-hell patterns, particles, simulations) | Large | Similar data sits contiguously, cache hit rates are high, and systems can run in parallel |
| Few entities, complex logic (board games, narrative tools) | Small | Not enough scale for scheduling and layout gains to show |
| Many heterogeneous entities, frequent component churn | Medium | Component layout migration has a cost; design must match the access pattern |
| Tools and simulations | Medium to large | Long, stable runs and data throughput are strengths |

Conclusion: come for scale and the payoff is honest; if scale is not on your side, base the decision on architectural value and language capability, not performance.

### 5.2 Optimization Checklist

- [ ] Dev build profile: optimize dependencies, or the numbers are all noise
- [ ] Data and queries: add filters to narrow sets; use change detection to process only changed entities; keep hot data in hot components and avoid adding/removing components every frame
- [ ] Drawing: atlasing, batching, fewer state changes (matching the general checklist in Programming Handbook §3.3)
- [ ] Parallelism: read the diagnostics to locate write conflicts and blocking between systems
- [ ] Memory and loading: large assets async and streamed; bullets and effects reused
- [ ] Measure first: a frame budget sheet plus profiler recordings, archived before and after changes

### 5.3 Platform Realities

Desktop is the most complete battleground — support it first; mobile and web have working paths, but their maturity trails desktop, so run small experiments early and write the conclusions into your selection document; for support status, the official statements are the authority — old blog posts and third-hand tutorials are extremely unreliable here.

## 6. Learning Path

### 6.1 Prerequisite: Rust Itself

Three steep climbs: ownership and borrowing, lifetime annotations, and generics and traits.

- Ownership rules will force design changes: data belongs to the ECS, and systems borrow it briefly. This is naturally isomorphic to the ECS division of labor; get through the first two weeks and it flows.
- Generics and traits are the engine's foundation, not a daily necessity for game logic: read them before you write them fluently; go through the everyday pieces — serialization, error handling, iterators — before touching the engine.
- Time intuition: with experience in another language, expect two to four weeks before you can write everyday game logic; the compiler will teach you the most the first time you try to make objects reference each other.

### 6.2 A Four-Week Onboarding Plan

| Week | Content | Output |
| --- | --- | --- |
| 1 | Rust basics plus running the official examples one by one | Can modify the examples and read the errors |
| 2 | Read through the official book plus a small toy | A moving square with a status display |
| 3 | ECS refactoring exercise | The toy split into input, logic and UI plugins |
| 4 | Micro-project vertical slice | One complete loop: input → rules → win/lose → restart |

### 6.3 Going Further

1. Write regression cases for logic with renderless tests; when reading engine source, follow the Bevy route in the Engine Internals Path.
2. Build a tool-oriented project (a viewer, a simulator, a format converter) and feel Rust's delivery quality.
3. Go all the way to release: desktop packaging, CI, store flows — entry points in Programming Handbook §6 and the release-related handbooks.

## 7. Common Pitfalls

1. **Fighting the borrow checker head-on**: write the game as "objects referencing each other" and the compiler blocks you every day. If you can't beat it, join data-oriented design: components don't hold one another, and systems communicate through queries and events.
2. **Taking debug builds as truth**: being an order of magnitude slower is normal; judging performance direction from them is wrong across the board (§5.2).
3. **Stale docs and tutorials**: APIs evolve fast, and old syntax fails to compile in droves. Defer to the official examples and migration guides; check publication dates on community posts.
4. **Underestimating ecosystem gaps**: the editor, middleware or platform integration you want may have no ready-made solution. Time spent "waiting for a crate" has to go into the schedule.
5. **Going to production blindly and upgrading in big leaps**: APIs change, the toolchain is still filling in, and platform support is uneven; a big cross-version upgrade stacks migration guides on top of each other. Sign keeping up with versions into the budget as a long-term cost, upgrade in small steps, and keep every step revertible.
6. **Stretching ECS beyond its problem**: forcing UI state and static configuration into ECS only takes the long way around. Keep the boundary clear: let ECS manage the sea of entities, not the whole program.
7. **Missing tests**: "games can't be tested" is an excuse; renderless tests happen to be an ECS strength, and every step you put it off adds a pitfall.
8. **Magic numbers scattered around**: parameters hide inside systems, so tuning means editing code and recompiling. A central parameter table and a runtime inspector — do these two first.
9. **Treating examples as architecture blueprints**: examples are written minimal for demonstration, while production demands split plugins, domain separation and asset management. Tutorials are a starting point, not a blueprint.

## Further Reading

- [Engine Internals Path](../../fundamentals/engine-internals/README.md): Route B is Bevy, connecting to §6.3 here.
- [Engine Tracks Overview](../README.md): positioning comparison across the 12 tracks and this page's place among them.
- Programming Handbook: §1 architecture choices, §2 core systems, §3 performance methodology — referenced throughout this page.
- Indie Survival: the ledger that counts keeping up with versions and ecosystem gaps as long-term costs.
- AI Workflows: review boundaries for generated Rust code — a passing compile is no substitute for reviewing logic; for the official resource index, see Resources and the repo's `catalog/`.
