# Ludo Atlas · Genre Handbooks · Tower Defense

> **Genre Handbooks · Volume 1**. Positioning: the tower defense development page, from paths and tower tables to wave curves, covering the core loop, the counter matrix, economy, tuning and how to begin a prototype.
> Companions: Game Design Handbook (balance and economy) · Level Design Handbook (pacing and paths) · Programming Handbook (pathfinding and performance) · Pitfalls & Anti-patterns.
> This page deliberately carries no links. Half of tower defense design lives in tables; if a tower table is badly tuned, no amount of analysis reading will help.

---

## 1. Positioning and Core Loop

Tower defense took shape in direct connection with the Warcraft III custom-map ecosystem: maze building, wave systems and difficulty curves all grew out of that batch of maps. In one line: **lay out defenses under limited resources, trading purchasing power and space for defense strength**. Players do not control units; they make three kinds of decisions: what to build, where to build it, and when to upgrade. The rules are simple; the difficulty is that the three decisions constrain one another.

The underlying pleasure is solving a spatial problem with a budget: the enemy route is known, tower prices and abilities are known, and the player has to find a viable combination "within these few waves". Once the combination clicks, the surface-level satisfaction has somewhere to land.

The core loop within a run:

`read the preview → spend on defenses → start the wave and clash → settle gold and leaks → adjust the layout → next wave`

Four nested layers of the loop:

- Second scale: a tower's shot, hit and kill feedback — impact feel lives at this layer.
- Minute scale: a wave's defense layout and settlement — the main decision layer.
- Level scale: a map's full curve, new tower unlocks, star ratings.
- Meta progression: chapter advancement, tech trees, endless-mode records.

Boundaries against neighboring genres: tower defense does no unit control, which is RTS; tower defense combat resolves automatically after the defenses are set, which puts it in the same family as auto battlers. Typical variants: fixed paths (Kingdom Rush, Carrot Fantasy), maze building (Gem TD), towers mixed with operators (Arknights), long-term progression plus an endless mode (Bloons TD 6). Plants vs. Zombies is closer to lane-style defense, sharing most of tower defense's design language.

## 2. Player Experience Goals and Benchmark Titles

Write the experience goals down first; every later decision gets checked against them:

- The thrill of intelligence and prediction: "I knew this wave would bring fliers, so I added anti-air at the corner in advance" — a win before the wave even starts.
- From three leaks to zero leaks: a clearly better run on the same map in the second game; the sense of growth comes from the player's own choices.
- The satisfaction of automated defense: watching your own crossfire grind through an entire wave.
- Build identity: the tower combination used this run is the player's own solution, not a standard answer copied from a guide.

Benchmark titles (all directly playable; play them before reading):

| Title | What to learn from it |
| --- | --- |
| Plants vs. Zombies | Lane defense, the sun economy and card cooldowns; a textbook of onboarding and pacing |
| Kingdom Rush | Fixed paths and tower-slot design, hero and ability pairing, mobile control feel |
| Gem TD | Maze blocking and random combining; the building rules are themselves the gameplay |
| Bloons TD 6 | An extremely long upgrade tree and long-term balance; how co-op and endless modes stay alive |
| Carrot Fantasy | Lightweight level wrapping: lowering the difficulty barrier while keeping the strategy |
| Arknights | Operator facing, path blocking and redeployment; tower defense fused with long-term progression |

## 3. Design Essentials

### 3.1 Paths, Maps and Blocking Rules

Everything starts from a node graph: spawn point, base, path nodes (n1, n2, …), connecting edges, and tower slots attached to edges or nodes. The node graph is both a design document and program data; each node records its coordinates, traversal width, adjacency and tower-slot count. Terrain and decoration wait until after gameplay validation — get the function working first.

```text
spawn → n1 ─┬→ n2 → base
            └→ n3 → base
```

The figure above is a two-route node graph: it splits in two at n1, and the two stretches each lead to the base. It can also be designed to fork first and merge later; the merge point is the most valuable tower slot (one tower covering two routes). A single-route map is just one branch removed.

Multiple paths (parallel routes, forks, merges) create resource-allocation problems: enemies come down two routes at once, there is only enough money to defend one, and the player must rank and choose — the meatiest class of decision in tower defense.

Three ways to handle blocking rules:

| Rule | Approach | Fits | Risk |
| --- | --- | --- | --- |
| Blocking allowed | Towers may be built on the path surface, but at least one traversable route must remain; sealing the path off forbids placement | Maze building, the highest strategic depth | High pathfinding and balance cost, heavy validation |
| Blocking forbidden | Fixed paths; tower slots are preset spaces | Easy to balance and art-direct; suits lightweight and narrative-driven titles | One less layer of strategic depth |
| Dynamic penalty | Blocking is allowed, but cutting the shortest path carries a price: a gold deduction, extra enemy health, enemies rerouting, or temporarily disabling the blocking tower | Balances freedom and control | With opaque rules, players feel arbitrarily punished |

Three details that are easy to overlook:

- Maps that allow blocking must validate the path: before placement, run a pathfind from spawn to base; if there is no solution, reject it.
- Cap the payoff for lengthening the route: a 20% longer trip is a 20% longer firing window and must not become an exploit for stalling indefinitely.
- Path stretches have different characters: curves suit slows and melee splash, straights suit pierce and long range. "Where is worth spending money" must be readable at a glance on the map.

### 3.2 The Tower Counter Matrix

You do not need many towers; each should own a stretch. Five functional roles are basically unavoidable:

| Role | Strongest against | Weak against | Key parameters | Common forms |
| --- | --- | --- | --- | --- |
| Single-target burst | Elites, bosses, high-health slow targets | Crowds of small enemies, where damage overkills badly | Damage per shot, attack speed, range | Sniper towers, heavy cannons |
| Area splash | Dense squads, crowds of small enemies | Single high-health targets, where firepower efficiency is poor | Splash radius, edge falloff | Mortars, flamethrowers, magic circles |
| Slow/control | Everything high-threat, creating windows for damage towers | Almost no return when standing alone | Slow percentage, duration, coverage | Frost towers, webs, swamps |
| Anti-air | Flying units | Ground units (half efficiency or unable to attack) | Target filtering, priority, vertical range | Flak cannons, archers |
| Buff/debuff | Amplifying existing firepower, marking vulnerability | Nearly useless used alone | Aura radius, amplification percentage, duration | Amplifier towers, vulnerability marks |

"Countering" is at bottom the matching of target structure to tower role: many low-health units fear splash, few high-health units fear single-target, fast runners fear slows, fliers fear anti-air. For every new enemy, write down clearly what it counters and what counters it before putting it into the wave table.

Range versus attack speed (at similar price and DPS):

- Long range buys coverage windows: it covers several path stretches and corners, at the usual cost of slow attack speed or a high unit price.
- High attack speed scales harder with damage multipliers and switches targets flexibly, at the cost of low per-shot damage and weakness to high armor; low attack speed with high per-shot damage tends to overkill fast runners and wastes badly on dense targets.
- The only trustworthy comparison standard is effective DPS: sheet DPS × hit rate × the share of time targets spend inside the range × switching losses. A tower whose effective DPS you cannot calculate has not been tuned.
- One rule of discipline: no tower may be best on range, attack speed, DPS and price all at once; every tower must have a situation only it can handle.

### 3.3 Economy: Sell-Back Ratios and Interest

The default is one main resource (gold). The discipline on resource types is less is more: every extra currency adds a production line, a display slot and a tutorial lesson, and is only worth adding if it creates a "you must pick one" trade-off. The two most common directions for a second resource: base health (a measure of tolerance for error), or population and power (a cap on the total number of towers).

Common ranges for sell-back and pricing:

| Action | Common value | Design intent |
| --- | --- | --- |
| Build | Baseline price, the anchor | All pricing is expressed relative to it |
| Upgrade | Each level costs 80%–150% of the previous level's price | Controls the slope of the growth curve |
| Sell-back | 60%–80% of cumulative investment, commonly 70% | Leaves room for trial and error without making constant re-layout free |
| Misclick refund | 100% refund within 3–10 seconds of building | Fixes slips of the hand without punishing misclicks |
| Full sell-back between waves | Forbidden in most titles, allowed in a few | When allowed, "sell everything and re-lay each wave" becomes the dominant play; enable with care |

Interest-style mechanics (settled each wave on the remaining balance, commonly 5%–10%, with a per-wave cap):

- Purpose: gives "saving" a legitimate strategy and a trade-off against "buying towers", so the early game is not all hoarding or all spending.
- Risk: when interest returns exceed tower returns, saving instead of building becomes the only solution, and the first few waves spin their wheels.
- Limiting measures: exempt interest in the early game, pay interest only on savings above a safety line, or decay interest as waves go on.
- Check method: compare the marginal return of "each gold spent on towers" against "each gold saved for interest"; the two must be on the same order of magnitude with interest slightly lower, making saving a transitional strategy rather than an endgame one.

Economy sync check: list expected income and expected spending for every wave. The first 3 waves must be able to buy the standard answer (one basic tower plus one upgrade); in the midgame every wave must contain at least one purchase decision that makes the player hesitate.

### 3.4 Wave Curves

Single-wave pressure can be roughly quantified:

`wave pressure ≈ the wave's total health ÷ the player's theoretical DPS potential at that moment`

(Add further corrections for speed, count structure and armor; account for flying units separately via anti-air coverage.)

A 10-wave introductory curve laid out by this standard:

| Wave | Content | Purpose |
| --- | --- | --- |
| 1 | 5 slow infantry | Tutorial; validates the first tower |
| 2 | 8 infantry | Validates upgrade returns |
| 3 | Fast runners appear for the first time | A new question: slows or high attack speed |
| 4 | Infantry and fast runners mixed | Validates combinations |
| 5 | Breather wave: a small squad that hands over gold | Economy top-up and pressure release |
| 6 | Flying units appear for the first time | The anti-air question; preview it in wave 5 |
| 7 | Elite: a high-health single target | Validates single-target firepower |
| 8–9 | Mixed composition, sustained pressure | The combined pressure peak |
| 10 | Boss: high health plus one mechanic | Chapter climax and settlement |

A few principles:

- Pressure rises overall, with breather waves sandwiched in between. Continuous high pressure slides the player from tension into numbness; a breather wave is also the window for topping up the economy.
- Introduce only one new enemy at a time. Every new enemy is a new question (flying, shields, healing, splitting, stealth, speed), and two questions in a row teach nothing.
- Elites and bosses need mechanics, not just health pools. Pick one of regeneration, summoning, charging or shielding allies, and preview it one wave ahead with an icon.
- Leak punishment comes in two kinds: one leak is a loss (the high-pressure type), or base health (the forgiving type, commonly 10–20 points). The latter is more common: it allows "running wounded" and makes failure more dignified.
- Do not make difficulty options all health multipliers. Three tiers: Easy (health ×0.8, income ×1.1), Normal (baseline), Hard (health ×1.3, starting funds −20%, enemy affixes). Affixes are more interesting than multipliers, and sell better.
- Leave a place in the clear rating for "zero leaks": the main line guarantees a clear, and perfect ratings are reserved for challenge-driven players.

### 3.5 Balance Tuning: Build the Tables First, Then Test

There is only one order: paper simulation → engine testing → player testing. Doing it backwards will crash you.

Build two tables first:

- Tower table: role, range, attack speed, damage per shot, DPS, price, upgrade curve, plus effective-DPS notes.
- Wave table: wave, enemy composition, count, per-unit health, total health, speed, armor, gold reward.

The first pass happens in the tables: estimate the player's DPS pool from "the best tower set the previous wave's income can buy", treat tower DPS × wave health as mental arithmetic, and keep each wave's "total health ÷ damage output" between 1.0 and 1.3. Below 1 is a walkover; sustained above 1.5 drives players away; the player's optimization space hides in that margin.

The second pass runs in the engine: finish the debug commands before the content (skip wave, add gold, invincibility, speed-up, batched enemy spawning). After every run, record three lines of data: leaks per wave, remaining gold, first tower type purchased.

The third pass brings in outside players: say nothing, just watch. Record three things: the wave where they stop following (an onboarding problem), the failure they cannot explain (a fairness problem), the tower nobody ever buys (a balance problem).

Log one line per change: what changed, why, and how it turned out. This is the defense against flip-flopping; for the related pitfalls see Pitfalls & Anti-patterns.

## 4. Technical Essentials

- Data-driven design is the baseline: towers, enemies, waves and economy parameters all go into tables (CSV, JSON or engine table assets), and code only reads tables. Any value hardcoded in a script becomes an incident later.
- Two path implementations: fixed paths use a waypoint array with enemies moving along the points in order; blockable maps use a grid with A* or a flow field, recomputing only the affected local region after each build.
- Path validation: before placement, run a pathfind from spawn to base; if there is no solution or it times out, reject it. Dynamic-penalty rules deduct or announce the cost at this step.
- Performance checklist: object-pool enemies, projectiles and damage numbers; throttle target acquisition by re-selecting targets every 0.1–0.2 seconds instead of every frame; use a spatial grid or quadtree for range queries; batch damage resolution. Hundreds of enemies on screen at once is the passing grade for tower defense; general methods are in the Programming Handbook §3.
- Separate logic from presentation: the simulation layer runs on a fixed timestep and the presentation layer subscribes to events for animation and audio. The payoff is that you can speed up, replay, and run automated tests with no rendering.
- Headless batch simulation: add a greedy AI (buy towers by priority whenever there is money), play thousands of games automatically, and output the average leak rate per wave. Unbalanced waves surface on their own; this is the most valuable internal tool in tower defense.
- Saves: in-run state (towers, gold, current wave) serializes easily, and mid-run saving is worth doing; mobile reconnect-after-drop is half of the same requirement.

## 5. Content Volume and Workload Reference

| Tier | Content list | Solo time reference |
| --- | --- | --- |
| Gameplay prototype (greybox) | 1 map, 3 towers, 10 waves, no production art | 1–2 weeks |
| Vertical slice | 3 maps, 6 towers, 20 waves per map, 3 enemy families, 1 boss | 2–4 months |
| Small commercial scope | 15–25 levels, 8–12 towers with upgrades, three difficulty tiers, achievements and an endless mode | 6–12 months |
| Long-running mobile scope | Continuous updates of towers, maps, events and seasons | Not applicable; teams of 5–15 |

Cost structure:

- The most expensive parts are towers and enemies: every tower needs four visual sets — build, upgrade, fire, destroyed — multiplied by upgrade tiers and skins; every enemy needs three sets — walk, hit, death.
- The cheapest part is maps: terrain kits are reusable, and one map's art cost is far below one tower's.
- The hidden bulk is tuning: over half of the prototype phase goes into tables and testing; when estimating, do not treat "the towers are done" as "it's done".
- The multiplication trap: towers × enemies × maps explode combinatorially, while validation is additive. Every new enemy means a pass over the wave tables of every map; that is the real maintenance cost.

## 6. How to Start the First Prototype

Work through this in order; do not skip steps:

1. One page of rules: path type (fixed or blockable), one resource, win and loss conditions, the role split of three towers.
2. Greybox one map: one S-shaped path, 10 tower slots, a spawn point and a base.
3. Implement three towers: single-target (arrow tower), area (cannon tower), slow (frost tower). Skip anti-air and buffs for now.
4. Write a 10-wave wave table: infantry ramping through the first 3 waves, fast runners in wave 4, a breather in wave 5, an elite in wave 7, a mechanic-driven boss in wave 10.
5. Put every parameter into tables, with the full set of debug commands (skip wave, add gold, speed-up).
6. Play 3 games back to back yourself, then have 3 people each play one (you stay quiet beside them) and record the sticking points.
7. Based on the notes, adjust only three things (prices, health, map), then return to step 6 for another round.

A set of starting parameters you can copy as is (small 10-wave map):

- Starting gold 100. Arrow tower 50 (DPS 10), cannon tower 80 (DPS 12, small splash), frost tower 60 (30% slow, no damage).
- Three enemy tiers: infantry 60 HP, runners 40 HP at ×2 speed, brutes 200 HP; the boss uses 8× infantry health with a regeneration mechanic.
- Per-wave income: roughly 30–60 gold from kills in total; 5% interest, capped at 10 gold per wave.
- Acceptance criterion: within ten games, an outside player has at least one loss where they know why they lost, and one win where "I defended this wave in advance".

## 7. Common Pitfalls

1. Building six or more towers in the first version: none of them are good enough, and players cannot remember them. Start with three, each with its own signature situation.
2. Tuning numbers straight in the engine without building tables: change one thing and three break; after enough back-and-forth, nobody knows what the right numbers are.
3. Allowing blocking without path validation: a player seals the whole route; at best the run is stuck, at worst pathfinding crashes.
4. Sell-back too low: a wrong purchase cannot be fixed, so the run gets restarted; too high, and selling is free, so decisions lose their weight.
5. Interest too high: "save instead of building" becomes the only solution from the start, and the first few waves spin their wheels.
6. Difficulty that only adds health: ten times the health is ten times the boredom. Changing enemy composition, speed or affixes all beat piling on health.
7. No breather waves: players go numb by wave four, and later climaxes can no longer land.
8. A boss that is just a big health pool: a five-minute punching-bag post is worse than three medium bosses with mechanics.
9. Fliers arriving out of nowhere: an air raid with no anti-air tools and no preview is simply unfair — a hot zone for negative reviews.
10. Balance validated only by the developer: the author knows every counter relationship; outside players quit by wave 4.
11. Upgrades that are only percentages: an upgrade tree of +10% damage carries no sense of decision; upgrades must give qualitative change (new targets, new effects, new range brackets).

## Further Reading

- Game Design Handbook §4: spreadsheet methodology (tables before code) and economy sources and sinks — the higher-level method behind every table in this page.
- Level Design Handbook §4: intensity curves and pacing tools, which map directly onto wave sequencing.
- Programming Handbook §2, §3: core systems checklist and performance engineering, matching this page's technical essentials.
- Pitfalls & Anti-patterns §2, §3: high-frequency pitfalls on the design and programming sides, including balance flip-flopping and path validation.
- Exercise 1: recreate the pacing of Kingdom Rush's first map (three towers, ten waves), aiming for "the player feels stronger within three games".
- Exercise 2: write Gem TD's blocking rules as a spec document: what is allowed, what is forbidden, what happens when the rules are violated — detailed enough to start coding from directly.
- Exercise 3: run a headless batch simulation on the map you are working on, find the three most unbalanced waves, then make changes.

Tower defense game feel comes from tables and real testing. Tuning one table until you cannot stop is worth more than reading ten analyses.
