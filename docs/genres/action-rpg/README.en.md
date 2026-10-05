# Ludo Atlas · Genre Handbooks · Action RPG

> **Genre Handbooks · Volume 2**. Positioning: a genre that stitches "hands-on skill in real-time combat" and "long-term growth through gear and stats" into a two-layer loop — the combat itself has to stay fun on repeat, and the loot has to be worth chasing.
> Companions: Game Design Handbook (core loops and progression numbers) · Programming Handbook (combat systems and performance) · Level Design Handbook (combat spaces and pacing) · Indie Survival (scope and scheduling).

---

## 1. Positioning and Core Loop

One-sentence positioning: an action RPG draws its fun from two sources, and it needs both. First, **the combat itself is fun** — dodging, footwork and attack timing, the craft in your hands, directly decide the outcome. Second, **getting stronger is visible** — every drop changes the numbers and the way you play, giving repeated combat a direction. Get the first right alone and you have an action game; the second alone, a stat-driven RPG. Both legs working is what makes it this genre.

The core loop, written as a verb ring:

`Scout the enemy → Engage and strike → Dodge and counter → Collect drops → Swap gear and tune skills → Take on tougher enemies`

This loop has two layers of pacing: the combat layer is measured in seconds, one exchange lasting 10–30 seconds and covering attacking, dodging and finishing off; the progression layer is measured in minutes to hours — one loot upgrade, one build coming together. The interface between the two layers is the felt sense of getting stronger: if a player can't tell any difference between now and ten minutes ago after a fight, the progression layer is broken.

Drawing boundaries with neighboring genres:

| Neighboring genre | Boundary |
| --- | --- |
| Pure action games | Combat feel comes from the same roots; the difference is the progression layer — winning requires growing steadily stronger through gear and numbers, not skill alone |
| Pure RPGs | A pure RPG settles win or loss in commands and numbers; in an action RPG, execution can clear part of the stat threshold, and stats can cover part of the execution shortfall |
| Soulslike | The heaviest-punishment branch of the family: death costs are high, pacing is built on learning and memorization, and gear progression is held tighter |
| Looter shooters | The same skeleton of drops, affixes and builds, with melee and spells swapped for guns and cover |

Two self-check questions: take away gear and numbers — is the combat still fun? Remove progression — will players still repeat fights? Answer "not fun" to the first and the action layer is in arrears; answer "no" to the second and the progression layer is.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Execution decides**: wins and losses are explained by player action — dodge timing, attack spacing and skill choices can all be reviewed and understood afterwards.
2. **Hits land with weight**: every hit gives clear feedback; the player knows exactly what they hit and how big the effect was.
3. **Growth is visible**: the difference new gear and new skills make must be felt within one or two fights, and the numbers can be traced to a reason.
4. **Build imagination**: affixes and skills leave room for combinations; players can invent their own archetypes, and are motivated to try a second playstyle.
5. **Farming with purpose**: drop pacing gives "one more run" a concrete target instead of open-ended luck.

Benchmark titles (play them yourself before breaking them down):

| Title | What to learn from it |
| --- | --- |
| Diablo II | The density benchmark for drop and affix systems; build-driven motivation to keep fighting |
| The Elder Scrolls V: Skyrim | Making progression follow the player in an open world; exploration and combat feeding each other |
| The Witcher 3 | Pre-fight preparation (blade oils, Signs) as gameplay in itself; the join between narrative and combat |
| God of War | Hit impact and camera expression; stitching a progression system into the narrative flow |
| Elden Ring | The sense of fairness in high-difficulty combat; gear variety and exploration rewards completing each other |
| Monster Hunter: World | Weapon feel and part breaking in a single hunt; long-term motivation from material drops and gear crafting |

## 3. Design Essentials

### 3.1 The Two-Layer Loop: Game Feel Is the Foundation, Progression Is the Engine

Tune the two layers separately, and govern the interface between them with one standard:

- **The combat layer's acceptance test is "playable with no gear"**: handed no equipment at all, the basic attack-and-defense loop must still carry a full fight through.
- **The progression layer's acceptance test is "gear you can feel"**: one qualifying core item must produce a felt difference within one or two fights — damage, combo rhythm or skill rotation changes in at least one of them.
- **The job of numbers is amplification, not substitution**: gear power may cover part of the execution difficulty, but never to the point where "you win standing still".

Keep a threshold channel between the two layers: execution can cover part of the numbers, so a skilled player on lower-tier gear can still clear the line; numbers can cover part of the execution, so a new player on higher-tier gear can still make progress. The test is direct: have a strong player fight with gear one tier down — they should clear it, but visibly struggle.

Every step up the progression ladder needs a new enemy-side answer to match it (new moves, new combinations, new mechanics), or growth is merely bigger numbers.

### 3.2 Skill Design: Resources, Cooldowns and Combos

A skill's two billing dials are resource and cooldown, and the common structure has three tiers:

| Tier | Role | Common practice |
| --- | --- | --- |
| Basic attacks | Filler damage, resource recovery, holding the combo rhythm | 3–4-hit combos with low per-hit damage; game feel has top priority |
| Spender skills | Main damage and utility (mobility, control, area) | Cost resource or run on a short cooldown; players cycle them on a set rhythm |
| Ultimates | Phase-level burst and emotional peaks | Long cooldown; usually fired once or twice per fight |

Don't bill resource and cooldown twice for the same skill: if you run a resource loop, go easy on long cooldowns; if you run cooldowns, don't stack resources — running both together strangles the skill cadence. Skill count obeys the button layout: comfortable gamepad and keyboard bindings usually support 4–8 active skills; beyond that, cut the rarely used ones or move them to a skill wheel.

Combos consist of input buffering and recovery cancels: when one attack's recovery is cancelled by the next attack, a dodge or a skill, the rhythm flows. Cancel windows belong in data tables, with every action annotated for what can cancel it — otherwise one animation change knocks everything out of alignment. Acceptance test: have a tester chain 30 attacks, then ask "did any hit feel like your input was eaten?"

### 3.3 Hit Feedback: Make Every Attack Land with Weight

Hit feedback is layered from five channels; miss one and it feels like punching cotton:

| Channel | Practice | Common magnitude |
| --- | --- | --- |
| Hitstop | Freeze both parties for a few frames at the moment of impact | 30–100 ms, longer on heavy hits |
| Hit reactions | The enemy's hit animation, displacement and hitstun | Light hits flinch, heavy hits stagger; when the enemy has super armor, move the feedback to the player's side |
| Camera and screen shake | Small screen shake, a slight camera nudge in the hit direction, field-of-view changes | Scale intensity by damage tier; allow players to turn it off |
| Audio-visual layer | Layered hit sounds (impact, guard break, crit) and hit effects | Trigger on the same frame as the hit resolution — never delayed |
| Numbers and status | Damage numbers, crit styling, status icons | The number must convey magnitude without blocking the action |

Ordering discipline: make hitstop and hit reactions solid first, then talk particles and screen shake. Reverse the order and it becomes a fireworks show where players can't read whether a hit landed or how hard it was.

### 3.4 Gear and Affixes: A Minimum Viable Design

An MVP equipment system compresses into five decisions, each of them table-manageable:

1. **Slots**: a weapon plus 3–4 armor slots (head, chest, boots, say) is enough to start; more slots are a lever for expanding content later.
2. **Quality**: start at three tiers (common, magic, rare); quality determines only affix count and value caps, never extra multipliers.
3. **Affix pools**: split by slot — no movement speed on weapons; every affix has an explicit weight, and uniform odds across the whole pool are not allowed. Be restrained with numeric affixes: mechanic affixes (triggered effects, behavior changes) are the real source of build diversity.
4. **Legendaries**: each one changes a specific behavior, e.g. "the next attack after a dodge always crits"; few and sharp, one memorable hook per item.
5. **Progression entry points**: deep systems like upgrading, socketing and reforging are all deferred; a first game keeps only one main path — "swap in something better".

The minimal form of affixes is a table: slot, affix pool, weight, value range. Maintaining that table costs less than writing a random-generation system, and balance changes never touch the code.

### 3.5 Drops and the Progression Curve: Make "the Next One" Worth Wanting

Drop design answers three questions — what drops (pool), how much (quantity) and how likely (weights) — and all of it goes into tables:

- **Pity and targeting**: long dry spells without a key piece need a pity system; a core build's gear gets one targeted acquisition channel (crafting, exchange, designated boss drops). Keep randomness for surprises, not for progress.
- **The salvage loop**: low-quality drops can be broken down into resources, so even an empty-handed run converts into progress.
- **A segmented curve**: high-frequency gear swaps in the first 30 minutes, so every minute feels stronger; slow down in the middle, sustaining novelty with affix combinations and new skills; close with rare drops and extreme challenges. Watch one metric throughout: how far the player is from "the next piece they want".

Difficulty steps follow the progression rhythm: each area posts a recommended power line — above it, progress is smooth; below it, you visibly struggle — letting players choose their own pace instead of being hard-gated by a stat wall.

## 4. Technical Essentials

The following is engine-agnostic; what it names are concepts and structures.

**Combat resolution**

- Attack resolution uses shape queries (box, capsule, sphere sweep); startup, active frames, recovery and hitbox range all read from data tables, and active frames are visualized in debug tools.
- Hitstun, invincibility frames and super armor are three concepts that must be implemented independently; interrupt rules go into an explicit table so who can interrupt whom is one lookup away — don't scatter them across code branches.
- Damage resolution is a pipeline with a fixed order: base damage, bonuses, crit, resistance, mitigation; it is loggable end to end, so any single hit can be reconstructed.

**Input and state machines**

- Input buffering and input queues are the infrastructure of game feel: commands pressed before the recovery ends must be remembered and consumed.
- The character state machine covers movement, attack, hit reaction, dodge and death; every action is annotated with what can cancel it and what can interrupt it.
- Combo windows, dodge cancels and skill chaining live in the same data, shared by animation and logic; maintaining two parallel sets is not allowed.

**Progression systems**

- Enemies, skills, affixes and drops are all data-driven; random drops use reproducible RNG — a fixed seed can be replayed, or live issues cannot be reproduced.
- Saves carry a version number and a migration strategy: after loot tables and affixes are updated, gear in old saves must still load correctly.
- Number tooling comes first: have a small tool that can edit values and run simulated combat before talking balance.

**Performance and experience**

- Pin down per-screen enemy counts and concurrent VFX limits for target devices, and design combat within budget instead of cutting back afterwards.
- Drops need caps, merging and pickup magnetism; long fights must not drop frames from loot piling up.
- Cap concurrent audio and set priorities — hit sounds outrank ambience, or the mix turns to mush.

## 5. Content Volume and Workload Reference

First, one multiplier law — also the biggest content trap in this genre: content cost is multiplied, not added. Add one enemy type and the cost is not just its own model and animations: multiply by the number of scenes (every combat space must accommodate its movement and targeting), multiply by the number of player builds (every build must be able to take it down), then multiply by the combinations with existing enemies. Scene count gets the same accounting: every new area needs a signature encounter that carries its theme, usually a new enemy or a new boss. Bosses multiply once more: scripting and debugging one boss usually equals three to five regular enemies combined.

Common magnitudes (reference values, not a commitment):

| Project type | Enemy types | Boss count | Timeline | Notes |
| --- | --- | --- | --- | --- |
| Combat prototype | 1–2 | 0 | 3–6 weeks | Validates game feel and hit feedback only |
| First game / small complete title | 8–15 (including variants) | 2–4 | 1–2 years | Use variants to buy density, not new skeletons |
| Typical indie title | 15–30 | 4–8 | 2–4 years | Content scope and balance testing split the effort |
| Commercial scale | 30+ | 8+ | 4+ years | Release content in phases |

The realistic picture for small teams:

- **Variants, not new species**: swap the weapon, swap the element, swap one core behavior, and it serves as a third or fourth enemy; keep the budget for each area's signature enemy.
- **Keep scene themes to 3–5**: create variety through layout and encounter configuration, not a steady stream of new materials and models.
- **Size skills to testing capacity**: keep the skill tree within what one test round can cover; build multiple archetypes by reworking the same skill set through affixes, not a fresh set per archetype.
- **Cut four things from a first game**: multiplayer, procedurally generated open worlds, multi-ending narrative, a second equipment system. Any one of them can eat another year.

Scheduling anchors: the game-feel prototype takes 3–6 weeks; reaching a vertical slice where "one boss fight is release quality" usually takes 3–6 months; extrapolate from there by content scope times a polish factor. More projects in this genre die from content estimates than from technical problems.

## 6. How to Start the First Prototype

The first prototype is a single combat room: one melee weapon, two or three enemies in rotation, and one complete drop loop. No story, quests, big map or shop.

**Weeks 1–2: combat sandbox.** Movement, dodge, one three-hit basic combo, one spender skill, hit reactions and death. Build the active-frame visualization first; the game-feel ledger starts here. Ugliness is expected at this stage.

**Week 3: hit feedback.** Install the five channels from §3.3 one by one: hitstop, hit reactions, screen shake, layered sound (placeholder assets), damage numbers. Record a clip after each one for comparison.

**Week 4: drop loop.** Kills drop random gear at two or three quality tiers; pickup, comparison, equipping and stat changes all work end to end. Only weapons and one armor slot.

**Weeks 5–6: internal testing.** Bring in 3–5 people who have never played it, and watch when they start seeking out fights, when they loot corpses, when they say "I got stronger that run". Log the stall points and the complaints — no hints, no explanations.

Success criteria (all observable):

- With nothing but greyboxes and placeholder audio, testers still want to fight the same enemy for 10+ minutes.
- After equipping a new weapon, testers can say for themselves what changed in damage or rhythm.
- After a kill, testers go pick up drops on their own instead of ignoring the glints on the ground.
- Change one value and within 5 minutes you can see its effect on game feel and time-to-kill in the build.

Once every link of the prototype passes, then talk about content production. Rework in these two foundations — game feel and drops — gets multiplied by the entire content scope.

## 7. Common Pitfalls

1. **Building only one of the two loops**: piling on numbers before game feel is settled, or a beautiful equipment system over bare-gear combat that isn't fun. Make bare-gear combat work first, then bring in progression.
2. **Estimating content linearly**: "10 more enemy types" on paper must be multiplied by scene fit, build compatibility and balance testing — this is where schedules usually blow out (§5).
3. **An undisciplined affix pool**: uniform odds across the whole pool with no slot constraints means players can never assemble the combination they want, and the motivation to farm flatlines.
4. **Runaway stat inflation**: attack affixes multiply without a cap, everything late-game is a steamroll, and all boss design is void. Cap the multiplier zones; leave the enemies a step to stand on.
5. **Drops idling for ages**: key pieces purely luck-based, with no pity and no targeted channel, leave players oscillating between "one more run" and uninstalling.
6. **Missing hit feedback**: damage numbers without hitstop or hit reactions turn combat into arithmetic. Fill in all five feedback channels before talking spectacle.
7. **Homogenized skills**: when every skill is a "high-damage big area", players only use the strongest one. Skills need functional roles — mobility, control, resource recovery and burst each doing their own job.
8. **Difficulty tuned with numbers only**: enemies get stronger by doubling HP and damage, with no new moves or combinations, and what players feel is "it got harder with nothing new".
9. **A first game overloaded with scope**: multiplayer, a big world, deep crafting and multiple endings at once means most likely finishing none of them (§5).
10. **Balancing by theorycrafting**: a balance table that never met real testers — the player community finds the combinations you never tested within hours of launch. The final judges of balance are testers and live player data.

## Further Reading

- Game Design Handbook: the source draft for core loops, balance tables and progression curves; §3 unfolded in full.
- Programming Handbook: methodology for combat architecture, hit resolution and performance.
- Level Design Handbook: combat space dimensions, pacing curves and the whitebox workflow.
- Indie Survival: scope control and scheduling discipline, complementing §5.
- Case Studies: postmortems of real projects — keep them beside you when breaking down titles.
