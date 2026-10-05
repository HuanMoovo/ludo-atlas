# Ludo Atlas · Genre Handbooks · TCG

> **Genre Handbooks · Volume 3**. Positioning: turn "collecting" and "battling" into a pair of loops that feed each other — it is only a TCG when both wheels turn at once; the battle gives collecting its reason, and collecting gives the battle its ammunition.
> Companions: Game Design Handbook (core loops and number tables) · Programming Handbook (data-driven design and resolution systems) · Multiplayer & Backend (server authority, matchmaking and economy security) · Live-Ops & Growth (seasons, card packs and long-term balance).
> This page carries no external links; benchmark titles are limited to widely known works, and the figures are common orders of magnitude — calibrate against measurement in your own project.

---

## 1. Positioning and Core Loop

In one line: a trading card game is the genre that **twists "collecting" and "battling" into a pair of loops that feed each other**. On the table a card is a battle tool; in the binder it is a collectible. Players expand the card pool through pack opening, crafting and trading, then build decks from that pool and bring them to the table to test.

The core loop written as a verb loop, with both loops turning at once:

`Collection loop: battles and quests earn currency → open packs or craft → the card pool widens → discover new combinations → want to try a new deck → back to battling`

`Battle loop: build a deck → get matched against an opponent → play cards and trade responses back and forth → win/loss resolution → review and adjust the deck → queue another match`

The two loops are each other's fuel: battling is the meaning of collecting (currency and goals only come from playing), and collecting is the ammunition for battling (the card pool decides what decks are possible). A product with only one wheel turning: collecting alone is a pack-opening simulator; battling alone makes collecting a mere shell.

Two preconditions: battles must be reviewable (on every key turn, the player can say what could have gone differently), and collecting must have a deterministic exit (crafting, pity, redemption — so spending has a target). Without the first, battles degenerate into comparing whose collection is more complete; without the second, pack opening degenerates into gambling. Pacing has three layers: a turn (half a minute to two minutes, resource allocation and card play), a match (commonly 5–20 minutes) and a season (weeks to months, new sets and rank resets). All three layers need decisions and freshness; the moment any layer stalls, players start fast-forwarding or leaving.

Drawing boundaries with adjacent genres:

| Adjacent genre | Boundary |
| --- | --- |
| Deckbuilding (single-player card games) | Building happens inside the run, the opponent is a designed level, and what you balance is your own level curve; in a TCG the deck is built before the match, the opponent is a real person, and what you balance is the whole-server metagame |
| Competitive card games (fully unlocked) | Also real-person battles, but collecting is not part of the main loop; in a TCG the collection loop is a second engine, and the card pool is itself content |
| Auto battlers | There is the build fun of a shared pool and lineup composition, but combat is fully automatic; in a TCG every play is a direct decision about hand cards, costs and timing |
| Traditional poker and mahjong | The deck is public and fixed, and outcomes rest on information and probability; in a TCG the cards are the player's private assets, and the outcome starts accumulating the moment you build the deck |

A self-check question: remove pack opening and card-pool growth, replace them with everything unlocked from the start — does the game still hold up? If the answer is "no", you are making a TCG; if it is "it still holds up", collecting is only a shell, your benchmark is fully unlocked competitive card games, and you can skip this page's dual-loop section entirely.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (ordered by priority):

1. **Expression and control at the table**: the deck is the player's own choice; winning brings the satisfaction of "I built this", and losing should be reviewable into "which play could have gone differently".
2. **The heartbeat of information play**: hand, board and an unknown opponent create guessing and probing; the suspense of holding one card back through a turn is tension unique to this genre.
3. **The sense of approaching completion**: the heartbeat of opening a pack, a pity counter closing in, a crafting goal reached; a new card can hit the table the day it arrives.
4. **Fairness and attributable outcomes**: card-draw randomness is intrinsic to the game, but comebacks cannot rest on randomness alone; a losing player should be able to say where the opponent was stronger, not that the opponent drew better.
5. **Long-term commitment**: new sets and seasons give a reason to come back next month; the metagame shows perceptible change every few weeks.

Anti-patterns: losing players broadly attributing defeat to "his cards are better than mine", or collecting for two months and finding they cannot keep up with the cost of mainstream decks. Once either becomes community consensus, retention collapses.

Benchmark titles (play them yourself before taking them apart):

| Title | What to learn |
| --- | --- |
| Magic: The Gathering | The full design of priority and the stack; the five-color wheel and color counters; the originator of format tiers and rotation; dual physical and online ecosystems |
| Hearthstone | Low-threshold digital packaging; the dual channels of pack opening and crafting; the live-ops cadence of rotations and balance patches |
| Yu-Gi-Oh! | High-density card text and a combo ecosystem; physical tournament operations; it also demonstrates the balancing problems that follow card-pool inflation |
| Pokémon Trading Card Game | The IP-plus-collecting mindset; starter preconstructed decks and offline events; physical and digital editions coexisting |
| Shadowverse | Digital-first seasonal operations; how the evolve mechanic reworks the resource model; a story wrapper to bring in new players |
| Marvel Snap | Short-match design (12 cards, 6 turns, three locations); per-match location variables; a mobile-first pace |

## 3. Design Essentials

### 3.1 Card Design: Effect Budget and Rarity Curve

Start by setting a ruler: the effect budget. 1 point of cost is roughly 1 unit of baseline value (one instance of damage, one point of stats; drawing a card is worth about two units), and each card gets only three lines in the design document: cost, effect size, attached condition. The budget table is the factory setting; measured metagame data is the final judge.

| Cost | Effect budget (reference) | What may appear | Attached condition |
| --- | --- | --- | --- |
| 1 | 1 unit | Basic units, small spells | None |
| 2 | 1.8–2.2 units | Workhorse pieces, small dual-effect cards | None or minor |
| 3–4 | 3–5 units | Tempo pieces, one-for-many trades | Usually needs a condition or target restriction |
| 5+ | High impact, turnaround potential | Finishers, board clears | Must have a prerequisite |

Rarity governs three things: collection difficulty, complexity budget and drama. Rarer cards may be more complex and more theatrical, but power and rarity may only be loosely coupled: the acquisition path for every mainstream deck's core pieces must be reachable (crafting price, preconstructed decks or events), or the competitive metagame becomes a paywall — the most expensive trust debt in this genre. Distribution reference (by cards per set): roughly half common, about thirty percent rare, and epic plus legendary about twenty percent; every top-rarity card needs a unique mechanic or presentation — it cannot just be a common card with bigger numbers.

Text discipline: one card does one thing (if the description runs past three lines, split it or fold it into the keyword list); establish the keyword list first, with a single wording template across the whole card pool; online there is no judge, so card text must survive one unambiguous reading by the rules engine — ambiguity gets amplified into disputes by the community.

Manage the power curve across sets: a new set's power floats around the current metagame baseline, and freshness comes from new mechanics and new combinations, not from higher numbers. Grow 10% stronger every season and in three years the early card pool is waste paper — a debt that can essentially never be repaid.

### 3.2 Card Pool Management: Formats, Rotation and Banned/Restricted Lists

The card pool is a TCG's long-term asset and its biggest liability; unmanaged, new players cannot get in and the metagame congeals for veterans. Three tools, used together:

| Tool | Content | Responsibility |
| --- | --- | --- |
| Format tiers | Standard (packs from the last one to two years) and Open (the full historical card pool) running in parallel | Standard protects balance and the new-player on-ramp; Open protects the value of players' assets |
| Rotation | Standard rotates old sets out on a schedule | Frees design space, caps the learning cost for new players, drives new pack sales |
| Banned/restricted list | Three tiers: watch list, restricted to one, banned | Emergency first aid for the metagame and concentration control; digital versions have an extra lever in numeric hotfixes |

Rotation discipline: announce the rotation scope one to two seasons ahead, giving players time to plan; rotation removes a card's strength in Standard, not ownership of the card. Refunds and compensation are executed as promised — one broken promise takes a year to repair.

How to use the banned/restricted list: anything solvable by numeric adjustment does not get banned; a ban is the last-resort emergency tool, and every one ships with an announcement that spells out why, whom it affects and what happens next. Digital has one more lever than physical (hotfixing numbers), so digital TCG balance runs on two tracks: bans and patches.

### 3.3 Battle Rules and Resource Systems

The resource model sets the tone for who wins and is the most immediately visible difference from competitors:

| Resource model | Representative approach | What you get | What you pay |
| --- | --- | --- | --- |
| Land-based | Magic: The Gathering | Resources enter deckbuilding and the draw, giving the greatest depth and expression space | Mana screw and mana flood are part of the design, and the barrier to entry is high |
| Automatic growth | Hearthstone | Smooth, mobile-friendly, quick to pick up | The resource dimension flattens; outcomes ride on cards and board trades |
| Fixed-cost short matches | Marvel Snap | Short matches, fast pace, suited to fragmented time | Depth has to be made up elsewhere, through locations and card effects |

Response timing decides the depth of the psychological game — this is an audience decision. With a full stack (Magic-style), you can act on your opponent's turn: cards go on the stack, both sides respond in turn, last in first out — maximum depth, and maximum engineering for rules and UI; simplified responses (Hearthstone-style, acting mostly on your own turn with a few triggered mechanics) are crisp and easy to learn, at the cost of the "fight back" layer. Decide who your target players are before choosing.

The win/loss vector must be graspable at a glance: main-unit health, deck exhaustion, location scoring, special victories — pick one or two as the main line and keep the rest as easter eggs; use the "empty turn" test to check decision density, and fix the pacing of any match where several turns in a row have nothing to do. Randomness discipline: card-draw randomness is part of the game itself, but in-match randomness (random effects, random targets) must be restrained. The principle is "randomize the options, not the outcomes", and audit the stock of random effects once per release.

### 3.4 Collection Economy and Pack-Opening Design

The dual channel is the foundation: packs give randomness and surprise, crafting gives certainty and goals, and both must exist at once. Packs alone let frustration accumulate into churn; crafting alone loses the ritual and the heartbeat. The two economies must be convertible (how many packs are worth how much crafting material), giving players a path they can calculate.

Pity and duplicate handling (reference values; publish them as fixed and never change them quietly): within the first 10 packs of each set, a top-rarity card is guaranteed; top rarity has a 20–40 pack pity, second-highest a 5–10 pack pity; and the rules for opening a card you already own (duplicate protection or material refunds by rarity) are stated up front.

The pack-opening presentation is this genre's "moment": revealing cards one by one, with rare-rarity effects and sound, is worth the investment; it must also be skippable — when a veteran opens dozens of packs at once, that is a hard requirement. The sense of approaching completion matters just as much: visible pity progress, trial channels for new cards (practice matches, preconstructed decks), so a new card can hit the table the day it arrives. Daily loop: daily and weekly quests provide steady free income so that "you can play without paying" holds true; pass-style long-term rewards bundle retention and payment — for the operations method see Live-Ops & Growth.

Compliance red lines: pack opening and gacha pulls are regulated in many places, and odds disclosure is a common hard requirement (including in major app stores' review rules); payments and playtime for minors have separate, explicit limits; some markets have stricter frameworks for randomized paid mechanics. Before release, check market by market — do not assume one scheme travels globally.

If you open player-to-player trading, bot farming, stolen-account fencing and money laundering will show up immediately — for the economy-security engineering see Multiplayer & Backend. Most digital TCGs replace trading with "craft and disenchant"; that is not laziness but risk management. The physical TCG secondary market gives cards their value retention and sense of ownership; digital versions have to fill that slot with certainty and commitments.

### 3.5 Balance and Testing: Metagame Data and Change Cadence

What you balance is the metagame, not individual cards. Every release records at least: each deck's play rate and win rate, individual cards' win-rate contribution, first-player win rate, match length distribution, and the number of mainstream decks four weeks after a new set launches. Target ranges (reference): deck win rates 45%–55%, first-player win rate near fifty percent; anything outside the range goes on the watch list.

Tool combination: a ladder data dashboard to find anomalies; bot matches on the rules engine for regression and crash testing — not a substitute for real-player data; a closed-test group (high-rank players playing the new set early) to find design holes and boring decks. Data answers "what is wrong"; people answer "what is not fun". You need both.

Change tiers: numeric tuning (digital only) → restricted to one (lower the concentration) → banned (emergency stop) → redesign (a text-level change, equivalent to reissuing the card). One change focuses on one theme, and the announcement spells out three things: what changed, why, and which data to watch next.

Cadence (reference): after a new set launches, let the metagame settle naturally for 2–6 weeks before the first balance adjustment; too frequent and players dare not commit to a deck; too sparse and a bad metagame burns trust. Physical has no patches, so ban announcements must land in one shot.

## 4. Technical Essentials

The engineering difficulty concentrates in five places: the rules engine, the response system, the server and hidden information, the economy service, and the content pipeline; the following is independent of engine choice — for general methods see the Programming Handbook, and for the full multiplayer and backend process see Multiplayer & Backend.

**Rules engine: state, events and resolution**

- Single source of truth plus an event queue: the game state (board, hand, library, resources, turn information) exists as one authoritative copy; every card effect hooks onto events and a timing table (enter play, death, turn start and so on) and resolves in a deterministic order.
- Atomic effects: damage, summon, draw and buff are built as data combinations, so new cards enter the table without code changes; the whole card pool keeps only a very small number of unique-mechanic cards that need code, each flagged with its maintenance cost.
- Resolution must be deterministic and replayable: the same seed plus the same sequence of actions produces the same result — the shared foundation of replays, reconnect and anti-cheat; logic finishes first, then animation plays from the queue, with speed-up and skip allowed.

**Engineering priority and the stack**

- The stack is the resolution loop, not a visual effect: played cards go on the stack, the two sides receive priority in turn, and once both pass, items resolve last-in-first-out, one at a time. The engine must be able to pause at any resolution point and accept new events — do not write it as "damage takes effect immediately".
- Response windows carry the highest networking and UI cost: waiting for a response needs time limits and a timeout policy (auto-pass, disconnect proxy), and mobile needs notification-style response design, or players will constantly miss their timing windows.
- If you choose a simplified response model (acting mostly on your own turn), the engine still needs hooks reserved for triggered effects, so adding mechanics later does not disturb the foundation.

**Server authority and hidden information**

- The client submits intents only (which card to play, which target to point at); all adjudication happens on the server. The opponent's hand, deck order and the random seed are never sent to the client. A TCG has exactly three cheat surfaces — seeing through hands, seeing the top of the deck, and automation scripts; keeping hidden information server-side closes the first two.
- Reconnect restores the match by replaying the seed plus the action log, not by serializing the whole match state; match records serve four uses at once — debugging, balance sampling, anti-cheat and community content. For the full ledger of matchmaking, ranks and anti-cheat see Multiplayer & Backend; the principle for new-player pools and bot backfill in off-peak hours is "rescue the experience, don't deceive the player".

**Server-side implementation of economy and pack opening**

- The server decides pack results and records them to the database immediately; the client only handles presentation. Each pack is one transaction, idempotent, uniquely numbered — any "send to the client first, record later" implementation becomes a pack-farming exploit.
- Account assets (card inventory, crafting materials, currency) need audit logs and customer-support tools; trading (if you build it) is a separate engineering track — listings, matching, risk control and account recovery are all indispensable.

**Content pipeline and hot updates**

- All card data (numbers, text, rules, card art references) goes into tables under version control; balance changes go out as numeric hotfixes and new cards ship as content packs — keep the two separate.
- Card art is the biggest asset cost: on mobile, download it on demand and split it into bundles, with the initial install carrying only basic cards; produce card faces and effects from templates, the same atomic approach as card design.

## 5. Content Volume and Workload Reference

The following are common magnitudes for comparable projects, for scope estimation only — not a commitment.

| Project form | Content volume | Timeline | Notes |
| --- | --- | --- | --- |
| Battle prototype | 40–60 cards, two preconstructed decks | 2–6 weeks | Paper plus greybox; validates only the rules and whether matches are fun |
| Single-player battler | 150–300 cards | 3–9 months | Opponents are AI; validates the collection loop and the card pool |
| Small online battler | 300–500 cards (2–3 sets at launch) | 1–3 years | Server, matchmaking and economy are all required |
| Live-service TCG | 100–250 cards per set, 3–4 sets a year | Ongoing investment | The content pipeline and live-ops cadence are the main body |

Conversion factors and the hidden ledger:

- Per-card cost: reusing effect atoms takes 0.5–2 days through design, copy and testing; the cost of introducing a new mechanic lands on the mechanic itself — add several days to one or two weeks. Illustration is outsourced per piece and is the card pool's largest external expense.
- Rules engine: a minimally playable match takes 2–6 weeks; the full version with responses, triggers and replay takes 2–4 months; the first playable loop (battle + pack opening + crafting, no seasons) takes 3–6 months, and a live-service 1.0 is often measured in years.
- The population ledger: matchmaking quality in competitive play degrades non-linearly as population drops — answer before launch which time slots can reliably fill matches.
- Scope discipline: the first card pool only needs to support complete decks for two or three styles; cutting cards is always cheaper than saving balance.

## 6. How to Start the First Prototype

Goal: answer one question in about a month — is fighting over these rules fun? Paper comes first; do not touch multiplayer, ranked, trading or seasons.

1. **Step 0 (2–3 days, before writing any code): paper prototype.** Print 30–50 cards (or write them on slips of paper), two preconstructed decks, and play by hand against a colleague. Bookkeeping is slow, but rule ambiguities and boring decisions surface immediately; TCG rules history is paper history — paper first, code second.
2. **Week 1: minimal rules engine.** Costs, units and spells, turn structure, win/loss conditions, text-only resolution, no art. It is supposed to be ugly.
3. **Week 2: a digital pool of 30–50 cards plus two preconstructed decks.** Play internally and record three things: the mana-screw rate, turns with no decisions, and the moments that made someone laugh.
4. **Week 3: a minimized collection shell.** Simulated pack opening (random cards plus pity and duplicate rules) and a crafting channel, to check whether the urge to "switch decks after a match" appears.
5. **Week 4: external blind test.** Find 5 people who have never played, teach the rules once, and observe: how long the first match takes, whether anyone changes their deck unprompted, and whether anyone wants another match.

Success criteria (all observable):

- With all art and sound removed, testers still want to play 5+ matches in a row.
- At least 3 of the 5 testers adjust their deck unprompted.
- The player who lost can say which card they want to swap for the next match.
- Match length lands at 10–20 minutes (the first session, including rules teaching, counts separately), resolution ambiguities shrink every day, and no ruling stays unresolved.

Not during prototyping: multiplayer, ranked, trading, seasons, story, mobile. These are amplifiers, not foundations.

## 7. Common Pitfalls

1. **A hard-coded rules engine**: every new card gets its own code, and card-pool growth becomes a disaster. Build effect atoms and a trigger-timing system first (§4).
2. **Building the server and pack opening first, with the rules unvalidated**: the whole backend is up, but matches are not fun. Get the match standing first (§6).
3. **Rarity equals power**: paying makes you stronger, and collecting crushes the competitive metagame. Rarity governs collection difficulty and presentation, not competitive power (§3.1).
4. **Power creep**: every season is stronger than the last, old card pools become waste paper, and trust goes bankrupt. New cards recharge through mechanics, not bigger numbers (§3.2).
5. **Bans with no warning and no compensation**: a core card is suddenly banned and players' investments are wasted. Announcement, reasons and refunds arrive as one package.
6. **No pity and opaque odds**: a double risk to reputation and compliance. Publish odds, fix the pity rules in writing, and keep the expected value calculable (§3.4).
7. **Hidden information sent to the client**: editing memory is enough to see through the opponent's hand, and the cheat barrier is zero. Keep hands, deck order and random seeds on the server (§4).
8. **Too many random effects**: stacking randomness for spectacle drains competitiveness. Randomize options, not outcomes (§3.3).
9. **Empty turns**: several turns with nothing to do and the player starts scrolling their phone. Decision density is an acceptance criterion for every card and every mechanic.
10. **Insufficient matchmaking population**: too few players to find opponents of similar skill, and the ladder experience collapses. Have the cold-start plan ready before launch (§5).
11. **Trading without economy security**: bot farming and stolen-account fencing destroy the economy outright. If your risk controls are not ready, replace trading with crafting (§3.4, Multiplayer & Backend).
12. **Copying cards without copying operations**: the card faces are copied, but the balance process, season cadence and community communication are not, and a year after launch the card pool is stagnant.

## Further Reading

- Game Design Handbook: general methods for core loops, number tables and probability design — pairs with sections 1 and 3 of this page.
- Programming Handbook: implementation details for data-driven design, resolution systems and saves — pairs with section 4 of this page.
- Multiplayer & Backend: the full ledger of server authority, matchmaking, anti-cheat and economy security; read it before building online play.
- Live-Ops & Growth: season cadence, card-pack operations and long-term balance — used together with §3.2 and §3.5.
- Indie Survival: scope control and scheduling; a competitive card game is a live-service product, so settle that account before you start.
- Pitfalls & Anti-patterns: common pitfalls in design and content production — read against section 7.
- Homework: play 10 hours of Magic: The Gathering and 10 hours of Hearthstone (or comparable products) and record three things: how your first deck came together (the reality of the collection loop), which loss you chalked up to luck, and which loss you chalked up to skill (information play and the sense of fairness).
