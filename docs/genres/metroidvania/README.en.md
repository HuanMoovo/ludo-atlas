# Ludo Atlas · Genre Handbooks · Metroidvania

> **Genre Handbooks · Volume 1**. Positioning: a development handbook for action games driven by "ability gates plus a connected map" and nonlinear exploration, covering the practice from lock-and-key room structure to full-map connectivity, revisit reasons and scope control.
> Companions: Level Design Handbook · Game Design Handbook · Programming Handbook · Indie Survival.

---

## 1. Positioning and Core Loop

Metroidvania's skeleton is made of three things: platforming, nonlinear exploration and ability gates. The player explores one large, continuously interconnected map, notes the places they cannot get past, comes back to pass them after finding a new ability, and repeats until the endgame. Compared with a platformer, it is one map rather than a string of levels; compared with an open world, it segments progress with ability gates rather than letting the player push straight through.

Core loop (minute scale): `explore a new area → hit a wall (ability missing / gate locked) → gain the key or ability → unlock and enter a new area → revisit old areas and find new routes → explore deeper`; nested loop (hour scale): `ability growth → rereading the map → world expansion → the next ability growth`, until the whole map converges on the endgame.

The test: remove every ability gate — does the game still hold up? If nothing changes, what you built is not a Metroidvania, just a platformer; if the whole structure collapses, the gates are real. The other counterexample is a broken revisit chain: the player gains a new ability but cannot remember where to go — §3.1 deals with this specifically.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

- **Looking back is growth**: the same space is relit by a new ability, and the player gains the felt sense that "the me of now can go further".
- **Building the map in your head**: spatial knowledge is itself the progress bar; the player can say "where I am and what I still lack" without looking at the map.
- **Solitude and discovery**: no arrows and no quest list — the route is found by the player; the system keeps only one promise: "coming back will always have something".

Structural signatures of the benchmark titles (for breakdown; no sales figures or years):

| Title | Structural signature (transferable practice) |
| --- | --- |
| Super Metroid | The original paradigm of "ability is the right of passage": one map unlocks in layers as abilities arrive, and locks are visible before their keys |
| Metroid Dread | A transit network connects the areas; chase sequences act as pressure pumps that push the player out of their comfort zone |
| Hollow Knight | The map must be drawn by hand, and the unease of exploration is made into a system; benches and currency give death a cost without driving players away |
| Ori and the Blind Forest / Ori and the Will of the Wisps | Movement is game feel, and upgrading abilities upgrades the thrill; chase battles are ability exams |

Common ground distilled from these titles (this is the genre's skeleton, not its style):

1. One continuous map: rooms are nodes, doors and corridors are edges; the map's boundary is the level boundary.
2. One and the same ability both solves combat and acts as a key; the player learns its use once and it pays off in two places.
3. Gates appear before their keys: the player has already seen the lock, touched it and remembered it before holding the key.
4. Revisiting is not busywork: every return trip brings a new way of reading the map and a new shortcut because of the new ability.

## 3. Design Essentials

### 3.1 Ability Gates: The Lock–Key–Revisit Triad

Everything in Metroidvania design starts from the triad: **lock** (the obstacle blocking the way), **key** (the ability or item that opens it) and **revisit** (the player remembering an old route and turning back).

| Element | Definition | Design rule |
| --- | --- | --- |
| Lock | A door, gap or obstacle you cannot pass | Must be visible and memorable: one lock type uses one visual language across the whole map — color may change, shape may not |
| Key | A new ability, item or boss drop | The moment it is obtained it must supply a reason to "go use it"; it opens more than one door |
| Revisit | The player voluntarily returning to old areas | Every key gets 2–3 revisit points: 1 on the main line plus 1–2 optional rewards |

"Every new ability must come with a revisit reason" is a hard rule. The method: keep an unlock list for every ability, spelling out the doors it opens, the platforms it reaches and the rewards it secures; an ability with fewer than 2 entries does not get greenlit.

| Ability | Combat use | Exploration use | Revisit point examples |
| --- | --- | --- | --- |
| Double jump | Dodge low sweeps | Jump onto high ledges | Every "just short" ledge in the early areas |
| Dash | Invincibility frames through bullet patterns | Pass through narrow gaps, cross long chasms | The floor cracks in the starting area |
| Grappling hook | Pull enemies in close | Hook onto anchors and swing | The suspended anchors in the atrium |
| Bombs | Area damage | Destroy cracked walls | The suspicious walls in the early areas |

Locks come in four forms: ability locks (the main-line skeleton, the most numerous), item locks (boss drops, strong sense of ritual), count locks (collect N fragments to open a door — positive feedback for side content) and story locks (narrative beats; use sparingly). The revisit toolkit has three pieces: map markers (unopened doors leave an icon on the map), memory anchors (place a distinctive landmark beside the lock) and hints (NPC dialogue or item descriptions give direction). If testers need to take notes outside the game, the locks' visibility has failed.

### 3.2 Map Connectivity: Hubs, Shortcuts, One-Way Doors and Back Doors

A map is not a collection of rooms; it is a structured graph. Fix five structural terms first:

| Structure | Definition | Suggested count | Role |
| --- | --- | --- | --- |
| Hub | A transit space connecting 3 or more areas | 2–3 across the map | The anchor for orientation: standing in a hub, the player can say "where I am and what I still lack" |
| Shortcut | An unlockable passage that shortens the trip on revisits | 1–2 per area | A reward for retrying players; keeps traversal from becoming torture |
| One-way door | A door that allows passage in one direction only | Use sparingly | Creates a "pushed along" flow; overuse earns the player's resentment |
| Back door | An unofficial entrance into an area | Be generous | Gives explorer-type players a taste of reward, and supplies material for speedrun routes |
| Loop | A circular route inside an area that leads back to its start | At least 1 per area | "It loops back around" is a cheap and reliable spatial surprise |

Connectivity check (run over the whole map):

- Is any room reachable from any other? (A connected graph has no isolated nodes)
- From the nearest save point back to any target, is the trip within 20–30 seconds?
- A dead end must either hide a reward or mark the site of a future gate; it can never be just a dead end.

Tolerance for back doors and sequence breaks comes in three tiers, each defined explicitly:

| Tier | Approach | Use | Cost |
| --- | --- | --- | --- |
| Sealed | Hard checks at key junctures | Story doors on the main line | Requires full regression testing |
| Tolerated | Skipping allowed, no reward | Alternative routes around most ability gates | The default tier; lowest cost |
| Rewarded | Routes designed specifically for speedruns | Hidden shortcuts, easter-egg rooms | Needs extra validation; becomes a community talking point |

Ruling: **a skip that breaks the flow is a gift; a skip that softlocks a save is a bug**. Maintain a "skippable list": for every key, record whether it can be bypassed, whether you can get out afterward, and whether you can come back. Guard especially against one accident: the player slips into a new area through a back door, takes a key item, and is then locked by a one-way door into a state they cannot leave. Test method: give testers the task "reach a certain place by the straightest route possible", log which gates they bypassed, and use that to decide where to patch walls and where to promote a route into an easter egg.

### 3.3 Ability and Level Coupling: New Abilities Rewrite the Old Map

An ability's introduction uses a four-beat rhythm: show (try it once in a safe environment) → use (clear an obstacle with it on the spot) → echo (2–3 places on the old map become reachable) → variation (combine it with an old ability for something new). All four beats are required; without the "echo", an ability is just a new rule.

A new ability, at heart, changes the way the player reads the map: after the double jump, every high ledge across the map becomes a "candidate target"; after the dash, narrow gaps that once looked dangerous become shortcuts; with a detection-type ability in hand, hidden rooms start getting actively "swept" out.

Ability checklist (tick every line for every ability):

- Does it have both a combat use and an exploration use?
- Within 10 minutes of acquisition, are there at least 2 places to spend it?
- Is there a reward on the old map (at least 1) that only it can reach?
- Is there a "combination gate" that only opens with it plus an old ability? Does it make some old room boring (skipping every challenge along the way)?

Counterexample warning: an ability that only opens doors, cannot fight and cannot save time is at heart a key in a glove. The player will not feel stronger — only that they are carrying more keys.

### 3.4 Scope Control: The Metroidvania Scope Trap

This genre's cost structure multiplies rather than adds: **total cost ≈ room count × per-room cost + ability count × full-map review rounds + connectivity testing cost**.

Three traps queue up in the order they appear: the map-area trap — planning as if "making a big world", discovering halfway through that per-room hours far exceed expectations, and after large-scale cuts the map no longer connects into a whole; the ability-count trap — every added ability adds a full-map review round (which rooms can now be broken into early, which locks stop working); the revisit-route trap — the rooms are all there, but revisits have no shortcut support, and by the third trip down the same long path the player starts to resent it.

The corresponding structural decisions:

- Few deep areas beat many shallow ones: 4 areas of 30 rooms each beat 8 areas of 15 rooms each, and save on connective structure and testing costs.
- Fewer abilities, not more: fix 5–8 first and give each a revisit list; 6 full abilities beat 12 filler ones.
- One core concept per area: one themed mechanic plus one ability payoff, so entering a new area means learning one thing.
- Content-cutting order when behind schedule: cut optional rooms and collectibles first, then merge areas (remove connections, convert to linear stretches); ability count is the fallback lever, because touching it ripples across the whole map.

### 3.5 The Whitebox Workflow and Readability Design

The Metroidvania whitebox order differs from ordinary levels: draw the graph first, then the rooms.

1. Connectivity graph: on paper or in a tool, fix the nodes (rooms) and edges (doors, corridors), marking every key and the locks it opens; if this step does not pass, do not build a single room.
2. Full-map greybox: build every room out of primitives only; the standard is "a complete route can be walked at every ability stage", and looks are not the goal.
3. Ability delivery test: pretend to acquire each ability in order, walk the whole map, and verify that every revisit holds up and nothing can be broken into early.
4. Guidance and landmarks: put 1–2 distant landmarks in each area, define the color zoning, and check whether the neighboring area can be recognized from any room.
5. Single-room refinement and the art pass: sculpt the platforming challenge and staging inside rooms; after art comes in, the guidance test must be rerun.

Tooling advice: for 2D projects use a level editor that supports room and entity annotation, such as Tiled or LDtk, or a custom in-engine room tool; whichever you choose, it must ship with debug features (all-abilities toggle, teleport to any room, reveal the whole map, display gate states) — without them, one full-map revisit check takes half a day. Manage room data as an asset: name IDs as "area-number-purpose", and record for every room its first reachable ability stage, the gates it contains, its revisit content and its checkpoint positions, so that a "revisit check" becomes a filter query.

Four items of readability design:

- **Area landmarks**: 1–2 silhouettes visible from afar in each area, in sight as soon as you cross the area boundary, answering "where am I".
- **Color zoning**: one dominant color per area, kept consistent across the scene, the minimap's base color and UI labels, answering "which place is this".
- **Lock visual language**: one lock type keeps one design across the whole map — color may change, shape may not — answering "what am I missing".
- **Three-state minimap**: never visited (black), visited but unmapped (outline), mapped (detail and doors), answering "where have I not been yet".

Spot check: ask testers "how do you get from the nearest save point to the boss, and how many areas do you pass through". If they cannot answer, readability is in debt.

## 4. Technical Essentials

This genre's technical difficulty is not scale; it is two things: **game feel** and **world-state consistency**. Everything else is routine 2D engineering.

| System | Key points | Common practice |
| --- | --- | --- |
| Game feel | Coyote time, input buffer, jump curve | Put the parameters in tables: coyote time 80–150 ms, input buffer 100–200 ms; work in frames, and calibrate gamepad and keyboard separately |
| Platform collision | One-way platforms, corner correction, slopes | Fixed timestep plus shape detection; leave half a tile of tolerance so players are not "clearly landed but bounced off the edge" |
| Camera | Smooth follow plus room constraints | Look-ahead offset (extend 10%–20% in the direction of movement); lock the camera in boss rooms and chase sequences |
| Map system | Rooms as nodes, doors as edges | Record "rooms visited, doors passed"; the minimap renders from node data and stores no image |
| Saves | World state and character state kept separate | Opened doors, cleared paths and dead bosses do not roll back; character resources and position roll back to the save point |
| Ability system | Flags plus parameter sets | Movement and combat read parameters from "the current ability set"; gates all go through the same check function |
| Debug tools | Teleport, all abilities, reveal map | Build them from day one; they are the precondition for efficient full-map revisit testing |

Key details:

- Saves center on a **flags table**: doors, shortcuts, events and items each take one bit; both the map display and gate checks derive from flags, with no separate map graphic stored.
- Settle the death-return policy during the prototype: the common approach drops part of the currency and returns the player to the nearest save point, with the currency recoverable; in the prototype you can start with a light penalty and fix the numbers after the loop runs.

## 5. Content Volume and Workload Reference

The figures below are magnitude references that shift with team size and your bar for completion; use them for estimation and for cutting requirements — they are not commitments.

| Tier | Rooms | Areas | Abilities | Time reference | Notes |
| --- | --- | --- | --- | --- | --- |
| Prototype | 15–25 | 2–3 | 3 | 2–4 weeks (solo) | Validates the lock–key–revisit loop; no art |
| Small commercial | 60–90 | 4–5 | 5–6 | 6–12 months (solo) | Exercises the full production pipeline; content comes from combination and reuse |
| Standard scope | 120–200 | 6–8 | 7–10 | 1 year+ (small team) | The common magnitude for established projects; needs a content pipeline behind it |
| Large scope | 250+ | 8+ | 10+ | Measured in years (full team) | Both cost and revisit-testing complexity go up an order of magnitude |

Per-room breakdown reference: for an ordinary room "with combat and environmental storytelling" — whitebox and playability 0.5–1 day, enemies and encounters 0.5–1 day, art 1–3 days, polish and testing 0.5–1 day — the magnitude is 2–5 person-days.

Conversion example: 120 rooms × 3 person-days on average ≈ 360 person-days. Solo (doing all the art yourself) that is roughly 1–1.5 years; a 3-person team about 4–6 months, provided the pipeline is already running smoothly. Estimation must also add the "ability review rounds": 7 abilities means at least 7 full-map walkthroughs.

Milestone suggestion: loop prototype (the lock–key–revisit loop holds; an outsider can play through) → vertical slice (1 area at final quality, used to calibrate scheduling; see the Production Handbook) → full-map connectivity (every room walkable, no isolated rooms and no deadlocking back doors) → content fill (art, enemies and collectibles in place; guidance test passed) → polish and submission (game feel tuning, performance, localization). Every step's pass condition is a playable artifact, not a completion percentage.

## 6. How to Start the First Prototype

The goal is only one: validate the minimal loop of "explore → hit a wall → gain an ability → revisit", with placeholder art, story and audio throughout. Mini map spec (copy as is): 12–20 rooms, 2 areas, 2–3 abilities (double jump plus dash recommended, with an optional grappling hook), 1 hub, 1 shortcut, 1 one-way door, 1 tolerated back door. For the technical start, use the platform controller that ships with a mainstream 2D engine; tune one room's platforming challenge until it feels good before expanding the map — do not write physics from scratch.

```text
[starting area] -- hub -- [area 2]
    |          \-- lock 2 (dash) -- [endpoint]
    \-- lock 1 (double jump) -- [high-ledge reward]
back door: a detour from the starting area reaches area 2, skipping lock 1; tolerated, no reward
```

Steps (run in order; every step ends in something playable):

1. Tune game feel: run, jump, coyote time, input buffer. Build two empty rooms and jump back and forth until you "want to jump one more time".
2. Draw the connectivity graph: nodes are rooms, edges are doors; mark every key and the locks it opens, and check the loops and one-way passages.
3. Greybox the whole map: first guarantee a full route at every ability stage, then add enemies and platforming challenges gradually.
4. Place gates and revisits: the first lock must appear at least twice before its key is acquired; give every ability 2 use points in old areas, one of which must be an optional reward.
5. Place checkpoints: spaced 20–30 seconds of travel apart, so death retries do not turn into traversal.
6. Find testers: 3 people who have never played it, with no hints and no explanation; record where they get lost, the moment they voluntarily backtrack, and the moment they quit.

Four-week cadence for reference:

| Week | Output | Verification |
| --- | --- | --- |
| Week 1 | Game feel tuned + 2 test rooms | Jumping itself is fun to repeat |
| Week 2 | 3–5 rooms connected | Walkable without getting lost |
| Week 3 | 2 abilities and 2 locks in place | Getting the key creates the urge to backtrack |
| Week 4 | 12–20 rooms fully connected + a 3-person playtest | The loop holds; decide whether to expand or cut |

Four acceptance questions for the prototype:

1. Can testers say "where they went and where they cannot get past"? (The gates' memory anchors hold)
2. After gaining an ability, does anyone voluntarily turn back? Does anyone ask "that high ledge will be reachable later, right?" (The revisit reasons and ability-gate expectations hold)
3. When stuck, do they say "what am I still missing" or "what is this game even doing"? (The former is correct)
4. How long is one full round from exploration to revisit? Target 10–15 minutes; over that, the map is laid out too big.

## 7. Common Pitfalls

1. **A big map with no routes**: plenty of rooms but thin connectivity, and revisits all rely on long-distance traversal. Draw the connectivity graph before building; shortcuts come before content.
2. **Abilities treated as mere keys**: an ability opens one door and nothing else, so the player never feels stronger. Every ability needs at least 2 application points, usable for both combat and exploration.
3. **Invisible locks**: doors that lock before the player has seen them are forgotten even after the key arrives. Gates must appear before their keys, with one unified visual language.
4. **No revisit reason**: ten minutes after a new ability arrives, there is nothing to do. Keep a revisit list per ability; not enough entries, no greenlight.
5. **One-way doors overused**: players get punished all the way back when they want to grab a missed collectible. One-way passages serve emotional beats only, and must be visible before use.
6. **Back doors with no safety net**: skipping a key item leaves you stuck in a state you cannot return from. Keep the skippable list and verify both ends of every entry and exit.
7. **Failed visual zoning**: one material and one hue across the whole map, and getting lost becomes routine. One dominant color per area, plus distant landmarks and minimap outlines.
8. **Combat and exploration living apart**: bosses do not test your movement abilities, and abilities are only useful in new areas. Bosses and chase sequences should quiz you on the ability you just earned.
9. **Map system in debt**: no minimap or no markers, so players draw maps outside the game. Treat the map as core UI: three-state display, markable.
10. **Scope out of control**: planned as 8 ideal areas, cut halfway until the map no longer connects. Build a "narrow full map" first (a low-room-count version with the whole line connected), then widen it laterally.

## Further Reading

- Level Design Handbook: the general form of lock–key–revisit, the whitebox workflow and spatial language.
- Game Design Handbook: core loops, experience pillars and gameplay validation methods.
- Programming Handbook: implementation essentials for movement feel, collision and save systems.
- Indie Survival: scope control, solo pacing and finishing on schedule.
- Case Studies: map structure and scope lessons from public postmortems.
- Pitfalls & Anti-patterns: the high-frequency pitfalls across the whole pipeline, from kickoff to launch.

Next step: whitebox a small 20-room full map first, run one full round of lock–key–revisit, then come back and fill in the design against this page's checklists.
