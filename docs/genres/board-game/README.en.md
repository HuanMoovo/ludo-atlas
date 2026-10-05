# Ludo Atlas · Genre Handbooks · Board Game

> **Genre Handbooks · Volume 3**. Positioning: moving rules that already work on a physical tabletop onto a screen. The gameplay doesn't change; what changes is who executes the rules — which parts the system resolves automatically, and which parts must stay with the player. That dividing line decides whether the product succeeds.
> Companions: Game Design Handbook (core loops and strategic depth) · Programming Handbook (data-driven systems and resolution) · Multiplayer & Backend (rooms, turn sync and reconnection) · Case Studies (samples of adaptation successes and failures).
> This page carries no external links; benchmark titles are limited to widely known digital editions and chess/Go apps, and the numbers are common magnitudes — calibrate against your own project's measurements.

---

## 1. Positioning and Core Loop

In one sentence: board game digitization is **the engineering work of automating rule execution**. The original's strategic depth already holds; what you deliver is execution speed, zero disputes, play-anytime availability and AI opponents; treating the board game as raw material for reinvention (jamming in real-time controls, for instance) strays from the genre. The loop's beat is the turn, not the second: there is no game feel to tune, and the fun comes entirely from decision quality — options must be clear, consequences predictable, information transparent (show what should be public, hide well what should be hidden).

Core loop:

`read the position → list the options → decide → system resolution → opponent action → new position`

Drawing boundaries with neighboring genres:

| Neighboring genre | Boundary |
| --- | --- |
| Traditional card and tile games (mahjong, poker) | Also "rules already fixed, engineering in automation," but card games lean far more on psychology and randomness; their product and live-ops systems are a separate account |
| Trading card games (TCG) | Card-pool economy and match balance are a different engineering problem; board game digitization does not operate a card pool |
| Social deduction (Werewolf-style) | The core is speech and deception, with rules accounting for a small share; this page only covers the rule-automation half |
| Board game sandbox platforms | Rules are not automated and pieces can be moved freely; what's sold is a simulator plus a component library — a platform product |

A self-check question: if a human referee executed all the rules in the system's place, would the game still hold up? If yes, the rules themselves are sound and your job is to automate them; if not, fix the rules first — don't start building.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Zero rules disputes**: legal actions are validated by the system and resolution is executed by the system; players never flip through the rulebook or act as referee.
2. **Decision density doesn't shrink**: digitization compresses resolution time, not thinking time; not one decision that was worth something in the original may be automated away.
3. **Controllable pacing**: animations skippable, the AI on a thinking budget, replays always available, and match length predictable.
4. **Stoppable at any time**: saves, reconnection and asynchronous matches mean "no time today" does not equal "abandon the game."
5. **An opponent always there**: beyond matches against real people, AI opponents guarantee there is always a game to play.

Benchmark titles (play them yourself before breaking them down; watching video won't teach you the pacing):

| Title | What to learn from it | Boundary reminder |
| --- | --- | --- |
| Catan digital edition | The benchmark for fully automated Euro-style board games: legal-move highlighting, resource resolution, trading and building expressed through UI | Licensing and IP ownership are complicated (§3.5) |
| Monopoly digital editions and the domestic Richman series | Digital migration of a mass-market IP, localized variants and presentation packaging | Simple rules; the fun depends heavily on the people at the table |
| Tian Tian Xiangqi | The nationwide sample of xiangqi digitization: human-vs-AI play, endgame puzzles and replays | Chess and Go AI is an engineering project of its own (§3.3) |
| Fox Weiqi, Tygem | Mature forms of online Go: ranked play by kyu/dan, replays and spectating | Go AI has a high bar; read the license before integrating an open-source engine |
| Sanguosha Online | A sample of a board game moving to an online room system: role-based gameplay, room social features and a tournament system | Overlaps with the social deduction and TCG lines |
| Tabletop Simulator | The other pole: zero rule automation, a physics sandbox plus player self-discipline | Validates a platform, not the productization of rules |

## 3. Design Essentials

### 3.1 The Automation Dividing Line: Who Executes the Rules

Start with one criterion: automate what is disputed, error-prone or easily forgotten; leave what involves promises, negotiation or performance to the players.

| Step | Suggested handling | Rationale |
| --- | --- | --- |
| Legal-action validation | Fully automatic; highlight selectable options in the UI | Removes disputes and misclicks, and doubles as an entry point for teaching |
| Turn and phase advancement | Fully automatic, with one-click skip | Kills the "whose turn is it" and "what do we do in this phase" conversations |
| Resources, damage, scoring | Fully automatic, with the process reviewable afterward | The part of a board game most easily miscounted |
| Hidden information (hands, roles, decks) | System-managed | Anti-peeking is a native digital advantage (for where to hide it online, see §4) |
| Trades, negotiation, alliances | Left to the players | The verbal game is the fun itself — don't write it into an evaluation function |
| Rule variants and house rules | Make them pre-game configuration | House rules differ wildly from table to table |

One discipline: never force manual play for what can be automated, but allow manual when the player wants it (manual resolution in replays and a slow mode are legitimate needs). Speed is also the first experience dividend: skippable animations, accelerated AI turns, instant resolution — veterans often pick the digital edition just to save those ten minutes of bookkeeping.

### 3.2 Rules Engine: How Far to Take Data-Driven Design

Honest layering is more practical than the slogan of "fully data-driven":

- **Content layer — data-driven wherever possible**: cards, pieces, boards, scenarios and events all go into tables; one component equals data of "trigger condition + targeting rules + effect sequence," and new content needs no code changes. The approach shares roots with card games; the Programming Handbook has the full treatment.
- **Flow layer — code is acceptable, but keep it contained**: for skeletons like the turn flow, phase order and victory conditions, full configuration is often a trap — its expressive power can't keep up with real rules, and every change takes three detours. Hard-coding the skeleton is fine; the key is to centralize rule decisions in one module that both the UI and the AI ask for answers.
- **Variant layer — configuration is mandatory**: ruleset versions, house-rule switches and optional expansions enter the game setup as match parameters and are written into saves.

Legal-move generation is the engine's central API: given a state, return all legal actions for the current player; UI highlighting, AI decisions, server validation and teaching hints all reuse it — get this one function right and four places get easier. The event log carries four jobs at once: input for animations (resolve first, animate after), data for undo and replays, credentials for reconnection, and evidence for online anti-cheat; one log entry per action is a habit to build on day one.

### 3.3 AI Opponents: Search, Heuristics and Difficulty

Handle them in three tiers by how solvable the game is:

| Situation | Mainstream approach | Notes |
| --- | --- | --- |
| Perfect information, manageable state space (chess and Go) | Search methods: alpha-beta pruning or Monte Carlo tree search (MCTS) | The bulk of the work is the evaluation function and the performance budget |
| Imperfect information (hidden cards, hands) | Sample-then-search (fill in the unknowns, then search), or heuristics directly | Anything the AI "shouldn't know," it must not know |
| Strategy board games with complex rules | Heuristic scoring; take the highest score | A low ceiling but cheap; "good enough" is the norm |

The minimal version of heuristic scoring: immediate-gain weights plus resource and position weights, plus a small random perturbation; the perturbation isn't slacking off — it keeps the AI from always taking the same path. Difficulty tiers come from three transparent knobs, not cheating: search depth or thinking budget, leniency of the evaluation function, and the size of the random perturbation. Cheats like reading hidden information or conjuring resources from nothing are forbidden — players will notice, and once trust collapses you lose everything.

Engineering discipline: the AI has a thinking-time cap (a common target is a move within 200–800 ms per step); on timeout, play the current best; run computation on a background thread or separate process — never freeze the UI. Spending compute on "fast and human-like" is worth more than spending it on "slow and hard."

### 3.4 Turn-Based Online Play and Asynchronous Matches

Board game multiplayer is an order of magnitude simpler than real-time action games: no client prediction or lag compensation needed — but there are three modes to choose from:

| Mode | Scenario | Implementation points |
| --- | --- | --- |
| Synchronous rooms | Friend games, competitive games | Everyone in the room is online; the server authoritatively validates every action; when the turn timer expires, auto-act or take over |
| Asynchronous matches | Casual, mobile | The match lives on the server; each move is logged and pushed as a notification, and players come back to continue anytime |
| Local hot-seat | Offline, shared screen | Players take turns on one device; watch the masking of hidden information and the hand-off prompts |

A recommended data model: a match equals a fixed seed + rules version + command log. Turn-based rules are discrete, so determinism is easy to guarantee, and restoring the position at any step only needs a log replay; reconnection, undo, replay, spectating and asynchronous mode all feed on the same scheme. The determinism pit of "command replay" that plagues real-time genres barely exists here — a genre dividend.

For service layering (account auth, rooms and lobbies, matchmaking, leaderboards, anti-cheat and the cost ledger), see Multiplayer & Backend: the real-time sync stack is mostly irrelevant; what applies is its service checklist, anti-cheat (§7) and cost accounting (§8). A small team can start with "lobby + rooms + friend invites," leaving ranked play and seasons until after validation.

A match must carry a rules version number: after a version update, in-progress old matches continue to completion under the frozen old rules — otherwise one balance update destroys every unfinished match and replay.

### 3.5 Licensing and Original Design: Two Roads, Two Ledgers

**Licensed adaptation**

- Gameplay rules themselves are usually not protected by copyright; what is protected is names, art, text, characters and specific expression; trademarks and occasional mechanic patents are two separate lines — defer to Legal, Patents & Competition for the judgment.
- Clauses to negotiate: scope of name and character use, the redraw boundary for art and text, term and renewal, whether adapted rules may be changed, and the revenue-split model; original rights holders are often hardline about whether digital-edition rules may be altered.
- "Copy it with a new name if the license doesn't come through" is a high-risk route: trademark and art enforcement wins these cases every time, and community reputation collapses first.

**Original rules**

- Validate on the tabletop first: paper cards, pieces and handwritten rules cost days, making tabletop testing the cheapest prototype tool. If the rules don't run smoothly on a table, digitization won't save them.
- Original board games demand real design skill (balance, combination depth, length control); without the trust of a classic IP behind you, start small with a single mechanic.

## 4. Technical Essentials

**State model and replay**

- States support snapshots: actions apply to a state to produce a new state; board game states are usually only tens to hundreds of KB, so take full snapshots and keep undo and rollback simple — don't do incremental optimization ahead of need.
- Separate state from presentation strictly: the rules layer doesn't know animation exists; the animation layer consumes the event stream.
- Use a fixed seed for randomness, or write each step's random results straight into the log; resolution must never read the system clock.
- Persist the event log: seed + rules version + command sequence equals a full reproduction; debugging, undo, reconnection, spectating and anti-cheat all share this one dataset.

**Online architecture** (details in Multiplayer & Backend)

- Server authority: the client only submits "what I want to do"; legality validation and resolution happen on the server; hidden information exists only server-side — shipping hands and decks to the client early is handing out cheating tools.
- Client-side highlighting is a hint, not a verdict; protocol encryption and anti-replay follow the general practices in (Multiplayer & Backend §7); the replay's rules version must match the match record, and updates coexisting with old matches is a required question (§3.4).

**Presentation layer**

- The event stream drives the animation queue, resolving first and performing after; animations are skippable and speed-up-able, and the network layer is decoupled from the presentation layer.
- Design input per platform: touch is taps and drags (with mis-touch tolerance on drags), desktop is hover previews (payoff and result), gamepad is focus navigation; the board must zoom and pan, cells and coordinates are labeled, and destructive actions (discarding, confirming a trade) get a second confirmation.
- Accessibility: distinguish sides by shape and texture as well as color; font size and contrast adjustable.
- Replay UI: move history, step jumping, marking key positions. Replay is a long-term retention feature and the best teaching tool.

**AI engineering**

- Keep computation off the main thread (background thread, separate process, or server-side); a hard cap on the time budget; the player is allowed not to wait for it.
- Seed the AI's randomness with a fixed seed, so replays can explain "why it made this move."

**Saves and telemetry**

- A save equals seed + command log + rules version; cross-device cloud saves defer to the server; the minimal telemetry set: match length, turn count, AI difficulty usage rates, illegal-action and abnormal-exit logs — after launch, field problems can only be argued from logs.

## 5. Content Volume and Workload Reference

The following are common magnitudes for projects of this kind, for scope estimation — not a commitment.

| Project shape | Content scale | Timeline scale | Notes |
| --- | --- | --- | --- |
| Rules prototype (offline + one AI tier) | 1 ruleset, 1 board | 2–6 weeks | Rules and AI split the work half and half |
| Small original board game, digital edition | 1 ruleset, 20–40 components, 3 AI tiers | 2–5 months | UI and animation are the hidden bulk of the cost |
| Classic licensed adaptation (with online play) | All original components and expansions, rooms and live-ops systems | 8–18 months | Licensing, legal and live-ops costs counted separately |
| Sandbox board game platform | Component library plus editor | 1–2 years and up | A platform product; content comes from the community |

Magnitude anchors (solo developer with engine experience):

- Digitizing a single component (reusing existing rule primitives): 0.5–2 days; introducing a new primitive adds 1–3 more days.
- One heuristic AI tier brought to "acceptable to play against": 3–10 days; a chess/Go search AI brought to a competent level starts at 1–3 months — or integrate an open-source engine, after reading its license and terms first.
- The online trio (rooms, asynchronous play, reconnection): 2–4 months; the offline loop, 3–6 weeks.
- Estimate animation and staging by action type, not by component: a dozen-odd action types usually cover ninety percent of the content, and 1–3 days of polish per type is the norm.

## 6. How to Start the First Prototype

Goal: a complete, playable offline board game with one AI tier in 2–3 weeks — no online, no art.

1. (1–2 days) Tabletop self-test: run the current rules for 3–5 games with paper cards and pieces, and log every moment where "the rules don't say clearly here" — that list is your automation requirements sheet.
2. (2–3 days) Plain-text core: state + legal actions + resolution, hot-seat play turn by turn in the command line, and illegal actions must be blocked.
3. (2–4 days) Event log and full-match replay: every step replayable. No log, no next step.
4. (3–5 days) UI pass: board, pieces, action highlighting, basic animation (movement and fades are enough), skippable.
5. (3–5 days) One heuristic AI tier: a 200–800 ms thinking budget, able to play a full match.

Acceptance criteria (all observable):

- Five people who have never played learn a full game within 10 minutes, with no verbal explanation of rule details.
- Zero rules disputes within a match: nobody needs to ask "is this move allowed?"
- The AI never makes the player wait more than 1 second; quitting mid-match and resuming works.
- With all art removed and a text-only interface, testers still ask for another game unprompted.

Not during prototype: online, ranked, achievements, multiple AI tiers, localization, skins. These are amplifiers, not foundations.

## 7. Common Pitfalls

1. **Building the UI before the rules are settled**: change a rule and all the UI and animation work is void. Get the rules running smoothly on paper first (§6, item 1).
2. **Over-automation**: negotiation, promises and performance all automated away, and the board game turns into a button-clicking pipeline. For the criterion, see §3.1.
3. **AI cheating**: reading hidden information, conjuring resources. Players notice, and lost trust means lost everything; tune difficulty with parameters, not cheats.
4. **AI analysis paralysis**: a frozen UI, or ten seconds of waiting on every move. Thinking budget, background thread, play-current-best-on-timeout — none of them can be skipped.
5. **Rule logic written into the UI**: resolution mixed into button callbacks and animation events; adding one house rule means touching ten places in code. Legal-move generation and resolution must be independent modules (§3.2).
6. **No logs or replay**: problems can't be traced, and undo, reconnection, spectating and anti-cheat all come to nothing. Have it from day one.
7. **Online before offline**: the complexity of rooms, sync and live-ops will drag the prototype to death. Make the offline loop work first.
8. **Hidden information sent to the client early**: hands and decks can be dug out on the client. In an online build, hidden information can only live server-side.
9. **Matches without a rules version**: one update voids every in-progress match and replay (§3.4).
10. **Vague licensing**: copying names, art and text outright, or assuming "a new name makes it fine." Run it past the Legal, Patents & Competition first.
11. **Designing for one screen only**: boards are extremely sensitive to screen size; with no budget for zoom, pan and information layering, the phone experience will fall apart.
12. **Forgetting to ask "why play the digital version"**: play anytime, an AI practice partner, painless resolution, friends across distance are the answers; align features and positioning with those answers — don't trace the physical experience onto a screen unchanged.

## Further Reading

- Game Design Handbook: core loops and strategic-depth design; read it first for the judgment call on whether the rules themselves are worth digitizing.
- Programming Handbook: implementation details for data-driven design, resolution systems and saves — the full expansion of §4.
- Multiplayer & Backend: rooms, accounts, matchmaking, anti-cheat and the cost ledger — the division-of-labor counterpart to §3.4 and §4.
- Legal, Patents & Competition: the boundary between gameplay and expression, trademarks and mechanic patents, licensing contract terms.
- Case Studies: methods for breaking down cases; cross-read while going through the pitfall list in §7.
- Exercise: pick a physical board game you know well, without looking at any digital edition, write its rules as an automation requirements sheet of no more than 20 items, and mark the items you decide not to automate. That sheet is your entry point into understanding this genre.
