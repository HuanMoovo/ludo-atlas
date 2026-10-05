# Ludo Atlas · Genre Handbooks · Space Sim

> **Genre Handbooks · Volume 3**. Positioning: the category that makes "piloting a ship around the stars and making a living at it" the first pleasure. Flight game feel and a sense of scale are the foundation; trade, mining, combat and exploration provide the long-term goals; players run their own slice of galactic life from the cockpit.
> Companions: Game Design Handbook (core loop and economic balance) · Programming Handbook (coordinate systems, scale and streaming) · Production Handbook (scope control and milestones) · Indie Survival (the reality slice for small teams).

---

## 1. Positioning and Core Loop

In one line: space sim is the genre **whose first pleasure is piloting a ship between the stars, surviving and building a livelihood**. Players build command of their ship through inertia, scale and instruments, and run a galactic business through trade, mining and combat; the ship is not a means of travel — the ship is the content.

The core loop, written as a verb chain:

`set a goal (mission, cargo manifest, coordinates) → take off and leave the station → fly within the system → jump between systems → act on arrival (trade, mine, scan, fight) → settle profits and risks → return to port for refits and upgrades → set the next goal`

This loop is measured in one trip, and a trip runs from a few minutes to a few hours. It holds on just two preconditions: flight feedback you can trust (§3.1) and scale handled with care (§3.2). A true-scale star system is empty for most of its playtime; translating that emptiness into pacing is most of what this page is about.

Drawing boundaries against neighboring genres:

| Neighboring genre | Boundary |
| --- | --- |
| Vehicle sim (ground) | Both have a cockpit and a hauling loop; ground driving is constrained by road networks and gravity, while space is all-directional motion with no roads — and almost no way to stop. |
| 4X and space strategy | The strategy layer moves fleets and never flies by hand; the space sim's first scene is the stick and the instruments in the cockpit. |
| Arcade space shooter | Clearing the screen and bullet-hell patterns are the core pleasure and flight is only the stage; in a space sim, navigation and the economy are themselves the content. |
| Survival building | The same sky with two centers of gravity: one on "fly and haul", the other on "survive and build"; works on both sides have stitched the other in. |
| MMO | Space subjects very often go online; room worlds and persistent worlds keep different books, so read Multiplayer & Backend first for the form question. |

A self-check question: replace the ship with one-click fast travel from a menu — what is left of the game? If the answer is "nothing left", you are making a space sim; if a whole management or strategy game is left, you are writing a different page.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **A sense of flight control**: the ship drifts, veers and overshoots, but every accident can be explained as your own input; losing control is a skill problem, not a game problem.
2. **Awe of scale**: planets grow slowly in the view, starlight slides past the porthole; "big" has to be felt, not read.
3. **Making a living in the galaxy**: every trip shows on-the-books progress; cargo holds, hulls and account balances are the evidence of time.
4. **The unknown and discovery**: the nav chart keeps producing new signals, new routes and new accidents; curiosity is the long-term fuel.
5. **Low-pressure failure**: ships blow up, but you can afford to blow up; insurance, saves and rebuild paths keep the next adventure cheap.

Benchmark titles (widely known works only; play them yourself before breaking them down):

| Title | What to learn from it |
| --- | --- |
| Elite Dangerous | Speed tiers under a 1:1 galactic scale: normal flight, supercruise and jumps each doing their own job. |
| No Man's Sky | The density lesson of procedural galaxies and years of iteration: turning "infinite" into "playable" step by step. |
| EVE Online | The long-term shape of a player economy and territorial politics; how a large world produces content out of its players. |
| Star Citizen | The cost boundary of ship-simulation detail and seamless-world ambition; a reality sample of content delivered in stages. |
| Kerbal Space Program | Orbital physics as the gameplay itself; translating formulas into instruments, sound and feedback. |
| Outer Wilds | A density sample of a handmade solar system; a twenty-some-minute loop that compresses scale and pacing into place. |

## 3. Design Essentials

### 3.1 Ship Game Feel and Multi-Degree-of-Freedom Controls (the Simplified Scheme)

The biggest difference between space flight and ground driving is **all-directional motion**: beyond pitch, yaw and roll there are three translation axes, plus throttle and reverse thrust — six degrees of freedom that can move at once. Opening all of it to hardcore players is a gift and handing it to newcomers is a way to get them lost; the default state must simplify.

| Dimension | Default simplification | Switch left for advanced players |
| --- | --- | --- |
| Steering | "Airplane-style" flight: pitch and roll carry the turns, yaw is weak | Independent yaw and a full 6DOF mode |
| Inertia | Automatic drag: release the stick and speed falls back toward the nose | Decoupled mode: accelerate only toward the nose and keep drifting |
| Takeoff and landing | Auto-align, auto-land, speed-limited corridors | Manual approach and deck landings |
| Attitude reference | HUD artificial horizon, velocity vector indicator, target box | Reduced assists, pure instrument flight |

Two disciplines:

- **Rebuild every directional reference in vacuum.** There is no ground and no horizon, so players live on the HUD: velocity vector, target direction, an up/down reference and proximity warnings are all non-negotiable; without references, players cannot tell roll from yaw, and motion-sickness complaints follow.
- **Guarantee "can stop" and "can get there" first.** A newcomer must be able to learn to slow to docking speed and stop cleanly within 30 seconds; chases, dogfights and drift turns are rewards for later.

A feel for the numbers: combat speed and travel speed differ by two or three orders of magnitude, and each speed tier gets its own controls and camera behavior; lock down three numbers first — acceleration, turn rate and braking distance — put them all in the balance sheet and support hot-reloading. Acceptance criterion: have 5 people fly for 20 minutes each; "getting disoriented or hitting something you should not" happens no more than 2 times per person, and after losing control they can say where their input went wrong.

### 3.2 The Art of Scale (Handling Star-System-Scale Distances and Speeds)

True scale is this genre's first math problem: planet diameters run in tens of thousands of kilometers, planet spacing in tens to hundreds of millions, and a ship crossing one trip at true acceleration would leave players waiting for hours. There are only three ways to handle it:

| Route | Approach | Cost | Common example |
| --- | --- | --- | --- |
| True scale with speed tiers | 1:1 distances, with multi-tier engines such as supercruise and jumps compressing the time back | Navigation and instrument systems grow complex; the learning curve is steep | Elite Dangerous |
| Compressed scale | Minutes between planets; the system folds into "a set of city blocks" | The awe of scale is discounted and patched with art and staging | No Man's Sky |
| Handmade solar system | One system only, with sizes and orbits hand-tuned to a good rhythm | Total content volume is limited; depth has to cover for breadth | Outer Wilds |

The general method is to design by **trading distance for time**: never ask "how many kilometers between these two points", only "how many seconds does it take the player to get from here to there, and what happens in those seconds". Common pacing: a hop between two points in-system, 30 seconds to 3 minutes; an inter-system jump, a 10-to-60-second transition or tunnel; landing and leaving port, 5 to 20 seconds. Align the speed tiers with this seconds table, not with physical constants.

Two disciplines:

- **Celestial bodies have to look like they are moving.** Planets must change in the view at a slow, naked-eye-perceptible angular rate, with the star's position and light moving in step; a completely static backdrop looks like wallpaper and the sense of scale drops to zero on the spot. The implementation ceiling is low: distant parallax, light angle and a rotation texture are enough.
- **Give speed a scale.** The three tiers — normal, supercruise, jump — must be tellable at a glance from instruments, sound and camera behavior, and players must know which tier they are in and why they cannot use a higher one (gravity wells, traffic lanes, fuel, overheating); the tiers themselves are the gameplay.

### 3.3 Economy and Exploration Loops (Trade, Mining, Combat)

The four activity types share one skeleton and differ only in what they trade time for:

| Activity | What one trip involves | Sources of risk | Form of return |
| --- | --- | --- | --- |
| Trade | Buy low and sell high; plan routes and cargo capacity | Pirates, tariffs, price swings | Cash from steady margins |
| Mining | Scan deposits, extract, refine, sell | Environment (heat, radiation) and raiders | Cash plus rare materials |
| Combat | Escort, clear out, bounty hunt, convoy | Enemy fire, repair bills, insurance | Bounties and drops |
| Exploration | Scan unknown bodies and signals, register discoveries | Fuel, supplies, no backup | Registration fees and codex progress |

Design discipline:

- **One balance budget runs all four activities.** Cargo, armor, engines and fuel share one weight and money budget: haul cargo and you fly slow, mount heavy guns and the cargo will not fit. While the trade-offs hold, the four activities explain each other; once they disappear, players find the optimal build in a day and the other three paths are void.
- **The mission board is a content generator.** Delivery, escort, clearing, mining and passenger runs are all written as templates, assembled from origin, destination, quantity, time limit and pay; hand-written missions are reserved for the main line and tutorials. Templates need foolproofing: reachable destinations, generous time limits, no penalty for declining.
- **The first perceptible income has to land in the first 30 minutes.** After the first cargo sale or the first bounty payment, players must be able to say right away "how much is still missing for the next ship".
- **Exploration has to settle.** Completed scans, body registrations and selling coordinates are all actions that turn "seeing" into "progress"; exploration without settlement degrades into screenshots.

Economy check: run the early curve at real time length and confirm what ship a player at hour 1, hour 10 and hour 30 respectively gets to fly; design insurance and repair fees as money sinks in the same pass, so one wipe does not zero out three hours of progress.

### 3.4 Density and Interest in World Generation

The biggest lesson of procedural galaxies comes from No Man's Sky's launch: the scale was infinite enough, the density was not interesting enough, and players learned "it is all the same" after ten planets. The fix is not a bigger generator but **density design**:

- **Density is defined on the trip, not in the galaxy.** The key metric is "how many interactables per minute of flight"; a suggestion: at least one signal, event or scannable body within any 2-to-5-minute stretch, and any dead window longer than 5 minutes needs a reason (supply lines, mood stretches, a long haul the player chose).
- **Handmade anchors plus procedural fill.** Main-line stations, landmarks and anomalies are placed by hand; procedural generation handles terrain, color, resources and random events. All-handmade cannot be afforded and all-procedural does not live long; set the ratio by team size, and at the start err toward more handmade.
- **Points of interest come from a template library.** Six base types — derelict stations, debris fields, pirate nests, convoys, anomalous signals, mineral deposits — each with three to five variants; the generation rules guarantee "reachable and worth a look" as the floor and surprise as the goal.
- **Keep promotional numbers apart from experience numbers.** "How many billion planets" is a tagline, not content; the number you are accountable to players for is "how many memorable places they meet in the first hour". Write milestone acceptance against the latter.

### 3.5 The Reality Slice for Small Teams (2D or Simplified 3D)

A full-3D, 1:1-scale space sim with seamless atmospheric entry is a hundreds-of-person-years engineering effort, and a small team aiming straight at it is handing itself a death sentence. There are only a few viable slices; pick one and take it all the way:

| Slice | Approach | What it saves | What it costs |
| --- | --- | --- | --- |
| 2D top-down | Space flattened into a plane; combat and trade unchanged | Rendering, physics and assets all drop an order of magnitude | Flight feel and scale awe are discounted; strategy depth has to cover |
| Single-system 3D | One handmade solar system, no interstellar travel | Galaxy generation and jump systems are skipped entirely | Total content volume is limited; system depth has to cover |
| Simplified 3D with segments | Systems are separate skybox boxes; jumps and entry switch via loading | Seamless engineering and art costs drop sharply | Immersion is discounted; staging and sound have to cover the transitions |
| Short-session structure | A session of tens of minutes; blow up, restart | Long-term economy and saves are off the table | The payoff of long-term operation is discounted; per-session builds have to cover |

Suggested scope-cutting order, heaviest first: multiplayer, planet-surface content, interior walking, seamless atmospheric entry, number of ship types. Once the ship's flight feel holds, everything else can grow in time; if the feel does not hold, everything else was wasted.

## 4. Technical Essentials

The engineering difficulty concentrates in four places: coordinate precision, physics under speed tiers, the procedural galaxy pipeline, and sound and information design. The following is engine-agnostic; for method details see the Programming Handbook.

**Coordinate systems and floating-point precision**

- Large coordinates are engineering debt number one: single-precision floats start to jitter at 10-km-scale coordinates, and hundred-million-kilometer systems demand the trio of double precision, floating origin and camera-relative rendering; run physics and rendering on separate ticks, with the presentation layer collecting camera-relative transforms every frame. Adopt it at kickoff — swapping coordinate systems later equals redoing the whole project.

**Speed tiers and physics**

- High and low speeds use different modes: normal flight runs full collision and inertia simulation, while supercruise and jumps switch to "navigation intent" input and skip per-frame physics, with the switch points covered by masks, sound and camera behavior; pick one inertia implementation — kinematic, which favors feel, or Newtonian, which is realistic and hard to control — and never mix the two on one ship.
- Anti-tunneling at speed: asteroid fields and stations need continuous collision detection or substepping at high speed, or ships pass through station hulls at will; low-speed precision scenarios such as docking and landing get validated separately under a fixed timestep.

**The procedural galaxy pipeline**

- Worlds generate from seeds and must be reproducible: the same seed gives the same planet on any machine, and testing, bug-fixing and saves all depend on it; points of interest are first laid out in bulk by rules and then filtered by hand, with the distribution data archived for regression checks.
- Celestial bodies are tiered by distance: a distant sphere with a texture, a landscape layer once you close in, surface data after landing; each tier has its own cache and performance budget.

**Sound and information design**

- Space has no sound, but games need it: the common practice is "structural sound heard from inside the cockpit" — engines, alarms, groaning metal and comms are all present, hiding information in the sound layer; silence itself is an asset, used at ritual moments such as jumps.
- Alarms and the HUD both need tiers: proximity, lock-on, overheating and full cargo separated by different tones and channels; five readings — velocity vector, target, route, fuel and cargo — live on the HUD permanently, with the rest expanding on demand. Long-haul players will turn the music off, so alarms must cut through any mix settings; test instrument layouts in greybox first, and do not wait for the art pass to discover that nobody can read them.

## 5. Content Volume and Workload Reference

The following are common magnitudes for comparable projects, for scope estimation only and not a commitment.

| Project shape | Content scale | Time reference | Notes |
| --- | --- | --- | --- |
| Flight prototype | One ship plus one greybox system | 2–6 weeks | Validates feel, scale and the HUD only |
| Small complete title | 1 system, 3–5 ships, one trade line and one combat line | 4–9 months | Trades content breadth for system depth |
| Common indie scale | 5–20 systems (or procedural generation), 8–15 ships | 1–3 years | The content pipeline and balance take the bulk |
| Commercial scale | A 1:1 galaxy or seamless planets, dozens of ships | 3+ years | Teams in the hundreds; not a fair benchmark |

Cost breakdown: a ship "at release quality" equals hull and cockpit (if included), engine and weapon effects, a sound signature, and a flight parameter set with balance; reusing one chassis with new looks and sound cuts cost significantly, but the parameters are still one set per ship. One system's cost equals its celestial bodies, stations, NPC traffic, events and mission templates; extrapolate system count as "a few weeks each", not as a geometric multiplier. Scheduling anchors: building a playable feel prototype from zero takes 2–6 weeks; a vertical slice (one system, one full economic line, one combat encounter) usually takes 2–4 months; after that, extrapolate as "system count multiplied by a polish factor". The thing most likely to run away in a procedural galaxy is not the generator but the filtering and hand-dressing after generation.

## 6. How to Start the First Prototype

The first prototype has only one ship, one greybox system and one economic line, done in 2–6 weeks, touching no story, no multiplayer and no planet surfaces.

**Weeks 1–2: single-ship flight.** An empty box with a ball (a fake planet), a station and an asteroid belt; make §3.1's simplifications and switches and §3.2's speed tiers all adjustable and hot-reloadable. Ugly is expected at this stage.

**Week 3: one economic line.** Buy cargo at a station, fly to another station to sell it, settle cash, upgrade the cargo hold once; add scanning and a target box to the HUD. The goal is a complete chain; rough numbers are fine.

**Week 4: one layer of pressure.** Add one pirate enemy or one mining site (just one), plus mission-board templates; tune feel from recordings and have 3–5 people who have never played watch for when they get lost, when they get bored and when they want one more trip.

**Weeks 5–6: tuning and acceptance.** Fix HUD and sound feedback, run the early economic curve once, and change only parameters and pacing — add no new systems.

Success criteria (all observable):

- With all art and audio stripped out, testers still want to fly the same route repeatedly, typically 15 minutes or more per session.
- At least 4 of 5 testers complete the full flow — take off, jump, buy, sell, upgrade — without verbal guidance; "disorientation" complaints run no more than 1 per person.
- For any one flight parameter you change, you can quantify its effect on flight within 5 minutes; testers can say "how much is still missing for the next ship", and someone asks for one more trip on their own rather than being asked to try again.

If feel and scale do not pass, do not start laying out systems; systems are this genre's most expensive content, and one round of rework breaks bones.

## 7. Common Pitfalls

1. **Copying true scale as is**: no speed tiers and no scale compression, so players stand around for hours between planets; design distance as time (§3.2).
2. **All 6DOF with no simplification**: newcomers get disoriented and quit within ten minutes; simplify the default state and put the advanced switches elsewhere (§3.1).
3. **No references and no HUD in space**: players cannot tell roll from yaw, and motion sickness and frustration erupt together; directional reference is a floor requirement.
4. **A procedural galaxy with infinity but no density**: aesthetic fatigue sets in by the tenth planet, and the bigger the galaxy the worse the reputation (§3.4).
5. **Seamless obsession**: atmospheric entry and interior walking casually eat half the schedule; build in segments first, and only consider seamless once the fun is validated.
6. **Four activities siloed**: trade, mining, combat and exploration each upgrade on their own, and players lock into one path after five hours; share one balance budget (§3.3).
7. **Floating-point precision discovered late**: coordinates jitter hundreds of millions of kilometers out, station hulls flicker, and the coordinate system has to be redone in the closing phase; adopt double precision and floating origin at kickoff.
8. **Nothing accompanying the trip**: long flights with no radio, no comms and no events, and players idle on their phones; every dead window needs a reason (§3.4).
9. **Treating multiplayer as the default**: the books for servers, synchronization and economic security are far beyond what you imagine; validate the gameplay single-player first and charter multiplayer as a separate project.
10. **System count as the selling point while actions get no receipt**: advertising "a thousand systems" where every one is empty, and players see through it in a day; mining without refining and scanning without registering leave every step without a receipt; do the math as "a few weeks of polish per system" (§5).

## Further Reading

- Game Design Handbook: the base document for core loops, balance sheets and economic curves — cited in several places in §3 here.
- Programming Handbook: method details for coordinate systems, streaming and performance budgets — the full expansion of §4.
- Production Handbook: milestones, scope control and the outsourcing process — read alongside §5.
- Indie Survival: scope control and reality accounting for small teams — read before picking a slice (§3.5).
- Case Studies: methods for breaking down success and failure cases — a reference when dissecting procedural and world-scale subjects.
- Pitfalls & Anti-patterns: high-frequency pitfalls on the kickoff and technical sides — a complement to §7.
