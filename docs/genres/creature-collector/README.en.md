# Ludo Atlas · Genre Handbooks · Creature Collector

> **Genre Handbooks · Volume 4**. Positioning: the collect-and-raise series modeled on Pokémon. Players draw motivation from four lines at once — collection, raising, battle and trading: bestiary completion supplies the long-term goal, ownership of the team supplies emotional investment, battles are where results are verified, and trading is the social outlet.
> Companions: Game Design Handbook (core loops and numeric tables) · Programming Handbook (data pipelines and battle resolution) · Case Studies (breakdown and retrospective methods) · Indie Survival (content accounting and scope control).
> This page links nothing externally; benchmarks are well-known works only, and the numbers are common orders of magnitude — calibrate them against real measurements in your own project.

---

## 1. Positioning and Core Loop

The one-line positioning: creature collection is **the genre that locks four things — capture, raising, battle and trading — into a single loop**. Collection is the gathering line, raising is the investment line, battle is the verification line, trading is the social line; the four lines feed ammunition to each other, and doing only one of them collapses.

The core loop, written as a verb cycle: `explore → encounter → weaken → capture → raise in the party → verify in battle → adjust evolution and moveset → explore a new area`; the trading loop hangs between collection and raising, inserted whenever the player needs it.

Each of the four loops has its job:

| Loop | What the player does | Where the stickiness comes from |
| --- | --- | --- |
| Collection | Encounter, weaken, capture, fill the bestiary | The reliable reward of "one more square filled"; rarity tiers |
| Raising | Level up, learn moves, evolve, adjust roles | Ownership and investment — the team is "mine" |
| Battle | Type matchups, action order, team composition | The retrospective sense of winning against the odds; the acceptance test for what you raised |
| Trading | Swap duplicates for gaps, trade rares | Social contact and mutual completion, a shortcut through the collection loop (optional, but high-reward) |

Drawing boundaries with adjacent genres:

| Adjacent genre | Boundary |
| --- | --- |
| JRPG | JRPGs are driven by fixed characters and story; here the creatures are the characters, the party is swappable, and strategy revolves around capture and composition |
| Raising sim | A raising sim is about people and relationships, where growth itself is the content; here growth has a definite combat outlet |
| Trading card game | Card collection is a paper asset; what you collect here are entities that grow, evolve and hold ecological niches — plus a trading line |

A self-check question: delete the bestiary, evolution and trading entirely, leaving only battle and leveling — does the game still stand up? If the answer is "no", what you are making is a creature collector.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (ordered by priority):

1. **The surprise of discovery**: new areas hold new creatures, and the encounter itself is the reward; rare and special individuals are the source of "lucky day" moments.
2. **Reliable returns on collection**: every bestiary entry filled leaves a record, a reward and a sense of progress — completion is visible.
3. **Ownership through raising**: individual variation, nicknames, movesets and evolution routes make players say "my team" instead of "the current lineup".
4. **Battles that bear review**: wins and losses are explainable (types, Speed, movesets, items) — win with understanding, lose with understanding.
5. **The social side of trading**: duplicates have somewhere to go, rares have somewhere to land, and filling the bestiary has a shortcut.

Negative feelings (any one of these is a red light): being toyed with by randomness (black-box probabilities, repeated failures with no explanation), raising with nothing to show (training results invisible and non-transferable), and bestiary traps (the one creature you are missing can never be located).

Benchmark works (all well-known titles; play them by hand before breaking them down):

| Work | What to learn |
| --- | --- |
| The Pokémon series | The textbook four-loop closed circle: capture, evolution, the matchup matrix and trade battles in their complete form — but don't take its scope as a starting point |
| Palworld | The fusion of collection with survival building and labor systems; creatures have production value beyond battle |
| The Digimon series | An evolution line of evolution trees and raising mechanics: branching evolution, conditional evolution and the lineage of virtual pets |
| Roco Kingdom | The Chinese browser-game paradigm of collect, raise and battle: lightweight collection and bestiary expansion under long-term live ops |

What players expect from this genre by default: visible catch probabilities and bestiary progress, batch operations for team management, confirmations for misinputs with partial recovery (evolution, forgetting moves), save-anywhere and a safe experience when interrupted. Miss any of these and the negative reviews arrive quickly.

## 3. Design Essentials

### 3.1 Creature Design: Ecological Niches, the Type Matchup Matrix and Evolution Chains

Define four dimensions first, then draw the art and write the numbers:

| Dimension | Question to answer | Common practice |
| --- | --- | --- |
| Ecological niche | Where and when it appears | Terrain, time of day, weather and rarity tiers |
| Combat role | Which tactical problem it solves | Damage, tank, control, support, speed — every creature fills at least one slot |
| Type combination | What it is on offense and defense | Single type to dual type; dual types add identity and amplify matchup risk |
| Growth position | Which stage of the evolution chain | Two- or three-stage evolution; low stages common, mid stages transitional, final stages rare |

The type matchup matrix (this genre's numerical foundation):

- Number of types: 6–10 for small projects, 12–18 for mid-size ones; past 12, check item by item that "every type matters on both offense and defense" — a type that doesn't matter is a liability.
- Multiplier conventions: three common tiers — super effective ×2, resisted ×0.5, immune ×0 (simplified projects can use 1.5 and 0.67); dual-type multipliers multiply, so 4× and 0.25× extremes exist by nature, and the overall share of extremes is part of matrix design.
- Matrix and balance discipline: every type must be able to answer "who fears me, whom do I fear, whom am I useless against"; the matchup chart is consultable in-game, with no hidden multipliers; run simulations measuring the win-rate gap between any two types, and when a single dominant type appears, adjust the matrix instead of adding more creatures.

Evolution chain design:

- Evolution must change a role or sharpen it, not reskin the creature at "1.5× the numbers"; three-stage evolutions give two qualitative jumps, which is what players have to look forward to.
- Keep evolution conditions simple: pick mainly one of level, item or condition; branching evolution is low-cost, high-reward replayability — split two routes with a rare item or a different condition.
- Low-stage creatures carry the early rush (low barriers, immediately usable), final stages carry the long-term goal; half the bestiary's sense of hierarchy comes from evolution chains.
- Design order: write "what tactical problem it solves" and "where it appears" first, then fix types and numbers, and leave the art until last; do it the other way — draw first, force the numbers in afterwards — and the type matrix inevitably loses balance.

### 3.2 Capture Mechanics: Turning Battle into Control

Capture is the gate of the collection loop and the number players account for most carefully. The general formula skeleton (implementations differ, the bones are similar):

`capture success rate = base catch rate × HP modifier × status modifier × item multiplier × level modifier`

- HP modifier: lower HP means easier capture — chipping and "killing" are one hit apart, and that hit is the entire tension of capture gameplay; the common form maps current HP linearly onto a 1–3× modifier range (full HP hardest, low HP easiest).
- Status modifier: status conditions such as sleep and paralysis apply a fixed multiplier (commonly 1.5–2×), which makes "control the HP, control the status" a fixed ritual before every capture.
- Item multiplier: capture items come in tiers (basic, improved, specialized), and the multiplier gaps between tiers give the economy an outlet; no hidden modifiers.
- Level and rarity: high-level, rare and legendary individuals get their own base rates; write the legendary's expected number of attempts into the table and convert it into item cost for the player.

Transparency and anti-frustration:

- Probabilities must be visible: record each creature's base catch rate in the bestiary; give process feedback during capture such as the number of shakes; repeated failures need an upper bound on cost, so players don't spin their wheels in "almost had it".
- Pity and recovery: after several failures, a hidden ramp, or a more expensive guaranteed-catch item; if the target is killed by mistake, there must be a path back to re-encounter it (respawn points, bestiary tracking) — the penalty for failure is "more time", not "missed forever".
- Compounding design: let catch rates rise slightly with bestiary completion or event progress, so collection feeds back into collection efficiency — the cheapest positive feedback in the collection loop.

### 3.3 The Raising System: Growth Curves and Simplification Trade-offs

Raising is where the sense of investment mostly lives. There are four knobs; pick two or three according to project scope:

| Knob | Classic approach | Simplification advice |
| --- | --- | --- |
| Leveling | The whole party gains EXP, the bench gains a share | Keep it; shared EXP and batch level catch-up are the floor of the experience |
| Move list | Learn moves by level, teach moves by item, forgetting recoverable | Keep it; divide moves by function: damage, control, support, passive |
| Individual variation | Dual track of individual values plus effort values | Cut it in small projects; replace with one of nature, ability or talent |
| Evolution | By level, item or condition | Keep it; evolution conditions are the valve that regulates content volume |

- Growth curve: the shape of the EXP curve decides whether "grinding" is a barrier or a backdrop; aim to keep grinding time under half the total play time — collection and exploration are the main course.
- Learnsets and individuality: each creature has 8–20 learnable moves, of which 2–3 are set as exclusive (no other creature can learn them); rather than giving every creature an all-purpose move pool, give each one or two things only it can do, with a visible role tag.
- Irreversible actions need confirmation: evolution, overwriting a move and consuming an item are the three actions most likely to feel save-destroying; a confirmation popup plus recoverable move forgetting are standard.

### 3.4 Battle and Trading: Verifying Results and Completing Each Other

Battle is the acceptance test for what you raised; start with a minimal scope:

- Battle formats: singles (1v1) plus switching is the minimal plan; doubles and online battles are extensions, scheduled separately.
- Action order and length: turn-based, ordered by Speed (with modifiers), with a fixed and visible speed-tie rule and a visualized action order — that is what lets players decide "should I switch this turn"; regular encounters run 2–4 turns (within 30–90 seconds), elite and boss fights 5–15 turns, and while a capture target is on the field the battle's objective shifts from "win" to "control" — this dual objective is the tension unique to this genre.
- Team building and visibility: party size and type coverage are a sudoku the player solves; encourage adjusting the team per area — one team beating the whole game means the matrix is too narrow; damage ranges, matchup multipliers and Speed priority are all consultable in-game, and hidden mechanics are kept for easter eggs only.
- Trading: do local or offline trading first (codes, LAN); online trading needs servers, validity checks and anti-duplication, an entirely different order of cost (see Multiplayer & Backend).

### 3.5 Narrative Framework: The "Become a Master" Journey Template

Narrative in this genre has a fixed skeleton; filling it in is less effort than inventing your own:

| Stage | Player goal | Narrative anchor |
| --- | --- | --- |
| Departure | Get your first partner, learn to capture | Small town, mentor, choose one of three starters |
| Growth | Take on the goals of each regional milestone | Every milestone binds a new terrain and a batch of new creatures |
| Turning point | Meet your rival and the villains | The rival's team grows with the player's progress, forming a mirror |
| Ascent | Face the endgame trial | A full-type examination of the player's team |
| Finale | The bestiary, rare creatures, hidden areas | Turn "the creature you don't have yet" into a long-term hook |

- The template's job is to give collection a geographical and emotional motive: why go to the next area? Because there are new creatures, new trials, a story there; "regional trials plus an endgame trial" is the skeleton, and trial-based, tournament-based and open-region structures are three common variants — pick by map structure.
- The rival and the legendary creatures are the two ends of the narrative line: the rival supplies tension, the legendaries are the collection line's endgame reward; keep each to single digits, and save the staging budget for a few key moments; the narrative minimum is that every new area gets a reason "why this place is worth visiting" and a sketch of local life — areas without a narrative anchor exhaust collection motivation quickly.

## 4. Technical Essentials

**Data-driven content and referential integrity**

- Five core tables: creatures (types, stats, evolution chain, bestiary text), moves (effect, power, accuracy, learning conditions), the type matrix, encounters (area, time slot, probability), items. Everything goes into CSV or JSON, code keeps only formulas, and hand-editing generated files is forbidden; reference validation goes into CI: pre- and post-evolution IDs exist, moves referenced by learnsets exist, creatures referenced by encounter tables exist, every creature has bestiary text (past a thousand rows, typos are the largest source of bugs — methods in the Programming Handbook).

**Layered resolution for battle and capture**

- Resolve a turn into an event list first (who hits whom, how much damage, whether the capture succeeds, whether anything faints), then play the staging from that list; skipping and fast-forward affect only the player, not the resolution. Capture is an independent event at the event layer, with logs and replays hanging off it; encounters, captures and criticals run on a seedable deterministic RNG, so anomalies reproduce with one click.
- Decouple the battle state machine from the scene: encounter → commands → ordered resolution → event playback → capture check → victory and rewards → return to field; every state is unit-testable, which is what lets bestiary and save features hang off it reliably.

**Saves and per-creature data**

- Each creature's individual data (level, EXP, moves, individual variation, nickname, capture location) must be serializable and migratable; a save = the player's party + bestiary + world state + version number, and version migration is built from day one. The bestiary is the database: capture records, distribution information and completion rewards all derive from the same bestiary table.
- As soon as online trading or battling is involved, creature data needs server-side validation (stat upper bounds, move legality, origin tags); offline projects should still reserve the fields — adding them later costs an order of magnitude more.

**Content pipeline and tools**

- A creature workbench: a debug tool where changing one table previews the bestiary card, battle sprite and move list in-game. The more content, the higher the return — the tool most worth investing in early in this genre.
- Freeze art specs first: sizes and naming conventions for sprites, icons, battle sprites (animation frames or rigs) and cries go into the asset ledger — changing specs late means rework for everyone; localization from day one: creature names, move names and bestiary text are the top three text volumes — give everything string IDs, and establish the glossary before writing.

## 5. Content Volume and Workload Reference

The cost formula in this genre is multiplicative, not additive:

`total content volume ≈ creature count × per-creature assets + move count × per-move assets + creature × move learnset entries + scene and encounter configuration`

- Each 2D creature needs one asset set (sprite, icon, battle sprite and animation, cry, bestiary text); small teams price by the day — commonly 2–5 person-days per set, more than double for 3D; each move takes 0.5–2 person-days. Learnset entries are the invisible bulk: 150 creatures × an average of 15 learnable moves = 2,250 configurations, each of which must pass reference validation and balance checks.
- Scope ladder (common orders of magnitude, for estimating range, not a commitment):

| Scope tier | Creatures | Moves | Types | Positioning |
| --- | --- | --- | --- | --- |
| Prototype | 10–20 | 20–40 | 4–6 | Validate the four loops, whitebox assets |
| Small finished work | 50–80 | 80–120 | 6–10 | The bestiary takes shape; 6–12 months solo to small team |
| Typical indie title | 100–150 | 150–250 | 10–14 | Requires dedicated content production and tooling |
| Large title | 300+ | 500+ | 16–18 | Years of team production, amortized through a series |

- Benchmark risk: the thousand-plus creature scope of the top titles is the accumulation of decades and generations of teams — don't make it the goal of your first work; greenlight around "50–80 creatures, one loop polished until it's fun" first, then expand the tables as capacity allows.
- Scheduling and discipline: the four-loop prototype takes 3–5 weeks; a vertical slice (one area, 30–50 creatures, complete capture and evolution) takes 3–6 months; extrapolate by content volume after that — expanding the bestiary is cheaper than adding systems. Creature count is a knob you can turn up or down; the type matrix and move system are the skeleton: freeze the skeleton first, then decide bestiary size by capacity; cutting creatures is safe, cutting the loop is dangerous.

## 6. How to Start the First Prototype

Goal: in 3–5 weeks, build the minimal four loops — "can catch, can raise, can evolve, can battle, has a bestiary" — without touching online trading, full narrative or polished art.

- Week 1: battle and capture closed loop. 3 creatures, 4 types, 8 moves, one capture check (with status and HP modifiers), paper walkthroughs plus in-game logs.
- Week 2: collection and raising. One encounter table of 10–15 creatures, leveling and move learning, one three-stage evolution chain, one minimal bestiary screen.
- Week 3: miniature content. One area (3–4 terrain types), rarity tiers, one regional trial milestone, completion rewards.
- Weeks 4–5: playtesting and judgment. Get 5 people to play until they have "caught 10 creatures, evolved 1, passed the trial".

Success criteria (all observable):

- Testers go after the fourth creature and beyond without being prompted (collection drive holds).
- Testers can say why a creature "stays on the team" (raising drive holds), can explain the causes of both a clean win and a crushing loss (battles bear review), and can restate the matchup between two creatures (the matrix is felt).
- Changing one number (a catch rate or one matchup multiplier) shows a quantifiable effect within 10 minutes, provided logs and simulation scripts are in place.

Decision gate: if any of the four loops breaks in playtesting, fix that loop before talking about expanding the tables; once "one asset set per creature" mass production starts, rework cost scales with bestiary size.

## 7. Common Pitfalls

1. **Over-sized bestiary**: planning for hundreds at greenlight, then running out of both art and configuration by creature 40. Avoidance: use 30 creatures to polish the four loops until they hold; production can expand, the loop cannot be skipped (§5, §6).
2. **Over-dense type matrix**: a dozen-plus types with under a hundred creatures dilute the matchups against each other; players can neither memorize them nor find a use for them. Avoidance: start with 6–10 types, each with a part to play on both offense and defense (§3.1).
3. **Black-box capture**: probabilities unpublished, no process feedback, half an hour of repeated failures — and players put it all on the game's ledger. Avoidance: visible probabilities, feedback during the process, an upper bound on failure cost (§3.2).
4. **Raising without ownership**: individual variation invisible and non-transferable; you train for ages and only the numbers grow. Avoidance: nicknames, visualized variation, role tags and exclusive moves (§3.3).
5. **Irreversible misclicks**: evolution, move overwrites and item consumption go through in one press, and the player feels the save is ruined. Avoidance: confirmation popups plus a recoverable forgetting mechanic (§3.3).
6. **Copy-pasted move lists**: every creature shares one learnset, leaving creatures different only in appearance. Avoidance: 2–3 exclusive moves per creature, designed by functional slot (§3.3).
7. **One team clears the game**: too narrow a matrix or unbalanced numbers let a single team ride through everything, and swapping creatures loses meaning. Avoidance: check usage rates with simulation scripts and adjust matrix and encounters dynamically (§3.1, §3.4).
8. **Battles reduced to cutscenes**: encounters end in ten seconds with no decisions, and collection degrades into picking things up. Avoidance: make status, HP control and switching all matter; keep regular battles at 2–4 turns of decision density (§3.4).
9. **Underestimating trading and online**: bolting on online trading late runs into the triple engineering bill of servers, legality and anti-duplication. Avoidance: do local trading first; greenlight online separately (§3.4).
10. **Blurry originality boundaries**: gameplay skeletons can be borrowed, but creature visuals, names and move text must be original — no recoloring, parody or closely similar designs of protected characters; when unsure, check the Legal, Patents & Competition handbook.

## Further Reading

- [Game Design Handbook](../../fundamentals/game-design/README.md): the underlying draft for core loops, numeric tables and type matrix methods; pairs with §1 and §3.1.
- [Programming Handbook](../../fundamentals/programming/README.md): implementation details for data-driven content, layered resolution and debug tools; pairs with §4.
- [Case Studies](../../postmortems/README.md): breakdown methods for collection and raising directions — consult when choosing and reviewing.
- [Indie Survival](../../../playbooks/indie-survival/README.md): content accounting and scheduling discipline, complementing §5.
- [Legal, Patents & Competition](../../publishing/legal/README.md): the boundary between gameplay and expression, the red line between borrowing and infringement — required reading before greenlighting.
- [Pitfalls & Anti-patterns](../../pitfalls/README.md): pitfalls in content and numeric production — read against §7.
- [Genre Handbooks · JRPG](../jrpg/README.md) and [Genre Handbooks · Trading Card Game (TCG)](../card-game-tcg/README.md): two sister lines, party battles and collectible battles; read against §1 and §3.4.
- Homework: build a paper model of 10 creatures, 4 types and 8 moves; hand-calculate the expected turn counts of two battles and one capture — then decide whether to greenlight.
