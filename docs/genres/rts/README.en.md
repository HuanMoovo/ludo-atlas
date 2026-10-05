# Ludo Atlas · Genre Handbooks · RTS

> **Genre Handbooks · Volume 2**. Positioning: running the three timelines of economy, production and combat at the same time — accumulating an advantage through management and cashing it out through execution; one of the real-time genres with the highest ceilings and the heaviest engineering load.
> Companions: Game Design Handbook (economy and counters) · Level Design Handbook (maps and pacing) · Programming Handbook (pathfinding and performance) · Multiplayer & Backend (match play and sync).
> This page deliberately carries no links. Half of an RTS's fun lives at the controls, half in the number tables, and both can only be verified by hands-on testing — there are no shortcuts.

---

## 1. Positioning and Core Loop

In one line: an RTS is the genre that **runs the three timelines of economy, production and combat at once under real-time pressure**. Management decides how much you own; execution decides how much of it you cash out; the two axes score separately, yet must be played at the same time. This is what fundamentally separates it from turn-based strategy (you can think slowly) and the MOBA (you manage a single hero).

The core loop, written as a verb chain:

`scout the map → gather and expand → build units and climb the tech tree → harass or engage → account for losses → adjust unit mix and expand → engage again`

How fast this loop spins is the player's own choice: the cautious player spins slowly but every step is solid, while the aggressive player spins fast with little margin for error. Good design makes both speeds work.

Four time scales: the second scale (micro, pulling wounded units, body-blocking, focus fire — the layer where the execution ceiling lives); the minute scale (build order, expansion, harassment and skirmishes); the match scale (tech routes, army composition, the timing of the decisive fight); the meta scale (map pool, balance patches, seasonal ranks).

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| MOBA | You control only one hero, with no base management and no multi-front management; you could say the MOBA is the RTS made by subtraction. |
| Tower defense | Once defenses are placed, combat resolves automatically; tower defense is a test of placement, an RTS a test of execution. |
| Real-time tactics (RTT) | No gathering or construction; resources are fixed within the level, leaving only combat and objectives. |
| 4X and grand strategy | Turn-based or pausable, allowing slow deliberation; in an RTS, the real-time pressure is itself a source of fun. |

A self-check question: take execution away — is management still fun? Take management away — is execution still fun? Both must have a yes for it to be an RTS; if only one does, what you are building is a different genre.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **A sense of command over management**: an advantage traces back to concrete decisions; losses are understood, wins are clear.
2. **The thrill of execution cashing out**: box-selecting, flanking, saving wounded units, multi-front play — hand speed and proficiency convert directly into results.
3. **The intelligence duel**: scouting and counter-scouting; the moment you read the opponent's intent ahead of time is more thrilling than any single big engagement.
4. **Masterable depth and immersion**: one map supports thousands of matches, skill grows measurably, and replays and reviews are the main path; the construction and advance from bare ground to a full army is narrative in itself.

Benchmark titles (play at least 20 full matches of each yourself, then compare against expert replays):

| Title | What to learn from it |
| --- | --- |
| StarCraft / StarCraft II | Asymmetric races, the execution ceiling, scouting and opening systems; the precedent for esports-grade balance maintenance |
| Warcraft III | Hero units woven into armies, two-front control, the map editor ecosystem |
| Age of Empires II / Age of Empires IV | Economic pacing and age advancement, wall and siege play; playable at a low execution floor |
| Command & Conquer: Red Alert 2 | Fast pace and blunt counters, the satisfaction of base building, the benchmark for rush pressure |
| Company of Heroes | Cover and squad systems, capture-point economy — terrain turned into the main variable |

## 3. Design Essentials

### 3.1 Units and the Counter Matrix

An RTS unit is essentially **a set of functions under time and resource constraints**. Define roles first, numbers second; if the roles are not clearly divided, no amount of number tuning will save it.

| Role | Best against | Loses against | Key parameters |
| --- | --- | --- | --- |
| Gathering unit (worker) | Does not take part in frontline combat | Every combat unit | Gather rate, round-trip time, survivability |
| Frontline melee | Soaking fire, blocking positions, tying up ranged units | Area splash, being kited | Health, armor, slow or net |
| Ranged damage | Slow melee, targets without cover | Fast chargers, flankers | Range, fire rate, wind-up |
| Anti-armor | High-armor units and fortifications | Cheap swarms | Armor-piercing method, anti-armor multiplier |
| Siege | Buildings and fixed defenses | Mobile forces | Anti-building multiplier, range, mobility |
| Air | Lineups with no anti-air, rear-area raids | Dedicated anti-air fire | Speed, capacity, ground-attack ability |

Four disciplines for counter design:

- **Counter multipliers need a ceiling**: the common practice is a damage swing of ±30% to ±50%, not three or five times. When the gap grows too large, numbers and execution lose meaning, and matches degenerate into rock-paper-scissors over unit choice.
- **Counters must be visible**: armor types get icons and sound effects, so players can guess correctly within two engagements without consulting a table.
- **Every unit needs a one-line job description**: a unit for which you cannot write the situation where it is indispensable gets cut. Of six units, three being useless is a common way for first projects to die.
- **Symmetric first, asymmetric later**: get matches running end to end on one shared unit skeleton in the initial version, then build faction-exclusive units; balancing multi-faction asymmetry costs far more than one faction.

Calibrate in seconds: record three numbers for every unit — seconds to kill a standard target, seconds to be killed by a standard target, and seconds to cross a map. Lock combat duration first; health and damage are merely its derived results.

### 3.2 Resource Gathering and Build Order (Economic Pacing)

Choose the economy model first, then talk numbers:

| Model | Approach | Reference titles | Notes |
| --- | --- | --- | --- |
| Worker round-trip gathering | Workers gather at resource nodes and carry loads back to base; nodes deplete and force expansion | StarCraft, Age of Empires | The most intuitive and the easiest to quantify; you must manage worker routes and node layout |
| Capture points with steady output | Holding points yields continuous income, and points change hands | Company of Heroes | Economy tied to the frontline, forcing players to seek fights; high demands on point layout |

Variants also include the Warcraft III-style gold plus lumber and Age of Empires' multi-resource system; every added resource type means another tutorial line and another UI slot — one or two is enough at the start.

Pacing design for the build order:

- The first 3 minutes allow "playing by the script": give a standard opening with 20–30 second precision, then leave two or three branches (how to switch to defense against a rush, how to respond to an opponent's expansion). Newcomers use it to get in; veterans use it as a yardstick.
- The mid game must produce real decisions: when income exceeds current production capacity, force the pick-one-of-three — expand, climb the tech tree, or mass units and push out. Each option must be genuinely viable; none may be dominated.
- The economics of harassment must be calculable: killing one worker costs not just its build price but the gathering time it represents; write "one worker equals how many seconds of income" into the table so players can feel the return on harassment.
- Resource nodes going from dispersed to concentrated or depleted naturally pushes the match toward a late-game decisive fight; the map decides "when you must fight".

Three phases of the economy:

| Phase | Income profile | What the player should do | What to watch |
| --- | --- | --- | --- |
| Opening (0–3 minutes) | Income small and steady | Memorize the standard opening; scout | Floating resources that can't be spent |
| Mid game (3–12 minutes) | Income exceeds what a single base can consume | The expand/tech/army choice | Does a "you must choose" moment appear |
| Late game (past 12 minutes) | Nodes concentrated or depleted | Decisive fight, lockdown, base raids | Comeback space before the decisive fight |

Anti-snowballing is an inherent RTS problem: the leader snowballs ever larger while the trailing player has a bad time. Common mitigations: upkeep or supply tax, escalating expansion costs, dispersing resource nodes so secondary bases are hard to hold, and capping harassment returns. Small teams should get 1v1 on a small map solid first and leave free-for-all and team modes for later — the complexity of snowballing and balance doubles there.

### 3.3 Execution and Controls

Execution is the only interface between the player and the simulation, and it must serve two things at once: give experts something to do (the ceiling) and keep newcomers from bouncing off (the floor).

| Interaction | Design point | Common failures |
| --- | --- | --- |
| Box selection | Combat units take priority; double-click selects all of a type; modifier keys separate workers from army | Overlapping units can't be picked; the selection result isn't what was expected |
| Control groups | Number-key groups with clear add, remove and replace rules; whether a dead unit's slot is preserved | Group order jumps around; new units automatically squeeze into old groups |
| Group movement | A large army needs subgroups and formations, not one blob; facing should be assignable | Armies jam into a queue at bridges and shove each other in chokepoints |
| Pathfinding | Units must never deadlock; when stuck they must auto-repath or detour | Spinning in place, jittering along walls, staring through walls |
| Command queue | Shift-queue multiple orders; the queue is visible and cancellable | Orders silently swallowed; the player has no idea where the unit went |
| Attack behavior | Attack-move, focus fire and hold-formation each get a hotkey slot | Units auto-chase enemies to the far side of the map |

The floor and the ceiling of execution:

- The floor: never force players to compete on hand speed. Low-execution paths must also be able to win — positional play, fortifications and letting the opponent break on prepared defenses all count; Age of Empires' long macro games and Red Alert's defensive counter-attacks are the soil this style grows in.
- The ceiling: pulling wounded units, flanking, multi-front harassment, managing two battlefields at once — these must cash out into clearly visible advantages, or experts have no room to separate themselves.
- One discipline: any moment where player intent and the result diverge (wrong selection, wrong path, stuck unit) is treated as a defect; "the player doesn't know how to play" is never an explanation.

Acceptance criteria: a mixed force of around 100 units moves and fights without jamming, crashing or large-scale idling; when 5 new players first command a large army, none of them has more than 2 "I thought it would go there" moments.

### 3.4 Scouting, Vision and Intelligence

- An RTS is an information game: the part of the map you can see equals the decision space you can act in — fog of war range, vision radius and detection range are three numbers that decide "who knows first".
- Scouting tools come in three layers: cheap early scout units, mid-game watchtowers and detectors, and late-game anti-stealth tools; every layer must carry a cost.
- Scouting returns must be readable: on seeing the opponent climb the tech tree, the player should immediately understand "their army is thin right now".
- Counter-scouting matters just as much: cloaking, disguise and feints make deception a legitimate strategy; an RTS with no room for deception turns matches into open-hand slugging.

### 3.5 AI and Difficulty Design

AI has two faces: to players it is opponent and teammate; to developers it is the cheapest tester. The design priority is to raise behavior quality first, then talk about difficulty tiers.

- Difficulty without cheating: players notice resource bonuses, full map vision and damage buffs quickly, and once trust breaks it never comes back. Prioritize making the AI genuine at scouting, expanding, switching composition to counter, and retreating when it should.
- The tier gap comes mainly from "how many mistakes the AI makes", not "how much money the AI has": lower difficulty makes it slow to react, unwilling to expand and unwilling to pivot; higher difficulty makes it commit fewer mistakes. Cheat parameters are an honest option only at the top tier, and are labeled clearly.
- AI and players share the same rules and the same simulation: the same pathfinding, the same economy formulas, the same data tables. That is what makes it a credible opponent — and lets it serve as a balance-testing tool on the side: when tuning balance, run batch matches and tally win rates and unit-type distributions (see §4).

## 4. Technical Essentials

The engineering difficulty concentrates in four areas: simulation architecture, group pathfinding, the command system and the toolchain. The following is engine-agnostic and can be implemented in any engine.

**Simulation architecture**

- Logic frames and render frames are decoupled: the simulation advances at a fixed step while rendering runs at whatever frame rate; game-feel interpolation lives in the presentation layer. Even if version one ships no multiplayer, write the simulation to be reproducible (fixed step, controlled random sources) — replays, spectating and reconnection all stand on this; violate it, and both multiplayer and replays get rebuilt from scratch (see Multiplayer & Backend §2).
- All units are data-driven: health, damage, armor, range and cost go into tables and code only reads them; balance iteration edits tables without rebuilds. For table methods see Game Design Handbook §4.1.

**Group pathfinding and movement**

- A three-layer structure: global pathfinding (flow fields or hierarchical pathfinding) decides "where to go", local avoidance decides "how to yield", and individual units self-recover when stuck. With only one layer, jams are guaranteed.
- Flow fields update incrementally by region: when a building goes up, recompute only the affected regions, not the whole map.
- Give crowd handling its own budget: test passage through chokepoints, bridges and doorways separately; push and yield parameters are part of the game feel, and large-army movement assigns target slots instead of sending every unit at the same coordinate.

**Command and selection system**

- The selection system handles priority and subgroups: after box-selecting, a key cycles subgroups (melee group, ranged group), and orders are dispatched per subgroup; the command queue must be visible, cancellable and insertable — it is the vehicle of multi-front play, and it must never silently drop orders.
- The entire hotkey system is customizable: construction, production, abilities, control groups — this is the accessibility floor for an RTS.

**Performance, tools and networking**

- Budget-driven: define the budget for "units on screen × per-frame simulation time", then back-derive AI decision frequency; throttle targeting and thinking to once every 0.1–0.5 seconds, never per frame. Units, projectiles and effects all use object pools, and rendering goes through instanced batching.
- Debug commands before content: add money, skip tech, reveal the map, game speed, direct unit spawning. Without them, every test session is spent hand-running the management loop.
- Batch-match tooling: run hundreds of AI matches with rendering off or at high speed, and output win rates and unit-type distributions — imbalance surfaces in the statistics first; build the replay system early, since it is both the player's review tool and the evidence for bug-hunting and balance.
- Settle the networking model early: the classic answer for an RTS is lockstep (sync only inputs, clients replay), at the cost of floating-point determinism and very difficult reconnection — but replays come almost free; state sync is more conventional, and bandwidth and prediction correction for large unit counts must be measured. The evaluation checklist is in §2; in sequencing, get the single-player simulation and AI working first, then attach the network layer.

## 5. Content Volume and Workload Reference

The following are common magnitudes for projects of this kind, for estimating scope; they are not commitments.

| Project shape | Content scale | Timeline scale | Notes |
| --- | --- | --- | --- |
| Gameplay prototype (1v1 vs AI) | 1 faction, 4–6 unit types, 1 symmetric small map | 2–4 months solo | Economy, pathfinding and controls working end to end |
| Small complete title (single-player leaning) | 2 factions, 8–12 unit types, a 10–15 mission campaign, skirmish AI | 1–2 years for a small team | Content accumulates linearly; mostly levels and scripting |
| Competitive multiplayer title | 2–3 factions, 15–20 unit types, 5–10 maps, matchmaking and anti-cheat | 2–4+ years for a team | Balance and service are long-term bills |

Art scale: 2D units multiply by facing — 8 directions times 4–5 actions is dozens of animation sets, putting one unit's art load close to an entire platformer protagonist; start with 4 directions or mirrored sprites to make up the count, then fill in after validation; 3D units save on facing (just rotate) but pay for rigging and animation blending, and buildings and effects likewise multiply by "faction × tier". Balance scale: the cost of one numbers change is "edit the table, run batch matches, watch replays"; each version touches only a few parameters, with a log kept.

How single-player campaigns and multiplayer divide the engineering load:

| Dimension | Single-player campaign | Multiplayer (ranked included) |
| --- | --- | --- |
| Cost shape | Content cost, growing linearly with mission count | Systems cost, growing with player population |
| Core work | Maps, scripting, cutscenes, difficulty validation | Balance, matchmaking, anti-cheat, network sync, spectating and replays |
| Delivery and risk | Can be finished in one push; content is the safe part | The meter starts at launch; network and economy security are ongoing investment |

The pragmatic path for a small team: start with "campaign plus skirmish AI", run friend matches on lobby-based or host-authoritative setups, and leave dedicated servers, matchmaking and seasons until after validation. The service-layering order on this route (accounts, rooms, matchmaking, game servers, leaderboards) and the cost ledger are fully laid out in Multiplayer & Backend §3 and §8 — read them once before you start.

## 6. How to Start the First Prototype

The first prototype validates exactly one thing: whether a 10-minute 1v1 skirmish holds up. Scope is locked: 1 faction, 5 unit types (worker plus melee plus ranged plus siege plus scout), 1 symmetric small map, 1 primary resource plus a supply cap. No multiplayer, no campaign, no saves, no final art.

- **Weeks 1–2: economy.** Worker round-trip gathering, resource nodes, supply cap, four building types (main base, supply, production, defense). Goal: run the full chain of gathering, construction and unit production by hand.
- **Weeks 3–4: units and execution.** Counter relationships for the 5 unit types, box selection and control groups, group pathfinding, damage and death. Goal: 100 units move as a group without deadlocking.
- **Weeks 5–6: AI and win conditions.** A skirmish AI that can gather, build, scout and attack, plus three difficulty tiers. Goal: a full match can be played to completion.
- **Weeks 7–8: testing and tuning.** Run batch AI matches to tune numbers; put 3–5 people in front of the build and log where they stall. Goal: testers finish a full match within 15 minutes and can explain clearly why they lost.

Starting parameters (one small map; copy them directly and adjust):

- Starting workers 4–6, with opening resources worth roughly two or three workers' cost; a gathering round trip takes 5–8 seconds and carries back 5–8 resources. Supply cap 50–100, unit costs 25–150, and the first combat unit on the field within 90 seconds.
- Target match length 8–15 minutes; ship exactly one win condition at first: "destroy the main base".
- Cut the three difficulty tiers at the behavior level — whether the AI scouts, whether it pivots, how fast it reacts — far more interesting than simply changing gather rates.

Acceptance criteria (all observable):

- An outside tester, with no instructions, completes gathering, construction, unit production and combat within 15 minutes.
- A ~100-unit melee doesn't drop frames or deadlock; pathfinding has gone through at least one fix pass.
- Testers who lose to the medium AI can say clearly whether they lost on management, execution or unit composition.
- You yourself are willing to play 3+ matches in a row; if the prototype isn't fun, content volume can't save it.

## 7. Common Pitfalls

1. **Many units, none with a signature moment**: three of six units are stat reskins, and matches only ever use two of them. Give every unit its indispensable moment first.
2. **Going multi-faction asymmetric from the start**: balance cost grows with the number of combinations, and a small team gets dragged down immediately. Get a symmetric skeleton working first, then break it into asymmetry.
3. **Adding units before pathfinding works**: units jam doorways, circle aimlessly, stand around doing nothing — players have zero tolerance for "not obeying orders", and it is the number-one source of bad reviews.
4. **An economy with a single optimal solution**: openings become rote memorization, and players churn before they ever practice execution. Keep at least two viable routes, each with its strong and weak phases.
5. **AI cheating caught red-handed**: extra money, map reveal, ignoring fog — players feel it quickly; tune difficulty through behavior first, and keep cheating only as the top tier's honest option.
6. **No low-execution path**: a hand-speed barrier locks out most potential players; fortifications, positional play and counter-punching — leave at least one route that can win.
7. **No scouting system**: with no way to read the opponent's intent, matches degenerate into rock-paper-scissors; fog of war, scout units and watchtowers need to be designed as a system.
8. **Numbers hard-coded in scripts**: changing one line of numbers requires a rebuild, and balance iteration bogs down into mud; units, tech and economy must all be data-driven.
9. **Multiplayer before AI**: multiplayer is a systems engineering project, while AI is single-player content and a testing tool in one; get the order backwards and neither gets finished — do the reading before you go online.
10. **Chasing "absolute balance"**: perfect balance doesn't exist; hold the floor first — no unbeatable opening, no useless unit — then approach it in small steps through version updates.
11. **Match pacing out of control**: a suffocating game with no contact in the first ten minutes, or a three-minute all-in that decides everything; use resource distribution and harassment returns to tune pacing toward the middle.

## Further Reading

- Game Design Handbook §4: number-table methodology, economy systems and balance methodology — the parent methods for this page's counter matrix and economic pacing.
- Level Design Handbook: map metrics, sightlines and pacing tools — the general foundation for RTS map design.
- Programming Handbook §2, §3, §5: core systems, performance budgets and networking basics — the counterpart to §4 of this page.
- Multiplayer & Backend §2, §3, §8: sync model choice, service layering and the cost ledger — required reading for RTS networking engineering.
- Pitfalls & Anti-patterns §2, §3, §8: high-frequency pitfalls on the design, programming and networking sides.
- Indie Survival: scope control and scheduling — the expanded ledger for §5.
- Exercise 1: write a counter matrix for five units, then run 50 AI matches to verify "no invincible unit".
- Exercise 2: build a group-movement test scene (bridge crossing, chokepoints, weaving through obstacles) and fix the stuck count to zero.
- Exercise 3: break down a replay of a top-player match, recording both sides' income and army size every 30 seconds, plot the two curves, and find the minute where the game turned.

The fun of an RTS lives in execution; the craft lives in the tables. Tune five units until they hold each other in check first, then talk campaigns and esports.
