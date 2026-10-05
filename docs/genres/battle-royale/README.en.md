# Ludo Atlas · Genre Handbooks · Battle Royale

> **Genre Handbooks · Volume 3**. Positioning: the genre that makes "dozens to a hundred players in one match, with a single winner" the core experience. Dropping and picking a landing spot, looting and growing stronger, the forced encounters of the shrinking circle and the final showdown string together into a ten-to-thirty-minute survival script per match; this page covers the genre formula, safe-zone pacing, the in-match economy, the networking hard threshold, cold start and how to begin the prototype.
> Companions: Game Design Handbook (core loops and balance) · Programming Handbook (networking fundamentals and performance) · Multiplayer & Backend (the full path of synchronization, matchmaking and backend) · Indie Survival (scope and scheduling).
> Division of labor: sync models, matchmaking, anti-cheat and server costs are fully the territory of Multiplayer & Backend; this page accounts only for the gameplay side — and whether you can afford to build it.

---

## 1. Positioning and Core Loop

One-line positioning: battle royale is the genre that **compresses survival competition into a single match**. Dozens to a hundred players drop into the same map, start with nothing and loot to arm themselves, and are forced into each other's path by a continuously shrinking safe zone (which the community calls the "poison circle"); elimination means you are out, the last surviving player or squad wins, and everyone starts over next match.

Family position: this repository files it under the shooter family, but its skeleton is really a **single-match elimination format container** that has nothing to do with theme or weapons. Melee weapons (Naraka: Bladepoint), building (Fortnite) and hero abilities (Apex Legends) have all proven the same thing: you can load any combat content into it and the skeleton does not change. Gun feel and hit feedback share their roots with the FPS page in the Genre Handbooks; map scale and rotation pacing sit closer to the survival genre.

The core loop, written as a cycle of verbs:

`Drop and pick a landing spot → Loot and grow → Rotate and clash → Circle shrinks and redistributes → Showdown in the final circle → Settle and requeue`

This loop runs in units of one match; a match commonly lasts 15–30 minutes (reference). It rests on only two preconditions: information about landing spots and resources must be readable (§3.1, §3.2), and the cost of elimination must be acceptable (§3.3).

Each of the genre formula's four links solves one problem; this is the skeleton of the whole page:

| Link | What the player is doing | Problem it solves | What breaks without it |
| --- | --- | --- | --- |
| Drop | Read the flight path, pick a landing spot, decide where to take the risk | Spreads players across the map so no two openings are alike | Fixed spawn points make openings formulaic, and only a corner of the map ever gets used |
| Loot | Search for supplies, gear up, stockpile resources | Creates the curve from "having nothing" to "combat-ready", with its risk trade-offs | Fully geared from the start; the early-match tension disappears entirely |
| Circle shrink | Being pushed along by the safe zone, planning rotation routes | Forces encounters and redistribution; puts a timer on the match | Players can hide in place and matches drag on forever |
| Showdown | Fighting it out inside the final circle | Delivers a definite ending and a single winner | Placement cannot be settled and the match has no narrative landing point |

Beyond the four links there is one invisible rule: **no respawns**. Elimination means leaving the match, and this decides the scarcity of the in-match economy (§3.2), the weight of the death experience (§3.3) and the necessity of a spectating system. Two product routes sit on the same skeleton: the realistic-survival route (scarce supplies, short time-to-kill, high weight on vehicles and terrain) and the hero-competitive route (abilities, respawns, fast pace, fewer players); game feel, player count and live-ops structure all differ, so pick one route at kickoff and take it all the way.

Drawing boundaries with neighboring genres:

| Neighboring genre | Boundary |
| --- | --- |
| Team competitive shooter | Fixed spawns, unlimited respawns, settled by score; battle royale gives you one life and settles by survival placement |
| Extraction shooter | Both are "enter the map, loot, weigh the risks"; an extraction shooter aims to carry loot out and accumulate it across matches, while battle royale resets everything inside the match and asks only that you survive to the end |
| Survival-crafting | Long-term survival in a persistent world; battle royale is a one-match world and a one-match life, and when it ends you carry out only meta accounts like seasonal points |
| Social deduction | Also a contest among strangers for "who survives to the end", but with no combat or map control — the outcome comes down to a vote |
| MMO | Both are about "many players in one space"; an MMO is a continuously co-inhabited world, while battle royale starts fresh among strangers every match |

A self-check question: if you removed the safe zone, would the game still stand? If it would, you are making an open-world survival shooter, not a battle royale.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **The tension of landing**: the first five minutes are the game's peak of pressure — no weapon, footsteps everywhere, a gun possibly behind every door. This opening pressure is unique to battle royale.
2. **The payoff of the search**: every door you open can change your fate; the risk-and-reward of hot zones makes "where to grow" the first real decision of a match.
3. **Stories told under the shrinking circle**: my route, my narrow win, how I escaped death — after a match you can tell it as a story, and this is the genre's biggest social currency.
4. **Comeback highlights**: fighting many alone, clutching a kill at low HP, winning the final gunfight in the deciding circle; the density of highlights decides whether players will recommend the game to others.
5. **Placement progress**: from "can make top 50" to "consistently top 10" and then to a "chicken dinner" — the community's term for winning, and the nickname the genre itself goes by — the steps are clear with visible progress at every level.

Benchmark titles (play at least 20 matches before taking them apart; the psychology of a single match only clicks once you are in it):

| Title | What to learn from it |
| --- | --- |
| PUBG | The realistic-survival baseline: a hundred players per match, scarce supplies, high weight on vehicles and terrain; its mod origins (ARMA) proved the single-match elimination format can stand alone as a genre |
| Fortnite | Building as a second combat language; free-to-play plus cross-play flatten the threshold; seasonal passes and cultural events turned BR into a venue for long-term live-ops |
| Apex Legends | Three-person squads with hero abilities; ping communication lets teams play without voice chat; its 60-player matches proved player counts can go down and pacing can speed up |
| Call of Duty: Warzone | A free standalone client; the cash-and-buy-station economy and the Gulag respawn mechanic turn the death penalty into layered design |
| Game for Peace | The mobile flagship: simplified controls, low-spec adaptation, the social graph and compliant operations — a complete sample of the mainland publishing path |
| Naraka: Bladepoint | Melee weapons and grapple movement proved the BR skeleton does not care about theme; its 60-player matches replace gun-line duels with close-combat play |

Common ground: map, shrinking circle and single-match elimination are the shared foundation, and the differences are in combat language, player count and live-ops shape. Competition at the top has moved to content updates and esports operations, which connects directly to the small-team accounting in §5.

## 3. Design Essentials

### 3.1 Map and Circle Pacing (Safe-Zone Design)

Map size is derived from player density: players per match multiplied by a single player's control radius roughly equals the map area. Realistic large maps for the hundred-player format commonly span 4×4 to 8×8 km, and small lobbies (20–40 players) can shrink to a few square kilometers (reference magnitudes, calibrated by movement speed and encounter density). However large the map, the gameplay center of gravity is still just "rotating from A to B"; piling up art for area is the worst return on investment in the genre.

POI tiering is the first design tool: high-resource hot spots (central districts, military facilities) come with high risk, edge wilderness with low risk, and several transition points in between. The number of hot spots, together with the flight path, decides the opening distribution of each match; the community spontaneously nicknaming locations and forming a landing-spot culture is a signal of successful map design. The flight path is randomized each match, but the randomness must be controlled: both sides of the path should offer spots worth dropping into, avoiding entire dead zones. Variations like dual flight paths and gradually shifting paths can wait for the second version.

The safe zone is the match's timer, advancing in phases (reference magnitudes, calibrated to your own movement speed and map size):

| Phase | Wait and shrink window | Out-of-zone damage | Design intent |
| --- | --- | --- | --- |
| First circle announcement | 60–120 seconds after landing | Near zero; a reminder only | Guidance only, almost no punishment, a generous window to grow |
| Mid circles (2–4) | Each circle faster, gaps shorter | Rising step by step to single digits per second | Create the first large-scale rotation and encounter |
| Final circles (last 2–3) | Shrink windows compressed to around 30 seconds | Raised to double digits per second | End the stalling, force the showdown |

Three tuning disciplines:

- Circle speed is tied to player movement speed: normal running must be enough to make the zone, but only just; vehicles and terrain are the variables that let players do the math on "run for the circle or tank the circle".
- Circle-center drift must be controlled: the next circle's center is confined to a reasonable range inside the current circle. A small drift creates rotations; a big jump creates misery; an extreme shift across half the map is an incident.
- Final circles must pass a terrain review: the last two or three circles must land on ground with a gradient of cover and room to move, avoiding water-logged dead ends and pure open field. A final that randomly lands in open wilderness is a lottery — at acceptance time, sample 30+ matches and tally the terrain distribution.

Rotation channels are the second review item: at least two viable routes between major districts; bridges and chokepoints can be made into "toll booths", but the whole map cannot have a single lifeline, or mid- and late-game encounters degenerate into standing in line. Checklist: when the first circle closes, does every player have a viable route in? How did the final-circle terrain sampling turn out? Is the share of deaths to the circle among all eliminations kept in check (share too high means circle speed or terrain has a problem)?

### 3.2 Loot, Gear and Vehicle Economy

The in-match economy has exactly one goal: keep "where to loot, how long to loot, when to leave" generating decisions. The scarcer the resources, the heavier the decisions; the more abundant, the more combat resembles a standard shooter.

| Category | Design role | Tuning knobs | Common pitfall |
| --- | --- | --- | --- |
| Weapons | Define engagement distances and match pacing | Damage, fire rate, ballistics, rarity weights | A brainless overpowered gun that "wins on pickup" makes looting decisions collapse |
| Armor | Leave tolerance for both the first mover and the latecomer | Tier, damage reduction, durability | When the tier gap is too wide, skill cannot overcome gear |
| Consumables | Sustain and comeback resources | Count, heal amount, use time | Too much healing lets players tank the circle forever and matches never end |
| Vehicles | Rotation, temporary cover, a noise source | Speed, durability, fuel, spawn density | Vehicles over-weaponized into mobile killing machines |
| Airdrops | Create public events and route choices | Drop schedule, landing spots, content list | Content too random; top-tier gear decides the match at the start |

- Landing guarantees: any landing area must guarantee a usable weapon within a short time. Being hunted while empty-handed by a fully geared player is the cheapest possible source of bad reviews.
- The airdrop is the second movement order besides the shrinking circle: a scheduled public event at a fixed location draws players from across the map toward one point, creating conflict and stories; the contents must be worth the risk, or nobody goes.

Vehicles should make the map "smaller": they offset the rotation cost of a large map and are part of the circle-pacing package; they also serve as mobile cover and noise sources, changing the shape of encounters. Tune the three knobs — speed, durability and terrain adaptability — separately; do not run everything on one parameter set. The reward ratio between fighting and looting is this economy's master switch: if only kills make you stronger, the whole lobby fights and abandons looting; if only looting makes you stronger, everyone hides until the final circle; the common approach is to give both — kills supply ammo and armor, looting provides weapons and key items. Checklist: is there a weapon guarantee in the first three minutes? Would you dare enter a hot zone empty-handed? Are vehicles a necessity or optional decoration? Does an airdrop trigger at least one multi-player contest per match (verify by spectating or with data)?

### 3.3 Elimination, Spectating and the Next Match (Death Experience)

With no respawns, the death experience is this genre's most important retention funnel: every minute after a player is eliminated decides whether they stay or quit.

- At the moment of elimination, deliver complete information: the killer's viewpoint, the source of damage, the kill distance. Without a post-mortem, players put the blame on the system and on cheaters.
- Immediately after elimination, hand over the next step: squad spectating, fast settlement, one-click requeue, with the goal of getting from elimination to the next drop in under 60 seconds; the results screen is the stage for review — placement, kills, damage and rotation distance tell the match's story on one screen, with "one more match" placed where the hand falls naturally.
- In squad modes, elimination is "the squad loses a member", not "the individual goes bankrupt": while teammates are still fighting, spectating must carry informational value; respawn mechanics (designs like Warzone's Gulag or Apex Legends' respawn beacons) are the leniency option, at the cost of softening the elimination format's hardness — whether to include them depends on your positioning.

Checklist: how long on average before an eliminated player starts the next match? Does spectating carry informational value? Is anyone leaving voice chat early because there is "nothing to do after dying"?

### 3.4 Player Count, Matchmaking and the Boundaries of AI Filling

The player count per match is BR's first parameter, and it decides map size and the circle table in reverse: a circle table built for 100 players placed in a 30-player match leaves the mid and late game absurdly empty; the density of 30 players stuffed into a 100-player match means encounters everywhere. Fix the player count first, then the map and circle table. Around 60 players is the common choice for the small-lobby tier (the tier Apex Legends and Naraka share), where encounter density is easier to control.

Matchmaking's hard problems are cold start and off-peak hours: a new game's launch, late-night windows and unpopular regions can all fail to fill a lobby; countermeasures ordered from low to high cost: flexible starts (e.g. a 100-player lobby opens at 60, with faster circle pacing compensating for density), time-and-region pooling (aggregating players into the same windows and nearby regions), AI filling (bots making up numbers and speeding up lobby starts during off-peak); pool splitting and wait times must be designed together — pools for newcomers, squads and rank tiers are all necessary, but split the pools too finely and the population is diluted until everyone waits (the matchmaking checklist in Multiplayer & Backend §4).

The boundaries of AI filling must be spelled out; this is a trust red line:

- Allowed: training matches, a newcomer's first several matches, off-peak fill-ins. The principle is "save the experience, do not deceive" — as Multiplayer & Backend §4 puts it: bot fill-ins can save the experience, but expectations must be managed so players never feel deceived.
- Not allowed: dressing bots up as "high-skill lobbies" to encourage spending; letting players discover their opponents are AI at the highlight moment of a rank-up or a championship. The moment competitive honor is proven false, the product's credibility is overdrawn.
- Ratios, behavior and disclosure must all be restrained: cap the share; bots must not perform superhuman plays (pre-aiming through smoke, perfect recoil control and the like) — an exposed AI taints the feel of real matches as well; write which modes, which hours and what ratio into the rules description: you may hide details, but you may not lie.

Three acceptance questions for cold start: what is the upper limit on matchmaking waits during off-peak hours? What are the bot-share cap and disclosure policy? In what context does a player first encounter an obvious bot match (training, off-peak, or beginner protection)? These three answers decide your first month's reputation.

## 4. Technical Essentials

### 4.1 The Networking Hard Threshold

Battle royale falls into the "competitive match (8–100 players)" tier; per the tiering in Multiplayer & Backend, there is no suspense at this tier: dedicated servers plus server-authoritative simulation. P2P and host authority lose on both cheat boundaries and sync quality — do not choose them. It shares the same synchronization stack as FPS (Multiplayer & Backend §2), and BR must additionally hold up four points:

- Interest management: synchronize only nearby players and objects, with distant updates throttled; write per-client bandwidth, tick rate (reference: commonly 20–60Hz) and per-frame entity budgets into the performance spec — do not wait for load testing to find out you cannot hold up.
- Hit detection: a player's shot must hit the target they see, which rests on server-side rewind (lag compensation); without it, "I clearly hit them and dealt no damage" happens every day and trust will not survive a week.
- Vehicle synchronization: vehicle and passenger state, physics and transfer timing are all server-authoritative, or you get "I am still on the vehicle, but you see me already off it".
- Reconnection: mobile network drops are the norm, and reconnecting into the original match should feel like nothing happened (the checklist in Multiplayer & Backend §9). Decoupling logic frames from render frames and layering the network layer away from game logic are two engineering iron laws; violate either and late-stage game feel tuning means starting over.

### 4.2 Large World and Client Performance

- Large maps rely on streaming: chunk the world, load and unload incrementally by distance; the render distance of distant grass and fog effects must pass a fairness review — machines of different tiers must "see the same fight", fairness before saving money; the number of visible entities far exceeds a conventional shooter, so tier player models, vehicles and dropped items into update levels and object pools, and throttle audio channels, with footsteps and gunshots at the highest priority because hearing is a core information channel.
- Mobile runs a different set of books: dynamic resolution, and the trade-off between heat and frame rate; touch-screen simplifications (auto-pickup, simplified inventory, aim assist) need interactions designed separately — they are not feature cuts.

### 4.3 Servers, Anti-Cheat and Cost

- Service layering follows the checklist in Multiplayer & Backend §3: one instance per match on the game servers, with scaling constrained by "a match must play out to the end" (Multiplayer & Backend §8); the cost model comes before the business model — peak CCU multiplied by per-match resource usage, plus bandwidth and labor, put into a spreadsheet before discussing scale; the server specs and counts for hundred-player matches are no rounding error, and this accounting belongs in the kickoff document.
- Anti-cheat is the highest-leverage investment in this genre: one cheater destroys a 100-player match experience (Multiplayer & Backend §7); all three layers — client detection, server-side behavior analysis and report review — must be present, with the server-side analysis layer live from day one and ban and appeal channels prepared alongside. Spectating, replay and evidence share one source: match viewpoints, death replays and report data all come from the same server-side record, so build the hooks early and there is no catch-up work when you go esports.

## 5. Content Volume and Workload Reference

The following are common magnitudes for projects of this kind, used for scope estimation and constituting no promise. Numbers are a ruler, not a promise; calibrate with your own team's speed.

| Form | Content magnitude | Timeline magnitude | Team magnitude |
| --- | --- | --- | --- |
| Small-lobby prototype (20–30 players, one greybox map) | One whitebox map of a few square kilometers plus one circle table | 2–4 months | 3–6 people |
| Shippable small-lobby BR (up to 60 players) | 1–2 finished maps plus a basic season structure | 1–2 years | 10–20 people |
| Mainstream-scale BR | Multiple maps and a season pipeline | 2+ years for the first release, then a seasonal cycle | 50+ people |

Module-level accounting (reference):

| Module | Minimum playable | Comfortable scale | Notes |
| --- | --- | --- | --- |
| Map | 1 greybox map | 2–3 finished maps | The art volume of one large map is on par with all the scenes of a single-player title, and it must pass performance and fairness review twice |
| Weapons | 6–8 | 15–20 | Every weapon needs a clear engagement-distance identity; no stat clones |
| Vehicles | 2–3 types | 5–8 types | Every vehicle is three systems: movement, cover and sound |
| Modes | 1 (solo and squad) | 3–4 | Each added mode re-tests every map and the whole balance pass |
| Season content | 1 basic battle pass | One season every 8–12 weeks | This is a pipeline, not a version number |

**The small team's reality check.** Put the following four bills on the table before deciding whether to build one: the server and ops bill rises linearly with peak CCU, per-match resource usage for hundred-player games is high, and there is no "closed for business" setting (Multiplayer & Backend §8); anti-cheat and customer support are standing costs in the most adversarial genre, and failing at them destroys retention outright (§4.3); the seasonal cadence of top products is backed by studio-scale output, and the content arms race cannot be won; cold start and off-peak both need bots and flexible mechanisms as a backstop (§3.4) — this is design debt, not a patch.

If the four bills add up to too much pressure, fallback options ordered by degree of compromise: a small-lobby BR (20–40 players, small map, fast pace); a themed BR (replace firearms with melee weapons, magic or vehicles and trade difference for room to live — Naraka has verified this); mechanical reuse (take only the "shrink plus elimination" mechanical skeleton into a PvE or single-player variant and remove the multiplayer cost entirely). Going head-on against top realistic BRs is one of the deepest competitive tracks there is; without multiplayer operations experience and steady content output, do not enter. Scheduling anchors: small-lobby prototype 2–4 months; vertical slice (one map at release quality plus a complete match) 6–12 months; extrapolate the launch version as "content scope times a polish factor", then keep investing season by season.

## 6. How to Start the First Prototype

The first prototype needs to validate exactly one thing: **whether this kind of match makes people want to drop again**. Do not touch 100 players at this scale — use a 20–30 player small lobby (fill with bots if real players are short) to run the skeleton end to end. Budget 4–8 weeks.

- **Weeks 1–2: offline single-match skeleton.** A greybox map of roughly 1 square kilometer, random spawns, pickup looting, the circle system (phases, durations, damage and drift all parameterized), elimination and settlement. Fill the lobby to 20–30 with bots and validate pacing and the circle table offline first.
- **Weeks 3–4: wire up multiplayer.** Start on an off-the-shelf backend (Multiplayer & Backend §5: all-in-one solutions like Nakama and Colyseus) and run 10–20-player matches with real players; server-authoritative movement and shooting, accepting lag and roughness for now, to validate "how people actually behave inside a match": where they drop, how long they loot, when they start fighting.
- **Weeks 5–6: the first map with a human feel, then tune parameters only.** Give landing-spot tiering, rotation channels and final-circle terrain one pass per §3.1; then pull 20–30 people (bots included) into custom matches and record the first-five-minute death rate, the share of deaths to the circle, and the kill and placement distributions. After that, change only parameters and layout, add no new systems, and watch eliminated players above all: do they stay to spectate or leave outright, and how long before they hit "one more match".

Success criteria (all observable):

- With all art and audio removed, testers still play match after match, a single session usually running over an hour; a match ends in around 15 minutes with real fighting in the last three circles, rather than two squads unknowingly hiding their way to the final.
- Eliminated testers can name their cause of death within 30 seconds (one of the four: an encounter, the circle, the terrain, a weapon gap).
- Change any single circle parameter and you can restart a match within 5 minutes and quantify its effect on match pacing.
- At least 4 out of 5 testers spontaneously ask for "one more match".

## 7. Common Pitfalls

1. **Scaling the player count before validating the match**: when the 100-player engineering goes up, the fun from drop to showdown has not been validated; with the order reversed, rework costs multiply by player count.
2. **Circle table mismatched to map size**: too large a map with too slow a circle becomes a wilderness hike; too fast and the whole match is spent running from the circle; derive the circle table from player movement speed (§3.1).
3. **No landing guarantee**: the frustration of being hunted empty-handed in the first minutes is the cheapest and most lethal; every landing area needs a weapon guarantee.
4. **Final circles without terrain review**: the last two circles randomly landing in open ground turn the final into a lottery; sample 30+ matches for terrain distribution.
5. **Death means exit**: nothing to do after elimination and a long chain from results back to a new match, and the funnel drains out at "the first kill" (§3.3).
6. **AI filling over the line**: runaway ratios or exposed fake-human bots collapse the core "real opponents" narrative; restrain the ratio and manage expectations (§3.4).
7. **Missing cheat governance**: BR has the highest cheating leverage, and one cheater ruins 100 players; the server-side analysis layer must exist from day one (§4.3).
8. **Costs pulled out of thin air**: the server bill rises linearly with popularity; build the cost model before setting scale (Multiplayer & Backend §8).
9. **Copying the top titles' seasonal arms race**: trading output with studios is a guaranteed loss for a small team; put differentiation in theme, mechanics or pacing, not update frequency.
10. **Homogeneous openings**: if even one of the three dimensions — flight path, loot, circle center — is fixed, players start rote-memorizing after fifty matches; randomize as a set.

Battle royale looks like it is selling drops and guns, but what it actually sells is a survival script that is never the same twice, and that "one more match" button on the results screen.

## Further Reading

- Game Design Handbook: core loops, number tables and validation methods — the source document behind the genre formula and the in-match economy.
- Multiplayer & Backend: the full expansion of §4 of this page — sync models (§2), matchmaking and off-peak filling (§4), anti-cheat (§7), cost and operations (§8).
- Indie Survival: scope and scheduling; before deciding to build a BR, read the four bills in §5 twice.
- Live-Ops & Growth: the accounting of seasons, battle passes and long-term operations — competition at the top of BR is really competition in operations.
- Case Studies: breakdown methods for cases like Fortnite, to consult before kickoff.
- The FPS page in the Genre Handbooks (Volume 2): the four elements of gun feel and hit feedback, the shared foundation of the combat layer.
- The Co-op page in the Genre Handbooks (Volume 3): complementary roles and rescue design, for comparison with squad modes.
- Homework: pick a BR you know well and record three of your own matches from your point of view, noting every five minutes your position, your gear and their relationship to the circle; then build a 1-square-kilometer, 20-player whitebox lobby with a shrinking circle, get friends to play a match, and count how many say "one more match".
