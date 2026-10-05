# Ludo Atlas · Genre Handbooks · Party Game

> **Genre Handbooks · Volume 3**. Positioning: the genre that makes "the chaos of a room full of people having fun together" the first-order experience. Rules are learned at a glance, and winning gives way to laughs; the design object is not one person's challenge curve but the emotional curve of a whole room.
> Companions: Game Design Handbook (experience goals and core loops) · Programming Handbook (local input and device management) · Production Handbook (scope and scheduling for collection content) · Case Studies (benchmark breakdown and postmortem methods).

---

## 1. Positioning and Core Loop

In one line: a party game is the genre that **makes "a crowd around one screen, laughing and yelling" its first-order experience**. Players come for "that moment just now", not for a clear; a single round is measured in minutes, a whole session in hours, and the standard is laugh density, not difficulty curve.

The core loop, written as a verb chain:

`learn it at a glance → fight for points or cooperate → chaos erupts (someone turns it around, someone wipes out) → the whole room laughs out loud → settle the scores and talk trash → next round`

This loop is measured in minutes. It holds on two preconditions only: the barrier must be low enough that anyone can join in the first minute after sitting down (§3.1); and the chaos must have boundaries, so people feel "I overplayed that" rather than "the game is messing with me" (§3.3).

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Local multiplayer (couch multiplayer) | Local multiplayer is the delivery form of "shared fun on one screen"; the party game is a way of organizing its content: a minigame collection plus a flow director. The two overlap constantly, and the party form leans harder on low barrier and laughs first |
| Co-op | A party game can be cooperative or competitive; the core is having fun together. Co-op's pleasure lies in solving puzzles together or getting through a hard time, and the atmosphere is a by-product |
| Social deduction | Social deduction runs on information asymmetry driving discussion; party-game conflict happens at the level of execution and luck, and the jokes get told after the scores are settled |
| Competitive versus play | Competitive play pursues fairness and skill stratification; party games deliberately introduce randomness and chaos so that even the least skilled player gets a round they can win |
| Elimination courses (online game show) | The elimination course is one of the party game's flow skeletons (§3.2); the difference is room size and platform, and the design accounts are the same |

A self-check question: if you swapped everyone else on the screen for emotionless AI, would the game still be fun? If the answer is "much less so", you are making a party game.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Zero-explanation onboarding**: rules are learned at a glance, the first round is usually the tutorial, and sitting down to starting play takes no more than half a minute.
2. **Chaos and laughs**: every round produces at least one "that moment just now"; failure is part of the show, not a shame to be hidden.
3. **Everyone has something to do**: no long stretches of dead waiting from the start of a round to the scoring screen; eliminated players and players left behind always have a way to keep participating (§3.2, §3.4).
4. **Losers are happy too**: catch-up and reversals keep hope alive for whoever is behind, and the humor of the scoring screen outranks serious rankings (§3.3).
5. **One more round**: switching between rounds takes seconds, and the tension of the score plus fresh randomness pushes the next round forward.

Benchmark titles (play these yourself under living-room conditions; hold at least one real-person gathering before breaking them down):

| Title | What to learn from it |
| --- | --- |
| Super Mario Party | The benchmark for minigame collections plus a board-game flow; rounds are short and turns are clear, and the flow layer is content in itself |
| Overcooked | The textbook of cooperative chaos: failed communication is the punchline, and the difficulty curve serves shouting density |
| Super Smash Bros. | Fighting turned into a party: the barrier is lowered (items and stage hazards) while the skill ceiling for experts is kept |
| Mario Kart | Item-based checks and catch-up design: even the last-place player holds a comeback weapon, and nobody gets eliminated |
| Human: Fall Flat | Physical comedy: loss of control is designed as the main punchline, and wiping out is more watchable than clearing |
| Fall Guys | The online elimination show: turning the wipeout into a public spectacle that can be watched and shared |
| Eggy Party | Online party plus UGC: a permanent flow skeleton guarantees the floor, and player-made content carries the content ceiling |

## 3. Design Essentials

### 3.1 Low Barrier and Chaos Design

Low barrier and high chaos are this genre's two pillars: the barrier decides how many people are willing to sit down, and chaos decides the output of laughs.

- Barrier budget: a player should learn the controls within one round of watching someone else play. Converge the controls to one verb plus one direction (push, grab, jump, throw), with no more than two buttons; anything beyond that needs icon prompts to bring it back down to "learned at a glance".
- The first round is the tutorial: build no separate tutorial level — hide the rules inside a normal round; keep the target in view, make the first mistake free of cost, and let prompts follow the device (three icon sets for gamepad, keyboard and touchscreen; see §4).
- Chaos source list: random events (wind, falling objects), item disruption (reversals, position swaps), physical tumbling, and teammate sabotage (you can shove people, you can steal points). Every chaos source answers two questions: what punchline does it produce, and how much of the player's control does it swallow?
- Chaos discipline: put chaos on the outcome, not on the controls. Input must always track the hand, and a wipeout must be readable as "I got greedy just now" rather than "the game is messing with me".
- Laughs first: make the wipeout visible and retellable with exaggerated character animation and sound effects, and hand out a "charge sheet" at scoring time (blown up by your own item three times, and the like).
- Duration budget: one round of a single minigame runs 30 seconds to 3 minutes; split anything longer into two rounds — attention at a party drains by the minute.

### 3.2 Collection Structure: Rotation, Elimination and Scoring

A single minigame cannot carry a party. The unit of party-game content is the session: a set of minigames plus a flow line that strings them together; the flow line manufactures context (scores, suspense, reasons for revenge).

Three common skeletons:

| Skeleton | Structure | Fits | Main risk |
| --- | --- | --- | --- |
| Rotation | A fixed number of turns, minigames drawn at random or in rotation, advancing along one main track (a board, a scoreboard) | Long living-room sessions with 4–8 players | A main track that runs too long drags the pacing apart |
| Elimination | Each stage eliminates the bottom few until a champion is decided | Large online rooms, streaming and spectating | Eliminated players leave early; the spectating experience must be designed separately |
| Scoring | Each minigame scores independently, ranks accumulate | Any player count, drop-in drop-out | Strong players snowball; needs catch-up points and compensation design |

The flow-director layer must settle four things:

- Who picks the next one: random draw, the trailing side chooses, the winner bans a pick; the right to choose is itself social currency.
- How ties and dead heats resolve: leave it to the show (a tiebreaker round at equal scores), and never explain it with complicated rules.
- How scores are displayed: keep a small scoreboard resident; make the suspense visible before the endgame (double points in the final round, chain bonuses).
- Pacing switches: 5–10 seconds between rounds, a scoreboard flash is enough; any transition sequence longer than 10 seconds and someone starts checking their phone.

One acceptance check: strip the flow layer and leave a single minigame — how many plays before testers get bored? If three plays is enough, the session needs the flow layer for context, and you also picked the wrong first minigame (§6).

### 3.3 Losers Must Be Happy Too: Catch-up and Reversals

Winning and losing in a party game is the show bill, not a verdict. Whether the trailing player stays until the end depends on three things: whether a window to draw level still exists, whether failure is funny, and whether the scoring screen lets them keep their dignity.

Catch-up mechanics come in three tiers:

| Mechanism | How it works | The price |
| --- | --- | --- |
| Trailing compensation | The trailing player gets more or stronger resources (items, time, score multipliers) | The leader feels it is unfair; keep the compensation invisible and small in magnitude |
| High-variance events | Concentrate comeback chances in the endgame (double points in the final round, a big random event) | With variance too high, skill has nowhere to prove itself, and the expert's frustration is a real emotion |
| Ineffective-lead design | Leading changes only the ranking, not the experience (everyone is in the same on-screen chaos, everyone gets their moment) | It needs content volume to hold it up; the advantage is that it costs nothing |

Three exits for the loser; design each one, or the moment one is missing a player starts checking their phone:

1. **There is always a next time**: at every moment, keep alive a reason for "next round I get them back" — the item they never drew, the minigame they never got, the score that was just short.
2. **Failure gets a performance**: blow up the staging of the wipeout moment (hit animations, sound effects, replay), and hand out non-ranking awards at scoring (Worst Moment, Most Times Friendly-Fired). The losing player walks away with a story, not a score.
3. **A dignified exit**: in elimination structures, the eliminated need a spectator role, a vote, or the right to meddle (audience votes that extend time, and the like). Dead waiting is the fastest way to kill a room.

One rule: people may lose, but they must not be humiliated. Turn penalties into comedy material, not into humiliating actions.

Acceptance criteria: within 10 seconds of the final scoring, someone who lost the whole session either asks for "one more round" unprompted or tells someone else about the wipeout that just happened — either one counts as a pass; run 5 gatherings and observe; 0–1 mid-session departures by trailing players is a pass.

### 3.4 Local Multiplayer: Devices, Seating and Information Distribution

The party-game venue is one screen plus a crowd, and devices and seating are level design: who holds what, who looks where, who is waiting — all of it decides the experience.

- Device slots: decouple "device" from "player". Gamepads, keyboard halves and touchscreens each register as slots, and slots then bind to players (name, color, avatar); support hot-plugging and mid-session joins — a new player picks up a gamepad and presses any key to hop in, and leaving does not interrupt the round in progress.
- Phones as controllers: the big screen shows the picture while phones provide input and private information (the Jackbox Party Pack series is the representative). The desktop or TV carries the main view, players scan a code or enter a room code to open a web page, no install required; it fits turn-based, voting, quiz and text gameplay, while real-time action gameplay is sensitive to network latency and is steadier left on local gamepads. For implementation tiers see §4.
- Information distribution: public information goes on the big screen (scores, the state of play), private information goes to phones (prompt words, votes, roles). Information asymmetry is the cheapest content generator in party games: one screen, and everyone knows and worries about something different.
- Camera approach: prefer a shared view (one camera that fits everyone), because the punchline must happen on the same screen; split-screen tears one joke into two halves. A shared view must handle "does not fit": pull back, follow the group's area, and force everyone into frame at key moments.
- Waiting seats: people waiting for their turn, spectating and queuing each need a role. Any waiting window over 30 seconds must be shortened or given an alternative way to participate.

### 3.5 Minigame Quantity and Quality

- The quantity account: out of 20 minigames, usually only 8–12 are genuinely funny; set the pass line at "if it gets drawn, someone laughs". The plan: build 6–8 polished ones first, then expand through variants (the same mechanic with new parameters, a new theme, a new chaos source); variants do not count as new mechanics.
- Quality grading (run every minigame through three questions): does it get a laugh the first time? Does it still get one on the third play? On the tenth draw, are people still willing to play it? Fail any one question and it goes into the rework queue — do not hide behind quantity.
- Replayability, in order: random people > random minigames > parameter variants. A new group of players brings far more variation than one more minigame; first learn how your existing minigames perform across different crowds.
- Cutting discipline: the two with the lowest laugh density in small-sample tests get cut outright, no rescuing; rescuing an unfunny minigame costs more than building a new one.
- Relationship with the flow layer: only a unified minigame interface (§4) lets the flow layer rotate, combine and re-run them freely; adding a minigame means writing the gameplay itself and never editing flow code.

## 4. Technical Essentials

The engineering difficulty concentrates in four areas: input and device management, the minigame framework, visuals and camera, and networking (if you build phone controllers or online play). Everything below is engine-agnostic.

**Input and device management**

- Decouple player slots from devices: devices (gamepads, keyboard halves, touchscreens, phones) register as slots first, and slots bind to in-game players; every minigame reads only "player input" and never cares which device it came from. Hot-plugging, mid-session joins and device swaps all touch only the registration layer.
- Test the full mixed-device matrix: gamepad plus split keyboard is the living-room norm; each minigame declares the input types it needs (directions, button count), and the framework handles filtering and prompts.
- Button prompts follow the device: the same action shows the matching icon on gamepad, keyboard and touchscreen; prompting with the wrong device is a newcomer's biggest source of frustration.
- Mid-session joins and exits: joins take effect from the next minigame round without interrupting the one in progress; exits are covered by a bot or simply skipped, never pausing the whole room.

**Minigame framework**

- The unified interface is the first system to write: each minigame implements five things — init, input mapping, per-frame update, results reporting, teardown — and the flow layer knows only the interface, not the specific gameplay. Without this layer, scheduling explodes after the fifth minigame.
- Decouple the scoreboard from the minigames: minigames report raw results only (placement, score, time taken), and the flow layer handles conversion and display.
- Every minigame runs standalone: during debugging you skip the flow and jump straight into a single minigame; parameters (duration, difficulty, chaos frequency) live in config files and are hot-editable.
- Leave hooks for bot players and a solo self-test mode in the very first minigame; without bots you cannot test a four-player flow.

**Visuals and camera**

- The shared-view camera must guarantee that everyone stays in frame, key objects stay readable, and the main character is not lost in the chaos. Test method: screenshot at the peak of the brawl and check whether any player has left the frame.
- Big-screen adaptation: living-room TVs and projectors are viewed from a distance, so size the fonts, icons and color contrast for "readable from several meters away", and make icons the first choice for all tutorial and prompt text.
- Performance budget: cap particles and physics objects in chaos scenes; dropped frames destroy both game feel and punchlines at once, so set a separate frame-rate floor for the low-spec tier.

**Networking (phone controllers and online)**

- Getting started with phone controllers: self-hosted rooms on the local network plus a web-based controller, entered by room code or QR scan; for the complete protocol and fault-tolerance plan, follow Multiplayer & Backend.
- Do not put real-time action gameplay on phone network input: latency makes "my mistake" and "network lag" indistinguishable; turn-based, voting and text gameplay are where phone input shines.
- Disconnects and exits: if anyone in the room drops, the flow must continue (skip, hand over to a bot, re-seat them); a party venue has no patience for waiting.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimating scope; not a commitment.

| Project form | Content volume | Timeline | Notes |
| --- | --- | --- | --- |
| Single-minigame prototype | 1 minigame plus a scoreboard | 2–4 weeks | Validates "learned at a glance" and the laughs; do not build a collection yet |
| Small party pack | 6–10 minigames plus one flow skeleton | 3–6 months for a solo dev or small team | The most common starting form for indie teams |
| Full commercial party game | 20–30 minigames, multiple modes, local plus online | 1–3 years for a team | Content and polish dominate the cost, and the flow layer is often rebuilt time and again |
| Online party with UGC | The above plus servers, rooms and creation tools | 2 years and up | Content updates and live operations are a long-term bill |

Two hidden lines in the content account:

- Each minigame's hidden cost approaches the body of the game itself: tutorial staging, results screen, sound effects, failure animations, balance parameters, regression tests across every device combination. Book it as "half the game, half the support"; 20 minigames mean 20 staging pipelines, and frameworking (§4) is the only way to push that bill down.
- Variants are the most cost-effective expansion: one funny minigame plus three variants (new theme, new parameters, new chaos source) is far cheaper than building a new prototype, and the laughs are already validated.

Scheduling anchors: from zero to "one minigame that made a tester laugh" usually takes 2–4 weeks; to "a vertical slice of six minigames plus a flow skeleton" usually 3–5 months; after that extrapolate by minigame count and reserve rework time for the flow layer. Quantity is not the goal: 12 minigames that are each worth drawing beat 30 that are annoying to draw.

## 6. How to Start the First Prototype

The first prototype is one minigame plus a rough scoreboard, finished in 2–4 weeks, touching neither online, UGC, art nor story.

**Week 1: pick one chaos source and build a four-player shared-screen minigame.** One verb, one goal, one source of chaos (a random event or an item). Get the device layer running with four slots first (gamepads plus a split keyboard), and build the input registration and button prompts — they are the foundation of every minigame.

**Week 2: validate "learned at a glance" with real people.** Find four people who have never played it, give them no explanation, and let them start. Record three things: how many seconds until they start doing anything; when the first laugh lands; and who went quiet, and when. Silence is more dangerous than cursing — it means the player has stopped feeling involved.

**Weeks 3–4: add the roughest possible flow layer.** A scoreboard, three minigames (the latter two can be variants of the first), a results screen, and a "one more round" button. Validate that the flow layer can push "next round" forward.

Success criteria (all observable):

- A stranger starts playing within 30 seconds with no explanation, and the first round produces at least one room-wide laugh.
- Someone who lost asks for "one more round" unprompted, or tells someone else about the wipeout.
- Four-player shared screen never drops frames enough to affect control, and everyone stays in frame throughout.
- One player plus three bots can complete the whole flow (for self-testing, not for fun).

If acceptance does not pass, build no second minigame. This genre's first priority is to refine the "laugh formula": once the first minigame is funny, copy the formula into the second and third, rather than gambling on a new mechanic.

## 7. Common Pitfalls

1. **Explaining rules in text**: manuals, long tutorials, walls of prompts. Change it to learned-at-a-glance: one verb, icon prompts, the first round as the tutorial.
2. **Turning the party into a competition**: chasing fairness and skill depth makes the laughter disappear. The balance goal of a party game is "nobody gets crushed so hard they stop laughing".
3. **Designing for four players only**: 2 players, 3 players, 5–8 players, odd player counts, mid-session joins and exits all need contingency plans; the living-room headcount is never decided by design.
4. **Dead-wait windows out of control**: during eliminations, turn-taking or turn-based play, someone spectates for a long time. Waits over 30 seconds must be shortened or given an alternative way to participate.
5. **Bloated minigame counts**: piling up to 30, half of them unfunny, and drawing one feels like punishment. Cut until every single one is worth drawing.
6. **Randomness swallowing control**: too much chaos, input stops tracking the hand, and players put the blame on the game. Put chaos on the outcome, not on the controls.
7. **Catch-up design out of balance**: the strong stay strong and nobody follows along, while compensation that is too blatant (everyone targeting first place) triggers real resentment. Keep compensation invisible and put comeback chances in the endgame.
8. **Device matrix not fully tested**: only two gamepads on the dev machine were checked. Models, hot-plugging, joins and exits, prompt icons — build the matrix and run every item.
9. **Punchlines nobody can see**: the wipeout happens in a split-screen corner or on separate screens, and nobody laughs. Prefer a shared view and put the punchline on the same screen.
10. **Rough flow and results screens**: the opener, scoring and awards are all default UI. These screens carry half the laughs; give them a budget on par with a minigame.
11. **Going online too early**: heading to the network before the local game is funny enough, and latency and disconnects strangle the mood first. Refine the laugh formula locally before considering an online version.

## Further Reading

- [Game Design Handbook](../../fundamentals/game-design/README.md): the drafting paper for experience goals, core loops and number methods; corresponds to section 3 of this page.
- [Programming Handbook](../../fundamentals/programming/README.md): implementation details for input management, data-driven design and debug tooling; corresponds to section 4 of this page.
- [Production Handbook](../../fundamentals/production/README.md): estimation, scheduling and scope control, complementing section 5.
- [Case Studies](../../postmortems/README.md): methods for breaking down successful and failed projects; consult when choosing a direction or dissecting benchmarks.
- [Pitfalls & Anti-patterns](../../pitfalls/README.md): pitfalls around greenlighting and content production; read against section 7 of this page.
- [Indie Survival](../../../playbooks/indie-survival/README.md): scope control and path choices, complementing section 5.
- [Multiplayer & Backend](../../pipelines/multiplayer-backend/README.md): the sync, room and live-ops ledger for phone controllers and online party play — the full expansion of section 4.
- Exercise: hold one gathering of 4–6 people and record three numbers: when the first laugh lands in the first round, the minute at which someone starts checking their phone, and how many times a loser says "one more round". Those three numbers are this handbook's acceptance sheet.
