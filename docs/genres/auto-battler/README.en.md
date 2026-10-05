# Ludo Atlas · Genre Handbooks · Auto Battler

> **Genre Handbooks · Volume 2**. Positioning: the genre that makes "building your lineup" the entirety of its decision space. Combat is fully automatic: players complete their purchases, combines and positioning in the preparation phase, then face the verdict in the spectate phase; the winners win on economy and composition, not on hand speed.
> Companions: Game Design Handbook (economy and probability) · Programming Handbook (automatic resolution and data-driven design) · Live-Ops & Growth (seasons and long-term balance) · Indie Survival (scope and scheduling).
> This page carries no external links; cases reference only widely known titles, and the numbers are common orders of magnitude — calibrate them against your own project's measurements.

---

## 1. Positioning and Core Loop

One-line positioning: the auto battler is the genre that **makes its decisions through the shop and the pool, and cashes them in through auto-combat**. Every action happens in the preparation phase and the outcome is announced in the spectate phase — most of a player's win or loss is written before they press "Start".

The core loop, written as a cycle of verbs:

`Prepare (buy units, combine, level up, position, scout) → Start → Spectate (auto-combat) → Settle (win/loss, HP loss, gold) → Prepare again`

The responsibilities and tempo of the two phases:

| Phase | What the player is doing | Typical duration | Output |
| --- | --- | --- | --- |
| Preparation | Browse the shop, buy units, combine and star up, buy XP to level, position, watch opponents | 30–60 seconds | A lineup and a formation |
| Spectating | Watch the auto-combat, read the result, work out how to recover HP or accelerate next round | 10–40 seconds | Win/loss, HP loss, next round's economy |
| Settlement | Collect income, resolve eliminations, move on to the next round | A few seconds to a dozen or so | New resources and standing |

Above the loop sits the match loop: commonly 8 players per game fought down to a single survivor, 20–40 minutes a match; above that sits the season loop, which rotates a batch of units and synergies every few months (§3.4).

Only two preconditions make the loop work: every purchase can be explained (why the shop offered these five), and every defeat can be reviewed (lost on economy, lineup or positioning). Without the first, the shop becomes a blind box; without the second, wins and losses all look like luck.

Drawing boundaries with neighboring genres:

| Neighboring genre | Boundary |
| --- | --- |
| Deckbuilder | Both share the joy of "gathering and choosing", but a deckbuilder keeps playing cards during combat; an auto battler hands over its lineup and stops acting, with every decision pushed up front |
| Tactics (turn-based tactics) | An auto battler is like a tactics game where you "set up and let the system play it out": round-by-round actions are removed, economy and a shared pool are added |
| Tower defense | Both set up and then watch the automatic result; tower defense defends fixed paths against waves, while auto battler is same-scale lineups colliding with multi-player elimination |
| MOBA and RTS | The same management DNA, but the auto battler strips execution and hand speed away entirely, leaving only economy and composition |

A self-check question: if you replaced the auto-combat with round-by-round manual play, would the game be better? If it would, you are probably designing a tactics game; the tension of an auto battler should come from "thinking it through, then pressing Start", not from your fingers.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **A sense of control over your economy**: win for reasons you can explain, lose in a way you can accept. What you find, what you buy, when you spend it all — every one of those is your own decision.
2. **The suspense of spectating**: handing the outcome to the system makes the tension stronger, not weaker. A blowout should be satisfying to watch, a close fight should raise your pulse, and a deciding round should have a moment worth replaying.
3. **Decision density**: the half-minute preparation phase usually calls for three to five small decisions (buy or not, roll or not, level up or not, place where), and a full match adds up to dozens of bets.
4. **A different solution every match**: what you draw, what you win the contest for, what you are forced to swap away — together they force out a lineup and tempo that belong to this match alone.
5. **Catch-up channels**: loss-streak bonuses, draft order, HP-loss mechanics — a temporarily trailing player should still have a comeback route through the mid game.

Anti-patterns (stop and fix the moment they appear): the spectate phase leaves nothing to do but wait; or nobody fights for the first ten rounds and saving gold becomes the only correct play.

Benchmark titles (play them yourself before taking them apart):

| Title | What to take from it | Boundary reminder |
| --- | --- | --- |
| Dota Auto Chess | The genre grammar it established in 2019: the shared pool, combine-three star-ups, interest and win/loss streaks — every later title builds on this foundation | The meta and numbers turned the page long ago; break down the mechanics, not the numbers |
| Teamfight Tactics | The model for seasonal updates: rotating units and synergies on a schedule, replacing endless number patching with "changing the environment" | Big-studio content volume; indie projects should scale down per §5 |
| Hearthstone Battlegrounds | The lightweight route: its own ecosystem and a more intuitive tribe narrative pull players who have never touched an auto battler into their first match | It is grafted onto a mature game; you must supply your own onboarding and user base |
| Battle of the Golden Spatula | The mobile form: touch-screen formation building, fragmented pacing, and a mass-market scale reference | Its characters and platform bonuses cannot be replicated; do not treat a port as the blueprint |

## 3. Design Essentials

### 3.1 The Economy: Make Every Coin Worth Counting

Start by building the income formula; common magnitudes (reference values, calibrate to your own project):

| Source | Typical magnitude | Design intent |
| --- | --- | --- |
| Base income per round | 5 gold | A floor rhythm everyone shares |
| Interest | 1 gold per 10 saved, cap 5 | A hard payoff for saving, creating the core "buy now or buy later" trade-off |
| Win/loss streaks | +1 to +3 gold | Reward or consolation for consecutive results, also a catch-up channel |
| Victory bonus | 1 gold | Slightly separate winners from losers without letting it dominate the economy |
| PvE rounds | Items instead of gold | Trade a change of resource type for a change of tempo |

Interest is the soul of this system: without it, the economy degenerates into spending everything every round; with it, players must weigh fighting strength against interest again and again. The price of saving is HP, and you are buying interest with HP: when HP is healthy, save up to 50 gold and collect full interest; when HP is critical, spend early to buy fighting strength and stop the bleeding; the worst state is being half-committed to both.

Win and loss streaks need symmetry, but they also need brakes: loss streaks pay out too, as a catch-up channel; but if a loss streak's "income minus HP penalty" works out more profitable than a win streak, players will start sandbagging on purpose. Early versions had playstyles that fed specifically on loss streaks and interest — evidence that this curve had drifted. How to check: simulate the two extreme paths, "save from the start" and "spend mindlessly", and see whether the power gap at round ten is acceptable; if the gap is too large, one path has become the only answer.

HP loss on defeat needs design as well: the common formula is a base value plus the sum of the surviving enemy units' magnitudes — a blowout costs more, a narrow loss costs less, so "losing small is winning" and cutting losses in time become playable strategies. PvE rounds and the shared draft are two other tempo regulators: the first swaps items in for gold, the second lets the bottom-ranked player pick first (optional to include).

### 3.2 Shop and Shared Pool: The Odds Table Is Your Value System

The shop commonly has five slots, each rolled against the odds table for the current level. The odds table is a two-dimensional distribution of "level × cost", and its shape matters more than the exact numbers:

| Level band | Low cost (1–2) | Mid cost (3) | High cost (4–5) |
| --- | --- | --- | --- |
| Low level | The mainstay, 70%+ combined | A small garnish | Zero or negligible |
| Mid level | Still rollable on demand | The main band | Starting to appear |
| High level | Mostly from natural refreshes | Transition pieces | The main goal |

The shared pool is this genre's proof of identity: each unit has a fixed number of copies in the match's pool, removed when bought and returned when sold or when a player is eliminated. Two core play patterns grow out of this: contesting units (when others take your core pieces, you can no longer find them and must pivot) and reading opponents (working backward from their boards to what remains in the pool). Pool capacity decreases with cost — typical magnitudes: twenty to thirty copies for low-cost units, around ten for high-cost; capacity doubles as the three-star difficulty table, since a unit needs at least 9 copies in the pool for a three-star to be possible at all, and the smaller the capacity, the harder it is for two players contesting the same unit to both complete it.

The design point of roll tempo: refreshing (spending gold to find units) and leveling (spending gold to raise board size and odds) compete for the same gold, forcing a choice each round. Typical magnitudes: a refresh costs 2 gold, buying XP costs 4 gold, and both XP requirements and board size grow with level — fast or slow pacing lives entirely in these tables.

An often-overlooked trust issue: odds and the pool must be transparent to players. When the odds table can be checked and pool counts are visible, players blame themselves for missing a unit; without that transparency, they blame the game.

### 3.3 Positioning, Lineups and Counters: Space Is a Second Language

Boards commonly come in two shapes: square grids (an 8×8 board or thereabouts) and hex grids (four to six rows). The shape decides how hard distances are to calculate in your head: squares are easy to read, hexes flow more smoothly — pick one and take it as far as it goes.

Positioning answers three questions: who makes contact first (the quality and order of the front line), whether focus fire can form (overlapping attack ranges), and where the core damage dealers hide (protection). From these come the common formations: spread out in a line to seize the opening, tuck into a corner to shield the back line, spread apart to dodge area skills. Formations are not decoration — their value is set by the combat's targeting rules: if targeting is fully random, positioning loses all meaning; the common approach is "nearest-first plus a little controlled randomness", which keeps positioning learnable and reproducible (§4).

Counters work on three layers: the numeric layer (physical against armor, magic against magic resistance), the mechanical layer (diver units striking the back line, control interrupting charges), and the composition layer (front-line quality countering burst). If any one layer dominates, the game is squeezed down to a single answer.

Information and counters feed each other: during preparation you can see opponents' lineups and positioning (scouting), so "this lineup loses — do I switch positioning or switch lineups?" becomes a high-frequency decision. The shared pool keeps pivoting always costly (the loss on selling, the rolls a new direction demands), and the pivot decision is one of the deepest moments in this genre.

A balance self-check: take one lineup and set it in two different formations to fight each other; the win-rate gap should fall in a perceptible range (reference magnitude: 10–20 percentage points). Too small a gap means space has no meaning; too large means a single correct formation exists.

### 3.4 Balance and Seasonal Updates: Turn Patches Into Festivals

Set the metrics before discussing changes. Each version records four groups of numbers: unit and synergy pick rates; each lineup's average placement (4.5 is the neutral line; anything clearly below it is due for a nerf); top-four rates and elimination-round distribution; match-duration distribution. Data finds the anomalies, playtesting finds the causes.

Change levers, ordered from smallest to largest: numbers (attack, health, cost) → odds tables and pool capacity → synergy thresholds → mechanical reworks. If numbers can fix it, do not touch the structure; if you touch the structure, preview and compensate in advance.

Seasonal updates are the standard answer to "balance fatigue" in this genre: every few months (commonly three to six), rotate a batch of units and synergies, periodically zeroing out the balance debt and keeping veteran players' knowledge base fresh. There is one design principle: new-season mechanics must change how you win, not merely swap in a new batch of numbers and skins. Recognize the cost too: players' lineup knowledge and guides expire, and the frustration of the update window needs onboarding, safety nets and familiarity to backstop it.

For the full cadence of versions, previews and player communication, follow Live-Ops & Growth; the discipline for changes is the same as with deckbuilders: one theme per version, community feedback locates the symptoms, and you write the prescription yourself.

## 4. Technical Essentials

**Combat resolution**

- Separate logic from presentation: compute the entire fight first, then play the performance. Speed-up, skipping and batch simulation all rest on this boundary.
- Determinism is the top priority: a fixed logic tick (commonly 30–60Hz), controlled randomness (explicit seeds), a deterministic update order and targeting rules. The same seed and the same inputs must produce the same result — that is the shared foundation for replays, spectating, balance comparisons and bug reproduction.
- Fast resolution mode: running matches in batches with no animation, paired with scripted opponents for self-play, is the daily tool of the balance workshop; do not substitute "playing by hand all day" for it.
- Grids and pathfinding: pathfinding (A* or flow fields) and occupancy management on a square or hex grid. Unit counts are small (commonly 10–30), so performance pressure is light and determinism pressure is heavy.

**Pool and shop**

- The pool is "inventory with a ledger": purchases subtract, sales and player eliminations return, everything recorded at a single point and exportable for reconciliation at any time. Any shortcut that bypasses the ledger will pay its debt in "why can't I find this unit in the pool" bugs.
- The odds table is data, not code: a two-dimensional level × cost table lives in a config file, so tuning it does not require a build.
- For an online version, pool state and roll results are delivered by server authority and clients submit intents only; even for single-player, put this logic in a separate simulation layer and leave a clean interface for multiplayer.

**Data-driven design and the content pipeline**

- Units, skills, synergies and items are all table-driven; skills are assembled from "effect atoms" (damage, healing, buffs, displacement, summons), so new units require no code changes; units with special mechanics carry their maintenance cost annotated separately (methods in the Programming Handbook).
- Synergy counting must be modeled explicitly: who counts, how duplicate units are handled, how thresholds trigger, how bonuses stack. It is the easiest system to write wrong and the hardest to test; a set of unit tests costs an order of magnitude less than chasing the bugs afterward.

**Presentation and experience**

- The spectate show is half the product: skill close-ups, damage numbers, feedback for kills and win streaks, plus one to three speed tiers and a skip toggle. The speed controls must exist during testing — they are both a development tool and a hard player requirement.
- The preparation interface: drag-and-drop, swapping, shop locking, the bench, opponent-scouting toggles; on touch screens, hit areas and gestures must be redesigned — shrinking the desktop layout does not count.
- Publish the information: odds tables, remaining pool counts, damage previews — make them checkable wherever possible. Transparency is the trust foundation of this genre.

**Testing and telemetry**

- Telemetry starts in the prototype: record each match's economy curve, lineup snapshots, placement and elimination round.
- Fixed-seed regression: after each round of changes, run a batch of fixed-seed matches and compare the curves for jumps.
- An economy simulator: get the incomes and outflows in the tables working first, then go into the game and playtest — it saves a great deal of back-and-forth.

## 5. Content Volume and Workload Reference

The following are common magnitudes for projects of this kind, used for scope estimation and constituting no promise.

| Content | First playable version | Full season version | Notes |
| --- | --- | --- | --- |
| Units | 15–25 | 40–80 | 1–3 days per unit (reusing skill atoms); new mechanics add 1–2 days |
| Synergies | 5–8 | 20–30 | Table-driven; the complexity lives in the counting rules |
| Items | 5–10 | 30–50 | Including base components and combine recipes |
| Boards and scenes | 1 | 2–4 | Art volume scales with the number of scenes |
| Match structure | Simplified 4–8 player game | Full 8-player game | Including PvE rounds and the shared draft (if built) |

Workload magnitudes (solo developer with existing engine experience):

- Combat simulation framework (including determinism, pathfinding and the skill system): 3–6 weeks.
- First playable loop (playing a full match through to settlement): 4–8 weeks.
- Content production (20 units with skills and presentation): 1–2 months.
- Balance and polish: 1–2 months minimum after the first version; for a seasonal product it is an ongoing cost.
- To 1.0: 6–18 months solo (reference range, varying with content scope and multiplayer scope).

Art and text magnitudes: units need character art or models, skill VFX, and shop portraits and icons; reusing VFX by skill atom saves the bulk of the work. Text volume is small, but synergy and skill descriptions must be consistent with the implementation — generate descriptions from the same source as the data.

## 6. How to Start the First Prototype

Goal: a minimal loop in 2–3 weeks that leaves you wanting "one more match" — single-player only, text interface only, touching no art, seasons or multiplayer.

1. (Half a day) Whitebox economy: use log text to run the "gold, buy XP, refresh, interest" income-and-outflow loop; prove this table works first.
2. (1 day) Two units auto-fighting: movement, attacks, HP loss, death; logic separated from presentation, reproducible from the same seed.
3. (1–2 days) Pool and combine-three: a mini pool of 8 units; purchases subtract, sales return, three of the same combine and star up.
4. (1 day) Shop and odds table: a five-slot shop, level-based odds, refresh and lock; the odds table lives in a config file.
5. (1–2 days) One complete match: one human plus several scripted opponents, running eliminations and settlement through to a placement.
6. (1 day) Positioning and scouting: drag to reposition, opponent boards visible, so the "look before you place" decision emerges.
7. (1 day) Speed-up and telemetry: spectating can be accelerated and skipped; economy curves and placements recorded.

Playtesting and acceptance (all observable):

- Find 5 people who have never played, and record only three numbers: whether the first match finishes within 20 minutes; how many spontaneously say "next match I want to try a different lineup"; whether anyone voluntarily starts another match within 10 seconds of being eliminated.
- With all art removed and a pure text interface, testers still want to play three matches in a row.
- After a match, at least half the testers can state one economic lesson of their own (e.g. "I should have stopped the bleeding earlier"), rather than attributing the loss to draw luck.

Not in the prototype: seasons, ranked play, skins, multiplayer, spectating systems, mobile support, achievements. These are amplifiers, not foundations.

## 7. Common Pitfalls

1. **No interest, or interest too strong**: with no interest, the economy degenerates into spending everything every round; with interest too strong, the whole lobby saves early and nobody fights. Interest is a starting point, not an endpoint — tune it together with HP loss and loss-streak rewards.
2. **Loss streaks more profitable than win streaks**: sandbagging becomes the optimal play. Keep loss-streak income symmetrical or slightly lower, then stack the HP-loss penalty on top and redo the full accounting.
3. **Pool counts pulled from thin air**: three-star odds, the tension of contested units and the scarcity of high-cost units all hinge on them. Work backward from "how many players can complete a three-star of the same unit at once" to set capacity, then calibrate through playtests.
4. **Odds hidden from players**: missing your core unit means cursing the game. Make odds tables and remaining pool counts checkable, and give players back the right to interpret their own luck.
5. **Reroll variance out of control**: several rounds without the key unit collapses a match's experience. Use pity systems, dynamic weighting or pool hints as a backstop; do not let luck veto management with a single roll.
6. **Fully random targeting**: positioning loses its meaning and spatial decisions are void. In-combat randomness must be controlled and readable.
7. **Combat that is not reproducible**: the same seed producing two different results makes balance comparison impossible and bug reproduction too. Build a fixed tick and controlled randomness from day one.
8. **No speed-up for spectating**: half an hour of animations every match, and veteran players churn first. Speed-up and skip are the minimum spec before release.
9. **Synergies that are pure numbers**: "+attack, +health" stacked across the whole table makes every season the same dish re-plated. New mechanics must change how winning works, even if only a few of them do.
10. **Balancing from community screenshots**: nerfing whatever gets complained about makes the mess worse. Use pick rates and average placement to locate problems; community feedback is for finding symptoms.
11. **Seasonal rotations that hit too hard**: wiping out everything players learned in three months all at once. Keep part of the mechanics stable (leave the economy and core rules alone), control the proportion replaced each time, and announce the changes in advance.
12. **Custom code per unit**: as content grows, the engineering schedule explodes. Atomize skills and annotate exceptions separately.
13. **Multiplayer before simulation**: a fight that cannot even be reproduced offline will only have its problems amplified online. Make the single-player resolution reproducible and batch-runnable before talking about server authority.
14. **Building combat but not spectating**: minutes of preparation paid off with an unreadable brawl turns all the earlier management into sunk cost. Spectating is the payoff moment — presentation and information design deserve the same care as combat resolution.

## Further Reading

- Game Design Handbook: general methods for core loops, economy and randomness design; corresponds to §3 of this page.
- Programming Handbook: implementation details for data-driven design, simulation loops and performance; corresponds to §4 of this page.
- Live-Ops & Growth: season cadence, version communication and long-term operations — the full expansion of §3.4.
- Indie Survival: scope control and scheduling, complementary to §5.
- Multiplayer & Backend: the full ledger of server authority, matchmaking and anti-cheat for moving the shared pool and rooms online.
- Pitfalls & Anti-patterns: pitfalls around balance churn and runaway content, to be read alongside §7.
- Homework: play 10 hours of Teamfight Tactics or Dota Auto Chess and record two things: which round the worst-value purchase of each match happened on; and at the moment you lose, whether you can say whether you lost on economy, lineup or positioning. Only when you can answer both questions are you truly getting started.
