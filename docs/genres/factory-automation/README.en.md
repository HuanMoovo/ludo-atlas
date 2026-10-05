# Ludo Atlas · Genre Handbooks · Factory / Automation

> **Genre Handbooks · Volume 4**. Positioning: a genre that makes "building a machine that runs by itself" the core pleasure. The player starts by hand-mining the first lump of ore, connects gather, haul, process and reinvest into a production line, then scales the line into a factory; this page covers the automation loop, belt logistics, recipes and tech trees, blueprint tools, and the performance bill of a big factory.
> Companions: Game Design Handbook (core loops and numbers) · Programming Handbook (data-driven design, performance and saves) · Production Handbook (content estimation and scope control) · Pitfalls & Anti-patterns (number and performance pitfalls).
> This page carries no external links; benchmark titles are widely known works only, and the figures here are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: factory automation is the genre that **makes "efficiency" itself the gameplay**. The player's opponent is not an enemy but their own capacity sheet: belts are not fast enough, raw materials are not mined enough, power is not enough — every time you scale up, the old bottleneck surfaces right on schedule. The pleasure comes from a system you built by hand running exactly as designed with you out of the loop.

The core loop, written as a verb chain:

`prospect and mine → haul and feed in → process and assemble → deliver and research → unlock and expand → a bigger bottleneck → back to step one`

This loop has three layers of time scale, each with a different hook:

| Layer | Duration (real time) | What the player is doing | Resolution point |
| --- | --- | --- | --- |
| Machine | Seconds | One machine completes a work cycle | Output readout and sound |
| Production line | Minutes to hours | Build a complete chain from raw material to finished goods and measure throughput | Items-per-minute readout |
| Factory | Tens of hours | Scale up, move to a higher logistics tier, kill bottlenecks | Tech unlocks and doubled capacity |

The loop holds on two preconditions only: item conservation (what goes in matches what comes out) and visible throughput (every number can be verified by the player themselves). Break either and the player stops trusting the system — a factory game degrades into grunt work.

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Management sim | Management runs people, money and process, and its goods are often abstract numbers; factory automation runs things — every item has a real position and destination in space, and throughput is everything. |
| Colony sim | The simulated unit of a colony sim is people (needs, mood, stories); the simulated unit of factory automation is items and machines, with people only an optional agent. |
| City builder | The city builder's decisions are about land and zoning, testing layout and demand; factory automation's decisions are about production chains and logistics, testing ratios and throughput. |
| Sandbox building | Sandbox building sells free expression, with no capacity target you must hit; factory automation has clear progress pressure (research, climbing the tech tree, expanding deliveries). |

A self-check question: hide every throughput number and remove every enemy — does the player still have a reason to expand to a second workshop? If the answer is "no", you may be making a different genre.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **A system grown from zero**: frantic at the start, machines turning by themselves at the end; the before-and-after contrast is the player's own exhibition of achievement.
2. **An arms race of throughput**: output per minute, belt-speed utilization and power-draw curves are all visible; progress is measured in numbers and never capped.
3. **Emergent puzzles**: the bottleneck is not a problem the author posed but one the player's own factory grew; "why is it backed up" is the most long-lived daily question in this genre.
4. **Efficiency tools you can pass down**: blueprints, copying and mirroring let one solution be reused a thousand times, turning player experience into a portable asset.
5. **Long sessions, low pressure**: there is no fail state, and how long you play is set by your own capacity goals; "building all night" is the player story unique to this genre.

Benchmark titles (play them yourself before breaking them down; logistics feel and bottleneck intuition live in your hands, not in a video):

| Title | What to break down |
| --- | --- |
| Factorio | The genre definer: the full baseline for belts, recipe tables, blueprints and performance optimization |
| Satisfactory | The cost and payoff of going 3D: first-person building, vertical factories and coupling with exploration |
| Dyson Sphere Program | A leap in scale: from in-planet production lines to interstellar logistics — the Chinese-made overseas breakout benchmark |
| shapez | Minimalist refinement: combat and art stripped away, exposing the logistics logic itself |
| Mindustry | Coupled with tower defense: the production chain dragged straight onto the battlefield for inspection |
| Oxygen Not Included | The simulation layer of fluids, gases and heat: an experiment in the upper bound of pipe and system complexity |

The common thread: item conservation and visible throughput are the foundation; scale, automation and tool efficiency carry the long-term content, not story or level volume.

## 3. Design Essentials

### 3.1 The Automation Loop: Gather, Haul, Process, Reinvest

Each of the four rings has a "manual prototype" and an "automated form", and the design work lies in sequencing the handoff between the two:

| Stage | Manual prototype | Automated form | Handoff design |
| --- | --- | --- | --- |
| Gather | Hand-mining, hand-picking | Mining drills, wells, automatic farms | Have the player hand-mine for a fixed duration; hand over the cure once the pain has landed |
| Haul | Backpack trips | Belts, pipes, vehicle fleets, robots | The first belt must clearly beat hand-carrying |
| Process | Hand-crafting | Processing and assembly machines | Cap hand-crafting reps by target and degrade it into loading machines as soon as possible |
| Reinvest | Manual upgrades | Tech tree and research delivery | Every expansion must answer "what new thing does this unlock" |

Two rules: the manual phase is a design parameter, not filler — the common practice is 5–15 minutes of manual work for each new stage, with the automated cure handed over once the pain has registered; every automated step must pay off visibly (numbers go up, or the workshop looks tidier), or the player will not feel themselves getting stronger. The reinvestment gate hangs on the tech tree (§3.3): new machines, new belt speeds and new recipes are handed out on a cadence, so expansion always has a fresh reason.

### 3.2 Belts and Logistics: Thinking in Throughput

Logistics is this genre's skeleton, and all design revolves around one number: **items per minute**. Recipes, UI and player talk all use this one unit, so that ratios can be calculated in your head.

| Logistics method | Throughput magnitude | Cost | Where it fits |
| --- | --- | --- | --- |
| Basic belts | Low | Cheap, takes up space | Opening lines and tutorials |
| Upgraded belts | Doubling-tier gains | Cost jumps with each tier | The main bus and mid-to-late main production areas |
| Pipes (fluids) | High but with a flow-rate cap | Fluids only; interfaces need dedicated design | Dedicated lines for oil, water and gas |
| Robots | Flexible, point-to-point | High power draw; a performance burden at scale | Small batches, long distances, ad-hoc restocking |
| Cargo trains | Very large | High station and track infrastructure cost | Cross-region high-throughput hauling |

Structurally there are only two main plays: point-to-point dedicated lines (each line serves one consumer, easy to calculate and easy to tear out) and the main bus (one trunk carrying many item types in parallel; cheap to expand, but congestion is contagious). Both must answer the same question correctly: what is this segment's flow cap, and when will it saturate. Splitters and mergers are the cheapest design lever: get priority, filtering and even distribution right, and players' factories will grow structures the author never wrote.

Backups are made a visible state (items piling up and stopping on the belt); a backup is itself this genre's most effective feedback — it tells the player exactly where the bottleneck is. Checklist: before a new line starts, are the capacity numbers worked out (how much the downstream needs, how much this line supplies)? Does every junction on the main bus leave room for expansion? When upgrading to a higher logistics tier, is the old line converted as a whole rather than patched?

### 3.3 Recipes and the Tech Tree: A Data-Driven Recipe Table

The recipe table is this genre's content itself; every recipe goes into one table: inputs, outputs, duration, processing building, tech prerequisite. The code only reads the table — adding content means adding rows.

- Every item has at least one source and one destination; orphan items do not ship.
- By-products either have a use or can be recycled; they are never allowed to quietly disappear.
- A production chain three to five layers deep is enough for players to read (raw material → intermediates → parts → finished goods → deliverables); deeper is hard to understand, shallower leaves no room to optimize.

The tech tree governs pacing: unlock new machines, new logistics and new recipes in sequence, with one new mechanic every 15–30 minutes across the opening hours, shifting mid-to-late to "the same things, bigger". Runaway unlock pacing is this genre's most common content failure mode: give things too fast and there is nothing to do in the back half; too slow and players churn out of boredom. For teaching, make the tutorial into goals rather than a wall of text: build the first mining drill, deliver the first batch of research packs, double capacity once — the player learns without reading.

### 3.4 Blueprints and Copying: Turning Player Efficiency into Tools

A blueprint is a saveable, pasteable, shareable configuration of buildings and recipes. It changes no gameplay rules, yet it decides whether players still want to expand past hour twenty: whoever hand-places their fiftieth machine quits, and whoever copies their capacity up tenfold with blueprints starts a new save unprompted.

The tool list, in shipping order: box-select copy and paste, mirror and rotate, undo and redo, a blueprint library (save, load, name), blueprint string sharing (cross-save, cross-player). Sharing is a community-level lifeline, but it needs version discipline: blueprint encodings carry a version number, and after an update a blueprint either imports or is explicitly rejected with a reason — never silently corrupted. Two design rules: pasting validates cost (materials, footprint, tech prerequisites) and says plainly when a paste is unaffordable; blueprints store only buildings and configuration, not runtime state (items in transit, power charge), and paste semantics must be simple enough for players to predict.

### 3.5 Power, Bottlenecks and Failures: Letting the System Surface Its Own Problems

Power couples the whole factory into one system: generation, storage and consumption settle on the same grid, and blackout priority must be decided up front (protect production or protect defenses). Its role is to turn scattered production lines into a system that needs coordination, and to give expansion a global cost.

Bottlenecks are this genre's core content, and the author only has to do three things: make bottlenecks measurable (flow counters on every logistics segment, utilization on every machine), make them visible (backed-up belts, missing-material icons), and make the fixes tiered (speed up, parallelize, change tier, refactor — four options at rising cost). Keep failure design simple: blackouts, jams and resource depletion are enough of a trio, and each needs clear visual and audio signals. Do not make random-breakage punishments — players of this genre treat the factory as a work of art, and randomly destroying their work is the most hated difficulty source there is.

## 4. Technical Essentials

The engineering difficulty concentrates in four places: the simulation core, big-factory performance, blueprints and saves, and building interaction and tools. Everything below is engine-agnostic; for general methods of data-driven design and performance budgeting, see the Programming Handbook.

### 4.1 The Simulation Core: An Item World on a Fixed Timestep

- The whole factory runs on a fixed-timestep simulation clock (commonly 30–60 ticks per second, with 60 the common upper reference); production, logistics and power settle on the same clock; rendering and simulation are decoupled, and both time acceleration and headless batch runs depend on it.
- Belt simulation has two mainstream approaches: items as entities moving along the line (intuitive, detailed, expensive at scale) and compressed grid simulation (each cell stores only count and destination — fast but less expressive); big factories choose the latter or a hybrid (entities nearby, statistics at a distance).
- Item conservation is the first discipline: any bug that loses or duplicates items is top priority — it makes the entire numerical balance a rumor.
- Recipes, items, tech and power parameters all go into tables, indexed at startup and read-only at runtime; tables must support hot-reload, because tuning speed sets iteration speed.

### 4.2 Performance Engineering for Big Factories

- Scale profile: mid-to-late saves commonly hold tens of thousands of machines and hundreds of thousands of items in transit; the goal is a stable simulation rate (commonly targeting 30–60 ticks per second), not render frame rate first.
- Partitioning and activation: cut the map into chunks; static regions drop frequency or freeze wholesale; only chunks that have "something changing" consume computation.
- Statistical simulation: distant and saturated segments are computed as aggregates (a full belt is counted by flow, not moved item by item), pressing cost down from item count to segment count.
- Parallelism and batching: logistics, power and production are distributed to worker threads by system or chunk, with reads and writes separated; optimize single-threaded first, or parallelism only moves the bottleneck to thread switching.
- Render separation: no entities outside the view, batched sprite drawing and simplified detail levels; late-game the first bottleneck usually appears on the simulation side, so performance probes must see both sides at once.
- Cost budgeting: define a per-second simulation cost for each machine type and each logistics segment; before adding any system, work out "how much slower a full factory gets with it"; on the debug side, provide time acceleration, a creative mode and stable readout displays.

### 4.3 Blueprint and Save Engineering

- Blueprint serialization: encode as a string with a version number and checksum, supporting cross-save and cross-player transfer; the data holds only buildings, positions and configuration, and import validates cost and tech prerequisites.
- Save strategy: factory saves balloon with scale to a magnitude players can feel — save and load times are real bills; keep serialization compact, make autosave fast, and give loading progress feedback and version migration.
- Statistics infrastructure: items-per-minute, historical curves and flow counters are wired into the data layer from day one — they are the player's basis for diagnosing the factory and your basis for balancing numbers.

### 4.4 Building Interaction and Debug Tools

- Building interaction is this genre's first game feel: hold-and-drag to lay belts, auto-snapping and underground belts, placement previews and validity hints, undo and redo; batch building (area fill, multiplied copy) ships as early as possible — it directly sets the operating cost of a large factory.
- The blueprint toolset: copy, paste, mirror, the blueprint library, string import/export — operations must complete in seconds and give the player no reason to "rebuild by hand".
- The debugging trio: item-flow probes, power curves, bottleneck highlighting; plus time acceleration and headless batch runs (compressing long simulations to run in seconds) for automated validation of throughput tables — numerical regressions do not rely on manual testing.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimating scope; not a commitment.

| Project shape | Content scale | Time reference | Notes |
| --- | --- | --- | --- |
| Core prototype | 3–5 resources, about ten recipes, 1 belt tier | 2–4 weeks | Validates one complete "hand-crafting to automation" ring |
| Small complete title | 30–60 items, 80–150 recipes, 1 handcrafted map | 4–9 months | Small content volume, deep systems — the realistic band for an indie team |
| Typical commercial title | 100–300 items, a tech tree with dozens of nodes | 1–3 years | Once the gameplay holds, the bulk is numbers, UX polish and performance |
| Large long-run title | Hundreds of items, multiple planets or dimensions, a mod ecosystem | 3+ years of continuous operation | The content engine shifts to community and mods |

Typical cost of a single content unit (magnitudes for reference):

| Content unit | Unit cost | Notes |
| --- | --- | --- |
| One recipe | Hours | Table entry, icon, a pass through the ratio sheet |
| One machine or building | 2–5 days | Model, animation (at least idle and working states), interfaces and numbers |
| One logistics tier | 1–2 weeks | Numbers, art, interaction and performance validation for a new belt speed or new vehicle |
| One tech node | Hours to 1 day | Cheap to table and write; the hard part is the unlock pacing it pulls |
| Blueprint and copy tools | 1–2 weeks of engineering | Serialization, validation, interaction and version migration |

This genre's cost structure is the inverse of content-driven categories: few content entries, deep systems, with the money going into numbers and tools. Scheduling anchors: a playable single-ring prototype in 2–4 weeks; a vertical slice (one map, one complete tech line, blueprint tools) usually takes 4–9 months; after that, scale by content entries — but every added recipe must pass the full-chain ratio sheet, and numerical validation is the main bill.

## 6. How to Start the First Prototype

The first prototype builds only one complete small production line, finished in 2–4 weeks, without touching blueprint sharing, combat or story:

1. (Week 1) Item and grid systems: one resource, one machine, one chest — items go in and out, and the books balance.
2. (Week 1) Manual phase: 5–10 minutes' worth of hand-mining, so testers feel the pain of hauling first.
3. (Week 2) The first belt and mining drill: drill → belt → furnace → output chest, closing the first automation ring.
4. (Week 2) A delivery goal: one research or construction goal that consumes the product, giving the player a reason for the next step.
5. (Week 3) Data-driven recipe table: even with only ten recipes, they all come from one table; unlock the second machine.
6. (Week 3) Visible throughput: an items-per-minute panel plus belt flow counters, so the player can find bottlenecks themselves.
7. (Week 4) A minimal set of efficiency tools: box-select copy and paste; test, review, and only then decide whether to scale content.

Starting parameters (copy as is): 1 ore, 3–5 machines, 2 belt tiers, around ten recipes, a single grid map; machine cycles measured in seconds (commonly 1–5 s), to get the feedback cadence to stand first. Acceptance criteria (all observable):

- Testers, without reading a tutorial, can explain "why my furnace is starving" (underfed or output-jammed).
- With all art and audio removed, testers still want to double capacity once, typically in sessions of 2+ hours.
- Item conservation holds for 30 minutes of continuous running with no anomalies; the numbers balance.
- Change one recipe's output rate and you can explain its effect on the entire chain within 30 minutes.

## 7. Common Pitfalls

1. **Belts do not conserve**: items are lost or duplicated, the player's trust in the system collapses on the spot, and every balance number is void. This is the top-priority defect.
2. **Units and measures not unified**: different times and quantities are used in different places, players can never calculate ratios, and the factory turns into mysticism. Unify items per minute across the whole genre.
3. **Automation arrives too late**: the hand-crafting phase drags on into the main content and players churn out of fatigue. Every stage's automated cure arrives on a minute-level budget.
4. **Backups invisible**: it is jammed, but the player cannot find out why. Flow counters, backed-up visuals and missing-material icons are mandatory.
5. **The recipe tree is one straight line**: no trade-offs and no by-products, and after two hours it is all repetitive labor; the recipe table must grow branches.
6. **Blueprints missing or hard to use**: past the midpoint all expansion is hand-placed and the quit rate spikes; box-select copy must exist early.
7. **Late-game performance collapse**: as scale grows the simulation rate drops and players are forced to shrink their factories or quit; performance budgeting and statistical simulation are planned from kickoff (§4.2).
8. **Tech-tree pacing gaps**: everything unlocks in four hours, or two days pass with nothing new; lay out the unlock table as "one mechanic per 15–30 minutes at the start".
9. **Random destruction as difficulty**: random breakage and disaster-style punishments treat the player's work as an enemy, and players of this genre will not stand for it (§3.5).
10. **Saves and blueprints with no version migration**: after an update old factories and old blueprints are scrapped — a reputation minefield, and the player's thousands of hours of sunk cost.

## Further Reading

- Game Design Handbook: the base document for core loops, number tables and unlock pacing — the higher-level method behind §1, §3.1 and §3.3.
- Programming Handbook: data-driven design, performance budgeting and save engineering — the full expansion of §4.
- Production Handbook: content volume and scheduling methods, used with §5; time "one recipe, one machine" first, then multiply.
- Pitfalls & Anti-patterns: numbers and performance are this genre's high-frequency pitfall zones — review before kickoff.
- Case Studies: Dyson Sphere Program's overseas breakout — note the combination of "category vacuum plus engineering quality".
- Exercise 1: work out an "ore → furnace → parts → deliverable" chain in a paper table: calculate the machines needed at each stage and mark when the first bottleneck appears.
- Exercise 2: write a "throughput dictionary" for the prototype you are building: every logistics method's per-minute flow, cost and power draw, within one page.
- Exercise 3: take a big-factory save, yours or someone else's, and list three "this would not have happened if I had automated earlier" moments, then back-derive where the automation debut line should move up.

Factory automation does not sell machines; it sells the loop of "turning chaos into order with your own hands, then pushing that order toward a bigger chaos" — item conservation and visible throughput are the ground of all trust.
