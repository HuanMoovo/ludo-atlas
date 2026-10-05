# Ludo Atlas · Genre Handbooks · Survival Horror

> **Genre Handbooks · Volume 4**. Positioning: the genre that turns "resources are never enough" into an engine. Players work through a mansion inside four ledgers — ammo, medicine, inventory slots and saves — and fear is produced by poverty itself; safety is metered by the mile, and firepower is rented.
> Companions: Game Design Handbook (core loops and resource curves) · Programming Handbook (saves and enemy AI) · Level Design Handbook (miniature-garden structure and lock-and-key loops) · Case Studies (breakdown methods for benchmark titles).
> No outbound links; benchmarks list only widely known works; numbers are common magnitudes — calibrate against your own project's measurements. The general mechanics of fear (atmosphere, sound, pursuit) live on the Horror page; this page covers only survival horror's particular set of ledgers.

---

## 1. Positioning and Core Loop

In one line: survival horror is **the genre that makes scarcity its first driver**. Horror (the parent genre) sells a recipe of three raw materials — the unknown, loss of control and scarcity; survival horror tightens only scarcity to its limit and wires it into combat, space and saves: not enough ammo, so every shot is a decision; not enough inventory, so every pickup is a trade-off; controlled saves, so every death has an entry in the ledger.

The core loop as a verb chain:

`explore and keep the books → encounter a threat → fight, go around or flee → settle the cost → return to the safe room (save, organize, craft) → plan a longer route → back to exploring`

The loop closes in ten-minute units: slower than a shooter's second-scale loop, faster than survival craft's day-scale loop. It holds on four preconditions: resources stay under control at both ends (§3.1), the space is worth walking repeatedly (§3.2), enemies force players into economic decisions (§3.3), and the safe room provides a breather (§3.5). If any one fails, the genre slides away: loosen the resources and it becomes an action shooter; scatter the space and it becomes tedious backtracking.

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Horror | Horror is the parent genre, brewing emotion from the recipe of the unknown, loss of control and scarcity; survival horror tightens only scarcity to its limit, supplies the other two as usual, and makes resource management the skeleton |
| Survival craft | Survival craft's progression eventually solves the pressure (get stronger, build walls, automate); in survival horror the player must stay weak — progression buys a breather, never a comeback |
| Action shooter | In an action shooter the higher the firepower ceiling the better; survival horror deliberately lowers the firepower ceiling so "to shoot or not to shoot" is always a problem you have to do arithmetic on |
| Metroidvania | Metroidvania's revisits open the way with new abilities and progression is positive feedback; survival horror's revisits run on keys and shortcuts, and the only thing the player gets better at is map memory and route choice |

A self-check question: triple the ammo supply — is the game better? If the answer is "better", what you are making is closer to an action shooter; if the answer is "it ruins everything", scarcity is your load-bearing wall.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Choices under scarcity**: every shot fired, every medicine used, every slot spent is an entry you have to sign for; decision density is this genre's real combat.
2. **Fragile mastery**: exploration brings a sense of command (routes get familiar, supplies get fuller), but the world can revoke it at any moment; a sense of safety is billed by the minute.
3. **Spatial mastery**: turning an unfamiliar mansion into your own backyard; shortcut unlocks and map reveals must deliver real weight.
4. **Tension and release**: safe rooms and danger zones alternate — exhale at home, grit your teeth on the way out; fear is sustained by a sawtooth curve, not by holding everything at maximum.
5. **Survivor narrative**: running, scrimping and scrambling are all part of the story; the ending settles the ledger for the whole road.

Benchmark titles (a widely known list; play them yourself before breaking them down — this genre feeds on the first encounter and the feeling of poverty, so keep a spoiler-free record of your first full playthrough):

| Title | What to learn from it |
| --- | --- |
| Resident Evil (the original and the HD remaster) | The original paradigm of the miniature-garden mansion: key-based loops, ink-ribbon saves, inventory slots and item boxes |
| Resident Evil 2 (remake) | The baseline for modern resource rationing and stalker deployment; the police station is a textbook of looping space |
| Resident Evil 7 | Family-scale miniature garden and escape pacing in first person; a redesign of the save point |
| Silent Hill 2 | The boundary of the puzzle-to-exploration ratio: puzzle difficulty is adjustable, and fear does not have to come from combat |
| Dead Space | Resource suppression and no-HUD presentation in a sci-fi shell; enemy body parts are themselves a resource game |
| The Evil Within | Mismatched design of ammo and traps; improvised solutions when you're cornered |
| Outlast | The unarmed limit case: battery management and chase pacing, testing the boundary of the "loss of control" end |
| Paper Bride | Chinese folk-horror short chapters and mobile pacing; a release structure that starts free |

## 3. Design Essentials

### 3.1 Scarcity Management: The Four Ledgers

Ammo, medicine, save points and inventory slots are four interlocking ledgers; tightening one alone does nothing — only when all four are slightly taut at once does panic arrive.

| Resource | Scarcity method | Reference magnitude | The cost of losing control at either end |
| --- | --- | --- | --- |
| Ammo | Net consumption per kill stays positive: drops generally come in below consumption | Clearing a zone is deliberately made to cost more ammo than the zone supplies — only fighting selectively leaves a surplus | Loose, and clearing everything becomes the default strategy, zeroing out the tension; tight to the point of no solution, and all you have left is skipping fights and reloading saves |
| Medicine | Healing items rationed to "save you from two fatal mistakes" | 1–3 per zone, with the big heals rarer | Loose, and mistakes cost nothing; tight, and one mistake writes off an hour of progress |
| Saves | Save-point design with controlled spacing | One save point group per 10–20 minutes, or per room cluster | Too dense, and the pressure deflates; too sparse, and the death penalty becomes backtracking |
| Inventory slots | Fixed slots plus safe-room storage; how much you carry out is a decision | Commonly 8–12 slots to start, expanded 2–4 times | Always enough, and the constraint is decoration; always overflowing, and organizing replaces gameplay |

A few execution disciplines:

- Net loss is the norm, and there must be two guardrails: "run if you can't win, go around if you can't afford it" always holds (consistent with the floor in Horror page §3.1); keep guaranteed supplies in fixed locations and never use dynamic drops — leave one fixed supply point per zone. Once players see through "run low and more stuff spawns", fear turns into the anger of being gamed.
- Let resources convert into each other instead of only being consumed: crafting (gunpowder plus materials), trading, multi-purpose items — give players room to turn one resource into another. You control the exchange rates, and they are your hidden difficulty dial.
- Saves can be a resource: expendable save items like ink ribbons or tape reels amplify risk, but only suit short, hardcore-leaning runs; the common compromise for long games is free save points with a limited number of save slots.
- Acceptance criterion: in a 30-minute test, the tester should hit 2–3 "running low" moments (ammo or medicine bottoming out), but never a true deadlock.

### 3.2 Space Design: Miniature Gardens, Loops and Locks

Survival horror's spatial standard is the "miniature-garden mansion": one hub connecting several sub-areas, each with its own small loop, and the whole map's exploration order controlled by locks and keys. Space is itself the second resource ledger, because it decides how far players are willing to walk.

Draw the graph before you touch the engine: rooms, doors, keys and one-way doors all go into a node graph (methods in the Level Design Handbook), and only after the loops and locks close should you start placing assets. Get the graph wrong and no amount of beautiful assets can save it.

| Spatial device | Function | Design points |
| --- | --- | --- |
| Central hall | The whole map's memory anchor | Sub-areas branch off from it, and loop endpoints return to it |
| Loop corridor | Turns the first long walk into a short one later | One-way doors open from the inside; the unlock moment must deliver instantly felt convenience |
| Locks and keys | Control the exploration order | A key's visible range matches its target door; the span of cross-zone keys must stay restrained |
| Three-state map | The navigation language of revisits | Unexplored, still has items, cleared — readable at a glance, no walkthrough required |
| Safe room | The system anchor (§3.5) | Bound to loop endpoints, storage and saves; never placed in a dead end |

A few disciplines:

- Close the loop before the player's first "I have to walk all the way back again" moment; the usual answer: shortly after picking up the first key — one short walk — the player can open a shortcut from the other side.
- Cap backtracking time: from the farthest corner back to the nearest safe room, commonly held under 2–3 minutes; beyond that number, revisits turn from exploration into a fine.
- Give every sub-area an identifiable identity (color, materials, a signature sound); large rooms carry combat, puzzles and staging, small rooms carry transitions and resources; the re-dress pipeline (recombining the same space into multiple states with lighting and props) is the strongest lever for cutting costs — but if everything is small rooms, everything is a corridor.

### 3.3 Enemy Design: Unkillable, Manageable, Outmaneuverable

Enemies are this genre's largest expense, so manage them as three roles, each with clear deployment discipline:

| Role | Can it be killed? | The player's solution menu | Deployment discipline |
| --- | --- | --- | --- |
| Unkillable (stalker) | No | Hide, run, slow it down with the environment | Appears on a 15–30 minute cadence, offset from the main scares; at high frequency, pressure turns into irritation |
| Manageable (standard enemies) | Yes, but every kill is a losing entry | Fight (pay ammo), avoid (pay familiarity), lure (pay items) | Clearing them out is always possible and always a bad deal; deployment density back-calculated from ammo income |
| Outmaneuverable (mechanic enemies) | Mostly not, or need not be | Study the pattern, close doors, use traps, avoid certain time windows | Carry tutorial and low-intensity stretches; their rules must be repeatable by players |

- Write an economic formula for every enemy before it ships: average kill cost, average drops, detour cost — three numbers into the table, with deployment back-calculated from the formula. Rare enemies get rare drops, and a few fights should be worth taking; keep ordinary enemies at "covers a little, never enough to spend".
- Few but excellent enemy types: the common scope is 4–6 basic enemies plus 2–3 boss fights; each needs its own tactical identity (weakness, cost, the context it appears in); filler enemies only dilute the animation budget and the fear at the same time.
- A stalker's rules must be readable: its appearance signal, escape conditions and patrol range stay consistent throughout. Players may fear it, but they must be able to reason about it (chaser behavior and AI design are in Horror page §3.3 and §4).

### 3.4 The Puzzle-to-Exploration Ratio

Combat density is low in survival horror, and the campaign is carried by exploration and puzzles. A typical mix for an 8–10 hour campaign:

| Segment | Common share | Function | Cost of making it thin |
| --- | --- | --- | --- |
| Exploration and revisits | 30%–40% | Spatial learning, resource gathering, route planning | The mansion loses its sense of place, and loops come for free |
| Puzzles | 15%–25% | Downshifting the pace, lock-and-key progress, the payout point for resource rewards | The campaign degenerates into one long monster-fighting corridor |
| Combat and evasion | 25%–35% | Cashing out resources, pressure peaks | The numbers stop balancing and scarcity stops working |
| Narrative and staging | Around 10% | Motivation and per-stage settlement | Players don't know why they are making this trip |

- Four puzzle types: fetch (keys, badges), mechanism (sequences, circuits, counterweights), combination (using crafted items), and environmental reasoning (reading traces and light signals). The first two are cheap and stable, the last two expensive but brilliant; mix them by budget — don't bet everything on one type.
- A single puzzle commonly runs 5–15 minutes; past 15 minutes of being stuck there should be tiered hints (a nudge, a clear statement, the answer outright). The hint layer is churn-prevention infrastructure, not cheating.
- Puzzles and exploration must feed back into the systems: pay puzzle rewards in hard currency like ammo, capacity upgrades and keys — puzzles that only yield story notes get skipped. Give every room at least one of the three: a progression item, resources, or a narrative trace; rooms with none of the three get deleted or merged into a neighbor.

### 3.5 Sound and Pacing: The Safe Room Is the Metronome

The safe room's three functions (recovery, organization, anchor) match Horror page §3.5; survival horror must additionally stuff two systems into the same room: saves and storage. Only when every reason to "go home" is concentrated in one place does the metronome stand firm.

- The excursion radius widens ring by ring: the first ring is two or three rooms, the second half a floor, the third crosses zones. The reasons to turn back are three needles: health, ammo on hand, inventory headroom; the three needles must be directly visible on the HUD, letting players make the "one more room" call themselves at the junction — this is the genre's core act of self-regulation.
- The distribution of safe rooms sets the breathing rhythm: commonly 2–4 per map, plus more when crossing zones; between two safe rooms there should be exactly one full unit of tension.
- Sound is the sound of the ledgers: enemy footsteps layer progressively closer (distant, next door, same room), pickup sounds are income cues, and the audio of door locks and save machines is process language; the safe room's music is made as its own set, crossfading smoothly across the door — that is the promise of "you're home", and it must be honored reliably, never randomly broken. The full sound discipline is in Horror page §3.4; here, one point is worth stressing: save the silent stretches for the moments when resources are running out.
- Pacing checklist: mark the "depart, explore, return home" beats of a full run on a timeline, and check whether safe-point intervals are even, whether each excursion lasts longer than the last, and whether the three reasons for returning rotate. Use the same reason three times in a row and the rhythm becomes mechanical shuttling.

## 4. Technical Essentials

The engineering difficulty concentrates in four areas: saves and state, inventory and items, enemy AI and deployment, and putting the resource economy into data. No engine is a barrier — Godot, Unity and Unreal can all get you started; what you must build yourself is save serialization, the item system and deployment tools.

**Saves and state**

- Choose the save scheme first: save-point style (typewriters, tape recorders and the like) amplifies resource and death risk and suits this genre; autosave checkpoints lower the risk and suit lighter directions. When unsure, ask one question: is the stretch players replay after dying a punishment or a review? Difficulty options hang here too, which fits the genre's language better than tying them to enemy health: whether saves consume resources, auto-aim strength, puzzle tier.
- Register state in one place: door locks, item pickups, enemy deaths and story flags all centrally registered; loading a save must never produce the tell of "a door I opened is locked again".
- Saves must restore something close to the original scene: enemy positions and aggro states, items on the ground, inventory layout. The player's first ten seconds after loading must connect seamlessly to the moment before saving.

**Inventory and item system**

- Grid-style (each item occupies cells) or slot-style (fixed positions) — choose by product direction: grids strengthen trade-offs and the ritual of organizing, slots lower the operating cost; the common compromise is a grid base plus a quick bar.
- Organizing must feel smooth: drag, rotate, sort, take in bulk; organizing is itself part of the gameplay (a breather, in fact), but it must not become an operating burden — test gamepad and mouse-and-keyboard separately.
- Item descriptions are a hidden guidance layer: writing what an item is for and where it goes ("useful on a certain door") measurably cuts stuck time; write them like clues, not like manuals.

**Enemy AI and deployment**

- Three enemy roles, three implementations: standard enemies use a state machine (patrol, sense, attack, death); stalkers additionally need whole-map pathfinding, cross-zone memory and appearance rules (scripted spawn points plus cooldowns); mechanic enemies are essentially a set of readable switches.
- Deploy through tools, not scattered triggers: one table governs spawn points, patrol routes, appearance conditions and cooldowns; tuning deployment without touching scene files — efficiency is quality.
- Stuck-prevention is mandatory: cover pathfinding tests for doors, stairs and narrow corridors; a stalker stuck on a door for three seconds does more damage to immersion than one that can't catch you.

**Putting the resource economy into data**

- Ammo, medicine, drops and healing — income and outgo all go into one numeric table, with a debug panel that exports the player's stock curve in real time; the test dashboard additionally logs kills, detours, ammo income and spend, death locations and causes of death, so one completed run can be read against the target curves. Without quantification you cannot tune the "tight but not dead" feel.
- The balance safety valve: when the deadlock combination of "resources bottomed out plus enemies dense" is detected, the guaranteed supply at a fixed location catches the player — never secretly retune drops as dynamic compensation.

## 5. Content Volume and Workload Reference

The following are common magnitudes for projects of this kind, for scope estimation; not a commitment.

| Form | Content volume | Playthrough length | Timeline magnitude | Notes |
| --- | --- | --- | --- | --- |
| Prototype | One small floor (8–12 rooms), one stalker, one resource set | 15–30 minutes | 3–6 weeks | Validates only resource pressure and looping |
| Short-form title | 2–3 zones, 4–6 enemy types, 8–12 puzzles | 2–4 hours | 6–12 months | One thematic art set; suited to a first project |
| Typical indie scope | 5–8 zones, 6–8 enemy types, 20–30 puzzles | 6–10 hours | 1.5–3 years | Rooms and puzzles are the cost centers |
| Larger scope | A 10+ hour campaign | 10+ hours | Multiple years | Needs mechanical variety to offset fatigue |

- The cost unit is the room: a room's full cost is the sum of art, lighting, sound, puzzles and enemy deployment; whiteboxing is fast and detailing is slow, with a blow-up factor commonly 1:3–1:5 (the same magnitude as the Horror page). Environment reuse is the strongest lever — build the re-dress pipeline first.
- Enemies are the most expensive single assets: a complete move set (intro, locomotion, attack, hit reaction, death) often eats the bulk of the animation budget; lock the roster to few and excellent, and never add monsters mid-production.
- Puzzle costs are often underestimated: a puzzle includes the mechanism, hints, failure states and testing, and full polish commonly estimates at 3–7 working days; make five first to validate your puzzle-design instincts, then produce in bulk.
- Duration discipline: 8–12 hours is the common comfortable ceiling for premium titles; stretching it longer must come from mechanical and spatial variety, never from longer corridors (for scope calibration see Case Studies and Indie Survival).

## 6. How to Start the First Prototype

Goal: 3–6 weeks to build a "half-hour small floor" that validates three things: whether resource pressure bites, whether the looping space is fun to walk, and whether the stalker holds up its end. Don't touch production art or story.

| Milestone | What to build | Acceptance (watch behavior, not surveys) | Reference time |
| --- | --- | --- | --- |
| M1 Whitebox floor | 8–12 rooms, two loops, two locks | With all enemies off, testers willingly explore and can sketch the layout from memory | 5–8 days |
| M2 Resources and inventory | Ammo, medicine, slots, one safe room (saves plus storage) | Testers hesitate over pickups and usage, and can explain their trade-off reasoning | 5–7 days |
| M3 The enemy trio | One standard enemy, one stalker, one detour route | Fighting and detouring both hold up; after being pushed back by the stalker, testers can restate its rules | 5–8 days |
| M4 One key and one shortcut | A key, a door, a loop that opens from the other side | Testers find the key themselves and open the shortcut with it, without asking | 3–5 days |
| M5 Wrap-up and testing | Pacing layout, guaranteed supplies, 3–5 outside playtesters | Someone says "I don't dare push my luck" and heads back to the safe room on their own; someone dies and understands why | 4–6 days |

Three rules:

1. All art stays placeholder: tension comes from ledgers and space, not textures; suppress the urge to beautify until the gameplay has passed testing.
2. Err tight on resources in the first version: a tight build exposes structural problems, while a loose one only earns false praise; tightening until deadlocks appear and then backing off beats starting out generous.
3. Ask only three questions each test round: Why is he saving? Why does he dare go far? What is he calculating when he comes home?

Success criteria (all observable):

- At least 3 of 4 testers complete the half-hour run without hints; 2 or more "running low" moments occur, but never a true deadlock.
- Nobody treats clearing all enemies as the default strategy (the ammo ledger doesn't support it), and nobody sprints through ignoring resources (the medicine ledger doesn't support it); after testing, players can still restate the location of one shortcut and one stalker rule.

## 7. Common Pitfalls

1. **Too much ammo**: once the drop rate exceeds consumption, clearing everything becomes the default solution and the fear floor is locked to the firepower ceiling; fix the resource table before you talk atmosphere.
2. **Inventory constraints as decoration**: always enough or always overflowing — neither produces a decision; the constraint must bite at the level of "medicine or ammo".
3. **Save spacing out of control**: too dense deflates the pressure, too sparse turns death into a backtracking tax; design by room cluster, not by a number pulled out of the air.
4. **Stalker overuse**: glued to you the whole time, appearing with no signal — irritation will eclipse fear; it should be like a bill, arriving on schedule, not every day.
5. **Loops turning into backtracking**: shortcut unlocks with no immediately felt convenience, keys spanning too far, backtracking time inflates, and the player starts to hate the mansion.
6. **Puzzles disconnected from resources**: puzzle rewards are only story notes, and puzzles degrade into campaign interstitials; wire the rewards back into ammo, capacity upgrades and keys.
7. **No help when stuck on a puzzle**: without a tiered hint layer, thirty minutes stuck is the quit point; hints are not cheating — they are churn-prevention infrastructure.
8. **"Avoid fighting when you can" read as license for rough combat**: fighting is still the high-frequency verb, and bad game feel detonates all at once when a fight is forced; it can be shallow, but it must not be unpleasant.
9. **Rooms as beads on a corridor**: no hub, no sense of territory, no recognizability — players can't remember the way, and revisits become torment.
10. **Selling the room count**: repeated corridors don't pile up playtime, only fatigue; fear intensity is extremely sensitive to repetition — choose short and dense over long and sparse.

## Further Reading

- Game Design Handbook: core loops, resource curves and numeric-table methods; §3.1's ammo and medicine rationing gets its tables built there.
- Programming Handbook: engineering details of save serialization, item systems and AI state machines; the full expansion of §4.
- Level Design Handbook: miniature-garden structure, lock-and-key graphs and revisit guidance; the expansion of §3.2.
- Case Studies: breakdown methods for benchmark titles; pair with Indie Survival and Pitfalls & Anti-patterns when calibrating scope.
- Homework: write down a 30-minute "resource ledger" for your prototype (starting stock, pickups, consumption, balance), then break down the first mansion section of a benchmark title and draw its lock-and-key graph and ammo income-spend curve; read the two charts against each other and you will see whether your numbers run loose or tight.

Survival horror ultimately tests only three things: whether players are reluctant to fire every shot, whether they remember every shortcut, and whether they can breathe easy when they get home. When all three hold, scarcity performs the fear all by itself.
