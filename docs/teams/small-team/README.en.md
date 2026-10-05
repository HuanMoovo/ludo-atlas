# Ludo Atlas · Teams & Scale · Small Teams (3–10)

> **Teams & Scale**. Positioning: teams of 3 to 10 people, where all three functional lines are held up by people wearing multiple hats, using light process and a fixed rhythm to take one game from kickoff to release.
> Companions: Production Handbook · Indie Survival · AI Workflows · Game Design Handbook.

---

## 1. Positioning and Fit

In one sentence: a small team is the scale band of **everyone wearing multiple hats, light process, weekly iterations**. Headcount has outgrown "one sentence keeps everyone in sync", yet is not enough to staff every link with a dedicated person; process has to be just enough to hold communication overhead down, and little enough not to slow development.

The three scales compared (the same framing appears in the scale section of Game Development at a Glance):

| Scale | Headcount | Ways of working | Biggest risk |
| --- | --- | --- | --- |
| Solo | 1–2 people | No meetings, decide as you build | Scope out of control, stalled progress |
| Small team | 3–10 people | Everyone wears multiple hats; light process plus weekly iterations | Communication overhead, direction drift |
| Studio | 10+ people | Dedicated division of labor, stage reviews | High cost, slow decisions |

Around 3 people, programming, art and design each deserve a primary owner; at 6–10, dedicated production becomes necessary: one person (even half-time) watching scope, schedule and risk, rather than whoever has time managing them. Do the communication-channel math too: 3 members have 3 potential pairwise channels, 6 members have 15, and 10 members have 45 — double the people, quadruple the communication surface. Process design has exactly one goal: make information travel by broadcast, not by pairwise private chat.

Signals it fits:

- Programming, art and design all have someone responsible; what is missing is rhythm and process, not people.
- The project spans 6–24 months, targeting a shippable product.
- Members have worked together before, or are willing to run a short project first to shake out how they work together.

Three situations where this playbook does not apply yet: members barely know each other and want different things from the project — shake out how you work together before committing long term; content volume clearly exceeds team capacity — cut scope first (Production Handbook §3) and schedule after; the core gameplay is not validated — prototype first, because weekly iterations cannot save a wrong direction.

## 2. Core Challenges and Countermeasures

Most small-team collaboration problems trace back to five sources. Each challenge gets an executable countermeasure, not a slogan:

| Challenge | Typical symptom | Countermeasure |
| --- | --- | --- |
| Communication overhead | More replies spawn more messages; decisions distort as they travel | Single source of truth, async first, a meeting budget (§4.3) |
| Multi-hat overload | Four or five titles each; everything stalls at 40% | Primary role plus secondary role, with fixed time blocks for the secondary |
| Direction drift | The core gameplay gets overturned again and again; scope keeps growing | Experience pillars and a scope statement; one in, one out for new requests |
| Opaque progress | Everyone works separately; pieces will not snap together near delivery | A weekly playable build; milestones accepted as playable versions |
| Single-point dependency | One person takes leave and the critical path stops | Document critical systems; every line has a second person who can take over |

- **Primary role plus secondary**: one primary role per person, taking 70–80% of time; a secondary taking 10–20%, for coverage rather than mastery — a programmer covering the toolchain, an artist covering UI implementation, and so on. The secondary must go into the weekly plan with a fixed time block, or it never happens.
- **One in, one out**: every new request cuts an equivalent item at the same time, logged in the change log. This guards against "working hard every week while the scope grows every week".
- **The second person**: on critical paths — builds, releases, save files, core gameplay code — someone else must have read the code and run the process end to end. A module only one person understands cannot survive leave or departure.

## 3. Workflow and Rhythm

### 3.1 The Weekly Iteration Loop

The whole team runs the same loop on a weekly cycle:

`Monday goal-setting (no more than 3 items each) → integrate continuously through the week → playable build on Friday → Friday brief → repeat next Monday`

- Every goal needs an owner and an acceptance-checkable definition of done. "Tuning combat feel" is not a task; "cutting hit-stun from 12 frames to 8 frames with before/after video" is.
- Friday's build must open, play and demo; a build that fails to appear is the week's biggest signal — cut the workload or admit the slip, do not paper over it with "we'll catch up next week". The brief is three fixed lines — what got done, where it is stuck, next week's plan — posted in a public channel.

### 3.2 The Task Board

A kanban board with four columns (Todo, Doing, Review, Done), on paper or in software — discipline matters more than the tool:

| Rule | How to put it into practice |
| --- | --- |
| Task granularity | Each card is no more than 2 days of output; split anything larger |
| WIP limit | No more than 2 cards per person in Doing at once |
| Card contents | Owner, definition of done, sign-off person — missing any of the three means the work does not start |
| Blockers | Anything blocked for more than 1 day is flagged red and escalated the same day; never let a card rot in silence |
| Weekly cleanup | A Friday pass; cards dragging past two weeks get split smaller or cut |

The Review column is not decoration: changes to art, levels or systems get seen by at least one other person before they reach Done. Small teams have no dedicated QA, so looking over each other's work is the only quality layer; for the minimum QA practice, see the Production Handbook §5.

### 3.3 Milestones and Demo Cadence

Milestones are accepted as playable builds, not document or code progress. The definitions and acceptance criteria for the five milestone levels (prototype, vertical slice, Alpha, Beta, RC) are in the Production Handbook §2.2; small teams add two more disciplines:

- **Every milestone is tied to a showable build**: at each checkpoint there must be a build an outsider can pick up within five minutes; whatever is missing becomes the next phase's risk list, and anything confirmed out of scope triggers the feature-cut plan immediately (Production Handbook §3).
- **Look outward every 4–6 weeks**: show friends, peers or target players the week's build with basic packaging, and ask only two questions: "which three seconds made you want to keep playing" and "where did you most want to quit". This feedback is more honest than status reports; add a 30-minute postmortem at every milestone, producing three actionable improvements (Production Handbook §9).

### 3.4 Communication Cadence

| Cycle | Action | Time budget |
| --- | --- | --- |
| Daily | Stand-up (text version counts): yesterday, today, blockers | Under 15 minutes |
| Weekly | Monday goal-setting; Friday build and brief | Under 30 minutes each |
| Monthly | Review the scope statement and risk register | 30 minutes |
| Every milestone | Tick off acceptance item by item; postmortem | 60–90 minutes |

- The stand-up answers three questions only and stops when time is up; topics that need depth get a separate meeting with the people concerned — never hold the whole team hostage.
- Keep one no-meeting day every week. Unbroken development time is the scarcest resource, and it is always the first thing meetings eat.

## 4. Collaboration and Division of Labor

### 4.1 The Role Triangle and Multi-Hat Coverage

Programming, art and design are the three lines that must have primary owners; the remaining functions are covered by doubling up and outsourcing. For the full skills inventory of each line, see the Roles & Skills Map in the Getting Started section.

| Function | Common split at 3–5 people | Common split at 6–10 people | Red line |
| --- | --- | --- | --- |
| Programming | 1 lead programmer, also covering tools and builds | Gameplay, tools or server split | A second person on builds and releases |
| Art | 1 lead artist, also covering UI implementation | Lead artist plus a technical artist or outsourcing liaison | Asset specs before mass production |
| Design | Lead design doubled by a programmer or artist | Dedicated design, possibly with levels | Numbers must live in tables |
| Production | Doubled by any member | Dedicated or half-time | Only scope, schedule and risk |
| Audio | Outsourced or asset libraries | Outsourcing plus a part-time musician | Set format and size budget first |
| Testing | Everyone on rotation | Everyone on rotation plus external playtests | A fixed destructive-testing slot per version |

Each person takes at most one primary role and one secondary; titles go into the responsibility chart, and who has the final say on what is written as one sentence pinned in the docs.

### 4.2 The Owner System

- Every module gets one owner: gameplay systems, art direction, the level pool, narrative, the build pipeline each count as a module. The owner decides the approach within their module; the team may weigh in, but the decision and the responsibility are the owner's.
- "Everyone is responsible" means no one is responsible in a collaboration context. Task cards, modules and risk items must all carry a specific name.
- Owner does not mean blame-taker: when something goes wrong, the postmortem process looks for root causes and fixes the process — focus on the problem, not the person (Production Handbook §9).

### 4.3 Communication Discipline: Documents, Single Source of Truth, Async First

Three rules keep communication overhead at a tolerable level:

1. **Single source of truth**: one task board, one docs area, one build distribution channel — exactly one place per category. Information in two places forks, and after three weeks of forking nobody knows which copy is right.
2. **Decisions in the open**: no settling things in private chats; major decisions become a five-line decision record (context, options, decision, consequences, date) kept in public. Conclusions first reached in private chats get a public record afterward too.
3. **Async first**: text over voice, a message over a live meeting. Interrupting someone's flow costs far more than replying two hours later. "Urgent" narrows to two cases: a release is blocked, or not handling it today drags someone else down.

- Write only four kinds of essential document: scope statement, decision records, asset specs, build instructions. Everything else is judged by "it counts only if it gets read" — do not produce documents nobody reads.
- Meeting discipline: agendas sent half a day ahead, attendees limited to those required, and a five-line summary before it ends (decisions, action items, owners).

### 4.4 Remote Collaboration

- Overlap windows: keep roughly 4 hours of daily overlap among remote members for stand-ups, reviews and questions; outside that, nobody is required to be online.
- Records instead of memory: synchronous meetings leave records by default, and key conclusions land in the docs the same day; absentees read the record — no replay meetings.
- Schedule by overlap: highly independent work (art assets, outsourcing liaison, writing) goes into low-overlap hours; work needing frequent collision (game-feel tuning, system integration) goes inside the overlap window. For checkpoints like vertical-slice reviews and demo sign-off, cameras on is recommended — a little ceremony makes the discussion more serious.

### 4.5 Outsourcing Management: How to Slice, How to Accept

Three principles for slicing work packages:

- Slice packages with clear boundaries and quantifiable acceptance: art assets, audio, localization, parts of testing, marketing materials.
- Do not slice packages with a high iteration frequency: core gameplay feel, numbers, core level design — they get reworked faster than any outsourcing conversation can keep up with.
- Each package has exactly one internal point of contact. Multiple interfaces to one vendor is how finger-pointing starts.

The process is five fixed steps; details in the Production Handbook §4.3:

`Requirements package (reference images, spec sheet, acceptance criteria, delivery format) → paid test (small batch to validate style and throughput) → milestone contract (staged payments) → staged acceptance (draft to final) → source-file and license archiving`

- Acceptance criteria must be quantifiable: dimensions, poly count, style reference images, animation timing, naming and layer conventions. No vague "this feels off" back-and-forth; batch feedback into one list and send it in one go — no fragmentation bombardment.
- Payments are tied to acceptance checkpoints, commonly in three stages: upfront payment, draft approval, final delivery; source files and commercial licenses are archived at each batch's acceptance — waiting until project wrap-up to ask often ends with missing files or missing people. For contracts, copyright and non-compete clauses, see the Legal, Patents & Competition Handbook.

## 5. Tools and Tech Stack Recommendations

Principle: subtract tools as the team scales — pick one per category, and merge categories wherever possible.

| Category | 3–5 people | 6–10 people | Notes |
| --- | --- | --- | --- |
| Task board | Trello, Codecks, Feishu tables | HacknPlan, Codecks | One board with four columns is enough |
| Docs | Repo docs, Yuque, Notion | Add a decision-record area | Where the single source of truth lands |
| Communication | One group chat plus one voice channel | A few channels split by function | Do not let the channel count run away |
| Version control | Git plus LFS | Same, with a large-file plan for assets | Binary assets go through LFS |
| Builds | Manual packaging each week | Automated builds plus internal distribution | Past 2 hours a week, it is time to automate |
| Assets | Shared drive plus naming conventions | Add a naming-check script | Specs come first |

- Build automation has the highest priority: manual packaging is a small team's biggest hidden cost, and once it exceeds 2 hours a week, spend one day automating it. Do not bolt a full CI/CD suite, multi-branch strategy and board automation onto version one — tools that go unused are pure maintenance overhead; start from a minimal set and add one item when a pain point shows up (cadence template in the Production Handbook §10).
- Use AI tools as a "headcount amplifier": coding agents, first-draft assets and document cleanup visibly absorb a chunk of the workload, but someone must sign off on the output — for red lines and process, see AI Workflows.

## 6. Common Pitfalls

1. **Meeting creep**: the stand-up stretches into a weekly meeting and the whole team is held hostage by the agenda. Cap the stand-up at 15 minutes and three questions; spin deeper topics into small focused sessions, and keep one no-meeting day a week.
2. **Direction drift**: every week a "good idea" enters the backlog; three months later the core gameplay is unrecognizable. Lock the experience pillars and scope statement, apply one in, one out to additions, and keep change records.
3. **Tasks with no owner**: a task someone will "take a look at when free" never gets looked at. Cards, modules and risks all carry a specific name; no owner, no start.
4. **Hiring too early**: hiring ahead for "we'll need them later" leaves the new hire without a clear task for three months while cash flow bleeds out first. Hire only when a bottleneck has persisted 2–3 months, and answer "what will they do for the next three months" before you do.
5. **Equity and revenue splits agreed only verbally**: percentages, exit mechanisms and contribution recognition all live in memory, and the moment revenue arrives or someone leaves it blows up. Put the split on one page in week one of forming the team; take clause questions to a professional.
6. **Integrating too late**: each person spends a month on a feature branch and the merge conflicts are soul-crushing. Small teams use trunk-based development, merge at least once a day, and ship a playable build every week.
7. **Hats stacked too full**: one person carries four or five titles and everything stalls at 40% completion. One primary role and one secondary per person, and the secondary gets fixed time blocks too.
8. **Process too heavy**: five people copy a big studio's full review and ceremony stack and the process itself becomes the workload. Start from a minimal set (weekly goal-setting, weekly builds, briefs, decision records) and add one item only when a real pain point appears.

## Further Reading

- Production Handbook: the master process for kickoff packages, estimation and scheduling, milestones, scope control and outsourcing — this page cites its sections throughout.
- Indie Survival: cash flow, cadence management and anti-abandonment strategy — the underlying methods are the same for small teams and solo developers.
- AI Workflows: concrete processes, checkpoints and red lines for using AI to cover headcount.
- Game Design Handbook: design reviews, number tables and gameplay validation methods — essential for the lead designer.
- Pitfalls & Anti-patterns: a quick reference for high-frequency pitfalls in the project management and team collaboration chapters; run through it during milestone postmortems.
- Case Studies: public postmortems filtered by scale; before forming a team and scheduling, read the failure cases from teams of the same size.
