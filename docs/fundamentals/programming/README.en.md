# Ludo Atlas · Programming Handbook

> About: an engineering handbook for game programmers, covering architecture pattern selection, core system implementation essentials, performance methodology, multi-platform adaptation, networking basics, engineering infrastructure, and engine concept cross-references.
> Companions: Pitfalls & Anti-patterns (Programming & Architecture section) · Production Handbook · Resources (tools & courses) · `docs/engines/` (12 Engine Tracks).
> Principle: this handbook offers "selection judgment and checklists"; concrete code implementation varies with the engine ecosystem — take the official documentation and your profiler as the authority.

---

## 1. Architecture Pattern Selection

| Pattern | What it solves | Good for | Avoid |
| --- | --- | --- | --- |
| Finite state machine (FSM) | Behavior switching for a single object | Character control, UI flows, boss phases | State explosion (upgrade when >10 states) |
| Hierarchical state machine (HFSM) | Reusing states by grouping them | Complex characters (layered movement/combat/hit reactions) | Over-engineering small projects |
| Behavior tree (BT) | Composable AI decisions | Enemy AI, NPC behavior | Cases that change dynamically and often (editing the tree is expensive) |
| GOAP / utility AI | Goal-driven dynamic planning | NPCs in sandbox/simulation games | Projects that rank expressiveness first (choice costs are high) |
| ECS | Data locality, massive entity counts | Simulations, bullet-hell, large worlds | Small projects (boilerplate cost > payoff) |
| Event-driven / signals | Decoupling modules | Achievements, UI notifications, sound triggers | Event chains so long nobody understands them (cap the nesting) |
| Command pattern | Input recording / replay / undo | Replays, undo, networked input streams | Pure added abstraction when you have no replay needs |
| Data-driven / asset pipeline | Non-programmers tuning values/content | Every project in mass production | Fake data-driven workflows without tooling (nobody maintains the tables) |

**Selection heuristics**: choose by "current team size × rate of change"; clear module boundaries matter more than an advanced pattern; before adding a layer of abstraction, ask which three duplications it removes.

## 2. Core System Implementation Essentials (Cross-engine Checklist)

### 2.1 Input System

- Action mapping layer (logical action `Jump` ↔ physical button), providing the basis for key remapping and multiple devices.
- **Input buffering**: buffer jump/attack inputs for 100-200 ms; **combo inputs** (double-tap dash) must guard against accidental triggers.
- Decouple input from frames: collect in Update, execute in the physics step; record input streams (for replays / test automation).

### 2.2 Character Control

- Separate the parameters: max speed / acceleration / deceleration / air control / gravity (ascent and descent kept apart); these are the core knobs of game-feel tuning.
- Jump forgiveness: coyote time of 80-150 ms + input pre-buffering; use ray/shape casts rather than pure collision events for landing checks (prevents tunneling).
- Model as a state machine (Idle/Move/Jump/Fall/Attack/Hit…), with debounced transitions (priority + lock windows).

### 2.3 Camera System

- Follow: target point + look-ahead (offset toward the movement direction); **dead zone** (small movements don't move the camera); smoothing (exponential approach > spring > hand-tuned interpolation).
- Bounds and interiors: camera constraint volumes, room transitions; zoom (pull back in combat, pull in for exploration).
- Screen shake: positional/rotational/scale types, with clamping rules when stacking; a disable option is mandatory (accessibility).
- **The camera is a "second player"** — its experience ranks second only to character control.

### 2.4 Save System

- Structure: version number + data blocks + checksum; **store state, never object references**; serialize with the engine-recommended format (JSON or binary depending on size).
- **Version migration**: write a migration function every time you change the save structure (chained v1→v2→v3); before launch, test the "old save → new version" path (see the save-file pitfall in Pitfalls & Anti-patterns).
- Atomic writes: write a temp file first, then replace it, so an interrupted write can't corrupt the save; cloud saves need a conflict-merge strategy (timestamps / manual choice).

### 2.5 Object Pooling & Instantiation

- Anything created and destroyed at high frequency (bullets / effects / enemies) always goes through a pool; prewarm to peak counts; define the pool-overflow policy explicitly (reject / grow / degrade).

### 2.6 UI Architecture

- Separate view from data (passive view); navigation stack management (back key / gamepad B button); popup priority and input-consumption rules.
- Multiple resolutions: anchors + safe areas + scaling strategy (see §4); test text overflow early (multilingual length +30%).

### 2.7 Audio System (Programmer's View)

- Playback buses: Master → BGM/SFX/Voice/UI groups; group volumes are independently adjustable.
- Make the playback API event-based (`PlayEvent("hit_metal")` rather than shoving files in directly); concurrency caps and priorities (important SFX don't get drowned out).
- Pooling and streaming: short SFX cached in memory, long music streamed; randomization (pitch / material variants) to prevent the broken-record feel.

### 2.8 Localization System

- Externalize strings as key-value pairs (never hard-code visible text); support plural/gender/word-order placeholders; a font fallback chain (CJK/Latin/emoji).
- Flexible layout: let text areas expand; pseudo-localization (pseudolanguage testing) surfaces layout problems early.

### 2.9 Time and Updates

- Fixed-timestep physics + variable render frames; drive logic with delta time or a fixed tick (be careful with variable delta in networked games).
- Global pause system: manage it from a single pause source (time scaling must also handle audio / animation / particles).

### 2.10 Random Numbers

- Route all randomness through a controllable seed (so debugging is reproducible); avoid using the global RNG directly; when network sync needs deterministic randomness, use your own PRNG implementation.

## 3. Performance Engineering Methodology

### 3.1 Budgets

- Set budgets before development: frame budget (an allocation table for 16.6ms@60fps / 33ms@30fps), memory budget (per platform), package-size budget, load-time budget.
- Give every asset category a quota (texture MB, audio MB, animation file counts); warn when over budget (even better, wire it into CI).

### 3.2 Measurement Tools

| Tool | Purpose |
| --- | --- |
| Built-in engine profilers (Unity Profiler / Godot Profiler / Unreal Insights) | CPU/GPU/memory overview |
| RenderDoc / Nsight / PIX | Frame capture, GPU pipeline analysis |
| Platform tools (Xcode Instruments / Android Studio Profiler) | CPU/memory/battery on real devices |
| Cloud device farms (WeTest / Testin) | Batch testing across a device matrix |

**Principle**: no optimization without measurement; record data before and after optimizing; real devices > editor (editor numbers are often misleading).

### 3.3 Common Hotspots and Fixes

| Hotspot | Symptom | Fix |
| --- | --- | --- |
| Too many draw calls | GPU waiting, CPU busy submitting | Batching (batched rendering / atlases / merged meshes), fewer material switches |
| Overdraw | Heat and frame drops on mobile | Reduce full-screen transparency, UI-mask overuse, particle density |
| GC stalls (C#/Java) | Periodic hitches | Object pools, no per-frame allocations, struct-based data |
| Physics cost | Large numbers of rigid bodies / complex collisions | Layered collision filtering, sleeping bodies, simplified colliders, lower physics frequency |
| Load hitches | Freezes when entering a scene | Async loading, instantiating across frames, preloading strategy |
| Texture memory | OOM on mobile | Compressed formats (ASTC/ETC2), mipmaps, streaming on demand |

### 3.4 Mobile-Specific Checklist

Device tiering (low/mid/high end); thermal strategy (a plan for thermal throttling); battery (background behavior); memory headroom (defense against the OS OOM-killing your process); first-package size and download conversion (split packages / external assets).

## 4. Multi-platform & Adaptation

- **Input abstraction layer**: logical actions ↔ devices (keyboard & mouse / gamepad / touchscreen / stylus); controller prompt icons switch per device (Xbox/PS/Switch).
- **Resolution and safe areas**: UI anchor strategy (corner alignment / proportional scaling), notch safe areas, an ultrawide (21:9) and 4K support checklist.
- **Platform difference checklist**: save-path conventions, permission requests, lifecycle (suspend/resume in background), multi-user switching (consoles), reading the system language.
- **Platform capability integration**: achievements, cloud saves, leaderboards, friends, gamepad motion — tick off each item against the platform's SDK list (cross-check the Multi-platform Launch Playbook).
- **Build matrix**: Windows/macOS/Linux + consoles + iOS/Android + web; CI builds every platform at least once a day (see §6).

## 5. Networking & Multiplayer Basics (an entry-level map)

| Model | How it works | Good for | Cost |
| --- | --- | --- | --- |
| State sync (server-authoritative) | Server runs the logic; clients send input and render | Most online games | Server costs; needs prediction/interpolation to fight latency |
| Lockstep (frame sync) | Only inputs are synced; each side deterministically replays | RTS, some MOBAs | Full determinism required; reconnecting after a drop is hard |
| P2P (no server) | Players connect directly to each other | Small-scale co-op | NAT traversal is complex; cheating is hard to prevent |
| Asynchronous online | Non-real-time data exchange | Leaderboards, ghost data | Doesn't solve real-time needs |

- **Latency toolbox**: client-side prediction (simulate locally first), server rollback, interpolated rendering (smoothing out other players), lag compensation (hit rewind).
- **Server form**: dedicated servers vs match hosting (PlayFab/Photon/Tencent GSE, etc.; see Resources §8.1); rooms + matchmaking + reconnection is the minimum online feature set.
- **Anti-cheat entry point**: make critical economy and combat determinations server-authoritative; clients do presentation only; integrate an anti-cheat system (early; see Pitfalls & Anti-patterns).
- Deep dive: the Gaffer On Games networking series (Resources §3.1).

## 6. Engineering Infrastructure

| Item | Minimum practice | Advanced |
| --- | --- | --- |
| Version control | Git + Git LFS (binary assets); commit message conventions | Branching strategy (trunk + feature branches), file locking |
| CI/CD | Daily automated builds + smoke tests; downloadable artifacts | Automated packaging and upload (Steam/TestFlight), performance benchmark regression |
| Testing | Unit tests for critical logic; headless smoke runs (launch → enter scene → simulate input) | Visual regression via screenshot diffs; cloud testing across a device matrix |
| Logging & monitoring | Levelled logs + crash reporting (with symbol tables) | Live metrics dashboards (crash rate / hitch rate) |
| Documentation | README + architecture overview + ADRs (decision records) | A newcomer can get running in 30 minutes |

## 7. Code Quality & Collaboration

- **Review checklist**: does it follow the project's naming/structure conventions? Error handling and edge cases? Are performance-sensitive paths backed by measurement? Testability? License check for newly added dependencies (see the Legal, Patents & Competition)?
- **Naming and organization**: a domain glossary (consistent game terms: Enemy/Turret/Projectile), directories by domain rather than type (`combat/` over `scripts/`).
- **ADR (architecture decision record)**: one page per major technical choice (context / options / decision / consequences); six months from now, you'll thank yourself.
- **Boundaries of AI-assisted programming**: generated code must pass review and tests; core systems must be explainable; for the toolchain and permissions see design doc §14 (including the engine MCP security model).

## 8. Engine Concept Cross-Reference (Unity / Godot / Unreal)

| Concept | Unity | Godot 4 | Unreal |
| --- | --- | --- | --- |
| Object | GameObject | Node | Actor |
| Component / behavior | Component (MonoBehaviour) | Node script (_ready/_process) | Component |
| Composition container | Prefab | PackedScene | Blueprint / Level |
| Scene | Scene | Scene (tscn) | Level / Map |
| Scripting language | C# | GDScript / C# | C++ / Blueprint |
| Events / messages | UnityEvent / C# event | Signal | Delegate / Event Dispatcher |
| Coroutines / async | Coroutine / async-await | await / signals | Blueprint Delay / Async |
| Physics | PhysX / Box2D | Godot Physics (Jolt optional) | Chaos |
| UI | UGUI / UI Toolkit | Control nodes | UMG |
| Asset import | Importer settings (.meta) | .import files | Import settings |
| Packaging | Build Profiles | Export Templates | Packaging |
| Services | Unity Services | Third-party | EOS / self-hosted |

> Purpose: a translation table for cross-engine migration and for reading one engine's tutorials while working in another; for differences in detail, the official docs for each engine version are authoritative.

## 9. Learning Route & Extensions

1. Language and engine basics → build 3 small games (covering: 2D movement, physics, UI, saves).
2. Implement each system from §2 of this handbook once (a minimal playable demo per system).
3. Optimize a deliberately badly written scene with a profiler (performance-intuition training).
4. Build an online demo (the trio: rooms + sync + reconnection) to get a feel for networked thinking.
5. Full project: move into the Production Handbook, max out the engineering infrastructure (§6), and run the whole release process once.

- Courses and tools: see Resources §1-§3; engine-specific material: see `docs/engines/`.
