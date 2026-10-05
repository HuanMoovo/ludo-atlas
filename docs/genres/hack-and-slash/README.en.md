# Ludo Atlas · Genre Handbooks · Hack and Slash

> **Genre Handbooks · Volume 4**. Positioning: the battlefield action genre that makes the "one against a hundred" sweep its first pleasure. Players take the role of officers with off-the-scale combat power, carving a path through full army formations — felling a swath with every attack while pushing one battlefield objective after another forward.
> Companions: Game Design Handbook (core loops and game-feel checklists) · Programming Handbook (combat hit detection and on-screen performance) · Level Design Handbook (battlefield objectives and pacing choreography) · Indie Survival (scope and scheduling).
> This page carries no external links; cross-references use handbook names and volume numbers. All figures are reference values — go by your own project's measurements and playtests.

---

## 1. Positioning and Core Loop

Hack and slash (musou) takes as its prototype the form opened up by Dynasty Warriors in 2000: third-person melee, with the player the only high-power individual on the battlefield and the opponents full army formations; fight one battle, mow a route of mooks, defeat enemy officers, complete a few battlefield objectives. In broader usage the English genre name refers to melee slaughter generally (including the gear-farming hack-and-slash line); this page develops the mainstream Chinese-community sense of "musou".

In one line: hack and slash is the battlefield action genre that **makes the overwhelming power of "one against a hundred" its first pleasure**. Duels are meaningless — who is stronger is settled the moment you enter the field; what players want to see is how wide a furrow their moves plow through a crowd.

The core loop, written as a ring of verbs:

`enter the field → advance along objectives → mow a path → defeat enemy officers or capture strongholds → the battle shifts (morale and reinforcements) → finish the battle → settle results and strengthen → the next battle`

This loop runs on the unit of one battle, lapping every ten to thirty minutes; the mowing inside a battle runs on the unit of seconds, and the feedback of felling a swath with one swing has to hold at that scale. It stands on two premises: the thrill must be disproportionate (§3.1), and the battlefield must have a skeleton (§3.2). Mowing with no battlefield gets old in ten minutes; a battlefield with no mowing turns back into a strategy game.

Drawing boundaries against neighboring genres:

| Neighboring genre | Boundary |
| --- | --- |
| Beat 'em up | Beat 'em up keeps three to five enemies on screen and demands reading offense and defense in every exchange; hack and slash props up the spectacle with enemy counts, felling a swath in one swing, with pressure coming from battlefield objectives rather than a single brawl |
| Action RPG | Action RPG stitches progression and loot into every fight, and getting stronger follows a stat curve; the hack-and-slash character's strength is overwhelming within a battle, and progression exists to amplify mowing efficiency, not to clear stages |
| Bullet heaven | In bullet heaven attacks happen automatically and the player only handles positioning and build; in hack and slash every swing is made by the player's own hand, and direction, moves and camera staging are all expression |
| Action-adventure (character action) | Character action's assignment is landing combos on a single strong enemy, testing the precision of the payoff; hack and slash's combo target is a crowd, testing coverage and rhythm |

A self-check question: cut the on-screen enemies down to single digits — does the game still hold up? If the answer is "yes," you are closer to a beat 'em up or character action; the thrill of musou has to grow out of "many", and it needs a battlefield to house that "many".

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Overwhelming thrill**: one attack fells a swath, with launches, chain collisions, dust and numbers all landing in sync; the player feels "strong" first and understands "why" second.
2. **A sense of battlefield advance**: objectives, morale and the state of the battle change mid-fight, and the player always knows "where to go now, and why". Mowing needs a direction and cannot be farming in place.
3. **Progression that pays off**: the gains from levels, weapons and skills must be felt in the body (the same combo, a shorter time-to-kill, a wider clear radius), not just a number popping up.
4. **Spectacle and a low floor**: musou attacks, executions and enemy-officer entrances are all staged events, and every battle needs one or two screenshot-worthy moments; mashing alone produces a decent combo, with the depth hidden in branches and cancels — beginners can win, and experts win more beautifully.

Benchmark titles (play them yourself before breaking them down — mowing game feel and battlefield pacing cannot be learned from video):

| Title | What to learn from it |
| --- | --- |
| Dynasty Warriors (series from 2000) | The genre prototype: the move matrix of characters and weapons, battlefield objectives (defeat, capture, escort) and the morale bar |
| Samurai Warriors (series) | Character differentiation after the same framework changes subject matter; the marriage of move personality and narrative staging |
| One Piece: Pirate Warriors (series) | How anime tie-ins are done: iconic scenes and moves reproduced from the source, with mowing cashing in "source-grade combat power" |
| Hyrule Warriors: Age of Calamity | The modern polish standard for licensed tie-ins: balance among on-screen counts, move richness and staging scale |
| Fire Emblem Warriors: Three Hopes | Another line of thought for translating a tactics game's class and faction frameworks onto the battlefield |

## 3. Design Essentials

### 3.1 The Thrill Formula: Launches, Counts, Combo Numbers

Mowing's thrill is not an adjective but an arithmetic that can be balanced:

`thrill ≈ enemies felled per attack × launch quality × feedback density ÷ input cost`

The meaning and the practice behind the four factors:

| Factor | How to do it | Reference magnitude |
| --- | --- | --- |
| Enemies felled | Detection must match the blade arc: normal attacks cover a fan, charged attacks and musou cover the full circle; lay out enemy density as "one squad, one patch" — never stretch it into a skirmish line | One normal attack hits three to five; charged attacks and musou reach into double digits |
| Launch quality | A hit means large displacement, and the bodies sent flying knock over allies to form chains; landing dust and a muffled thud supply the weight | Tune mook launch velocity to "two or three body-lengths of flight"; enemy officers only step back half a pace and never go down |
| Feedback density | Combo numbers, kill counts, the musou gauge and sound effects all fire on the same frame, in layers; numbers must pop, not huddle in a corner of the screen | Combos accumulate per enemy hit; after a clear, give a results close-up |
| Input cost | Mashing produces combos, while branches and cancels are left for advanced play; the core thrill is never hidden in a command list | Start with one attack button plus one charge button |

Three disciplines:

- Detection follows the blade arc, with the generosity kept on the player's side: wherever the blade arc passes, detection should connect — better too many than too few; "swept through a crowd and nobody fell" hurts the thrill more than a phantom hit does.
- Launches need weight tiers: mooks fly out of the crowd, captains fly shorter and get up quickly, enemy officers step back half a pace but expose an opening — give every enemy type the same launch and the crowd loses its layers. Combo counting should be forgiving: the rules for dropping a combo (taking a hit, going a long stretch without connecting) must be explicit and predictable to the player, because a counter that stutters and stops kills the spectacle.

### 3.2 Battlefield Pacing and Objective Design: Strongholds, Morale, Escort Missions

A battle is a list of objectives on one map, and mowing is how you work through the list. Objectives fall into four types:

| Objective type | Typical form | Design and function |
| --- | --- | --- |
| Defeat | Enemy officers operate across the battlefield, and their troops waver once they fall; the commander-in-chief is the battle's victory condition | Main-line objectives that string the advance route together |
| Capture | Clear the defenders in an area and the stronghold changes hands, altering the advance corridors on the map | Cuts the map into stages and gives mowing a direction |
| Escort | Escort allied forces to a designated position, or prevent allies from being routed (with a countdown) | Creates time pressure and the decision of running between two fires |
| Defense | Fall back when the main camp and key points come under threat, with a countdown sounding | Creates a sense of crisis and forces the player out of their comfort zone |

Morale is the feedback layer that translates the player's results into shifts in the battle, and also the dial for dynamic difficulty. Common practice: defeating enemy officers and capturing strongholds raises your side's morale and enemy mooks turn passive; when the main camp is in danger or allies are struggling, alerts sound (voice lines, a flashing map, warning tones). The morale bar lets the player read "is this going well" at a glance.

Lay out a battle's pacing in four beats: the opening march and warm-up mowing (enemies are sparse); the mid-game fight over objectives (strongholds and officers, density rising); the climax (ambushes, reinforcements or a showdown-grade enemy officer); and the wrap-up (chasing down remnants or salvaging a lost cause). Ambushes and reinforcements are the cheapest pacing tools: add one group of enemies to the same stretch of battlefield and the pressure curve changes shape.

A battlefield is an order of magnitude larger than an action stage, and getting lost is the biggest experience failure. All three guidance pieces are indispensable: a minimap with objective icons, direction guidance (camera or arrows), and voice lines plus notification sounds when objectives change. Objective priority needs dynamic sorting — a main camp in danger outranks side objectives — so the player never makes a pointless hesitation between two objective lists.

### 3.3 The Character-and-Weapon Content Matrix: Character × Weapon × Moveset

This genre's content budget is a multiplication chain — and its biggest pitfall:

`playable characters × weapon modules × movesets × enemy officers × battlefields`

There are two routes for building the skeleton (the third, hybrid route is recommended); pick one before starting work:

| Route | How it works | Cost and payoff |
| --- | --- | --- |
| Weapon-decoupled | Moves follow weapon categories and are shared by all characters; characters carry only stats, a signature musou and staging | Highest reuse — swapping weapons swaps game feel; characters feel thin |
| Character-exclusive | Every character gets a complete moveset and a signature weapon | The strongest personality at the highest cost; the roster cannot grow |
| Hybrid | Shared modules per weapon category as the base, with the protagonist and flagship characters given signature musou attacks and unique moves | Content volume stays manageable; marketing focuses on a few characters |

The move system must be "shallow input, deep branches": normal attacks mashed out in a combo string, with the charge button plugged in at different combo nodes to branch into moves with different coverage and properties (known in the community as the C-technique system); the musou attack is the full-circle rescue and burst, used two or three times a battle, with camera staging. Player expression lives in branches, cancels and move combinations, not in a command list. Do the matrix math in advance: every new weapon module has to pass a balance pass against every battlefield and every enemy officer, and every new officer has to be playtested against every playable weapon; a reference approach is to build two or three weapon categories first, take the protagonist to full, fill the rest of the roster with shared modules plus staging, and only consider adding characters after the gameplay is validated.

### 3.4 Enemy Tiers and AI Choreography

Enemies need tiers, or a hundred identical mooks are just punching bags:

| Tier | Behavior | How the player answers |
| --- | --- | --- |
| Mooks | Advance in packs with slow attacks, and fly every which way when launched | Area attacks clear them — the main source of the thrill |
| Captains and elites | Carry shields or resistances, have short hitstun, and cannot be cut down before their guard breaks | Charged attacks break the guard, teaching the player to switch moves |
| Enemy officers | Super-armor moves, blocks and counters; they interrupt any combo other than musou | Move reading, combos and musou — a duel-grade opponent |
| Commander-in-chief | Phased behavior and an entrance sequence; the battle's resolution target | The showdown objective |

AI choreography aims not at smart but at "photogenic and fair": only a few enemies ever press in and actually attack at any moment (the attack quota), while the rest advance and probe from surrounding positions; the bodies sent flying must spread out and be able to hit others — never spin in place. Mooks that are too fierce will surround the player to death, and ones that are too dumb line up to die; both ends get balanced during the prototype. Enemies off-screen make no attack decisions, or must enter the frame before attacking; an unannounced knife in the back is a source of bad reviews.

### 3.5 The Progression Line After the Harvest

Strengthening between battles is why players stay, and levels, weapon forging and skill trees are designed around "make the next battle mow faster". The perceptible measures of progression are clear time and enemies felled per attack, not panel numbers; weapons and materials drop in tiers by battlefield difficulty, giving repeated runs a legitimate reason. Keep progression shallow: mowing's depth lives in the battlefield and the moves, not in a loadout sheet.

## 4. Technical Essentials

The engineering difficulty concentrates in three places: on-screen counts and performance, combat detection at scale, and staging and the camera. Everything below is engine-agnostic; it names concepts and structures.

**On-screen counts and performance**

- Stress-test the on-screen budget before designing against it: on the target platform's minimum spec, run a "mook-count ladder" (reference: 20, 50, 100 and 200 in turn), record frame times and memory, and write the conclusion into the design constraints; attack coverage and enemy density both work within that budget. The budget decides game feel and cannot be cut after the fact.
- Render mooks as cheaply as possible: share animation skeletons and materials, update at distance-banded frequencies (distant enemies drop to lower-rate animation and turning; off-screen ones freeze or degrade), and turn off unnecessary physics and particles. On-screen counts are bought with savings.
- Do not give large crowds full pathfinding: reserve the navmesh for main routes and enemy officers, steer mook crowds in bulk with formations and flow-field steering (one shared target point plus separation forces), and let a steering layer handle piling and detours.
- Object pools cover mooks, effects, damage numbers and drops, with spawning and recycling done in batches; cap audio concurrency and set priorities (hit sounds above voice lines, voice lines above ambience) — with mooks everywhere, the audio system is the first subsystem to break.

**Combat detection at scale**

- Hitboxes hang on active frames, and each attack resolves at most once per target; hit queries go through spatial partitioning (drop mooks into a grid and check only the cells the hitbox covers) — the key to detection holding up with hundreds of targets.
- Mook hit reactions must be "cheap and good-looking": use animated displacement or simplified trajectories for launches, check only a few nearby targets for collisions, and skip full rigid-body physics; resolve combo counts and kill statistics in one place rather than scattering them across each enemy's own script — with a hundred enemies each keeping their own state, the tallies will eventually disagree.

**Staging and camera**

- Musou attacks and executions are camera events: push in, slow motion, with VFX and sound synchronized on the same frame; lock input and grant invincibility during the sequence, hold a stretch of protection frames at the end, and allow skipping.
- The battlefield camera's basic requirement is "see the encirclement clearly": distance and angle must cover the threats around the player; once mowing density rises, any shaky camera work becomes a source of motion sickness.

**Data-driven**: characters, weapons, moves, enemy officers and battlefield objectives all go into data tables; battlefields are described in script files — triggers, timings and conditions — so non-programmers can lay out battles too (methods in the Programming Handbook).

## 5. Content Volume and Workload Reference

First, memorize the multiplier law: cost is multiplied, not added. Playable characters times weapon modules times movesets, with enemy officers multiplying another layer and battlefields another; every new weapon has to be validated across all battlefields and officers, and every officer has to be playtested against every weapon. Licensed tie-ins open a separate ledger: licensing, licensor approval and move reproduction are all independent budgets.

| Project shape | Playable characters | Battlefield scale | Timeline scale | Notes |
| --- | --- | --- | --- | --- |
| Mowing prototype | 1 | 1 small battlefield | 3–6 weeks | Validates the thrill formula and the on-screen budget only |
| First title / small complete game | 2–4 | 5–8 | 8–14 months | Weapon categories reused; 5–8 enemy officers |
| Typical indie scope | 6–10 | 12–20 | 1.5–2.5 years | Both the character and weapon matrices need feeding |
| Commercial scale | 20+ | 30+ | 3+ years | Tie-ins and licensing separate; release content in stages |

Animation scale (reference): one playable character's animation set (normal combo strings, charge branches, musou, mounted movement, hit and knockdown reactions, entrance and victory staging) usually runs 50 to 100 sets, and nearly all of them need their active frames tuned frame by frame; weapon-module reuse is the main lever for pushing this line down. Mooks share one skeleton, varied by weapon, palette and body type; enemy officers are cut down from the playable modules first (swap the weapon and stats, write behavior and AI separately).

The realistic cut for small teams:

- **Weapon modules first, character personality later**: build two or three weapon categories first, take the protagonist to full, and fill the rest of the roster with shared modules plus staging; keep battlefield themes to 3 to 5, creating variety through terrain layout and objective configuration rather than an endless stream of new art.
- **Tier the enemy officers**: enemy variants fill out density, officers are cut from existing modules plus AI, and special treatment goes only to the commander-in-chief and flagship officers.
- **Cut four things from a first game**: online play, an open world, multi-faction storylines, deep progression systems — any one of them can eat several more months; an open world is a double amplifier of scope and engineering for mowing, and a first game should not touch it.

Scheduling anchors: a thrill prototype, 3–6 weeks; a vertical slice where "one battlefield is at release quality", usually 4–6 months; extrapolate from there as content scope × a polish coefficient. The big budget lines in this genre are character animation, battlefield art and combat polish.

## 6. How to Start the First Prototype

The first prototype is one small battlefield only: one playable character, two mook types, one enemy officer, three objectives (defeat, capture, escort) — 3–6 weeks, with no art, story, saves or menus.

**Week 1: the thrill formula.** One normal combo string, one charged area attack, one musou; get launches, chain collisions, combo numbers and kill counts in first. It is supposed to look ugly, but the moment of "one swing fells a swath" must hold.

**Week 2: on-screen counts and tiers.** Run the mook-count ladder stress test and fix the on-screen budget; add an enemy officer (super armor and counters) and validate the feel of "a duel inside a sea of mooks".

**Week 3: the battlefield skeleton.** One small map, three objectives, the morale bar and the three-piece guidance kit; write "where to go after clearing" into the objective chain.

**Weeks 4 to 6: tuning and testing.** Find 3 to 5 people who have never played it, have each play twice, and record whether combos are pursued spontaneously, whether the musou is used on the player's own initiative, and whether objective guidance is readable with zero verbal explanation.

Success criteria (all observable):

- With greybox art and placeholder audio, testers still want to replay the same battlefield for more than 10 minutes.
- Testers can name the thrill points themselves (felling a swath, chain launches, a musou finish) — not "I beat up some guys".
- Objectives and guidance are readable with no explanation given: testers find the next objective point on their own.
- The on-screen count reaches the budget you fixed in stress testing with a stable framerate; change one game-feel parameter and you can see the difference in the running game within 5 minutes.

If the thrill formula and the on-screen budget fail acceptance, do not start spreading content: rework on the foundation multiplies across all characters and battlefields (§5).

## 7. Common Pitfalls

1. **Spreading content before the thrill holds**: characters, weapons and battlefields go into mass production, only to find "one swing fells a swath" doesn't hold, and everything is redone. Freeze the thrill formula and the on-screen budget first (§3.1, §4).
2. **Detection that can't keep up with the blade arc**: the swing visually passes through a crowd but only two or three take the hit; or the reverse, phantom hits at a distance. Let the blade arc define detection, and keep the generosity on the player's side.
3. **Cutting the on-screen count after the fact**: attack coverage and enemy density are designed for "a hundred", stress testing says thirty, and the gameplay is torn down and rebuilt. Fix the budget by stress testing first, then design the gameplay (§4).
4. **Enemies who surround you to death or line up to die**: everyone piles in and combos the player to death, or they stand around queuing to be hit; the attack quota and the rotation of attackers both need balancing (§3.4).
5. **A battlefield with no guidance**: the player gets lost between the main camp and the enemy camp, guessing at objectives. Minimap, direction guidance and voice lines — the trio is all indispensable (§3.2).
6. **Estimating content linearly**: characters × weapons × officers × battlefields (§5); overruns usually hide in the multiplication signs.
7. **Mowing with no battlefield**: the map degenerates into a practice dummy range, one pile cleared after another, bored within ten minutes. Objectives and morale give mowing a direction (§3.2).
8. **Runaway musou staging**: the sequence runs too long, cannot be skipped, and the player is beaten up the moment it ends. Give staging invincibility and protection frames, and allow skipping (§4).
9. **Copying existing works' visuals**: historical and mythological subject matter is common material, but character designs and move staging are each studio's assets; copying is a copyright risk, not a tribute.
10. **Betting a first game on an open world**: an open world magnifies content volume and engineering complexity by an order of magnitude at once — the number-one scope disaster for a first mowing game (see Indie Survival).

## Further Reading

- Game Design Handbook: core loops, number-table methods and game-feel checklists — the draft under §3.
- Programming Handbook: methodology for combat detection, on-screen performance and object pooling.
- Level Design Handbook: battlefield objectives, pacing curves and the whitebox flow — complementary to §3.2.
- Case Studies: postmortems of classic and tie-in mowing titles; use them as reference when breaking down games.
- Indie Survival: scope control and scheduling discipline — complements §5.
- Pitfalls & Anti-patterns: pitfalls in action design and content production; cross-read with §7.
