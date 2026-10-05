# Ludo Atlas · Genre Handbooks · Educational

> **Genre Handbooks · Volume 4**. Positioning: the genre that writes "players actually learn something" into its acceptance criteria. It owes two debts at once: the gameplay must be fun enough that someone is willing to play it, and the learning must be effective enough to show evidence; this page covers dual-objective design, knowledge embedding, learning-outcome assessment, age tiers and classroom scenarios, plus adjacent serious-game territory such as vocational training and medical rehabilitation.
> Companions: Game Design Handbook (core loop and feedback design) · Production Handbook (content volume and scheduling estimates) · Case Studies (breakdowns of comparable products) · Pitfalls & Anti-patterns (child data and compliance pitfalls).
> No external links here; the benchmark list covers only widely known titles, and all figures are typical orders of magnitude — once something lands in a project, go by what you measure.

---

## 1. Positioning and Core Loop

In one sentence: an educational game is **the genre that makes "players learn something" a product promise**. Its difference from an ordinary game is not subject matter but acceptance: an ordinary game only has to be fun, while an educational game also has to show evidence that "the player learned." Neither debt is optional: fun decides who shows up, effectiveness decides who stays and buys again. An ordinary game's loop passes through and is gone; an educational game's loop must leave traces: each round has to leave a change in the player's ability, plus one observable piece of learning evidence (§3.3) — that is the engineering watershed between the two.

The core loop, written as a chain of verbs:

`Meet new knowledge (introduced in context) → Use it once in gameplay → Get feedback and explanation → Correct and try again → Mastery rises, difficulty or scenario steps up`

Boundaries against adjacent genres:

| Adjacent genre | Boundary |
| --- | --- |
| Trivia & quiz | A quiz measures the existing stock of "do you know it" and ends when the answering ends; an educational game manages the gain from "doesn't know" to "knows", and must carry teaching and error correction |
| Gamified apps | Gamification wraps an existing process in a reward shell (points, badges, streaks) without touching the process itself; an educational game rebuilds the learning task as the core action |
| Courseware and online courses | Courseware is accepted on "finished explaining"; an educational game is accepted on "knows it after playing", and owes an extra debt of fun and motivation |
| Ordinary games (any gameplay vehicle) | The gameplay can be identical; the difference is goals and evidence — an educational game designs for "still knows it afterwards", and will trade away some thrill for transfer |

One self-check question: write down, in one sentence, "what players learn after playing, and what proves it." Only when you can write both is it an educational game; if you can't, or can only manage "raised interest", don't start yet.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **The moment of learning**: the progress from not-knowing to knowing is perceived by players themselves — the first-hand experience unique to this genre.
2. **Fun that stands on its own**: strip away the learning wrapper and the gameplay still holds up; players come back to play, not to hand in homework.
3. **Safe trial and error**: wrong answers bring no shame and no public punishment; mistakes are part of the learning path, and retries are counted in seconds.
4. **Visible progress**: what has been learned, how far mastery has come, and what the next goal is — all visible at any time.
5. **Learning that transfers**: practice ties to real scenarios, and what is learned still works outside the game (transfer, §3.3).

Benchmark titles (widely known; play them yourself before breaking them down). Any one of these negative feelings is a red flag: a test-like feel, rewards holding the learning hostage, difficulty mismatch, learning with no evidence.

| Title | What to learn from it |
| --- | --- |
| Duolingo | The benchmark for gamified practice: courses cut into short levels where practice itself is the gameplay; streaks, leaderboards and daily goals add a habit shell on top — both layers done properly |
| Minecraft: Education Edition | The sandbox-vehicle route: building and collaborating are themselves the learning tasks, while the teacher console assigns tasks, watches progress and runs the classroom |
| The Oregon Trail | The grandfather of educational games: history, geography and resource decisions embedded in one westward-journey simulation — even failure teaches a real situation |
| Carmen Sandiego (series) | Geography hidden inside a pursuit game: the clues are themselves the knowledge to be learned, and the detective structure naturally fits "learning by verification" |
| Early-literacy and number-sense apps (the iHuman Chinese kind) | The benchmark for the preschool tier: one small concept per level, daily tasks and parent reports — the three staples; voice-first, no fail states |

## 3. Design Essentials

### 3.1 Dual-Objective Design: Two Acceptance Checklists

An educational game has two objectives from kickoff; write one checklist for each — missing one makes half a product:

| Objective | How to write it (counter-example → good example) | How it is accepted |
| --- | --- | --- |
| Learning objective | "Raise interest in math" → "Can independently complete two-digit addition with carrying, 8 of 10 correct" | Pre/post-tests and delayed retests (§3.3) |
| Gameplay objective | "Edutainment" → "With the learning content stripped out, blind-test players still play three rounds in a row by choice" | Unprompted blind-test observation |

- Write the learning objective to the point of "acceptable": what is learned (the smallest knowledge unit), to what degree (recognize, state, apply, and apply in a new scenario — four tiers), and what proves it (the test and the data definitions). Any module that can't fit these three cells doesn't get scheduled.
- Mastery advances through four tiers: recognize, state, apply, transfer. Most products actually stop at tier two while their marketing talks in tier-four terms — a high-incidence zone for reputation accidents.
- One module carries only one or two learning objectives: the more concepts, the higher the cognitive load, and the more the gameplay feels like rushing through a schedule.
- When the two objectives conflict, protect the gameplay experience first, then split the concepts smaller or change the embedding method (§3.2); force-fed knowledge is neither fun nor memorable. At kickoff, write each objective as one sentence and show it to a layperson — it passes only if they can repeat it back.

### 3.2 Knowledge Embedding: Learning-as-Gameplay vs. Reward Wrapping

- **Learning-as-gameplay**: the core mechanic is itself the act of using the knowledge (instructions in a programming puzzle are programming; the ledger in a management sim is economics). To finish the game the player cannot route around actually mastering it — learning and play are the same action. The most solid results, and the hardest to build.
- **Reward wrapping**: gameplay and knowledge are separate — correct answers buy stars, coins and cosmetics; knowledge is the level ticket and gameplay is the reward. Low cost, fast results, suited to young ages and habit-building — but players see through the trick easily, leave as soon as the learning is done, and the ceiling on effect is low.

| Diagnostic question | Learning-as-gameplay | Reward wrapping |
| --- | --- | --- |
| Replace the knowledge with meaningless symbols — does the gameplay still work? | No (the knowledge is core) | Yes (the knowledge is a shell) |
| Can players win by bypassing the learning? | No | Yes, if the rewards are designed cleverly |
| Main risk | Built shallow, it's an ordinary game with a label | Built hollow, it's a reskinned quiz bank |

- Embedding points are not limited to "answering questions": input (the action itself calls on the knowledge), rules (constraints decided by the knowledge), goals (the clear condition is the application), feedback (error explanations carry the concept), generation (questions and levels generated from the knowledge system). With a limited budget, prioritize goals and feedback.
- The choice rests on three things: target age, knowledge type (factual recall or procedural skill), and whether the team has a subject-matter expert. Without one, stay away from the learning-as-gameplay route for now.

### 3.3 Learning-Outcome Assessment and Data

What to measure: a three-layer funnel, from process to outcome.

| Layer | Example metrics | Question it answers | Collection method |
| --- | --- | --- | --- |
| Engagement | Retention, session length, level pass rate | Will players play it? | In-game event tracking |
| Immediate learning | Accuracy, hint usage, distribution of error types, mastery change | Did learning happen along the way? | Event tracking plus pre/post-tests |
| Transfer and retention | Delayed retest scores, accuracy on unseen problems of the same type, real-scenario use | Can they apply it, and does it stick? | Transfer tasks and post-test follow-up |

How to measure it (a checklist you can copy straight into your kickoff):

- Pre-test and post-test: run the same problem set again at least a day apart; use a control group (play vs. no play, old vs. new version — in schools, often split by class). Without a control, score changes can't be attributed; a single test measures "remembered on the spot", not learning.
- In-game event tracking: accuracy, stuck points, hint dependence, quit points, session length; define the "mastery" threshold first (e.g., 90% correct on two rounds in a row), then build the tracking.
- Transfer tasks: new problems of the same type that were never taught, or use in a different scenario; this is the only test that separates "learned" from "memorized".
- Data discipline: report process metrics (length, retention) and outcome metrics (score change) separately — never tell the two sets of numbers as one story; handle children's data under data minimization and parental consent (details in Pitfalls & Anti-patterns).

### 3.4 Age Tiers and Classroom Scenarios

The usual three age tiers (boundaries follow your actual target users):

| Tier | Design focus | Interaction and copy | Session length |
| --- | --- | --- | --- |
| Preschool (roughly 3–6) | Senses and habits: big buttons, voice first, no fail states | Little text, more voice; get it right before getting fast | Under 10 minutes per session |
| Primary school (roughly 6–12) | Rules and competition: clear goals, reward systems, light social features | Short sentences, image and text side by side, answers can be changed | 15–20 minutes per session |
| Middle school and up (roughly 12+) | Systems and autonomy: simulations, sandboxes, project tasks | Can read long text; encouraged to set their own goals | 30 minutes and up |

- Age-tier differences are product structure, not a reskin: text volume, failure penalties and social exposure all scale up with age; the youngest tier gets no public leaderboards and no losing situations; a product spanning tiers shares systems but separates pacing and onboarding — estimate the work as two products.

Classroom scenarios (essentially a different product from the home version):

- Class-period constraints: a lesson runs 40–45 minutes, and the product must be cuttable into one complete segment (a few minutes of introduction, ten-odd minutes of practice, a few minutes of summary) — pausable, savable and resumable at any moment.
- Device reality: computer labs, tablet carts, student-owned devices, one big screen; unstable networks are the norm, and offline play is a common hard requirement; download resources in per-unit packages so the whole class isn't waiting on a progress bar together before class.
- Account discipline: batch account creation and resets, class-code or picture-code sign-in, profile switching for several students sharing one device; a product whose login eats the first ten minutes of class will not get a second lesson.
- Teacher tool checklist (needed in version one): class and roster management, task assignment, progress board (who is stuck where), commonly-missed problem summaries, cast-to-screen demo mode, content allowlist (store and chat switched off); the usability bar: assign a task within five minutes without reading a manual, and walk out of one lesson with a presentable summary (completion rate and commonly-missed problems).

### 3.5 Adjacent Serious-Game Applications

Serious games are games whose primary purpose is not entertainment, and educational games are one branch of the family; the same family includes vocational training, medical rehabilitation, science outreach and emergency drills. The gameplay and engineering foundations carry over; the difference is the acceptance criteria: education looks at scores and transfer, training at operation pass rates and error rates, medical work at clinical indicators.

**Vocational training**

- Pilot and flight-crew training leans heavily on full-flight simulators — simulators are this industry's home turf; driving, heavy machinery, power and chemical emergency drills, surgical and endoscopic simulation all have mature forms.
- Fidelity is allocated by training objective: sensors and control consoles tied to assessment get full treatment while scenery can be cut; every operation is logged, generating assessment reports tied to job qualification.
- Expensive mistakes are allowed: messing up in simulation costs far less than in reality — simulation training's hardest selling point.

**Medical rehabilitation**

- Repetition and monotony are the backdrop of rehabilitation training, and gamification solves the motivation problem of "being willing to practice"; common forms include post-stroke hand and gait training, cognitive and attention training, and VR exposure therapy.
- The attention-training direction already has a prescription-grade precedent: EndeavorRx is regulator-approved in the United States for children aged 8–17; products that make therapeutic claims may be regulated as medical devices — clarify the pathway before kickoff.

**Shared discipline**

- Set acceptance metrics before gameplay: training starts by asking "what gets assessed, what counts as passing", rehabilitation by asking "which indicator can be quantified"; if you can't write the metric, the project doesn't start.
- Professionals take part throughout: subject experts, instructors and clinicians are both the requirements side and the acceptance side; the dev team cannot define "effective" on its own.
- For small teams, the entry point is a vertical scenario with an institutional partner (schools, training providers, hospitals), delivering to the client's acceptance criteria; build one closed loop first, then talk platforms.

## 4. Technical Essentials

The engineering difficulty concentrates in three blocks: the content pipeline, learning data, and classroom infrastructure. The following is engine-agnostic; educational games carry no game-feel technical risks — the risks are all "can content be changed, can data be measured accurately, will it work in a classroom".

**Content pipeline (subject experts must be able to edit content directly)**

- Concepts, problems, level scripts and difficulty tags all become data (spreadsheets or JSON; methods in the Game Design Handbook), with code only reading the tables; content goes into version control, edits are traceable and rollbackable, and review records travel with the content.
- A parameterized problem generator: templates plus random values produce variants of the same concept, with question text and answer computed from one source, plus a validator guaranteeing answers are unique, solvable and unambiguous; every variant runs through automated checks before entering the bank.
- Multiple grade tiers and languages reuse one content structure: prompt, options, explanation and audio all separated, with the glossary established first.

**Learning data and assessment**

- Event tracking goes in early in development: answers, hints, error types, retries, session start and end; define the "mastery" criteria before instrumenting, or the data that comes back proves nothing.
- A mastery model: concepts organized as a graph (with prerequisite relations), mastery maintained by rolling statistics or probabilistic estimation, driving unlocks and teacher reports; review is scheduled by spaced repetition — long-term retention comes from the system, not from expecting players to come back on their own.
- Local-first data pipeline: school networks are unstable, so events are batched locally and uploaded on reconnect — a whole lesson must run offline; learning data is authorized in tiers by person and by class (compliance in Pitfalls & Anti-patterns).

**Classroom infrastructure**

- Accounts: batch import and reset, class-code or picture-code sign-in, profile switching and fast restart on shared devices.
- Teacher back office: task assignment, progress board, error distribution, cast-to-screen demo, feature allowlist; resources packaged per unit with pre-class preload; how complete this back office is directly decides repeat purchases.
- Accessibility: read-aloud voice, colorblind-friendly palettes, subtitles, screen-reader compatibility; both a compliance requirement and a functional need for young and special-education scenarios.

## 5. Content Volume and Workload Reference

The following are common magnitudes for comparable projects, for scope estimation — not a commitment.

| Project form | Content volume | Timeline | Notes |
| --- | --- | --- | --- |
| Gameplay prototype | 1 knowledge unit, a dozen-odd exercises | 2–4 weeks | Validates only the embedding method and the pre/post-test tools; no accounts or back office |
| Small complete title | 1 subject or skill, 1 grade tier | 3–6 months | The common starting point for small teams, including a complete teacher or parent report |
| Classroom product | One semester of content (cut into 30–60 lesson segments) plus a teacher back office | 6–12 months | The back office, accounts and device compatibility are hidden work |
| Platform product | Multiple grade tiers and subjects, hundreds of hours of content | 1–3 years for a team | Content is a monthly bill: production line, review and updates are long-term costs |

- The biggest cost is often not programming: concept breakdown, problems and level scripts, and subject review together often equal or exceed it; time "one knowledge unit" first, then multiply by the unit count.
- Unit-cost magnitudes: a teaching-and-practice level set for one knowledge unit, 3–10 days (including review); a core teacher back office, 2–6 weeks; reserve 10%–20% of the total budget for the pre/post-test kit and one round of data analysis.
- Schedule the two rhythms separately: gameplay iterates weekly, learning outcomes are measured monthly (delayed retests required); put outcome validation into the schedule, or the project stalls at "launched and done".

## 6. How to Start the First Prototype

The first prototype validates exactly one thing: whether the knowledge-embedding method holds up. Finish it in 2–4 weeks; touch no final art, accounts or back office.

1. **Pick one smallest knowledge unit**: the kind that can be learned in ten-odd minutes and measured with ten problems; write the learning objective and the acceptance evidence as one sentence each.
2. **Build the gameplay core with the knowledge stripped out**: swap the content for neutral symbols (color blocks, letters) and make the gameplay itself hold up first; if the gameplay doesn't stand, putting the knowledge back won't save it.
3. **Put the knowledge back into the core action**: choose the embedding method per §3.2; on the learning-as-gameplay route, put the knowledge into one of input, goals or feedback — do one spot first, don't overreach.
4. **Build a pre/post-test set**: ten problems as pre-test, fifteen minutes of play, immediate post-test, delayed retest a day later; plus two transfer problems that were never taught.
5. **Run a blind test with 6–10 target users and write a one-page conclusion**: no hints, no explanations; record their willingness to keep playing on their own, the immediate accuracy change, and what survives the delayed retest; write down testers' verbatim words as they "state the concept in their own words" — that is the hardest evidence in the conclusion.

Success criteria (all observable):

- Testers ask for another round on their own, rather than being asked to play again.
- Post-test accuracy beats the pre-test, and the delayed retest still beats the pre-test.
- At least three of ten people can restate the core concept in their own words.

## 7. Common Pitfalls

1. **Dual objectives with no acceptance**: goals like "raise interest" or "edutainment" can't be accepted, leaving only vibes; write each objective as one measurable sentence (§3.1).
2. **Force-fed knowledge**: gameplay and knowledge as two separate layers — players have fun but learn nothing, or answering feels like detention; go back to §3.2 and pick an embedding method — protect gameplay first, then split the knowledge.
3. **Passing off time-on-device as outcomes**: "plays 30 minutes a day" is a process metric, not evidence of learning; report the two sets of numbers separately (§3.3).
4. **Testing only immediate recall**: no delayed retention or transfer means good-looking but untrustworthy data; a next-day retest is the floor (§3.3).
5. **Mismatched age tiers**: one set of text, penalties and social design for everything; age differences are a structural problem, not a reskin (§3.4).
6. **Missing teacher tools**: if a teacher can't get productive within five minutes or get a lesson summary, the product never reaches lesson two (§3.4).
7. **No budget for outcome validation**: school partnerships, pre/post-tests and data analysis have no people or hours, and in the end there is no evidence to tell; put this budget line into the kickoff (§5).
8. **Crossing compliance lines**: children's data, therapeutic claims, content licensing — clarify the regulatory pathway before kickoff (§3.5, §4).
9. **Disconnected from the curriculum**: content doesn't line up with the school's teaching schedule, so teachers can't fit it into the timetable; align on one usable curriculum list before talking volume.

## Further Reading

- Game Design Handbook: core loops, feedback and difficulty curves — the source material for sections 1 and 2.
- Production Handbook: content-volume estimation and scope control; use alongside section 5.
- Case Studies: methods for breaking down comparable products; consult when validating the dual-objective design.
- Pitfalls & Anti-patterns: children's data, content licensing and compliance pitfalls; consult at kickoff and in postmortems.
- The Trivia & Quiz page in the Genre Handbooks (Volume 3): question-bank engineering, draw fairness and difficulty calibration; cross-reads with §3.2 and §3.3.
- Exercise: for a learning app you know well, write the two acceptance checklists (a learning objective and a gameplay objective, each with an extra "what proves it" column), then write three embedding ideas for the same concept (one each in input, goals and feedback) and pick one for a two-week greybox.

In the end, an educational game tests only two things: whether players really learned, and whether they are willing to come back for the next lesson on their own.
