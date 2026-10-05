# Ludo Atlas · Genre Handbooks · 4X

> **Genre Handbooks · Volume 3**. Positioning: the strategy genre whose primary content is growing a civilization's history from a single starting point. Players split turns and resources across four verbs — explore, expand, exploit, exterminate — growing one snowball while reading opponents through the fog of war; drop any one of the four Xs and the game collapses toward a neighboring genre.
> Companions: Game Design Handbook (core loops and system coupling) · Programming Handbook (simulation architecture, AI and performance) · Production Handbook (content estimation and scope control) · Pitfalls & Anti-patterns (the Design & Gameplay and Programming & Architecture chapters).
> This page carries no external links; benchmark titles are widely known works only, and the figures here are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: 4X is the genre that **turns "explore, expand, exploit, exterminate" into a time machine**. Every hour the player invests answers the same question: with limited cities, population and turns, where do you point them — and where will your civilization stand several dozen turns later. Combat can be backstopped by auto-resolution; trade-offs cannot. Numbers can be looked up in tables; planning cannot. The core loop, written straight from the four Xs' names:

`explore (lift the fog of war) → expand (settle cities and claim land) → exploit (build and climb the tech tree) → exterminate (friction and war) → new resources, new problems, new goals → back to exploring and expanding at a larger scale`

The four Xs are not four parallel modules but one timeline competing with itself: opportunities that exploration finds must be claimed by expansion; the production capacity expansion consumes must be replenished by development; the advantages development accumulates must finally be cashed in through conquest. If any one of the four sits out for long, the player feels at hour ten that "this game has no direction". The loop is measured in turns — a game commonly runs from dozens to several hundred — and every click of "next turn" is a small commitment; good design always leaves the player one reason to "play one more turn" (§3.5).

The turn is the container for this timeline; the skeleton is usually:

1. **Resolution and briefing**: last turn's research, production, events and diplomatic messages come due; read the information before deciding.
2. **The action phase**: move units and issue build, research and diplomacy orders; all four Xs' actions happen here.
3. **End turn**: click "next turn" and the system batch-resolves combat, resources, growth and victory progress.
4. **AI turn and the new turn**: opponents act on their own personalities and goals, the player re-prioritizes against the new information, and the loop returns to step 1.

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| RTS | RTS runs several timelines in parallel under real-time pressure; 4X lets you think it over, and the turn is the container for thinking |
| Grand strategy (the Paradox kind) | Grand strategy is built on continuous time and diplomatic management, with a historical scenario supplying the stage; 4X starts from zero, and the map and opponents are all variables |
| City builder | The city builder's opponent is the system's own side effects; 4X's opponents are living civilizations, and win or loss is finally written into the after-action report |

A self-check question: take away exploration and the opponents — does your loop still turn? If not, what you are building is a city builder or a management sim; only when all four Xs can independently supply decisions is it a 4X.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **A sense of discovery**: the map starts unknown, and the reward for exploring is "every tile you open"; unexplored space is both a content generator and the source of tension.
2. **Delayed gratification**: a route committed to dozens of turns ago becomes national power dozens of turns later; "planning cashed in" is a pleasure unique to the genre and the hardest to copy.
3. **A sense of control**: city layout, resource mix and diplomatic relations are all traceable; a win should survive a retrospective, and a loss should be explainable.
4. **Narrative generation**: at the end of a game the player can tell a story of their own (who backstabbed whom, who snowballed, which comeback turned the game); stories are this genre's best marketing material.
5. **One more game**: a single game has an endpoint, but the combinations of civilizations, maps and victory routes make the next game's assumptions completely different; "starting another game" is the core retention metric.

Benchmark titles (widely known names only; finish a full game of each before you talk about breaking them down):

| Title | What to learn from it |
| --- | --- |
| Sid Meier's Civilization V / Civilization VI | The rule simplification of one unit per tile; district placement and Eureka moments; parallel victory routes and the stickiness of "one more turn" |
| Stellaris | The sense of scale of a procedurally generated galaxy; an event and narrative system that gives space 4X its emotional anchor |
| Endless Space 2 | Civilization differences taken down to the rules layer: each faction has its own resources and gameplay systems |
| Humankind | Merging cities and swapping civilizations by era — a direct answer to the "mid-to-late-game drag" problem |
| Old World | The Orders economy and event cards, turning "the number of actions in a turn" into an allocatable resource |

One question unifies the breakdown of all these titles: how do they leave the player with something they still want to do on turn one hundred.

## 3. Design Essentials

### 3.1 The Four-X Loop: Weights, Resolution and Information

All four Xs must appear in the player's first hour, only scaled down: a patch of fog, one city, two or three build options, one small skirmish. Whatever is hidden in the first hour cannot be made up for later.

| X | What the player is doing | Main resource sink | Design levers |
| --- | --- | --- | --- |
| Explore | Send scouts to lift the fog; assess tiles and neighbors | Unit time (turns) | Fog layers, density of exploration rewards, map generation rules |
| Expand | Pick sites and settle cities, claim borders, grab resource belts | Production and settler units | City spacing, freedom of placement, border rules |
| Exploit | Queue build orders, pick technologies, shift policies | Production and gold | Tech tree structure, building combinations, internal management systems |
| Exterminate | Build armies, fight, force peace or erase nations | The entire resource stock | War cost, diplomatic consequences, win-loss determination |

Hard discipline for turn resolution: **fixed order, reproducible causality**. Whether production resolves before research, whether combat resolves after movement or simultaneously — all of it goes into the rules documentation and stays stable. Resolution must also be "explainable": every number change the player sees must trace back to their own orders or to known rules; changes that cannot be explained are raw material for negative reviews.

### 3.2 Map and Scouting: Three Layers of Fog of War

The 4X map is not backdrop but the primary content carrier; the fog is designed in three layers, because information itself is a resource:

| Layer | What the player sees | Design requirement |
| --- | --- | --- |
| Unexplored | Solid black or outlines only; contents unknown | Exploration payoffs must be dense: resources, ruins, natural wonders, a neighbor's borders |
| Seen but unscouted | Terrain memory: terrain visible, units not | The memory layer must be sufficient yet not permanent, so that "who do I send to take a look" becomes a decision |
| In sight | Live information: both terrain and units visible | Vision radius, scouting tools and counter-scouting must form a complete set |

- The map is a variable, but a "controlled variable": procedural generation plus hand-tuned templates (terrain skeleton, resource distribution belts, neighbor layout) so that both fairness and drama can show up.
- Terrain must participate in strategy: mountain passes, river mouths, archipelagos and the placement of resource belts decide expansion direction; pure-noise terrain is as good as no map.
- Exploration needs a clock: the early land and ruin grabs carry urgency; once the map is fully revealed at midgame, the explore X shifts to "scouting the opponent's intentions", and troop movements in the fog carry the information war of the second half. The fog must sell the player one belief: information is worth buying with turns — otherwise the explore X degrades into a map-revealing ritual.

### 3.3 Tech Tree and Civilization Differences

The tech tree is the skeleton of the exploit X; the two mainstream structures each have their use:

| Structure | Shape | Strength | Risk |
| --- | --- | --- | --- |
| Tree | Clear branches and prerequisites; plan ahead | A strong sense of planning and of delayed gratification ("saving up for the big payoff") | Easy for players to compute a single optimal route |
| Web and triggers | Research options are randomized, or triggered by actions (Civilization VI's Eurekas, for instance) | Every game's route differs, cancelling out the optimal solution | The sense of planning gets diluted, and luck favors the strong even more |

Design discipline: keep 2 to 4 meaningful branches at each tier, and make the trade-offs between branches visible; technologies must unlock not just numbers but "new verbs" (new terrain passability, new diplomatic actions, new ways to expand); the balance goal is not "every route equally strong" but "no single route is optimal in every situation".

Civilization differences come in three cost tiers; small teams build them in order:

| Tier | Content | Cost | Notes |
| --- | --- | --- | --- |
| Stat tier | Different bonuses, traits and starting conditions | Lowest | Do these first; they carry the sense of choice in the first version |
| Unique units and buildings | Every civilization fields its own pieces | Medium | The 4X player's "main course"; visible gameplay |
| Rules tier | Exclusive resources, exclusive systems, an exclusive gameplay layer | Highest | One faction's rules tier is roughly half a new game — do it only as your capacity allows |

Victory routes are the other half of "civilization differences": the common routes — military, science, culture, diplomacy, religion — need their own resources and pacing, so different civilizations have home turf on different routes. The point of parallel victory routes: your neighbor's threat comes in more than one form, and so does your defense.

### 3.4 Opponent AI: The Genre's Hardest Problem

A 4X AI must do four jobs at once: domestic management, army employment, exploration and expansion, and diplomacy and trade; their algorithms and budgets are completely different — do not write them as one "AI class". The goal is not "human-like" but **readable, beatable and full of character**:

- **Readable**: the player must be able to explain the AI's behavior (why it attacked, why it made peace); behavior patterns are low-frequency but obvious, and the diplomacy screen spells out where each attitude comes from.
- **Beatable**: the AI must be able to lose, and to win; "you can never win" and "it always throws itself away" discourage players equally.
- **Full of character**: different civilizations use different parameter profiles (aggression, expansion appetite, tech preferences, loyalty to allies); one algorithm plus a parameter table is cheaper and more controllable than four separate algorithms.

Diplomacy is "conversation with consequences": relationship state (an attitude value plus a history of backstabs, aid and border friction), deals and treaties (trade, open borders, alliances, cease-fires, with valuation done as two-sided bids), decision logic (a state machine or utility scoring, explainable through the UI), and written-back consequences (war weariness, economy, reputation). All four are required — miss one and diplomacy is just trade with a new coat of paint.

The AI's compute budget is an engineering red line (§4); on the design side, three things go with it: strategic-layer replanning at low frequency, tactical-layer decisions every turn, and local pathfinding for unit movement — prefer solutions that are "suboptimal but hold up in time"; difficulty tiers must be open and transparent (resources, speed, whether the AI can see through fog; fog cheating must be extremely restrained, because one caught instance makes players doubt every AI behavior); AI behavior logs must exist from day one, or tuning the AI amounts to groping in the dark.

### 3.5 Game Length and Pacing Control

A single game commonly runs from a few hours (small map, fast settings) to a dozen-plus hours (large map, a full climb up the tech tree); in multiplayer marathons it is normal to split one game across several sessions. Length itself is not the problem; "not one minute of the mid-to-late game still contains a decision" is the problem. The way to close the game out is to hand each era new verbs or new choices, not to multiply the same choices by bigger numbers.

| Stage | Player state | Design task | Common mistake |
| --- | --- | --- | --- |
| Early game | Least information, most pressure | Use exploration and land grabs to create urgency; keep decision density high | Nothing to do for the first twenty minutes |
| Midgame | Expansion and friction coexist | Let diplomacy and war take turns in the spotlight; give the midgame its own goals | The leader locks in victory early and everyone else is just along for the ride |
| Late game | Production explodes, micromanagement balloons | Close it out: accelerate victory, compress micro | Clicking through dozens of cities per turn — running the empire becomes an approval meeting |

The toolkit for control:

- **A second clock**: victory conditions must be able to "accelerate the ending" and make the finish predictable; never let players run out of everything without knowing whether they have won.
- **Automation and delegation**: auto-management, appointed governors, city-queue templates, plus speed settings, shortened animations and auto-end-turn; make micromanagement optional — forced micro is a drag amplifier.
- **Scale caps**: city caps, unit caps and map size as explicit design variables; "the bigger the empire, the harder to run" must be a mechanic, not an apology.

## 4. Technical Essentials

The engineering thesis in one line: **turn-based play is this project type's biggest technical dividend — it moves complexity out of "real time" and into "scale and AI"**. The following is engine-agnostic; for details see the Programming Handbook.

- **Logic decoupled from presentation**: resolution runs in batches at turn boundaries, and the presentation can be delayed, sped up or skipped; the correct shape is unit animation mid-playback while the data has already resolved.
- **Data-driven**: units, buildings, techs, civilizations and events all live in external tables that the code only reads; balance is this genre's main work, changing a number must not wait on a compile, and the table schema is designed together with the modding interface.
- **Determinism**: randomness runs on a reproducible seed system (logical randomness kept separate from presentational randomness); replays, multiplayer sync and AI batch runs all depend on it.
- **Layered AI budgets**: strategic planning runs at low frequency and can be asynchronous, tactical decisions every turn, unit pathfinding at high frequency and highest cost; each layer gets its own budget, the AI turn's time cap goes into the spec, and better a dumber AI than a stutter.
- **Pathfinding is the biggest line item**: A* plus hierarchical pathfinding or flow fields; cap how many routes get recomputed per turn on large maps; unit movement can "pick the destination first and solve it across frames".
- **AI tooling first**: behavior logs, hidden evaluation panels and batch simulation (AI versus AI, hundreds of games) are the only realistic way to do balance work.
- **Fog and map caps**: split the fog into three data layers — terrain memory, current visibility, unlocked regions — and update vision changes incrementally; the three caps (map size, unit count, city count) are fixed during the prototype phase.
- **Saves and multiplayer**: saves carry version numbers, migration functions and rotating backups (a game runs dozens of hours — a corrupt save is the number one crime in reviews); multiplayer comes in three modes of increasing cost — hotseat, asynchronous turns, simultaneous turns — and small teams build the first two first.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimating scope; not a commitment.

| Project shape | Content scale | Time scale | Notes |
| --- | --- | --- | --- |
| Four-X prototype | 1 small map, 1–2 civilizations | 2–3 months | Zero art; validates the turn structure and a minimal AI |
| Small complete title | 1 map, 4–6 civilizations | 9–18 months | AI and balance are the invisible bulk |
| Typical indie scope | Several maps, 6–10 civilizations | 2–3 years | Content and AI both eat the budget |
| Large title | Many maps, many civilizations, mod support | 3+ years | The Civilization series' order of magnitude |

Cost structure per content unit:

| Content unit | Unit cost (magnitude) | Minimum viable | Commercial scope | Notes |
| --- | --- | --- | --- | --- |
| Civilization | 1 week to 1.5 months each | 4–6 | 10–20 | Rules-tier differences cost the most; the stat tier the least |
| Tech node | Half a day to 2 days each | 60–120 | 200+ | Coupled to buildings, units and victory routes |
| Unit | 2–5 days each | 15–30 | 60+ | Including numbers, model, animation and AI usage preferences |
| Map | 1–3 weeks each | 3–5 | 10–20 | Generation templates plus hand-placed landmarks |
| Victory route | 1–3 weeks each | 2 | 4–6 | Design cost shared with civilization differences |

Two magnitude conclusions: balance and AI are the invisible bulk — set aside more than 20 percent of total production time for "AI and balance tuning", and have batch simulation tooling from the prototype phase (§4); the cost of civilizations is not linear — too many rules-tier civilizations means building several games at once, so decide "how many rules-tier civilizations" before scheduling. Scope-cutting order: number of civilizations, number of maps, number of victory routes — AI depth comes last, because cut the AI's depth and the genre stops existing.

## 6. How to Start the First Prototype

The first prototype: 2–3 months — 1 small map, 1–2 civilizations, zero art — validating exactly one thing: whether the four-X loop and the turn structure can grip players.

1. **Grid and movement**: generate a small map (two terrain types and one resource), let units move by click, and resolve something at end of turn.
2. **Explore**: a minimal implementation of the three fog layers; place two or three exploration rewards to validate that "what is in the fog is worth going to see".
3. **Expand and exploit**: one city that can be settled, grow population and queue production; a small tech tree of 10 to 20 nodes, played to the first fork.
4. **Exterminate and close out**: one military unit plus simplified combat resolution — units can fight each other and take cities; set a closing condition (capture all enemy cities, or survive to a specified turn count) so that "one game" has an endpoint.
5. **A crude AI**: capable of exactly three things — expand, build units, push toward the player — enough to finish this small map; behavior logging starts that day.

Acceptance (all observable):

- Testers can read the four Xs unaided and say what they are betting on in this game; the scaled-down game plays out in under an hour.
- At least once, a tester plays "one more turn" out of their own drive, rather than being asked to try again.
- With art turned off and only icons and numbers left, the game still stands; the AI can expand and attack without locking up.

Counter-examples: ten civilizations first, full diplomacy first, a campaign story first, art first. Until the four Xs loop, these are all sunk cost.

## 7. Common Pitfalls

| Pitfall | Symptom | How to avoid it |
| --- | --- | --- |
| Leaving the AI for the end | The content is done and the AI is still a scarecrow; the game does not stand | The AI is one of the core content pieces — schedule it at kickoff and have a minimal AI in the prototype phase |
| One of the four Xs missing | Nothing left but building units and scoring; exploration and development become decoration | Every X needs its own decisions and payoffs (§3.1) |
| Mid-to-late-game drag | Cities and units balloon linearly; dozens of repetitive clicks every turn | Build in automation, scale caps and a closing clock from the design phase (§3.5) |
| A single optimal tech route | Players copy the guide and choice dies | Give each branch its own situations and costs; check optimal routes with regular batch simulation |
| Civilization differences as skins only | Reskins without gameplay change; a fake sense of choice | Schedule along the three tiers — stats, unique units, rules layer (§3.3) |
| The AI's fog cheating gets caught | Players stop trusting any AI behavior; "cheating" becomes a review keyword | Tune difficulty through open rules (resources, speed); be extremely restrained about secretly changing information |
| War eats everything | Combat is too fun, players fight the whole game through, and the four Xs degrade | Make war costs and diplomatic consequences real; do not let the military monopolize every victory route |
| The map is just backdrop | Generated terrain has no logic; exploring is like opening blind boxes | Terrain must join the strategy: mountain passes, river mouths and resource belts decide expansion direction |
| Underestimating multiplayer cost | Simultaneous turns and reconnection drag the schedule down | Small teams build single-player and hotseat first (§4) |

## Further Reading

- Game Design Handbook: core loops, system coupling and numeric methods; as an exercise, draw the four Xs as a loop diagram of your own.
- Programming Handbook: AI budgets, pathfinding, deterministic randomness and data-driven details — the companion to this page's §4.
- Production Handbook and Indie Survival: estimation, scope control and scheduling discipline; time "one civilization, one map, one unit" first, then multiply by content volume (§5).
- Pitfalls & Anti-patterns: the Design & Gameplay and Programming & Architecture chapters, read alongside this page's §7.
- Case Studies: retrospective methods for successes and failures; use them when breaking down a 4X you know cold.
