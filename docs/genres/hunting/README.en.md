# Ludo Atlas · Genre Handbooks · Hunting

> **Genre Handbooks · Volume 4**. Positioning: the genre that makes the patient loop of "track, lie in wait, one shot" its first pleasure. Players read sign, judge the wind and wait for the moment; most of the time is spent lurking, and all the tension concentrates into the instant the trigger is pulled. This page covers tracking systems, the simulation/arcade divide, gear progression, ecology and the boundaries of depiction, and the realistic arithmetic of content volume.
> Companions: Game Design Handbook (core loops and numbers) · Programming Handbook (perception AI and data tables) · Case Studies (breakdown and postmortem methods) · Indie Survival (scope control and content accounting).
> This page carries no external links; benchmarks list only widely known works; the legal and ethical questions of real hunting get one line, in §3.4.

---

## 1. Positioning and Core Loop

In one line: hunting is the genre that **turns patience into ammunition**. Scout, lurk, wait, aim — one shot settles everything; slow is the body, fast is the climax, and all the design is about managing "exposure" and "timing". **Patience must be part of the reward, not a punishment.**

The core loop, written as a verb chain:

`scout and read the map → follow the trail → judge wind and sound → lie in ambush → take the shot → recover the kill and settle up → grow and pick the next quarry`

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Shooters (FPS/TPS) | A shooter's targets are enemies that fight back and die; hunting's target is an animal inside an ecosystem that mostly doesn't know you are there — the threat comes from "exposure", not from firefights |
| Action hunting (Monster Hunter-style) | Action hunting writes animals as move-set opponents and material sources — boss fights at heart; this genre's animals are behavior models and ecology, and the verdict lands before the shot |
| Survival craft | There, hunting is just one gathering method (food and hides) and a small slice of a host system; this genre expands it into the whole game |
| Stealth | In stealth, exposure triggers punishment (alarms, combat); in hunting, exposure mostly just means the chance slips away — failure has to be cheap |
| Hunt: Showdown-style PvPvE | The quarry becomes an objective marker and the players become the main threat; hunting degrades into a trigger here, and the showdown happens between players |

A self-check question: replace the quarry with a stationary target that leaves no sign — does the game still hold up? If the answer is "yes", you have built a shooting range; the workload in hunting is not in the gun, it is in "the animal is an ecosystem".

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **The tension of lurking**: every stir could mean exposure; crouching, circling around, stopping — movement itself is a decision.
2. **The reasoning of tracking**: reading a line of sign as a map — when it passed, where it went, how far ahead it is; having a deduction confirmed or broken are both core pleasures.
3. **The ritual of the one shot**: breathe out, aim, pull the trigger; one shot decides it, and the preparation happened tens of seconds earlier.
4. **A collection with a scale**: antlers and pelts, size records, a compendium and a trophy room turn repeat kills into long-term goals.
5. **Settling into the wilds**: ambient sound, light and weather are the payoff of the slow pace; the quiet itself has to be worth enjoying.

Negative feelings (any one of them is a red light): walking an hour with no target; firing the moment you spot something; a hit with no feedback; rarity that lives only in a probability table.

Benchmark titles (all widely known; play them yourself before breaking them down):

| Title | What to learn from it |
| --- | --- |
| theHunter: Call of the Wild | The baseline of modern simulation hunting: need zones (drinking, feeding, resting), tracks and calls, wind and the ambush rhythm |
| Way of the Hunter | The comparison sample at the top of the simulation range: ballistics and hit replays, herd behavior, trophy generation and narrative wrapping |
| Hunting Simulator 2 | The middle tier between streamlined and simulation: dog assistance, mission-driven structure |
| Red Dead Redemption 2 (hunting subsystem) | Hunting embedded in an open world and an ecology: pelt quality, market prices and the crafting system feeding each other |
| Hunt: Showdown | The PvPvE variant where the quarry becomes an objective and players are each other's main threat; the boundary is in §1 |
| Monster Hunter | The action-oriented branch: the other evolutionary path for hunting vocabulary, with animals written as move sets |
| Duck Hunt | The arcade ancestor: the shortest loop of one shot per round, where aiming is the entire game |

## 3. Design Essentials

### 3.1 Tracking: Sign, Sound and Wind — Three Information Systems

Tracking is this genre's engine. It is made of three overlapping kinds of "reading", and all three must be visible to the player:

| System | Information unit | What the player is working out |
| --- | --- | --- |
| Sign | footprints, droppings, blood trails, leftover food, rubbed tree trunks | direction, freshness, species, whether it is wounded |
| Sound | footsteps (tiered by ground material and gait), calls, ambient noise | how loud am I; what is nearby; which call to lure with next |
| Wind | the global wind vector plus local turbulence | which way I am approaching from; which way the quarry's nose points; which side to close in from |

Execution notes:

- **Sign needs a freshness scale**: start with three tiers — fresh, normal, old — distinct in both appearance and information; freshness decays over time, and rain accelerates the decay; blood trails get three or four tiers by hit location, carrying both hit feedback and tracking clues at once.
- **Perception priority must be fixed and learnable**: the simulation convention is smell farthest, hearing in the middle, sight nearest; the three radii go into the animal's config, not a mysterious formula; circling upwind, quieting your footsteps and using cover correspond one-to-one to those three radii.
- **Ambushing is downstream of tracking**: need zones (drinking spots, feeding grounds) and choke points are natural ambush positions; maps must leave terrain where "lie in the right place and wait for it to come" works; the player is working out when it arrives, from where, and where to stand.
- **Information must be visualized in one pass**: wind is repeated through drifting fur, grass blades and the HUD compass; perception feedback is read from animal behavior (head up, ears cocked, staring at you); a system with no visualization is a system you didn't build (see §4); tools are fine (highlighting the nearest sign, binocular tagging), straight-line waypoints are not — "I read it myself" is the whole pleasure of tracking.

### 3.2 The Simulation/Arcade Divide

The divide comes before the elements: the same deer hunt is two different products at the two ends, in session length, ballistic complexity and information volume. Pick the niche first, then talk mechanics.

| Dimension | Simulation-oriented | Arcade-oriented |
| --- | --- | --- |
| Session length | a full hunt runs 10–40 minutes | a round runs 1–5 minutes |
| Ballistics | drop, wind drift, breath-holding and zeroing | crosshair equals hit |
| Tracking | sign and wind are required coursework | target highlights, audio direction cues, indicators |
| Failure | the animal slips away and you come home empty-handed (the cost is time) | lose a life or restart the round (the cost is the score) |
| Animal presentation | ecological schedules and herd behavior | target-dummy spawns and procedural movement |
| Representatives | theHunter: Call of the Wild, Way of the Hunter | Duck Hunt and the arcade light-gun hunting lineage |

The middle tier (Hunting Simulator 2 and the like) wants simulation looks and arcade pacing at the same time; it is not impossible, but it will alienate part of the audience on both sides; small teams should pick one end outright. One self-check: how many minutes is your player willing to wait before their first shot? The answer decides which side you are on.

### 3.3 Gear and Skill Progression

- **Gear is organized by "what it can take", not by number size**: firearms are tiered by caliber and use (small, medium, large game), with bows as a separate line; sights, ammunition, clothing (camouflage and scent), dogs or support tools each get a line of their own.
- **Skill lines serve information and handling**: tracking (sign visible from farther away), breath control (a longer steady window), stealth (less movement noise), zoology (species prompts and habit markers).
- **Unlock points must pass two checks**: every new piece of gear opens a class of quarry or a distance you could not take before; every new skill removes a category of information noise. If it does neither, it is pure numbers — cut it.
- **Consumables and progression pacing**: ammunition, lures and scent eliminators handle day-to-day costs and reasons to head out; work out the returns first — how much per kill, how many kills an hour — then tune; simulation progression is a long curve with small steps, where caliber, scope, ammo, clothing and dog each change only a little; don't let any single item change everything.

### 3.4 Ecology Presentation and the Boundaries of Depiction

- **The ecology is three tables**: a species table (herding or solitary, diurnal or nocturnal, alertness), a schedule table (where and when they feed, drink and rest), and a distribution table (map × habitat × time slot). Players study the schedule; designers write the tables.
- **Fix the depiction level once**: blood, how downed animals are handled, whether field dressing and carcass handling are shown — decide it together with the target audience and the distribution platform's rules; change it midway and all art and animation gets reworked.
- **Don't write the animals as enemies**: animals carry no aggro and should not hunt the player on their own; even aggressive species' threat has to match their habits. Write animals as monsters and the genre slides toward action hunting — a different category.
- **Boundary in one line**: real hunting is constrained by local regulations and animal-ethics considerations; this page discusses game design only and is not guidance for hunting in real life.

### 3.5 Content Matrix: Species × Maps × Gear

- **Content volume is multiplication**: species × maps × gear, times the text, sound and behavior cost per species; measure your team's output in weeks per species first, then set the launch scope (see §5).
- **Species differences belong in behavior**: solitary, herding, nocturnal, alertness, territoriality; if two species differ only in numbers and textures, merge them into one.
- **The map is gameplay**: the habitat mix (forest, grassland, wetland, mountains) decides the species table and the approach routes; a good map has workable terrain for both "approach upwind" and "ambush at long range".

## 4. Technical Essentials

The engineering difficulty concentrates in three places: animal perception and behavior, sign and sound as world state, and debug visualization. Everything below is engine-agnostic.

**Animal AI and perception**

- Perception runs on three channels: sight (view cone plus range), hearing (the propagation radius of sound events), smell (a perception zone carried along the wind vector); each channel gets its own parameters — coarse and readable beats fine and mystical.
- The alert state machine: calm, suspicious, alert, fleeing and so on, with transitions driven by perception intensity and thresholds; fleeing must be predictable (where it goes, how far, whether it turns back) — the player's pursuit decisions rest entirely on it.
- Herd behavior starts from templates: herding herbivore, solitary herbivore, predator, waterfowl — four templates cover most needs; individual variation goes through parameters, not new code.
- Performance tiers: low-frequency decisions at distance (once or twice a second), simplified perception at mid range, full speed up close; population caps and spawn areas managed dynamically around the player's position.

**Sign and sound as world state**

- Sign is a class of world object (position, type, freshness, heading), continuously spawned and decayed; rendering and queries stay separate (player tools query "the nearest sign"), with spatial partitioning to prevent full-map scans.
- Sound and wind: sounds split into player events (footsteps, gunshots) and ambience (wind, rain, birds); lure calls are implemented as "play a sound event, respond by probability", with response parameters configured by species and distance; wind is a global vector plus local turbulence, affecting scent propagation and sign decay, and rain affects sign and sound propagation, acting as both cover and the eraser for sign.

**Debugging and validation**

- The first tool is perception visualization: three radii, the current state-machine state and the wind vector on one screen; without it, behavior tuning in this genre cannot proceed.
- Simulation tests and hit resolution: script an AI hunter to approach an animal in a straight line under different wind directions and record the distribution of detection distances — the quantitative ruler for "is the perception radius readable"; hits resolve by region collision (vital zone, slowing zone, ineffective zone), with bullet drop and wind drift added for simulation titles — a simple projectile model is enough.

**Saves and data**

- Species, gear and perception parameters all live in external data tables, and the compendium and size records derive from the same species table; kill records, compendium progress and the trophy room are long-term data — version them from day one; on-map sign does not need to be persisted one by one — define first which pieces are saved and which are regenerated.

## 5. Content Volume and Workload Reference

Cost is approximately multiplicative: `total content ≈ species × assets per species + maps × assets per map + gear × configuration`.

| Tier | Species count | Maps | Gear scale | Positioning |
| --- | --- | --- | --- | --- |
| Prototype | 1–2 | 1 small map | 1 gun, 1 bow | validates the loop from tracking to shooting |
| Small finished title | 6–10 | 1–2 | 10–20 items | 6–12 months for one person or a small team |
| Typical indie title | 12–25 | 3–5 | 30–60 items (including consumables) | needs a content pipeline and tools |
| Simulation-oriented commercial title | 30–80 | 4–8 (including add-on content) | a hundred-plus items, long-term updates | measured in years, a series to spread costs |

Per-unit costs (magnitude references for estimating scope; not a commitment):

| Content unit | Unit cost | Notes |
| --- | --- | --- |
| One animal (3D) | 1–3 weeks | model, animation set (idle, walk, run, feed, sniff, hit, down), behavior parameters, sound, sign and compendium text |
| One map | 1–3 months | terrain, vegetation, habitats and need zones, species distribution and schedules, landmarks and routes |
| One piece of gear | 0.5–2 person-days | number tuning, model and audio, acquisition path |

- Species is the first cost item you hit a wall on: players can burn through several maps in a week, so count output in weeks per species — do the multiplication before greenlighting.
- Schedule anchors: the tracking-and-shooting prototype takes 3–6 weeks (slower than a normal shooter prototype — animals and sign are extra infrastructure); a vertical slice (one map, 3–5 species, full progression) takes 2–4 months; extrapolate by content volume from there.
- The order for cutting scope: cutting species is safe, cutting tracking is dangerous; cutting map count is safe, cutting ecological depth is dangerous.

## 6. How to Start the First Prototype

The first prototype makes one small map, two species and one gun, finished in 3–6 weeks, touching neither a gear tree nor multiple maps, with all-whitebox art.

1. **Week 1: animals and perception.** One herbivore plus one predator, three-channel perception, the alert state machine, fleeing and turning back; perception visualization is in from day one.
2. **Week 2: sign and tracking.** The trio of footprints, droppings and blood, with freshness tiers and decay; one binocular or highlight tool.
3. **Week 3: shooting and settlement.** Gun feel, hit-location resolution, one-shot kills versus follow-up pursuit, recovery and a results screen; add breath-holding to aiming.
4. **Weeks 4–5: wind and sound into the loop.** The wind vector, sound propagation, noise tiers for crouch-walking; add one "approach upwind" route and one "ambush downwind" route to the map to test whether the terrain reads.
5. **Week 6: external testing.** Find 5 people who have never played and have each play for 30 minutes, recording three things: do they crouch on their own; while tracking, do they say "it went that way"; after a miss, do they keep chasing or restart.

Success criteria (all observable):

- A single full hunt lands in 5–20 minutes, and testers can explain why that shot hit and why the animal got away.
- Testers actively use wind and sound information instead of treating it as decoration; ask "how do you know it is over here" and the answer mentions sign, wind or sound.
- After a failed shot, the behavior is to keep tracking, not to give up or restart.
- Change one perception parameter (say, the smell radius) and you can quantify its effect on kill success within 10 minutes.

If the test doesn't hold up, don't lay out more species: the loop is this genre's foundation; species are just bricks.

## 7. Common Pitfalls

1. **Shooting with no tracking**: the genre shrinks into a sniper range, half the ecology and sign content never exists, and players are bored after two rounds.
2. **An unreadable perception system**: wind, sound and smell are all implemented, but players cannot see or learn them — the same as not building them (§3.1, §4).
3. **Come-home-empty punishment too heavy**: an hour of hunting with nothing to show and no secondary targets turns patience into anger; give players incidental targets and information that persists.
4. **The shot costs nothing**: no ballistics, no breath control, no aftermath to a miss — tension drops to zero; the heart of the simulation side is making the one shot expensive.
5. **Homogeneous species**: ten animals whose behaviors differ only in numbers; stacking content volume produces no difference in experience (§3.5).
6. **Maps that are empty scenery**: no need zones, no approach routes, no landmarks — tracking degrades into luck.
7. **Obsessed with ballistics realism**: full aerodynamics and breathing/heartbeat simulation only drives most players away; a projectile model plus wind drift is enough (§4).
8. **A depiction level that keeps changing**: gore and carcass handling revised as you go means reworked art and animation; ratings and platform rules must be fixed once (§3.4).
9. **Content arithmetic never done**: players burn through several weeks of output in one week, and the update cadence collapses; multiply weeks per species by maps and gear (§5).
10. **No onboarding**: new players can't hit anything in their first hour and can't say why; make "reading the three channels" into staged teaching and referenceable prompts.

## Further Reading

- Game Design Handbook: core loops, numbers and progression curves — the underlying draft for §1 and §3.
- Programming Handbook: implementation details for perception AI, state machines and debug tools; corresponds to §4.
- Case Studies: how to break down simulation-oriented and long-running titles — read alongside when greenlighting and postmorteming.
- Indie Survival: scope control and scheduling discipline, complementing §5.
- Pitfalls & Anti-patterns: common pitfalls in content production and simulation-oriented projects — read against §7.
- Genre Handbooks · Stealth (Volume 3): general techniques for perception systems and alert state machines — the foundation of the tracking system.
- Genre Handbooks · Fishing (Volume 4): the sister page on the rhythm of waiting — cross-read on slow pacing and "the probability of coming home empty".
- Genre Handbooks · Survival Craft (Volume 1): a reference for host-system design when hunting is a gathering subsystem.
- Homework: first write a schedule table for one species — time slots, areas, behaviors, and perception priority for smell, sound and sight; then hand-calculate the expected time from first detection to a kill, and decide whether to start.
