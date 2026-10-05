# Ludo Atlas · Genre Handbooks · City Builder

> **Genre Handbooks · Volume 2**. Positioning: the genre whose core pleasure is land layout and system coupling. Players make a chain of placement decisions on empty ground, watch population, demand, services and traffic pull on one another across four layers, and grow a patch of land into a machine that develops its own faults.
> Companions: Game Design Handbook (loops, system coupling and balance) · Programming Handbook (simulation architecture and performance) · Production Handbook (estimation and scope control) · Pitfalls & Anti-patterns (the Design & Gameplay and Programming & Architecture chapters).

---

## 1. Positioning and Core Loop

One-line positioning: city building is the genre that **makes "placement decisions on land" the primary pleasure**. Where the road goes, how the zoning is spread out, which intersection a service sits on — every decision must produce chain consequences on a scale of tens of hours; the simulation is responsible for making the consequences visible, and the player is responsible for repairing every trouble they have created.

The core loop, written as a verb ring:

`Survey the land → Zone → Lay roads → Build services → Population moves in → Tax collection and demand shifts → New problems surface (congestion, pollution, deficit) → New tools unlock → Expand again`

This loop reaches further than in other building genres: the consequence of one layout decision may only become visible an hour later, so the feedback pipeline that delivers simulation results to the player's eyes (layers, charts, alerts) matters as much as the building tools themselves.

Drawing the boundary against neighbouring genres:

| Neighbouring genre | Boundary |
| --- | --- |
| Management sims (the Two Point Hospital kind) | Those manage abstract rooms and processes; city building manages the land itself — position and network decide success |
| Colony sims (the RimWorld kind) | Those sell individual agents and story generation at a small scale; in city building residents are statistics and the point is the system working as a whole |
| Survival crafting (the Minecraft kind) | Those are about crafting and survival from an individual perspective; city building operates on planning, not on people |
| 4X and RTS | Those have opponents and confrontation, with wins and losses written into a match report; city building's opponent is the simulation's own side effects |

A self-check question: if you replaced the map with a list of numbers, would the game still hold up? If the answer is "yes", what you are making is probably a management sim rather than a city builder.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **A sense of control**: the city runs the way you designed it, rises and falls can be explained, and when you break it you know where to fix it.
2. **The urge to create**: the land is a canvas and the layout is self-expression; players will happily spend three extra hours on "looking good".
3. **Problem solving**: congestion, pollution, finance — one engineering problem after another, each with a clear payoff when solved.
4. **The wonder of growth**: from an empty plot to a living thing that lights its windows and jams its roads; scale itself is the reward.
5. **A long-term project**: the city is both a save file and a body of work; every return visit leaves one more spot you want to change.

Reference games list only household names; if you have not played one, play it first — two hours of playing beats two hours of analysis:

| Game | What to learn |
| --- | --- |
| SimCity 4 | The classic implementation of zoning and demand (RCI); pacing and tension at the small-to-mid city scale |
| Cities: Skylines | The modern standard for freeform curved road tools and traffic simulation; how a mod ecosystem amplifies a product's lifespan |
| Frostpunk | Pressure design in goal mode: the trio of countdown, moral choice and resource desperation |
| Anno 1800 | Coupling between production chains and city tiers; making "looking good" part of the system's rewards |
| Banished | A complete small-scope sample; the failure spiral woven from population age structure and resource chains |
| Canal Towns | The mobile form: light interaction plus collection and placement layers, proving the genre can be pared down |

Counter-examples are worth studying too: the plot sizes and online requirements of SimCity (the 2013 reboot) are a public sample of the price of restricting players' freedom of expression.

## 3. Design Essentials

### 3.1 The Simulation Core: The Four Layers of Population, Demand, Services and Traffic

The city simulation is four interlocking layers. First make clear what each layer manages and which layer drives which:

| Layer | What it manages | What it outputs | Common implementation granularity |
| --- | --- | --- | --- |
| Population | Residents and households: count, age, education, employment, move-in and move-out | The source of every demand | Statistics by building and household, not simulated one by one |
| Demand | Development appetite for residential, commercial, industrial and office; land value and housing prices | What the player should zone and build | Formulaic demand curves |
| Services | Fire, police, healthcare, education, utilities, garbage | Satisfaction and city health | Coverage range plus capacity |
| Traffic | Road network, commute times, congestion, public transit | Whether the top two layers can actually reach | Road-segment flow plus sampled vehicles |

The four layers interlock as "population drives demand, demand drives construction, and services and traffic decide whether population stays". One complete chain of linkage: a new residential district is completed, population grows, commute volume rises, the main roads start to jam, fire trucks cannot reach the new district, satisfaction falls, and residents stop moving in or even move away. Every link in the chain needs its own visible feedback, built into a layer or a chart; a simulation you cannot see does not exist.

Design discipline: pick one or two of the four layers to make deep and keep the rest thin. All four deep is a workload for a large team; small teams usually make traffic deep (it is the layer players see most easily) and services thin (a radius plus capacity is enough).

### 3.2 Zoning and Roads: Grid or Freeform Planning

Two foundations to settle first: how roads are drawn and how plots are cut.

| Approach | Representative | Player-side advantage | Technical cost |
| --- | --- | --- | --- |
| Grid | SimCity 4 | Clean alignment, easy to read, density planning is intuitive | Expression is constrained; curves and diagonals are hard |
| Freeform | Cities: Skylines | Free expression; the city has a "hand-drawn" feel | The plot subdivision algorithm is complex; building alignment needs tooling to patch up |

The hidden cost of freeform planning is the "plot": roads can cross at any angle, but buildings need flat, road-facing plots, and behind that sit polygon splitting, edge alignment and slope adaptation — a whole stack of geometry work. Without a technical budget of two months or more, do not touch full freeform. The compromises, ordered from low cost to high: pure grid; grid plus diagonal arterials; grid as the base with decorative curves supported (roads bend visually while the logic still runs on the grid); fully freeform. Most projects stop at the second tier, and that is enough.

The rule list for roads and zoning:

- A plot must front onto a road to be developed — this is the core rule that sets city building apart from other building genres; write it into the design document before writing any code.
- Road hierarchy: arterials, collectors and local roads, with different widths and speed limits; upgrading and demolishing must warn about the loss.
- Zoning is painted with a brush; zone type (residential, commercial, industrial, office) times density level (low, medium, high) jointly decides which buildings grow.
- Intersections are both the bottleneck of traffic and the point where design bites: roundabouts, one-way streets, elevated roads and tunnels serve as the "new tools" of the mid and late game, matching the new problems the city grows into.
- Public transit (bus, metro, rail) is the unlock answer to congestion; deliver it after the player has first been hurt by congestion — do not hand it over early.

### 3.3 The Traffic Layer: Turn "Accessibility" into a Visible Number

Traffic is the most expensive and the most rewarding layer in city building. Design-wise it does only three things: make flow visible, give commuting a cost, and let tools fix what is broken.

- **Visible flow**: road colours graduate with flow, and the tidal ebb and flow of rush hour must be visible. If players cannot see where the jam is, they cannot design a fix.
- **Commute cost**: the commute time remembered by each household group is one of the core variables of moving in and out; when a commute passes the threshold, residents move to a closer district. This rule lands more directly than any tooltip.
- **A ladder of repair tools**: widen roads (relieve) → one-way streets and signals (channel) → public transit (replace) → new districts (divert); each rung corresponds to a stage of city size.

The "realism" of pedestrians and vehicles is held up by sampled agents (see §4). Design promises only one thing: on the screen the player can see, the traffic in the streets must match the numbers on the statistics panel.

### 3.4 Failure States and Negative Feedback: The Disaster System and Pressure Sources

A city builder without pressure loses its player by hour ten. Pressure sources come in four kinds, delivered on a gradient from gentle to urgent:

| Pressure source | Manifestation | Warning visible to the player | Correct response |
| --- | --- | --- | --- |
| Finance | Maintenance costs exceed tax income and the books turn red | Budget charts, an itemised expense list | Adjust tax rates, cut redundancy, bridge with loans |
| Disasters | Fire, flood, earthquake, plague | Risk layers, radio bulletins | Preventive service coverage, post-disaster rebuilding |
| System decay | Congestion, pollution, crime, unemployment | Layers worsen, icons flash | Targeted retrofits, one stretch at a time |
| External pressure | Timers, budgets and events in goal mode | Countdown, story prompts | Prioritise and make trade-offs; sacrifice the part to save the whole |

Design discipline for the disaster system:

- Every disaster ships with all four parts: trigger conditions, prevention means, a visible spectacle when it happens, and a repairable aftermath. A disaster missing prevention is pure random destruction; a disaster missing repair is a save deletion.
- Probability and frequency become difficulty tiers, and in the sandbox they can be dialled to zero; save-wrecking events (large-scale earthquakes, meteors) appear only in goal mode or in options the player has explicitly switched on.
- The job of a disaster is to break the player's assumption of "absolute safety", not to punish. One fire should teach the player the value of fire coverage, not make them restart.

The death spiral of negative feedback is a priority to guard against: finances collapse, services stop, population flees, tax income falls further — once this chain starts turning, the player abandons the save within two hours. Countermeasures: multi-stage warnings before bankruptcy, emergency loans or subsidies, maintenance costs that can be downgraded, and a degraded mode where "turning off half the systems still keeps you alive". Punishment needs a gradient and the exit needs to be dignified.

### 3.5 Sandbox and Goal Modes: Two Products, One Simulation

The choice between sandbox and goal (scenario, challenge) modes is a decision to settle at kickoff:

| Dimension | Sandbox mode | Goal mode (scenarios and challenges) |
| --- | --- | --- |
| Player motivation | Creation and expression | Problem-solving and conquest |
| Resources and constraints | Loose: adjustable funds, no countdown, disasters can be switched off | Tight: fixed budgets, time limits, disaster frequency |
| Content cost | One simulation plus one toolset | The same simulation plus parameter packs and scripted events |
| Risk | Explodes in the first few hours, then loses its goal | A balance misfire becomes a turn-off, especially in the first 30 minutes |
| Representative | Cities: Skylines | Frostpunk (an extreme form, almost purely goal mode) |

Trade-off advice:

- The simulation must run clean in sandbox first. Goal mode magnifies every flaw in the simulation; building scenarios on an unstable simulation only concentrates the frustration on your most dedicated players.
- Sandbox needs intrinsic goals too: population milestones, landmark unlocks, achievements, blueprints and photo mode. A sandbox with no intrinsic goals turns into an idle screensaver after three hours.
- Goal mode is the best-value content: reuse the same simulation and change the initial conditions, constraints and victory conditions — a single scenario costs far less than a set of new buildings.
- On release order, sandbox holds the floor and scenarios raise the ceiling: first let creative players play on indefinitely, then hand challenge players one problem after another.

## 4. Technical Essentials

The engineering proposition is one sentence: **you do not have to simulate every resident individually**. The performance red line in city building is set by simulation granularity, and granularity is set by the screen: only what the player can see is worth computing carefully.

- **Layered agents**: residents and households are stored as statistics (distributions aggregated per building and per district); vehicles and pedestrians are just "visualisation agents" sampled from the statistics, carrying the presentation of traffic flow. The agent count is capped, and off-screen ones degrade to pure numeric flow.
- **Tiered simulation frequency**: traffic and vehicles run at high frequency (per frame or several times per second), services and construction at medium frequency (per second), population, economy and demand at low frequency (tens of seconds to a minute). Low-frequency layers settle in batches; never traverse everything in full every frame.
- **Traffic solving**: roads are a graph, nodes are intersections, edges are road segments. Pathfinding is dynamically weighted with congestion cost; as the city grows, district subgraphs and flow approximation (folding vehicle fleets into flow numbers) hold the cost down. Traffic is almost always the performance ceiling for this kind of game — aim your first performance budget at it.
- **Coverage and accessibility**: coverage for services like fire and healthcare is computed as a multi-source breadth-first distance field (spreading outward from the service point), one to two orders of magnitude cheaper than pathfinding per building.
- **Data-driven**: buildings, zoning, services, policies and economy parameters are all externalised into tables, and the code only reads tables. Balance is the main work of this genre, and changing a parameter cannot wait for a compile.
- **Saves**: the city state is large (every building, every road, every zone), so saves need version numbers and migration functions, plus automatically rotating backups. Players invest tens of hours here; a broken save is the number-one felony in negative reviews.
- **Presentation decoupled from simulation**: building growth, vehicle movement and day-night lighting are all presentation layer and may interpolate and lag, with the data as the simulation's truth; the render side carries scale with instancing and merged meshes, while the simulation side carries frequency with background threads or frame slicing.
- **Debug tools**: a simulation statistics panel (population, employment, income and expense curves), layer toggles (coverage, noise, pollution, flow), time acceleration and batch simulation. Without these tools, balancing four layers of simulation is blind tuning.
- **The data cost of planning mode**: a grid map is a two-dimensional array, and the cost of building and querying is negligible; freeform planning needs a geometry library to support plot operations, and every road you lay re-evaluates the surrounding plots, so pressure-test with the most complex intersections early.

## 5. Content Volume and Workload Reference

Half of a city builder's cost is simulation and half is content, and the two do not transfer between each other. The following are common magnitudes, for scoping, not promises:

| Project shape | Scale | Timeline magnitude | Notes |
| --- | --- | --- | --- |
| Simulation prototype | One small map, a simplified version of the four layers | 4–8 weeks | Zero art; validates the population-drives-demand loop |
| Small complete title | One mid-size map, one building set | 6–12 months | The Banished direction; solo or two to three people |
| Common indie and mid-size titles | Several maps plus scenario mode | 1.5–3 years | Balancing and tuning swallow a considerable share |
| Large titles | Large maps, multiple cities, mod support | 3+ years | Benchmarked against the Skylines-class games |

The cost structure of a content unit:

| Content unit | Unit cost (magnitude) | Minimum viable | Commercial volume | Notes |
| --- | --- | --- | --- | --- |
| Building assets | 1–3 days each | 30–50 | 150–400 | The largest cost item; modularity plus recolouring is the life-saver |
| Zoning and service number tables | Half a day to 2 days per table | 3 zone types, 5–8 services | The full system | Balanced over and over, with chained changes |
| Vehicles and pedestrians | 1–2 days each | 5–10 | 30–80 | Includes animation and day-night lights |
| Maps | 1–3 weeks each | 1 | 5–15 | Hand-made terrain, or generation plus hand-placed landmarks |
| Scenarios (goal mode) | 1–4 weeks each | 2–3 | 10–30 | Reuses the simulation; mostly constraints and scripts |

A few magnitude takeaways:

- Balance is this genre's hidden bulk: with four coupled layers, changing one tax rate can move housing prices, demand and migration. Reserve more than twenty percent of the total schedule for balance and tuning.
- Building assets expand along density level times zone type, and every category still needs variants and upgrade forms. This is exactly where scope runs away most often: fix the total building cap first, then allocate it downwards.
- Priority order for cutting scope: building variants, map count, scenario count, with simulation depth last. Cut simulation depth, and the game itself stops standing.

## 6. How to Start the First Prototype

The first prototype makes only one small map and the minimal four-layer loop: 4–8 weeks, touching no art, disasters or scenarios.

1. Camera and map: a grid map within 64×64, a top-down camera with pan and zoom; terrain is only flat ground and water at first.
2. Road tool: two drawing modes, straight lines and rectangle drag, with the demolition tool built in the same batch.
3. Zoning brush: residential, commercial and industrial, low density only; a plot may be developed only if it fronts onto a road.
4. Growth and population: plots in a zone grow buildings automatically, and population begins to accumulate. This is the whole project's first positive-feedback highlight — go all out on the growth animation.
5. Demand loop: population generates residential demand and employment produces commercial demand — one simple formula is enough; when demand is out of balance, the map shows a visible cue.
6. One service: do only one (fire or power), circular radius coverage, with a warning icon on buildings outside the coverage.
7. Minimal traffic: vehicles travel from residential zones to work zones, first in straight lines, then upgraded to shortest paths; observe how the first jam forms.
8. Panels and layers: one statistics panel (population, budget, employment rate) and one coverage heat map. Without these two, the effect of the first seven steps cannot be accepted.

Prototype acceptance (all observable):

- Play continuously for 30 to 60 minutes and the player can say "where the next road goes" and "what the biggest headache is right now". Pain points are the gameplay; failing to name one means the feedback chain is not connected.
- The population curve can climb to the first bottleneck (usually road capacity), and the cause of the bottleneck is visible to the naked eye.
- With all art cues switched off and only the panels and layers left, reverse-engineering the city's state shows no obvious error.

Counter-example: build freeform curved roads first, disasters first, art assets first. City building's art volume is enormous; before the simulation loop holds, every building is sunk cost.

## 7. Common Pitfalls

| Pitfall | Symptom | Avoidance |
| --- | --- | --- |
| Laying out content before the simulation loop holds | The building table has hundreds of rows, but population and demand are not linked to each other | Get the minimal four-layer loop running first, then open the content production line |
| Traffic performance out of control | Every vehicle runs full pathfinding, and the frame rate drops to unplayable as the city grows | Layered agents plus flow approximation; give traffic the first performance budget |
| Bankruptcy deletes the save | After a financial collapse there is no way back, and the player abandons the save outright | Death-spiral countermeasures: loans, subsidies, downgraded maintenance costs |
| Disasters that destroy but never prevent | A random fire burns a district and the player had no preparation at all | The four-part disaster kit: trigger, prevention, warning, repair |
| A single mode, or a sandbox without intrinsic goals | Half the creative or challenge-driven players are cut off, or they start idling and sightseeing after three hours | Sandbox holds the floor and scenarios raise the ceiling; milestones, landmarks, achievements and blueprints become visible progress |
| Balance coupling out of control | Change one tax rate and housing prices, demand and migration all go haywire | Parameters centralised and externalised; long simulation runs used as regression tests |
| Missing layers | Players cannot see why traffic jams or why satisfaction has dropped | Give every simulation variable an outlet as a layer or a chart |
| An empty opening | The first twenty minutes of a broke start have nothing to do, and players churn away | Compress the early game; deliver the first "it is built" highlight as fast as possible |
| Saves blowing up | A city of tens of hours corrupts or fails on version compatibility | Version numbers, migration functions, rotating backups — ship them on day one |

## Further Reading

- Reread two sections of the Game Design Handbook: core loops and nesting, and the sources and sinks of the economy system; before reading, draw a coupling diagram of the four-layer simulation.
- The performance and architecture chapters of the Programming Handbook: agent models, frame-sliced computation and data-driven design, corresponding to §4 of this page.
- The estimation chapter of the Production Handbook: time "one building, one map, one scenario" first, then multiply by content volume. City building is a disaster zone for runaway scope.
- Read the Design & Gameplay and Programming & Architecture chapters of Pitfalls & Anti-patterns against §7 of this page.
- Play rather than read: put ten hours each into SimCity 4, Cities: Skylines and Frostpunk, and note what was happening in the minute you wanted to quit.
- Hands-on exercise: without writing code, build a small four-layer linked model in a spreadsheet (population, demand, service capacity, commute time), run a hundred turns, and see where the failure spiral emerges.
