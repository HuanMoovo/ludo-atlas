# Ludo Atlas · Genre Handbooks · Idle / Incremental

> **Genre Handbooks · Volume 1**. Positioning: a raising genre where time stands in for operations — one of the genres with the lowest engineering barriers and the highest balance barriers, and a common direction for indie developers to train their craft and monetize.
> Companions: Game Design Handbook (loops and balance curves) · Programming Handbook (settlement and saves) · Production Handbook (scope and content cadence) · Indie Survival (the solo path and business models).
> This page deliberately carries no links. The fun of idle games lives in the curves: reading ten analyses is worth less than working out the first ten minutes of numbers by hand.

---

## 1. Positioning and Core Loop

Idle and incremental are often used interchangeably: the former stresses "it produces while you are away", the latter "the numbers keep growing". Mature works are almost always a fusion of the two: the player makes the decisions, the game works in the player's place, and time accumulates on the player's behalf.

In one line: **the player uses a limited number of decisions to raise the production rate, and time completes the rest automatically.** The core loop:

`produce → buy upgrades → production speeds up → unlock a new tier → prestige reset → produce faster`

What is genuinely scarce in this loop is the player's decisions, not the player's actions. The ideal state is "glance every few minutes, make one decision, leave satisfied"; the moment any layer has "nothing to do", the player leaves.

| Layer | Player action | Feedback | Typical interval |
| --- | --- | --- | --- |
| Second scale | Clicking, watching the numbers | Numbers ticking, sound effects | 0.1–1 second |
| Minute scale | Deciding what to buy | The output rate jumps a tier | 10–60 seconds |
| Hour scale | Unlocking a new system | New mechanics, new units | 1–3 hours |
| Day scale | Returning offline, resetting | A large speed-up | 8–24 hours |
| Week scale | Content updates, new tiers | New goals | 1–4 weeks |

Every layer needs a "next temptation" planted in it: an upgrade within reach, an unlock sitting at 87%, an offline countdown almost full. Self-check: come back an hour later, play for 3 minutes — if there is not a single decision worth making, that layer is short on content.

Boundaries against neighboring genres: management sims demand continuous operation (placing, scheduling), while idle games compress operation to a minimum and sell waiting itself; the roguelite restarts for randomness and execution, the idle game for time and numeric accumulation; raising card games can be stitched on (idle play plus character raising is the mainstream form in China), but the core loop's first principle is still the production rate.

Good fits and bad fits: good for solo developers and small teams, low budgets, and projects that want to train balance design; a bad fit for projects chasing game feel, heavy narrative or heavy art, and for teams without the patience for long-term updates.

## 2. Player Experience Goals and Benchmark Titles

Experience pillars (align every decision with these):

1. The thrill of growth: the numbers grow visibly larger, and "larger" has ceremony (tier jumps, digit carries, qualitative leaps).
2. The pleasure of optimization: buying the right tier and timing the reset correctly are rewarded on the intellectual level.
3. Treated well by time: leaving pays, returning surprises, and nothing feels like punishment.
4. Pressure-free companionship: no focus required, pick up and put down at will, suited to a second monitor and fragmented time.

Negative goals (any one of these is a failure): the punishment of wasted offline time, the coercion of being chased by push notifications and ads, the boredom of nothing but mechanical repetition in the mid-to-late game. Day-one acceptance: at least 3 "clearly faster" moments within 10 minutes; back to full speed and a new goal within 5 minutes of returning after an overnight absence.

| Title | Form | What to learn from it |
| --- | --- | --- |
| Cookie Clicker | Web (since 2013) | The founding text of clickers; the ceiling of achievement and easter-egg culture; a textbook balance curve |
| Clicker Heroes | Web / mobile / Steam | The three-part structure of click, hire, reincarnate; the popularizer of big-number formatting |
| AdVenture Capitalist | Mobile / Steam | Parallel idle lines; events and timed bonuses; the mobile return loop |
| Melvor Idle | Web / Steam / mobile | A skill system that adds depth to "waiting"; the balance between active and idle play |
| AFK Arena | Mobile | The commercial fusion of idle production and card raising; daily-rhythm design |
| King of Salted Fish | Mobile (the Chinese mini-game ecosystem) | The combination of idling and lightweight battles; a domestic mini-game publishing path |

When reading these cases, watch three things: how many upgrades the first 10 minutes hand out, at what minute prestige unlocks, and what formula offline earnings use. These three largely decide success or failure.

## 3. Design Essentials

### 3.1 Time Dilation and Offline Earnings: Designing "Coming Back" as a Reward

Time dilation means the value of in-game time far exceeds real time: what took an hour of production at the start is made up in seconds later on. The dilation factor is the felt unit of "getting stronger", sourced from exponential growth in the production rate (see §3.2). Take doubling production every 15 minutes early on: 4 hours is 16 doublings, about 65,536×; what the player perceives is not "I played for 4 hours" but "one second now equals an hour before". Protect that feeling, while avoiding inflation so fast that all the content is cleared in a few hours.

Offline earnings formula skeleton (usable as is for the first version):

`offline production = min(offline duration, cap) × production per second × efficiency factor`

- The cap starts at 2–4 hours and can be upgraded to 12–24 hours. Sleeping for 8 hours is the most frequent offline scenario; the cap should cover at least that.
- The efficiency factor runs 25%–100%; keep offline slightly below online (say 80%) to preserve the motive to play online, but not so low that it hurts.
- Reference values: 10/second idling for 8 hours at 100% efficiency is about 288,000; with a 4-hour cap at 50% efficiency it drops to just 72,000 — whether that buys the next tier is obvious at a glance.
- "Offline efficiency +10%" and "offline cap +2 hours" are the most popular prestige-shop shelf items; the upgrades themselves are content.

The three-beat return of "log in and get stronger" (fixed order):

1. Settlement presentation: popups, rolling numbers, sound effects — even automatic credit must be staged; players do not remember money they never saw.
2. A purchase is possible within a minute: offline output should equal roughly the price of 1–3 current key upgrades. Affording nothing is a letdown; affording everything skips the decision.
3. A new goal appears: unlock progress, a teaser for a new unit or a prestige preview — any one of the three, guaranteeing a "next step after seeing the earnings".

Other return hooks: offline build/research queues, offline random events, daily chests, idle auto-buy unlocks. One principle: offline time that only pays money is wasted — it should also supply "decision material".

### 3.2 Exponential Curves and Number Formatting: The Craft of Working with Numbers

Why exponential is non-negotiable: player output grows exponentially, so if upgrade prices were linear, a late-game player would buy a hundred per second and decisions would vanish. The price curve must be slightly steeper than the production curve, so that "the next one" always costs a few minutes of waiting. Classic formula: price `cost(n) = base price × r^(n-1)`; output jumps by tier, with each tier about 5–10× the one before.

r is the single most important dial in the whole game; common values run 1.07–1.15:

| r | Purchases to double the price | Price of the 100th unit, as a multiple |
| --- | --- | --- |
| 1.05 | About 14 | 125× |
| 1.07 | About 10 | About 811× |
| 1.10 | About 7 | About 12,500× |
| 1.15 | About 5 | About 1.02 million× |
| 1.25 | About 3 | About 3.9 billion× |

Take a base price of 15 and r = 1.15: the 25th copy costs about 429 (28.6× the original price). If r is too small (1.05), players buy dozens in one go and the repeated actions wear them out; if it is too large (1.25), two purchases and they can no longer afford a third. A common approach: use a large r early to create rhythm, then switch to a smaller r in the mid-to-late game to stretch the decision intervals.

Milestone number tables: do not hand-fill every level — write a generation rule plus key thresholds. For example, "every 25 owned permanently doubles that tier's output (stacking)":

| Cumulative owned | 25 | 50 | 100 | 200 |
| --- | --- | --- | --- | --- |
| Cumulative multiplier for that tier | ×2 | ×4 | ×16 | ×256 |

Milestones turn "buying quantity linearly" into "pushing toward quantity with checkpoints", and supply raw material for achievements and progress bars.

Big-number systems (number formatting): up to around 10^4 a number is readable by anyone; past 10^6 it must be formatted. Three approaches:

| Approach | Display example | Pros | Cons |
| --- | --- | --- | --- |
| Scientific notation | 1.23e15 | Universal, simple to implement, never expires | No sense of growth narrative; reads like lab data |
| Tiered units | 1.23 trillion / 1.23 aa | Ceremony at each jump; controllable pacing | Requires maintaining a unit table; localization is a hassle |
| Hybrid | Custom units early and mid, scientific notation past 10^15 | Gets both | The switch point needs readability testing |

Two routes for custom units: the Western K/M/B/T/Aa/Ab double-letter carry (popularized by Cookie Clicker) and the Chinese wan/yi/zhao/jing ladder. For Chinese-speaking players use wan and yi, and switch straight to scientific notation past 10^16 — otherwise nobody can read the "zhao yi jing gai" string out loud. Three more points: show only 3–4 significant digits (12.3 wan, not 123,456); the length of the number is itself a progress bar; the carry moment needs presentation (999 to 1000 gets a color change and a sound effect). Keep the data layer and the display layer separate, computing internally with a uniform scientific-notation structure.

### 3.3 The First Ten Minutes: Turning Clicks into Automation

The first 10 minutes decide retention; the goal is completing the "clicking → automatic → parallel" transition with zero text teaching: no tutorial popups — prices, animation and sound teach everything. Reference pacing:

| Time | Player state | Design action | Reference values |
| --- | --- | --- | --- |
| 0–30 seconds | Clicking manually, watching the number climb | Immediate feedback on every click | 1 click = 1 resource |
| 30 seconds–2 minutes | Buying the first automatic unit | The moment "your finger is freed" | First purchase at 10–15 clicks; output 0.1–0.2/second |
| 2–5 minutes | Comparing the second tier's value | Show locked tiers (greyed out) | Second tier about 10× the price, 5–8× the output |
| 5–10 minutes | Buying automation with automated output | The first "snowball" | 3 cumulative "faster" milestones |
| 10–15 minutes | Meeting the first non-money system | Achievements, a chest, an offline teaser | Unlock the first achievement group |

Key principles: price the first purchase at 10–15 clicks — if nothing is buyable before 30+ clicks, you lose players in the first three minutes; the first automatic unit pays for itself in 1–3 minutes (15 buys 0.1/second, paid back in 150 seconds); make clicking an active accelerator (temporary buffs, crits), not unlimited linear income, or an autoclicker script becomes the optimal strategy; show locked content ahead of time (locked tabs, the next tier greyed out, question marks) — "visible but unaffordable" is one of the strongest drives in an idle game.

The zero-operation acceptance test: take the click button away, and the game still plays for 5 minutes with production uninterrupted — the transition holds. Give the first hour a goal chain (3–5 visible goals): buy the 10th tier-one unit, unlock tier two, total output past a thousand, the first achievement group, a prestige teaser — presented in the achievement or quest panel, never as forced popups.

### 3.4 Prestige Resets: Designing the Reset as a Reward

Prestige means voluntarily abandoning current progress in exchange for permanent bonuses, then running back faster and surpassing it. It is the mid-game engine of an idle game and the turning point from "one curve" to "multiple rounds". Example formula:

`prestige points = floor(√(this run's total output / threshold))`, with the threshold set to the output of roughly the first 10 minutes.

An output 16× the threshold earns 4 points; output must quadruple for the points to double. The meaning of the square-root curve: the later you reset, the lower the marginal return — players should reset when growth slows. Supporting mechanics:

- Each prestige point grants a permanent bonus (say +10% global output), active immediately after the reset.
- A reset preview is mandatory: "reset now for X points, or wait 1 hour for Y more". Without a preview, players do not dare reset and the mid-game stalls dead.
- Put the first prestige unlock at minute 30–60 (it must be experienced once on day one); gate it on a number (total output crossing the threshold), not on a popup at a set time.

Four psychological payoffs: a confirmation show before the reset ("the next run returns to this point in about 20 minutes" — swapping the sense of loss for a sense of plan); a grand gift at the moment of reset (keep some upgrades, unlock a new screen, a full-screen effect); a clearly faster second run (bulk buying, speed multipliers, skipping the early game); and making "saving operations" the most expensive goods (auto-buy per tier, automatic offline settlement, one-click max purchase all unlocked with prestige points — what idle players most want to buy is always "not having to click").

Layer design: one more layer can be stacked on top of prestige, but each layer must change the rules (a new resource, a new screen, a new dimension), not merely multiply coefficients — purely additive layers bore players by the third round. Common failures: reset gains that cannot be predicted (so nobody dares press the button), a first 30 minutes after the reset that is too painful, and prestige unlocking too late (not seen in the first week, while the bad reviews arrive first).

### 3.5 Progress Visualization: Making the Wait Visible

The essential experience of an idle game is waiting, and waiting must be visualized — otherwise players feel only time passing, not progress being made.

| Element | Target | Role |
| --- | --- | --- |
| Progress bar | The next upgrade, the next unlock | Turns "40% to go" into a wait you can predict |
| Rolling numbers | Output per second | The core of instant feedback; satisfying even muted |
| Milestone grid | 10/25/50/100 count thresholds | Mid-term goals; the discrete pleasure of "lighting up" |
| Achievement system | Covering every behavior | Surprise, humor, hidden tutorials |
| Compendium / stats | Every unit and form | Collection-driven; the long tail of satisfaction |

Keep achievement density at no less than one per 10–20 minutes, with humorous names (achievement copy is the cheapest content this genre has); turn some achievements into hidden tutorials ("click 1,000 times in a row" tells players that clicking matters); keep 1–2 epic achievements as long-term goals. The compendium pairs unit cards with event cards and a stats page (total output, total clicks, playtime); show the collection rate as a percentage, with a small reward for completing it.

The satisfaction trio: getting bigger (numbers), filling up (collections and grids), being seen (achievement shows, leaderboards, sharing). Self-check: turn off animation and sound — how much fun is left? If almost none, visualization is propping up too much of the experience, and the pacing of the numbers themselves (§3.1–§3.4) needs rework.

## 4. Technical Essentials

Settlement model: the whole game has exactly one settlement function, shared by online and offline:

`resources += production rate × (now - lastUpdate)`, then `lastUpdate = now`

Settle by timestamp difference, not by "ticking once per second". This solves three things at once: offline catch-up, background tabs being throttled (browser background timers get slowed to minute granularity or frozen outright), and identical results across devices with different frame rates.

Big numbers and precision: double-precision floats (double / JS Number) stop representing integers exactly past 2^53 (about 9.0×10^15), so players hit "bought it and the number did not change"; at about 1.8×10^308 it overflows straight to Infinity. The fix: past 10^15 switch to a "mantissa plus exponent" structure (for example `(1.23, 15)` for 1.23×10^15), or bring in an existing big-number library; rounding away low, aligned digits in addition is acceptable, but comparisons and multiplication/division must be exact. Never let the interface show Infinity.

Saves: store a version number and write migration functions — every data-structure change must still read old saves; throttle autosave to once per 30–60 seconds, with immediate saves at reset, large purchases, exit and similar moments; use a checksum plus light obfuscation against direct save editing, and offer export/import (especially needed on Web, where clearing the cache loses saves); handle time tampering as "now earlier than lastSave means a rollback, zero earnings", and let the offline cap keep time-cheating gains limited. Offline-game protection to this level is enough; leaderboards and in-app purchases are what need server authority.

Platform differences (the same numbers, three carriers):

| Platform | Player scenario | Technical key | Monetization | Main pitfalls |
| --- | --- | --- | --- | --- |
| Web | Idling on a second monitor; instant-open links | Background throttling demands timestamp-difference settlement; saves must be exportable | Ads, sponsorships, premium | Clearing the cache loses saves; background-tab output stalls |
| Mobile | Fragmented time plus push-notification returns | Push "offline earnings are full"; background processes get reclaimed by the system | Ads plus IAP | Forced ads interrupt idling; battery drain and data usage |
| Steam | Second-monitor / idle games; long-running processes | Cloud-save conflict strategy; stability across a full day of idling | Premium plus supporter packs/DLC | Insufficient content volume — "nothing to do while idling" earns instant bad reviews |

Notes: on mobile, push notifications are the number one lever on return rate — no more than 1–2 per day, only "earnings are full" and "new event"; on Steam, players idle for long stretches, so the process stays resident and both saving and rendering must be optimized for "running all day"; interface text refreshing once per second is enough, cache formatted big-number strings, and watch memory during long idle sessions as well as battery on mobile.

## 5. Content Volume and Workload Reference

| Version | Systems | Upgrade entries | Other content | Solo estimate |
| --- | --- | --- | --- | --- |
| Minimal prototype | 1 resource plus 3 upgrade tiers | 10–20 | None | 1–3 days |
| Publishable small Web title | 3–4 systems plus offline plus 1 prestige layer | 60–150 | 40–80 achievements, 1 compendium set | 3–8 weeks |
| Commercial mobile release | Characters/cards plus events plus a long-term cadence | 300+ | 150+ achievements, several event sets | 6–18 months (2–4 people) |

Content volume anchors: 2–4 hours of meaningful experience on day one (the first prestige loop completed); in the first week, about 30 minutes per day of "a reason worth logging in for"; in the first month, 1–2 system-level expansions (new tiers, new resources) rather than number inflation; a content pack every 2–4 weeks — stop updating for three months and the core base scatters.

Workload structure: balance tuning takes about 30–50% of work hours, higher than in most genres. The bulk of the content is number tables (CSV-driven; several hundred rows is common) and copy (achievements, compendium, jokes). Art can be minimal, but number presentation must be polished: number animation, sound effects, tier-jump effects. Cost cutters: randomized upgrade pools (redrawn on each reset) and event templates (multiplier events, timed goals).

## 6. How to Start the First Prototype

An hour-by-hour starter checklist:

1. Pick one verb and one resource (click once, dough +1).
2. Write two formulas: price `base × 1.15^(n-1)`; output `count × per-unit output`.
3. Build three upgrade tiers: click bonus, automatic unit, global multiplier.
4. Share one piece of code between offline and online settlement; write it on day one.
5. Display layer: K/M/B formatting plus one progress bar.
6. Calibrate the first 10 minutes: first purchase at 10–15 clicks; by minute 5, automatic output exceeds manual.
7. Plant the first prestige (available at 30–60 minutes) and 20 achievements (half visible on day one).

V1 test checklist:

- 10-minute self-test: count the "clearly faster" moments; fewer than 3 means adjust r and the tier jumps.
- Offline test: advance the system time by 8 hours; the settlement error must be zero and the cap must take effect.
- Autoclicker test: write a 20-line script to click for 1 minute — its gains must not break away from normal play.
- Return test: come back after 24 hours; a clear new goal must appear within 5 minutes.
- Remove-the-button test: with clicking disabled, the game still advances — proof that the zero-operation transition holds.

Tooling: any Web stack or engine can handle this genre — rendering demands are minimal; spend the time on data tables and the settlement function. For choosing a stack, see the Programming Handbook.

## 7. Common Pitfalls

1. Offline earnings credited automatically, in full, with no cap: players log in only once a day, and you have designed your own online time away. Use a cap plus an efficiency factor, and keep the online rate slightly above the offline one.
2. First purchase too far off: the first upgrade only after 30+ clicks, and most players churn in the first 3 minutes.
3. No new decisions in the mid-to-late game, only "waiting for the next tier": a new goal or a new choice must be inserted every 1–2 hours.
4. Floating-point precision incidents: past 10^16 a purchased upgrade does not move the number, or big numbers overflow into Infinity.
5. Prestige too late or its gains invisible: players do not dare reset. A preview and a day-one experience point are mandatory.
6. Clicking and automation out of balance: clicking is always optimal (forcing human autoclicking) or entirely useless (killing engagement).
7. Counting on timers: background browser tabs get throttled and idle output drops to zero. Timestamp-difference settlement solves it.
8. Push and ad abuse (mobile): one come-back ping per hour and the uninstall rate spikes; bind ad slots to actions the player was going to take anyway (watch an ad to double the offline earnings you are claiming), and never interrupt idling.
9. Numbers without mechanics: a new version that is only "a new tier with ×10 output" and veteran players churn within three days.
10. Saves with no version and no migration: add a field and old players' saves fail to load — see you in the review section.
11. Leaderboards with no server validation: time manipulation farms scores and community trust collapses.
12. Ignoring the muted context: idle players spend much of their time muted or on a second monitor; key feedback needs a visual channel.

## Further Reading

- Numbers must-read: the GDC talk series "The Math of Idle Games" (Anthony Pecorella) — a first-hand breakdown of idle-game formulas and pacing; entry points in the GDC list in Resources.
- Academic origin: Ian Bogost's Cow Clicker (2010) — a satirical experiment on clickers that accidentally became the genre's defining case.
- Community and feedback: the r/incremental_games forum and the incremental tag on itch.io are the main sources of playtest feedback during prototyping; when posting a prototype, include the question "at what minute did you lose your goal?" — that is more useful than a survey.
- Within this repository: the Game Design Handbook's growth curves and economy sources and sinks; the Programming Handbook's saving and performance chapters; the Production Handbook's milestones and scope control; Indie Survival's business models and the solo path.
- Exercise: day one, reproduce the minimal "click to automatic" loop; day two, add prestige and offline; day three, run a simulation of the first 3 hours (data tables as the input, a script as the player). Once the curve runs, the prototype stands.
