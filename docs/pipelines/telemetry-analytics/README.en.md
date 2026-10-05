# Ludo Atlas · Pipelines · Telemetry & Analytics

> **Pipelines & Workflows**. Positioning: turning "how players actually play" into queryable, trustworthy, actionable data — a complete data pipeline covering event design, collection, governance, dashboards and privacy minimization.
> Companions: Live-Ops & Growth · Legal, Patents & Competition Handbook · Production Handbook · Pitfalls & Anti-patterns.
> Audience: minimum event tracking (crashes, sessions, the core funnel) should be in place as soon as you reach playable testing; small single-player titles can trim it, but the event dictionary and data minimization are the two things you never cut. Boundary with the Live-Ops & Growth: that handbook is about using the numbers to make live-ops decisions; this page is about where the numbers come from and whether they can be trusted.

---

## 1. Positioning and Applicability

The telemetry and analytics pipeline is a channel that turns behavior into evidence: events start in gameplay code, pass through collection, governance, storage and aggregation, and arrive at dashboards and decision meetings. It is not responsible for "what to do with the numbers once you have them" — that is the territory of the Live-Ops & Growth; it is responsible for "can the data be trusted, can the questions be answered":

- **Traceable**: every data point can be traced to an event definition and a trigger moment; definitions are written in the dictionary, not passed around by word of mouth.
- **Purposeful**: every event carries one specific question and one consumer; define the question before adding event tracking (§3.1).
- **Bounded**: collection defaults to minimization — anonymize when you can, don't collect what you don't need (§3.3).

Get the five stages straight first; the rest of the page keeps referring to them:

| Stage | What happens | Owner |
| --- | --- | --- |
| Event design | Define events, properties and definitions | The event dictionary, in the same repo as the code |
| Collection | Client-side triggering, buffering, uploading | Client engineering |
| Governance | Deduplication, cleaning, retention periods, deletion paths | Data-side processes |
| Storage and query | Raw-detail retention, aggregate tables, definition-based rollups | Data warehouse or analytics store |
| Consumption | Dashboards, reports, alerts and decision records | Dashboards and regular meetings |

When is this pipeline worth setting up: when you can already ask "where do players get stuck, do they come back, how long is a run" but have no data to answer with; when launch is near and you need to watch crashes and the core funnel. During prototyping you can keep just crashes and one key behavior and find direction through playtests and interviews; once you reach playable testing, minimum event tracking should be in place — bolting it on the night before launch throws away all the early curves you most need to see.

## 2. Toolchain

The chain has five segments, each keeping one primary tool; selection starts with ownership:

| Segment | In-house option | Service option | Selection notes |
| --- | --- | --- | --- |
| Collection SDK | In-house: batched, asynchronous, resends from the last checkpoint | Vendor SDK (Firebase, GameAnalytics and the like) | Reporting must not cost frames; offline resend needs a window |
| Ingestion and processing | Self-hosted endpoint plus scheduled cleaning | Vendor endpoint | Deduplication, clock handling and environment isolation are this segment's job |
| Storage and query | Cloud data warehouse or columnar store (BigQuery, ClickHouse and the like) | The vendor's built-in storage | Work out raw-detail retention and query cost up front |
| Dashboards and reports | Open-source BI (Metabase, Grafana and the like) | Vendor dashboard | Metric definitions follow the dictionary, not the tool |
| Crashes and performance | Self-hosted reporting plus aggregation | Crash collection service (Crashlytics, Sentry and the like) | A separate channel from gameplay events — same source, different route |

The build-vs-buy trade-off is the core of selection:

| Dimension | Service | In-house |
| --- | --- | --- |
| Startup cost | Low — plug in the SDK and you have a dashboard | High — every segment has to be built |
| Speed of change | Constrained by the vendor's release cycle and quotas | Add what you want, when you want |
| Data sovereignty | Data sits with the vendor; cross-border transfer and compliance need assessment | Everything stays in your own store — maximum transparency |
| Cost | Rises with event volume and often exceeds budget at scale | Mostly fixed costs; labor buys control |
| Maintenance burden | Close to zero | Someone has to keep it alive long term |
| Fits | Teams with no data-engineering staff; the validation phase | High event volume, compliance-sensitive, special requirements |

Three rules: service first, build later is the common route (use a service to see which dashboards people actually look at, then decide what moves in-house); the event dictionary always lives in your own repo (tools can change, definitions must not follow the vendor); free-tier quotas, retention periods and sampling are hidden costs — read the fine print before choosing.

## 3. Process and Conventions

### 3.1 Define the Question First, Then Add Event Tracking

The forward chain is fixed: question → hypothesis → metric → event → dashboard. Done in reverse — instrumenting a pile of events first and looking for a use later — you get a roomful of curves nobody watches. The event skeletons for three kinds of questions:

| Question type | Typical question | Core events | Key properties |
| --- | --- | --- | --- |
| Funnel | Where do players get stuck? What is the conversion from tutorial to first win? | Entry and completion of key steps, e.g. `tutorial_step_start`, `tutorial_step_complete` | Step number, duration, result |
| Retention | Do players come back? Which cohort vanishes by day two? | Session start `session_start` plus the first key action, e.g. `first_win` | Channel source, version, first-seen date |
| Curves | What level are duration, difficulty and economy at? | Start and end of a run, e.g. `level_start`, `level_end` | Level number, win/loss, duration, score or resource amount |

- The action for a funnel question is to change flow and onboarding; for a retention question, to change the early experience; for a curve question, to change the numbers. The three kinds of questions differ in data flow and dashboard shape — don't cover them all with one big table.
- Write the hypothesis before pulling data: predict "more than 30% churn at tutorial step two", then compare against the measurement. With no prediction up front, hindsight explanations belong entirely to intuition.
- Quantitative and qualitative are two legs: telemetry answers "how many, at which step"; playtests and customer support answer "why". Numbers alone don't know the reason; feel alone doesn't know the range.

### 3.2 Event Naming and Property Conventions

Event names are an interface — shipping them is a promise. Once the conventions are fixed, write them into the repo:

- Naming format: all lowercase, underscore-separated, verb last, in the form `object_action` or `flow_step_action`; versions, numbers and parameters never go into the name.
- Semantics only grow, never change: to change semantics, add a new event and deprecate the old one; deprecation goes through a stop-collection announcement, with a migration window for dashboards.
- Three rules for properties: common fields (time, session, version, platform, channel, region) are attached by the collection framework; enum values use fixed lowercase English constants — free text is forbidden; numeric values carry a unit convention, e.g. `duration_ms`.
- Property minimization: each event carries only the properties needed to answer its question. Every extra field is both a cost and an extra privacy surface.

The event dictionary is the single source of truth — one table settles everything:

| Event name | Trigger moment | Required properties | Question it answers | Consumer |
| --- | --- | --- | --- | --- |
| `session_start` | Entering the game's main screen | Channel, version | Activity and retention definitions | Health dashboard |
| `level_end` | At run settlement | Level number, win/loss, duration | Difficulty and duration curves | Gameplay dashboard |
| `purchase_complete` | Payment callback succeeds | Product ID, price tier, currency | Purchase funnel and revenue definitions | Live-ops dashboard; definitions align with the Live-Ops & Growth |

The dictionary lives in the same repo as the code and changes go through review; before adding an event, answer three questions: what question does it answer, who consumes it, and will anyone still look at it in six months. If you can't answer all three, don't add it.

### 3.3 Data Minimization and Privacy Compliance

The principle in one sentence: as long as the questions can still be answered, collect as little as possible. For the full list of regulations and platform rules, see the Legal, Patents & Competition Handbook (Legal, Patents & Competition Handbook §6.1, covering GDPR, CCPA, COPPA, PIPL and store privacy labels); this section lists only the actions the pipeline side must implement:

- Minimum by default: for every field, first ask "without it, can the question still be answered"; if it can, don't collect it; profile fields such as age and gender are optional and skippable.
- Identifier discipline: device-level anonymous IDs are stored separately from account IDs, resettable and unlinkable; don't request system permissions unrelated to the game — contacts, photo library, precise location and clipboard stay untouched.
- Consent and toggles: the privacy notice on first launch matches actual collection item by item; provide a switch that turns data collection off, and the game keeps working with it off.
- Lifecycle: every data category gets a retention period and is purged when it expires; account deletion and erasure requests must reach the detail store, the aggregate store and the backups — if you can't actually delete it, it isn't compliant.
- Children and teens: for genres aimed at children or likely to reach them, parental consent and minimization standards are stricter — run the plan past the children's-data clauses in the Legal, Patents & Competition Handbook first.
- SDK ledger: register every third-party collection SDK — what is installed, what it collects, where it sends it; store privacy labels and data-safety forms must match the ledger item by item. A mismatch is a takedown-level risk, not a copywriting problem.

### 3.4 Collection Discipline and Data Quality

- Client discipline: reporting is asynchronous, batched and droppable, and never drags on frame rate or input under any circumstances; when the network drops, write to a local buffer and resend within a window once it recovers; every event carries a unique ID for deduplication.
- Time basis: the server's receive time is authoritative, client time is diagnostic only; fix the daily-report time basis across time zones in advance.
- Environment isolation: three sets of keys — dev, test and production; test builds and bot data never enter the production store; isolate from day one, because cleaning up afterward costs an order of magnitude more.
- Four quality checks: key events must arrive when triggered, latency within the window, definitions stable after deduplication and out-of-order handling, and cross-validation against store- or platform-side data. Turn the four checks into a routine report, not an ad-hoc spot check.
- Flow monitoring: set a baseline for each event's daily arrival volume and alert when it deviates past the threshold. If the flow dies at midnight, you should know by morning — not discover it at the end-of-month review.
- Technical side first: crash rate, startup failure rate and frame-rate distribution are the first problems the data pipeline has to serve; if the technical side can't ship, no gameplay dashboard, however complete, can deliver.

### 3.5 Dashboards and Decision Habits

- Layer the dashboards, keeping only key metrics per layer: health layer (crashes, retention, core funnel) → gameplay layer (levels, systems) → economy layer (revenue and spend, if any) → technical layer (performance, build size). Start with 5–10 metrics per layer; to add one, take one off first.
- Every metric on the board gets a three-piece kit: an owner, a comparison basis (last week or the baseline), and a trigger action (what to do when it falls by how much). Metrics with no trigger action come off the board.
- Cadence: the automated daily report sends a summary, the weekly meeting covers only anomalies, and definitions are reviewed monthly. Meetings look at anomalies and actions, not reciting numbers line by line.
- Data assists, it does not lead: numbers tell you where the problem is; players tell you why. When a metric worsens, break it down by dimension first (which cohort, which version, which platform), then decide the action; if you can't break it down, go play the game.
- Decision records: for important changes, write down the rationale and the expectation and come back to reconcile after launch; an expectation that didn't happen is also a conclusion — write it into the postmortem (for the method see the Production Handbook (Production Handbook §9)).
- Anti-vanity: don't look at total registrations or cumulative downloads; look at the active-player distribution and duration percentiles. Average duration lies; the median and the tail tell you what's going on.

## 4. Automation and Acceptance

Machines check format and completeness; humans check definitions and questions. Script the checks below wherever possible and attach them to the build and the data chain:

| Check | When it runs | On failure |
| --- | --- | --- |
| Event registration check | At build time, tracking code is checked against the dictionary | Build fails |
| Property schema validation | Before reporting and before storage; checks types, required fields and enums | Drop and alert |
| Critical-path assertions | Automated tests run critical paths and assert that events fire | Test fails |
| Arrival volume and latency monitoring | Daily baseline comparison | Alert; on-call follows up |
| Privacy scan | Before release, scans for sensitive fields and unregistered SDKs | Release blocked |
| Dashboard refresh | Scheduled job recomputes aggregates | Anomalies auto-flagged |

Acceptance looks at four things, all observable:

- Take a new question; from defining the metric to the dashboard producing an answer, no verbal explanation is needed anywhere.
- Spot-check three key events: the structure and magnitude of live data match the dictionary, and the trigger moments match the documentation.
- Turn off the entire collection pipeline: gameplay and frame rate are unaffected, and the data side backfills from the buffer as agreed or discards safely.
- File a player deletion request: the player's raw data cannot be found in the detail store, the aggregates or the backups.

The pipeline's own four metrics: event arrival rate, schema violation count, the cycle time from question to conclusion, and the share of dashboard metrics that carry a trigger action. The first three measure health; the fourth measures whether this pipeline actually takes part in decisions.

## 5. Common Pitfalls

1. **Copycat tracking**: collecting whatever others collect, with nobody looking at it afterward. For each event, write down the question it answers and who consumes it first; if you can't, don't collect it (§3.1).
2. **Metrics without action**: the dashboard refreshes daily and no number has ever triggered an action. Going on the board means fixing the owner, threshold and action; if you can't, leave it off (§3.5).
3. **Privacy overreach**: casually collecting device information and user profiles because "it might be useful later". Minimization is the default; children's data goes through the regulations first (§3.3, Legal, Patents & Competition Handbook).
4. **Numbers without players**: retention dips, the reports show no reason, and the only move is to throw rewards at the problem. Numbers set the range, players explain the reason — walk on both legs (§3.1).
5. **Naming and definitions each going their own way**: engineers rename after the fact, live-ops works to its own definitions, and two numbers fight it out in the meeting. The dictionary is the single source; definition changes go through the same review (§3.2).
6. **Tracking that eats frames**: reporting waits on the network synchronously and the stutter shows up in players' faces. Collection is asynchronous, batched, droppable (§3.4).
7. **Unnoticed reporting loss**: bad networks, app updates, SDK failures — a corner of the data goes missing and decisions follow a broken curve. Arrival-volume monitoring and a resend window are standard equipment (§3.4).
8. **Test data polluting production**: test builds, bots and dev-machine data all land in the production store and inflate the metrics. Isolate environments from day one (§3.4).
9. **The dictionary left unmaintained**: the code changed and nobody updated the dictionary; six months later you don't dare trust the table yourself. Adding and deprecating events goes through review and announcement (§3.2).
10. **Missing technical telemetry**: instrumenting gameplay but not watching crashes and startup failure rate means chasing churn in the wrong direction. Technical data and gameplay data go on the board together (§3.4).

## Further Reading

- Live-Ops & Growth: the consumer side of metric definitions and live-ops decisions; that handbook handles using numbers to make decisions, while this page handles where the numbers come from and whether they can be trusted.
- Legal, Patents & Competition Handbook: privacy regulations, platform privacy labels and children's-data clauses — the legal drafting source behind §3.3 (§6.1).
- Production Handbook: event tracking and dashboards are scheduling items too; the postmortem methods explain how data is used in project postmortems (§9).
- Pitfalls & Anti-patterns: a list of concrete cases around telemetry, data and privacy, to read alongside §5.
