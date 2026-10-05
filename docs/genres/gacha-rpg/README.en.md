# Ludo Atlas · Genre Handbooks · Gacha RPG

> **Genre Handbooks · Volume 4**. Positioning: a raising RPG built on the three rings of collecting characters, raising characters and fielding teams in combat, with pulls from gacha banners as the collection method; content is supplied on a rolling version cadence, and long-term live ops are part of the product form.
> Companions: Game Design Handbook (core loops and probability numbers) · Programming Handbook (data-driven design and resolution) · Live-Ops & Growth (long-term cadence and monetization ethics) · Legal, Patents & Competition (odds disclosure and publishing compliance).
> This page carries no external links; benchmark titles are widely known works only, and the figures here are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: gacha RPG is the raising RPG that **packs the three rings — collecting, raising and team building — into a single character pool**. Gacha decides who you own, raising decides who gets stronger, and team building decides who takes the field to solve the problem; all three rings share the same cast of character assets and feed one another ammunition.

The core loop, written as a verb cycle: `save resources → pull to collect → invest in raising → field a team → resolve rewards → back to saving resources`. The loop rolls forward with the version as its long-term unit: one pull is an emotional peak lasting seconds, one raising investment is a plan spanning days, one version is a wait of weeks and its payoff.

| Ring | What the player is doing | Where the stickiness comes from |
| --- | --- | --- |
| Collecting | Saving pull currency, pulling, filling the collection and affinity | The pull of new characters; the closeness of "just a few more pulls" |
| Raising | Leveling up, upgrading skills, farming gear, unlocking story | The ownership that comes from investment; visible growth in power and content |
| Team building | Assembling teams, clearing dungeons and the main story, adjusting roles | Where raising results get verified; the itch to "swap someone in and try" and solve the puzzle |

The three rings are each other's ammunition: collecting supplies raising with raw material (new characters to raise), raising supplies team building with strength (someone who can take the field and clear the stage), and team building supplies collecting with reasons (when you can't win and want a different solution, you start wanting new characters and more power). Let any one ring collapse and the other two lose their meaning: without team-building depth, gacha degenerates into stamp collecting; without raising investment, pulled characters just lie in the warehouse; without collection pressure, team building degenerates into pure stat comparison.

Drawing boundaries against neighboring genres:

| Neighboring genre | Boundary |
| --- | --- |
| Creature collector | Its collectibles are obtained through exploration and capture, and individuals can be traded; gacha RPG characters come from banners, and narrative, staging and character design are what sell them |
| Trading card game | Cards come from the same source as pack opening, but opponents are real people and decks are settled before the match; gacha RPGs are mostly PvE, and team building revolves around roles and counters |
| JRPG | Fixed parties and content that concludes once and for all; gacha RPGs treat characters as continuously updated merchandise, with balance and content rolling out by version |
| Idle incremental | Idle growth runs itself on time; in a gacha RPG growth demands the player's active decisions and investment, and time is only one resource of several |

A self-check question: replace the banners and the three rings with "a fixed party plus a linear clear" — how much fun is left? If the answer is "hardly any", you are making a gacha RPG; if the answer is "still fun", you may be making a traditional RPG, where gacha is only the monetization layer.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Character appeal**: the motivation to pull comes from the character itself (personality design, character art, voice acting, story status), with power a distant second. No matter how generous the odds, a banner whose characters don't land won't retain anyone.
2. **A gacha you can do the math on**: pity progress visible, odds and rules disclosed, duplicates with a destination; when players can work out "the worst case is this many pulls away", waiting becomes saving instead of torment.
3. **Visible returns on raising**: invested resources convert into visible power and content (a skill that changes quality, new voice lines, new staging), not a pure percentage bump.
4. **Solution space in team building**: roles and counters let different lineups clear different stages, raising results get a proving ground, and guides have something worth discussing.
5. **Long-term anticipation**: every version brings new characters, new story and new gameplay, so players always hold the next goal in hand.

Negative feelings (any one of these is a red light): a pity track with no visible end and no way to calculate how many pulls remain; a character you raised for a month being completely outclassed by a new release; a daily loop that feels like clocking in for work.

Benchmark titles (a widely known list; play each by hand before breaking it down):

| Title | What to learn from it |
| --- | --- |
| Genshin Impact | The open world plus character banners combination; its disclosure standards for pity and cross-banner rules; a version-driven event update engine |
| Fate/Grand Order | Story and character writing as the biggest selling point: card art, Noble Phantasm staging and main-story updates forming a long-term pull |
| Arknights | The marriage of tower-defense combat and operator collection; restrained power creep; event storytelling and a rerun rhythm |
| Honkai: Star Rail | The lighter-weight turn-based combat; the role (Path) system; a guaranteed early-game growth track |
| Onmyoji | The paradigm of Chinese card RPGs: a long-term loop of Soul farming, guilds and live event operations |
| Umamusume: Pretty Derby | The layering of single-run training and banners: training scenarios, support cards and major races, three goal layers feeding one another |

What players expect from this genre by default: transparent odds and pity rules, pull history they can check, duplicates with a conversion outlet, a manageable daily burden, and events they can catch up on. Miss any one and bad reviews and churn arrive together.

## 3. Design Essentials

### 3.1 The Three-Ring Structure: Characters Are the Only Currency

Collecting, raising and team building all revolve around the same cast of characters, so a character's design dimensions must be thought through in one pass:

| Dimension | The question it answers | Common practice |
| --- | --- | --- |
| Looks | Why the player wants them at first sight | Character art or a model, expression variants, signature staging |
| Combat role | What problem they solve in the team | Damage, tank, healer, support, control — each character holds at least one post |
| Personality and narrative | Why players remember and like them | Trait tags, relationship networks, character-specific story and voice lines |
| Acquisition and rarity | At what cost you acquire them | Rarity tiers tied to the banner schedule |

A character with these four out of alignment won't sell: great art but homogenized skills, and players bench them right after the pull; good mechanics but a flat personality, and community discussion and fan works never take off. There is only one acceptance question for a character: will players pay for owning her as such, and not just for her power?

Pick two or three raising tracks by priority and polish them — stacking them all will blow past what players can keep account of:

| Raising track | Common forms | Its job |
| --- | --- | --- |
| Level and ascension | EXP items, ascension materials, weekly dungeons | The numeric chassis and progress checkpoints |
| Skills | Upgrade materials, signature skills | The points where mechanics and multipliers transform |
| Gear or stat rolls | Random-affix gear, signature weapons | The long-term farming loop and headroom for the cap |
| Affinity and bonds | Gifts, taking characters along, character-specific story | Emotional payback and the fulfillment of character content |

Design an outlet for duplicates up front: the value gap between a first copy and a repeat (converted into shards, star-up materials or a dedicated currency) is the shock absorber of the gacha experience and the goal structure of long-term collecting.

### 3.2 Banners and Odds Design: Structure, Pity and Disclosure

Banner structure and odds methods:

- Banner tiers: standard, limited and beginner banners, plus gear or weapon banners where needed; limited banners use a featured rate-up (UP) to create their window, and reruns fill the gaps.
- Odds work in two layers: base rates handle rarity tiers, pity handles the worst case. Hard pity guarantees the drop once the counter hits its cap; soft pity ramps the odds up as the cap approaches; rules like "miss this one and the next is guaranteed" trade certainty for a sense of fairness and have become the mainstream approach in recent years.
- Calculate expected value before you use it: balance business and experience on expectations and distributions (not single-point probabilities), and rerun the simulation every time you change a parameter (tools in §4).
- Pity must be calculable and continuous: players can work out the worst case; whether the pity counter carries over between banners, and across which ones, is written down and fixed in stone.

Compliance baseline (the floor; the full expansion is in the Legal, Patents & Competition handbook):

- Disclosing odds and pity is a hard requirement: the names, attributes, probabilities and pity rules of pullable items are disclosed truthfully, disclosure matches reality, and nothing is changed quietly.
- Pull records are checkable and auditable: the server keeps the full pull history, players can view it, and support tickets can be traced back.
- When going overseas, check market by market: some overseas markets have strict rulings and restrictions on randomized paid mechanics (loot boxes) — do not assume one scheme travels globally.

Design discipline: duplicates have an outlet — don't let "another duplicate" become pure waste; free players can save up to pity through time and planning, which is the retention floor. The actual numbers for odds and pity are derived from simulation and the business model; this page covers structure and discipline only.

### 3.3 Stamina and the Long-Term Economy: The Pacing Valve

Stamina (action points) is the throttle on content consumption, doing three things at once: governing the pace of progress, buying time for content production, and providing a monetization point. Design it to serve pacing, not to lock motivated players outside:

- Buffer it: overflow storage, mail deliveries, weekly resupply — avoid the frustration of "logging in late costs you".
- Offer choices: stamina goes into several lines (main story, materials, events) so players make priority trade-offs instead of mindlessly draining the bar.
- Enable catch-up: event and dungeon windows are wide enough for latecomers, and reruns plus permanent availability are low-cost catch-up channels.

The economy has three ledgers: currency (free hard currency and paid currency), pull resources (tickets and their currency equivalents) and raising materials; put all three layers' income and spending into tables before discussing release pacing.

Power creep is the largest long-term debt a gacha product carries: new characters offer freshness through mechanical differences and complementary roles, not through bigger multipliers; reruns, buffs and rebalancing keep the value of veterans' rosters intact. The long-term cadence rotates through four things: version updates, the event schedule, dailies and weeklies, and rotating gameplay; how to watch retention and payment metrics and how to lay out events are covered in the Live-Ops & Growth handbook. The standard for monetization ethics also comes from Live-Ops & Growth: charge for love, not for anxiety.

### 3.4 The Content Engine: Story Events and Version Updates

For a long-running product the lifeline is content throughput, not first-package quality. Every version ships a set of "new characters plus new story plus a new mode or event plus new rewards":

- Story events carry the bulk of the text and serve both character building and banner promotion; their structure typically has three parts: a story stretch, a battle-challenge stretch and a reward settlement stretch. Time-limited modes adjust the rhythm, while reruns refill the schedule at low cost and let new players who missed them catch up.
- Decouple characters from events: an event doesn't bind to a single character, a character's window doesn't bind to a single mode, so a delay on either side doesn't cascade.
- Throughput discipline: develop several versions in parallel with one or two versions of buffer in reserve; work out how many characters and how much story your team can steadily deliver per month, and set the version cycle accordingly (scheduling methods in the Production Handbook).
- When the story stops updating or its quality slips, the banner's appeal slides with it; conversely, character popularity feeds back into story and community content — the two ends share one rope.

### 3.5 Shipping Reality: Publishing and Compliance Up Front

The gacha format raises publishing complexity by an order of magnitude; the following must be reviewed at greenlight (full processes and material checklists are in the Multi-platform Launch Playbook):

- Game license: every formal commercial channel in mainland China (app stores, mini-game virtual payments, domestic PC platforms) requires one; approval timelines are unpredictable, the wait must be built into the schedule, and being finished does not mean you can launch.
- Real-name and anti-addiction: integrating real-name verification and a minors-protection system is a hard listing requirement; the rules for play windows, play time and spending limits follow each channel's latest policies.
- Odds disclosure and overseas differences: the disclosure duty for randomized pulls (§3.2) is part of the compliance floor for launch; overseas platforms don't go through the game-license system, but they do need ratings and local-law compliance, and randomized-payment regulation must be checked market by market.

The reality for small teams: every item above points to ongoing compliance and live-ops investment. The more realistic form is to first build a single-player version of manageable scope (gacha as gameplay, not as monetization), validate that the three rings hold, and only then decide whether to enter the live-service track.

## 4. Technical Essentials

The engineering difficulty concentrates in four places: server authority, data-driven design, reproducible odds and the content pipeline. General methods are in the Programming Handbook; the full multiplayer and backend pipeline is in the Multiplayer & Backend handbook.

**Server authority and resolution**

- Pull results are decided by the server and written to the database immediately; the client only handles presentation. Any "send to the client first, record later" implementation becomes an exploit for farming pulls and resources.
- A pull is one transaction: deduct resources, roll the result, grant the items, write the log — four steps, atomized; requests are idempotent so a reconnect neither double-charges nor loses a result. Audit capability from day one: pull records, resource ledgers, support compensation and rollback tools, and a pull-history view on the player side.

**Data-driven design and config**

- Characters, skills, banners and events are all managed in external tables, with only formulas and flow left in code; config validation goes into CI so a bad table can't ship sick. Banner schedules and odds parameters are live-ops config that switches without a client update, and every change is logged and reviewed so "quiet config edits" don't become incidents.

**Reproducible odds and simulation**

- RNG is seedable and reproducible: every pull records its seed and pity count so support tickets and bugs can be replayed; a Monte Carlo tool runs millions of samples per parameter change, outputs expectation, pity distribution and edge cases, and reruns on every table edit — it is the acceptance tool for odds design.
- Live monitoring: if the actual drop distribution doesn't match the config, that's an incident; abnormal pull behavior (scripted activity, anomalous drops) goes on the watchlist.

**Content and asset pipelines**

- Character assets (art, models, voice, staging) ship in bundles and download on demand, with the first package and incremental packages' boundary designed up front; event toggles and banner switches are timed by the server with assets pre-embedded in the client, and minute-precise launch times must enter the pipeline early.
- Layer staging and resolution: settle the result first, then play the animation; skip and fast-forward affect playback only, never the result.

For a free single-player version (gacha as gameplay), you can skip the server, but saves must resist tampering; the moment real-money payment enters, server authority is mandatory — there is no middle ground.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for scope estimation only — not a commitment.

| Project form | Content scale | Time reference | Notes |
| --- | --- | --- | --- |
| Three-ring prototype | 1 banner, 8–12 characters, 5–8 stages | 4–8 weeks | Fully local, zero art; validates gacha, raising and team building only |
| Small single-player scope | 15–25 characters, one main storyline, premium | 6–12 months (small team) | Gacha is gameplay, not monetization; light compliance burden |
| Small live-service scope | 30–60 characters, 1–2 new characters per version | 1–2 years and up, ongoing investment | The content pipeline, servers and live ops are the bulk |
| Top-tier scope | 100+ characters, multi-region release | Years with a full team | A heavily capitalized live-service project; read §3.5 before benchmarking against it |

Per-character unit cost (rough): a full character is a cross-discipline delivery — art (illustration or model, variants), combat (skills and numbers), staging (ultimate animation), voice, story text, testing and localization, none of which can be skipped; a 2D card-art character typically takes weeks, a high-quality 3D character months with several disciplines working in parallel. Reusable components and templates lower the cost, but the staging and art investment on high-rarity characters cannot be squeezed out.

A cost-structure reminder: gacha RPG is a live-service product where development is only one part; the other half is ongoing content production, servers, support and community investment. Write the budget for "steady output every month after launch", not for "done and dusted". Scope discipline: back-calculate launch character count and version cycle from capacity, never from ambition.

## 6. How to Start the First Prototype

Goal: 4–6 weeks to a minimal loop that "can pull, can raise, can fight, can do the math". Fully local, zero art, no servers and no real money.

1. Week 1: the gacha skeleton. 8–12 placeholder characters and one banner (base-rate tiers plus a pity counter and soft pity); the pull presentation starts as one-by-one reveals; settle the result first, then play it, and log everything.
2. Week 2: team combat. Pick the simplest battle form (turn-based or semi-auto), 3–4 character teams, role slots plus one counter relationship; the acceptance question is "does swapping someone in solve the problem".
3. Week 3: raising and resources. Two or three raising tracks and an income/spending table for stamina and materials; run a simulated "one week" and check whether the progress curve is steep or flat.
4. Weeks 4–6: miniature content, playtesting and tuning. Build 5–8 stages plus a proto-event, get 5 people who have never played it to play for two or three days, and record the emotional curve of pulling and any team adjustments; then run the simulation scripts for expectation and pity distributions, tune parameters against the playtest records, and decide whether to move into networking and art investment.

Success criteria (all observable):

- Testers can clearly state "how many pulls away the worst case is", and the pity structure is calculable.
- With art and audio stripped out, testers still actively save resources toward their next pull, and single sessions run past 30 minutes.
- At least 3 of 5 testers voluntarily adjusted their team and can explain why.
- Change any probability or pity parameter, and within 10 minutes you can read its effect on expectation and experience from the simulation and logs.
- Testers' reaction to duplicates is not pure frustration; the conversion mechanic works.

Not in the prototype: servers, payments, real money, anti-addiction integration, multiple languages. Those are launch engineering, not gameplay validation; if the three rings don't hold, fix the rings first.

## 7. Common Pitfalls

1. **Black-box odds, quiet changes, incalculable pity**: disclosure doesn't match reality and pity rules are vague, so players can't work out the worst case. Avoidance: fix the disclosure in writing, keep records auditable, show the counter, and state cross-banner carryover explicitly (§3.2, §4).
2. **Runaway power creep**: every version's new character is the new god, and veterans' rosters turn into scrap paper. Avoidance: prioritize mechanical differences over bigger multipliers, with reruns and buffs as the floor (§3.3).
3. **Raising tracks piled up**: level, ascension, skills, gear, signature weapon and affinity all stacked to the ceiling, and players give up because they can't keep the accounts straight. Avoidance: polish two or three tracks first and add layers by the priority order in §3.1.
4. **Stamina as a lockout gate**: players want to play but can't, and core players are locked outside. Avoidance: stamina serves pacing, with buffer, choice and catch-up mechanics (§3.3).
5. **Content supply cuts out**: after launch, throughput can't keep up and content droughts drag retention down. Avoidance: version buffers and event reruns; set capacity first, then the version cycle (§3.4, §5).
6. **Piling on numbers with no presentation**: pulls, ultimates and rewards land with zero expression, and emotion has nowhere to land. Avoidance: give the pull presentation and key skill staging their own budget (Art & Audio Handbook).
7. **Duplicates with no outlet**: pulling a repeat is pure waste and negative feeling piles up. Avoidance: conversion mechanics such as shards, star-up materials and exchange currency (§3.2).
8. **Team building with no depth**: auto-battle plus power-rating stomps, and gacha and raising lose their proving ground. Avoidance: solution space from roles and counters, with stages that ask "you must swap someone in" (§3.1).
9. **Compliance and publishing bolted on late**: half-way through, you realize the game license, anti-addiction and odds disclosure were never prepared. Avoidance: walk the §3.5 checklist at greenlight (Legal, Patents & Competition, Multi-platform Launch Playbook).
10. **A small team benchmarking top-tier scope**: characters, story and events laid out at a top-tier cadence, and none of it gets finished. Avoidance: ship a complete product at manageable scope first, then talk about going live-service (§5).

## Further Reading

- [Game Design Handbook](../../fundamentals/game-design/README.md): the general methods for core loops, numeric tables and probability design — the base document for §1 and §3.
- [Programming Handbook](../../fundamentals/programming/README.md): implementation details for data-driven design, layered resolution and hot updates; pairs with §4.
- [Multiplayer & Backend](../../pipelines/multiplayer-backend/README.md): the full account of server authority, economy auditing and anti-cheat; required reading before building online gacha.
- [Live-Ops & Growth](../../publishing/live-ops/README.md): retention, event scheduling and monetization ethics — the expansion of §3.3.
- [Legal, Patents & Competition](../../publishing/legal/README.md): odds disclosure, game licenses and overseas regulatory standards — the basis for §3.2 and §3.5.
- [Multi-platform Launch Playbook](../../../playbooks/platform-launch/README.md): the game-license, real-name and anti-addiction processes specific to online games — the full expansion of §3.5.
- [Art & Audio Handbook](../../fundamentals/art-audio/README.md): specs and pipelines for character art, models and staging assets; pairs with §3.1 and §7.
- [Production Handbook](../../fundamentals/production/README.md): scheduling and estimation methods for the content pipeline; pairs with §3.4 and §5.
- [Pitfalls & Anti-patterns](../../pitfalls/README.md): numbers and content-production pitfalls — read against §7.
- [Genre Handbooks · Creature Collector](../creature-collector/README.md) and [Genre Handbooks · Trading Card Game (TCG)](../card-game-tcg/README.md): two sister lines, collection-and-raising and banner economy; read against §1 and §3.
- Homework: build a paper gacha model in a spreadsheet — 8 characters and one banner with pity — and hand-calculate expectation and the worst case; then have a friend "pull for ten days" against the model and record which pulls his emotional peaks land on.
