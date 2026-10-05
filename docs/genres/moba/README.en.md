# Ludo Atlas · Genre Handbooks · MOBA

> **Genre Handbooks · Volume 3**. Positioning: turning "five players, one symmetric map, a fresh start every match" into a competitive product; single-hero control, three lanes, team economy and a ranked ladder — four systems meshed into one long-running fighting machine.
> Companions: Game Design Handbook (loops and economy) · Programming Handbook (data-driven design and networking fundamentals) · Multiplayer & Backend (synchronization, matchmaking and anti-cheat) · Esports & Competitive Design (balance, spectating and events).
> This page carries no external links; the reality warning for small teams sits in §5: the bills for the hero pool, ladder population and anti-cheat start burning from day one.

---

## 1. Positioning and Core Loop

In one line: MOBA is the team-competitive genre in which **five players each control one hero, fighting to the rhythm of lanes and resources on a diagonally symmetric map**. It collapses the management and execution of an RTS into a single character, then amplifies five players' division of labor into the main variable of victory: execution decides the local fight, exchanges decide the whole match.

The core loop, written as a ring of verbs:

`last-hit in lane → trade and poke → recall to heal and buy → roam and reinforce → contest neutral objectives → teamfight and push → take towers toward the base → the next exchange`

The loop mixes two time scales: second-level last-hits, abilities and positioning, and minute-level lane management, objective contests and item timing; above those sit the match level (lane assignment, build paths, push tempo) and the meta level (patch balance, hero pool, ranked environment). A match typically runs 20–40 minutes, and the mobile form typically 10–20; between matches only rank, proficiency and cosmetics carry over, and all numbers reset to zero — this is the divide between the MOBA and progression-based competitive games.

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| RTS | You control a single hero, with no base building and no multi-front production; the MOBA is the RTS made by subtraction, "management" replaced by "a character" |
| Action RPG | The growth curve resets every match and both sides' numbers are symmetric; victory is destroying the enemy base, not farming gear |
| Auto battler | The same hero subject matter, but execution and hand speed are stripped away entirely, leaving only economy and composition; in the MOBA, execution is the pleasure itself |
| Battle royale and tactical shooter | They also have seasons and ranks, but no vertical structure of lane waves, economy and tower pushes; a match settles in one go |

A self-check question: shrink five players into a 1v1 and three lanes into one lane, and if the fun barely changes, what you have validated is an action game rather than a MOBA; everything this genre adds uniquely lives in the layer of "multiplayer division of labor multiplied by map management".

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Instant payoff for execution**: last-hits, ability trades and last-second kills — every action gives feedback at the second scale, and a mistake can be reviewed down to the exact beat.
2. **The achievement of team effort**: division of labor, reinforcements, saves, initiations and protection — an exchange between five people carries more weight than a solo duel, and is more worth rewatching.
3. **Lose with understanding, come back from behind**: victory and defeat must trace back to a specific exchange and a specific economy gap before players will file them under "the match"; the trailing side needs tools to bite back and the snowball needs a ceiling for a game worth watching and worth playing (see §3.3).
4. **Long-term growth and identity**: hero pool, rank, proficiency and cosmetics form the long-term reason of "who I am, what I practice"; watching matches and streams is an extension of the gameplay, not packaging.

Benchmark titles (play them yourself before breaking them down; lane feel cannot be learned from match videos alone):

| Title | What to break down |
| --- | --- |
| Dota (a Warcraft III custom map) | The genre's origin: three lanes, last-hits and denies, and an item-driven "one match, one world" framework |
| Dota 2 | The baseline of systemic depth: denies, couriers, active items and mechanics colliding — a high ceiling and a high barrier |
| League of Legends | The on-ramp engineering and esports-system sample: ability indicators, clearer information expression, league and season operations |
| Honor of Kings | The mobile-form sample: touch controls, match length compressed to a dozen minutes, competitive play brought into mass social play |
| Heroes of the Storm | A different answer: shared experience and no personal items — a test of what happens when individual economy is removed |

## 3. Design Essentials

### 3.1 Map and Lane Structure

The MOBA map is a metronome: three lanes push offense and defense on schedule, the jungle and river give reasons to step away from lane, and bases and towers define the ladder of the push. Fix the geometry first, then the numbers.

| Element | Structure | Design function |
| --- | --- | --- |
| Base and towers | Each side's base holds one corner of the map, with towers placed along the lanes | The ladder and metronome of the push: every tower taken shifts map control and the safe zone once |
| Three lanes | Top, mid and bottom; mid is the shortest, the side lanes are longer | Length sets return speed and roam radius: mid is the reinforcement hub, the side lanes are the battlefield of resources and lane play |
| Jungle | Neutral-camp areas wedged between the lanes, split half and half between the two sides | The jungler's income source and roaming corridor; vanishing from lane manufactures information asymmetry |
| River and objectives | Public ground cutting across the middle of the map, spawning periodic buffs and epic neutral objectives | The reason both teams get pulled off the lanes to fight; the main stage for vision contests and teamfights |

Geometry discipline: the map is symmetric about its diagonal centre (rotate it 180 degrees and the two sides swap places). Any bias where "one side is closer to a resource" must be balanced with an equivalent; diagonal symmetry also naturally produces an advantage lane and a disadvantage lane, which is why lane assignment and lane swaps are the first set of decisions in a match.

Lane cadence (typical ranges): one wave every 25–30 seconds, growing in size and strength over time. Last-hitting, denying, wave control and camp pulling — "fighting without fighting" — set the floor of economy and experience; the full last-hit income of one lane wave is the economy's base unit of account (§3.3).

Information structure matters as much as geometry: fog of war, wards, high ground and brush make up the vision system. Vision is the MOBA's intelligence economy: who sees whom first decides whether an encounter is a meeting or an ambush; "how vision is gained and how it is countered" must be written into the first version of the map rules, not treated as a system bolted on later.

### 3.2 Hero Design and Roles

Heroes are the main body of content and the smallest unit of balance. Write duties first, numbers second; if roles are not separated, no amount of number tuning will save them.

| Role | Duty | What it fears | Power window |
| --- | --- | --- | --- |
| Tank (front line) | Initiate, soak damage, hold key positions | Ground down by sustained damage; cannot dictate when to engage or disengage | Early to mid teamfight, once durability comes online |
| Fighter | Secondary front line, single-lane duels and split-pushing | Being kited and poked; helpless under a chain of crowd control | Mid game, small-scale skirmishes |
| Assassin | Dive the back line, delete a single carry | Hard crowd control and grouped protection; with no way in, its value drops to zero | One item window from mid to late game |
| Marksman | Steady sustained damage, tower damage and cleanup | Being jumped; with no front line it has no room to deal damage | Late game, once the front line and its items have both come online |
| Mage | Area damage and control, mid-game burst | Forced open during ability downtime; falls off once magic resistance comes online | Mid game, at the peak of ability levels and items |
| Support | Protection, vision, initiation and rescue | When teammates collapse, its utility stops paying | All game long, carried by judgment rather than economy |

Write this as a counter chain: the tank uses control to push damage dealers out of safe positions, the assassin uses burst to punish isolated carries, the support uses protection and counter-engage to void the assassin's dive, and the carry grinds through the tank with sustained damage. When this chain closes, a composition has a skeleton; heroes outside the chain must either have a clear utility role (tower pushing, split-pushing, global support) or be merged or cut. Counters mostly live at the level of position and vision, not numbers: hard counters should be few and tunable (anti-heal, detection, crowd-control cleanse), with counterplay slots left for items and compositions — avoid matchups where "you lose at hero select".

A hero's kit is usually one basic attack plus three to four abilities, at least one of them a dash or a control, with one ultimate carrying the hero's highlight. Two disciplines:

- Every hero must be expressible in one sentence of "the situation where nothing else will do"; if you cannot write it, merge or cut the hero.
- Role differences come from ability kits, not from reskinned numbers; every hero needs strong and weak windows, and "no weak phase at any point" is where balance accidents start.

### 3.3 Economy and Experience Curves

Economy is the MOBA's second health bar. Fix the income sources before the prices; work out the "income budget per minute" before discussing the price of any single item.

| Income source | How it is earned | Design role |
| --- | --- | --- |
| Last-hitting | Killing minions or jungle monsters; income goes only to whoever lands the kill | The individual economy floor; turns the laning phase into a game of profit and loss |
| Kills and assists | Killing enemy heroes; assists share the payout by rule | Volatile, high-risk high-reward income; sharing the payout is what makes it a team affair |
| Team resources | Taking towers, killing epic neutral objectives, wages and passive income | Converts "one player is strong" into "the whole team is strong"; gives supports and junglers an income line that does not depend on last-hitting |

Two rules for experience and levels:

- Experience allocation between solo and duo lanes decides lane assignments: two players in a duo lane split one share of experience and naturally lag behind a solo lane in levels — the mathematical basis of roaming and pressure.
- Level gaps need an exchange rate: write how many stats each level difference is worth into a table — "what one level is roughly worth in gold" is the core exchange rate of all balance reasoning; the level cap and the ability-unlock cadence, in turn, decide at which minute a match hits its climax.

Anti-snowballing is a required course in the economy system and the divide between a MOBA and a "snowball simulator":

- **Shutdown bounties**: the longer the kill streak, the higher the bounty, paid out in one lump when that hero dies — turning the leader from hunter into prey.
- **Catch-up compensation**: the trailing side receives partial experience or economy compensation (the form varies by title); the defensive reinforcement of high ground, base and towers buys time to hold out and wait for mistakes, so a comeback path exists objectively rather than by the opponent's charity.
- **Acceptance question**: can the side that has led for 10 minutes close the match out in 3 without suspense? If yes, the snowball is over the limit.

### 3.4 Balance and Patch Updates

Balance is not about leveling win rates flat but about maintaining a diverse, readable meta. Build the ledger before you touch anything:

- **The ledger has three tables**: hero win rate (split by rank bracket), pick rate and ban rate. Watching overall win rate alone misses the meta rot at high ranks; the first two weeks of a new patch are basically noise as a sample — do not draw conclusions from them (for the method see Esports & Competitive Design §4).
- **Order and rhythm of changes**: numbers first, then mechanics, with reworks after every other tool; changes at the game-feel level are the most expensive because players have to rebuild muscle memory. At the same time, hold the line of "one theme per patch": nerf assassins, buff supports and rework items all at once and players will treat patches as random events.
- **Patch notes must state what changed and why**: speaking with data and giving reasons for changes are the daily deposit of live-ops trust (for patch cadence and community communication see Live-Ops & Growth §5 and §8).

Patch cadence: the seasonal model is the industry norm — major changes cluster at season boundaries, and the version is frozen before major tournaments; write "when major changes are allowed" into a policy instead of deciding case by case.

### 3.5 Matchmaking, Anti-Cheat and the Esports Ecosystem

The long term rests on three systems: matchmaking decides the experience of every session, anti-cheat guards the delivery of the competitive promise, and tournaments decide how efficiently population and content are amplified.

- **Matchmaking is a product foundation, not a backend feature**: hidden MMR separate from displayed rank, pool discipline (newcomer pools, quarantine pools), and wait-time constraints relaxing with the population level; autofill and lane assignment also belong in matchmaking design — nobody wants to be autofilled three queues in a row (for the methods see Multiplayer & Backend §4).
- **Anti-cheat is the ground you stand on**: client-side detection, server-side behavior statistics, and reporting with manual review — all three layers are indispensable; packet modification, wallhacks and scripts are the MOBA's three mortal enemies, and server-side validation plus behavior analysis is the only reliable gate (Multiplayer & Backend §7).
- **Tournaments are an amplifier, not a lifeline**: the ladder is the root of players and viewers; official tournaments are a long-term cost center. Before running one, audit three things: is the spectating experience clear, does the team have event operations and broadcast capability, and can the daily active population support both matchmaking and viewership (Esports & Competitive Design §5 and §7). Spectating and replays are the foundation of all of it: reviews, content creation and broadcasts share one set of infrastructure — leave room for it in the architecture phase (Esports & Competitive Design §3).
- **The fairness red line**: keep monetization focused on cosmetics and expression (skins, battle passes) and decouple heroes and power from payment as far as possible; selling power is self-evidently unfair inside a ranked ladder and burns competitive trust directly (Live-Ops & Growth §10).

## 4. Technical Essentials

The engineering difficulty concentrates in three places: server-authoritative real-time combat, the game feel of abilities and hit detection, and the data-driven toolchain. Everything below is engine-agnostic; the MOBA mainstream runs state sync (authoritative server simulation plus client prediction and correction), not the classic lockstep of RTS games (for the on-ramp map see Programming Handbook §5, and for the model choice Multiplayer & Backend §2).

**Server authority and synchronization**

- Damage, economy, cooldowns and drops are all computed on the server; the client only gathers input and predicts presentation. "Anything the server can decide, the client never decides" is a security floor, not a performance option.
- Client prediction must be restrained: movement and basic attacks may start locally, but ability hits and gold changes defer to the server, with deviations smoothed away at the presentation layer. Reconnecting after a drop is a hard requirement: a match runs twenty-odd minutes, so a dropped connection must have a way back; write the rules for reconnects and AFK players (bot takeover or a loss ruling) before launch.
- Track network quality in tiers (latency, packet loss and jitter measured separately); work out the cost in advance on the "one game-server instance per match" model (Multiplayer & Backend §8).

**Combat, abilities and game feel**

- Ability input is the MOBA's first game feel: tap-to-cast and hold-to-show-indicator, release-to-confirm coexist; direction and range must be what-you-see-is-what-you-get, and input buffering and ability pre-input directly set the execution ceiling.
- Basic attacks are the hidden protagonist: wind-up, projectile, hit feedback and attack-moving (stutter-stepping) are tuned frame by frame — they are the technical floor under last-hitting and trading.
- Hit detection and visuals must agree: hitboxes, projectiles and effect attachment points use one set of data; lag compensation (hit-rewind style solutions) must go in early — otherwise ranged and melee heroes split into different feels under the same network conditions, and "it looked like a hit but did not register" becomes a bad-review hotspot.

**Data-driven design and toolchain**

- Heroes, abilities, items, lane wave timings and monster spawns are all table-driven; balance iterations change tables only and ship as hot updates without downtime — that is how the live cadence breathes (Multiplayer & Backend §8).
- Reserve replays and spectating from the architecture phase (for the spectating engineering checklist see Esports & Competitive Design §3): record inputs or snapshots; replays serve player reviews, tournament broadcasts and anti-cheat review at the same time, and are a source of balance telemetry probes; once the hero count passes double digits, balance without statistical support inevitably runs away.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for scoping estimation; not a commitment. Numbers are a ruler — calibrate them against your own team's speed.

| Project form | Content scale | Time reference | Notes |
| --- | --- | --- | --- |
| Gameplay prototype (room-based 3v3) | 4–8 heroes, 1 simplified symmetric map, one win condition | 3–6 months for a small team | Validates only the lane and teamfight loop; no ranked mode |
| Small competitive title | 12–20 heroes, 1–2 maps, light ranked plus baseline anti-cheat | 1–2 years for a small team | Balance and servers are the main bills |
| Commercial-scale MOBA | A hero pool on the order of a hundred, multiple maps and modes, a season and tournament ecosystem | 3–5+ years for a team, plus continuous operations | A live-service product, not a one-off project |

Breaking down the bills:

- **Per hero**: ability and number design, concept art, model and animation, VFX, SFX, voice, the skin pipeline and balance testing; at commercial scale a single hero costs person-months, and every new hero adds a row to the matchup tables of every existing hero.
- **Balance**: per-patch tuning, data runs, patch notes and community communication are fixed overhead; the more heroes there are, the more maintenance cost grows with combinations.
- **Servers, security and behavior governance**: per-match game servers, matchmaking services, anti-cheat and report review settle monthly, and shutdowns and server merges are long-term bills; AFK players and toxic players eat retention directly, and the headcount for reputation systems and review must go into the budget up front.

**The realistic path for a small team.** Scale the shape of a commercial MOBA down proportionally, rather than up to fit the dream:

| Dimension | Commercial MOBA | Small-team starting point |
| --- | --- | --- |
| Scale | 5v5, a hundred-hero pool | 3v3 or 1v1, 8–12 heroes |
| Match length | 20–40 minutes, full economy and builds | 10–15 minutes, compressed levels and item slots |
| Matchmaking | Multi-pool ranked and anti-cheat quarantine | Room-based with hidden MMR; add light ranked later |
| Servers | A dedicated server fleet | Start on an off-the-shelf backend (Multiplayer & Backend §5) and validate the gameplay first |
| Tournaments | Leagues and a licensing system | Community-run events; no official commitments |

If what draws you is the thrill of team competition, validate your scope on co-op runs or room-based competitive play first; if what draws you is esports, read Esports & Competitive Design §7 first: when the daily active population cannot fill ranked matchmaking, tournaments are a river without a source.

## 6. How to Start the First Prototype

The first prototype answers one question only: after a 3v3, 10–15 minute match, do you want another one? Lock the scope: 1 whitebox symmetric map (one lane plus two jungle areas validates most of the loop), 4–6 heroes (3 abilities plus 1 ultimate each), 2–3 towers plus a base per side, room-based online play, server authority. No ranked mode, no skins, no tournaments.

- **Weeks 1–2: the online skeleton.** Rooms, synchronized movement on both clients, server-side hit detection for basic attacks and one ability; write it server-authoritative from day one — do not build single-player first and bolt on networking later.
- **Weeks 3–4: the economy loop.** Lane waves spawning, gold from last-hits, experience and levels, recall and purchase; set "the full last-hit income of one lane wave" as the economy's base unit of account (§3.3).
- **Week 5: objectives and towers.** Tower offense and defense, one neutral objective (a periodic buff or empowered lane waves are both fine), and a working win condition from tower pushes to the base.
- **Weeks 6–7: hero differentiation and practice AI.** Get the 4–6 heroes to play genuinely different roles; add simple AI in a practice range, and build replay export and test scripts.
- **Week 8: human playtest.** Get 6 people into two teams for three consecutive evenings and record three things: the action they get stuck on most often, the most infuriating way to lose, and the most satisfying way to win.

Starting parameters (copy and adjust): a match target of 10–15 minutes; lane waves every 25–30 seconds; heroes starting at level 1 with a prototype cap of 5–8; 4–6 item slots with 10–15 items in the shop; 2–3 towers per side.

Acceptance criteria (all observable):

- The 6 testers play three evenings in a row and organize the next match on their own; after every match, the losing team can say which exchange or which stretch of economy gap they lost to.
- Disconnect reconnection and AFK handling have been rehearsed at least once for real; nobody can change damage or gold by editing local files.
- Change one item or ability by 20% and you can state its effect on win rate within a day; if you cannot, the data and tools are not in place yet.

## 7. Common Pitfalls

1. **Scoping at the commercial scale**: five bills arrive at once — 5v5, a hundred-hero pool, ranked, anti-cheat and tournaments — and a small team does not survive the second year; read the scaled-down path in §5 first.
2. **Client authority**: with damage, gold and cooldowns computed locally, packet modification and scripts break the ladder open overnight; all resolution happens on the server.
3. **Overlapping hero roles**: a batch of reskinned numbers with no leverage point when it comes time to balance; give every hero a "nothing else will do" duty first (§3.2).
4. **No economy baseline, no snowball ceiling**: last-hits and jungle camps are each tuned by gut feel, and within ten minutes players find one optimal route nobody can counter; the leader snowballs out of reach and the trailing side has no tool to bite back (§3.3).
5. **Balancing on overall win rate alone**: meta rot at high ranks stays invisible inside the average; read win rate, pick rate and ban rate split by bracket.
6. **Frequent overhauls of game feel and mechanics**: muscle memory is a competitive player's sunk cost, and every change is paid for in trust; keep overhauls inside the season window.
7. **Splitting matchmaking pools too early**: modes, party size, rank and premades stack into multiple layers of pools, the population is diced into pieces, and queue times kill the game before balance does.
8. **Client-only anti-cheat**: it shatters at first contact with professional cheats; server-side behavior statistics and report review are the real battlefield (Multiplayer & Backend §7).
9. **Tournaments before the ladder**: tournaments only amplify results; until the ladder population and the viewing experience are in place, running events is self-indulgence (Esports & Competitive Design §7).
10. **Behavior governance and communication left vacant**: AFK players, flamers and malicious teaming do not eat one match, they eat retention — reporting, reputation and review flows must exist from launch day; patches that change without saying so consume trust just the same, and the "the designers are teaching you how to play" impression comes from changing without saying (Live-Ops & Growth §8).

## Further Reading

- Esports & Competitive Design §3, §4, §5 and §7: spectating systems, balance methodology, the tournament ecosystem and "when not to do esports" — the full expansion of §3.5 and §7 of this page.
- Multiplayer & Backend §2, §4, §7 and §8: sync models, matchmaking, anti-cheat and the cost ledger — the expansion of §4.
- Game Design Handbook §2 and §4: core loops, numeric tables and economy-system methods — the underlying draft of §3.3.
- Programming Handbook §5: the on-ramp map for networking and multiplayer fundamentals; read it before §4.
- Live-Ops & Growth §5, §8 and §10: patch cadence, community communication and monetization ethics — companions to §3.4 and §3.5.
- Indie Survival and Pitfalls & Anti-patterns: scope control and high-frequency pitfalls, complementary to §5 and §7.

Exercise: pick a public replay of a high-level match (League of Legends or Dota 2 will do), record both sides' economy gap, tower count and level gap every 5 minutes, plot them as three curves and locate the minute where the match turned; then, against the checklist in §3.3, see what the trailing side used to hold on and at which point the leading side missed its closing window.

A MOBA's outcome is written in the exchanges between five players, not in one hero's number table. Make "finish a match and want another" real first; talk about hero pools, ladders and tournaments after that.
