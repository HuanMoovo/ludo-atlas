# Ludo Atlas · Teams & Scale · Studios (10+)

> **Teams & Scale**. Positioning: the organizational handbook for studios of 10+ people, covering department structures and review mechanisms, pipelines and specs, and phase models and risk control — breaking "big-studio process" down into executable actions.
> Companions: Production Handbook · Art & Audio Handbook · Multi-platform Launch Playbook · Pitfalls & Anti-patterns.

---

## 1. Positioning and Applicability

In one line: a studio is an organizational form that **trades process for certainty**. Ten people is the dividing line: past that size, whole-team "sync in person" stops holding up, coordination overhead starts eating individual output, and the complexity has to be absorbed by department structure, asset specs and a phase cadence.

"Studio" on this page means an organization with 10+ people, multiple disciplines running in parallel (design, programming and art each as their own line), and project cycles measured in years. Two cases fall outside it:

| Scenario | Where to go instead |
| --- | --- |
| Small teams of 2–8 people | the minimal process in the Production Handbook (Production Handbook §4.1) |
| Solo development | Production Handbook §7, the solo development chapter, and Indie Survival |

Three changes that scale brings:

- Communication goes from "said in person" to "written down": information needs a single source of truth, and verbal decisions don't count.
- Decisions go from "one person calls it" to "layered review": each layer is responsible only for its own scope.
- Quality goes from "feels right" to "verifiable": everything that can be described with a checklist and standards gets written down.

## 2. Core Challenges and Countermeasures

### 2.1 Coordination Cost: From Addition to Multiplication

- The more people, the more communication links: n people have n(n-1)/2 links among them — about 45 at 10 people, about 435 at 30. Most of a studio's process design is, at bottom, about keeping those links under control.
- Countermeasure 1: route through departments. Cross-department information flows only between liaisons; in-team details don't rise to all-hands topics.
- Countermeasure 2: decisions land in documents. Each decision gets written as "background, options, decision, consequences" and stored in a shared space (the same practice as the decision records in Production Handbook §4.1).
- Countermeasure 3: cap meeting headcount. Keep decision meetings to seven people or fewer; input from everyone else goes through written pre-review.

### 2.2 Pipeline First: Asset Specs and Automation

Small teams carry scale on craftsmanship; a studio must carry it on the pipeline: when headcount and asset volume rise together, the cost of manual processes grows multiplicatively. Before mass production, put four things in place (spec details in the Art & Audio Handbook):

| Item | Contents | Where it lives |
| --- | --- | --- |
| Naming convention | category_subject_action_number; prefixes such as SM_/SK_/T_ | Art & Audio Handbook §2.3, §3.1 |
| Spec sheet | Resolution, polygon count, texture size and compression, animation frame rate | Art Bible plus a technical budget |
| Import automation | Scripted engine import settings, atlas packing and compression parameters | Engine-side scripts |
| Check-in validation | Automatic naming and spec checks before commit; violations block the check-in | CI or commit hooks |

There are only two acceptance criteria: a newcomer can independently produce spec-compliant assets in their first week; and when a different person makes the same kind of asset, the specs come out identical.

### 2.3 Production Phase Model and Milestones

The phase model (prototype → vertical slice → Alpha → Beta → RC, with each phase's freeze and acceptance criteria) is in the Production Handbook (Production Handbook §2.2) and is not repeated here. Three additions for the studio context:

- Complete pipeline validation before the slice: the slice counts only once the toolchain can produce compliant assets at volume; if the pipeline isn't proven, measured hours don't count.
- A freeze is a contract between departments: Feature Lock freezes the feature list, Content Lock freezes the content list; anything added after a lock goes through the change process, not a casual "add it while I'm in there".
- A milestone deliverable equals a playable build plus each department's checklist. Acceptance goes item by item against the verifiable definitions in Production Handbook §2.2 — no passing a review on presentation decks.

### 2.4 Risk Register and the Content-Cut Process

The risk register follows the framework in Production Handbook §6, with two extra columns in the studio version: trigger conditions (e.g. "slice runs 50% over estimate", "outsourced work fails acceptance twice in a row") and owner. When a trigger trips, the contingency executes — no re-debating.

Common studio-level risks:

| Risk | Trigger signal | Contingency |
| --- | --- | --- |
| Key-role single point | One person's absence blocks a whole line | Each critical system is maintainable by at least two people; docs keep pace with the code |
| Cross-department dependency block | Downstream repeatedly waits on upstream deliverables | Interface contracts come first; liaisons align daily |
| Outsourcing quality below the bar | Two failed acceptances | Switch vendors or take it back in-house (process in Production Handbook §4.3) |
| Optimistic scheduling | Two consecutive weeks behind schedule | Start the content-cut contingency, not the overtime contingency |

Content cuts are called by the producer/director, not by vote; the order follows Production Handbook §3 (cosmetic skins → side content → extra modes → system depth → content volume, with the core loop last). One studio addition: for each cut, assess at the same time which department's hours are freed and which department faces rework, and announce the result to the whole team.

### 2.5 Relations with Publishers and Platforms

- With a publisher, milestones are usually tied to payment and acceptance: what gets delivered at demo, vertical slice, Alpha and release candidate goes into the delivery list in the contract appendix, aligned with internal acceptance criteria (Production Handbook §2.2).
- Platform certification has to start early: console certification (cert) requirements — save-data error handling, gamepad support, suspend/resume, crash reporting — must enter the requirements list before Alpha, or you rework after Beta (standards and preparation checklists in the Multi-platform Launch Playbook).
- Store assets, multilingual copy and trailers: build masters early per the general preparation pack in Multi-platform Launch Playbook §2, and export them in one pass after mass production; domestic channels have long license and review cycles, so factor them into the schedule from kickoff.
- External demos present a playable build and data, not a PPT.

## 3. Workflows and Cadence

### 3.1 Three-Layer Cadence

| Cycle | Action | Output |
| --- | --- | --- |
| Daily | 15-minute in-team standup answering only "yesterday/today/blockers" | Blockers reported the same day |
| Weekly | Friday playable build plus a cross-team sync | The build and a 3-line brief |
| Monthly | Risk-register review plus scope-statement review | An updated risk table |

Build discipline: the trunk is playable at all times, with at least one automated build a day; when a build breaks, stop the line and fix it immediately — higher priority than any new feature.

### 3.2 Review Mechanisms

Reviews come in three layers, with fixed frequency and outputs:

| Review | Subject | Frequency | Output |
| --- | --- | --- | --- |
| Requirements review | New features/new content before they enter the schedule | A fixed weekly window | Do / don't / simplify — choose one of the three |
| Milestone review | Phase exits (prototype, slice, Alpha, Beta, RC) | Once per phase | Item-by-item acceptance, retrospective and re-estimation of the remainder |
| Build review | The weekly playable build | Weekly | A list of experience problems (experience only, no code talk) |

Requirements reviews bring design, programming and art together to confirm gameplay value, cost and dependencies, avoiding the situation where "programming only finds out it can't be done after receiving the requirement". Review discipline: set the decision maker first in every session; debate a topic for one round only, with new opinions going through the change process; conclusions go into the decision records and are made public.

## 4. Collaboration and Division of Labor

### 4.1 Department Structure

| Department | Scope of responsibility | Main deliverables | Main interfaces |
| --- | --- | --- | --- |
| Design | Systems, levels, balance, narrative | Design docs, balance tables, levels | Programming, art |
| Programming | Gameplay, engine, toolchain, server | Playable builds, tools, performance reports | Design, art, QA |
| Art | Concept, characters, environments, animation, UI, technical art | Assets and specs | Design, programming |
| Audio | Music, SFX, voice-over and implementation | Audio assets and loudness standards | Art, programming |
| QA | Test plans, regression, device matrix | Defect lists and quality reports | Everyone |
| Production | Scope, schedule, risk, outsourcing | Schedules, risk tables, acceptance records | Everyone |

Division-of-labor principles:

- Every asset and system has exactly one owner; a review can involve many people, but the call is made by one.
- Write interfaces as contracts: the data formats programming provides to design, the delivery specs art provides to programming — fixed in documents.
- No single point of knowledge: at least two people can run key processes such as builds, releases, rigging and animation state machines.

### 4.2 Information Flow and Documentation Discipline

- Single source of truth: one authoritative document per topic; everything else references it (Production Handbook §4.1).
- Decisions stay unlocked: decision records are readable by everyone; meeting minutes go public within 24 hours.
- Anti-funnel: no decisions in one-on-one private chats; any verbal conclusion is added to the documents the same day.
- Change announcements: features cut and features added are announced weekly, together with the build brief.

### 4.3 Interfacing with Outsourcing and External Help

- Outsourcing follows the Production Handbook §4.3 process (requirements package → paid trial → milestone contract → staged acceptance → archiving), with a dedicated liaison assigned — otherwise communication overhead will consume your lead artist or lead programmer.
- Quantified acceptance criteria: dimensions, style comparison images, animation durations and delivery formats stated clearly once; no "it doesn't feel right" back-and-forth.

## 5. Tooling and Tech Stack Recommendations

Tools are where process becomes permanent; set the process first, then choose tools, and once chosen, don't change them often. Default tiers by purpose:

| Purpose | Default choice | Notes |
| --- | --- | --- |
| Tasks and scheduling | HacknPlan / Codecks / Jira / Feishu | Large projects require a two-tier structure of requirements and tasks, plus a milestone view |
| Docs and decisions | Notion / Confluence / Yuque | Single source of truth; writing the same thing in multiple sources is forbidden |
| Version control and assets | Git plus LFS; Perforce when asset volume is very large | Binary assets get commit-hook validation |
| Builds and CI | Jenkins / GitHub Actions / self-hosted build machines | Daily automated builds, distributed to test machines |
| Defect management | The same system as tasks, with S1–S4 severities | Severity definitions in Production Handbook §5 |
| Communication | IM plus the weekly build brief and screen-recorded reviews | Key meetings must have minutes |
| Telemetry (post-launch) | Self-built or third-party analytics services | Event design comes first; for privacy compliance see the Legal, Patents & Competition |

The hard criterion for tool selection: can it automatically validate assets and builds? Any step that relies on manual checking will inevitably fail once scale arrives.

## 6. Common Pitfalls

1. **Coordination cost underestimated**: adding people is not adding capacity, and communication links grow quadratically; adding people to a project that's already late usually makes it later still. Cut scope first, then consider adding people.
2. **An overlong vertical slice**: the slice has no timebox; a year passes without it finishing, and the budget is eaten up. The slice is a calibration tool: when it overruns, shrink its scope first, then re-estimate full production (Production Handbook §2.2).
3. **A quality bar that sways with progress**: vague acceptance criteria, or lowering them mid-project, leaves rework and delays waiting downstream. Once the bar is published, lowering it must go through the change process and be announced.
4. **Information funnels**: decisions stay in meeting rooms and private chats; downstream starts work on old information and only finds out during rework. A single source of truth plus published decisions is the cheapest insurance.
5. **Pipeline deferred**: mass production first, specs later, and asset rework multiplies; most obvious with art and outsourced assets — freeze the specs before mass production.
6. **Reviews with no decision maker**: the meeting ends with no one making the call, and the same topic gets meeting after meeting. Every review sets a decision maker and a deadline, and debates one round only.
7. **Process too heavy**: a 10-person team copies large-scale process wholesale — documents at every layer, weekly meetings nested in weekly meetings — until management overhead overtakes output. Trim the process to the scale; delete every meeting you can.
8. **Single points of key knowledge**: only one person understands the build system or the rigging process, and one vacation blocks everything. Document it and name a backup; eliminate single points while things are calm.
9. **Certification rework**: treating platform certification as wrap-up work; only after Beta do you discover that save-data, gamepad and other requirements are not met, squeezing the polish period.
10. **Outsourcing out of control**: without a dedicated liaison and quantified acceptance criteria, outsourcing turns into endless back-and-forth, and quality and schedule collapse together.

## Further Reading

- [Production Handbook](../../fundamentals/production/README.md): the master outline of phase models, scope control and risk registers, cited in several places on this page.
- [Art & Audio Handbook](../../fundamentals/art-audio/README.md): details on the Art Bible, asset specs and the import pipeline.
- [Multi-platform Launch Playbook](../../../playbooks/platform-launch/README.md): platform certification, launch preparation packs and version management.
- [Pitfalls & Anti-patterns](../../pitfalls/README.md): project-management and collaboration pitfalls; check them item by item at kickoff reviews.
- [Indie Survival](../../../playbooks/indie-survival/README.md): the counterpoint read from the other end of the scale.
