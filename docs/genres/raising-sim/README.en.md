# Ludo Atlas · Genre Handbooks · Raising Sim

> **Genre Handbooks · Volume 3**. Positioning: the genre that turns "raising a character" from a numeric process into an emotional experience. Players lay out plans and make trade-offs inside a limited span of time, investing resources into a person who grows, responds and eventually leaves; this page covers the raising loop, stat curves, event branching, emotional connection and content-volume accounting.
> Companions: Game Design Handbook (core loops and balance) · Production Handbook (content estimation and scope control) · Case Studies (subject-driven raising cases) · Pitfalls & Anti-patterns (content and numbers chapters).
> This page carries no links; benchmark titles are widely known works only — if you have not played one, play it first: two hours of hands-on experience beats two hours of reading breakdowns.

---

## 1. Positioning and Core Loop

In one line: a raising sim is the genre **that makes "raising a character" itself the primary content**. The player's core action is neither fighting nor managing but scheduling time: every point of time spent on a stat or a relationship leaves visible and invisible traces on the character, converging into an ending that belongs to this run alone.

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Management sims | The object of management is an abstract organization and a budget, and you read the reports; a raising sim's object is one character with a personality, and you watch what kind of person they grew into |
| Farming sim | The daily loop and the time budget share the same roots, but a farm's output is money and a homestead; a raising sim's output is stats, relationships and endings — currency is only an intermediate resource |
| Virtual pets (the Tamagotchi kind) | An offshoot of the same roots in lightweight form: real-time companionship, micro-interactions, a single thread; raising sim unfolds it into a full structure with a schedule table, a stat system and an event library |
| Monster raising (the Pokémon kind) | There, raising serves battling and collecting; in a raising sim, combat (if any) is only a way to test stats, and the output is relationships and endings |
| Dating sim | A dating sim's endpoint is the character being courted; a raising sim's object is a character the player raised with their own hands, and the romance line is just one optional route |

The core loop, written as a verb cycle:

`read status and goals → make a plan (schedule classes / arrange activities) → execute (spend time and resources) → stats and mood change → events and resolution feedback → adjust the next round's plan`

This loop repeats four beats — plan, execute, grow, reward: planning is where trade-offs happen, execution is the spending, growth is the change in numbers and personality, and reward is events, staging and endings. If any one of the four beats is missing, the game degrades into clicking buttons to watch numbers.

The loop's nested layers, each of which needs its own hook:

| Layer | Duration (real time) | What the player is doing | Resolution point |
| --- | --- | --- | --- |
| One action | Ten-odd seconds | Pick a class or an activity | Immediate feedback |
| One week (one round) | 1–3 minutes | Fill the week's action slots | Weekend resolution |
| One stage | 20–60 minutes | Sprint toward exams, handle major events | Exams, contests, school progression |
| One run | 2–5 hours | Raise a whole life or relationship to the end | Ending |

Nail down three numbers before work starts; every other system revolves around them:

1. How many rounds make up one run, and how much in-game time one round represents.
2. How many action slots a round has and what resources they spend.
3. What the weekly resolution announces (stat changes, mood, triggered events).

A one-line self-check: strip out every event and ending, leaving only stat numbers — does the game still hold up? If the answer is "no", emotion and narrative are this kind of project's real cost line and its moat (§5).

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **The feeling of raising**: invested time pays visible returns, and stats, relationships and living state all change.
2. **The pleasure of planning**: resources are never enough, every schedule is a trade-off, and there is no single solution anyone can memorize.
3. **Emotional connection**: players treat the character as a person rather than a container of numbers — they feel for them, take pride in them, and are reluctant to let go.
4. **Exploration and collection**: events, routes and endings form a list that pulls players into one more run with a different raising approach.
5. **Expression and projection**: players use the character to try out the choices they want, and the ending is the answer to that stretch of choices.

Benchmark titles (a widely known list; raise one full run by hand before breaking them down):

| Title | What to learn from it |
| --- | --- |
| Princess Maker series | The genre prototype: class and schedule planning, stat thresholds, multiple-ending divergence, and the emotional payoff of the father–daughter relationship |
| Chinese Parents | A local-subject sample: turning collective memory into gameplay, stage structure, face and the relatives' quiz, multiple-ending collection, and the sense of boundaries that comes with restrained scope |
| Tamagotchi | The simplest form of emotional connection: real-time companionship, micro-interaction care, responsibility and parting |
| Travel Frog | A spread sample of low-interaction raising: no stat panel; waiting, postcards and gifts keep the attachment alive |

One reminder: these benchmarks carry the scope of a series' accumulation or years of iteration. Match their content density and emotional payoff; do not match their first version.

## 3. Design Essentials

### 3.1 The Raising Loop: Plan, Execute, Grow, Reward

Each of the four beats needs its own design clauses, signed off one by one:

| Beat | Player action | What the system must do | Check question |
| --- | --- | --- | --- |
| Plan | Allocate time across limited action slots | Show expected returns and the uncertainty around them | Can the player say "I'll train this first for the next few weeks"? |
| Execute | Confirm the schedule and spend resources | Resolve stats, mood and money | Does spending feel like it costs something? |
| Grow | See the change | Numeric feedback, state changes, new actions unlocked | Are the changes perceptible and explainable? |
| Reward | Receive events and progress | Trigger staging, advance routes, publish evaluations | Does the reward shape the next plan? |

The time budget is this genre's lifeline: what players want to do must exceed the action slots, or trade-offs do not exist. Size a week's budget like this (the numbers only illustrate the structure):

| Unit | Time cost (in-game) | Player decision | Notes |
| --- | --- | --- | --- |
| One class / one training session | Half a day | Which stat to train | A basic cell of the payoff matrix |
| One part-time job / social outing | Half a day to one day | Trade for money or for a relationship | Competes with raising for time |
| One rest | One day | Trade for mood and stamina | The relief valve of the condition system |
| One week's schedule | The whole week | How to distribute 3–5 action slots | The core decision unit |
| Stage exam | Varies | Sprint or give up | Feedback and threshold |

The budget's acceptance standard is "how much fits into one week": completing 60–70% of what the player wants is the healthy band, with the rest left to the following week. If everything fits, the constraint has failed; if only 20% fits, the pacing is off.

Feedback delay is a hidden pit: an arrangement made at the start of the week that only resolves at the end of the stage strips players of cause and effect. The principle is that resolution never waits overnight — every beat needs immediately perceptible output (numbers ticking, one line of dialogue, an expression).

### 3.2 Stats and Growth Curves: Caps, Bottlenecks, Variety

Fix the skeleton of the stat set first: 4–6 core ability stats, plus 2–4 condition stats and several relationship stats. Condition stats are the shared source of bottlenecks for every stat.

| Category | Examples | How it grows | Caps and bottlenecks |
| --- | --- | --- | --- |
| Ability stats | Intellect / physique / charm / art | Classes and practice | Per-stat caps plus stage ceilings; the later the game, the more expensive each point |
| Condition stats | Mood / stress / stamina | Rest and events | Decide the number of usable actions per week and the return multiplier |
| Relationship stats | Family / friends / mentors | Interaction and events | The thresholds that unlock events and routes |
| Hidden flags | Personality leanings, key choices | Accumulated choices | No visible number; they shape branches and endings |

Three disciplines for the growth curve:

- Diminishing returns are the default shape: repeating the same action yields less each time, forcing players to vary their methods and making late-game maximization cost something. All curves live in config tables, never hard-coded in code.
- Put bottlenecks in resources, not in randomness: limit expansion with mood, stamina and money rather than blocking progress with probability. Players can accept being poor; they cannot accept being bullied by dice.
- Stage jumps supply the thrill: passing an exam unlocks new actions, new scenes and higher return tiers, so growth has steps instead of one flat slope.

How to check variety: lay every action out as a payoff matrix (action × stat) and look for a row that dominates every other row. If one exists, that is the single optimum — players will copy answers off forums instead of making trade-offs; keep the return gap between adjacent actions in the 20–40% magnitude.

Keep stat visibility restrained: give ranges and previews, not exact formulas. Players know "practicing piano roughly raises art and costs some mood" without pulling out a calculator to lay out an optimum; at the same time, identical conditions yield identical results, so hidden randomness never destroys the sense of planning.

### 3.3 Events and Branching: Personality and Route Divergence

Events are the bridge between numbers and emotion: numbers say what happened, events say what it means. The event library splits into four types by trigger condition, and their proportions need quotas:

| Type | Trigger condition | Form | Output |
| --- | --- | --- | --- |
| Daily events | No conditions; repeated at low frequency | 1–2 screens of short dialogue | Character feel, worldbuilding |
| Threshold events | A stat or relationship reaches a threshold | Dialogue plus choices | New actions, new routes |
| Milestone events | Fixed round nodes (birthdays, big exams, holidays) | Staged sequences | A sense of stages, main-line progress |
| Chain events | Prerequisite events plus combined conditions | Multi-screen story | Route divergence, ending clues |

Three disciplines for branch governance:

- Divergence needs convergence points: routes may split, but they cannot split without end. The common structure is three acts — a common phase (roughly the first third) → a split phase (divided into 2–4 lines by personality and numbers) → a convergence phase (funnelling into ending resolution). If every line runs independently to an ending, the budget is guaranteed to blow up (§5).
- Personality accumulates from behavior, not from a single pop-up: the same kind of choice appears in different periods with different weights, and personality flags shape the event pool and ending resolution. Players need the felt sense that "my character is this kind of person", not a permanent label slapped on after one choice.
- Conditions predictable, moments surprising: players should be able to sense that "once the stat is there, something will come", yet the round it triggers must feel fresh. Hang the heaviest events on three combined conditions: stats, prerequisite events and a time window.

Endings are the branch system's final ledger: the resolver (stat thresholds plus route flags plus hidden conditions) must be written as a rule table a person can read and look up; every ending gets its own text and staging — an ending that only swaps one line of subtitles will be seen through on the spot.

### 3.4 Emotional Connection: Anthropomorphism and Feedback

Emotion is not a gift from the plot; it is accumulated from feedback. The three-piece kit that makes a character "seem like a person":

- **High-frequency micro-feedback**: the character reacts immediately after each action resolution (an expression, a catchphrase, a little gesture); in low mood they sulk, in high mood they volunteer extra practice. Most of a player's sense that "the character is responding to me" comes from these few-second moments, not from extended staging.
- **Visible states**: tired, hungry, happy, dejected — all must be seen and heard; dialogue and expressions shift gears with state, instead of one set of lines for every state. The finer the state mapping, the more alive the character feels.
- **Memory and forms of address**: the character remembers what the player did ("last time you made me work, I was so tired"), and how they address you changes with the relationship. The lowest-cost method is to give lines interpolation variables for state and past experience.

Four anthropomorphism techniques: naming (the investment of giving a name), quirks and mannerisms (details unique to this character), anniversaries and birthdays (time anchors), and farewells (the final emotional payoff). Raising sim's emotional highs often land on partings: graduation, journeying away, watching someone leave — the scenes where players most easily cash out their feelings.

The anti-checklist: numbers tick but expressions never change; state changes touch no line of dialogue; the character speaks in one tone from start to finish. With all three together, the character degrades into a container of numbers, and what the player grieves is only their own wasted time.

How to accept it: during testing, watch whether players discuss the character by name, whether they volunteer screenshots to share, and whether they watch the ending through in silence. Any two of the three appearing means the emotional connection holds.

### 3.5 Single Run vs. Full Content: Replay Value

One run should only ever see part of the whole: the totals of the event library, routes and endings must all exceed what a single run can reach, and single-run coverage should sit at 40–60% of the total, with the remainder as fuel for replays. Three hooks: an ending list laid out as a collection, routes not yet finished and character events not yet seen, and speed-up or carry-over options for a second playthrough.

A single-thread, experience-first raising sim can also work, but it needs denser emotional staging; if you plan to carry playtime on replays, the route raised on the second run must differ substantially from the first. Swapping lines without changing structure will not hold players.

## 4. Technical Essentials

The engineering difficulty concentrates in four places: number resolution, event scheduling, the text pipeline and debug tools. A raising sim has no real-time pressure; the hard parts are scaling data and content, and tuning numbers without touching code.

**Data-driven: three tables**

- The stat table, action table and event table all live outside the code (CSV or JSON), and the code only reads tables. The action table stores the payoff matrix, prerequisites and random ranges; the event table stores trigger conditions, dialogue IDs and action instructions. Changing balance means changing tables, not code — the single most important engineering discipline for this kind of project.
- Write resolution logic as pure functions: input the character state and this round's schedule, output the new state and the event queue — no side effects, reproducible. The same random seed must yield the same result; saves, replays and automated tests all lean on it.

**The round framework and event scheduling**

- Drive every system on discrete rounds (weeks or days): at the node, resolve stats, mood, relationships and the event queue; real time suits only the virtual-pet form, and if you take it, handle offline resolution and time cheating in advance.
- Send every trigger through one engine: write condition combinations (stat × relationship × time × prerequisite events) as rules, and never let hand-written ifs scatter across the codebase; keep a separate event roster to self-check content coverage and empty windows.
- Saves serialize the full character state, flags, event history and random seed, with a version number and migration functions. With this many branches and flags, a corrupted save is especially expensive (see Pitfalls & Anti-patterns).

**The text pipeline**

- Keep text external and referenced by ID, with variable interpolation (character name, forms of address, state words) — writing decouples from programming, and proofreading and localization save half the effort.
- Once text volume climbs, build search and consistency tools: one character's way of speaking must stay consistent across different events, and human eyes cannot hold that in memory.

**Debug and validation tools**

- The first tool is a number simulator: render nothing, run the raising logic for tens of thousands of runs, and output the ending distribution, stat growth curves and event trigger rates. Use it to answer "does practicing piano nonstop dominate everything" and "is some ending never triggerable".
- The second tool is decision-log replay: reconstruct one test run as a timeline marked with hesitation points, event triggers and mood lows — far more effective than guessing from a tester's face.
- Feedback presentation (resolution animations, sound effects, curves and radar charts) amplifies the feeling of growth, but it must not paper over curve problems: if the books do not balance, fix the tables first, then talk about staging.

## 5. Content Volume and Workload Reference

Estimate with a "per-unit content cost". The following are common magnitudes for solo developers and small teams; not a commitment:

| Content unit | Unit cost (magnitude) | Minimum viable | Commercial scope | Notes |
| --- | --- | --- | --- | --- |
| One action / class | Half a day to 1 day | 15–25 | 60–150 | Includes numeric setup and copy |
| One event | Half a day to 2 days | 60–120 | 400–1,000 | Includes conditions, dialogue, staging and testing |
| One route | 3–10 days | 2–3 | 6–10 | Includes its exclusive event chain and ending |
| One ending | 1–3 days | 3–5 | 15–40 | Exclusive text, CGs and staging counted separately |
| Character sprite and expressions | 1–3 weeks | 1 set (6–12 expressions) | 3–5 sets (including stage and outfit variants) | Art priced per asset, counted separately |
| Event CGs | 3–10 days | 3–6 | 20–60 | Used for milestones and endings |
| Text | 2,000–4,000 characters of first draft per day | 30k–80k characters | 150k–400k characters | Revision counted separately at 0.5–1× |

A few magnitude conclusions:

- The event library is cost item number one: text, conditions and staging all live inside it. Write down a fixed time budget per event before you start writing, then multiply by the event count.
- Single-run content coverage decides the scope strategy: reaching 40–60% of all events is the healthy band. Below 30% is waste — players never see what you wrote; above 80% one run is the whole picture, and replays lose their point.
- Endings are the most expensive single items: tier them into grand endings, route endings and hidden endings, invest heavily in the grand endings, and let the rest reuse templates and scenes.
- Writing speed and the revision multiplier follow the Visual Novel page's conventions (2,000–4,000 characters of first draft per day, revision at 0.5–1×).
- Benchmark reminder: Princess Maker and Chinese Parents both carry the scope of series accumulation or years of iteration. Any plan to "build a complete raising sim in three months" should be halved, then halved again.
- Cutting priority, highest to lowest: merge events and endings (one piece of content serving several lines) > replace staging with text > reduce the number of routes > trim sprite variants and animation > cut the number of raisable characters. Cut in the wrong order and the first thing sacrificed is the emotional payoff — the part you should least afford to save on.

## 6. How to Start the First Prototype

The first prototype takes 2–4 weeks: one character, 4 stats, 2 routes, 10–15 events, 2–3 endings, one run of 16 rounds played to the end, without touching final art or voice acting.

**Week 1: paper design and the resolution skeleton.** First write three tables on paper — the stat table, the action table (the payoff matrix) and the ending resolution table; then implement round resolution and one action, closing the minimal loop of "schedule, resolve, change". This week only checks whether the books balance; ugly is expected.

**Week 2: curves and bottlenecks.** Put in 4 stats, 6–8 actions, and mood and stamina as two condition stats; run 100 consecutive runs in the simulator to check for must-train actions, dead-end routes and stepped growth. The goal is a trade-off every round and no single optimum.

**Week 3: events and divergence.** Write 10–15 events (some daily, some threshold, some milestone, some branch chains), hook up 2–3 endings, and get the "stat arrives, event comes" triggers working so one run plays from start to finish.

**Week 4: testing and the emotion check.** Find 5 people who have never played and have each raise one run (20–40 minutes per run), with no hints and no explanations; record hesitation points, laugh points, boredom points, and whether anyone calls the character by name.

Success criteria (all observable):

- At least 4 of 5 testers finish a run with no hints and can say which ending direction they want to raise toward.
- At least 3 volunteers say they "want to raise one more on a different route"; without replay appetite, divergence and content coverage are insufficient.
- Someone discusses the character by name, and someone shows real emotion at the ending; if neither happens, go back and add micro-feedback and state-driven lines (§3.4).
- Change any single number and you can quantify its effect on the ending distribution in the simulator within 5 minutes.

Only once both gates — numbers and emotion — pass should you lay out the event library and the art. Reverse the order and the rework lands on the content side, where it costs far more than during the prototype.

## 7. Common Pitfalls

1. **Constraints fail**: so many action slots that everything you want fits, trade-offs vanish and players start clicking mindlessly. Avoidance: set the time budget first, then the content (§3.1).
2. **Runaway curves**: by the late game one round maxes every stat, or the early game stalls to a crawl. Avoidance: diminishing returns plus stage ceilings, with the simulator running distribution checks (§4).
3. **A single optimum**: one action or route dominates every other choice and trade-offs become memorized answers. Avoidance: keep a 20–40% tier gap across the payoff matrix and check it row by row (§3.2).
4. **Numbers decoupled from events**: stats rise and nothing happens in the character's life. Avoidance: attach one stat-gated event to every stage so the character reacts to their own growth (§3.3).
5. **Branch costs out of control**: every route gets its own plot, and by the third one you realize you cannot finish. Avoidance: the three-act structure with convergence points, and tiered endings that reuse assets (§3.3, §5).
6. **Emotional connection absent**: one tone from start to finish, and states that never touch the lines. Avoidance: high-frequency micro-feedback, state mapping and changing forms of address (§3.4).
7. **Feedback delayed too long**: a decision's consequences take so long to appear that players lose their sense of cause and effect. Avoidance: resolution never waits overnight; every week has visible output (§3.1).
8. **Endings unreachable or unreadable**: players do not know which way to go, or one ending never triggers. Avoidance: give clues sparingly but give them, and verify with the simulator that every ending is reachable (§4).
9. **Content volume underestimated**: thinking "events are quick to write", then finding half-way through that it is a multi-year project. Avoidance: work through the §5 tables first, cut down to something deliverable, then start.
10. **Replays with no point**: one run is the whole picture, and ending collection cannot save it. Avoidance: keep single-run coverage at 40–60% and save substantial differences for a second playthrough (§3.5).

## Further Reading

- Game Design Handbook, two sections to reread: core loops and nesting, and the sources and sinks of the number system — then draw a flow diagram of "time → stats → events → endings".
- The estimation chapter of the Production Handbook: time one action, one event and one ending each once, then multiply by the content volume.
- The Chinese Parents piece in Case Studies: note the conclusions on "subject resonance and scope restraint", and the time structure by which talkability drives spread.
- The content and numbers chapters of Pitfalls & Anti-patterns: read against §7 of this page.
- Companion pages in this handbook: Farming Sim (time budgets and content estimation), Visual Novel (text governance and staging conventions), Idle / Incremental (the extreme form of numeric curves).
- Homework: build a 16-round raising model on paper and in a table — 4 stats, 6 actions, 2 endings; hand-calculate one growth route and its ending resolution, then decide whether to greenlight.
