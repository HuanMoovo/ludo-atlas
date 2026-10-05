# Ludo Atlas · Genre Handbooks · Tactics / SRPG

> **Genre Handbooks · Volume 4**. Positioning: making "arranging your forces" the first pleasure, using action economy, turn order and probability on a grid to turn every attack into a reviewable choice. This page covers action systems, classes and counters, the feel of hit rates, levels and reinforcements, permadeath and leniency, and scope references for small teams.
> Companions: Game Design Handbook (core loops and number tables) · Level Design Handbook (maps and encounter pacing) · Programming Handbook (turn-based architecture and AI) · Indie Survival (scope and scheduling).
> This page carries no external links; benchmark titles are widely known works only, and the figures here are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: Tactics / SRPG is **the turn-based tactics genre that makes position and turn order themselves the core resource**. Every attack spends actions, every move changes next turn's options; the pleasure comes from the closed loop of "predict, execute, cash in", not from hand speed or execution precision.

Two schools share one underlying skeleton: the SRPG school — Fire Emblem, Super Robot Wars and Final Fantasy Tactics — draws its long-term motivation from character growth and narrative; the tactics school — XCOM, Advance Wars and Into the Breach — concentrates the test in the puzzle-solving depth of a single map. Both share the same base: grid, actions, probability, resolution.

The core loop, written as a verb chain:

`scout the enemy and terrain → read the objectives and constraints → deploy and maneuver → attack and resolve (hit, counter, kill) → enemy turn → assess losses and reinforcements → revise the plan`

The tempo is in the player's hands: the steady player establishes formation before advancing, the fast player sends mobile units straight for the objective; good design leaves both approaches room to live, but neither comes free.

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| JRPG | Turn-based combat is an exchange of skills and resources, and positioning is usually abstract; tactics makes position itself the primary variable. |
| Auto battler | An auto battler resolves itself once the setup is done; in tactics, every move must be executed and adapted by the player in person. |
| RTS | RTS's real-time pressure is the point; tactics lets you think slowly and tests operational planning, not hand speed. |
| 4X and grand strategy | Strategic-layer management belongs to 4X; the tactics board is a single level, at squad scale. |

A self-check question: if combat resolved fully automatically and the player could only deploy and watch, would the game still stand? If the answer is yes, what you are building is an auto battler or an idle game; the pleasure of tactics must live in the manual decision of every single move.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **A sense of operational control**: victory and defeat trace back to concrete deployments and trade-offs; a loss shows you which move was wrong, and a restart begins with a definite conclusion.
2. **The drama of decisive rolls**: a hit landing in a desperate situation, the suspense of a pivotal miss — the emotional peaks unique to turn-based combat; the premise is honest probability (§3.3).
3. **Attachment to your units**: units gain experience, change class and swap gear, and the player feels responsible for "the squad I raised" — the SRPG's long-term engine.
4. **The thrill of beating the odds**: turning the battle around through terrain, counters and coordination is the classic highlight scene of tactics games.
5. **Failure you can review**: the cause is visible and explainable, and the motivation to restart comes from "I know what to change", not from resentment.

Benchmark titles (play at least one through to the end before breaking it down; the tension of the battlefield can only be felt first-hand):

| Title | What to learn from it |
| --- | --- |
| Fire Emblem series (Three Houses and others) | Character growth bound to the battlefield, chapter-based levels, permadeath paired with turn-rewind options, the support conversation system |
| XCOM 2 | Hit chance and cover, the two-action system, permadeath and difficulty customization, the twin loops of tactics and base management |
| Super Robot Wars series | Presentation- and collection-driven design, spirit commands, a low barrier to entry and serialized content operations |
| Final Fantasy Tactics / Tactics Ogre | Height differences, facing, class trees and job changes, a deep fusion of narrative and battlefield |
| Advance Wars | Pure tactics with no progression: unit counters, capture and production, designing the map as a puzzle |
| Langrisser | The commander and mercenary system, long-term accumulation of series recognition (including its continuation as a mobile game) |
| Into the Breach | The opposite pole of determinism: all information public, no hit chances, every enemy intent previewed — replacing "save-scumming" with "puzzle-solving" |

## 3. Design Essentials

### 3.1 Grids and the Action System: Movement, Turn Order, Counters

The board, actions and resolution are the base of everything — settle them first, then talk about classes and levels; new projects are advised to start from square four-neighbor or eight-neighbor grids.

Grid type selection (topology first, feel second):

| Grid type | Distance metric | Upside | Cost |
| --- | --- | --- | --- |
| Square, four-neighbor | Manhattan distance | The most intuitive rules; movement ranges form diamonds, and pathfinding and previews are easy to build | No diagonal movement, so mobility feels stiff |
| Square, eight-neighbor | Chebyshev distance, or a surcharge for diagonals | Movement feels more natural and mobile units read better in space | Without a diagonal surcharge, straight-line paths lose their meaning; spell the rules out first |
| Hex grid | Axial six-direction distance | Equal distance in six directions, no diagonal disputes, the most uniform battlefield | Higher UI and art adaptation cost; tutorials take more effort |

Three mainstream action systems — pick one and take it all the way:

| Approach | Structure | Exemplars | Consequences |
| --- | --- | --- | --- |
| Faction turns | Your whole side acts, then the enemy's whole side | Fire Emblem, Super Robot Wars | Clear tempo and easy staging; the side that moves first snowballs easily |
| Speed order | Units act one by one, sorted by a speed stat | Final Fantasy Tactics, Tactics Ogre | Speed becomes a core stat and tension runs high; displaying turn order is a hard requirement |
| Action points | Each unit gets a small pool of action points per turn (move plus attack) | XCOM | Every move is a trade-off; translating the rules into UI is expensive |

- Movement of 4–6 tiles is a common starting point; for terrain entry costs (1 on flat ground, 2 in grass and the like), first ask "what does it teach the player" — if you cannot answer, cut it; movement and attack ranges must preview on the same screen, and range calculation should use the pathfinding result directly.
- Counters are the core tool for regulating the first-strike tax: the common rule is that the defender counters within weapon range — the melee disadvantage against ranged units and the archer's safe spots both grow from it; first strike must be priced, and the player must see counter damage before attacking, so that "strike first but eat a counter" holds and the first-strike tax holds.

### 3.2 Classes, Skill Trees and Counters

A class is essentially "a set of functions packed into one piece on the grid": define the function first, then the numbers.

| Role | Battlefield function | What it fears | Key parameters |
| --- | --- | --- | --- |
| Tank / front line | Plugging chokepoints, soaking damage, shielding the back line | Armor-breaking and magic, being flanked | Defense, HP, deliberately low movement |
| Melee damage | Breaking through and finishing kills, handling key units at close range | Counter chains, being focused down | Attack, speed, overload-type skills |
| Ranged / mage | Dealing damage from a safe distance, picking off targets over the front line | Close-quarters brawls, mobile units diving in | Range, hit rate, close-range penalty |
| Healer / support | Sustain, cleansing status, granting key units an extra action | Frailty, being targeted first | Heal amount, action economy |
| Mobile / harasser | Contesting points, diving the back line, ferrying and pinning | Formation fire nets, counters | Movement, evasion, disengage ability |

Two disciplines for job changes and skill trees:

- Trees must be narrow and deep, and advanced classes must not be pure upgrades: give each class 1–2 signature abilities, and make long-term growth cost something — a linear upgrade tree makes choices vanish quickly.
- Every class needs one "no substitute" sentence: any class for which you cannot write "in what situation must you bring it" gets cut or reworked; three of six classes being reskins is a common way novice projects die.

Two disciplines for counters (the unit or weapon triangle):

- Multipliers need a ceiling: the common practice is a ±20% to ±40% damage swing, not three to five times; once the gap is too wide, positioning and coordination lose their meaning.
- Counters must be visible, and symmetry comes before asymmetry: show the multiplier directly in the damage forecast; run the first version on one shared class skeleton, and leave signature classes and asymmetric balance for later.

### 3.3 The Intuition of Hit Rates and Probability (Perceived Fairness)

Probability is the easiest thing for players to hold a grudge over: people remember a 90% failure far more strongly than a success. The goal is not mathematical fairness but perceived explainability.

- The displayed value and the roll must match, or use an explainable correction (averaging two random rolls is the classic practice): never silently change the probability — get caught once and trust is gone.
- Avoid the "rock-paper-scissors band": making key 60%–80% rolls into pass/fail switches invites complaints; give decisive moments guaranteed-hit tools (criticals, commands, items) or fold them into deterministic design; keep crits (3%–15%) as seasoning, and do not let them act as the arbiter alongside permadeath.
- The combat forecast panel is the vehicle of trust: hit chance, damage, counter damage, crit chance and lethality all on one screen; the forecast and the resolution must share one calculation pipeline (§4).
- Pity systems and random sources must both be inspectable: a small compensation after repeated misses may exist, but it must be internally auditable and survive a datamine; randomness runs on a reproducible seed system, because save-scum control and balance verification both depend on "same input, same result".

Acceptance criterion: have 5 testers each make 20 attacks at 70%–90% hit chance, then ask how many they missed; if more than half misjudge the actual count by more than 2, check the forecast–resolution consistency first, then whether the cost of failure is too heavy.

### 3.4 Level Design: Terrain, Reinforcements and Hidden Objectives

One map is one puzzle plus one stretch of pacing; an SRPG level carries both the tactical test and the narrative staging, and the two purposes must not undercut each other.

- Terrain must read, and every map gets one theme mechanic: height differences, cover and terrain bonuses (defense, evasion, regeneration) must be drawn on the map; the theme mechanic (a chokepoint, a destructible bridge, a fortress assault, a river crossing) must be understood at first glance and still pay off after several turns.
- Victory and defeat conditions both deserve care: seize, hold for N turns, escort, retreat, assassinate — each condition is a pacing gear shift; main-line defeat conditions (all units dead, time out) must be explicit, and hidden objectives (treasure chests, NPC survival, completing within a turn limit) give skilled players extra helpings without conflicting with the main line.
- Reinforcements must be telegraphed or readable: untelegraphed reinforcements are a punishment, not a test; use turn counts, area triggers or story text to leave clues, so reinforcements become a hint to "speed up or pull back".
- Levels need breathing room: opening reconnaissance, encounter, mid-level pressure, climax and wrap-up each get a breath; 20–40 minutes for a first clear is the common range — an extremely long single level paired with permadeath is a frustration factory.

Run every map through the acceptance questions: what objective does the player see at first glance? Is there a "safe but boring" solution (if so, nerf it)? Can the cause of the first failure be stated clearly? How many minutes does a restart cost?

### 3.5 Permadeath and Difficulty Design (Rewind and Save Leniency)

Permadeath (dead units stay dead) is a classic SRPG setting and the easiest thing to abuse as a hardcore badge. Its real job is to give every unit weight, and its premise is that losses are avoidable and failures survivable.

- Permadeath pushes player behavior toward caution: without leniency, players turtle, stall and save-scum relentlessly; decide whether you want "choices with weight" or "high-pressure filtering", then flip the switch.
- Grant at least one of the three leniency pieces: rewind (a limited number of action or turn rollbacks), suspend saves (quit and resume any time), and difficulty or mode options (revive-on-death versus stay-dead, chosen by the player); the recent Fire Emblem titles and many peers offer rewind, and it deserves priority.
- Layered saves and save-scum signals: keep per-battle suspend saves separate from campaign saves, with three to five auto-rotating slots; if players reload over and over to reroll a hit, some part of probability or tolerance has failed — rather than blocking saves, offer controlled randomness or guaranteed-hit tools (§3.3).
- Difficulty comes from pressure combinations, not number stacking: pick two of the four pressure sources — turn limits, reinforcements, scarce resources, conflicting objectives — and use them thoroughly; make difficulty explicitly selectable and lowerable mid-run, and keep the hardest mode as an optional highlight, not a default hell.
- Write the rules for dead units first: whether experience and gear are recovered, whether story dialogue keeps a slot, whether there are enough bench slots; "the unit did not make it, but the script is still calling their name" is a high-frequency continuity break in low-budget projects.

## 4. Technical Essentials

The engineering thesis in one line: **the difficulty is not real-time responsiveness but the consistency of resolution, the readability of AI and the robustness of saves**. Everything below is engine-agnostic and implementable in any engine.

**Board and range calculation**

- The board is "a grid data structure plus overlay layers": one table each for passability, entry cost, terrain bonuses and occupying units, separated by layer, so changing one mechanic does not disturb the others.
- Movement range uses weighted pathfinding (Dijkstra or A*, with terrain cost as the weight); attack range equals movement range composed with weapon range; cache per turn and recompute locally after each action; model unit blocking separately from impassability, and hard-code one consistent rule for "blocks enemies, passable for allies".

**Turns and the resolution pipeline**

- The turn manager is implemented as a phase state machine: player phase, enemy phase, event and reinforcement resolution, victory check; write the order into the spec and keep it stable — change the order and saves no longer line up.
- Forecast and resolution are forced to share one pipeline: the same inputs, the same damage formula, the same sequence of random calls; two code paths are the only source of "inaccurate forecasts".
- The damage formula is built as an additive chain (attack, defense, terrain, counters, crits — one segment each, all in tables, each segment toggleable); randomness uses a reproducible seed system with a fixed roll order — the foundation for rewind and for "same save, same result" debugging.

**AI**

- The mainstream solution for tactics AI is "enumerate candidate actions plus scoring": for each unit, enumerate move destinations and targets, score them by damage, threat and objective weight, and take the best; do not chase "human-like" — chase readable, counterable and characterful.
- Behavior must be explainable; across difficulty tiers, tune behavior before parameters: focus the frailest unit, take points first, withdraw below a health threshold — rules a player can learn by watching two or three turns; easy lets the AI look one step less far and drop chases, hard lets it read forecasts and protect key units; keep cheating as an honest, disclosed option for the top tier only.
- AI is a free playtester: batch-simulating one map across many compositions and difficulties and collecting win rates and clear-turn counts is the realistic way to balance levels.

**Saves, replays and tooling**

- Suspend saves must capture the complete state mid-battle (turn, unit coordinates and HP, random source progress, event triggers all serializable, with a version number and migration function); rewind is implemented with a snapshot stack or command-log replay — use snapshots during the prototype phase.
- A map editor and debug commands pay off the earlier the better: the editor must at minimum support editing terrain, placing units and reinforcements, setting win conditions and one-click playtest; debug commands cover level skip, adding units, editing experience, controlling randomness and forcing triggers.
- Battle animations must be skippable, speed-up-able and disable-able; keep the defaults restrained — a level with dozens of battles cannot wait for long animations.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimating scope; not a commitment.

| Tier | Scale | Time reference | Notes |
| --- | --- | --- | --- |
| Systems prototype | 1 whitebox map, 4–6 units, 2–3 classes | 1–2 months (solo) | Movement, resolution and AI running end to end |
| Small complete title | 10–15 levels, 8–10 classes, a complete combat system | 1–2 years (small team) | Levels and narrative are the main cost |
| Typical indie SRPG | 20–30 levels, class trees and job changes, support and story text | 2–4 years (small team) | Text and portrait art double with each character added |

Art volume: each playable unit commonly needs 1–2 pieces of portrait art (with expression variants) plus a battlefield sprite; traditional 2D frame-by-frame battle animation runs dozens to hundreds of frames per character, and ten characters is a heavy bill — the alternative paths are a shared 3D skeleton with weapon attachment points, or light movement plus effects. Maps get tilesets per theme, dozens to hundreds of tiles each; enough for whiteboxing first, replaced gradually; skill and status icons are priced by count, and every one needs a readable small-size version.

Level scale and scheduling: a whitebox takes one to two days and polish three to five, a time ratio of roughly 1:3 to 1:5; SRPG levels add multiple full-clear test passes (one run per composition and difficulty) and staging the story sequences. From zero to "a level that plays for ten minutes without getting tiresome" typically takes 1–2 months, to a vertical slice (a complete combat system plus 3–5 release-quality levels) typically 3–6 months, then extrapolate as "level count times text volume, times a polish factor"; the main cause of scope loss is the number of characters and classes — every added character is five bills: portrait, animation, numbers, text, balance.

## 6. How to Start the First Prototype

The first prototype validates one thing only: whether "move, attack, resolve" on a single map is fun. Scope lock: one 20x15 to 25x20 whitebox map, 4–6 player units, 2–3 classes, 6–8 enemy units, one primary victory condition (elimination) plus one variant (hold for N turns). No story, no saves, no job changes, no production art.

- **Weeks 1–2: board and resolution.** Grid, pathfinding, movement range display; hit, damage, counter, death and the forecast panel; goal: forecast and resolution match exactly.
- **Week 3: turns and AI.** Faction turn state machine, scoring-based enemy AI; goal: play one full level to the end.
- **Weeks 4–6: one map to tune pacing.** Terrain bonuses, reinforcements, a second victory condition, and one of rewind or suspend save; get 3–5 testers and collect numbers.

Starting parameters (copy and adjust):

- Map 20x15 to 25x20 squares; movement 4–6 tiles; weapon ranges: melee 1 tile, ranged 2–3 tiles; base hit chance 70%–90%.
- Start the damage formula at "attack minus defense", no multiplier chain yet; unit HP 20–40; one level runs 10–20 turns and 15–30 minutes with 4–8 units per side; experience and growth get two levels for now — enough to validate.

Success criteria (all observable):

- At least 3 of 5 testers have never played a game of this kind and complete the map with no verbal guidance; each person has at most 1 moment of "I don't understand why I missed or why I died".
- Testers can explain which move the last dead unit got wrong, and at least 2 proactively restart a second run driven by "trying a different approach" rather than frustration; if more than half the answers point to luck, go back and fix probability or leniency (§3.3, §3.5).
- You can retune one map's numbers and verify it via hot update within 5 minutes; if you cannot, build the editor first (§4).

## 7. Common Pitfalls

1. **Forecast and resolution on two code paths**: the numbers disagree and every decision the player made on the forecast loses its meaning; forecast, resolution and AI scoring sharing one pipeline is this genre's first law.
2. **A probability band as the pass/fail switch**: decisive moments lean on the 60%–80% coin-flip band, so wins and losses are all luck; backstop them with guaranteed-hit tools or deterministic design.
3. **Permadeath with very long levels and no suspend save**: one mistake costs forty minutes, and what players learn is fear, not tactics; grant at least one of the leniency trio, with suspend saves and auto-rotation as the floor.
4. **Unreadable AI behavior**: it suddenly commits everything or spaces out entirely, and players cannot form expectations; better stably dumb than randomly smart.
5. **One optimal class and nothing else**: reskins, strict upgrades and dead-on-arrival classes, the triple; write one "no substitute" sentence per class first, and rework the ones you cannot.
6. **Stats flattening tactics**: two levels of grinding rolls over everything and levels become a walkthrough; use experience decay, level suppression or growth pacing to protect "tactics as the primary variable".
7. **Elimination as the only victory condition**: twenty levels of mopping up; mid- and late-game fatigue comes from repetition, not difficulty — victory and defeat conditions are cheap level seasoning.
8. **Reinforcements as untelegraphed backstabs**: players have no window to respond and only save-scumming left; reinforcements need trigger clues and the option to retreat or speed up.
9. **Battle animations that cannot be skipped**: long animations on by default and dozens of battles per level is an instant refund; animations must be optional, speed-up-able and disable-able.
10. **Building characters and classes before the systems are frozen**: portraits, animations and balance can all be redone; polish 6–8 classes and one map to fun first.
11. **Testing only with the developer's own composition**: the optimal solution masks every weakness of a level; balance verification must rotate compositions, difficulties and players.

## Further Reading

- Game Design Handbook §4: the number-table methodology and balance workflow — the higher-order method behind this page's counter matrix and probability design.
- Level Design Handbook: map metrics, pacing and the whitebox process — the full expansion of §3.4.
- Programming Handbook: turn-based architecture, pathfinding and AI budgets, save engineering — the counterpart to §4 of this page.
- Indie Survival: scope control and scheduling — the extended version of this page's §5 ledger.
- Pitfalls & Anti-patterns: high-frequency pitfalls on both the design and engineering sides, complementing §7.
- Exercise 1: write a counter matrix and a one-line duty for each of 6 classes, then cut the classes you cannot write a "no substitute" sentence for.
- Exercise 2: build three victory conditions (elimination, defense, escort) on the same whitebox map and record whether testers' optimal solutions change with them.
- Exercise 3: log the count, causes and timing of save reloads and rewinds in one playtest, and turn the list into input for calibrating difficulty and leniency.

Victory in tactics is not decided on the board alone: until actions, probability and leniency are tuned, classes, story and presentation are debts still to be paid.
