# Ludo Atlas · Genre Handbooks · Walking Sim

> **Genre Handbooks · Volume 3**. Positioning: a narrative genre with no combat, no puzzles and no fail state, in which the player reads a story by walking, looking and listening; space itself is the narrator, and this page covers its interaction contract, staging ledger, HUD-free guidance and scope control.
> Companions: Game Design Handbook (core loops and narrative design) · Art & Audio Handbook (scene and audio specs) · Case Studies (breakdown methods) · Indie Survival (scope and scheduling).
> This page carries no external links. Benchmark titles are widely known works only; the figures here are common magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: the walking sim is the genre **that makes "walk, look, listen" itself the content**. No failure, no resource management; the player's entire toolkit is presence and attention, and the story does not grow in cutscenes but in space, objects and sound. Chinese-speaking communities also call it "walking simulation" or "narrative adventure"; this page standardizes on "walking sim". This genre's rhythm is measured in minutes, and every pause and discovery has to hold up on a second look; the fuel is curiosity, not a reward table, and the loop stalls in exactly one way: the player neither knows where to go nor cares.

The core loop, written as a verb chain:

`walk → notice something out of place → approach and look → read a piece of information → your understanding shifts → want to go to the next place`

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Visual Novel | Reading is the first action and space degrades into a backdrop; the walking sim hands advancement to walking, and reading is the reward |
| Point & Click Adventure | Puzzles are gates that only open once solved; the walking sim has no gates, and curiosity sets the pace |
| Interactive movie (the Life is Strange, Detroit: Become Human kind) | Key beats are carried by choices and timed actions; the walking sim gives key beats to space and text, interrupting the walk as little as possible |
| Walking horror (the Layers of Fear kind) | Also tells its story through walking and sound, but the threat takes over the pacing; the walking sim refuses punishment, and tension comes from the information itself |

A self-check question: remove all combat, puzzles and fail states — are players still willing to walk to the end? If the answer is yes, what you are making is a walking sim; if it needs mechanics to hold people, it is something else wearing a narrative skin.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Presence**: the player believes they are standing in that place; light, sound and the details underfoot all play along.
2. **Curiosity as the pull**: there is something after every corner, and that something is worth the walk.
3. **The pleasure of assembly**: information is not handed over all at once — players connect the fragments themselves and arrive at a truth of their own.
4. **Emotional payoff**: every step walked finally gathers into one emotional landing point, and the story ends inside "your own journey".
5. **Being respected**: not treated as a fool (no arrows added, no hints fed) and not punished (you cannot die, cannot get stuck, and can stop at any time).

Benchmark titles (widely known works only; play them to completion yourself before breaking them down):

| Title | What to learn from it |
| --- | --- |
| Firewatch | Two-hander dialogue over the walkie-talkie: the two characters never share a frame, and the relationship arc is carried by lines and silence; canyon terrain used as level design |
| What Remains of Edith Finch | One standalone interaction per family member, a dozen-plus modes of expression inside two hours; text, objects and space assemble the family history |
| Gone Home | One 1995 house, the whole story grown on objects and notes; a textbook on delivering the ending's information |
| Dear Esther | The extreme form of walking plus monologue, the island is consciousness; interpretation handed to the player whole |
| The Stanley Parable | The narrator against the player; disobedience as gameplay, proof that a walking sim can be funny and hold up to replays |
| Journey | The wordless cousin of the walking sim: space, music and anonymous companionship make up the entire narrative, and the emotional curve is the only goal |

What players expect from this kind of work is "one complete emotional journey", not "a system to replay over and over"; that expectation decides almost every design trade-off on this page: it can be short, but it must not drag; it can be quiet, but it must not be dull.

## 3. Design Essentials

### 3.1 Narrative-Driven Exploration: Space, Objects and Sound

Three narrative carriers, with different jobs:

- **Environmental storytelling (space as narrator)**: layout, furnishings, wear and lighting all say something. Acceptance test: turn off all text — can a single room tell you "who lives here and what happened recently"? If not, it is set dressing, not narrative.
- **Objects and text**: notes, letters, recordings, photographs, graffiti. One text carries only one new piece of information; "long text equals depth" is an illusion, and the skip rate is proportional to length (§7).
- **Sound (including a unified voice)**: ambient layers, distant sounds, radio and monologue; sound is the only narrative layer that works without being looked at, and it doubles as guidance (§3.4). Establish the voice sheet before writing any text, so that multiple writers do not clash — the same method as the Visual Novel page.

Information is registered in three tiers, with placement and fallback written into a table:

| Tier | Content | Placement | If the player misses it |
| --- | --- | --- | --- |
| Main-line information | Facts the player must know | Mandatory paths, mandatory interactions | System fallback: deliver it again somewhere else |
| Character information | Personalities and relationships | Optional side paths, object text | Missing it is allowed; it does not affect understanding the main line |
| Atmosphere information | Worldbuilding detail and aftertaste | Odd corners, repeated observation | Missed is missed; saved for a second playthrough and discussion |

Three disciplines:

- Key information needs at least two delivery channels: once along the mandatory path, once again through a revisitable piece of physical evidence; a single-point trigger is the most common way these works crash and burn.
- Out-of-order compatibility: players may arrive early or late and wander in any direction; text and dialogue must survive out-of-order access, with references that do not depend on a fixed order.
- Fact-table reconciliation: characters, dates, places and objects stay consistent across the whole work; all the charm rests on details being credible, and one contradiction tears down the whole wall.

### 3.2 The Player Contract: Tolerance for Slowness and the Do-Not List

- The first ten minutes are the signing period: players use that time to confirm two things — there is no danger here, and this is worth seeing. One pressure-free opening plus one clear payoff (a view you can take in at a glance, a mystery) and the contract is signed.
- Tolerance for slowness is set not by duration but by payoff density: three to five minutes in a row with no new information (visual, textual or audible) and players start to doubt the pacing. Calibration method: mark the moments in testing when players "voluntarily stop to look at something" on a timeline — the gap between two such stops is your ceiling for slowness; any stretch that feels hard to sit through even in your own replay: cut it or add something.
- Speed gets signed into the contract too: the default walking pace is the touch players live with, and the standard is "sightseeing without impatience, traveling without pain"; provide an effortless sustained run and no stamina bar.

The do-not list (explicit exclusions — writing the contract into the design):

| Not doing | Why |
| --- | --- |
| Fail states and death | Incompatible with the "look freely" contract; falling is handled by putting the player back |
| Combat, chases, stealth | They change how players allocate attention; the horror branch is a different contract, not to be mixed in |
| Time limits and countdowns | System-level anxiety serves no narrative; in-story urgency is carried by staging |
| Resource management and inventories | They switch players from "reading a story" to "balancing the books" |
| Collectible checklists as compulsion | Checklists make players walk for completion percentages; collecting must serve the narrative (photo albums, recordings) |
| Making players find the way themselves | Getting lost is an incident, not a level; the sense of direction must come from the design (§3.4) |
| Forced cutscenes and input locks | Staging should happen during the walk as much as possible; lock the player as little as possible |

The comfort floor matters as much as the list: pause and quit at any time, autosave, skippable and rewatchable staging, adjustable subtitles and font sizes; these are not bonus points but part of the contract.

### 3.3 Staging Costs: The Voice, Text and Animation Ledger

Get the cost structure straight first: the walking sim does not burn money on gameplay systems, it burns money on staging. You need three sheets from the moment you greenlight: text word count, voice minutes, and the count of animation and environmental motion entries.

Voice is the biggest variable, and the choice of staging format decides the cost tier outright:

| Staging format | Cost tier | Fits | Watch out for |
| --- | --- | --- | --- |
| Radio / walkie-talkie style | Low | Two-character relationship narrative; no shared frame, no lip-sync or camera overhead | The voice needs device texture and spatial processing, or it slides into narration |
| Monologue / narration style | Low to medium | Private, poetic narrative | Keep information density restrained; it slips easily into a staged reading |
| Full-scene dialogue with lip sync | High | Works with live NPC interaction | Animation and camera costs multiply; every script change means a re-record |
| No voice, text only | Lowest | Prototypes, experiments and small-scope works | The emotional ceiling is limited; writing and staging have to make up for it |

- Text and voice ledger: keep separate books for dialogue, monologue, object text and subtitles; writing speed and the revision multiplier follow the Visual Novel page's conventions (2,000–4,000 characters of first draft per day, revision at 0.5–1×); for voice, total up the spoken duration first and multiply by the rate — have a voice actor read a sample against a stopwatch to convert, and only enter the booth after the text is frozen; budget extra for re-records when the script changes.
- Animation and audio ledger: animation splits into three books (first-person hands and props, interactables, environmental motion), and environmental motion is the biggest share of atmosphere and the most easily underestimated; audio carries two lines, guidance and emotion, and reverb transitions, music trigger points and the radio audio chain all deserve their own lines in the plan.
- Budget discipline: expensive staging (full-screen scripted sequences, drastic lighting changes, wide-scope animation) goes only at emotional peaks, with a per-chapter budget sheet; if every stretch wants to be spectacular, nothing in the whole work is. Put important conversations into "listen while you walk" formats (radio, telephone, tape recordings) — players control the pace, and you save on camera and lip sync; Firewatch's walkie-talkie structure is the classic model for this route.

### 3.4 HUD-Free Guidance: Sense of Direction and Focus Guidance

The principle: these works can hardly ever carry quest arrows or minimaps — they dismantle the pleasure of "finding it yourself" on the spot. Guidance has to grow inside the world; the toolbox is as follows:

| Tool | How | Notes |
| --- | --- | --- |
| Light | Keep the main path and the next landing point bright; darkness de-emphasizes side branches | The cheapest and most effective guidance |
| Composition | Door frames, gaps in trees and street corners form viewfinders that frame the target | Players walk toward what looks like a picture |
| Landmarks | One anchor visible from afar per area (a tower, smoke, a lit window) | If players can say "where am I", they will not get lost |
| Sound | Ambient sound points toward the objective; radio and music pull the eye | Guidance that arrives without being looked at |
| Motion | Wind, smoke, birds, a flickering lamp | The only moving thing in a still frame is the focal point |

- Sense-of-direction design: an anchor system plus sightline corridors, revealed progressively. Entering a new area, first give players an anchor they can see at a glance, then set them loose to explore; the anchor gets used again and again to answer "which way should I go". Focus guidance is subtraction too: anything you need players to look at cannot have equally striking things around it — clear the stage at staging moments, then place the focus.
- Getting lost is an incident: the price of no HUD is high lost-costs, so catch it with testing and record three kinds of lost events — spinning in place, repeated backtracking, long stretches without heading for the objective; the fix is more light, more sound, more landmarks, not more arrows. Also build a toggleable "guided mode" (brighter focus cues, more prominent audio), off by default, as a fallback only for those who need it.

### 3.5 Length Control: Why 2–4 Hours Holds

- Scope logic: walking itself has no growth curve, and curiosity is a one-time resource; how fast novelty decays is what makes this genre suited to being short — 2–4 hours is a complete journey across one to three evenings, aligned with how players price and talk about these works; stretch it past 8 hours and you need multiples of scenes, text and staging density to keep curiosity's half-life up — the moment density drops, players switch from "exploring" to "commuting".
- Structure template: the opening (5–10 minutes) signs the contract, establishes the place, plants the mystery and teaches "walk, look, listen"; the middle develops and does one information reshuffle, giving players a second-layer understanding of what they have already seen; the last 30–60 minutes converge and pay off the emotion — keep walking distances short, and do not let the climax be diluted by walking.
- Pacing table (common magnitudes): one small find every 2–3 minutes (a readable object, a change in the scenery, a radio line); one medium payoff every 10–15 minutes (a new area, key text, a staged moment); one major node every 30–40 minutes (a plot turn or an emotional peak). Time a full greybox playthrough, then time strangers playing to completion; look at the distribution, not just the average — the shortest and longest runs each expose a kind of problem, guidance too direct or getting lost too often.

## 4. Technical Essentials

The engineering difficulty concentrates in four blocks: first-person movement, interaction and triggers, staging scheduling, and audio and saves. Starting from the stock first-person templates in Unity, Godot or Unreal is enough; a custom engine brings no return.

**First-Person Movement**

- Trust only measurements when tuning speed: take three to five people unfamiliar with the project and ask two questions — is it urgent, is it too slow; take the intersection of their feel as your speed, with an effortless sustained run alongside the default walk.
- Camera and motion sickness: head bob, field of view, motion blur and camera sway all become settings, defaulting to the conservative tier; motion sickness knocks some players out of the game outright, and having no options is the same as closing the door on them.
- Steps and low walls get automatic traversal plus animation, not a jump action; collision must match what the player sees — players will try to squeeze into every corner that looks reachable, and "looks passable but is not" hurts presence more than anything.

**Interaction and Triggers**

- One shared template for interactables: visibility condition, action, feedback, post-completion state — the four-piece set; even "take a look" becomes an inspect interaction with zoom and rotation, the cheapest reading gesture there is. Hints use the object's own visual language (outlines, a faint glow) rather than text labels — the lower the presence, the better.
- Triggers, state tables and debug commands: volume triggers plus event scheduling, with key staged sequences on state-checked triggers (if the condition is met, deliver it — a player who skips past or triggers early is covered either way), and out-of-order access handled as first-come-first-served with late arrivals catching up; register every flag in one place, and look up double or missed triggers in the table (the same principle as the Point & Click Adventure page); build the debug commands for jumping scenes, injecting and skipping staging, and highlighting interactables first — without them, every test pass means walking the whole route again.

**Staging Scheduling**

- Timeline plus state machine: dialogue, camera, audio and animation run on one shared timeline, and player input is handled in three tiers — locked input, soft lock (you can turn your head but not walk), unlocked — preferring the latter two; keep cutscenes restrained: full-screen cutscene cameras are expensive and break presence, so events that can happen inside the space should happen inside the space. Staging can be simple, but it must not fall apart — one animation stuck in mid-air or one hard audio cut shatters the mood the previous ten minutes built.

**Audio and Saves**

- Spatial audio and reverb zones are half of "presence": sound tells players where they are before the visuals do; music trigger points with fades in and out, two or three rises and falls per chapter are enough (the same BGM discipline as the Visual Novel page); the radio audio chain (compression and filtering) is worth its own pipeline.
- Saves and accessibility: autosave triggers at both area and node points, with chapter select and read markers, and no "restart the section" penalty of any kind; subtitle size and background, independent volume for voice, ambience and music, motion-sickness options, guided mode and color-blindness checks each go into the settings page, tested before release.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimation and for cutting requirements; not a commitment.

| Tier | Scene scale | Completion time | Timeline scale | Notes |
| --- | --- | --- | --- | --- |
| Prototype | 1–2 rooms | 10–15 minutes | 2–4 weeks | Validates walking feel, focus guidance and one information chain |
| Short piece / jam | 3–6 scenes | 20–40 minutes | 1–3 months | A single emotional theme, completable solo |
| Typical indie release scope | 8–15 scenes | 2–4 hours | 6–18 months | The main costs are text, voice and scene art |
| Larger scope | 20+ scenes | 4–8 hours | Multiple years for a team | Density maintenance costs climb steeply; not advised for a first work |

- Scene and art ledger: each scene equals greybox layout (days) plus art refinement (days to weeks, depending on style) plus text and recording plus staging script plus audio layers; from greybox to release quality, the time is usually three to five times the greybox. Environmental assets are grouped by theme and reused modularly (wall panels, floors and furniture built as kits); one scene theme's asset kit typically runs from dozens to hundreds of pieces.
- Text and voice ledger: dialogue and monologue in a 2–4 hour work typically run 15,000 to 40,000 characters, with object text and notes counted separately; writing speed and the revision multiplier follow the Visual Novel page's conventions; for voice, total up the spoken duration and multiply by the rate, and budget extra for re-records when the script changes.
- Scheduling and localization: from zero to a fifteen-minute playable prototype takes 2–4 weeks; one scene at release quality (a vertical slice) typically takes 2–4 months, and you extrapolate by scene count from there; text and voice come before art refinement — record before the text is frozen and you will redo it, guaranteed. Ambient sound design, mixing, text export and glossaries are ongoing work that enters the plan on day one, not finishing work.

## 6. How to Start the First Prototype

Goal: in 2–4 weeks, build a 10–15 minute "one path plus one room" that validates three things: walking feel, HUD-free focus guidance, and whether one information chain reads as it should. Do not touch voice, final art or menus.

1. Days 1–4: install the engine, get the first-person template running, make walk speed, camera and bob parameters tunable, and confirm the defaults do not grate at your scene's scale; then write one ten-minute information chain on paper: what the player should know before entering, which three to five things in the room are worth looking at, and what conclusion they should reach afterward.
2. Days 5–10: greybox one path, one room and three to five interactables (colored blocks with text labels), with all text written as final copy — no placeholder junk; here the text is the content. Then run the guidance experiment: strip every HUD element and text hint, use only light, sound and composition to lead players to each interactable, and walk it ten times yourself to confirm it works without hints.
3. Days 11–12: add audio (ambience plus one music trigger point) and autosave; test with 3–5 strangers who do not play this genre — no hints, no talking — and record the lost points, the skipped points and the spots where they linger longest.
4. Days 13–14: iterate on the record — add light or sound at lost points, cut text or change the format at skipped points, and write down the lingering spots, because those are the techniques to reuse in the real content; at the end, ask only one question: "Do you still want to know what happens next?"

Acceptance criteria (all observable):

- At least 4 testers complete the whole route without hints, with no more than one lost event each.
- Someone voluntarily stops to look at details and voices their own guess — only then does the environmental storytelling hold; with all art and audio removed, the greybox plus text still reads as "what happened".
- The post-completion retelling matches the design intent: the story testers tell is the same as your information chain's answers, or at least not contradictory; they leave discussing the story rather than asking "what is this game even about".

## 7. Common Pitfalls

1. **Space that does not narrate**: rooms are just corridors and ornaments, and after the full walk nobody can say what happened anywhere. Fix: make every scene answer one question — "who is here, and what happened recently" (§3.1).
2. **Single-point information triggers**: a key staged moment fires once, and wandering off the path misses it forever. Fix: two channels for key information, out-of-order compatibility, state-checked triggers (§4).
3. **Falling back on the HUD**: add quest arrows and a guidance bar and the sense of exploration drops to zero on the spot. Fix: exhaust light, sound and composition first; arrows exist only as an accessibility option (§3.4).
4. **Settling for walking feel**: shipping default parameters, so speed and camera feel awkward the whole way and motion sickness gets no options — ten minutes is all it takes for players to pass sentence. Fix: tune walk speed, camera, bob and motion-sickness settings as one system (§4).
5. **Text indulging itself**: notes written as little essays, skipped wholesale by players. Fix: one text, one new piece of information; cut the atmospheric-description filler; put the skip rate into your review metrics.
6. **Voice and audio jumping the gun**: entering the booth before the text is frozen means a re-record for every changed line and a doubled budget; outsourcing audio as a music pack leaves scenes stuffy and the sense of space lost. Fix: record after the text is frozen, and record in batches in "listen while you walk" formats first; budget ambience and reverb per scene, and bring audio work in early (§3.3).
7. **Staging locking the player down**: input locks every few minutes for a cutscene, breaking the sense of autonomy again and again. Fix: stage during the walk as much as possible, preferring a soft lock or no lock at all (§4).
8. **Scope out of control**: aiming for eight hours, discovering halfway through that curiosity cannot carry it, and watching the density collapse. Fix: cap a first work at four hours, and check stretch by stretch against the pacing table in §3.5.
9. **Motivation dropping out**: players do not know why they should go to the next place and navigate by "wherever looks like a path", and the game degrades into a maze. Fix: before any objective lands, ask "what does the player want to know right now" — motivation comes from the information gap.

## Further Reading

- Game Design Handbook §8, narrative design: the methodological base for worldbuilding presentation, environmental storytelling and information placement, and the parent method for §3 of this page; pair it with the Case Studies breakdown methods when dissecting the benchmarks in §2.
- Art & Audio Handbook: scene art specs, ambient sound design and mixing standards — the expanded ledger for §3.3 and §5 of this page.
- Indie Survival and Pitfalls & Anti-patterns: scope control, scheduling and content-production pitfalls, complementary to §5 and §7.
- Companion pages in this handbook: Visual Novel (the text-and-staging division of labor) · Point & Click Adventure (guidance and softlock prevention) · Interactive Fiction (state tracking); boundaries in §1.
- Exercise: for a fifteen-minute scene, write one three-tier information chain (main line / character / atmosphere), marking the two places where each tier is delivered; then break one benchmark work's first ten minutes into three rows — "path walked / information given / your emotions" — and lay out a timeline.

In the end, the walking sim tests only two things: whether every detail you put into the space speaks, and whether the player, at the end of the walk, has assembled the complete truth.
