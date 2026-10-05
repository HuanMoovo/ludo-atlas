# Ludo Atlas · Genre Handbooks · Trivia / Quiz

> **Genre Handbooks · Volume 3**. Positioning: the genre that makes "I know this" its first pleasure. Knowledge is the ammunition, questions are the stage; players come for the confirmation of a right answer, and stay for "almost had it".
> Companions: Game Design Handbook (core loops and difficulty curves) · Programming Handbook (question-bank pipelines and draw services) · Live-Ops & Growth (timely content and long-term maintenance) · Case Studies (show formats and product breakdowns).
> This page carries no external links; benchmarks use widely known show and party formats only, and the figures are common magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: trivia / quiz is the genre **that makes "knowledge verified" its first pleasure**. Players find confirmation between "I think I know this" and "I actually got it right"; a question is the smallest playable unit of knowledge, the question bank is the content proper, and rules, scoring and staging are only the shell around the bank.

The core loop, written as a verb chain:

`read the question → search memory (or reason it out) → answer or buzz in → adjudicate → score and feedback → next question`

This loop is measured in seconds: a fast buzz-in question runs around ten seconds, a slow thinking question thirty seconds or more. It holds on just two preconditions: questions are fair (a single verifiable answer, §3.1); and a wrong answer still pays off (a new fact learned or a laugh, §2). The loop at three scales:

| Scale | Loop | What the player gets |
| --- | --- | --- |
| One question (5–30 seconds) | Read the question → answer → adjudicate | One immediate knowledge check |
| One match (10–30 minutes) | Dozens of questions plus scoring or elimination | A knowledge contest, or a stretch of time to chat together |
| One season (weeks to months) | New questions enter, old ones rotate out, divisions advance | A steady supply of "a fresh batch just dropped" |

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Puzzle | A puzzle's answer is derived by reasoning from the rules; a trivia answer is retrieved from memory, and the test is whether you know it |
| Party game | Trivia often borrows party formats (shared screen, phone rooms, a host); the difference is whether the question bank is the substance or a prop — the laugh of answering is only one layer of a party's shell |
| Social deduction | In social deduction the answer moves between players and there is no guaranteed truth; a trivia answer sits in the question bank and the system rules on right and wrong |
| Text adventure | Input in a text adventure advances the narrative; input in trivia only cashes out into score and feedback, and does not change the world |

A self-check question: swap every question for a random arithmetic problem — does the game still hold? If it stops holding, what you are making is trivia; if it still holds with arithmetic, you are making arithmetic practice, and knowledge is only a coat of paint.

Team framing: content-driven gameplay with a low engineering bar; the cost sits almost entirely in the question bank and review; the scarce capability is people who can keep producing good questions and are willing to do fact-checking and timely maintenance. One-line conclusion: trivia / quiz does not sell rules, it sells the density and freshness of the question bank.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **The moment you know**: getting it right is the pleasure of being confirmed. The observation point for acceptance is whether a player says "I knew that" rather than "I guessed" after a correct answer.
2. **Fairness**: questions are solvable, answers are unique, nothing is disputed; a miss is blamed on your own memory, not on a stale or obscure question.
3. **Everyone has a question to answer**: difficulty is tiered — common-knowledge questions give everyone footing, hard questions give the knowledgeable their spotlight; one or two questions that silence the whole room per match are an easter egg, three in a row is an incident.
4. **A wrong answer still pays off**: the reveal adds a new fact or a laugh; wrong-answer feedback is content in itself.
5. **One more round**: scores stay close, new questions come in, the next round can start any time; the bar between matches must be low enough that no resolve is required.

Negative feelings (any one of them is a red flag): humiliated (nobody in the room knows the question, and losing feels like not being part of it); cheated (disputed answers, unclear rules); left waiting (others are answering while you sit idle); railroaded (repeated questions, consecutive questions on the same fact).

Benchmark titles (all widely known show and party formats; play or watch several full rounds before breaking them down):

| Title or format | What to learn from it |
| --- | --- |
| TV quiz show format | Every question is a small drama: the order of lock-in, lifelines, elimination and reveal is a ready-made emotional curve |
| Reward-ladder quiz show format | The ladder is the difficulty curve; at one moment of uncertainty the player chooses whether to push on or walk away, carrying the risk themselves |
| Charades-style party quiz | The answer moves from "say it" to "act it out or describe it"; the expression constraint is itself the gameplay and the punchline |
| General-knowledge quiz board game | Questions hang off progress: answering is the pathway, while jostling for position, blocking and comebacks are the real narrative |
| Friends'-room phone buzz-in | A room code plus a short match turns trivia into social content anyone can start and pull friends into on a whim |

## 3. Design Essentials

### 3.1 Question-Bank Engineering: Categories, Difficulty and Time-Sensitive Questions

The question bank is the substance, so settle its structure before arguing about volume. One record per question; freeze the fields in the first week of work:

| Field | Contents | Use |
| --- | --- | --- |
| Prompt | A one-sentence question, with no ambiguous phrasing | Everything the player sees |
| Correct answer and aliases | The unique answer plus acceptable spellings | Adjudication tolerance (abbreviations, typos, transcribed spoken answers) |
| Distractors | Two to three credible wrong options | The foundation of multiple-choice; quality decides difficulty |
| Category tags | A two- or three-level domain tree; one question can carry several tags | Draw weighting and content health checks |
| Difficulty | An initial estimate plus calibration against accuracy | The match's difficulty curve |
| Source basis | The verifiable basis written down when the question is authored | Review and dispute arbitration |
| Time sensitivity | Evergreen or time-sensitive; time-sensitive questions mark their expiry point | Automatic retirement or rewrite on expiry |

- Categories are the index for drawing questions and the stethoscope for a content health check: if 80% of a bank sits in one domain, the papers it draws will look bad — audit the category shares before launch.
- Difficulty is not decided by the author but calibrated with data: the trio of accuracy, answer time and skip rate. A question only discriminates if its accuracy sits between 30% and 70%; questions above 90% are warm-ups; questions below 20% are fit only as easter eggs — and check first whether the question itself is broken.
- Lay out the difficulty curve per match: the opening two questions must be ones the whole room knows, the middle alternates high and low, and the endgame holds the hardest questions plus easter-egg questions where a wrong answer costs no points.
- Keep time-sensitive questions in a separate, tagged set: questions about years, champions, new films or new versions mark their expiry point and are automatically retired or rewritten into evergreen versions on expiry. A common evergreen-to-time-sensitive mix is 8:2; an all-evergreen bank goes stale, and an all-time-sensitive bank is unmaintainable.
- A verifiable answer is the entry threshold for the bank: write down the source basis while authoring; a question whose basis cannot be written down does not enter the bank. This applies to AI-authored questions too (§3.6).

### 3.2 Question Draw: Fairness and Repetition Control

The goal of the question drawer is not "random", it is "fair in appearance and fair in fact". Three principles: even (categories and difficulties appear by weight), no near-duplicates (the same fact is tested only once per match), and auditable (which questions a match drew, and why those, can be replayed).

- Start with weighted rotation: one weight per category, drawing in weighted rotation, with a forced pool switch after two consecutive questions from the same category. Simple rules are easy to maintain and easy to explain to players.
- Repetition control in three tiers: a per-player recency list degrades through "unseen first, not seen for a while, anything"; inside one match, take the union of all players' seen sets so that nobody at the table has just answered the exact same question.
- Difficulty quotas: draw per match against the difficulty curve's quotas rather than pure random; for strongly competitive modes such as ranked or ladder runs, enumerate the quotas first and then fill them.
- Decide the pool-exhaustion strategy up front: loosen the repetition tolerance, prompt maintainers to add questions, or switch to a limited mode. Decide it late and players will beat you to saying "this one again".
- Self-check method: replay one day's match logs at random and look for repeated facts, category imbalance, and questions nobody answered correctly.

### 3.3 Answer Interaction: Formats and Adjudication Tolerance

The mainstream answer formats each have their own temperament:

| Format | Player action | Strengths | Risks |
| --- | --- | --- | --- |
| Multiple choice | Pick one of four | Cheapest, most tolerant, guess rate controllable | Poor distractors turn it into a giveaway |
| Buzz-in | Race to buzz, then answer | The most tension and the best viewing | Adjudication that scores hand speed alone punishes slow networks and cautious players |
| Spoken or typed | Say or enter the answer | Guess-proof, the strongest sense of knowledge | Adjudication that rejects aliases and typos feels unfair |
| Ordering or matching | Put elements in order | One question tests several layers of knowledge, and it reads well | High input cost; touch, gamepad and mouse must be tuned separately |
| Wagering | Stake points before answering | Turns "knowing" into risk management | Score swings are large; guard against all-in imbalance |

Adjudication discipline: casual and party settings score right or wrong, not hand speed (the engineering definition of the adjudication window is in §4); accept aliases, abbreviations and common typos, and keep the adjudication table out of hard-coded scripts; wrong-answer feedback reveals the correct answer with a one-line source note first, and runs the point-loss animation afterwards — feed before you punish.

### 3.4 Multiplayer Competition and Live Broadcast Formats

Trivia's multiplayer formats have three common skeletons:

| Skeleton | Structure | Suitable settings | Main risks |
| --- | --- | --- | --- |
| Shared-screen or friends'-room versus | One shared prompt, buzz-in or turn order, live scoring | Living rooms and online friend groups | Unfair buzz-in adjudication; slower players trail the whole way |
| Ladder run | Solo or squad, difficulty and rewards rising step by step, with a guaranteed cash-out | Solo long sessions and streams | One mistake wiping progress drives players away |
| Big-room broadcast | One prompt synced to everyone, a unified countdown, a public board | Streams and variety events | Look-up cheating; a poor experience for anyone who drops |

- The four-piece kit of a live broadcast format: synced prompts, a visualized countdown, comment or live-chat interaction, and a public board plus survival curve at the results. Each one amplifies the feeling of "I am on stage too".
- The waiting window is multiplayer trivia's biggest waste: in turn order, everyone else just waits out the current question. Give waiting players a second task (wagering, predictions, cheer points), or change the structure so that everyone answers the same question at once.
- A program can play host: reading the question, pausing, revealing, locking in, lifelines and eliminations all become system events; when the staging budget is limited, sound effects and pauses pay off better than animation.
- The same discipline as Genre Handbooks · Party Games: low barriers, laughter first, no one waits more than thirty seconds; the device accounting for shared screens and phone rooms (controllers, room codes, hot-plugging) follows that page directly.
- Cheating and answer-searching: in-person matches rely on mutual supervision; online, use time pressure (no time to search), question-bank rotation and reports of abnormal answer patterns to suppress the payoff of searching.

### 3.5 Content Cost and Review: The Real-World Pressure

- Real authoring speed: from topic selection, sourcing, drafting and distractor writing to review, a question commonly takes ten to thirty minutes; the bulk of the cost is sourcing, not typing. Statistics questions and name-attribution questions are the most time-consuming.
- Review is a double gate: factual checking (numbers, years, spelling, alternative names, attribution) and compliance checking (current affairs and religion, region and ethnicity, living people and privacy, trademarks and brands). A question enters the bank only after both gates; anything doubted at either gate is shelved or dropped.
- Real-world pressure lands entirely on the questions: questions about disease, disasters, the deceased or contested events keep being reinterpreted, and an old question can turn from a fun one-liner into an incident. Discipline: do not chase disaster-related timeliness, and inspect questions about people on a regular cycle.
- The question bank is a monthly fee, not a one-time purchase: maintenance, retirement, rewrites and top-ups are a long-term bill. The repetition rate across a twenty-question match and the average number of questions a player sees per week together decide the top-up tempo; for an operations-grade cadence, see Live-Ops & Growth.
- Scheduling arithmetic: commonly fifteen to thirty questions per working day (including review and fixes), plus 30–50% on top for review labor; a clean thousand-question bank commonly runs one to three months of solo effort, with time-sensitive questions on a separate weekly production line.
- Retirement discipline: disputed, expired and duplicate questions are retired outright; saving a bad question costs more than writing a new one.

### 3.6 The Boundaries of AI Question Writing

- Placement: AI suits first drafts and pipeline chores — question drafts, distractors, category tagging, near-duplicate detection, multilingual transcription — but not adjudicating final facts.
- Three common failures: stale knowledge (the answer changed after the output), hallucinated invention (answers, numbers and attributions conjured from nothing), and drift (one fact with two answers). Numbers, years, names and attributions must each be traced back to a source; nothing enters the bank on "looks right".
- Process: AI drafts, a human fact-checks, a second person reviews or a sampled share is inspected, and the question enters the bank with its source labeled; AI drafts carry a uniform tag for batch re-inspection later.
- Red lines: unverified AI questions do not ship; anything disputed after launch comes down first and gets discussed second; external disclosure and ledger conventions follow the compliance framework in AI Workflows.
- The call comes back to the same decision table: how verifiable the output is, and how costly a mistake is. Knowledge questions are cheap to verify and expensive to get wrong (reputation), so the configuration is "use drafts freely, always fact-check, keep good records".

## 4. Technical Essentials

The engineering difficulty concentrates in two places: the question-bank pipeline and multiplayer synchronization. Trivia has no real-time game-feel requirement, and web, mobile and PC can all carry it; everything below is engine-agnostic.

**Questions Are Data**

- Freeze the question record structure on day one (fields in §3.1); manage it in a spreadsheet or JSON so that content edits never touch code.
- Put question-bank files under version control: edits leave a trail and can be rolled back; use scripts for bulk edits — hand-editing a thousand questions does not last.
- With multilingual plans, organize around string tables: prompts, options and feedback copy kept fully separate, with the glossary established first.

**Question-Bank Pipeline and Quality Tools**

- The import validator is the first tool to write: complete fields, a unique answer, legal categories, no duplicate distractors, and expiry reminders.
- Near-duplicate detection: prompt similarity plus fact fingerprints (different phrasings of the same fact) to prevent two questions for one fact.
- A disputed-question queue: questions with abnormally low accuracy, many complaints or a high option-switch rate enter the queue automatically for human adjudication.

**The Draw Service**

- Four capabilities — weights, exclusion lists, difficulty quotas and audit logs (§3.2); match logs are replayable, for verifying fairness.
- Pin the acceptance cases: ten consecutive matches by one player with no repeats; category shares within target; a fallback strategy when the pool runs dry.

**Multiplayer Sync and Adjudication**

- Buzz-in adjudication lives on the server: unified timestamps, latency compensation and a consistent adjudication window, with the client only displaying; high-latency players get a compensation window or a mode without buzz-in.
- Round sync needs only three events: prompt broadcast, answer submission and a unified step; on reconnect, push the current question and scores down in one go.
- Big broadcast rooms: a limited set of questions but high concurrency — batch answer submissions and keep leaderboards approximate.

**Telemetry and Verification**

- Record accuracy, answer-time distribution, skip rate and option distribution per question; once samples pass a thousand, re-calibrate difficulty from the data (§3.1).
- Player-side records keep strengths, weaknesses and seen-question flags, reusing the draw exclusion lists rather than maintaining a second copy.
- The engineering order is clear: the question-bank pipeline and tools first, multiplayer sync added as modes require; neither end carries game-feel risk.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimating scope and for cutting requirements; not a commitment.

| Tier | Question-bank scale | Time reference | Notes |
| --- | --- | --- | --- |
| Prototype | 50–100 questions | 1–2 weeks | Validates the loop and adjudication only; the bank is hand-written |
| Small complete title | 500–1,500 questions | 1–3 months | The common starting point for solo developers; includes one full-bank review |
| Live product | Thousands of questions plus a time-sensitive production line | Ongoing | Bank size decides retention; maintenance is a monthly fee |

Conversion conventions and hidden undercurrents:

- Estimate authoring at fifteen to thirty questions per working day (review included), ten to thirty minutes per question; count review and re-inspection separately at 30–50% of the authoring effort.
- Time-sensitive production line: a fixed top-up window each week or each season; commonly 10–20% of the bank is time-sensitive and gets rewritten or retired on expiry.
- Art and staging are the small end: prompts, options, feedback animations, a results screen and one theme track — a single template covers the whole bank; the cost is always in the question bank.
- Scope discipline: cutting questions is always cheaper than saving them; acceptance for a bank looks at "grab twenty questions at random — how many are worth screenshotting to a group chat", not the total count.

## 6. How to Start the First Prototype

Goal: answer one question in one to two weeks — is this loop tiresome? No art, accounts or seasons.

1. **Days 1–3: fifty questions and a minimal question drawer.** Hand-write the bank, ignore category balance for now; shuffle the draw, exclude answered questions, multiple-choice adjudication with right/wrong feedback. Ugly is expected.
2. **Days 4–7: scoring and reveals.** Streaks, difficulty weighting, reveal animations and sound; a match of ten to twenty questions with a results screen at the end.
3. **Days 8–14: two rounds of blind testing.** Have five people each play a match and record the accuracy distribution, disputed questions, questions that silence the whole room, and whether anyone starts a second match on their own. The second round fixes disputed questions and difficulty breaks.

Success criteria (all observable):

- At least three of the five testers start a second match on their own.
- No more than two questions get zero correct answers, and each can be attributed (too obscure, ambiguous prompt, disputed answer) rather than written off as "they are just bad at this".
- No question is judged to have a wrong answer; rulings on disputed questions are on record.
- Testers can explain their score with "I knew that" — they know which answers they guessed right and wrong.

If the budget allows, spend half of the second week on a two-player shared-screen buzz-in version: the same device, the same keyboard, to test whether competition is more tense than solo play. Once competition holds up, talk about multiplayer formats and scaling up the question bank.

## 7. Common Pitfalls

1. **The question bank is too small**: players burn through a few hundred questions, and by day two everything is old. Put repetition control and a top-up plan in place before the pool runs dry (§3.2, §5).
2. **Difficulty by obscurity**: questions nobody knows, answers that rely on rote memorization. Obscure facts are an easter-egg quota, not the axis of difficulty.
3. **Disputed answers**: multiple valid answers, stale facts, unrecognized alternative names. One answer per question plus its source; the adjudication table accepts aliases (§3.3).
4. **Near-duplicates out of control**: the same fact appearing twice in a match, or resurfacing in a new skin. Fact fingerprints plus exclusion lists (§3.2).
5. **Buzz-in scored on hand speed alone**: latency punishes some players and caution is penalized. Casual matches score right or wrong only, with a tolerant adjudication window (§3.3, §4).
6. **Time-sensitive questions left unmaintained**: year and champion questions hang in the bank past expiry, and players find the errors for you.
7. **AI questions shipped straight to production**: hallucinated answers enter the bank without review, and reputation is gone in one go (§3.6).
8. **Dead waiting windows**: in turn order, everyone else has nothing to do for long stretches. Switch to everyone answering the same question, or give waiting players a second task (§3.4).
9. **Everything outside the questions is missing**: a question bank with no pacing, staging or results. Half of trivia's showmanship lives outside the questions.
10. **A single assumed audience**: writing questions from your own knowledge structure leaves blind spots for the target audience (generation, region, industry). Have someone outside that audience answer the set once before shipping.

## Further Reading

- [Game Design Handbook](../../fundamentals/game-design/README.md): core loops, feedback and experience-goal methods — the drafting paper for sections 1 and 2.
- [Programming Handbook](../../fundamentals/programming/README.md): data-driven design, toolchains and debugging methods; corresponds to section 4.
- [Live-Ops & Growth](../../publishing/live-ops/README.md): content update cadence and the long-term operations ledger; corresponds to §3.5 and section 5.
- [Case Studies](../../postmortems/README.md): methods for breaking down shows and products; consult when choosing a direction or running a postmortem.
- [Genre Handbooks · Party Games](../party/README.md) (Volume 3): low barriers, laughter first and the multiplayer device ledger; cross-reads with §3.4.
- [AI Workflows](../../ai/README.md): verification boundaries, ledgers and disclosure conventions for AI drafts; read against §3.6.
- [Pitfalls & Anti-patterns](../../pitfalls/README.md): content-production and live-ops pitfalls; read against section 7.
- Homework: hand-write twenty questions, have three friends answer one round each, and record three things: the most disputed question, the question that silenced the room, and whether anyone says "one more" afterwards. Those three records are this handbook's acceptance sheet.
