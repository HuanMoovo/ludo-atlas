# Ludo Atlas · Genre Handbooks · Stealth

> **Genre Handbooks · Volume 3**. Positioning: the genre that makes "information and route planning" its first driver. Players observe first, plan next and execute last, trading information advantage for an edge over the enemy; head-on conflict exists, but is usually not the optimal solution.
> Companions: Game Design Handbook (core loops and number tables) · Programming Handbook (AI perception and performance budgets) · Level Design Handbook (patrol routes and spatial language) · Case Studies (breakdown methods).
> This page carries no external links; benchmark titles are widely known works only, and the figures are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: stealth is **the genre that makes "the information gap" its first driver**. Know more than the enemy and you have half the win already; let the enemy know more than you and the pressure arrives at once. Stealth's opponent is not the enemy's damage but the enemy's perception.

The core loop, written as a verb chain:

`observe (sightlines, patrols, sound) → plan the route and timing → infiltrate and execute → handle surprises (hide, misdirect, disengage) → reach the objective or replan`

This loop adds a whole stretch of "not acting" that an action game doesn't have: observation and planning take the bulk of the time, and action happens within seconds. It holds on two preconditions: perception rules must be readable to players (§3.1, §3.2), and failure must be cheap enough to bear (§3.5). Lose either one and the game slides toward rote-memorized set pieces or a reload simulator.

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Immersive sim | Immersive sims use unified systems to permit any solution; stealth keeps two guaranteed main paths — "bypass" and "handle" — with one notch less freedom in the systems |
| Action shooter | In shooters the default solution is to open fire; in stealth the default solution is not being seen — firing is the fallback, and a cost |
| Survival horror | Horror manufactures fear from powerlessness; stealth manufactures satisfaction from a sense of control — the two cross where resource pressure lives |
| Puzzle | A puzzle's answer is made unique by the designer; stealth's answers are improvised on the spot by the player inside dynamic systems |

A self-check question: replace all the enemies with decorations that can neither see nor hear — does the game still stand? If it does, what you are making is an exploration game; if it doesn't, it's stealth.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **A sense of control**: the situation is decided by your own observation and judgment; being spotted is information, not a verdict.
2. **Heartbeat moments**: slipping past at the edge of a vision cone, ducking back into cover by a hair — tension and release trading places.
3. **A smart self**: every route can be retold as "why I went this way", and the credit belongs to the player, not to luck.
4. **Low-noise retries**: back on the scene within seconds of failing, with the cost of repeated observation and probing pressed to a minimum.
5. **Stories worth telling**: the improvisation that follows a broken plan is the material players want to tell others about.

Negative experiences (any one of them is a red flag): tightrope walking (a single invisible safe path the whole way, one wrong step and everything resets); a reload simulator (being spotted leaves nothing but reloading); memorization fatigue (routes are completely fixed and it plays like a rhythm game); bullying the AI (holes everywhere in its rules, and the tension drops to zero).

Benchmark titles (play them yourself before breaking them down; video misses a great deal of perception feedback):

| Title | What to learn from it |
| --- | --- |
| Metal Gear Solid series | The baseline for vision cones and auditory perception, readable feedback for alert tiers, and information sharing through radio calls |
| Hitman series | Social stealth (disguises and crowds), many solutions to one map, and contract-style replay as a level's second life |
| Assassin's Creed series | Crowds and vertical routes, social rules (who belongs where), and pursuit and escape once wanted |
| Dishonored | The dual route of stealth and assault, ability combinations that reshape route planning, consequences written into world state rather than a results screen |
| Batman: Arkham series | Predator rooms: one-against-many stealth hunting, fear rhythm and taking enemies down one by one |
| Ghost of Tsushima | Reconnaissance and assassination chains when infiltrating camps, a seamless switch to assault once spotted, and the damage-control design of "being spotted is not failure" |

## 3. Design Essentials

### 3.1 Perception: Sight, Hearing and the Alert State Machine

The world in the enemy's eyes is built from three channels: sight, hearing and information sharing. Each channel has its own parameters and its own readable feedback (§3.2), and all three feed into the same alert state machine.

Sight's deciding factors (from cheap to expensive): distance, angle, lighting, posture and motion, occlusion. The common approach is a "detection progress" meter: those factors jointly set how fast the bar fills, rather than a binary judgment.

| Sight parameter | Typical range | Notes |
| --- | --- | --- |
| Vision cone angle | 90° to 120° horizontal | Top-down 2D can go narrower for readability; wider than 140° reads as radar and players can never slip behind |
| Sight distance | Commonly 15 to 30 meters indoors in 3D; convert per tile in 2D | Calibrating in "seconds walked at the player's normal speed" is more stable |
| Full detection time | 0.5 to 3 seconds | Distance and angle spread the tiers apart, leaving a reaction window |
| Posture effect | Crouch-walking slowest, running fastest | Running sharply shortens detection time; it is the price on "fast but loud" |
| Lighting effect | Fast in light, slow in dark | Align with art and lighting; darkness must be consistently readable |

Hearing is managed by events, each noise event carrying a radius and an intensity:

| Noise event | Reference magnitude (rescale to your project's scale) | Design role |
| --- | --- | --- |
| Crouch-walking, slow walking | Nearly silent | Rewards patient routes |
| Normal walking | A few meters | Dangerous only up close; corridors and corners are the thresholds |
| Running | Ten-odd meters | The bill for "fast" |
| Opening doors, climbing through windows, glass | Around ten meters | Part of route choice; the quiet route must have a cost |
| Gunshots, explosions | Tens of meters, or the whole level | The invoice for going loud (§3.4) |

Alert tiers use an explicit state machine, commonly four levels:

| State | Entry condition | Typical behavior | Exit condition |
| --- | --- | --- | --- |
| Relaxed | Default | Patrol, watch, chat | Detection progress starts building |
| Suspicious | Partial perception (a silhouette, a sound) | Stop, turn, walk over to check | Threat confirmed, escalate; nothing there, fall back |
| Search | Target lost or detection interrupted | Search around the sighting position, typically 10 to 30 seconds | Target found, enter combat; timed out, fall back |
| Combat | Threat confirmed | Pursue, call for backup, use weapons | After the target has been lost for a while, step back down tier by tier |

Three disciplines: de-escalation is slow and escalation is tiered, giving players a wrap-up window; the sighting position (last known position — where the enemy most recently saw or heard you) is the foundation of search behavior and also information players can actively exploit — misdirection is built on it; information sharing must be designed explicitly, since who can notify whom, over what range, directly decides whether "picking them off one by one" holds.

Acceptance criterion: find 5 people and have each play 10 minutes, recording the number of "I have no idea how he spotted me" incidents — 0 to 1 per person passes.

### 3.2 Information Visualization: Making Perception Readable

Stealth's fairness floor: every perception that leads to a consequence must give feedback ahead of that consequence; players must know they are being exposed before they take the hit. Feedback splits into four beats, stronger the later they come:

| Beat | Content | Common practice |
| --- | --- | --- |
| About to happen | The enemy notices something off | Overhead symbols (question-mark family), a subtle sound cue, a turn-and-pause animation |
| Happening | Detection progress is building | A progress indicator, swelling audio, escalating color |
| Has happened | Discovery confirmed | Alarm sound, exclamation mark, the enemy calling out and giving chase |
| Aftermath | Global state | Alert level permanently on screen, red dots on the minimap, radio dialogue |

Player-side information tools are design objects too: x-ray and tag-style recon modes, sound-event visualization, vision cones on the minimap. They turn "reading the system" into a core skill, but they need cooldowns or costs, or stealth degenerates into map reveal. Three principles: the feedback layer and the AI share one set of perception data — two separate sets will inevitably disagree; numbers may be hidden, trends must be visible; color conventions stay restrained and accessibility-aware (color-blind modes), with rules like "yellow means noticed, red means exposed" fixed from the first build.

Checklist: can players state the current alert tier within 0.5 seconds? When spotted from the side or rear, can they point to the source? With all UI off, is the perception story still readable from animation and audio alone?

### 3.3 Level Space: Patrols, Cover, Multiple Entrances and Vertical Layers

Stealth level space revolves around four words: vantage points, routes, windows and escape routes.

- **Patrol routes**: waypoint loops with a readable rhythm (pause, turn, leave), allowing one or two small variations while the whole must be observable and memorable; routes are edited visually in the editor and maintained as first-class assets. Leave high ground and dark corners at the objective area's edge — "watch for a while before acting" is stealth's main mode of play.
- **Cover**: distinguish "blocks sight" from "blocks the body", and place half-height cover along main paths so wall-to-wall movement holds; cover height links to posture (standing, crouching).
- **Multiple entrances**: every objective area gets at least 2 to 3 entrances with distinct cost profiles (the front gate is heavy with guards, the side door needs a key, the roof needs climbing, the sewer is filthy but safe). The number of entrances is the number of solutions.
- **Vertical layers**: roofs, mezzanines, ventilation ducts and balconies are a second route system for the same space; height changes both sight (looking down you see far, looking up you have many blind spots) and movement (falls make noise, local drops are one-way). This is the cheapest source of variety.
- **Light, dark and sound terrain**: bright and dark zones are gameplay resources, not art filters; the noise differences of gravel, glass and metal stairways form a route dimension. Hiding areas must be stable and learnable, so players can learn "where is safe".

Checklist: from the main vantage points, can you see the objective area's full patrol cycle? Can you retell each entrance route's rough duration and risk? With all the lights on, does the ghost route still exist (guarding against gameplay propped up by one fixed blind spot)? Has the retreat route been designed?

### 3.4 Dual Path: Both Stealth and Assault Must Hold

Dual path is not the slogan "stealth primary, combat as the fallback" but two complete routes that both get serious verification, plus a smooth middle band.

| Path | What the player gets | Cost | Design duty |
| --- | --- | --- | --- |
| Ghost (zero detection, zero kills) | A sense of control, score and narrative rewards | The time spent observing and waiting | Every level must have a viable ghost route, verified stretch by stretch |
| Stealth clear (non-lethal takedowns) | Safer passage, fewer variables | The time and risk of handling and hiding bodies | Knockouts, dragging and hiding need complete systems and feedback |
| Assault | Instant resolution, rhythmic release | Noise, reinforcements, alert escalation, a lower score | The combat system cannot be half-finished, or the audience halves |

The middle band is the key: once spotted, "fight then hide again" and "fight while falling back" are allowed; combat and stealth share one perception and noise system, and the switch never needs a reload; consequences are expressed softly — alert escalation, a discovered body triggering a search, witnesses reporting, score penalties — mild punishment beats hard failure. Scoring and replay (no kills, zero alarms, timed challenges) are why stealth levels get reused so heavily, but they must exist as an optional layer, not a gate on completion; combat's rewards sit one notch below stealth's, so that "not fighting" becomes the sensible choice.

### 3.5 Failure Tolerance: Being Spotted Is Just a Transition

Stealth's failure rhythm is choppier than an action game's: one sightline slipping, one body hidden badly, and the situation changes. The system must guarantee these changes are handleable, not capital sentences.

- **Correction window**: detection is not instantaneous (§3.1); when the player is a hair away from being seen, give them a chance to duck back into cover. This is the most common source of "dramatic escapes".
- **Disengage routes and soft failure**: give at least two of smoke, a change of clothes, crowds and dark corners for slipping away; define disengagement explicitly (distance, time, all sightlines broken) so players believe they can get away. Being caught, disarmed or locked up needs a jailbreak or a ransom as its landing point; if death is the only outcome, the level's tolerance must be raised across the board.
- **Fast retry**: manually restarting the encounter or level completes within seconds; from failure to playing again stays within 10 to 30 seconds. Checkpoint density is divided by "one complete plan", not by scene changes; unskippable cinematics are public enemy number one in the retry loop.
- **Save policy**: quicksave and quickload buy players extreme probing (the reload playstyle), checkpoints buy heavier individual decisions — both are legitimate, but they test differently; whichever you choose, loading must stay in the seconds.

Acceptance criteria: after being spotted, more testers choose to keep responding (hide, flee, fight) than restart immediately — that passes; after a failure, the complaint is aimed at themselves, not the system — that passes.

## 4. Technical Essentials

The engineering difficulty concentrates in three places: the perception system, the state machine and AI, and testability. Everything below is engine-agnostic; navigation and behavior trees have off-the-shelf solutions in mainstream engines — what you must build yourself is the perception parameter framework and the visualization tools.

**Perception system**

- Three-stage filtering plus reduced update frequency: distance, then angle and facing, then occluder rays — cheap checks first, rays last; occlusion samples the head, torso and feet so half-height cover works naturally. Perception updates at 5 to 10 Hz globally, spread across frames per enemy, with distant enemies thinned further; never run a full per-frame sweep over every enemy — it is this genre's most common performance sink.
- All sight parameters are data-driven: cone angle, distance, the detection-fill speed curve, lighting and posture coefficients go into number tables with runtime hot-reload. Balance comes from iteration — don't hard-code the numbers.
- Hearing runs on an event bus: noise events (type, position, radius, intensity) are broadcast, and enemies subscribe with distance and occlusion filters. Propagating as "radius plus wall attenuation" is close enough — consistent rules matter more than physical correctness.
- Information sharing is implemented separately: calls, radio and per-region propagation all work, but "who can notify whom, with what delay" must be an independent knob, never hard-coded in passing.

**State machine and AI**

- Alerts use an explicit state machine (relaxed, suspicious, search, combat), each tier with entry and exit conditions and timers, all data-driven; don't assemble an implicit state out of a pile of booleans.
- Search behavior needs "sighting position plus search-point generation", the link most easily botched: written shallow, it looks like perfunctory circling; written heavy, it looks omniscient. Place search points around the directions the player could have fled.
- Patrols and navigation are data assets: waypoints sit on the navigation data, edited visually in the editor (pause, facing, branches, small randomness); 3D uses a NavMesh, 2D uses grid pathfinding, with cover points and vantage points marked separately so the AI, the map and the hint systems reuse the same data.

**Testability**

- Debug visualization is the first-priority tool: vision cones, detection progress, current state, sighting position, noise radii and pathfinding routes all toggleable, with single enemies slowable; add an AI decision timeline (recording who perceived what, and when, in one encounter) for investigating every scene where "the player felt this was unfair".
- 2D versus 3D: top-down 2D computes sight and occlusion precisely with grid or geometric algorithms — cheap and intuitive, with vision cones drawn straight onto the map; 3D uses rays plus occluders — remember that "it simulates off-camera too", and LOD is the floor. Side-view 2D needs extra treatment of depth (front and back layers), or players cannot tell whether they are in the enemy's line of sight.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimating scope; not a commitment.

| Project shape | Content scale | Time reference | Notes |
| --- | --- | --- | --- |
| Perception prototype | 1 room, 2 to 3 enemies | 2 to 4 weeks | Whitebox; validates perception and readability only |
| Small complete title | 6 to 10 short levels | 3 to 9 months | Single theme, few enemy types |
| Typical indie title | 10 to 15 levels | 1 to 3 years | Multi-route verification and polish dominate |
| Open sandbox levels | 4 to 8 large maps | 2 to 4 years | Hitman-style; a single map is often polished in months |

- Enemies are perception devices, not health bars: 3 to 6 enemies with clearly distinct "perception profiles" (sight-focused, hearing-focused, heavy, canine and scout) are usually enough, each with learnable parameters and visual feedback. Fewer than an action game, but each one costs more.
- The verification matrix decides the cost: each level's main routes (ghost, non-lethal, assault) each get verified once, so testing volume is roughly "level count times route count"; the time ratio of level iteration to testing commonly sits at 1:4 to 1:6, higher than a platformer.
- Reuse and scheduling: scoring challenges, restrictions, higher difficulties and contract-style custom missions let a single level be digested over and over, so unit reuse is very high — provided the perception system is stable enough to take new rules. Scheduling anchors: 2 to 4 weeks for the perception prototype, 2 to 4 months to a vertical slice (one stretch of content at shippable quality), then extrapolate by content volume times a polish coefficient; scope drift is risk number one — build narrow and deep first, then wide.

## 6. How to Start the First Prototype

The first prototype builds only one room or one corridor: 2 to 3 enemies, one objective (take an item or reach a point) and two entry routes. Finished in 2 to 4 weeks, without touching story, saves or menus.

**Week 1: the perception backbone.** One enemy: vision cone, hearing, four alert tiers, sighting position; the player: crouch, walk and run movement tiers plus one hiding spot. All parameters hot-reloadable. Ugly is expected.

**Week 2: readability.** Indicators, sound cues, alarm feedback and debug views all in place; find 3 to 5 playtesters and ask one question only: do you know why you were seen?

**Weeks 3–4: micro-sandbox.** Add a second entrance, a second enemy and one assault route; run the same room through teach, test, variation: a safe zone teaches observation and stealth, a low-pressure route examines it, and a tightening window supplies the variation. Validate the dual path, transitions and retry speed.

Success criteria (all observable):

- At least 4 of 5 testers can state at least one patrol regularity and one safe vantage point.
- "I have no idea why he spotted me" complaints at or under 1 per person.
- After being spotted, most testers choose to keep responding (hide, flee, fight) rather than restart immediately.
- With all UI and art off, working from blocks and sound alone, the perception story is still broadly readable; change any one perception parameter and you can quantify its effect on "average detections per room crossing" within 5 minutes (precondition: debug visualization is in place).

If the perception backbone does not pass acceptance, do not start laying out levels. Stealth's foundation is the perception system, and rework on this block is the most expensive bill.

## 7. Common Pitfalls

1. **Perception rules that can't be read**: the player lost to information they never saw. Every consequence-bearing perception needs a warning ahead of time (§3.2); invisible detection is a review-bomb machine.
2. **Writing being spotted as failure, or an alert system that is only on and off**: no correction window, no middle states, no disengage routes, and players are forced to reload; being spotted should be a transition, not a verdict (§3.5).
3. **Only one real route**: multiple entrances never built, assault left half-finished — which amounts to ordering players to play one kind of game. Both paths must be verified (§3.4).
4. **Patrols mechanical or random**: fully fixed plays as memorization, fully random cannot be learned; a readable pattern plus a few variations is the soil that plan-driven play grows in.
5. **Information sharing out of control**: the two extremes are instant map-wide propagation (stealth stops working) and total deafness (the AI looks like furniture); propagation range is a gameplay knob and must be tuned explicitly.
6. **Retry costs out of control**: slow loads, long walks back, unskippable cinematics. Repeated observation is expensive enough already; the retry loop must not fine the player a second time.
7. **Perception tooling absent**: parameters scattered in code, not hot-reloadable and not in number tables, or no debug visualization at all — balance becomes guesswork and AI debugging becomes mysticism.
8. **Light, dark and sound detached from gameplay**: the spots that should be dark get lifted in post, noise terrain buried under textures; gameplay and art must be calibrated against the same table.
9. **Demo-grade AI**: performs on one scripted route and falls apart the moment the player wanders. AI is a system; test it for "triggered anywhere, in any order".
10. **Testing only yourself**: the author always knows every route and every window, which cannot substitute for a new player's observation costs and misjudgments.

## Further Reading

- Level Design Handbook: the spatial design of patrol routes, vision cones and alert tiers — the full expansion of §3.3; its classic breakdown methods apply equally to dissecting stealth levels.
- Game Design Handbook: the base document for core loops, number tables and feedback checklists, corresponding to §3.
- Programming Handbook: the engineering detail of AI, navigation and performance budgets, corresponding to §4.
- Case Studies: breakdown methods for success and failure cases; consult them when calibrating §5's scope and §7's pitfalls.
- Pitfalls & Anti-patterns: a quick reference to scope-control and project-management pitfalls, for comparison at kickoff and retrospective.

Stealth ultimately tests only two things: whether the player's "cleverness" is honored by the system, and whether the player's "mistakes" are caught by the system.
