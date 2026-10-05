# Ludo Atlas · Pipelines · Version Control & Collaboration

> **Pipelines & Workflows**. Positioning: bring code, binary assets and scene files under one version control discipline, so that merges, rollbacks and release builds all leave a traceable record.
> Companions: Programming Handbook · Production Handbook · Pitfalls & Anti-patterns · Multi-platform Launch Playbook.

---

## 1. Positioning and Applicability

A game repository is a mix of three kinds of files whose version control needs pull against one another:

| File type | Typical examples | Version control difficulty |
| --- | --- | --- |
| Source text | Scripts, configs, shaders | Readable and mergeable; mostly stays out of the way |
| Binary assets | Textures, audio, models, video | Not readable, not mergeable; every change replaces the whole file |
| Semi-structured files | Scenes, prefabs, blueprints, levels | Nominally readable; merges are extremely prone to semantic corruption |

The default habits of a pure-code project (branch freely, parallelize freely, merge whenever) cause cascading failures in a game repository: clones get slower and slower, conflicts become impossible to fix, and artists' work gets silently overwritten. The goal of this pipeline is to push that class of accident close to zero.

If any one of these signals applies, adopt the reinforced tier:

- The repository exceeds 1GB, or a clean clone takes several minutes to finish;
- Someone on the team works in art, level design or audio, and their output is not code;
- Accidents like "who overwrote my scene" or "why won't this asset roll back" have already happened;
- You need to produce builds for multiple platforms and multiple channels from the same codebase.

Adopt it by scale: solo projects first put up the three lists in §3.1; teams of two to ten implement all of §3.2 through §3.5; above ten people, layer on the file locks of a centralized asset library and stricter release-branch discipline.

Three underlying principles; every detail that follows is an expansion of them:

1. The repository is the single source of truth: a change that is not in the repository does not exist, and verbal sync does not count.
2. Anything regenerable never enters the repository: caches, import intermediates and build outputs are ignored across the board; they can be rebuilt at any time.
3. Large binaries get their own channel: through LFS or into a centralized asset library, never mixed into ordinary history.

## 2. Toolchain

| Area | Tool | Notes |
| --- | --- | --- |
| Core version control | Git; asset-heavy teams evaluate a centralized option such as Perforce | Git has the widest ecosystem; centralized options ship with file locking, suited to artists editing the same files in parallel at high frequency |
| Large-file storage | Git LFS | Only pointers stay in the repository; the real content lives in a separate storage area |
| Ignore and attribute lists | `.gitignore` and `.gitattributes` | The carrier of every convention; maintain them continuously as tools and asset formats evolve |
| Engine integration | The engine's built-in version control window and merge tools | Let non-programmers commit from inside the engine and reduce manual operations |
| Commit validation | Local hooks: pre-commit checks and commit message validation | Intercept cache files, oversized files and format errors |
| Continuous integration | Hosted CI (Actions, GitLab CI, Jenkins-type) | The final line of defense: build, test, scan, package |
| Diff and merge assistance | GUI clients and text diff tools | Lower the barrier to entry; handle text merges |
| Backup | A remote mirror plus LFS object backups | LFS content is not in an ordinary clone; backups must cover it separately |

Selection verdict: for a team of two to fifty, Git plus LFS is enough; once art assets reach the density of "several people re-editing the same large files every day," seriously evaluate a centralized option. Do not build half of each — the migration cost doubles.

## 3. Process and Conventions

The daily routine is fixed as a one-line flow:

`pull the latest trunk → cut a short-lived branch → commit in small steps with self-checks → push and pass merge checks → merge back to trunk or tag a release`

### 3.1 Repository Setup and the Three Lists

Write the three lists on the day the repository is created; the cost of backfilling them grows with history:

- **Ignore list**: engine caches, import intermediates, build outputs, logs, local config, system files. Every time a new tool or platform comes in, add its entries that same day.
- **Attribute list**: the formats covered by LFS, per-platform handling rules, and file types declared binary. Write it along two dimensions, extension and path; err on the broad side.
- **Lock convention list**: which files only one person may modify at a time (large scenes, critical prefabs, core blueprints), and the etiquette for locking and releasing. Where a tool can lock automatically, use the tool; where it cannot, write the convention down.

### 3.2 Git LFS Strategy

The criteria for entering LFS: the file is not readable, is large, and every change rewrites it as a whole. The typical roster:

- Graphical assets: models, texture source files and finals, atlases;
- Audio assets: audio projects, waveforms, music, voice-over;
- Video and animation: cutscenes, promotional material, frame sequences;
- Engine binary assets: native engine asset formats and level files;
- Fonts and large data tables.

What does not go into LFS: scripts, configs, text documents, and text-format scene files that are small and frequently edited (when text merges cleanly, ordinary tracking is actually faster). The LFS roster lives in the attribute list, with `.gitattributes` as the authority; add the entry for a new format before it enters the repository.

Discipline for history migration: for large files that slipped into the repository early as ordinary commits, a thorough cleanup means rewriting history; a rewrite invalidates every local clone, so you must schedule a freeze window, notify the whole team and re-clone in unison. The common compromise: migrate only the directories that genuinely exceed the limits, accept some weight remaining in the old history, and route all new assets through LFS from that day on.

Day-to-day LFS operations:

- Every client and CI machine must have LFS installed and complete a pull, or all you get is pointer files;
- On hosted services, LFS storage is billed by capacity and traffic; for large projects, estimate the growth rate in advance;
- Backups must cover the LFS storage area; an ordinary repository mirror does not include the real content;
- Before a new file format enters the repository, confirm the attribute list covers it — one missed extension is one contamination.

### 3.3 Branching Strategy

Trunk plus short-lived feature branches plus release tags is the default answer:

| Branch or marker | Role | Discipline |
| --- | --- | --- |
| Trunk | The single integration branch; buildable and runnable at all times | Not allowed to stay broken for long; self-tests pass before merging |
| Feature branch | A single feature or fix | Cut from the latest trunk; lifetime measured in days; merged back as soon as possible |
| Release branch | Freezes a candidate version; accepts fixes only | Enabled for large teams and multi-platform cases; small teams can use tags instead |
| Release tag | An immutable snapshot of each public version | Once cut, a tag never moves; rollbacks go by tag |

Supporting rules:

- Agree on a version numbering scheme first, so tags, installers, store entries and crash reports all line up;
- Switching branches can trigger a mass asset re-import; concentrate switching into fixed windows, or give artists a second working copy;
- Candidate builds come off the frozen branch; tag only after acceptance passes; the commit behind a tag accepts no further changes;
- Hotfixes branch from the release tag, and after the fix merge back to trunk as well, so the fix is not lost in the next version.

### 3.4 Scene and Prefab Conflict Management

Semi-structured files are the densest accident zone; the measures, in priority order:

1. **Convention locks**: one scene, one prefab, one critical blueprint — only one editor at a time; commit and release as soon as the change is done. Lowest cost, highest payoff.
2. **Small commits**: commit after every meaningful change in the editor; compress "one commit a day" into "one commit an hour," shrinking the conflict surface from a whole day to a few minutes.
3. **Split the structure**: break large levels into sub-scenes or chunked loading, extract shared parts into standalone prefabs — structurally reduce the chances of several people editing one file.
4. **Engine tools**: use the engine's built-in features for merges and conflict handling first; leave semantic judgment to the side that understands the file format. Do not hand-stitch the conflict markers of a text scene — the stitched file may open and run, but its structure is already wrong.
5. **Arbitration**: on a real collision, designate one side to drop its local changes and let the other side rebuild to the requirements — cheaper and more reliable than patching up conflict markers.

When committing scenes and prefabs, confirm two things along the way: is this a small-step change with a single intent? Does it reference any temporary asset that exists only on this machine?

### 3.5 Commit Conventions and Hooks

Commit messages are the repository's narrative layer; adopt a format from day one:

- Structure: a type prefix plus a one-line summary; the body states why the change was made and what it affects;
- Define your own type prefixes (feature, fix, art, level, build, etc.); what matters is that the whole team uses the same ones;
- One commit does one thing; a feature change and a repo-wide reformat do not ride in the same commit;
- Write the outcome, not the process: "fixed saves vanishing after a day rollover" beats "changed the save-related stuff" by far.

The division of labor between hooks:

- Pre-commit checks: intercept cache directories and build artifacts, files over the size threshold, and formats that should not enter the repository;
- Commit message checks: validate the format against the team convention;
- Pre-push checks: optionally run a quick compile or smoke test;
- Hooks are a local convenience, skippable, and must never be treated as a security boundary; put enforcement in the CI of §4.

Pre-commit self-check list:

- Do the changes include caches, logs or temp files? Walk them against the ignore list item by item.
- Is every newly added binary file covered by LFS?
- Are the scene and prefab changes small-step and single-intent?
- Will the commit message let you understand the reason six months from now?

## 4. Automation and Acceptance

### 4.1 CI Triggers

| Trigger | What runs | Purpose |
| --- | --- | --- |
| Every push | Commit message validation, large-file scan, ignore-hit scan, LFS pointer validation | Block violations before they merge |
| Pull request | Compile, automated tests, asset import checks | Keep trunk buildable at all times |
| Nightly | Full build, multi-platform packaging smoke | Expose configuration drift as early as possible |
| Release tag | Formal packaging; generate release attachments and verification info | Make a tag correspond directly to a distributable artifact |

### 4.2 Checkpoints and Thresholds

| Checkpoint | How it is checked | Reference line | When exceeded |
| --- | --- | --- | --- |
| Repository size | Scheduled reports on repository and LFS storage growth | A steep jump in the growth curve raises the alarm | Locate the biggest new additions; evaluate migration |
| Single-file size | Scan newly added files on push | Over the team's agreed threshold | Move to LFS or compress and commit again |
| Caches and artifacts | Compare commit paths against the ignore list | Any hit fails the check | Remove the file and add the ignore entry |
| LFS coverage | Cross-check newly added binaries against the attribute list | Anything uncovered fails the check | Add the attribute entry and commit again |
| Commit message | Format validation | Non-conforming fails the check | Fix it locally, then push |

### 4.3 Acceptance Criteria

- A new member follows the repository's instructions to clone and start the project, gets it running within half a day, and needs no verbal supplements;
- Any release tag can be rebuilt into a runnable version on a clean machine;
- A release rollback completes within hours, and the process has been rehearsed at least once;
- For a random sample of binary assets, the commit history tells you the provenance, license and current version;
- A full month passes with no "overwrote someone's scene" or "large file polluted history" accidents; if one happens, go back to §3 and shore up the conventions.

Metrics give discussions a basis: repository size, clone time, conflict count, LFS traffic — review once a month; abnormal swings matter more than absolute values.

## 5. Common Pitfalls

1. **Caches and build artifacts in the repository**: engine caches, import intermediates and packaging output get committed, the repository balloons, and teammates overwrite each other's regenerable files. Write the ignore list in full on day one.
2. **Large files polluting history**: assets enter the repository as ordinary commits first; by the time you notice, history is carrying dozens of versions of large files, and the longer you wait the more it costs (migration strategy in §3.2).
3. **Ignore rules lagging behind**: a newly installed tool or newly added platform comes in and the ignore list does not keep up, so junk files seep in batch after batch. Add the entries the same day the tool lands.
4. **Managing binary assets like text**: no locks, no serialization; two people edit the same source file and the earlier push silently overwrites the other's work.
5. **Hand-merging text scenes**: stitching conflict markers around node IDs yields a file that opens but is structurally wrong — far costlier than a rebuild.
6. **Long-lived feature branches**: the branch dangles for weeks and merge day turns into a big-bang integration. Branch lifetimes are counted in days for a reason.
7. **Empty commit messages**: a screen full of "update" and "fix"; when something breaks you can neither locate it nor roll it back.
8. **Local hooks without CI**: hooks can be skipped, or never installed at all; staking all validation on the local machine equals no validation.
9. **LFS for commits but not operations**: new members cannot get real files when cloning, the quota runs dry, backups miss the LFS storage area — the problems all erupt together half a year later.
10. **Credentials mixed into history**: tokens, keys and accounts written into config and committed; deleting the file does not delete the history. Credentials must be rotated, and history must be either rewritten or carried as a risk.

## Further Reading

- Programming Handbook: the full treatment of engineering infrastructure and asset pipelines; this page is the practical version of its version control portion.
- Production Handbook: the higher-level framework for collaboration conventions, QA and the release process — see it for how team size maps to the strength of conventions.
- Pitfalls & Anti-patterns: the graded collection of version control and collaboration pitfalls; check against it in milestone reviews.
- Multi-platform Launch Playbook: the packaging and release process, downstream of release tags and build pipelines.
- Neighbors in the same section: Modding & UGC and Multiplayer & Backend are the published neighboring pages of this pipeline; cross-read their respective collaboration and tooling chapters.
