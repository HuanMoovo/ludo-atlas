# Ludo Atlas · Pitfalls & Anti-patterns

> Positioning: a concentrated catalogue of the most common and most costly pitfalls across the entire game development process, as a three-column quick reference: "symptom → consequence → avoidance".
> Every pitfall carries a **cost rating**: 🔴 high (can ruin a project or a company) · 🟠 medium (heavy rework or a missed window) · 🟡 low (localized rework).
> Sources: public industry postmortems, community consensus and public cases; this is an experience-based compilation and does not constitute legal or business advice. Suggested use: walk the tables once at kickoff reviews and milestone postmortems.
> Companions: Legal, Patents & Competition · Multi-platform Launch Playbook.

---

## 1. Kickoff & Direction

| Pitfall (symptom) | Why it's fatal | How to avoid it | Rating |
| --- | --- | --- | --- |
| Making the first project a "dream game" (MMO/open world/RPG with online play) | The scope is far beyond individual capacity; 99% get abandoned; the goal of a first project should be "a complete release" | Ship 2–3 small releasable projects first; split the dream project into stages and use the earlier games as practice | 🔴 |
| Scope creep: features only get added, never cut | Development time grows exponentially; it never ships | Write a "what we won't do" list at kickoff; every added feature must cut one; filter with "can the gameplay be explained in under a minute" | 🔴 |
| Ignoring market validation: asking "who will buy this" only after it's done | A cold start with no wishlist buildup; dead on launch | Do competitor/audience research at kickoff (see the Competition chapter of the Legal, Patents & Competition); start public exposure mid-development | 🟠 |
| Picking platforms on a whim (PC/mobile/console/mini-games mixed together) | The platform decides input scheme, business model, review cycles and tech stack; switching mid-way = redoing half of it | Lock the first platform and the second platform at kickoff; consult distribution data for comparable games | 🔴 |
| Business model deferred (finish first, then think about premium/IAP/ads) | Free-to-play plus IAP requires a completely different economy and progression design; bolting it on later = tearing it all up | The kickoff document must state the business model; validate IAP/ad gameplay in the prototype phase | 🟠 |
| Chasing trends and hype (a genre suddenly blows up and you go all in) | Production takes 6–24 months; by launch the wave has passed; followers don't capture the top traffic | Ask yourself "would I have made this genre if I'd started two years earlier?"; combinatorial innovation beats naked bandwagon-jumping | 🟠 |
| The line between reference and copying out of control | "Over-referencing" art/code/copy can constitute infringement (see the Legal, Patents & Competition) | Reference gameplay mechanics (legal); never trace specific artistic expression; keep design-process documents | 🔴 |
| No answer to "why me?" | No differentiated selling point = competing with a sea of look-alikes for exposure | Answer in one sentence: the hook / the audience / the difference from competitors | 🟡 |

## 2. Design & Gameplay

| Pitfall (symptom) | Why it's fatal | How to avoid it | Rating |
| --- | --- | --- | --- |
| Building the system framework first and validating "is it fun" last | However elegant the framework, a boring core loop is worth zero | Build a "toy prototype" first (whitebox/paper): test only the core fun; playable within 10 minutes | 🔴 |
| Polishing too early: two weeks spent on the game feel of level one | Polishing before the gameplay is settled is wasted work; later gameplay changes tear it down again | Polish only after the core loop is frozen; use placeholder assets before that | 🟠 |
| Numbers picked by gut, never put in a spreadsheet | Balance problems can't be fixed systematically; players find the broken numbers after launch | All numbers into tables (CSV/asset files): batch-adjustable, regression-comparable | 🟠 |
| Severely underestimating content volume ("20 more levels and it's done") | Level production often takes 2–3× the time of code; content is a long-tail cost | Build one "benchmark level" first and time it, then multiply by the level count; content is the scissors gap | 🟠 |
| No onboarding/tutorial design | Data shows a large share of players churn within 5 minutes and never reach the core fun | Teach by doing through level design instead of a wall of text; playtest and observe with 3 strangers | 🟠 |
| Difficulty curve out of control (no difficulty testing) | Feedback polarizes: too easy = boring, too hard = negative reviews | Log death/failure rates per level; target: most players in the "slightly straining but passing" zone | 🟡 |
| Building "depth systems" too early (talent trees/crafting/reputation) | Low marginal fun but high cost; dilutes the core loop | Keep depth systems peripheral; the core loop completes within one screen | 🟡 |
| Solo development ignoring "designing for yourself" | Finding it fun yourself ≠ players finding it fun | External playtests at every milestone; release a public demo | 🟠 |

## 3. Programming & Architecture

| Pitfall (symptom) | Why it's fatal | How to avoid it | Rating |
| --- | --- | --- | --- |
| Premature optimization (squeezing performance before it even runs) | Wastes time and optimizes in the wrong direction (no measurement, no optimization) | Make it work → measure with a profiler → optimize the hotspots | 🟠 |
| Over-architecting for a "future big team" | Solo developers and small teams can't maintain heavy abstraction; iteration slows down | Design for the current scale: leave extension points, don't pre-build extensions | 🟠 |
| Hardcoded values and magic numbers scattered everywhere | Changing one number means opening ten files; no data-driven iteration | Keep numbers/config external (spreadsheets/assets); code only reads config | 🟠 |
| Global singletons/static state abused | Unit tests can't isolate anything; modules couple; collaboration conflicts spike | Dependency injection or explicit parameters; singletons only for genuinely global facilities | 🟠 |
| No automated tests or regression suite | Every change is hand-tested; the later it gets, the more afraid you are to change anything | Headless engine + unit/smoke tests into CI (e.g. gdUnit4/GameCI) | 🟠 |
| Save-compatibility problems: updates corrupt saves for returning players | A leading source of negative reviews; extremely expensive to fix | Version-stamped saves + migration functions; test the "old save → new version" path before launch | 🔴 |
| Frame-rate-dependent logic (timing by frame count, physics bound to frame rate) | Behavior differs across devices; high-refresh devices misbehave | Fixed-timestep physics + delta-time logic; test for frame-rate independence | 🟠 |
| Single-player mindset + adding online later | Network synchronization requires redoing the architecture layer (state/determinism/rollback) — effectively a rewrite | Decide the network model at kickoff (see §8); it cannot be retrofitted | 🔴 |
| Platform adaptation deferred (gamepad/resolution/multi-language/save paths) | Platform-wide problems only surface before launch, delaying the release | Integrate early: input abstraction layer, resolution scaling, localized strings kept external | 🟠 |
| Choosing an engine wrongly (watching only popularity, not ecosystem/platform/talent) | Switching engines mid-way = a redo; niche engines lack tutorials and plugins | Evaluate on: target-platform support, ecosystem plugins, community activity, hiring market | 🔴 |
| No memory or asset-loading budget (mobile OOM crashes) | Crash rates spike on low-end devices; store ratings suffer | Set a memory budget sheet; load/unload per scene; a downgrade strategy for low-end devices | 🟠 |
| No logging, crash reporting or version numbering | Live issues can't be diagnosed; player reports have nothing to trace | Wire up crash monitoring (Bugly/Crashlytics/Sentry); a version-number convention | 🟠 |
| Case-sensitive asset-path problems (developed on Windows → crashes on Linux/Android) | Blows up only on the release platform; not reproducible locally | All-lowercase naming convention + CI builds on multiple platforms | 🟡 |
| No commit conventions, messy repository management (large files in git) | Repo bloat, collaboration conflicts, painful rollbacks | Manage binary assets with Git LFS; commit-message conventions; branching strategy (see pipelines/version-control) | 🟡 |

## 4. Art & Content

| Pitfall (symptom) | Why it's fatal | How to avoid it | Rating |
| --- | --- | --- | --- |
| Underestimating the art workload ("a simple art style is fast") | Art often takes 50%+ of total hours; the simpler the style, the more easily it looks bad | Make an asset list and per-piece time estimates first; scaffold with free assets, then replace | 🔴 |
| Inconsistent style (a patchwork look) | Reads as cheap at a glance; the presentation suffers | Set an Art Bible (palette/line/lighting rules); check every new asset against the benchmark image | 🟠 |
| Inconsistent specs (sizes/orientation/pivots/naming in chaos) | Alignment explodes inside the engine; animation and VFX get reworked | Asset spec sheet + naming convention + import checklist | 🟠 |
| Misused copyrighted assets (fonts/textures/music from unreliable sources) | Demand letters and even takedowns with claims (font enforcement is rampant in mainland China) | Use only assets with a clear license chain; log every source (asset ledger); free-for-commercial-use font lists in Resources | 🔴 |
| AI assets used without records, placeholder assets never replaced | Undisclosed or leftover placeholder assets discovered at launch (repeated public blowups) | Keep an AI asset ledger (tool/model/degree of modification); full audit and replacement before launch | 🔴 |
| AI-generated style drift (a set gets less and less consistent) | Heavy manual patching needed; ends up slower | Fix style anchors + a LoRA/reference-image workflow; generate in batches, select in batches | 🟡 |
| Atlas/loading strategy out of control (a thousand loose images packed directly) | Slow loading, large build size, high memory | Atlas planning + compression rules + a build-size budget sheet | 🟡 |
| UI/UX left to last ("paint the skin once the features are done") | Interaction problems surface too late; rework is expensive | Low-fidelity UX first; define UI rules together with the art style | 🟠 |

## 5. Audio

| Pitfall (symptom) | Why it's fatal | How to avoid it | Rating |
| --- | --- | --- | --- |
| Inconsistent loudness (quiet BGM, exploding sound effects) | A miserable player experience; forced to turn the volume down, they miss critical feedback | A project loudness standard (unified around -14 LUFS, for instance); bus limiting at playback | 🟠 |
| Loop points handled badly (pops/gaps) | The details expose a cheap feel | Every looping track gets a seamless-loop test; keep the toolchain fixed | 🟡 |
| Audio format and size out of control (WAVs dumped straight into the build) | Build size balloons; mobile download conversion drops | Compression rules (an ogg/mp3 strategy) + an audio size budget | 🟡 |
| Unclear music licensing scope (bought "usage rights" but can't ship on Steam) | Discovered at release that the license doesn't cover commercial/global/perpetual use | Write it into the contract: commercial, worldwide, perpetual, modifiable, usable in sequels and promotion | 🔴 |
| Underestimating the SFX count (one action needs 3–5 variants) | Late SFX patching drags the schedule | List SFX at kickoff (enumerated by interaction event) | 🟡 |

## 6. Project Management & Teams

| Pitfall (symptom) | Why it's fatal | How to avoid it | Rating |
| --- | --- | --- | --- |
| No milestones or acceptance criteria (the "90% done" trap) | The last 10% eats 90% of the time; schedules are forever optimistic | A milestone = a playable build (clickable, playable), not "the code is written" | 🔴 |
| Perfectionism and endless polish | The project never ships; testing time gets squeezed out | Define "good enough"; freeze on schedule; keep polish on its own prioritized list | 🟠 |
| Chronic crunch (permanent overtime) | Research consistently shows sustained overtime lowers output and raises error rates; people quit | Refuse normalized overtime; use scope control instead of stacked hours | 🔴 |
| Invisible tasks (no board, no weekly rhythm) | Blockers are felt, not seen; collaborators block each other | A lightweight board (HacknPlan/Codecks/Feishu) + a 30-minute weekly sync | 🟡 |
| Oral agreements: partner splits and outsourcing terms living in WeChat chats | No evidence when disputes come; the relationship and the project both lose | Put every financial agreement in writing (see the Contracts chapter of the Legal, Patents & Competition) | 🔴 |
| Outsourcing out of control (no acceptance criteria, no interim deliveries) | Rework is unbounded; money spent with no usable assets delivered | Pay by milestone; define each delivery precisely (format/specs/source files) | 🟠 |
| Hiring/expanding too early | Communication costs rise; cash flow snaps | Outsource what you can instead of hiring; automate instead of adding process | 🟠 |
| Solo-developer burnout (isolation, no positive feedback) | One of the leading causes of abandonment | Join communities/jams; keep a public devlog for feedback; fix a rest rhythm | 🟠 |
| Team communication failures (key decisions only in DMs, known to no one) | Duplicated work, contradictory decisions | Decision records (ADRs); centralized documents (single source of truth) | 🟡 |

## 7. Testing & Release

| Pitfall (symptom) | Why it's fatal | How to avoid it | Rating |
| --- | --- | --- | --- |
| Store page and wishlists started too late | Steam wishlists are a compounding asset; too late = no exposure at launch | Put the store page live at the "playable demo" stage; accumulate wishlists continuously | 🔴 |
| No external testing before launch | Launch-day bugs trigger a review avalanche; negative reviews are irreversible | Closed test → public demo → release; stand up a feedback channel | 🔴 |
| Underestimating review cycles (console certification/Apple review/game licenses) | Miss the release window; coordinated marketing wasted | Reserve a 2–3 month review buffer; allow 2–6 weeks for console certification | 🟠 |
| Device-compatibility blind spots (testing only on the dev machine) | Low-end crashes, resolution glitches, peripheral problems | Build a device matrix (low/mid/high-end + mainstream resolutions); cloud device testing (WeTest/Testin) | 🟠 |
| Release-day collision (launching the same day as a major title) | Exposure gets swallowed whole | Watch the release calendar (Steam's upcoming releases); avoid big titles in the same genre | 🟠 |
| No hotfix plan at launch (can't fix, afraid to fix) | A serious bug sits for a week; the rating collapses | Drill the hotfix pipeline (branch/build/upload); prepare a rollback plan | 🟠 |
| Machine translation shipped as-is, no LQA | A top source of negative reviews (especially in text-heavy genres) | LLM translation + glossary + sampled human close reading; native-speaker proofreading for key UI | 🟠 |
| Ignoring platform-required features (achievements/cloud saves/gamepad/Steam Deck rating) | Platform requirements force rework; recommended placements missed | Tick through each platform's checklist item by item (see the Multi-platform Launch Playbook) | 🟡 |

## 8. Multiplayer & Online Games

| Pitfall (symptom) | Why it's fatal | How to avoid it | Rating |
| --- | --- | --- | --- |
| Wrong network model (P2P for competitive play, lockstep for real-time) | Architecture-level rewrite; latency/cheating problems become unsalvageable | Decide the model at kickoff: state sync / lockstep / server-authoritative; follow proven patterns from the genre | 🔴 |
| Anti-cheat only considered at launch | Cheaters flood in at launch; the economy collapses | Make critical logic server-authoritative; integrate anti-cheat early (see Resources §8.4) | 🔴 |
| No server-cost model (free players estimated like paying ones) | The monthly bill spirals on a surge; rate limiting wrecks the experience | Build a CCU cost sheet (with peak and DDoS headroom); open up only after load testing | 🔴 |
| Mismatched real-time expectations (playing cross-region like it's local) | Gameplay experience goals don't match network reality | Discuss the latency budget at design time: turn-based/asynchronous play has low network demands — prioritize it | 🟠 |
| Careless account and save design (server merges/migrations become hard) | No merges or economy changes during live-ops; player-asset disputes | Separate account and character data; design server IDs and character IDs with a merge path reserved | 🟠 |
| Over-promising updates (a road map of tall tales) | Promises that can't be kept trigger trust crises (multiple public cases) | Put only "definitely doable" items on the road map; phrase in tiers: "planned" and "possible" | 🟠 |
| Ignoring mainland-China online-game compliance (game license/anti-addiction/real-name) | Operating in violation = takedown/penalties; no license, no charging | See Multi-platform Launch Playbook §7, the online-game-specific flow (game licenses, the real-name system at wlc.nppa.gov.cn) | 🔴 |
| No shutdown or refund plan | Mishandled shutdown notices and player compensation risk public backlash and lawsuits | Write the shutdown plan before launch (notice period, compensation, data export) | 🟠 |
| Charging during testing crosses the line (selling "test bundles" without a license) | A clear violation; may force a takedown and rectification | Free testing only while unlicensed; charging must wait for the license (same for mini-game virtual payments) | 🔴 |

## 9. AI Workflows

| Pitfall (symptom) | Why it's fatal | How to avoid it | Rating |
| --- | --- | --- | --- |
| AI content not disclosed as platforms require (Steam and others) | Breaches the platform agreement, risking takedown; a player-trust crisis | Follow the Steam content survey: distinguish "pre-generated/runtime-generated" disclosures; internal-tool exemptions still need records (see design doc §14.9) | 🔴 |
| Letting an AI agent rewrite the project overnight (MCP write access wide open) | The project gets polluted, scenes break, nothing is traceable | Tier permissions (read/write/dangerous); commit before operations; isolate work branches | 🟠 |
| Hallucinated APIs / no grasp of the engine lifecycle | Generated code that "compiles but won't run", or hides performance landmines | Generated code must pass a review checklist: lifecycle, performance, error handling; verify in small steps | 🟠 |
| AI-generated assets drift in style; fixing them costs more than drawing | Output is unusable; time wasted | Fix style anchors and workflow templates; track batch pass rates | 🟡 |
| Vast amounts of AI code nobody understands (a maintenance disaster) | Bugs come up with nobody able to fix them; team capability hollows out | Human-readable docs for critical systems; core logic must be human-rewritten/read closely | 🟠 |
| Asset sources and licenses unrecorded (AI output can carry third-party rights disputes too) | Nothing to show in enforcement actions or platform reviews | Asset ledger (tool, model, date, degree of human modification); see the Legal, Patents & Competition | 🟠 |

## 10. Live-Ops & Community

| Pitfall (symptom) | Why it's fatal | How to avoid it | Rating |
| --- | --- | --- | --- |
| Pricing mistakes (too low won't save the reputation, too high won't convert) | Revenue takes a direct hit; the discount room is locked shut | Benchmark the price band of comparable quality in the same genre; a 10–15% launch discount is standard | 🟠 |
| Arguing with players / retaliating against negative reviews | A PR disaster; the screenshots live forever | In public, always calm, specific and grateful for feedback; keep templates for negative responses | 🔴 |
| Update cadence breaking down (weekly promised, yearly delivered) | The community drains away; sentiment flips | Promise only a "sustainable cadence"; small updates count as updates | 🟠 |
| Telemetry and privacy non-compliance (data collected without consent/without a policy) | Store takedowns, regulatory penalties (GDPR/PIPL) | The privacy policy covers every data point collected; minimize collection; extra care around children | 🔴 |
| No support or refund process | Disputes pile up into public backlash | Prepare an FAQ/refund guide in advance; follow platform policy | 🟡 |
| Neglecting community management (selling only, never talking) | No organic word of mouth or UGC spread | A fixed home base (pick one primary and two secondary from Discord/QQ/Tieba); developers answer posts themselves | 🟡 |
| Content direction held hostage by negative reviews (the loudest voices win) | Core users churn | Build an "opinion weighting" mechanism: data + core players + your own vision | 🟡 |

## 11. Legal & Compliance (see the Legal, Patents & Competition for details)

| Pitfall (symptom) | Why it's fatal | How to avoid it | Rating |
| --- | --- | --- | --- |
| Game name promoted without a trademark search | Squatted or hit with infringement complaints; forced to rename (huge sunk cost) | Search the China Trademark Office at kickoff; register early in key markets (classes 9/41/42) | 🔴 |
| Outsourcing without a written copyright assignment | Legally the copyright may stay with the creator; you can't assert your rights | Contracts must include a written "copyright assignment" clause and a deliverables list | 🔴 |
| Shipping closed-source with GPL/AGPL code | License violation = infringement; forced to open-source or refactor (AGPL binds server-side too) | Dependency list (SBOM) + license scanning; check engines and libraries one by one | 🔴 |
| Missing privacy policy, or one that doesn't match actual collection | App-store rejections; regulatory penalties | Generate the privacy policy from the real data flow; audit before launch | 🔴 |
| Monetizing before the game license exists (including mini-game virtual payments) | A clear violation | See the online-game section of the Multi-platform Launch Playbook | 🔴 |
| Gacha/loot-box odds undisclosed or non-compliant | Penalties for violations; regulation in multiple countries (odds and pity mechanics must be transparent) | A published-odds page + compliance review; watch loot-box regulation trends by region | 🔴 |
| Broken licensing chains for music/fonts (agency sublicensing problems) | Claims or takedowns | Accept only verifiable license documents; keep purchase receipts | 🔴 |

---

> **How to use this**: once linked into the repository, this section is intended to go live as `docs/pitfalls/` and to be cited section by section in every milestone review template; community contributions of new pitfalls follow the four-part format "symptom/consequence/avoidance/rating" (template in `templates/`).
