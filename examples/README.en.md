# examples/ — Examples Roadmap

The handbooks explain the concepts and the trade-offs; the examples turn those concepts into the smallest project that runs. This page is the blueprint for the examples section: positioning and boundaries, directory conventions, the planned example list, and the complete process for contributing a new example. The examples section is currently in its preparation stage before the first batch lands; nominations and claims under this page's rules are welcome.

## What the examples section is

- Each example is a standalone directory: the engine project itself plus a README page; the goal is clone-and-run.
- Examples are teaching material, not production projects — one example drills one or two topics thoroughly; cut everything you can, and introduce no dependencies unrelated to the teaching points.
- Examples are companions to the handbooks: the handbooks explain why to do it this way, the examples give the minimal viable how; every example in the roadmap table is tagged with its corresponding handbook.
- Division of labor with [templates/](../templates/README.md): templates are copyable document skeletons, examples are runnable code and assets.

## Directory structure conventions

Every example directory uses the same skeleton, keeping only the files the engine needs to run:

```text
examples/
├── README.md            # this page: roadmap and contribution guide
└── <engine>-<topic>/        # a single example directory; naming below
  ├── README.md          # the README page (required)
  ├── <engine project files>   # e.g. project.godot, Assets/, package.json
  ├── src/            # code and scenes, organized per engine convention
  ├── assets/
  │  └── CREDITS.md       # asset list: source and license per item (required)
  ├── LICENSE           # license notes: code MIT, assets per CREDITS.md
  └── .gitignore         # ignore engine caches and build artifacts (required)
```

Rules:

- **Naming**: `<engine>-<topic>`, all lowercase English with hyphens; no spaces and no Chinese; engine names follow the spellings in [Engine Tracks](../docs/engines/README.md) (godot, unity, bevy, raylib, renpy, etc.).
- **Project files**: keep only the minimal configuration that opens and runs directly; the README page states the engine major version, e.g. Godot 4.3, Unity 6.
- **Code**: organize under src/ or the engine's conventional directories; the total should be readable in one afternoon — keep the scale restrained.
- **Assets**: all under assets/, with source, author, license and whether it was modified registered item by item in CREDITS.md; when there are no external assets, keep the list anyway and state the situation. Keep the whole example directory within 10 MB if you can; anything larger should use generation scripts or smaller substitute assets.
- **License**: code defaults to MIT (consistent with the root [LICENSE-CODE](../LICENSE-CODE)); asset licenses are annotated item by item in the list; the README page's last section restates the same terms.
- **README page**: five fixed sections; see the template below.

## Example roadmap

The table below is the roadmap for the examples section: 12 examples covering six engine tracks — Godot, Unity, Web, raylib, Bevy and Ren'Py; five are marked as the first batch (matching the example slots of Phase 2 in the repository plan), proving the clone-and-run chain across five different tracks first, with the rest proceeding in claim order. Directory names are planned claims; discuss and adjust them in the corresponding Issue before implementation.

| Example | Engine | Difficulty | Status | Topics covered | Corresponding handbook |
| --- | --- | --- | --- | --- | --- |
| Platformer feel demo · `godot-platformer-feel` | Godot 4 | Beginner | First batch | Movement and jump curves, coyote time, jump buffering, variable jump height, camera follow | [Game Design Handbook](../docs/fundamentals/game-design/README.md) (Game Feel) · [Platformer](../docs/genres/platformer/README.md) |
| 2D controller · `unity-2d-controller` | Unity | Beginner | First batch | Input system, rigidbodies and custom movement, jump buffering, one-way platforms | [Unity track](../docs/engines/unity/README.md) · [Platformer](../docs/genres/platformer/README.md) |
| Web release pipeline · `phaser-web-pipeline` | Phaser 3 | Beginner | First batch | Packaging and initial bundle size, touch input and responsive layout, static hosting, versioning and caching | [Web Games track](../docs/engines/web/README.md) · [Mini-Game Development](../docs/publishing/minigame/README.md) |
| Mini-game skeleton · `raylib-mini-game` | raylib | Beginner | First batch | Main loop and fixed timestep, state switching, collision and input, cross-platform builds | [Lightweight Frameworks track](../docs/engines/micro/README.md) · [Build & Release](../docs/pipelines/build-release/README.md) |
| ECS starter · `bevy-ecs-starter` | Bevy (Rust) | Intermediate | First batch | Components and systems, queries and filters, fixed timestep, states and schedules | [Bevy track](../docs/engines/bevy/README.md) · [Engine Internals Path](../docs/fundamentals/engine-internals/README.md) |
| Tower Defense skeleton · `godot-tower-defense-skeleton` | Godot 4 | Intermediate | Later batch | Paths and waves, tower tables and economy, target selection, stat-to-UI binding | [Tower Defense](../docs/genres/tower-defense/README.md) · [Programming Handbook](../docs/fundamentals/programming/README.md) |
| Massive-enemy object pool · `godot-enemy-pool` | Godot 4 | Intermediate | Later batch | Object pool reuse, thousands of entities on screen, batched drawing, physics culling | [Bullet Heaven](../docs/genres/bullet-heaven/README.md) · [Programming Handbook](../docs/fundamentals/programming/README.md) |
| Shader exercise set · `webgl-shader-exercises` | WebGL2 | Intermediate | Later batch | UVs and noise, lighting models, dissolve and distortion, screen-space post-processing | [Renderer from Scratch](../docs/fundamentals/graphics/README.md) · [Art & Audio Handbook](../docs/fundamentals/art-audio/README.md) |
| Data-driven stat tables · `unity-data-driven-stats` | Unity | Intermediate | Later batch | Numbers and formulas separated, ScriptableObject, runtime tuning, formula self-tests | [Game Design Handbook](../docs/fundamentals/game-design/README.md) (Numbers and Balance) · [Programming Handbook](../docs/fundamentals/programming/README.md) |
| Mini dialogue system · `godot-dialogue-mini` | Godot 4 | Intermediate | Later batch | Dialogue data formats, conditions and variables, typewriter effect and choices, save-system integration | [Visual Novel](../docs/genres/visual-novel/README.md) · [Game Design Handbook](../docs/fundamentals/game-design/README.md) (Narrative Design) |
| Localization example · `unity-localization` | Unity | Comprehensive | Later batch | String tables and key naming, placeholders and plurals, font fallback, pseudo-localization validation | [Localization](../docs/pipelines/localization/README.md) · [Pitfalls & Anti-patterns](../docs/pitfalls/README.md) |
| Minimal branching narrative example · `renpy-branching-story` | Ren'Py | Beginner | Later batch | Branches and jumps, variables and conditions, sprites and transitions, packaging and release | [Ren'Py track](../docs/engines/renpy/README.md) · [Visual Novel](../docs/genres/visual-novel/README.md) |

Difficulty comes in three tiers: Beginner (follow along with basic engine skills), Intermediate (pair with the corresponding handbook to fill in a concept or two), Comprehensive (several systems assembled together, sized close to a small project). Examples for more engines (Cocos, Unreal, GameMaker, MonoGame, Defold and others) are welcome as nominations in later batches.

## Contributing a new example

Five steps; the README page template and the review points are below.

1. **Nominate.** File an Issue with the "New Content" template, titled `[Example] <engine>-<topic>`, stating the teaching points it should cover, the target engine and version, the minimal feature list, and its relationship to the roadmap and existing examples (if it overlaps, state the increment). Once confirmed, you can claim it.
2. **Build the skeleton.** Create the directory per the directory conventions; write the README page before the code — if you can't say what it teaches, the topic is still too big.
3. **Implement and self-test.** In a clean environment (clone fresh once), run it through strictly by the README page's steps, recording the engine version, commands and expected behavior. Three red lines: it doesn't run, asset licensing is unclear, the README is missing sections.
4. **Open a PR.** One example per PR, with run verification attached to the description; pass markdownlint and the link check per the conventions in [CONTRIBUTING.md](../CONTRIBUTING.md).
5. **Review and merge.** Review walks the acceptance checklist item by item; once it passes, it is merged, and the status column in the roadmap table on this page is updated to Merged.

### README page template

```markdown
# <example name> (<engine and major version>)

- Teaching points: <one sentence>
- Estimated time to run: <x minutes>
- Prerequisite reading: <relative link to the corresponding handbook>

## What problem it solves

<Why this example exists; what the reader can do after finishing it.>

## How to run it

<Engine version, commands one by one, expected behavior; no reliance on verbal supplements.>

## Key files guide

<A file-to-role mapping, explaining why it is organized this way.>

## Exercises and suggested changes

<Two or three small tasks to try changing by hand.>

## License and assets

<Code is MIT (see LICENSE-CODE at the repository root); asset sources and licenses are in CREDITS.md.>
```

### Review points

- **Runs directly**: the reviewer gets it running in a fresh environment following the README page; commands and versions are explicit, with no reliance on verbal supplements. Missing dependencies, or anything that only runs on the author's machine, goes straight back.
- **No copyright issues**: every asset is traceable and license-compatible; extracting assets from commercial works is forbidden; fonts and audio are registered the same way; borrowed code cites its source and license.
- **Complete documentation**: all five sections present, explaining why it is written this way rather than just pasting code; prose in Simplified Chinese, terminology consistent with the rest of the repository.
- **Restraint and consistency**: naming and directories follow the conventions; no dependencies unrelated to the teaching points; no caches or build artifacts committed.

## Example acceptance checklist

Check every item before merging; contributors are advised to go through it themselves before opening a PR.

- [ ] Directory name follows the `<engine>-<topic>` convention: all lowercase English with hyphens
- [ ] Runs in a clean environment following the README page; engine version and commands are explicit
- [ ] README page has all five sections: What problem it solves / How to run it / Key files guide / Exercises and suggested changes / License and assets
- [ ] Every asset registered in CREDITS.md, with verifiable source and license
- [ ] Code under MIT, asset licenses annotated separately, and the two do not conflict
- [ ] No engine caches or build artifacts committed; .gitignore configured for the engine
- [ ] No dependencies beyond the teaching points; remove what can be removed; scale restrained
- [ ] In-repo references use relative links; markdownlint and the link check pass
- [ ] PR description includes run-verification records (environment, commands, results)
- [ ] When referencing or porting from public tutorials, the source is credited and license compatibility confirmed

## Related

- [Engine Tracks](../docs/engines/README.md): the 12 engine tracks — the authority for engine naming and engineering practices in examples.
- [About This Repo](../docs/meta/design.md): overview and conventions.
- [templates/](../templates/README.md): document templates, complementary to the example README pages.
- [CONTRIBUTING.md](../CONTRIBUTING.md): submission conventions and CI (markdownlint, link checking).
- [Content Roadmap](../docs/meta/roadmap.md): the release batch and stage goals the examples section belongs to.
