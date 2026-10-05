# Ludo Atlas · Genre Handbooks · Management Sim

> **Genre Handbooks · Volume 2**. Positioning: a handbook page for running an organization, breaking the "invest, produce, expand" loop, the numeric economy, system coupling and dashboard information design into executable checklists.
> Companions: Game Design Handbook (core loops and economy) · Production Handbook (content estimation and scope control) · Case Studies (management-sim cases) · Pitfalls & Anti-patterns (the numbers and content chapters).
> This page carries no links. Benchmark titles list only widely known works: play them for ten hours first, then come back and break them down against the tables.

---

## 1. Positioning and Core Loop

A management sim puts the player in charge of running an organization: a hospital, an amusement park, a restaurant, a zoo, a game company — any of them. Players don't wait tables, sweep floors or prescribe medicine themselves; they decide what to build, whom to hire and what to charge. The staff do the work and the customers pay the bills. The organization runs itself according to the rules the player sets up, and the player's job is to tune it into a machine with positive cash flow, then make it bigger.

In one line: **through building, hiring and pricing, make a system that runs by itself survive on the books first, then grow it.**

The core loop, written as a verb chain:

`site selection and construction → recruiting and training → serving customers and producing → settling revenue and satisfaction → unlocking and upgrading → expanding and relocating → a bigger customer base → back to step one`

The loop nests three levels deep, and each level has a different hook:

| Level | Duration (real time) | What the player is doing | Settlement point |
| --- | --- | --- | --- |
| Minute level | Seconds to tens of seconds | One customer completes the flow, one payment lands | Immediate sound effects and floating text |
| Business-day level | 5–15 minutes | A full day of operations and revenue/expenses | The daily settlement report |
| Stage level | 1–3 hours | One map or one star-rating objective | Unlocking new facilities and new maps |

The loop's engine is positive feedback: revenue funds expansion, expansion brings foot traffic, foot traffic brings more revenue. The designer's job is to install gates on this circuit (§3.1) and open them on a rhythm, rather than letting it burn out in the opening two hours.

Boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Farming sim | That genre manages one character and one plot of land, down to a single day and a single tile; this genre manages abstract organizations and budgets, down to rooms, staff and cash flow |
| City builder | Its subject is the city itself, with layout and zoning as the main event; this genre's subject is one organization, with the micro-flows of staff and customers as the main event |
| Colony sim | There, every individual has personality and generated story; here, customers and staff are a population in the statistical sense |
| Idle/incremental | That genre minimizes operations and turns waiting into the selling point; this genre demands continuous decisions and adjustments |

## 2. Player Experience Goals and Benchmark Titles

Players come to this genre for five things, in priority order:

1. **A sense of control**: a chaotic organization becomes orderly in the player's hands, bottleneck by bottleneck.
2. **Visible growth**: numbers (revenue, foot traffic, ratings) and space (new rooms, new floors) grow at the same time.
3. **The optimizer's delight**: higher efficiency toward the same goal, with players finding better layouts and processes themselves.
4. **Crisis and firefighting**: emergencies (broken equipment, a wave of complaints) bring brief tension, released once solved.
5. **Self-expression**: arranging, naming and landscaping, so the organization carries the player's own mark.

Benchmark titles (all directly playable; play first, read later):

| Title | What to learn from it |
| --- | --- |
| Theme Hospital | The prototype textbook: rooms, staff and illnesses as a trio, wrapped in humor |
| Two Point Hospital | The modern version: department circulation, staff progression, level star ratings and light narrative |
| RollerCoaster Tycoon | Park operations plus building expression; the coupling of facilities and visitor needs |
| Planet Coaster | The move to 3D and creator tools; how player-made content becomes a selling point |
| Planet Zoo | Conservation and management as two lines; turning the theme into mechanics |
| Kairosoft series | Lightweight and high-density: squeezing invest, produce and expand into a few hours on a small screen |

## 3. Design Essentials

### 3.1 The Management Loop and Positive-Feedback Pacing

The three stages — invest, produce, expand — cycle at a fixed beat, and each one hands the player a clear next step:

| Stage | Player action | System response | Checkpoint |
| --- | --- | --- | --- |
| Invest | Build rooms, hire staff, buy equipment | Costs visible, build times visible | Every dollar spent shows what it bought |
| Produce | Watch the operation, fine-tune the setup | Revenue and satisfaction move in real time | The cause-and-effect chain is visible within seconds |
| Expand | Unlock new facilities, open new areas | A bigger customer base, new needs appear | Expansion immediately brings new problems rather than simple scaling |

Positive-feedback pacing is controlled by three things:

- Unlock gates: new facilities hang off objectives (star ratings, fame points, quest chains), so players can see exactly what is still missing.
- Cost ladders: expansion costs grow faster than revenue (an upgrade fee rising 50% while revenue rises only 20%), pushing players to optimize instead of just stacking more rooms.
- Breathing stretches: after intense expansion, give a low-pressure stretch of operations so players can digest the new systems while enjoying the payoff; introduce only one new system between two stage objectives.

### 3.2 The Numeric Economy Architecture: Resources, Exchange Rates and Inflation

Discipline on resource types: **one to three, and if one will do, don't have two**. Every extra resource adds another output line, another display slot, another tutorial lesson. There are only two legitimate reasons for a second resource: to put a speed limit on expansion (reputation, credentials), or to create an either/or trade-off (two customer segments each accepting their own currency).

Secondary resources beyond the main currency all end up converted into the main currency in the player's head. Write the conversion rule into the design document:

| Secondary resource | Conventional conversion | Design role |
| --- | --- | --- |
| Satisfaction | Converts into a foot-traffic or revenue multiplier | Turns service quality into a visible number |
| Reputation and fame | The accumulated value sets customer-segment and facility thresholds | Puts a speed limit on expansion |
| Research points | Convert into a long-term efficiency multiplier | Steers money toward long-term investments |

The table fixes only the conversion rule; tune the coefficients against measurements in your own project. The test for whether a secondary resource should exist at all: does it let players make a trade-off that no other resource can express?

Inflation is the biggest mid-game pitfall: if costs stay flat while revenue rises linearly, the game loses its challenge a third of the way in. Three categories of control:

- Synchronized increases: reset the cost structure with each new map or stage, so old levels' solutions cannot be carried over directly.
- Diminishing returns: building repeated facilities of the same type yields less (a second identical ward runs at a discount), pushing players to vary their mix.
- Money sinks: outlets that consume money without producing anything — decoration, training, charity — giving surplus cash somewhere to go.

Balancing has exactly one discipline: build the table first, measure second; reverse the order and the project flips over.

- Build a "net profit per unit time" table: one row per facility or production line, counting net profit, not the price tag of a single sale.
- Annotate the payback period: how many hours until an investment breaks even, so players can work out for themselves whether it is worth it.
- Review the curves every ten hours: money that cannot be spent (not enough sinks) or money that is never enough (output too low) both surface at this step.

### 3.3 System Coupling and Dashboard Information Design

Coupling is where this genre's depth comes from: staff affect service speed, service speed affects satisfaction, satisfaction affects foot traffic, foot traffic affects revenue, revenue decides expansion. The longer the chain, the more depth — and the easier it turns into a black box.

The dashboard's mission is to crack the black box open in front of the player. Three principles:

- No more than five key metrics: cash, foot traffic, satisfaction, staff load, objective progress. Everything else goes onto a secondary screen.
- Traceable cause and effect: any abnormal number can be traced to its source in two or three clicks (low satisfaction → 12 people queuing at one department → missing a diagnostic room).
- Tiered alerts: surface only the highest-priority alert at a time, with the rest queued; twenty lines of red text amount to no alert at all.

Checklist: ten minutes into the game, can a new player say "why am I losing money right now"? If not, fix the dashboard before adding systems.

### 3.4 The Trade-off Between Automation and Micro-management

What players do personally should stay at the decision layer forever; repetitive labor goes to the staff (the in-game AI):

| Layer | Examples | Who handles it |
| --- | --- | --- |
| High-level decisions | What to build, where to build, pricing, whom to hire | The player, always manual |
| Mid-level management | Scheduling, upgrades, training, priorities | The player sets it once, then it runs automatically |
| Low-level execution | Cleaning, delivering medicine, seating guests, maintenance | Staff, executed automatically |

Three balance points for automation:

- Too early and players lose their sense of involvement; too late and their patience wears out. The common dividing line: once the same task has been done twenty times, an automation option should appear.
- Automation needs toggles or policy options: players can intervene in how it behaves (priorities, zone restrictions), rather than all-or-nothing.
- Keep one category of emergency handling that only the player can do (sudden events, VIP visits), so micro-management keeps a little game feel.

Acceptance test: have a player play for three hours straight, then ask "at which moment did you feel most like the boss". If they can't answer, the line between decisions and micro-management is not drawn well.

### 3.5 The Multiplicative Relationship Between Content Volume and Systems

This genre's cost structure is multiplication, not addition: number of systems × number of content entries × verification passes per level.

- Every facility type added has to be tested against every customer segment, every level and every staff profession.
- Every customer type added (patients, visitors, diners) has to be able to complete the objectives across all facilities and all levels.
- Order of magnitude of combinations: 3 facility types × 4 customer types × 10 maps = 120 combinations, and each one has to be verified in the table at least once.

Discipline: **fix the ceiling on the number of systems first, then fill each system with content**. Do it the other way around and you will discover mid-project that verification costs exceed the development budget.

## 4. Technical Essentials

- Separate simulation from presentation: the simulation layer runs on a fixed step (commonly 10–20 ticks per second) while the presentation layer subscribes to events for animation and audio. The payoff: time acceleration, save-and-replay, and batch runs with no rendering.
- Data-driven all the way: facilities, equipment, professions, customer types, level objectives and economy parameters all go into tables (CSV, JSON or engine table assets); code only reads tables.
- Customer flow is the core system: a needs state machine (arrive, queue, walk over, get served, leave or return for a follow-up visit), paired with a navigation mesh and queue-point management.
- Staff AI goes from simple to complex: the first version uses a task queue plus priorities (scan for to-dos, claim, execute); don't start with the full behavior-tree toolkit.
- Performance: with many agents, use time-slicing and zone activation (distant customers update at a lower rate), and cache and batch-recompute pathfinding; test worst cases first (clinic rush hour, a full zoo).
- Debug tools and batch runs: time acceleration, direct money editing, state flags, inspecting one customer's full flow; add a placeholder player that builds and hires automatically, run ten sessions and print the revenue/expense curves per level — imbalanced spots float to the surface by themselves.
- Saves: serialize the full set of simulation objects with a version number and migration functions, so loading mid-session loses no state; old saves surviving a balance update is basic courtesy in this genre.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimation and for cutting requirements; not a commitment.

| Project form | Content list | Time magnitude |
| --- | --- | --- |
| Gameplay prototype (greybox) | 1 floor plan, 1–2 facility types, 1 customer type, no production art | 2–4 weeks |
| Vertical slice | 1–2 maps, 5–8 facility types, 3–5 customer types, one set of level objectives | 3–6 months |
| Small commercial scope | 8–15 maps, 15–25 facility types, 10–20 customer types, achievements and stats | 12–24 months |
| Full commercial scope | Dozens of facility and customer types, three or more profession lines, continuous updates | 1–3 years for a team |

Typical cost per content unit (magnitude reference):

| Content unit | Unit cost | Notes |
| --- | --- | --- |
| One facility type | 3–10 days | Model, animation, numbers, icon, balance |
| One customer type or need | 2–5 days | Flow, behavior, numbers, copy |
| One staff profession | 3–7 days | Task logic, animation, skills and upgrade line |
| One map and its objectives | 1–3 weeks | Layout, level objectives, difficulty tuning |
| One tier of feedback sound effects | A few hours | Cheap individually, but they add up |

A worked multiplier example: adding one more facility type visually doesn't cost 3–10 days — it multiplies by the number of customer types and maps it has to be tested against. Write the multiplication result down on paper before deciding whether to build it.

## 6. How to Start the First Prototype

The first prototype builds one complete chain only, finished in 2–4 weeks, with no production art or story:

1. One floor plan with one entrance and one exit; first make it possible for customers to get in and out.
2. One need: customer arrives → queues → gets served → pays → leaves. Get this single path working and the game has a heartbeat.
3. One staff member: automatically scans for to-dos and handles them one by one. This is the project's first AI — build the simplest version.
4. Cash flow: one construction cost, one service payment, one settlement per day. Play three days straight and see whether the curve points the right way.
5. One dashboard: cash, foot traffic and satisfaction plus one objective progress bar; players must be able to understand why.
6. One expansion: add a second facility type and the new customers it brings, validating the "expansion brings new problems" loop.
7. Saves: version numbers from day one.

Acceptance criteria (all observable):

- Within ten minutes the player feels the urge to "build one more" — and can say where the money will come from.
- After one failure (cash run out or customers lost), the player can name the cause and a plan to fix it.
- With all art and audio removed, testers still want to play to the third business day.

## 7. Common Pitfalls

| Pitfall | Symptom | Avoidance |
| --- | --- | --- |
| Too many stacked systems | Players cannot remember how rooms, staff and numbers relate | Fix the system ceiling first (§3.5), then fill in content |
| A flood of resource types | Five currencies each holding a display slot; everything turns into conversion homework | One to three; convert the rest into the main currency |
| Runaway mid-game inflation | Halfway through, money has nowhere to go — or is never enough | Review the revenue/expense curves every ten hours; add money sinks or adjust the ladder |
| An unreadable dashboard | Players say "I don't know what happened" | The five-metric principle plus causal tracing; fix the dashboard before adding systems |
| Automation at the wrong tempo | Players call it idle, or call it exhausting | Use "done it twenty times" as the line for automation to appear |
| Staff AI deadlocks | Customers jam the door yelling; the game looks broken | Write deadlock detection and fallback handling into the first version of the AI |
| Tuning tables without touching structure | Ten revisions of the numbers, same problem | Fix structural problems first (flow, coupling), then tune numbers |
| Underestimating the content multiplier | The back half of the schedule explodes; no time to cut anything | Use the worked multiplier example in §5; cut systems to protect quality |
| Neglecting audiovisual feedback | The logic is right but players cannot feel it | Every payment, achievement and complaint needs a picture and a sound |

## Further Reading

- Game Design Handbook: core loops and nesting, sources and sinks in the economy — the higher-level method behind §3.1 and §3.2.
- Production Handbook: estimation and scheduling, to be used alongside §5. Time "one facility, one customer" first, then do the multiplication.
- Case Studies: postmortems of management titles; pay attention to the iteration cadence of "running it while being educated by the data".
- Pitfalls & Anti-patterns: balance flip-flopping and runaway content volume are high-frequency hazards; run through it before starting work.
- Indie Survival: scope control. The ceiling on system count is set by your team and budget, not by ambition.
- Exercise 1: pick one Theme Hospital level and draw the complete flow diagram of a customer from arrival to departure, marking every queue point and chokepoint.
- Exercise 2: build a ten-day economy model on paper: two facility types, two customer types, three cost categories; compute the net profit per day and compare the experience difference between day one and day ten.
- Exercise 3: write a dashboard checklist for the prototype you're working on — five key numbers, the causal source of each, and the highest-priority alert when it misbehaves.

The foundation of a management sim is one chain that can run by itself: make it turn first, and only then talk about expansion.
