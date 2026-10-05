# Ludo Atlas · Genre Handbooks · Roguelite

> **Genre Handbooks · Volume 1**. Positioning: turning the pleasure of "restart every run, a different run every time" into a system: the dual-loop structure, controlled randomness, build construction, death payoffs and difficulty tides; applies to both 2D and 3D.
> Companions: Game Design Handbook (loops and randomness) · Level Design Handbook (rooms and pacing) · Programming Handbook (procedural generation and saves) · Pitfalls & Anti-patterns.
> This page carries no external links; examples name publicly known titles only, and the figures are common magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: a roguelite is the genre that "buys variety with randomness, rhythm with death, and momentum with accumulation". Players repeatedly cycle through "start a run, grow stronger, die, start again" inside one ruleset, and with every cycle they understand a little more and bring a little more back.

Two loops must be turning at the same time:

- **In-run loop (run)**: one run from start to finish, 20 minutes to 1 hour. Verb chain: `enter → explore/fight → pick up upgrades → build comes together → challenge the floor boss → die or win`. It answers "is this run fun?"
- **Meta loop (between runs)**: accumulation across runs, hours to tens of hours. Verb chain: `results → unlock new content → switch character, switch weapon, switch difficulty → start another run`. It answers "will I want to open this again tomorrow?"

| Loop | Cycle | Question it answers | Output | On failure |
| --- | --- | --- | --- | --- |
| In-run (run) | 20–60 minutes | "Can I clear this run?" | This run's build and immediate growth | Death; only this run is lost |
| Meta | Hours and up | "What am I still missing?" | Unlocks, blueprints, difficulty tiers | Progress only ever increases |

Three hard checks:

1. **The run stands alone**: even with no meta progression, a single run should be fun on its own. Run design that only holds together because of meta numbers is unpaid debt.
2. **Meta is visible**: the main menu always shows 1–2 concrete "next unlocks", so "one more run" has a visible reason.
3. **Run-length red line**: past 90 minutes per run, a single failure stings hard enough to drive most players away; 20–40 minutes for a beginner run is the common range.

## 2. Player Experience Goals and Benchmark Titles

Target experience, in priority order:

1. **A different run every time**: the same actions produce different decisions and a different feel each run.
2. **Visible growth**: within ten minutes, going from "can't dent anything" to "mowing down a whole stretch", with the power change both visible and audible.
3. **Death is acceptable**: the reaction to losing is "I'll try a different approach next run", not "this game is out to get me".
4. **Understanding beats power**: growing stronger comes mainly from understanding synergies and risk, not from stacking stats.
5. **Always something to aim for**: at any moment the UI shows one or two concrete next goals.

Anti-patterns (stop and fix the moment they appear): players attribute failure to "bad luck with nothing I could do about it"; across the first ten runs, not one makes the player want to review it of their own accord.

Benchmark titles (one lesson each — take the lesson, not the shell):

| Title | What to take from it | Boundary warning |
| --- | --- | --- |
| Hades | Narrative bound to death: every death moves the story and relationships one step forward | Heavy text and voice acting; hard for a small team to replicate |
| The Binding of Isaac | Item synergies: pairs stack into qualitative changes, and the synergy table is content in itself | Extremely hard to balance; conflicts need code rules as a backstop |
| Slay the Spire | Transparent information: routes, card pool and enemy intents all visible, so losses make sense | Large number surface; high testing cost |
| Dead Cells | Action game feel and traversal pacing first: even when random, the movement itself is worth playing | The control barrier filters out part of the audience |
| Risk of Rain 2 | Difficulty grows multiplicatively with time: stalling is itself a risk | Online sync and performance are new problems to solve |
| Enter the Gungeon | A clean implementation of twin-stick combat; solid room templates and gun feel | Diversity is piled up out of content volume |

## 3. Design Essentials

### 3.1 Controlled Randomness: Luck Can Be Complained About, Never Despaired Over

Randomness splits into three layers, each under different control:

1. **Structural randomness** (how rooms connect): owns freshness, and playability must be validated.
2. **Drop randomness** (what you get): sets the ceiling on build diversity; weights and pity rules are all spent here.
3. **In-the-moment randomness** (triggers inside combat): owns drama; keep variance small so randomness never decides life and death outright.

The item-pool weight table is the core tool. Rarity is just a label; actual probability comes from weights:

| Tier | Weight share | Appearances per run | Role |
| --- | --- | --- | --- |
| Common | around 60% | 8–12 | Fill the base; supply synergy raw material |
| Rare | around 30% | 3–5 | Reinforce the direction already taken |
| Epic | around 9% | 1–2 | Define this run's highlight |
| Legendary/evolved | around 1% | 0–1 | Create a memory worth retelling |

Three kinds of pity rule, all written into code:

- **Frequency pity**: after N consecutive rolls without rare or better, the next one is forced up.
- **Repeat pity**: the same item is not issued twice in the short term, preventing "this again" fatigue.
- **Quota pity**: high-rarity items are capped at X per run, preventing one jackpot run from punching through the late-game difficulty.

Synergy filtering (a restrained version of smart loot): the system can see the player's current build and weights related items (after picking up a fire weapon, fire items get a probability bump). But keep a floor on surprise: at least 30% of rolls still hand out random pool items — following the player completely costs you both surprise and learning.

Remaining rules:

- **Pool hygiene**: items already maxed out or useless for this run leave the draw pool; every run guarantees all three build directions are stocked.
- **Randomness acts on "situations", not "numbers"**: different enemy layouts are fun; the same reward varying by 10% is just noise.
- **Despair comes from "seeing no way out"**: bad luck needs a stop-loss (pity), failure must leave residue (currency carried back from the results screen), and strong combinations get no advance notice (avoiding the "so close" torment).

### 3.2 Build Construction: Draw the Synergy Matrix Before Writing Items

The synergy matrix is the roguelite's "recipe sheet": arrange mechanic tags (ignite, freeze, ricochet, summon, crit, shield, lifesteal, dash) as rows and columns, and write the combined effect at every intersection. Matrix first, items second — and every item must interact with at least two tags.

| Tag | Ignite | Freeze | Ricochet |
| --- | --- | --- | --- |
| Ignite | Double burn | Melt: enemies take amplified damage | Fireball bounces once |
| Freeze | Melt | Deep freeze: ice shards splash | Ice crystal chain |
| Ricochet | Fireball bounce | Ice crystal chain | Projectile count +1 |

The above is only a three-row sample; expand the matrix to fit your own tag system — the fuller the rows and columns are filled in, the easier items are to write.

Remaining points:

- **Rarity governs the behavioral radius**: common items add numbers, rare items change behavior (burn on hit), epic items change rules (burning spreads). Players always remember behavior changes, not whether it is 15% or 20%.
- **Evolution and fusion routes**: two items of the same family fuse into a single evolved item (e.g. Spark + Fuel = Wildfire); publishing the recipe chart early gives players a hoarding goal; an evolved item must cash out the "qualitative change" three ways at once — visuals, sound and numbers.
- **Make builds converge**: a single run supports 2–3 core chains, and the chains do not exclude one another (a melee chain does not kill the ranged chain). Set diminishing returns against "mindlessly stacking one item": the 4th same-family item's effect drops to 70%, with the rule written explicitly into the item description.
- **Quantity baseline**: the first playable version needs at least 3 directions (melee assault, ranged attrition, summoning or spells), and within 4–6 items per direction the player should feel a build "come together".

### 3.3 Death Pays Out: Unlocks Before Raw Numbers

Death ends a run; it is not the player's failure. There is only one design requirement: every death must bring something back, and what comes back must be understandable and spendable.

Unlocks fall into three tiers, allocated by scheduling budget (ratios shift with your pillars; below are common starting values):

| Type | Share reference | Examples | Role |
| --- | --- | --- | --- |
| Content unlocks | around 70% | New weapons, characters, floors, events, boss variants | Change gameplay and options |
| Convenience unlocks | around 20% | Starting rerolls, cutscene skip, compendium, quick restart | Respect veteran players' time |
| Raw stats | around 10% | Max health, starting gold | A safety net for weaker players |

- **Content unlocks are the main force**: goals for newcomers, novelty for veterans, and they have no balance ceiling.
- **Keep raw-stat growth restrained**: cap it, publish the cap, and narrow the returns after three to five runs. Unbounded stat growth dilutes the tension of "starting from zero every run" into "winning because the level is high enough".
- **Death penalties have a ceiling**: they swallow only this run's gains and never make global seizures (revoking unlocks, wiping currency) — unless that is a core selling point you have publicly promised.
- **Make repetition pay too**: character mastery and cumulative kills unlocking variants or cosmetics — a hidden line for specialist players.
- **Results must be fast**: every second between the death animation and the results screen bleeds patience; say "what you brought back, how far the next unlock is" in a single screen.

### 3.4 Power Inflation and Difficulty Tides

Player power inflates multiplicatively (1 → 10 → 100), while enemies grow linearly or in steps. Three phases with distinct pacing roles:

| Phase | Player state | Enemy pressure | Design goal |
| --- | --- | --- | --- |
| Early (roughly 0–25%) | Blank slate; use whatever you find | Low numbers, slow, single attack patterns | Learn the controls; lay the build's foundation |
| Mid (roughly 25–75%) | The build has 1–2 chains online | Numbers and combinations ramp up; elites appear | Refine the build; hand out key components |
| Late (roughly 75–100%) | Power approaches domination; one slip kills | Elites, bosses, stacked mechanics | Cash out the power fantasy; test build completeness |

- **Leave a "steamroll stretch" in the mid game**: it is the payoff for the build and the breath before the climax; resist the itch to nerf it.
- **Difficulty tides**: an overall climb with dips between floors (safe rooms, shops, event rooms). Risk is the player's choice: the route map states danger levels, and "how much risk to eat" is a decision, not a scripted arrangement (see Slay the Spire's route design).
- **Prevent runaway**: cap single-stat stacking (crit rate ceilings, cooldown floors) and put hard gates on "infinitely stackable" mechanics; for version validation, always run two control sets — the "strongest build" and the "weakest build".

### 3.5 The Boundary Between Roguelike and Roguelite

Traditional roguelikes descend directly from Rogue: turn-based, grid maps, one decision per step, and death takes everything with no meta progression. Roguelites keep the two skeletons of "procedural generation + permadeath", swap the turn-based layer for real-time action or cards, and add meta unlocks so that every run, win or lose, deposits something into the account.

## 4. Technical Essentials

- **Generation splits into two layers**: the structural layer (how rooms connect) and the content layer (what goes inside them) are implemented separately. Structure uses "templates + graph connection": pick room templates, assemble the graph under constraints, then validate. Pure noise generation almost always fails on level readability.
- **Generation must always run three validation steps**: connectivity (can all required rooms and exits be reached from the entrance), mechanic reachability (constraints such as jump distance and key order), and density (too empty and too full are both unplayable). If any step fails, reroll the whole layout or fall back to a handcrafted map.
- **Seed system**: one visible seed per run, with identical generation for the same seed (handy for bug reports, speedrunning and daily challenges); generation randomness and combat randomness run as two independent random streams that never contaminate each other (otherwise tuning numbers disturbs the map).
- **Data-driven**: items, enemies, rooms and drop tables are all driven by config tables, so editing a table needs no rebuild; build an in-house balance console (hot reload, direct item grants, room skipping) — without it, late-stage balancing drags the project to death.
- **Saves and results**: meta progress gets a checksum against tampering; results writes use atomic replace (write a temp file, then rename) so a crash can never swallow a run's outcome — this is a bad-review hotspot; new fields must tolerate old saves, since losing a veteran player's save is a trust incident of the highest order.
- **In-run state**: reward events use controlled snapshots that support replays and automated tests; pause and reconnect recovery must preserve the run in progress.
- **Performance**: enemy crowd AI updates spread across frames; projectiles and drops are object-pooled; generation completes during the loading phase so the opening never drops frames.

## 5. Content Volume and Workload Reference

First-version content list (figures are common magnitudes; calibrate to your own cadence):

| Content | First playable version | Full-version reference | Notes |
| --- | --- | --- | --- |
| Room templates | 10–15 sets | 40–80 sets | One room pool per theme |
| Enemies | 6–10 types | 25–40 types | One readable behavior template per type |
| Weapons | 3–5 | 12–20 | Each needs its own game feel |
| Items/upgrades | 30–50 | 120–200 | Cover at least 3 synergy chains |
| Bosses | 1 | 4–6 | One per floor; expensive to redo |
| Events and service rooms | 5–8 | 20–30 | Shops, altars, gambling, rest |
| Unlocks | 5–10 | 30–50 | Characters, weapons, difficulty tiers |

- **Workload magnitude** (solo, full-time, with existing engine experience): the first "plays 10 runs in a row without wearing out" version takes about 1–3 months; taking content and balance to 1.0 adds another 6–18 months. Keep the meta system and the first content unlock within 2–4 weeks.
- **Spend the first 30% of the time on mechanics and tools** (generator, data tables, balance console), adding no art; if the tools fall short, every piece of content piled on later gets reworked.
- **Content burn-rate warning**: roguelite players can burn through a large amount of handcrafted content in ten hours. Sustain playtime with combination density: 100 items that combine with one another outlast 200 isolated items, and the possible build combinations grow roughly with the square of the core item count.
- **Art load**: every item needs an icon, a use effect and compendium text; at 120 items, art is the largest expense, and the art style can be simplified (pixel art, silhouettes, monochrome icons).

## 6. How to Start the First Prototype

Go in order, skip no steps; the whole sequence takes about 4–8 weeks:

1. **Build the "thrill" of a single room first**: one player, one enemy type, one attack set, three items that interact. Do not write the generator yet; hand-place three rooms. Validate three things: does fighting feel good; does picking up the second item produce an "oh" moment; after dying once, do you want another go.
2. **Wire in the pick-one-of-three**: change drops to a choice of three. This is the heart of the roguelite (both Hades and Slay the Spire are driven by it). Structure the options as "two good, one risky", never "one good, two duds".
3. **Run the room loop end to end**: clear a room → door opens → next room → floor mini-boss. A fixed room order is fine; the point is to get the rise and fall of "fight, breathe, fight again" working.
4. **Add death and results**: dying returns you to the base, with one screen showing "what this run brought back"; add the first permanent unlock (a new weapon or character) priced at roughly 2–3 runs' worth of income. At this point the meta loop's foundation is poured.
5. **Only then wire in the generator**: hand the handmade rooms to the generator to arrange, and hook up the content pools. At this stage the variation randomness brings becomes a bonus rather than an excuse for bad game feel.

Acceptance checkpoints (written as observable statements):

- Testers play 5 runs in a row without stopping voluntarily, and from run 3 onward can say which combination they are trying to assemble.
- With no hints, testers figure out the purpose of every resource on the results screen within two runs.
- In 5 runs, at least once the player changes their approach because a specific item dropped.

Not during the prototype: save encryption, multiple characters, achievements, daily challenges, online play. These are amplifiers, not foundations.

## 7. Common Pitfalls

1. **A thin in-run loop**: all growth is parked in meta stats, the run loop itself has no content, and ten runs feel like one.
2. **An over-heavy meta layer**: permanent stats are handed out too freely, erasing the tension of "starting from zero every run", and the roguelite degrades into an idle grind.
3. **Pure randomness with no pity**: a run of bad luck forces the conclusion "trash game" — a bad-review hotspot.
4. **Items that are only plus signs**: all stat stacking with no synergy quality change; everything plays the same and the build never forms.
5. **Piling on content before the mechanics are validated**: one game-feel change and all 100 items are redone — a total loss.
6. **No difficulty tides**: either relentless pressure or a total walkover the whole way through; players go numb or get bored.
7. **Walking distance stuffed into the death cost**: reviving means a three-minute walk back to the death spot, punishing busywork instead of the failure itself.
8. **Runs that are too long**: at 90 minutes or more per run, a single failure stings too much, and players churn in the first hour.
9. **No onboarding**: 30 mechanics dumped on newcomers, with no compendium and no progressive teaching, leave the first five runs lost in confusion.
10. **Balancing by gut feeling**: with no data tables and no fast test loop, versions swing back and forth and nobody can say what is strong or weak.
11. **Generation without validation**: players get wedged into unsolvable or unwinnable states, and "I'm bad" blurs into "the game is broken".
12. **Testing only on yourself**: the designer can recite every synergy answer, so newcomer confusion never surfaces; a roguelite must put the first 10 runs in front of outside players.

## Further Reading

- Game Design Handbook: general methods for core loops, growth curves and randomness design.
- Level Design Handbook: room pacing, guidance techniques and the whitebox workflow — the counterpart to the handcrafted half of this page.
- Programming Handbook: implementation details for procedural generation, data tables and save design.
- Production Handbook: run length, content burn rate and schedule calibration.
- Case Studies: successes and failures from roguelite projects; read alongside this page's pitfall list.
- Pitfalls & Anti-patterns: the high-frequency pitfalls cross-referenced with this page.
