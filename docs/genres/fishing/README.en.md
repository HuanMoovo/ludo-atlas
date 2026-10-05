# Ludo Atlas · Genre Handbooks · Fishing

> **Genre Handbooks · Volume 4**. Positioning: the genre that makes the four-beat loop — "cast, wait, bite, fight" — its first pleasure. The player's core actions are reading the water and controlling the line; the catch is the joint result of probability and skill, with the compendium supplying the long-term goal and environment and ritual supplying the relaxed experience.
> Companions: Game Design Handbook (core loops and probability design) · Programming Handbook (state machines and data tables) · Case Studies (breakdown and retrospective methods) · Indie Survival (scope control and content-volume accounting).
> This page carries no external links; benchmark titles are widely known works only, and the figures here are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: fishing is the genre that **makes "waiting" content too**. Of the four beats, waiting takes the largest share, the fight is the climax and the compendium is the long tail. Get waiting wrong and the game degrades into a numbers settlement screen; get the fight wrong and the waiting has no moment of payoff.

The core loop, written as a ring of verbs:

`pick a spot and set your rig → cast → wait and read the water → bite → fight and reel in → land it and settle → update the compendium and economy → switch spots or switch bait`

The time split of the four beats (typical magnitudes for the casual direction): cast 2–5 seconds, wait 5–30 seconds, bite window 0.5–1.5 seconds, fight 5–60 seconds. This split hides the genre's biggest design contradiction; for how to handle it see §3.3.

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Farming sim / survival crafting | Fishing there is a subsystem you can sum up in a few lines; this genre expands it into the whole game |
| Arcade fishing (the Fishing Joy style) | Those games aim, fire and hit instantly — essentially shooting and scoring; this genre settles through waiting, probability and the fight |
| Idle / incremental | Both sell time, but idle automates the process away; fishing's entire selling point is the process itself |

A self-check question: compress the waiting into "one tap and everything settles instantly" — does the game still hold up? If the answer is "more or less", what you are making is a gacha screen, not a fishing game.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Suspense in the anticipation**: there is something unknown beneath the surface, and every cast could bring up something good; the probabilities need not be public, but the patterns must be perceptible (time, weather, bait, depth).
2. **The duel of the fight**: one reel-in is a 10–60 second tug-of-war; win in a way you understand, and when the line breaks, know why.
3. **The completionist pull of collecting**: the compendium, size records and rare specimens give the reason for "one more cast".
4. **Relaxation and ritual**: the default state is calm; ambient sound and light settle the player down, and tension appears only after the bite.
5. **A visible scale of growth**: rod, line, hook, bait and levels turn "getting stronger" into a visible curve.

Negative feelings (any single one is a red flag): waiting with nothing to do; holding down one button for the entire fight; a rare fish that never shows up and no one can say why; line breaks that feel purely random.

Benchmark titles (all widely known; play them yourself before breaking them down):

| Title | What to learn from it |
| --- | --- |
| Fishing Planet | Realistic fishing methods (float fishing, lure fishing), gear upgrades and a quest-driven long-term structure |
| Russian Fishing 4 | The upper-bound sample of realistic scale: the trade-offs of an extremely slow pace and a fiddly gear system — see the audience boundary clearly |
| Stardew Valley (fishing system) | The minimal duel model of the green-bar fight; fishing and the farm economy feeding each other |
| Animal Crossing: New Horizons | Minimal bite-timing interaction; a month-gated compendium and museum-style collecting |
| Red Dead Redemption 2 (fishing side content) | Making fishing part of world immersion and survival supplies |

## 3. Design Essentials

### 3.1 The Fight: Tension, Stamina and Timing

The fight is the genre's technical core: player and fish contend over the same stretch of progress, and the way to win must be explainable. Pick the model first, then tune the numbers:

| Model | Gameplay | Onboarding barrier | Common in |
| --- | --- | --- | --- |
| Green-bar | Keep a moving bar overlapping the fish icon; overlap accumulates progress | Low | Stardew Valley, most casual fishing |
| Tension | Reeling raises tension; exceeding the limit breaks the line; releasing vents it | Medium | Realistic titles such as Fishing Planet and Russian Fishing 4 |
| Timing | Press the button at the instant of the bite; hit the window and it is yours | Very low | Animal Crossing and the lightweight versions in many subsystems |

- **The progress bar is a two-way tug-of-war**: the player pushes forward, the fish forces pushback along the way; failure is not progress reset to zero but a hook-off or a line break, with a readable reason.
- **The fish needs behavioural tiers**: charging, sprinting and head-shaking split into 2–4 kinds; the sprint is the tension peak and the highlight point for sound and rumble; without behavioural tiers, the fight is just holding the button down.
- **Make releasing useful**: the essence of the tension model is the rhythmic alternation of reeling and easing; the essence of the green-bar model is predicting the fish's next hop; a fight that only knows how to hold the button will not survive thirty fish.

Balance skeleton (magnitude references):

| Knob | Reference range | Role |
| --- | --- | --- |
| Bite window | 0.5–1.5 seconds, longer in casual games | Timing leniency; below 0.3 seconds is extremely unfriendly on touchscreens |
| Single-fight duration | Small fish 3–10 s, common 10–30 s, rare 30–90 s | The felt scale of rarity, measured in time |
| Fish stamina | Falls with the fight and with sprints | Provides the floor of "patience will win" |
| Line tension limit | Tied to line strength and fish power | The source of break risk; the warning comes before the break |

### 3.2 Compendium and Rarity: Condition Tables and Collection Payoffs

Rarity is not four labels but a "spawn condition table"; what players actually study are the conditions, not the probabilities themselves:

| Rarity (illustrative) | Base weight | Additional conditions | Experience role |
| --- | --- | --- | --- |
| Common | Around 60% | None | Guarantees a catch every time |
| Uncommon | Around 25% | A specific bait or depth | The mid-game research goal |
| Rare | Around 10% | Combinations of time, weather and season | The key cells of the compendium |
| Legendary / monster fish | A few percent | Stacked conditions plus long-term accumulation | The highlight and the talking point of a session |

- Conditions must be expressible: locked compendium cells show a silhouette and clues to where it appears (time, weather, waters); no pure black boxes.
- Weights plus pity: after several consecutive empty casts, lean toward targets that fit the current conditions; put the pity counter into the save file, so effort has an echo.
- Size records are the long tail: track the largest size per species so repeat catches still mean something, at a cost far below adding another batch of species.
- Collection needs payoffs: compendium completion gives rewards and titles, and rare fish need a display spot (aquariums, museums, home decorations — whatever the vessel is); a collection that only adds numbers might as well not exist.

### 3.3 Waiting: Ritual and the Edge of Boredom

Waiting is this genre's double-edged sword: handled well it is ritual, handled badly it is torture. The baseline is that waiting must simultaneously be "something happening" and "nothing happening": the environment moves (currents, light and shadow, birds, jumping fish) and the player makes decisions (changing bait, changing depth, shifting spots) — only the pace is slow.

- The bite has a wind-up and the wait carries information: false bites and float twitches stage the end of the wait as a little play; fish shadows under the water, a rod tip that stirs, shifts in water color — the wait has things to read.
- Leave variance in the rhythm: many short waits in a row go stale; occasionally stretch one out and then deliver a crit (a good fish) — variance matters more than the average.
- Pin the boredom edge with numbers: one session (10–20 minutes) should run the full loop 5–10 times; the moment a single wait passes 30 seconds, either give information, give an event, or accept it as a deliberate audience filter for realistic-leaning players.
- Auto-fishing is relief, not replacement: mobile games trade an auto mode for players valuing the manual highlights; design the reward gap between the two modes clearly, or manual play becomes decoration.

### 3.4 Fishing as a Subsystem: Blending with Management and Survival

When fishing is a subsystem, the evaluation standard shifts from "is it fun" to "is it worth a slice of the player's day":

- Give it a full economic role: food, cooking ingredients, money, quest delivery, gear materials — it must occupy at least one mature economic loop; put fishing's per-hour yield into the same yield table as the host game for comparison (methods in Genre Handbooks · Farming Sim §3.2).
- Feed the main line both ways: fish feed the farm and survival loops (food, fertilizer, potions), and the host in turn provides fishing with gear and unlocks; a subsystem that only gives and never receives gets judged skippable by players.
- Fix the time budget: in schedule-driven games, lock down how much in-game time one full loop consumes (reference: around 30 minutes of in-game time), or it eats the main line's pacing.
- Restrained entry and a baseline: the subsystem version's mechanical depth should be pared down — a green bar or timing model gets there in one pass — and the full realistic gear tree is left to standalone titles; clearing the game without fishing is the correct baseline — fishing players get obvious returns, but no hard gate.

### 3.5 Gear and Progression: The Four-Piece Set and Modifier Tables

The four pieces each hold a share of the say: rod (pull limit and casting distance), line (tension limit — the lead actor in line breaks), hook (bite and hook-off rates), bait (species preferences). The four lines upgrade independently, so "new gear, new approach" rather than swapping in a bigger set of numbers.

- Modifier tables and acquisition pacing: every fishing method and species applies modifier values to gear; audit loadout usage rates with simulation scripts to avoid a single globally optimal set; a new gear unlock should mean "fish you could not catch before become catchable", not a pure stat bump.
- Consumables (bait, groundbait) carry the daily upkeep and the reason to come back; their consumption rate must be quantifiable (how many packs an hour) — do not let the economy run with inflow alone.

## 4. Technical Essentials

The engineering difficulty sits in three places: the numeric simulation of the fight, the datafication of probability and content, and the immediacy of feedback. Everything below is engine-agnostic.

**The fight system**

- The fight is a small numeric simulation plus a state machine: the states are waiting, bite, tug-of-war and settlement; the fish has power, stamina and a behaviour script, and the player has reel input and tension parameters. Run the settlement on a fixed tick (on the order of 10–20 Hz); do not force it through a physics engine.
- Leave margin in the line-break check: as tension nears the limit, first give audiovisual warnings that the line is groaning, and only break after several frames of sustained excess; a system that snaps on a single over-limit frame just feels random.

**Probability and data tables**

- Species, scenes and gear are all externalized as data tables (CSV or JSON); draws use weighted tables plus modifiers: final weight = base weight × time × weather × season × bait modifier, with the multipliers configurable, never hardcoded. Pity is a separate layer: count consecutive misses of a target rarity into the save file, and once the threshold is reached multiply that rarity by a lean coefficient; run distribution tests with a fixed random seed.
- The compendium is a database: catch records, maximum sizes and condition hints all derive from the same species table; the compendium page only reads the table, with no second source to maintain.

**Feedback and presentation**

- Bite and fight feedback is audited frame by frame: sound, rumble, rod deformation, and the line's slack and tautness must all fire on the same frame to pass; anything beyond two frames of latency is very hard to sell (methods in the Programming Handbook).
- Water surfaces and fish schools can be economized: stage the surface with shaders and textures; skip real underwater schools and cover them with "shadows plus probability"; simulate school behaviour only in realistic-leaning projects, with the cost budgeted separately.
- Saves carry a version number from day one: the compendium, size records, gear and quest progress are all long-term data that must migrate across versions; for online-leaning projects, catch settlement must have server-side validation of randomness and numeric upper bounds.

## 5. Content Volume and Workload Reference

The cost formula is close to multiplication: `total content ≈ species count × per-fish assets + scene count × per-scene assets + gear count × configuration + compendium and quest text`.

Typical magnitudes for species × scenes × gear (for estimating scope — not a commitment):

| Tier | Species | Scenes | Gear scale | Positioning |
| --- | --- | --- | --- | --- |
| Prototype | 5–10 | 1 | 1–2 rods, 2–3 baits | Validate the four beats and the fight's feel |
| Small finished title | 30–60 | 3–5 | 3–5 tiers per each of the four pieces | 6–12 months solo or small team |
| Typical indie title | 60–120 | 6–10 | Over a hundred gear and consumable items | Needs a content pipeline and tooling |
| Realistic commercial title | 100–300 | 10–20 | Hundreds, continuously updated | Long-term live ops or a series to amortize cost |

Per-unit costs (magnitude references, as above):

| Content unit | Unit cost | Notes |
| --- | --- | --- |
| One fish (2D / 3D) | 0.5–2 person-days / 3–10 person-days | Artwork or icon, animation, compendium card and text; 3D adds a model and behaviour parameters |
| One scene / water body | 1–3 weeks | Terrain, lighting, fishable spots and fish-pool configuration |
| One piece of gear | 0.5–2 person-days | Balance configuration, icon, acquisition chain |

- Species count is the most flexible knob: freeze the loop and the fight's feel first, then expand the table according to production capacity; cutting species is safe, cutting the fight is dangerous.
- Compendium and quest text are the invisible big-ticket item (writing, proofreading and localization each pass through it); give the text IDs from day one; scheduling anchors: fight prototype 2–4 weeks; vertical slice (one water body, around 30 species, complete economy) 2–4 months; commercial scale counted in years.

## 6. How to Start the First Prototype

The first prototype builds a single water body, finishes in 2–4 weeks, touches no quest system, builds no gear tree, and uses all-whitebox art.

1. **Week 1: close the four-beat loop.** One rod, 3 species (common, uncommon, rare) and one stretch of riverbank; cast, wait, bite and fight settlement all run end to end, with the simplest weighted table for draws to start.
2. **Week 2: tune the fight.** Pick and implement one model — green bar or tension (timing is too thin to carry the validation); tune bar speed, vent rate and fish sprint behaviour into a rhythm; record frame by frame and tally the duration distribution of single fights.
3. **Week 3: waiting and the information layer.** Environmental staging (water surface, light, fish shadows), the bite wind-up, empty-cast feedback; specifically test reactions to "20 seconds with no payoff" — this stretch is more honest than any parameter.
4. **Week 4: external testing.** Find 5 people who have never played, and have each cast 20 times; record three things: when they zone out, when they curse, and when they reach for a screenshot; then go back and fix wait durations against the boredom edge in §3.3.

Success criteria (all observable):

- Testers fish for their 10th catch and beyond on their own initiative, not because they were asked for one more cast.
- After a line break or a hook-off, testers can name the reason (tension, timing or gear — one of the three).
- Wait durations and catch frequency form a rhythm testers can recount; they can predict "something is about to happen".
- Changing one value (a weight or the tension limit) lets its effect on the experience be quantified within 10 minutes.

If the rhythm falls short, do not lay out content yet: expanding the species table is cheap, reworking the loop is expensive.

## 7. Common Pitfalls

1. **Waiting turned blank**: no wind-up, no information, no environmental staging — the player is idling. For fixes see §3.3.
2. **The fight reduced to one button**: holding the reel always wins and the duel disappears. Give the fish behaviour and make releasing useful (§3.1).
3. **A probability black box**: rare fish with no clues and no pity, effort with no echo. Make conditions visible and put pity into the save (§3.2).
4. **Economy out of step with the main line**: fish prices detached from the gear curve, or the subsystem out-earning the main line twofold. Fold it into the host's yield table by per-hour returns, and cap the yield (§3.4).
5. **A realistic onboarding wall**: terminology and fishing methods keep newcomers outside the door for an hour. Teach in three tiers: catch something first, and only then talk about catching well (§3.5).
6. **A bite window too narrow**: a 0.1-second window is a disaster on both touchscreens and gamepads. Set the window by the worst device (§3.1).
7. **Over-punishing line breaks**: losing a rare fish also wipes bait and durability, and the player uninstalls on the spot. Keep pity on hook-offs and cap the losses.
8. **Homogenized waters**: the species table piles up to 200 entries while fish pools and conditions are identical everywhere, and collecting degrades into gacha. Design condition tables and scenes in the same batch (§3.2, §3.5).

## Further Reading

- [Game Design Handbook](../../fundamentals/game-design/README.md): the base document for core loops, probability and collection systems, covering §1 and §3.2.
- [Programming Handbook](../../fundamentals/programming/README.md): implementation details for data-driven systems, state machines and debug tooling, covering §4.
- [Case Studies](../../postmortems/README.md): breakdown methods for long-term collection-driven works — a reference when choosing a direction and running retrospectives.
- [Indie Survival](../../../playbooks/indie-survival/README.md): scope control and scheduling discipline, complementary to §5.
- [Pitfalls & Anti-patterns](../../pitfalls/README.md): the checklist of pitfalls in content and balance production, to read against §7.
- [Genre Handbooks · Farming Sim](../farming-sim/README.md): the host example for fishing as a subsystem — the full counterpart to §3.4.
- [Genre Handbooks · Survival Craft](../survival-craft/README.md): gathering loops and pressure-source design — a reference for survival blends.
- Homework: first write out, on paper, the spawn condition tables for 10 species and the modifier tables for three pieces of gear, hand-calculate the expected rarity distribution over ten draws, and only then decide whether to start building.
