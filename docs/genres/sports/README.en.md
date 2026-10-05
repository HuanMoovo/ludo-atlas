# Ludo Atlas · Genre Handbooks · Sports

> **Genre Handbooks · Volume 3**. Positioning: the genre that makes "winning the contest by rules everyone already knows" its first pleasure. Players walk in carrying real-world rules knowledge — the teaching cost is near zero, and the price is that their sensitivity to the calls and to inputs delivering on intent runs far higher than in other genres.
> Companions: Game Design Handbook (core loops and balance) · Programming Handbook (ball physics, adjudication and networking) · Production Handbook (estimation and scope control) · Indie Survival (small-team slices and scheduling).
> This page carries no external links; benchmark titles are widely known works only, and the figures here are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: sports games are the genre **with the competition format and contest of a real sport as their skeleton**. Players win the match on a field where "everyone already knows the rules", through their inputs and decisions; the credibility of the score, the format and the calls is this genre's worldbuilding. Players bringing their own rules knowledge is its greatest asset and its greatest debt: the teaching cost is near zero, but players have zero tolerance for "the goal that should have gone in didn't" and "the foul that should have been whistled wasn't" — fidelity and game feel are not bonus points, they are the floor of trust.

The core loop, written as a verb chain:

`read the situation → decide (pass, shoot, defend, substitute) → execute the action → adjudication and resolution → score and situation shift → adjust positioning and strategy → the next play`

This loop is measured in "plays": one attack in football, one possession in basketball, every point in tennis. It holds on just two preconditions: controls must deliver intent (§3.2), and calls must be consistent (§3.1).

On one skeleton (rules, competition format and a player ability model) sit three orientations: simulation weighs physics and detail (the eFootball series), arcade weighs simplification and thrills (the Mario Tennis series), and management weighs data and running a club (the Football Manager series). The trade-offs point in different directions, but the skeleton and the problems are the same: which rules to keep (§3.1), how to simplify adjudication (§3.2), and how to keep the AI from giving itself away (§3.3).

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Racing | Both are physical contests, but racing's carrier is the car and the track, and victory is measured in lap times; in sports, victory is the score between two teams or two players |
| Fighting | Both are contests, but fighting has no competition format, no score and no teammates; half of sports' pleasure comes from the rules and half from the collective |
| Management sim | Management deals with the organization and the budget, read through reports; a manager-oriented sports game still deals in results on the field, and reports are only the means |
| Party game | The party hides inside a sports shell (motion controls and minigame collections); a sports game's real match is still a full competition format |

A self-check question: strip away the competition format, the score and the calls, leaving only physical contest — does the game still stand? If the answer is "no", what you are making is a sports game.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Credible rules**: every call can be explained and anticipated; wins and losses trace back to rules and inputs, not to "the referee robbed me".
2. **Inputs that deliver**: the loss between "I wanted to pass over there" and "the ball went over there" must be small; controls that don't obey are this genre's most lethal problem.
3. **Attacking and defending tension**: one attack, one possession is a small story, its rhythm swinging between build-up, risk and burst.
4. **The collective**: teammate AI makes the field feel like a team, not the player against everyone; in management-oriented games the collective comes from the squad and the tactics.
5. **Mastery and the long game**: from "can play" to "can really play" lies a long ramp; seasons, squads and progression supply the long-term goals.

Benchmark titles (play them yourself before breaking them down; video alone won't teach you ball feel or the rhythm of the calls):

| Title | What to learn from it |
| --- | --- |
| eFootball series | The game-feel baseline for a single touch and fine center-of-mass control; how player personality maps onto stats and animations |
| FIFA series | A reference for licensed content and full-mode operations; how assist tiers flatten the gap in input skill |
| NBA 2K series | The animation volume of realistic basketball and the content scale of career mode; broadcast-style presentation |
| Football Manager series | Proof it holds up without an action layer: how data and text carry a "real season" |
| Rocket League | Minimal rules, maximal control ceiling; the model example of going deep on "one verb" |
| Mario Tennis series | Casual rule trade-offs; pick-up-and-play and party appeal |

## 3. Design Essentials

### 3.1 Rules Fidelity and Gamification Trade-offs

Real-world rules split into two layers: **structural rules** (format, field, scoring and player counts) decide what the game is — keep them, or replace the whole set with a smaller, self-consistent format (11-a-side to 3-a-side, half-court, short matches); **execution rules** (offside, fouls, dead-ball procedures) decide detail credibility — cut them against the player's input bandwidth. There is only one test for the trade-off: does this rule create decisions?

| Rule type | Examples | Recommendation | Reason |
| --- | --- | --- | --- |
| Structural rules | Format, scoring, field size | Keep, or replace as a whole | Players' sense of "what a match is" comes from here |
| Decision-making calls | Offside, fouls, stamina, obstruction | Simplify but keep consistent | They create trade-offs of position, timing and risk |
| Procedural detail | Substitution paperwork, stoppage time, assistant referee routines | Cut or automate | Only the referee's point of view cares; players never notice |
| Presentational content | Entrance ceremonies, commentary, replays | Optional, by budget | Raises polish; doesn't change gameplay |

Simplification is not deleting rules, it is swapping in a smaller but equally self-consistent set: an arcade-oriented game can switch off offside, but the defensive line will collapse with it — so shrink the field and cut the player count at the same time, until "fail to track back and you get played through" holds again. Change the rules and balance must be retuned; deleting without replacing is an accident. One discipline: players cannot remember every detail of the real rules, but they are extremely sensitive to inconsistency — the same collision whistled once and let go once does more damage than a wrong call.

### 3.2 Physics and Adjudication: Simplified Models

The ball is the protagonist, adjudication is the referee. Neither chases physical accuracy; both chase predictability, explainability and reproducibility.

Ball trajectories use simplified integration, not full fluid computation:

| Element | Simplified model | The feel it preserves |
| --- | --- | --- |
| Parabola | Constant gravity; initial velocity sets the arc | The intuition of a shot, a jump shot and a long pass |
| Air drag | Deceleration proportional to speed | Long shots fade instead of flying dead straight at constant speed |
| Spin | Side spin adds lateral acceleration (an approximation of the Magnus effect); topspin adds dip | Curled shots and topspin keeping the ball down |

Spin and drag coefficients all go into number tables with hot-reload support; what players perceive is "can this shot curl inside the post", not the real spin rate. The adjudication layer and the presentation layer are built separately:

- Player–ball adjudication uses simplified geometry (a sphere against a capsule or cylinder) and is deliberately generous: physics yields to the eye — better to count it in than to count it lost; key events (goals, out of play, touches) are resolved automatically with trigger volumes or line-segment tests, never interrupting the match's rhythm.
- Calls that need explaining, such as fouls and offside, run in two stages: the adjudication layer outputs candidate events (contact, position, possession state), and the arbitration layer issues calls under the rules and a tolerance band; the band is tiered by difficulty.
- Adjudication must be deterministic at a fixed timestep: same input, same result. Replays, ghosts and online play are all built on this.

Acceptance in the build: the fastest ball must not pass through the goal line or the touchline (trigger volumes plus line segments as double insurance); record a match and step through it frame by frame — no visible mismatch between the call and the picture.

### 3.3 Teammate and Opponent AI: This Genre's Real Hard Problem

Sports AI must, inside the constraint of a team sharing one field, deliver both local actions and a global formation. All of teammate AI's mistakes are charged to the player's account; opponent AI must lose believably and win for good reasons — neither end may give itself away. Three layers, built one at a time:

| Layer | Responsible for | Common practice | Failure mode |
| --- | --- | --- | --- |
| Formation layer | Positioning and zonal responsibility | Assign positions and recovery runs from the ball's location | The whole team chases one ball and the formation becomes a mob |
| Decision layer | Chasing, marking, support, tracking back | Responsibility assignment (nearest player chases) plus utility scoring | Two players contest one ball and the box is left empty |
| Execution layer | Turning decisions into actions | A move library plus error injection | Actions fight the physics and the player twitches in place |
| Difficulty layer | Losing believably, winning for good reasons | Three knobs: decision quality, reaction time, execution error | Hidden speed boosts and ultra-fast reactions, spotted by players in the moment |

Teammate AI's job is to let the player play well, not to play for them: support runs offer passing lanes, defending doesn't steal the show, the ball the player is interacting with has priority (no stealing a certain goal), and after being beaten they chase back. Write all of these into the AI requirements document as acceptance items.

Opponent AI difficulty uses only the three knobs, never cheat parameters; high difficulty wins through better choices, not faster legs — once players notice hidden cheating, both winning and losing stop meaning anything. Verify with a simulator, not your eyes: run AI-versus-AI matches in batches and read the statistics (shot counts, pass completion, possession distribution, goal-timing distribution) to find formation and probability problems; a single match's feel will lie, a hundred matches of statistics won't.

### 3.4 Licensing Reality: The Intellectual Property of Teams and Players

Real leagues, clubs, player names, likenesses, crests, kits and competition identities are mostly protected assets, and are usually licensed in league-wide or club-wide bundles whose cost and negotiation lead time exceed most indie budgets. For the process of clearing licensing terms, see the Legal, Patents & Competition.

Going unlicensed is the norm, and the alternative must come as a full set:

- Original teams, players and competitions: build recognizability from cities, colors and playing style, stay clearly distinct from real clubs, and don't skate the line with designs "recognizable as the original at a glance"; invent the competition format yourself — that is freedom, actually, letting you tailor the season structure to the gameplay.
- The editor route: letting players create their own teams and players is a common path, but edit and share features need clear moderation boundaries (naming, likeness and asset policy — see the Legal, Patents & Competition).

Three red lines: no soundalikes or near-identical spellings of real names; no synthesis of real people's faces and voices; no copying real crests and color combinations. Names and assets are all managed through IDs: if a challenge arrives, renaming and swapping assets is a day's work, not a full rework.

### 3.5 The Small Team's Realistic Slice: Arcade Style and Small Fields

Benchmarking a small team against fully licensed simulation leagues is a dead end; that scale is an annual-release engineering effort of hundreds of person-years. Three workable slices:

| Slice | Approach | Form examples | Cost intuition |
| --- | --- | --- | --- |
| Small field, fewer players | 3v3, 1v1, half-court | Street basketball, cage football, table tennis, pool | Lowest; both AI and animation volume halve |
| One verb, deep | Drill a single action to mastery | Rocket League–style one-touch finishing | Low, but game feel must be perfect |
| Casual and party | Simplified rules, exaggerated presentation, local multiplayer | Motion-controlled tennis, party minigames | Medium; presentation and device fit are the variables |

Savings all three directions share:

- One animation skeleton shared across the whole team, with personality coming from parameter differences (speed, height, strength); signature moves go only to a few star players.
- One field plus time-of-day and weather variants carries the content; the match core (physics, adjudication, AI) is built once, and season, cup and training modes all reuse it; prioritize presentation that is cheap and effective: stadium ambience, a spare broadcast-style camera and a scoreboard.

In one line: what a small team sells is "one clear verb", not "fidelity".

## 4. Technical Essentials

The engineering difficulty concentrates in three places: ball physics and adjudication, AI architecture and verification, and adjudication authority in online play. Everything below is engine-agnostic, with method detail in the Programming Handbook.

**Ball physics**

- Fixed timestep (60 Hz is common) decoupled from rendering; the ball is fast and a single frame's displacement can exceed its diameter, so use substepping or continuous detection, with double insurance on goal-line and touchline decisions. Spin uses a simplified model: side spin adds lateral acceleration, topspin adds dip; the coefficients go into number tables with hot-reload support. A full realistic trajectory is a bonus, not a baseline.
- Ball–player interactions are managed centrally: trapping, dribbling, poking and aerial duels — each interaction is a short state machine; the transition points are where game feel breaks most easily, so tune them frame by frame.

**AI architecture and verification**

- The three layers update separately: the formation layer at low frequency (a few times a second), individuals near the ball every frame, distant individuals at reduced rate — performance and the look both benefit. Ball prediction is a shared module: compute the landing point and time to arrival once, and let the whole team consume it; perception is a snapshot, with different vision and delay per difficulty tier, so the AI "misses things" like a human.
- Build two tools first: an AI-versus-AI match simulator (batch-run matches for statistics, verifying formations, pass completion and score distributions) and adjudication visualization (drawing adjudication volumes, predicted ball landing points, the offside line and trigger volumes — almost every call dispute can be pinned down with it).

**Online (if you go multiplayer)**

- Adjudication authority must be singular: host-adjudicated or server-adjudicated, with clients doing presentation and prediction only; if both sides compute their own ball, the "whoever scores decides" deadlock is inevitable. Input delay compensation, interpolation and rollback follow the networking chapters of the Programming Handbook; the network approach must be fixed at kickoff, not left until the wrap-up.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimating scope; not a commitment.

| Project shape | Content scale | Time reference | Notes |
| --- | --- | --- | --- |
| Game-feel prototype | 1 player plus 1 ball (or 1v1) | 2–6 weeks | Validates controls, adjudication and ball feel only |
| Small arcade title | 3v3 or a single-discipline contest, a few teams | 3–9 months | Shared animations, minimal rules, local-first |
| Typical indie title | One complete league or competition system | 1–2 years | Animation volume and AI debugging dominate |
| Simulation-league title | Full-league licensing, all modes | Annual-release team and schedule | Not a benchmark, for reference only |

Cost breakdown: the player is the most expensive content unit — a model plus a move library, a parameter set, a face and voice, and how it is acquired. Animation volume is the largest single cost: one move set per sport (run, stop, pass, shoot, defend); build the shared skeleton first and add signature moves only when the budget has room. Field and broadcast presentation (camera, scoreboard, ambience) are low-cost, high-perception investments, ranked above entrance ceremonies and full commentary.

Scheduling anchor: taking one match from zero to "shippable quality" (a vertical slice) usually takes 2–4 months; extrapolate from there by team count and mode count. Order of scope control: freeze the match core first, then lay out teams, seasons and modes; do it the other way round and every game-feel change reworks all the content (scheduling method in the Production Handbook).

## 6. How to Start the First Prototype

The first prototype makes only one half-court, one ball, one player and one opponent, finished in 2–4 weeks, without touching teams, seasons or art.

**Week 1: ball feel.** One player plus one ball: stop, dribble, pass and shoot, four moves, with the ball flying along a simplified trajectory; all ball physics parameters go into number tables with hot-reload support. Ugly is expected at this stage.

**Week 2: one AI opponent.** Chase, intercept and tackle wired into one chain; build a single difficulty tier first, with error injection parameterized; implement "possession" (who controls the ball) as a foundational concept.

**Week 3: adjudication and rules.** Goals and out-of-play judged automatically; add one minimal rule (a three-second hold, say, or a single foul type) and wire the two-stage structure of "adjudication layer proposes candidates, arbitration layer issues calls"; build adjudication visualization alongside.

**Week 4: testing and tuning.** Find 3–5 people who have never played it and give each 10 minutes, no hints, no explanations; record two categories of problem — "controls don't obey" and "the calls make no sense" — and tune only parameters and call tolerance, adding no new systems.

Success criteria (all observable):

- With all art and audio removed, testers are willing to play again and again, typically 10+ minutes a session.
- At least 4 of 5 testers finish a full match with no verbal instruction; "I pressed shoot and nothing happened" complaints at or under 1 per person.
- Testers can predict a call before it arrives and, afterwards, explain its reason in their own words.
- Change any one ball physics parameter and you can quantify its effect on goals and match rhythm within 5 minutes.

If ball feel and adjudication don't pass, don't start laying out teams and competition formats; this genre's foundation is "this shot counts".

## 7. Common Pitfalls

1. **Benchmarking against full-rules simulation from day one**: 11-a-side plus a full league is the classic scope death sentence; start with a small field, fewer players and one rule (§3.5).
2. **Teammate AI playing dumb**: players put teammates' mistakes on the game's tab, and it drives them off harder than an opponent that's too strong; support runs, making way and not stealing a certain goal must go into the AI acceptance list (§3.3).
3. **Inconsistent calls**: the same collision whistled once and let go once burns all trust at once; separate the adjudication layer from the arbitration layer and quantify tolerance per difficulty (§3.2).
4. **Ball feel like hockey or a balloon**: the ball is too fast and slippery, or too slow and floaty, with the arc and the bounce untuned; the ball is the protagonist — tune it frame by frame (§4).
5. **AI that wins by cheating**: once hidden speed boosts and ultra-fast reactions are spotted, victory and defeat both lose their meaning (§3.3).
6. **Licensing that skates the line**: soundalike team names and near-identical crests are risk, not a shortcut; do the unlicensed set in one pass (§3.4).
7. **Runaway animation volume**: bespoke moves for every player, and the budget burns out on the first player; shared skeletons first (§5).
8. **Building seasons before the match core is frozen**: formats, balance and AI are all still changing, and seasons, transfers and progression get scrapped pass after pass; freeze one match first (§5, §6).
9. **Online adjudication authority undecided**: both sides compute their own ball and goal attribution becomes an incident; single-player first, or fix the authority at kickoff (§4).
10. **Presentation piled too high**: entrance ceremonies and bespoke commentary are expensive and all for nothing if the gameplay doesn't hold; ambience and the scoreboard come first (§4).

## Further Reading

- Game Design Handbook: writing core loops, difficulty and experience goals — the base document for §1 and §2 of this page.
- Programming Handbook: fixed timestep, adjudication, AI architecture and networking detail.
- Production Handbook: estimation, slices and scope control, used together with §5.
- Indie Survival: small-team slice selection and scheduling reality, complementing §3.5.
- Legal, Patents & Competition: the intellectual property policy for teams, players, competitions and editor content — the full expansion of §3.4.
- Art & Audio Handbook: the presentation budget for animation, stadium ambience and commentary.
- Homework: greybox a 1v1 match with one rule, and write down clearly what the adjudication layer and the arbitration layer each own; then pick a sports game you know well and log which real rules it simplified and which it kept, and how it makes you believe that "this shot counts".

What sports games sell is not fidelity but "the shot I pressed counts": trust the adjudication once and players dare to make the next move; trust a whole match's score and it's worth playing another.
