# Ludo Atlas · Genre Handbooks · Point & Click Adventure

> **Genre Handbooks · Volume 2**. Positioning: a narrative adventure of "look, take, use, talk" inside handcrafted scenes; puzzles and story are each other's flesh and bone. This page covers the interlocking structure of its two legs, and the art, dialogue and localization accounts that structure dictates.
> Companions: Game Design Handbook (narrative structure and core loops) · Art & Audio Handbook (scene art and animation specs) · Level Design Handbook (guidance and spatial circulation) · Indie Survival (scope and scheduling).
> This page carries no external links; benchmark titles are widely known works only, and the figures here are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: point-and-click adventure is the genre that **cuts narrative into a chain of actionable puzzles**. The story is what makes players want to act; the puzzles are what make them act; with story alone it slides toward visual novel, with puzzles alone it slides toward escape room.

The core loop, written as a verb chain:

`observe the scene → pick up items, note clues → talk to NPCs → combine or use → solve the puzzle → the story advances → walk into a new scene`

The metronome is the scene: a scene usually carries one objective, one or two obstacles and one new clue; once it is solved, the story pays out and sets the next hook. The only state in which the loop stops turning is the player being stuck, so dead-end prevention takes priority over how clever a puzzle is (§3.3).

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Visual novel | Players make choices inside text; point-and-click adventure performs actions inside space, and the right of way forward sits with the puzzles |
| Logic puzzle | Its puzzles are abstract rules; point-and-click puzzles grow out of a world, with clues coming from items, dialogue and scenes |
| Escape room | One space, dense mechanisms, story mostly packaging; point-and-click crosses scenes, has NPCs and character arcs, and the story is the real body |
| Text adventure | Driven by typed text, with no visual scenes; point-and-click turns the same exploration into clickable pictures |

A self-check question: take the puzzles away — does the story still make people want to see it through? Take the story away — do the puzzles still make people want to solve them? Only if both answers hold is it a point-and-click adventure.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **The payoff of a click**: anything you point at gives a decent response, and the world has game feel everywhere. This is the most basic and the most expensive item, and the bulk of the writing lives here.
2. **The moment of insight**: the clues were in front of the player all along, and they connect the wires themselves — the "aha".
3. **The pull of the story**: every solved puzzle earns a stretch of story, so players shut the game down and boot it back up carrying "what happens next?".
4. **Character voice**: humor, personality and worldview grow out of the dialogue; this is the biggest difference in temperament from logic puzzles.
5. **The safety of never getting stuck for good**: no dead ends, hints available for the asking, save at any time — only then do players dare to try wild things.

Benchmark titles (a widely known list; play them through yourself before breaking them down):

| Title | What to learn from it |
| --- | --- |
| Monkey Island 1 & 2 | Humorous dialogue, puzzles and story interlocking, the design philosophy of "no dead ends, the player never dies" |
| Broken Sword 1 | Organizing mystery narrative, cross-scene clue chains, the classic approach to dialogue trees |
| Machinarium | Wordless storytelling, hand-drawn art, the in-game hint book — a textbook of tiered hints |
| Day of the Tentacle | Three protagonists solving puzzles across three parallel timelines; the mature late LucasArts interface |
| Grim Fandango | Adult subject matter and art direction, plus a recorded lesson in the 3D transition and the generational change in controls |
| Rusty Lake series | Short-form pacing, series interlinking, atmospheric storytelling and mobile-friendly scope control |
| Paper Bride | Chinese folklore subject matter, mobile short-form episodes, and the release model of a serialized series |

Players come to this kind of work expecting "a story you can act in": it can be slow, it can be interrupted, it can be saved at any time — but they must never be told halfway through to start over because of an earlier mistake.

## 3. Design Essentials

### 3.1 The Two Legs: Narrative and Puzzles Interlocking

Fix the structure before writing content. Three common structural shapes:

| Structure | How it works | Strength | Risk |
| --- | --- | --- | --- |
| Linear chain | Clearing the previous scene's puzzle is the only way into the next scene | Narrative pacing stays controllable, production order is clear | One stuck point stalls the whole machine |
| Hub-and-spoke | One main base plus several branch locations you can travel between freely | Players feel agency, and can switch lines when stuck at one | State combinations multiply; dialogue must tolerate out-of-order visits |
| Parallel objectives | Several objectives open at once inside the same act | Shows scope in the mid-to-late game and is naturally anti-deadlock | Objectives affect each other; convergence points must be designed cleanly |

Before building anything, draw a puzzle dependency graph: the nodes are the information and items the player acquires, the edges are who unlocks whom. It has three uses: finding orphan nodes that will never be used; checking that every node has at least one prerequisite clue; and serving as the navigation chart for testing and the hint system.

Register five things for every puzzle before implementing it in the engine: motive (why the player wants to solve it), obstacle (what it blocks), clue (where it can be discovered), solution (which established connections it uses), payoff (what it unlocks). If the registration sheet cannot be filled out, do not build the puzzle yet.

A puzzle's motive is part of the narrative: the same act of opening a door reads completely differently in an "escape" situation versus a "keep the appointment" situation, and the player's investment changes with it — answer "why open this door" before "how to open it". The reward for solving a puzzle is the story moving forward one stretch, not a harder puzzle thrown in your face; after a big puzzle, schedule an emotional payoff so the tension has its rises and falls.

Checklist:

- Can every puzzle's motive be stated in one sentence, and is it tied to the main line?
- How many nodes on the dependency graph have no prerequisite clue? The answer should be zero.
- At the end of every scene, does the player hold at least two routes of "something to try next"?
- Do stuck stretches and comfortable stretches alternate?

### 3.2 Items, Environment and NPCs: The Interaction Triangle

The player's entire toolkit is three things: what is in the inventory, the objects in the scene, and people. Every puzzle is one line drawn across this triangle, and the verbs used to draw it are the whole language the player has to learn.

Start with the interaction model; it decides game feel for the player and writing cost for you:

| Model | How it works | Cost | Fit |
| --- | --- | --- | --- |
| Verb bar | Every object gets a row of verbs (look, take, use, push, talk, etc.) executed in combination | Every invalid combination needs written feedback; the writing doubles with each verb | Comedy density first, classic style |
| Context cursor | A single click performs the most reasonable action, offering no choice | Cheapest writing, fastest pacing | Mobile, lightweight narrative |
| Middle path | Two to four verbs plus cursor states, commonly "look / use / talk" | Manageable | The starting point for most new projects |

Six rules for items:

- The source must be clear: the player should be able to point at an item and say where they got it.
- The destination must be inferable: when designing an item, fix which puzzle it goes into and how it leaves the stage.
- Consumed means gone: a used-up item leaves the inventory automatically; permanent tools like journals and maps live elsewhere and stay out of the puzzle chain.
- Capacity discipline: cap active items at 8–15; go beyond and players get through by brute force.
- Combining restraint: A plus B equals C is allowed, but stay within two steps and keep results predictable; the fun of combining comes from reasonableness, not surprise.
- Invalid interactions must respond: give feedback in three tiers — a working combination gets positive feedback, an obviously mismatched one gets a humorous line, and a near miss gets the character muttering a hint to themselves.

Dialogue is the triangle's third vertex and the puzzle interface too: NPCs hand out information, hand out items, and act as referees (confirming the player's understanding of the world). Carry it with a dialogue tree plus a topic list; topics grow with progress and can be asked again and again. Before writing dialogue, give every character a voice sheet (catchphrases, sentence length, forms of address, topics they cannot bring themselves to discuss) — with multiple writers, it is what keeps the voices from blending.

### 3.3 Guidance, Hints and Dead-End Prevention

The most common bad review for a point-and-click adventure is one sentence: "I got stuck, and then I looked up a walkthrough." Treat that sentence as the enemy; every design in this section exists to kill it.

Setup before solution:

- The iron rule of fairness: the information needed to reach the solution must appear in the world before it is needed. The lock shows itself first, the key arrives later; a mechanism must be seen working once before taking it apart occurs to the player.
- Clues must echo: planted setups fall into two classes, "opened" and "paid off"; keep a payoff table in which every setup has its moment of delivery, and during audit delete the ones without a payoff or fill one in.
- Solutions use only established connections: only causal relationships the player has seen elsewhere may be turned into an exam question; teaching a new rule and testing it immediately is the usual source of "the solution came down to guessing".

Tiered hint system:

| Tier | What it gives | Timing |
| --- | --- | --- |
| 1 | Observation hint: pull attention back to a scene or a hotspot | The player opens the hint entry themselves, or it brightens slightly after being stuck too long |
| 2 | Direction hint: state what is missing, and who or where it relates to | Unfolds further inside the hint screen |
| 3 | Solution hint: specific down to "use whom on what" | Still opened by the player themselves |

- Hints are always requested by the player and never pop up on their own; the entry sits quietly in the UI, interrupts no flow and passes no judgment. "Think harder" is a taunt; "try looking somewhere else" is help.
- The classic reference is Machinarium: it turns a step-by-step walkthrough into a hand-drawn hint book inside the game. A full walkthrough is not shameful; the real problem is when the player cannot find a fallback inside the game.

Dead-end audit (four checks):

- Can an item be permanently lost or irreversibly consumed?
- Does any scene state suffer irreversible destruction with no alternative path?
- Can an NPC leave the stage carrying necessary information?
- Does progress depend on a one-chance-only event?

Design discipline: take "irreversible" out of the system. Items either are never consumed, or are already useless at the moment of consumption; characters always wait where they stand; world state only grows, never shrinks. The genre paid this tuition in a generation of bad reviews during its golden age; there is no need to pay it again.

Stuck-point observation: have testers record three numbers — time from entering a scene to solving it, invalid clicks, and the hint tier used; when a spot holds players more than three times the test median, go back and reinforce clue placement and visual guidance first, then consider adjusting the puzzle itself. Calibrate tests around a reasonable stuck ceiling of 10–15 minutes per puzzle; past that, add setup.

### 3.4 Backgrounds and Animation: The Art Bill

Backgrounds are the hardest cost unit in this genre: one image at final quality per scene, count for count with the number of scenes. Fix the resolution and composition spec first — interactables must look clickable, and circulation must lead the eye — then produce them one by one.

- Layering and reuse: split backgrounds into far, middle and near layers to support parallax, opening-and-closing and local animation; keep reuse variants like day and night restrained — each extra version costs one whole extra image.
- Character animation: keep a minimal action list per character (idle, walk, talk, use, plus one or two special actions); hold frame counts by the "good enough" principle — the classic era's 8–12 frame walk cycle is still usable because it is cheap.
- Scene micro-animation: doors must open, bells must ring, passers-by must shift posture; these small motions carry the promise that "the world is alive" and are the best hotspot hints; budget one to five groups per scene.
- Budget order: start painting the first production background only after the whitebox has run the scene count and the puzzle chain through end to end; every image finished before gameplay validation may turn into sunk cost.

## 4. Technical Essentials

The engineering difficulty concentrates in four blocks: the interaction scripting system, dialogue and state, saves and the toolchain, and localization. All four are general requirements that mainstream engines can deliver; use off-the-shelf tools for your first game — do not build an engine.

**Interaction scripting system**

- Scenes as data: backgrounds, hotspots, conditions, actions and feedback all go into data files, and the engine interprets them. The SCUMM family of the golden age already fixed this "engine separated from content" architecture; changing one line of data tunes a puzzle, and that is the floor for iteration speed.
- Make hotspots a fixed structural template: visibility and clickability conditions, actions (pick up, open, move), feedback (success text, invalid text). Only with a stable template can content production be batched.
- World-state table: register every flag, counter and scene switch in one place; scripts may reference only registered state; scattered condition checks are this genre's most typical technical debt.
- Debug commands before content: jump scenes, grant items, set flags, fast-forward dialogue, hot-reload scripts; without them, every test means a full playthrough.

**Dialogue and state system**

- Dialogue data takes one of two forms, a node graph or a topic list, with nodes carrying conditions and effects (change flags, grant items, open scenes); writing stays separate from logic, so writers change text without touching structure.
- Skip-read, auto-play, dialogue history and text speed are baseline features; skip rate and re-read rate double as health-check data for the writing.
- Voice acting is an option, not the foundation: full voice in multiple languages is expensive, so leave hooks in the data layer first and decide whether to do it at the scope meeting.
- Localization starts on day one: every player-visible string goes through the string table; decide in advance how to handle text inside scene art (signs, newspapers, gravestones) — redrawing and texture replacement both go into the asset spec, and retrofitting later is the most expensive option.

**Saves and toolchain**

- A save equals "flag set + inventory + scene and position + dialogue-read table", decoupled from story content; after every content update, test with an old save, and run it once more before release.
- Autosave covers entering scenes, solving puzzles and key conversations; players should never have to replay a stretch just to save.
- Stuck-point telemetry with a local log is enough: scene dwell time, invalid clicks, hint tier; start recording during the prototype — tuning difficulty and hints depends on it.
- Smoke script: use a script to walk one main line automatically (jump scenes, simulate interaction sequences) and run it after every change to conditions or flags, to prevent one broken spot from stalling the whole line.

**Platform and input**

- The mouse is the smoothest input: hovering previews the action, double-clicking runs; touchscreens must rebuild this interaction — hover becomes tap-to-preview, running becomes press-and-hold or short-range auto-pathing.
- Design touch hotspots for fingers, starting from a rule of thumb of 9 mm square; in dense scenes, split hotspots apart or offer a magnifier and a highlight mode.
- Resolution fitting: draw backgrounds at full target resolution — scaling down to a small screen loses detail; test UI font sizes on the smallest target screen; point-and-click interfaces are element-heavy, and phones expose font-size and spacing problems first.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for scope estimation; not a commitment.

| Tier | Scenes | Playtime | Schedule scale | Positioning |
| --- | --- | --- | --- | --- |
| Prototype | 3–5 scenes, one puzzle chain | 15–30 minutes | 2–4 weeks | Validate the interaction model and the flow |
| Short | 10–15 scenes | 1–3 hours | 3–6 months | The mature jam form and small commercial titles |
| Mid-size complete work | 25–40 scenes | 5–8 hours | 1–2 years | The usual commercially sellable scope |
| Large | 50–80 scenes | 10+ hours | Multiple years for a team | The tier of golden-age first-rate titles |

Three conversion formulas:

- Per-scene cost = background (typically 2–5 artist-days) + hotspots and interaction scripts (1–2 days) + dialogue and feedback writing + scene animation (1–5 groups). All told, 1–3 weeks of investment per scene is typical, with art taking the largest share.
- Writing volume: a complete work's dialogue and description text commonly runs 50,000–150,000 characters, a large share of it hotspot feedback that "responds to everything" rather than main-line dialogue; estimate writing speed at 2,000–4,000 characters of first draft per day for an experienced writer.
- Puzzle volume: a 5–8 hour work typically has 15–25 core puzzle nodes, with more nodes on the dependency graph; arrange one "big puzzle" per 30–60 minutes, filling the gaps with small puzzles, dialogue and exploration.

Total art volume: background count matches scene count plus variants; character count follows the cast, with one minimal action set each; prop icons follow the item list; the most underestimated item is scene micro-animation, which stacks linearly with scene count. A 30-scene work starts at 30 final-quality background paintings alone; this part must be spelled out in the project charter.

Schedule anchors: from zero to a playable complete puzzle chain usually takes 2–4 weeks; to a vertical slice (one chapter at final quality) typically 2–4 months; extrapolate from there by scene count. Cutting content is always safer than delaying: removing a node from the puzzle chain is just deleting logic, while a background abandoned halfway is a pure loss.

## 6. How to Start the First Prototype

The first prototype builds only one puzzle chain: 3–5 scenes, one NPC, one flow carried end to end with "take, use, talk". Finish it in 2–4 weeks without touching final art, voice acting or multiple languages.

1. Days 1–2: pick tools and run a sample through. Among off-the-shelf options, Adventure Game Studio is the free, open-source veteran point-and-click engine; the Godot camp can use open-source frameworks such as Escoria; Unity projects commonly use Yarn Spinner or ink for the dialogue layer. Also fix the verb model (§3.2), starting with the middle path.
2. Days 3–4: draw the puzzle dependency graph on paper, 5–7 nodes; write out all five items for every node (motive, obstacle, clue, solution, payoff); list each scene's points of interest and hotspots clearly.
3. Days 5–7: whitebox it — color-block backgrounds with text labels, hotspots, inventory, cursor feedback. Give every invalid interaction one line of response text from the start. Ugly is correct.
4. Days 8–10: add one NPC with a dialogue tree, state flags and saves; stub in the three-tier hint entry.
5. Days 11–12: add telemetry logging (dwell time, invalid clicks, hint tier), play the main line through three times yourself, and note the spots where you get stuck — those are the disaster zone.
6. Days 13–14: test with 3–5 strangers. Say nothing, give no hints, and record stuck points, misclicks and drop-off points; at the end, ask only one question: "do you want to keep playing?"

Success criteria (all observable):

- At least 3 testers get through the whole chain without hints, averaging no more than two stuck points each and no more than 10 minutes per point.
- Every stuck point can be attributed to a concrete design problem (not enough clues, an inconspicuous hotspot, a dependency over two steps long) rather than to "how did they not figure it out".
- Spontaneous "let me go check over there" appears during testing, instead of heads-down walking of the single path.
- With all art and sound removed, the flow still holds up.

## 7. Common Pitfalls

1. **Puzzles and story living on separate planes**: puzzles designed for their own sake make players feel like they are doing the designer's chores. Fix: write the motive before the mechanism (§3.1), and have solutions refer back to things that have already happened in the story.
2. **Solutions that rest on guessing**: the puzzle depends on connections inside the designer's head, leaving players nothing but brute-force collision. Fix: setup before solution; use only established connections; have someone unfamiliar with the project verify.
3. **Dead ends and irreversible states**: an item permanently lost, an NPC gone, a one-time event missed — and the player only discovers hours later that the only option is starting over. Fix: world state only grows, never shrinks; an item must already be useless when it is consumed (§3.3).
4. **Silent clicks**: invalid interactions with no feedback leave players unable to tell "it doesn't work" from "I missed the click". Fix: every interaction gets at least one line of text or one sound effect.
5. **Runaway inventory**: thirty items in stock and combinatorial explosion switch players from reasoning to brute force. Fix: cap active items at 8–15, and let used items leave immediately.
6. **Hints at two extremes**: either none at all, or outright spoilers. Fix: three tiers, player-requested, with the entry surfacing quietly.
7. **Pixel hunting**: hotspots smaller than the visual body, or a picture where nothing looks clickable. Fix: hotspots larger than the visual, a highlight key, and one art language for interactables.
8. **Underestimated art budget**: scene counts grow linearly while per-scene cost (background, animation, interaction) stacks multiplicatively, and halfway through painting you find it cannot be finished. Fix: run the full chain in whitebox before starting to paint.
9. **Self-indulgent dialogue**: inside jokes and long speeches that players skip straight through. Fix: cap hotspot responses at one to three lines, and put skip rate into the retrospective metrics.
10. **A missing tutorial**: the first ten minutes fail to teach "look, take, use, talk", and the first puzzle is where players quit. Fix: make the first puzzle the tutorial — the actions it teaches are the actions clearing the game requires.
11. **Localization postponed**: hard-coded strings, no plan for text inside art, fonts whose licensing was never confirmed. Fix: from day one, organize text and assets as if they will be translated (§4).
12. **Copying only the classics' surface**: you take the verb bar and the hand-drawn look but not the "responds to everything" writing system, and the world instantly turns mute and thin. Fix: establish the response-writing system first, then build the UI skin.

## Further Reading

- Game Design Handbook §8: narrative design, dialogue and worldbuilding presentation — the higher-level method behind this page's §3.
- Art & Audio Handbook §2, §10: the 2D pipeline and delivery specs — the expanded ledger behind this page's §3.4 and §5.
- Level Design Handbook: guidance, circulation and the whitebox workflow — the spatial practice for puzzle scenes.
- Genre Handbooks · Puzzle (Volume 1) §3.4, §4: tiered hints, stuck detection and solver tools — mutual references with this page's §3.3.
- Case Studies: how to break down a case — read alongside §2's benchmarks and §7's pitfall list.
- Pitfalls & Anti-patterns: pitfalls around content production and project management — cross-read with this page's §7.
- Indie Survival: scope control and scheduling, complementing §5.
- Exercise: draw a puzzle dependency graph on paper for a three-scene mini adventure, marking each node's motive, clue and payoff; then hand it to a friend who does not play this genre and see whether they can say what the first step should be.

In the end, point-and-click adventure tests only two things: when players are stuck, are the clues enough; when they figure it out, does the story deliver.
