# Ludo Atlas · Playbooks · Vertical Slice

> **Playbook**. Positioning: turn "one short stretch of the complete experience at finished quality" into a presentable, calibratable production unit, used as a quality bar (internally), proof of direction (externally) and an estimation baseline (scheduling).
> Companions: Production Handbook · Game Design Handbook · Art & Audio Handbook.
> Principle: a slice proves quality and capability, not volume; it is a ruler, not a shrunken final release.

---

## 1. When to Use It and What It Is For

A vertical slice cuts vertically: rather than spreading horizontally within one system, it cuts through a layer, bringing gameplay, art, audio, UI and performance all to finished quality in one short stretch of experience. In scope it is usually one level, one sequence or a short quest chain; vertically it must cut through every system, with all systems genuinely running (§3.3).

The usual size is 15–30 minutes of playable content (narrative games can be shorter, systems-driven games longer; treat the figures as an order-of-magnitude reference). It carries two roles at once: the quality bar, which all later content copies; and the budget ruler, whose real work-hours feed back into the full production schedule.

A slice is not a marketing demo: a demo can be all booth effect, but a slice must be playable, runnable and usable as a baseline. The four goals it must achieve:

- **Prove the direction**: the core fun still holds when wrapped in finished-quality production, and the selling point is visible at a glance.
- **Prove capability**: the team (or you alone) can produce this quality reliably, not by luck.
- **Calibrate the budget**: recalculate full scheduling from the slice's actual work-hours and cost (conventions in Production Handbook §2.2).
- **Align the vision**: give every stakeholder one concrete thing they can play, argue over and accept — in place of documents and verbal descriptions.

Who each audience is, and what they look at:

| Audience | What they look at | What the slice must prove | Common misuse |
| --- | --- | --- | --- |
| Team | A shared quality standard and scope boundary | "This is what we are making" | Treating the slice as a production asset library and expecting its content to be reused directly |
| Publisher / investor | The selling point, the state of completion and execution ability | The direction is credible and the budget is credible | Making a booth demo and dodging the real systems |
| Yourself | Whether the direction deserves the next stretch of time | The fun is real, not self-indulgence | Substituting internal leniency for external acceptance |

When to do it, and when to hold off:

- Do it when: the toy prototype has passed external playtesting and the next step is production; or you need to prove direction and capability to outsiders.
- Hold off when: the core loop is not yet validated — go back to the prototype layer and pass the toy test first (Game Design Handbook §1); spending slice budget on unvalidated fun is the most expensive mistake.
- Prerequisites (all true before work starts): the core loop has passed playtesting; the one-pager and scope statement are in place (Production Handbook §1); the target platform and target hardware are set; reference titles for quality are chosen.

What you get when it is done (deliverables you can accept):

- A 15–30 minute playable build at finished quality.
- A quality baseline set: asset specs, game-feel parameters, acceptance conventions — copied wholesale in production.
- A set of showcase materials: playtest package, screenshots, trailer concept, updated one-pager.
- A full schedule and budget recalculated from slice data, plus a decision record for the three-way choice.

## 2. The Process at a Glance

Five steps on the main line: `Set the bar → Pick the segment → High-fidelity → Polish → Showcase`, closing with review and calibration.

| Stage | Timebox (reference) | Main actions | Exit criteria |
| --- | --- | --- | --- |
| 0 Set the bar | 3–5 days | Success criteria, timebox, reference titles, budget | Success criteria verifiable; the timebox locked |
| 1 Pick the segment | 1–2 weeks | Choose the representative segment; draw the flow and emotion curve | The segment covers every key system |
| 2 High-fidelity | 4–10 weeks | All systems genuinely running; assets swapped to finished quality | Playable end to end with no placeholders left |
| 3 Polish | 2–6 weeks | Game feel, pacing, audio-visuals, accessibility | External playtest passed (§4) |
| 4 Showcase | 1–2 weeks | Playtest package, screenshots, trailer concept, one-pager update | Materials complete; deliverable on its own |
| 5 Review and calibration | 3–5 days | External demo, collect feedback, recalculate full production time | Follow-up decisions on paper |

Three disciplines, more important than the timebox itself:

- Estimate the total at 2–4 months (starting from a prototype, full-time small team; an order-of-magnitude reference); when it overruns, cut scope first and then re-estimate — extending only eats the production budget.
- Every stage's exit is a playable build or a verifiable artifact, not a completion percentage; if the exit criteria are not met, do not enter the next stage.
- If the review does not pass, do not enter production; rework during the slice costs an order of magnitude less than rework during production.

## 3. Step-by-Step Execution

### 3.1 Set the Bar: Write the Standard First, Then Start

Write the success criteria as 3–5 verifiable sentences before work begins. Examples (replace the numbers per project; order-of-magnitude reference):

- External playtest with 5–10 people (conventions in Production Handbook §5): most finish without hints and can state the selling point in one sentence afterwards.
- Quality checked against 2–3 reference titles: side-by-side screenshots and game-feel comparisons that do not come up short.
- Frame rate on target on the target hardware; 30 minutes of continuous play without a crash.
- Timebox and budget: total weeks locked; the polish reserve listed separately (§3.4).

Reference titles are where the bar comes from: pick titles of comparable quality and scope, break down their screenshots, screen recordings, game-feel parameters and asset specs, and turn "looks finished" into a checkable list instead of an adjective.

### 3.2 Pick the Segment: Where to Cut

Three criteria for the segment; all three are required:

| Criterion | Meaning | Counterexample |
| --- | --- | --- |
| Selling-point density | The ten-odd minutes that best put the selling point on display | A flat, feature-by-feature walkthrough |
| System coverage | Every core system appears at least once in full | Movement only, no combat or inventory |
| Stands on its own | Has a beginning and an ending; needs no outside context | A mid-game passage where outsiders cannot tell what is going on |

- Avoid choosing: a tutorial opening (weak selling point), a finale set piece (costs out of control), a medley of separate passages (the main line cannot be explained).
- Method: score 2–3 candidate segments on "selling-point display, system coverage, workload, risk", pick one and write down the reasoning.
- The slice may re-tune pacing and content for presentation, but mark which assets and levels can migrate into the full game and which are one-off investments, so that not all the work is wasted.
- Exit check: draw the chosen segment as a 15–30 minute flow diagram (goal, events, small climaxes, ending) and walk the team through it once.

### 3.3 High-Fidelity: Every System Genuinely Runs

What the slice cuts is a vertical face: gameplay, UI, saves, audio, settings and platform features must all genuinely run. A wall of screenshots cannot replace a playable build.

System checklist (trim per project; every item must be walked through completely in the slice):

- The core gameplay loop and onboarding (if the slice needs it).
- Menus and settings: resolution, volume, key bindings and gamepad.
- Saving and continue (whatever the full game has, the slice must have).
- Audio: music, sound effects, mixing (specs in the Art & Audio Handbook).
- UI/HUD and text layout, including loading and pause.
- Performance: measured on the target hardware — no dropped frames, no memory overruns.
- Edge cases: window switching, sleep, unplugging devices, full save slots.

Asset-replacement discipline: whitebox → benchmark assets → batch replacement. Make 1–2 "hero assets" first to pin down the quality ceiling and specs, then build the rest to that baseline; with each replacement pass, compare against the reference titles once. Ship a playable build every week (the cadence in Production Handbook §10); mark ugly parts honestly; never substitute screenshots for the build.

### 3.4 Polish: The Time Budget for Polishing

- Reserve 30%–50% of production time for polish. It is normal for "the first 90% of progress and the closing 10% to each take half the time"; do not estimate at a linear rate.
- Polish order: fix experience-blocking problems first (controls that do not respond, pacing that drags, crashes), then upgrade the presentation layer (camera, effects, sound layers); reverse the order and the money goes into things destined for rework.
- Feedback loop: internal self-test → targeted external 5–10 people (Production Handbook §5); observe without prompting and record pause points, failure points, laugh points and curse points; each round, fix only the top few items on the issue list; it passes only when feedback converges across two consecutive rounds.
- Set the acceptance line in advance (§4) and freeze once it is met. Polish is a converging action, not endless smoothing.
- Prioritize the details that can be seen and heard: input feedback, camera, sound effects, visual effects; they decide whether it "looks finished".

### 3.5 Showcase: Make the Slice Visible

- **Playtest package**: a build that can be distributed on its own — no developer pop-ups, a clear beginning and end, running through completely on the target hardware; attach a one-page explanation (what this is, how to play, what feedback is wanted) and a feedback channel.
- **Screenshot set**: multi-resolution versions to storefront specs, covering at least the three kinds of shots — gameplay, selling point, atmosphere (asset methods in the Live-Ops & Growth).
- **Trailer concept**: a 30–60 second script and storyboard with the selling point in the first 3 seconds; cut a concept version from slice footage and wait for production assets for the real trailer.
- **One-pager update**: swap the vision for facts verified by the slice — selling point, quality, schedule and budget each with a source.
- **Demo script**: a 10–15 minute run-through for publishers/investors, spelling out how to open, which part to demo, which part to leave for them to play, likely questions and a data page.
- Delivery discipline: builds, screenshots, videos and documents go into a single delivery directory, with versions aligned to the slice build number.

### 3.6 Review and Calibration

- The review answers only two questions: is the quality good enough (against the reference titles), and is the direction right (does the selling point hold). Answers are backed by evidence — playtest records, screenshot comparisons, the playable build — not adjectives.
- Work-hour calibration: full estimate = actual slice work-hours × (full content ÷ slice content), then corrected by the experience multiplier (content work ×2–3) and buffer (30%–50%) (conventions in Production Handbook §2.1–2.2).
- Decision exit, one of three: continue to production (freeze the quality baseline), adjust the direction (return to the prototype layer and change the core), or shrink scope (bring the project down to a size the slice can anchor); the conclusion goes into a decision record.
- Archive the slice assets: passing assets and specs are frozen as production templates and acceptance baselines; one-off parts are clearly marked and kept out of the reuse pool.

## 4. Acceptance Checklist

- **Experience**: most of the 5–10 external playtesters finish without hints; they can state the selling point within 10 minutes of play ✓; someone actively wants to keep going ✓
- **Quality**: side by side with the reference titles (screenshots, game feel, audio) it does not visibly come up short ✓; no placeholder assets remain ✓
- **Engineering**: every system genuinely runs (menus, settings, saves, audio, UI) ✓; frame rate on target on the target hardware, 30 minutes of continuous play without a crash ✓; edge-case handling passes ✓
- **Showcase**: the playtest package is clean and distributable (no debug information) ✓; the screenshot set and trailer concept are complete ✓; the one-pager is updated with slice data ✓
- **Scope and calibration**: the timebox is met (overruns handled through the scope-cutting process) ✓; the full schedule and budget have been recalculated from slice data ✓
- **Decision**: the conclusion — continue, adjust or shrink scope — is on paper with owner and date ✓

## 5. Common Pitfalls

1. **The slice keeps growing**: 15 minutes becomes an hour, the timebox breaks down, and the production budget is eaten up. Countermeasure: lock the timebox; when it overruns, cut scope first and then re-estimate; the slice is a calibration tool, not a content reserve.
2. **Art only, no systems running**: the slice becomes a beautiful wall of screenshots — menus, saves, audio and performance never hooked up — and only at the review do you find out it cannot stand. Countermeasure: all systems genuinely running is part of the slice's definition, not a closing step (§3.3).
3. **Polish time doubles**: the first 90% of progress and the closing 10% each take half the time; a linearly estimated schedule is bound to blow up. Countermeasure: reserve a 30%–50% polish budget; set the acceptance line in advance and freeze when it is met.
4. **Treating it as full-game development**: laying out content to production standards, building every pipeline system, adding features along the way — the slice becomes a big project with no deliverables. Countermeasure: build only what the chosen segment needs; write everything else into the "won't-do list" (Production Handbook §3).
5. **No success criteria**: when it is finished the only verdict is "looks decent", and there is no way to judge whether to enter production. Countermeasure: write 3–5 verifiable criteria during the set-the-bar stage (§3.1).
6. **Substituting internal leniency for acceptance**: showing it only to friends and family brings encouragement, not data. Countermeasure: targeted external playtests, observe without prompting (§3.4).
7. **The slice disconnected from the full game**: the chosen segment is a one-off deal, every one-off asset is discarded, and none of the work-hours carry into production reuse. Countermeasure: mark migratable items when picking the segment, and make specs and assets to reuse standards (§3.2).
8. **Scope creep after the showcase**: every new request harvested from the external demo is accepted wholesale. Countermeasure: one in, one out; requests go into the backlog and are recorded (Production Handbook §3).
9. **Performance and stability left to production**: if the slice runs, it counts as done; only in production do you discover the target hardware cannot keep up. Countermeasure: performance and edge-case handling go into slice acceptance (§4).

## Further Reading

- Production Handbook: milestone definitions, estimation multipliers and buffers, scope control — the underlying draft for §2 and the work-hour calibration here.
- Game Design Handbook: core loops, toy tests and playtest validation methods — the preconditions for a slice to hold up.
- Art & Audio Handbook: quality bars, asset specs and polish checklists; the "looks finished" part of the slice executes against it.
- Level Design Handbook: pacing, guidance and whitebox methods inside the segment; general for 2D and 3D.
