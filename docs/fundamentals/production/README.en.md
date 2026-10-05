# Ludo Atlas · Production Handbook

> Positioning: a handbook that turns "finishing a game" into a manageable process, covering kickoff documents, estimation and scheduling, phase models, scope control, team collaboration, outsourcing management, testing and QA, risk management, a dedicated chapter on solo development, and postmortem methods.
> Companions: Game Design Handbook · Programming Handbook · Pitfalls & Anti-patterns (project management chapter) · Multi-platform Launch Playbook · the template library (design doc §9).
> Principle: **management exists to serve "shipping something good"**; the lighter the process the better — but every feature cut must be recorded.

---

## 1. Kickoff Package (the three documents that must exist before the project starts)

| Document | Contents | Length |
| --- | --- | --- |
| One-pager (pitch) | Concept/player fantasy/core loop/target platforms/audience and competitors/differentiators/business model | 1 page |
| Mini GDD | Plus controls, systems list, content plan (level table), art and audio direction, technical baseline | 3–8 pages |
| Scope statement | An explicit **won't-do list** + success criteria (what counts as "done") + draft milestones | 1 page |

> Success criteria must be verifiable (e.g. "launched on Steam, ≥80% positive reviews, recouped its cost"); "fun" is not a criterion.

## 2. Estimation and Scheduling

### 2.1 Estimation Methods

- **Analogous estimation**: find a similar feature/title you have completed (your own previous work is the most accurate) → apply a multiplier (unfamiliar territory ×1.5–3).
- **Three-point estimation**: optimistic/realistic/pessimistic, take `(O+4M+P)/6`; for game asset work, default to the pessimistic value.
- **Experience multipliers**: content production (levels/art) commonly runs 2–3× the first estimate; online/unknown platforms 2×+.
- **Buffer**: keep a **30–50%** buffer in the overall schedule (not laziness — it is the reality industry statistics show).

### 2.2 Milestone Design

| Milestone | Definition (verifiable) | Check |
| --- | --- | --- |
| Prototype | Core loop playable, with placeholder assets | The "toy test" passes (Game Design Handbook §1) |
| Vertical slice | A short complete experience at **final quality** | Quality bar established + schedule recalibrated (use it to re-estimate full production time) |
| Alpha | All systems in place (features complete, content missing) | Feature Lock: the feature list is frozen |
| Beta | All content in place (completable/playable end to end) | Content Lock: content is frozen, only bug fixes and polish |
| RC / Gold | Release candidate | Code Lock: only blocker-level bug fixes allowed |

- Iron rule: a milestone = a **playable build**, not "code finished" or "docs finished".
- Weekly/biweekly cadence: set goals on Monday (three or fewer) → playable build + a brief on Friday (what got done/what's blocked/what's next week).

## 3. Scope Control (the skill that decides whether the project lives or dies)

- **Prioritization framework**: label every item with MoSCoW (Must/Should/Could/Won't); write the "Won't" list down explicitly and make it public (to stop it from being resurrected).
- **Feature-cut order** (first cut to last cut): cosmetic skins → side content → extra modes (Photo Mode/endless mode) → system depth (talent-tree branches) → content volume (level count/character count) → **anything touching the core loop is cut last**.
- **Principle**: you cut features to protect the experience and the completion; **"a finished small game" beats "an unfinished masterpiece"** (see Pitfalls & Anti-patterns).
- New-feature approval: every addition must be "one in, one out" (cut an item of equal size), and it gets recorded in the changelog.

## 4. Iteration Cadence and Team Collaboration

### 4.1 Minimal Process for Small Teams (2–8 people)

- Kanban board (HacknPlan/Codecks/Feishu/Trello): four columns Todo / Doing / Review / Done; every card is ≤2 days of output.
- Standup: 15 minutes a day (or an async written version); answer only "yesterday/today/blockers".
- Decision records (ADRs): write 5 lines for each major technical/design decision (context/options/decision/consequences) to prevent "collective amnesia".
- Documentation discipline: a single source of truth (Notion/Yuque/repo docs); **never make decisions in private chats** (see Pitfalls & Anti-patterns).

### 4.2 Roles and Division of Labor (the small-team merge trick)

| Big-studio role | Merged into, on a small team | Key point |
| --- | --- | --- |
| Producer/project manager | Any team member, as a side role | Do only three things: scope/schedule/risk |
| Designer (systems/levels/balance) | Lead designer or a programmer doubles up | Balance numbers must live in tables (Game Design Handbook §4.1) |
| Technical artist | Art lead + a programmer, together | Asset conventions and import scripts |
| QA | Everyone, on rotation | A fixed "destructive testing" slot for every version |

### 4.3 Outsourcing Management Process

1. Requirements package (reference images + spec sheet + acceptance criteria + delivery format) → 2. Quotes and paid tests → 3. Milestone contract (staged payments) → 4. Staged acceptance (draft → final) → 5. Source-file and license archiving (for compliance see the Legal, Patents & Competition Handbook).

- Acceptance criteria must be **quantifiable** (dimensions/style comparison images/animation durations); no "it just doesn't feel right" back-and-forth.

## 5. Testing and QA

- **Playtest organization** (progressive): self-test → internal cross-testing → targeted external (5–10 target players) → public demo (Demo/Next Fest, Live-Ops & Growth).
- **Minimum QA plan**: verify the feature list item by item + destructive testing (unplugging/sleep/full memory/rapid clicks) + regression list (retest old bugs) + device matrix (Multi-platform Launch Playbook/Programming Handbook).
- **Bug severities**:

  | Severity | Definition | Handling |
  | --- | --- | --- |
  | S1 Blocker | Crash/freeze/save loss/cannot continue | Fix immediately; blocks release |
  | S2 Critical | Feature broken but there is a workaround | Must fix before release |
  | S3 Normal | Experience issues/minor errors | Schedule the fix |
  | S4 Minor | Text/visual blemishes | Fix when there is time (goes to the backlog) |

- Test records go into one shared system (kanban or Excel both work); every bug carries: reproduction steps/environment/screenshot or video.

## 6. Risk Management

- **Risk register** (updated at every monthly review):

| Risk | Probability | Impact | Contingency |
| --- | --- | --- | --- |
| A core member leaves/gets sick | Medium | High | Document critical systems; no single point of knowledge |
| Optimistic scheduling (the most common risk) | High | High | Buffer + a feature-cut contingency ready to go |
| Engine/platform technical pitfalls (e.g. a platform export fails) | Medium | Medium | Early technical validation (spikes; see the design doc §19 plan) |
| Approval/game license delays (mainland China) | Medium | High | Plan 6–12 months ahead; keep an overseas release as a backup |
| Running out of money (full-time development) | Medium | Very high | Set aside 6–12 months of living expenses; bridge with outsourcing/part-time work |
| A competitor launches first or copies you | Low | Medium | Speed + community + differentiation (Legal, Patents & Competition Handbook §7.5) |

- Every risk has a "trigger condition" (e.g. "slice takes 50% longer than estimated" → start the feature-cut contingency); when it trips, execute — no debate.

## 7. Solo Development (a dedicated chapter)

- **Time reality check**: weekly available hours = total hours − life − day job (if any); at 10h per week, a small project ≈ 6–12 months — set scope by that (shrink the one-pager until it fits).
- **Weekly deliverable**: by the end of each week there must be a build you can open and see changed; visible progress is fuel for motivation.
- **Anti-abandonment strategy**: split the project into several shippable mini-phases; make a public commitment for each phase (devlog/community); stuck for 3 days means switch tasks or ask for help (see the burnout pitfall in Pitfalls & Anti-patterns).
- **What to outsource**: outsource art/music first (the highest-leverage use of money); do only "core fun + systems" yourself.
- **Mindset**: completion > perfection; the "regret list" at launch is the starting point for the next project.

## 8. Game Jam Training (take your management skills to the gym)

- Value: run the whole "kickoff → scope → production → release" process within 48 hours; the cure for people who can never finish anything.
- Strategy: settle the "one playable sentence" first → cut to the very core → use assets or AI assistance for all art/audio → freeze 2 hours before submission (Multi-platform Launch Playbook template).
- Cadence: 2–4 jams a year; deliberately practice one weak spot per jam (narrative/levels/game feel/release process).

## 9. Postmortem Methods (mandatory after a project ends / after a milestone)

- **Writing a postmortem**: goals vs results (data) → what went right (reusable) → what went wrong (root causes, no blame) → what to change next time (≤5 actionable items).
- **Reading postmortems**: prioritize "same genre × same scale" postmortems (Resources §4 and `docs/postmortems/`); beware survivorship bias: failure cases carry more information.
- Archiving: they go into `docs/postmortems/` (template at `templates/postmortem.md`), becoming team assets.

## 10. Production Cadence Template (safe to copy as-is)

| Cycle | Action |
| --- | --- |
| Daily | 15-minute sync (text is fine); log blockers |
| Weekly | Friday: playable build + a 3-line brief; Monday: set ≤3 weekly goals |
| Monthly | Review the risk register + review the scope statement (did anything sneak in?) |
| Every milestone | Tick off each acceptance criterion + postmortem + re-estimate the remaining schedule |
| Every release | Walk the release checklist (Multi-platform Launch Playbook §10) item by item |

> In one sentence: **a believable scope × a visible cadence × decisive cuts = a project that lives to be finished.** After that, hand it to the Live-Ops & Growth to turn it into a business.
