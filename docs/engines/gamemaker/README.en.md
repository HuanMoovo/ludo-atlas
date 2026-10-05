# Ludo Atlas · Engine Tracks · GameMaker

> **Engine Tracks**. Positioning: a rapid-development engine born for 2D — GML scripting plus visual blocks press the learning threshold to its lowest, and the prototype-to-launch path for pixel art and small-scope 2D is extremely short.
> Companions: Programming Handbook · Game Design Handbook · Multi-platform Launch Playbook · Indie Survival.

---

## 1. Positioning and Choice

GameMaker is a commercial engine with 2D written into its genes: rooms, objects and events — the three-piece set — are all organized around 2D games, and the scripting language GML has simple syntax and a complete manual; without writing any code at all, visual blocks can build complete playable works, migrating to code whenever you like. Well-known indie titles such as Undertale and Hotline Miami came from this track.

The license model defines the boundary of use: the free tier serves learning and non-commercial use, with limited features and release scope; commercial release requires a purchased license, with tiers and platform coverage (consoles included) per the official terms. The engine is closed source and steered by a single company — product direction and license policy are not subject to community votes.

### Who it fits

- People making small-scope 2D and pixel-art projects: the fastest class from prototype to finished work — an evergreen choice for indie developers and small teams.
- Beginners with no programming experience: the gradual path from blocks to GML is gentle, and the tutorial ecosystem is video-heavy and dense.
- Game jams and prototypes needing fast gameplay validation: the editor responds fast; a playable screen is hours away.
- Systems- and gameplay-minded designers: the built-in sprite editor, room editor and tile maps press the cost of "making one level" very low.

### Who it does not fit

- 3D projects: 3D capability exists but is not its battlefield — heavy 3D should not start from this track.
- Teams depending on open source and modifiable engine code: the engine is closed; engine-level problems mean waiting on the vendor or routing around.
- Projects leaning heavily on commercial plugins and middleware: the ecosystem runs a notch smaller than Unity's — verify critical capabilities before choosing.
- Projects unwilling to pay for a license: commercial release requires purchase — this bill belongs on the table at step one of selection.

### Against Godot and Unity

| Dimension | GameMaker | Godot | Unity |
| --- | --- | --- | --- |
| Positioning | 2D-focused | 2D/3D all-rounder | Commercial all-rounder |
| Language | GML, with visual blocks alongside | GDScript / C# | C# |
| License | Free tier limited; commercial release needs a license | No strings attached | A personal free tier exists; terms per the official page |
| Time to productivity | The fastest class | Fast | Medium |
| 2D workflow | Sprites, rooms and tile maps out of the box, pixel-friendly | 2D is a first-class citizen | Mature toolchain, heavier engineering |
| 3D | Not suitable as a mainline | Usable for mid-scale | Strong |
| Export platforms | Desktop, mobile, Web, consoles (within licensed tiers) | Desktop, mobile, Web; consoles need third-party porting | All platforms, terms per the official page |
| Ecosystem | Small and concentrated, mostly video tutorials | Medium, excellent official docs | The largest |
| Source | Closed | Open | Closed |

The trade-off in one line: for small-scope 2D and the fastest route to a playable screen, put GameMaker in the first evaluation round; if the plan grows toward 3D or heavy engineering, return to the Godot and Unity tracks.

## 2. Ecosystem and Project Structure

A GameMaker project looks more like an asset library: beyond one project file, sprites, objects, rooms, scripts, sounds, fonts and shaders each live in typed directories, with references managed centrally by the IDE. Rename and move assets inside the IDE — renaming by hand at the filesystem level severs the reference chain outright.

### 2.1 Directories and asset classes

| Asset type | Content | Usage notes |
| --- | --- | --- |
| Sprites | Images and animation frames | The built-in editor crops frames on import; frame order and origin placement directly shape game feel |
| Objects | Logic units | Everything that acts in the game is born here |
| Rooms | Runtime containers and levels | The game entry is a room; title, menus and levels are all rooms |
| Scripts | Reusable logic | Where logic goes once it leaves object events; split files by system |
| Sounds, fonts, shaders | Presentation-layer assets | Bring in as needed; mind format differences across platforms |

Project files are text formats — friendlier to Git than pure binary projects; but parallel edits to one asset still conflict, so collaboration relies on splitting assets small and staggering edits (version-control methods in the Programming Handbook §6).

### 2.2 The ecosystem's boundaries

- The official manual is high quality and comprehensive — the only authority; the tutorial ecosystem is mostly videos and community projects with wide version spreads, so budget for filtering.
- Extension packs and the asset store offer platform extensions and art assets at a notch below the Unity store in scale; check maintenance status and license terms before buying, and verify commercial scope line by line.
- The engine is closed and run by one company: platform support and license policy move at the vendor's discretion; this is a risk selection cannot hedge on your own — keep fallback plans for important needs.

### 2.3 Self-check questions

If you tick two or more among 3D, heavy engineering, and "must read source to modify the engine", go back to the Engine Selection Guide and re-evaluate; and if you cannot take the fast rhythm of small-scope 2D, this track is the wrong pick.

## 3. Core Workflows

### 3.1 From zero to running

1. Install the IDE and create a project: start from the blank template; keep the sample projects for reference.
2. Import assets: drag images into the IDE, crop frames and set origins in the built-in editor.
3. Create objects, write events: behavior logic goes into events; get it running with visual blocks first, then migrate gradually to GML.
4. Create rooms, place instances: place objects into rooms — a room is the smallest runnable unit.
5. Run and debug: run straight from the IDE; get familiar with the debugger's breakpoints, frame stepping and variable watches first.
6. Wire up version control: project and assets into the repository, caches and build outputs into the ignore list.
7. Configure target platforms and build: desktop first, mobile and Web verified one by one, consoles applied for within licensed tiers.

### 3.2 The event model: where the code goes

- All of an object's behavior hangs on events: create, destroy, step (begin, regular, end), draw (world, GUI layer), alarms, collisions and async callbacks.
- Event types and execution order are the engine's skeleton: within one object, step runs before draw, and different objects execute in instance processing order. When hunting a bug, confirm order assumptions before suspecting logic.
- Put logic in the right event: initialization in create, state updates in step, presentation only in draw; stuffing gameplay rules into the draw event is the classic structural accident.
- Async events receive platform callbacks (saves, network, IAP and more); callbacks complete at a definite time — never assume they return immediately.

### 3.3 Export and multi-platform

| Target | Path | Notes |
| --- | --- | --- |
| Desktop | Build executables directly | The smoothest route; distribution and store integration per the Multi-platform Launch Playbook |
| Mobile | Platform toolchains must be configured | iOS builds depend on a macOS environment — non-Mac teams should plan ahead |
| Web | Export a web build | The browser environment has many constraints; memory and audio strategy need real-device verification |
| Consoles | Provided within licensed tiers | Dev-kit applications and certification follow vendor channels — budget the schedule early |

Builds support scripted invocation and can wire into automation for daily builds; the infrastructure checklist is in the Programming Handbook §6.

## 4. Idioms for Key Systems

### 4.1 The three-piece mental model

- Rooms are the stage, objects are the actors, events are the lines: rooms answer "where", objects answer "who", events answer "what happens when".
- One object carries one kind of instance logic: a bullet object handles flight and hits only; pickup logic belongs to the pickup object.
- Object inheritance expresses true kind-relations (a family of enemies sharing base behavior) — never use it to scrape together reuse; prefer composition and script functions.
- Instances are an object's concrete presence in a room: one object can be placed many times, each instance holding its own variables — do not rewrite instance state into global state.

### 4.2 Code organization discipline

- Keep event windows thin: each event holds only calls, with logic sunk into script resources split by system.
- Variable scope comes in three layers: local, instance, global. Prefer local over instance, instance over global.
- Prefix names by asset type (objects, sprites, rooms, scripts each get one), or search and filtering stop working.
- Manage magic numbers centrally: values live in data files or a constants script — never scattered through event windows.

### 4.3 Drawing and cameras: getting 2D right

- For pixel art, align three things first: texture interpolation off, integer scaling, rounded camera follow — or the screen blurs and shakes.
- Cameras (views) are configured in rooms or controlled at runtime; tune follow and dead-zone logic together with character feel (methods in the Programming Handbook §2.3).
- Draw events split into world and GUI layers: the interface does not move with the camera — health bars, scores and menus draw on the GUI layer.
- Choose the animation route by asset budget: frame sequences are cheap and controllable, skeletal animation saves resources; before committing to large images or skeletons, ask whether you truly need them.

### 4.4 Data, saves and configuration

- Data-driven from day one: values, level configs and text content live in text data files — content changes without code changes.
- Saves store state, not presentation: fields carry version numbers and migration functions, so later structure changes do not mean rework.
- The built-in quick-save interface suits prototypes and small projects; real projects take a self-managed format for control and cross-platform consistency.

### 4.5 Extensions and dependencies

- Platform extensions and third-party extensions come in as needed; check maintenance and licensing first, and regression-test item by item on engine upgrades.
- Never depend on a single irreplaceable extension: keep at least one fallback path for critical capabilities such as payments, ads and analytics.
- A closed engine means "wait for the vendor to fix it" can take a long while — think detours through in advance.

## 5. Performance and Optimization

The general rule holds: measure before optimizing — smooth on the dev machine does not count; target devices do (methodology in the Programming Handbook §3). GML executes on its own VM, and performance habits decide the ceiling more than language choice.

### 5.1 Four high-frequency problems

| Habit | The pathological form | The right way |
| --- | --- | --- |
| Instance management | Creating and destroying bullets and effects every frame | Object pools with activate/deactivate, reusing instances |
| Per-frame cost | Looking up objects and concatenating strings in step events | Cache references ahead, build strings ahead |
| Event weight | Every object carrying the heaviest step event | Move anything not needed each frame to alarms or conditional triggers |
| Draw calls | Scattered assets causing constant texture switches | Group assets by texture, control layer order |

### 5.2 Rendering and assets

- Texture pages are packed automatically by texture group; manage the grouping deliberately — one image landing in the wrong group multiplies batches for nothing.
- Large amounts of homogeneous visuals (particles, rain, snow, sparkles) should use the particle system, not hundreds of object instances.
- Large images and high-resolution assets dominate memory and bandwidth — prepare them tiered by target platform.

### 5.3 Platform differences

- On mobile, watch memory and heat, with low-end devices as the floor.
- Verify Web memory and audio strategy early in the project — do not cram it in before launch.
- Testing discipline holds: real target devices, with a set of numbers recorded before and after each optimization.

## 6. Learning Path

A straight line accepted by "something made":

1. Official onboarding: walk the manual's getting-started chapters and official tutorials — the goal is a little thing that moves, collides and changes rooms.
2. The language: finish GML's core (variables, functions, arrays, structs, methods and scope), checking the manual as you write.
3. First complete work: small but whole, playable to the ending, covering movement, collision, UI, saves and audio.
4. Toolchain: use the debugger, version control and build scripts one by one; run one real test of the native compile tiers for release builds.
5. Advanced directions: shaders, sequence animation, physics and particles — chosen by project need, not by greed.
6. Release: walk one full store submission on a target platform, clearing licensing and qualification steps in advance.

Acceptance criteria (all observable):

- Without tutorials, build from an empty project to "levels, a fail condition, restart".
- When a bug appears, locate it to "which object, which event, which frame" before saying how to fix it.
- The finished work installs and runs on someone else's clean machine.

## 7. Common Pitfalls

1. **Code piled into event windows**: hundreds of lines each in create, step and draw, with reuse by copy-paste; logic belongs in scripts, events only make calls.
2. **Globals as the backpack**: all state into globals, dependencies and load order invisible; loosen scope stepwise starting from local.
3. **No version control, or caches committed**: asset metadata conflicts resist merging, and half the repository is regenerable cache; set the ignore list on day one.
4. **Casual naming**: no prefixes, chaotic casing — past a thousand assets, search is essentially broken.
5. **Hoisting old tutorials wholesale**: the engine renamed and changed license models across generations, and old tutorials' assets and methods often no longer match; the official manual is the arbiter, and imported old projects need compatibility verified item by item.
6. **Ignoring license boundaries**: shipping commercially on the free tier, or mixing platforms the license does not cover; check tier and target platforms (consoles included) before release.
7. **Unguarded performance habits**: per-frame instance churn, per-frame string building, unmanaged texture groups — all erupting on mobile; self-check against the list in §5.1 from the prototype stage.
8. **Forcing 3D or big projects onto it**: beyond the small-scope 2D positioning, the price is continuous engineering strain; go back to the Engine Selection Guide first.
9. **Unaware dependence on one ecosystem**: a closed engine steered by one company — the survival of extensions and platform support is not in your hands; keep fallbacks for critical capabilities.
10. **Not checking asset licenses**: verify commercial scope for store assets and audio line by line — do not discover at launch that a purchase cannot be used commercially.

## Further Reading

- [Programming Handbook](../../fundamentals/programming/README.md): the general version of core systems, performance methodology and engineering infrastructure — the base document cited throughout this page.
- [Game Design Handbook](../../fundamentals/game-design/README.md): design methods for deepening gameplay validated by fast prototypes.
- [Multi-platform Launch Playbook](../../../playbooks/platform-launch/README.md): desktop, mobile and Web release flows and store integration details.
- [Indie Survival](../../../playbooks/indie-survival/README.md): the math of license costs and scope control, complementing §1 here.
- [Pitfalls & Anti-patterns](../../pitfalls/README.md): high-frequency pitfalls across the pipeline — read against section 7 here.
- [Engine Tracks index](../README.md): all 12 tracks at a glance and what comes first.
