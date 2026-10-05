# Ludo Atlas · Pipelines · Build & Release

> **Pipelines & Workflows**. Positioning: turn the engineering-side work between "code freeze" and "builds delivered to channels" into a reproducible, traceable, rollback-capable pipeline — where versions match up, channels are kept distinct, and failures can be rolled back.
> Companions: Programming Handbook · Production Handbook · Multi-platform Launch Playbook · Pitfalls & Anti-patterns.
> Division of labor with the Multi-platform Launch Playbook: the Multi-platform Launch Playbook covers store review submission, qualifications and compliance; this page covers the engineering side — builds, packaging, signing, archiving and rollback — up to the point where "the build is in the channel's hands." This page does not write out specific commands; for interface details, defer to each engine's and platform's official documentation.

---

## 1. Positioning and Scope

The build and release pipeline solves one problem: **how does the same game content reliably become a build that every channel can use directly?** In this pipeline, "it runs" is not enough — four conditions are all required:

- **Reproducible**: any version you have shipped can be rebuilt from its corresponding code and assets, with identical behavior.
- **Traceable**: for any build, you can answer which commit it came from, which build number it carries, and who built it and when.
- **Channel-separable**: store builds, test builds and internal distribution builds each follow their own rules, with no cross-contamination.
- **Rollback-capable**: when something goes wrong live, you can fall back to the previous stable version within the agreed time limit.

When you need it: as soon as any build leaves your development machine (sent to testers, pushed to a test channel, submitted to a store), you need it. Solo developers can trim it to the minimum (version numbers plus archiving plus one-command builds), but "hand-assembling a build and sending it to players" should stop being acceptable from the first external tester onward.

Four concepts to pin down first; they recur throughout:

| Concept | Meaning | Discipline |
| --- | --- | --- |
| Flavor | Build variants split from the same codebase by purpose: dev, internal, test, release | Differences live in configuration, not in human memory |
| Build number | A globally increasing sequence number generated automatically on every build | Only increases, never reused, never entered by hand |
| Channel build | An artifact customized for a given store or distribution channel, carrying platform and channel identifiers | One build belongs to exactly one channel |
| Signing | The identity mechanism by which a platform verifies that "this build really came from you," backed by certificates and private keys | Certificates centrally managed; private keys never enter the repository |

Boundaries: launch processes, qualifications and review timelines live in the Multi-platform Launch Playbook and are not repeated here; build-farm setup and pipeline internals belong to the CI/CD pipeline (planned), and this page only defines the rules it must satisfy; version control and asset schemes are another pipeline's business — this page assumes code and assets can already be rebuilt from a commit.

## 2. Toolchain

The toolchain spans six stages, keeping exactly one primary tool per stage:

| Stage | Tool type | Common choices | Selection notes |
| --- | --- | --- | --- |
| Build entry | The engine's command-line export and headless build | The engine's built-in headless export plus an in-project build script | Every parameter goes into the script; humans only fill in version and flavor |
| Build orchestration | CI service plus a version-stamping script | Hosted CI or a self-hosted build machine | Clean environment, pinned toolchain versions, globally increasing build numbers |
| Packaging | Installer and compression tools | Platform installer generators, archive format tools | Settle the packaging format up front, per channel requirements |
| Signing | Platform signing tools | Each platform's official signing chain | Wired into the keystore; plaintext private keys never land on disk |
| Archiving | Artifact repository or object storage | In-house artifact repository, object storage plus a ledger | Append-only; searchable by version |
| Distribution | Internal distribution and test channels | Internal distribution pages, platform test tracks | Access-controlled, stamped with version and expiry |

Three selection disciplines:

- **One-command builds are the baseline; scripts live in the same repo as the project and get the same review.** A toolchain that needs five manual menu clicks to produce a build can neither be automated nor made stable; scripts scattered across individual machines might as well not exist — changes go through code review.
- **Build environments are separated from development environments.** Build machines carry no extra runtimes and leave no historical files behind, so "it passes on a clean machine" actually means something; a build that runs smoothly on your dev machine proves nothing (same methodology as the Programming Handbook).
- **Keys and certificates never enter the repository.** Build machines retrieve from a central keystore, with least privilege, and every retrieval is logged.

## 3. Process and Rules

### 3.1 Build Target Matrix: Platform × Flavor × Channel

The first dimension of the matrix is flavor. Four fixed flavors, purposes never mixed:

| Flavor | Purpose | Configuration stance | Who may receive it |
| --- | --- | --- | --- |
| Dev | Day-to-day debugging on your own machine | All debug features on, local services reachable | Developers |
| Internal | Daily verification by the team and QA | Ships with debug symbols, diagnostic entry points kept | Team-internal |
| Test | External testers and platform test channels | Close to release configuration, logging tightened | Controlled external parties |
| Release | Production stores and channels | All optimizations on, no backdoors, symbols stored separately | All players |

The second dimension is platform and channel — what the engineering side must prepare varies with the delivery format:

| Platform & channel | Delivery format | Platform-specific engineering items |
| --- | --- | --- |
| PC stores | Installer or archive, store-backend upload | Multiple architectures, delta upload, runtime packaging |
| Console platforms | Certification candidate builds | Platform toolchains, proprietary signing and version formats, certification checklist items |
| Mobile stores | Signed store builds | Certificates and provisioning profiles, hardening, package splitting, target OS version |
| Domestic Android channels | Channel builds | Channel identifiers, channel SDKs, multi-build management |
| Mini-game platforms | Platform packages | Subpackaging and remote assets, platform toolchains |
| Web | Static asset bundles | Cache strategy, path prefix, version fingerprint |

Matrix discipline: **combinations that are not in the matrix are not allowed to exist.** Every cell's build parameters (platform + flavor + channel) live in a single configuration table: optimization switches, log level, server address, channel identifier. When someone asks to "just change one thing and push a build," the change goes into the configuration table and then through the build; patching the artifact by hand is not allowed.

### 3.2 Version Numbers and Artifact Naming

The versioning system runs on two tracks:

- **Marketing version**: three segments (major, minor, patch), used to communicate with stores and players; it steps only at milestones and cannot be rewritten after release; it must increase monotonically within a channel — stores will reject a version number that has been reused.
- **Build number**: a globally increasing integer, incremented on every build, never reused, never rolled back; it comes from automation (commit count or a pipeline counter), and hand-entering it is forbidden. One marketing version usually maps to several build numbers; the ledger records which one actually went live.

Rules:

- The version and build number must be written **inside the artifact** (executable properties, app manifest, a visible in-game corner badge), not just in the file name; a player's bug-report screenshot must be able to carry both numbers.
- Artifact names carry the five locating elements: project, version, build number, platform and architecture, flavor and channel; all lowercase, no spaces or Chinese characters, one separator convention across the repo, so names parse from scripts and sort stably (example: `project-name-1.2.0-b514-win64-release-steam`, field order identical repo-wide).
- The mapping between commit hash and build number goes into the ledger; when tagging a release, the tag, the build number and the ledger must agree in all three places — if any one is missing, that release is void.

### 3.3 Build Automation: Command-Line Export and Trigger Rules

The foundation of automation is the engine's command-line export (headless build): without it, forget the rest; with it, orchestration can begin.

- **Manual triggers go through the same entry point**: humans may start builds, but only through the same scripts and the same parameter set (version, flavor, channel); "duck into the editor and export by hand" is banned as an emergency measure — every emergency leaves one more hole in the ledger.
- **CI triggers on three kinds of occasions**, each with its own job:

| Occasion | Trigger | What gets built | Who it serves |
| --- | --- | --- | --- |
| Daily | Every merge to main | Smoke build (launches, reaches a level) | Developers and QA |
| Scheduled | A fixed time each day | Full internal-flavor build | The team's daily verification |
| Milestone | Release tag or manual approval | Test-flavor and release-candidate builds | Testers and channels |

- **Fully automated inputs**: the build machine takes everything from version control and leaves no manual edits behind — commit first, then build; version, flavor and channel are injected as parameters; the build process is zero-interaction; any step that needs a human to answer on the spot is a gap in the automation.
- **The build output trio**: the artifact itself, the build log, and the ledger entry — one set per build, none optional.

### 3.4 Channel Build Management: Store Builds, Test Channels, Internal Distribution

One version can produce several channel builds, but **channel differences are only allowed to live in the packaging layer**: channel identifier, channel SDK, login and payment, server address, icon and name. The practice is one configuration per channel, injected at packaging time; writing channel differences as conditional branches in code is forbidden — every such branch forces a full regression pass per new channel.

- **Store builds**: the builds used for review submission and official launch. Once uploaded, a version number cannot be reused in that store; so the order is always "test channel validates first, store build second" — doing it backwards means experimenting with your review slots.
- **Test channels**: use the platform's built-in test tracks (mobile test groups, PC-store test branches, and so on); every build handed to testers comes with a three-line note: which version, when it becomes downloadable, and where to report problems. The build on the test channel and the upcoming store build must come from the same build parameters, differing only in the channel identifier.
- **Internal distribution and provenance**: internal-flavor builds go to a controlled internal distribution page or artifact repository, stamped with version number, build number and expiry, and cleaned up automatically on expiry; every channel build must be able to answer "which build number it came from, who uploaded it, and when." The same build artifact may not be redistributed after its configuration is changed.

### 3.5 Signing and Certificate Management (Concepts and Discipline)

Signing is the mechanism by which a platform verifies that "this build really came from you"; certificates and private keys are identity assets. Know the types and the consequences of failure first:

| Scenario | Credential form | Consequences of loss or expiry |
| --- | --- | --- |
| iOS | Distribution certificate and provisioning profile (both expire) | Once the certificate lapses you cannot ship again; an expired provisioning profile must be re-signed |
| Android | Signing key (including the upload key) | If the key is lost with no reset option, the path to updating the same app is blocked — the equivalent of starting over with a new app |
| Windows & macOS | Code-signing certificate, notarization credentials | No new builds can be signed; released versions are unaffected, but new releases are frozen |
| Console platforms | Platform-specific signing and credentials | Certification builds cannot be produced — a full stop |
| Mini-game platforms | Platform-side keys and backend configuration | Cannot upload or update |

Management discipline:

- **Central custody, two-person handling**: certificates and private keys go into a unified keystore (a password manager or a dedicated key vault); they must never exist only on individual machines, in email attachments or in chat logs; at least two people hold retrieval rights and know the process, and the handover checklist when personnel change must carry an item for "credentials and permissions."
- **Offline and off-site backups**: at least two offline backups of every private key, one of them off-site; the backups themselves are encrypted.
- **Registered and tracked**: every credential records its purpose, owner, expiry date and renewal method; renew ahead of expiry — an expired store certificate freezes your releases.
- **Least privilege and audit trails**: build machines retrieve credentials only as needed, and both retrieval and signing operations are logged; private keys never enter the repository or the build logs.
- **Regular drills**: run at least one drill of "switch to another machine, use the backup credentials, rebuild a signed build"; a backup that has never been drilled is not a backup.

### 3.6 Artifact Archiving and Rollback

What gets archived is not "all builds" but **every build that went out externally**: every test-channel and store version, every internally distributed build. The archiving quartet:

| Archived item | Purpose | Retention policy |
| --- | --- | --- |
| The artifact itself | Rollback and forensics | Forever for store-listed versions and console-certified versions |
| Debug symbol files | Resolving live crash stacks | Same lifetime as the corresponding version |
| Build logs | Reproduction and accountability | Kept at least until the version reaches end of support |
| Ledger entries | Version history and mapping | Forever |

Three preconditions for rollback — miss one and you cannot go back: complete archives (the old build and its old symbols can both be produced); reproducible builds (in the worst case, an old version can be rebuilt from its old tag with identical behavior); a drilled process (owner, time limit and operating path decided in advance — don't learn them the night of the incident).

The realistic view of rollback: most stores do not support downgrades; the standard engineering workaround is to rebuild the previous stable version with a higher version number and push it (or push a rollback patch), and console certification makes that path slower still. So "rollback time" is a number that goes into your contingency plan and gets drilled — not a slogan.

## 4. Automation and Acceptance

Machines handle form; humans handle judgment. All of the following checks are scripted and wired between build and distribution:

| Check | When it runs | What happens on failure |
| --- | --- | --- |
| One-command rebuild in a clean environment | Every release candidate | Blocks release |
| Version and build numbers unique and monotonic; naming compliant | Every build | Build fails |
| Release flavor free of debug backdoors and cheat entry points | Release-flavor builds | Blocks release |
| Signature verification passes | After packaging | Upload refused |
| Smoke test (launch, new save, load save, quit) | Every build | Blocks distribution |
| Spot-check on target devices | Release candidates | Blocks launch |
| Archiving quartet complete | Before distribution | Blocks distribution |

Acceptance looks at four things, all observable:

- For any version you have shipped, you can produce its artifact and corresponding commit the same day, and rebuild it.
- The version ledger matches the live versions in each store backend one-to-one — no "build not found."
- The rollback drill has been run at least once, and the owner can restore the previous stable version to the test channel within the agreed time limit.
- Zero manual interventions across the whole pipeline: from parameter injection to channel upload, nobody has to "help it along."

Three metrics to watch for yourself: manual intervention count, build failure rate, and the time from "decide to ship" to "downloadable on the test channel." One manual intervention is one too many; if the latter two keep climbing, the process is rotting — fix the pipeline before you talk about shipping.

## 5. Common Pitfalls

1. **Hand-built builds**: only one development machine can produce builds, parameters depend on memory, and releases stop the moment that person goes on vacation; artifacts don't match commits, and problems can't be reproduced.
2. **Version-number chaos**: hand-filled, duplicated, rolled back; stores reject uploads, player-side updates misbehave, support can't pin down a version, and the ledger becomes decoration.
3. **Lost certificates and private keys**: they exist only on individual machines or in chat logs; a personnel change or a disk failure freezes releases outright (§3.5).
4. **Tested only on the dev machine**: the dev machine has runtimes installed and historical files lying around, and the build crashes on any other machine; a clean build machine plus a smoke test is the baseline (§3.3).
5. **Backdoors left in the release flavor**: debug panels, cheat commands and verbose logging not turned off; when players find them after launch, that's an incident, not an Easter egg.
6. **Incomplete archives**: artifacts or symbol files missing, so rollback can't find the old build and crash stacks can't be resolved — none of the damage can be undone (§3.6).
7. **Test channel and store build diverge**: what was tested and what shipped don't come from the same build parameters, so the test conclusions are void.
8. **Channel differences scattered through code**: every new channel forces a full regression; differences belong in the packaging-layer configuration (§3.4).
9. **Keys or certificates committed to the repository**: one repo leak costs you both security and identity; credentials never enter version control (§2).

## Further Reading

- Programming Handbook: engineering infrastructure, build systems and the "measure first" methodology — this page is its release-side slice.
- Production Handbook: milestones, freezes and acceptance processes; release windows tie directly into the acceptance section (§4).
- Multi-platform Launch Playbook: the full flow of store review submission, qualifications and compliance; together with this page it forms the relay from engineering to launch.
- Pitfalls & Anti-patterns: a quick reference of release- and collaboration-related pitfalls — read alongside §5.
