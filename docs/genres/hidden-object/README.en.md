# Ludo Atlas · Genre Handbooks · Hidden Object

> **Genre Handbooks · Volume 4**. Positioning: an observation-based casual game that makes "finding the target in a dense picture" the first pleasure. Players do the main content with their eyes: scan, recognize, click; every hand-drawn scene is an exam paper, and this page covers hidden-object dynamics, scene-art costs, narrative integration, the variant family and the mobile monetization structure.
> Companions: Game Design Handbook (core loops and feedback design) · Art & Audio Handbook (scene production and outsourcing management) · Live-Ops & Growth (energy, ads and long-term content cadence) · Pitfalls & Anti-patterns (high-frequency pitfalls in casual genres).
> This page carries no external links; benchmarks are widely known works only, and the figures are common magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

Hidden object (with spot-the-difference and interactive hidden-object as its two close relatives) is a pillar genre of casual games. Its ancestor is the seek-and-find game in picture books and magazines (the Where's Wally branch); in the PC era, Big Fish's Mystery Case Files series (from 2005) carried the industry, and the mobile era brought it to a much larger audience with Zhao Ni Mei (Zhao Ni Mei, 2012) and June's Journey (2017). If you can see, you can play — there is almost no prerequisite barrier.

One-line positioning: hidden object is the genre that **makes "seeing it for yourself" the first pleasure**. The targets are laid out right there in the picture; the answer is not in logic but in eyes and attention; and the design work revolves around one thing: making "discovery" frequent, loud and cheap.

Three scales of core loop:

| Scale | Loop | What the player gets |
| --- | --- | --- |
| A single click (1–3 seconds) | scan → recognize → click → hit or miss | One confirmation: it is, or it isn't |
| One scene (2–15 minutes) | read the list → scan in zones → find them one by one → completion settlement | The satisfaction of emptying the list |
| One main line (days to weeks) | advance chapters → unlock new scenes → collect and decorate → the next chapter | A sense of progress and long-term goals |

The loop holds on three preconditions: the picture must hold up to "looking", because the scene is the entire content — density, theme and detail decide whether players are willing to stare for two more seconds (§3.2); the moment of finding must pay off, because hit feedback is the genre's only currency of satisfaction (§3.1, §4); getting stuck needs an exit — hints are the safety net, and without them the targets kept for the finale become churn points (§3.1).

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Logic puzzle | Puzzle progress comes from deducing rules; hidden object gives every answer up front, so progress comes only from visual recognition — it tests attention, not reasoning |
| Point-and-click | Point-and-click has players decide which item to use and where; hidden object only asks you to find everything on the list; the two merge in HOPA (hidden-object puzzle adventure) |
| Spot-the-difference | The other half of the same family: one finds targets against a list, the other finds differences between two images; they share feedback design and the production pipeline (§3.4) |
| Idle and collection | When items are collected automatically and the player only confirms and upgrades, the pleasure has already shifted from "discovery" to "accumulation" — that is idle-game content packaging, not hidden object |

Self-check question: highlight every target and take the list away — what is left of the game? If nothing, you are making a hidden-object game; if it still plays, your core is really some other mechanic — greenlight it against the matching genre handbook instead.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (ranked by priority):

1. **The moment of discovery**: the instant a target "pops" out of the background is the genre's one core thrill; a hit must be instant, loud and stackable.
2. **Low barrier, no pressure**: playable without reading any rules and stoppable at any moment; the main line has no failure, and timers and hints are optional pressure valves — those in a hurry have scores to chase, and those taking it slow are never rushed.
3. **A picture worth gazing at**: even when you cannot find something it is not boring — density, theme and small clickable interactions make "looking" itself interesting.
4. **A reason to look at the next one**: a story mystery, a map unlock or a collection list gives "one more scene" its pull.

Benchmark titles (play them yourself before breaking them down — each product solves "cannot find it" in a completely different way):

| Title | What to learn from it |
| --- | --- |
| Where's Wally? (picture books) | The genre's intuitive prototype: find a specific character in dense hand-drawn scenes; "who to find" is more memorable than "what to find" |
| Hidden Folks | Black-and-white hand drawing plus full-scene interaction; no time limit and no score — proof that "finding" can stand on its own |
| Dajia Lai Zhaocha (Spot the Difference) | The mass-market memory of spot-the-difference: two images compared, timed for speed |
| Zhao Ni Mei | The 2012 Chinese hit: goofy lists, timed levels and items combined — proof of light hidden-object's viral power |
| Mystery Case Files series (Big Fish) | One of the genre's defining HOPA series: one case per episode, advancing a cold case through hidden-object scenes, serialized for more than twenty years |
| June's Journey | The long-term mobile structure: hidden object, story, decoration management and team competitions; long a top revenue performer in the genre |

Common ground: the core verb is only one — "find"; scene art is the competitive advantage itself; polishing feedback outranks designing difficulty; long-term retention comes from outside the picture (story, collection, competition). Get all four right and the game will not be bad.

## 3. Design Essentials

### 3.1 Hidden-Object Mechanics and Dynamics

A scene has only five knobs that can move: distinctness, time limit, hints, streak and feedback. Make every one a tunable parameter in the numbers table (method in the Game Design Handbook) — do not scatter them through the code.

| Knob | What it does | Design stance |
| --- | --- | --- |
| Distinctness | Decides the difficulty of a single search | Hidden plausibly: occluded, disguised, close in hue; difficulty comes from occlusion relationships, not resolution (§7) |
| Time limit | Creates tension and replay motivation | The main line defaults to generous (leave ample headroom over the average test time); put timed play in a separate mode or challenge levels; when it expires, degrade to a hint instead of wiping progress |
| Hints | The exit when stuck | Three tiers: hot-and-cold detection (sound and cursor change as you get close) → zone highlight → direct highlight; the main line always keeps a free path — payment and ads buy speed (§3.5) |
| Streak | Rewards "finding fast" | Consecutive hits stack the score, a misclick breaks it; reward only, never punish |
| Feedback | Cashes out the moment of discovery | Hit: animation, sound, checklist tick; miss: light feedback (a shake, a low tone) — no popups, no fines |

Additional stance:

- Pick a side on pacing first: the spot-the-difference branch is arcade pacing, timed for speed (one image per round, replaying to beat scores); HOPA is relaxed pacing, a few minutes per scene (untimed or generously timed). One set of base mechanics, two tuning philosophies.
- Target count and difficulty distribution: a single scene commonly holds 8–15 items — below 8 the round ends too fast, above 15 "finding" degrades into "itemizing" (§7); in distribution, most targets are giveaways that build rhythm, a few demand close reading, and one or two are the finale — with all hard targets, players quit midway.
- Lists and misclicks: run the list on two tracks, text plus icons — icons let young and non-native players start without translation, with an art style matching the scene; a misclick must be cheap, because it is information (not here), not an error — at most it breaks the streak, and penalties never stack.

### 3.2 Scene-Art Costs

Dense hand-drawn scenes are this genre's one unavoidable large asset: code, UI and audio can all be cheap, but the scene players stare at cannot. The cost structure of one release-grade scene:

- Background plate: composition, theme and lighting right in one pass. It is the image players linger on longest, and it passes acceptance when the composition stays readable scaled down to the target device.
- Target items: each must be its own layer or sprite so it can move and be clicked individually — so they must be drawn as separate pieces from the start; splitting them apart afterwards often costs more than a repaint.
- Occlusion and interaction layers: curtains you can lift, cabinet doors you can open, grass you can part. Interactive details upgrade a static picture into a scene worth exploring, and each one is joint art-plus-scripting work; hit effects, click points and hint data are counted per item in configuration cost.

Reference magnitudes: a single scene commonly takes one illustrator one to two weeks from sketch to implementation; a seasoned illustrator's steady output is about two to four scenes a month, and the more realistic the style and the denser the detail, the higher that ceiling goes; for the production pipeline and outsourcing management see the Art & Audio Handbook. Save money along the grain of the genre: scenes are the main course, so cut chapter count and staging specs first — cutting scenes is cutting the content itself.

Reuse has four disciplines:

- Variants before new art: day and night, seasons, holidays, before and after renovation — a modified version of the same composition costs far less than a new painting; but variants must be slotted into the rhythm, since consecutive repeats of one image burn freshness.
- Spot-the-difference is inherently one artwork, two versions: the original and the altered image share the composition, so a single scene's cost is split across two modes.
- A cross-scene object library needs aesthetic discipline: the same key appearing everywhere breaks credibility, and reusing local elements beats reusing whole images.
- Give outsourcing an acceptance checklist: check composition at thumbnail size, check target selection at full size, and run click tests on the target device; style consistency comes from reference packs and the acceptance process, not from the vendor's self-discipline.

### 3.3 Integration with Narrative

Hidden object and story have a natural interface: the items you find can be the clues. The standard HOPA progression structure:

`chapter opening (dialogue or cutscene) → 2 to 4 hidden-object scenes → key items unlock a light puzzle or a new location → chapter wrap-up and a suspense hook`

- Items split into two kinds: story items (once found they enter the inventory, can be used in puzzles, and tie scenes together) and atmospheric objects (found purely for the sake of finding). The share of story items decides the narrative quality; worst of all is a list that is a random noun table, living a separate life from the script (§7).
- Scenes are the metronome: control pacing through the number of scenes per chapter, interleave dialogue, light puzzles and map travel between scenes; hidden object supplies content density and the story supplies the motive to advance; end each chapter on a hook (a new clue, a new location, a new character) that turns "one more scene" into "I want to know what happens next".
- Story-driven products have no failure: finding slowly does not block progress, at most it costs stars and rewards; progress always moves forward — that is the floor for the casual genre.
- Schedule the two lines in sync: first draw the chapter flow chart (scene nodes and progression conditions), then break down the scene list and the script; scenes waiting on the script or the script waiting on scenes are both scheduling accidents.

### 3.4 The Variant Family

| Variant | Core test | Production difference | Common representatives |
| --- | --- | --- | --- |
| Hidden objects (list-based) | Find against a list in a single dense scene | Dense scene plus separate target layers; the cost baseline | Mystery Case Files |
| Spot-the-difference | Compare two near-identical images to find differences | One artwork, two versions; low incremental cost | Dajia Lai Zhaocha (Spot the Difference) |
| Interactive hidden object (Hidden Folks style) | Find characters and events, with no list | The whole scene is clickable; heavy interaction scripting | Hidden Folks |
| Automatic hidden object | The system scans or auto-collects; the player confirms and upgrades | Reuses existing scenes; the lightest mechanics | Common in idle and casual hybrids |

- Spot-the-difference and hidden object share the production pipeline and feedback design, and many products run both modes — getting two uses from one set of scene assets is the main lever for thinning out art cost; the same goes for hybrids: hidden object plus decorating and management (June's Journey), hidden object plus puzzle adventure (the dominant HOPA form), and spot-the-difference embedded in other genres as a minigame.
- Interactive hidden object removes the list and drops the timer, putting the difficulty into "scene interactivity": behind doors, under curtains, inside grass, there may be content. Hidden Folks carries the entire game on 32 hand-drawn scenes, 300-plus targets and 500-plus interactive details — density itself is the content.
- Automatic hidden object demotes "finding" to collection, shifting the pleasure toward collecting and growth. As an assist feature (accessibility, stress-relief mode, lighter events) it is valuable; when a whole product is greenlit on it, account it as an idle game and do not apply this page's scene budget.

### 3.5 Mobile Monetization Structure

A long-term mobile product's monetization is built from four layers, and the proportions and order vary by product; calibrate the specific numbers against your own retention and friction-point data (operations method in the Live-Ops & Growth handbook) — only the structure is given here:

- Energy system: starting a scene costs energy, energy recovers over time, and when short you wait or watch an ad to top up. It aligns how fast players consume content with how fast the team ships it; the energy parameter is the hub between business and content — set it before setting output.
- Ad placements: hint acquisition, energy top-ups, interstitials after a scene settles. One red line: never interrupt the moment of a hit or a settlement — those seconds are the most expensive attention in the genre.
- Item purchases: consumables such as hints, lenses and hot-and-cold detection, sold individually and in bundles; what payment buys is "faster", not "possible".
- Chapter and collection gates: collectibles, stars or keys unlock the next chapter, creating long-term goals; the free path must run the whole length, and payment is only an accelerant.

Premium counterpoint: the classic PC form uses "try before you buy" (Big Fish's storefront signature), and it still holds up on Steam and mobile stores; which one to pick is decided by channel, scope and content cadence.

Data discipline: friction points, churn points and conversion rates belong on a dashboard. "The player is stuck" comes in two kinds — design friction and monetization friction; when players cannot tell them apart, the bill is recorded against the experience.

## 4. Technical Essentials

Hidden object's tech stack is shallow: no physics, no AI, no networking, with the difficulty concentrated in two places — scenes as data and the precision of click interaction. A small engineering volume does not mean you can relax: if the tools are not good, content throughput locks up outright.

- **Scenes as data**: write a scene as a data file of "background image + target list (name, coordinates, shape, state, hint text) + distractor parameters"; code only interprets it — stand this up in chapter one, because it decides the throughput of every scene that follows; hints derive from it too — hot-and-cold detection drives sound and visual intensity off target distance, zone highlights drive off highlight animation and camera movement — and a hardcoded route backfires on maintenance cost once scenes multiply.
- **Hit detection and the feedback chain**: use polygon or compound-shape colliders, not per-pixel hit testing; make the hit area slightly larger than the visuals to compromise with fingers; when targets overlap, prioritize by layer order; a hit fires animation, sound, a checklist tick and the count; a miss gives light feedback, and on touchscreens add an instant visual response on press — keep total latency under 100 ms.
- **Panning and zooming**: dense scenes on phones must pan and zoom; implement zoom as a viewport transform with click coordinates inversely transformed; separate panning from clicking with a movement threshold, tuned so that "meaning to click never pans and meaning to pan never clicks".
- **Resolution adaptation and saves**: use normalized coordinates for click points; render scenes at the target device's highest resolution and step down with texture compression and atlases; include one small-screen low-end device in the acceptance set; save the found list, elapsed time and hint count per scene ID so a mid-scene exit resumes where it left off — and this data is your first-hand material for tuning difficulty and hints.
- **A scene configuration tool**: annotating targets on the image, auto-generating colliders and click points, one-click hot reload — the highest-return technical investment; without it, every scene needs a programmer and throughput collapses for certain.

## 5. Content Volume and Workload Reference

The following are common magnitudes for projects of this kind, for scoping estimates — not a commitment.

| Project form | Scene scale | Timeline scale | Notes |
| --- | --- | --- | --- |
| Mechanics prototype | 1–2 scenes (using ready-made art) | 2–4 weeks | Validates click feedback and hints only |
| Small title | 20–40 scenes | 3–8 months | A single mode, or hidden object plus spot-the-difference |
| Story-driven product (HOPA) | 6–10 chapters, 3–5 scenes each | 1–2 years | Scenes, script and puzzles in three parallel tracks |
| Long-term mobile product | 50+ scenes at launch | Topped up monthly after launch | Scene throughput bound to the update cadence |

Art magnitudes (reference): count one release-grade scene as one to two weeks of one illustrator's time (including separation and configuration); steady output is about two to four scenes a month; leave rework headroom in the schedule and plan at 80% of capacity.

Workload stance:

- Do the throughput math before setting the chapter count: scenes × person-weeks per scene ÷ team capacity is the physical lower bound on the content cycle ("ship first, patch later" does not hold in a scene genre); the reuse factor is the most effective scope lever — variant scenes, one-artwork-two-versions and cross-scene object libraries all push the per-scene average down, but keep the repetition players can perceive under control.
- The proofing pass per scene cannot be skipped (a thumbnail composition check, a full-target click test and a hint-path test, usually half a day to a day of acceptance); script and scenes must be produced on the same rhythm — if either line stalls, the other starves or stockpiles.

Scope control: this genre's number-one cause of death is output failing to keep up with consumption. Players can burn through two weeks of production in a day; cutting weak scenes before launch only makes the experience tighter, and any operational promise of "a few scenes a month" should be signed only after checking illustration capacity.

## 6. How to Start the First Prototype

Goal: spend 2–4 weeks answering one question — can a single scene make someone willing to stare for two minutes, and laugh out loud when they find something. Use ready-made assets; do not draw new art.

1. **Borrow an existing image**: find a dense, free illustration or photo (run the licensing past Legal, Patents & Competition first); hand-mark 10–15 targets and write them into a data file. The prototype's job is mechanics, not art.
2. **Minimal interaction and feedback chain**: click hits and misses, checklist ticks, completion settlement, plus hit animation, sound, a streak counter and one crude hint (clicking a list item weakly highlights it); a prototype without feedback only ever gets the word "boring" back, and cannot test the real questions.
3. **Hallway testing and a data wrap-up**: find 3 to 5 family members or friends who don't play games, have each play twice, and record without speaking: completion time, misclick count, when they ask for help out loud, when they laugh out loud, and whether they ask "is there more" at the end; then record time-to-find for every target — the slowest should be your designed finale, and if the fast-slow distribution is the opposite of your intent, tune the data before talking about art.

Success criteria (all observable):

- At least 4 of 5 testers start without instructions, and none quits because "I can't click it"; when they finish, at least one asks for the next scene unprompted.
- You can finish editing one scene's data (adding or removing targets, adjusting hint cooldown) within 10 minutes and have a tester retest; the time ratio between the slowest and fastest targets must land in the expected band — if every target is fast, distinctness is too low.

If the feedback chain and data pipeline do not pass acceptance, do not start painting production scenes: hand-drawn scenes are this genre's most expensive purchase, and a wrongly drawn scene has to be redone entirely.

## 7. Common Pitfalls

1. **Difficulty built on resolution**: targets so small they need a magnifying glass, or a hue half a shade off the background. Difficulty should come from occlusion and camouflage, and acceptance must include scaling down to the target device (§3.2).
2. **Overloaded lists**: twenty targets crammed into one image turns "finding" into "itemizing". Set the target count by experience duration, not by "getting your money's worth from one image" (§3.1).
3. **List and story cut from different cloth**: the items found have nothing to do with the story, and players are doing vocabulary drills inside a mystery. A story-driven product's list must mostly relate to the theme (§3.3).
4. **Stacked penalties and gates**: fines for misclicks, progress wiped on timeout, forced exits when energy runs out, all layered on top of energy, hint and chapter-gate paywalls — the free path becomes impassable; casual players are here to relax, so penalties become churn verbatim, and the reviews deliver the verdict before the revenue report does (§3.1, §3.5).
5. **Hints missing tiers or fully automatic**: no hints and endgame targets deadlock; hints too readily available and "discovery" loses value. Tier them, and make the player ask (§3.1).
6. **Feedback and detection both failing**: detection tightened to the pixel so a slight offset reads as a miss, and feedback so weak it is a dull thud — one is the compromise with fingers, the other the payoff to the eyes (§4).
7. **Only finding, no looking**: the scene is a pile of random objects with no theme, no easter eggs, no interaction; players leave the moment they finish and never revisit or take a screenshot (§2).
8. **Throughput unaccounted**: players burn two weeks of output in a day, the update cadence collapses, and operational promises cannot be kept (§5).
9. **Outsourcing without acceptance**: every scene painted in its own style, and together they look like a flea-market of assets; reference packs, sample sheets and an acceptance checklist are all mandatory.

## Further Reading

- Game Design Handbook: core loops, feedback design and numbers-table methods — the draft under §3.1.
- Art & Audio Handbook: the hand-drawn scene production pipeline, outsourcing management and style acceptance — the full expansion of §3.2.
- Live-Ops & Growth: the operational stance on energy, ads and long-term content cadence — the companion to §3.5 and §5.
- Pitfalls & Anti-patterns: casual-genre and content-production pitfalls, to read against §7.
- Case Studies: breakdown and retrospective methods — use alongside each other when dissecting Zhao Ni Mei and June's Journey.
- Closing advice: get one scene running through the full pipeline with borrowed art first, then come back and reread §3.2 and §5. A hidden-object project's lifeline is scene throughput, not the idea.
