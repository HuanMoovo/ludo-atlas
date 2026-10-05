# Ludo Atlas · Genre Handbooks · Shmup

> **Genre Handbooks · Volume 2**. Positioning: the arcade shooting genre whose first pleasure is "threading through bullet patterns". Players steer a single small hitbox, reading the gaps in an ever-densifying stream of bullets and passing through them, trading dodging precision for score and resources.
> Companions: Game Design Handbook (core loops and risk-reward) · Programming Handbook (object pools and on-screen performance) · Level Design Handbook (pacing and intensity curves) · Case Studies (breakdown methods).
> This page carries no external links; cross-references use handbook names and volume numbers, and all figures here are reference values — calibrate them against measurements and playtests in your own project.

---

## 1. Positioning and Core Loop

Shmup (known as STG in arcade circles) evolved from the fixed shooter (the Space Invaders and Galaxian branch) and went further in three directions: bullet patterns grew from a few scattered shots into full-screen patterns; the player hitbox shrank from the size of the ship down to a single point; and the center of gameplay shifted from "clear the enemies first" to "read the bullets first". Once the number of bullets rose by an order of magnitude, player attention moved from aiming to positioning — and only then did the genre gain a gameplay identity of its own.

In one line: **shmup is the genre of "reading patterns and threading gaps"**. The bullets are patterns written by the designer, and the player finds a way to live inside them; damage output is mostly automatic or semi-automatic, and positioning precision is the real skill divide. The core loop, written as a verb chain:

`read the bullets → find the gap → micro-move through → shoot and collect score → pressure escalates → read again`

This loop turns in seconds: a threading window is often under half a second, and one mistake costs one life. It holds on just two preconditions: the hitbox must be small (§3.2), and the gaps must have a solution (§3.1).

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Fixed shooter | Enemies advance in formation as a whole and bullet patterns are simple; the shmup makes the bullet patterns themselves the source of difficulty |
| Twin-stick shooter | Movement and aiming are separate, and facing can change freely; in a shmup the ship's facing is fixed and firepower always points forward |
| Run-and-gun | Has jumping, platforms and terrain; the shmup dodges in two dimensions within a continuously scrolling airspace |
| Survivors-like | Attacks are fully automatic and pressure comes from the physical density of enemies; shmup pressure comes from bullet patterns and demands precise pattern reading |

A self-check question: drop the bullet density to zero — does the game still hold up? If the answer is "no", what you are making is a shmup.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **The thrill of reading**: turning a screenful of chaos into a rule-governed pattern; the moment you see through it, panic becomes order.
2. **Within a hair's breadth**: the hitbox is often smaller than the bullets, and skimming past shots holds danger and safety at once — a thrill unique to this genre.
3. **A sense of control**: every death has a cause the player can name (missed a read here, got greedy for a shot there) — when they lose, they blame themselves.
4. **Betting on score**: score is the product of kills, grazing, chains and no-miss runs, pushing players to actively flirt with danger for gain.
5. **Short runs, instant restarts**: a run lasts 15–30 minutes, and going from failure to a fresh run takes seconds; retrying is itself the gameplay.

Benchmark titles (play first, read later; the experience of reading bullet patterns cannot be learned from video alone):

| Title | What to learn from it |
| --- | --- |
| Raiden | The basic vertical-scrolling skeleton, the red/blue weapon trade-off, the coupling of pickups and level design |
| DoDonPachi | The density ceiling of bullet hell, bee-item chains, scoring structures |
| Ikaruga | Polarity absorption: turning "eating bullets" into a resource, with dodging and damage coming from the same source |
| Touhou Project series | The standard formula of a small hitbox plus grazing, the performative quality of bullet patterns, community and difficulty layering |
| Strikers 1945 | Short, fast, tight level structure, looping difficulty and high-score routes |

## 3. Design Essentials

### 3.1 Bullet-Pattern Design Language: Density, Gaps and Reading Paths

Bullet-pattern design is not about piling up numbers — it is about writing patterns: with the same bullet count, arranging a readable pattern is design, and scattering at random is bullying. Start with the density tiers:

| Tier | On-screen bullets (reference) | Where it appears | Design requirement |
| --- | --- | --- | --- |
| Sparse | 10–60 | Openings and popcorn sections | Teach the player how the current bullet type moves |
| Medium | 60–200 | Mid-level | Positioning pressure appears, with margin left for one mistake |
| Dense | 200–600 | Boss climax sections | Patterns stay clear and readable; gaps exist and form a system |
| Extreme | 600–1000 | The peak of bullet-hell titles | Demands full-pipeline dedicated optimization; attempt only if you can afford it |

Density is only the entry ticket: high density with readable patterns is the thrill, high density with scrambled patterns drives players away. The gap is the real mechanism: with no gap the pattern has no solution, and a gap that cannot be read may as well not exist. Three rules of thumb:

- A comfortable gap width is at least 3 times the hitbox diameter; high-pressure gaps narrow to around 1.5 times that (reference), but a safe path must always remain.
- Leave a transit window between consecutive gaps, commonly 0.5–1 second (reference); with too little window, players are not unwilling to dodge — it is physically impossible.
- Patterns need symmetry and periodicity so players can predict the next cycle within two or three cycles; the moment a prediction lands is the payoff.

**Reading path.** Manage the player's attention in chronological order:

| Layer | Content | Practice |
| --- | --- | --- |
| Telegraph | Laser sight lines, the boss's wind-up animation, sound effects | Signal before firing, giving a reaction window of 0.5 seconds or more |
| The threat itself | Bullets, lasers, charging enemies | High contrast with a bright core; moving bullets take top priority |
| Background | Scenery and decoration | Desaturate, darken, strip detail; never clash with bullet colors |

**Color contrast.** Half of a full-screen pattern's readability lies in the palette:

- Enemy bullets use a unified warm palette (red, orange, purple), while player shots use cool colors or white, so "whose shots are whose" is clear at a glance; distinguish speed by shade within the same hue and bullet type by shape — never rely on hue alone, for the sake of players with color vision differences.
- Enemy bullets carry a bright core or outline; the brightest values on screen are reserved for the bullets.

### 3.2 Hit Detection and Grazing: A Small Hitbox and Risk-Reward

**The hitbox.** The player ship consists of two layers: the visual ship (large) and the hitbox (small).

| Element | Common size (reference) | Notes |
| --- | --- | --- |
| Player ship visual | 24–64 pixels | Looks good and reads clearly; takes no part in damage detection |
| Hitbox | 2–4 pixel radius | The circle that actually takes hits; visualized while the slow-move key is held |
| Graze circle | Several times the hitbox | The near-miss detection radius; each graze is counted once |

One hard line: the hitbox must be clearly smaller than the visual and must be visualized; "it looked like a miss but I died" can never happen once, while "it looked like a hit but nothing happened" is the pleasant surprise.

**Slow move and grazing.** Holding the slow-move key (focus) drops movement speed to about half and displays the hitbox, which is how fine positioning is done; a bullet passing close by the hitbox counts as one graze — the most elegant risk-reward device in the genre. Two design axes: reward (converting to score, charge, a counting sound) and intensity (tuned to "willing to take risks, but never daring to graze the whole run", calibrated with side-by-side playtests).

**Getting hit and protection.** After being hit, the player enters brief invincibility (commonly 1–3 seconds, reference) while bullets are cleared fully or locally; a life is lost and firepower may roll back. The protection window is time for the player to re-read the pattern, not a window for piling on extra punishment.

### 3.3 Level Pacing and Boss Bullet Patterns

**Level skeleton.** An arcade-style single level commonly runs 3–6 minutes (reference), in three stages: the opening lays out popcorn enemies and teaches the level's new bullet type or enemy behavior; the middle section escalates pressure with mixed formations, interspersed with item carriers (score or firepower); a boss fight closes it out, commonly 60–150 seconds long (reference). One discipline: introduce only one or two new bullet types or enemy behaviors per level — precise placement beats dense placement.

**Multi-phase bosses.** The boss skeleton is "segmented health bars plus pattern switching":

| Phase | Design content |
| --- | --- |
| Each health segment | One primary bullet pattern plus one or two secondary patterns; each pattern needs its own distinct identity |
| Phase transition | A full-screen bullet clear plus a short cutscene beat plus a brief non-attacking window, giving the player time to breathe and reposition |
| Final segment | Bullet intensity and presentation peak at the same time — the memory point left with the player |

Not clearing bullets during a phase transition is the cheapest source of unsolvable situations: the old pattern has not left, the new one has already arrived, and the overlapping instant kills the player who just emptied a health bar — maximum rage, guaranteed.

**The bullet-pattern library.** Do not hardcode patterns into bosses; build a reusable, parameterized pattern library instead:

- Each pattern records "bullet type, count, angle, speed, interval, rotation, duration"; changing the parameters of one pattern yields a new difficulty variant. Prepare 6–12 patterns per boss (reference), rotated by health-bar or timeline index; 2–4 patterns are enough for a mid-sized enemy.
- Tag patterns by their solution: circling, hugging the edge, threading gaps, predictive movement; a whole set that tests only one ability becomes dull. Change speed and density for the second loop, and the same batch of patterns combines into replay value.

### 3.4 Arcade Structure: Score, Lives, Continues

The genre's meta-structure inherits from arcade coin-op economics; the three-piece set must be designed together:

| System | Common configuration (reference) | Design intent |
| --- | --- | --- |
| Score | Kill points plus item points plus graze points plus a chain multiplier | Gives skill a comparable yardstick; score-chasing is a long-term motive |
| Lives | 2–3 to start, plus 2–3 bombs | Puts a buffer layer between "one mistake" and "run over" |
| Continue | Revive in place, with score marked or zeroed | The arcade is a spending gateway; home versions must keep continues from diluting the sense of achievement |

The score structure is the key point: a score that counts kills only has no expressive power. Four useful multipliers: chains (rapid consecutive kills without breaking the chain), graze count, no-miss section bonuses and item collection rate. Stack the four and the score gap on the same level stops being "a few more kills" and becomes "a completely different way of playing" — only then do leaderboards mean anything. 1CC (clearing on one credit) is the genre's cultural anchor: reaching the end without continuing is the player's final statement about their own skill.

## 4. Technical Essentials

### 4.1 On-Screen Counts and Bullet Object Pools

Set the bullet budget first, then set the content volume:

| Scenario | On-screen bullets (reference) | Engineering note |
| --- | --- | --- |
| Popcorn waves | 10–60 | An ordinary pool covers it |
| Mid-section pressure | 60–200 | Positioning and prediction required; collision starts to eat performance |
| Boss climax sections | 200–600 | The peak scenario; frame-accurate updates; the priority optimization target |
| Extreme titles | 600+ | Attempt only after full-pipeline dedicated optimization; on mobile, halve the peak first |

- **Pool everything, keep memory compact**: pre-allocate enemy bullets, player shots and items uniformly and pre-warm the pools to peak load, and forbid runtime creation and destruction (GC spikes destroy game feel outright); store bullets contiguously in struct-of-arrays form and iterate in order, removing via swap-delete or a unified end-of-frame reclaim; write the pool-overflow policy (refuse to fire, grow, degrade) into the design document.
- **Only pair up the collisions that matter**: player-versus-enemy-bullets is a one-way "one point against N shots" check; player shots against enemies go through a spatial grid for coarse filtering; bullet-versus-bullet is never tested.
- **Fixed timestep and render batching**: bullet updates and hit detection run on a fixed timestep (commonly 60 Hz) decoupled from rendering, and fast bullets use swept checks to prevent tunneling; bullets share an atlas and material, drawn batched or instanced, with updates halted off-screen.

### 4.2 Data-Driven Bullet Patterns and Tooling

- Parameterize emitters: bullet type, count, angle, speed, interval, rotation and acceleration all go into data tables; describe patterns as event sequences of "wait time plus emitter call", stored as table files or JSON.
- A bullet-pattern editor is worth building early, even in its simplest form: frame stepping, slow motion, hitbox overlay and hot-reloading of patterns. Debugging patterns without a preview tool multiplies the cost.
- Pattern-library reuse: tag patterns and put them into the library, and have bosses assemble from it; for the second loop and higher difficulties, change parameters directly, and the same assets combine into replay value.

### 4.3 Hit Detection Implementation, Replays and Saves

- The hitbox is a circle of 2–4 pixels radius (reference), fully separate from the visual, and the slow-move key draws it; grazing uses a larger detection radius for near-miss checks, counted once per bullet, wired to score and sound.
- Run the hit flow as a state machine: hit detected, life deducted, invincibility frames, bullet clear, firepower rollback (optional), re-enter combat; get the order wrong by one step and the player dies the instant they revive.
- Replays and leaderboards: with a fixed timestep and deterministic logic, the input sequence is the complete replay (small, verifiable and a foundation for anti-cheat); you can skip building it at first, but leave room for determinism in the architecture. Saves store only the high score, the 1CC mark and unlocks.

## 5. Content Volume and Workload Reference

The following are common magnitudes for projects of this kind, for estimation only; not a commitment.

| Project form | Content volume | Time reference | Notes |
| --- | --- | --- | --- |
| Prototype | 1 level plus 1 three-phase boss, 3–5 bullet types | 2–4 weeks | Zero art; whitebox bullet patterns |
| Small complete title | 3–5 levels, 1 boss each, 2–3 player ships | 3–6 months | Solo, vertical pixel art |
| Arcade-grade title | 5–6 levels plus multiple loops and branching routes | 1–2 years | Bullet-pattern debugging dominates |

Sub-item reference (solo): bullet-pattern editor 2–4 weeks (a one-time investment); a single boss 1–3 weeks (design, implementation and balancing of 6–12 patterns); bullet and enemy art is small in size and mass-producible by one person (8–24 bullet types, 10–30 enemy types); balancing and tuning run throughout, with 1CC clear rate and score distribution as acceptance metrics.

A scope warning: the content volume of this genre looks light, but between "beatable" and "fun" lies bullet-pattern debugging, and twenty revisions for one boss is normal. When scheduling, budget 2–3 times the implementation time for debugging.

## 6. How to Start the First Prototype

Goal: build the minimal loop of "1 level plus 1 boss" in 1–2 weeks, validating whether pattern reading and gap threading hold up.

1. (Half a day) Player ship: normal-speed movement, the slow-move key, hitbox display (2–4 pixel radius, with the visual far larger than the hitbox).
2. (One and a half days) Get the bullet object pool, straight-shot emitter, hit detection and graze counting working, then assemble fan, ring and spiral patterns from parameter tables.
3. (One day) A three-phase boss: one primary pattern per phase, with a full-screen bullet clear plus a cutscene beat on each phase change.
4. (Half a day) Death, lives, invincibility frames, bullet clear, score tallying and fast restart.
5. (One day) Tune three sets of numbers: movement speed, hitbox size and gap width, aiming for the threshold where it is "scary but not lethal".
6. (One day) Playtest acceptance: bring in 3–5 strangers, give no hints and no explanations, and record the causes of death.

Acceptance criteria (all observable):

- Testers can state the cause of every death, rather than "I just died for no reason".
- Zero complaints of "it missed me but I died".
- At least half the testers ask for another run on their own.

If any of the three falls short, do not lay down a second level yet: pattern readability and hitbox forgiveness are the foundation, and rework is the most expensive thing there is.

## 7. Common Pitfalls

1. **Hit detection disagreeing with visuals**: it looked like a miss, but you died. The hitbox must be clearly smaller than the ship and visualized — this is the number one source of bad reviews in the genre.
2. **Unsolvable patterns or unreadable gaps**: the pattern closes into a dead end, or a solution exists that nobody can see. Before release, run a hands-on slow-motion pass over every bullet section.
3. **Background clashing with bullet colors**: desaturate and darken the background, and reserve the brightest parts of the frame for the bullets.
4. **Difficulty from speed and volume alone**: new bullet types, new combinations and new solutions are the backbone of a difficulty curve; endlessly raising density just hits the ceiling early.
5. **Bullets not pooled**: runtime creation and destruction and GC spikes ruin game feel; pool first, then expand content volume.
6. **Phase transitions that do not clear bullets**: old and new patterns overlap into an unsolvable instant — a cheap yet lethal source of rage.
7. **Input latency out of control**: this genre's latency budget is commonly 1–2 frames; lengthen the chain and players feel the controls "sticking".
8. **Dying the instant you revive**: invincibility frames, bullet clear and repositioning not done together, so one death costs three lives in a row.
9. **A single-axis score structure**: kill points alone have no expressive power; back it with the four multipliers of chains, grazing, no-miss runs and collection rate.
10. **Continues handled poorly**: after a continue everything carries on as before and the 1CC yardstick breaks; continues must be marked or zeroed.
11. **Graze rewards out of balance**: too high and everyone hugs bullets, too low and nobody bothers — both are failures; tune with a risk-reward table.
12. **Bullet patterns hardcoded**: changing one angle means a recompile and debugging efficiency goes to zero; data-driven design plus a preview tool is the baseline configuration.

## Further Reading

- Game Design Handbook: general methods for core loops, risk-reward and score systems.
- Level Design Handbook: pacing and intensity curves — the counterpart to this page's level skeleton and boss pacing.
- Programming Handbook: object pools, collision and performance engineering — the full expansion of §4.
- Case Studies: breakdown and retrospective methods for classic shooting games.
- Exercise: clear any one level of Raiden and of Ikaruga, noting "which stretch was the most panic-inducing, whether you died while panicking, and who you blamed when you died"; then build the minimal loop from §6, tabulate the causes of death by category, revise the patterns three times and look at the table again.
