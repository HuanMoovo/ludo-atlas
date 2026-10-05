# Ludo Atlas · Genre Handbooks · Co-op Horror

> **Genre Handbooks · Volume 4**. Positioning: the multiplayer genre that makes "being scared together with friends" the core experience. In a crowd, fear runs by different rules: it gets shared, spread and amplified — and also diluted by clustering and small talk; half the designer's job is keeping the supply of fear ahead of the sense of safety that teammates bring.
> Companions: Game Design Handbook (core loop and pacing) · Programming Handbook (networking fundamentals and performance) · Multiplayer & Backend (sync, voice and the full backend pipeline) · Live-Ops & Growth (update cadence and community operations).
> No outbound links. Benchmark titles are limited to widely known works; numbers are common magnitudes — calibrate against your own project's measurements. The general mechanics of fear (atmosphere, sound, pursuit) live on the Horror page; this page covers only the part about what changes when fear meets a crowd.

---

## 1. Positioning and Core Loop

One-line positioning: co-op horror is the genre that **turns "being scared together" into a product**. What it sells is not one person's fear but the whole live scene of "several people screaming at once, laughing at once, making it back alive and immediately debriefing"; the monster is just the machine that produces that scene.

The core loop as a verb loop:

`take a contract and enter the map → split up to investigate or scavenge → collect evidence and raise the stakes → decide to extract → carry it out and settle up → go for a bigger bet`

The loop runs 15–40 minutes per session and stands on three premises: the goal is not to kill the threat but to get something done right under its nose (§3.2); extraction is more tense than arrival (§3.2); and death has a price — heavy enough that you don't dare gamble, light enough that you dare come back (§3.4).

Drawing boundaries with neighboring genres:

| Neighboring genre | Boundary |
| --- | --- |
| Single-player horror | Single-player is one person being fed scripted scares; online, several people scare and rescue each other — the teammates themselves are the biggest variable |
| Co-op | Co-op's default assumption is "it can be done"; co-op horror assumes things go messy, and retreat is often the right call |
| Asymmetric multiplayer | Asymmetric is player-versus-player hunting with one side playing the monster; in co-op horror everyone is on the same side and the system plays the threat |
| Survival crafting | In survival crafting, growth eventually removes the threat; co-op horror requires the threat to still stand after growth |
| Extraction shooter | In an extraction shooter the opponent is other players; in co-op horror the opponents are the system and your own nerve, and incidents mostly come from mistakes and luck |

One line on the boundary with single-player Horror (Volume 3): there, fear is scripted and fed one-on-one; here, fear is produced live by the team — who falls behind, who panics, whether to rescue — all new sources of fear.

A self-check question: mute all voice chat and play a run again — does the threat itself still stand up? If it doesn't, you're selling "friends", not horror; both businesses are viable, but know which one you're in.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (ranked by priority):

1. **Shared screaming**: fear only becomes a memory and a talking point once it's shared; the mark of a good run is someone unable to stop debriefing "that moment" afterwards.
2. **It only counts if you carry it out**: the win condition is completing the objective and coming back alive, not clearing the map; however heavy your firepower, something must remain untouchable.
3. **Mutual need**: every player owns one thing no one else can do (carrying the camera, running the breaker, doing the rescues); dependency is fear's amplifier.
4. **Screams and laughter on the same frequency**: being scared into a scream and laughing until you can't stop are the two ends of one nerve; this genre doesn't reject comedy, but comedy must sit on a bed of fear.
5. **Survivor narrative**: who pulled the monster, who forgot to close the door, who almost didn't make it out — that is the story; the results screen should turn a session into an accident report.

Benchmark titles (gather a squad of about 4 and put a few sessions into each before breaking them down; half of what these games deliver lives in the squad's chemistry, and videos don't teach it):

| Title | What to learn |
| --- | --- |
| Phasmophobia | The standard skeleton of investigate–evidence–extract; evidence tools are the division of labor; the truck doubles as safe room and shop; fear comes from waiting, not jump scares |
| Lethal Company | The quota economy and the mental accounting of death drops; the oppression of abandoned facilities; screams and laughter on the same frequency in four-player chaos |
| Left 4 Dead 2 | The complete vocabulary of four-player co-op: the director system pacing the action, the safe-room structure, downed-and-revive, special infected and coordination |
| Content Warning | The minimal loop of film–upload–get paid; turning "the riskier the shot, the higher the views" into revenue; high replayability at small scale |
| The Outlast Trials | Bloody chases compressed into repeatable trial missions: mission structure and long-term progression turn a single escape into a repeatable run |

## 3. Design Essentials

### 3.1 The mechanics of fear in a crowd: what amplifies, what dilutes

Multiplayer is not "single-player horror times four". In a crowd, fear is pulled by two forces at once:

| Variable | Amplifies fear | Dilutes fear |
| --- | --- | --- |
| Positioning and division of labor | Objectives force splitting up; isolated stretches; the regroup itself becomes an event | Four players moving shoulder to shoulder; the whole squad becomes a walking safe zone |
| Voice | Proximity distance and death silence; a teammate's breathing and silence are information | Nonstop small talk turns a horror film into a comedy routine in three minutes |
| Death cost | Drops and retrieval runs, quota losses — pressure infects the whole team | Free respawns; tension zeroed out |
| Objective structure | Extraction is harder than arrival; timers and quotas force trade-offs | The objective is just to kill everything, then leave |
| Information | Evidence and anomalies are visible to only some players; retellings degrade | Once the guide is memorized, the ghost becomes a flowchart |

Three design disciplines:

- **Splitting up is the fear production line**: stage moments that force separation, like "one person throws the breaker, one person guards the door"; when two people do the same job together, fear gets split evenly away. Splits need timers and a rendezvous point, or getting separated just becomes boring.
- **Voice must be mechanized**: set rules for "who can hear whom, and when" (proximity falloff, walls between, a death channel), so that speaking carries both risk and reward; third-party voice chat will always exist, and built-in voice only gets used if it has mechanical value.
- **Attrition is the pressure curve**: losing players must change the situation immediately (quieter, slower, more afraid), not just leave "time to restart"; being grabbed, going down or falling behind must each leave a playable aftermath (§3.4).

### 3.2 The core loop: investigation, evidence and extraction

Three common in-run skeletons; pick the structure before you talk about skin:

| Structure | Goal | Reference | Feel |
| --- | --- | --- | --- |
| Investigation | Collect a fixed number of pieces of evidence and identify the threat | Phasmophobia | Slow-burn, waiting-heavy |
| Scavenge-for-quota | Gather valuables, meet the quota, carry them out to settle | Lethal Company | Greed-driven, opt-in risk |
| Mission list | Complete several objectives, then extract | The Outlast Trials | Level-based, coordination-heavy |

Shared discipline:

- **Extraction is the second climax**: the trip back must keep its variables (battery running low, the threat escalating, hauling loot slowing you down); before heading out, offer one "should we grab one more thing" choice; an extraction with no return pressure is just a results button.
- **It only counts if you carry it out**: in-run earnings feed into out-of-run progression (gear upgrades, tool unlocks), and death losses have a floor; at least let "what this run taught me" land somewhere, or failure leaves nothing but standing in the corner.
- **15–40 minutes per session**: beyond that, fear becomes physical labor; playing 3–6 runs in an evening is the common pattern, so content must be randomly re-sequencable (§3.6).
- On the investigation line, evidence must be retellable (sayable clearly over voice), scattered across multiple locations (forcing splits), and allowed to be misjudged (you must decide before the evidence is complete — that's what makes the tension real).

### 3.3 Division of labor, voice and information

Division of labor follows the co-op genre's three complementary layers (ability, information, timing), plus one this genre adds: **fear tasks get divided too**. The bold scout and bait, the meticulous own evidence and timing, the timid hold the rear and cover the retreat; everyone fears differently, so fear should not be distributed evenly.

- Tools are roles: each piece of equipment maps to one verb and one responsibility (the light carrier owns visibility, the camera operator owns revenue, the instrument user owns judgment); the tools need one another, and no single player can carry the whole kit.
- Information splits into two layers: the shared layer (objective progress, teammate position and status) doesn't eat voice bandwidth; the private layer (the evidence in your hands, the anomaly you saw) must be worth shouting about; non-voice fallbacks must be complete (pings and quick phrases — borrowing the discipline from the Co-op page).

### 3.4 Attrition, rescue and where death goes

- Attrition cuts both ways: fewer people means more fear (firepower and efficiency down), but also more quiet and focus; good attrition design gives each survivor their own way through.
- Where you go after death matters more than death itself: staying in the run (as a ghost, on the monitors, over the radio) beats being kicked back to the lobby — visible but unable to help keeps both engagement and dread alive; this choice sets the emotional undertone of the whole game.
- Rescue must cost something (abandoning your current task, taking a risk, burning resources), or rescue becomes a free extra life; make a total wipe settle as a tellable accident (debrief the causes of death, keep part of the haul), not a guillotine.

### 3.5 Pacing and safe zones

- Tension and release follow the sawtooth curve from the Horror page, with one extra beat in the multiplayer version: the departure room (truck, base, lobby) handles registration, inventory and socializing; after departure, pressure rises monotonically and the return trip cashes it out; safe rooms get a stricter trust boundary — absolute safety belongs only to the departure room, and in-run safe spots are absent or extremely brief, or with more players the safe zone turns into a chat room and the pressure drains away.
- Distribution has to be built into the design: streaming and video are this genre's main acquisition channel, so incidents must be understandable, highlights must be clippable, and the level's flow must let viewers follow "what they're afraid of".

### 3.6 Content units and update cadence

Content is managed as a four-piece set: **maps, threats, items, rules** (challenges and difficulty tiers).

- A map is a stage: layout, assets, sound, interaction points and balance passes each count as a line item; the same scene is recombined into multiple states through lighting, props and sound — invest first in the "re-dress" pipeline (borrowing the reuse discipline from the Horror page).
- A threat is one behavior archetype (patrol, hunt, perception, deception, environment) plus skin and parameters; build reusable archetypes, not one-off monsters.
- Players consume fast: 3–6 runs an evening, and the first-look content is gone within a week. Set the update cadence by your own capacity (Live-Ops & Growth): a map plus a threat plus an event as one content pack, interleaved with weekly challenges and difficulty toggles, kept alive by re-sequencing and new threats; promising a cadence your capacity can't hit is this genre's most common cause of death.
- Veterans inevitably go numb: the only answers are rotation and additions — write that into the update plan instead of pretending it won't happen.

## 4. Technical Essentials

The engineering splits into two parts: networking and voice. For online discipline at the gameplay layer, see §4 of the Co-op page; for sync selection and the full backend pipeline, see Multiplayer & Backend.

**Networking and sync**

- Scale facts: rooms commonly hold 2–4 players, so the architecture choice is far more forgiving than a battle royale. Start with host-authoritative plus room codes (near-zero cost, best for friend groups), defer public matchmaking and dedicated servers, then evaluate against the selection table in Multiplayer & Backend §1 and the cost math in Multiplayer & Backend §8.
- Minimum sync set: position and facing, action state, held items, doors and switches, pickups, threat position and state machine (run on the authority), and the random seed. Anything that can be left unsynced, leave unsynced.
- Threat AI runs on the authority; clients only smooth presentation; chases and hiding resolve first, perform second — accept a bit of latency rather than "I clearly hid, but it judged me dead".
- Design disconnects and joins as high-frequency paths: on disconnect, don't remove the character immediately (suspend it or hand it to simplified AI), and on reconnect restore inventory, objective progress and timers; settle the fairness rules for mid-session joins up front.
- Safety and governance: private rooms, kicks and reporting come first (griefing teammates is more common than cheating); add a reputation and ban system when public matchmaking arrives (Multiplayer & Backend §7).

**Voice**

- Built-in voice needs mechanical value: proximity falloff, walls and occlusion, a death channel isolated from the living channel, and visualization of who is speaking.
- Voice relay: use an off-the-shelf VoIP service (Vivox, Photon Voice or an engine built-in, for example) or self-host; test echo cancellation, crosstalk and mobile-network jitter most heavily; channel switching must not be a hard cut.
- Treat voice as a gameplay resource: talking attracts the monster, doors muffle words, the dead can't give the living intel — make "staying silent" an active strategy; non-voice players get the fallback channel of pings and quick phrases, and callouts and calls for help must all be completable through it.

**Debugging and testing**

- Ship network simulation toggles (latency, packet loss, jitter) in the first version; cross-region two-player sessions are a standard test item.
- Multiplayer tooling: multiple local clients, one-click session start and section skipping, threat events on demand; store match records and replays from the prototype stage on, for three uses — debriefs, balance sampling and evidence for reports.

## 5. Content Volume and Workload Reference

The following are common magnitudes for projects of this kind, for scoping estimates — not a commitment.

| Form | Content scale | Timeline scale | Notes |
| --- | --- | --- | --- |
| Prototype | 1 map, 1 threat, one complete loop | 2–4 weeks | Online plus voice already working; everything else whitebox |
| Small complete title | 2–4 maps, 3–5 threats, a basic item pool | 3–8 months | Meta progression and matchmaking kept simple |
| Common indie release scale | 4–8 maps, 6–10 threats, events and challenges | 1–3 years | Update capacity determines the lifecycle |
| Live-service scale | 10+ maps, threats and modes added continuously | Years | The content pipeline and community operations are the main body of the work |

- Per-map cost: layout and flow, assets (including "re-dress" variants), sound, interaction points, balance passes, online testing; whiteboxing is fast, atmosphere is detailed — a 3–5× blow-up factor is common.
- Per-threat cost: behavior archetype plus animation skeleton (reused), sound effects (the best-value investment), counterplay design (players must know what to do, or at least how to run).
- Online testing costs more than a single-player project of the same scale: changes get walked through by player count and duo combinations, and budget 1.5–2× for the logistics of organizing real squads.
- The reuse lever is randomization: layout, threat pool, item and objective placement decide replay value; one good map's reuse rate is worth more than one extra mediocre map.

## 6. How to Start the First Prototype

Goal: 2–4 weeks to get "one small whitebox map, one threat, one complete loop, 2-player online with voice" up and running, validating three things: does the loop hold together, does the threat keep up the pressure, and what does two-player play do better than solo. Don't touch production art or meta progression.

| Milestone | What to build | Acceptance (watch behavior, not questionnaires) | Reference time |
| --- | --- | --- | --- |
| M1 Loop skeleton | Run "enter the map, find the goods, carry them out, extract" end to end in a whitebox map | Not boring even solo blind-tested; real trade-offs | 3–5 days |
| M2 One threat | Patrol and perception, one chase, one hiding spot | Players can state the rules while being chased; zero lock-ups | 4–6 days |
| M3 Online and voice | Host opens a room, friends join, proximity voice | 30 minutes of cross-network play with no breakdowns | 5–7 days |
| M4 Fear check | A minimal pass of lighting and sound | Solo with voice off is tense; with voice on there are screams and laughs | 3–5 days |
| M5 Squad test | A squad of about 4 playing three runs back to back | When it ends, they ask for "one more run" | 3–5 days |

Three rules:

1. First validate that "multiplayer makes this better", then expand the map; a horror that can stand on its own shouldn't be counting on multiplayer to save it.
2. Build real voice early: interim solutions skip proximity design and hand you wrong test conclusions.
3. Record only three things per test round: who shouted what, and when; where people laughed; where it went quiet; strip away all art — it only passes if the threat's rules and pressure still stand.

Success criteria (all observable): the test squad produces natural voice calls (callouts, calls for help, joking) within two runs; afterwards they can retell "who did what and why they died", and what they discuss is "how to coordinate next time".

## 7. Common Pitfalls

1. **Clustering is invincibility**: four players moving as one and the threat loses its pressure; split-up sections and isolated situations are a required course (§3.1).
2. **Small talk eats the fear**: voice turns into a comedy routine in three minutes; mechanics must make talking both valuable and risky (§3.1).
3. **Death for free**: a death without cost zeroes out the tension; costs must leave room to "recover half of it back" (§3.4).
4. **An extraction with no drama**: the objective is two steps from the door; the return trip must keep variables and one trade-off (§3.2).
5. **The threat only bites one person or gets stuck on walls**: an AI lock-up hurts immersion more than failing to catch you; target selection needs explainable rules.
6. **Devoured by guides**: threats and tricks never rotate and veterans see through the hand within three days; keep it alive with new maps, new monsters and difficulty toggles (§3.6).
7. **Treating random matchmaking as the main path**: the quality of stranger lobbies is uncontrollable; friend rooms and room codes are the main venue — build kicks and private rooms first.
8. **Forcing voice**: without pings and quick phrases as a fallback, you're shutting non-voice players out at the door.
9. **Server costs off the top of your head**: get host-authoritative working first, then do the dedicated-server math per Multiplayer & Backend §8; a four-player room is not zero cost.
10. **Horror as mere packaging**: swap the threat for a sticker and the flow still runs — that means the objective structure has come loose from the fear; the self-check question is in §1.

## Further Reading

- Genre Handbooks · Horror (Volume 3): fear's resource model, atmosphere and sound design — the emotional-engineering draft for this page; boundary in §1.
- Genre Handbooks · Co-op (Volume 3): general methods for complementarity, rescue and communication design, cited throughout §3 and §4.
- Multiplayer & Backend: sync selection (§1, §2), service layering (§3), matchmaking (§4), anti-cheat (§7), cost and operations (§8); the full expansion of §4.
- Live-Ops & Growth: the math of release cadence, events and community operations — the companion to §3.6.
- Game Design Handbook: core loop and numbers-table methods — the draft under §1 and §3.
- Pitfalls & Anti-patterns: online and content-production pitfalls, to check against §7.
- Homework: get about 3 friends together for an evening of Phasmophobia or Lethal Company and record two moments — the loudest minute and the minute when everyone suddenly goes quiet — and which mechanics each happened under; then build a 10-minute whitebox map and have the squad run it three times, watching how what everyone fears changes from pass to pass.

Co-op horror ultimately tests only two things: whether the threat can sustain pressure, and whether the team grows stories on its own. When both hold, friends are both this genre's best source of fear and its best safety net.
