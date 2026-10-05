# Ludo Atlas · Genre Handbooks · Life Sim

> **Genre Handbooks · Volume 4**. Positioning: the genre that makes "living an everyday life" itself the main loop. Characters begin each day carrying needs, relationships and identity; the player answers them with a time budget, and day stacking on day becomes long-term progress. This page covers five structural blocks: the needs-driven schedule loop, character customization and identity expression, the modularization of social systems, content-matrix management and long-term live-ops.
> Companions: Game Design Handbook (core loops and systems design) · Programming Handbook (simulation loop and data pipelines) · Production Handbook (content volume and scope control) · Case Studies (series breakdowns and live-ops retrospectives).
> This page carries no external links; benchmarks are widely known works only, and the figures are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: a life sim is the genre **with "living an everyday life" as its first-class content**. The character is not a vehicle to be steered through a clear condition but a person carrying needs, relationships and identity; the player's job is to arrange the character's every day sensibly — and arrange it into something like "the life they want to live". The core loop is a needs-driven daily schedule loop: needs rise over time, the player satisfies them one by one within the day's schedule, and the time left over beyond that satisfaction is the discretionary room used to live "the wanted life". Without needs, the schedule has no direction; without discretionary time, the schedule is just an assembly line.

The core loop, written as a verb chain:

`wake up → check needs and mood → plan the day → do things, work, socialize → relationships and the ledger change → sleep settlement → a new day`

The loop's nesting levels:

| Layer | Measurement (real time) | What the player is doing | Settlement point |
| --- | --- | --- | --- |
| Day | 10–30 minutes | Planning and trading off one day's schedule | Sleep settlement (needs restored, bills, relationship retention) |
| Life stage | Tens of hours | Growing up, career, romance, having and raising children | Stage transition (birthday, graduation, retirement) |
| Generation | Long-term commitment | Continuing the family line and collecting its stories | Generational handover |

Drawing boundaries against neighboring genres:

| Neighboring genre | Boundary |
| --- | --- |
| Farming sim | A farming sim's day is a production plan and its main line is accumulation and expansion; a life sim's day is an answer sheet of needs and its main line is the characters and their relationships. |
| Management sim | A management sim runs an abstract organization and its budget; a life sim runs one concrete person's or one family's day. |
| Raising sim | A raising sim cultivates an assigned subject toward a clear graded endpoint; the life sim's goals are set by the player, with no uniform completion. |

A self-check question: delete the need bars and the schedule system entirely — does the game still stand? If the answer is "yes", what you have is closer to a decorating or collecting game; only if it is "no" is the needs-driven loop really carrying the genre.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Self-expression**: looks, personality, home and lifestyle are all defined by the player — expression itself is the first pleasure.
2. **Command of the everyday**: needs attended to and the books kept, the days arranged more and more smoothly, until the player feels "I've really figured out how to run this family's life".
3. **Relationships that respond**: characters are remembered and cared about; changes in relationships are visible, tangible and lasting.
4. **Emergent stories**: systems collide into scenes the player never rehearsed — and afterwards they want to tell someone about them.

Benchmark titles (all widely known works; play them yourself before breaking them down — watching videos will not convey how a day gets lived):

| Title | What to learn from it |
| --- | --- |
| The Sims series | The foundation of the genre: how the four-piece set — needs, schedule, relationships, building — is organized; the trait system; long-term live-ops with expansions and a mod ecosystem |
| Animal Crossing series | Real-time clock and zero failure: soft-goal writing, seasonal calendars, and a sample of sharing and community ecosystems |
| Story of Seasons series | A life at small-town scale: schedules, stamina and community relationships in a compact scope |
| Stardew Valley | The indie sample: why one person's small-town life holds up across dozens of hours of repetitive labor |

One reminder: these works' scope comes from years of iteration and industrial pipelines — match their lived-in feel and pacing, not their total content volume.

## 3. Design Essentials

### 3.1 Needs and Schedule: A Day Is an Allocation Problem

Organize the needs list in two branches: physical needs (hunger, energy, toilet, hygiene) and psychological needs (social, fun, environment). Discipline on the count: 5–8 is right. Fewer than 5 leaves nothing to trade off; more than 8 turns into a checklist. Every need must have at least two ways to satisfy it, and the ways must differ in cost (instant noodles are fast; cooking is slow but lifts mood). Every need gets three parameters: decay rate, threshold tiers (comfort, warning, failed), and failure consequences. The consequences must be restrained and rare: passing out or losing composure in public is a story once in a while, and torture if it happens daily. The core decision every day is "which part of the needs gets left to tomorrow": stay up late to finish what you want to do, or go to bed on time and protect tomorrow's state.

A day's time budget splits into two stretches, need maintenance and discretionary time:

| Stretch | Share reference | Content | Design goal |
| --- | --- | --- | --- |
| Need maintenance | 50%–60% | Eating, sleeping, washing, commuting, basic work | Make the everyday feel real without swallowing all the time |
| Discretionary | 40%–50% | Socializing, hobbies, running side businesses, tending the home | Everything in "the life the player wants" lives in this stretch |

### 3.2 Character Customization and Identity Expression

Customization is the product's signature and its largest asset pipeline. Fix four dimensions together:

| Dimension | Content | Cost warning |
| --- | --- | --- |
| Appearance | Face shape, body type, skin tone, hair, clothing | Every added part category adds a category of modeling, rigging and clipping tests |
| Voice and manner | Voice, gait, habits of movement | Voice is the cost item with the widest variance — limit it to scenes on screen |
| Personality | 2–4 traits | Every trait must change one observable behavior; see below |
| Background | Name, age, family, starting funds | Determines a whole opening set of scripts and numbers |

Discipline for the trait system: **every trait changes at least one observable behavior or number**. A lazy character cooks slowly but gains little stress; a neat one cleans unprompted; a loner's social need decays more slowly. A trait that changes behavior is gameplay; one that does not is a sticker.

Identity expression runs through three channels: the character itself (looks, personality, habits), the look of the home (building and decorating), and lifestyle choices (career, hobbies, daily rhythm, pets). The house is a self-portrait the player paints; the furniture is the set for the lines. Build and buy modes are therefore not accessories but a second engine on the same tier as the needs system.

Checklist: once the character is made, can the player say "who this person is and what kind of life they want"? If not, customization has only finished the reskin layer.

### 3.3 Modularizing Social and Relationship Systems

Relationship data must be stored as a graph: between two people, two one-way affinities (A toward B and B toward A tracked separately), two axes (friendship and romance), one relationship label (stranger, friend, best friend, lover, spouse, family, rival), plus a family tree attached to it. The family tree is a long-term asset; from day one it must hold up under generational continuity.

The core formula of modularization: **interaction = verb × target × relationship state × context**, all registered in one interaction table — never one script per interaction:

| Verb | Applicable conditions | Effect | Context dependence |
| --- | --- | --- | --- |
| Greet | Any two people | A little affinity | Lines and outcomes differ for a first meeting and for old friends |
| Deep talk | Friend or closer | Big affinity gain, stress down | Needs a private place or a full stretch of time |
| Argue | Tense relationship or trait conflict | Large affinity loss | Costs more in public |
| Date | Romance axis unlocked | Big movement on the romance value | Occupies a venue and half a day's schedule |

NPC autonomy splits into two layers: characters on screen with the player act on their own needs and personality, while off-screen characters settle through a coarse model (proportional progression or probabilistic events). Full simulation of everyone is a luxury — do not buy it in version one.

Budget for "being remembered": each character keeps a short event memory (who did what to whom), and interaction lines can reference it. This is the key step that turns relationships from progress bars into people.

Checklist: pick any two characters — can the system generate a believable everyday interaction? Is their relationship history fully consultable, editable and testable? If every new interaction has to be hand-scripted, the content will outgrow your ability to write it.

### 3.4 Breadth of Activities and Venues: Content-Matrix Management

A life sim sells a cross-section of life; breadth is managed by a matrix, not by adding content on a whim. Rows are venues, columns are activity categories, and each cell marks whether that combination works:

| Venue | Social | Entertainment | Skills | Earning | Collection |
| --- | --- | --- | --- | --- | --- |
| Home | Hosting, dinner parties | TV, games | Cooking, fitness | Side work, crafting | Photo albums, souvenirs |
| Park | Chance meetings, picnics | Morning jogs | Fishing, gardening | Market stall | Birds and insects |
| Diner, bar | Gatherings, live music | Dancing | Bartending | Part-time work | Limited-edition drinks |
| Library, museum | Quiet socializing | Viewing exhibitions | Knowledge | — | Collections |
| Shopping street | Socializing while shopping | Shopping | — | Wage work | Limited-edition goods |

Matrix discipline: every venue supports at least 3 activity categories; every activity appears in at least 2 venues; a blank cell is either deliberate negative space or a gap, and every blank must have a reason you can state. Priority for new content, high to low: repeatable small activities inside venues > one-off events > new systems; repeatable small activities cost the least and hold up the day-after-day loop best.

Off-screen activities settle through rabbit holes: work and school — activities that do not need the player present — advance probabilistically, which is the only way to hold the cost down; activities requiring the player's presence are the main content. The same logic applies at neighborhood scale: fill one street first, then talk about a seamless large map; simulating the whole city costs more performance than it is worth, and most projects compromise between chunked loading and layered simulation.

Recurring events are the calendar's highlights: birthdays, festivals, parties, graduations — costed by the scene. Holidays serve socializing and commemoration, not as containers for combat activities; do not blur the two kinds of tasks.

### 3.5 Long-Term Live-Ops and Community Ecosystems

Content consumption speed: a player typically burns through one content pack in a few dozen real-world hours, so even a single-player title has to plan long-term. The common mix is free updates to hold the reputation and paid expansions selling new life scenarios; the iron rule for expansions: **one content pack = one new life scenario + a system hook bound to it** (city, countryside, pets, seasons, university — each an example). Pure decoration packs can be giveaways, never the headline.

UGC and mods are half the lifespan of a single-player life sim. For a long run, the official editor and scripting interface set the community's ceiling, and the rules for extension interfaces, version compatibility and save rollback have to be settled early; the two successful samples bring different strengths: one runs on tools (players can change systems and make content), the other on showing off (players share outfits, homes, islands). A display-driven ecosystem only needs room for sharing and visiting, while a tool-driven one must make mod troubleshooting and version announcements part of daily operations; community challenges are a free content engine: generational challenges, building challenges, themed character contests — the rules come from the community, and the official side only needs to leave space for them, plus featured slots and creation contests as incentives.

## 4. Technical Essentials

The engineering difficulty concentrates in four places: the simulation loop, space and interaction, character AI, and saves and tooling. Everything below is engine-agnostic.

- **Simulation loop**: one global clock plus an activity scheduler (who is doing what, when it ends, the event queue); process needs in batches at settlement points rather than iterating over every character each frame; spread large batches of decisions across frames so a single frame does not make them all.
- **Data and text**: needs, interactions, furniture, items, careers, events and dialogue are all externalized as tables that the code only reads; systematic text is assembled from templates × word banks, with hand-written passages reserved for key beats. In a content-heavy genre, the pipeline comes before the volume.
- **Space and interaction**: furniture is defined by interactable slots (a chair can be sat on, a bed slept in, a fridge raided), and interactions hang off the slots; multi-floor interiors, furniture blocking and room detection (automatic wall and floor cutting, camera sectioning) are this genre's own spatial engineering — do not underestimate them.
- **Character AI**: needs-driven behavior selection uses a scoring subsystem or behavior tree, with adjustable autonomy levels; the selection must guard against a "need avalanche", with a priority queue and cooldowns as backstops.
- **Relationship and family graphs**: a graph structure stores two-way affinity, labels and bloodlines; kinship checks and validity validation are written as graph algorithms, so generational growth needs no rework.
- **Saves**: the state volume is enormous (every object, every character, every relationship, every memory); build version numbers and migration functions from day one, so old saves still open after expansion content stacks on.
- **Tooling**: the first tool is a debug panel (edit needs, edit relationships, teleport, adjust the time multiplier) plus an event log; build mode has to be built as a product-grade tool (grid snapping, rotation, wall editing, an undo stack), not a leftover of the engine editor.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for scope estimation; not a commitment.

| Content unit | Unit cost (magnitude) | Minimum viable | Commercial scope | Notes |
| --- | --- | --- | --- | --- |
| Needs and basic action set | 2–4 weeks | 5 needs | 8–12 needs with tiers | A one-time foundation every system hangs off |
| One interactable furniture piece | 0.5–2 days | 15–20 | Hundreds | Modeling, animation, slots, clipping tests |
| One social interaction | 0.5–1 day | 15–25 | Hundreds | Reused by verb and condition once modularized |
| One followable career | 2–6 weeks | 0–1 | 5–10 | Each equals a mini-game |
| One life stage | 1–3 weeks | 2–3 | 6–8 | Animations, interactions and growth rules |
| One expansion-level system | 2–6 months | — | Several every 1–2 years | New scenario + system hook + asset pack |

Magnitude conclusions:

- The bulk of the cost is the product of system × assets × combination testing: add one need, and what you owe is its cross-testing against every piece of furniture, every interaction and every AI path.
- The realistic slice for solo developers and small teams: cut breadth (venue count, appearance part count, career count) and keep depth (get needs, schedule and relationships working first). A small cut is a common way to live: one apartment, one family, one career — go deep on one small patch.
- Reserve content consumption at a few dozen real-world hours per pack, and use that as the scheduling anchor: needs prototype 4–8 weeks; vertical slice (one day plus one family plus one relationship line plus one career, all at finished quality) 6–12 months; then extrapolate by content units times a polish factor. Free small updates and paid large packs each have their own cadence — decide which one you are running first.

## 6. How to Start the First Prototype

Goal: in 6–8 weeks, build the minimum playable version — "one person, one room, one day" — all placeholder art, without touching the deep end of character creation or build mode.

Mini spec: 1 character, 1 small house (kitchen, bedroom, bathroom), 5 needs, 10–15 furniture pieces, 15 interactions, 1 rabbit-hole job, 1 neighbor, 1 bill.

Steps (run in order; every step ends in something playable):

1. Needs and clock: 5 needs plus a day's time flow, with sleep triggering settlement; tune only "is one day fun" first.
2. Character and furniture: movement, pathfinding, using furniture (eating, sleeping, washing, playing, sitting) — furniture runs on slots, no special cases.
3. One neighbor: a relationship value, two interactions (chat and gift), one relationship-upgrade event — get the minimal social pipeline running.
4. Schedule pressure: one job plus one bill, so time and money fight for the first time.
5. Testing: have 3–5 people play 3 in-game days in a row, with no hints and no explanations; record what they attend to first, what they sacrifice, and how many times they say "one more day".

Acceptance criteria (all observable):

- Testers can state the character's needs status and "what I want to do tomorrow".
- At least one instance of the "one more thing and then I'll sleep" hesitation is observed.
- With art and audio removed, someone still wants to play 3 in-game days in a row.
- At least one retellable emergent scene appears: needs clashing, a relationship crashing, or the schedule collapsing all count.

Anti-patterns: building the character creator first, build mode first, or a big family first. This genre's foundation is "needs plus a day", not "asset count".

## 7. Common Pitfalls

1. **Needs list out of balance**: under 3 there is nothing to trade off, over 10 it becomes a checklist. Keep it at 5–8, each with at least two ways to satisfy it (§3.1).
2. **Maintenance swallowing the day**: the player has no room left to live the wanted life. Hold the maintenance stretch to 50%–60% and leave 40%–50% discretionary (§3.1).
3. **Deep character creation and build mode too early**: the art and clipping-test load is bottomless while the gameplay is still unvalidated. Keep only a minimal placeholder version during the prototype (§6).
4. **Interactions written as special cases**: one script per interaction, and costs explode as characters and content are added. Modularize by verb × condition × state (§3.3).
5. **Relationships as a single-value progress bar**: with no memory and no stages, NPCs are faceless robots. Add event memories, stages and confirmation events (§3.3).
6. **Venues and activities living apart**: beautiful streetscapes with nothing to do. Check coverage with the content matrix; every blank cell needs a reason (§3.4).
7. **Simulating everyone in full**: chasing a seamless whole city, and the performance avalanches. Compromise on layered simulation plus chunked loading (§3.4, §4).
8. **Expansions stacked with decoration**: a new pack that only adds cosmetic content, and players do not buy it. One pack, one new scenario plus a system hook (§3.5).
9. **UGC interfaces postponed**: the long run depends on them, but the tools never come and the community never starts. Settle extension interfaces and save compatibility early (§3.5, §4).
10. **Saves without version numbers**: the larger the state, the more fatal a corrupted save. Build version numbers and migration functions from day one (§4).

## Further Reading

- [Game Design Handbook](../../fundamentals/game-design/README.md): the base document for core loops, systems design and numeric tables.
- [Programming Handbook](../../fundamentals/programming/README.md): implementation essentials for the simulation loop, AI and saves — the base for §4.
- [Production Handbook](../../fundamentals/production/README.md): content estimation and scope control, complementing §5.
- [Case Studies](../../postmortems/README.md): breakdown and live-ops retrospective methods for series-style works.
- [Indie Survival](../../../playbooks/indie-survival/README.md): scope control and scheduling — read before greenlighting a small-cut project.
- [Genre Handbooks · Farming Sim](../farming-sim/README.md) (Volume 1): the sister page with the closest boundary — for the production-and-accumulation side, defer to it; this page covers only needs and life.
- [Genre Handbooks · Dating Sim](../dating-sim/README.md) (Volume 4): the deep-dive version of relationship systems — for affinity and event-triggering details, defer to it.
- Homework: without touching an engine, lay out one person's day in a spreadsheet — 5 needs, 10 actions, 16 waking hours a day; hand-calculate both a "living well" and a "falling apart" arrangement, then decide whether to build that 6–8 week prototype.
