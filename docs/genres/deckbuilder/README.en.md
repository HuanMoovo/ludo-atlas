# Ludo Atlas · Genre Handbooks · Deckbuilder

> **Genre Handbooks · Volume 2**. Positioning: turning "building the deck" itself into the core gameplay. The deck is the character's skill sheet, and every new card is one deckbuilding decision; combat cashes out the build, and the build explains the combat.
> Companions: Game Design Handbook (loops and numbers) · Programming Handbook (data-driven design and resolution systems) · Production Handbook (scope and cost) · Case Studies (samples of success and failure).
> This page carries no external links; examples are limited to well-known titles, and the numbers are common magnitudes — calibrate against your own project's measurements.

---

## 1. Positioning and Core Loop

### 1.1 One-Sentence Definition

The deckbuilder is the genre of "using cards as parts to assemble a machine that grows." Combat is the check; building is the main course: half the player's fun comes from what to play this turn, and the other half — more than half, even — comes from "which card to take next and which direction the deck grows in."

Drawing boundaries with neighboring genres:

| Neighboring genre | Boundary |
| --- | --- |
| Card dueling (TCG and CCG) | Also built around deck construction, but the opponent is a real person: the build is finished before the match, and the thing being balanced is the metagame. The structural differences are laid out separately in §3.5 |
| Roguelike action | Randomness, death economy and meta-progression share the same roots, but the control layer swaps real-time feel for turn-based decisions |
| Auto-battler | Has the build fun of picking units and assembling synergies, but combat is fully automatic, with no hand and no energy |
| Card-driven games | The cards are just random number generators (draw it, play it); there is no freedom to "build" or "cut" |

A self-check question: if you replaced the card system with a skill tree, would the game still stand? If it would, you have made something wearing card skin.

### 1.2 Core Loop (the Verb Ring)

`play cards in combat → resolve rewards → pick one of three or visit the shop → the deck grows stronger → enemies grow stronger → until you clear the run or die`

The loop rests on just two premises: every card pick the player makes can be explained (why give me these three?), and every failure can be reviewed (which decision was wrong?). Without the first, building turns into opening blind boxes; without the second, winning and losing both feel like luck.

Pacing has three layers: the turn (10–60 seconds, allocating energy), the fight (5–10 minutes, executing a plan and adapting on the fly), and the run (30 minutes to 2 hours, deciding on a build direction). Every layer needs decisions; the moment a layer has none, players start fast-forwarding.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **A sense of command over the build**: wins you can explain, losses you can accept. The cards were chosen by you; the deck was assembled by you.
2. **The combo discovery moment**: two ordinary cards suddenly click together, and the player "invents" a combo on their own — the most valuable experience this genre has to offer.
3. **The tension of resource decisions**: energy is limited each turn; playing A means not playing B; you are always a step short of perfect.
4. **Every run different**: the same rule set grows different decks and different play patterns.
5. **Transparent information**: enemy intents, draw counts and damage previews are all visible, so a losing player can point to the step where they went wrong.

Anti-patterns (stop and fix the moment one appears): losses get blamed on "I just couldn't draw the right cards" while the player feels powerless; after several runs in a row, the player cannot say how this run differed from the last.

Benchmark titles (play them yourself before breaking them down):

| Title | What to take from it | Boundary reminder |
| --- | --- | --- |
| Slay the Spire | Transparent information (intents, draws and the route map all open) and the numeric baseline for single-player card games: 3 energy, draw 5 per turn, pick one of three after combat | Large amounts of content and numbers; balance testing is expensive |
| Magic: The Gathering | The color wheel and the mana curve, the semantics of rarity, and lands as the classic answer to resource systems | Paper cards and the tournament format system are complex; don't copy the whole set |
| Hearthstone | Digital game feel, low-barrier packaging, single-card showcase | Random effects are a double-edged sword; too much variance eats trust |
| Monster Train | Decision pressure from multi-lane defense and synergy-axis design | High complexity up front; teaching costs are large |
| Balatro | The thrill of multiplicative math, with "remodeling the deck" as the core | A number explosion must come with strict caps |
| Night of the Full Moon | Level-based packaging and mobile pacing for single-player card games in the Chinese market | The power curve runs flat; weak for hardcore tastes |

## 3. Design Essentials

### 3.1 The Card Design Framework: cost × effect × rarity

Start by setting the smallest possible ruler: the effect budget. In the design doc, each card gets only three lines: cost, baseline effect size, attached cost. The baseline (reference values): 1 energy is worth roughly 6 damage, 5 block, or 1 card drawn.

| Cost | Effect budget | What may appear | Attached cost |
| --- | --- | --- | --- |
| 0 | About half a 1-cost effect | Card cycling, small buffs, conditional triggers | Must carry a hidden price: exhaust, HP loss, once per turn |
| 1 | 1 unit | Basic attacks, block, draw 1 | None |
| 2 | About 1.8–2.2 units | Dual-effect cards, medium-strength single-target | None, or minor |
| 3 and up | 3–4 units | Highlight cards, board clears, key win conditions | The risk of a dead card in hand is itself part of the cost |

The deck's cost curve matters just as much: workhorse cards cluster at 1–2 cost, and 3+ cost cards are win conditions, not daily rations. Drawing two opening turns in a row with nothing playable is bad-review-grade frustration — plug that hole in the budget table first.

Rarity is not a power label; it is a gate on "radius of behavior": common cards add numbers, rare cards change behavior (applying a status on hit), epic cards change rules (statuses spread, costs can be substituted). Distribution reference: about 60% common, 30% rare, 10% epic; an epic card appears 0 to 1 times per run. Text discipline comes down to two rules: one card does one thing (if the description runs past two lines, split the card or fold it into the keyword table); a card the player cannot understand does not exist (one shared wording template across the whole card pool).

### 3.2 Resource and Draw Systems: energy, hand and discard-pile loops

The four piles (draw pile, hand, discard pile, exhaust pile) are this genre's engine. Lock down five numbers first (reference values):

| Parameter | Common value | Notes |
| --- | --- | --- |
| Energy per turn | 3 | A global constant; growth goes to cards and relics, not to the turn count |
| Draw per turn | 5 | Paired with 3 energy: you draw more than you can play, so trade-offs appear naturally |
| Hand limit | 10 | Overflow is discarded; prevents unlimited hoarding |
| Starting deck | 10–15 cards | You can cycle through the whole thing once within three to five turns |
| Single fight | 3–6 turns | Past 8 turns it starts to drag |

Loop math — do the arithmetic first, test after: with a deck of N cards and 5 drawn per turn, a given key card appears once every N/5 turns on average; when the deck bloats from 15 cards to 30, key combos come together at half the speed. The card-removal channel matters as much as drawing: cutting one junk card raises the density of every key card.

Discard-pile details: when the draw pile runs empty, shuffle the whole discard pile back in — that is the standard cycle, and it also gives each fight a soft cap; exhaust is the balance valve, keeping "played and gone" power cards out of the loop and cutting off fuel for infinite loops; targeted search is a scarce good — give too much and randomness stops mattering, so 1 to 2 per run is enough; energy is the global pacing knob, and changing it means recalculating the value of the entire card pool — a late-game growth to a 4-point cap is doable, but touch it at most once or twice per project.

### 3.3 Building and Combos: synergy, the card pool and deck hygiene

Build the tag system before you write cards: define 8–12 mechanic tags across the whole card pool (vulnerable, poison, shield, energy, draw, summon, exhaust, combo), and hang at least one tag on every new card; a card with no tag is an orphan card, and an orphan card is tomorrow's dead card.

Combos come in three tiers, each with its own job:

| Tier | Shape | Example | Design job |
| --- | --- | --- | --- |
| Two-card combo | Card A plus card B; together they pay off more than used separately | Apply vulnerable first, then a multi-hit attack | Let the player taste the sweetness of combos in the first five hours |
| Engine | Steady resource output every turn | Draw converts into energy, energy converts into more draw | A mid-game build goal; its strength must stay controllable |
| Infinite loop | Net resource growth that never closes | Cost and draw feed each other | Either seal it shut, or make it a rare once-per-run reward |

The five-piece card-pool control kit: the rarity gate (§3.1); handing out cards by weight in the pick-one-of-three rather than at equal odds; pity weighting when combo pieces fail to appear again and again; a per-card copy cap of 1 to 2, so nothing bets everything on one card; and removal and upgrade outlets, so the deck has subtraction to do.

Two disciplines: prefer 20 combos each 30% stronger over 1 combo ten times stronger — the first is an ecosystem, the second a single solution; when a broken combo appears, decide first whether "a part is too strong" or "the interaction is too strong" — a strong part gets cut, a strong interaction gets conditions first (limited turns, limited targets) before you consider cutting the interface. For a single-player roguelike, a deck that fluctuates between 20 and 35 cards is healthy; don't let it bloat without end.

### 3.4 Balance and Testing: how to find dead cards and broken combos

Build the data before you talk about balance. Every version should log at least four sets of numbers: each card's pick rate (the share of times it is chosen in the pick-one-of-three and the shop); each card's contribution to win rate (decks with it versus decks without it); the turn count and the player's HP-loss ratio per fight; and the distribution of where runs die (which floor, which fight, which enemy).

Decision rules (reference thresholds): a pick rate below 5% for two versions running with no significant win-rate contribution means a dead card — investigate in the order text, numbers, dominating card, and prefer a rework over simply adding numbers; a pick rate above 80%, or a win-rate contribution that stands alone, means a broken card — decide first whether it is a "component" or an "answer": an answer gets weakened, a component means examining the interfaces it plugs into; pair up high-tier cards two at a time in automated scans, and any of these three — net resource growth, over-the-line one-turn kills, being unpunishable by any enemy — goes on the blacklist immediately.

The testing toolbox, ordered by when to invest:

- Telemetry: do it first; local logs are enough — record the deck, each card played, win/loss and floor.
- Fixed-seed regression: after every round of number changes, run 20–30 fixed-seed games and compare the curves for jumps.
- Automated AI battles: batch-run games with animation-free fast resolution to find dead cards and overpowered cards; don't expect it to validate the fun for you.
- Human playtests: 3–5 outside players each week; watch the recordings for three things — where they get stuck, which card they curse, which two cards made them laugh. Data finds the anomaly; playtesting finds the cause.

Change discipline: one version touches one theme only (this batch tunes the poison system, say) — don't change 30 cards at once; community feedback is for locating problems, not a prescription — players are precise about "where it hurts," not necessarily about "how to fix it."

### 3.5 Single-Player Roguelike Cards vs. Dueling Card Games: two different blueprints

| Dimension | Single-player roguelike cards | Dueling card games (TCG and CCG) |
| --- | --- | --- |
| Opponent | Designed AI encounters | Human players |
| When you build | Gradually during the run, picking cards after combat | Assembled in advance, before the match |
| Card sources | Drops, shops, events | Collecting, crafting, trading, pack opening |
| What you balance | Matching your own encounter curve | The metagame and match win rates (45%–55% is the common target) |
| Balance tools | Direct number changes, card reworks | Bans and restrictions, set rotation, counter-cards |
| Source of randomness | Draw randomness plus events; controllable | Draw randomness plus opponents; uncontrollable |
| Content lifetime | New characters, events, difficulty tiers | New card sets, new seasons |
| Engineering focus | Resolution system, data tables, saves | Server authority, matchmaking, anti-cheat |

Realistic advice for small teams: for a first card game, favor the single-player roguelike form. Its balance target is an environment you designed yourself, and testing and tuning all happen locally; dueling card games are live-service products where servers, matchmaking, anti-cheat and a season cadence are all non-negotiable — not a starting option.

In the dueling version, the card system itself is only the first 20% of the work; the other 80% is online and live-ops engineering — details in the Programming Handbook. The single-player version is cheap to validate: whether the card pool is fun has nothing to do with servers, platforms or outside opponents, so answer that question first.

## 4. Technical Essentials

**Make cards data, not code**

- Define a set of "effect atoms": deal damage, gain block, draw cards, apply a status, exhaust, and so on; a card equals a data combination of several atoms plus targeting rules plus trigger conditions.
- Framework goal: a new card never changes code. The designer fills in three columns (cost, target, effect sequence) and restarts to go live. In projects that can't reach this, every late-stage card turns into a programming schedule item.
- Exceptions go to unique mechanics only: the whole pool may contain 5–10 special cards that need code, but flag them individually and assess the maintenance cost.

**The resolution system is the heart**

- The effect queue and resolution order must be deterministic: play the card, enter the queue, resolve one by one, trigger chains, play animations. Keep logic and presentation separate — finish resolving before playing animations, or long combos get dragged down by animation and bugs hide inside the animations.
- Multiple triggers in the same timing window must have an explicit order (on play, at end of turn, on taking damage) and be written into the in-game reference; players only dare to attempt long chains when they can predict them.
- Replays: recording "seed plus action sequence" for each fight reproduces it fully — the common foundation for debugging, balancing and anti-cheat.

**Saves and in-run state**

- The state of a run (deck, relics, map seed, current fight and each pile) must serialize as a whole, so players can quit and resume at will; a crash swallowing a run is the highest-grade trust incident in this genre. Updates must tolerate old runs: new fields get default values, and when the structure changes drastically, let players update only after the old run has resolved.

**UI and input — half of a card game's feel lives here**

- The fanned hand, drag-to-play, targeting guides and hover previews (the result after damage and statuses resolve) are the baseline; layout and readability once the hand passes 7–8 cards is a common point-loser — design it early, and design mouse, touch and gamepad separately; don't expect one layout to serve all.
- Accessibility: pair color with shape and text markers (status icons must be distinguishable by shape alone), and let damage numbers and status stacks be enlarged.

**Performance and presentation**

- Pool all VFX and floating numbers; with resolution decoupled from animation, long combos must allow speed-up or skipping — add a speed toggle during testing; after launch it becomes a hard requirement for veterans. Give each effect atom one animation template and build special cards separately; don't let every card drive its own programming request.

**If you build the dueling version, three more pieces of engineering**

- Server authority: the client submits only intents; all resolution happens on the server; random numbers are handed down by the server and never exposed to the client early (anti-prediction and anti-cheat).
- Reconnect by replaying the action log, not by serializing the whole battle state.
- Matchmaking, seasons and the reporting system are planned up front on the live-ops cadence — see the Programming Handbook and the Production Handbook.

## 5. Content Volume and Workload Reference

Content checklist for the first release of a single-player roguelike card game (reference magnitudes; calibrate to your own pace):

| Content | First playable version | Full-version reference | Notes |
| --- | --- | --- | --- |
| Cards | 40–60 (single character) | 200–300 (2–4 characters) | Full cost of 0.5–2 days per card, depending on how new the mechanic is |
| Relics and passives | 20–30 | 60–100 | Reuse effect atoms; low marginal cost |
| Enemies | 8–12 | 25–40 | One readable intent template per enemy |
| Elites | 2 | 8–12 | One or two per floor |
| Bosses | 1 | 3–5 | One per floor; reworks are expensive |
| Events | 10–15 | 30–50 | Text plus options plus rewards; low cost, high return |
| Level structure | 1 floor, 3 nodes | 3–4 floors | Node counts designed around 30–90-minute runs |

Workload magnitudes (solo developer, existing engine experience):

- Combat and resolution framework in shape: 2–4 weeks.
- One new card (reusing existing atoms): 0.5–2 days from design to copy, icon and testing; a card that introduces a new mechanic adds another 1–3 days.
- A single character's first 40–60 cards: 1–2 months.
- Number balance runs throughout, with a concentrated 1–2 month sprint at the end; the first playable loop overall takes 3–6 weeks, and reaching 1.0 solo takes 8–18 months (reference).

Text and art: each card needs an icon, a card frame and a play effect — a simplified art style (pixel, silhouette, single-color symbols distinguished by palette) keeps art spending very low; text is what players read most, three drafts on a description is normal, so put "reads smoothly" into the acceptance criteria.

## 6. How to Start the First Prototype

Goal: in 2–3 weeks, build the minimal loop that makes you want one more fight after finishing one — single-player only; don't touch art, story or saves.

1. (Half a day) Whiteboard combat: 3 energy, a 5-card hand, 10 hand-written cards (three atoms: 6 damage, 5 block, draw 1), two enemies with intent display, no animation, resolution shown as log text.
2. (Half a day) Get the four piles running: draw pile, hand, discard pile, exhaust pile, shuffle back when empty, hand limit. At this point the engine is installed.
3. (1–2 days) Move cards into a data table: one row of data per card; new cards only edit the table. While you're at it, write one test card to verify "it goes live without touching code."
4. (1 day) A pick-one-of-three reward after combat and a deck viewer; every card in the deck must fit within two screens.
5. (1–2 days) A mini route of three nodes: fight, elite, boss, with the results taking you back to the hub.
6. (1 day) Telemetry: card-by-card plays, turns per fight, win/loss and cause of death, written to a local log.
7. (2–3 days) Make two cards that click together (apply vulnerable plus a multi-hit attack, say); add no hints and see whether testers assemble it themselves.

Playtesting and acceptance (all observable):

- Find 5 people who have never played, and record only three numbers: how many turns the first fight took; how many spontaneously said "next run I want to try..."; whether anyone voluntarily clicked play-again within 10 seconds of dying.
- Without hints, testers can articulate one idea about their deck by the second run, and at least half of them spontaneously play a two-card combo within two runs.
- With all art removed and a pure-text interface, testers are still willing to play three runs in a row.

Do not build during prototyping: multiple characters, card upgrades, relic shops, daily challenges, online play, achievements. These are amplifiers, not foundations.

## 7. Common Pitfalls

1. Numbers pulled out of thin air, no effect budget table: cards stop adding up against each other and balance is down to gut feel. Set up the ruler from §3.1 first.
2. Dead cards left alone: 30% of cards see no picks and that content was built for nothing. Clean house regularly with pick-rate data; prefer reworks over adding numbers.
3. A deck that bloats without end: with no removal channel, key cards never show up and building degenerates into collecting.
4. Rarity equals power: rare cards are mindlessly strong and picking cards becomes grabbing cash. Rarity should control radius of behavior.
5. The infinite combo discovered only at launch: resource caps and simulation testing were missing. Put the hand limit, exhaust and cost ceilings in place first.
6. Enemies with no intent: players cannot plan their turns and combat becomes checking answers. Showing intent is basic courtesy.
7. Fights that run too long: ten minutes starts to feel normal, a run lasts two hours, and a mid-run loss stings too hard. Build 3–6-turn fights first.
8. Randomness crossing the line: damage and targets all random, wins and losses decoupled from decisions. Randomness should land on "what choices you are offered," not on "whether the result was right."
9. Unskippable animations: a long combo plays for 30 seconds and testers and veterans alike churn. Add a speed toggle and queue the animations.
10. A small team starting with PvP: servers, matchmaking, anti-cheat and season operations — none can be skipped. Build the single-player version first to validate the cards themselves.
11. Copying cards but not systems: the card ideas get copied but not the numeric budgets, card-pool control and balance process, and the result cannot be tuned.
12. Combat only, no route: shops, events and the route map are all building decisions — remove them and the game is just a card-playing simulator.
13. Balancing against community screenshots: whoever gets screenshotted gets nerfed, and the mess grows. Use telemetry and fixed-seed regression to locate problems; community feedback is for finding symptoms.
14. Opaque text: a card you cannot understand does not exist. Build a keyword table per mechanic and hold the whole pool to one set of wording.

## Further Reading

- Game Design Handbook: general methods for core loops, number curves and randomness design — corresponds to §3 here.
- Programming Handbook: implementation details for data-driven design, resolution systems and saves — corresponds to §4 here; the server side of the dueling version is in there too.
- Production Handbook: scope control and scheduling; its marginal-cost assessment for card content pairs with §5.
- Case Studies: case breakdown methods — read it against the pitfall list in §7.
- Homework: play 10 hours of Slay the Spire and 10 hours of Magic: The Gathering (or similar titles), and record two things: "which combo did you figure out yourself" and "which card did you never use once." The second answer is the real-world version of the dead-card problem.
