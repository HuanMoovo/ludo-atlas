# Ludo Atlas · Genre Handbooks · Physics Puzzle

> **Genre Handbooks · Volume 2**. Positioning: a development handbook for the genre that turns the physics intuition everyone already uses — gravity, launching, stacking, breaking — into puzzle objects, and makes "predict and verify" the core pleasure.
> Companions: Game Design Handbook (core loops and tuning methods) · Programming Handbook (fixed timesteps, determinism and performance budgets) · Level Design Handbook (teaching sequences and the whitebox workflow) · Case Studies (breakdowns of success and failure cases).
> This page carries no external links; benchmark titles are widely known works only, and the figures here are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: physics puzzle is the puzzle genre **with physics simulation as its first mechanic**. Players solve puzzles not with precise switches and rules, but with everyday intuitions — gravity, elasticity, friction, connections; the simulation makes feedback continuous and believable, and at the same time introduces noise. All of the design difficulty concentrates on one thing: keeping the simulation's uncertainty inside a range players can learn and predict.

State one principle that runs through this whole page first: **determinism and predictability take priority over realism**. An erratic simulation degrades into a game of luck, and players chalk their failures up to the game; only a predictable simulation is a learnable rule set. Physics parameters are design parameters, not physical constants: tune until it plays and predicts, then consider whether it looks real (expanded in §3.1).

The core loop, written as a verb chain:

`read the situation → work out a plan in your head → act → watch the simulation play out → compare against expectation → adjust and try again`

This loop is measured in seconds: one attempt takes 5–60 seconds, and a level consists of a few to a few dozen attempts. It holds on two preconditions: the simulation's results can be explained (§3.1), and failure is cheap (§3.5).

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Logic puzzle | The rules are discrete and the states enumerable, so the answer can be reached by pure reasoning; a physics puzzle's intermediate states are continuous, and it must be verified by hand (compare the Puzzle page in the Genre Handbooks) |
| Sandbox building | They share the physics simulation, but a sandbox sells free creation, with no puzzle and no failure; a physics puzzle has goals, constraints and retries |
| Platformer | Physics acts on the character, selling game feel; in a physics puzzle, physics acts on the puzzle objects, selling prediction |
| Action game | Once clearing the game depends mainly on time limits and hand speed, it has slid into action-game territory; treat game feel and pacing by action-game methods |

A self-check question: replace the physics simulation with a fixed animation — does the game still hold up? If the answer is "no", what you are building is a physics puzzle.

Team and market profile: 2–10 people is the common team size, and 2D is lower than 3D in both barrier and cost; both mobile and premium PC hold up; art is elastic, but the readability of materials and states must take priority over visual fidelity.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Prediction paid off**: the player works out a route in their head, and after they act, the simulation plays out as expected. "I knew that would happen" is worth more than "it actually worked".
2. **Visible causality**: every failure can be attributed (angle, force, mass, geometric jam), the player accepts the verdict, and then revises the plan themselves.
3. **Cheap verification**: one attempt takes seconds, resetting is frictionless, and revising the plan doesn't mean tearing it all up.
4. **Controlled surprises**: delights like chain collapses and two birds with one stone are bonuses, but must never become the only way to clear a level.
5. **Freedom of solution**: players are allowed to leave a personal signature on a level (saving materials, taking odd routes, brute force), and the design is tolerant of those playstyles.

Benchmark titles (play them yourself before breaking them down; physics game feel can only be calibrated by hand):

| Title | What to learn from it |
| --- | --- |
| Angry Birds | Visualizing the causal link from launch arcs to structural destruction; one failure costs only seconds |
| Cut the Rope | The continuous physics of ropes and pendulums; multiple solutions and star ratings coexist without conflict |
| Human: Fall Flat | Ragdoll physics turns uncertainty into comedy: physics is both the puzzle and the punchline |
| World of Goo | Puzzles built from connections and load-bearing; structural stability converts directly into level difficulty |
| Poly Bridge | Physics puzzle as construction: budget, stress and collapse replays are the teaching |
| Kerbal Space Program | Hardcore simulation can carry puzzles too; "failing beautifully" is content in itself |

The common thread: simulation results are readable at a glance, retries cost seconds, and surprises mostly stay within what players can explain to themselves.

## 3. Design Essentials

### 3.1 Physics as a Mechanic: Determinism over Realism

Get one thing straight first: gravity, friction, elasticity and damping are all design knobs, not natural constants to be reproduced. Move real values (gravity constants like 9.8 m/s²) straight into the game and what you mostly get is soft arcs, collapsing stacks and sluggish falls; the common approach for action-oriented physics puzzles is to scale gravity up, increase damping and keep elasticity low, so every simulation converges quickly to rest and every step stays on screen.

Determinism checklist (the same input must produce the same result):

- The simulation runs on a fixed timestep (commonly 60Hz), with rendering decoupled from physics; the physics step never floats with the frame rate.
- Random numbers are used only for scenery and effects, never in force calculations; when randomness is required, use a seed that can be chosen and recorded.
- Bound the value ranges: cap maximum velocity, maximum impulse and joint tension to prevent the unstable simulation where "one contact explodes the whole scene".
- Reproducible failure takes priority over pixel precision: the same level and the same move must replay stably; cross-platform floating-point differences are covered by lenient judging (§3.5).

Realism versus readability (tune the prototype stable by the right-hand column first, then dial it back locally as the theme requires):

| Parameter intuition | Realistic leaning (use with care) | Arcade leaning (common practice) |
| --- | --- | --- |
| Gravity strength | Slow and floaty — fits floating themes | Fast and crisp — the whole arc plays out on one screen |
| Elasticity decay | Bounces on and on without stopping | Converges within two or three bounces |
| Friction and damping | Sliding and swinging drag on for a long time | Comes to rest quickly, states easy to read |
| Mass differences | Extreme enough that objects won't budge | Within 10× — differences perceptible and usable |

### 3.2 The Mechanics List and a Cognitive-Load Budget

Physics-puzzle mechanics are a set of forces and constraints answering "what can be done to objects". The common list (each entry with its readability requirement):

| Mechanic | Gameplay use | Readability points |
| --- | --- | --- |
| Gravity and stacking | Balance, order, dominoes | Center of mass and support relationships judgeable at a glance |
| Elasticity (springs, launch pads) | Charging, crossing, chain jumps | Deformation and sound telegraph direction and force |
| Buoyancy and fluids | Raising and lowering, transport, water levels | Floating and sinking states have clear visuals (water lines, bubbles) |
| Friction and surface materials | Ramps, braking, sliding | Material differences must be visually distinguishable |
| Connectors (ropes, chains, hinges, welds) | Pendulums, pulling, building | Connection points and their tightness are visualized |
| Destruction and fracture | Opening paths, knocking things down, dismantling | Cracks telegraph the break; no sudden collapses |
| External forces (launching, wind, magnets, explosions) | The player's main input | Force and direction controllable and finely adjustable |
| Time control (slow motion, pause) | Observation and precise action | Slow motion is an aid, not a crutch; overuse dilutes the challenge |

Cognitive-load budget (reference values; calibrate against your own tests):

| Budget item | Suggested cap | Notes |
| --- | --- | --- |
| New mechanics per level | 1 | Forces and constraints count as mechanics; retuned numbers and reskins do not |
| Active objects on screen | 20–60 (reference) | Active objects can be many, but manipulable objects must be few (commonly 3–7) |
| Simultaneously available action verbs | 2–3 | Drag, launch, rotate, build — the more, the messier |
| Material types per level | 3–8 | The longer the material list, the harder intuition is to build |
| Hidden variables the solution depends on | 0 | Mass and friction coefficients the player cannot see must not gate puzzle progress |

Every new mechanic and material has to pass the one-sentence test: can you explain what it does in one sentence? If not, leave it out for now.

### 3.3 Teaching Sequence and Solution Diversity

Teaching follows the three-stage format (show, use, variation, combination), but a physics puzzle has one more thing to teach: **make players trust that their own intuition is trustworthy here**. The whole value of the first few levels is building the trust that "what you work out in your head is what the simulation will produce".

1. **Show**: watch a complete causal chain in a zero-failure scene; the shot, the hit, the collapse, replayed once in slow motion.
2. **Use**: a level using only the new mechanic, stringing 2–3 progressive goals (break it, then break it precisely, then break it under a resource limit).
3. **Variation**: replay with different mass, a different material, a different force direction; the player starts to break away from imitation.
4. **Combination**: cross it with old mechanics and enter the real puzzle-solving territory.

Multiple solutions or a single solution is the first decision a physics puzzle has to declare:

| Leaning | Suits | The cost |
| --- | --- | --- |
| Multiple solutions (recommended default) | Casual themes, share-and-create play, physics fun itself | High verification cost — every level's main solutions must be exhausted; extreme cheesing can break the pacing |
| Single solution | Precision building and engineering themes, speedrun-competitive play | Puzzles turn brittle — widen the judging a little and they fall apart; players easily get stuck on "the solution was right but the execution wasn't" |

The practical compromise: judging watches "was the goal achieved", not "was the process reproduced"; design one official solution but accept that shortcuts exist; the tool for separating players is scoring and achievements, not walling off the only path.

### 3.4 Physics Tuning: Feel Right Comes First

The goal of tuning is not a good-looking parameter table; it is that players dare to bet on their intuition. "Feels right" can be verified:

- **The rule of three**: after teaching, a new player should hit the expected result within three attempts on the same setup; more than three and the parameters are too erratic.
- **Dispersion check**: repeat the same action ten times — the distribution of results must be narrow; where dispersion is large, either narrow the randomness or switch to a deterministic approach.
- **Plausibility first**: looking reasonable matters more than being physically correct; cut realism that plays no part in gameplay (full rigid-body rotation, cloth-level detail) without hesitation, and spend the budget on the parts players can understand.

Tuning workflow (the three rules you'll use every day):

- All parameters in tables and hot-reloadable: mass, gravity scale, elasticity, friction, damping, joint stiffness, maximum velocity; scattered magic numbers strictly forbidden.
- Judge only by screen recordings: slow motion, frame stepping and overlaid trajectory lines, all three at hand; "feel" is triangulated through A/B comparison.
- One sentence per change: what changed, why, and what happened; without this log, two weeks later nobody remembers why the friction coefficient is 0.3.

Starting values (2D reference; calibrate against tests in your own project): begin with gravity scaled 1.5–3× above realistic; elasticity coefficient 0.1–0.5, so objects settle within a few bounces; linear damping 0.1–1 as a first rough pass; keep mass ratios within the same level under 10×.

### 3.5 Softlock Prevention and Lenient Judging

Physics simulation has one more failure mode than logic puzzles: state softlocks. Prevention is designed around a single overarching principle: **the player has an exit at every moment**.

| Softlock situation | Prevention |
| --- | --- |
| An object falls out of the playable area | Recycle on exit: return it to its original position or the respawn point; never let any object "disappear" |
| Stuck in a geometric crevice, jittering endlessly | One-button reset (completes within 1 second); run rest detection on active objects and snap them back if they haven't settled in a long time |
| A key component breaks or is used up and the solution is no longer reachable | Unsolvable detection (rule triggers or a simplified solvability check); on a hit, notify the player and return to the nearest checkpoint |
| A dead end in the flow | Reset available at any moment; no penalty, no confirmation dialog, no rating lost |
| No valid input for a long time | Gentle camera guidance, highlight interactable objects; do not pop up tutorial windows that interrupt thinking |

- **Reset is a first-class citizen**: keep a full reset under 1 second; in a level where setting up again takes 30 seconds, the cost of trial and error is raised by an order of magnitude.
- **Undo provided where needed**: for placement-style puzzles, do operation-level undo where possible, all the way back to the level's start; the alternative is state snapshots plus an action log.
- **Three rules for lenient judging**: the judging area is one layer larger than the visual target (a common tolerance is 10–30% of the target's size); partial success passes first (hit the main goal and the level is cleared, perfection is left to scoring); the micro-jitter phase is judged by a steady-state threshold, with no points deducted for the last 1% of wobble.
- **Simulation-side finishing touches against deadlock**: give objects a sleep threshold, so they sleep after a long stretch at low speed; cap the number of simultaneously active fragments in chain structures, so a "sea of debris" doesn't drag down the frame rate and readability.

## 4. Technical Essentials

The engineering difficulty concentrates in four places: the simulation foundation, determinism and reproducibility, the toolchain, and performance and platforms. Everything below is engine-agnostic; specific APIs and performance methods unfold in the Programming Handbook.

**Simulation foundation**

- Physics always runs on a fixed timestep (commonly 60Hz), and rendering only interpolates; never use a variable timestep that changes with the frame rate.
- Enable continuous collision detection or substepping for fast-moving objects to prevent tunneling; fix the speed cap for launched objects at the design layer.
- Configure materials as "material pairs" (elasticity, friction, damping) in a central table; encapsulate joints as components by purpose: rope (length, damping, break threshold), hinge, spring, weld — reuse beats haphazard tuning.
- Choose the destruction approach first: pre-fracturing (stable, cheap on CPU, the first choice for structural puzzles) versus runtime cutting (free-form, expensive — only for games whose selling point is dismantling); start with pre-fracturing.
- Simulation LOD and caps: reduce the update rate or sleep distant objects, run fragments and effects through object pools, and cap the number of simultaneously active objects in chain reactions.

**Determinism and reproducibility**

- Fixed timestep, fixed iteration count and a choosable seed — only with all three can you talk about "same input, same result"; this is the infrastructure for failure replays and batch acceptance.
- Store one reference clearing replay per level (an input sequence) and batch-replay after changing physics parameters or engine versions; levels that diverge automatically enter the regression list.
- Cross-platform floating-point differences are a reality: don't demand frame-accurate reproduction; accept with lenient judging and result ranges; if you really want speedrun rankings, then consider platform locking and server-side validation.

**Toolchain (the highest-return investment)**

- Trajectory prediction lines and force indicators: the pre-action prediction line for launching and force-based moves is core UI, not a garnish; players learn your physics through it.
- Debug visualization toggles: contact points, force vectors, velocity, sleep state and joint tension, all inspectable on one screen, shared by tuners and level designers.
- Slow motion and frame stepping: for tuning, for recording teaching replays, and as an observation aid for players — one tool, three uses.
- Levels and parameters data-driven: levels, materials and mechanisms all live in data files (text is fine), so changing a level doesn't mean changing code; get the data format first, build the editor later.
- Telemetry: attempts per level, reset counts, failure-point distribution, single-attempt duration; a difficulty curve can only grow out of real attempt data.

**Performance and platforms**

- 2D's rigid-body budget is usually several orders of magnitude higher than 3D's: on mobile, keep active rigid bodies in the dozens (reference), and it can loosen further with sleeping and simulation LOD; 3D is far more sensitive to counts and joint complexity.
- Touchscreens require redesigning the interaction: enlarge the grab radius, snap to key points, auto-pan the camera when dragging to the screen edge; don't port mouse-level pixel precision directly.
- Keep mouse, touch and gamepad inputs equivalent, and build a touch-only "preview before release" so aiming is learnable on all three devices.

## 5. Content Volume and Workload Reference

Start with the formula: **content volume = number of mechanics × solution space**, not level count. If three mechanics cross into a deep enough solution space, forty levels make a complete work; if ten mechanics each stand alone, a hundred levels are just ten unconnected mini-games.

Reference ranges (2D, 1–3 people):

| Project shape | Mechanics | Level count | Timeline | Notes |
| --- | --- | --- | --- | --- |
| Game-feel prototype | 1–2 | 3–5 experimental levels | 1–2 weeks | No art; validates "can this be predicted" |
| Jam-sized piece | 2–3 | 10–20 levels | 2–6 weeks | One material set, one teaching line |
| Small commercial title | 3–5 | 40–80 levels | 3–8 months | Mobile or premium PC |
| Full commercial scope | 8–12 | 100–200 levels | 1.5–3 years | Depth comes from mechanic crossovers, not level count |

Workload profile:

- Level iteration counts run above average: a whitebox becomes playable in 1 day and commonly takes 3–8 rounds to tune stable; schedule on 1–3 playable prototypes per day — planning for ten a day is certain to go wrong.
- Global parameter regression must be costed as its own line: changing parameters like gravity, elasticity or mass means retesting every accepted level; write the parameter freeze point into the schedule up front.
- 3D is not 2D scaled up linearly: velocity, angles and contact surfaces each gain a layer, and readability and tuning difficulty go up a whole step.
- Art is elastic, but don't waste it: material and state differences (ice, wood, stone) are gameplay information and must be distinguishable at a glance; scene decoration can be minimal.
- Sound's priority is often underestimated: the audio for launching, breaking and settling carries a large share of causal feedback and is worth investing in before visual effects.

## 6. How to Start the First Prototype

Goal: answer one question within two weeks — "can this simulation be predicted". No art, story or menus.

1. (Days 1–2) Minimum simulation: one ground plane, one kind of interactable object, one way to apply force (launch or drag), running on a fixed timestep; wire up the reset key and slow-motion key on day one.
2. (Days 3–4) Parameters into tables: gravity, elasticity, friction, mass and damping all in files and hot-reloadable at runtime.
3. (Day 5) Trajectory visualization: the pre-action prediction line and hit feedback; it is the most important "game-feel organ" of the prototype phase.
4. (Days 6–8) Five experimental levels: one pure demonstration, two single-mechanic, two with variations; each level's goal stated in one sentence (break, deliver, stack high, catch).
5. (Days 9–12) Playtest with outsiders: at least 3 people who haven't seen the project, staying silent throughout; record points where prediction fails, stuck points, and the seconds between failure and the next attempt.
6. (Days 13–14) Retro and converge: tune parameters by the rule of three in §3.4, add exits per §3.5; add no new mechanics.

Success criteria (all observable):

- After teaching, testers can hit the goal three times in a row; after failing they retry on their own rather than being asked to.
- Every failure can be attributed by the tester to one of four categories: angle, force, mass, geometric jam.
- With all art replaced by color blocks, testers still want to keep playing for 10+ minutes.
- For any one physics parameter you change, you can quantify its effect on the success rate within 5 minutes.

## 7. Common Pitfalls

1. **Treating physical constants as gospel**: real gravity and friction go straight in, arcs turn soft and stacks collapse, and then months go into "fixing the realism". Parameters are design knobs (§3.1).
2. **Erratic simulation results**: the same action gives different outcomes and players chalk failures up to the game; once the "game of luck" verdict forms, it is nearly impossible to recover from.
3. **Chasing realism where it doesn't touch gameplay**: the budget goes into full rigid-body rotation, cloth and fluid physics detail, and nobody benefits at the gameplay level.
4. **Cognitive overload**: one level throws in five materials and six mechanisms at once; reading the situation takes all the effort and solving is zero fun.
5. **A single solution paired with strict judging**: only one solution exists, and judging also demands identical execution; the player gets the solution right and still can't pass.
6. **No reset exit**: after an object jams in a crevice, falls out of bounds or a key part breaks, the player's only option is to quit and re-enter. Any softlock is a design incident.
7. **Expensive retries**: restarting means 30 seconds of re-setup and re-watching a cutscene; once trial and error gets expensive, players degrade from experimenting to guessing.
8. **Parameters not in tables**: tuning means editing code and restarting — an efficiency black hole and the most common time killer in physics-based projects.
9. **No trajectory or causality visualization**: players can only flail around to learn the feel, and the learning curve is pointlessly stretched.
10. **Unstable simulation**: tunneling through walls, stacks exploding apart, high-frequency jitter; treat it as a bug the first time it appears — once trust breaks, it can't be repaired.
11. **Trading execution precision for puzzle-solving**: treating "one slip from failure" as difficulty produces an action game that pleases neither audience.
12. **Porting to mobile as-is**: pixel-precise dragging mapped straight to the finger, and no grabbable object can be held.
13. **Testing only on yourself**: the author's familiarity with their own simulation hides every readability problem; verification must come from someone else.

## Further Reading

- Game Design Handbook: core loops, number tables and tuning methods; §3.4 here pairs with its numbers section.
- Programming Handbook: the engineering detail of fixed timesteps, determinism, performance budgets and toolchains.
- Level Design Handbook: teaching sequences, pacing curves and the whitebox workflow — the full expansion of §3.3 here.
- Case Studies: breakdown methods for success and failure cases; consult it when estimating scope.
- The Puzzle page in the Genre Handbooks: rule restraint, hint systems and solver practice from the logic-puzzle side, a mutual reference with this page.
- Homework: hand-build a single scene of "launch plus collapse" and tune it until someone else can hit the target within three tries; then replay Angry Birds and Human: Fall Flat and log "how cheap failure is and how funny the surprises are" in each.

What a physics puzzle sells was never the physics engine: it is those few seconds when the player's everyday intuition about physics is reliably honored — and occasionally cleverly exploited.
