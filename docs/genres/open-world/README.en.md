# Ludo Atlas · Genre Handbooks · Open World

> **Genre Handbooks · Volume 4**. Positioning: dissecting "open world" as a spatial structure. It does not answer "what the player is playing", only "where to go, what to do, and who decides the order"; this page lays out the structural trade-offs, density and pacing, quest structure, the technical bar, and a realistic slice of what a small team faces.
> Companions: Game Design Handbook (core loops and content pacing) · Level Design Handbook (density, guidance and spatial language) · Programming Handbook (streaming and performance budgets) · Indie Survival (scope control and honest accounting).
> This page carries no external links; benchmarks are widely known works only, and the numbers are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

Start with this page's most important sentence: **open world is a structure, not a genre**. It describes a way of organizing space that hands the decisions of "where to go, what to do, in what order" to the player; what the player actually does inside that space (shooting, slashing, sneaking, farming, racing) is another layer entirely. The same gameplay can be linear, miniature garden or open world, and the three structures keep completely different books.

The trade-offs among the three spatial structures:

| Structure | Who decides the path | How content is delivered | Cost shape | Best-fit emphasis |
| --- | --- | --- | --- | --- |
| Linear | Essentially none; the author fixes the order | Appears section by section; pacing is the most controllable | Highest content utilization; build one stretch, play one stretch | Staging, pacing, a carefully choreographed intensity curve |
| Miniature garden (wide linear) | Local freedom, but the order of segments is still fixed by the author | A few anchor points placed within one area; density stays controllable | Between the other two | Wanting a touch of exploration without letting pacing fall apart |
| Open world | Fully autonomous; the player decides which place comes first | Spread out across space, waiting to be found | The cost of the same content multiplies severalfold; waste is unavoidable | A sense of autonomy and curiosity; the journey itself is the content |

A self-check question: if you replaced the world with a "level list" menu, would the game still hold up? If the core fun is all in the combat or the puzzles, the open world has only made the menu bigger; only if part of the fun lives in the act of walking there yourself does the structure earn its keep.

The core loop, written as a verb chain:

`see a goal on the horizon → plan a route → run into something along the way → arrive and resolve it → settle rewards and grow → climb to a new height and spot the next goal`

This loop is measured in "trips", each lasting from tens of seconds to tens of minutes. It holds on two preconditions only: something visible makes you want to go there (guidance and attraction, §3.2), and the road there has something on it (density and pacing, §3.1). Break either one and the loop degrades into "open the map, click a fast-travel point, do the quest, open the map again".

Drawing boundaries against neighboring structures:

| Neighboring structure | The boundary |
| --- | --- |
| Sandbox | A sandbox is a toy box with no preset goals; an open world still carries its own choreographed purposes and content |
| Miniature garden | The miniature garden locks density and the handcrafted feel into a local area; the open-world experience requires at least one stretch of genuinely empty distance |
| Survival craft | That is a gameplay genre that often borrows open-world space; the two keep different books, and conflating them does a disservice to both (for the counterpart see Genre Handbooks · Survival Craft) |

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **A sense of autonomy**: where to go, what to do, when to give up — all decided by the player. When players retell their experience, the subject is "I", not "the quest made me".
2. **Curiosity-driven**: every silhouette at the edge of sight asks "what is over there"; the motivation comes from wanting to see, not from checking off a list.
3. **The journey is the content**: what is worth retelling are the things that happen along the way — the detour, the chance encounter, the gamble of traveling at night; these cannot rely on luck alone but must be produced probabilistically by density and systems, and standing on a high point should let the player gather the whole road walked so far into one view.
4. **Low-pressure failure**: taking the wrong path is not failure, it is content; and dying must not cost half an hour of progress.

Benchmark titles (widely known works only; look at structural differences, not rankings):

| Title | What to learn from it |
| --- | --- |
| The Legend of Zelda: Breath of the Wild | A curiosity-driven density specimen: the triangle rule of occlusion and reveal, and the physical consistency of "if you can see it, you can walk there" |
| The Witcher 3: Wild Hunt | The quality bar for side-quest narrative: side quests are small stories with endings, not errands; also study the long-criticized side of its question-mark checklist |
| Grand Theft Auto V | The industrial form of the urban open world: multiple protagonists and a quest-type library, vehicles and radio stations; a reference for scale and its costs |
| The Elder Scrolls V: Skyrim | The density of handcrafted points of interest and a landmark mindset; "the mountain is over there and something is on it" — you only realize how much you skipped when you check a guide |
| Elden Ring | Guidance without a quest list: landmarks as compass, rumor as clue, giving observation and memory back to the player |
| Assassin's Creed series | A ready-made lesson in checklist content: how question-mark icons and repetitive activities turn exploration into a to-do list |

## 3. Design Essentials

### 3.1 Density and Points of Interest: Laying Content Out Across Space

An open world's experience quality is decided by density, not by area. Standardize how you measure density: how many interactables fall within sight and reach for every minute the player spends walking — interactables, note, not decorations.

| Space type | Density reference (per 1 minute of walking) | Content devices |
| --- | --- | --- |
| Cities and settlements | 3–5 | Shops, NPCs, events, side-quest entrances, enterable buildings |
| Countryside corridors (near the traffic routes) | 1–2 | Camps, ruins, gathering nodes, roadside encounters |
| Wilderness and negative space | 0–1; consecutive empty windows are allowed | Terrain, distant views, wind; the empty windows are there to build anticipation |

Three rules:

- **Density follows the traffic routes; it is not salt sprinkled evenly.** Main-story corridors, junctions and resource loops are where players most likely pass, and they are the last places that should be empty; corners and far places are left to explorers willing to stray, and there density can drop a tier.
- **Negative space is a resource, not waste.** Filling everything in leads to player fatigue and a world where nothing is worth much; the proper function of an empty window is to build anticipation and amplify the payoff of arriving. Any empty window longer than a few minutes needs a justification: scenery, radio, a shortcut or risk — at least one of the four.
- **Every point of interest pays out on three layers.** Immediate payoffs (loot, numbers), short-term payoffs (unlocks, recipes, shortcuts) and long-term payoffs (story, changed world state). A point of interest that only hands out immediate rewards is consumable; build a hundred more and players are still sick of them.

| Tier | Magnitude (per region) | Form | Payoff on arrival |
| --- | --- | --- | --- |
| Spine | Single digits | Main-story nodes, settlements, large strongholds | Story progress, regional change |
| Anchors | A dozen or so | Side-quest starts, dungeons, challenge spots | Handcrafted rewards, dedicated content |
| Micro points | Dozens | Gathering, relics, roadside events | Resources, small surprises |
| Vistas | No limit, but do not skimp | Viewpoints, wonders | They stand without rewards; they are the map's memory points |

Density acceptance test: record a 30-minute playtest and count how many times the player voluntarily turns off the path; 0–1 times means guidance or density has failed.

### 3.2 Movement and Guidance: Letting the World Point the Way

Players spend most of their open-world time moving. Movement must either have game feel (running, climbing, gliding, vehicles) or carry information (reading the road, taking in the view); it cannot be filler. Four levers:

**Vantage points.** The classic trio of climb high, unlock the map and light up objectives really works by translating the to-do list into things inside the sightline. Three rules: the climb itself must have gameplay (route choice, climbing); once at the top, at least two or three destinations should be visible; and do not build twenty identical towers in one world — repeated tower climbing demotes exploration to labor.

**Landmarks and occlusion.** A landmark needs three properties: a distinctive shape, a fixed position and recognizability from multiple angles. It is the player's mental coordinate system — "past that broken tower, turn left". Guidance strings the path together with three layers of sightlines: distant silhouettes do the luring, mid-range path hints (a broken bridge, firelight, footprints) do the confirming, and nearby audio-visual cues finish the job; then use hills, buildings and vegetation to block part of the sightline, so that players keep acquiring new goals as they detour, occlusion creating the question and reveal giving the answer. The minimap and arrows are the fallback only — let them take the lead and players walk with their eyes glued to the interface while the world goes to waste.

**Fast travel.** Offering it is a given — withhold it and reviews will punish you — but it costs design work: where the warp points go (too many and travel disappears, too few and players are left standing around), whether to charge for it, whether the first arrival has to be on foot to unlock it. Two rules: departure and arrival both need a "reason to still be willing to walk", and the road must have content on it; and fight over every second of fast-travel loading time, because it is a tax on the experience.

**Traversal abilities as rewards.** Unlocking climbing, gliding and mounts one by one re-measures the same world; it is the cheapest map renovation you can buy.

### 3.3 Quest Structure: Main Line, Side Quests and Emergence

The fundamental difference between open-world quests and linear-game quests: the player may meet a quest in any order and from any direction. Entrances must tolerate mistakes, order must be loose, and state must heal itself.

Content mix reference (by content volume; calibrate per project):

| Content layer | Share reference | How it is written | Form |
| --- | --- | --- | --- |
| Main line | 20%–30%, but must cover the whole journey | Handcrafted, staged, and pickable-up-again | Chapter quests, key strongholds, region liberation |
| Side quests | 30%–40% | Self-contained small stories with endings and consequences | Commissions, character vignettes, regional quest lines |
| Systemic emergence | 30%–50% | Templates plus rules plus boundaries, combined by the systems | Encounters, escorts, bounties, stronghold activities |

- **The main line must be pickable-up-again.** A player might return to it after tens of hours away: the objective location is visible on the map, the quest log states the next step in one sentence, and failure or abandonment can always be retried. Forced single-threaded staged sections either stay out of the open world or get wrapped in instances, teleports and clear warnings.
- **Side quests come in three forms with different costs and payoffs.** Narrative side quests are the most expensive and the best (writing, staging, voice); systemic ones are mid-cost (hunts, escorts, gathering — they run on templates); collection ones are the cheapest (repeat for quantity). You need all three; a quest list that is nothing but collection types is a disaster.
- **Emergent events need boundaries.** Template-generated events are content multipliers, with three boundaries: do not interrupt what the player is doing; the template library must be large enough, because the third repetition gets seen through; and consequences must land — a cleared stronghold really stays empty, and only then does the player believe the world remembers them.
- **The quest system must implement "skip and compensate".** More than half of open-world bugs come from state combinations: the NPC is already dead, the item already taken, the location already cleared. Anything the player did early must have an alternative path (already holding the item, hand it straight over; the target already dead, confirm it straight away) rather than a dead end; every quest must pass the check "does this still hold after being done out of order?".
- **Cap the size of the quest list.** Keep simultaneously active quests within 5–8; a full list means the player cannot recall a single one.

### 3.4 The First Hour: Spawn Point and First Goal

The spawn point carries three jobs: teach movement, present a spectacle that must be inside the sightline, and offer one small thing to do right now; the first goal must be visible, finishable in ten to twenty minutes, and acknowledged (a visible change in the world). The first 30 minutes give curiosity first and the list second, and must yield at least three small surprises (one spectacle, one chance encounter, one unexpected reward); count them out — if you cannot, redo it.

### 3.5 The Small Team's "Small Open World"

In one line: density can be bought with hand labor, area cannot. The small team's way out is to build a small, full box, not a large, empty plain.

| Approach | What it is | What it saves | The price |
| --- | --- | --- | --- |
| One island or one valley | 0.5–2 square kilometers of handcrafted terrain | Less streaming and art pressure, and every corner stays controllable | The sense of scale is discounted; make up for it with depth and detail |
| Vertical city | One city block, multi-level interchanges, rooftops and underground | Height traded for area | Level design and occlusion get more complex |
| Segmented world | Several miniature gardens connected by load transitions | Seamless engineering and art costs are avoided entirely | Immersion is discounted; cover the seams with transitions and sound effects |
| Procedural generation with handcrafted accents | Generated terrain, hand-placed points of interest | Terrain cost drops by an order of magnitude | The workload moves to curation and accents — do not underestimate it |

Three rules:

- Content reuse runs on the combination of "template × terrain × faction × time of day", and the red line is anything the player sees through at a glance; the third time they see the same ruin layout, the reuse has given itself away.
- State the scale honestly on the store page and in marketing. A compact open world is not an embarrassing position; pretending to be a huge world costs you bad reviews.
- Suggested cutting order, heaviest first: number of regions, seamless movement, vehicles and the traffic network, dynamic weather and seasons, side-quest count and voice-over, life-sim activities (fishing, card games and the like). Area is the thing least worth defending.

## 4. Technical Essentials

The engineering difficulty concentrates in four places: streaming, LOD and culling, the world toolchain, and saves and world state. Everything below is engine-agnostic; mainstream commercial engines ship terrain and zone streaming as built-in capabilities, while a custom-engine route means writing the whole set yourself.

**Streaming**

- Split the world into chunks (or cells): the area around the player stays resident, distant parts load and unload on demand; big chunks save management overhead, small chunks save memory. Loading needs cover: tunnels, corridors, elevators, bends — loading the player never sees is good loading.
- Lock the target platforms down first, then write a loading budget sheet: how many seconds are allowed for boot, fast travel and region transitions, each verified item by item. HDD, SSD, handheld and mobile I/O differ by orders of magnitude; never assess on the dev machine.
- Seamlessness is an engineering abyss: once you commit to it, run the worst-case scenarios on target devices during the prototype stage; discovering the problem late equals a rewrite (§3.5).

**LOD and culling**

- Do LOD separately for geometry, shadows, materials and animation, and fill in distant silhouettes with proxy models (textured shells, billboards and the like); vegetation and scatter props are frame-rate black holes, so layer the density, tier the view distance, and do the instancing and batching.
- In a large world the cost driver is usually not the triangle count but draw calls and shadows; occlusion culling and the lighting approach (fully dynamic, or baked plus probes) must be settled before the art style is locked.
- Acceptance is tabled by scene type: combat, city, wilderness and night scenes each get their own frame-time budget; do not paper over it with "60 FPS on average".

**World toolchain**

- The production bottleneck on these projects is tools, not headcount: terrain editing, roads and rivers, point-of-interest placement, quest editors, batch replacement, procedural assistance with seed reproduction, automatic map and compass generation.
- Keep all data in external tables under version control: points of interest, quests, drops, spawn rules. The world itself is data, and data must be diffable and batch-validatable.
- Treat tools as first-class citizens: the one most worth building first is a density heat map that plots points of interest, interactables and empty windows on a single image, so you can see at a glance where it is bare and where it is piled up; every hour saved on tools during content production comes back multiplied as rework.

**Saves and world state**

- The world has memory: which strongholds are cleared, which chests are open, which NPCs have left. Use incremental per-chunk storage plus a global state table; save size grows with exploration, so set caps and compression. The state combinations woven from quests, factions, time and weather are a bug breeding ground; back them with explicit state machines and validation scripts, so a dead NPC never keeps handing out quests.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimating scope; not a commitment.

| Project form | World scale | Content volume | Timeline | Notes |
| --- | --- | --- | --- | --- |
| Exploration prototype | One small map that takes ten minutes to cross | 5–10 points of interest | 2–6 weeks | Validates only the "see it, walk there, get paid" loop |
| Small complete title | 1–3 square kilometers of handcrafted terrain | 20–40 points of interest, 3–6 hours of main line | 6–18 months | A small miniature-garden-style open world, segmented or lightly streamed |
| Typical indie scope | One region, mostly handcrafted | 50–100 points of interest, 10–20 hours of main line | 2–4 years | Content production is the bulk of the cost |
| Commercial scale | Tens of square kilometers and up | Hundreds of points of interest, dozens of hours of main line | 4+ years | The toolchain and content pipeline come first; small teams should not benchmark against this |

Cost breakdown and scheduling anchors: a single qualified point of interest costs terrain shaping, art assets, placement and scripting, rewards and text, and testing, counted in person-days; run the estimate backwards — first work out how many points of interest the team can produce in a year, then back-calculate world area and schedule from the target density, instead of fixing the area first and then looking for ways to fill it. Main-line hours multiplied by scene density gives the environment art volume; voice-over and cutscenes go to key nodes only. A playable exploration prototype takes 2–6 weeks, a vertical slice (a small stretch of world at shipping quality) 3–6 months, and after that extrapolate on "content volume times polish factor". World-based projects carry a higher polish factor than linear ones, because the same content must be tested across more state combinations. Cutting content is always safer than piling it on.

## 6. How to Start the First Prototype

The first prototype is one small map plus one complete loop, 4–6 weeks, touching neither story nor multiplayer nor art.

| Milestone | What to build | Acceptance (watch behavior, not surveys) | Time reference |
| --- | --- | --- | --- |
| M1: walkable terrain | Handcrafted terrain that takes ten minutes to cross, movement feel, camera | Testers are willing to wander around in it for ten minutes | 1 week |
| M2: see it and want to go | 2–3 landmarks, 1 vantage point, 5–8 points of interest | Testers can say where they want to go next, and why | 1–2 weeks |
| M3: the loop | One quest template, one emergent event, reward payout | After finishing "discover, arrive, get paid" they want to find the next one | 1 week |
| M4: memory and stress | Saves and world state; worst-case performance and loading scenarios run on target devices | Quit and relaunch and the world is still there; the frame-time and loading budgets from §4 are met | 1–2 weeks |

Three rules for getting started:

1. If seamless streaming is a project premise, run the technical prototype in parallel during M2 — do not wait for the vertical slice.
2. Find 3–5 people who have never seen the project, let them play for 20 minutes, and only observe behavior — no hints.
3. Each milestone changes parameters and content only; add no new systems.

Success criteria (all observable):

- With story and art stripped out, testers still explore on their own for more than 20 minutes.
- At least 3 of 5 testers spontaneously walk toward a point of interest you never guided them to, and can say why.
- Testers can sketch a rough mental map: spawn point, landmarks, places they have been.
- No more than 1 "I don't know where to go" complaint per person, and someone asks to keep playing.

## 7. Common Pitfalls

1. **Area as the selling point, density piled only around the spawn point**: the world is big and empty, or everything is stacked at the spawn, and players vote with their feet; the approval threshold is density, and density must be distributed along the traffic routes (§3.1).
2. **Checklist-ification**: turning exploration into question-mark stamp collecting — strong on execution, but the soul is gone; open with curiosity first and the list second, and keep the list as a fallback (§2).
3. **Guidance that lives on the interface**: the minimap and arrows serve as the main guidance, players walk with their eyes on the UI, and the world goes to waste (§3.2).
4. **Quests and events that cannot tolerate mistakes**: something the player did early jams a quest, and an emergent event interrupting main-line staging also costs goodwill; skip-and-compensate must be solved at the system layer (§3.3).
5. **Fast travel kills the travel**: the teleports are there, but the road has nothing worth walking for, and however big the map is it is just a corridor (§3.2).
6. **Seamlessness as an obsession**: a small team commits to a seamless large world and half the schedule sinks into streaming and memory; segmentation plus loading cover is the right answer for most projects (§3.5, §4).
7. **Content cliff**: players chew through a year of the team's content in two hours; ship a compact world that holds up, then expand through updates (§5).
8. **Saves and world state out of control**: a state-combination explosion jams quests and resurrects NPCs; back it with chunked storage and validation scripts (§4).
9. **Greenlighting a structure as if it were a genre**: without a gameplay core that stands on its own, the bigger the structure, the more obvious the empty shell (§1).

## Further Reading

- Game Design Handbook: core loops, content pacing and number-table methods — the drafting paper for section 3 of this page.
- Level Design Handbook: the full expansion of density, guidance and spatial language; read against §3.1 and §3.2.
- Programming Handbook: method details for streaming, LOD and performance budgets — the drafting paper for section 4.
- Indie Survival: scope control and honest accounting for small teams — read it before choosing an approach from §3.5.
- Case Studies: breakdown methods for successful and failed projects — consult when dissecting world-based works, paying attention to the real numbers for content consumption and production timelines.
- Pitfalls & Anti-patterns: high-frequency pitfalls in greenlighting and content production — the supplement to section 7.
