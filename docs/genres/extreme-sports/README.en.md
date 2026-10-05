# Ludo Atlas · Genre Handbooks · Extreme Sports

> **Genre Handbooks · Volume 4**. Positioning: making "doing tricks in three-dimensional courses" the first pleasure of the genre. The player's core verbs are run-up, launch, trick and land; the score is adjudicated by a system that can be memorized and refined, and the course is written into a score sheet by ramps, rails, snow bumps and cliff faces. This page covers sports game feel and trick scoring, course structure (the trade-off between handcrafted courses and procedurally generated mountains), failure tolerance and retry cadence, cultural packaging, and scope accounting for small teams.
> Companions: Game Design Handbook (game feel and number tables) · Level Design Handbook (course and line structure) · Programming Handbook (state machines, terrain collision and replay) · Art & Audio Handbook (music, camera and cultural packaging).
> This page carries no external links; benchmark titles are widely known works only, and the figures here are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: extreme sports is the genre that **makes "doing the trick" itself the first pleasure**. On skateboards, skis, BMX bikes and climbing walls, players convert speed and terrain into a chain of scorable tricks; the trick is not a by-product of getting around — the trick is the content, and the score is the destination.

The core loop, written as a verb chain:

`run up and load → launch → pick and correct the trick in the air → landing judged → combo confirmed or wiped → go for a higher score and run it again`

This loop is measured in "one line" and "one run"; a run usually takes one to three minutes. It holds on two preconditions only: tricks must be controllable (§3.1) and falls must be cheap (§3.4). Two main branches: park-style score farming (grinding a single course over and over in timed rounds) and line-style scoring (a one-shot run from start to finish, with checkpoints and themed lines); their skeletons share an origin, and this page covers the trunk the two share.

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Racing | Racing is about who reaches the line first, with victory written in times and placings; extreme sports is about who scores higher, riskier and more stylishly on that line — the scoring system is the backbone |
| Platformer | Jumping there is a means of clearing levels; here, time in the air is the content itself, with its own move list and scoring |
| Sports games (ball games) | Ball games settle victory through rules and opponents; extreme sports is mostly individual performance, and the judge is the scoreboard and the community |

A self-check question: remove the scoring system and keep only "reach the finish line" — does the game still stand? If the answer is "no", what you are making is extreme sports.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Command of flight**: launch, hang time and landing are carried by one body system; in the air the player has time to read, choose and correct, and the moment of landing explains success or failure.
2. **Style expression**: the same terrain accommodates different tricks and lines, and scoring rewards variety and risk; players will re-run for "a beautiful ride", not just for "the most score ground out".
3. **Self-priced risk**: harder tricks, hugging rails, hugging cliff walls — all the player's own choice; the riskier, the higher the score, and the player signs for the cost of the fall themselves; the system prices risk, it does not give the player orders.
4. **Low-pressure retry**: falling is the normal beat, and fall-to-retry is counted in seconds; after a fall, what the player thinks is "I'll complete it this time", not "I'll shut the game off".
5. **Cultural belonging**: music, clothing, graffiti and camera language make people believe this is that board, that mountain, those people; cultural packaging is half the content of this genre (§3.5).

Benchmark titles (play them yourself before breaking them down; hang-time game feel cannot be learned from video alone):

| Title | What to learn from it |
| --- | --- |
| Tony Hawk's Pro Skater series | The trick scoring system (base score, combo multiplier, variety), timed-round structure and course density |
| Riders Republic | Multiple sports sharing one map, organizing line-based content, and mainstream party packaging |
| Steep | Route design at mountain scale, sense of exploration and replay challenges |
| Trials series | Physics-driven balance and crash feedback, instant-retry level pacing |

## 3. Design Essentials

### 3.1 Sports Game Feel: Making Riding, Hang Time and Landing a Four-Stage Controller

In this genre the "character" is a combination of person and vehicle: a board, skis, wheels or a climbing body. Game feel is not one jump parameter pack but a four-stage construct; hang time is this genre's currency, decided jointly by launch speed, slope angle and gravity, and course scale is back-derived from "one maximum jump" (§3.3); all four stages' knobs go into number tables and support hot-reloading.

| Stage | Core knobs | Common practice | Cost of getting it wrong |
| --- | --- | --- | --- |
| Ride | Forward drag, steering response, angle payoff of edge or board pressure | Speed decays naturally with slope and friction; steering gives precise micro-adjustment early and large angles late | Riding feels floaty or lifeless, and players stop trusting even a straight line |
| Takeoff | Charge window, takeoff input buffer, launch-surface detection | A buffer of 100–200 ms, same as a platformer; keep a small window after leaving the launch surface | Zero it and three in ten takeoffs are wasted; too much and it feels like cheating in the air |
| Hang time | Rotation speed, attitude fine-tuning, grab hold | Adjustable rotation speed (tap for slow spin, hold for fast); add a correction key to "flatten out" your posture | Nothing to do in the air, and the player turns from player into spectator |
| Landing | Landing detection angle, balance gauge, save window | Attitude angle error within the tolerance threshold counts as a clean landing; imbalance first gives a warning and one save | Detection disagrees with the visuals, and players pin the blame on the game |

Acceptance criteria: have 5 people each attempt the same trick 20 times and record the number of "I input it right but still fell" cases — 0 to 1 per person passes; after a fall, testers can say whether they got the attitude, the timing or the line wrong.

### 3.2 The Trick System: Move List, Combos and Scoring

A trick is not a canned animation; it is a look-up-able move list plus an explainable scorer. The move list lays the skeleton first: each trick is one row of data, with fields for input sequence, difficulty score, linkable segments and animation; aim for expression before quantity (the same flip with a different grab, foot or direction is a new row). For resolution, take one of two structures: **combo resolution** (the score is wiped only when the combo breaks — a high scoring ceiling and good to watch) or **segment confirmation** (every landing banks the score immediately, more forgiving, suited to a casual route); pick one as the main mode and never maintain a separate balance pass for both.

The minimal structure of a scoring system is a three-piece set:

| Component | Role | Common practice | Cost of getting it wrong |
| --- | --- | --- | --- |
| Base score | Price each trick | Tiered by rotation count, number of flips, grab difficulty | Pricing is a mess and players do not know what to practice |
| Combo multiplier | Reward "not stopping" | Each linked trick raises the multiplier; banked on landing confirmation, wiped on a fall | A multiplier explosion or frequent wipes both strip the mid-run of choices |
| Style coefficient | Reward variety and danger | Repeat tricks decay; bonuses for proximity to obstacles and for height | One single routine farms every course and the space for expression disappears |

Three rules for scoring: the score must be budgetable by the player — within ten hours of play they can predict "roughly what this jump is worth"; caps and inflation control come first, to prevent "one trick farming its way to the top of the leaderboard" — the score-farming pipeline and stylistic freedom can only keep one major direction; the special-move meter's charge and multiplier go into their own table entry and are never tuned in the same formula as the combo multiplier.

### 3.3 Courses and Levels: Handcrafted Courses Are the Main Content, Procedural Mountains a Supplement

The course is this genre's "level", and the unit of authorship is the line: one main line passes through a number of playable objects (ramps, quarter pipes, rails, stairs, snow bumps, tree runs, cliff faces). The process shares an origin with racing tracks: start with a vehicle metrics sheet (launch speed, maximum jump, hang time, turning radius), derive every distance and height from those numbers, then go from whitebox to art.

Three rules for authoring a course:

- One main line plus equivalent side lines: the main line reads clearly and can be farmed repeatedly; side lines hide close by, giving skilled players room for expression; never hard-code a single correct route.
- The course must speak for itself: rideable surfaces are guided by color, lighting, graffiti and wear marks; where the entry is, where to launch, where the landing is — all written in visual language.
- Teach, test, vary: a new object appears first in a safe spot, second under low pressure, third combined with old objects (for the three-pass detail, see the Level Design Handbook).

Procedural generation holds in exactly one scenario: long-line roles, such as a ski run from summit to base. Its discipline shares an origin with endless-runner segment stitching: handcrafted segments (playable groupings), rule-based stitching, difficulty budgeting, reproducible seeds — and the acceptance line is unsolvability and unreadability. Generated mountains serve daily challenges, long runs and volume supplements, not the main content; what players will grind over and over is still the handcrafted course.

| Dimension | Handcrafted course | Procedurally generated mountain |
| --- | --- | --- |
| Role | Main content, repeatedly farmed | Long descents and event supplements |
| Cost | High per-item investment, can be finely polished | One-time investment in the generator |
| Risk | Not enough courses | Repetitive, unreadable, unsolvable |
| Fits | Parks, streets, indoor arenas | Downhill runs, daily challenges |

### 3.4 Failure Tolerance and Retry Cadence

In extreme sports, falling is not a fail state — it is the beat itself: fall, get up, go again. Stretch this cycle out and the fun starts leaking; tolerance design answers one question: when the player falls once, how many seconds, how many points and how much progress do they lose.

| Loss | Numbers to control | Common practice |
| --- | --- | --- |
| Time | From fall to riding again | Put the reset point near the fall; park-style gets a one-button restart of the current segment |
| Score | Whether the combo is wiped | Freestyle score farming wipes the score on a broken combo; long lines resolve per segment, or keep part of the segment's score |
| Progress | Checkpoint density on long lines | Space checkpoints at "a few tens of seconds per segment" so the cost of re-riding stays controlled |
| Emotion | Whether the cause is clear | Give a slow-motion or replay freeze on the fall: edge angle, launch timing or landing spot |

Three general practices: leave a save window for "almost" — when the landing goes off balance, first show a visible wobble warning, then offer one recovery input (righting yourself, shifting your weight, and the like); take the fall only when it cannot be saved. The restart button is always easier to find than the quit button: one-button restart of the current run or segment on a fixed key, and the results screen puts retry first. Tolerance is layered: the hardcore tier (strict detection, no saves, fall means restart) is made a standalone option, so both crowds share one set of content.

Acceptance criteria: watch whether a tester's first reaction after a fall is a button press or a sigh; after three falls in a row, do they still want to ride again. If yes, the tolerance is enough.

### 3.5 Cultural Packaging: Music, Clothing and Camera Language

Extreme sports sells not only gameplay but a whole lifestyle: music, clothing, graffiti, events, camera language and community vocabulary — miss one piece and the "the crew never went to the scene" tell shows through. Cultural packaging is not skin-deep stickers but consistency of behavior and vocabulary; music and camera must be scheduled as part of the gameplay, and edits and slow-motion cut to the beat are themselves half of the spectacle.

| Vehicle | Practice | Discipline |
| --- | --- | --- |
| Music | Licensed or original tracks must fit the sport's temperament; entrances, edit beats and slow-motion clips stay in sync | Cost out real-band licensing fees and lead times early; run the pipeline first on license-safe assets |
| Clothing and skins | A reuse pipeline of one skeleton with swapped parts; the character is on screen constantly, so skins are the highest-value display space | Recognizability first — at distance and in low light you must still tell who is who |
| Scenes and camera | Graffiti, posters, spectators, event banners; wide-angle follow cams, low angles, slow-motion on key tricks | Do not pile up symbols; fix the community viewpoint first (whose contest, who is watching, where the camera sits) |
| Vocabulary and feedback | Trick names, shouts, celebrations and fall reactions match in-scene habits | Research any vocabulary you are unsure of before it goes into the game; invented slang reads as fake at a glance |

## 4. Technical Essentials

The engineering difficulty concentrates in four places: vehicle control, data-driven tricks and scoring, terrain interaction, and replay and reproducibility; everything below is engine-agnostic, with method detail in the Programming Handbook.

**Vehicle control**

- The kinematic approach is the default starting point: compute speed yourself, slide along terrain normals, accelerate on slopes and decelerate with friction — do not hand the person and board to full rigid-body physics; riding, hang time and landing share one attitude state, with the transition conditions written explicitly.
- Landing detection is more forgiving than the visuals: normal-vector angle, speed threshold and balance gauge combined in three layers; detect generously, with the error direction uniformly biased toward the player.

**Data-driven tricks and scoring**

- The move list is data-driven: input sequence, difficulty score, preconditions, animation and sound effects all become fields; write the scoring engine as a pure function (state sequence in, score out) and manage the combo multiplier and style coefficient in separate tables with hot-reload, so both splitting scores and tuning balance never touch code — prioritize the tuning speed of "what is this trick worth" over animation precision.

**Terrain interaction**

- Build terrain from heightmaps or splines plus block-face collision, and give playable objects one unified friction and bounce parameter table; at high descent speeds use substepping or continuous detection, test rails and edges segment by segment — no sticking, no flinging, no clipping through.

**Replay, records and performance**

- If you build leaderboards, both physics and scoring must be reproducible: fixed timestep, reproducible random numbers, frame-rate independence; land sampled replay first and treat input replay as the advanced step, and any change to game feel means re-evaluating the comparability of existing records.
- Plan the performance budget around the longest line and the biggest scene: streaming loading, graded vegetation density, graded snowflakes and speed lines; the generator needs step-by-step visualization that draws its stitching results on screen.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimating scope; not a commitment.

| Project shape | Content scale | Time reference | Notes |
| --- | --- | --- | --- |
| Game-feel prototype | 1 greybox course, 10 tricks | 2–4 weeks | Validates only controls, hang time and landing |
| Small title | 2–4 courses, one scoring system | 3–9 months | Course and game-feel polish take the bulk |
| Typical indie title | 6–10 courses, move list and line modes | 1–2 years | Music and course iteration are ongoing costs |
| Open-world multi-sport | One shared map, switchable between sports | 3+ years | Team and budget are a different order of magnitude |

- The course is the most expensive content unit: one park equals modular pieces, props, lighting, playable lines and playtesting each one; size courses against the vehicle metrics sheet, and never draw comparisons like "bigger than a real park" that have no acceptance criteria.
- The move list is the second cost item: each trick equals animation, input, scoring and sound; 30 handcrafted tricks are worth less than 12 tricks with rich room for expression (swapping grabs, directions and links is reusable by design). Animation skeletons and semi-transparent previews are the key to saving money.
- Scheduling anchors: a vertical slice of "one course plus one scoring system" from zero usually takes 2–4 months; music, skins and events are estimated on two ledgers, reuse and licensing (skins run the one-skeleton swap-parts pipeline; one track equals three bills — licensing fee, editing and adaptation; lock an event theme one major version ahead); the typical death by scope is shipping open world, multi-sport and online leaderboards all at once.

## 6. How to Start the First Prototype

The first prototype makes only one flat area, one ramp, one quarter pipe and one box, finished in 2–4 weeks, without touching art, music, career mode or online.

**Week 1: riding and air.** A rideable character with slope acceleration, takeoff, one full rotation in the air and landing detection wired up; the follow camera is built to a usable standard first, without chasing style.

**Week 2: tricks and scoring.** 3 to 5 tricks go into the move list, with the combo multiplier and landing wipe wired up; all game-feel and scoring parameters go into number tables and support hot-reload.

**Weeks 3–4: micro-course and internal testing.** Build three playable lines in one small course (one main, two side), closing the loop on timed rounds, score resolution and one-button restart; find 3–5 people who have never played it, give each 15 minutes, and record fall causes, complaints and the moments of "want to try again" — no hints, no explanations, just observation.

Success criteria (all observable):

- With all art and audio removed, testers still want to farm score, typically 10+ minutes per session, and someone asks unprompted for another run.
- At least 4 of 5 testers complete a takeoff, a trick and a landing with no verbal instruction; "I input it right but still fell" complaints stay at or under 1 per person.
- Change any one parameter (hang time, landing tolerance or one trick's base score) and you can quantify its effect within 5 minutes; testers can explain their own falls as timing, attitude or line.

If game feel and scoring do not pass, do not start laying out courses; rework on the foundation is the most expensive bill in this genre.

## 7. Common Pitfalls

1. **Laying out courses before game feel is frozen**: courses are built around the wrong launch speed and hang distance, and moving one parameter forces a full rebuild; freeze the controls first, then mass-produce courses.
2. **No decisions in the air**: the trick plays out automatically after takeoff and the player becomes a spectator; rotation speed, attitude correction and early landing must leave room for input (§3.1).
3. **Scoring unexplainable, one routine eats everything**: the score structure disagrees with the player's understanding, and after long play they cannot say where the points come from; repeat decay and difficulty pricing must ship together to prevent "one trick farming to the top" (§3.2).
4. **Landing detection disagrees with the visuals**: it looks like a clean landing but it is a fall; it looks like a fall but it is saved; bias detection uniformly toward the player and give a save window (§3.1, §3.4).
5. **Fall penalties too heavy**: a long line has no checkpoints and one mistake means tens of seconds of re-riding; when a fall costs more than ten seconds, the fun starts leaking (§3.4).
6. **Procedural mountains as the main content**: generated routes are unreadable, unsolvable and repetitive in threes; generation fits only long-line supplements and events (§3.3).
7. **Cultural packaging as stickers, not a lifestyle**: music, clothing and vocabulary each say something different and it reads as fake at a glance; fix the community viewpoint before writing symbols, and schedule music rights and replacement workflows into the milestones (§3.5).
8. **Replay and community tools missing**: half the drive in extreme sports is "showing others"; replay, ghosts and edits are the engine of retention, not a nice-to-have.

Extreme sports looks like it sells points, but what it actually sells is "that last one was this close to landing": keep tricks controllable, falls cheap and scores honest, and one more run is always worth it.

## Further Reading

- Game Design Handbook: core loops, game-feel checklists and number-table methods — the base document for §3.
- Level Design Handbook: metrics, guidance, pacing and the whitebox workflow — the full expansion of the course and line material.
- Programming Handbook: state machines, deterministic physics, replay and performance-budget detail.
- Art & Audio Handbook: music, camera language and feedback synthesis, complementing the cultural-packaging section.
- Case Studies: review methods for success and failure cases, for comparison when breaking down titles.
- The Racing page in the Genre Handbooks (Volume 3) and the Platformer page in the Genre Handbooks (Volume 1): a comparative read on sense of speed, line reading, jump feel and failure tolerance; §1 of this page draws the boundaries.
- Indie Survival: scope control and scheduling, complementing §5.
- Homework: greybox a score-farming prototype of "a three-line course plus 3 tricks plus a combo multiplier", run it for a full hour and record the three most common fall causes; then take a title you know well and write one of its lines out as a score sheet, segment by segment, marking each playable object's score source and risk tier.
