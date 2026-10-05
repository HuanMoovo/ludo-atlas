# Ludo Atlas · Genre Handbooks · Vehicle Sim

> **Genre Handbooks · Volume 3**. Positioning: the genre that makes "driving and hauling" itself the first pleasure. Vehicle physics and road conditions are what it stands on; the career loop and map exploration supply the long-term goals, and the player runs a small life of their own from the driver's seat.
> Companions: Game Design Handbook (core loops and economy balance) · Programming Handbook (vehicle physics, streaming and performance) · Art & Audio Handbook (scenery, engine audio and radio) · Indie Survival (scope control and scheduling).
> This page carries no external links; benchmark titles are widely known works only, and the figures here are common magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: vehicle sim is the genre **whose first pleasure is operating a vehicle and completing a haul**. Players build mastery of the machine through the interplay of weight, inertia and road conditions, and find immersion in "running a small life of their own" through the road network and career goals; driving is not a means of getting somewhere — driving is the content itself.

The core loop, written as a verb chain:

`take a job or pick your own destination → plan the route → prepare and load → drive the long haul → handle road conditions and weather → deliver and get paid → upgrade the vehicle and unlock new regions → take another job`

This loop is measured in trips; a trip runs from a few minutes to several hours. It holds on just two preconditions: driving feedback is believable (§3.1), and job rewards are visible (§3.3).

The simulation divide (three directions share one skeleton, with physics and the loop weighted differently):

| Direction | First pleasure | Physics weight | Mainstream benchmark |
| --- | --- | --- | --- |
| Simulation | Fidelity and the operating procedures themselves | High: behavior close to a real car | Microsoft Flight Simulator |
| Arcade | Immediate thrills and readable feedback | Low: game feel first | Forza Horizon series |
| Career sim | Management goals and map conquest | Medium: adequate is enough | Euro Truck Simulator 2 |

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Racing | Racing's win condition is lap times and placing; the vehicle sim's is delivering on time without an accident |
| Management sim | In management the vehicle is a row of numbers; in the vehicle sim, operating is the primary scene and numbers are support |
| Survival crafting | Both use vehicles to travel; in survival the vehicle is a tool, in the vehicle sim the vehicle is the protagonist |
| Open-world action | Driving is only a way to move; in the vehicle sim, hauling and road conditions are the whole gameplay |

A self-check question: take away rivals and lap times, leaving only the road network, the weather and hauling goals — does the game still hold? If the answer is "yes", you are making a vehicle sim.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Mechanical mastery**: weight, inertia, gears and braking distance can all be anticipated, and every scrape can be explained as your own input.
2. **A sense of journey**: departure, road conditions, weather and arrival string into one complete passage; the road is content, not a pipe connecting two points.
3. **Atmospheric immersion**: the scenery, the radio and the time alone on a long haul are this genre's unique emotional value, and its biggest difference from other driving genres.
4. **Career returns**: income, unlocks and garage growth give every trip visible progress on the books, with clear long-term goals.
5. **Low-pressure failure**: scrapes and late deliveries must be punished in proportion, but without wrecking hours of driving; resumable and rollback-able.

Benchmark titles (play them yourself before breaking them down):

| Title | What to learn from it |
| --- | --- |
| Euro Truck Simulator 2 | The combination of career loop and map scale; running long-haul pacing and radio atmosphere |
| Microsoft Flight Simulator | The tiered barrier to realistic operation; the sightseeing value of real geographic data |
| SnowRunner | The depth of terrain and surface interaction; the slow-paced pleasure of rescue work |
| Farming Simulator series | The coupling of vehicles and the management loop; scheduling jobs against farm work |
| American Truck Simulator | How regional cultural differences land in the road network and landmark design |
| Forza Horizon series | A mainstream wrapper for arcade driving; open-world cruising |

## 3. Design Essentials

### 3.1 Vehicle Physics and Game Feel: Translating "Heavy" into Instinct

Game-feel discipline shares its roots with racing (predictability over correctness), but the temperament is opposite: vehicles are heavier, accelerate slower and brake longer, and the player's relationship with the car is cooperation, not pushing limits; the thrill comes from driving steadily, not driving fast.

| Instinct | Corresponding parameters | What breaks when it is wrong |
| --- | --- | --- |
| Sense of weight | Vehicle mass, center-of-gravity height, suspension stiffness, steering damping | Too light feels like paper; too heavy feels like steering a boat, and trust never forms |
| Inertia | Acceleration and deceleration curves, air drag and rolling resistance | Without it, every input is cut off instantly and the car feels like it is floating |
| Drivetrain | Gear logic, the coupling of rpm and traction | Automatic transmission tunes out rough, and manual gears become pure burden |
| Grip | The friction-coefficient table between tires and each surface | One feel across every surface makes the surface and weather systems wasted work |

Three general practices:

- Low-speed maneuvering under heavy load is the everyday verb: precision in narrow-road turnarounds, parking and trailer reversing matters more than high-speed limits; establish the game feel at low speed first.
- Both camera views must hold up: the cockpit view carries immersion, third person carries everyday driving and parking; reversing gets assists like mirrors and guide lines.
- Make the fidelity-and-forgiveness trade-off explicit: manual gears, clutch and weak assists serve simulation players; the default tier offers automatic transmission and forgiving handling — both experiences must be fully playable.

Tuning discipline: game-feel parameters are collected into one balance table and support live editing; run the same stretch on a fixed route from a fixed starting point, comparing driving data and frame-by-frame recordings, changing one parameter group at a time. Acceptance criterion: take 5 people for 20 minutes each — no more than 2 "unexpected losses of control" per person, and after a loss of control they can say what they did wrong.

### 3.2 Surfaces and Weather: Layering the "Road"

Road conditions are this genre's second content source after the vehicle itself; build them in three layers:

| Layer | Content | Role |
| --- | --- | --- |
| Surface material | Asphalt, concrete, gravel, mud, snow, sand | Differences in friction, bumps and noise feed straight into the physics |
| Weather and time | Clear, rain, fog, snow, day and night | Visibility and grip change with the environment, turning a familiar road into a new challenge |
| Road events | Traffic jams, roadworks, closures, accidents | Force route decisions and break up the monotony of a long haul |

Three disciplines:

- Separate decorative weather from gameplay weather: raindrops and wet reflections are atmosphere; grip and braking distance actually changing is gameplay. Gameplay weather must be foreseeable — give the forecast before departure, and the punishment stays fair.
- Weather needs gradients: light rain, heavy rain and a rainy night only mean something if their effect on grip differs; jumping straight from clear to blizzard is laziness.
- Vehicle damage, fuel and rest (if you build a fatigue system) form one visible pressure chain: refueling, repairs and rest are all part of route planning, and stacked together they must not exceed the player's management bandwidth.

### 3.3 Career Loop: Jobs, Economy, Unlocks

The career loop is the engine of long-term retention, with three layers each minding a stage: jobs hand out the content, the economy defines the pace, and unlocks control the order the map opens in.

Job structure: one job equals five fields — origin, destination, cargo, time limit, payment — priced in three tiers:

| Job tier | Examples | Design role |
| --- | --- | --- |
| Short haul | Deliveries within a city or to a nearby city | Steady income, practice, low failure cost |
| Long haul | Cross-region transport | High pay for high time investment; the backbone of progression |
| Special | Heavy, fragile, oversize | Trades an operating barrier for a premium; the challenge for experienced players |

Job templates must be assemblable procedurally (origin, cargo and time limit drawn and combined), or hand-written jobs will eat the whole content budget.

Economy curve: income is made of a base freight rate, distance, a cargo coefficient and an on-time, damage-free bonus; expenditure is fuel, repairs, fines and employees (if you build a fleet). There is only one way to verify it: run the early curve at real durations and confirm what a player at hour 2, hour 10 and hour 30 can each afford. Too tight and players leave; too loose and they buy out the whole garage in a day.

Unlock pacing: garage expansion, new vehicles, map regions, skills (long haul, heavy cargo, fragile transport and the like). Unlocks are the gate that releases content: every piece of map opened gives old jobs new destinations and old roads new reasons. Tie map unlocking to progress; do not open it all from the start — a fully open map is a maze to a newcomer, not freedom.

Punishment design: speeding fines, cargo damage compensation and drowsy driving are reminders, not a manhunt — punish enough to sting; rollovers and accidents take their penalty in pay and time, without wiping progress.

### 3.4 Map and Scenery: The Rules for the Biggest Cost

The map is the largest expenditure on projects like these; set the rules before work begins:

- Settle the scale decision first: fix the "real-mileage compression ratio". Ground vehicles are rarely built at 1:1; the common approach keeps the road-network topology and landmarks, compresses the distance between two points, and trades the time saved for map coverage; the ratio is a product decision — change it late and the whole map is rework.
- Build the library in three modular layers: road pieces (straights, curves, ramps, bridges and tunnels, toll booths), regional themes (prairie, mountains, coast, industrial zones) and landmark buildings managed separately; cities and industrial zones have the highest detail density and the heaviest cost — control them with building clusters and distant impostors.
- Landmark density: players can tolerate repeated road pieces as long as a memorable landmark appears every few minutes; a hundred-kilometer route with no landmark at all is one players won't remember driving the next day.
- Wayfinding is the other half of the map: navigation, road signs, distance markers and the placement of gas stations and rest stops decide whether players can read your road network; a vehicle sim where routes have to be memorized by rote does not pass.

### 3.5 The Peripheral Ecosystem: A Ladder from Keyboard to Steering Wheel

This genre has a rare hardware ecosystem: players buy steering wheels, pedals, shifters and multiple monitors for it. Peripherals are not a bonus feature but part of the content, designed as a ladder:

| Tier | Hardware | Experience goal |
| --- | --- | --- |
| Lowest barrier | Keyboard, gamepad | Complete long hauls and reversing smoothly, never punished for the input method |
| Advanced | Force-feedback steering wheel | Road surface, load and slip come through the wheel |
| Full set | Wheel plus shifter, clutch, handbrake | Fidelity to the operating procedures themselves; playing the process, not the result |

Three disciplines:

- "Playable" at the lowest barrier comes before "fun" on peripherals: most players have only a gamepad, and a rough lowest tier shuts the majority audience out.
- Force feedback is the translation layer for physics: road information, tire slip and collision impacts all need their own corresponding feedback — don't turn everything into the same shake; build a compatibility matrix for mainstream brands and models and test device by device.
- The settings menu is part of the peripheral experience: sensitivity, dead zones, force-feedback strength and gear modes adjustable, with presets; players share setups with each other, and that is a low-cost live-ops asset.

## 4. Technical Essentials

The engineering difficulty concentrates in four places: vehicle physics, large maps and streaming, the global coupling of weather and audio, and peripheral support; everything below is engine-agnostic, with method detail in the Programming Handbook.

**Vehicle physics**

- Start from a single-rigid-body plus approximate-tire model (the same route as racing); the simulation direction then adds per-wheel forces, suspension and drivetrain solving; heavy loads also bring trailer articulation, multiple axles and rollover boundaries.
- Run physics on a fixed timestep decoupled from rendering; heavy vehicles are more sensitive to low-speed precision, so reversing and parking must be validated separately under the fixed step.
- Make vehicle parameters inheritable chassis templates: swap the body, interior and soundbank on the same chassis to derive a new vehicle — the most effective cost-reduction lever (§5).

**Large maps and streaming**

- Stream road pieces in and out by spatial chunk, with low-poly models and impostors for distant views; plan the budget around "the roadside stays readable", not "you can see far".
- Navigation and the road network share one data source: a single road-network graph feeds pathfinding, navigation callouts and job generation, avoiding three datasets that each tell a different story.
- Time scale is one global knob: the day/night cycle, job time limits, fatigue and fuel consumption all read the same clock; day/night must be fast-forwardable on demand, or night-driving problems will only surface during the final polish.

**Weather and audio**

- Weather is a global state machine: clouds, rain and snow particles, wet-road textures, spray and lighting switch in lockstep; wetness runs on one parameter chain from visuals to physics — don't let the two layers drift apart.
- Engine audio is half this genre's life: layered samples (idle, low load, high revs, backfire) mapped to rpm and load, with two sets of listening inside and outside the cockpit; tire, wind and trailer sounds complete the information layer.
- The radio is the heart of the long-haul atmosphere: built-in songs carry licensing costs, and the common approach is to support player-supplied music or internet radio, avoiding negotiations over a track list.

**Peripherals and settings**

- Route peripherals through a device abstraction layer: wheel steering, force feedback, pedals and gearing abstracted into unified interfaces, then configured per device; input logic must not be scattered around the codebase.
- Give every device class default configs and a calibration flow (steering range, pedal travel, gear mapping), with settings persisted to the player profile.
- Key remapping, assist toggles and HUD layout are technical requirements, not polish patches; this audience expects more settings options than most genres.

## 5. Content Volume and Workload Reference

The following are common magnitudes for similar projects, for estimating scope, not a promise.

| Project form | Content scale | Timeline scale | Notes |
| --- | --- | --- | --- |
| Feel prototype | One test route plus one vehicle | 2–4 weeks | Validates driving, road conditions and one job only |
| Small complete title | One city and its surrounding road network, 3–5 vehicles | 3–9 months | The road network and scenery are the main cost |
| Typical indie scope | One region (a road network across several cities), 6–10 vehicles | 1–2 years | The map and scenery are usually the single largest budget line |
| Large title with live ops | A multi-country road network, dozens of vehicles | 3+ years | Map expansion packs are the main follow-on content |

Cost breakdown: one kilometer of road "at shipping quality" equals the road surface and markings, roadside fixtures, landmarks, traffic and event logic, plus day/night and weather variants; the map and scenery are the single largest budget line. Vehicle costs break down as: exterior model plus cockpit interior (if you build one), engine and full-vehicle audio, a power and game-feel parameter set, liveries and acquisition method; deriving from a shared chassis cuts cost noticeably, but interior and soundbank are still one per vehicle.

Scheduling anchor: building a vertical slice from scratch (a small piece of map plus one complete career job chain) typically takes 2–4 months; extrapolate afterwards by "map area × polish factor". The map is the most expensive content to redo: anything that can be done later should not be done early.

## 6. How to Start the First Prototype

The first prototype builds only one route, one vehicle and one complete job, finished in 2–4 weeks, touching neither large maps nor any system beyond the economy.

**Week 1: the vehicle and one route.** A route with a start and an end, corners and elevation changes; one vehicle; basic physics plus two cameras, cockpit and chase; a timer at the start point. Ugly is expected at this stage.

**Week 2: one complete job chain.** Get all five steps running — take the job, navigate, drive, deliver, get paid; give the payment a crude formula for now — the point is a complete chain, not exact numbers.

**Week 3: one layer each of road conditions and weather.** Surface materials and one gameplay weather type (rain, say) enter the physics, with a few simple traffic cars on the road; find 3–5 people who have never played, and watch when they zone out, when they curse, and when they want to run one more trip.

**Week 4: tuning and acceptance.** Tune the game feel with frame-by-frame recordings, run the early economy curve, and change only parameters and the route — add no new systems.

Success criteria (all observable):

- With all art and audio removed, testers still want to run this route again and again, a session typically lasting over 15 minutes.
- At least 4 of 5 testers complete a job with no verbal guidance; "this car is broken"-type complaints no more than 1 per person.
- Change any one physics parameter and you can quantify its effect on driving within 5 minutes.
- Testers can say what they did wrong in an accident; someone asks to run another trip unprompted rather than being asked to try again.

If the game feel and the job chain don't pass, do not start laying down the map; the map is this genre's most expensive foundation, and redoing it once is a serious wound.

## 7. Common Pitfalls

1. **Map laid out big before the gameplay is validated**: scenery is the biggest cost, and starting before the core loop is frozen means one gameplay change equals redoing the whole map.
2. **Treating physical correctness as the goal**: real-car physics is often hard to drive in a game; players want predictability — simulation is a candidate means, not the end.
3. **Empty routes**: no traffic, no events, no landmarks, and a long haul turns into a dull wait; solve "what happens on the road" first, then talk about map scale.
4. **Weather as a texture**: rain that doesn't change grip or braking gets read as decoration, and players stop trusting any weather forecast afterwards.
5. **Economy curve stalling**: ten hours in and you cannot afford a second vehicle, or two hours in and the garage is full; the economy curve is the retention curve (§3.3).
6. **A broken peripheral ladder**: a keyboard that is merely tolerable to drive with and a steering wheel with no feel at all offend both ends; the lowest barrier and the high-end payoff must hold at the same time (§3.5).
7. **Copy-pasted maps**: no landmarks, no regional theme differences — players can't remember the roads they drove, and the bigger the map grows, the more lost they feel.
8. **Punishment stealing the show**: fines, fuel and fatigue stacked into three layers turn the cab into a dashboard exam room; the pressure chain must leave management bandwidth.
9. **No save elasticity on long jobs**: an hour-long drive that resets the moment it is interrupted won't be forgiven a second time; resuming from a breakpoint is a baseline requirement.
10. **Benchmarking scope against the big studios**: copying a big publisher's map and vehicle list outright is this genre's classic crash (§5).

## Further Reading

- Game Design Handbook: how to write core loops, economy balance and experience goals — the base document for sections 2 and 3 of this page.
- Programming Handbook: the details of fixed-step simulation, streaming and performance budgets.
- Art & Audio Handbook: engineering practices for scenery assets, engine audio and radio.
- Indie Survival: scope control and scheduling, to be read against §5.
- Exercise: greybox a ten-minute route plus one complete job, and write down its road events and payment formula; then pick a vehicle sim you know, record how the shares split across "operation, road conditions, economy", and how it forecasts weather and settles payment.

Vehicle sim doesn't sell speed; it sells "life on the road": when the road is believable, there is a reason to set out; when the rewards are clear, another trip is worth taking.
