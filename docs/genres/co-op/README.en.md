# Ludo Atlas · Genre Handbooks · Co-op

> **Genre Handbooks · Volume 3**. Positioning: the genre that **makes "needing each other" the core pleasure**. Complementary roles, information asymmetry, rescue and call-outs form the design skeleton; this page covers co-op mechanics, difficulty and player-count scaling, communication design, the gameplay-layer networking basics, and how to start the prototype.
> Companions: Game Design Handbook (core loops and balance) · Programming Handbook (networking basics and performance) · Multiplayer & Backend (sync, matchmaking and the full backend path) · Case Studies (how to break down a case).
> Division of labour: the full path of sync models, matchmaking, anti-cheat and backend costs belongs to Multiplayer & Backend; this page settles only the gameplay-layer accounts.

---

## 1. Positioning and Core Loop

One-line positioning: co-op is the genre that **makes "needing each other" the core pleasure**. In a single-player game the player solves problems for themselves; in co-op the player must solve problems together with another person; every segment must be able to answer the same question: without the other player, does this still work?

The core loop, written as a verb ring:

`Observe your teammate's position and state → Divide the work → Execute your own parts → Cover each other (revive, fill in, relay) → Regroup and breathe → Next stretch`

This loop adds an "align information" beat that a single-player loop does not have. One more person means one more layer of communication cost, and also more misunderstanding, more rescue and more shared highlights; good co-op design turns that beat itself into content rather than treating it as friction. The loop rests on two preconditions: the dependency is real (§3.1) and failure is cheap (§3.3).

Drawing the boundary against neighbouring genres:

| Neighbouring genre | Boundary |
| --- | --- |
| Party games | The fun of a party game is chaos and laughing together: wins and losses are light and rounds are short; co-op has a clear success goal and pressure |
| Local multiplayer | Local multiplayer only describes the form of "sitting at the same screen", and can be cooperative or competitive; co-op is a gameplay relationship, which both online and local play can carry |
| Raids and co-op online games | Once the player count reaches double digits and social economies and long-term progression pile on, the problem domain becomes an MMO; co-op's common scale is 2–4 players and level-by-level stages |
| Single-player with AI teammates | When teammates are supplied by the system, communication and misunderstanding disappear — that is a single-player game with a different control scheme, not co-op |

A self-check question: if you replaced the teammate with an AI, would the game still hold up? If it holds up everywhere, you are making a single-player game with an online mode; if it breaks down everywhere, you are making co-op.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Feeling needed**: each player's skills and actions are irreplaceable in the system; missing one person breaks the run.
2. **The immediate reward of communicating**: one shout, one marker, and the teammate responds at once; language itself is an input action.
3. **Shared highlights**: a victory can be retold as "who patched what at which moment", and it is worth telling other people.
4. **Low-pressure griefing**: failures caused by chaos and mistakes are funny; failures caused by system punishment are infuriating; retries must be fast and cheap.
5. **Growing chemistry**: each player's own proficiency and the pair's coordination both show visible progress — the main source of long-term retention.

Reference games (find a partner and complete a playthrough together before breaking one down; you cannot learn coordination from watching video alone):

| Game | What to learn |
| --- | --- |
| It Takes Two | Enforced two-player division of labour, high-density mechanic swapping, narrative bound to gameplay |
| Overcooked! 2 | Communication pressure, information asymmetry (orders read and dishes cooked in separate places), the comedy of chaos |
| Deep Rock Galactic | Class complementarity, division of labour in procedurally generated levels, atmosphere and ritual |
| Portal 2 | The information gap in two-player puzzles, communication design where "you have to say it out loud to get through" |
| Monster Hunter: World | Quest structure for co-op hunts, how preparation and loadouts create differences in cooperation |

## 3. Design Essentials

### 3.1 Complementarity Design: Make Both Players Irreplaceable

Complementarity comes in three layers, shallow to deep: ability (one dismantles, one crosses), information (one can only see, one can only act), timing (one holds the window, one executes). The deeper the layer, the more real the dependency.

- Every character needs a verb the other does not have: pull, lift, charge, scout, unlock; that verb must be called on frequently across levels before players treat it as their identity rather than a one-off key.
- Beware fake complementarity: two players doing the same thing with the workload merely doubled is "side-by-side single player". The test is to delete one side's verb and see whether the level can still be completed.
- Give each verb at least three uses (the same "pull": pull a lever, pull a teammate, pull a heavy object); chemistry only begins to appear on the second or third use.
- Leave gaps in the dependency for independent play: a division of labour that demands identical pacing becomes following in lockstep; one that allows improvisation on the spot holds up longer.
- Two players couple most deeply and suit strong-dependency design; four players couple more loosely by nature, and the structure of "each has their own task line, converging at the end of the stage" is more stable.

### 3.2 Information Asymmetry: The Fuel for Communication

Information asymmetry is the core device that makes players speak up: one side holds information the other cannot see (a list, a code, a map, a status), the other holds the ability to act, and only the two together make a complete answer.

- Every piece of asymmetric information needs a "say it and it can be executed" channel: if it cannot be said clearly or cannot be understood, the result is a deadlock or silence.
- Keep a shared layer permanently on: mission objectives, teammate position and state (health, ammo, downed), resource levels — put them in the HUD or a marker system so they do not consume voice bandwidth.
- Control the number of communication points at any one moment: no more than two items to align at the same time; past that, communication turns from strategy into noise.
- Pings are the fallback for voice: there must be combos you can play without speaking up, or you are filtering out half your players.
- Put call-out peaks at the climax of a stretch and schedule breathing room between stretches; constant high pressure drags communication into mutual blame.

### 3.3 Rescue Mechanics: Failure Covered by the Other Player

Rescue is the emotional core of the co-op genre: the few seconds when one player sprints over after a teammate goes down are remembered longer than ten minutes of smooth clearing.

- Make most failures "rescuable": the survival window after going down, the time to revive, and the protection time after being revived — define all three parameters explicitly and make them all tunable.
- Settling failure only when the whole team is down is the classic structure that keeps tension alive; at the same time, players must be able to read "why it is not over yet".
- Rescuing has a cost: risk while pulling someone up, dropping what you are carrying, giving up a damage window. A rescue with no cost is a free respawn and zeroes out the tension.
- Consecutive downs need a price (each rescue heavier, resources consumed), or rescue becomes infinite extra lives.
- In single-player mode the object of "rescue" is the system (self-revive, drones, loading a save); define that rule set separately — do not patch it onto the two-player rules.

### 3.4 Difficulty and Player-Count Scaling

The goal of scaling: 2, 3 and 4 players all sit in a "busy but winning" state, and each has their own job. That requires a change of structure, not a multiplier.

- List of things to scale: enemy count, per-unit threat (control and one-shots), resource generation, mission requirements (numbers, time limits, routes), and rescue and respawn rules.
- The more players, the higher the coordination cost, and the burden on any one player should fall: enemies can be more numerous, but per-unit punishments should be softer.
- Use linear "health times player count" scaling sparingly: the result is not harder, just a longer slog against a damage sponge.
- Dynamic difficulty is common practice (see Left 4 Dead's Director, which paces pressure to team state), but it needs upper and lower bounds — do not let players notice they are being let off.
- Validate both player-count and character combinations: each extra supported headcount adds a whole set of scaling and level checks; 4 selectable characters paired up make 6 combinations. Also, state "minimum players required" plainly on the store page; that is cheaper than adding scaling after the fact.

### 3.5 Communication Design: Turn Call-outs into Mechanics

Dialogue in a co-op game is not social decoration; it is a core input device. The goal: make players speak up at the right moment, for the right reason.

- Create "must shout" moments: synchronised actions (press together), relaying information (codes, directions, colours), and calls for support (revive me, cover me, let me through) — rotate the three types.
- Build "shouting pays off" loops: when a teammate responds, give immediate positive feedback (a switch turns, an enemy drops), so that speaking up gets reinforced.
- Budget communication bandwidth: at most two pieces of information that need aligning per combat stretch; split complex information into fragments that can be relayed in batches.
- Offer a ladder beyond voice: quick phrases, markers, emotes, each a fallback for the one above; in fast stretches, typing is always too slow.
- Validate with real conversation: record two-player test sessions and count the calls and their content; all silence or all shouting are both signs that the design is not working.

### 3.6 Two-Player First, or Single-Player Viable

Answer one question first: in the core loop, is the existence of the second person itself the fun?

- If yes, go two-player first (the It Takes Two route): customise every segment for two; the cost is that players must find a partner and the release surface narrows, so the store page and trailer must make this clear in the first second.
- If not, make it single-player viable with optional co-op: co-op is an amplifier, and whether the amplifier is worth building depends on the budget.
- Cost order of single-player fallbacks: local co-op is the cheapest (no network code needed); online co-op sits in the middle; AI teammates are the most expensive, having to supply half of the real interaction, and the workload is routinely underestimated.
- A common self-deception: build a single-player version first, "add co-op later". When the core loop depends on a second person, the single-player version is the wrong foundation to begin with; when it does not, what you add later is just side-by-side single player.

## 4. Technical Essentials

This page covers only the gameplay-layer networking accounts: what must be synchronised, which interactions fear latency, and whether a disconnect is gameplay or an exception. For sync model choice, service layering, matchmaking and backend costs, see Multiplayer & Backend.

### 4.1 First Define the Minimal Sync Set

Networking starts from "what is the least we must send"; anything that can go unsynced stays unsynced:

| Gameplay object | Sync cost | Gameplay-layer response |
| --- | --- | --- |
| Character position and action state | Low | Standard handling for state synchronisation |
| Grabbed and carried heavy objects | Medium | Single-side authority (whoever grabs it owns it), or turn the heavy object into a follow animation |
| Synchronised actions (pressing together, entering together) | Medium | Judge with a generous window, confirmed uniformly by the authority |
| Shared resources and progress (cargo, ammo, switches) | Low | The authority counts; clients only send intent |
| Ragdolls, ropes, stackable objects | High | Limit them or turn them into scripted animations; do not build a whole physics sync stack for them |

### 4.2 Gameplay-Layer Networking Discipline

- Decide authority early: host authority or server authority — for the choice itself, see §1 of Multiplayer & Backend; it decides "what happens when someone drops". Whether the survivors carry on or the game pauses after a teammate disconnects is a design question, and the prototype stage must answer it.
- Rescue, grabbing and synchronised actions are the three most latency-sensitive interactions: give them generous checks (lead-in and widened windows), or design them so that cross-region players are not required to synchronise tightly.
- Reconnecting must restore gameplay state: position, inventory, quest progress, timers — not just the network connection.
- Define fair rules for joining mid-run: how progress and gear are granted, and whether the newcomer catches up first or watches first.
- Local co-op is a separate route: split-screen or a shared camera, with the performance budget doubled for rendering, and input handling for assigning and disconnecting two controllers.
- Build network simulation switches (latency, packet loss, jitter) in from the first version; friends playing across regions is the norm, not an edge case.

## 5. Content Volume and Workload Reference

The following are common magnitudes for comparable projects, for estimating scope, not as promises.

| Project shape | Content volume | Timeline magnitude | Notes |
| --- | --- | --- | --- |
| Two-player prototype | 1 co-op room | 2–4 weeks | One complementarity mechanic plus one rescue loop, local same-screen |
| Small co-op title | 8–15 short levels | 3–6 months | A single mechanic axis, local or online two-player |
| Common indie co-op title | 20–40 levels or one repeatable level pool | 1–3 years | Level density and online polish take the biggest share |
| Four-player co-op | Procedural generation plus long-term progression | 2–4 years | Balance and the content pipeline are the main costs |

Three accounts unique to the co-op genre:

- **Animation and state volume**: every playable character needs a full action set (idle, move, interact, carry, downed, being rescued, rescuing), and the character count multiplies straight onto it; cooperative animations are produced in pairs — one set for the one pulling, one for the one being pulled.
- **Testing cost**: every change has to be run through per player count and partner combination, plus a "busy/idle distribution" check confirming both players always have something to do. Testing volume for this kind of project is higher than for a single-player title of the same size; budget 1.5 to 2 times when scheduling.
- **Level reuse**: two-player levels are very hard to slice and recycle into single-player content, so do not assume reuse in the budget; conversely, a high-quality co-op room usually has higher replayability than a single-player level.

## 6. How to Start the First Prototype

The first prototype builds only one room, finished in 2–4 weeks, played by two people, local same-screen first, touching no story, saves, menus or online code.

**Week 1: the two-player complementarity prototype.** Two characters with one exclusive verb each (push and pull, dismantle and assemble), and one door that can only be passed cooperatively. It is supposed to look ugly.

**Week 2: the rescue and failure loop.** Going down, rescuing, and the full-wipe retry connected seamlessly, compressing the time from failure to restart to seconds.

**Weeks 3 to 4: information asymmetry and call-outs.** Add one information channel only one player can see (a list, a code, a map) and watch whether testers speak up on their own, and what exactly they say.

Networking order of operations: first validate with local two-player that "the gameplay really needs a second person", then spend budget on online; start online from direct host connections, and leave matchmaking and dedicated servers until after gameplay validation.

Success criteria (all observable):

- Strip out art and sound, and the two testers will speak up to each other on their own, saying game information rather than tutorials on how to control the game.
- When testers retell the round they just played, they say "we", not "I".
- Fake one side disconnecting for thirty seconds and the other side shows clear frustration; if they do not care, the dependency is not real.
- After a failure the two discuss "how to coordinate next time" instead of blaming each other.
- In every stretch both players have a clear task; specifically record the time when "one is busy, one is waiting" and press it to the minimum.

## 7. Common Pitfalls

1. **Fake complementarity**: two players doing the same thing with the volume merely doubled. Delete one side's verb and the level still clears — that is side-by-side single player.
2. **One player riding along**: one side does all the work while the other looks at the scenery; the centre of gravity of the division of labour should rotate between stretches.
3. **Call-out bandwidth overload**: demanding alignment on three or more things at once slides players from communication into shouting at each other; budget the peaks.
4. **Punishing individual mistakes**: in co-op, responsibility is naturally blurred; when a teammate "gets you killed", a blame screen or a heavy penalty sours the atmosphere instantly.
5. **Free rescue**: a rescue without a cost is infinite extra lives, and the tension and highlights vanish together.
6. **Scaling as multiplying health**: more players just means a thicker damage sponge; change the demand structure, not the numbers.
7. **Treating disconnects as exceptions**: dropping out, quitting and joining mid-run are all high-frequency paths, and the gameplay rules (continue, pause, reconnect) must be written in advance.
8. **Forcing voice chat**: with no pings and quick phrases as a fallback, you are shutting non-voice players out of the door.
9. **Network before gameplay**: building the network before the gameplay is validated means amplifying a signal that does not exist yet with the most expensive amplifier.
10. **Ignoring "can't find a partner"**: two-player-first narrows the audience and the release surface; this is a matter to face head-on at kickoff and on the store page, not a line in the store description saying "single-player supported".
11. **Promising AI teammates too early**: AI has to supply the interaction volume of a real teammate and the workload is routinely underestimated; do not put it in your launch promises before a playable version exists.
12. **Designing only to an expert's pace**: a level designed around skilled players makes the partner's experience fall off a cliff; align difficulty with "the slowest player".

## Further Reading

- Multiplayer & Backend: sync models, service layering, matchmaking, anti-cheat and the cost accounts; the counterpart to §4 of this page — read it before going online.
- Game Design Handbook: core loops, number tables and validation methods — the drafting paper for complementarity design and scaling design.
- Programming Handbook: networking basics and performance budgets; when building local split-screen, cross-reference the rendering and input handling.
- Case Studies: the method for breaking down public cases; when breaking down a co-op title, read "who saved whom, and when" as design evidence.
- Level Design Handbook: metrics, guidance and pacing for co-op levels — the expansion of the level-design part of §3.
