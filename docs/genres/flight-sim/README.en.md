# Ludo Atlas · Genre Handbooks · Flight Sim

> **Genre Handbooks · Volume 4**. Positioning: the genre that makes "flying an aircraft and completing a full leg" its first pleasure. The flight model and instruments are what it stands on; mission routes and scenery provide the long-term goals; in the cockpit, the player reads the sky and the ground as a map to be conquered.
> Companions: Game Design Handbook (core loops and balance) · Programming Handbook (flight physics, streaming and performance) · Art & Audio Handbook (scenery, sky and cockpit audio) · Indie Survival (scope control and cost accounting).
> This page carries no external links; benchmark titles are widely known works only, and the figures here are common magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: flight sim is the genre **whose first pleasure is flying an aircraft and completing a full leg**. The player builds mastery of the aircraft through the interplay of aerodynamics, power and instruments, and finds a sense of order in routes and missions — "flying a leg from A to B, start to finish"; flying is not a means of getting somewhere, flying is the content itself.

The core loop, written as a verb chain:

`pick an aircraft and a route → cold-and-dark startup and checklists → taxi and takeoff → cruise and navigation → approach and landing → debrief and unlocks → fly another leg`

This loop is measured in legs; a leg runs from a dozen minutes to several hours. It holds on just two preconditions: flight feedback is believable (§3.2), and the barrier matches the audience (§3.1). Three simulation tiers (three approaches sharing one skeleton, differing in how much weight the flight model carries and where the barrier sits):

| Tier | First pleasure | Flight model | Mainstream benchmark |
| --- | --- | --- | --- |
| Arcade | Immediate thrills and readable feedback | Low: simplified aerodynamics, heavy stability augmentation | Ace Combat series |
| Semi-realistic | The feel and flows of "a real aircraft" | Medium: a credible aerodynamic skeleton, togglable assists | War Thunder |
| Full simulation | Fidelity and the operating procedures themselves | High: aerodynamics and systems in full | Microsoft Flight Simulator, X-Plane, DCS World |

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Vehicle sim (ground vehicles) | Both have cockpits and a transport loop; the ground is bound by the road network while the sky is continuous three-dimensional space, with an extra vertical dimension and aerodynamics — freedom and difficulty each a tier higher |
| Space sim | Both are vehicle piloting; space has no atmosphere, swapping in six degrees of freedom and jump navigation; flight sim keeps to atmospheric logic (climb, stall, wind and clouds) |
| Racing and combat flight | One races the clock, the other races for kills; flight sim's primary arena is always control and procedure — both are only parts of it |

Self-check question: take away the map, the missions and the scenery, leaving one aircraft and one sky — does the game still hold? If the answer is "yes", you are making a flight sim; if the answer rests entirely on dogfighting, your center of gravity is no longer on flying.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Mastery**: pitch, roll, throttle and trim are gradually internalized; every accident can be explained as your own input, and a failed landing is a skill problem, not a luck problem.
2. **The journey and a sense of the world**: taxi, takeoff, cruise and approach string into one complete passage; airports, landmarks and weather assemble a believable slice of Earth; sky and ground are content, not a loading animation between two points.
3. **Sense of ritual**: cold-and-dark startup, checklists, radio calls and the landing flare — the seriousness of the procedure itself is an emotional value unique to this genre.
4. **Low-pressure failure**: crashing, drifting off course or getting lost must be punished in proportion; retrying is cheap, and replay and review are available.

Benchmark titles (play them yourself before breaking them down):

| Title | What to learn from it |
| --- | --- |
| Microsoft Flight Simulator series | The scale effect of real geographic data and global scenery; the tiered barrier of realistic operation; a mainstream wrapper that makes sightseeing a first-class gameplay |
| X-Plane series | The engineering approach to the flight model (blade-element theory); long-term cultivation of an add-on ecosystem and aircraft expansion |
| DCS World | Single-aircraft depth: cockpit interaction and checklist flows; the barrier and the payoff of study-level |
| Ace Combat series | Arcade wrapping: mission staging, wingman narrative and a low barrier to flying |
| War Thunder | A generous design running multiple simulation tiers on one server: arcade, realistic and simulator each get their own crowd |

## 3. Design Essentials

### 3.1 Three Simulation Tiers and Audience Segmentation

The three tiers differ in audience size by an order of magnitude; choosing a tier is choosing a market:

| Tier | Target audience | Control barrier | Product risk |
| --- | --- | --- | --- |
| Arcade | All players | Playable on keyboard, mouse or gamepad; a readable camera | Flying degrades into background; differentiation rests on subject matter and staging |
| Semi-realistic | Mainstream sim players | Assists toggle, procedures kept to essentials | Between two stools: sim players find it shallow, the mainstream finds it fussy |
| Full simulation | Core players willing to read the manual | Peripherals plus tutorials; demands real commitment | Narrow audience, high per-aircraft cost; failure tolerance needs finer design |

- One title can cover several tiers: turn the assists into a row of switches (auto-trim, auto-throttle, stall protection, simplified aerodynamics) — newcomers leave them all on, veterans turn them all off; the switches are the teaching ladder (§3.5), but there is only one default tier, and it sets the tone of the reception.
- Full simulation's cost is not in the physics but in the systems: every switch, every checklist, every failure mode has to be implemented and tested, and taking one aircraft to full simulation often takes years of work (§5).

### 3.2 Flight Model and Controls: Translating "Feels Like Flying" into Intuition

Flight feel shares its roots with ground driving (predictability over correctness), but adds a vertical dimension and an entire aerodynamic grammar:

| Intuition | Corresponding implementation | What breaks when it's wrong |
| --- | --- | --- |
| Lift and weight | The four forces of lift, drag, thrust and gravity; lift varies with angle of attack and speed | Without them the aircraft is a floating sprite; turns have no bank and no sense of G-load |
| Inertia and stability | Angular damping, center of gravity and trim, stability assists | Too stable feels like a tram on rails, too twitchy like a spinning top — neither builds trust |
| The stall boundary | Stick shaker, warning tone and softening controls at the edge of the envelope | With no warning, players never know they are on the line; soften it too far and it loses its teaching value |
| Ground handling | The takeoff and landing roll, crosswind correction and braking | Takeoff and landing become cutscenes, and the genre's most important two minutes lose their tension |

- Fly stably first, then talk fidelity: stability in level flight, turns and approaches comes before maneuvering limits; the stall is the first true mechanic — arcade softens or disables it, semi-realistic gives warning, full simulation reproduces the envelope and the recovery procedure, and all three tiers must cover it once in the tutorial.
- The peripherals ecosystem has a rare hardware ladder: the lowest rung is keyboard, mouse and gamepad, which must be able to complete cruise and local takeoffs and landings; the next is a joystick plus throttle (HOTAS); the full set adds rudder pedals, head tracking, multiple monitors or VR. "Playable" at the lowest barrier comes before "fun" on peripherals, and the settings menu (curves, dead zones, trim steps, key mapping) should ship with generous presets — players sharing their setups is free live-ops material.
- Keep flight-feel parameters in one tuning table with hot reloading, and fly the same leg under fixed routes and fixed weather, changing one group of parameters at a time; acceptance: take 5 people for 20 minutes each — no more than 2 "crashes that shouldn't have happened" per person, and after a crash they can say what they did wrong.

### 3.3 Missions and Route Content

Missions and routes are the engine of long-term retention: missions hand out the content, routes supply the reasons, unlocks control the order the map opens in. Missions split into four tiers:

| Mission tier | Examples | Design role |
| --- | --- | --- |
| Sightseeing and free flight | Landmark tours around the home field, valley runs | Lowest barrier, shows off the scenery, a newcomer's first leg |
| General aviation and transport | Regional passenger and cargo runs, rescue, firefighting and patrol | Steady income and route coverage — the content trunk |
| Challenge missions | Short runways, crosswind landings, night flying and low-ceiling approaches | Trades a control barrier for a sense of achievement; for skilled players |
| Campaign and scenarios | Historical missions, escort, disaster response | The vehicle for narrative and staging; sets the product's tone |

- Split a leg into five stages: planning, takeoff, cruise, approach and landing; plant one operational event in each stage (crosswind, diversion, night approach) and give each route a reason to look at landmarks and a reason to fly it (rewards and unlocks); a route with two airports and one straight line turns into commuting the second time you fly it.
- Templatize missions: assemble from seven fields — origin, destination, aircraft type, weather, time of day, objective, reward; reserve hand-authored missions for tutorials and campaigns, or hand-authoring will eat the whole content budget.
- Chain unlocks through licenses and ratings: subjects, aircraft and airports hang off ratings, and the gates are written as practical checks (e.g. "three crosswind landings in a row") rather than grinding flight hours.

### 3.4 Scenery and Airport Data: The Rules for the Biggest Cost

Scenery is the single largest expenditure on projects like these; set the rules before work starts and build the pipeline in three layers:

| Layer | Content | Approach |
| --- | --- | --- |
| Global base | Terrain elevation, imagery, water networks and roads, vegetation | Auto-generated from real geographic data; responsible for "looks acceptable" |
| Regional refinement | Cities, mountain ranges, coastlines and landmarks | Hand-made or semi-automated; responsible for "worth remembering" |
| Handcrafted assets | Runways, taxiways, lighting, terminals, landmark buildings | Hand-made; responsible for "holds up when you look closely" |

- Settle the scale decision and the data pipeline first: coverage and precision allocation (what is automatic, what is hand-made, which airports enter the handcrafted list) are fixed before work starts, with one standard for formats, coordinates and versions; changing either late means redoing the whole map.
- Airports are flight sim's "levels": players remember runways far better than they remember sky, and a change of runway direction, lighting and approach scenery is a new level; give each handcrafted airport an asset list (runways, taxiways, lighting and signage, terminal, surroundings) and manage the workload airport by airport.
- Landmark density: use landmarks as navigational signposts, aiming for at least one recognizable landmark (a peak, a river, a bridge, a city skyline) every ten to fifteen minutes of flight; a cruise with no landmarks is one players won't remember flying the next day.

### 3.5 The Teaching Curve: Turning a High Barrier into Four Steps

Aviation is an inherently high-barrier subject, and teaching is not an accessory feature but the lifeline of retention. Lay it out as four steps:

| Step | What it teaches | Acceptance action |
| --- | --- | --- |
| Foundations | Basic control: level flight, turns, climbs and descents | Complete a level turn and a climb to a specified altitude without prompts |
| Handling | Takeoff and landing: the traffic pattern, approach and flare | Three safe landings in a row |
| Navigation | Navigation and procedure: airways, radio, autopilot | Complete a full route unaided and without prompts |
| Mastery | Weather and emergencies: crosswind, low ceilings, failure handling | Land safely in bad conditions |

- One skill per page, hands-on before reading: tutorials are measured in "do it once" units, with as little explanatory text as possible; veterans can skip, and skipping is not punished.
- Checklists are both a teaching aid and a ritual: use highlighting and step-by-step guidance to teach procedure, and a completed checklist must be reviewable (which step was missed, and what followed from it).
- Failure must be reviewable: replay, telemetry and "here's what went wrong" prompts translate a crash into a lesson; failure that punishes without explaining teaches avoidance, not flying.
- Audience segmentation reaches into teaching: arcade is measured in minutes, semi-realistic in hours, full simulation in "read the manual plus long-term practice"; for the core audience, the learning process is first-class content in itself.

## 4. Technical Essentials

The engineering difficulty concentrates in three places: flight physics, scenery streaming, and the cockpit and input; the following is engine-agnostic, with method details in the Programming Handbook.

**Flight physics**

- Start from a simplified aerodynamic model: the four-force equations plus lift and drag curves, with "flies stably" as the first acceptance bar, then layer on stability augmentation, ground effect, stalls and systems; run physics on a fixed step decoupled from rendering, and validate the integration error at high speed separately.
- Make aircraft inheritable templates: the same aerodynamic skeleton with different parameters, power and cockpit can spawn a new aircraft (§5); telemetry and replay are both debugging tools and gameplay — "crashes can be reviewed" and "tweaks can be compared" are the same requirement.

**Scenery and streaming**

- Stream terrain, imagery and buildings in spatial chunks: imagery and low-poly models at altitude, detail swapping in at low altitude; plan the budget around "the runway and terrain must be sharp on approach", and airport data must finish loading before the approach; what is playable offline is a product decision — decide it before you promise it.
- Weather is a global state machine: clouds, visibility, wind and day/night all read from the same weather source; wind must enter the flight model (affecting ground speed and fuel burn) — wind that is only visual does not count.

**Cockpit, instruments and input**

- The cockpit is the primary UI: airspeed, altitude, attitude, heading, vertical speed and RPM are the core information sources — make them "readable" before "realistic"; arcade leans on the HUD, realistic tiers lean on cockpit instruments and checklists, and both need readability testing; at full simulation, cockpit interaction (clickable switches, instrument readouts) is a major cost, and every interactive element needs the trio of state, animation and sound — cut the count in whole sets.
- Autopilot and flight director are the playable simplification layer: automating the management of altitude, heading and attitude moves the player from "overwhelmed" to "managing the flight", and they are a key prop of the teaching ladder (§3.5).
- Route input through a device abstraction layer: abstract pitch, roll, yaw, throttle and trim into unified axes and actions, then do per-device mapping and presets; head tracking and VR feel immersive but double the performance budget — evaluate them as a separate milestone, and don't stuff them into the prototype phase.

## 5. Content Volume and Workload Reference

The following are common magnitudes for similar projects; for estimating scope, not a promise.

| Project form | Content scale | Timeline scale | Notes |
| --- | --- | --- | --- |
| Feel prototype | One patch of sky, one aircraft, one local route | 2–4 weeks | Validates flight feel and takeoff/landing only |
| Small complete title | One region (a few dozen airports), 2–3 aircraft | 3–9 months | Scenery and airports are the main cost |
| Typical indie scope | One country or region, 10+ aircraft types | 1–2 years | The data pipeline sets the cost ceiling |
| Global-scale title | Global data plus a set of handcrafted airports | Team-scale, multi-year | Only holds for large teams and large capital |

Cost breakdown: scenery is counted by area — each block "at shipping quality" equals imagery and terrain processing, vegetation and buildings, landmarks, plus day/night and weather variants; airports are counted per airport — each one equals runways and taxiways, lighting and signage, terminal and surroundings, plus the approach scenery. Aircraft are counted individually: exterior model plus cockpit (almost half a title at full simulation), an aerodynamic parameter set, engine and wind-noise soundbanks, and two sets of listening, inside and out; deriving from a shared skeleton cuts cost noticeably, but cockpit and soundbank are still one per aircraft. Scheduling anchor: building a vertical slice from scratch (a small region plus one complete mission chain) typically takes 2–4 months; extrapolate afterwards by "scenery area × polish factor". Scenery is the most expensive content to redo: until coverage and precision allocation are frozen, do not mass-produce a single map.

## 6. How to Start the First Prototype

The first prototype covers only one patch of sky, one aircraft and one local route, finished in 2–4 weeks, touching neither global scenery nor anything outside the mission system.

**First two weeks: fly stably first, then complete a leg.** One aircraft, one recognizable patch of ground (one runway plus two or three landmarks), a simplified flight dynamics set, and two cameras (cockpit and chase); get all five stages — takeoff, climb, cruise (one waypoint), approach, landing — running, closing the loop on "flying a leg from A to B, start to finish". Ugly is expected at this stage.

**Last two weeks: teach one person to fly, then tune and verify.** Add minimal teaching: one tutorial each for takeoff and landing; find 3–5 people who have never played, and watch when they get disoriented, when they want to quit, and what they say after a successful landing — no prompts, no explanations. Then tune feel and cameras frame by frame, try a gamepad and one joystick, and change only parameters and routes — add no new systems.

Success criteria (all observable):

- With all art and audio removed, testers still want to fly this local route again and again, a session typically running over 15 minutes.
- At least 4 of 5 testers complete a traffic pattern (landing included) without verbal guidance; "this aircraft is broken" complaints no more than 1 per person.
- Change any one aerodynamic parameter and you can quantify its effect on flight within 5 minutes; testers can say what they did wrong in a crash, and someone asks to fly another leg unprompted.

If the flight feel and the leg loop don't pass, don't start laying down scenery; scenery is this genre's most expensive foundation, and redoing it once is a serious wound.

## 7. Common Pitfalls

1. **Fidelity before feel**: starting out with the full aerodynamic model and systems checklist ends in an aircraft that won't fly stably and can't be taught; fly stably first, fidelity later (§3.2).
2. **Teaching missing**: aviation is inherently high-barrier; a tutorial that lives only in the manual and never made it into the game drives most players away in the first ten minutes (§3.5).
3. **A default tier that satisfies no one**: full simulation by default scares off the mainstream, full arcade by default angers the core audience; layer the assist switches and make the default tier an explicit trade-off (§3.1).
4. **Answering only to peripheral owners**: a keyboard/mouse and gamepad experience that is merely tolerable, or outright unusable, shuts the majority audience out; the lowest barrier must hold (§3.2).
5. **Scenery started too early**: laying down maps before the core loop is frozen means a total redo the moment coverage or precision changes; scenery is this genre's most expensive one-time investment (§3.4, §5).
6. **Unreadable instruments**: the cockpit looks real but its information can't be read, so players fly on guesswork; readability comes before fidelity of detail.
7. **Stalls and emergencies that punish without teaching**: a crash with no explanation teaches "avoid stalls" rather than "understand stalls"; review tools are part of the teaching design.
8. **Weather as a texture**: wind and visibility that don't enter the flight model make the weather system wasted work, and players stop trusting the forecast (§4).
9. **No save elasticity on long flights**: a flight over an hour long that resets the moment it is interrupted won't be forgiven a second time; resuming from a breakpoint and autosave are baseline requirements.
10. **Benchmarking scope against the big studios**: measuring yourself directly against Microsoft Flight Simulator's global data and DCS's single-aircraft depth is this genre's classic crash; small teams should take the slice of "one region plus one kind of play" (§5).

## Further Reading

- Game Design Handbook: how to write core loops, experience goals and spec sheets — the base document for sections 2 and 3 of this page.
- Programming Handbook: the details of fixed-step simulation, streaming and performance budgets.
- Art & Audio Handbook: engineering practices for scenery assets, sky lighting and cockpit audio.
- Indie Survival: scope control and scheduling, to be read against §5.
- Exercise: greybox one patch of sky plus one local traffic pattern, and write down its assist switches and teaching ladder; then pick a flight sim you know, record how the shares split across "flight model, missions, scenery", and how it teaches a new player to complete their first landing.

Flight sim doesn't sell speed; it sells the sense of order that comes from completing a leg from start to finish: when flying is believable, the sky has weight; when the teaching is clear, the runway earns a second landing.
