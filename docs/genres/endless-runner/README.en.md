# Ludo Atlas · Genre Handbooks · Endless Runner

> **Genre Handbooks · Volume 4**. Positioning: the genre that makes "always running forward" its core tension, holding up a procedurally generated endless track on a control floor of one or two gestures; one mistake ends the run, and distance plus coins are what bring players back. This page covers minimal controls and depth, procedural generation and the difficulty curve, sense of speed and camera, revival and monetization, the long-term pull of skin collection, and scope arithmetic for small teams.
> Companions: Game Design Handbook (core loop and difficulty curve) · Programming Handbook (procedural generation and performance) · Live-Ops & Growth (retention, monetization and long-term operations) · Art & Audio Handbook (sense of speed and feedback).
> No external links here; the benchmark list covers only widely known titles, and all figures are typical orders of magnitude — calibrate against your own project's measurements.

---

## 1. Positioning and Core Loop

In one sentence: an endless runner is **the genre that makes "always forward" its core tension**. The character runs on automatically and the player makes few but high-frequency decisions; the track extends forever and is procedurally generated, a run is settled by how far you ran, and one mistake ends it on the spot.

The core loop, written as a chain of verbs:

`Read the road → Swipe or tap → Dodge obstacles and grab pickups → Speed keeps climbing → Mistake → Results → Another run`

The loop is measured in seconds, with a run typically lasting tens of seconds to a few minutes; death to restart is one click apart. This is what sets it apart from most action genres: the entire penalty falls on "this run is void", not on lost progress. Two main branches: 3D three-lane runners (swipe-driven) and 2D side-scrolling runners (built on taps or holds); the skeleton is shared, and the difference is input grammar and freedom of scene — this page covers the trunk both share.

Boundaries against adjacent genres:

| Adjacent genre | Boundary |
| --- | --- |
| Platformer | Platformers have handcrafted levels and an ending; endless runners are procedurally generated, forever forward, and settled one run at a time |
| Racing | Racing competes on closed circuits for position and lap times; the endless runner is a one-way survival distance with no rivals and no return leg |
| Hypercasual | Hypercasual is a scope and publishing tier, not a gameplay skeleton; many hypercasual titles stand precisely by borrowing the runner loop |

One self-check question: remove the rule that one mistake ends the run — does the game still stand? If the answer is "no", what you are making is an endless runner.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Zero-threshold start**: no text tutorial in the first run — players figure it out within ten seconds; the input grammar reads at a glance.
2. **Attributable failure**: every death can be explained as a missed read, a slow hand or greed for coins — never "the generator killed me".
3. **Speed and command feeding each other**: the farther you run the faster it gets, and precision rises along with it; the pull to play once more peaks when a run closes in on a personal record or quest goal (§3.4).
4. **Long-term collection motivation**: skins and characters give the run a permanent showcase position at the center of the screen (§3.5).

Benchmark titles (play them yourself before breaking them down — watching video won't teach you the rhythm):

| Title | What to learn from it |
| --- | --- |
| Temple Run (series) | The origin of three-lane play and swipe gestures; the pursuer creating opening tension and turn rhythm |
| Subway Surfers | Fast-paced lane switching, and a long-term operations example of quest systems and skin collection |
| Tiantian Kupao | A mass-market pathway grafting a runner onto progression, pets and social play |
| Alto's Adventure | The minimal restraint of one-button control; an emotional curve where slopes and music rise and fall with speed |
| Jetpack Joyride | A single hold-to-rise input; variation from achievement quests and random in-run abilities |

## 3. Design Essentials

### 3.1 Minimal Controls and Depth: The Limit of One or Two Gestures

An endless runner's input set is tiny, so fix it down first: swipe left/right to switch lanes or steer, swipe up to jump, swipe down to slide, tap to jump (2D often uses tap or hold). Keep base actions to no more than three — beyond that, gestures start stealing each other's recognition and the touchscreen experience collapses.

| Gesture | Action | Common misreads and countermeasures |
| --- | --- | --- |
| Swipe left/right | Lane switch or steer | A diagonal swipe registers as the wrong direction; set a threshold for direction recognition and give the dominant axis priority |
| Swipe up | Jump | Repeated triggers inside the takeoff window; lock lane switching during a jump, or explicitly allow it to interrupt |
| Swipe down | Slide, roll | A too-short swipe reads as a tap; recognize on both speed and distance |
| Tap | Jump or fire | Rapid taps drop inputs; add input buffering — the same technique as in platformers |

Three general rules: once a gesture is recognized, the action executes in full — no half-way interruption; only one unfinished gesture at a time; the input zone and the thumb-occlusion zone stay separate, with a safe margin left around the readable area.

Depth comes not from button count but from route and timing trade-offs: put rewards (coins, power-ups, shortcuts) on dangerous lines and safety on empty ones, and the player makes a "greedy or not" micro-decision every second. 2D one-button runners (the Alto kind, the Jetpack kind) stake all their depth on rhythm and terrain reading — input drops to one button while decision density actually rises.

One self-check: explain the full control set to someone who has never played — under thirty seconds; yet they will still discover a new route trick on run ten.

### 3.2 Procedural Generation and the Difficulty Curve

The unit of generation is the chunk, not the individual obstacle. Hand-design a library of chunks (obstacle groupings), each tagged with length, minimum speed tier, difficulty rating and the entry/exit types it can connect to; at runtime they are stitched by rules, not scattered at random. Pure random scattering produces unreadable — even unsolvable — sequences within tens of seconds; it is the most common technical failure in this genre.

Generation divides into four layers with clear responsibilities:

| Layer | What it covers | Who decides |
| --- | --- | --- |
| Chunks | Obstacle groupings and safe routes | Hand-designed, tested and tagged one by one |
| Stitching | The order in which chunks appear | Rule-constrained randomness: difficulty budget, anti-repetition, entry/exit matching |
| Parameters | Speed, density, chunk pool | Curve functions of distance, all kept in balance tables |
| Decoration | Scene props, atmosphere and collectibles | Free to randomize, but must not mislead or collide |

The difficulty curve climbs on two axes at once: speed rises with distance and then caps, after which the other axis keeps adding pressure; chunk difficulty unlocks in tiers by pool — single obstacles first, then combinations, then combinations of combinations. The "difficulty budget" is the core tool: each stretch of distance grants a budget, drawing a chunk spends it, harder combinations cost more, and when the budget runs out a breather chunk is forced in.

Fairness discipline (the generator's acceptance line):

- Solvability and readability: at every moment at least one passable route exists, verified by "speed × reaction time" — and retested whenever speeds change; no surprises from blind spots, and jump landing spots and slide exits must be visible.
- Pacing: insert empty running or low-density stretches between hard segments; sustained pressure amounts to a hidden death trap.
- First appearance: a new obstacle is demonstrated in full once in a safe environment (the same teach-then-test variation as elsewhere), then enters the draw pool.
- Reproducible seeds: randomness is driven by a fixed seed, which is what makes daily challenges and same-map friend comparisons stand (§4).

### 3.3 Sense of Speed and Camera

The sense of speed is this genre's core product; it is not a number on a gauge but an ensemble of five devices:

| Device | How | Caveats |
| --- | --- | --- |
| Field of view | FOV widens with speed and caps | Large swings cause nausea; tune the cap on a real phone |
| Camera | Follow distance stretches with speed, lane switches eased, shake kept small | Shake serves the sense of speed; it must not block the readable zone ahead |
| Pitch | Wind, engine and footstep pitch and volume rise with speed | Speed changes need smooth transitions; jumps grate on the ear |
| Near-field | Streetlights, railings, particles and speed lines whipping past close to camera | Must not cover the anticipation zone ahead of obstacles |
| Character | Forward lean, afterimages, animation frequency accelerating with velocity | Visuals and hit detection must agree; nothing may look hittable but fail to register |

The camera has three dedicated jobs: lane-switch buffering — the visual interpolates laterally while hit detection uses a continuous capsule, and the two must never split into a crack where "you are in the middle but get declared dead"; at the moment of death, slow down and push the camera in, because the cause of death must be seen clearly — that is the precondition for players accepting failure; after a revive the camera resets and must not carry the pre-death tilt or zoom into the next stretch. Turn-style cameras (the right-angle street-corner kind) are highly legible, but the telegraph has to be real: road-surface changes, arrows or wall guides given early — otherwise every turn is a nausea source.

### 3.4 Results, Revives and Monetization Rules

When a run ends, give three things first: this run's distance (including how close it came to the personal record), the coins earned, and quest progress; restart is one button, no more than one click away. The results screen is mobile's most valuable ad slot and also where it is easiest to make players sick — the recommended rules:

- Rewarded video appears only when the player actively chooses it: revives, coin doubling, bonus draws; no interstitials during a run, ever — interrupting the run with an ad is hand-building an uninstall point.
- Revives are a common mobile design: continue once from the same spot (watch an ad or spend in-run currency), but set three rules: a per-run cap on revives; the instant of revival clears the obstacles ahead or grants a stretch of invincible safe distance — never revive straight into a death; revived runs carry a mark on the leaderboard or go to a separate board, so the credibility of clean scores stays uncontaminated.
- The boundary between IAP and ads: selling skins, ad removal and currency packs is mainstream; selling a direct power lane to "run farther" dilutes the credibility of scores, and friend comparisons and leaderboards slide with it.

### 3.5 The Long-Term Pull of Skins and Character Collection

The runner character lives at the center of the screen — one of mobile's highest-value showcase slots: skins extend a game's life more in this genre than in most, because players see them on themselves every single run.

| Layer | What it covers | Source of drive | Rules |
| --- | --- | --- | --- |
| Skins | Looks, themed crossovers, holiday limited editions | Display and rarity | Legibility first — recognizable at distance and in low light |
| Characters | Looks plus a tiny difference (e.g., slightly faster starting acceleration) | Feel preference and identity | Keep differences negligible; power tiers are forbidden |
| Quests and achievements | Daily and weekly goals | Daily logins and a sense of goals | Quest-driven play (slide cleanly N times), not attendance check-ins |
| Collection album | Completion percentage and unlock tree | The long-tail goal that closes things out | Acquisition pacing must sustain months of daily logins — don't release it all at once |

Three rules: skins follow a reuse pipeline of "one skeleton, reskinned plus accessory parts" — that is the only way costs stay controllable; when characters carry ability differences, run a balance audit so paying never feels like cheating (monetization ethics in Live-Ops & Growth §10); limited-time runs and events are the main engine of return motivation, and holiday-themed skin schedules need to be locked one major version ahead.

## 4. Technical Essentials

The engineering difficulty concentrates in four places: runner control, procedural generation, mobile performance and input recognition; the following is engine-agnostic, with method details in the Programming Handbook.

**Runner controller**

- Use rails or a spline to define the forward path, and move the character kinematically: compute forward speed, lateral lane interpolation and the jump parabola yourself instead of handing them to full rigid-body physics; approximate collisions with capsules or boxes and keep hit detection lenient — near misses give feedback but don't kill, with every error biased in the player's favor.
- Frame-rate independence: compute displacement in delta time so the logic stays consistent on low-frame-rate devices; the latency budget from input to judgment takes priority over visual quality.
- Lane switching, jumping and sliding form a state machine with explicit interruption rules (can you switch lanes mid-air; can you jump while sliding) — all written into a single state table.

**Procedural generator**

- The chunk library is data-driven: each chunk is a config (length, difficulty, speed range, exit type) plus an object manifest; the generator knows configs, not scenes.
- The stitcher carries constraints: difficulty budget, anti-repetition window, entry/exit matching, minimum safe stretch; generation logic needs single-step visual debugging that draws the budget and draw results on screen.
- Object pooling: obstacles, coins and decoration props are all pooled and reused to avoid allocation hitches mid-run; unloading recycles rather than destroys.
- Seeded randomness: the same seed produces the same track — daily challenges, replay recordings and score arbitration all depend on it.

**Mobile performance**

- Set the budget by the worst device: lock a target frame rate (60 is common, 30 on low-end hardware), and when frame rate wobbles, cut decoration and particles first — never readability.
- Draw calls, memory and heat: batch materials, share atlases, stream-generate chunks ahead and recycle them immediately behind, and derive the memory cap backward from low-end phones; heat and battery drain are retention problems, so quality tiers, resolution scaling and frame-rate strategy become switches from day one.

**Input and gestures**

- Three elements of gesture recognition: direction threshold, speed-and-distance dual conditions, dominant-axis priority; calibrate diagonal-swipe misreads against real finger-trace data, not desktop mouse simulation.
- Input buffering and stacking rules: taps may be queued to take effect after landing; two different gestures must never be recognized as the same action in the same frame. Keyboard and gamepad mapping is a bonus, but polish the default experience for touch, and run the tolerance parameters on a phone first.

## 5. Content Volume and Workload Reference

The following are common magnitudes for comparable projects, for scope estimation — not a commitment.

| Project form | Content volume | Timeline | Notes |
| --- | --- | --- | --- |
| Feel prototype | 1 endless track, 3 obstacle types, 2 gestures | 1–2 weeks | Validates only controls, the speed curve and restart |
| Small title | 1 scene theme, 1–2 characters | 1–3 months | The generator and camera polish take the bulk |
| Typical mobile title | 2–4 scene themes, a chunk library of a hundred-plus entries, 4–8 character skins | 3–9 months | Skins and events are ongoing costs |
| Long-running live title | Seasonal theme updates | Ongoing after launch | Live-ops investment exceeds initial development |

- A generated chunk is the cheapest content unit: a chunk's whitebox can come out in a day, but testing and difficulty-tagging each one is the hard part; once the library passes a hundred entries, richness comes from the constraint system, not from piling on more.
- Estimate skins and scene themes along the reuse pipeline: a character's full animation set (run, jump, slide, death, showcase) is a one-time investment, and later skins are just a set of accessory parts and textures — costs drop by an order of magnitude; a scene theme equals one modular set of scene pieces plus decoration, with the same reuse discipline as racing tracks — spread one theme across several event seasons, squeeze it dry before making a new one.
- Scheduling anchors: from zero to "a stretch of run experience at shipping quality" (vertical slice) usually takes 1–2 months; extrapolate from there by content volume times a polish factor. The common way scope spirals to death: skins, systems and events all launched at once while not a single track is polished.

## 6. How to Start the First Prototype

The first prototype makes only one endless track, one controllable character and three obstacle types (lane-dodge, jump, slide), finished in 1–2 weeks — no skins, ads, quests or leaderboards.

**Days 1–2: auto-forward and camera.** The character runs forward automatically along the rail, speed rises linearly with distance, the camera follows; generate no obstacles yet — get the felt sense of the speed climb smooth first.

**Days 3–5: the full control set.** Wire up the lane-switch, jump and slide trio, tuning input tolerance item by item: gesture thresholds, buffer windows, state-machine interruption rules. Try it with 2–3 people and log the two complaint types: "gesture didn't respond" and "wrong direction".

**Week 2: generation and restart.** Build a dozen-odd chunks first, put the difficulty budget and anti-repetition into the stitcher; wire the closed loop of death → results (distance and coins) → one-click restart. After that, tune parameters only — add no systems.

Success criteria (all observable):

- With all art and audio stripped out, testers still run repeat sessions, usually 10+ minutes at a time.
- At least 4 of 5 testers start running with no verbal instruction; "I clearly swiped and nothing happened" complaints run at no more than 1 per person.
- Testers can explain their own deaths (missed a read, slow hand, greedy for coins) — not "the generator screwed me".
- A tester asks for another run on their own, rather than being asked to try again.
- Change any speed or budget parameter and you can quantify its effect on average distance within 5 minutes.

If controls and generation don't pass, don't start laying content; rework on the foundation is the most expensive bill in this genre.

## 7. Common Pitfalls

1. **Laying content before the input grammar is settled**: gestures and camera still churning while skins, themes and events have already gone first — everything gets torn down; freeze the controls and speed curve first, then mass-produce content.
2. **Purely random obstacle scattering**: unreadable — even unsolvable — sequences destroy trust with precision; the unit of generation must be hand-designed, difficulty-tagged chunks (§3.2).
3. **Difficulty carried by speed alone**: once speed caps, the game goes flat in an instant; speed and combination complexity must climb on two axes (§3.2).
4. **Blind-spot surprises and dead-end combinations**: a generator that doesn't verify solvability and readability turns deaths from "I'm bad" into "the game is broken", and negative reviews and churn both start here.
5. **Visuals and hit detection split apart**: declared dead halfway through a lane-switch interpolation, or a slide animation shorter than its detection; keep detection lenient and aligned with the visuals (§3.3, §4).
6. **Piling everything into one sense-of-speed device**: only widening the FOV or only adding shake leaves players nauseous and the screen dirty — and the sense of speed still doesn't land; it is an ensemble (§3.3).
7. **Ads interrupting the run**: an in-run interstitial is an uninstall button; rewarded video appears only when the player chooses it (§3.4).
8. **Sloppy revive handling**: no clearing of the obstacles ahead and no safe distance turns the continue into a second death; revived scores mixed in with clean ones cost the leaderboard its credibility (§3.4).
9. **Indistinguishable skins, powerful characters**: a palette-swap skin gives no urge to collect, and a character with real power makes paying equal cheating; apply the discipline on both sides (§3.5).

An endless runner looks like it sells speed and coins; what it really sells is "so close to the record": as long as death stays cheap and scores stay honest, the next run is always worth taking.

## Further Reading

- Game Design Handbook: core loops, difficulty curves and balance-table methods — the full source material for section 3.
- Programming Handbook: procedural generation, object pooling, performance budgets and input handling, expanded.
- Live-Ops & Growth: retention curves, monetization design and event cadence — the companion to §3.4 and §3.5 here; monetization ethics in its §10.
- Art & Audio Handbook: the audiovisual mix behind the sense of speed and character animation feedback.
- The Platformer page in the Genre Handbooks (Volume 1): the three elements of game feel and general input-tolerance techniques — the foundation of the control layer.
- The Racing page in the Genre Handbooks (Volume 3): a comparative read on sense of speed and camera handling; boundaries in section 1.
- Indie Survival: scope control and scheduling, complementing section 5.
- Assignment: greybox one track containing "three obstacle types, one speed jump and one breather stretch", play a hundred-plus runs and record the death-point distribution; then take a title you know well and record where it guides your eyes in the first 60 seconds and how much obstacle lead time it leaves.
