# Ludo Atlas · Genre Handbooks · Hero Shooter

> **Genre Handbooks · Volume 4**. Positioning: the team-competitive genre that packs two mastery lines — gunplay and character abilities — into the same character, turning heroes into gameplay dials and a long-term content engine. Players pick heroes, build compositions and fight over objective points, with gunplay and abilities each holding half the say.
> Companions: Game Design Handbook (core loops and numbers) · Programming Handbook (data-driven design and performance) · Multiplayer & Backend (synchronization, matchmaking and anti-cheat) · Esports & Competitive Design (balance, spectating and events).
> This page carries no external links; benchmark titles are widely known works only, and the figures are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: hero shooter is the team-competitive genre that **grows a second mastery line and a content engine out of "character ability kits" on a foundation of shooting**. Every hero enters with their own weapon, abilities and movement; teams divide labor by role and fight over objective points; victory and defeat are decided jointly at three layers — gunplay, abilities and composition.

Family position: the culminating form of the "competitive team" branch of the shooter family. Gun feel and hit feedback share their roots with the FPS page in the Genre Handbooks, and role division and counters share theirs with the MOBA page in the Genre Handbooks — but it sells neither the raw gunplay duel of a single match nor in-match growth; what it sells is the difference of "swapping heroes is swapping a whole way to play".

The core loop, written as a ring of verbs:

`pick heroes and composition → enter the objective area → exchange gunplay and abilities → build the ultimate → win the team fight → push or defend the objective → the round settles and resets`

The loop carries two time scales: second-level aiming, positioning and ability exchanges, and minute-level ultimate charge and objective progress. It stands on three premises: the gun feel must hold up (§3.1), abilities must be readable and counterable (§3.1), and compositions must have counterplay (§3.2).

Drawing boundaries against neighboring genres:

| Neighboring genre | Boundary |
| --- | --- |
| First-person shooter (FPS) | FPS puts everyone into one set of guns and abilities, with outcomes all down to gunplay, position and tactics; hero shooter binds weapons and abilities to heroes, adding two more variables — abilities and composition — on top of gunplay |
| MOBA | MOBA's growth and resources accumulate within a match (lane waves, levels, items); a hero shooter's numbers are essentially fixed for a match, growth shows only in ultimate charge and coordination, and the outcome lands on objective points rather than a base |
| Battle royale | Battle royale is one-shot elimination per match with resources from looting; hero shooter is a multi-round objective mode with respawns, where composition and heroes can be adjusted mid-match |
| Tactical shooter | In tactical shooters one bullet is life or death and abilities are only auxiliary tools; hero shooters run a longer TTK, trading abilities and teamwork for room to jockey and turn the match around |

A self-check question: replace every hero with the same character, the same gun and the same ability set — if the fun barely changes, you are not making a hero shooter; everything this genre adds lies in each hero answering "how do I play this match" anew.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Two-channel mastery**: gunplay has its own progress curve and abilities have their own timing to master; players can see their growth on both lines.
2. **Character identity**: the hero pool and proficiency form a long-term relationship of "who I train, who I fear" — swapping heroes is itself gameplay.
3. **Role division that pays off**: tanks open the way, damage dealers reap, supports keep people alive; roles are not paper settings but contributions every teammate can feel each match.
4. **Ultimate highlights**: charge fully, unleash in the team fight, turn the match; every hero must leave behind a moment worth retelling.
5. **Lose with understanding, retry fast**: rounds and respawns make failure cheap, and the review lands on a specific exchange.

Benchmark titles (play them yourself before breaking them down; the feel and pacing of abilities live in the hands, not in video):

| Title | What to break down |
| --- | --- |
| Overwatch | The genre definer: the baseline sample of hero roles, objective modes and ultimate economy |
| Team Fortress 2 | The origin of nine-class teamwork: duties before numbers, where the class itself is the gameplay |
| Apex Legends | Abilities in service of movement and information; how abilities change the rhythm of firefights under a long TTK |
| Valorant | Hero abilities joined to a short-TTK tactical shooter: abilities for map control, gunplay for life and death |
| Marvel Rivals | 6v6 team synergy: turning "hero combinations" themselves into a system |

What they share: the hero is the smallest unit that carries difference, and the mode is the container that carries pacing; only when both hold does long-term updating have somewhere to go.

## 3. Design Essentials

### 3.1 Hero Design: The Two Axes of Gunplay and Abilities

Every hero first answers two questions: how does this weapon play (engagement range, TTK, feel)? And how do these abilities change "how it plays"? The hero is a gameplay dial, and what it dials is exactly four things: distance, movement, information and resources.

| Ability type | What it dials | Typical tools | Design discipline |
| --- | --- | --- | --- |
| Mobility | Movement rules | Dashes, jumps, teleports, glides | Give it routes and cooldown costs; it must not become a mindless escape button |
| Defense | Firefight duration | Shields, damage reduction, brief invincibility | Windows must be short and readable; invincibility is a high-incidence zone for balance accidents |
| Healing and buffs | Team resources | Healing, speed boosts, damage boosts | Healing is tied to TTK, and healing overflow is extra health in disguise |
| Recon and information | Information rules | Marking, wallhacks, traps | Information breaks the mind game most easily and must have a duration and a counter |
| Crowd control | The opponent's control of their character | Stuns, slows, launches | Hard control should be few and expensive, with duration and cooldown strictly reciprocal |
| Ultimate | Team-fight pacing | Area control, big damage, team buffs | Must be telegraphed and counterable; the charge economy gets its own table |

Two balance disciplines:

- Strong gun, restrained abilities; weak gun, compensating abilities — a common direction; but every hero's "weapon strength × ability contribution" has to live in a table, and balancing looks at the table before the win rate.
- Abilities cannot aim for the player: auto-aim and lock-on abilities that are too strong void the gunplay axis outright, and the genre slides toward the other end.

Ultimate charge is a second economy: it accumulates by contribution (damage, healing, objective progress), commonly one ultimate per several tens of seconds to two minutes; "I have ultimate" is team information, and teammates must be able to see it. The ultimate decides when team fights switch on, so its cast bar, sound cues and on-screen signals are baseline design, not a polish item. Every hero must also yield one sentence of "what situation is unthinkable without it"; if you cannot write it, consider merging or cutting the hero rather than adding numbers.

### 3.2 Roles and Team Composition

Roles set the "exam questions" for a team, and stats are merely the answer sheet. Three base roles, with damage further split by range and mobility:

| Role | Duties | Strengths | Weaknesses |
| --- | --- | --- | --- |
| Tank (heavy) | Open paths, hold space, soak damage | Space control and durability | Limited damage; if teammates don't follow up, the tank absorbed it for nothing |
| Damage | Create kills, suppress key positions | Burst or sustained damage | Fragile; caught alone means dead |
| Flanker (mobile damage) | Harass the backline, cut formations apart | Mobility and picking off stragglers | Hard control and stacked teams; if they can't get in, their value is zero |
| Support | Healing, buffs, control, rescue | Stretches team resources and room for error | Low damage; caught once and the whole team loses its lifeline |

The counter chain in one sentence: long-range fire suppresses advances across open ground, mobile characters punish lone long-range damage dealers and supports, tanks swallow the harassment of mobile characters with space and shields, and supports re-glue the line with control and healing. Only when this chain closes does a composition have a skeleton; the test is that "every role can be handled by another role through gameplay means", not brute-forced by stats.

Three mandatory questions for composition: who initiates, who reaps, and who keeps people alive. As long as all three answers have an owner, whether the ratio is 2-2-2 or 1-2-2 is just form. Two disciplines:

- Leave at least two options per role covering different ranges or duties, avoiding "one role dominates while its substitutes are all reskins".
- Hard counters should be few and tunable (anti-heal, anti-stealth, cleanse), and compositions need counter slots to avoid matches where "the draft already decides the loss"; letting players swap heroes is the outlet for composition counters, and the cost of swapping (ultimate charge reset to zero and the like) must be written into the rules so adjustments have a path.

### 3.3 Modes and Pacing: Objective Modes as the Spine

Hero shooters do not sell "how many you killed"; they sell the spatial mind game around objectives. The mainstream forms are all objective modes:

| Mode | Structure | Pacing character | Notes |
| --- | --- | --- | --- |
| Point capture | Both sides contest control points, and the holding side accumulates progress | A cycle of fighting, capturing and holding | A single-point round is clear and makes a good first map |
| Payload | Attackers escort a vehicle along a route while defenders stall | A linear tug-of-war with repeated hold points | Asymmetric attack and defense; the route is the level's pacing |
| Hybrid | Capture first, payload second (or the reverse) | Two pacing sections switching | Gives a match a fuller rise and fall |
| Contested objectives | Grabbing resources, capturing flags or holding multiple points | Frequent swaps and repositioning | The best arena for proving a mobile role's value |

Rounds and overtime: a match is made of rounds, and the rules for swapping sides and attack/defense must be written clearly; overtime (final pushes, overtime point captures) is a spectacle valve — set and test its rules early. Respawn time is the pacing valve, commonly 5–15 seconds; the breathing room of "regroup after a wipe, then fight again" comes from the product of respawn time and spawn-to-objective distance.

Map discipline: at least two or three approach routes around the objective, with near and far engagement layers; the distance from spawn to objective decides how hard it is to fall back and defend. The map is the mode's metronome, and the full methods for metrics and guidance are in the Level Design Handbook. Take one mode to the point where it holds before adding a second; the same hero differs in strength across modes, so balance readings must be split by mode — otherwise you tune point capture and break payload.

### 3.4 The Content Update Engine: New Heroes and the Cost of Balance

Heroes are a content engine and a cost engine at once. A new hero serves as a patch event, a talking point and a returning-player hook all at the same time, but every hero runs a full pipeline from concept to launch.

Cost checklist: gameplay concept and ability prototypes, model, animation and VFX, sound and voice, the skin pipeline, balance testing and matchup-table updates. Before launch, the new hero must be walked through matchups against every existing hero; the more heroes there are, the more this table grows combinatorially — ten heroes means dozens of pairwise matchups, twenty approaches two hundred — and balance without tooling is bound to slip out of control. Update cadence: for commercial products, new heroes run on a seasonal cycle, one or two per season being the common magnitude, with development and balance as standing teams; small teams should budget against the reality of "one or two per half-year" rather than copying the commercial cadence — the content engine is ultimately a cash-flow question.

Three balance ledgers: pick rate, win rate and per-match contribution (damage or healing per minute), each split by mode and by rank bracket; a new hero's first two weeks of samples are noise, so don't rush into big changes (methodology in Esports & Competitive Design §4). Patch discipline copies the standard practice of competitive titles: one theme at a time, numbers first, mechanics second, reworks as the fallback; changes at the game-feel layer are the most expensive, because players rebuild their muscle memory. Commercialization puts its weight on cosmetics and battle passes, keeping heroes and power decoupled from payment as far as possible; selling power is proving unfairness inside your own ladder and burns competitive trust outright.

### 3.5 Matchmaking, Anti-Cheat and Events

The long game is held up by three systems: matchmaking decides the experience of every session, anti-cheat guards the delivery of the competitive promise, and events decide how efficiently population and content amplify.

- **Matchmaking is the product's foundation**: separate hidden MMR from displayed rank, and keep newcomer pools and quarantine pools as buffers for new and returning players; fix the pool rules for squads and solo queue up front — the fill experience is especially sensitive for role-based teams, and nobody wants three straight matches without a support. Tune wait time and match quality against the waterline (methods in Multiplayer & Backend §4).
- **Anti-cheat is the ground you stand on**: client detection, server-side behavior statistics, and reports plus human review — all three layers, no omissions; for a hero shooter, hit rewind and ability resolution must be server-validated, or packet edits and aimbot scripts will punch through the ladder overnight (Multiplayer & Backend §7).
- **Events are an amplifier, not a lifeline**: before running one, self-check three things: whether matches are understandable (are ability VFX and information expression clear?), whether the team has broadcast and event-operations capability, and whether the ladder population can support matchmaking and viewership. Spectating and replays are the foundation under all of it — review, content creation and broadcast share one set of facilities, and they must be provisioned at architecture time (Esports & Competitive Design §3, §5, §7).
- **The fairness red line**: keep heroes and power decoupled from payment as far as possible; freeze the build before important tournaments, and write "when big changes are allowed" into policy rather than deciding ad hoc each time.

## 4. Technical Essentials

The engineering difficulty concentrates in four places: server-authoritative competitive sync, the ability system and hit resolution, team information expression, and provision for spectating and replays. Everything below is engine-agnostic; for the full expansion of sync and matchmaking see Multiplayer & Backend, and for performance and data-driven design see the Programming Handbook.

### 4.1 Server Authority and Synchronization

- Damage, cooldowns, charge and objective progress are all computed on the server; the client only gathers input and predicts presentation. "Anything the server can judge never goes to the client" — this is not a performance choice but a security floor. Client prediction must be restrained: give movement and gunfire immediate presentation, but let ability hits and charge defer to the server, smoothing deviations at the presentation layer; do latency compensation (hit rewind) early, or different weapons will feel split apart under the same network conditions.
- Mobility abilities change movement rules and must be designed together with collision, steps and the prediction system; clipping through walls and getting stuck on terrain are the most common live incidents for these abilities.
- Write the rules for reconnect and mid-match joining early: a match runs about ten minutes, and a disconnect needs a road back; decide AFK and quitting policy (whether bots take over) during design, not in a scramble before launch.

### 4.2 The Ability System and Data-Driven Design

- Heroes, abilities, cooldowns, charge and numbers are all table-driven, so balance touches only tables and supports hot updates — the breathing rhythm of live operations; ability implementation runs on two layers of "config plus script", with numbers and durations in tables and special logic in scripts; ability parameters must never be scattered through code.
- States and modifiers (buffs and debuffs) need a unified management system: write the rules for stacking, refreshing and dispelling clearly, and define the priority of control and control immunity in one shared table.
- Hit resolution and visuals must agree: the ability indicator, hit detection and VFX attachment points share one set of data; "it looked like it hit but didn't" is prime territory for collapsed trust.

### 4.3 Team Information and Expression

- Team-visible information is the foundation of coordination: teammate health, ultimate charge, respawn countdowns and objective progress must all be readable; pings and quick chat must be able to carry basic coordination in place of voice.
- VFX and audio must budget together: multiple ability sets bursting at once in a team fight is a double disaster for performance and readability; hold the line on "see it clearly" with ownership colors (allied and enemy), layer priorities and VFX level toggles; throttle audio by distance layer and threat priority, and give ultimates and control abilities cue sounds the whole team can distinguish (methods in the Art & Audio Handbook).

### 4.4 Spectating, Replays and Data Probes

- Provision replays and spectating from the architecture phase (Esports & Competitive Design §3): review, content creation, event broadcast and report review share one set of facilities, and building it late means rebuilding it; automatically record pick rate and win rate per match along hero, mode and rank-bracket dimensions — balance iteration runs on ledgers, not feelings.
- A practice range and custom lobbies are long-term infrastructure: aim training, ability practice, and validating maps and rules all rely on them, and they are where community events find their container.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimation and for scoping; not a commitment. The numbers are a ruler — calibrate them against your own team's speed.

| Project shape | Content scale | Timeline scale | Notes |
| --- | --- | --- | --- |
| Gameplay prototype | 1 map, 4–6 heroes, 1 objective mode, room-based | 3–6 months (small team) | Validates whether the "gunplay × abilities" dual axis holds, with no ranked |
| Small competitive title | 8–12 heroes, 2–3 maps, 2 modes, light ranked and anti-cheat basics | 1–2 years (small team) | Balance, servers and anti-cheat are the main bills |
| Commercial hero shooter | A hero pool starting in the tens, multiple maps and modes, seasonal operations and an esports ecosystem | 3–5+ years (team) plus ongoing operations | A live product, not a one-off project |

Bill breakdown:

- **A single hero and balance**: gameplay design, ability prototypes, model and animation, VFX, sound and voice, skins and testing — at commercial scale the cost runs in person-months; every new hero adds another pass to the existing heroes' matchup and balance tables, and tuning, data runs and community communication across past versions are standing costs too — with more heroes, maintenance grows combinatorially.
- **Maps**: each map must survive dozens to hundreds of playtest rounds; iterating on hold points, spawns and routes usually takes longer than the art.
- **Servers and security**: per-match server billing, matchmaking services, anti-cheat and report review settle monthly; server shutdowns and merges are long-term bills, and behavior governance (AFK, toxicity) eats retention directly, so review headcount goes into the budget up front.
- **The small team's realistic path**: shrink the scale proportionally rather than inflating it to match the dream: 4v4 or 3v3, a hero count under 8, one objective mode, room-based play with bot fill-in, and ranked and events postponed. If what draws you is "the mind game of hero combinations", first validate that people finish a ten-minute match and want another; if what draws you is esports, read Esports & Competitive Design §7 first: when the daily-active population cannot fill matchmaking, events are a river without a source.

## 6. How to Start the First Prototype

Goal: build a greybox objective-mode room in 4–6 weeks, validating "at the same level of gunplay skill, can abilities and composition add another layer of fun to a match". No ranked, no skins, no backstory writing.

1. (Week 1) The shooting foundation. A whitebox arena plus one gun: instant raycast hit detection, movement and camera, and the full hit-feedback package (hit flash, sound effects, kill confirmation). If the gun feel doesn't hold, everything after it is wasted.
2. (Week 2) Three hero skeletons. One tank, one damage, one support, each with just "one weapon plus two abilities plus one ultimate", all made of primitives and placeholder VFX; have the abilities demonstrate each of the three dials once — change distance, change movement, change resources.
3. (Week 3) The objective mode. Pick point capture or payload and build the full loop: capture, progress, respawn, rounds and win/loss resolution; a second rough map validates route differences.
4. (Week 4) Ultimates and team information. The charge economy goes into tables; teammate ultimate and health information becomes visible; key events (ultimate use, being controlled, objective reversals) get placeholder sound effects as audio signals first.
5. (Weeks 5–6) Testing and review. Train AI fill-ins first, play internally for three days, and record "which hero is absurdly strong" and "which exchange left us without a clue"; then get 8–10 people to play in two teams for three evenings, changing only numbers and layout, adding no new systems.

Starting parameters (copy them straight and adjust): 4v4 or 3v3; 4–6 heroes; a match around 10 minutes; ability cooldowns 6–15 seconds, ultimates one per 1–2 minutes (both typical magnitudes); respawn 5–15 seconds.

Acceptance criteria (all observable):

- With all art and audio removed, testers still want to play again and again, sessions typically running past 20 minutes.
- At least 6 of 8 testers can say whether the previous round was lost on composition, ability timing or objective play — not just "the other side had better aim".
- The same tester playing two different heroes feels a clear difference in handling; after switching back to the default character, they can say "what's missing".
- Change any one ability number and you can explain its effect on round outcomes within a day; if you can't, the data and tooling are not in place yet. Testers ask for another match on their own, rather than being asked to try again.

## 7. Common Pitfalls

1. **Abilities before the gun feel is settled**: abilities cannot save the shooting foundation; get "willing to fire a second shot" to hold first, then talk about heroes.
2. **Reskinned heroes with overlapping roles**: a batch of stat copies leaves balance with nothing to grip; give every hero a "no one else does it" situation first (§3.1).
3. **Abilities upstaging the guns**: auto-aim, invincibility and control chains too strong void gunplay and slide the genre toward MOBA-fication.
4. **Ultimates with no telegraph or counter**: whoever charges first wins and team fights become a button race; sound cues, visual telegraphs and counter windows are mandatory.
5. **Compositions with no answer**: one family dominates or the counter chain breaks, and the draft already decides the result; hard counters must be few and tunable (§3.2).
6. **One mode with monotonous pacing**: no rounds or attack-defense swings, bored by the third match; modes are pacing's second design layer (§3.3).
7. **Balancing only on overall win rate**: without splitting by mode, rank bracket and hero proficiency, the average hides a broken meta (§3.4).
8. **Content cadence out of control**: new-hero development drags down balance and art until even patches can't get scheduled; fix "how much one season can deliver" before fixing ambition.
9. **Matchmaking pools split too early**: modes, divisions, squads and servers cut the pool at several layers and shred the population — queue times kill the game before balance does (§3.5).
10. **Anti-cheat and spectating infrastructure missing**: packet edits and scripts punch through the ladder overnight (Multiplayer & Backend §7); replays and spectating not provisioned leaves events, content and review all stuck on infrastructure (Esports & Competitive Design §3).
11. **Selling power**: a new hero paid-for on day one and over-tuned is proving unfairness inside your own ladder.

## Further Reading

- Game Design Handbook §2, §4: core loops and number-table methods — the draft under §3.1 and §3.2.
- Programming Handbook: performance budgets, data-driven design and hot-update engineering — the companion to §4.
- Multiplayer & Backend §2, §4, §7, §8: sync models, matchmaking, anti-cheat and the cost ledger — the expansion of §3.5 and §4.1.
- Esports & Competitive Design §3, §4, §5, §7: spectating systems, balance methodology, the esports ecosystem, and self-checks before running events.
- Level Design Handbook: metrics and guidance for objective points, routes and cover — the expansion of §3.3.
- Art & Audio Handbook: how to layer ability VFX and sound.
- Indie Survival and Pitfalls & Anti-patterns: scope control and high-frequency pitfalls — complementary to §5 and §7.

Homework: pick a recording of a public hero-shooter match and record both sides' remaining ultimates and objective progress every 2 minutes, to find which exchange the match turned on; then play two matches each as a tank, damage and support, and write down the three roles' different answers to "where should I stand this match".

Hero shooters look like they sell characters, but what they actually sell is the mind game of "one more layer of judgment above gunplay", and a reason to want a different hero the moment a match ends.
