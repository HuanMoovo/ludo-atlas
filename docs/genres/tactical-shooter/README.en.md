# Ludo Atlas · Genre Handbooks · Tactical Shooter

> **Genre Handbooks · Volume 4**. Positioning: the team-competitive genre that turns "preparation before the firefight" into the primary arbiter of victory. Low fault tolerance makes every bullet expensive; the information game makes "who knows first" decide the outcome earlier than "who shoots straighter"; and the round economy makes every round a bet placed on the next one.
> Companions: Game Design Handbook (loops and balance) · Programming Handbook (data-driven design and performance) · Multiplayer & Backend (sync, matchmaking and anti-cheat) · Esports & Competitive Design (balance, spectating and tournaments).
> This page carries no external links; benchmark titles are widely known works only, and the figures here are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: the tactical shooter is the team-competitive shooter genre **that turns "preparation before the firefight" into the deciding factor**. Low fault tolerance (a few bullets decide life or death, one sniper shot kills) forces players to take every exposure seriously; the information game (who sees whom first, who holds the angle first) tips the balance of the firefight; and the round economy (what to buy, what to save, when to force) strings individual rounds into a budget chain.

Family position: within the shooter family, it is the branch that pushes competitive confrontation up to the level of institutions. Gun feel and hit feedback share their roots with FPS (see Genre Handbooks · FPS), but it adds three rule sets — rounds, economy and information — on top of gun feel, turning "the cost of one bullet" from a single number into a system.

The core loop, written as a verb chain:

`scout and hold angles → exchange information and plans → clear a path with utility and enter → short, sharp firefights → plant, defuse or handle the clutch → round resolution → economy reset → next round`

The loop carries two time scales: the second scale (holding angles, swinging out, where utility lands) and the round scale (economy, score, halves). It holds on three premises: hit detection is trustworthy (every bullet's destination is explainable), the information rules are self-consistent (sound, sightlines and callouts can be trusted), and the economy closes its loop (winning is rewarded, losing still has hope).

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| First-person shooter (FPS) | FPS is the foundation of gun feel and spatial language; the tactical shooter stacks rounds, economy and information on top of it, amplifying the value of a single bullet into a whole system of rules. |
| Hero shooter | Hero shooters use a longer TTK, abilities and respawn windows to stretch the firefight into jockeying and comebacks; the tactical shooter goes the other way, compressing TTK to the lowest in the genre and demoting abilities to auxiliary utility, so the outcome is decided before the firefight. |
| Extraction shooter | Extraction shooters take the risk outside the match (only what you carry out counts); the tactical shooter settles risk per round, re-buys gear every round, and wipes the slate the moment the round ends. |
| Battle royale | Battle royale is one life per match with resources from looting; the tactical shooter restarts across many rounds and turns the contest for resources into a buy-phase economy. |
| Hardcore simulation shooter | Mil-sim shooters (military simulation) pursue the real complexity of the battlefield; the tactical shooter is the competitive abstraction, cutting irrelevant procedure and converging the variables to serve fair competition alone. |

A self-check question: strip out the round structure, the economy and the information rules — if what remains is just an ordinary FPS, what you are building is not yet a tactical shooter.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Deaths you can understand**: the premise of low fault tolerance is a sense of fairness; every death must be reviewable down to "who had which angle first". Die for unclear reasons and the learning curve breaks.
2. **Information is advantage**: footsteps, scopes, utility sounds and callouts make up an intelligence ledger you can manage; ears and judgment are worth as much as aim.
3. **The heartbeat of the economy**: saving, forcing, full-buying — every round's decision pulls on the next round's nerve.
4. **Coordination that pays off**: utility combinations, crossfire, calls in the clutch; beyond individual skill there is a second, team-level progression curve.
5. **Clutch highlight moments**: 1v3 defuses, comebacks and overtime are the moments most easily retold and shared in games of this kind.

Benchmark titles (play them yourself before breaking them down; the feel and pressure of low fault tolerance live in your hands, not in videos):

| Title | What to break down |
| --- | --- |
| Counter-Strike series | The genre baseline: round economy, bomb-site maps and the competitive yardstick of "aim decides life or death" |
| Valorant | A tactical skeleton plus hero abilities: abilities handle information and map control, while gunplay still decides life or death |
| Rainbow Six Siege | Prep phase, destructible environments and information utility: expanding "before the firefight" into a whole round's worth of content |
| CrossFire | The mass-market sample in mainland China: faster pacing, a lower barrier to entry and a huge internet-cafe population |

## 3. Design Essentials

### 3.1 Low Fault Tolerance and the Information Game

TTK is the first dial. Typical magnitudes: three to five rifle bullets to kill, one or two to the head, one sniper shot per life; armor and penetration are the main adjustment levers. The discipline for tuning TTK: give "first hit" an overwhelming payoff, but never let "a graze" equal death, or frustration will overpower the desire to learn.

Low fault tolerance stands on three things:

- **Deaths you can understand**: kill replays, directional damage indicators and hit sounds are the baseline kit; transparency of detection is trust.
- **First strike has value, but it can be broken**: pre-aiming and holding angles confer an advantage, and the attackers must trade utility, angles and numbers to win it back; if first strike is fixed beyond counterplay, the round becomes a lottery.
- **Spawn sightlines tested one by one**: who can see whose spawn at the start of a round is part of map balance and goes into the sheet like any other number.

Foundations of the information game: sound is the cheapest information channel — footsteps, scoping, reloads and utility landings all need distance falloff and material differentiation; visual information (cracks, shadows, utility edges) prices holding angles and swinging out. Callout language must be standardized: name the positions first, then talk tactics; once the same sentence paints the same picture for every teammate, coordination has a starting point.

### 3.2 Round Economy and Equipment Purchases

The economy is this genre's second balance sheet. Its goal is not to accumulate money but to make someone run the numbers every round: go for this one, or save.

Sources of income and typical magnitudes:

| Source | Typical magnitude | Design intent |
| --- | --- | --- |
| Round win reward | Around 3,000 | The winning side's baseline income, while keeping the snowball from killing the game |
| Loss bonus | Ramping from about 1,400 up to about 3,400 in steps | Gives the losing side visible hope; the core anti-snowball valve |
| Kill reward | 100 to 900, by weapon | SMGs and shotguns pay high, snipers pay low; rewards upsets |
| Plant and defuse reward | A few hundred each for the whole team | Prices the objective actions, encouraging players to do the job rather than hide |
| Money cap | Around 16,000 | Prevents unlimited accumulation; an edge cannot stretch across too many rounds |

The buy menu docks in tiers: pistols; SMGs and shotguns; rifles; snipers; armor and defuse kits; utility. The price list must guarantee that "each tier up buys more edge — and more risk of going broke", so that buying a gun is a real decision. Four baseline round decisions: full buy (the whole team gears up for safety), force buy (half gear, an all-in bet against the opponent's economic rhythm), full save (no buys, keeping guns only), and half buy (a few heavy guns carrying a few light ones); all four need a clear "affordable to lose, worth it to win" accounting before players will seriously study the economy.

Three team disciplines: economy and buy information visible to the whole team; save rounds require team consensus (one player secretly buying wrecks the whole team's rhythm); the shot-caller must read the opponent's economy (how deep the loss streak runs, whether they will force — the second board besides the clutch). Anti-snowball relies on a three-piece kit: differentiated kill rewards, a stepwise loss bonus, and a money cap plus side-swap reset; miss any one and the leading side full-buys all the way to the end while the economy becomes decoration.

### 3.3 Tactical Utility and Team Coordination

Utility is the second weapon set that "changes the situation without relying on aim". The mainstream quartet each has its job:

| Utility | Role | Typical use | Counter |
| --- | --- | --- | --- |
| Smoke | Blocks sightlines, draws temporary boundaries | Cut firing lanes, block defuse angles, fake a push direction | Counter-smoke, locate by sound, blind-fire through smoke |
| Flash | Strips away the vision window | Flash a site before entry, flash to retake an angle | Turn away from the flash, play the geometry, count the timing |
| Incendiary | Blocks routes and forces movement | Clear corners, block a defuse, buy time | Wait it out, take a different angle |
| Frag grenade | Damage and armor break | Force movement, probe spots, drain resources | Dodge by moving, listen for the pin pull |

Three disciplines for utility design: predictable (same throw point, same result — only then is practice worth anything; randomness may appear only where it does not matter); counterable (smoke can be answered, flashes can be turned, fire can be waited out; any "no-answer utility" ruins the round design); and costly (price and carry limits create trade-offs; utility cannot be a free, all-purpose solution).

The smallest unit of coordination is "one player paving the way for another": smoke cuts the firing lane for the entry fragger, a flash gets the second player in, fire burns off the defender's retreat. Above that sits the team structure: the entry fragger opens angles, the support guarantees the entry, the sniper watches the long sightlines, the shot-caller reads economy and tempo. Roles are a division of labor, not a class restriction.

"Default" and "execute" are two tempos on the same map: the default controls the map, squeezes out information and waits for the opponent to err; the execute dumps all the utility into one site inside a minute. Both tempos must work, or the match has no variation.

The clutch is the highlight zone for individual skill and information management: holding back the opponent's information with calls, saving utility, stalling the clock, tracking the opponent's economy; design must give the clutch "a story worth telling" (the defuse countdown and the economic cost of a 1vN), so that even the losing side earns applause. Communication infrastructure is not optional: a position-name sheet, quick signals, in-round information discipline (call "who, where, how much HP, what gear"); beyond voice there must be a workable information channel — that one exists for all players, not only for those on mic.

### 3.4 Map Design: Symmetry and Bomb-Site Structure

Two traditions run in parallel: the symmetric competitive map (the Counter-Strike and Valorant lineage: spawns at both ends, two bomb sites plus one mid lane) and the destructible-space map (the Rainbow Six lineage: floors, breachable surfaces and information utility make the "shape of the map" variable). Both start by drawing topology: connectivity and distances first, then cover, utility spots and angles.

The four-piece kit of bomb-site structure:

- **Two entry routes plus one mid lane**: every site needs at least two real entrances; mid is the bus line for information and rotations, and the side that controls mid takes the clutch tempo first.
- **The distance difference from spawn to site**: it decides retake and rotation times; the timetables of both sides must sit in the same magnitude.
- **Angle economics**: every held angle must carry a cost (exposure window, retreat); crossfire points and wallbang spots (listed separately by material) are the map's second language.
- **The time scale**: start to first contact, plant time, defuse time, overtime; fix these numbers first and the map grows around them.

Symmetry is realized not as art symmetry but as opportunity symmetry: the entry cost, utility payoff and retake time of the two sites must sit in the same magnitude; read attack and defense win rates per map and per site, and when the skew is large, inspect the map first (lane widths, cover, utility payoff) rather than blaming the weapons. Guidance and readability belong to map design as well: spawns, landmarks and audio-zone differentiation (locating by sound) are the map's first lesson — where each of the three lanes leads and which carries utility spots must be something a new player can sketch for themselves within a few matches.

### 3.5 Matchmaking, Competitive Systems and Anti-Cheat

The competitive system is one chain: matchmaking decides the daily experience, ranks and seasons decide the sense of purpose, and tournaments and platform ecosystems set the ceiling for population and content.

- **Matchmaking**: separate the hidden rating from the displayed rank; give newcomers a pool and returning players a buffer; write the party and solo-queue pool rules down first. Tactical-shooter matchmaking is especially sensitive to communication quality — differences in voice use and information discipline get amplified at low ranks (for methods see Multiplayer & Backend §4).
- **Ranked and tiers**: seasonal structure, promotion and demotion, placement and skip rules must be explained clearly; players' trust in the ladder is part of this genre's long game.
- **Tournament ecosystem**: from community cups and third-party platforms to official leagues; spectating and broadcasting are the amplifier — first self-check "is the match understandable to watch" (how utility, clutches and economy read on screen), then talk about running events (Esports & Competitive Design §5, §7). Version stability is the floor: players' tactic libraries and muscle memory accumulate per version, and heavy mid-season changes are a cardinal sin (Esports & Competitive Design §2).
- **Anti-cheat**: under a short TTK cheating pays extremely well (one bullet is one life, one detection rewrites a round); client detection, server-side behavior statistics and manual report review — all three layers are indispensable; replays are the shared foundation for both review and spectating (Multiplayer & Backend §7). Anti-cheat is an ongoing arms race; write it into the long-term budget, not into a plug-in you install before launch.
- **The fairness red line**: decouple cosmetics from stats; freeze the build before major matches; write "when big changes are allowed" into policy instead of deciding it ad hoc.

## 4. Technical Essentials

The engineering difficulty concentrates in four places: low-fault-tolerance detection under server authority, the determinism of the utility system, replay and spectating infrastructure, and the server and operations budget. Everything below is engine-agnostic; for the full treatment of sync and matchmaking see Multiplayer & Backend, and for data-driven design and performance see the Programming Handbook.

### 4.1 Server Authority and Hit Detection

- Damage and hits are all computed on the server; the client only collects input and predicts presentation. A low TTK magnifies the cost of detection errors to the extreme: a shot that looked like a hit locally but was not counted can cost a round. Anything the server can rule on does not go to the client — this is a competitive floor, not a performance option.
- Lag compensation (hit backtracking) is mandatory: the server replays the judgment against what the player saw at the time; the backtrack window must have a cap and be publicly specified. Without backtracking, high-latency players are systematically eliminated; with no cap, low-latency players feel "killed through walls".
- Decouple the tick rate from detection frequency: beyond the server tick rate (the traditional 64 or 128), the newer approach binds shot detection to the moment of input instead of waiting for the next server frame. Either way, client prediction must stay restrained: movement leads, hits defer to the server, and deviations are smoothed out in the presentation layer.
- Peeker's advantage is a collusion between networking and level design: interpolation and latency let the player who swings out of cover see the one holding the angle first. Do not expect the network layer to fix it outright; absorb it in the level with terrain, cover depth and angles.

### 4.2 Engineering the Utility System

- Smoke, flash and fire are each a set of entities and detection models: smoke is volume and sightline occlusion, flash is a line-of-sight visibility check, fire is an area and time field. All three must be consistent across rounds (same spot, same result), or their training value drops to zero.
- Throwables render physics first but defer to the server: trajectories may be client-predicted, while landing points and effects are arbitrated by the server; interactions such as smoke extinguishing fire, counter-smokes and destructible utility are computed server-side as well.
- Manage materials in one merged table: bullet-penetrable, impenetrable, one-way (blocks players but not bullets) and utility-occluding entries live in the same table, so detection and visuals use one data set — eliminating "it looks sealed but is not".

### 4.3 Replay, Spectating and Anti-Cheat Infrastructure

- Replay recording starts in the prototype phase: review, report verification, spectating and content creation all share one set of infrastructure, and doing it late equals doing it twice (Esports & Competitive Design §3).
- The spectating system provides for a director view, slow motion and an info panel; broadcast delay isolates information (preventing stream-sniping) — set it during design.
- Data probes: log economy, utility spend, first-kill time and site per round; balance work runs on ledgers, not feelings.
- Training and custom rooms are long-term infrastructure: aim practice, utility lineups and community events all begin there.

### 4.4 The Server and Operations Budget

- Two ledgers, latency and operations: regional server placement, match pooling and cross-region merges are experience parameters (Multiplayer & Backend §8); servers, matchmaking and anti-cheat review settle monthly, behavior governance (AFKing, griefing) eats directly into retention, and review headcount goes into the budget up front.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimating scope only; not a commitment. The numbers are a ruler — calibrate them against your own team's speed.

| Tier | Scale | Time reference | Notes |
| --- | --- | --- | --- |
| Gameplay prototype | 1 greybox map, 1 round mode, room-based | 3–6 months (small team) | Validates only whether the "low fault tolerance plus round economy" round heartbeat holds |
| Small competitive title | 3–5 maps, basic ranked and anti-cheat in place | 1–2 years (small team) | Balance, servers and anti-cheat are the main bills |
| Commercial-scale tactical shooter | Multiple maps, seasonal operations and a tournament ecosystem | 3–5+ years (team) plus ongoing operations | A live-service product; anti-cheat and maps are standing bills |

Breaking down the bills:

- **Maps**: every map eats dozens to hundreds of playtest passes; change the terrain and every utility lineup is retested. The map is this genre's most expensive single asset — and half of the tactical layer.
- **Anti-cheat and security**: a continuous arms race settling monthly; the headcount for report review and false-ban appeals goes into the budget and cannot be estimated as a one-time purchase.
- **Weapons and utility**: the feel, damage and price of every gun need round after round of tuning; every utility item's interaction with a new map (where it seals, where it burns) adds test volume.
- **Economy tuning**: pull one hair and the whole body moves (change one price and every tactic is recalculated) — do not touch it without simulation and batch data tools.
- **The small team's realistic path**: scale everything down proportionally — 1–2 maps, 5v5 or 3v3, two or three utility items, room-based play and community servers first, with ranked and events later. If what draws you in is "the low-fault-tolerance mind game", validate one thing first: when a match ends, does the player want the next round immediately?

## 6. How to Start the First Prototype

Goal: build a greybox, round-based room in 4–6 weeks and validate the round heartbeat of "low fault tolerance plus economy plus utility". No ranked, no skins, no story.

1. (Week 1) Gun feel and detection. A whitebox arena plus one rifle and one pistol: server-side detection, hit feedback and kill replays in place, so that "deaths you can understand" holds first.
2. (Week 2) The round structure. Attack and defense rounds, plant and hold timers, round and half scoring, side swap; get one mode to a closed loop first.
3. (Week 3) Economy. Starting money, round rewards, loss bonus, kill rewards and a three-to-four-tier buy menu; put all economy numbers into tables, hot-reloadable.
4. (Week 4) Utility and the map. Pick two of smoke, flash and incendiary and build them fully; one symmetric sketch: two sites plus mid, with positions and routes as greybox geometry first.
5. (Weeks 5–6) Testing and review. Run 5v5 internally for three days straight and log economy decisions, utility usage and clutch handling; tune numbers and layout only — add no new systems.

Starting parameters (copy and adjust): 5v5; rounds around 100–120 seconds; buy phase around 20–30 seconds; starting money around 800; first to 13 per half; 2–3 utility types; 1 map.

Acceptance criteria (all observable):

- With all art and audio stripped out, testers still want to keep playing, in sessions of 20 minutes or more.
- Testers can say whether they lost the previous round on "economy, information or aim", rather than only "their aim was better".
- Save rounds and force rounds get seriously discussed in the debrief (the minimal evidence that the economy reads).
- Change any price or reward number and you can explain its effect on round outcomes within a day; if you cannot, the tools are not in place.
- Testers actively want another round, rather than being asked to try one more.

## 7. Common Pitfalls

1. **TTK swinging or detection opaque**: players cannot build expectations and do not know why they were instantly killed; damage sheets and kill replays come before any other polish.
2. **Economy imbalance**: the winner full-buys forever and the loser never gets a gun back, or save rounds mean nothing; loss bonus, differentiated kill rewards and the cap are all required (§3.2).
3. **Maps built as art symmetry only**: routes and timings are asymmetric and one side rolls over the other; read per-map win rates before touching weapon numbers (§3.4).
4. **Utility random or overpowered**: the same spot yields different results and its training value is zero; smoke, flash and fire detection must be predictable and counterable (§3.3).
5. **Vague information rules**: footstep loudness, through-wall visibility, shadows and light effects are undefined, and the information game degrades into guesswork.
6. **Anti-cheat built late**: under a short TTK, aimbots and wallhacks pay the best, and the ladder can be breached overnight (Multiplayer & Backend §7).
7. **Only gunplay, no tactical layer**: without maps and utility to match, the genre is indistinguishable from an ordinary FPS and the competitive ecosystem has no foothold.
8. **Matchmaking pools split too early**: new tiers, multiple modes and regions slice the population into pieces, and queue times kill the game before balance does (Multiplayer & Backend §4).
9. **No provision for spectating and replays**: tournaments, content and report review all stall on infrastructure (Esports & Competitive Design §3).
10. **Big version changes interrupting the tactic library**: heavy mid-season changes to feel and maps void everything players have accumulated (Esports & Competitive Design §2).
11. **Treating "difficulty" as the selling point**: without tutorials, a training range and a newcomer pool, only a tiny hardcore audience stays.
12. **Payments coupled to power**: selling power is self-evidently unfair inside a ladder, and competitive trust burns out in one go.

## Further Reading

- Game Design Handbook §2, §4: core loops and the number-table method — the source draft behind §3.2's economy system.
- Programming Handbook: data-driven design, hot updates and performance methodology — the companion to §4 of this page.
- Multiplayer & Backend §2, §4, §7, §8: sync models, matchmaking, anti-cheat and cost operations — the expansion of §3.5 and §4.
- Esports & Competitive Design §2, §3, §5, §7: patch stability, spectating systems, tournament ecosystems and event self-checks.
- Level Design Handbook: metrics and guidance for routes, cover and utility spots — the expansion of §3.4.
- Pitfalls & Anti-patterns and Indie Survival: high-frequency pitfalls and scope control, complementing §5 and §7.

Exercise: pick a public recording of a tactical-shooter match, log the economy, utility spend and first-kill timings round by round, and find which rounds' economic decisions rewrote the match; then play three matches yourself and write down the "three most expensive mistakes" of each.

The tactical shooter looks like it sells aim, but what it actually sells is judgment and accumulation "before the firefight": aim is the ticket in; information, economy and coordination are how you win.
