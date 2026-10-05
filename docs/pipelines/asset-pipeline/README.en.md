# Ludo Atlas · Pipelines · Asset Pipelines

> **Pipelines & Workflows**. Positioning: moving art assets from the creator's workbench into the game reliably — source files not lost, specs not drifting, rebuildable on another machine — through conventions, automation and freeze gates, not through memory and verbal handoffs.
> Companions: Art & Audio Handbook · Programming Handbook · Production Handbook · Pitfalls & Anti-patterns.
> Audience: teams with outsourcing, multi-person collaboration or hundreds of assets; small solo projects can trim it, but "source files and exports kept separate" and "naming and directory conventions" must be there from day one.

---

## 1. Positioning and Applicability

The art asset pipeline (asset pipeline) is a transport-and-QC channel: assets start with the creator, pass through specs, production, export and import, and arrive, in usable form, in every frame on the player's screen. It is not responsible for "whether it's drawn well" — that is the territory of the Art & Audio Handbook; it is responsible for "whether it gets there reliably":

- **Nothing lost**: every asset can answer three questions: where the source file is, who made it, and what the license is.
- **Nothing wrong**: specs come from the spec sheet, not from memory, not from verbal transmission.
- **No rework**: whatever a machine can check is never checked by eye; errors are caught at the cheapest stage of the process.

Four concepts to get straight first; the rest of the page keeps using them:

| Concept | Example | Handling |
| --- | --- | --- |
| Source files | Layered image projects, 3D projects, animation projects, audio projects, UI design files | Must be kept; go into the large-file store or a dedicated archive |
| Exports | Bitmaps, model interchange formats, finished audio | Rebuildable at any time; regenerated at build time |
| Imports | Asset entries and import settings inside the engine | Versioned together with the exports |
| Import settings | Options such as compression, sampling, anchors, scaling | Treated as code; must be versioned |

When is it worth standing the pipeline up: when outsourcing goes beyond one person, when the asset count passes a hundred, or when you have already been burned by any one of these three — a source file you can't find, an import that doesn't match, a license scrambled at the last minute before launch. The cost of building conventions rises with asset volume, so the earlier the cheaper; a full pipeline for three or five images is a different kind of waste.

## 2. Toolchain

The toolchain spreads across the pipeline's five stages, keeping one primary tool per stage — the shorter the chain, the easier to maintain:

| Stage | Tool type | Common choices | Selection notes |
| --- | --- | --- | --- |
| Authoring | Source tools | 2D: Aseprite, Krita and the like; 3D: Blender and the like; audio: a DAW | Output formats must be scriptable, not dependent on manual clicking |
| Version control | Binary-friendly solution | A repo with large-file extensions, or a dedicated asset versioning tool | Binaries must support file locking, so two people can't edit the same file |
| Export and conversion | Batch processing | Source-tool export scripts, atlas packing, audio transcoding and loudness checks | Export parameters go into config files, not dialogs |
| Import | Engine import pipeline | Import presets plus batch rebuild | Settings files live in the same repo as the assets |
| Validation | Check scripts | Scans of naming, dimensions, budgets and reference integrity | Wired into commits and builds, not left to individual diligence |

Three selection rules: only stages that can be scripted qualify to stay a bottleneck long term; large files need a dedicated solution, don't let the main repo get blown up by binaries; fewer tools is better than more, because every extra one adds maintenance and training cost.

External assets (purchased and free) travel the same channel, but with their own entrance: register the source and license first, then place them in a read-only directory that nobody edits directly. For how to check licenses, see the Art & Audio Handbook.

## 3. Process and Conventions

### 3.1 The Five-Stage Pipeline: Spec → Production → Export → Import → Validation

Five fixed stages, each with an explicit output; a stage that doesn't pass does not flow into the next:

| Stage | What happens | Output | Pass criteria |
| --- | --- | --- | --- |
| Spec | Define the spec sheet, naming, directories, freeze gates and owners | Spec sheet, template project | The producing side confirms it can be executed |
| Production | Produce in the source tools per spec, including in-progress self-checks | Source files, production log | Self-check against the spec sheet passes |
| Export | Batch-produce intermediates per the export conventions | Exports in the import-staging area | Scan script reports zero errors |
| Import | Import into the engine, applying the team's import presets | Imports, import settings, preview | References complete; result matches the reference sample |
| Validation | On-device checks, budget reconciliation, review records | Acceptance record, ledger updated | Review passes; ready to freeze |

Loop-back rule: if any stage finds that the spec itself is wrong, change the spec sheet and re-run that stage; patching a single asset in place plants an inconsistency for the future.

### 3.2 Naming and Directory Conventions

Naming is a team-level convention, pinned in the repo in a single copy that new members read on day one. A sample scheme: category first, subject in the middle, action and number last, e.g. `char_hero_idle_01`, `env_forest_rock_03`, `ui_icon_sword`.

- All lowercase, underscore-separated, ASCII letters and digits only; spaces, Chinese characters and mixed case are landmines in search and scripts.
- Zero-pad sequence numbers; keep variant suffixes consistent: `_n` for normal maps, `_e` for emissive, `@2x` for high-density images.
- Words like "final", "latest" and "confirmed-final" must not stay in file names; versioning is handed to the repo and the freeze records, not to file names.
- Prefixes and directories share one scheme: see the prefix and you know which directory it goes into; see the directory and you can infer how the prefix is written.

Directories are split into four zones by who produces the content and who uses it:

| Directory | What goes there | Rules |
| --- | --- | --- |
| Source area | Layered images, models, animations, audio, UI projects | On the large-file strategy with backups; excluded from the runtime build |
| Export area | Intermediates produced from source files | Safe to wipe and rebuild; not a deliverable in itself |
| Asset area (in-engine) | Imports and import settings | Version-controlled; organized by function, not by author |
| External assets area | Purchased and free assets | Read-only, with source and license registered alongside |

Once production starts the directory structure is frozen; to adjust it, do one team-wide migration first — don't let half the team use the old structure and half the new one; two structures in parallel cost more than either.

### 3.3 Separating Source Files and Exports

One governing principle: **exports are always rebuildable; source files cannot be regenerated**. Losing an exported image is ten minutes' work; losing a source project means scrapping the whole asset and redoing it.

- What counts as a source file: layered bitmap projects, 3D projects (including unapplied edits, material nodes and animation curves), audio projects, UI design files, font projects and license files.
- How to store them: source files go into large-file version control or a dedicated archive, with offline cold backups — at least two copies, one of them off-site; exports stay out of long-term storage and are rebuilt at build time, and if one goes missing you just rebuild it.
- Hard acceptance condition for outsourced delivery: source files must be delivered, with format and naming written into the requirements package; delivering only a bundle of finished bitmaps or model files does not count as a delivery.
- The anti-pattern: source files scattered across personal machines is betting the whole team's assets on the assumption that nobody quits and no disk dies.

### 3.4 Formats and Specs

The spec sheet is the single source of truth. It covers at least the rows below for each asset category; the values are for the project to decide, and once decided they are uniform project-wide:

| Asset category | Spec items that must be uniform | Consequences of inconsistency |
| --- | --- | --- |
| 2D images | Aspect ratio and pixel density, transparent margins, stroke width | Non-integer scaling sneaks in and the image looks blurry |
| Atlases | Page size tiers, padding, grouping rules | Sampling fringes, edge bleed |
| 3D | Units, orientation, pivots, naming prefixes | Wrong scale after import; flipped orientation |
| Textures | Size tiers, channel packing, compression profiles | Compression artifacts; rework and re-import |
| Audio | Format, sample rate, loudness target, loop points | Volume jumps up and down; clicks at loop points |
| Fonts | License scope, subsetting, fallbacks | Missing commercial license; a last-minute scramble before launch |

The values and detailed practices are drafted in the Art & Audio Handbook; this page covers only uniformity itself: one spec sheet, one review sign-off, one change record. Atlas grouping must be planned once, by function and usage scenario; shoving images in at packing time is the number one source of atlas bleed.

### 3.5 Versioned Import Settings

Import settings are not casual options in a dialog; they are part of how an asset behaves: change the compression profile, sampling method, anchors or material mapping, and both the look and the feel change.

- Import settings (the engine-side asset description files, import presets and conversion configs) must go into version control together with the assets; settings that exist only on somebody's machine are forbidden.
- Team-level presets take priority: each asset category converges on one set of defaults; individual differences are either merged into the preset or rejected.
- The bar is reproducibility: after wiping the imports, one button rebuilds them from the exports and settings in the repo, matching the frozen batch.
- Changes go through review: editing import settings ranks the same as editing code — record who changed what, why, and which assets are affected; after an engine upgrade, do a full rebuild and check for drift in visuals, size and behavior.

### 3.6 Review and Freeze Gates

Four gates: Draft → Review → Final → Freeze. Each gate's exit criteria are agreed in advance, and the review is against the spec sheet and the style baseline, not personal taste.

- How review runs: check formal items (dimensions, naming, format) exhaustively, spot-check stylistic consistency; record who, when, and which version passed.
- What freeze means: after a given milestone, that batch of assets stops accepting non-defect changes; changes go through a change request that spells out the impact, the rebuild cost and the approver.
- Freeze and scheduling: art freeze usually comes before code freeze, leaving a window for integration, polish and submission.
- Post-freeze re-check: run a full asset health check before the build (see §4) to confirm the frozen batch is the build batch; if the two don't match, the acceptance is void.

## 4. Automation and Acceptance

The division of labor is clear: machines check form, humans check taste. All the checks below are scripted and wired between commits and builds:

| Check | When it runs | On failure |
| --- | --- | --- |
| Naming and directory compliance | Before commit and in continuous integration | Reject the merge |
| Dimensions, ratios, transparent margins | After export | Send back for re-export |
| Atlas bleed and sampling overflow | At packing time | Reject the pack |
| Texture sizes and compression profiles | After import | Warn; fail if past the hard line |
| Audio loudness and loop points | After export | Send back for rework |
| Missing references and placeholder assets | At build time | Build fails |
| Triangle counts, material counts and texture budgets | After import | Warn and log to the ledger |

Acceptance looks at three things, all observable:

- A new asset goes from source file into the game with no verbal handoff or verbal explanation anywhere along the way.
- After wiping the exports and imports, one button rebuilds assets identical to the frozen batch.
- Pick ten assets at random; every one of them can produce its source-file path, author and license on the spot.

Four metrics to watch internally: first-import pass rate, rework rounds, lost item count, builds failed because of assets. If any metric rises for consecutive periods, the conventions are loosening — check the process first, then the execution.

The asset ledger is the backstop: one record per asset, covering origin, author, license, source-file path and frozen version. It doubles as the audit and legal record, and in outsourcing work it is shared with the acceptance process in the Production Handbook.

## 5. Common Pitfalls

1. **Chaotic naming**: files are found from memory, automation has nothing to grab onto, and whoever takes over spends the first week on archaeology.
2. **Storing only exports**: source files are scattered across personal machines and chat logs, and any staffing change cuts the supply.
3. **Inconsistent specs**: two stroke widths, three pixel densities, loudness levels that don't agree — the game looks stitched together at a glance.
4. **Losing source files**: no archive and no off-site backup — one disk failure writes off a batch of assets.
5. **Import settings outside version control**: re-importing on another machine no longer matches what was reviewed.
6. **No ledger for external assets**: the license turns out to be unclear just before launch, too late to fix it.
7. **Freeze in name only**: editing continues after the freeze, the build batch no longer matches the reviewed batch, and the acceptance is void.
8. **Atlas packed ad hoc**: grouping was never planned; every added image bleeds the atlas and packing gets reworked again and again.
9. **Large files shoved into the main repo**: with no large-file solution, the repo bloats until nobody wants to clone it.
10. **Checks left entirely to human eyes**: the conventions live only in a document, with no scripts or build gates behind them.

## Further Reading

- Art & Audio Handbook: where specs, style and production methods are drafted; this page is its logistics and QC layer.
- Programming Handbook: the technical side of import pipelines, resource budgets and build processes.
- Production Handbook: outsourcing, milestones and acceptance processes, connecting directly to the freeze gates in §3.6.
- Pitfalls & Anti-patterns: concrete cases from the art and collaboration chapters, to read alongside §5.
