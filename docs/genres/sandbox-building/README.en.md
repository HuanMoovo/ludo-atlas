# Ludo Atlas · Genre Handbooks · Sandbox Building

> **Genre Handbooks · Volume 2**. Positioning: the genre that turns "building things" itself into the core gameplay. Tools are the gameplay, creations are the content and sharing is the continuation; what players build supplies the game with levels, contraptions and spectacles it could never produce on its own.
> Companions: Game Design Handbook · Programming Handbook · Modding & UGC · Indie Survival.

---

## 1. Positioning and Core Loop

In one line: sandbox building is the genre **with creation tools as its core gameplay**. It is not "a game with a building feature", but "the building tools are themselves the game": every tool the player receives is a way to play, and every creation the player makes is a piece of content.

The core loop, written as a verb chain:

`wander and survey the empty ground → place the first block → assemble a structure → discover it is not enough → tear down, rework and extend → build something that works → play with what you made → want something bigger and cleverer → (see someone else's work) back to the first block`

This genre's pacing has four tiers, each solving a different motivation: second-scale placement feedback delivers immediate satisfaction, minute-scale "build something that works" delivers a sense of achievement, hour-scale bases and contraptions deliver a sense of project, and week-scale polishing and sharing of creations delivers self-expression. All four tiers need an outlet; ship only one and players will not stay.

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Survival craft | That type organizes building around survival pressure; sandbox building has no forced pressure (or it can be turned off entirely), and building and sharing are themselves the main loop |
| City builder | That type manages land and statistics at a macro scale; sandbox building manages structures and shapes at the object scale |
| Physics sandbox (toys-first) | That type's first pleasure is the interactive experiment itself; sandbox building's first pleasure is making works that persist, can be shown off and can be played with |
| Management sim | That type deals in abstract rooms and processes; sandbox building deals in the depth of the toolset in the player's hands |

A self-check question: lock all the building tools away and leave only fixed content — does the game still hold up? If the answer is "no", what you are making is sandbox building.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Free expression**: shape, size and purpose are all set by the player; the official game provides materials and rules, not standard answers.
2. **Combinatorial mastery**: with the same set of primitives, a beginner puts up a small house and a veteran builds a calculator. The sense of mastery comes from combinatorial depth, not from numbers.
3. **Creations that are seen**: creations can leave the house, be played with and receive responses; being seen is the strongest life support a creator can get.
4. **A long-term sense of project**: a world or a single creation can be worked on for weeks on end, with something new to change on every return.
5. **Immersion and focus**: in the building state there is no forced countdown, and players can dwell quietly inside it (for the layering of tension and release, see §3.5).

Benchmark titles (widely known names only; play them yourself before breaking them down):

| Title | What to learn from it |
| --- | --- |
| Minecraft | Purity of primitives and combinatorial explosion (redstone), the chunk performance system, separate Creative and Survival modes |
| Terraria | The coupling of building and combat, wiring systems, the community habit of sharing world files |
| Garry's Mod | Combinatorial gameplay out of physics constraints, the Workshop ecosystem, the floor and ceiling of toybox freedom |
| Roblox | The platform path: creation, publishing, playtesting and monetization in one chain |
| Super Mario Maker 2 | The editor as the product, share codes and a global level library, positive feedback from being played and liked |
| Dragon Quest Builders 2 | Commission-style guidance: NPCs turn "what should I build" into "your turn"; island uploads and sharing |
| The Legend of Zelda: Tears of the Kingdom | Predictable combinations of physics rules; Ultrahand is a modern sample of "few primitives, deep combinations" |
| Animal Crossing: New Horizons | Island building and display in a low-pressure environment; Dream Address-style low-friction sharing |

Negative examples are worth studying too: when an editor opens too late or a sharing outlet goes missing, community interest usually stops at the launch window. When breaking down such cases, focus on which link of the creation chain is broken.

## 3. Design Essentials

### 3.1 Tools Are the Game

In other genres the editing tools are interface; in this one the tools are the gameplay itself. The essence of the genre is **a creation platform**: the tools in the player's hands are the gameplay, and what the tools can do is what the game can be played as. How well the tools handle is the game feel: placement must feel responsive (preview and snapping visible instantly), demolition must be cheap (materials refunded, undoable), and bulk operations must be strong (box select, fill, copy, mirror).

| Tool family | Features to build | Why it is gameplay |
| --- | --- | --- |
| Place and remove | Single placement, hold-to-place chains, block picker, area delete | The operation count sets the ceiling on creation size; if it does not feel responsive, there are no large creations |
| Bulk and transforms | Box select, fill, replace, copy-paste, rotate and mirror | Efficiency tools for large projects; players use them to play the "scale" step |
| Undo and history | Undo stack, replay of the last N steps, zero cost for mistakes | Allowing experiments is the precondition of creation; people afraid of mis-removing only build the smallest houses |
| Blueprints and projections | Save templates, place projections, reuse across maps | Separating "design" from "construction" is the precondition for turning building into engineering |
| Measurement and aids | Alignment lines, counting, scale references, coordinate display | Precision is the demand of advanced creations and the bragging language of the community |

Platform differences are a long-standing problem: mouse and keyboard suit precision and hotkeys, controllers need radial menus and fast cycling, and touchscreens rely on long-presses and two-finger gestures. Ship before the controller or touch scheme is polished and building retention on that platform will be visibly lower; get the tools feeling right on one platform before talking about porting.

An acceptance habit: have 3 people each build a small house and count three numbers — misplacements, undo uses, and operations from breaking ground to finishing the roof. The tools only pass if all three numbers stay below your expectations.

### 3.2 Primitives and Rules: Predictable Combinatorial Explosion

The depth of these games does not come from content volume but from **the combination space of a small number of precise primitives**. Three design laws:

- **Orthogonal**: each primitive governs one dimension only (electricity, motion, load-bearing, fluids); primitives with overlapping duties fight each other and the combination graph turns into a mess.
- **Deterministic**: the same input must give the same output. Only when physics and logic are reproducible will players push their contraptions toward precision; a simulation that works only sometimes sends everyone back to the most conservative builds.
- **Observable**: the state of every primitive must be visible (lit or unlit, open or closed, flowing); players learn the rules with their eyes, not from a manual.

Combinations grow out of "obvious uses": every component needs at least one basic use everyone understands and two or three advanced uses that take some thought. The table below is a self-check tool for the design phase:

| Primitive | Obvious use | Advanced combinations (examples) |
| --- | --- | --- |
| Circuit components (switches, delays, pulses) | Turning a light on and off | Automatic doors, traps, combination locks, timers, logic gates chained into a calculator |
| Motion components (pistons, axles, thrusters) | Building an elevator | Moving machines, aircraft, assembly lines, trap mazes |
| Fluids and gravity (water, sand, gravity blocks) | Decorative ponds | Waterworks, transport canals, traps, buoyancy mechanisms |
| Load and structure | Building a bridge | Suspension cables, arches, collapsible arenas, integrated bases |
| Sensors (pressure, light, coordinates) | Automatic lights | Fully automated farms, challenge levels, unmanned vehicles |

Test combinatorial depth regularly: with every new primitive, brainstorm all pairwise combinations with the existing ones and pick the 3 most interesting to implement as official templates (§3.3). Rules must also stay restrained: writing a special case for every situation shatters the combination space into patches, and players can neither learn it all nor trust it.

### 3.3 Guidance Design: From Blank Slate to First Creation

The biggest enemy of newcomers in this genre is not difficulty but the blank slate: facing open wilderness or a blank page, most people react with "I don't know what to build". Guidance has to answer "what to build", not "how to build" (that is the tools' and the tutorial's job). Five instruments, used together:

| Instrument | What to do | What it solves |
| --- | --- | --- |
| Inspiration trigger | Show possibility right at the start: a wall of featured creations, a sketch inside a letter, visible in-game signs of "what others have built" | Blank-slate fear on first entering the game |
| Templates and blueprints | Half-finished frames, unlockable blueprints, structure projections; give the starting point and skeleton, never the finished product | Players who are new but want to build big; doubles as official style guidance |
| Commissions and goals | Specific commissions from NPCs or the system: build a room, repair a bridge, light up an area | Turns "freedom" into "your turn" — the starter for a newcomer's creativity |
| Achievements and challenges | Achievements that introduce mechanics one by one: first wiring, first working contraption, first upload | Turns "try every mechanic once" into visible progress |
| Community showcase | A creations entrance on the main menu, weekly features, themed build events | Gives returning players a reason and creators a goal |

Two disciplines. First, guidance gives feedback rather than answers: blueprints sketch only the skeleton and leave completion to the player; automatic building is reserved for teaching demos and never enters the real toolset. Second, the first 30 minutes must let players build "something of their own that works" — a vegetable patch or a small bridge will do; a newcomer who spends an evening copying official creations will not come back the next day.

### 3.4 Sharing Mechanisms: Creations Must Leave the House

The lifespan of a building game is proportional to how much its creations circulate: a creation that gets seen brings the next creation, and one playtest brings one player back. Sharing design picks the unit first, then the channel:

| Sharing unit | Examples | Reach and cost |
| --- | --- | --- |
| A single creation or blueprint | Share codes, strings, small files | Fastest and lightest to spread; suits contraptions, buildings, small levels |
| A whole world | Save files, seed numbers | Medium reach; suits large saves and survival worlds, with file size as the barrier |
| Level and creation libraries | In-game upload, search, playtesting, likes | The heaviest and most effective; needs servers, recommendation slots and moderation (the Mario Maker route) |
| Platform workshops | Steam Workshop, mod.io | Reuses platform infrastructure and user habits; suits PC and cross-platform |

For a creation to "leave the house" it must pass three gates: **export** (one click produces a transferable format, with a dependency list and version number), **display** (browsing, search, playtesting, ratings — good works must be findable), and **response** (likes, comments, play counts, featured recommendations, so the author knows someone played it). Miss any one gate and creative enthusiasm dies out within weeks.

Three baselines for community operations: features and recommendations need a rhythm (weekly themes, official reshares, creator leaderboards); derivative works must be allowed and credited (tearing down and reworking someone else's creation is the healthiest loop in this kind of community); and moderation and reporting must be transparent (delisting criteria and an appeal channel, with compliance costs budgeted according to platform scale). Support tiers, Workshop version control, the mod.io cross-platform route and community legal terms are fully expanded in Modding & UGC; in-game creations are lighter than code-level mods, but the costs of moderation, recommendation slots and version compatibility are just as real.

### 3.5 Scale Management: Make Performance a Design Parameter

Players will always build big — that is a basic fact of human nature in this genre. Performance ceilings cannot wait until just before launch; they must become parameters and vocabulary in the design phase:

| Design decision | What to do | What the player is told |
| --- | --- | --- |
| Area budget | Entities and logic components have a quota per chunk or per region; exceeding it shows "load" | Not a ban — it is "there are too many machines here" |
| Soft degradation | Distant contraptions tick slower, details are culled, animations simplified | The world "dreams" in the distance and wakes up as you approach |
| Gameplay-led teaching | Official templates demonstrate performance-saving patterns like "signals instead of entities" | Turns optimization into an advanced technique that veterans show off with |
| Hard caps | Keep them only where they prevent crashes (total entity count, per-cell stacking) | Write the caps into the store page and tutorial to avoid arguments later |

For pacing design, tension (timed challenges, commission deadlines) and release (goalless sandbox) must be delivered in layers: the pressure of Survival and Challenge modes pulls people back, and the no-pressure of Creative mode keeps them around. With tension only, casual creators churn; with release only, there is no reason to return. Multiplayer spaces must also be defined in advance: visitor permissions (view-only, playable, editable), conflict handling for cooperative building, and isolation so that "someone else's creation does not wreck my framerate"; for the engineering path see Multiplayer & Backend.

## 4. Technical Essentials

The engineering brief in one line: **player creativity has no ceiling, the performance budget does; the entire job of systems design is to weld those two things together**. The difficulty is not in gameplay code but in world representation, simulation scheduling and the lifecycle management of user content.

**World representation and rendering**

- Three routes: voxels (the Minecraft way, a grid of blocks), modular parts (prefabs combined at snap points) and free physics (the Garry's Mod way, arbitrary rigid bodies and constraints). Voxels suit large-scale terrain and vast worlds, modular parts suit architectural precision, and free physics suits contraptions and vehicles; the choice decides the rendering, collision and save pipelines, and switching routes midway is a rewrite.
- The voxel route requires chunk management and mesh merging: generate merged meshes per chunk, with visible-face culling and graded render distance; any approach of "one object per block" collapses on the first large building.
- Lighting is the hidden cost center of voxel games: propagate light with a queue-based flood fill and amortize day-night and light-source updates across frames — never recompute everything in the same frame as a placement.
- Community creations are the test cases: freeze the ten most complex works in the creation library into regression tests and, after every change, run their loading and framerate. This is more real than any synthetic benchmark.

**Simulation and scheduling**

- Drive logic on a fixed tick (commonly 10–30 Hz) and render with interpolation; event order within a tick must be deterministic for contraptions to be reproducible.
- Allocate the tick budget by region: one budget bucket per chunk, with over-budget contraptions slowed down or put to sleep (idle machines do not tick, full chests are not polled), turning "the more you build, the slower it gets" into "the more you build, the more the distance saves".
- Entities are another black hole: merge dropped items into stacks and auto-despawn them, downgrade NPC and creature simulation by distance (for simulation LOD methods see the Programming Handbook), and rate-limit high-frequency components such as conveyor belts and assembly lines.
- Dangerous combinations need defenses ahead of time: large-scale fluid spread, chain explosions, full-scene light recomputation and recursive circuits are all things the community will certainly build; give every system a "worst-case budget" and write it as an automated test.

**User content lifecycle**

- Saves and export: worlds use incremental storage with dirty-chunk flags; exported single creations use "local coordinates + dependency list + format version", and imports validate size and reference legality. Give the format a version number and migration functions from day one — old creations must open after a game update.
- Import safety: treat player creation files as foreign data — limit size, validate references, reject unknown instructions; in-game creations execute no code and stay isolated from code-level mods.
- Online building: server-authoritative, with operations broadcast as events (placement, removal, transform), conflicts avoided through room or chunk partitioning, and deletions and rollbacks always undoable; players joining mid-session first receive a chunk snapshot — the full path is in Multiplayer & Backend.
- Toolchain: the undo stack and blueprint system are hard requirements on the player side, and a performance inspector (letting authors see the load cost of each creation) is the guardrail on the community side; both must appear in the first version of the tools — adding them later equals redoing the tools.

## 5. Content Volume and Workload Reference

This genre spans an extremely wide range: a playable tool prototype takes three weeks, while a platform-level product is a ten-year engineering effort. The following are common magnitudes, for estimating scope only — not a commitment:

| Project form | Scale | Time reference | Notes |
| --- | --- | --- | --- |
| Tool prototype | One flat plot, place/remove/save-load | 3–6 weeks | Zero art; validates only tool feel and the urge to build |
| Small complete title | One world, one parts set, local sharing | 6–18 months | Solo or 2–3 people, with a low-cost art style |
| Typical commercial scope | Multiple themes, online, UGC platform | 2–4 years | Performance polish and community features eat a substantial share |
| Platform product | Editor plus creation library plus operations | 3+ years plus long-term operations | Community operations are half the product (the Mario Maker / Roblox direction) |

Magnitudes for content units:

| Content unit | Minimum shippable | Comfortable volume | Notes |
| --- | --- | --- | --- |
| Blocks and building parts | 30–60 kinds | 150–400 kinds | Every piece must be tested in the combination environment of all existing pieces |
| Mechanic primitives (physics/circuits/sensors) | 3–5 | 8–15 | Each primitive gets a tutorial slot, template contraption and achievement entry |
| Prefab templates and official showcases | 5–10 | 30–60 | Serve as guidance, style anchors and performance demonstrations |
| Achievements and challenges | 20–40 | 80–150 | Each one is an invitation to "go try this mechanic" |
| Environment themes and biomes | 3–5 | 8–15 | Decide the cost of visual volume and asset combinations |
| Guidance commissions (if there is a story line) | One main line | Main line plus side lines | Commissions are the cheapest way to teach creativity |

Rough workload accounting (taking the project to a 1.0 launch): tools and systems about 35%, content production about 35%, performance and optimization about 15%, and the sharing platform and community about 15%. Contrary to traditional titles, the tools in this genre get redone repeatedly: the first version of the tools carries the prototype, the second carries the community, and tool iterations usually outnumber content iterations. When scope runs away, the cutting order: cut environment themes first, then part counts; primitive depth and tool quality stay last — they are this genre's lifeblood. For scope-control methods see Indie Survival.

## 6. How to Start the First Prototype

Goal: in three to six weeks, build the minimal tool loop — "can build, can save, can show others" — with placeholder art and one theme.

| Milestone | What to do | Acceptance (behavior) | Time reference |
| --- | --- | --- | --- |
| M1 Placement loop | Grid, place/remove/pick, camera, preview | A tester walls off a room within 10 minutes | 1 week |
| M2 Save and undo | Save/load, undo stack, blueprint copy | Close and reopen, and yesterday's build is still there | 1 week |
| M3 A set of primitives | 2–3 combinable mechanics (such as a switch plus a door, gravity plus fluids) | Testers spontaneously build contraptions that "do something" | 1–2 weeks |
| M4 One toy | Wrap a micro-gameplay out of the primitives (a mechanism, a mini-game) | Players spend more than 5 minutes playing with their own contraption | 1–2 weeks |
| M5 Sharing loop | Export and import share codes, a bare-bones creations showcase | Send a creation to a friend, who opens it successfully | 1 week |
| M6 Stranger testing | Bring in 3–5 people who have never seen the project | Someone builds for 30 minutes straight and comes back on their own | Ongoing |

Three rules for starting out: keep all art as greyboxes and color blocks — anyone who wants to beautify it should go play M1 first; add only one new primitive at a time, and run it through the combinations with all old primitives the moment it lands; every 30 minutes of your own play, note down "what I want to tear down and what I want to change" — that list is your next tool requirement.

Success criteria (all observable; once met, freeze the tools and the feel and start laying down content):

- With no art and no tutorial text, testers complete their first structure of their own choosing within 15 minutes and start extending it on their own.
- In 30 minutes of observation, each person shows at least 3 instances of "tearing down and reworking their own build" — a sign that players are starting to treat their creations as creations.
- At least one tester asks "can this be shared", or tries to record or screenshot it.
- Complaints about the tools not feeling responsive (failed placement, accidental removal, cannot find undo) come to no more than 1 per person.

If the tool loop does not pass, do not start laying down block styles and environment themes: that is the most expensive kind of rework, and players' first impressions will die there.

## 7. Common Pitfalls

1. **Tools that do not feel responsive**: placement takes ages to aim, mistakes cannot be undone, removals are not refunded. Tool feel is this genre's equivalent of jump feel — every other design rests on top of it.
2. **Blank-slate fear left unhandled**: players arrive at an empty plot with no commissions, no templates and no inspiration entrance, and retention dies in the first hour.
3. **Too many or too few primitives**: too few and the combinations run out after two tries; too many and they conflict with each other and the tutorial can never cover them. Every primitive must answer "what can it combine with" — if it cannot, do not make it.
4. **Unpredictable physics**: the same contraption works only sometimes, players retreat to the most conservative builds, and depth goes to zero.
5. **Guidance that gives answers**: finished blueprints and automatic building shipped in the real toolset take the joy of building away from the player.
6. **Sharing is a dead end**: no export, no browsing, no recommendation slots; creations cannot leave the house, creators stop creating, and the platform dream becomes a single-player dream.
7. **Performance demolished by players**: community creations are not used as regression tests, so after launch lag on large buildings becomes the main theme of negative reviews.
8. **Performance ceilings faced too late**: only at the end of development do you discover a hard cap is needed, and players read it as "freedom restricted", eroding trust.
9. **Updates that break creations**: changed IDs and rules break old creations or change their behavior; once the creator community walks out, it rarely comes back.
10. **Online co-building left undesigned**: two players editing the same cell, visitors dismantling the host's world, duplication exploits — multiplayer turns from a selling point into an incident.
11. **Moderation missing**: UGC will grow rule-breaking content; with no recommendation slots or reporting channel, the risk is simply left to the platform and publisher.
12. **Scope out of control**: part counts, biomes, online and platform all in flight at once. Cut down first to one complete journey for a single creation — build, save, show off — with no step missing.

## Further Reading

- Game Design Handbook: layered core loops and system interlocking are the general foundation for this page's "four-tier pacing" and "primitive combinations" sections.
- Programming Handbook: rendering budgets, simulation LOD and world management — the counterpart to every engineering detail in §4.
- Modding & UGC: support tiers, the Workshop and mod.io, community operations and compliance — the full expansion of this page's §3.4.
- Indie Survival: scope control and scheduling; this genre is the worst-hit disaster area for runaway scope.
- Multiplayer & Backend: the engineering path for co-building and UGC distribution.
- Exercise: pick the building game you know best, list all of its primitives (no more than 20), draw the use matrix for every pair and find three cells the official game has not done yet; then write a tool checklist that defines the operation steps for each item, from "placement" to "undo".
