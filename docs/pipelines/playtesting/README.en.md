# Ludo Atlas · Pipelines · Playtesting

> **Pipelines & Workflows**. Positioning: the minimum discipline for replacing "I think" with "I saw" — each round starts from a hypothesis, strangers are observed to capture real behavior, feedback is triaged by evidence, and after fixing you test again.
> Companions: Production Handbook · Game Design Handbook · Live-Ops & Growth · Pitfalls & Anti-patterns.

---

## 1. Positioning and Scope

Insiders' judgment about their own game drifts out of calibration over time: you know what every button does, you remember what every bit of onboarding was meant to achieve, and you've even worked out in advance where players will get stuck. Playtesting is how you bring an outside perspective back in: it doesn't answer "are we doing it right," only "what did the target players actually experience."

One-line definition: **validate a hypothesis written down in advance using the real behavior of real target players.**

Three ground rules, referenced throughout:

1. **Hypothesis before people**: with no question to validate, the round shouldn't start (§3.1).
2. **Watch behavior, don't just listen to opinions**: what players say is cheap, what they do is honest (§3.4, §3.5).
3. **Small and frequent rounds**: 5–8 people per round; fix as soon as testing ends, then test again (§3.6).

What it applies to, and when:

- Before the acceptance review of any milestone (prototype, vertical slice, Alpha, Beta);
- After the core loop first becomes fully playable, and after any major overhaul of mechanics, numbers or onboarding;
- Before a public playtest (a demo, a store event) as a dry run; and whenever an internal argument about a design decision runs past ten minutes with neither side producing evidence.

Drawing the boundary: playtesting doesn't hunt bugs (that's the QA process; see Production Handbook §5), and it doesn't do large-sample data analysis (that's post-launch telemetry work). Its remit is "how people understand it, how they get started, where they get stuck, whether they want to keep playing" — small sample, high depth.

## 2. Toolchain

Principle: the lighter the tools the better — don't build a platform for testing. A pen, a form and a screen recording are enough to start; only move to heavier setups when testing genuinely outgrows them.

| Stage | Common choices | Key points |
| --- | --- | --- |
| Recruiting | Player communities, niche forums, offline meetups, remote sessions | Record profile and contact info; use strangers from the target audience only (§3.2) |
| Informed consent | A one-page explanation plus recording release | State the purpose, privacy boundaries and how to withdraw; confirm before recording |
| Screen recording | Screen-recording software (OBS and the like) plus a microphone | Record every session; name files uniformly "date-version-tester code" |
| Notes | A timecoded note sheet (document or pen and paper) | On-site, record facts only: time, behavior, verbatim quotes |
| Remote testing | Video call plus screen sharing | If the connection is unstable, switch to "recording plus async follow-up" — don't force it |
| Post-session survey | A short survey, mostly open questions | Placed after the interview; rating questions are not the only evidence |
| Build distribution | A separate test build with its version number clearly marked | Isolated from the dev build; record which versions went out, and when |
| Behavioral telemetry | Death points, completion rates, stuck-point counts | Supporting evidence, cross-checked against observation notes; never the sole basis for conclusions |

Notes:

- Fix the note-sheet fields up front: timecode, actions and behavior, verbatim excerpts, event type (stuck / misunderstanding / emotion / question). Stable fields are what make rounds comparable.
- Surveys don't replace observation: surveys capture players' self-perception, observation captures real behavior, and when they conflict, behavior wins (§3.5); telemetry can hint at "where something went wrong" but can't explain "why" — attribution comes from observation and interviews.

## 3. Process and Rules

A complete round runs through six steps, in this order: hypothesis → recruiting → script and tasks → observation notes → triage → fixes and regression (verified next round).

### 3.1 Goals and Hypotheses First

Before testing begins, write a "test card" — no more than one page, with three things:

- **Hypothesis**: we believe [which players] under [what conditions] can / will [do something or feel something].
- **Observation signals**: if the hypothesis holds, what countable or visible behavioral signs should we see.
- **Decision rules**: what results count as pass or fail; and what to change on failure.

Example: "We believe first-time players will discover the dash without any prompt. If it holds, at least half the players in the multiplayer task will use it unprompted; if it doesn't, check the dash's prompt and visual presentation first — not delete the feature."

Discipline:

- At most 2–3 questions per round, sorted by "the hypothesis most likely to kill the project" — validate the most expensive, most uncertain one first.
- "Let's see how people react" and "is it fun" are not hypotheses. If you can't write down observable signs, the question isn't thought through yet.
- The round type determines the script: concept rounds (does the idea make sense), usability rounds (can players get started on their own), balance rounds (are the difficulty curve and numbers reasonable), experience rounds (does the emotional pacing land). Different types call for different participant counts and task designs.

### 3.2 Who to Test: Strangers First

One-line rule: **strangers from the target audience > general players > friends**. The reason is methodological, not about politeness:

| Dimension | Friends | Strangers |
| --- | --- | --- |
| Know the answer you want | Play along and say nice things | React only to the game itself |
| Design-information contamination | Have heard your pitch, played earlier versions | Start from zero, equivalent to a new player |
| Behavior when stuck | Push through, help you find excuses | Quit or complain the way they actually would |
| Feedback value | High emotional value, low decision value | Usable as decision evidence |

- 5–8 people per round. Problems of a kind repeat heavily in small samples: what the first few people expose is usually what the rest would too. The count isn't the point — "all of them are strangers from the target audience" is.
- Screen the profile at recruiting time: do they play this genre, how many hours a week, how familiar are they with this kind of control. Test a casual-leaning game with hardcore players and the stuck-point list fills up with mismatched problems.
- Keep it fresh: the same tester stops being a "new player" from the second round on. For milestone-level validation, rotate people each round where possible; when you must reuse someone, separate the versions and time slots, and note it.
- Friends aren't entirely unusable: during a resource-strapped prototype phase you can use them, but be clear this is "downgraded evidence" — it can raise problems, never declare a pass. Before milestone acceptance and public playtests, the conclusions must come from strangers.

### 3.3 Task Design and Questioning Taboos

Task design has a single guiding principle: **give goals, not steps.**

- Give a situation and a goal: "find a way to reach the platform across the gap," "level your character to 3," "find the exit."
- No control hints: "press A to double-jump," "click here first" steal away the very process of the player figuring things out — and with it, what this round exists to observe.
- Three to five tasks, covering the core loop; 5–10 minutes each; open with 2–3 minutes of free exploration so players build their own intuition.
- A fixed three-line opening script: we're testing the game, not you; don't worry about looking bad when it gets hard; please say out loud what you're thinking.

Questioning and moderating taboos:

- Don't ask "is it fun," "is it hard," "do you like it": social politeness will answer for them.
- No leading questions: "was the prompt hard to notice?" writes the answer into the question, and players just agree.
- Don't help the moment they get stuck: being stuck is the data. Allow plenty of silence; only when they're truly dead in the water do you intervene with the smallest possible hint — and log the hint level and time (§3.4).
- No hypothetical questions: "what would you do if we added feature X" harvests wishes; ask about real behavior and memory instead: "what were you trying to do at that step?"
- When players ask questions, log the question without answering it; turn "what players asked" into a tutorial-gap list.

### 3.4 Observation and Notes

The single rule of note-taking: **record facts, not impressions**. The moderator's impressions wait for the triage stage; on-site, you collect only four kinds of facts:

- **Stuck points**: pauses over 30 seconds, repeated failure at the same spot, backtracking loops, a visible slowdown in actions.
- **Misunderstanding points**: taking A for B, hunting for a nonexistent feature, misreading UI information; follow up afterwards with "what did you think this was at the time?"
- **Emotional points**: laughter, sighing, cursing, leaning forward, putting the controller down. Emotion is experience data in its rawest form.
- **Question points**: every question a player asks unprompted marks something the game failed to explain.

Intervention rules: by default, don't help, don't rescue, don't explain. When they're dead in the water (roughly 2–3 minutes with no progress), give the smallest hint and log the hint level and the time; any segment that needed a hint gets down-weighted in analysis.

Roles and practice:

- Two people is the ideal setup: the moderator runs the session and the interview, the note-taker watches only behavior and timecodes — no crossing roles.
- For solo testing, secure a complete recording first, move the interview to after the review, and fill in timecoded notes while reviewing.
- Pair the interview with playback: have players narrate what they were thinking while watching the recording; memory plus footage is testimony of far higher quality than recall in the dark.
- Write up the round's notes within 24–48 hours: memory beautifies itself automatically, and loses details automatically too.

### 3.5 Feedback Triage: Separate Opinions from Behavior

A session yields four kinds of input, each handled completely differently — sort first, discuss second:

| Input | Nature | Handling |
| --- | --- | --- |
| Behavioral evidence (stuck points, misunderstandings, quit points) | The hardest kind; can support decisions directly | When several people repeat it, it enters the fix list |
| Player opinions and suggestions | The problem is often real, the proposed solution often wrong | Dig into the intent behind it; rarely adopt the solution as-is |
| Technical defects (crashes, errors, display glitches) | An engineering problem | Move to the bug list, triaged by severity |
| Praise and pleasantries | Emotional value | Not evidence; just say thanks |

Triage rules:

- Look for repetition first: it takes 2–3 target players stuck at the same point before the design itself is fair game; a single person's one-off stuck point is logged first, to see whether later rounds reproduce it.
- Changing "information and onboarding" beats changing "difficulty": much of what gets called too hard is really not understanding what to do. Add prompts, improve feedback, adjust the camera — then touch the numbers.
- Mine suggestions for needs: when a player says "add auto-pathing," the need behind it is usually "I got lost" or "walking is boring." Solve the latter; don't copy the former.
- Suggestions that clash with the core fantasy don't get adopted right away, but do check whether "the player didn't understand your intent"; if it's a communication problem, fix the communication, not the fantasy.
- Every piece of feedback gets a disposition: change / don't change / watch, with the reasoning written down. Collecting a pile and handling none is testing for nothing — and it burns through your testers' goodwill (see §5, item 3).

### 3.6 Iteration Cadence: Small Rounds, Fast Regression

The cadence formula: **one round of 5–8 people → triage → fix list → freeze a new build → next round**; intervals run 2–4 weeks or one milestone, following the release cadence, not your mood.

- The fix list is capped at 5–7 items per round, ordered by impact; change too much and you lose the ability to attribute results — and you won't finish anyway.
- Build discipline and regression: freeze the build and tag it with a version number each round — changing while testing voids the conclusions; last round's fixes are listed as "must-check items" next round and regression-verified by new players; an unverified fix is not a finished fix.
- Stop condition: new strangers stop producing new high-frequency stuck points on the core tasks, and the milestone acceptance criteria are met. The stop signal is not "nobody has feedback" — someone always has feedback.
- Leave a one-page report per round: what was tested, what was seen, what was changed, what gets verified next round. Accumulated over rounds, it is the project's decision log.

## 4. Automation and Acceptance

Playtesting is inherently human work — there is no such thing as full automation; but templates, notes, aggregation and regression can be semi-automated, saving the moderator's energy for observation and follow-up questions.

| Stage | What can be semi-automated | Notes |
| --- | --- | --- |
| Templates | Fixed test-card, note-sheet, survey and report templates | Copy and use; fields stay uniform, rounds stay comparable |
| Archiving | Uniform naming for recordings and notes, archived by round | Name by "date-version-tester" and it takes no extra effort |
| Metrics aggregation | Task completion rate, time to first success, stuck-point count, hint count | Aggregated from the note sheets into one table at the end of each round |
| Behavioral data | Death heatmaps, completion rates, drop-off-point statistics | Cross-checked against observation notes; hints at where, not why |
| Regression | Last round's fix list becomes next round's must-check items | Fixes and verification always travel in pairs |

End-of-round self-check:

- [ ] The test card was written before testing began, with hypothesis, observation signals and decision rules all in place;
- [ ] At least 5 participants, all strangers from the target audience (zero friends, or flagged as downgraded), with a complete recording and timecoded notes for every session;
- [ ] The moderation involved no teaching, no explaining, no leading (verifiable by spot-checking the recordings);
- [ ] Triage finished within 48 hours, every piece of feedback dispositioned change / don't change / watch; the fix list completed and regression-verified by new players in the next round;
- [ ] This round's report written down: what was seen, what was changed, what gets verified next round.

Acceptance reference lines are fixed in the test card in advance — for example, "the share of new players who complete the first core task with no hints," "average stuck-point count," "the share who want to keep playing at the end." The numbers vary by genre; the discipline is one and the same: set the line first, then read the score — no deciding after the fact.

## 5. Common Pitfalls

1. **Testing only with friends**: praise from friends is not data. Friend-circle testing can raise problems but never declare a pass; milestone validation requires strangers.
2. **Explaining instead of observing**: the moderator can't resist teaching controls, explaining design intent, defending the game. The moment you explain, the stuck point disappears — and the round's most valuable information disappears with it.
3. **Collecting a pile and handling none**: surveys and notes go in a drawer and the next round repeats itself. Every round needs a fix list and regression verification, or testing is just ritual.
4. **Testing without a hypothesis**: "let's see how people react" leaves only impressions and kind words, supporting no decision. Write the test card first (§3.1).
5. **Leading questions**: "is it too hard" elicits politeness; "where does it feel hard" elicits information; take the player's answer as it comes — don't write the answer for them.
6. **Testing on an unfrozen build**: changing while testing means participants may not be playing the same version; the data is incomparable and the conclusions unusable.
7. **Testing the wrong crowd**: validating a casual experience with hardcore players, or standing industry professionals in for ordinary players. Check profiles before recruiting.
8. **Mistaking players' solutions for needs**: copying "add auto-pathing" without solving the "getting lost" itself. Mine the need, don't copy the solution.
9. **Testing only the opening**: every round starts from the beginner stage, and the mid- and late-game are never seen by a stranger; rotate the tested segment by hypothesis, and test the most expensive hypothesis first.
10. **An audience effect**: a roomful of people staring at the screen makes testers perform or tense up, and their behavior distorts across the board; clear the room except the moderator and note-taker, and for remote tests keep only essential personnel.

## Further Reading

- Production Handbook: the tiered testing-and-QA framework in §5 (self-test → internal cross-testing → targeted external → public demo); this page expands the "targeted external" tier in full.
- Game Design Handbook: validation methods and the source material for the "toy test" — how test goals grow out of design questions.
- Live-Ops & Growth: public demos, store events and wishlist cadence — the next tier, where playtesting scales from small samples to large ones.
- Pitfalls & Anti-patterns: the full list, with cost tiers, of pitfalls like "building behind closed doors" and "listening only to the people around you" — check against it at kickoff and milestone reviews.
- Template reference: the test card, note sheet and triage checklist can be built from the fields in §3 of this page; one page is best; good enough is all it needs to be.
