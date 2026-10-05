# Ludo Atlas · Genre Handbooks · FPS

> **Genre Handbooks · Volume 2**. Positioning: a shooter development handbook that makes "aim and fire" the primary skill in first-person view, with space, sightlines and pacing as the core contest; both the single-player campaign and competitive multiplayer routes are in scope.
> Companions: Game Design Handbook (core loops and numeric tables) · Programming Handbook (performance and data-driven design) · Level Design Handbook (space and encounters) · Multiplayer & Backend (sync, matchmaking and anti-cheat).
> This page carries no external links; cases name public titles only, and the figures are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: FPS (first-person shooter) is the genre **presented in first-person view, with aiming and shooting as the core action**. First person is not a camera position but an information device: what the player sees is what the character sees, threats come in from the edge of the screen and vanish behind your back, death arrives fast — and its cause must be explainable.

Family position: the archetypal member of the shooter family. Tactical, competitive, hero, extraction and looter branches all stack rules on the same core; gun feel and spatial language are the shared foundation.

The core loop, written as a verb chain:

`identify the threat → aim → fire → reposition and switch lines → clear and push forward`

This loop is measured in seconds: one firefight runs 1–5 seconds, and a match is made of dozens to hundreds of exchanges. It holds on exactly two preconditions: firing must have weight (§3.1), and death must be reviewable (§3.2, §7).

Two product routes grow from the same core: the single-player campaign sells pacing and staging, competitive multiplayer sells contest and long-term balance. They share gun feel and spatial language, while their engineering and content structures are entirely different (§4.4).

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Third-person shooter (TPS) | The camera sits outside and the character is visible; FPS compresses all information onto the screen, so the pressure comes from a different source |
| Twin-stick shooter | Aiming is decoupled from movement and assistance is heavy; in FPS, aiming is the primary skill |
| Immersive sim | Shares first person, but its weight is on multiple solutions and system interaction; shooting is only one tool |
| Run-and-gun | A branch of the same family: the mix leans toward movement over shooting, and the pacing is more forgiving |
| Extraction shooter | Stacks looting, extraction and loss rules on top of firefights — an extension of the same core |

A self-check question: break the gun feel (remove recoil, hit feedback and sound effects) — does the game still stand? If the answer is "no", what you are building is an FPS.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **The immediate pleasure of firing**: every shot has weight, sound and consequence; players keep going to "fire one more shot".
2. **Visible growth in aim**: from fumbling to snap shots on target; the mastery curve runs long, and players can feel every step themselves.
3. **Battlefield reading**: grading threats within half a second is the genre's "intelligence" component and the divide between veterans and newcomers.
4. **Pacing and breathing room**: firefight, breather, firefight again; the single-player act and the multiplayer round are both containers for this rhythm.
5. **Competitive narrative**: being pinned down, turning it around, the clutch 1v3 at the decisive moment; stories of the process are the fuel for long-term retention.

Benchmark titles (play them with your own hands before breaking them down — game feel is learned in the hands, not by watching):

| Title | What to learn from it |
| --- | --- |
| DOOM (1993 and 2016) | The rhythm of high-speed run-and-gun; 2016's glory kills returning resources turn "attacking" into a survival strategy |
| Halo: Combat Evolved | The tolerance of controller shooting; shield regeneration turns "back off when losing" into a pacing tool |
| Counter-Strike | The pure competitive structure of a short TTK: economic rounds, learnable spray patterns, map control |
| Call of Duty 4: Modern Warfare | The density of scripted encounters; how a multiplayer progression loop keeps players in the game |
| Half-Life 2 | Level design that tells a story through space and staging; the narrative use of physics interaction |
| Overwatch | Class-based division of labor and character readability; how the hero pool constrains team structure |
| Titanfall 2 | Wall-running and sliding: movement as a second weapon system |
| Battlefield (series) | Large-scale battlefields and the layered design of vehicles and classes |

What they share: the credibility of the gun is the foundation. This genre is extremely crowded; good gun feel is only the ticket in — subject matter, modes and long-term live ops decide whether players stay.

## 3. Design Essentials

### 3.1 The Four Elements of Gun Feel

Game feel is built from four channels stacked together; break any one and the other three cannot cover for it.

| Element | What it does | Reference values | Cost of getting it wrong |
| --- | --- | --- | --- |
| Weapon feedback | Recoil, spread, fire rate and reload make up the gun's "weight" | Vertical recoil 0.2–1.5 degrees per shot; the first 8–12 shots of the pattern fixed, then random (common practice) | No recoil feels like a water gun; fully random is unlearnable |
| Hit feedback | Hit markers, directional damage indicators, damage numbers, kill confirmation | The marker arrives on the same frame as the hit; kill confirmation within 100–200 ms | Shots land but do not bite, and firefights become a guessing game |
| Audio | Three layers — firing, impact, mechanical (reload, bolt) — plus a distance layer and a tail | At least 3–4 sound layers per gun | The gun sounds like a toy; if you cannot hear direction, you cannot hear threats |
| Camera shake | A short kick on firing, directional shake on taking hits, falloff shake from explosions — all adjustable and toggleable | Firing shake 50–150 ms | Too much shake causes motion sickness; none at all feels pasted on |

Recoil and spread are two different things: recoil pushes the view, and the player can pull back against it to compensate; spread is random deviation in where shots land, and the only answer is waiting for it to settle. Tell "learnable" and "random" apart: competitive titles give almost everything to a learnable pattern with minimal spread, and only the thrill-focused route scales the randomness up.

TTK (time-to-kill) is the master switch for the whole game's temperament:

| Approach | Feel | Skill focus | Reference |
| --- | --- | --- | --- |
| Short TTK | First strike decides life or death (about 0.1–0.3 seconds) | Information, position, aim speed | Counter-Strike |
| Long TTK | Trading and sustained damage (1 second or more) | Movement, tracking, teamwork | Halo |

Mixing the two ends is a common beginner death: the maps are built for dodge-based pacing while the numbers do scratch damage, and firefights turn into two sides standing around punishing each other.

Tuning discipline (same root as frame-level tuning in platformers): trust only frame-by-frame recordings, never "the feel is about right"; tune at the target frame rate and on target hardware; put sensitivity (cm/360), FOV and ADS zoom into the parameter sheet with defaults and adjustment ranges.

Acceptance criterion: with 5 people, each firing 30 shots at a static target and 30 at a moving one, record the count of "I was clearly aiming at it and missed"; 0–1 per person passes. Then chase the cause and pin the blame on sensitivity, recoil or spread.

### 3.2 Combat Space and Encounter Design

Combat space exists before decoration. Before laying out any encounter, draw three lines: sightline (who can see whom), distance (which weapon covers point-blank, mid and long range) and verticality (who can stand higher and suppress whom).

- **Vertical layering**: ground, platform and beam heights decide who suppresses whom. Any high sniper perch needs at least one counter path (stairs, a side corridor, a breakable floor), or the space becomes a one-way abattoir.
- **Distance layering**: arrange three engagement ranges along a single attack route, door by door, forcing players to rotate weapons. A space that is all long-range serves only one kind of gun.
- **Sightline management**: doors and corridors are information exchanges; entering a door means checking "the line that can threaten you" first; every long sightline needs something worth seeing or something threatening at its end — an empty long corridor is a level-design accident.

Cover comes in three tiers, each with a different job:

| Tier | Definition | Role |
| --- | --- | --- |
| Full-height cover | Blocks the whole body even standing; breaks sightlines | The safety line: reload, recover, re-decide |
| Half-height cover | Full cover crouched, upper body exposed standing | The main tool for switching between attack and defense; peeking out and pulling back make up the firefight rhythm |
| Soft cover | Penetrable (planks, sheet metal, smoke) | Compresses "absolute safety" and makes camping come at a price |

Encounter choreography runs in three beats: telegraph (sound, shadow, environmental change), engagement (fire exchanged, and the player must have at least two lines of advance) and cleanup (a breather, resupply, a hook into the next section). Size references: rifle engagement sightlines of 15–30 meters; corridors 2–3 body-widths wide; cover spacing tied to grenade throw distance — never let players clear a space by lobbing grenades from one spot.

Checklist (run through it for every encounter): which threat do you see the moment you enter? Are there two routes of advance? Where do you retreat when pinned? Is there a counter to the high ground? For the full methods of metrics and guidance see the Level Design Handbook.

### 3.3 Enemy AI and Enemy-Type Composition

Getting started needs only one concept: the behavior tree. Write enemy decisions as a priority-ordered tree; four node types are enough: selector (try from the top down, run the first viable one), sequence (a chain of steps, complete only when all are done), condition (a read of state) and leaf (the action that actually executes). A minimal FPS tree: selector → attack if the player is visible (condition plus action), investigate a noise, otherwise patrol. Draw the tree before you talk about code.

Enemy-type mixes set the "problem types" for the player; more of the same enemy is still the same problem:

| Enemy type | Forces the player to | Counter | Mixing note |
| --- | --- | --- | --- |
| Rusher | Back off, swap weapons, shoot on the turn | Shotguns, melee, holding mid range | Enters from the side of cover; pairs raise the pressure |
| Suppressor | Take cover, change routes | Flanking, wall-penetrating weapons | Stage at a different distance from rushers: one pins, one charges |
| Sniper | Check long sightlines, stop exposing themselves | Smoke, flanking, counter-sniper positions | Must give position clues (muzzle flash, sound) |
| Grenadier | Leave cover, stop camping | Movement, shooting down projectiles | Combined with a suppressor it destroys all cover — use sparingly |
| Heavy elite | Swap weapons, spend resources | Weak points, mechanic interactions | One per encounter at most, with ample telegraphing |

Start with three: a close-range rusher, a mid-range shooter and a heavy; behavioral differences are worth more than visual ones. Three rules:

- Leave reaction time and error in aiming (commonly a 0.2–0.5 second reaction delay plus a fixed angular error); perfect aim is a quit moment.
- Give attacks startup and sound before they land; players must be able to anticipate, and ambushes are reserved for scripted staging.
- Taking hits requires feedback: hit-stun, impact effects, voice lines; the enemy's feedback is where the player's output lands.

Count discipline: keep active threats in a frontal fight to 3–4 at a time (reference); extras join in from a distance, queued up. Once too many threats press the screen at once, backing away is the only move left.

## 4. Technical Essentials

The engineering difficulty concentrates in four places: the first-person view foundation, shot resolution and the weapon system, AI and performance, and the divide between single-player and multiplayer. The following is engine-agnostic; for method details see the Programming Handbook.

### 4.1 The First-Person View Foundation

- The camera is the visible world and the body is the collider, decoupled as two systems: the body is an invisible cylinder (standing, crouching and prone are all collider states) and the head does nothing but see.
- First-person weapons render in their own layer to avoid clipping into walls or being culled; weapon animation, muzzle effects and the crosshair belong to this layer.
- Provide options for FOV, sensitivity and camera sway, and record their defaults; motion sickness is this genre's most common accessibility complaint, and view narrowing, a shake toggle and hold-versus-toggle crouch are all baseline items.
- Input is tuned per platform: keyboard and mouse use raw input with an acceleration toggle (off by default in competitive); the controller's friction and slowdown curves are two separate aim-assist systems; touchscreens get a third.

### 4.2 Shot Resolution and the Weapon System

- Decide the resolution method first: hitscan suits fast pacing and competition, projectiles suit dodgeable slower firefights; mix the two and players cannot build intuition.
- Hitboxes and part multipliers: head, torso and limbs as separate zones, with the head commonly at 2–4× or outright lethal (reference); resolution must match the visual model — "I hit it and nothing registered" is ground zero for broken trust.
- Weapons are table-driven: one row of data per weapon (damage, fire rate, magazine, reload, recoil curve, spread, range falloff, part multipliers); changing numbers never touches code.
- A weapon state machine guards the line between animation and logic: animation is interruptible, logic is not; swap time and movement penalty are part of the gun's "weight".

### 4.3 AI and Performance

- Split the AI into four layers: navigation (pathfinding grid), perception (vision cone plus occlusion rays, sound events), decision (state machine or behavior tree) and execution (movement, shooting, animation).
- Simulation LOD: distant enemies run perception and decisions at lower frequency, and off-screen ones stop being simulated every frame; shell casings, hit effects and damage numbers all go through object pools.
- Audio channel limiting: play at most N firing sounds at once, prioritized as player weapon, nearby threats, environment; explosions and sustained fire are the worst offenders for clipping.
- Split the frame budget with separate caps for rendering, logic, AI and audio; do not optimize without measurement — for tools and methods see the Programming Handbook.

### 4.4 The Engineering Divide: Single-Player vs Multiplayer

Single-player FPS is a "playback": the level is a stage, pacing, staging and saves are all locally controllable, and the engineering weight sits in the content pipeline and performance. Multiplayer FPS is "coordination": there is no director, several clients each operate on the same world, and the engineering center of gravity shifts from content to state.

| Dimension | Single-player | Multiplayer |
| --- | --- | --- |
| Source of truth for state | Local and immediate | The server (or host) rules authoritatively |
| Timeline | Pausable, slow-motionable | Globally unified; latency is a constant |
| Content unit | Levels, encounters, staging | Maps, modes, seasons |
| Production weight | Staging and levels | Balance, networking, live ops |
| Typical failure | The content is not fun | Latency, cheats, broken matchmaking |

Route discipline: get single-player gun feel and the combat loop standing first, then decide whether to enter multiplayer; once networking is in, every design must re-answer "does the server know this state?", and anything the server can decide does not go to the client. Multiplayer is not "adding a mode" but a second product line: servers, anti-cheat and live-ops cadence are all inside it — for the full chain see Multiplayer & Backend.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimating scope; not a commitment. Numbers are a ruler, not a promise — calibrate them against your own team's speed.

| Content module | Minimum playable | Comfortable scope | Notes |
| --- | --- | --- | --- |
| Campaign levels | 5–8 | 10–15 | 20–40 minutes of experience each |
| Multiplayer maps | 3 | 6–10 | Each one must absorb dozens to hundreds of playtest rounds |
| Weapons | 6–8 | 10–15 | One clear role each; no number clones |
| Enemy types | 4–6 | 8–12 | Behavioral differences before visual ones |
| Modes | 1–2 | 3–4 | Every added mode means retesting every map once more |
| Campaign length | 3–5 hours | 8–12 hours | The first ruler for sizing content cost |

Asset-volume traps (this genre's most expensive line items):

- **First-person weapons are the most expensive single item**: they occupy a third of the screen and every animation is watched right against the camera; a full set — model, hand animation, sounds, effects, icon — commonly takes 1–3 weeks (reference). Ask for weapons by role, not by quantity.
- **Art density for enemies and maps**: players see the whole space up close, so a single level's art tolerance is far lower than in top-down or distant-camera genres; the ratio from whitebox to final commonly runs 1:3 to 1:5.
- **The bulk of a multiplayer map's cost is playtesting**: art is the small part; iterating on positions, spawns, economy and balance is the rest — plus long-term maintenance for balance and exploits after launch.
- **Cheap copies give themselves away**: color-swapped enemies and "+10% damage" guns are seen through at a glance; reuse must carry behavioral or role differences.
- Single-player and multiplayer maps cannot be repurposed for each other: the former is designed for pacing, the latter for control points and spawn logic — different spatial objectives.

Workload references (reference values): gun-feel prototype 2–4 weeks; single-player vertical slice (one level at shipping quality) 2–4 months; a small single-player title 1–2 years; a small title with competitive multiplayer is also on the 1–2 year scale, with the bulk in balance, networking and live ops. For scope getting out of control and the content-cutting order, see the Production Handbook.

## 6. How to Start the First Prototype

Goal: a greybox room in 2–4 weeks, validating "firing once makes you want to fire a second shot". No multiplayer, no reload animations, no story.

1. (Two days) A 10×20-meter whitebox room plus one gun, hitscan resolution; complete the full hit-feedback set first: white flash on hit, audio, damage numbers, kill confirmation.
2. (Two days) Movement and camera: walk, run, crouch, jump, with sensitivity and FOV in a settings menu; no head bob yet.
3. (Three days) Put every weapon parameter into tables with hot-reload: damage, fire rate, magazine, reload, recoil, spread; three days of frame-by-frame tuning in a shooting range, and nobody is allowed to texture anything yet.
4. (Two days) Add one enemy type (pathfinds, has attack startup, often misses you) and two sets of cover, and build a 30-second encounter.
5. (Three days) Assemble a small level of three encounters: one beat each of telegraph, engagement and cleanup, with one intensity peak in the middle; have someone who has never seen the project play it blind.
6. (The remainder) Retrospective: check the frame-by-frame recordings against the problem checklist (§3.1 and §3.2); change only parameters and layout, add no new systems.

Success criteria (all observable):

- With all art and audio removed, testers still willingly shoot targets and take fights, usually for 15 minutes or more at a stretch.
- At least 4 of 5 testers complete the 30-second encounter with no verbal guidance.
- Change any game-feel parameter and within 5 minutes you can quantify its effect on firefight outcomes.
- Every tester death comes with a stated cause (it fits one of four categories: sightline, distance, reaction, position).
- Testers start another round on their own, rather than being asked to try again.

## 7. Common Pitfalls

1. **Laying out content before gun feel is settled**: recoil and TTK will overturn every assumption in levels and animation; do not mass-produce before the gun is tuned.
2. **Hit feedback on only one channel**: audio only or visuals only makes players doubt "did I hit that", and firefights become guessing games.
3. **Unlearnable recoil**: fully random patterns make practice meaningless; a learnable pattern plus a little randomness is the common answer.
4. **Invisible deaths**: snipers with no telegraph, spawns behind your back, instant kills; every death must have a reviewable cause.
5. **Encounters with only one route**: corridor target practice has no decisions, and one suppression is enough to make players want out.
6. **AI that aims perfectly or stands there at point-blank**: both ends ruin the experience; reaction delay, error and startup are the readability trio.
7. **TTK fighting the map's temperament**: one-shot numbers with run-and-hide pacing, or scratch-damage numbers with trench warfare.
8. **Going multiplayer before single-player is proven**: networking magnifies every design problem; make single-player stand first.
9. **Estimating content by count**: the real cost of weapons, maps and enemy types lives in animation and playtesting; subtract before you add.
10. **Accessibility missing**: FOV, sensitivity, acceleration and shake all fixed, and motion sickness arrives together with the bad reviews.
11. **Audio missing**: gunshots with no distance layer or tail, and hit sounds indistinguishable from firing sounds; audio is half of game feel (see the Art & Audio Handbook).
12. **Copying layout from videos but not feel**: feel comes from playing with your own hands and frame-by-frame recordings; a video gives you composition, not the weight of the gun.

## Further Reading

- Game Design Handbook: core loops, numeric tables and game-feel checklists; the tuning methods in this page's §3.1 pair with its numbers sections.
- Level Design Handbook: metrics, guidance, pacing and the whitebox workflow — the full expansion of this page's §3.2.
- Programming Handbook: performance budgets, data-driven design and multiplatform engineering details.
- Multiplayer & Backend: the full path from "it connects" to "it holds up and keeps cheats out" — required reading for multiplayer FPS.
- Art & Audio Handbook: gun animation, layered sound design and mixing practice.
- Case Studies: shooter and competitive breakdowns to compare against real scope-control and live-ops numbers.
- Exercise: rebuild half of a map you know in greybox and log the cause category of every death; then play a stretch of a short-TTK and a long-TTK title and write down the difference in feel between them.

FPS looks like it sells guns, but what it actually sells is the credibility of the instant of firing — and a reason, ten minutes later, to want another round.
