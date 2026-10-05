# Ludo Atlas · Genre Handbooks · Fighting

> **Genre Handbooks · Volume 3**. Positioning: the competitive genre where two players, one axis and one set of frame data turn "reading your opponent" into the first pleasure; its content is mainly mechanics that can be taken apart over and over, not levels.
> Companions: Esports & Competitive Design (competitive balance and tournaments) · Multiplayer & Backend (rollback sync and matchmaking) · Game Design Handbook (core loops and balance tables) · Programming Handbook (input and deterministic simulation).
> This page carries no external links; frame counts and durations are common reference ranges — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: fighting is the competitive genre that **makes frame-level mind games its first pleasure**. Two characters take turns holding the "right to act" inside a bounded space; players use moves, positioning and prediction to steal choices out of the opponent's hands. Winning a round is not about clearing the content — it is about reading the other side wide open.

The core loop, written as a ring of verbs:

`read the opponent's habits → probe in neutral → find the opening (a hit, a counter, a guaranteed punish) → convert the combo into damage → reset back to neutral`

This loop is measured in frames: an exchange is often decided within half a second, and inside that half second both sides make several decisions. It also differs from most genres in one fundamental way: content is never consumed. The same stage and the same opponent can be taken apart for ten years.

Form-wise it splits into three branches: 2D fighting (a horizontal axis plus jumps — this page's main line), 3D fighting (sidesteps and staying facing forward) and platform fighters (knockback rules and defending the stage edge); the differences among the three are closed out in §3.2.

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Beat 'em up | The opponents are AI crowds and the core is clearing the screen and positioning; fighting is 1v1, and frame data is the language both sides share |
| Action-adventure (combo-driven) | Combos there are presentation and rhythm; fighting's combos are competitive currency and must enter the balance and resource economy |
| Soulslike and hardcore action | The enemies are designed level content; fighting's "level" is the opponent themselves, impossible to exhaust through design |

A self-check question: swap the opponent from a real person to a scripted AI — how much pleasure is left? If the answer is close to zero, you are making a fighting game: it turns "another player" into irreplaceable content.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **The thrill of reading people**: predictions must be payable in damage immediately; "I know what you're about to do" is the peak.
2. **Losses that make sense**: a loss must be attributable — frames, distance or choice, at least one of the three must balance the books — or players won't want a rematch.
3. **Controllable onboarding**: moves come out, combos connect, and there is somewhere to practise; the path from beginner to "plays decently" is clear.
4. **Rhythm and tension**: a match has its own breathing (probing, bursts, breathers), not two sides each playing their own game.
5. **Character appeal and long-term growth**: picking a character is picking a personality; ranks, combo libraries and the character pool give reasons to keep playing.

Benchmark titles (play them yourself before breaking them down — match videos alone won't teach you game feel):

| Title | What to break down |
| --- | --- |
| Street Fighter II | The archetype of modern fighting: six buttons, motion inputs, and the origin of the neutral and frame-data vocabulary |
| Street Fighter 6 | A contemporary sample of systems and onboarding engineering: the Drive system, Modern controls, and heavy investment in training and single-player content |
| The King of Fighters '98 | One of the most widely played fighting games in Chinese arcades: 3-on-3 and a faster resource rhythm |
| Super Smash Bros. Ultimate | Platform fighting's independent evolution: percent knockback, party rules, and mass accessibility that broke out of the niche |
| Tekken 7 | A complete sample of 3D fighting's frame systems and long-term balance operations |
| Mortal Kombat 11 | The commercially heaviest single-player sample in fighting: story mode and towers, to set against the dilemma in §3.5 |

## 3. Design Essentials

### 3.1 The Frame-Data World: Startup, Active and Recovery

The biggest disciplinary difference between fighting and other action genres is that it turns "time" into a table of numbers. Every move is a timeline: startup first, then active frames, then recovery; victory and defeat hide in the lengths of these three segments and the differences between them.

| Term | Meaning | Design use |
| --- | --- | --- |
| Startup | From the button press to the attack hitbox appearing | Decides who acts first; the faster the startup, the smaller the reward must be |
| Active frames | The window in which the attack hitbox exists | The shorter, the harder to whiff punish; the longer, the more easily it eats a counterattack |
| Recovery | The time after active frames end during which you cannot act | Decides whether the move is safe on block |
| Frame advantage | The difference in the two sides' recovery time after a hit or a block | Positive numbers keep the pressure on; negative numbers enter punish territory |
| Hitstun and blockstun | The time the receiver cannot act | Added to recovery, it produces frame advantage |
| Invincibility frames | A window unaffected by hitboxes | The resource backing for wake-up reversals and supers |
| Hitboxes | Attack box, hurtbox, pushbox | Three sets of collision geometry plus one set of visuals; the gaps between them must be disciplined |

Common reference ranges (in a 60 fps system, one frame is about 16.7 milliseconds): light attacks start up in 3–6 frames, medium attacks in 6–10, heavy attacks in 10–20. Frame advantage on block: near zero is the safe pick, around -4 enters the light-attack punish range, and -10 or lower is basically a guaranteed punish.

Three more notes on hitboxes: hurtboxes are usually slightly larger than the visual outline, because players trust their eyes; an attack box must have a "visible reason" in the presentation, and the longer it is, the slower it has to be; the pushbox decides whether the two fighters stand face to face or pass through each other, and it also affects the camera's and the AI's distance judgments. Visualizing all three box sets is required coursework in the prototype's first week (§4.3).

The combo language is built out of cancels: normals cancel into specials, specials cancel into supers, plus confirms (they only count on hit). Two disciplines for combos: damage needs scaling, to prevent a one-combo kill; presentation length needs a cap (commonly 3–6 seconds). Combos are a means, not the star.

### 3.2 Move Sets and Character Differences: Neutral, Combos and Resources

Each character gets one kit: normals (direction plus attack button), specials (motion or simplified input), supers (consume resources) and throws (another key to beat blocking, with throw teching). During prototyping, 8–12 moves are enough to hold up; in commercial titles a single character's move set (including follow-ups and supers) commonly runs on the order of 20–40 entries.

Resource meters are fighting's economic system. How the super meter fills (landing hits, taking hits, blocking, charging manually) decides the rhythm of attack and defence; the second resource that became mainstream in recent years (defensive resource, escape resource, burst resource) turns "save it or spend it" into a decision every round. Write down three numbers per resource: how fast it builds, where it gets spent, and the value of holding on to it.

Character archetypes are built as a table of "what the character tests in the opponent", not as reskinned numbers:

| Archetype | Playstyle | What it tests in the opponent |
| --- | --- | --- |
| Balanced | Decent answers at every range | The quality of fundamental neutral exchanges |
| Rushdown | Sustained pressure once in close | Blocking the first wave, taking back the right to act |
| Zoner | Managing distance with long limbs and projectiles | Routes through the fire and patience |
| Grappler | High health, a strong throw game | Reading and teching throws; denying reasons to get in close |
| Counter | Baiting the opponent into moving first | Discipline and patience in committing |
| Stance | Stance switches, summons and setups | Recognizing states and choosing the right response |

Neutral is in essence the management of distance and options: divide the stage into far, mid and close ranges, and write down, range by range, what answers the character has and what answers it lacks; where answers are missing is the opening you leave for others. The combo library is listed under four categories: hit-confirm combos, punish combos, resource-burst combos and corner combos — every character needs a slot in each category.

The 3D and platform-fighter differences: with sidesteps added, 3D fighting makes "staying facing forward" a skill in itself, and pressure relies mainly on frame traps and throws; platform fighters use percent knockback and losing a stock at the stage edge, turning "defending the edge" into a second health bar, with a visibly wider barrier to entry and audience.

### 3.3 The Input System: Motions, Buffers and Leniency Windows

Motion inputs are fighting's instrument: quarter circles, half circles, dragon punches, charges and so on are the community's shared language. The input interpreter must be lenient — frustration at moves that won't come out is charged directly to the game.

The leniency checklist (figures are typical reference ranges):

- **Input buffer**: button presses completed within a several-frame window can combine into the motion, commonly 2–8 frames.
- **Direction completion**: diagonal directions can be skipped or auto-completed; keyboard and gamepad are treated alike.
- **Simultaneous-press priority**: the sync window for pressing two buttons together is commonly 1–3 frames; throws and button combinations both benefit from this leniency.
- **Key release counts as input too** (negative edge): some classic moves trigger on release; it adds leniency and misinputs in the same stroke — decide deliberately whether to include it.
- **Input queueing and mash buffering**: inputs during block and hitstun are pre-stored, preventing "I pressed it and nothing happened".

Input display (listing directions and buttons frame by frame) is the industry standard for training mode and the number-one debugging tool during development (§4.3). The modern-controls route (one-button specials plus assisted combos) moves the barrier from execution to decision-making, at the cost of some actions being limited by rewards or cooldowns; whether to do it is a question to answer at greenlight in this generation.

### 3.4 Balance and Tuning Process

Set up the ledgers before talking about game feel: one frame table per character (each move's startup, active frames, recovery, damage, movement, stun and cancel windows), plus a matchup table (character by character, recording win-loss tendencies). Without these two tables, balance discussions degenerate into arguments.

The object of balance is the match, not the numbers: first eliminate matchups lost at the opening, then fix the strength gradient; the goal is not for everyone to be equally strong, but for every character to have its own set of answers. Spend the change budget in order: move level first (frames, hitboxes, damage), then character level (health, resource gains), and system level last — because one system change forces every matchup to be retested.

Data and communication carry equal weight in balance work: win rates, usage rates and high-rank samples are the evidence, and patch notes that spell out what changed and why are trust currency. Patch cadence must be stable, with major changes announced in advance. On testing: rerun high-frequency matchups after every patch and get real playtests with humans; simulation and AI can only screen, they cannot replace human match play.

### 3.5 The Realistic Dilemma of Single-Player Content

An industry-wide problem: single-player content in fighting games is generally weak, and the root cause is where the fun comes from. The core thrill comes from "another human is gambling on your choice", and AI cannot lie: let it read inputs and counter instantly (the classic arcade cheat) and the fun hits zero once players see through it; don't let it read inputs and it is too dumb to feel like an opponent. This dilemma has never been broadly solved.

Common single-player fillers and how they actually hold up:

- **Arcade mode**: a string of AI matches with staging at the head and tail; light on volume — it cannot carry the promise of "single-player content".
- **Story mode**: represented by the Mortal Kombat run, carrying scope with staging and cutscenes at a cost measured in publisher-grade team-months; Street Fighter 6's World Tour is a heavier sample.
- **Combo trials, survival and towers**: low cost, effective for core players, nearly useless for passersby.
- **Training mode and sparring partners**: the audience is people already playing, not people who have not decided to buy yet.

The pragmatic route for small teams: position single-player as "training grounds plus tutorial" and treat online as the main battlefield. Training mode (frame table display, hitbox visualization, opponent recording and playback) must be built to launch-content standards — it serves beginners and veterans at the same time. If you insist on making single-player a selling point, first make a cost comparison table: the budget for one story mode is usually enough to build two or three extra playable characters.

### 3.6 Round Structure and Match Packaging

The standard structure of a match is best of three, with the round going to whoever empties the health bar or leads on health when the timer expires; the reset between rounds makes "whether resources carry over between rounds" an explicit design decision (the 3-on-3 format is another carry-over scheme). Knockdowns and wake-ups are the round's breathing: wake-up options such as invincibility, backward rolls and delayed getup make attacker and defender gamble once more at the wake-up spot. Victory and defeat staging (KO slow motion, victory lines, entrances, supers) is where most of the character-appeal budget goes, and it is also the most reused asset: the same set of animations will be watched across thousands of matches, so it deserves a high standard — but keep it decoupled from frame data; never let staging hide the hitboxes.

## 4. Technical Essentials

### 4.1 Deterministic Simulation and Input Sampling

- Advance the simulation at a fixed step (commonly 60 Hz) and decouple rendering from simulation; all hitboxes and physics run on integer frames only.
- The same input sequence must produce the same result: controlled randomness, no frame-rate dependence, no side effects. Replays, opponent recordings, reconnection and rollback all rest on this foundation.
- Input is sampled per frame: collect an input snapshot each frame, let the interpreter turn leniency windows into "completed motions", and let the simulation consume only the completed results; check the whole input-to-screen chain per frame as well, measuring sampling points, buffering and display latency together.

### 4.2 Rollback Netplay and Local Versus

Fighting's latency tolerance is the lowest of any genre: one exchange is decided within half a second, and delay-based netcode is simply unplayable across regions. The industry consensus is rollback netcode: keep executing locally on prediction, and on receiving remote input roll back to the divergence frame and resimulate; local same-screen two-player play, meanwhile, is the genre's cheapest, best-feeling origin form — prototypes, testing and offline scenes all lean on it. Implementation points:

- The simulation must be replayable: state snapshots, no side effects, the same frame produces the same result (§4.1).
- Predict remote inputs; the rollback window is counted in frames; the worse the network, the more rollback — hide it with view-layer smoothing, no flicker, no jumps.
- Matchmaking, ranks and anti-cheat are the other half of the online game; the full ledger is in Multiplayer & Backend.

### 4.3 Frame-Data Assets and Debug Tooling

- One data asset per move: startup, active frames, recovery, damage, hitboxes, movement, and sound/VFX attachment points; changing values does not touch code, and a patch is a reviewable diff.
- The essential five-piece toolset: frame stepping and pause; real-time hitbox visualization (attack box, hurtbox and pushbox in separate colors); frame-by-frame input display; recording and playback (doubling as sparring partners and test scripts); automatic frame-table export and in-match frame advantage display.
- Put the data under version control and log every adjustment: which table changed, which values, and why. "Two months later nobody can explain why it is the way it is" is the most common chronic disease of projects like this.

### 4.4 Presentation Engineering and Single-Player Sparring

- Hit-feel layering: hit-stop (commonly on the order of a few frames), knockback, hit reactions and sound effects start with three tiers — light, medium, heavy — and climb with damage; effects fire only on key frames, and never hide hitboxes.
- Replay systems are implemented as "store inputs, not results": an input stream plus deterministic simulation is the minimal foundation for recordings, ghosts and spectating; single-player sparring should prefer recorded replays and scripted behaviour, never input-reading cheats (cheating AI is the number-one killer of single-player fun, see §3.5).

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimating scope — not a commitment. The numbers are rulers; calibrate them against your own team's speed.

| Content module | Minimum playable | Comfortable scope | Notes |
| --- | --- | --- | --- |
| Characters | 1 (mirror match) | 4–8 | Differences must change gameplay, not reskins |
| Moves | 8–12 moves | 20–40 actions per character | Including follow-ups and supers; frame tables are the management object |
| Combos | 2–3 | 6–10 per character | Every character needs a slot in all four categories (§3.2) |
| Stages | 1 | 6–12 | With boundaries, music and staging |
| Modes | Local versus | Add online, training, arcade | Training mode built to launch-content standards |
| Staging assets | One set each for victory and defeat | Entrances, victory, supers in full | Highest reuse; deserves a high standard |

Workload anchors (reference values): game-feel prototype (1 character, local versus, greybox) 4–8 weeks; one character's full move set — for 2D, frame-by-frame animation counted in hundreds to over a thousand frames; for 3D, tens to about a hundred actions — commonly measured in months; rollback integration 1–3 months, depending on how clean the deterministic architecture is; each balance patch cycle 1–2 weeks (including testing and patch notes). Project scope extrapolation: a small shippable title (4–6 characters, rollback netplay, training mode) is on the order of 1.5–3 years for one person; today's mainstream commercial fighting games (15–25 characters plus long-term seasons) are publisher-grade teams at 3–5 years plus ongoing live operations. Scope out of control is this genre's number-one cause of death, tied with platformers; for the order of handling see Indie Survival.

## 6. How to Start the First Prototype

Goal: in 6–8 weeks, build a prototype where "two people at the same machine want to play each other again and again". One character (mirrored on both sides), 8–12 moves, all greybox, no online and no single-player.

1. (Weeks 1–2) Body and hitboxes: movement, jump, crouch, plus three normals; hitbox visualization and frame stepping must be finished the same week — without them, every following week is blind tuning.
2. (Weeks 3–4) Defence and exchanges: blocking, hitstun, hit-stop, throws and throw teching; get the feel of the three outcomes — hit, blocked, punished — fully right; sound effects and animation can be placeholder blocks for now, but the frame counts must be real.
3. (Week 5) Specials and combos: two or three specials (including one projectile or dash), building the first hit-confirm combo and the first punish combo; the super meter goes into the system in its first version, even with a single super.
4. (Week 6) Freeze the tables and start playing: get all move data into the frame table and wire up rounds and victory (first to two wins); start finding people to play daily and record three things: the matchup you get stuck in most often, the most infuriating way to lose, and the most satisfying way to win.
5. (Weeks 7–8) Validate the second form: add a second character or a stance variant of the same character, and test whether "one system, two sets of distance answers" holds; if the difference will not come out, the system is not enough — fix the system first, do not add characters.

Success criteria (all observable):

- Two testers can play each other for over 30 minutes straight, and come back on their own initiative — not because they were asked to try again.
- After each round, the loser can name the choice they lost on, even if only half right.
- With all-greybox visuals throughout, the presenter can explain from the frame table why this move is strong and why that move cannot be thrown out carelessly.
- "I pressed it and it didn't come out" complaints stay at no more than 1 per person per round (the leniency-window acceptance check in §3.3).

## 7. Common Pitfalls

1. **Stacking characters before freezing the system**: mass-producing characters before frame tables and hitbox conventions are frozen means reworking all of them when the system changes. Hammer the system out with one character first.
2. **Hitboxes that do not match the visuals**: it looks like a hit but misses, it looks like a clean dodge but gets hit; fighting players will screenshot frame by frame and compile montages — this kind of mismatch is a disaster zone for negative reviews.
3. **Unforgiving input**: moves will not come out and beginners churn at once; leniency windows and input display are floor configuration (§3.3).
4. **Combos and staging too long**: time spent watching animations exceeds time spent playing, and staging eats the match's rhythm; set a presentation-length cap for combos.
5. **Balancing by gut feel**: touching numbers with no frame table or matchup table makes each patch messier than the last; log every change and its reason (§3.4).
6. **Forced single-player content**: passing input-reading AI off as an opponent collapses the moment it is seen through; either position single-player as training and tutorial, or fund it like a publisher (§3.5).
7. **Online started too late**: building networking only months before release — a deterministic simulation cannot afford the rework; write a replayable simulation from day one (§4.2).
8. **Training mode missing**: with no frame table display, hitboxes or recording and playback, the community cannot teach itself and retention breaks; it is standard equipment for this genre, not a bonus.
9. **Scope out of control**: setting the character count by what you want to make rather than what you can finish, and animation costs blow up; 4–6 characters is already the upper-bound magnitude for a small team (§5).
10. **Greenlighting a fighting game as a single-player one**: writing the design document around "a single-player experience", and only mid-development discovering that the main content is another human — target audience and development focus both misaligned.

## Further Reading

- Esports & Competitive Design: competitive balance methodology, tournaments and spectator systems — fighting is its native battlefield.
- Multiplayer & Backend: the complete engineering path for rollback sync, matchmaking and anti-cheat, corresponding to §4.2 of this page.
- Game Design Handbook: the base document for core loops, balance tables and validation methods.
- Programming Handbook: general practice for fixed timesteps, determinism and toolchains.
- Indie Survival: scope control and scheduling, complementary to the magnitude accounting in §5.

Exercise: pick a widely known sample (Street Fighter II, say), copy one character's ten moves into a frame table under "startup, active frames, recovery, frame advantage on block", then run three paper matches against the table with a partner; then build a six-week prototype per §6 and test whether the joy of "reading people" holds up in your hands.

Fighting has only one deciding factor: make players believe that a loss is their own misread, not the game cheating them. Every piece of frame data, every leniency window and all the netcode engineering serve that one thing.
