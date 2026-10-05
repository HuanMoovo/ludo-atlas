# Ludo Atlas · Genre Handbooks · FMV

> **Genre Handbooks · Volume 4**. Positioning: the narrative genre whose primary material is live-action footage. The player's actions are watching, choosing and searching; the footage and the performances carry conviction, the branching and the editing carry participation, and the cost of the footage decides whether the project survives. This page covers four load-bearing blocks: the footage cost structure, branch-editing governance, interaction design and performance.
> Companions: Game Design Handbook (branch structures and narrative costs) · Art & Audio Handbook (video and audio specs) · Case Studies (breakdown and postmortem methods) · Indie Survival (scope control and budget discipline).
> This page carries no external links; benchmark titles are widely known works only, and the figures here are common magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: FMV is the narrative genre that **treats live-action footage as its primary content**. Every action the player takes happens in the gaps between shots: pick a path, search for a word, click a detail; whether the picture stops, how long the player gets to think, and whether a choice has consequences — that is the whole of this genre's design craft. It descends from the video experiments of the laserdisc era and was brought back to the mainstream in the digital-distribution era by Her Story and the generation of works it inspired; Chinese-language communities know it by several names (live-action interaction, full-motion video, interactive film), and today it lives on both game platforms and streaming platforms.

The core loop, written as a verb chain:

`watch a stretch of footage → make a choice or run a search → see the consequences → revise your understanding of the story → want to watch the next stretch`

This loop's rhythm is set by the cut points: inside a clip the player can only watch, and only at a clip boundary can they act. So more than half the design work is deciding "where the doors open, and how wide" (§3.1, §3.2).

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Visual novel | In one line: the visual novel spends its budget on writers, FMV spends its budget on the set; the branch governance is shared, the cost structures are opposites |
| Walking sim | The power to advance lies in footsteps and gaze; FMV locks the power to advance at clip boundaries, and the player's actions are choosing and watching |
| Interactive narrative drama (Telltale-style 3D staging) | Both advance through dialogue and choices; the other side burns animation and facial-capture pipelines, FMV burns shoot days |
| Traditional film and television | The audience can only watch; the player has a say at key nodes. FMV sells exactly that say, and image quality is the ticket in |

A self-check question: cut out every choice and edit it into a single finished film — is it still watchable? If not, the footage doesn't pass; and if removing the choices costs nothing, you have shot a film and paid for the interaction system on top.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **The persuasion of performance**: the detail on a real human face cannot be replaced by animation or text; once the footage's believability breaks (muddy sound, false performance, rough lighting), all the design behind it is buried along with it.
2. **The weight of a choice**: what my decision changes is what actually happens on screen, not a number; the first hint of a consequence must appear by the next clip at the latest.
3. **The pull of watching**: every clip boundary owes an answer (who next, why, what happens); keeping people watching for half an hour without wanting to stop is this genre's basic pacing skill.
4. **Digging and sharing**: multiple endings, hidden routes and a searchable footage library turn "watch it again" into gameplay; live-action work is naturally easy to screenshot and easy to discuss — for an indie project, the highest-value layer of word of mouth.

Negative feelings (any one of these is a red flag): choices with no consequences; clips padded to fill runtime with no information; interaction disconnected from the footage (irrelevant little actions inserted into a dialogue scene).

Benchmark titles (all widely known works; play them yourself before breaking them down):

| Title | What to learn from it |
| --- | --- |
| Her Story (2015) | The extreme sample of archive search: shot with zero branching, a feature film's worth of footage cut into 271 clips, with one search box carrying the entire gameplay |
| Immortality (2022) | Three kinds of footage interwoven — film clips, behind-the-scenes material, private recordings; a matching mechanic makes "archaeology" the core loop |
| Late Shift (2016) | A production sample of a full-motion branching film: 180-plus choice points and 7 endings; the picture never pauses for choices, testing the measure of timed interaction |
| Black Mirror: Bandersnatch (2018) | An interactive experiment on a mainstream feature-film platform; the controversy over "fake choices" and pacing is the best postmortem material |
| The Invisible Guardian (2019) | A commercial sample of live-action interactive film in mainland China: the combination of footage and choices, and the publishing playbook |
| Love Is All Around (2023) | A virality sample of live-action dating interaction: audience targeting and topic design matter more than production specs |

## 3. Design Essentials

### 3.1 Branch Structure: Chained Branching and the Footage Library

The two structures correspond to two cost models and two shooting plans:

| Structure | Gameplay | Cost profile | Representative works |
| --- | --- | --- | --- |
| Chained branching | Choice points point directly to different subsequent clips; branches converge and continue | Every choice point must actually be shot; cost stacks roughly linearly with the number of branches | Late Shift, The Invisible Guardian |
| Footage-library search | Footage is not pre-cut into branches; the player decides what to watch, and in what order, through search and browsing | Shot once, all of it usable; cost sits in the amount of footage and the tagging system | Her Story, Immortality |

Three governance rules for chained branching (each of them converts into money):

1. Convergence points first: before opening any fork, write down where it rejoins. Two branches merging back into the same scene cost addition; a tree that never converges costs multiplication.
2. Restraint with key choices: hard choices that truly change the direction stay in the single digits to low teens; the rest are implemented as light variations (swapped lines, shots or reactions within the same scene).
3. The clip table is the single source of truth: every clip registers its ID, duration, incoming edges, outgoing edges, affected flags and shooting status; the shooting plan and the edit progress both derive from this table, and a clip that is not registered does not exist in the project.

Editing governance follows three disciplines of its own:

- Clips must be intelligible on their own: the player may see any branch first, so every clip must hold up when watched alone, and its references must not depend on a fixed viewing order.
- Reshoots reuse the same shot plan: multiple branches of the same scene are shot with identical camera positions and framings, so the edit can cross-assemble and substitute them.
- Re-watch every time you wire an edge: when adding a new incoming or outgoing edge, check the transition frames, audio crossfades and duration joins; a wiring error is what the player experiences as a jump out of the story.

The convergence shape of a clip graph (schematic): `opening clip → choice point → branch A or branch B → convergence clip → next choice point`.

### 3.2 Interaction Design: Choice Points, Timed Choices and Small Interactions

The interaction toolbox comes in three tiers by degree of interruption; only mixing them gives a sense of participation without chopping up the rhythm:

| Tier | Form | Frequency scale | Measure |
| --- | --- | --- | --- |
| Explicit choice | The picture pauses or fades out and waits for the player to finish choosing | A handful to a low teens per film | Give ample thinking time; options must show a clear difference in stance |
| Timed choice | The picture keeps rolling; answer within the countdown or the default applies | Commonly one every 1–3 minutes | The default must be safe; set the duration by the slowest tester |
| Small interaction | Click a clue, search a keyword, leaf through an object | Depends on the gameplay | Must relate to the footage; no minigames that interrupt watching |

- Visibility of consequences: after a choice, give a perceivable response (a line, a shot, a status prompt) by the next clip at the latest; if players can't judge the consequences, they start choosing at random.
- The measure of timed choices: Late Shift made "no pausing" a selling point, and the price is that slow-handed players get overruled. The three-tier fallback: key decisions are untimed; medium choices are timed but come with a safe default; only small atmospheric choices are allowed to be "miss it and it's gone".
- Choosing small interactions: search-style interaction (keywords, matching) suits this genre naturally, because "watching" and "acting" are the same act; QTEs are used only when the footage itself is an action passage, and failure must route into a branch, never a loss judgment.
- Density check: plot every interaction point on the timeline; anywhere a continuous stretch runs over 3–5 minutes with nothing to do, add a search point or an environmental interaction point, or cut the stretch shorter.

### 3.3 Performance and Script: Writing Drama for Branches

The script is written to three standards — "shootable, editable, branchable" — not written as a linear script and taken apart afterwards:

- The trio moves together: the scene-by-scene script, the branch table (§3.1) and the shooting list (camera positions, props, cast, duration budget) are written and frozen together; the camera does not roll until the script is frozen.
- Short lines, clear direction: in branch passages, every reaction an actor gives may become material, so give execution directions rather than essays; leave improvisation to atmosphere scenes only.
- Leave a joint on every scene: prepare two endings (different emotions, different information) for a possible convergence — a discipline that linear script training never teaches.
- Casting and rehearsal are not optional: the audience judges live-action performance by film and television standards, and amateur acting drags the whole thing down a grade. Common practice: one week set aside for casting, one to two days for a table read and rehearsal, and a blocking pass on key scenes before the shoot.
- Performance density runs lower than film and television: players pass through the same performances again and again on different paths; crying scenes and shouting scenes must be used sparingly, or they depreciate on the rewatch.

### 3.4 The Shooting Cost Structure: Footage Is the Most Expensive Asset

The cost divides into four blocks, with the weights stated up front: footage (the shoot), post-production (editing, color grading, mixing, subtitles), the interaction layer (programming, UI, QA, platform adaptation) and pre-production (script, casting, location scouting, rehearsal).

- Footage is the only asset that cannot be reused: a scene shot badly (sound, performance, lighting) cannot be saved in post and can only be reshot; and a reshoot means paying again for money, schedules, cast, locations and equipment, all of it. Footage quality is the project's ceiling.
- The shoot day is the hardest constraint: crew, locations and equipment are priced by the day, and overrunning is overspending; variables like weather, location permits and cast availability go into the plan as "buffer days", not on luck.
- Spend money where it can be felt inside the frame: script polish, casting, production sound and basic lighting have the four highest marginal returns; gear stockpiling and fancy camera moves the lowest.
- Do the footage-ratio math first: total shot ÷ finished runtime, commonly 3–8× for linear short films; a branching work shoots every choice for real, so the total stacks with the branch count (the fix goes back to the convergence points of §3.1). The footage-library form approaches "everything you shoot is usable", but the cost transfers to the amount of footage and the upkeep of the tagging system.
- Rough-cut as you shoot: cut each clip roughly into the clip table the moment it is finished and confirm it stands alone and connects to all its incoming and outgoing edges; owing nothing on set is the cheapest insurance against rework.

## 4. Technical Essentials

The engineering difficulty concentrates in four places: the player and branching engine, the footage pipeline, branch state, and cross-platform build size.

**The player and branching engine**

- Treat the clip graph as data: nodes are clips (duration, subtitle track, thumbnail, flags), edges are choices and conditions, the player is only an executor and all structural management lives in the table; the clip boundary is the experience's bottom line — black frames, stutter and volume jumps instantly puncture the illusion that "this is a film", so transition frames, preloading and audio crossfades are reviewed point by point at every boundary.
- Two engine routes: the general-purpose engine route (Late Shift is a Unity project, with mature video and platform adaptation) and a self-built player route (web or native, suited to lightweight works and web distribution); the shared requirements are hardware decoding, buffering ahead and behind, and skip and rewind.

**The footage pipeline**

- The footage table manages two sets of specs: a stable ID plus metadata for each clip, proxy footage (low bitrate) for editing and development previews, and the finished cut entering the build by the platform spec table (resolution, bitrate, codec, audio track, loudness); the edit, the code and QA all reconcile against the same table, and localizations ship as external subtitle tracks without re-encoding the video.
- Backup discipline: dual backups on set (card plus drive), and footage archived by clip table the moment it enters the edit system; "the footage is missing" is the most common fatal incident on independent teams.

**Branch state and saves**

- Flags registered centrally: who has seen what, who knows what, what is in hand — all of it into one state table; choices only write the table and the edit only reads it; debug commands support setting flags directly and jumping to clips, so branches can be tested without watching from the start.
- Rewatch and save discipline: watched clips can be replayed and new clips are highlighted, with ending lists and collection progress defusing the anxiety of "what did I miss"; the save stores "flags and the set of watched clips" rather than clip pointers — pointer-style saves break the moment the structure updates, so test with old saves before any update (the same save discipline as the Visual Novel page).

**Platform and build size**

- Video size is an invisible barrier to conversion: 1080p high-bitrate footage runs about 3.5–7 GB per hour (at 8–15 Mbps), and a few hours of finished film runs straight into the platform's psychological download limit. Strategy: chapter packages, quality tiers (play at low bitrate first, download HD as progress demands) or streaming playback (only if the network and the licensing can carry it).
- Touchscreen adaptation gets its own test pass: choice-button hit areas, portrait and landscape, mis-touch protection; timed choices need extra leniency on touchscreens.

## 5. Content Volume and Workload Reference

The cost formula:

```text
Total cost ≈ finished runtime × branch multiplier × shooting cost per unit of finished runtime + post-production + interaction layer + pre-production
```

Branch multiplier = total usable footage ÷ single-playthrough runtime. Chained branching commonly runs 2–4×; the footage-library form can approach 1×, but the absolute footage volume is large and organized through search and ranking (Her Story is a clip library of around three hundred pieces).

Scope tiers (magnitude references, not a promise):

| Form | Finished runtime and footage scale | Timeline scale | Notes |
| --- | --- | --- | --- |
| Prototype short | 10–20 minutes finished, 1–2 hours of footage | 4–8 weeks | One chain with three choice points; validates the full path from shooting to playable |
| Small finished work | 40–90 minutes finished | 3–6 months | One cluster of locations, two or three main branches; a simplified version of Late Shift's scope |
| Commercial feature | 90–150 minutes finished, branch footage totaling several hours | 12–24 months | Film-grade production pipeline, professional production and post crews |
| Footage-library form | Several hours of footage, organized by search | Depends on the shoot's scale | No branch editing; cost sits in the volume of footage shot and the tagging system |

Three per-unit anchors:

- Shoot-day output (magnitude): a low-budget crew completes 5–15 minutes of footage a day; divide by the footage ratio (§3.4) for the finished runtime it contributes, with extra days reserved for reshoots and safety options.
- Editing workload: branch editing is not the addition of linear editing; every incoming and outgoing edge must be wired and re-watched, commonly several times the finished runtime in hours, estimated as the number of clips times the wiring cost per edge.
- Text and subtitles: lines, subtitles, ending descriptions and store copy all go on one list; organize localization from day one around "this will be translated" (the same convention as the Visual Novel page).

Scheduling anchors: from zero to a 10-minute playable prototype, 4–8 weeks; to a vertical slice (15–20 minutes, one complete branch chain, shipping-quality image) commonly 2–4 months; commercial scope is measured in years.

## 6. How to Start the First Prototype

Goal: 6–8 weeks to build a 10-minute "one chain, three choice points", running the whole path — write, shoot, edit, play, test. No multiple endings, no visual effects, no professional gear.

1. Weeks 1–2: script and clip table. Write a 10-minute piece: 3 choice points, 2 parallel branches (1–2 minutes each), 2 convergence points; produce the clip table and shooting list alongside. No script freeze, no camera.
2. Week 3: the concentrated shoot. One camera, natural light plus basic fill, forced production sound (a lavalier mic beats post-dubbing); shoot convergence scenes before branches, and get enough safety coverage per clip for the edit.
3. Weeks 4–5: rough cut and wiring. Cut every clip to stand alone per the clip table, then wire them into a clip graph by the choice relations; transition frames, audio crossfades and subtitles land in one pass.
4. Weeks 6–8: interaction shell and external testing. Add choice-point loading to the player (looks are not a concern yet) and test with 5 strangers: record where they drop out, their reactions after choices, and whether anyone wants to see the other branch unprompted; also log real working hours as the estimation base for the next project.

Success criteria (all observable):

- A stranger watches the whole thing with no prompts and can say at least once "my choice caused…".
- At least 2 of the 5 voluntarily restart to see the other branch's consequences.
- The whole path runs end to end with real numbers for the footage ratio: the clip table matches the footage, the edit matches the branches, the player matches the choice points, and the next budget doesn't rest on guesswork.

## 7. Common Pitfalls

1. **Shooting before the script is frozen**: one changed line triggers a chain of reshoots and doubles the budget. Avoidance: freeze script, branch table and shooting list together before the camera rolls (§3.3).
2. **The footage ratio out of control**: every choice shot for real with no convergence points leaves hours of unusable footage piled up in the edit. Avoidance: write convergence points before branches, and put the ratio into the budget (§3.1, §3.4).
3. **Fake choices**: nothing is perceptible after choosing and players stop taking it seriously after two rounds. Avoidance: either deliver real variation or cut the choice (§3.2).
4. **Production downgrade**: muddy sound, flat lighting, amateur acting, and the audience sentences the whole thing within three minutes. Avoidance: put the money into sound, fill lighting, casting and rehearsal; keep the gear simple (§3.3, §3.4).
5. **Interaction misfiring**: the default in timed choices is always the most timid one and slow-handed players get overruled; or an action QTE is jammed into a dialogue scene and playing and watching undercut each other. Avoidance: make defaults safe and leave important decisions untimed; pick interaction forms to match the footage passage (§3.2).
6. **No rewatch or watched-state tracking**: without a remedy for "what did I just miss", a branching work's replay cost runs too high to bother with. Avoidance: put rewatch, watched markers and ending lists into the design from day one (§4).
7. **No footage management or backups**: a single card and a single drive on set and chaotic naming lose footage or break the matching. Avoidance: dual backups on set, archived and named by clip ID (§4).
8. **Build size out of control**: full high-bitrate downloads shut mobile players out. Avoidance: choose tiers, packages or streaming per platform (§4).
9. **Rights and contract ambushes**: unclear scope in music, location and likeness licensing blows up on the eve of release. Avoidance: keep documentation for every license, and write likeness scope and re-editing rights into cast contracts.

## Further Reading

- [Game Design Handbook](../../fundamentals/game-design/README.md) §8 narrative design: the methodological base for branch-cost management and choice design; corresponds to section 3.
- [Art & Audio Handbook](../../fundamentals/art-audio/README.md): video and audio specs and mixing rules — the expanded ledger for §3.4 and section 4 of this page.
- [Case Studies](../../postmortems/README.md): methods for breaking down and postmorteming live-action interactive works; consult when dissecting the section 2 benchmarks.
- [Indie Survival](../../../playbooks/indie-survival/README.md): scope control, budget and scheduling discipline, complementing section 5.
- [Pitfalls & Anti-patterns](../../pitfalls/README.md): kickoff, content production and legal pitfalls, to be read against section 7.
- [Genre Handbooks · Visual Novel](../visual-novel/README.md): the sister page on branch governance; the cost-structure contrast with the text route.
- [Genre Handbooks · Walking Sim](../walking-sim/README.md): the other end, with no choices; a reference for narrative pacing and staging costs.
- Exercise: break the first 15 minutes of a benchmark work into a clip table (IDs, durations, incoming edges, outgoing edges, choice points) and estimate its equivalent footage ratio; finish this table before deciding whether to shoot your first project.
