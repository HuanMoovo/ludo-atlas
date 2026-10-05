# Ludo Atlas · Genre Handbooks · Puzzle

> **Genre Handbooks · Volume 1**. Positioning: a development handbook for the genre whose main line is logic puzzles, running from mechanic budgets and wordless teaching through insight design all the way to hint systems and the level toolchain.
> Companions: Game Design Handbook (core loops and complexity budgets) · Level Design Handbook (teaching sequences and the whitebox workflow) · Case Studies (successful and failed projects) · Programming Handbook (state, data and toolchain).
> This page deliberately carries no links: a puzzle lives or dies in the few seconds when the player frowns in confusion and then relaxes in understanding, and that can only be observed in your own prototype — reading ten analyses is worth less than building ten rooms by hand.

---

## 1. Positioning and Core Loop

Puzzle games have exactly one core pleasure: understanding the rules and using them. Player progress comes not from stat growth or hand speed but from "I figured it out". Every design effort ultimately serves one thing: delivering the moment of figuring it out to the player at a steady frequency, in a clean form.

Draw the boundaries first. This page focuses on **logic puzzles**: the Sokoban, grid-logic, mechanism-room and rule-assembly family. Physics, word, match-3 and hidden-object variants only borrow the general principles here; their special practices belong to their own sub-genre pages. If clearing it depends on reaction time, it is closer to an action game — follow the Level Design Handbook's pacing and game-feel sections instead.

The core loop at three scales:

| Scale | Loop | What the player gets |
| --- | --- | --- |
| One attempt (10 seconds to 3 minutes) | Read the situation → form a hypothesis → put it to the test → read the feedback → revise | One piece of boundary information, or one small insight |
| One room (3 to 20 minutes) | A new element appears → trial and error until familiar → find the solution → clear it | Mastery of one new rule |
| One chapter (30 minutes to 3 hours) | Mechanic variations → combinations → a comprehensive exam → the chapter climax | A sense of command: I have learned this language |

Three fundamental differences from action genres:

- Failure comes from misunderstanding, not from execution error. The retry cost must be pushed toward zero: undo, unlimited restarts, no penalties.
- Information is the difficulty dial. Give too much and there is no fun; give too little and there is no way in. The design work orbits around what information to give and when.
- The flow curve is a sawtooth of stuck and breakthrough. Five minutes stuck is design; an hour stuck is an incident; pacing management is the bulk of a puzzle designer's workload.

Team and market reality: 2 to 8 people can build one; art demands are elastic; networking and live ops are not required; premium and mobile both work. The scarce skill is not programming (data and tools are ordinary technology) but a designer who can keep producing puzzle ideas and is willing to overrule their own work again and again.

In one line: puzzle games do not sell content volume; they sell the density of figuring things out.

## 2. Player Experience Goals and Benchmark Titles

Player experience goals, scored one by one at acceptance:

- **A sense of command**: the rules are fully transparent, and clearing it was my own doing — nobody made that click for me.
- **The thrill of insight**: an "aha" every few rooms, like a light suddenly switching on.
- **Safe trial and error**: players are certain that being wrong costs nothing, so they dare to experiment and dare to try wild things — this is where puzzle information mainly comes from.
- **Gentle confusion**: confusion is the prelude to a solution; being lost is a design failure. The test is that the player always holds a "something to try next".

Negative feelings (any one of these is a red flag): being fooled (the solution came down to guessing), being humiliated (condescending hints), being worn down (repetitive labor, map traversal, brute-force hauling).

Benchmark titles (all widely known works; play them before reading, and take one lesson from each):

| Title | Tag | The transferable lesson |
| --- | --- | --- |
| Portal | First-person mechanism puzzles | The one-concept-per-room teaching template: show, use, vary, combine; the puzzle is the story |
| The Witness | Island line-drawing puzzles | Wordless teaching throughout, letting the puzzle sequence speak for itself; insight budgeted as a currency |
| Baba Is You | Sokoban meta-puzzle | The rules themselves can be rewritten — the ceiling of expectation violation; a sample of few mechanics and deep combinations |
| Monument Valley | Visual-illusion puzzles | Low difficulty can still earn high praise: mood and interaction feedback hold the experience up, with almost no fail state |
| Tetris | Falling-block stacking | A one-sentence rule with infinite combinations — the extreme proof of mechanic count multiplied by combination depth |
| Sudoku and Minesweeper | Grid-reasoning classics | They work with no art and no narrative; difficulty comes from the length of the deduction chain, not the number of rules |

What these works share: the rules can be explained in a few sentences; depth comes from combinations rather than piled-up content; teaching is built into the level sequence; and the cost of failure is zero or close to it. Hit all four and the game will not be bad.

## 3. Design Essentials

### 3.1 Element Restraint: One Core Concept per Room

Principle: a room introduces only one core concept; a second new concept can only be a variation of the same mechanic. Player cognitive load is a budget, not a sponge.

| Budget item | Suggested cap | Notes |
| --- | --- | --- |
| New concepts per room | 1 | Variations do not count as new concepts; only independent rules do |
| Active mechanics per chapter | 2–4 | Past 4, cross-combinations run out of control and teaching and testing costs rise almost exponentially |
| Total mechanics per game | 3–10 | 3–5 for small scope; 8–12 is the ceiling for a full-scale work, and beyond that some mechanic is bound to become decoration |
| Mechanic interactions per room | No more than 2 | Two mechanics crossing is already a mid-to-late-game difficulty; save three-mechanic combinations for the final chapter |
| Solution length reference | 3–5 steps for beginners, 8–15 mid-game, 20+ late | Step count is not difficulty; piling on steps only produces fatigue |

- Every mechanic must earn its keep: supporting at least 8–15 rooms (2–3 teaching, 3–5 practice, 3–5 variation, 2–4 combination). If it cannot, cut it or fold it into another mechanic.
- The crossing check: list the mechanics and count the effective crossings between each pair; a mechanic with fewer than 3 crossing points will probably be neither remembered nor used.
- Counter-example: a room that at once demands understanding of teleportation, color doors and timed switches leaves most players lost in the fog of "did I do it wrong, or do I not understand the rule?". Such rooms can appear only in the final chapter, and each element needs its own separate setup beforehand.

### 3.2 Wordless Teaching: Show, Use, Vary

There is only one reliable path for a new mechanic into the player's head:

1. **Show**: in a zero-risk environment, let the player see what the mechanic does. Puzzle teaching does not rely on an NPC demonstration but on the room itself: the goal close at hand, the only path to it using the new mechanic.
2. **Use**: give a small room that uses only the new mechanic, so the player does it once by hand, with no old mechanic stacked on top.
3. **Vary**: change one condition (direction, order, distance, timing) so players discover on their own that "it can work like this too"; this step decides whether they "can do it" or "understand it".

Only after the three stages comes combination, paired with old mechanics — combination is the exam. Teach one concept at a time, and give teaching rooms no failure penalty.

Three supplements for the puzzle genre:

- Text explanation is the last resort. If you must write it, write one line and place it after a failed attempt as a follow-up hint, never before the attempt as a manual.
- Acceptance method: find someone who has never played it, keep your mouth shut the whole time, and watch whether they teach themselves within a few minutes. Failure to learn is a design problem, not a player problem.
- Teaching checklist (run through it for every new mechanic): what is the player doing the first time they see it? Is there space for safe trial and error? Within 5 seconds of failing, can they see why? Where is its first crossing point with an existing mechanic?

### 3.3 The Moment of Insight: Expectation Violation and Combination

Insight (the aha moment) is the puzzle game's only currency of satisfaction; in essence it is an assumption politely overturned — the player first thinks they understand, the room gently tells them no, and a new rule settles into place. Insight must be laid out the way an action game lays out its combat.

Three reliable ways to manufacture it:

- **Expectation violation**: first let the player build expectation A (all three blocks are walls), then give a situation where A does not hold (the third block can be pushed). The body of the puzzles in both The Witness and Baba Is You is this structure.
- **Multi-mechanic combination**: two mechanics the player has learned separately cross into a new meaning nobody has seen. The number of crossings is the size of the puzzle space and the ceiling on content output.
- **A wrong answer is information too**: every failed attempt should shrink the search space and reveal one boundary. Silence is the worst feedback; no response equals throwing the player back to square one.

Layout and acceptance:

- At least one small insight every 5–8 rooms, with a combination-driven big insight at the end of each chapter; leave rooms for familiarity and breathing between insights — do not bombard back to back.
- Guard against fake insight: clears that come from hidden information, pixel-level discernment or brute-force grinding produce no insight, only relief; in hindsight players remember only that the game was messing with them.
- Self-test question: after clearing the previous room, can the player restate one new rule in their own words? If not, the room gave them an operation, not an understanding.

### 3.4 Frustration Prevention: Hint Tiers, Skipping and Stuck Detection

Principle: five minutes stuck is design; half an hour stuck is churn. The goal of frustration prevention is not to lower difficulty but to turn "being stuck" into "a retry with direction".

The hint system is tiered by granularity — direction first, answer later — and always requested by the player:

| Tier | What it gives | Trigger |
| --- | --- | --- |
| 1 | Points out which area deserves another look | Stuck detection triggers it; a weak entry quietly surfaces |
| 2 | Names which mechanic this step calls for | The player is still stuck and opens it themselves |
| 3 | Gives a specific operation hint for the current layer | The player is still stuck and opens it themselves |
| 4 | Demonstrates the full solution, with skipping allowed | The player explicitly asks for the demonstration |

- Red line one: hints never pop up to interrupt flow; at most, the "want a hint?" entry surfaces quietly.
- Red line two: hint text never judges. A tone like "how could you not think of that" drives customers away.
- Skip option: allow skipping a room or a whole chapter without affecting completion or the ending. Adults have limited time; skipping retains players, it is not a concession. To distinguish hardcore players, use achievements (a full no-hint clear), not shame pop-ups.

Common stuck-detection thresholds (local counters are enough; no networking required):

| Metric | Reference threshold | Action |
| --- | --- | --- |
| Dwell time in a single room | More than 3 times the team's test median (about 10–15 minutes) | The weak-hint entry surfaces |
| Failures and restarts in a single room | 8–10 | Escalate the hints and review the room for design flaws |
| Idle time | 60–90 seconds | Light guidance: camera move, highlight interactables |
| Post-launch room-level drop-off rate | More than twice the game-wide average | Classify as a problem room and rework it first |

Calibrate the thresholds against your own test data; do not copy them. Stuck data is the most valuable design data a puzzle project has; start recording it on day one.

### 3.5 Tools First: Build the Level Editor Before Talking About Visuals

Iron rule of development order: mechanic prototype → level editor (or at least a data format) → content mass production → art packaging. Reverse the order and iteration speed gets locked down by visuals.

- Puzzles iterate harder than most genres: every room goes through three to eight rounds of design, playtest and retune. Without tools, changing a room means changing code; with tools, it means changing one line of data.
- Editor acceptance standard: a non-programmer can lay out a new room in 30 seconds and hot-reload it into the game with one button. Miss that bar and content output collapses sooner or later.
- Cheapest possible start: text ASCII art plus hot reload is enough to carry the first 50 rooms; build the drag-and-drop visual editor once entity complexity rises.
- Visual investment priority: interaction feedback > state readability > atmospheric art. Players solve puzzles through the readability of state and causality, not through texture resolution. Every mechanism state needs a look you can read at a glance — that matters far more than high-resolution materials.

## 4. Technical Essentials

The technical difficulty of puzzles concentrates in three places — data, state and tools — with rendering the least important. Start with a minimal example: a room can be nothing but a block of text.

```text
#######
#@ $ .#
#######
```

Legend: `@` is the player, `$` a box, `.` a target, `#` a wall. The logic code interprets this text, and the editor generates and validates it.

Key points in order of importance:

- **Separate level data from logic**: rooms are described by data (entities, coordinates, parameters) and the code only interprets that data. The payoff: content can be mass-produced, editors can be bolted on, and community levels become possible later.
- **Undo and redo are first-class citizens**: the guardrail for puzzle trial and error. Implement it with the command pattern recording every operation, or periodic snapshots plus an operation log; you must be able to undo all the way back to the room's starting point. No undo on mobile means shutting most players out.
- **Saves store an action log, not a state snapshot**: small, replayable, analyzable, easy to sync to the cloud, and with less room for cheating. Room-level autosave is the least troublesome approach for puzzles.
- **Write a solver**: most logic puzzles can be covered by breadth-first or iterative-deepening search. This is the highest-return technical investment in the genre, with at least four uses: verifying that every room is solvable (mistake-proofing); computing the shortest solution length as data for difficulty tiers and the hint system; finding multiple or missing solutions (which decides whether puzzles are brittle); and batch regression-testing the whole library after rule changes.
- **Build the hint system as a forward search for the next step**: start from the player's current position and use the solver to search for the next step, rather than hard-coding text in advance. Hint tiers correspond to search results at different granularities: the area, the mechanic name, the operation.
- **Stuck-detection telemetry**: room ID, dwell time, operation count, restart count, hint tier, exit point. A local log is enough during the prototype, with lightweight reporting after launch. Together with solver data, it supports most of the difficulty-curve decisions.
- **Input and platform**: fix the minimal input set first (select plus confirm, or drag), then make the touch, mouse and gamepad mappings equivalent, without depending on capabilities touchscreens lack such as hover. Puzzles place almost no demand on the GPU; the bottleneck is loading and state serialization, and on mobile, power draw and heat are a separate account.
- **The presentation layer's duty is causal readability**: why a mechanism triggered, and who affected whom, must be clear at a glance from the animation. A cheap feature that earns high praise is causal replay: a slow-motion rerun of what just happened. Hover highlights, trajectory display and camera zoom are all reading aids for puzzle players, worth building early.

## 5. Content Volume and Workload Reference

Start with the formula: **content volume = number of mechanics × combination depth**, not room count. Two mechanics that cross well make forty rooms a whole game; fifteen mechanics each going their own way make a hundred rooms fifteen unrelated sketches.

The corollary is "depth before breadth": go deep with 2–3 mechanics first, explore every combination, and complete a small self-contained work of 40–80 rooms; only once you confirm that the set still produces new ideas do you introduce the next mechanic. The cost of adding a mechanic was never "one more mechanic"; it is one more batch of combinations, one more teaching round, and double the testing.

Reference ranges (single-player logic puzzles):

| Scope | Mechanics | Rooms | Playtime | Schedule (1 to 3 people) |
| --- | --- | --- | --- | --- |
| Jam and prototype | 1–2 | 10–20 | 15–30 minutes | 48 hours to 2 weeks |
| Small commercial (mobile or Steam) | 3–5 | 60–100 | 2–5 hours | 3–8 months |
| Full commercial scope | 8–12 | 150–300 | 8–20 hours | 1.5–3 years |

Workload references (for schedule calibration):

- A room usually takes 3–8 rounds of iteration from idea to acceptance; the first version may take half an hour, and polishing it to stable takes several hours.
- One person steadily produces 1–3 playable room prototypes a day; scheduling at ten a day is guaranteed to fail.
- Teaching rooms take about 2–3 times as long to polish as ordinary rooms, because both information load and failure cost have to be managed at once.
- The key art investment is not quantity but consistency: a readability spec where color equals function is worth more than ten extra asset sets.
- Hints, achievements and localization are all light workloads, but their fields must be reserved in the data format — do not wait until just before launch to retrofit them.

Scope control: the typical death of a puzzle project is not failing to finish but rooms that keep multiplying. Cutting 20% of the weak rooms before launch only improves the experience; freeze the mechanic list after some version, and write down new ideas for a sequel or DLC.

## 6. How to Start the First Prototype

Goal: answer one question within two weeks — is this mechanic combination interesting? Do not casually start making the game itself.

1. **Paper first**: no engine. Draw 10 rooms on paper grids and playtest the paper version with people around you. Ideas cut at the paper stage are the cheapest cuts.
2. **Pick the mechanics**: 1 core mechanic plus 1 supporting mechanic, each with a one-sentence rule. A combination that cannot be explained in one sentence is not ready to build.
3. **Data format**: define the room's text representation — ASCII art is enough — and write a minimal loader. This is the first step before any editor.
4. **Minimal interaction**: get to where you can move, interact and judge win or loss; missing animation, missing sound and missing art are the normal state.
5. **Add undo and restart on day two**: without them, all the playtest feedback you get is distorted.
6. **Build three teaching rooms**: one each for show, use and vary. Test with someone who has never played, keep your mouth shut the whole time, and record only where they pause, what they try and when they laugh out loud.
7. **Build ten proper rooms**: arranged into a complete arc of introduction, practice, variation and exam, then ask testers whether they can restate the rules.
8. **Expand laterally**: keep the mechanics fixed and keep adding rooms with new layouts and new combinations. When you yourself start to feel the ideas repeating, the combination depth is bottoming out — that is the moment to decide between adding a mechanic and wrapping up.

Acceptance questions (continue only if every answer is yes): can testers state the rules in their own words? Did an "aha" expression or sound occur? Are the people who get stuck trying with purpose, or just staring? Over ten days, did you yourself want to open it again?

## 7. Common Pitfalls

1. Mechanic overload: a dozen-plus mechanics piled into the game, and players remember four. Fewer mechanics, deeper — a law this genre has verified again and again.
2. Multiple concepts per room: a teaching room teaches two things at once, and ends up teaching neither.
3. Explaining rules with text: an explanation pop-up is a band-aid over a design problem — players do not read it, forget it if they do, and blame you when they forget.
4. The author's filter: a puzzle you have done fifty times is brand new to the player. Designers are the worst testers of their own games; validation must come from someone else.
5. Fixation on a single solution: hard-coding the win check to one path makes puzzles both brittle and slow to produce. Check for the goal state instead, and let players invent solutions you never designed — that is the player's highlight moment.
6. Trial-and-error costs too high: no undo, and restarts require a long walk back. When costs rise, players degrade from experimenting to cautious guessing, and the insight disappears with it.
7. Wrong hint rhythm: auto-pops destroy insight, and hints that never show themselves bleed players. The right posture is a single quiet entry.
8. Difficulty by hidden information: puzzles that tuck key feedback into visual dead corners or rely on guessing colors or judging by sound are not hard, they are bad.
9. Brute-force punishment: making players eliminate wrong answers through repeated hauling. Information should come directly from the attempt, and cleanup and rollback should cost nothing.
10. Content without an arc: rooms in arbitrary order and mechanics with no managed entrance and retirement, so players never feel the language they know growing.
11. Skipping shamed: confirmation pop-ups in the "are you sure you want to give up?" style drive away adults with limited time.
12. Visuals before tools: only after hand-coding thirty rooms do you remember the editor, and the rework eats a quarter.
13. Overinvesting in presentation: the budget goes into materials and effects while outsiders have not yet played the puzzles through even once.

## Further Reading

- Teaching sequences, the whitebox workflow and pacing curves: Level Design Handbook §3 and §6.
- How to write core loops, complexity budgets and gameplay validation: Game Design Handbook §2, §3 and §9.
- Breakdowns of successful and failed projects: Case Studies.
- State, saves and data-driven architecture: Programming Handbook.
- Publishing, live ops and pitfall avoidance: Pitfalls & Anti-patterns, Indie Survival.
- Public talks: the developers of Portal, The Witness and Baba Is You all have public GDC talks and interviews — search the title plus GDC and you will find them.
- A closing suggestion: finish ten rooms first, then come back and reread §3 and §7. The ability to make puzzles can only grow out of watching real people get stuck.
