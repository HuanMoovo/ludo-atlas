# Ludo Atlas · Genre Handbooks · Social Deduction

> **Genre Handbooks · Volume 3**. Positioning: the multiplayer genre that makes "who is lying" its sole tension. Some players hold the truth and are charged with disguising it, while the rest have to piece the truth back together from deliberately incomplete information; speech, votes and the debrief are not packaging — they are the main gameplay itself.
> Companions: Game Design Handbook (information structure and core loop) · Programming Handbook (rooms, state machines and engineering architecture) · Multiplayer & Backend (matchmaking, anti-cheat and running costs) · Live-Ops & Growth (content updates and community governance).
> This page carries no external links; benchmark titles are widely known works only, and the figures here are common magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: social deduction is the genre that **manufactures conflict out of information distribution and settles win or loss in language**. Execution is nearly zero; winning and losing is decided by "who knew what and who believed whom"; it is also the most anti-single-player of games — with too few players, or with mouths shut, the game stops turning.

The core loop, written as a verb chain: `deal identities → act (commit the crime or gather evidence) → confront (speak, apply pressure, lie) → vote (to exile) → resolve (reveal identities) → debrief → next round`

The fuel for this loop is hidden identity: an identity is known only to the player and their faction, and everyone else receives second-hand information. The loop holds on two preconditions: every player must hold something no one else knows (§3.1), and every match must end with a debrief (§3.2). Without the first, the game degrades into rock-paper-scissors; without the second, winning and losing both feel arranged by the system.

Drawing boundaries against neighboring genres:

| Neighboring genre | Boundary |
| --- | --- |
| Party game | Party games (Eggy Party, Overcooked) make laughter out of execution and chaos; social deduction decides win or loss by speech and judgment, and execution is only a prop. |
| Asymmetric multiplayer | Asymmetric multiplayer (Dead by Daylight-like) is unequal in power but its information is essentially public, and the contest is maneuvering; the two sides of social deduction are comparable in power, and what stays hidden is identity and intent. |
| Co-op | In co-op everyone is on the same faction and a loss is blamed on coordination first; social deduction buries at least one internal fault line, so a loss is blamed on the impostor first. |
| Single-player deduction | Single-player deduction (Ace Attorney-like) reasons through a finished script and an answer necessarily exists; social deduction reasons about living players — there is no guaranteed answer, and the players themselves are the content. |
| Tabletop Werewolf | The two ends of one genre: the tabletop form runs on face-to-face ritual, the online form on voice, matchmaking and short matches; the flow and terminology are shared, but the paths to product could hardly be more different. |

A self-check question: lay every identity face up on the table — does the game still hold? If the answer is "yes", what you are building is more likely a party game or a co-op game than a social deduction game.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **The heartbeat of lying and seeing through lies**: a disguise has to hold the whole match, and a lie must be dismantled well when it breaks. This is the tension unique to the genre, one no other genre can deliver.
2. **The urge to be heard**: speaking is the stage. The good side's analysis and the impostor's fabrication are both performance, and the system has to set aside time and an audience for performance.
3. **Understandable losses**: losing to "he played it well" is an acceptable story; losing to "the system screwed me" is where churn starts. The debrief is part of the experience, not decoration.
4. **Zero execution barrier and natural spread**: no reflexes or practice needed — if you can talk, you can take a seat; one rule set keeps generating talk of "that trick from last round", and social spread is its engine.

Anti-patterns (stop and fix the moment they appear): a silent player can idle the whole match and still win with the crowd; for most of a match, no one gets to speak.

Benchmark titles (play them yourself before breaking them down; this genre's experience hides in "still wanting to say a few words about it after playing"):

| Title | What to take from it |
| --- | --- |
| Werewolf | The pure-language form of information asymmetry: one-by-one speeches, counterclaims, open votes and the debrief ritual; a complete sample of a tabletop game turned into an online app. |
| The Resistance: Avalon | The structure that replaces exile with team votes; mission vote tallies open the evidence chain section by section, clean and decisive. |
| Among Us | Anchoring speech to action and space: tasks, routes and body locations are all contestable; the design template for short matches, fast restarts and post-death spectating. |
| Goose Goose Duck | Scaling by adding identities instead of numbers: the method of extending with character skills and multiple factions; a mass-market sample tightly bound to streaming. |

## 3. Design Essentials

### 3.1 Information Asymmetry Is the Core

Draw an information map first: settle "what each player knows and what others do not", then talk about gameplay. Four resources are the entire material:

| Resource | Who knows it | How it is faked | How it is dismantled |
| --- | --- | --- | --- |
| Identity | The player and their faction | Bold fake claims, posing as an ordinary player | Cross-verify with skill information, settle accounts in the debrief |
| Actions | The faction and witnesses | Forged timelines, alibis | Witnesses, task progress, body locations |
| Speech | Everyone | Invented stories, steering the room, smearing | Catch contradictions and timeline conflicts |
| Votes | Public results (per design) | Riding the vote, hiding behind an abstention | Debrief the vote chain, see who is protecting whom |

Three hard requirements:

- Every player must hold something only they know. Without private information there are no lies, only guessing.
- Lies must be able to win: the disguised side needs operable paths (a fake identity, a fake route, a fake explanation) for the contest to hold.
- Every key conclusion needs at least one independent clue that can verify it. Self-check: cut all skills and witnesses and leave only speech and votes — does the game still run? If it does, the core is language and skills are only amplifiers; if it does not, go back and check whether you handed out enough clues.

### 3.2 The Rhythm of Discussion, Voting and Spectating

The live content of this genre is talking, so pacing design is scheduling it. Two mainstream discussion formats:

| Format | Match length | Strengths | Costs | Fits |
| --- | --- | --- | --- | --- |
| Ordered speaking turns | 20–40 minutes | Everyone gets a mic, and the interrogation chain is complete | Weak players are punished with standing and listening; online attention cannot hold | Voice rooms, sessions among acquaintances |
| Free discussion | 10–20 minutes | Tight, with a high density of highlight moments | Mic hogs dominate, and the silent are drowned out | Random matchmaking, short matches |

Common pacing parameters (magnitudes for reference): 30–90 seconds per speaker; a 10–60-second voting window; action and meetings alternate, and the number of meetings sets match length. Target anchor: no more than 20 minutes from entering the room to watching the results — go over, and you have a churn point.

Three things about the spectating experience:

- Death does not mean leaving: the dead go to a spectator channel, can watch the whole match but are forbidden from communicating with the living — cut the message channel at the technical level.
- Fast restarts and the stream defense line: the results screen must offer "play again" within 10 seconds; a streamer's viewpoint leaks every identity, so built-in delay, information occlusion and a streamer mode belong in the launch scope — viewer callouts (stream sniping) are a safety problem, not a low-probability event.

### 3.3 Matchmaking and Player Count: Cold Start Is the Fatal Weak Point

Player count is a hard threshold; set the scale first:

| Mode | Common player count | Notes |
| --- | --- | --- |
| Small match | 4–6 | One impostor, simplified map; used during cold start and while waiting for players |
| Standard match | 8–12 | The genre's main range, around two impostors |
| Large room | 12–16 | Multiple factions and a complex role pool; demanding on the flow |

Key constraint: players cannot be swapped once a match begins. Identities are already dealt, and swapping mid-match breaks the information structure, so the goal of matchmaking is "fill a whole match", not the continuous backfill of a MOBA. Responses to a player shortage, in priority order:

1. **Ready rooms plus a small-match mode**: a waiting room that shows "two players short" beats waiting inside a match; the 4–6 player small match simplifies the rules — play small matches while waiting, so the wait does not become churn.
2. **Friend rooms**: sessions among acquaintances are this genre's main scenario, not a compromise. Make sharing room codes and pulling friends in a core path — social spread is its cold-start engine.
3. **Pool merging, bots and regional concentration**: merge 8-player and 10-player queues into one pool filled at random — do not carve out smaller pools by player count that starve each other; bots go into practice rooms only, since a speaking bot is spotted instantly; during cold start open servers by region and time slot — better to queue than to have rooms that can never fill.

### 3.4 Premade Groups and Anti-Cheat

Premade groups cannot be cured: friends sitting together will talk, and you cannot police their mouths. The design goal is to shrink the payoff of unannounced teaming:

| Scenario | Problem | Countermeasure |
| --- | --- | --- |
| Party ranked | Friends on the same faction collude privately; strangers lose out | Separate pools for parties and solo players; cap party size; randomized nicknames and avatars in ranked |
| Malicious teaming | Strangers ally on the spot against a third party | Behavioral data (co-occurrence rate, vote-agreement rate) plus reports, with reputation-score penalties |
| Alt accounts | Two accounts in one match share one view | Device and network fingerprint deduplication, with strict validation within a match |
| Role-peeking cheats | X-ray view of identities and positions | Solve at the architecture layer: the server never sends information that should not be seen (§4) |
| Viewer callouts | A live stream leaks identities and positions | Built-in delay, hidden room information, banning viewers in the same match from taking part |

Evidence retention, tiered penalties and motive reduction — governance fails if any one is missing:

- Evidence retention and penalties: voice recordings, chat logs and vote chains must be inspectable; penalties tier from warnings to queue bans to account bans, with an appeal channel — the more transparent, the fewer wrongful convictions.
- Motive reduction: anonymization and pool separation thin out the payoff of cheating; do not let leaderboards make "showing off stats" the main pursuit.

### 3.5 Variants and Ongoing Content

The content formula: role pool × rule switches × maps. The only standard for a new role is that it changes "who knows what"; a role that only adds numbers or swaps a skin is an invalid update.

| Variant axis | Examples | Cost magnitude |
| --- | --- | --- |
| Roles | New information roles, new disguise roles, new factions | 1–3 days each (reusing the skill framework), with balance testing taking the bulk |
| Rules | No exile, double impostor, multiple factions, timed tasks | Days-level, but each needs validating |
| Maps | New scenes and task locations | Weeks-level; the largest art cost |
| Social | Text rooms, voice rooms, open room parameters | Low cost; community-made modes are the cheapest content |

Ongoing-content discipline:

- The default room is always the simplest rule set, and complexity opens to veterans only; never sell identities or information — cosmetics and passes are sellable, but selling resources that affect a match is selling win or loss.
- Set the update cadence by team size: small teams keep frequency up with the "roles plus switches" modularity; do the books for seasons and long-term operation along Live-Ops & Growth before making promises.

## 4. Technical Essentials

Settle one judgment first: this genre's networking demand is low-frequency — mostly turn-based messages — and it is not latency-sensitive. The real engineering difficulty is one sentence: information permissions — each client receives only the information it is entitled to see.

**Information visibility (an architectural decision to get right in version one)**

- Server authority plus per-perspective snapshots: identities, actions and votes are all adjudicated by the server, and clients submit only intent; the server computes "what this player may see" player by player before sending, and data that should not be seen never enters client memory. This is the foundation of anti-cheat, not an after-the-fact patch.
- Host-based rooms suit friend rooms only, since the host can see every identity; public matches demand dedicated servers. Both room types can be two options in one product, but the difference must be stated.

**Room and match state machines**

- Lifecycle: waiting, dealing identities, the loop (actions plus meetings plus votes), resolution, debrief, restart; every step must support disconnect and reconnect.
- Matches run 10–20 minutes and a disconnect is very expensive: reconnection windows, takeover for players who never return, and quit rulings must be explicit in version one; a match with identities already dealt cannot take replacements and only waits for the next round — make "waiting for the next round" a normal state, not an error message.

**Voice and text**

- Voice is the main battlefield of the live experience and also the most latency-sensitive, most expensive link in the chain: solve echo, crosstalk and turn-based mic control — the system opens the mic for whoever's speaking turn it is; text rooms need word-list filtering, spam rate-limiting and report-evidence retention, and input efficiency and quick-phrase templates decide the speaking rhythm.

**Anti-cheat and auditing**

- Event logs: actions, sightings, votes and chat land in the database with timestamps. The debrief screen, report evidence collection and balance analysis all depend on it — log from the prototype stage.
- Alt accounts and boosting: device fingerprints plus in-match deduplication; dead and spectator channels are physically isolated from the living, and streamer mode ships with built-in delay and information occlusion; stats are for reference only — do not let them become a motive for cheating.
- Telemetry watches four groups of numbers: role win rates, meeting counts, the correlation between speaking time and win rate, and mid-match quit rate. Data finds anomalies, replays find reasons; a report queue and support tooling are launch essentials, with server-side capabilities delivered along Multiplayer & Backend.

## 5. Content Volume and Workload Reference

The following are common magnitudes for comparable projects, for scope estimation only and not a commitment.

| Content | First playable version | Public launch version | Notes |
| --- | --- | --- | --- |
| Identities / roles | 3–5 | 15–40 | Reuse the skill framework, 1–3 days each; balance testing takes the bulk |
| Maps | 1 | 3–6 | The single item with the largest art cost |
| Action minigames | 3–5 | 10–20 | Half a day to two days each |
| Player-count modes | 1 | 2–3 | Small-match rules need testing of their own |
| Systems | Rooms, voice, voting | Matchmaking, ranked, reporting, debrief | Backend and community tooling are a long-term investment |

Workload magnitudes (solo, with existing multiplayer experience):

- Whitebox prototype (text rooms, one server): 2–4 weeks; first playable loop (with voice and restarts): 1–2 months; to public-testable (with matchmaking, anti-cheat and content moderation): 3–9 months — the reference range floats with how far you take it.
- After launch it is an ongoing account: servers, content moderation and community governance do not end at release — build up your reserves along the Indie Survival framework first.

Two optimistic facts: this genre needs less code than action games, and several benchmark titles were made by teams of fewer than ten people; the real barrier is not team size but assembling a roomful of players willing to play again and again. Two pessimistic facts: content is consumed fast, and slow role releases mean boredom; governance is a long-term cost and the biggest cause of death for games in this genre that go wrong.

## 6. How to Start the First Prototype

Goal: 2–4 weeks for the minimal loop of "one room, four identities, voice meetings, a debrief after the vote"; no art, no matchmaking, no seasons.

**Step 0 (half a day, no code): run three rounds by hand with playing cards and a group voice call.** You act as the moderator and record three things: did anyone start lying; did the losers accept the outcome; does everyone want another round. If the rules do not run, writing code only makes the mistakes more expensive.

**Step 1 (4–6 days): rooms, identities and the action phase.** Players join by room code, a match starts at 6 players, identities are dealt at random, disconnects can reconnect; one sketch map, one or two tasks and one kill, with player movement and discoverable bodies.

**Step 2 (2–3 days): meetings and votes.** Finding a body triggers a meeting; speaking order (clockwise or random); voting, tie rules and the exile sequence.

**Step 3 (2–3 days): resolution, debrief and logs.** Identity reveals, a replay of the key-event timeline, a "play again" button; actions, votes and chat land on disk, ready for the debrief and balance work.

Testing is a social activity from day one — this genre cannot be tested solo. Find 6–10 friends willing to play three rounds in a row and watch three things: how often people open their mics (someone silent the whole time means the pacing design failed); post-match mood (are they discussing "how did he pull that off" or "this game has problems"); exit behavior (do they actively pull people in, or make excuses to log off).

Success criteria (all observable):

- With all art stripped out, the test group wants to play three or more rounds in a row.
- After each round, at least half the players can say which piece of information they lost on, rather than attributing it to luck.
- At least one argument happens in which the debrief replays someone's exact words; someone actively pulls a newcomer into the next round, and the seed of social spread appears.

Not during prototyping: matchmaking, ranked, seasons, skins, multi-platform adaptation. The exception is information permissions — they change the architecture, so get them right from day one; everything else is a multiplier.

## 7. Common Pitfalls

1. **All clues random**: identities random and information random, so reasoning degrades into rock-paper-scissors. Every match must hand out enough verifiable information sources (action evidence, witnesses, skills).
2. **An unbalanced speaking economy**: speaking turns so long they count as a standing penalty, while silence carries no cost — good players are working for the idlers. Shorten the speaking limit or switch to free discussion, and give costs to not acting, not voting and not speaking (nudges, reputation score, no rewards).
3. **Two kinds of cheat written into the architecture**: a host acting as the server is a dealer cheating, so public matches demand server authority; anti-cheat must block role-peeking, alt accounts and callouts, and it starts from "do not send the information" — no patch applied afterward can save it.
4. **Voice on a third-party app**: with no official voice, random matches instantly become a premade party. Built-in voice or an official voice channel is standard for random matches.
5. **Nobody cares about the debrief**: the results screen says "you lost" and everyone leaves — players never learn and never accept it. Identity reveals plus a timeline replay are the basic courtesy of this genre.
6. **Mid-match quits that never come back**: an 8-player match with 2 gone collapses outright. Reconnection, takeover, quit penalties and a "wait for the next round" entry point — none can be missing.
7. **Roles pile up into confusion**: every update adds roles without teaching, and newcomers are crushed by twenty identities in their first match. The default room is always the simplest rule set.
8. **Selling identities and information**: paid roles that are naturally stronger, paid identity reveals — fairness collapses overnight. Monetization may sell cosmetics only.
9. **Ignoring content safety**: harassment, abuse and risks to minors in voice and text are regulars in this genre; filtering, reporting and human moderation belong in the launch scope, not in a live-ops catch-up class.

## Further Reading

- Game Design Handbook: core loops, social systems and validation methods — corresponds to §1 and §3.
- Programming Handbook: room services, state machines and engineering infrastructure — the underlying expansion of §4.
- Multiplayer & Backend: matchmaking pools, anti-cheat, economic security and server cost; §3.3 and §3.4 execute along its lines.
- Live-Ops & Growth: content cadence, community governance and version communication — the full expansion of §3.5.
- Indie Survival: scope control and scheduling — complementary to §5.
- Pitfalls & Anti-patterns: high-frequency pitfalls in social and online games — read against §7.
- Homework: pull six friends into three rounds of Werewolf or Among Us, and after each round ask everyone one question: "which piece of information do you think you lost on". A round players can answer on their own is a round this genre is doing right.
