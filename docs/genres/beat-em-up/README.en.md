# Ludo Atlas · Genre Handbooks · Beat 'em Up

> **Genre Handbooks · Volume 3**. Positioning: the side-scrolling action genre that makes the "one against many" brawl its first pleasure. The player reads positions inside the encirclement, strings combos, breaks out with throws, and clears and advances stretch by stretch.
> Companions: Game Design Handbook (core loops and game-feel checklists) · Programming Handbook (combat hit detection and on-screen performance) · Level Design Handbook (wave choreography and pacing curves) · Indie Survival (scope and scheduling).
> This page carries no external links; cross-references use handbook names and volume numbers. All figures are reference values — go by your own project's measurements and playtests.

---

## 1. Positioning and Core Loop

Beat 'em up (in the arcade era also called the side-scrolling brawler or the screen-clearing game) was standardized by Double Dragon and Final Fight and never left that template: a fixed-camera side-scrolling push forward, enemies entering in groups, the player opening up the encirclement again and again with combos, throws and specials. It shares one move vocabulary with fighting games but solves a different problem: fighting is a two-player duel of frame reads; beat 'em up is one player reading the positioning of a crowd.

In one sentence: beat 'em up is the genre that **makes "one against many" physical brawling its first pleasure**. Winning a one-on-one means nothing; the real assignment is how to carve out space in a crowd and give the fight a sense of rounds.

The core loop, written as a ring of verbs:

`read positions → cut in with combos → launch or throw to open a gap → turn to handle the flank → clear the screen → unlock and advance`

The loop runs on the unit of one exchange, lapping every 10 to 30 seconds. The metronome is scroll lock: walk forward to the trigger point, the camera locks, a wave enters, and it unlocks only when cleared — pressure and breathing are both allocated by the "lock, clear, advance" cycle. It stands on two premises: the crowd-combat structure must be fair (§3.1), and hit feedback must carry real weight (§3.2).

Drawing boundaries with neighboring genres:

| Neighboring genre | Boundary |
| --- | --- |
| Fighting games | Fighting is a 1-v-1 duel of frame data; beat 'em up is one-vs-many spatial management, where difficulty comes from encirclement and flanking, not from reading frames |
| Hack-and-slash (musou) | Musou props up the spectacle with enemy counts, felling a crowd in one swing; beat 'em up keeps three to five enemies on screen, where every exchange demands reading both offense and defense |
| Action RPG | Action RPG stitches progression and loot into combat, and getting stronger comes from stats; the beat 'em up protagonist's strength stays roughly constant for the whole run — what changes is the player's move vocabulary |
| Run-and-gun | Run-and-gun leans on ranged fire and mobility; beat 'em up combat happens at grappling range, where grabs and throws are the core tools |

A self-check question: cut the on-screen enemies down to one — does the game still hold up? If the answer is "yes," you are closer to a fighting game; beat 'em up fun has to grow out of "many."

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Mastery of crowd combat**: threats from every direction are visible, readable and manageable; when you lose, you blame yourself, not that one hit from behind.
2. **Meaty hits**: every hit in a combo carries weight, with all three parts of the feedback trio (§3.2) present.
3. **Forward rhythm**: the beat of lock, clear, advance is crisp and decisive, with pressure rising and falling.
4. **Move expression**: combos, throws and specials form the player's move vocabulary; play long enough and you develop a personal style.
5. **Fighting side by side**: two-player co-op is a native configuration; the chaos and the rapport are the fun itself.

Benchmark titles (play them yourself before breaking them down — the rhythm of crowd combat cannot be learned from video):

| Title | What to learn from it |
| --- | --- |
| Double Dragon (series from 1987) | The starting point of two-player co-op; symmetric move design between player and enemies (enemies can grab and throw too); the tradition of friendly fire it left behind |
| Final Fight (1989) | The industry template for wave clearing and scroll-locked advance; the offense-defense read of grabbing and throwing; role division among enemy grunts |
| Streets of Rage 2 (1992) | The mature form of combos and specials; a boss and soundtrack that stick in memory; the difficulty curve |
| Streets of Rage 4 (2020) | The polish benchmark for modern pixel beat 'em ups: frame-by-frame refinement, combo continuation, difficulty tiers and online play |
| Cadillacs and Dinosaurs (1993) | Picking up and using weapons and firearms; interaction with throwable objects; arcade-grade density and pacing |
| Teenage Mutant Ninja Turtles: Shredder's Revenge (2022) | A modern implementation of online co-op; contemporary polish on a classic template; the engineering scale of pixel art |

## 3. Design Essentials

### 3.1 Crowd Combat Structure: Encirclement, Lock-On and Hit Protection

The core tension of a beat 'em up: the player can only deal damage in one direction at a time, while enemies close in from all sides. More than half the design work is balancing "pressure" against "fairness" — too little pressure and it becomes a mindless mow-down; let fairness fail and it becomes a gang beating. Four tools:

| Tool | How it works | The problem it solves |
| --- | --- | --- |
| Attack quota | Only one or two enemies are allowed to attack at any moment; the rest pace or jockey in surrounding positions | Everyone piling in and combo-ing the player to death; gives offense and defense a sense of rounds |
| Surround slots | Enemies hold a few battle positions around the player (front, flank, rear), yielding and rotating out after attacking | Gives the group fight a choreographed feel; the player can read where the next threat comes from |
| Lock-on behavior | Attacks auto-turn toward the nearest enemy, overridable by the player's input direction; no manual lock-on | The "I can't hit the enemy next to me" frustration; must hit accurately on both keyboard and gamepad |
| Hit protection | After the player takes a hit, 0.3–1 seconds of invincibility plus a white flash (reference); further hits in the window cause only light hitstun and no damage | Being combo'd to death endlessly while surrounded; gives the player a window they can act out of |

Two disciplines:

- Keep the numbers in separate tables: player invincibility (after being hit, on wake-up, during specials) and enemy hitstun are two separate parameter sets — lump them into one value and changing either side hurts the other. Enemy hitstun also has to survive a full combo: shorter than the combo's total length and the opponent strikes back mid-combo, losing all sense of pressure (methods in the Programming Handbook).
- Pressure from behind is allowed, but it needs a tell: enemies circling around should first telegraph with a movement cue or a sound effect — an unannounced stab in the back is a source of bad reviews. Also give the player one or two always-available escape tools (a crowd-clearing special, a dash, or a grab); an encirclement with no escape route does not work.

### 3.2 The Hit-Feel Trio: Hitstop, Screen Shake, Sound Effects

Hit feel is the face of a beat 'em up. Animation and VFX are a matter of budget; what really decides "did I connect, and how hard did it land" are three devices, all synchronized to the active frames:

| Device | How it works | Reference range |
| --- | --- | --- |
| Hitstop | Attacker and defender freeze together for a few frames on contact, longer for heavy hits, longest for specials | 30–100 ms, tiered by move |
| Screen shake | Small camera displacement, direction optionally following the attack direction, graded by damage tier | Minimal on light hits, rising on heavy hits and throws; the amplitude never enough to interfere with reading the move |
| Sound effects | Layered: whiffs cutting air, hits on flesh or metal, critical hits and guard breaks, enemy screams and reaction cries | One sound palette per character; cap the number of concurrent voices |

Three disciplines:

- Tuning order: hitstop and hit reactions first, screen shake and particles after. Reverse the order and it becomes a fireworks show, and the player can't read whether a hit connected.
- Hitstop is part of combo rhythm: a quick jab and a heavy punch get different freeze frames, and that is what gives a combo its light-and-heavy cadence; one value throughout and the game feel goes flat.
- Launch, juggle, knockdown and follow-up hits are the beat 'em up feedback chain: ending a string with a knockdown or a launch asks the player to choose between "safe" and "chasing more hits," and hit feedback grows into a decision.

### 3.3 Wave Design: Advance, Scroll Lock and the Pressure Curve

A level section alternates combat segments and connective segments: connective segments handle walking, pickups and environmental storytelling; combat segments are triggered by scroll-lock points. Advance to the trigger line, the camera locks, enemies enter in batches, and it unlocks when cleared. Build the parameters as a table first:

| Parameter | Reference | Notes |
| --- | --- | --- |
| Enemies per wave | 2–4 | 1–2 at the opening, 2–4 in standard segments, 4–6 in climax segments, entering in batches |
| On-screen cap | 4–6 | Fix it early against target hardware and readability; wave design works within that budget |
| Batches | 1–3 | Staggered arrivals sustain pressure peaks; if one wave clears too fast, the segment feels empty |
| Entry style | Walk-in, jump-in, door-break, from above/below | Rotate entry styles within one scene and repetition drops |
| Enemy-role mix | Basic, disruptor, suppressor, elite | At least two roles per wave; it takes a combination to make a "problem" |

Composition method: treat each wave as a problem to solve. Basic grunts fill space and teach; jumpers force a vertical answer; ranged enemies force the player to fix position first; elites soak damage and set the tempo. Give a new enemy type two solo appearances before it enters mixed waves.

There are four intensity knobs: count, role mix, terrain (narrow alleys, bridge decks, elevators), and scene props and throwables. Turn only the count knob and what you get is boring enemy piles. Pacing curve: a level section holds 3 to 5 combat segments with connective segments to breathe in between; the climax gets high-density crowd combat or a boss, with an empty stretch before the boss. Intensity cannot rise monotonically — it needs its dips, so the player has the spare attention to actually use their moves.

### 3.4 The Move Skeleton: Combos, Throws and Specials

The player's move vocabulary is organized in three layers (reference controls: start with three buttons — attack, jump, special; grabs are contact-triggered or on their own button):

| Layer | Content | Design points |
| --- | --- | --- |
| Combos | 3–4-hit normal attacks, ending in a knockdown (safe) or a launch (continuation) | Combo windows and cancel rules go into the data table, shared by animation and logic |
| Grabs and throws | Grab a mook, hit twice, throw them; the thrown body can hit a third character | The genre's signature tool: damage, escape and crowd control in one |
| Specials and escapes | A one-button move that knocks back or knocks down nearby enemies | Usually carries a cost (startup, a resource, or a bit of health), turning "should I use it" into a decision |

Character differences live on three axes: speed, range, power — plus one signature move. Differences must be felt, but characters share the same skeleton, or every character equals a level's worth of content scope. Whether to include defense is a matter of direction: classic titles mostly have no dedicated block button, substituting positioning, grabs and escape moves; adding defense significantly changes the shape of gang-up pressure, so think it through before building it.

### 3.5 Two-Player Co-op: Classic Gameplay and Modern Implementations

Two-player local play is this genre's native product form: Double Dragon made "two people fighting together" the selling point — shared camera, shared scroll lock, shared chaos. The classic parts still apply today:

- Shared camera: neither player can leave the screen; handle stragglers with edge constraints, catch-up speed, or a brief invincible sprint back in — never let one player get dragged along.
- Friendly fire: the friendly-fire tradition left by Double Dragon creates laughs and friction alike; modern titles usually have it off by default, or as an option.
- Enemy scaling: with two players, raise wave counts and the on-screen cap (reference: by 30% to 100%) so both players have a fight; copy the single-player curve over and it becomes kill-stealing or one player watching the show.
- Death and revival: after going down, wait for a rescue or respawn by life count; the run fails only when both players are down; the invincibility on revival must last through a melee.

Modern implementations split two ways:

- Local shared screen: the least engineering and the steadiest experience, still the first choice; just make the handling of two input devices and the UI split clean.
- Online co-op: the heavy lifting is not gameplay but sync, latency, reconnection and matchmaking, with a testing cost far above local; when the budget is short, platform features in the remote-play-together vein can cover part of the remote two-player need at low cost. Whichever path you choose, test two-player separately: single-player balance data does not hold in a two-player session — pacing, pressure and the sense of purpose are a different ledger.

## 4. Technical Essentials

The engineering difficulty concentrates in four systems: combat hit detection, crowd-combat AI, on-screen performance, and game-feel infrastructure. The following is engine-agnostic; it names concepts and structures.

**Combat hit detection**

- Melee attacks are built as "hitboxes attached to active frames": startup, active frames, recovery and hitbox shape all go into a data table, and active frames are visualized in debug tools.
- One attack resolves at most one hit against the same target: keep a list of already-hit targets; multi-hit attacks are split into a segment list configured separately.
- Throws are implemented as a state binding: once the grab lands, both parties enter the same state machine, and the struggle timer, throw direction and damage when slamming into a third character are all routed from here; throws are the worst offender for detection and visuals disagreeing, so test them separately.
- Hit results come in three tiers: light hitstun (mid-combo), launch (combo ender), knockdown (can be hit on the ground, invincible on wake-up). Who interrupts whom and which states can be grabbed go into an explicit table — not scattered across code branches.

**Crowd-combat AI**

- A three-layer structure: the behavior layer runs each enemy's state machine (approach, surround, attack, hit, down, escape); the director layer runs attack quotas, slot assignment and pressure pacing; the data layer holds per-enemy-type parameters (speed, aggression, hitstun).
- Surround and separate: assign enemies target points around the player and separate them from one another so they don't pile into a blob; enemies that have attacked yield their slot and queue up at the back.
- Off-screen rules: enemies outside the frame make no attack decisions, or must first move into frame; ranged enemies announce their entrance with a sound or visual cue — no attacks without warning.
- Make slots, quotas and states into a visual debug layer: most AI problems can't be tuned because you can't see them.

**On-screen performance**

- Stress-test the on-screen cap before fixing it (against target hardware); design waves and effects within the budget instead of cutting after the fact.
- Object pools cover enemies, effects, damage numbers and throwables; pixel animation goes through atlases and batching, with material switches kept in check; cap audio concurrency and set priorities — hit sounds above ambience — or a melee turns into mush (see the Programming Handbook).

**Game-feel infrastructure**

- Input buffering, combo windows and a fixed step: the next chain pressed before recovery ends must be remembered and consumed; window values go into the data table, one config shared by animation and logic. Time launches, knockdowns and hit protection on a fixed step (commonly 60Hz) so they stay reproducible and tunable inside a melee.
- Script the levels as data: describe waves and scroll locks in script files — spawn timing, positions, enemy types and conditions — so non-programmers can tune levels.

## 5. Content Volume and Workload Reference

First, memorize one multiplier law — it is also this genre's biggest content-scope trap: cost multiplies. Enemy types × level segments × encounter combinations — every enemy must be validated in every level segment (terrain, encirclement, throwables, combinations with other enemy types); multiply again by playable characters, since each character needs balance redone against all enemies and levels. Bosses multiply on their own layer: the move, scripting and staging tuning for one boss usually equals 3 to 5 ordinary enemies. Animation scale (reference): one ordinary enemy's move set (idle, walk, two or three attacks, hit, launch, knockdown, wake-up, grabbed, death, special behavior) usually runs 15 to 25 sets; playable characters more, usually 25 to 35 including combos, specials and throws. When pixel animation is hand-drawn frame by frame, these numbers convert directly into person-months.

| Project shape | Enemy types | Level scale | Timeline scale | Notes |
| --- | --- | --- | --- | --- |
| Crowd-combat prototype | 2 types | 1 single-screen room | 2–4 weeks | Validates crowd-combat structure and hit feel only |
| First title / small complete game | 6–10 types (with variants) | 6–8 levels | 6–12 months | 3–4 themes; fill density with enemy variants |
| Typical indie title | 10–20 types | 8–12 levels | 1–2 years | Multiple playable characters and online co-op each eat a large budget block |
| Commercial scale | 20+ types | 12+ levels | 2+ years | Release content in stages |

The realistic cut for small teams:

- **Make enemy variants, not new species**: swap the weapon, change body type and speed, add one core behavior — that's a new enemy; save new skeletons for signature enemies and bosses.
- **Keep level themes to 3–5**: create variety through layout and wave configuration, not a never-ending stream of new art.
- **Start with 1–2 playable characters**: a second character costs roughly "one character's animation and balance bill × all levels" — do that math before adding anyone.
- **Cut four things from a first game**: online co-op, branching routes, multiple endings, character progression systems — any one of them can eat several more months.

Scheduling anchors: a crowd-combat game-feel prototype, 2–4 weeks; a vertical slice where "one level is at release quality," usually 2–4 months; extrapolate from there as content scope × a polish coefficient. The big budget lines in this genre are enemy animation, level art, and polish time.

## 6. How to Start the First Prototype

The first prototype is one single-screen room: one playable character, two enemy types (one basic plus one flanker), one scroll-locked clear. No art, story, saves or menus — 2–4 weeks.

**Week 1: combos and knockdowns.** A three-hit normal combo, knockback, hitstun, knockdown and wake-up invincibility; stand up the active-frame visualization and data tables first. It is supposed to look ugly at this stage.

**Week 2: crowd-combat structure.** Three surrounding slots, attack quotas (at most one or two attackers at a time), hit protection and the scroll-lock flow (unlock only when cleared). Do not add a third enemy type until this step passes.

**Week 3: the hit-feel trio.** Hitstop, screen shake, layered sound effects (placeholder assets are fine). Record a clip after each device goes in for comparison, with every parameter hot-reloadable.

**Week 4: one playtest.** Find 3 to 5 people who haven't played it — one single-player pass, one two-player pass — and record reactions when flanked, how often combos get interrupted, and how long after clearing before they move on. No hints, no explanations.

Success criteria (all observable):

- With grey-box art and placeholder audio, playtesters still want to replay the same wave for more than 10 minutes.
- When they get hit or die, testers can name the reason themselves (they got flanked, they got greedy, they got up too slowly) — not "I just died for no reason."
- In the two-player test, both players always have something to do; after a wipe, someone asks to go again unprompted.
- Change one game-feel parameter (hitstop frames or invincibility duration) and you can see the difference in the running game within 5 minutes.

If crowd-combat structure and hit feel don't pass acceptance, do not start spreading content: rework on the foundation multiplies across all levels and enemies (§5).

## 7. Common Pitfalls

1. **Crowd-combat rules break down**: everyone piles in at once, or off-screen enemies attack without warning, until the player is beaten into helplessness; attack quotas and rear-threat tells — neither can be skipped (§3.1).
2. **Hit feel as animation only**: no hitstop and no screen shake, and combos look like a slideshow (§3.2).
3. **Invincibility frames and hit protection lumped into one value**: too few and the player gets combo'd to death, too many and hits stop hurting; keep player invincibility and enemy hitstun in separate tables.
4. **Detection that disagrees with visuals**: attack boxes much longer or shorter than what's drawn, and players can't read the distance; make detection follow the visuals, and keep the generosity on the detection side.
5. **Turning only the count knob for waves**: six of the same enemy is worse than three types at two each; pressure has to come from role combinations (§3.3).
6. **Two-player treated as single-player plus one**: enemy counts don't scale with player count, so two players either fight over kills or one watches; co-op needs its own curve and its own tests (§3.5).
7. **Estimating content linearly**: enemies × levels × combinations × characters (§5) — overruns usually hide in the multiplication signs.
8. **Balancing single-player only**: never testing two-player before launch leaves pacing and difficulty as blind spots.
9. **First-game scope overload**: four-player online, branching, progression systems all at once, and none of them gets finished; a beat 'em up's completeness lives in the polish, and cutting scope is the only answer (see Indie Survival).

## Further Reading

- Game Design Handbook: core loops, game-feel checklists and number-table methods — the draft under §3.
- Programming Handbook: methodology for combat hit detection, AI structures and on-screen performance.
- Level Design Handbook: wave choreography, pacing curves and the whitebox flow — complementary to §3.3.
- Case Studies: postmortems of classic and indie beat 'em ups; use them as reference when breaking down titles.
- Indie Survival: scope control and scheduling discipline — complements §5.
- Pitfalls & Anti-patterns: pitfalls in action design and content production; cross-read with §7.
