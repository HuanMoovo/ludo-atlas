# Ludo Atlas · Genre Handbooks · Racing

> **Genre Handbooks · Volume 3**. Positioning: making "speed and control" the first pleasure — trading game feel for the player's trust in the car, and trading tracks and rivals for the urge to run one more lap.
> Companions: Game Design Handbook (game feel and number tables) · Level Design Handbook (tracks and pacing) · Programming Handbook (vehicle simulation, performance and synchronization) · Case Studies (breakdown and review methods).

---

## 1. Positioning and Core Loop

In one line: racing is the genre **with speed and control as its first pleasure**. Players build trust in the car through driving feedback and cash it into position and lap times inside the pincer of track and rivals; "driving fast" is not a means of travel — speed is itself the content.

The core loop, written as a verb chain: `pick a car → start → take the line through the corners → battle rivals → cross the finish line → read lap times and position → run one more lap`

This loop is counted in laps, with a lap running from tens of seconds to a few minutes. It stands on two preconditions: the car must be predictable (§3.1), and failure must be cheap. Racing has two mainstays: the arcade direction leans on readability and instant thrill, the simulation direction on physical fidelity and tuning depth; the skeleton is one and the same, and this page covers the trunk the two share.

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Vehicular combat | The carrier is likewise a car, but victory comes from destruction, not lap times |
| Open-world driving | Driving is a way to move, and racing is one activity inside it |
| Racing-adjacent sports (parkour, skateboarding) | Also chasing speed, but the route is a free three-dimensional path, not a closed circuit |

A self-check question: take away lap times and position entirely — does the game still hold up? If the answer is "no", you are making a racing game.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Sense of speed**: fast must be seen, heard and felt; turning up the gauge numbers alone does not constitute a sense of speed.
2. **Sense of control**: every mistake can be explained as braking, line or throttle — not "this car is broken".
3. **Racing tension**: position, lap times, close-quarters battling and the finish-line moment are why rivals exist (§3.3).
4. **Mastery space**: between "finishing a race" and "setting records" there is a continuing return on practice (lines, shortcuts, exit timing).
5. **Low-friction retries**: crash or drop to last place, and running one more lap costs nothing psychologically.

Benchmark titles (play them yourself before breaking them down; feel and sense of speed cannot be learned from video alone):

| Title | What to learn from it |
| --- | --- |
| Mario Kart series | Item-based balance design, a low entry bar, local split-screen as a party fixture |
| Forza series | Layered assist systems and realistic trade-offs; the open-world driving pleasure of the Horizon line |
| Gran Turismo series | Licence-style teaching sequences, simulation-grade pricing and the benchmark of realism |
| Need for Speed series | Street-tuning culture as packaging; the pressure of police chases |
| DiRT Rally | The rhythm of single-track rally stages, with pace notes becoming part of driving |
| KartRider | Layered drift technique and the mass-market reach of item races |

## 3. Design Essentials

### 3.1 Driving Feel: Translating Physics into Instinct

Racing feel does not demand physical correctness; it demands predictability — the moment players release the steering, they can predict where the car will slide. Tuning is not copying real-car parameters into the engine; it is translating a handful of concepts — weight, grip, slip — into action responses players understand on first contact.

| Instinct | Corresponding parameters | What players perceive | What breaks when it is wrong |
| --- | --- | --- | --- |
| Grip | Tire lateral grip and its falloff curve | whether the car understeers or oversteers | infinite grip puts the car on rails; too slippery makes every corner a gamble |
| Weight transfer | how braking and throttle distribute grip between the front and rear wheels | nose dive under braking, squat under acceleration | no transfer slides like a sheet of paper; too much makes it unpredictable |
| Drift | rear-wheel slip angle and exit compensation | the thrill of kicking out and still pulling it back | too easy and every corner leans on the throw, weakening the line; too hard and the core thrill is out of reach |

Three general practices:

- Steering falls off with speed: agile at low speed and stable at high speed is the common convention; add an input response curve that gives precise micro-adjustment early and full-lock steering late.
- Tune the brake on its own: braking distance, the ability to turn while braking and braking-point consistency — the verb with the widest gap between novices and veterans.
- Pick a primary drift trigger: handbrake (rally and karting), power oversteer (arcade) or the brake-tap kick (simulation) — choose one as the primary; reward the exit with acceleration so "drifting well" cashes out directly into speed.

Assist systems are part of the feel, not a patch: racing-line assist, traction control, stability assist, automatic transmission and auto braking — each independently toggleable, with defaults friendly to novices and switchable off for veterans.

Tuning discipline: all feel parameters live in one number table and support live editing; compare lap times and frame-by-frame recordings on a fixed test track from a fixed starting point, changing one parameter group at a time. Acceptance criterion: take 5 people for 10 minutes each and record "unexpected loss of control" events — 0–2 per person is a pass; after a loss of control, the tester can say what they did wrong.

### 3.2 Track Design: Corner Rhythm and Shortcuts

A track is a sentence written in corners: straights are breaths, corner groups are clauses, and read one after another they make a lap's rhythm. Build the corner library first: fast sweepers, hairpins, linked S-bends, chicanes, blind crests and combination corners with jumps.

Before laying out a track, get hold of the car capability table: full-speed-to-stop distance, minimum turning radius, radius and speed in a drift; the entry speed of every corner, corner spacing and straight lengths are derived from these numbers rather than placed by feel (measurement methods in the Level Design Handbook).

Rhythm and shortcut discipline:

- Alternate fast and slow: strings of small corners (tension) alternate with long straights or large-radius corners (breathing); no single density across the whole map.
- At least one climax corner per track: the fastest, most recognizable corner of the whole lap, demanding a precise braking point, placed in the mid-to-late race.
- Teach, test, vary: new elements like jumps, dirt and weather appear safely first, are used under low pressure second, and combine with variation third; teach only one new thing at a time.
- Visible: shortcut entrances must be visible on the normal line, so players do not need a guide to find them.
- Learnable: a shortcut can be taken reliably after a try or two; a shortcut that cannot be learned is a trap that breeds a memorize-the-map feel.
- Worth the price: faster but harder, or safer but slower — both must hold; do not make the shortcut the only correct line unless you explicitly want to raise the competitive bar.

Guidance and readability: kerb colors, braking-point markers (distance boards, ground color patches), billboards and spectators, distant landmarks, lighting and weather; without a visual anchor at the braking point, a race becomes a memory test. Checklist (walk every corner): where do I brake at the entry, and is there a visual anchor? Where does the car hug the apex, and are the kerbs clear? Where do I get on the throttle at the exit, and can I see the next stretch afterward?

### 3.3 Rival AI: Pacing Is a Product Decision

The AI's goal is not to beat the player but to make this race a win with weight and a loss that makes you want to go again. The implementation has four layers: racing line (an ideal line computed offline or at runtime) → speed profile (target cornering speed per corner) → error injection (line deviation, braking-point jitter, occasional mistakes) → recovery behavior (rejoining and re-entering after being knocked off track); an AI with no error and no mistakes is a slot car — you would be better off making a time trial.

Rubber banding's books must be kept straight:

| Measure | Pros | Cons |
| --- | --- | --- |
| Trailing car sped up | keeps suspense, keeps novices from being left behind | the player's lead is devalued and victory loses credibility |
| Leading car slowed down | keeps the race from losing suspense too early | the most cheat-flavored option; trust collapses once noticed |

Further tools for pacing design:

- Difficulty tiers: set AI baseline lap times to tiers like 90%, 100% or 105% of the player's historical lap times (for reference), and calibrate actual AI lap times from replays — do not trust your sense of it.
- Ability bias and mistake design: some AI fast on straights, some strong in corners, creating overtaking windows; give each AI a small per-lap chance of a mistake, so players have opportunities to seize.
- Transparency: difficulty and assist choices sit in the open; players accept declared difficulty, not invisible cheating.

Checklist: after collisions, do AIs get stuck on walls or spin in place? After being overtaken, do they react (chase or change line)? When the player leads for the whole race, does P2 create "just barely" pressure without going over the line?

### 3.4 Cars and Customization Systems: Scope Control

Cars are racing's content currency and its most easily runaway cost item: one car equals a model, an interior (if you do a cockpit view), engine audio, a parameter set, livery slots and an acquisition method.

Three scope disciplines:

1. Build cars by role, not by count: starter, balanced, top-speed, cornering, drift, off-road — one flagship per role, with feel differences plain to the eye; matching a big publisher's car count is this genre's most classic way to crash.
2. Cars in the same tier must feel different: performance ratings are surface numbers, and collection motivation comes from feel differences; recolors and pure-stats cars are a review-bombing hot zone.
3. Do not touch real-car licensing: the fees and negotiation cycles for real vehicles usually far exceed an indie project's budget and schedule; original cars are the default.

The customization system comes in three tiers; choose by the project's character:

| Tier | Content | Cost intuition | Suits |
| --- | --- | --- | --- |
| Cosmetic | liveries, decals, wheel colors, racing numbers | low; one editor investment | every project |
| Performance tuning | tires, gear ratios, suspension, downforce | medium; requires feel parameters to be tunable and explainable | projects that want hardcore players |
| Performance upgrades | engine, turbo, kits and other capability upgrades | high; every change forces a retest of all track balance | projects with a progression loop |

The principle of customization is trading characteristics, not stacking numbers: hard tires last longer but grip less; high downforce is fast in corners but slow on straights; every upgrade carries a price, so players make trade-offs, not checklist stamps. The upgrade curve should mainly change driving characteristics (unlocking drift tuning, off-road tires and the like) rather than turning the same car into a faster same car; once upgrades ship, AI pacing and track feasibility must be recalibrated.

### 3.5 Mode Structure: Time Trials, Versus and Career

One track plus one rule is one new event; racing's mode design is, at heart, content reuse.

| Mode | Positioning | Cost | Notes |
| --- | --- | --- | --- |
| Time trial | solo against ghosts and leaderboards | lowest | the core retention tool; depends on the reproducibility of physics and results (§4) |
| Local versus | split-screen or shared-screen multiplayer | low to medium | strong party value; racing's most underrated high-value mode |
| Online versus | matchmaking, synchronization and anti-cheat | high | close to the investment of a separate product line; evaluate separately at greenlight |
| Career | trophies, stars and unlocks strung into progression | medium to high | track reuse as events; variants (reversed, mirrored, time-limited, weather) do the heavy lifting |

Priority advice: single-player titles should make the time trial solid first (a single track still holding up after a hundred runs means the feel and the track are already passing), then decide on versus and career investment; split the audience with assist-system toggles rather than building one set of tracks per crowd.

## 4. Technical Essentials

The engineering difficulty concentrates in four places: vehicle physics, the audiovisual synthesis of speed, ghost and result determinism, and online synchronization; everything below is engine-agnostic, with method detail in the Programming Handbook.

**Vehicle physics and collision**

- For the arcade direction use a single-rigid-body approximation: one body rigid body plus approximate models for tire grip, slip and weight transfer — easy to tune, controllable, cheap on performance; only the simulation direction needs per-wheel forces and suspension solving. Independent starters begin from the single rigid body.
- Fixed physics timestep, decoupled from rendering (60Hz and up is common); a car at speed is extremely sensitive to timestep — change it and both the feel and every result baseline must be retested.
- At high speed, one frame's displacement can exceed the car's length: use substepping or continuous collision detection; collision response slows and pushes apart rather than hard-bouncing, and guardrails and car-to-car hits must be tested stretch by stretch to be non-sticky, non-bouncy and non-clipping.
- Feel parameters (steering falloff, grip curves, power curves, braking) are all data-driven and support hot editing, with scattered magic numbers forbidden; body roll and suspension jolt may serve the visuals, but their direction must match the physics.

**Camera, audio and sense of speed**

- The chase camera needs look-ahead, pulling distance and FOV back with speed, and a slight lag toward the corner's inside through turns.
- Speed sensation is synthesized: field of view, camera shake, wind noise, the scale of scenery, texture-scroll speed on the ground — drop one and players feel "slow".
- Engine audio is a mapping of "rpm times load" (pitch, layers and mix moving with rpm and throttle); tire squeal and wind noise carry the grip limit; audio must be planned early and cannot be added at the finish (methods in the Art & Audio Handbook).

**Ghosts, replays and online**

- Two ghost schools: sampled replay records position and orientation (simple, slightly larger files); input replay records only inputs and re-simulates on deterministic physics (tiny, requires reproducible physics). Time-trial fairness demands deterministic physics, controllable randomness and frame-rate independence; change the feel and you must re-evaluate the comparability of existing results.
- The hard part of online sync is collision authority (both cars believe they own the line): the common approach is server arbitration plus client interpolation and rollback, tolerating small errors in exchange for smoothness.
- Plan performance for top speed: streaming and LOD budgets must cover the full-speed stretches; spectators, dust and tire marks are tiered by platform; split-screen renders two worlds, so halve the budget up front.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for scope estimation — not a commitment.

| Project shape | Content volume | Timeline | Notes |
| --- | --- | --- | --- |
| Feel prototype | 1 test track + 1 car | 2–4 weeks | validates driving, camera and timing only |
| Small arcade title | 4–8 tracks + 6–12 cars | 3–9 months | spread track cost with variant events |
| Typical indie title | 8–15 tracks + 10–20 cars | 1–2 years | track art and polish dominate the bill |
| Simulation-oriented title | cars and data counted by licence | 2+ years | physics calibration and licensing are the main costs |

A track is the most expensive content unit: one track equals road surface and guardrails (modular pieces), landmarks and backdrop, spectators and advertising, collision and shortcut logic, plus day, night and weather variants; the reuse discipline is to have one track cover three to four events — squeeze it dry before building new. Car costs break down as: model plus interior (if you do a cockpit view), engine and tire audio, feel parameter set, livery slots, acquisition method; players consume tracks faster than cars, and a new track usually buys more life than a new car.

Schedule anchor: building one release-quality track and one car from scratch (a vertical slice) usually takes 2–4 months; extrapolate from there as content volume times a polish coefficient. For scope control and the content-cutting order see Indie Survival; a content table benchmarked against big publishers is this genre's number one trap.

## 6. How to Start the First Prototype

The first prototype builds only one greybox test loop plus one car, finished in 2–4 weeks, and touches neither art, career mode nor online.

**Week 1: the car and the loop.** One circular test track: a straight, a fast sweeper, a hairpin, a set of S-bends; a single-rigid-body car with a chase camera; a start-line timer. Ugly is expected at this stage.

**Week 2: tabulate the feel and tune.** Steering falloff, grip, braking, drift and power curves all go into the number table and support hot editing; record frame by frame on the same test track, on the same lap, changing one parameter group at a time.

**Week 3: ghost car and internal testing.** Record your own ghost car as the baseline; find 3–5 people who have never played, run 10 minutes each, and record loss-of-control points, complaints and "one more lap" moments — no hints, no explanations.

**Week 4: three AI tiers and fine-tuning.** The same racing line with three pacing tiers and simple error, running a small race against three AI cars; change only parameters and the track, and add no new systems.

Success criteria (all observable):

- With all art and audio removed, testers still want to keep lapping, usually for 10 minutes or more in a session.
- At least 4 of 5 testers complete 3 laps with no verbal guidance; "this car is broken"-type complaints no more than 1 per person.
- Change any one feel parameter and you can quantify its effect on lap time within 5 minutes.
- Testers can explain their own mistakes as braking, line or throttle; some tester asks for one more lap unprompted rather than being asked to try again.

If the feel does not pass, do not start laying tracks; rework on the foundation is this genre's most expensive bill.

## 7. Common Pitfalls

1. **Laying tracks before the feel is frozen**: tracks built to wrong braking distances and corner speeds all need rework the moment a parameter moves; freeze driving feel first, then mass-produce tracks.
2. **Treating physical correctness as the goal**: real-car physics is often "hard to drive" in a game; players want predictability, not correctness — simulation is a candidate means, not the end.
3. **Selling speed with the gauge alone**: the dial reads high while the screen feels slow; speed sensation is an ensemble of camera, FOV, wind, pitch and scenery scale (§4).
4. **Rubber banding showing its seams**: leads are pulled back and trailing cars are let off, and victory loses credibility; prefer positive reinforcement and declared difficulty (§3.3).
5. **AI that knows one line and never errs**: an AI with no error and no mistakes is a slot car — no overtaking windows, no incidents and no personality.
6. **Tracks with difficulty but no rhythm**: corner after corner with no breathing room, or long straights with nothing to do; a track needs fast-slow alternation and at least one climax corner (§3.2).
7. **Braking points with no visual anchor**: braking points memorized by rote turn a race into a memory test; entry, apex and exit must all be readable.
8. **Shortcuts out of balance**: invisible, useless once learned, or "win only by taking the shortcut"; shortcuts must be visible, learnable and carry a price (§3.2).
9. **Cars copied without differentiation**: recolors and pure-stats cars are a review-bombing hot zone; reuse must carry a feel or role difference; a content table benchmarked against big publishers is likewise the number one trap.
10. **Audio and determinism engineering left for the end**: engine-audio layering and ghost-result reproducibility both need early planning — they cannot be crammed in or recovered at the finish.

## Further Reading

- Game Design Handbook: core loops, number tables and game-feel checklists — the base draft for the tuning discipline in §3 of this page.
- Level Design Handbook: metrics, guidance, pacing and the whitebox workflow — the full expansion of track and corner rhythm.
- Programming Handbook: fixed timestep, determinism, performance budgets and networking engineering in detail.
- Case Studies and Indie Survival: review methods and scope control; use against §5.
- Homework: greybox a track containing "one teaching corner, one exam corner, one variation corner"; pick a racing title you know well and record its braking points and guidance devices over one lap; then play one session each with assists on high and all assists off, and write down the feel differences clearly.

Racing looks like it sells speed, but what it actually sells is the player's trust in the car: once that trust holds, every lap is worth running again.
