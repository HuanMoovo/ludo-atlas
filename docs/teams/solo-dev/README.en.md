# Ludo Atlas · Teams & Scale · Solo Dev

> **Teams & Scale**. Positioning: breaks "one person finishing a whole game" down into actionable scope discipline, a weekly cadence and mental expectations, covering the full path from a one-sentence kickoff to post-launch updates.
> Companions: Production Handbook · Indie Survival · AI Workflows Handbook · Game Design Handbook.

---

## 1. Positioning and Fit

Solo development means one person covers the core roles (design, programming, art, audio, QA, publishing). It and team development are two different ways of making trade-offs: teams expand capacity through division of labor, solo developers protect completion by cutting scope. Works like Stardew Valley and Vampire Survivors both went the solo route; what they have in common is that everything left in them was cut down to the essential.

Find your row by commitment level first (figures are reference values):

| Form | Hours per week | Time to finish a small commercial project | Prerequisites and risks |
| --- | --- | --- | --- |
| Hobbyist, student | 5–10 hours | Measured in years, or jam-scale projects only | Use small projects to practice the full pipeline; a drawn-out timeline is the main risk |
| Part-time | 10–20 hours | 6–12 months (per the Production Handbook §7) | Stable income; fixed slots are mandatory, or the project drags on indefinitely |
| Full-time | 40+ hours | 3–6 months (linear extrapolation at the same scale) | Calculate your runway first (12+ months recommended; Indie Survival); if you don't finish, the money runs out |

Project shapes that suit solo development: mechanic-driven, small in scope, stylistically consistent, single-player or turn-based. What it is bad at: long-form narrative RPGs, large volumes of hand-made assets, live-service games that need long-term online operations. When scope conflicts arise, change the scope, not the resolve.

"Solo" means one person holds the decisions and the core production — not that every task is done by yourself. Outsourcing, asset libraries and AI are the three levers (see §4); use them to free up time first, then talk about scope.

## 2. Core Challenges and Countermeasures

### 2.1 Time and Energy Budget

Available hours per week = 168 - sleep - day job - life. Plan against that number, not against your wishes. Three disciplines:

- Scheduling uses only 50–70% of available slots; the rest goes to buffer, chores and getting sick (for the estimation and buffer conventions, see the Production Handbook §2).
- Lock your two or three best-energy slots each week to core production (design, code, levels); batch replies, purchases and asset sorting into fragmented slots.
- Do a two-week time audit before starting: log actual hours first, then set scope. Most people underestimate chores and overestimate focused time.

### 2.2 Scope Discipline: Cut Until One Thing Is Left

You cut scope with process, not willpower. Work through the sequence below:

1. One-sentence test: the player is in ____, repeatedly does ____ (one verb), in order to ____. If you cannot fill in this sentence, do not start.
2. List every system you want to build and sort them into three piles: core (without it the game does not exist), enhancement (more fun but not essential), decoration (actually lifted from some other game). Version one builds only the core pile.
3. Cut version one down to one thing: one verb, one resource, one goal. Everything extra goes into the "enhancement pile" until the content is validated.
4. Interrogate each item destructively: if this were cut, could the game still be played? If yes, cut it — or write it into the "won't do" list pinned to the front of the board.
5. Order of cutting: number of platforms and languages, looks and extra modes, system depth, content volume — the core loop comes last (full checklist in the Production Handbook §3).
6. One in, one out for new features: before adding one, cut an equivalent old one, and log it in the change log.
7. Keep the core-mechanic validation prototype to 1–4 weeks: if you cannot get to "I want to play again", changing direction is cheaper than forcing it.

One concrete downgrade example: drop "open world + combat + building + story" to "one map + one mechanic + 30 minutes of play"; once that is done and still holds up, add the second system back as needed. Self-check for whether the cutting went far enough: describe the project to someone who has never heard of it — they should be able to repeat back the core gameplay.

### 2.3 Mindset and Burnout

Abandonment clusters around four points; recognize them in advance and you can go around them:

| Stage | Typical state | Countermeasure |
| --- | --- | --- |
| First 1–2 months | Novelty fades, progress is invisible | Break goals down to the week; every week must produce a build you can open and see change |
| First external playtest | A cold shower of problems | Say up front that you are looking for problems, not praise; log only fixable items |
| Pre-launch polish | The illusion that it will never be finished | Freeze scope; define the "good enough" acceptance bar; set a hard deadline |
| Post-launch cold start | "Nobody is playing, it was all for nothing" | The first game's goal is to finish the pipeline; use the data to fix the next one |

- Stuck-for-3-days rule: if any problem eats 3 days, switch tasks, shrink the problem, ask the community — do not grind on it.
- Put rest in the plan: keep one day a week completely away from the project; sleep is real capacity.
- Solo development gets isolating: park yourself in one developer community and find 1–2 peers you can playtest each other's work with.

A word of its own on post-launch expectations: the goal for a first game is to finish the release and run the pipeline end to end — that is more realistic than succeeding on the first try. Slow wishlists, revenue and word of mouth at the start are the norm; use the launch data to decide what to change in the next game, not to write off this one.

## 3. Workflow and Rhythm

### 3.1 The Weekly Cycle

The default weekly split shifts by phase (development / shipping & communication / learning):

| Phase | Development | Shipping & communication | Learning |
| --- | --- | --- | --- |
| Prototype | 85% | 5% | 10% |
| Production | 70% | 15% | 15% |
| 8 weeks before launch | 55% | 35% | 10% |
| 3 months after launch | 55% | 35% | 10% |

- Spend learning time on what you will use this month, not on learning for its own sake; tutorial hell is the solo developer's number-one time sink (see §6).
- The shipping-and-communication slot is never zero from the vertical slice onward: public records (screenshots, short devlogs) are the only free inventory you will have on launch day; keep three weekly minimums — one playable build, one public update, one 15-minute weekly review. Cap weekly goals at three, and commit to them when you set goals on Monday (Production Handbook §10).

### 3.2 Milestones and the Task Board

- A milestone = a playable build, not "the code is done". Minimum sequence: toy prototype (1 month) → vertical slice → content production → Alpha (feature freeze) → Beta (content freeze) → release; acceptance conventions in the Production Handbook §2.
- Task board, four columns: Todo / Doing / Self-test / Done; no more than 2 cards in Doing, and each card cut to under 2 days of work.
- Solo developers have no second pair of eyes, so self-testing replaces QA: run every version through the regression checklist and destructive testing (loading saves, disconnecting the network, rapid clicking, full inventory); whatever cannot be fixed goes onto the known-issues list.

### 3.3 The Single Source of Truth

- Decisions, specs and tasks each live in exactly one place: the design doc goes in the repo (`design.md` to start), tasks go on the board, and major decisions get 3–5 lines in the change log the same day.
- Recover "temporary decisions" from chat logs into the docs every week; keeping state in your head is solo development's biggest hidden cost.
- Write commit messages and code for the version of you three months from now: spell out the "why", and archive build artifacts by version number.

### 3.4 Release Cadence

A release is a timeline, not a single action:

| Point | Action | Mental preparation |
| --- | --- | --- |
| After the vertical slice | Run a small-scale playtest on itch.io or a similar channel and start collecting feedback | More problems than praise is normal |
| 3–6 months before launch | Store page goes live; the earlier the wishlist starts the better; keep posting public updates | Slow wishlist growth is the norm — watch the trend, not single days |
| 4–8 weeks before launch | Prepare a demo for showcase events; finalize marketing assets | Asset quality drives click-through; it is worth redoing |
| Launch week | Walk the launch checklist item by item (Multi-platform Launch Playbook §10); keep whole days free for hotfixes | Do not schedule anything else for the first 24 hours |
| 2–4 weeks after launch | Hotfixes, responding to feedback, writing the postmortem | "Ship and vanish" damages early word of mouth |

## 4. Collaboration and Division of Labor

### 4.1 When to Outsource

The test: outsource work that delivers predictably and is easy to accept; keep work that needs repeated iteration in-house.

| Task | Recommendation | Rationale |
| --- | --- | --- |
| Core gameplay, game feel, core loop | Do it yourself | Changes most frequently; the communication cost of outsourcing exceeds the payoff |
| Key art (key visuals, cover, characters) | Outsource or commission | Determines how it sells; the best value when it is not your strength |
| Music, theme songs | Commission or licensed libraries | Per-track commissions are common; confirm the license scope |
| Sound effects | Asset libraries plus your own edits | Low unit price and high volume; libraries are enough |
| Localization | Outsource (before launch) | Native-speaker review per language; machine-translated draft plus human editing |
| Console porting and certification | Outsource if budget allows | A high experience barrier; a first game can skip it for now |

For timing, see Indie Survival: wait until your own quality or speed has become a real bottleneck and asset volume has ramped up; do not place orders while the style is unsettled. The process follows the Production Handbook §4.3: requirements package (reference images, specs, acceptance criteria, delivery format) → paid test → milestone contract with staged payments → staged acceptance → source files and license archiving. Budget ballpark: outsourcing usually accounts for 20–40% of a project's budget.

### 4.2 How to Find Collaborators

- Channels: game jams, developer communities, paid tests on outsourcing platforms, former colleagues. Start a long-term collaboration with one small task, then talk about continuing.
- Prefer paid buyout work with clear ownership; for revenue-share collaborations, the workload, timeline and exit conditions must be put in writing — for contracts, see the Legal, Patents & Competition Handbook.
- Inputs to collaborators are always documents, never verbal paraphrase: "the way it is in my head" is the number-one source of outsourced rework.

### 4.3 How One Person Covers Art and Audio

| Route | Suited to | Watch out for |
| --- | --- | --- |
| Asset packs | Prototypes, non-critical assets, sound effects | Check the license for each one (commercial use, attribution, redistribution); you hold the line on stylistic consistency |
| Outsourcing, commissions | Key visuals, character art, theme music | Requirements package and acceptance criteria first; staged payments |
| Do it yourself | Pick a low-barrier style (pixel, geometric, black-and-white) | Make one style-test piece to set the spec before mass-producing (specs in the Art & Audio Handbook) |
| AI generation | Concept sketches, placeholder assets, texture variants | Treat output as intermediate only; the final version is human-finished and disclosed |

Skipping audio entirely is not recommended: a minimal setup of a sound-effect pack plus one licensed theme song costs little but heavily shapes the perception of "completeness" (specs in the Art & Audio Handbook).

### 4.4 Boundaries of Treating AI as a "Team Member"

- Positioning: AI is an accelerator; judgment and sign-off stay with you (the overarching premise of the AI Workflows Handbook).
- Safe to use: boilerplate code, tool scripts, configuration, batch conversion, placeholder assets, first-draft copy.
- Human pass required: translation drafts, marketing copy, art assets that need finishing; verify every number and conclusion item by item.
- Do not use directly: game-feel decisions for core gameplay, unprocessed final art, any output that recreates someone else's work.
- Keep a paper trail: maintain an AI usage log (tool, stage, purpose of the output) — platform disclosures and postmortems both need it; for disclosure requirements see the AI Workflows Handbook §4.5, §8.

## 5. Tools and Tech Stack Recommendations

The principle for the toolchain is good enough, easy to swap, low fuss — set it up once, keep maintenance under half a day a month; when torn, pick the free option you know best.

| Area | Good-enough setup | Notes |
| --- | --- | --- |
| Version control | Git plus one remote repository | Commit at least once a day; tag before big changes; large files via LFS or ignored |
| Backups | Three copies: local, cloud, off-site (3-2-1) | Run a restore drill regularly to prove the backups actually open |
| Task management | Any one kanban tool (Trello/Notion/Feishu/Codecks is plenty) | Solo developers do not need heavyweight project management; cards under 2 days |
| Design docs | `design.md` in the repo plus a change log | Single source of truth; stray "temporary decisions" recovered weekly |
| Outsourcing | Email or docs plus a source-file archive directory | Requirements and acceptance criteria in documents, not spoken words |
| Builds and releases | Engine export plus store backends; builds archived by version | Keep every uploaded version on file — you will need it for store rollbacks |

The good-enough launch-channel setup: for PC, start with "itch.io for the demo, Steam for launch", and consider a second platform only with capacity to spare; mobile and mini-games are a separate calculation driven by platform requirements. Go deep on one platform before adding the next — every added platform steps QA and support costs up a level.

## 6. Common Pitfalls

1. **Scope out of control**: trying to make a big game as your first. If the one-sentence test does not fill in, cut; if it does not fit in 12 months, downgrade it and re-estimate.
2. **Art piled up during prototyping**: any fine work done before the core gameplay is validated can be wasted. Greybox it and pass external playtesting first.
3. **Building in a vacuum**: hearing real feedback for the first time on launch day. Playtest with 3–5 people at every milestone.
4. **Zero shipping bandwidth**: going live with zero wishlists and zero community. Keep a public record going from the first presentable content onward.
5. **Tutorial hell**: using new-tool learning to avoid making the game. Let learning be triggered by the project's current gaps; do not stockpile.
6. **No backups, no docs**: one disk failure destroys everything. 3-2-1 backups plus externalizing the key design.
7. **Trading health for progress**: progress ground out of all-nighters is repaid several times over later. Put rest and sleep into the plan.
8. **Outsourcing the core gameplay**: handing off the thing that needs the most iteration; the back-and-forth eats all the upside.
9. **Mismatched expectations**: assuming "finish it and players will come". The first game's goal is finishing the pipeline; the data belongs to the next one.

## Further Reading

- Production Handbook: kickoff packages, estimation and scheduling, scope control, and a dedicated solo-development chapter — the full expansion of sections 2 and 3 here.
- Indie Survival: mode selection, runway math, funding sources and decision checkpoints.
- AI Workflows Handbook: the AI suitability decision table, disclosure requirements and the red-line list.
- Game Design Handbook: the base document for core loops and system trade-offs.
