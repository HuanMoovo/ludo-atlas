# Ludo Atlas · Genre Handbooks · Extraction Shooter

> **Genre Handbooks · Volume 4**. Positioning: the shooter genre that turns "only what you carry out counts" into its core tension. Gear has real ownership: entering a raid is a bet, extracting is cashing out, and dying is liquidation; this page covers the four-ring formula, the psychology of risk and loss, map and spawn pacing, the meta economy and stash, server authority and anti-cheat, and the small team's reality check.
> Companions: Game Design Handbook (core loops and economy balance) · Programming Handbook (server architecture and performance) · Multiplayer & Backend (sync, anti-cheat and economic security) · Indie Survival (scope and scheduling).
> Division of labor: the full path of sync models, anti-cheat and backend costs belongs to Multiplayer & Backend; this page settles only the gameplay side — and whether you can afford to build it. This page carries no external links; benchmark titles are widely known works only, and the figures here are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

One-line positioning: the extraction shooter (community nickname "extract-and-fight") is **the shooter genre that turns "only what you carry out counts" into its core tension**. Players bring the gear they have accumulated outside the match into a raid, loot supplies, trade fire with AI and players, and walk out alive through an extraction point — only then is the haul truly theirs; die, and everything on you stays in the map. Escape from Tarkov fixed this formula; Arena Breakout carried it to mobile.

Family position: it is filed under the shooter family, but its skeleton is **a single-match loop that wagers assets**, independent of theme: swap the modern military for a weird-tales era and the wager structure does not change. Gun feel and hit feedback share their roots with FPS (see Genre Handbooks · FPS); tactical depth is borrowed from hardcore shooters, and long-term motivation from looter and survival genres.

The core loop, written as a verb chain:

`bring gear into the map → loot and fight → weigh the backpack against the situation → head for the extraction point → carry out and cash in, or lose everything → sort the stash and queue the next raid`

The four-ring formula is "enter, loot, risk decision, extract" — each ring solves one problem, and this is the skeleton of the whole page:

| Ring | What the player is doing | Problem it solves | What breaks without it |
| --- | --- | --- | --- |
| Enter | Decide what gear to bring and which map to enter | Converts outside accumulation into in-raid combat power; gives every match a real bet | Gear loses ownership, gains and losses carry no weight, and the meta economy stalls |
| Loot | Search containers and bodies, make trade-offs in a limited backpack | Creates a resource curve and turns "what is valuable" into player knowledge | No objectives; the match degenerates into a pure gunfight |
| Risk decision | Push your luck or extract, detour or push straight through, fight or hide | Turns "when to call it" into each match's heaviest decision | Pacing collapses into a straight line; the tension between greed and fear disappears |
| Extract | Walk out alive through an extraction point and cash in the loot | Gives the match a clear survival line, and charges the next one | Death and success become indistinguishable; the loop breaks |

A match commonly runs 10–30 minutes (reference). Fast-paced short maps and slow-infiltration long maps are two product routes: the former compresses a match into ten-odd minutes and encourages repeated deployment; the latter stretches the infiltration feel with map scale and movement cost; pick one route at kickoff and see it through.

Drawing boundaries with neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Battle royale | Battle royale resets everything each match and asks only for a survival placement; the extraction shooter carries loot out of the map and accumulates it across matches — the bet is the assets in your own stash |
| Looter shooter | In a looter shooter, drops serve stat growth; extraction-shooter items have a real economy and two-way gains and losses — picking something up does not count, carrying it out does |
| Survival-crafting | Survival-crafting is a continuously co-inhabited long-term world; every extraction-shooter match is a standalone infiltration that only lands when you are back in the stash |
| Roguelike | A roguelike's failure costs only time, with gains settling into permanent progression; extraction-shooter failure directly loses the physical assets you brought in |

One line on the boundary with Genre Handbooks · Battle Royale: battle royale is a one-match, reset-on-death survival elimination; the extraction shooter is an asset gamble where you bring your belongings in and carry them home when you win.

A self-check question: if you removed the "only what you carry out counts" rule (dying costs no gear, loot goes straight to storage), would the game still stand? If it would, you are making a looter shooter or a co-op shooter, not an extraction shooter.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **The weight of gain and loss**: every piece of gear you bring into a raid was accumulated bit by bit outside; every outing is a bet of real value. This is the genre's main emotional power supply.
2. **The tug of greed and fear**: the backpack is almost full, there are footsteps outside, and the extraction point is not open yet. A match's peak is often not a gunfight but this inner negotiation; the point of the design is to make the negotiation happen every match.
3. **Hunting and being hunted**: hunter and prey swap roles at any moment. Listening for footsteps, flanking to set an ambush, harvesting a cleanup fight — PvPvE gives every match two games at once: "against people" and "against the environment".
4. **The stash's growth**: from one battered gun to a wall of collectibles — the stash is the player's trophy room and the carrier of long-term goals.
5. **Stories worth telling**: a rags-to-riches run, a last-second extraction, a teammate holding the rear — narrow escapes become anecdotes, and the density of social currency decides the spread.

Benchmark titles (play a dozen-plus matches yourself before breaking them down; the betting psychology only clicks once you are in it):

| Title | What to learn from it |
| --- | --- |
| Escape from Tarkov | The genre definer: realistic ballistics and locational damage, grid backpacks and the long body-search ritual, no crosshair; the ceiling of the hardcore route and a concentrated display of every hard problem in the genre |
| Arena Breakout | The mobile flagship: simplified the hardcore formula and rebuilt the controls and UI for the phone; a complete sample of mainland publishing and long-term operations |
| Hunt: Showdown | Moved the extraction structure into a weird-tales era: kill the boss, seize the bounty, extract; permanent-death hunters; the slow pacing of antique firearms — proof that both theme and pacing can be swapped |
| The Division (Dark Zone) | An early prototype: contaminated gear had to be extracted for recovery, and squadmates could betray at any moment — proof that "only what you carry out counts" holds inside a looter game too |
| Delta Force (Hazard Operations) | Free-to-play extraction at big-studio scale: seasonal content and a live-ops pipeline sustain the heat; shows how the formula can be made competitive and scaled up |

Common ground: asset wagers and extraction payoffs are the shared foundation; the differences are in theme, pacing and degree of hardcore. Competition at the top concentrates on realistic hardcore depth and content updates, which connects directly to the small-team accounting in §5.

## 3. Design Essentials

### 3.1 Risk and Reward: Making "the Bet" a Tunable Parameter

This genre's emotional engine is loss aversion: losing a piece of gear hurts noticeably more than finding one of equal value feels good. The design goal is not to eliminate that pain but to tune it to a magnitude that is bearable and reviewable. Start by establishing three knobs:

| Knob | What it controls | Consequences of tuning it wrong |
| --- | --- | --- |
| Entry cost | Sets a match's bet size; the lower the cost the bolder players are, the higher the more cautious | Cost too high and nobody dares deploy; cost too low and gains and losses lose their weight |
| Return expectation | Sets "how much is worth being greedy for"; the value distribution decides where players move on the map | Returns too high across the board cause inflation; too low and nobody is willing to take risks |
| Loss recovery | Decides "what is left after a loss"; insurance, guaranteed minimums and relief channels all sit in this band | Without recovery mechanisms, bankrupt players quit the game outright |

- **A guaranteed way back in**: provide a zero-cost or very-low-cost entry (common practices: a free character, a loaner loadout, a daily relief package) and delete the "cleaned out" state from the system. Bankruptcy protection is not charity; it is retention design.
- **Insurance mechanics**: let some gear return to the stash under specific conditions — insurance attached to every bet, and a valve for tuning players' risk appetite.
- **Risk layering**: high-value areas and targets come with high risk; low-value routes leave a way out for conservative players. The payoff curve is like peeling an onion — those who dare go deeper get the meat, those who do not still pick up scraps.
- **The extraction-rate metric**: watch the ratio of "matches carried out ÷ total matches". Too high means insufficient pressure; too low and the penalty is out of control and players bleed value long-term; it may fluctuate with patches, but it cannot stay out of control.

### 3.2 Maps, Spawn Points and Dynamic Pacing (PvPvE)

The map is this genre's stage board: players, AI, resources and extraction points are all placed on it, and every match's action is a recombination of these four. Fix three things first; talk about randomness only after.

- **Player spawns**: arrange them for "no face-to-face at the start" — multiple spawns distributed across map edges and the interior, so two teams are not forced into mutual attrition within ten seconds of kickoff; give the location pool and spawn time window controlled randomness, so spawns cannot be memorized and camped.
- **Loot spawns**: containers and supply points come in three tiers. The guaranteed tier ensures basic returns on any route; the competitive tier concentrates in hot zones to create encounters; the surprise tier uses low-probability, high-value items to create sudden-riches stories. Configure the spawn table by area weights and manage everything in tables (for number-table methods see the Game Design Handbook).
- **Extraction points**: the match's closing decision point. The common combination is fixed, random and conditional points (time-limited, item-gated, paid) used together; there must be enough of them, spread apart, with cover and detour routes nearby — otherwise camping overwhelms normal play.

AI is PvPvE's third line of pressure: trash mobs supply resources and noise, elites guard high-value areas, and bosses generate public events. AI does not replace players; it heats the map: where there is gunfire there is a story, and where there is a story people gather. Hearing is this genre's first information channel — footsteps, breaking glass, reloads and healing sounds must rank at the very top of the audio budget.

Dynamic pacing is sustained by a timeline and public events: the match clock, boss activation, airdrops, contestable objectives — each of them tells players on the map "where to be now". Checklist: does the match naturally produce encounter peaks? Is camping one extraction point more profitable than normal play? Is there any route nobody touches all match?

### 3.3 The In-Match Economy and the Meta Stash (the Gear Loop)

The extraction shooter has two economic layers: in-match is "what you find", meta is "what you keep", and the two are gated by the extraction point. First principle: everything that can be carried out must have an outlet and a use — otherwise it is just a number taking up grid space in the backpack.

Items fall into four categories by purpose: combat (weapons, ammo, armor), sustain (medical, food, throwables), quest (designated collectibles) and treasure (purely for selling). Treasure is the main source of loot feel; its value gradient must be spread wide, so one glance tells the player whether it is worth the risk. Three questions for item design: what problem does it solve? How much is it worth? Does it have a second use (crafting, trading, quests)?

The meta stash does four things: storage (capacity itself can be a progression line), organizing (sorting and batch operations must be smooth — a messy stash is a churn reason), trading (the market turns items into prices, and prices turn items into knowledge) and sinks (crafting, building and quests all eat stash stock). The sink is a first-order priority: an economy with output but no sinks inflates, and players quickly find nothing is worth anything; the common approach is quest systems, crafting recipes and periodic sink events working together, with prices and currency velocity watched from the backend (for monitoring methods see Multiplayer & Backend §6).

The gear loop's intensity knob is the ratio between "lethality" and "insurance depth": the shorter the time-to-kill and the harder the gear gap, the more weight muscle and calculation carry, and the harder it is for new players to turn things around; the deeper the insurance and the thicker the guarantees, the lower the betting threshold — but the tension is diluted. Both directions can work; what to fear is being stuck in the middle, pleasing neither.

### 3.4 Trust Design: Every Loss Must Be Accounted For

In this genre, "where did my stuff go" must always have a clear answer. The death-experience trio: the killer's viewpoint (who, from how far, with what weapon), the damage record (what hit me) and the loss list (what I lost). Miss one and players will put the blame on the system and on cheaters.

- Death replays or killer viewpoints are standard; do not get stuck debating whether "replays leak tactical information" — the cost of concealment is far higher.
- Death settlement must be fast and clear, and immediately offer the next step: refit, deploy again, or switch to a more conservative route. The time from death to the next deployment is the retention funnel second only to the opening experience.
- Trades and transfers must be logged: which item went from whose backpack to whose market — only a complete chain allows economic security (Multiplayer & Backend §6).

## 4. Technical Essentials

### 4.1 Server Authority: This Genre's First Engineering Iron Law

The extraction shooter falls into the competitive-match tier; per the tiering in Multiplayer & Backend there is no suspense: dedicated servers plus server-authoritative simulation. P2P and client authority lose on both cheat boundaries and economic security. Compared with a standard shooter, this genre has one extra class of core asset: **items**.

- Backpacks, stash, trades and drops are all server-authoritative; the client is presentation only. Every change in items must be recorded in a ledger that can be audited and rolled back (Multiplayer & Backend §6).
- Movement and shooting run on server authority plus lag compensation, and hit detection must let players hit the target they see; actions like searching bodies, picking up and opening doors get action locks and state sync to avoid the tearing "I picked it up, but you say I didn't".
- Match instances have lifecycles: create, settle, reclaim. Reconnection must return players to the original match — otherwise one network blip equals liquidation, and mobile-network players churn on the spot (the checklist in Multiplayer & Backend §9).
- Compensation rules for server crashes or rollbacks must be written down in advance: how insurance is counted, how gear brought into a map but not extracted is counted. Clear rules matter more than generous compensation.

### 4.2 Anti-Cheat and Economic Risk Control

Anti-cheat is one of the highest-leverage investments in this genre: what a cheater carries out is not a kill but assets that can flow into the market and contaminate the whole loop; one person running cheats stirs the prices of an entire server. Execute the three-layer structure from Multiplayer & Backend §7 — not one layer is optional:

| Layer | What it does | Who it targets |
| --- | --- | --- |
| Client-side detection | Integrity checks, memory scanning, driver-level solutions | Scatters amateur cheaters |
| Server-side analysis | Behavioral statistics and anomaly detection: hit rate, input frequency, movement patterns, economic flow rate | The main target: professional cheating and scripts |
| Reports and review | Report entry points, data evidence, human judgment, tiered bans and appeal channels | The backstop, and public opinion |

Economic risk control matters as much as anti-cheat: item duplication, value transfer and black-market trading are a second illicit chain independent of gunfight cheating. The countermeasures are server authority plus audit logs plus abnormal-flow rules, with account-level suspicious trades frozen and traced back (Multiplayer & Backend §6). This is adversarial spending — budget it by commercial scale, not as a moral issue.

### 4.3 Map Loading, Audio and Performance

- Large maps rely on streaming: chunk the world, load and unload incrementally by distance; machines of different tiers must "hear the same gunfight and see the same encounter" — fairness before saving money.
- Give audio its own budget: footsteps, gunshots, doors and healing sounds rank at the highest priority, on dedicated channels with distance-attenuation models. It is the first information channel — cutting audio equals cutting information.
- Corpses and dropped items are the map's performance and state baggage: tiered updates, object pooling and timeout cleanup are all required; at the same time, budget for loot visibility — the body-search experience is part of the genre and must not be turned into a black box for performance's sake.

## 5. Content Volume and Workload Reference

The following are common magnitudes for projects of this kind, used for scope estimation and constituting no promise. Numbers are a ruler, not a promise; calibrate with your own team's speed.

| Form | Content magnitude | Timeline magnitude | Team magnitude |
| --- | --- | --- | --- |
| Gameplay prototype (offline or small-scale online) | 1 greybox map, 10–20 items, 1 simple stash | 2–4 months | 3–5 people |
| Shippable small-scope title | 1–2 finished maps, 50+ items, quest lines, a basic market | 1–2 years | 10–20 people |
| Mainstream-scope title | Multiple maps plus a season pipeline, hundreds of items, a complete economy | 2+ years for the first release, then a seasonal cycle | 50+ people |

Module-level accounting (reference):

| Module | Minimum playable | Comfortable scale | Notes |
| --- | --- | --- | --- |
| Map | 1 greybox map | 2–3 finished maps | Every map needs a full gradient of routes, hotspots and extraction points; the art volume is on par with a complete tactical-shooter map |
| Weapons | 5–8 | 15–20 | Every gun needs an ammo lineage and mod attachments — ammo and armor penetration are the real balance knobs |
| Items and gear | 30–50 | 150+ | Every item needs a price, a use and a sink; the item table is the content volume itself |
| Quest lines | One tutorial chain | One set per map, progressing by level | Quests are the steering wheel of a free sandbox and the means of directing where players go during development |
| Economy and live-ops | Manual price tweaks | Monitoring plus a tuning pipeline | The three tables — prices, output and sinks — must be updatable weekly; this is the standing work of operations |

**The small team's reality warning.** Put the four bills on the table before deciding whether to build one: the server and ops bill rises with peak CCU (Multiplayer & Backend §8); anti-cheat and risk control are the most adversarial standing costs, and failing at them directly destroys the economy and retention (§4.2); the output demands for items and map content are high, and the economy needs continuous rebalancing — this is the most operations-intensive kind of game; top products pour heavy investment into realistic hardcore depth and content updates, head-on competition has no chance of winning, and differentiation can only come from theme, pacing or scope. There is also one easily overlooked bill: game feel, traps, camping and economy balance are full-time jobs, not something that only moves at release.

If the four bills add up to too much pressure, the fallback options ordered by degree of compromise: small-scope online (10–20 players, small maps, fast pace); a PvE or co-op route (keep the search-and-extract skeleton, replace PvP with bots or co-op — existing titles have proven this path viable); single-player extraction (package the mechanics into a single-player or lightly online experience and remove the ops and anti-cheat costs entirely); lending "only what you carry out counts" to other genres (survival, roguelikes and co-op shooters can all use it — the mechanics can be pulled out and reused). Scheduling anchors: prototype 2–4 months; vertical slice (one map at release quality plus a complete match) 6–12 months; extrapolate the launch version as content scope times a polish factor.

## 6. How to Start the First Prototype

The first prototype needs to validate exactly one thing: **whether "only what you carry out counts" can get its hooks in**. Offline before online, small map before big production; budget 4–8 weeks.

- **Weeks 1–2: offline single-map loop.** One small greybox map, 3 spawn points, 2 extraction points, a handful of loot containers, a few AI dummies; the player deploys with a virtual loadout, dies to empty, extracts to storage. Skip services and accounts for now; use local saves to validate whether the "greed or extract" decision arises naturally.
- **Weeks 3–4: wire up multiplayer.** Start on an off-the-shelf backend (Multiplayer & Backend §5: all-in-one solutions like Nakama and Colyseus) and run 8–12-player matches with real players; server-authoritative movement and shooting, backpacks and stash on the server; accept lag and roughness for now and observe where players move, when they start fighting and how soon they extract.
- **Weeks 5–6: fit the most minimal economy, then tune parameters only.** Market, quests and insurance all get minimal versions, purely to validate "is it worth it"; then pull 8–12 people into custom matches and record three numbers: extraction rate, time from death to the next deployment, and average extracted value. After that, change only numbers and layout, add no new systems.

Success criteria (all observable):

- With all art and audio removed, testers still want one match after another, a single session usually running over an hour.
- Testers can spontaneously tell at least one story of "almost didn't make it out" or "made a nice little profit".
- Most testers who lose a loadout are queuing the next match within minutes, rather than closing the game to cool off.
- Some testers start researching on their own which route is safest and which crate is the most valuable. The moment knowledge accumulation appears is the harbinger of a working economy.
- Change any single spawn rate or price parameter, and within 5 minutes you can read its effect on extraction rate and average returns from the logs.

## 7. Common Pitfalls

1. **Guns first, economy later**: the skeleton is the asset wager, not gun feel; mass-producing weapons and mods before the economic loop is validated makes rework extremely expensive.
2. **Death penalties with no floor**: a bankrupt player with no guaranteed way back in quits after one disastrous loss; guaranteed entry, insurance and relief gear belong in the first version.
3. **Runaway inflation and deflation**: with nobody watching the three tables — output, sinks and prices — items quickly become dirt-cheap or a bottomless pit; economy monitoring ships alongside gameplay.
4. **Extraction points camped**: fixed positions, too few of them, no cover around — camping outearns normal play; use more points, randomization and terrain fixes (§3.2).
5. **Cheats and illicit trade ungoverned**: assets carried out by cheaters contaminate the whole market, and duplication and black-market money are the second illicit chain; server-side analysis and economic audits must exist from day one (§4.2).
6. **Gear phobia**: good gear never leaves the stash out of fear, players only ever play junk-loadout matches, and in-match intensity and content consumption both collapse; use guarantees, insurance and acquisition curves so good gear is "affordable to use" (§3.1).
7. **PvPvE ratio out of balance**: PvE only turns it into a single-player farming map, PvP only turns it into an arena; AI needs presence without stealing the show.
8. **Spawns and loot runs memorized**: fixed positions and fixed rhythms have players rote-memorizing the tables after fifty matches; randomize as a set — location pool, time window and weights together.
9. **Quest lines running dry**: once the quests are eaten through, players have no next goal and churn begins immediately; quest design needs a steady output rhythm, or equivalent self-set goals.
10. **Scope out of control**: maps, items and systems laid out at top-title scope, none of them finishable; build one map's complete loop first, then talk about scaling up.

The extraction shooter looks like it is selling gunfights and looting, but what it actually sells is the weight of the sentence "this is mine": everything you carry out of the map first has to survive someone trying to take it.

## Further Reading

- Game Design Handbook: core loops, economy and number-table methods — the full source draft behind §3.
- Multiplayer & Backend: the full expansion of §4 of this page — sync models (§2), service layering (§3), economic security (§6), anti-cheat (§7), cost and operations (§8).
- Indie Survival: scope and scheduling; before deciding to build an extraction shooter, read the four bills in §5 twice.
- Pitfalls & Anti-patterns: scope, economy and content-production pitfalls — read alongside §7.
- Genre Handbooks · Battle Royale (Volume 3): a comparison for single-match structure and opening pacing — boundary in §1.
- Genre Handbooks · FPS (Volume 2): the four elements of gun feel and hit feedback, the shared foundation of the combat layer.
- Case Studies: case-postmortem methods, to consult when breaking this genre down.
- Homework: pick an extraction shooter and play ten matches yourself, logging one line per match — value brought in, value carried out, cause of death, and the one item in your backpack you would least want to lose; then build an 8-player greybox match and have friends play three rounds, observing the situation in which they first voluntarily extract early.
