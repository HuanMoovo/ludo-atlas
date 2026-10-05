# Ludo Atlas · Genre Handbooks · Puzzle-Platformer

> **Genre Handbooks · Volume 3**. Positioning: the genre that stitches "jumping" and "thinking" into a single fabric. Movement abilities are puzzle elements, and the puzzle's answer defines the jump route; players figure it out first, then jump it out, and the two pleasures relay back and forth.
> Companions: Game Design Handbook (core loops and mechanics budget) · Level Design Handbook (teaching sequences and the whitebox workflow) · Programming Handbook (character control, state and tooling) · Indie Survival (scope control and scheduling).
> This page carries no external links; benchmark titles are widely known works only, and the figures are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: a puzzle-platformer is the genre where **movement and puzzles are each other's question and answer**. Movement abilities mark out "where you can reach", and the puzzle layout decides "where to go and in what order"; players clear the game in their heads first, then execute the answer with their hands. Three scales share one logic: a single attempt (seconds to 1 minute) tests one route, a room (1–10 minutes) cashes out one insight, and a chapter (20 minutes to 2 hours) masters one mechanical language.

`observe the room → form a hypothesis → plan the route → execute the movement → fail or pass → correct your mental model → try again`

This loop runs half a beat slower than a platformer and half a beat faster than a logic puzzle, and it counts in units of "one room". It stands on exactly two preconditions: failures can be attributed (you can tell whether you thought wrong or jumped wrong), and retries are cheap (a restart is measured in seconds). Lose either one and the experience slides into the swamp of "I don't know what I did wrong".

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Platformer | The platformer tests execution, and movement is itself the content; the puzzle-platformer's movement serves the puzzle — what hangs on the walls is a question, not a path |
| Logic puzzle | The logic puzzle's inputs are choice and placement; the puzzle-platformer's solution has to be "done", and execution is the means of verification, not the test |
| Metroidvania | The Metroidvania organizes exploration with ability gates, and progress means a longer ability list; the puzzle-platformer's ability list is usually fixed, and progress is understanding and orchestration deepening |
| Physics puzzle | The physics puzzle's variable is the simulation itself, and the fun is playing with the system; the puzzle-platformer's variables are the level arrangement and the movement abilities, with simulation as no more than the execution medium |

A self-check question: swap the jumping for "click once and walk straight there" — does the room still hold up? If yes, you are making a puzzle; remove the puzzle and keep only the platforming — does it still hold up? If yes, you are making a platformer. Only when neither holds up are you making a puzzle-platformer. Team caliber: 2–6 people can build it; the engineering bar is moderate, art is flexible, and what is scarce is designers who can both produce puzzles and personally polish the game feel. In one line: what a puzzle-platformer sells is not the level count but how densely the two payoffs — "figuring it out" and "jumping it out" — chain together.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **A double highlight**: the moment of insight and the moment of execution arrive on each other's heels — first the "aha", then the "nice"; miss either and it falls flat.
2. **Clean attribution**: on failure, players can say whether they thought wrong or jumped badly — the source of trust and the precondition for another attempt.
3. **Low-pressure trial and error**: restarts are measured in seconds and experiments carry no penalty; players who dare not experiment cannot solve puzzles.
4. **Trust and alternation**: the same input gives the same result; thinking stretches and doing stretches take turns — when thought tires, jump a stretch; when jumping tires, think a stretch.

Negative feelings (any one of them is a red flag): thought blocked by execution (you see the answer but cannot do it); hand speed punished by the puzzle (you jump perfectly but do not know where to go); muddled attribution (you cannot tell whether you were wrong or the game is broken); busywork (every retry first runs an irrelevant stretch of route).

Benchmark titles (all widely known works; play them before breaking them down):

| Title | What to learn from it |
| --- | --- |
| Braid | Time rewind pushes the cost of trial and error to zero, turning failure from a price into information; one time mechanic deeply coupled with the level puzzles |
| FEZ | Rotating the view by one step rewrites spatial relationships; one mechanic sustained through the whole game — a model of mechanical restraint |
| The Talos Principle | A teaching textbook of one concept per room; thinking is the main gameplay, and execution tolerance is extremely high |
| Celeste | Single-screen rooms and instant retries; failure staging short enough not to break your mindset |
| Super Mario series | Movement is puzzle-solving; the same jump set keeps growing new uses as different level elements interrogate it |

What these works share: one idea per room; once figured out, execution is not torture; the failure loop is measured in seconds; every element is readable from the picture alone, with no text explanations. Hit all four and the game will not be bad.

## 3. Design Essentials

### 3.1 Mechanics Coupling: Movement Abilities Are Puzzle Elements

This genre's vital nerve is coupling: jumping cannot be just a travel tool, and puzzles cannot be just locks hidden behind doors. From day one, list two resource lines separately — the movement side (jump, dash, wall jump, grab, carry, throw, glide) and the level side (switches, pressure plates, pushable blocks, moving platforms, gravity zones, portals, keys and locks) — and design levels with "one movement" as the smallest unit.

Four coupling modes, rotated when setting puzzles:

| Coupling mode | Structure | Example |
| --- | --- | --- |
| Ability as key | A route segment is passable only with a certain ability | A ledge only a wall jump can reach, with a switch on top |
| Landing as trigger | The movement act itself changes the world | Standing on a pressure plate opens a door — the landing spot is the mechanism |
| World changes movement | Level elements temporarily rewrite movement rules | Anti-gravity zones, low-friction surfaces, forced bouncing |
| Two-way combination | Two mechanics cross into a third meaning | Time rewind plus dash, storing a dash to use again on the way back |

Budget discipline: 2–4 movement abilities across the whole game, 6–12 level elements. Every ability added is not one more verb but one more combination table with the old abilities, and the test volume doubles with it.

Metrics and balancing: first measure the full-speed jump's horizontal distance D and maximum jump height (see the Platformer page in the Genre Handbooks for the method), then place puzzle-platformer jumps in three tiers — 0.8D, 1.0D, 1.2D — and never make execution stretches more aggressive than the base table. One principle runs through: thinking difficulty and execution difficulty rise and fall against each other — the deeper the puzzle, the more forgiving the landing spots; if you really want to test execution, give the room full information and a straightforward solution.

### 3.2 One Room, One Concept, and Combination Variations

Principle: a room introduces only one core concept, and the second new thing can only be a variation of that same concept — players' comprehension is a budget, not unlimited. Rooms are single-screen or small-scale by default: one screen holds one idea, so the eye never hunts back and forth; restarts skip the map run, pushing attempt cost toward zero; the camera is fixed, so the room's state is taken in at a glance. Long scrolling stretches are reserved for transitions and atmosphere, not for posing questions.

Variations turn four knobs:

| Knob | Change | Example |
| --- | --- | --- |
| Space | change direction, distance, height | move the same mechanism from a courtyard to a narrow corridor |
| Time | add a limit, change the timing | a platform beats once every three ticks; now every two |
| Count | add one element of the same kind | one switch becomes two, and order starts to carry meaning |
| Condition | restrict an ability or a resource | this room forbids the dash |

Combination discipline: the number of crossings between mechanics is the size of the puzzle space. Any two mechanics must yield at least 3–5 good rooms; if they cannot, the pair is dead — swap it early. Close a chapter with a combination room as the exam: the answer usually calls on two or three mechanics, and there is more than one solution.

Walk every room past a checklist: is the goal visible at first glance? Is this room one question or three? Can the solution be told in one sentence? Which old concept does it reuse — a room without reuse is an island.

### 3.3 Teaching Sequences: Teach, Test, Vary

This genre teaches two things: the verbs in the hands (how jump and dash work) and the concepts in the head (how elements fit together). Both lines go through teach, test and vary, and the control line always runs ahead of the concept line.

| Stage | What is taught | Environment | Failure cost |
| --- | --- | --- | --- |
| Teach · controls | what the new verb does | flat ground, no pits, no damage; breaking it is fine | zero |
| Teach · concept | the first correct use of an element and an ability | a single-step problem with the goal right there | tiny |
| Test | let players use it themselves, no prompts | a low-pressure room where one slip is acceptable | small |
| Vary | change one condition and use it again | a medium room | present, but checkpoints are close |
| Combine | use it together with an old mechanic | mid-to-late chapter | death allowed, retries must be fast |

Two supplements:

- Teach only one new thing at a time; teaching rooms carry no death penalty — trial and error is itself where clues come from.
- Acceptance method: find someone who has never played, stay silent throughout, and record when they stop, for how long, and whether they stare at the screen or blank out. Staring at the screen means the question has landed; blanking out means it is one breath short.

### 3.4 Anti-Frustration: Checkpoints, Fast Retries and Stuck-Point Hints

This genre has two kinds of failure, handled separately: a bad jump is an execution failure, treated with low retry cost; a wrong idea is a cognitive failure, treated with hints and safe experimentation.

| Failure type | Remedy | Goal |
| --- | --- | --- |
| Bad jump | room-level checkpoints, one-button instant restart (no menu), short and quiet failure staging | retries of 1–3 seconds, emotional cost held down |
| Wrong idea | tiered hints (point at the area → name the mechanic → give the first step → demonstrate the solution), a no-death sandbox, stuck detection | stuck points have a dignified way out; players dare to experiment |

Calibrate thresholds from the median of your own test data; never copy them: when something runs 2–3 times past the median, let a weak-hint entry appear quietly; rooms with clearly abnormal restart counts get audited for design defects rather than punished harder. For players who "figured it out but cannot jump it", add one more layer: accessibility options, room skip, denser checkpoints; these tools are decoupled from achievements — using them affects neither completion nor story, and hardcore records are flagged separately.

Three red lines: hints never pop up automatically and interrupt thinking — at most, the entry appears quietly; hint tone never judges, stating only facts and direction; no score deduction, no progress wipe, no retries counted into ratings — retries are gameplay in this genre, not mistakes.

### 3.5 Tools First: Editors and Hot Reload

The iron law of development order matches Genre Handbooks · Puzzle: mechanics prototype → room editor (or at least a data format) → content production → art pass. This genre adds three hard requirements on top:

- Rooms as data: every room is readable, diffable data (entities, coordinates, mechanism wiring, goals), hot-reloaded at runtime; changing a room equals changing a line of data, and you can teleport straight into any room to test it without clearing what comes before.
- Visual mechanism wiring: which door a switch connects to, and who controls a door, can be drawn in the editor and overlaid at runtime.
- Live parameter tuning: gravity, jump, dash and platform speed are all adjustable while running and saved back to file; feel and puzzle balance are two faces of the same set of knobs.

Acceptance criterion: a non-programmer can lay out a playable room in 30 seconds and verify it with a one-button hot reload. If that fails, content throughput will collapse sooner or later.

## 4. Technical Essentials

This genre's stack is roughly the platformer plus state management: character control and game feel follow the foundation laid out in the Platformer page in the Genre Handbooks (kinematic controller, fixed timestep, coyote time, input buffering); only what it adds is written here.

**Movement, state and reset**

- Implement every movement ability as an independent state with an independent parameter set, and write down explicit priorities for switching between and coexisting with abilities (half-way up a climb, whose jump is it? there must be a clear rule); pair every new ability with a greybox test course.
- After parameter changes, batch-regress against recorded clears of existing levels so one tuning change cannot wreck a region of old rooms; ability-combination testing scales with the combination count (3 abilities give 3 pairwise crossings and 1 triple crossing), with a test room per group.
- The room is the smallest reset unit: entering saves the game, dying returns to a clean initial state, with mechanisms, crates, timers and platform phases all reset; use "rebuild" instead of "in-place reset", re-instantiating the entire room from data — leftover state is a breeding ground for bugs.
- World-level progress (keys, unlocks, story) and room-level transient state (switches, crate positions) go into two separate stores that never contaminate each other; saves record an action log, not state snapshots.

**Determinism and replay**

- Fixed physics timestep, seedable random sources; for puzzle reproducibility, stability matters more than realism.
- Input recording plus deterministic replay does two jobs: developer recorded regression (after physics or level changes, batch-replay known solutions to find regressions) and player-facing ghost replays and racing content. For time-rewind mechanics, store state snapshots in a ring buffer — low-frequency full snapshots plus snapshot deltas is the common practice — and write rewind duration and memory limits into the design parameters.
- An honest reminder: this genre's solvability cannot be batch-verified by a solver the way pure logic puzzles can, because solutions involve continuous action; what can be automated is a coarse reachability check and replay regression — the rest is human testing.

**Mechanisms and signal systems**

- Organize mechanisms with a small signal system: the connections from sources (switches, pressure plates, timers) to targets (doors, platforms, hazards) are data — drawn in the editor, and one graph explains cause and effect at runtime.
- Mechanisms need a glance-readable look for all three states — open, closed, in progress; dangerous elements give an audiovisual warning before they engage, so players do not mistake "did not see it" for "did not think of it".

**Toolchain**

- The essential debug bench: mechanism-state overlay, collision boxes, trajectory and arc previews, room bounds, goal-reachability highlight, per-room timing and death stats; hot reload from day one, so data edits never need a restart.
- Room-level telemetry from the prototype stage onward: time spent, death count, restart count, hint tier. This genre's difficulty curve is calibrated entirely by it.

## 5. Content Volume and Workload Reference

Conversion rule: **playtime ≈ number of rooms × average time per room**, and half of the per-room time is thinking while half is jumping, with enormous variance — always estimate from the median of your own test data.

Reference ranges (2–6 person team):

| Scale | Room volume | Playtime | Timeline | Notes |
| --- | --- | --- | --- | --- |
| Mechanics prototype | 1 room plus a test course | minutes | 2–4 weeks | validates coupling and feel only |
| Jam and small scope | 20–40 rooms | 30 minutes to 1 hour | 1–2 months | one mechanic, one theme |
| Small commercial | 80–150 rooms | 3–6 hours | 6–12 months | two or three mechanics taken deep |
| Full commercial scope | 200–400 rooms | 8–15 hours | 1.5–3 years | combination throughput sets the ceiling |

Workload figures (for schedule calibration):

- A room usually takes 3–8 iterations from idea to sign-off; half a day for the first version, one to two days to polish until solid. One person steadily produces 1–3 playable room prototypes a day; scheduling ten a day will derail for certain.
- This genre carries double testing cost: every room must be verified for "can it be thought through" (cognitive) and "can it be jumped through" (execution); prepare a test budget 1.5–2 times that of an ordinary puzzle game.
- Teaching rooms take about 2–3 times the polish time of ordinary rooms; art's key investment is consistency and readability — state specs for moving elements and mechanisms are worth more than extra art assets, and "can stand" versus "cannot stand", "can touch" versus "will die" must be discernible at a glance.

Scope control: this genre's typical death is not failing to finish but adding mechanics endlessly while rooms get thinner. Freeze the mechanic list after a certain version and write new ideas down for a sequel; cutting the weakest 20% of rooms before launch should not hurt on a play-through — the experience will only improve.

## 6. How to Start the First Prototype

Goal: answer one question in two to four weeks — is stitching "jumping" and "thinking" together actually fun? Do not casually start building the game.

1. **Pick one coupling (first half of week 1)**: one movement ability plus one or two level elements; write the rule in one sentence, precise down to "dash a crate onto a pressure plate to open a door". If the combination cannot be told in one sentence, do not build it yet.
2. **Draw ten rooms on paper (first half of week 1)**: draw rooms and routes on grid paper and walk through one-room-one-concept and teach, test, vary; ideas cut at the paper stage are the cheapest.
3. **Greybox and metrics (weeks 1–2)**: build the character controller and single-screen room loading in the engine; first measure the jump radius table (full-speed jump distance, jump height, air time), then place platforms from the table. Ugly is expected.
4. **Three lifeline tools (week 2)**: room-level checkpoints, one-button restart, tiered-hint entry. Without them, all playtest feedback is distorted.
5. **A ten-room sequence (weeks 2–3)**: teach controls, teach concepts, test and vary in their places, ending with an exam room that combines two concepts.
6. **The silent test (weeks 3–4)**: find 3–5 people who have never played, stay silent throughout, and record two things: where they stop (cognitive problems) and where they die (execution problems); attribute every stuck point to a concrete design defect, fix it, then run another round.

Success criteria (all observable):

- At least 2 of 3 testers clear the full sequence without verbal guidance, with no more than two stuck points per person, each attributable to design (the question did not land, execution too harsh, feedback unclear) rather than "how did they not figure it out".
- After figuring out a solution, testers clear it within one or two attempts; complaints of "I know how to get through but I just cannot" mean execution tolerance is out of balance.
- Strip all art and audio and the sequence still holds; you yourself still want to open it again during these four weeks.

## 7. Common Pitfalls

1. **Two separate games**: jumping is jumping and puzzles are puzzles, with platforms only for travel. Coupling never got built — two half-finished games stapled together.
2. **Muddled attribution**: failure feedback does not say whether the idea or the jump was wrong, and players just think the game is broken. Visible landing spots, marks that stay at death positions, and a clean initial state on restart — all three, or it fails.
3. **Figured out but cannot jump it**: thinking and execution difficulty both maxed out, or execution difficulty posing as puzzle difficulty, ruining the insight into corporal punishment. The balancing principle is one line: the harder the puzzle, the more forgiving the execution.
4. **Multiple concepts per room**: one room introduces two new things at once and players retain neither.
5. **Teaching missing**: a new element's first appearance comes with a hard room, and players circle inside "did I get it wrong or is it just like this".
6. **Unclean room state**: after a restart, switches have not reset and crates are still in place, adding a variable to the puzzle logic out of thin air. Use rebuild instead of in-place reset.
7. **Stingy checkpoints**: a retry costs ten-odd seconds of backtracking, breaking the thinking rhythm and sliding players from experimentation into caution.
8. **Hints missing or humiliating**: players who thought wrong have no way out, or are driven away by copy like "you could not even think of that". A tiered-hint entry is standard equipment.
9. **Non-deterministic physics**: change machines or drop a frame and solutions stop working; this class of problem costs more to fix than the puzzles themselves.
10. **Rooms too large**: scrolling rooms flatten one-room-one-concept, turn retries into map runs, and make problems impossible to localize to a specific stretch.
11. **No editor**: dozens of rooms are hand-coded before anyone remembers to build tools, and the rework eats a quarter.

## Further Reading

- Genre Handbooks · Platformer (Volume 1): the three elements of game feel, camera and jump-radius measurement — the base draft for §3.1 and §4 of this page.
- Genre Handbooks · Puzzle (Volume 1): mechanical restraint, wordless teaching and tiered hints — mutual references with §3.2 to §3.4 of this page.
- Level Design Handbook: teaching sequences, spatial guidance and the whitebox workflow, in full.
- Programming Handbook: state, saves and data-driven architecture, corresponding to §4 of this page.
- Indie Survival: scope control and scheduling, complementing §5 of this page.
- Homework: lay out ten rooms on grid paper — three teaching controls, two teaching concepts, three variations, two combinations — marking each room's new concept and checkpoints; have a friend solve it on paper and record which room holds them for over two minutes.

A puzzle-platformer is ultimately tested on two things: when the player figures it out, is the execution worthy of that cleverness; when the player lands the last jump, is the room worthy of that "nice".
