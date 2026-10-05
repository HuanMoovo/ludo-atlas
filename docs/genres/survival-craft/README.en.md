# Ludo Atlas · Genre Handbooks · Survival Craft

> **Genre Handbooks · Volume 1**. Positioning: breaking "from having nothing, to surviving the first night, to building a world of your own" into an executable handbook: the four-stage loop, restraint with pressure sources, tech-unlock pacing, base building, multiplayer differences and long-term updates.
> Covers both 2D and 3D, single-player and multiplayer. Companions: Game Design Handbook (systems and balance) · Programming Handbook · Level Design Handbook (space and guidance) · Case Studies (breakdowns of successes and failures).
> This page carries no external links. In this genre, game feel comes from the first shelter you build with your own hands — reading ten breakdowns is worth less than starving to death once yourself.

---

## 1. Positioning and Core Loop

Survival craft's formula: **a resource loop driven by survival pressure + high-freedom spatial building + long-term progression**. Take away any one of the three pillars and the genre falls apart:

| Pillar | The question it answers | The cost of leaving it out |
| --- | --- | --- |
| Survival pressure | If I don't do this, do I die? | Degenerates into a stress-free stroll, or a pure farm |
| Resource loop | Can what I harvest become a stronger capability? | Degenerates into a tree-chopping simulator, repetitive labor |
| Spatial building | Is what I've built the shape I wanted? | Building degenerates into spawn points; the sense of freedom disappears |

Boundaries: survival craft is not a farming sim (low-pressure routine, time management), not a colony sim (commanding AI instead of doing things yourself), and not a pure roguelike (death clears the board rather than building a persistent world).

### 1.1 The Four-Stage Loop

Written as a verb chain, the core loop has four stages:

`gather → craft → build → expand/explore → (pressure escalates) → back to gathering`

| Stage | What the player is doing | Output | Who is applying pressure |
| --- | --- | --- | --- |
| Gather | Chop trees, mine, hunt, forage for food | Raw materials | Hunger, nightfall |
| Craft | Assemble tools and weapons, process food | Stronger capabilities | Not enough materials, durability running out |
| Build | Raise houses, bridge gaps, build defenses and facilities | Safe zones and efficiency facilities | Night raids, weather |
| Expand/explore | Head outward, find new resources and landmarks | New recipes, new regions | Unknown dangers, long journeys |

There is only one linkage rule: **each stage's output must feed the next stage**. Wood builds tools, tools speed up gathering, materials raise a house, the house holds off night raids, and only once you're safe do you dare go far; break one link and the loop halts at that link (new players most often break at "I built a house but don't know why I should go outside"). Expansion must also leave behind new reasons to gather: new regions bring new materials, new materials open new recipes, and exploration is the opening line of a larger round of gathering. Second-scale feedback, minute-scale tasks, hour-scale goals, week-scale narrative — at the end of each layer of the loop, the start of the next layer must be visible; that is the universal formula for "the next step".

### 1.2 "Every Login Has a Next Step"

Survival craft is a long-session genre; a player might open the game 30 times in 30 days, and the first 5 minutes of each login decide whether they come back. If they return with nothing to do (resources fully automated, every building finished, the map fully revealed), the game dies quietly (see §3.5).

- The three login questions must answer two of themselves immediately: What do I eat today? What do I build today? Which way do I head today? The answers should be visible directly in the HUD or the scene.
- The world leaves "unfinished invitations" while you are offline: an unroofed house, ore still smelting, a cave mouth you didn't dare enter yesterday; and you log off carrying an unfinished goal ("tomorrow I'm getting that iron pickaxe made").

## 2. Player Experience Goals and Benchmark Titles

Write 2–4 experience pillars first, then use them as the ruler for every decision. The four common to survival craft:

- **Zero to one**: turn wasteland into a stronghold with your own hands. Every part of what gets built should be the player's own choice.
- **Planning under pressure**: not enough resources and limited time force real trade-offs. Tense but recoverable, not constant panic.
- **Unknown frontiers**: stranger things lie farther out on the map. Curiosity is the cheapest driver there is.
- **Building together** (the multiplayer branch): divide the labor to build something no single person could.

Anti-pillars must be written down too: if the game is not going punishment-first, explicitly rule out designs like permadeath or hunger draining health, so the team doesn't waver late in development.

Benchmark titles (all widely known; structural differences matter more than quality rankings):

| Title | Pressure-source configuration | Loop signature | One transferable lesson |
| --- | --- | --- | --- |
| Minecraft | Night and monsters dominate; hunger is very light | Survival plus unlimited building; tech unlocked through exploration | Survival pressure can be very light — building freedom alone can sustain long-term motivation |
| Don't Starve | Hunger, darkness and sanity all on at once | Trial-and-error recipes; the season as a macro-cycle | Seasons are a long-cycle pressure structure that outlasts any single event |
| Valheim | Food buffs, cold, combat | Biome bosses drive the whole progression; load-bearing building | Using bosses to unlock tech is the cleanest structure for driving exploration |
| Rust | Player conflict, periodic map wipes | Social pressure in place of environmental pressure | Multiplayer competition is the longest-lived pressure source, but it eats server operations |
| ARK: Survival Evolved | Hunger, temperature, dinosaurs | Taming turns creatures into production tools | Turn resources into production tools that move on their own |
| 7 Days to Die | The blood-moon raid cycle | A tower-defense stronghold loop | A raid that is announced in advance is the healthiest driver for building |
| Palworld | Survival pressure plus creature labor substitution | Base automation and labor management | Outsourcing repetitive labor to creatures is the right answer for freeing up player time |
| LifeAfter | Hunger, infection, multiplayer camps | Camp social life and division of professions | Social structures and professions are the main engine of long-term retention |

## 3. Design Essentials

### 3.1 Pressure Sources: Fire with Restraint

Pressure-source checklist (don't use them all; write down only the ones you use):

| Pressure source | Form | Solution | Design notes |
| --- | --- | --- | --- |
| Hunger and thirst | Timer | Food chain, water sources | Either one alone is enough; dual timers are a newcomer graveyard — and make the penalty slow |
| Temperature | Environment | Fire, clothing, shelter | An immediate fix must exist; freezing to death must be foreseeable |
| Night and darkness | Cycle | Light sources and shelter | The strongest emotional lever at the lowest implementation cost — do it first |
| Monsters and raids | Event | Weapons, walls, running away | Always keep the "run if you can't win" option available |
| Durability and rot | Timer | Repairs, stockpile management | Never punish being offline; everything rotting overnight while you're logged out is a top source of bad reviews |

**Switch on only 1–2 pressure sources at the start**. All of them at once means the player is hungry, cold, bitten and poisoned within ten minutes, and then uninstalls. Bring pressure online item by item, in step with the player's capability:

| Period | Pressure switched on | Purpose |
| --- | --- | --- |
| 0–30 minutes | None (or nightfall warnings only) | Teach gathering and crafting |
| First night | Darkness and cold | Create the desire to go home |
| First three days | Hunger comes online (decay slowed) | Turn foraging into a daily rhythm |
| From mid-first-playthrough | Predators and raids, later weather, disease, sanity, player conflict | Give defensive building and base upgrades a reason to exist |

**At most two pressures maxed at any one time**; when three spike together, keep at least one way out (drink soup, hug the campfire, hide in the basement). Pressure resonance is an advanced technique (going hungry on a Don't Starve winter night), and a quit-the-game bomb for new players. The same goes for death penalties: dropping your pack, losing XP, losing durability are all fine, but "run five minutes to your corpse, then get killed by the same monster again" is double punishment — fix it.

### 3.2 The Tech Tree and the Unlock Curve

**Hand out a "new toy" every 15–30 minutes**. A new toy means any kind of new capability: a new tool, a new recipe, a new building piece, a new mechanic, a new area permit. When you can't hand one out, the player is marking time, and the churn starts on the very next step.

| Player time | The new toy due | Typical examples |
| --- | --- | --- |
| 0–30 minutes | The first tool and the first shelter object | Stone axe, campfire, bed |
| 30–60 minutes | The smelting on-ramp | Furnace, the first metal |
| 1–2 hours | Tier-shifting equipment | Metal tools, the first set of armor |
| 2–4 hours | Base efficiency pieces | Storage system, cooking, farmland |
| 4–8 hours | New-area permits | Cold-resistant gear opens the snow mountain; a boat opens the waterways |
| 8+ hours | Large projects and automation | Electricity, teleportation, animal husbandry |

Unlocking generally runs three routes in parallel: **resource unlocks** (picking up a new material immediately yields a recipe), **prerequisite unlocks** (the tech tree clicked through in order), and **discovery unlocks** (ruin blueprints, recipes found by trial and error); the first two manage pacing, the third manages surprise. Three things prevent a broken chain:

- Locks must be visible: players only go and gather when they can see that there is still more to unlock and can look up where a recipe's materials grow.
- Don't build material walls: chopping for 20 minutes for 30 planks is not gameplay, it is detention. Load-reducing mechanics — batch felling, multi-target swings — should arrive as early as possible.
- Self-check regularly: record a 60-minute play session and count the "oh, something new" moments; fewer than 2 means the curve is too steep, more than 5 means players can't digest it all.

### 3.3 Base Building: Balancing Freedom and Guidance

Pick a build-freedom tier first, then talk details:

| Tier | Approach | Representative titles | The price |
| --- | --- | --- | --- |
| Voxel blocks | Every cell placeable and removable | Minecraft | Heavy rendering and save pressure; the art is hard to control |
| Modular assembly | Walls, windows, doors and beams combined at snap points | Valheim, Rust | Freedom limited by the parts; legality rules must be written |
| Prefab strongholds | Whole buildings placed and upgraded | Palworld, LifeAfter | Fastest to pick up; the weakest sense of ownership |

The balance point between guidance and freedom: **strong guidance for functional anchors, weak guidance for shapes**.

- Functional anchors: bed (sleep), fire (heat and light), chest (storage), workbench (crafting) — each must have an irreplaceable role, and players will naturally build their house around them.
- No blueprints for shapes: the quest only guides "build somewhere you can sleep"; how to enclose it, how big, what materials — that is left to the player. Handing out finished blueprints kills the joy of building outright. Guard against both failures: under-guided, players build a hut that leaks wind on all four sides and puts out its own fire when it rains, then freeze to death; over-guided, every player's base looks identical. The fix is feedback (draft warnings, cold warnings), not blueprints.

What the blueprint and snapping systems look like in practice:

- Placement preview (ghost): green when placeable, red when not, with the reason spelled out (floating, not enough materials, over the height limit); show the material cost before placing.
- Snapping and bulk operations: grid snapping as the baseline, angle and edge snapping as the advanced layer; continuous placement, drag-to-place in bulk, copy and mirror all need doing.
- Demolition and legality: demolition refunds 50%–100% (100% recommended, to encourage experimentation); load, support and enclosure checks should exist, but skip the collapse penalty — "over the structural limit and it just collapses" is the extreme approach, while "parts of it simply can't be placed" is gentler.
- Treat the base as level design: site selection is driven by water, resources and chokepoints; leave expansion circulation inside the walls; keep landmarks visible from the roof. The base is essentially a level the player builds themselves — details in the Level Design Handbook.

### 3.4 Multiplayer: Division of Labor and Coordination Costs

As headcount rises, individual survival pressure falls (gathering is shared across players), so new tension must be added, or the game becomes a pressure-free chat room:

| Dimension | Single-player | What multiplayer must add |
| --- | --- | --- |
| Pressure | Survival itself | Denser raids, synchronized events |
| Division of labor | One person covers everything | Allow but never force specialization (gathering, building, cooking, exploring) |
| Resources and coordination | Self-sufficiency | Shared storage and permissions, map markers and voice are all hard requirements |
| Progression | One line | A structure for mixed paces — some players race ahead, some flake out |

Division of labor brings efficiency, and also waiting (someone waiting on materials, someone standing guard). Coordination tools must at minimum include shared chests, map pins and visible progress status; the opposite failure is over-management — pile on enough quests and quotas and the game becomes a day job. On headcount, 2–4 players is the sweet spot (pressure shared, coordination costs controllable, development survivable); going past 8 players requires dedicated synchronization and anti-cheat design, which is another project entirely.

Saves and synchronization are where multiplayer design most easily crashes:

- **Authority model**: start friend-hosted rooms as host-authoritative; long-term live operation requires server authority, or item duplication and value edits can't be stopped.
- **Save ownership and offline progress**: who holds the save, whether others can play when the host is away, and whether the world pauses or keeps running with nobody in it — all of this must be decided and written into the store page; most small teams choose pausing, at the cost of stalling whenever teammates don't show.
- **Sync granularity**: high-frequency interpolation for positions, event-based sync for inventory and construction; building placement needs confirmation and rollback to prevent two players placing into the same cell at once.
- **Join-in-progress and reconnection**: a new player entering the world must quickly see the current state (buildings, markers, storage); skip reconnection and negative reviews are available on demand.

### 3.5 Long-Term Content: Update Cadence and the "Graduation" (Endgame) Problem

Admit the reality first: players consume content far faster than teams produce it. Automation, building megastructures and exploration racing can compress 40 hours of launch content into a single week. So long-term content is not "more maps", but **systems that generate the next step on their own**:

| Type | Means | Examples | Audience |
| --- | --- | --- | --- |
| Challenge | Higher difficulty, stronger enemies | Blood moons, seasonal bosses, hard mode | Completionists |
| Expansion | New biomes, new dimensions | New ecologies bring new resources and recipes | Explorers |
| Creation | Large projects and automation | Electricity, teleport networks, factories | Builders |
| Reset | Seasons, periodic refreshes | Full resets, limited-time events | Competitors |
| Co-creation | Mods and UGC | Workshops, map sharing | Everyone |

"Graduation" is this genre's real endpoint: once the tech is fully unlocked, every boss is down and the base is finished, players need new questions, not bigger numbers. Graduation design comes down to two things:

- Leave every player group something to play after graduation: builders want creation space without a ceiling (a sandbox or creative mode to divert them), completionists want a higher-difficulty replay layer; also watch for a self-organizing challenge culture in the community (speedruns, building contests) — it is the cheapest indicator of lifespan.
- Promise conservatively on update cadence, deliver reliably: major content updates plus patch fixes is the common combination for premium titles. Before every update, answer one question: "What is a returning player's first step?" If you can't answer it, don't ship yet.

## 4. Technical Essentials

**Building systems.** Choose the implementation route by the tiers in §3.3; the differences land in three costs: collision and pathfinding, save size, and render batches. Voxel blocks need chunk management and mesh merging; modular assembly needs snapping, legality checks and an undo stack; prefabs need upgrade chains and placement-point rules. All three share the same placement pipeline: preview entity (ghost), legality check, resource check, commit or roll back (the undo stack keeps the last N operations — players will absolutely spam the button).

**World generation.** Lay out biomes over a noise base, and distribute resources in "bands" (mining areas, forests, water sources) so exploration has route logic instead of random scatter. Spawn areas need guarantees: basic food, wood, stone and water within two minutes' walk. Revisitable landmarks (ruins, cave mouths) drive long-term exploration better than pure scenery.

**Saves and networking.** Incremental chunk storage with dirty-chunk flags; decouple entities from players so multiplayer join and leave stay stable; autosave writes to disk asynchronously (write to a temp file first, rename on success, guarding against crash corruption), every 5–10 minutes, with manual saves supported; keep a version number and a migrator in the save, so old worlds can be upgraded when the data structure changes. Decide the networking scheme first: friend rooms (host-authoritative) and dedicated servers (server-authoritative) are two different orders of effort. Split sync into three classes: positions use high-frequency interpolation, inventory and construction use event broadcasts plus server validation (anti-duplication), world state (time, weather) uses low-frequency broadcasts. Send a snapshot on join-in-progress, deltas on reconnect.

**Performance.** Three performance black holes: dropped items (merge stacks, sleep them, stop rendering them individually past a cap), AI (simulation LOD: full speed nearby, reduced frequency at mid distance, events only far away), and large-base rendering (batching and instancing, visible-face culling — past a few thousand building pieces it will stutter). Also, autosave hitches are a top source of bad reviews; use asynchronous disk writes or spread the work across frames.

## 5. Content Volume and Workload Reference

Order-of-magnitude reference for launch content volume (the numbers are a ruler, not a promise — calibrate against your own team's speed):

| Content module | Minimum shippable | Comfortable | Notes |
| --- | --- | --- | --- |
| Biomes | 4–6 | 8–12 | Mix old and new; each biome gets exclusive resources |
| Resource types | 15–25 | 30–50 | From raw materials through intermediates to finished goods |
| Items and recipes | 120–200 items, 150–250 recipes | 300+ items | Recipe count sets the density of the tech rhythm |
| Building pieces | 60–120 | 200+ | Including decorative and defensive pieces |
| Tech nodes | 25–40 | 60+ | One unlock every 15–30 minutes |
| Creatures and enemies | 10–15, including 1–2 large threats | 25+ | Two or three per biome, with behavioral differences |
| First-playthrough length | 15–25 hours | 40+ hours | Building-minded players will double it |

Rough workload split (a 3–5 person team reaching an EA launch): systems and tools about 30%, content production about 45%, balance and polish about 15%, launch and community about 10%. For content-driven projects the cost center is always content production, and investing in tools early (map editor, recipe sheets, batch validation scripts, test commands) is the highest-return decision you can make; solo developers have to accept that content volume cannot be piled up linearly by person-month — ship 1–2 biomes at launch, cut half the recipes, and only call it passing once the loop is polished to "can't stop playing". For the concrete algorithms of scope control see the Production Handbook.

## 6. How to Start the First Prototype

Goal: within two weeks to a month, build a prototype that plays for 20 minutes and makes people want a second run. Placeholder art, one biome, two pressure sources.

| Milestone | What to build | Acceptance (watch behavior, not surveys) | Reference time |
| --- | --- | --- | --- |
| M1 Gathering and crafting loop | 2 resources, 2 tools, a crafting screen | A playtester spontaneously makes their first tool within 5 minutes | 3–5 days |
| M2 Day/night and one pressure source | A day-night cycle plus darkness or hunger (only one) | When night falls, players spontaneously want to find a light source or go home | 3–5 days |
| M3 Building and shelter | One placeable piece, fire, bed | Players build the minimal shelter on their own in order to last the night | 5–7 days |
| M4 Persistent world | Save, load, world memory | Quit and relaunch — the world is still there and the player continues yesterday's business | 3–5 days |
| M5 Tech ladder | 6–10 recipes, a clear material ladder | Three "new toy" moments within one hour | 5–7 days |

Three rules for the start:

1. Use geometric primitives and flat color blocks for all art; anyone who wants to beautify it can go play M1 instead.
2. After every new system is added, pull in someone who hasn't seen the project and have them play for 20 minutes; watch behavior only, no hints.
3. At the end of every milestone ask three questions: Will the player voluntarily start the next day? Will they be reluctant to log off? Are there "one more tree and then I'll quit" moments? The more the third question shows up, the healthier the loop; also get the data-table structure in place early — items, recipes and drops should use external tables from the start.

## 7. Common Pitfalls

1. All pressure switched on: hunger, cold, monsters and poison come online together and players uninstall within ten minutes. Start with only 1–2, and guarantee resources at the spawn point.
2. Tech starvation and material walls: no new toy for 15–30 minutes, or forcing half an hour of repetitive chopping — either way players churn.
3. A crafting UI that tortures people: no search, no bulk operations, no diff hints when materials are short.
4. Inventory torture: too small, no sorting, no tabs, and a death drop you can't find your way back to.
5. Building with no undo: demolition doesn't refund materials, misplacements can't be fixed, and the player never experiments again.
6. Double death punishment: run five minutes to your corpse, only to be killed by the same monster again.
7. Graduation left undesigned: you assume players will find their own fun, and the completionists simply walk away.
8. Multiplayer as single-player times N: no shared storage or markers, progress out of sync, and the world gets force-restarted.
9. Fragile saves: one crash loses hours, and autosave stutters to the point of being unacceptable.
10. Numbers off the top of your head: one-shotting the whole map in the late game, or chip-damage fights that drag on for five minutes — both mean the curve was never designed.
11. Graphics first: art investment too early, and one mechanics change scraps every texture.
12. Missed update promises: the EA cadence you promised can't be delivered, and after two misses the returning players are gone.

## Further Reading

- Systems and balance: revisit the core loop, system interlock and economy sources-and-sinks sections of the Game Design Handbook; the survival-craft economy is a typical exercise in "many sources, many sinks".
- Space and guidance: base siting, circulation and landmark design are level-design problems — see the guidance and spatial-language sections of the Level Design Handbook.
- Engineering: networking sync and performance budgets are in the Programming Handbook; the full path from "it connects" to "it holds up" in multiplayer is in Multiplayer & Backend.
- Case studies: look for the open-world and survival breakdowns in Case Studies, and pay attention to the real numbers on content consumption and update cadence.
- Homework: break down the first 30 minutes of Don't Starve, logging every "new toy" moment and the interval between them; reimplement a minimal version of load-bearing rules in your engine; write a 4-hour unlock table for your game. For reading lists and a wider case index see Resources; for team-level pitfalls see Pitfalls & Anti-patterns.
