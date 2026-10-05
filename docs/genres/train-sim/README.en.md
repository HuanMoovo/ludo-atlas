# Ludo Atlas · Genre Handbooks · Train Sim

> **Genre Handbooks · Volume 4**. Positioning: the genre that makes "driving a train and running a route to timetable" itself the primary pleasure. Players build trust in machinery and institutions through operating procedures and signal rules, cash in results through punctuality and stopping precision, and take journey atmosphere from the scenery along the line; driving is not a means of getting somewhere — driving is the content.
> Companions: Game Design Handbook (core loops and scoring design) · Programming Handbook (train dynamics, streaming and performance) · Modding & UGC (route and rolling-stock workshops) · Indie Survival (scope control and scheduling).
> This page carries no external links; benchmark titles are widely known works only, and the numbers are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: train sim is the genre **with a realistic operating loop as its primary pleasure**. Its uniqueness is assembled from three things: driving under track constraints, a rules system made of timetables and signals, and scenery that keeps flowing past the window. Without the last two, a title slides toward vehicle sim; without the first, it slides toward transport management. The core loop, written as a verb chain:

`sign on and take over the train → prepare and inspect → depart → cruise under traction → watch signals and speed limits → brake to a stop on the mark → open doors and exchange passengers → depart on time again → hand over at the terminus and settle`

This loop is measured in runs; a run lasts from 10 minutes to several hours. It stands on only two preconditions: operating feedback must be believable (§3.1), and the timetable and signals must be readable (§3.1, §3.2).

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Vehicle sim (trucks, buses) | The same realistic skeleton; trains add a layer of track constraints and signal rules, steering is decided by the route, and braking distances are an order of magnitude longer |
| Transport and railway management | Management does network planning and dispatching and the player never steps into the cab; in train sim the primary scene is always the cab |
| Racing | Racing compares lap times and placings; train sim compares punctuality, stopping precision and smoothness |
| Open-world driving | Driving is a means of movement; in train sim the operating flow is the entire gameplay |

A self-check question: take away free route choice, opponents and management panels until only one track, one timetable and one signal system remain — does the game still hold up? If the answer is "yes", what you are making is a train sim.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **The ritual of procedure**: preparation, departure, notching the handle, stopping on the mark — every action has a clear order and feedback, and players gain a sense of control from "doing things by the book".
2. **Punctuality and stopping precision**: the timetable is a judge you carry with you; catching up on delays, clocking in on the dot and metre-level stop-mark accuracy provide clear practice payoffs and a source of excitement.
3. **Journey atmosphere**: scenery along the line, day-night and weather cycles, on-board announcements and the flow of passengers make up the emotional value of "spending a stretch of the trip by the window" (§3.3).
4. **Low-pressure failure**: delays, overshooting and accidental signal mistakes must have a cost, but a recoverable and retryable one; long-haul runs must allow save points.

Negative feelings (any one of these is a red flag): one keypress for the whole run; a timetable that might as well not exist; a blank void outside the window; one mistake wiping out an entire run's progress.

Benchmark titles (play them yourself before breaking them down):

| Title | What to learn from it |
| --- | --- |
| Train Simulator series | The long-tail model of routes and rolling stock split into content packs, with missions and free driving side by side |
| Densha de GO!-style titles (Japanese train operation sims) | The closed scoring loop of punctuality and stopping precision, low-barrier controls and tiered evaluation |
| Train Sim World series | The immersion of the first-person cab, streaming a corridor world and platform life |
| Microsoft Train Simulator (a historical title) | The early path of realistic operating procedures and community-made expansion content |

## 3. Design Essentials

### 3.1 The Realistic Operating Loop: Timetable, Signals, Procedures

The operating loop is held up by three pillars; each pillar is both a rule and content:

| Pillar | What the player reads | Failure mode | Forgiving design |
| --- | --- | --- | --- |
| Timetable | Arrival and departure times, passing times, connections and turnarounds | Delays accumulate, connections are missed | Leave recoverable slack; score across the whole run, never reset mid-way |
| Signals | Aspects, speed-limit boards, block sections, the vigilance device | Passing a red light triggers emergency braking | The tutorial tier gives previews and soft prompts; the realistic tier is fully manual |
| Procedures | Preparation and inspection, brake-handle notches, traction notches, door operation | Wrong order of operations, forgetting to release the handbrake | A checklist that can be toggled; procedure errors only cost points, never block progress |

A run is settled on five things, all quantifiable: punctuality (arrival and departure deviation, in seconds), stopping position (stop-mark deviation, in metres), smoothness (constraints on acceleration, braking and longitudinal jerk), energy consumption (an optional advanced item) and safety (signal and speed-limit violations). Scoring tiers (tutorial, standard, realistic) are player options, not fixed to full realism from the start. Four accompanying rules:

- Layering: the default tier carries assists (automatic braking, signal prompts) and the realistic tier is fully manual; both must be fully playable — do not turn realism into a punitive option.
- Predictable beats correct: a real train's braking curve can be unwieldy in a game; players want rules they can learn, not an engineering simulation report.
- Three things in sync: if the handle notch, the gauge needles or the audio feedback lag anywhere, realism turns into guesswork; scoring and scene scripts read one shared data set (§4).
- Acceptance: have 5 people run the same service; on the tutorial tier at least 4 must complete it independently and be able to say which scoring item lost them points, and why.

### 3.2 Route and Rolling-Stock Content: The Content-Pack (DLC-Style) Model

Train sim burns through content fast: once a route is mastered, what players want is new routes, new rolling stock, new timetables. Content splits into four categories, each with its own cost and purchase motive:

| Content type | Cost magnitude | Purchase motive | Reuse relationship |
| --- | --- | --- | --- |
| Route pack | Highest (lineside assets and timetables) | New geography, new scenery, new challenges | Combined with compatible rolling stock for old trains on new routes |
| Rolling-stock pack | High (exterior, cab, sound, physics) | New driving feel and beloved classic trains | Combined with compatible routes for new trains on old routes |
| Mission and timetable pack | Low to medium (writing and testing) | Operating challenges with goals and stories | Reuses the same routes and rolling stock |
| Livery and sound pack | Low | Collecting and personalization | The reusable piece across all content packs |

- Combination matrix and data-driven design: routes and rolling stock each maintain compatibility tables, and the multiplicative value of content packs comes from combinations; route topology, signals, timetables and vehicle parameters are all data files, and content packs and community mods share one set of loading and editing tools (§3.4).
- Launch content volume decides everything: one route plus one train is prototype scale; ship too few routes and trains and the first line of the reviews will be "not enough content".
- Brand licensing: real railway operators, rolling stock and service names and liveries carry licensing costs; when the budget is short, fictional liveries and invented brands are the common workaround.

### 3.3 Cameras and Sightseeing: Half the Game Is Out the Window

Train sim sells driving for half its value and sightseeing for the other half; the camera system is where the two meet:

| Camera position | Purpose | Design points |
| --- | --- | --- |
| First-person cab | The main operating view, carrying immersion | Eye point close to the driver's position; readable gauges; head shake must be filtered — steadier beats shakier |
| External chase | Checking the train consist, sightseeing | Multiple position presets (side, low angle, rear); camera tangents while cornering and entering stations |
| Free camera | Screenshots, scouting the line, enjoying the view | Supports pause and free flight; a must-have for sightseeing players, not a debug feature |
| Passenger and platform views | Atmosphere and the railfan's perspective | Carriage interiors match the view outside; watching trains arrive and depart from the platform, reproducing real services in step with the timetable |

- Landmark density: every few minutes needs a memorable viewpoint (a bridge, a mountain pass, a city skyline, platform life); a route without landmarks is forgotten as soon as it is over.
- Sense of speed and weather: the sense of speed comes from the density of reference objects (catenary masts, parallel roads, houses), not from gauge numbers; the same stretch of line on a rainy night and on an early morning are two different routes, so weather switching must be convenient.
- Sightseeing mode: the combination of free camera, pause and photo mode; screenshots and videos are this kind of title's cheapest promotional assets.
- Acceptance: over a 10-minute trip, testers can name at least 3 landmarks along the line, and someone voluntarily uses the free camera to take photos.

### 3.4 Community and Content Workshops

Genres that burn through content live on their communities: route editors, rolling-stock and livery mods, timetables and mission scripts are this kind of title's healthiest long tail. The methods follow the Modding & UGC:

- Support tiers progress from L0 to L3: open data (parameters, liveries) → official toolchain and API → platform distribution (Steam Workshop) → a full editor; the community's ceiling depends on how far the official editor is opened up.
- Version-compatibility discipline: official updates breaking mods is the norm; a test branch that lets authors adapt early cuts the losses significantly (the workshop version-control scheme in the Modding & UGC).
- Moderation and operations: fan works of real routes and trains involve trademarks and licensing, so the platform side needs moderation, takedown standards and an appeals channel; featuring and charts give creators exposure, and cross-promotion with top authors is the most effective growth lever in a niche community.

### 3.5 Small-Team Angles

Without building a big network or a big rolling-stock roster, small teams have three realistic paths:

| Angle | Gameplay core | Content volume | Fits |
| --- | --- | --- | --- |
| One route, done deep | High-fidelity recreation of a single route (geography, timetable, service research) | 30–90 minutes of journey, 1–2 trains | Teams with a railway background or research skills |
| One system, done deep | One major system taken to the finest detail in the genre (signals, braking and train dynamics) | A few routes plus system depth | Technically minded, aimed at hardcore audiences |
| Experience-driven | Low-barrier controls with strong atmosphere (night scenes, snowy country, commuter drama) | One main route plus several vignettes | Aimed at a broad audience, valuing sightseeing and narrative |

Shared discipline: ship one route done in full (timetable, missions, scoring, sightseeing), be data-driven from day one, and fill the long tail with community content rather than overtime.

## 4. Technical Essentials

The engineering difficulty concentrates in four places: the data model for routes and signals, train dynamics, the corridor world, and audio and peripherals. Everything below is engine-agnostic; for detailed methods see the Programming Handbook.

**Track, signals and timetables**

- Model the route as "a directed graph plus mileposts": segments carry curvature, gradient, speed limits and cant; switches are nodes of the graph; signals are data-driven rule sets hung on edges, and block occupancy, speed limits and vigilance triggers all read from route data.
- The timetable is the single source of truth: AI traffic, signal clearing, mission scripts and final scoring read one shared data set; three data sets each telling their own story is the most common engineering debt in this kind of project.

**Train dynamics**

- Start with a simplified model: an approximation of longitudinal forces (traction, braking, gradient and curve resistance, air resistance) plus visual articulation of multiple cars — a single rigid body with trailing cars is a common approach; use a fixed timestep decoupled from rendering, and validate separately the low-speed stop-mark phase, which is the most sensitive to timestep.
- The realistic direction then adds per-car longitudinal forces, coupler slack and brake-pipe pressure propagation; longitudinal jerk in heavy long consists is deep water — validate before building.

**The corridor world and streaming**

- A railway is a natural corridor: stream it in spatial chunks along the line, with low-poly models and billboards in the distance; budget around "seeing the trackside clearly", not "seeing far".
- Stations and urban sections are the density peaks: the most expensive assets and the greatest performance risk — establish a standard-parts library for platforms and station buildings first; world size is a product decision, and changing it late means redoing the whole map (the same cost discipline as Genre Handbooks · Vehicle Sim).

**Cameras and audio**

- Decouple the cab camera from the physics frame and filter it; external and free cameras support pause, variable speed and multiple position presets.
- Audio has three layers: traction and braking (motors and diesel engines, converter tones), track and wheelsets (joint rhythm, switches), and ambience and announcements (wind, rain, stations and on-board announcements); half the sense of speed is carried by sound, and on-board announcements and station-name calls are the highest-value atmosphere layer — a set of station-announcement sounds costs far less than laying one more kilometre of track.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimating scope; not a commitment.

| Project shape | Content magnitude | Timeline magnitude | Notes |
| --- | --- | --- | --- |
| Prototype | One 5–10 minute branch line plus one train | 2–4 weeks | Validates only the operating loop, scoring and stop-mark braking |
| Small complete title | A single route of 20–40 km, 2–3 trains | 4–9 months | Sightseeing assets and timetables are the bulk of the cost |
| Typical indie scope | A single route or region of 60–150 km, multiple trains | 1–3 years | Route mileage is usually the single largest budget item |
| Large live-service operation | A multi-route network with content packs added continuously | 3+ years | The content-pack cadence is the operating cadence |

Cost breakdown: one kilometre of release-quality route equals track and catenary, lineside scenery and landmarks, stations and platforms, signals and level crossings, timetables and missions, and density cost in suburban sections is far above open country; rolling-stock cost equals exterior models, cab, sound, physics parameters and liveries, and deriving variants within a family cuts costs significantly, but the cab and sound are still one set per train. Scheduling anchors: zero to vertical slice (a 10–20 minute route plus one train plus a complete scoring chain) is usually 2–4 months, after which you extrapolate by "route mileage times a polish factor"; routes are the most expensive content to redo, so anything that can be done later should not be done earlier. The estimation and scope-control methods of the Production Handbook apply here directly.

## 6. How to Start the First Prototype

The first prototype covers one route, one train and one complete run, finished in 2–4 weeks, without touching a large map, multiple trains or a content-pack system.

**Week 1: the train and a short line.** A 5–10 minute branch line with two to three stations, one train, simplified longitudinal dynamics, a cab camera plus one external position. Keyboard-playable, with assisted braking on by default. Ugly is expected at this stage.

**Week 2: the operating loop.** Departure, cruising, one signal and one speed limit, braking to a stop on the mark, opening doors and exchanging passengers, clocking in — the whole chain running end to end; start scoring with a crude formula (punctuality and stop-mark accuracy are enough), with the emphasis on a complete chain.

**Weeks 3–4: timetable, sightseeing and tuning.** Add a set of arrival and departure times and one meet with an AI train to the timetable; place 3 to 5 landmarks along the line; bring traction and braking sound up to two sampled layers; use frame-by-frame recording to tune the feel of braking and stopping on the mark. Find 3–5 people who have never played it and watch when they look out the window, when they look at the timetable, and when they curse; change only parameters and route layout — add no new systems.

Success criteria (all observable):

- With all art and audio removed, testers still voluntarily run another trip (rather than being asked to try again), usually 10 minutes or more each.
- At least 4 of 5 testers complete a run with no verbal guidance; on the tutorial tier, "can't stop on the mark" complaints are at most 1 per person.
- Testers can say which scoring item lost them points, and why.
- Change any one physics parameter, and you can quantify its effect on braking and stop-mark accuracy within 5 minutes.

If the stop-mark game feel and the scoring loop do not pass, do not start laying routes; the route is the most expensive foundation in this genre (§5).

## 7. Common Pitfalls

1. **Wanting a big network and a big rolling-stock roster**: matching the content volume of a major studio is the classic way this kind of project crashes (§5); validate with one route first, then talk about expansion.
2. **Physics taken to either extreme**: a fully accurate model is undrivable, pure animation has no feel; take the predictable middle layer, with assisted and realistic tiers side by side (§3.1).
3. **Timetable, signals and scripts as three data sets**: scoring says you are late, signals say you were not cleared, the script says you passed; read one shared data set (§4).
4. **Sightseeing neglected**: an empty lineside with no landmarks turns long runs into standing punishment; sightseeing is half the selling point of this kind of title (§3.3).
5. **Stop-mark judging taken to extremes**: an unguided centimetre-level requirement is torture, while stopping anywhere is a shrug-off; give the forgiving tier a guidance line and the realistic tier reference points (§3.1).
6. **Procedures piled with jargon**: throwing twenty gauges at the player with no teaching fails the mainstreaming effort at step one; teach in layers, introduce terms as they are used.
7. **A content model that is not data-driven**: it can be neither packaged as content nor modded, closing off the long tail at the source (§3.2, §3.4).
8. **Official updates breaking mods with no contingency**: community content is invalidated overnight, and losing authors is harder to replace than losing players.
9. **No save points on long runs**: a one-hour trip interrupted and zeroed will not be forgiven twice; resuming from a break is a baseline requirement.
10. **An unstable cab camera**: excessive head shake and a wrong field of view shut some players out entirely through motion sickness; steadier beats shakier (§3.3).

## Further Reading

- [Game Design Handbook](../../fundamentals/game-design/README.md): the base document for core loops, scoring and balance sheets — the full expansion of sections 1 and 3.
- [Programming Handbook](../../fundamentals/programming/README.md): the details of data-driven design, streaming and performance budgets — the companion to section 4.
- [Modding & UGC](../../pipelines/modding/README.md): support tiers, the workshop and community operations — the full expansion of §3.4.
- [Production Handbook](../../fundamentals/production/README.md): content-volume estimation and scope control, complementing section 5.
- [Indie Survival](../../../playbooks/indie-survival/README.md): scope control and scheduling discipline — read it before greenlighting a small cut.
- [Genre Handbooks · Vehicle Sim](../vehicle-sim/README.md): the closest sibling page; the boundary is nearest of all, so road conditions, peripherals and career loops are read there, and this page covers only the track and operations side.
- Assignment: greybox a 5-minute two-station branch line and write down its timetable and scoring formula (how punctuality and stop-mark accuracy convert into points); then pick a train sim you know well and record what proportions it gives to procedures, timetable-and-scoring, and sightseeing, and how its content packs are split.

Train sim does not sell transport; it sells "a train that you drive passing through the scenery on time": procedures must be believable for the timetable to carry weight, and the window must have something to look at for long runs to hold up.
