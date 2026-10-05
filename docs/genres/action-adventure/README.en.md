# Ludo Atlas · Genre Handbooks · Action-Adventure

> **Genre Handbooks · Volume 4**. Positioning: weaving the three pillars — exploration, combat and puzzles — into a journey whose pacing you control, using handcrafted space and measured cinematic staging to keep supplying "discovery" and "conquest". This page covers three-pillar ratios, miniature-garden structure, item reuse, staging costs and scope accounting.
> Companions: Game Design Handbook (core loops and experience pillars) · Level Design Handbook (miniature gardens, guidance and pacing) · Programming Handbook (camera and staging systems) · Case Studies (benchmark breakdown methods).
> This page carries no external links; benchmark titles are widely known works only, and the figures here are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: action-adventure is the genre **with exploration as its skeleton and combat and puzzles as its flesh and blood**. Players push through one handcrafted, zoned small world after another — discovering new areas, clearing obstacles, fighting their way through — and at the end arrive at a showdown worth the trip. The three pillars are all indispensable: exploration alone is a walking sim, combat alone is a beat 'em up, puzzles alone are an escape room.

The core loop, written as a verb chain:

`get an objective or get curious → enter a new zone → solve puzzles to open the way → clear the combat → acquire a new item → backtrack to clear old obstacles / open new routes → advance`

This loop is measured in minutes; one round trip of explore–puzzle–fight–reward usually takes 10–20 minutes. It holds on two preconditions: the three pillars rotate without dragging on each other (§3.1), and each new item pays off within ten minutes (§3.3). Zoom out to the hour scale and the loop becomes "advance zone by zone → expand the toolset → reread the world".

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Open world (a structural label) | Action-adventure uses zoned miniature gardens to control pacing and cost, and sells a curated journey; the open world sells free roaming and large-map scale. Simply scaling a miniature garden up does not make an open world — only a bigger, emptier miniature garden. |
| Metroidvania | Metroidvania spreads ability gates across one continuous map, and revisiting and rereading that map is the core pleasure; action-adventure's zones are relatively independent and advance mainly linearly — items can open doors, but backtracking is not the main gameplay. |
| Action RPG | Action RPG progression lives in gear and numbers, with grinding and builds carrying the long-term loop; action-adventure progression lives in new tools and new gameplay. Numbers stay restrained, and winning or losing comes down more to understanding and timing. |

A self-check question: ask playtesters to retell "where you went, what you picked up, what you did with it". If they can, the three pillars are working together; if they can't, the exploration stretches were probably just commuting.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **A sense of discovery**: every ridge crossed and corner turned has something worth seeing; the map is content, not backdrop.
2. **A sense of control**: combat can be read and countered, mechanisms can be understood and reasoned about; success and failure trace back to yourself.
3. **Rising and falling pacing**: combat, puzzles, staging and exploration alternate, tension and release rotate, and no stretch overstays its welcome.
4. **Progression that pays off**: a new item rewrites puzzles, combat and routes at once, and is usable within ten minutes of pickup.
5. **Journey memory**: what players remember in the end is a journey; landmarks, music and staged moments all keep the journey's books.

Benchmark titles (all widely known works; play them yourself before breaking them down):

| Title | What to learn from it |
| --- | --- |
| The Legend of Zelda: Ocarina of Time | The original template for the three pillars: an item-centric puzzle language, lock-on combat and the 3D camera baseline, miniature-garden zones. |
| The Legend of Zelda: Breath of the Wild | The upper bound of exploration freedom and system interaction: items and environment rules reused everywhere, a map driven by curiosity. |
| God of War | Seamless handoffs between staging and play; combat feel and narrative given equal weight; in-game dialogue carries much of the story. |
| Uncharted series | Staging-driven section pacing: climbing, puzzles, gunfights and cutscenes rotate; chase sequences are built as staged set pieces. |
| Tomb Raider (the reboot trilogy) | Audiovisual guidance for environmental puzzles, layered scene mechanisms, control over exploration density. |
| Batman: Arkham Asylum | Three-pillar choreography inside a single miniature garden: stealth, group combat, puzzles and information feedback. |

## 3. Design Essentials

### 3.1 The Three Pillars and Their Ratios

The three pillars are not three equal slices of content but three voices modulating each other: exploration decides where players go, combat and puzzles decide what they do there, and only rotation creates rhythm. Common ratios (rough shares of playtime; magnitudes for reference):

| Approach | Explore : combat : puzzle | Core logic | Main risk |
| --- | --- | --- | --- |
| Zelda-style | 4 : 3 : 3 | Puzzles extend exploration; combat is the metronome | Puzzle sections slow combat-minded players down |
| God of War-style | 3 : 5 : 2 | Combat is the spine; puzzles and climbing buffer the pacing | Puzzles degrade into errands and players just want to skip them |
| Uncharted-style | 5 : 3 : 2 | Staging and climbing drive progress; combat is the section climax | Not enough gameplay depth; staging carries the show |

The ratio is an output, not a target — first write a division-of-labor table for one 30-minute stretch of experience (what the player does, in what order), then count the shares afterward. Three rules:

- One dominant pillar per scene: no trash mobs during puzzle sections, no mechanism puzzles stuffed into combat sections; mixing happens only in deliberately designed hybrid sections.
- Cap the length of each segment: puzzle sections 2–10 minutes, combat encounters 1–5 minutes, a single staged sequence 30–90 seconds (typical magnitudes); when it runs over, split it.
- Pillars borrow from each other: knock enemies into mechanisms, use mechanisms to break enemy super armor; puzzles and combat share one item language so they don't feel like two different games (§3.3).

### 3.2 Miniature-Garden Structure: Zoned Small Worlds and Pacing

The spatial unit of action-adventure is the **miniature garden**: a zone with boundaries and a theme, roughly 30–50 minutes from entrance to exit. The whole world is assembled from several miniature gardens plus a hub, rather than one continuous large map. Zoning brings three benefits: pacing you can control, cost you can control, and a complete arc per zone. Fix the structural vocabulary first:

| Structure | Definition | Design rule |
| --- | --- | --- |
| Hub | The transit space connecting the zones (a village, a camp, a travel point) | Hosts shops, saves and story progress; also the emotional anchor for "coming home" |
| Wilds | Open stretches focused on exploration and encounters | Landmarks first: 1–2 distant landmarks per wilds area, answering "where am I" |
| Dungeon | The most puzzle-dense, most enclosed zone | Each zone teaches only one new mechanic; the exit examines it |
| Gate | A passage restriction created by an item or by the story | Visible and memorable; one visual language per lock type across the whole game; never hard-lock progress before the player has seen that lock type |

Per-zone pacing template (roughly 45 minutes; if it runs longer, split the zone; between zones, leave corridors, elevators and viewpoints as breathing stretches and loading cover, and rotate puzzles, combat and staging between adjacent zones to create a pacing difference):

| Stage | Content | Time reference |
| --- | --- | --- |
| Entry and survey | Distant landmarks, the zone objective in sight, a few encounters | 3–5 minutes |
| Teaching | A low-pressure scene that teaches this zone's new tool or new enemy | 5–10 minutes |
| Development | Puzzles and combat escalate in alternation, combined with old mechanics | 15–20 minutes |
| Climax | The most structurally complex mechanism, or a boss fight | 5–10 minutes |
| Reward and exit | A new item, a new shortcut, a teaser for the next zone | 3–5 minutes |

### 3.3 Item Reuse: One Item, Three Uses

An action-adventure item cannot be just a key. The design rule: **every item needs at least two applications in each of the three contexts — puzzles, combat and exploration** — and at least one of them must be usable within ten minutes of pickup.

| Item | Puzzle use | Combat use | Exploration use |
| --- | --- | --- | --- |
| Bombs | Blow open cracked walls and fissures | Area damage, interrupt casts | Blast out hidden passages and collectibles |
| Grappling hook | Pull distant mechanisms, swing over gaps | Pull enemies in or disarm them | Reach high ledges, cross chasms |
| Time stop | Freeze the timing of mechanisms | Slow enemies, create damage windows | Cross fast-moving platforms |
| Ranged (bow, gun) | Hit mechanisms within sight | Pick off fragile targets and pull aggro | Shoot down hanging objects and open rope routes |

The names are yours to choose; the check is that every row can fill all three use cells. Companion rules:

- Four beats for introducing an item: show (try it once in a safe environment) → use (clear an obstacle on the spot) → echo (at least two places in old scenes unlock because of it) → variation (combine it with an old item for something new). Without the "echo", an item is just a new rule.
- Maintain a use list per item (context × use × reachable stage); anything with fewer than 3 entries is not greenlit; an item that only opens one door is demoted to part of a mechanism and does not take an item slot.
- Combination check: any two mid-to-late-game items must combine into at least one new puzzle or one new way to fight; the later the game gets, the more the item set needs chemistry.

### 3.4 Staging and Camera: The Cost of Cinematic Presentation

Three camera rigs, duties kept separate:

| Camera mode | Duty | Key points |
| --- | --- | --- |
| Exploration camera | Read the path, take in the view | Follow plus look-ahead, terrain avoidance; keep landmarks in frame |
| Combat camera | See enemies and yourself clearly, control the space | Lock-on, pull-back, controlled hit-stop; never block gameplay signals |
| Staging camera | Tell the story, deliver emotion | Separate rail animation; skippable, rewatchable |

Cinematic storytelling costs are counted by the minute (typical magnitudes; voice acting and motion capture excluded): a 30–60 second in-engine scripted sequence — design, animation, camera, audio and integration — runs about 5–15 person-days; facial expression and lip sync push it higher; fine motion capture or pre-rendered footage costs another order of magnitude per second. In commercial action-adventure, "few but polished" is the norm: full staging at key beats, with environmental storytelling and dialogue bridging the gaps in between; single cutscenes stay around one minute, playable stretches separate consecutive ones, and skippable is standard. The cost-reduction checklist:

- Turn staging into gameplay: hide the camera direction inside playable stretches (the one-take approach) rather than cutting back and forth; the price is that levels and tooling have to serve the camera.
- Walk-and-talk dialogue and environmental storytelling: put conversations into walking, elevator-riding and boat-riding stretches; let the scenes themselves deliver the backstory at zero animation cost (methods in the Level Design Handbook).
- A staging budget sheet: every mandatory staged sequence gets its duration, purpose and skippability spelled out; cut outright any cutscene not tied to gameplay or emotion.

### 3.5 Guidance and Readability

Action-adventure often markets itself on "almost no quest markers", but that is designed, not absent: guidance goes into the space first (one consistent symbol language for interactables, landmarks in frame, light shafts and color pulling the eye, difficulty tiers that only test what was just taught), with UI markers as the fallback; every puzzle gets two tiers of hints (a companion's whisper, the target object glowing), with trigger conditions written into the design sheet.

Checklist: find 5 playtesters and record their first lost point, how long until their first stuck point, and how often they voluntarily walk back; for every point where players stall for over 10 minutes, add guidance one by one.

## 4. Technical Essentials

The technical difficulty concentrates in four places: the camera, the interaction system, the staging pipeline and world-state consistency. Everything below is engine-agnostic; assembling these systems from an engine's stock modules can reach a passing grade — what you actually have to build yourself is the state-management layer between them.

| System | Key point | Common practice |
| --- | --- | --- |
| Camera | Three modes switching without breaking | A unified manager: modes, priorities, transition curves; obstacle-avoidance rays; separate rails for the staging camera |
| Interaction system | One item, many kinds of interactable | A unified "interactable registry": type, required item, feedback; hint UI renders from the registry, with at most three on-screen prompts |
| Puzzle objects | Mechanisms are state machines | Triggers plus state flags, resettable and force-completable; every mechanism gets a debug panel |
| Staging pipeline | Camera, animation, dialogue and audio in sync | The engine's timeline tooling; whole sequences seekable and skippable; staging state decoupled from game state |
| Saves | World state and character state kept separate | Doors, mechanisms and collectibles use flags; checkpoint autosave; rolling back does not undo a world already opened, and version upgrades do not kill saves |
| Debug tools | Teleport, noclip, invincibility, all items | Build them on day one; without them, one full test pass across all zones takes a day |

Key details:

- The camera is technical debt number one: the three cameras must have a unified manager, or every handoff — "staging triggered during combat", "return to combat when staging ends" — becomes a bug.
- Buffer the seams between staging and playable stretches: leave transitions before and after taking and returning control to prevent swallowed input; define the input policy during staging explicitly (the common choice: skip only).
- Puzzle state machines must be resettable: when the player leaves, gets stuck or does steps out of order, a one-button reset restores the mechanism, preventing softlocks; during testing, sweep the whole map with debug tools.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimation and for cutting requirements; not a commitment.

| Tier | Scale | Time reference | Notes |
| --- | --- | --- | --- |
| Prototype | 1 miniature garden, 2 items, 1 boss | 2–4 weeks (solo) | All greybox; validates the three-pillar loop |
| Small title | 4–6 zones, 6–10 hours of play | 6–12 months (small team) | One toolset, low staging content |
| Typical commercial scope | 8–12 zones, 15–25 hours of play | 2–4 years (dozens of people) | Cinematic staging, outsourcing and voice pipelines |
| Large commercial scope | 12+ zones, 25+ hours of play | 4–6 years (100+ people) | Staging, mocap and voice pushed to the limit |

Per-zone breakdown reference: for one 45-minute miniature-garden zone — layout and circulation 3–7 person-days, puzzle design 5–10, combat encounters 3–7, art and environmental storytelling 10–20, testing and polish 5–10 — the total is on the order of tens of person-days; staging gets its own budget: multiply the game's total staging minutes by the person-days-per-minute rate from §3.4 and list it as a separate line — 60–90 minutes of full staging across a 20-hour game is already typical commercial scope.

Content-cutting order (when behind schedule): cut collectibles and optional puzzles first; then merge small zones (remove gates, convert to linear stretches); then downgrade staging (full staging becomes walk-and-talk dialogue). Bosses and the main-line structure are the floor. The master anchor for extrapolation is "zones × per-zone cost" — do not back-calculate from total playtime.

Milestone suggestion: three-pillar prototype (one miniature garden played through, each pillar with a representative stretch) → vertical slice (one zone at final quality, including a staged sequence and a boss fight) → main line complete (greybox fully connected, no softlocks) → content fill (art, staging, voice, collectibles in place) → polish and submission. Every step's pass condition is a playable artifact, not a completion percentage.

## 6. How to Start the First Prototype

Goal: validate the minimal three-pillar loop — "explore → puzzle → fight → get item → use item" — in a single miniature-garden zone, all placeholder art, without touching story or menus.

Mini spec (copy as is): 1 hub, 1 wilds area (~10 minutes), 1 dungeon (3–5 rooms), 2 items (bombs plus a grappling hook recommended), 3 standard fights, 1 boss, 1 staged sequence of 15–30 seconds.

```text
[hub] → [wilds: exploration + combat] → [dungeon: puzzles] → [item 2] → [boss] → [staging outro]
item 1 (bombs): picked up in the wilds, blows open the dungeon entrance
item 2 (grappling hook): picked up mid-dungeon, immediately usable in the boss fight
```

Steps (run in order; every step ends in something playable):

1. Movement and camera first: the minimal set of run, jump and climb, with an exploration camera that keeps up; greybox one wilds area and confirm that "just walking around is worth doing".
2. Add combat: one melee type, one or two enemy types; try both lock-on and free-camera strategies, then freeze the combat camera.
3. Add puzzles: design mechanisms backwards from the items; start with two bomb applications, one obvious and one hidden.
4. String the zone together: connect it along "entry, teaching, development, climax, reward", hardcode checkpoints and autosave; add a staged sequence along the way to validate the toolchain and the "skippable" flow.
5. Get testers: 3 people who have never played it, no hints; record the first stall, the first time they get lost, and the moment they "want to use that item again".

Four-week cadence for reference:

| Week | Output | Verification |
| --- | --- | --- |
| Week 1 | Movement and camera, greybox wilds | Walking and the camera don't feel awkward |
| Week 2 | Combat encounters and a mini-boss | Fighting is worth repeating |
| Week 3 | Two items and their mechanisms | Items have a use within ten minutes of pickup |
| Week 4 | Zone connected, one staged sequence, 3-person playtest | The three-pillar loop holds; decide whether to expand or cut |

Acceptance criteria (all observable): testers can retell the flow as "where you went, what you picked up, what you did with it"; at least one person voluntarily backtracks to find a missed mechanism use; every switch between combat and puzzles has no blank wait longer than 5 seconds; with art and audio removed, the flow still plays through and someone is willing to run it again.

If any one of the three pillars doesn't hold up (testers skip through puzzles, or don't want a second fight), fix the pillar before laying down more content.

## 7. Common Pitfalls

1. **The three-pillar ratio out of balance**: puzzles eat most of the playtime and combat-minded players quit midway. Set the ratio first with a 30-minute experience allocation table, then lay out content.
2. **Items are one-use keys**: an item opens one door and is never used again. Greenlight standard: two uses in each of the three categories, including a place in combat.
3. **No pacing difference between miniature gardens**: three zones in a row of "fight, open door, fight". Zones need thematic differences (rotate puzzle zones, combat zones and staging zones) and transitions that give breathing room.
4. **Too much staging, none of it skippable**: cutscenes start at 2 minutes, and three play back to back. Give staging a budget sheet; skippable is the floor.
5. **Puzzles and action stepping on each other**: trash mobs spawn during puzzles, mechanisms hard-control you during combat. One dominant pillar per scene; mix only in deliberately designed hybrid sections.
6. **Cameras each doing their own thing**: the view jumps, clips through walls or loses its target when combat hands off to staging. Build the unified camera manager from day one (§4).
7. **Guidance that is all quest markers**: no landmarks or visual language in the space, so arrows replace the pleasure of exploration. Build guidance into the space first (§3.5); keep UI as a fallback.
8. **Collectibles turn into checklist cleanup**: collectibles untethered from story, gameplay or the map are a liability. Every collectible must answer "what is this good for?"
9. **Softlocks**: mechanisms done out of order, an item stuck somewhere unreachable, and the player is trapped by their save. Make mechanisms resettable; sweep the whole map with debug tools during testing.
10. **Scope out of control**: planned as a 20-hour main story, then half-way through, zones get cut until the main line breaks. Build a "narrow full pass" first (one main line from start to finish), then add zones and side content laterally.

## Further Reading

- Game Design Handbook: the base document for core loops, experience pillars and gameplay spec sheets.
- Level Design Handbook: metrics, guidance, pacing and the whitebox workflow — the full expansion of this page's §3.
- Programming Handbook: implementation essentials for camera, interaction and staging systems.
- Case Studies: how to break down benchmark and failed projects — a reference when dissecting miniature gardens and staging.
- Indie Survival: scope control and scheduling; when the budget falls short, follow the content-cutting order in §5.
- Pitfalls & Anti-patterns: the high-frequency pitfalls across the whole pipeline, from kickoff to launch.

Next step: greybox one 45-minute miniature-garden zone, run one full round of "explore, puzzle, fight, item", then come back and fill in the design against this page's ratios and item-reuse checklists.
