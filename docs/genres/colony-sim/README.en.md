# Ludo Atlas · Genre Handbooks · Colony Sim

> **Genre Handbooks · Volume 2**. Positioning: don't play a hero — direct a group of people with minds of their own as they try to survive in a dangerous world. The player is a planner and a responder; the story isn't written, it grows out of the interplay between needs, moods, events and responses.
> Companions: Game Design Handbook (core loop and narrative systems) · Programming Handbook (AI agents and performance) · Production Handbook (scope and estimates) · Case Studies (long-project retrospectives).
> No outbound links in this document. Benchmark titles are limited to widely known works — play anything you haven't played before you study it. All numbers are order-of-magnitude references; your own project's measurements are the standard.

---

## 1. Positioning and Core Loop

One-line positioning: a colony sim is a genre about **managing a group of individual agents**. There is no protagonist; the object of control is a camp and every person in it. Individuals have their own needs, moods and skills; they eat, sleep and work on their own, and get themselves into trouble on their own too. The fun comes in two layers: being the manager (planning, assigning, optimizing) and being the responder (a crisis arrives — how do you take it). Its baseline difficulty sits in the higher band of the genre matrix, because four hard problems arrive at once: individual simulation, emergent narrative, performance and saves.

Drawing boundaries with neighboring genres:

| Neighboring genre | Boundary |
| --- | --- |
| Survival crafting | There the player chops the trees and builds the house; in a colony sim the colonists do the hands-on work, and the player decides "who goes, and when" |
| Management / city builder | There you manage abstract resources and statistical curves; a colony sim goes down to "a named person missed a meal today and argued with their roommate" |
| RTS | RTS units are expendable numbers; a colony sim's individuals are assets and story carriers — the death of one named person is an event |
| 4X / grand strategy | There you steer empires at long distance; a colony sim usually goes deep around one settlement and a few dozen people |

A self-check question: replace the individual simulation with anonymous numeric labor — does the game still hold up? If the answer is "no", you're making a colony sim.

The core loop as a verb loop:

`plan and build → assign work → individuals live their own lives (eat, sleep, socialize) → events and threats interrupt → respond and clean up → expand and upgrade → heavier threats`

The loop nests, and every layer needs a hook:

| Layer | Duration (real time) | What the player is doing | Resolution point |
| --- | --- | --- | --- |
| Minutes | once every dozen seconds or so | One decision: take this job or not, fix this wall or not | Immediate feedback |
| Day | 10–30 minutes | A stretch of routine plus one event | Event ends, log updates |
| Week | Several hours | A build phase: housing, defense, heating, medical care | Milestones (new room, new tech) |
| Whole run | Tens of hours | From castaway to fortress | "The story is told" or rebuild |

Before starting work, nail down three questions: what shape a run takes (endless sandbox, finite goals, or staged narrative beats); the target band for colony size (commonly a dozen to a few dozen people, see §4); and where pressure comes from (the outside world, internal emotions, or an alternation of the two). The three answers determine the shape of every system that follows.

## 2. Player Experience Goals and Benchmark Titles

Players come to this genre for four things, ranked by priority. Note that the third and fourth naturally fight each other — you must pick a side; wobbling pleases neither:

| Experience goal | In the player's own words | Where design pushes |
| --- | --- | --- |
| Story ownership | "This is **my** story" | Named individuals, causal events, a log you can reread |
| Management pleasure | "Put every person where they belong" | Work priorities, zones, automated facilities |
| Crisis response | "The raid is here — who do I save first" | Event strength matches strength; multiple solutions, recoverable |
| Attachment and loss | "I can't accept that he died" | Relationship webs, skill specialization, gravestones and memorials |

Benchmark titles (widely known samples only; structural differences matter more than quality rankings):

| Title | Core stance | One move worth learning |
| --- | --- | --- |
| RimWorld (also translated as "Edge World" in Chinese) | The definer of the story-generator paradigm | Weaving random events into stories with "pacing strategy + event pool + strength evaluation" |
| Dwarf Fortress | The ceiling of simulation depth | "Losing is fun": the world exists before the player, and dying meaningfully is content too |
| Prison Architect | A small-site sample of needs and policy | Turning the "needs → policy → feedback" chain into a readable UI system |
| Oxygen Not Included | Physics simulation stacked with colony management | Pressure from coupled systems (gas, temperature, liquids), not foreign enemies |
| Against the Storm | An in-run variant of the colony loop | Using a roguelite run structure to solve "late-game bloat and runs that go too long" |

These five share one premise: individuals have needs and emotions, and stories grow out of the systems. Copy their "system density", not their "first version".

## 3. Design Essentials

### 3.1 Individual simulation: needs, moods and skills

The individual is the genre's smallest narrative unit and its largest cost item. Get the trio standing first:

**Needs**: each need is a quantity that decays over time, and the decay rate sets the pace. Ship needs and solutions as pairs — a need with no solution is pure punishment. A common list:

| Need | Satisfied by | Penalty line | Design notes |
| --- | --- | --- | --- |
| Hunger | Eating | Low value drops mood; zero harms health | The most common early interruption; slow the decay |
| Sleep | Sleeping | Sleep loss drops mood and productivity | Differentiate bed quality |
| Rest/recreation | Leisure facilities | Too little recreation breeds slow depression | Comes online mid-game; prevents "nothing to do once the work is done" |
| Social | Chatting, gatherings | Loneliness drops mood | The story engine of the relationship web (see §3.4) |

**Mood**: the weighted sum of need satisfaction, plus event modifiers (positive and negative buffs). Mood is not decoration; it's an instrument you can intervene on:

- Thresholds must be layered: low mood warns first, then moves into "breakdown behavior" (going berserk, binge eating, running away, brawling); after a breakdown, give a recovery window (sleep, medicine, talking it out) — don't destroy the character in one stroke.
- Every modifier must be traceable: "why is he in a bad mood" must have an exact answer, otherwise players will treat the system as a random number generator.

**Skills and traits**: skills determine work speed and quality, with interest bonuses that speed up learning; traits modify behavior rather than just numbers (a lazy person works slower, and also spends more time on recreation). Together they create **difference**; difference creates division of labor, and division of labor creates stories: "our only doctor is injured" is a hundred times better than "medical throughput down 20%".

### 3.2 Work assignment and priorities

A colony sim's management layer has only three levers: who goes (grouping), what they do (work types), and what comes first (priorities). All of it revolves around one work table.

- Make work types a list (harvesting, construction, hauling, cooking, medical, combat and so on; 10–20 kinds is common); every individual has a level and a toggle for each type. Simple priority tiers (disabled, low, medium, high — 3–5 levels) beat pseudo-continuous percentages for readability, and the defaults must be designed — otherwise the first thing a newcomer sees is colonists running around at random.
- Assignment must support batching and templating (grouping people, job presets, copying settings); give "waiting" visibility — who is slacking, who is stuck, visible at a glance — so players don't read system problems as a broken AI.

### 3.3 The story generator: event-driven narrative

The idea in one sentence: **don't write plots; write systems that generate plots**. What players want is not set pieces the writer scripted, but a story that "only I went through, this run". In implementation it's a trio:

1. **Strength evaluator**: compute a strength value for the colony (population, wealth, equipment, defenses) — the metronome of the event system. RimWorld's approach lets threat strength follow colony wealth, so "the richer, the more dangerous": every asset the player stockpiles is turning into future trouble.
2. **Event pool**: events tiered by type (threats, opportunities, trivia) and strength, with combinable trigger conditions (season, weather, location, prerequisite events).
3. **Pacing strategy**: one event system — change the pacing and you change the experience. Build one each in steady escalation, long respite and irregular styles, and let the player choose at the start, or unlock them with difficulty.

Stories grow out of systems via two amplifiers:

- **Relationship web**: individuals' social ties grow automatically (friends, lovers, enemies); arguments, reconciliation and the death of loved ones are all inherited — a free story engine.
- **Records and presentation**: event logs, family trees, gravestones and memorials translate the system's "output" into a "story" the player can retell. The log itself is a narrative interface; a simulation that isn't presented equals one that didn't happen (see §3.5).

### 3.4 Events and randomness: the pressure curve of danger events

Events are a colony sim's "levels". The randomness players accept layers like this:

| Randomness layer | Content | Function | Consequence of losing control |
| --- | --- | --- | --- |
| World generation | Map, companion traits, starting location | Defines "this run's problem" | The run is doomed from the start (no food, no mining area) |
| Process randomness | Events, weather, disease, visitors | Creates pace and surprise | Events chain-fire; the player fatigues or goes numb |
| Outcome randomness | Hits, item quality, surgery success | Creates tension | Save-scumming to reroll; tension hits zero |

Four rules for the pressure curve (same lineage as the intensity curve in the Level Design Handbook):

- Strength tracks power, not a timetable: threat tiers are chosen from the strength evaluation; no wipe-tier event in the first 30 minutes.
- Leave breathing room between peaks: after every major event, a calm production stretch; long respites alternate with crises.
- Major events get advance warning: scouting reports before an ambush, a season-change notice before winter. Invisible disasters are a bad-review magnet.
- Give the death spiral a stop-loss exit: one broken link triggering a cascade (food cut off, everyone weakened, even less able to produce) is this genre's classic loss of control. Keep at least one lifeline: ally relief, caravans, difficulty options, retreat and rebuild.

One more source of randomness needs restraint: **retries**. Single-player players will reload saves, so downweight the randomness that can be farmed (outcome randomness gives only small modifiers, not success or failure) and upweight the randomness that can't (world generation, events). Reload to reroll, or take the gamble — that's a design stance, and it has to be settled in advance.

### 3.5 Boundary control for emergent narrative

Emergent narrative collapses in two directions; boundary control guards against both.

**One end is numbness**: the system is running, but the player doesn't perceive it. Symptoms: mood drops and the player never knows; events happen and the player doesn't care; the story exists only in the log. Countermeasures:

- Visible state: every abnormal status must lead to its cause and its exit within one or two clicks.
- Filter the output: the presentation layer keeps only "tellable stories" (named, causal, consequential) and lets trivia sink into the log; every event must map to at least one player decision (prevent, respond, clean up) — an event that maps to none is noise.

**The other end is loss**: the player loses control, and the narrative becomes bullying. Symptoms: accidents that can't be prevented, punishments that can't be undone, being forced to watch your life's work ground up by a random number. Countermeasures:

- Interruption budget: cap the number of forced interruptions to the player's flow per unit of time; trivia doesn't pop up.
- Tiered failure: from injury and lost property, to buildings destroyed, to death — penalties escalate tier by tier; every tier gets a recovery window, not a one-step leap.
- The player is one of the authors: every crisis has at least two solutions (tough it out, dodge, negotiate, flee); single-solution high-pressure events only at rare major beats.
- Closing rituals: loss must be tellable — gravestones, relics, naming the next ship after the dead — turning loss into a story's ending instead of the delete key.

There is only one self-check: after a playtest, ask the player to retell "what happened this run". If they can't tell a story, then however complex the system is, it isn't converting into narrative.

## 4. Technical Essentials

A colony sim's engineering pain concentrates in the simulation loop (tick), individual AI, pathfinding, saving and performance — all engine-agnostic; this section gives structure only. One baseline runs through every system: be data-driven — individuals are not scripts but combinations of data components and behavior systems; this is the precondition for mods and a long community tail (see the Programming Handbook and the Modding & UGC handbook).

**Simulation loop and tick strategy** (the balance point between counts and performance):

- Logic runs on a fixed-step tick (30–60 Hz is common), decoupled from rendering; simulation quantities split into frequency layers: position and execution high-frequency (every tick), needs and mood evaluation downclocked (once every 0.5–2 seconds), and macro quantities like crop growth, temperature and economy at the lowest frequency (seconds or coarser).
- **Time slicing**: give every individual a nextThink timestamp and spread decisions across frames; never "evaluate all individuals in the same frame". Worth doing at a few dozen individuals; at a few hundred, skipping it guarantees stutter.
- **Simulation LOD**: downclock individuals far from the player's view, or compute them as events only; sort visitors and enemies by necessity.
- Use **utility scoring** for the decision architecture, not hard-coded state machines: score every candidate behavior by need urgency, run the highest; interrupt and re-evaluate when a need crosses a threshold or a goal goes invalid. State-machine branch explosion is the number-one technical debt in projects like this.
- Write the per-frame millisecond budget into the design doc: how much individual AI and pathfinding get; when it's over, downclock or downgrade — don't "add machines".

**Pathfinding and space**:

- One shared walkability graph (grid or hierarchical), not each individual holding its own terrain data; work and rest are just points and regions on the graph.
- Pathfinding cache: cache paths per region and recompute only when the goal changes; large maps use hierarchical pathfinding (a room graph plus grids inside rooms); doors, furniture and deconstructable buildings change the graph dynamically — mark the affected regions dirty when the graph changes instead of recomputing the whole map.

**Saving**:

- A save is the entire world: map cells, individuals, items, event state and the random seed, serialized in full. Carry a version number and a migration function from day one; old saves must be able to upgrade when data structures change; corrupted saves are a bad-review magnet.
- Save size grows with items and map, so items must stack and compress; autosave writes to disk asynchronously (write to a temp file first, rename on success, preventing corruption on crash). Multiplayer (if any) is another order of magnitude: get single-player right first, then evaluate sync granularity (see the Multiplayer & Backend handbook).

## 5. Content Volume and Workload Reference

The following are common magnitudes for projects of this kind, for scoping estimates — not a commitment.

| Content unit | Unit cost (order of magnitude) | Minimum viable | Commercial scale | Notes |
| --- | --- | --- | --- | --- |
| One simulation system (needs, work, combat, medical, etc.) | 1–4 weeks | 5–7 | 12–20 | None is hard alone; the cost is in system coupling |
| One event (with conditions and outcomes) | 2 hours–2 days | 20–30 | 80–200 | Writing, balance and testing each get a pass |
| One item and recipe | 1–4 hours | 60–100 | 200–400 | Icon and balance included |
| One work type | Half a day–2 days | 6–10 | 15–25 | Priorities and animation included |
| Writing one trait | 0.5–2 hours | 30–50 | 100–200 | Cheap and story-dense — make more |
| One faction / creature | 1–3 days | 3–4 | 8–15 | Behavior logic and balance included |
| First-run length | 10–20 hours | 30–60 hours | 100+ hours | In sandbox form, the player decides |

A few order-of-magnitude conclusions:

- The cost structure is "front-heavy, then long": the simulation skeleton (needs, work, pathfinding, event system) is the big front load; after that comes continuous content and balancing (events, items, updates) with no end point. Budget visualization and tuning tools for the strength evaluator: balancing is a bottomless pit, and tuning it all by feel will spin out of control late.
- RimWorld was led by one developer and spent years in early access; Dwarf Fortress has run for over twenty years with two developers. Any "make a RimWorld in half a year" estimate: multiply by three, then multiply by three again.
- Compression priority, high to low: cut map size, merge factions and creatures, cut items and recipes, cut event count. **Never cut the depth of individual simulation** — that's this genre's selling point; rather half the content than lose the feeling that "the people live on their own".

## 6. How to Start the First Prototype

Goal: two weeks to a month for the minimal loop of "one colonist living on their own". Placeholder art, one room, one person.

| Milestone | What to build | Acceptance (watch behavior, not questionnaires) | Reference time |
| --- | --- | --- | --- |
| M1 A colonist who lives | Two needs (hunger, sleep), plus eating and sleeping, plus pathfinding | Leave it alone and the colonist finds food and a bed | 3–5 days |
| M2 Three people and division of labor | Work priorities plus 2–3 work types | Change a priority and watch behavior change with it | 5–7 days |
| M3 Mood and log | Mood system plus event log plus state inspection | The player can say "why he's in a bad mood" and fix it successfully | 3–5 days |
| M4 One threat and the clean-up | One raid or disease, plus medical care and recovery | After the crisis ends, the player can tell what happened | 5–7 days |
| M5 Building and saving | Placement and demolition, plus full saves | Close and reopen: the world is still there; pick up yesterday's work | 5–7 days |

Startup discipline:

- Settle "the shape of a run and the fail condition" before writing a line of code (endless sandbox and finite goals mean completely different event systems); at every scale tier, play it for an hour yourself first and answer only one question: "Did anything worth telling happen in this hour?"
- No art, no multiple settings, no big maps; externalize the data tables from M1 on (needs, work, traits). This genre's first pleasure is "watching the colonists live" — validate that first.

## 7. Common Pitfalls

1. **Individual AI written as hard-coded state machines**: branches grow exponentially; after the fifth system nobody dares change anything. Switch to utility scoring plus data tables (§4).
2. **Unreadable mood system**: a colonist breaks down and the player can't look up why. Every modifier needs a source; thresholds need layers (§3.1).
3. **Event strength ignoring player strength**: devastating early, boring late — both directions are failure. Build the strength evaluator first (§3.3).
4. **Events chain-fire with no respite**: the player goes from anticipation to numbness — narrative fatigue. Put the interruption budget into the design doc (§3.5).
5. **Irreversible death spiral**: food breaks and everyone weakens, and the comeback gets harder and harder. Keep at least one rescue channel (§3.4).
6. **Work-priority defaults left undesigned**: newcomers see colonists running around and decide "the AI is dumb". Defaults are part of the product.
7. **Evaluating all individuals in full every frame**: a few dozen people stutter to unplayable. Use all three tools — frequency layers, time slicing, simulation LOD (§4).
8. **A simulation with no presentation layer**: rich content the player can't perceive equals work not done. Logs, alerts and status panels are core systems, not UI odds and ends (§3.5).
9. **Saving taken lightly**: full world state plus later structural changes equals corrupted saves. Version numbers and migration functions from day one (§4).

## Further Reading

- Game Design Handbook: the core loop, system interlock and narrative sections are the draft under §3.
- Programming Handbook: methodology for AI agents, pathfinding and performance budgets — the full expansion of §4.
- Production Handbook: estimating, scope control and long-horizon scheduling; complementary to §5.
- Case Studies: find the simulation- and building-genre breakdowns, and study the real numbers on content consumption speed and update cadence.
- The Tarn Adams profile in Indie Developer Profiles: a sample of a twenty-year solo marathon, Dwarf Fortress style.
- Pitfalls & Anti-patterns: project management and collaboration pitfalls — check them one by one at kickoff review.
