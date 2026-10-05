# Ludo Atlas · Genre Handbooks · Platformer

> **Genre Handbooks · Volume 1**. Positioning: making the act of jumping itself the first pleasure, and using game feel and level pacing to keep producing the urge for "one more try".
> Companions: Level Design Handbook · Game Design Handbook · Programming Handbook · Art & Audio Handbook.

---

## 1. Positioning and Core Loop

In one line: the platformer is the genre **with movement and jumping as its first pleasure**. Players get a sense of control from responsive control feedback, and a sense of conquest from the level pacing; jumping is not a means of getting around — jumping itself is the content.

The core loop, written as a verb chain:

`read the terrain → predict the landing spot → jump → adjust in mid-air → land or fail → try again immediately`

This loop is measured in seconds, even in frames. It holds on just two preconditions: controls must be responsive (§3.1), and failure must be cheap (§3.4). If any link's feedback latency exceeds 200 ms, players will chalk it up to the game rather than to their own hands.

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Endless runner | The platformer has handcrafted levels and an ending; the endless runner is usually procedurally generated, only ever forward, and restarts on one mistake |
| Metroidvania | Metroidvania is the platformer plus a connected map and ability gates; the bodily pleasure shares its roots, but the skeleton becomes exploration and revisiting |
| Precision platformer | The same game feel, two product positionings: one screens its audience by death density, the other widens its audience with safety nets |
| Action game | In an action game the object of the action is enemies; in a platformer it is the terrain |

A self-check question: break the jump feel — does the game still hold up? If the answer is "no", what you are building is a platformer.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Sense of control**: every jump's success or failure can be explained by the player — losing means blaming yourself, winning makes you want to run it again.
2. **Smooth cadence**: controls, camera and sound land on the same beat; players stop noticing which key they are pressing and think only about the next landing spot.
3. **Progressive challenge**: difficulty comes from new hazards and new combinations, not from stacked numbers (slippery ground and smaller platforms must be used with restraint).
4. **Low-pressure retries**: from failure to restart is a matter of seconds, and retrying is itself part of the gameplay.
5. **Moments of surprise**: players are allowed to use the mechanics to find routes you never designed, and those routes get room for rewards.

Benchmark titles (play them yourself before breaking them down; watching videos won't teach you game feel):

| Title | What to learn from it |
| --- | --- |
| Super Mario Bros. | The baseline for jump feel, wordless teaching, flow guidance |
| Celeste | The leniency of hard levels, difficulty layering (the main line and the challenge side split the audience) |
| Super Meat Boy | Instant retries, turning failure into positive feedback |
| Rayman Legends | Level pacing synchronized with the music's beat |
| Hollow Knight | Movement and combat sharing one body-feel system |
| Kirby | Low-barrier jumping and loose mid-air correction |

## 3. Design Essentials

### 3.1 The Three Elements of Jump Feel

Game feel is not mysticism; it breaks down into adjustable parts. Get these three right first:

| Element | Common range | Effect | If you get it wrong |
| --- | --- | --- | --- |
| Coyote time | 80–150 ms | The grace window that still allows a jump after leaving a platform's edge | Set it to zero and edge jumps fail constantly; too long and it feels like cheating in mid-air |
| Input buffering | 100–200 ms | A jump pressed before landing is remembered and fires the moment you land | Set it to zero and chained jumps drop inputs; too long and mid-air mashing auto-jumps too |
| Variable jump height | Tap height is 1/3 to 1/2 of hold height | Releasing the button immediately cuts ascent speed, or switches to heavier fall gravity | Without it, small and big jumps are indistinguishable and landings can only be guessed at |

Two bonus touches: ascent and descent use different gravity (fall gravity is usually 1.3–2× ascent gravity, which makes jumps crisper); the takeoff frame gives the initial velocity directly instead of accelerating slowly (a sense of burst).

Tuning discipline: trust only frame-by-frame recordings and a stopwatch, never "feels about right"; tune at the target frame rate and target resolution, not under the editor's default state.

Acceptance criterion: have 5 people jump 20 times each and record the number of "I pressed it but it didn't jump" cases — 0 to 1 per person passes.

### 3.2 Movement Curves: Tune the Three Knobs Separately

Acceleration, deceleration and air control are three independent knobs, all managed in number tables (table methods in the Game Design Handbook):

| Knob | Common 2D range | Tuning goal |
| --- | --- | --- |
| Ground acceleration | 0.05–0.25 seconds to full speed | A crisp start, no float when held |
| Ground deceleration | Stops 0.05–0.2 seconds after release | A sharp stop without sliding, a light tap moves half a step |
| Air control | 50–80% of ground acceleration | Landings correctable in mid-air, but with less authority than on the ground |

2D has two classic leanings: the Mario style, with inertia — both starts and stops keep a sense of glide, and landings are forgiving, good for exploration; the Celeste style, starting and stopping almost instantly, where the landing spot is life or death, good for single-screen hardcore play. Which one you pick depends on whether your levels want to punish or forgive.

3D differs in turning: not instant reversals but interpolated body orientation, with longer turning radii and stopping distances; movement direction is usually camera-relative, acceleration is a notch lower overall, and a landing shadow or ground marker compensates for the missing sense of distance in 3D space.

Checklist: does tapping a direction repeatedly cause slide-stepping? Does a full-speed emergency stop drift? Can one nudge in mid-air hit the spot exactly? These three answers decide the tier of your game feel.

### 3.3 Camera Design: The Second Player

The camera is the second player — it reads the road for the player and telegraphs danger for them. It has to satisfy three things at once: the character is clearly visible, the road ahead is visible far enough, and it doesn't make anyone dizzy.

| Mechanism | Common practice | Number intuition |
| --- | --- | --- |
| Look-ahead | The camera offsets toward the direction of movement, growing with speed and capped | Roughly 0.3–0.6 seconds of lead distance, capped at 20–30% of the screen width |
| Dead zone | The camera stays still while the character moves inside the dead zone | The vertical dead zone is commonly 10–20% of screen height, and can be smaller horizontally |
| Vertical follow | No twitching with every jump; the camera pushes up or down only past a height-difference threshold | The threshold is 15–25% of screen height, with easing |
| Boundary lock | The camera never shows outside the level, and room transitions are smooth | Each room defines its own bounds and transition duration |

Horizontal soft follow plus vertical lag suits most platformers; fast stretches need a cap on follow speed to prevent camera flinging. Room transitions, getting knocked back and falling to your death are the three easiest places to break the illusion — test them one by one.

Acceptance criteria: after 30 jumps in a row, no per-jump jitter is visible; at full sprint the landing spot is always on screen with margin to spare; no tester reports "the camera swung so hard I couldn't see".

### 3.4 Level Pacing: Teach, Test, Twist

A new mechanic's introduction follows a fixed three-beat structure (teach–test–twist):

1. **Teach**: show it once in an environment with no death cost, so players get it without even thinking.
2. **Test**: let players use it themselves in a low-pressure scene, where failing and retrying costs almost nothing.
3. **Twist**: use it again under changed conditions (add time pressure, switch terrain, stack old mechanics) to check that the skill transfers.

Teach only one new thing at a time; stuff two new mechanics into the same room and cognitive load doubles and players remember neither.

Safety nets come in two layers: the micro safety net is coyote time, input buffering and landing leniency; the level safety net is checkpoint density, wide platforms and reversible paths. The retry walk-back is usually kept within 10–20 seconds; past 20 seconds, frustration starts eating into the will to take on the challenge.

The distribution of death penalties follows an intensity curve: a section's climax can punish heavily, but pure execution stretches must punish lightly and get the player back into the game fast. Tension alternates with release — leave a breathing stretch before and after every boss fight or chase.

Run every new room through the checklist:

- What do players see the moment they enter? Is the objective in view?
- Does the new mechanic have a second use (something players can do with it once they are fluent)?
- Can players say out loud why they died the first time?
- How many seconds does a retry cost? What is the exact number?

### 3.5 Metrics: Setting Platform Spacing with the Jump Radius

Before laying out levels, measure five numbers: the horizontal distance of a full-speed jump on flat ground (call it D), the maximum jump height, airtime, fall speed, and the time needed to reach full speed. Tape these numbers beside your monitor; every distance derives from them.

Platform spacing is tiered by D:

| Multiplier | Positioning | Where to use it |
| --- | --- | --- |
| 0.8D | Comfortable | Main paths, teaching stretches, reward routes |
| 1.0D | Standard challenge | The ceiling for main-line difficulty — allowed, but accuracy required |
| 1.2D | Extreme | Optional content, shortcuts and mastery payoffs only; never on a mandatory path |

Vertical spacing is tiered the same way: common layer heights are 0.6–0.9× the maximum jump height, and anything above 0.9× should be marked "needs skill". Spacing is measured as the net distance from takeoff edge to landing edge, with half a character-width of visual margin at each end; build separate tables for extra mobility — dashes, bounces, wall jumps — and don't mix them into the base table.

Checklist: is there any mandatory jump over 1.0D on the main line (if so, it is a design incident)? Does a 1.2D spot get visual telegraphing? Are landing spots in fast stretches covered by the camera (§3.3)?

## 4. Technical Essentials

The engineering difficulty concentrates in three places: character control, the parameter system and testability. Everything below is engine-agnostic; Godot and Unity both ship kinematic character-controller components, with counterparts for 2D and 3D, so you don't need to build your own to start — what you do build yourself is the parameter system, the state machine and the camera logic.

**Character control**

- Manage the character kinematically: compute velocity, gravity and collision response yourself; never hand the character to full rigid-body physics, or the engine's solver will dictate your game feel.
- Use a fixed physics timestep (commonly 60Hz) with rendering decoupled from physics; sub-step or run continuous detection when per-frame displacement exceeds half a collider, to prevent high-speed tunneling.
- Make landing detection more lenient than the visuals: sample several points under the feet and let half a foot over the edge count as standing firm. Players trust their eyes, so let the physics concede to the eyes.
- One-way platforms, moving platforms and pass-through walls are three separate systems. Of the two mainstream ways to carry the character on a moving platform, adding the platform's displacement to the character each frame is usually more stable than parenting; test all three cases — lateral movement, vertical movement and direction changes — for jitter and sliding.

**The parameter system**

- Coyote time, input buffering and variable jump height are all implemented as "timer plus state flag": start a countdown when leaving the ground, keep one pending jump request before landing, switch the ascent speed or increase fall gravity on release. Put all of it in the character state machine, not in animation events.
- Keep game-feel parameters in one place (a number table or config file) with stray magic numbers forbidden; parameter changes must take effect immediately in the running game. Tuning efficiency sets the ceiling on game feel.

**Testability**

- The first debug tool is jump-trajectory visualization: velocity vectors, arc previews and current parameter values on one screen. Without it, tuning is blind groping.
- Visual and audio feedback are amplifiers, not life support: takeoff stretch, airborne tuck, landing squash, plus dust particles and audio layers, so good feel is seen and heard (methods in the Art & Audio Handbook).
- Check input-to-screen latency in frames, targeting within 2–3 frames; test keyboard, gamepad and touch separately, and for touch also design the position and size of virtual buttons.
- If you plan to support speedruns or ghost replays, the physics must be reproducible (fixed timestep, reproducible random numbers); every game-feel change demands a fresh assessment of whether existing records remain comparable.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimation and for cutting requirements; not a commitment.

| Project shape | Level count | Timeline | Notes |
| --- | --- | --- | --- |
| Game-feel prototype | 1 room | 2–4 weeks | No art; validates jumping and the camera only |
| Small complete title | 10–20 short levels | 1–3 months | A single mechanic, one themed art set |
| Typical indie 2D title | 15–30 levels, or 6–10 themed areas | 1–3 years | Level iteration and polish take the lion's share |
| 3D platformer | 8–15 levels plus collectibles | 2–4 years | Art and environment costs far above 2D |

Art volume: a 2D character's base move set (idle, run, jump, land, hurt, die) usually totals 30–60 animation frame groups, plus effects and UI icons; one theme's tileset is usually tens to hundreds of tiles, progressing by "enough for whitebox first, then replace piece by piece".

Level volume: whiteboxes come out fast and polish is slow, with a time ratio usually of 1:3 to 1:5 (one day of layout to three to five days of testing and revision). Level count is not the goal — density is: a 30-second stretch of experience usually needs one small climax, one decision or one discovery.

Scheduling anchors: a playable game-feel prototype from zero usually takes 2–4 weeks; reaching a vertical slice (one stretch at release quality) usually 2–4 months; extrapolate from there by "content volume × polish factor". Runaway scope is this genre's most common cause of death — cutting levels is always safer than piling them on.

## 6. How to Start the First Prototype

The first prototype is a single room, done in 2–4 weeks, with no art, story, saves or menus.

**Week 1: single-room game-feel prototype.** One flat patch of ground, three to five platforms, one pit, one wall for wall jumps, one camera. Make all three elements from §3.1 and all three knobs from §3.2 adjustable and hot-reloadable. Being ugly at this stage is correct.

**Week 2: tuning and internal testing.** Tune game feel from frame-by-frame recordings; bring in 3–5 people who have never played it, watch when they stop, when they curse, when they laugh, and log death points and pause points without prompting or explaining.

**Weeks 3–4: miniature pacing validation.** Add teach, test, twist to the same room: one platform that teaches the new mechanic, one low-pressure path to test it, one combination as the twist. Validate whether the feel you tuned can support level design, then decide whether to lay down volume.

Success criteria (all observable):

- With all art and audio removed, testers still want to play again and again, typically 10+ minutes per session.
- At least 4 of 5 testers clear the room within 3 minutes with no verbal guidance; "I pressed it but it didn't jump"-type complaints come no more than once per person.
- For any one jump parameter you change, you can quantify its effect on clearing the room within 5 minutes (provided the metrics and tools are in place).
- Testers retry on their own rather than being asked for one more try.

If the game-feel acceptance doesn't pass, don't start laying out levels. Rework on the foundation is the most expensive bill in this genre.

## 7. Common Pitfalls

1. **Laying out levels before feel is locked**: levels built on the wrong jump radius all get redone the moment a parameter changes. Until game feel is frozen, don't mass-produce a single level.
2. **Tuning by feel without watching frames**: no recordings, no frame counts, no metrics, and months of tuning go nowhere. Game feel is a frame-by-frame problem.
3. **Hard-binding the camera to the character every frame**: the view becomes a source of motion sickness and all landing-spot information is lost. The camera needs soft follow, look-ahead and a dead zone (§3.3).
4. **Judging inconsistent with the visuals**: a ledge that looks standable isn't, a jump that looks clearable isn't. Players trust their eyes; don't concede and you eat the bad reviews.
5. **Measuring platform spacing in character pixels**: the right ruler is the jump-radius table (§3.5), not body size.
6. **Punishment too heavy**: checkpoints too far apart, death wiping progress, half a minute of walking back at minimum. Death in a platformer should be cheap and retries should be smooth.
7. **Air control as strong as ground control, or missing entirely**: the former robs jumps of weight, the latter leaves nothing correctable in mid-air. Both extremes ruin game feel.
8. **Moving platforms that don't carry the character, or jitter when they do**: rework it with a displacement-inheritance approach; don't patch it by brute force with "feel correction".
9. **Levels with passability but no expression**: all-symmetric grids, no landmarks, no vistas — players can't remember the route and take nothing away.
10. **Piling on art during the prototype**: texturing before the greybox has passed testing means every gameplay change voids the work; every image created before art enters production may be sunk cost.

## Further Reading

- Level Design Handbook: metrics, guidance, pacing and the whitebox workflow — the full expansion of §3 here.
- Game Design Handbook: the base document for core loops, number-table methods and game-feel checklists.
- Case Studies: retrospective methods for success and failure cases; consult when breaking down titles.
- Indie Survival: scope control and scheduling, complementing §5 here.
