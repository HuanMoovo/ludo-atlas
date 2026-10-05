# Ludo Atlas · Genre Handbooks · Match-3

> **Genre Handbooks · Volume 3**. Positioning: the grid genre that makes "swap and chain" its first pleasure. Within a budget of moves or time, players tame a randomly refilling board into a path toward the objective; this page covers swap game feel, the level balance skeleton, difficulty curves, board engineering and the level mass-production pipeline.
> Companions: Game Design Handbook (core loops and reward psychology) · Programming Handbook (board generation and tooling) · Production Handbook (level scheduling and content estimation) · Indie Survival (scope control and the ongoing content bill).
> This page carries no external links; benchmark titles are widely known works only, and the figures here are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: match-3 is the grid genre **with swap and chain as its first pleasure**. The rules take two sentences; all the depth lives on the board. Randomness supplies the material, and each choice the player makes decides how efficiently that material gets used.

The core loop, written as a verb chain:

`read the board → find a legal swap → swap → resolve and chain → cascade and refill → read the board again`

This loop is measured in seconds: one valid move takes one to three seconds, plus one or two more for the chain resolution. It holds on just two preconditions: the rules are readable at a glance (§3.1), and the consequences of each step are understandable — chains come from the rules, not from mysticism.

The loop at three scales:

| Scale | Loop | What the player gets |
| --- | --- | --- |
| One move (1–5 seconds) | Read the board → swap → resolution and chains | An instant hit of positive feedback, or a readable bounce-back |
| One level (1–5 minutes) | Hit the objective within budget, push for stars | The certainty of a clear, or the "so close" urge to retry |
| A stretch of levels (days to weeks) | A new mechanic debuts → variations → a combined test | A board language that keeps updating; a reason to keep coming back |

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Puzzle | A puzzle's solution is derived by deduction and the result is deterministic; a match-3 board shifts with every cascade — players make optimal decisions under constraints, and the winning path is not unique |
| Tetris | Where a piece lands is chosen by the player, testing placement and speed; match-3 hands refills to the system, and the test is "which swap do I pick" |
| Deckbuilder | Building happens inside the run, with the card pool as content; match-3 has no in-run growth, and the content lives in the levels and obstacles |
| Idle/incremental | Idle removes the operations and hands progress to time; every point of match-3 progress has to be swapped out by hand |

A self-check question: take away the chains and cascades, leaving only fixed-position elimination by swapping pairs — does the game still hold up? If the answer is "no", what you are making is a match-3; half of this genre's pleasure comes from a chain reaction set off by a single move.

Team-level framing: a content-driven genre whose engineering concentrates on the board and the level tooling; art is packaging, levels are the substance; no online dependency. The real workload is level design and tuning, and the scarce skill is the person who can tune a "sense of randomness" into a "sense of fairness" and reliably ship levels. One-line conclusion: match-3 doesn't sell rules — it sells level density and satisfying feedback.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Readable at a glance**: board state, objective progress and available moves are understood in one sweep; a board you cannot read is an accident scene.
2. **Low effort, rich feedback**: a single move is a one- or two-second swipe, and the payoff is swathes of elimination and chains; the gap between input cost and feedback volume is the source of the satisfaction.
3. **A sense of planning**: experts can plan chain routes while beginners still profit from tapping at random; skill differences show up in "how many steps ahead you can see", not in hand speed.
4. **The tension of "so close"**: being one or two objectives short at settlement is what creates the urge for one more try; the progress bar and settlement panel have to make the gap clear.
5. **Cheap retries and steady novelty**: failing and restarting is cheap and the cause traceable; new mechanics debut on a rhythm, so long-term play never repeats itself.

Negative feelings (any one of them is a red flag): controls that misfire (a swipe with no response, an unreadable bounce-back); being cheated by the system (dead boards, unreachable objectives); being obscured (effects covering the board); being worn down by repetition (stacking quantity without changing the pattern).

Benchmark titles (all widely known works; play them yourself before breaking them down):

| Title | What to learn from it |
| --- | --- |
| Bejeweled | The genre's origin point: the baseline for swap resolution, chains and effect feedback; the split between timed and relaxed pacing |
| Anipop | The mass-market level-based sample: a moves-based system, a level language of objectives and obstacles, a low-barrier daily rhythm |
| Candy Crush Saga | The long level sequence: rotating objective types, arranging difficulty peaks and troughs, the ceremony of map progression |
| Gardenscapes | The match-3 chassis plus long-term goals: matches produce resources, and renovation and story supply the reason to return |
| Tiantian Ai Xiaochu | The mobile short-level format: a clear per-match objective, light pacing, playable in any spare moment |

## 3. Design Essentials

### 3.1 Core Rules and Game Feel: Swaps, Chains and Effects

The rules skeleton in two sentences: swap two adjacent pieces; line up three or more and they clear; pieces fall in from above and resolution repeats until the board is stable. Any rule combination that cannot be told in two sentences should not enter the prototype yet.

For swap input methods, mobile prioritizes swipe feel above all:

| Input method | How it works | Pros | Risks |
| --- | --- | --- | --- |
| Drag-swipe | Press a tile and slide toward a neighbor | Feels responsive; the mobile mainstream | Fast repeated swipes easily drop input |
| Tap twice | Tap the origin tile, then an adjacent tile | Precise, few mis-taps | One extra tap; slightly slower pacing |
| Cursor plus direction keys | Select a tile, then move with the direction keys | Works on desktop and gamepad | Unusable on touchscreens; two mappings to maintain |

- Resolution and pacing discipline: a failed swap bounces back, and the bounce should end as fast as possible (a common target is within 200 ms); resolution runs in the logic layer first, with animation following the logic. Chains (what players call combos) advance on a fixed beat — a common cadence for one resolution chain (clear → cascade → clear again) is 0.15–0.35 seconds — and each chain level raises the effects and pitch one step; for exact timings, tune frame by frame.
- Special pieces: matches of four or five generally spawn line-clear, explosive and same-color-clearing pieces; the combo effects triggered by swapping two special pieces are a major source of depth, their rules must be expressible in one sentence, and the first trigger must be readable at a glance.
- The feedback trio: particle flashes, an ascending chain scale, and short hit-stop plus vibration on big clears — all three landing on the same beat; drop any one and the chain feels floaty.
- Idle hint: after a few seconds without input, give a light "where can you still move" nudge — point the direction only, never make the move.

Game-feel acceptance: have 5 people play for 5 minutes each and count the "swipe did nothing" and "cannot read the bounce-back" incidents — both should be near zero; bounce duration, chain cadence and effect durations all go into the numbers table, tuned against screen recordings.

### 3.2 The Level Balance Skeleton: Budget, Objectives, Obstacles

A level's numbers compress into one sentence: given the board and the obstacles, hit the objective within budget. The three pillars are budget (moves or time), objective and obstacles.

- Deriving the moves budget: measure the average output per move with simulation (§4), then multiply by a tolerance factor (commonly 1.2–1.5, i.e. leaving 20% to 50% slack), and calibrate by hand-play. Filling in numbers by gut feel is the number-one source of runaway difficulty.
- Objective types: collect (gather N of a given element), clear (wipe all target tiles), transport (bring items down to the bottom row) and score (reach a score within a time or move limit). Any two can be stacked; stacking three needs caution.

| Objective | What the player does | Design points |
| --- | --- | --- |
| Collect | Clear N of a given element | The most basic skeleton; quantity and the board's color count together set the difficulty |
| Clear | Wipe all target tiles (jelly, dirt types) | Positions are fixed; tests coverage routes and ordering |
| Transport | Guide items through the board to the bottom row | A duel with obstacles and cascade paths; the highest teaching cost |
| Score | Reach a score target within a time or move limit | Naturally supports replay and light leaderboards; good for relaxed levels |

Obstacles fall into four behavior categories; add them one at a time, never in parallel:

| Obstacle | Behavior | Teaching point |
| --- | --- | --- |
| Blocker (ice, chains) | Occupies a tile or piece; cleared by matching next to it | Teach "clear the piece beside it" first |
| Absorber (jelly, vines) | Takes multiple hits to clear; its state must be visible | Teach the visual read of "how many hits are left" |
| Spreader (venom, lava) | Spreads on its own, creating time pressure | Must have a spread cap and a slow-down valve |
| Terrain (walls, holes, portals) | Changes connectivity and cascade paths | Establish the map grammar before discussing numbers |

- There are only about six or seven difficulty dials: budget slack, objective quantity, board size and shape, color count (commonly five to six), obstacle type and count, and drop weights. Move only one or two at a time; move more and you can no longer tell where the difficulty came from.
- One data row per level: ID, objective, budget, board layout, color count, obstacle list, drop parameters and expected rating; measured data (pass rate, average moves left) goes back into the same table. Star thresholds are set as two or three tiers on moves left or score, giving repeat attempts a second-layer goal, with threshold values likewise drawn from simulation data; for how to manage the table, see the Production Handbook.

### 3.3 The Difficulty Ladder and the Psychological Curve

Match-3 difficulty is not a climbing slope but a sawtooth: a few smooth levels, one tight level, then a breather. The design work is arranging where the peaks and troughs of that sawtooth fall.

- Macro structure: teaching stretch (almost no failures) → rhythm stretch (alternating sawtooth) → milestone (a new mechanic or obstacle debuts) → exam level (a combined test of old mechanics) → breathing level, cycling onward; only one new thing debuts at a time, and combinations appear only after each component has been taught. Pressure peaks have three natural positions — the mechanic exam, the milestone level and the chapter finale — so leave a breathing level on each side of every peak; two high-pressure levels in a row double the frustration.
- "So close" is engineering, not mysticism: the settlement panel has to tell players exactly how short they fell (how many pieces still missing, whether there is hope within a few moves); being slightly short creates drive, being far short creates surrender, and what you are calibrating is the band between the two.
- Keep the three layers of feedback on separate rhythms: the action layer (particles and sound on every clear), the level layer (progress bar and stars) and the sequence layer (the sense of unlocking new mechanics and chapters); give any one layer too densely and players go numb.
- Placement of paid points: in long-running products, the spots where players most want help (extra moves, retries, items) naturally coincide with difficulty peaks; where those spots sit and how far apart they are is a difficulty-curve placement question — get the placement right and what players get is room to "still save it". This page covers only the placement, not monetization methods.
- Self-test question: line up the first-attempt pass rate of the last twenty consecutive levels and look at the shape; if it is close to a straight line, you have laid out a level sequence, not a curve.

### 3.4 The Level Mass-Production Pipeline: Editor and Test Tooling

Match-3 is a content genre, and level throughput decides the project's life or death. The pipeline has exactly one standard: designers can build, test and tune levels without touching code.

- Levels are data: one row per level (§3.2), with code acting only as the interpreter; any level parameter written into code is a rework order planted for the future.
- Editor acceptance criteria: a designer lays out a new board in under 30 seconds and hot-reloads it into the build with one click; the preview screen can overlay objectives, obstacles and cascade directions directly.
- Batch validator: field completeness and reference validity; combined with the no-move detection from §4, run seeded simulation over the whole level library, tally completion rates and average moves, and auto-queue wildly deviant levels for review.
- Headless simulator: make the board logic a standalone module that does not depend on animation, and it can play thousands of games against itself; run a few thousand with a simple policy (greedy targeting of objectives) to get a pass-rate profile per level, serving three purposes at once — difficulty grading, regression testing and balance adjustment.
- Regression discipline: after changing mechanics, cascades or obstacles, run the full-library simulation regression before moving on; skip this step and you are betting the fate of a hundred levels on luck.

### 3.5 Board Readability and Presentation Budget

- Keep the color count around six; hue separation has to survive small screens and outdoor light, and leave a non-color cue (shape or texture) for color-vision deficiencies; special pieces and obstacles need silhouette-level differences, and state changes (jelly worn down once) must read "how many hits left" at a glance.
- Effect budget: cap the concurrent particles and sounds in one big chain; the presentation layer's job is amplifying feedback, not covering the board. Every animation must be speedable or skippable without affecting the resolution result.

## 4. Technical Essentials

The engineering difficulty concentrates on the board logic and the tooling; rendering is the relatively unimportant part; everything below is engine-agnostic.

**Board, Generation and Randomness**

- Data structure: a 2D grid where each cell records element type and state (normal, special piece, obstacle, target tile); board sizes commonly run from 7×7 to 9×9.
- Four constraints on initial generation: no ready-made three-in-a-row; at least one legal swap exists; the color distribution matches the level configuration; target items and special-piece spawn points are reachable. If any one fails, reroll — never let it through.
- Cascades and refills: fill in from the top, falling column by column; compute a whole column's fall order in one pass to avoid the sorting errors that cell-by-cell falling produces.
- Randomness and reproducibility: one random seed per level decides the initial board and the cascade sequence; the same seed must reproduce, with testing, simulation and replay sharing one random implementation; drop weights (color distribution, target-item rates) go into the level config — never let them scatter as magic numbers in code.

**Swap Resolution and Chain Settlement**

- Legality checks look only at the affected row and column: after a virtual swap, check whether the horizontal and vertical lines through the two cells form a match of three; never rescan the whole board.
- Chain settlement uses a cyclic queue: mark clears → score → cascade → refill → resolve again, until the board is stable; special-piece chain triggers enter the same queue, keeping the order predictable. The logic layer produces the full resolution sequence first (the resolution script), and the presentation layer plays it in order; speed-up and skip change only playback speed, never the logic result — a discipline that feeds both the simulator and replays.

**No-Move Detection and Reshuffling (Mandatory Engineering)**

- Detection method: iterate over every cell and its right and lower neighbors, virtually swap and check for a match of three; if all fail, the board is dead with no moves. A full-board scan is a small bill — don't skip it.
- Trigger points: detect after every resolution settles; initial generation must be detected too.
- Shuffling and rearranging: keep special pieces and obstacle states, reshuffle the normal elements; the result must satisfy both "no ready-made three-in-a-row" and "at least one legal swap" — if not, shuffle again — and give players a visible "board reshuffle" cue animation; repeated failures need a fallback policy and logging.
- Frequency watch: frequent shuffling means the drop weights or obstacle layout have a problem — go back to the level data first, rather than raising the shuffle threshold.

**Presentation and Performance**

- Input and performance: bucket swipes by angle and snap to the origin tile; handle broken touches (lifting mid-swipe) and rapid consecutive operations without dropping inputs; give particles, floating text, sound channels and haptics channels all object pools and concurrency caps — the longer the chain, the more restrained the per-beat effect count must be.
- Telemetry: attempts per level, average moves left, failure points, exit points; local logs suffice during prototyping, and this is the only raw material for reviewing the difficulty curve.

## 5. Content Volume and Workload Reference

The following are typical magnitudes, for estimating scope; not a commitment.

| Form | Level magnitude | Time magnitude | Notes |
| --- | --- | --- | --- |
| Prototype | 10–30 levels | 2–6 weeks | Three objective types, two obstacles; validates the loop and difficulty only |
| Small complete title | 100–300 levels | 3–9 months | One mechanic language explored in depth, editor and simulator included |
| Long-running level product | 500+ levels, continuously replenished | Ongoing investment | The content pipeline is a long-term bill; schedule by pack |

Conversion and discipline:

- Hours per level: design, simulation, playtesting and tuning together commonly take half a day to two days, with most late rework coming after store testing; the bar for shipping a new mechanic is supporting at least 15–30 levels of variations and combinations — if it cannot, don't add it.
- Art is template work: one material set for the board and pieces, one effect atlas, one UI framework can carry the whole library; the bulk of the cost always sits in levels and tuning.
- Scope discipline: cutting levels is always cheaper than rescuing them; a flat line of a thousand levels is worth less than a good curve of three hundred.

## 6. How to Start the First Prototype

Goal: answer one question within two weeks — is this swap, chain and resolution loop annoying or not? Don't touch art, saves or leaderboards.

1. **Days 1–3: grid and swaps.** 7×7 or 8×8, five to six colors; swapping, bounce-backs, match-of-three resolution, cascades, refills and chain settlement. It should look ugly.
2. **Days 4–6: no-move detection and shuffling.** Build this completely during the prototype; do it late and dead boards become the design norm, carrying bad habits all the way into production levels.
3. **Days 7–10: three objective types, two obstacles, a minimal budget.** One level each for collect, clear and transport; estimate budgets as "average output per move times the tolerance factor" (§3.2), then tune once.
4. **Days 11–14: blind testing.** Get 3 to 5 people to play 10 levels each; record pass rate per level, average moves left, willingness to retry and "what did you not understand".

Success criteria (all observable):

- Testers start their first swap within 30 seconds, with no verbal instruction.
- The complaints "swipe did nothing" and "the board is dead" never occur, not once.
- The teaching stretch's pass rate is clearly above the challenge stretch's — the sawtooth curve has taken shape.
- More than half of testers ask on their own to keep playing the next level.

Once the prototype passes, externalize the level data first (one row per level), and only then discuss the editor and content mass production; reverse the order and your throughput gets locked down by code.

## 7. Common Pitfalls

1. **No-move detection missing or half-done**: the board is still dead after a shuffle, or dead boards are simply left to the player; both detection and shuffling are mandatory (§4).
2. **Swap resolution that does not feel responsive**: swipes drop inputs, diagonal directions are ambiguous, bounce-backs are too slow; fail the game-feel acceptance and everything after is a castle in the air.
3. **Uninterruptible settlement**: long chains cannot be sped up or skipped, forcing players to watch the show; and skipping breaks state sync (the resolution script in §4).
4. **Difficulty raised by inflating objective counts**: bigger objectives with an unchanged budget turn challenge into harassment; what should be tuned is slack and layout.
5. **Generation and reachability left unchecked**: ready-made matches at the start, unbalanced colors, or obstacles and drop weights making target items unreachable; the four generation constraints (§4) and full-library simulation (§3.4) must be in place early.
6. **Mechanic overload**: every obstacle crammed onto one board, new mechanics with no teaching level; teach only one new thing at a time.
7. **A difficulty curve that is a straight line**: all flat and players get bored, all steep and they leave; the sawtooth is the playable shape (§3.3).
8. **Effects drowning out information**: particles cover the board, chain sounds mask one another, hit-stop is too dense; presentation is an amplifier, not the lead actor (§3.5).
9. **Scheduling by gut feel**: planning content at "ten levels a day" and then getting stuck entirely on tuning and rework (§5).
10. **Missing telemetry**: without per-level pass rates and moves-left data the curve cannot be reviewed, and tuning turns into mysticism (§4).
11. **No editor**: designers wait on programmers to change a level, and throughput is locked down from day one; put the editor in the first batch of milestones.

## Further Reading

- Game Design Handbook: core loops, reward psychology and difficulty-curve methods — the base document for §1 and §3.
- Programming Handbook: data structures, random implementation and tooling discipline — corresponds to §4.
- Production Handbook: content estimation and scheduling conventions, to be used alongside §5.
- Indie Survival: scope control and the ongoing content bill — they decide how many levels you lay out and at what cadence you replenish them.
- Genre Handbooks · Puzzle (Volume 1): the sister page; the three-part teaching structure and the general anti-frustration discipline defer to it — this page covers only the board, randomness and mass-production engineering specific to match-3.
- Homework: without touching an engine, design 10 levels in a spreadsheet — three objective types, two obstacles, one curve with peaks and troughs — and hand-calculate the moves budget for one of them; then decide whether to build that two-week prototype.
