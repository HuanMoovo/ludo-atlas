# Ludo Atlas · Genre Handbooks · Farming Sim

> **Genre Handbooks · Volume 1**. Positioning: the genre that turns "farming, raising animals and getting along with the neighbors" into a long-term loop. The smallest unit is a day's schedule budget, with seasons and years wrapping around progress; there is no fail state, and checklists, collecting and relationships are what keep players around.
> Companions: Game Design Handbook (core loops and economy) · Production Handbook (content-volume estimation and scope control) · Case Studies (the Stardew Valley chapter) · Pitfalls & Anti-patterns (the content and balance chapters).
> This page carries no external links; benchmarks are widely known works only — if you haven't played one, play it first: two hours of firsthand experience beats two hours of reading breakdowns.

---

## 1. Positioning and Core Loop

At its core, the farming sim (also often called a life sim — Stardew Valley, Story of Seasons and Animal Crossing are the standard-bearers) is about managing "a day with a deadline": each day's time and stamina are fixed budgets, there is always more to do than can be done, and so trade-offs are forced; trade-offs accumulate into seasons and years, and the farm gets a little better.

How it differs from adjacent genres:

- Versus management sims (the Two Point Hospital kind): those manage abstract organizations and budgets; the farming sim manages one character and one plot of land, down to a single day and a single tile.
- Versus survival crafting (the Minecraft and Don't Starve kind): those manufacture pressure with danger and death; the farming sim's pressure comes from the calendar and stamina — the player almost never loses.
- Versus life simulation (like The Sims): that kind is choreographing a play; the farming sim's backbone is production and accumulation, with socializing both a side dish and a staple.

The core loop, written as a verb chain:

`wake up → check the weather → tend crops and animals → forage/fish/run errands → talk and give gifts → sell goods and buy supplies → work until stamina bottoms out → sleep and settle the day → the next day`

Every nesting layer of the loop needs its own hook:

| Layer | Duration (real time) | What the player is doing | Payoff point |
| --- | --- | --- | --- |
| Minute | Once every 10–20 seconds | One watering, one conversation | Immediate feedback |
| Day | 10–20 minutes | Laying out a whole day's schedule | Sleeping |
| Season | 2–4 hours | Planting plans, festivals, exploration | Season change (crops wither) |
| Year | 20–40 hours | Buildings, relationships, collections, evaluation | Year-end settlement |

Nail down three numbers before production starts; every other system revolves around them:

1. How long a day is (the conversion rate between real time and game time).
2. How many days a season has.
3. What gets settled when the player sleeps (stamina recovery, crop growth, the ledger).

## 2. Player Experience Goals and Benchmark Titles

Players come to this genre for four things, in priority order:

| Experience goal | What players say | Design focus |
| --- | --- | --- |
| A sense of control | "My farm is getting better" | Visible growth: levels, buildings, crop quality |
| A sense of rhythm | "I'll finish watering this plot and go to bed" | The schedule budget and the stamina bar |
| A sense of belonging | "Everyone in town knows me" | NPC affinity and community events |
| The collecting itch | "Three fish to go" | Compendiums, checklists, achievements |

Benchmark titles and the one move each one teaches:

| Title | Core orientation | The one move to learn |
| --- | --- | --- |
| Stardew Valley | Farming, mining, fishing, socializing and collecting — all of it | Intensity control: every system is only a skeleton, and thickness comes from the combination |
| Story of Seasons (the Mineral Town entries) | The series prototype: schedules, stamina, affinity, festivals | Small-map density: cross the whole town in five minutes and pass everyone daily |
| Animal Crossing | Real-time clock, zero failure, decoration and socializing | How to write soft goals: nothing is mandatory; players hand themselves their own tasks |
| Rune Factory | Farm plus combat plus romance | Cross-system feeding: combat materials feed back into the farm; farm produce supports combat |
| My Time at Portia | A 3D workshop plus a quest-chain-driven town | Quest chains as the pacing skeleton, filling the dead air of "waiting for crops to grow" |

One reminder: every title above is the scope of years of iteration. Match their "content density", not their "first version".

## 3. Design Essentials

### 3.1 The Schedule: A Day's Time Budget and "What Time to Sleep"

A day is a fixed resource-allocation problem, with two resource pools: time and stamina. Time constrains "sunset, shops closing, NPCs going home"; stamina constrains "how much work can still get done today". Only when both pools run short do trade-offs hold.

"What time to sleep" is the core decision, because it is the one choice each day where the player actively gives up the rest of today in exchange for tomorrow's state. Design conditions:

- Staying up late costs something: tomorrow's stamina cap is lower, or the player passes out in the small hours and drops a few items.
- Sleeping early tempts: full stamina tomorrow, plus morning-exclusive events (the mailbox, visitors, weather).
- Between the two lies a continuous range: sleeping at 22:00 is safe, at 24:00 you get two more hours of work, at 2:00 it is a gamble. Intermediate values are what keep the decision from being binary.

Measure a day's time budget like this:

| Action | In-game time | Stamina cost | Notes |
| --- | --- | --- | --- |
| Water one tile | ~5 seconds | Low | The main repetitive labor of day one |
| Hoeing, chopping trees | ~10 seconds | Medium | Falls after tool upgrades |
| Walking to town | 1+ hour combined | None | Time is the entry fee for socializing |
| One fishing trip | 30 minutes | Low | A money tree that is also a time sink |
| Descending one mine floor | 1–2 hours | High | A high-risk, high-reward stretch |

The acceptance test for the budget is "how many things fit in one day": an ideal day finishes 60–70% of the to-do list, leaving the rest for tomorrow. Finishing 100% means there was no design; finishing only 30% means the balance was botched.

Size the stamina bar with "1.5 times a day's core labor" as the reference; food restores stamina, which turns cooking from decoration into a resource. Write the details of time flow (pause in menus, whether indoors pauses, whether festivals skip time) into the design document — don't leave the programmer to guess.

### 3.2 Crops and Livestock: The Crop Matrix and Balance

The crop matrix has three dimensions: growth time (including multi-harvest patterns), sale price, and labor (waterings and pickings per crop cycle). Every crop must occupy its own spot in that space, or there is no choice to make.

Profit is not about sale price — it is "profit per tile per day":

(total sale price - seed cost) ÷ days of land use

Multi-harvest crops fold in their every-4-days regrowth. This table is the main battlefield of economic balance. Example structure (the numbers illustrate structure only; don't copy any title's figures):

| Crop | Growth time (days) | Sale price | Labor | Harvest pattern | Profit per tile per day | Role |
| --- | --- | --- | --- | --- | --- | --- |
| Fast-growing greens | 4 | Low | Low (1 watering) | Single | 1.0 (baseline) | Tutorials and early cash flow |
| Root vegetables | 6 | Medium | Medium | Single, chance of extra yield | ~1.2 | A stable alternative |
| Strawberry type | 8 | Medium | Medium | Regrowth (every 4 days) | ~1.4 | Mid-to-late spring mainstay |
| High-value fruit | 13 | High | High | Regrowth (every 4 days) | ~1.6 | Summer and fall mainstay |
| Giant crops | 13 | Very high | Very high (3 waterings) | Single | ~2.0 | The late-fall showpiece, filling whole plots |

Four balance rules:

- Rank by "profit per tile per day" with 20–40% gaps between adjacent tiers; never let a 3× cliff appear (end-of-season clearance crops excepted).
- Labor correlates with profit: time-saving crops have a high floor; labor-heavy crops have a high ceiling.
- Convert non-farming income (fishing, foraging, mining) into "earnings per hour" and put it in the same table, or players will compute a single optimal solution.
- Add new seeds and machines each season, but keep the total restrained: 30–60 crops is already enough for commercial scope (see §5); 8–15 are realistically choosable per season, and the ones players actually use stay under 5.

The processing chain is the mid-game engine: set the revenue of selling produce raw at 1, and pull processing (jam, wine, cheese) up to 1.5–3×, at the cost of machine time and build cost. Livestock follows a "fixed investment" route: a large upfront outlay with fixed daily output, tying the player's route to the barn area (feeding, petting) and taking 10–20% of each day; cash flow runs slightly below crops of the same period, but it supplies stability and emotional value (naming, interaction).

### 3.3 Socializing: NPC Schedules, Affinity and Event Triggers

The social system is a set of three: the schedule table, affinity, and event triggers.

**Schedules**: every NPC gets a "time → place → behavior" roster, with holiday variants. Schedules make the world feel alive, and they also create the friction of finding people. The principle is that people must actually be findable: when the player wants to give a gift, they should either find the person within a reasonable time or know exactly where to meet them tomorrow — otherwise socializing turns from gameplay into punishment.

Complexity comes in two tiers — don't write everyone a full version: core NPCs get 10–30 entries plus festival variants; background NPCs get 3–5 entries plus a fixed post.

**Affinity**: heart levels (0–10 hearts) hang off gifting, conversation and quests. Gifts are capped at one per day to prevent farming, and birthdays run a high multiplier (×8, for example). Affinity pays out four kinds of returns: recipes, story events, discounts and helpers, romance and marriage. The substance behind the affinity numbers is writing: every heart-level tier needs new lines, or the heart bar is just a progress bar spinning in place.

**Event triggers**: one event equals a combination of conditions plus a scene. Write the conditions as readable rules before they go into code:

| Event | Conditions (all must hold) | Format | Output |
| --- | --- | --- | --- |
| Harvest festival invitation | Any candidate at ≥4 hearts, spring, clear weather | Two-person dialogue at the village entrance | Relationship progress |
| Grandfather's letter | Auto-triggers on day 3 | A monologue on the farm | A long-term goal (the yearly evaluation) |
| Mine rescue | Affinity ≥6 hearts, after the player has reached mine floor 40 | A mine scene, 3 people | Unlocks a new area |
| Rainy-night visitor | Affinity ≥8 hearts, raining, after 20:00, player on the farm | Two-person dialogue at the door | Romance line progress |

The principle for triggers: players should be able to sense that "the relationship is there, so it will come", but the moment it fires should still surprise. The heaviest events hang on a double condition of affinity plus a prerequisite event. Fewer, better people: 8–12 NPCs with real stories beat 30 broken records; the cost of each social NPC is in §5.

### 3.4 Soft Goals: Retaining Players Without a Fail State

With no fail state, all motivation comes from the itch of an unfinished checklist. The checklists come in four kinds:

- Collection: the fish compendium, artifacts, recipes, fossils, lost items. A progress bar saying "3 to go" is the best reason to come back.
- Construction: house upgrades, the greenhouse, bridges, restoring the community center or museum. Turns big spending into visible engineering.
- Relationships: town-wide affinity, marriage, family. Relationships are the slowest and steadiest progress bar.
- Self: decoration, rare crops, achievements, titles. Give players a plot of their own and let them assign themselves their own work.

How to arrange them: keep goals at three scales running at once (finish watering today; build the bridge this week; complete the community center this year), so the player always has a next action. Every checklist needs visible progress (slots, hearts, percentages); a collection you cannot see does not exist.

The difference from a traditional quest list: soft goals can be set aside at any time, with no countdown pushing. Season exclusives provide a soft deadline: miss it and wait for next year — and the game says plainly that "it comes back next year". The anti-pattern is locking content behind a mandatory quest chain; this genre's core players like to choose their own order, so the main line can only be one or two optional skeletons.

### 3.5 Seasons and Years: A Sense of Progress and "One More Year"

The season is the biggest progress tick: when the season turns, the previous season's crops wither, forcing a clear-out and replant; each season swaps in a new set of crops, fish and forageables, and the schedule is forced to change. That is a free "chapter system" — no story needs to be written for it.

Parameter suggestions: 28 days per season (a magnitude reference; 4 weeks is easy to remember and easy to build); 1–2 festivals per season as highlights; a full four-season year runs 20+ hours of real time, depending on the length of a day.

Years provide the steps: year 1 is learning the basics and accumulating, year 2 is expanding production and processing, year 3 is completing the large goals (the community center, marriage, village revival). The content design must guarantee that year 1 cannot finish everything however it is played — only then do the year hooks hold.

The "one more year" hook checklist — at year's end the player should be holding 3–5 of them:

- Unfinished collections and construction.
- Newly unlocked areas, seeds and machines that aren't second nature yet.
- The new year's festivals and limited events.
- The yearly evaluation display (family history, total compendium count, grandfather's letter).

The acceptance method: ask players "what do you plan to do next year"; if they can't answer, there are not enough hooks.

## 4. Technical Essentials

- Global clock and schedules: one clock service (minute ticks) plus a time-multiplier table (separate pause rules for outdoors, indoors, festivals and menus); everything about "what happens at what time" goes into data tables (shop hours, NPC rosters, lighting, music).
- Crop state machine: tile data (species ID, planting day, watered flag, growth stage, regrowth status) lives in tables — never one script per plant; growth is driven by "daily settlement plus watering events", not by iterating over a thousand tiles every frame.
- Event and dialogue systems: data-driven (dialogue trees plus conditions plus actions); a trigger engine handles the combination checks of "affinity × time × place × weather × prerequisites". Keep a separate event roster as a self-check on content coverage.
- Saves: crops, affinity, event flags, world objects and the random seed all serialized in full, with a version number and migration functions. Corrupted saves after an update are a disaster zone for negative reviews (see Pitfalls & Anti-patterns).
- Time cheating and cloud saves: multi-device sync and players changing the local clock (Animal Crossing's old "time travel" problem) — settle the policy before writing code. Lenient offline, strict online is a common compromise.
- Performance: large farms run to hundreds or thousands of tiles — manage rendering and logic with area activation and diff-based updates; harvest effects and particles go through object pools; on mobile, watch memory and battery, because players of this genre often stay in-game for long stretches.
- Input: the minimal loop of one tile, one action (select tool, highlight target, execute), tested separately for mouse-and-keyboard and gamepad; for repetitive labor (watering), reserve a place at the systems layer for automation upgrades.
- Data tables: crops, items, NPCs, schedules, events, dialogue and shops all externalized as CSV or JSON, with code only reading the tables. In a content-heavy genre, this is the only engineering discipline that keeps you alive.

## 5. Content Volume and Workload Reference

Estimate by "unit content cost". Below are common magnitudes for solo developers and small teams — not a commitment:

| Content unit | Unit cost (magnitude) | Minimum viable | Commercial scope | Notes |
| --- | --- | --- | --- | --- |
| Social NPCs (dialogue and events included) | 30–80 hours | 5–8 | 20–40 | The single largest cost item in the whole project |
| One piece of dialogue (trigger conditions included) | 5–15 minutes | 200–400 | 2,000–5,000 | Written, proofed, integrated and tested — one pass each |
| One story event (2–6 screens) | Half a day to 2 days | 10–20 | 150–400 | Portraits, expressions and staging counted separately |
| One crop | 1–2 days | 8–12 | 30–60 | 4–6 pieces of growth-stage art |
| One animal | 3–7 days | 2–3 | 6–10 | Animations and buildings included |
| One festival | 1–3 weeks | 2–3 | 8–12 | Venue, mini-games, dialogue, rewards |
| One scene | 1–3 weeks | 3–5 | 10–20 | Density before area |

A few magnitude conclusions:

- NPC dialogue and events are this genre's number-one cost, often exceeding programming and art combined. Before you start writing, freeze the "dialogue budget per NPC": 100–300 lines per NPC is 30–80 hours of a writer's time.
- Stardew Valley's magnitude is 30+ social NPCs, dozens of crops, hundreds of events plus years of free updates, and its author alone worked on it for more than four years (see Case Studies). Any plan to "make a Stardew Valley in three months" should be cut in half, then cut in half again.
- Cutting priority, first to last: merge NPCs and events (one character carrying several lines) > text instead of voice acting > fewer festivals > a smaller map (dense first, expand later) > touching seasonal content.
- The symptoms of mis-sized content all erupt in year 1's winter: the player has nothing to do. Winter must have indoor content ready (mining, ice fishing, cooking, festivals).

## 6. How to Start the First Prototype

Build in order; every step ends playable:

1. A one-screen town plus one room plus one plot. Within 30×30 tiles; density first, area later.
2. Clock and sleep: 6:00 to 2:00 the next day in game time, 10–15 minutes of real time; press the sleep key, settle, and it is 6:00 the next day. Do only this, and test whether "a day" is fun first.
3. Three crop states: 3 crops (fast, standard, multi-harvest) with planting, watering, maturing and harvesting — and draft the §3.2 table while you're at it.
4. Economic loop: one shop (buy seeds, sell goods), one currency. Play 3 days in a row and look for positive feedback.
5. Stamina and food: a stamina bar plus one stamina-restoring food, making "stay up or not" a real choice for the first time.
6. One NPC: a greeting, one gift, one heart. Get the minimal "affinity plus event trigger" pipeline running.
7. One season change: force the season change on day 28, clear the crops, and feel the season tick once.
8. Saves: save-anytime plus save-on-sleep, with a version number present from day one.

Prototype acceptance: play 7 in-game days in a row and be able to say "what I want to do tomorrow" at the end of each day. If you can't, go back to step 2 and retune the schedule.

Anti-patterns: building a big map first, building the romance line first, buying art assets first. This genre's foundation is "a day", not "a map".

## 7. Common Pitfalls

| Pitfall | Symptom | How to avoid |
| --- | --- | --- |
| Underestimating content volume | Thinking "dialogue is easy to write", then discovering halfway through that it is a multi-year project | Run the §5 table first; cut to what you can deliver before starting |
| Unbalanced schedule | A day only fits 30% of the to-do list (anxiety), or everything gets done (boredom) | Hold the 60–70% completion rate; tune time costs from playtest measurements |
| Stamina penalties too harsh | Passing out drops items and halves the next day, and players abandon the save | Penalties need gradient and warning; give a dignified way to end the day |
| No failure means no pressure | By day 5 the goal is gone and play turns into idling | Soft deadlines (seasons) plus three-scale checklists plus festival highlights |
| Socializing turns into hide-and-seek | NPC schedules are too complex, and the person cannot be found day after day | Write core NPCs finely and simplify background ones; provide tools for finding people |
| Broken economy | Mid-game money has nowhere to go, or the early game is too poor to get moving | Stock enough money sinks (buildings, upgrades, cosmetics); check the curve every ten hours |
| Copying balance tables | You copied someone's table but not their pacing | A table is structure; pacing must be measured yourself (the 60–70% principle) |
| Save corruption | Corrupted saves, time travel, cloud-sync conflicts | Ship version numbers and migrations from day one; put the time policy in the design document |
| Automation too late | Watering gets old by the second hour | Put the automation upgrade right at the point boredom starts (around the end of season 1) |
| Farming only | No fishing, mining, festivals or socializing; nothing left by hour three | At least two side lines, and they must cross-feed with the main planting loop |

## Further Reading

- Reread two sections of the Game Design Handbook: core loops and nesting, and the sources and sinks of the economy — then draw a money-flow diagram over the crop table.
- The estimation chapter of the Production Handbook: time "one NPC, one event, one festival" first, then multiply by content volume.
- The Stardew Valley chapter of Case Studies: note the time structure of "learning by doing" and the timing factor of a demand vacuum.
- The Eric Barone feature in Indie Developer Profiles: a complete sample of one person covering programming, art, music and scriptwriting.
- Play, don't read: play Stardew Valley, Story of Seasons and Animal Crossing to year 2 each, then come back and find the gaps.
- Hands-on exercise: build a paper-spreadsheet economy model of 28 days × 5 crops (no code yet), work out how much the player earns per hour in year 1 and where it gets spent, and only then decide whether to greenlight the project.
