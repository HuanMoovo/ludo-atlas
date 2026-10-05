# Ludo Atlas · Playbooks · 30 Days: Idea → Demo

> **Playbooks**. Positioning: use 30 days to compress a one-sentence gameplay idea into a 10-minute demo that is playable, presentable and reviewable, and get the evidence that "the core loop is worth investing in" — rather than build a complete game.
> Companions: Game Design Handbook · Production Handbook · AI Workflows · Pitfalls & Anti-patterns.
> Principle: **validation before completeness**; one acceptance gate every 10 days — fail a gate and you fix the loop or cut scope; never set off carrying problems.

---

## 1. Applicability and Goals

**Applies to**:

- You can already state the core gameplay in one sentence: "under what constraints, do which action, get what feedback." If you can't say it in one sentence, get that clear first.
- You can invest 2–4 hours a day for 30 straight days; the goal is a greenlight decision, a competition submission, finding a publisher, or persuading teammates to commit alongside you.
- You know one engine's basics and can scaffold a runnable project yourself.

**Doesn't apply to**:

- Still learning engines and programming basics: start with the Getting Started section's Your First Game, build one complete small project, then come back.
- The idea itself isn't focused yet: first use a one-pager to squeeze the scope down to a size that fits in 30 days.

**Target positioning**: validate that "the core loop is worth investing in," not that the game is finished. When the 30 days are up, the demo must answer three questions:

1. **Is it fun?** Take away the art and audio — will strangers still replay it willingly?
2. **Does it hold up?** Can teaching, challenge and wrap-up chain into one complete 10-minute experience?
3. **Do we commit?** Keep building, adjust and build, or shelve — is there a clear conclusion?

**Demo standard (a complete 10-minute core-loop experience)**:

- Complete from launch to ending: it opens, the core loop runs over and over, and there is a clear ending and a play-again.
- Teaching, challenge, one small climax and a wrap-up all happen within 10 minutes, with no extra documentation needed.
- New players enter the core loop within 5 minutes and complete the run within 10, with no verbal guidance.
- No blocking-severity issues anywhere (crashes, freezes, being stuck with no way out), and the build runs directly on someone else's computer.

> Difference from the Getting Started section's Your First Game: that page trains the shipping skill of "finishing the game"; this page trains the decision skill of "validate first, then commit." The output is a demo for review and playtesting — not a release product.

## 2. Process Overview

Four stages, three acceptance gates, and a close-out review on Day 30. The schedule below assumes 2–4 hours a day; full-time development can compress stage lengths, but never the gates.

| Stage | Output | Duration |
| --- | --- | --- |
| 1. Mechanics prototype | A playable, replayable greybox prototype; a game feel parameter table; toy test notes | Days 1–10 |
| 2. Content skeleton | A content structure table (levels or waves); one complete whitebox run (teaching, challenge, wrap-up) | Days 11–20 |
| 3. Experience polish | Feedback and audio filled in; the full UI set; a playable build with content frozen | Days 21–27 |
| 4. Demo and review | A distributable build; a demo script; playtest notes and feedback forms; a one-page review conclusion | Days 28–30 |

- **Acceptance gates**: on Days 10, 20 and 27, ticking off the criteria item by item; you enter the next stage only through the gate — fail it and you fix the loop or cut scope. The close-out conclusion lands on Day 30.
- **Rhythm**: fix one block of development time every day; each stage produces at least one build that plays the moment it opens; report progress in builds, not in "how much code was written."
- **Red line**: the demo is decision material, not a storefront debut; no stage adds content to "look more finished."

**Scope-cutting order** (when scope runs out of control, cut in this order):

1. Looks and decoration (skins, effect upgrades, non-essential animation)
2. Extra content (additional levels, waves, enemy types)
3. Extra systems (achievements, compendiums, stats pages, collectibles)
4. Peripheral features (multiple save slots, settings options, key rebinding)
5. Run length (tighten from 10 minutes toward 8)
6. Core loop, game feel and teaching content (**do not touch**)

**Scope discipline**: every new addition must cut an equal item; ideas you can't bear to cut go into the "next phase list" for safekeeping — that doesn't count as losing them.

## 3. Step-by-Step Execution

### 3.1 Days 1–10: Mechanics prototype (validate feel and the loop)

Get the core loop running and prove that it "wants to be replayed on its own."

- Days 1–2: write a one-pager (core loop, target experience, not-to-do list); scaffold the project: input, main loop, scene switching, one-click run.
- Days 3–5: implement the core actions and the opposition: player verbs, enemies or obstacles, win/lose conditions; all greybox and placeholder assets, no art.
- Days 6–8: tune feel and pacing; externalize all parameters into one table, so a change takes effect in the running build immediately.
- Days 9–10: toy test — 3–5 people play for 10 minutes each, recording replay willingness and sticking points; do one round of fixes from the feedback, then freeze the core loop.

**Stage gate (Day 10)**:

- With art and audio pulled out, testers still want to replay it, in sessions of 10+ minutes.
- At least 4 of 5 complete one loop within 3 minutes with no verbal guidance; "I pressed it and nothing happened" complaints: no more than one per person.
- All core parameters live in the table; any change's effect can be verified the same day.
- Testers start another run on their own, rather than at your request for one more try.

### 3.2 Days 11–20: Content skeleton (levels, waves, the flow strung together)

Fit the loop into one complete 10-minute main line, mostly whitebox.

- Days 11–13: lay out the content structure table: the level or wave list, each section's new elements and difficulty, and time budgets; build one benchmark level first and time it, then extrapolate the full set by multiplier.
- Days 14–17: mass-produce whitebox content from the table, with difficulty ramping up; string the opening, teaching, challenge, failure-retry and ending into one line.
- Days 18–20: full-run testing (yourself plus 1–2 people), recording total length, sticking points and pacing breaks; settle the demo content list and start converging.

**Stage gate (Day 20)**:

- In the whitebox state, the full loop runs from launch to ending with no freezes and no dead ends.
- New players learn the controls within 5 minutes with no guidance.
- A single run lands in the 8–12 minute range; every section serves a teaching or challenge purpose, with no filler.
- The content structure table matches what is actually built; the table is the auditable basis for scope.

### 3.3 Days 21–27: Experience polish (feedback, audio, UI)

Turn the whitebox into something that "looks like a game" — polish only, no mechanics changes.

- Days 21–22: add feedback item by item — hits, taking hits, scoring, failure, buttons; every action gets a visual or audio response (particles, screen shake, numbers, sound effects).
- Days 23–24: sound effects and music (asset libraries are fine); fill in volume settings and make sure key actions have sound.
- Days 25–26: the full interface set — title, control prompts, pause, results and ending; run one pass of adaptation and performance on target devices.
- Day 27: freeze content and mechanics, bug fixes only; organize one full playtest round, logging every error and experience issue.

**Stage gate (Day 27)**:

- No long dead stretches within the 10 minutes; every action has visible or audible feedback within 0.5 seconds.
- Strangers reach the ending screen on their own and can start another run without explanation.
- Content is frozen: bug fixes only, no new features or content.
- The build runs stably on target devices at the target frame rate.

Any core-mechanics problem you find goes on the list and waits until after the demo; letting the polish stage fight for time with mechanics rework is the most common way a 30-day plan derails.

### 3.4 Days 28–30: Demo and review

Turn the demo into deliverable decision material.

- Day 28: package and distribute (including controls documentation and a known-issues list); write the demo script: how to guide someone through 10 minutes, where to stop, where to talk — without taking over the controls from the player.
- Day 29: review playtest — recruit 5–10 target players; watch, don't teach; record sticking points, completion time, their first words at the end, and willingness to keep playing (1–5).
- Day 30: close-out review: tick through the §4 checklist item by item, answer "did the core loop pass, what does the next phase do, what gets cut," and write it into a one-page conclusion to keep on file.

**Stage gate (Day 30)**:

- Strangers complete the 10-minute loop unaided; the build runs on other people's machines.
- At least 5 feedback forms collected; playtest notes carry raw data on times and sticking points.
- The review conclusion lands clearly on one of three options — "keep investing," "adjust and re-verify," or "shelve" — with the next phase's scope and milestones written out.
- Build, script, notes and conclusion all archived; teammates can review them independently.

## 4. Acceptance Checklist

**Demo standards (a complete 10-minute loop; miss one item and it doesn't pass)**

- Launch to ending is one loop: it opens, the core loop runs over and over, and there is a clear ending and a play again.
- Teaching, challenge, a small climax and a wrap-up within 10 minutes; new players enter the loop within 5 minutes with no guidance.
- No blocking-severity issues anywhere; the build runs directly on other people's computers, with controls documentation.
- At least 5 strangers play it through and leave a willingness-to-continue score and revision notes.

**Stage gates (three checkpoints plus close-out; pass the gate to continue)**

- Day 10: still worth replaying with art and audio removed; all parameters in tables.
- Day 20: the whitebox completes the full 8–12 minute run; the content structure table matches what was built.
- Day 27: feedback and interface complete, content frozen, bug fixes only.
- Day 30: review conclusion on paper, all materials archived.

**Common to every stage**

- A build that plays the moment it opens, not "the code is done."
- Walk the scope statement every week: has anything been added quietly? If so, was an equal item cut?
- Leave a record when you stop: what was done, where it got stuck, what's next — three lines is enough.

## 5. Common Pitfalls

1. **Going straight into mass production**: the idea is barely settled and you're laying out levels, drawing art, writing story. Until the loop is validated, all of it can become sunk cost. For the first 10 days, touch only the core loop, all in placeholder assets.
2. **No stage acceptance**: you move by the calendar, Day 10 arrives and passes by default, and problems roll into the next stage doubled. Tick off all three stage gates item by item; fail one and you fix the loop or cut scope.
3. **The demo keeps growing**: you can't resist adding systems, characters, storylines. A fourth idea doesn't fit in 30 days: every addition must cut an equal item, and whatever doesn't fit goes into the "next phase list."
4. **Continuing with no playtests**: it feels fun to you, so you grind away heads-down for 20 days and show no one until the end is near. The toy test on Days 9–10 and the review playtest on Day 29 are hard checkpoints — 3–5 people and 5–10 people respectively.
5. **Changing mechanics during polish**: after Day 21 you're still redoing feel and the loop, and completed feedback and interface work all needs rework. Content freeze and mechanics freeze take effect together; problems get logged, not fixed.
6. **Treating the demo as the finished product**: holding the demo to release standards and chasing downloads and reviews only leads to endless delays. The demo's deliverable is evidence and a conclusion, not sales.
7. **Missing records**: nothing is written down on the spot during playtests, it gets retold from memory afterward, and the review meeting turns into an exchange of impressions. Fill in forms on the spot, note times and sticking points on the spot, and tidy it up the same day.
8. **No demo script**: at the review you hunt for features and explain gameplay on the fly, burning all your attention on operating the game. Walk the 10-minute guided-play script end to end one day ahead.

## Further Reading

- Game Design Handbook: the methodological source for core loops and toy tests — §3.1 here is its expansion.
- Production Handbook: the formal practice for milestones, scope control and feature-cutting order — Sections 2 and 4 here draw from it.
- AI Workflows: using AI to stand in for placeholder assets, boilerplate code and documentation cleanup, and the boundaries of acceptance and disclosure.
- Pitfalls & Anti-patterns: the full list of kickoff, scope and playtest pitfalls, with severity levels.
- The Getting Started section's Your First Game: the 30-day plan that trains "finishing"; finish that first, then come back to the validation on this page.
- Art & Audio Handbook: the detailed how-to for feedback, sound and interface in §3.3.
