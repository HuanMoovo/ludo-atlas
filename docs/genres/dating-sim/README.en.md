# Ludo Atlas · Genre Handbooks · Dating Sim

> **Genre Handbooks · Volume 4**. Positioning: the genre that makes "managing a relationship" the main loop through numbers and a schedule. Players spend a limited amount of time laying out actions, building affinity and waiting for events, turning heart-flutter into a ledger that can be planned, won and lost; this page covers four structural blocks — affinity and event triggering, time management, route structure, and staging and localization.
> Companions: Game Design Handbook (core loops and numbers) · Art & Audio Handbook (sprite and voice specs) · Case Studies (subject-matter cases and retrospectives) · Indie Survival (scope control and content accounting).
> This page links nothing externally; benchmarks are well-known works only. The numbers here are common orders of magnitude — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

The one-line positioning: a dating sim is **the genre where "managing a relationship" is the first-class content**. Text supplies the heart-flutter; the schedule and the numbers make it plannable, winnable and losable; romance is not a reward after clearing the game — romance is the main line itself.

The core loop, written as a verb cycle: `check the calendar and status → plan today's actions → trigger dialogue and events → resolve affinity and stats → resolve the week and season → unlock new events → plan again`. It is measured in days or time slots and runs on three layers: the slot level (seconds to minutes, holding attention through immediate feedback), the week level (scheduling and resolution, pacing the game with fixed events), and the playthrough level (replaying on another route, carried by multiple endings and collection).

Drawing boundaries with adjacent genres:

| Adjacent genre | Boundary |
| --- | --- |
| Visual novel | A VN's engine is reading and branching, with numbers at most a side dish for unlocks; the dating sim is driven by affinity and schedule, and the text exists to cash out the numbers. |
| Raising sim | A raising sim's subject is the character the player develops, with romance just one route among many; the dating sim's endpoint is the love interest, and every system converges on "the relationship". |
| Farming sim | Romance is one system among many in a farming sim; in a dating sim it is the only main line. |
| Otome and male-oriented | A theme and audience dimension, not a systems difference; both sides must solve the same problem — making the player feel "responded to". |

A self-check question: delete the affinity and schedule systems entirely — can the story still be read? If the answer is "yes", what you are making is closer to a visual novel; only if it is "no" does this genre hold.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (ordered by priority):

1. **Being responded to**: everything you do, the characters remember and react to. This is the genre's most fundamental pleasure, more important than any single scene.
2. **A sense of progress**: every step of the relationship has a rung (forms of address, distance, exclusive events and places), and the player always knows where they stand.
3. **The pleasure of planning**: there is never enough time, every schedule is a trade-off, and there is no single optimal solution to look up.
4. **Moments of heart-flutter**: spend generously on staging the key scenes — the goal is for players to screenshot them, rewatch them, recommend them.
5. **Collection and replays**: multiple characters, multiple endings, the checklist feel of CGs and events — what pulls players into another route and another playthrough.

Benchmark works (a well-known list; play them by hand before breaking them down — watching videos cannot teach the hesitation of a choice):

| Work | What to learn |
| --- | --- |
| Tokimeki Memorial | The founding anchor of numbers-driven narrative: schedule management, stat thresholds, negative friction (rumors and bombs), the target structure of a graduation confession |
| LovePlus | Relationship upkeep that only begins after you start dating: real-time daily rhythms, daily dialogue reused by time slot |
| Sakura Wars | A genre-stitching sample mixing affinity values (trust), timed choices and combat sections |
| Persona 5 | The modern reference for calendars and action slots: free daytime and night actions, confidant rewards and pacing |
| Mr. Love: Queen's Choice | A mobile otome sample: card raising bound to a story romance, voice acting and a long-term update structure |

One reminder: these benchmarks' scope comes from years of iteration and industrial pipelines — match their emotional payoff, not their content volume.

## 3. Design Essentials

### 3.1 Affinity and Event Triggering: Numbers-Driven Narrative

Affinity is the main scoreboard, but it cannot be a single number: it splits into three layers — the **affinity value** (a continuous 0–100 per character, used for threshold checks; a daily interaction grants +2 to +6, a satisfying date +5 to +15), the **relationship stage** (4–6 tiers cut by thresholds — stranger, acquaintance, friend, interest, lover — determining the dialogue pool and the set of triggerable events), and **memory flags** (a boolean set letting later dialogue reference past choices and experiences). Event triggering, in turn, is a five-part combination: `affinity band × time slot or date × location × prerequisite event × player stats`, all registered in the event table so conditions are consultable, testable and editable:

| Column | Content | Example |
| --- | --- | --- |
| Trigger condition | The five-part combination written out in full | affinity 20–39 and Wednesday after school and library and event 01-02 not yet triggered |
| Priority | The competition order when several events qualify in the same slot | key story > anniversary > character event > daily |
| Variants | Lines and expressions swapped by stage or flag | three tiers of tone variants |
| Assets | The sprites, expressions, CG, BGM required | school-uniform sprite + surprised + bgm_daily_01 |

Scheduling discipline:

- When several events qualify in the same slot, queue them by priority; key events must never be bumped by random ones, and anything bumped needs a perceptible reschedule or compensation. Keep conditions generous, not strict — don't let a player reach a fourth playthrough without ever seeing an event.
- Attach one "confirmation event" to every stage: it fires once on reaching the stage and tells the player clearly that the relationship has changed, solving problem number one — "the number moved but the player doesn't know". Missed key events are reissued or downgraded rather than creating permanent regret (unless that is a deliberate failure route).

Visibility and negative feedback:

- Visibility runs on three proxies: expression and body language, tone and forms of address, and event permissions (where you can invite someone, which places you can enter). Don't show a bare stat panel, but the player must be able to answer "why is she angry".
- Negative feedback (being ignored, jealousy, rumors) must satisfy three things: preventable (there are omens), recoverable (there is a clear remedy), signposted (the player knows what happened). Tokimeki Memorial's "bombs" are the classic reference — and the classic lesson that overdoing it becomes annoying.

### 3.2 Time Management and Schedule Design: Action Points, Weekdays and Seasons

Time granularity decides the feel of the whole game; choose the macro frame first:

| Granularity | Form | Suited to |
| --- | --- | --- |
| Action points | N points per day, actions priced in points | Short sessions, mobile, lightweight works |
| Time slots | 3–4 slots per day, one action per slot | The mainstream; the best balance of narrative feel and trade-offs |
| Weeks | Fixed events pinned to weekdays; the player plans a week | Works that favor the pleasure of planning |
| Seasons or terms | The macro frame, dividing chapters and assessment milestones | A long-term progress bar wrapping the earlier granularities |

Budget like this (the numbers only illustrate the structure): a term of 16 weeks, 5 discretionary days per week, 3 slots per day gives roughly 240 total slots; after fixed classes and rest, only about half remain free to allocate. Design the player's desires at 1.5–2× the budget — the surplus of wanting is the trade-off; every action serves exactly one goal (one character, one stat or one rest), and exclusivity is where this genre's tension comes from.

Schedule discipline:

- The calendar must be readable in advance: exams, the school festival, holidays and birthdays are all marked ahead of time; a birthday is each character's natural countdown, turning "gift preparation" into a lead-time decision. Leave a preparation window before big events and a recovery window after — all-tension and all-relaxation are equally boring.
- Stat actions and social actions compete for the same slots, and the pull of "train yourself or go see her" must be constant; use stamina, mood or money as a third resource to prevent mindless action stacking — put the friction in resources, not in randomness.

Checklist: does what the player wants to do substantially exceed the slots (1.5× or more is good)? Does any row of the reward matrix dominate all the others (if so, a unique solution exists and players will copy it)? Do sprint stretches and rest stretches alternate?

### 3.3 Character Route Structure: Common Route and Individual Routes

The trunk structure in one line: `common route (all characters interactable) → split point (route lock) → individual route (three acts: approach, confirmation, test) → individual ending`. Text volume distributes along the trunk like this (common orders of magnitude):

| Segment | Share | Notes |
| --- | --- | --- |
| Common route | 40%–50% | Shared by all characters: first meetings, group interactions and the world |
| Individual routes | 40%–50% combined | Route-specific story after the split; with 4 characters, about 10%–12% each |
| Endings and variants | 10% | Each ending, failure routes, epilogues and common-route variants |

Split rules — choose one of three:

| Rule | Method | Risk and discipline |
| --- | --- | --- |
| Explicit choice | Key nodes list the candidate characters and the player chooses openly | Controllable, and the mainstream approach; choice text must not spoil the consequences |
| Threshold lock | After a fixed date, the route locks automatically to the highest affinity | Players who court both sides feel stabbed in the back by the system; needs explicit advance notice |
| Gate filter | Missing the threshold leads to a solo ending or failure route | Failure is content too — give it a full segment, not one line of subtitles |

Cost discipline: each added romanceable character equals one individual route plus common-route variants, plus a full set of sprites, expressions, CGs and voice — the cost is close to linear; make 2–3 characters deep first, then decide by the §5 ledger whether to add more. Each character is then accepted against a checklist: one three-act individual route, 3–5 emotional peaks (with CGs and staging), 8–15 route-exclusive events, daily lines that differ from the common route, and one exclusive ending plus one missed or failure ending.

### 3.4 Staging and Localization: The Ledger of Sprites, Voice and Text

Asset orders of magnitude (for a mid-length work with 4–6 characters):

| Asset | Spec and magnitude | Notes |
| --- | --- | --- |
| Sprite | 1–3 poses per character, canvas 1200–2000 px tall | Export in layers; expression variants are composited in the engine |
| Expression variants | 8–12 per character | Heads only; surprised, shy, angry and disappointed are the bare necessities |
| Event CG | 5–10 per route, 1920×1080 minimum | Each one anchors an emotional peak — be stingy when choosing subjects |
| BGM and SFX | 15–30 loopable BGM tracks; 30–80 sound effects | Get the high-frequency sounds right first: clicks, transitions, gifts |
| Voice | Varies enormously | Full voice is the biggest cost variable; strategy below |
| UI | One set | The calendar and action menu are UI engineering specific to this genre — do not underestimate them |

Staging discipline, tight and loose: daily segments move fast (few expression changes, no effects, short pauses); heart-flutter segments move slowly (stretched pauses, subtle expression changes, BGM rises and falls); key segments overspend (CG, staging and voice all in). If every line shakes the screen, none of them does.

Voice strategy falls into three tiers by budget: full voice (cost bound linearly to text volume — the highest); voice for key scenes on the main and individual routes with daily life left silent (the common compromise); only signature lines voiced (forms of address, catchphrases, the ending confession). Starting with "key scenes" and filling in after release based on data is a common approach that can be pushed or pulled back. The usual cost ranking: full voice first, sprites/expressions and CGs second, BGM and SFX relatively light; text burns no money — it burns people.

Localization points: the text is the product, so translation volume equals the full script; use the engine's string system and a glossary from day one (forms of address are the disaster zone — names, nicknames and honorifics distort most easily in translation). Confirm font licensing one by one (commercial licensing for CJK fonts); voice is usually kept in the original language with subtitles. After the translated script goes back in, run a staging regression: line breaks, forbidden punctuation rules, and mismatch between voice and text.

### 3.5 Calculate Before Writing: Numbers Validation

Get the economy to add up before you write a line: each character's affinity curve, the time cost of each stage, and the number of slots available per person all go into tables first.

Validate at least three things: every ending is reachable within budget; multiple winning solutions exist (not one unique optimum); a single playthrough covers 40%–60% of the content, leaving room to replay. Simulations and shipping numbers share the same tables, so reruns are just table edits; run 1,000 simulated playthroughs with different play styles and check whether the ending distribution lands in the design band.

## 4. Technical Essentials

The engineering difficulty concentrates in three areas: data and scheduling, the content pipeline, and tooling. This genre has no real-time performance pressure; the hard parts are the number of states and "changing content without changing code".

**Engines and frameworks**

- Ren'Py: the de facto standard for VNs — saves, rollback and multi-language support work out of the box, and the Python layer is enough to write schedule and affinity systems; the first choice for a pure-2D text-staging route — don't build your own. A custom engine is only worth considering when your staging form exceeds every existing tool; don't do that for a first work.
- Unity or Godot: take these two when you need 3D scenes, deep Live2D integration or embedded mini-games; schedule, event and affinity systems must be built in-house or started from plugins.

**Data and scheduling**

- Three external tables (CSV or JSON; code only reads them): the event table stores trigger conditions, priority, variants and assets, with IDs running through the script, asset and voice lists; the character table stores affinity thresholds, stage dialogue pools, likes and turn-offs; the schedule table stores the slot structure, the fixed-event calendar, season milestones and the action reward matrix.
- Write resolution as a pure function: input the date, player state and schedule; output the new state and event queue — no side effects, reproducible; saves, replays and automated tests all lean on it.
- Time drives everything as discrete slots: actions consume slots, events hang on slots, and resolution happens at slot boundaries; each slot the scheduler walks the event table, filters the qualifying set, queues by priority and resolves conflicts, with key events carrying a postponed fallback.
- The save serializes the date, each character's affinity and flags, player stats, the set of triggered events, and the current route and ending state, with a version number and migration function. With many branches and many flags, a corrupted save costs especially much.

**Tools and testing**

- The debug panel is the first tool: jump dates, edit affinity, list currently triggerable events, force-trigger, jump straight to an ending; without it, testing one route means manually repeating dozens of slots. Automated simulation lets scripts play a thousand-plus runs in different play styles and outputs the ending distribution and a list of untriggered events; before release, run full event-reachability and all-endings traversal regressions, and after the translated script goes back in, run the staging check again.

## 5. Content Volume and Workload Reference

The following are common orders of magnitude for comparable projects, for estimation and scope decisions — not a commitment.

| Form | Romanceable characters | Text volume | Event count | Timeline |
| --- | --- | --- | --- | --- |
| Numbers prototype | 1 | 10k–20k characters | 15–25 | 2–4 weeks |
| Small releasable | 2–3 | 60k–120k characters | 60–150 | 4–8 months |
| Commercial mid-length | 4–6 | 150k–350k characters | 200–400 | 1–2 years |
| Team long-form | 8–12 | 500k+ characters | 500+ | 2–4 years |

Conversion rates:

- Writing speed: a practiced writer drafts 2,000–4,000 characters a day, and revision adds another 0.5–1× (same basis as the visual novel page); event integration averages 0.5–2 days each (conditions, variants, staging, testing).
- Cost per character: individual-route text (15k–30k characters) + 8–15 exclusive events + one set of sprites and expressions + 3–5 CGs + one block of voice + a week or more of integration testing; every added character repeats the whole bill.
- Release form shapes structure: premium titles design content volume and playthroughs around a "complete experience in one purchase"; live-ops titles release characters and events on a version cadence — two different scheduling logics.

Scheduling anchor: a vertical slice of "common route + one complete individual route" usually takes 2–4 months; extrapolate linearly by character count after that, then multiply by a polish factor. Scope-cutting order: character count first, then voice tier and variant depth; the text is the product itself — cutting text is cutting the product.

## 6. How to Start the First Prototype

Goal: within 4 weeks, build the minimum playable version — "one character, one term, can reach an ending" — without a single finished illustration.

1. Week 1: table modeling. Leave the engine alone for now: compress a term into 10–16 decision points, 1 character, 3 locations, about 15 events, 2 endings; work out action rewards, affinity thresholds and event triggering completely, and verify that "an ending can be assembled".
2. Week 2: get the skeleton running. Wire up time progression, the action menu, affinity and flags, and the event scheduler in Ren'Py; use placeholder assets throughout, but use the real pacing and script format from day one.
3. Week 3: content and staging. Write 10–15 events, with 2 built to full emotional-peak spec (pauses, expressions, BGM rises and falls); tune the trigger feel so events land like a chance encounter rather than clocking in.
4. Week 4: closed testing. Have 3–5 people who have not read the design doc play the full flow and watch three things: whether they plan on their own, what they missed, and whether they want to replay; hint nothing, explain nothing, and note where the emotional peaks land.

Acceptance criteria (all observable): at least 3 of 5 testers replay another route on their own; testers can name at least two specific preferences of a character, showing the numbers system was read correctly; all routes and events are reachable with no deadlocks; you can adjust a path to a different ending in 5 minutes by changing tables alone.

## 7. Common Pitfalls

1. **Affinity black box**: the number rises, but expressions, lines and forms of address never change, so the player does not know they are making progress. Avoidance: three layers of proxy feedback, and one confirmation event per stage (§3.1).
2. **Unreachable events**: conditions are obscure or contradictory, and some events never appear even after three full playthroughs. Avoidance: register conditions in the table and run a full event-reachability simulation before release (§4).
3. **A schedule without trade-offs**: there are so many slots that everything gets done, or there is one optimal solution to copy. Avoidance: set the budget before the content; keep adjacent actions' reward differences in the 20%–40% band (§3.2).
4. **Too many characters**: every route is half-written and none goes deep. Avoidance: make 2–3 deep first, and run the §5 ledger before adding more.
5. **Fake variation**: one line changes but the outcome does not, and once players see through it they stop taking choices seriously. Avoidance: a variant must change at least one visible outcome — attitude, reward or follow-up event (§3.3).
6. **Text decoupled from numbers**: the story has reached deep affection while the affinity bar still sits at "friend". Avoidance: attach confirmation events to stage thresholds so the two stay in sync (§3.1).
7. **Negative feedback out of control**: neglect is punished irrecoverably, or there is no friction at all. Avoidance: preventable, signposted, recoverable (§3.1).
8. **Full voice blows the budget**: treating full voice as the default configuration. Avoidance: voice the key scenes first, fill in after release based on data (§3.4).
9. **Localization as an afterthought**: hard-coded text means a full rework when going overseas. Avoidance: use the string system and glossary from day one (§3.4, §4).
10. **Testing only the main route**: unpopular routes and failure lines go unplayed, and the game deadlocks on release. Avoidance: run all-endings traversal and simulation regressions before release (§4).

## Further Reading

- [Game Design Handbook](../../fundamentals/game-design/README.md): core loops, numeric tables and validation methods — the underlying draft for §1 and §3.
- [Art & Audio Handbook](../../fundamentals/art-audio/README.md): delivery specs for sprites, expression variants and voice; pairs with §3.4.
- [Case Studies](../../postmortems/README.md): four-part breakdowns of subject-matter cases — consult before greenlighting.
- [Pitfalls & Anti-patterns](../../pitfalls/README.md): the content production and numbers sections — read against §7 here.
- [Indie Survival](../../../playbooks/indie-survival/README.md): scope control and content accounting, complementing §5.
- [Genre Handbooks · Visual Novel](../visual-novel/README.md) (Volume 1): the sister page; branching governance, text engineering and staging conventions defer to it — this page covers only numbers and the schedule.
- [Genre Handbooks · Raising Sim](../raising-sim/README.md) (Volume 3): time budgets and stat curves; the action-slot design is mutually borrowable.
- Homework: without touching an engine, build a one-term schedule model of 48 slots in a table — 1 character, 6 actions, 2 endings; hand-calculate one route that reaches an ending, then decide whether to build that four-week prototype.
