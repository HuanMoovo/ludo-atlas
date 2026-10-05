<div align="center">
<p><a href="README.md">简体中文</a> · <b>English</b> · <a href="README.ja.md">日本語</a></p>
<img src="assets/logo.svg" alt="Ludo Atlas logo" width="150">
<h1>Ludo Atlas · Game Development Panorama Handbook</h1>
<p><strong>A Chinese-first, structured, open-source knowledge base for game development.</strong> From learning, pitfalls, legal and launch, to design, engineering, art, production, live-ops and AI workflows: "making games" broken into <strong>139 documents (~982k characters)</strong>, every external link verified one by one, built to be contributed to.</p>
<p><strong>📖 Read online: <a href="https://huanmoovo.github.io/ludo-atlas/">https://huanmoovo.github.io/ludo-atlas/</a> (switchable between 简体中文 / English / 日本語 · GitHub Pages, deployed by CI)</strong></p>
<p><a href="https://github.com/HuanMoovo/ludo-atlas/actions/workflows/lint.yml"><img src="https://github.com/HuanMoovo/ludo-atlas/actions/workflows/lint.yml/badge.svg" alt="Lint"></a> <a href="https://github.com/HuanMoovo/ludo-atlas/actions/workflows/links.yml"><img src="https://github.com/HuanMoovo/ludo-atlas/actions/workflows/links.yml/badge.svg" alt="Link Check"></a> <a href="LICENSE"><img src="https://img.shields.io/badge/License-CC%20BY--SA%204.0%20%2B%20MIT-blue.svg" alt="License: CC BY-SA 4.0 + MIT"></a> <a href="https://github.com/HuanMoovo/ludo-atlas/stargazers"><img src="https://img.shields.io/github/stars/HuanMoovo/ludo-atlas?style=flat&label=Stars&color=48D64F" alt="Stars"></a></p>
</div>

## Preface

Chinese-language material on game development is never in short supply. Tutorials, videos, book lists, link dumps — a single search turns up hundreds of hits. What is missing is the skeleton that organizes them, and one complete route from "I want to make a game" to "it is out in the world."

This repository exists to add that skeleton. It addresses four long-standing problems:

- **Learning has no order**: beginners do not lack single-point tutorials; they lack a sequence, and a standard for how good is good enough to move on. The Getting Started section and the learning paths give three routes by goal, each step carrying an explicit bar to clear.
- **Production stages lack material**: most Chinese-language content stops at code and visuals, while the stages that really decide whether a project gets finished — kickoff, scope control, playtesting, localization, launch, compliance, live-ops — have very little systematic public documentation. This repository fills the gap with Pipelines & Workflows, Publishing & Business, and the playbooks, and gives each stage a minimal checklist.
- **Material goes stale**: engine versions, platform policies, fees and compliance requirements change every year, and blogs and videos often lag generations behind. Policy-related content here carries the date it was last checked; external links are verified one by one, and CI keeps re-checking them continuously.
- **The AI era has no standard answers yet**: coding agents and generative art and audio are entering real projects. The AI Workflows section collects reusable workflows, a tool matrix and compliance boundaries, to be picked up according to project scale.

The name comes from Latin: ludo (I play) and atlas (a map collection) — drawing as complete a map as possible for making games. There is only one organizing principle: place knowledge in the order real development happens. The content is Chinese-first; every document answers one concrete question, and documents reference each other instead of repeating.

This is a continuously maintained open-source project, and mistakes are unavoidable: Issues and PRs with corrections or additions are welcome, and errata get the highest priority.

If you can't do magic, you'll have to go to Hogwarts for training.

## What this is

An open-source handbook set covering the full game development lifecycle:

- **It explains both the "how" and the "why"**, with no platitudes; figures, policies and fees always come with verifiable sources and the date they were checked.
- **Every external link is verified one by one** (each verified before release, plus automated weekly re-checks in CI), with a full process for handling dead links.
- **Structured by design**: 139 documents, each with a single job, cross-referencing instead of repeating. See the [design doc](docs/meta/design.md) for the layout and long-term plan.

The library is Chinese-first; English editions are being added section by section — this README, the site home and the Preface are the first to land.

## Content map

### Fundamentals (docs/fundamentals/)

| Handbook | What it covers |
| --- | --- |
| [Game Design Handbook](docs/fundamentals/game-design/README.md) | Process, core loops, systems, balance, game feel, UX, narrative |
| [Programming Handbook](docs/fundamentals/programming/README.md) | Architecture choices, core systems, performance, multi-platform, networking, infrastructure |
| [Art & Audio Handbook](docs/fundamentals/art-audio/README.md) | Art bible, 2D/3D, UI, technical art, audio design and delivery |
| [Production Handbook](docs/fundamentals/production/README.md) | Kickoff, estimation, phase models, scope control, QA, postmortems |
| [Level Design Handbook](docs/fundamentals/level-design/README.md) | Metrics, teaching, pacing, whiteboxing, ten classic breakdowns |
| [Engine Internals Path](docs/fundamentals/engine-internals/README.md) | Godot / Bevy / small engines, methodology and weekly plans |
| [Renderer from Scratch](docs/fundamentals/graphics/README.md) | Software rasterizer → real-time APIs → ray tracing |

### Risk & legal

| [Pitfalls & Anti-patterns](docs/pitfalls/README.md) | High-frequency pitfalls (by area, by severity) |
| [Legal, Patents & Competition](docs/publishing/legal/README.md) | Copyright, trademarks, patents, contracts, cross-border compliance, competitor analysis |

### Publishing & platforms (docs/publishing/)

- [Multi-platform Launch Playbook (incl. online-game specifics)](playbooks/platform-launch/README.md)
- [Live-Ops & Growth](docs/publishing/live-ops/README.md)
- [Mini-Game Development](docs/publishing/minigame/README.md) (WeChat / Douyin / hardware channels)
- [Console Development](docs/publishing/console/README.md) (ID@Xbox / PlayStation / Nintendo)
- [VR/AR Development](docs/publishing/xr/README.md)
- [Esports & Competitive Design Handbook](docs/publishing/esports/README.md)

### Pipelines & deep dives (docs/pipelines/)

- [Modding & UGC](docs/pipelines/modding/README.md)
- [Multiplayer & Backend](docs/pipelines/multiplayer-backend/README.md)

### AI & case studies

- [AI Workflows](docs/ai/README.md): coding agents, engine MCP, art & audio pipelines, 8 end-to-end workflows, compliance guardrails
- [Case Studies](docs/postmortems/README.md): 24 public cases in a four-part breakdown

### History & people (docs/meta/)

- [Game History](docs/meta/history/README.md)
- [Indie Developers & Companies](docs/meta/people/README.md)
- [Indie Developer Profiles](docs/meta/people/indie/README.md) (44 profiles)
- [Design Doc](docs/meta/design.md): repository design and iteration log

### Practice & resources

- [Indie Survival](playbooks/indie-survival/README.md)
- [Game Development Resources](resources/README.md) (521 links)
- [Open Source Picks & Book Recommendations](resources/books-and-repos.md) (103 GitHub projects + 60+ books)

## Three recommended reading paths

- **Starting from zero**: [Resources](resources/README.md) → [Game Design Handbook](docs/fundamentals/game-design/README.md) → [Programming Handbook](docs/fundamentals/programming/README.md) → [AI Workflows](docs/ai/README.md)
- **Building your first release**: [One-page GDD](templates/gdd-mini.md) → [Production Handbook](docs/fundamentals/production/README.md) → [Pitfalls](docs/pitfalls/README.md) → [Indie Survival](playbooks/indie-survival/README.md) → [Multi-platform Launch Playbook](playbooks/platform-launch/README.md)
- **Going deeper**: [Engine Internals Path](docs/fundamentals/engine-internals/README.md) → [Renderer from Scratch](docs/fundamentals/graphics/README.md) → [Multiplayer & Backend](docs/pipelines/multiplayer-backend/README.md)

## Repository layout

```text
docs/           Handbook content (grouped by topic)
catalog/        Machine-readable entries (YAML + schema, single source of truth)
resources/      Link directory and book list
playbooks/      End-to-end playbooks (launch, survival)
templates/      Reusable templates (one-pagers, postmortems)
scripts/        Tooling scripts (link checking)
```

## Link & fact checking

- Every external link is verified before release; CI re-checks them weekly.
- Policy, fee and platform-rule content carries the date it was checked; before acting, always confirm against the latest official documentation.

## Contributing

Errata, new content and engineering improvements are all welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md).

## Star history

[![Star History Chart](https://api.star-history.com/svg?repos=huanmoovo%2Fludo-atlas&type=Date)](https://star-history.com/#HuanMoovo/ludo-atlas&Date)

## License

Documentation is under [CC BY-SA 4.0](LICENSE); code is under [MIT](LICENSE-CODE).

## Notes

Handbook content draws on a large body of public material, official platform documentation and developer interviews, with rights belonging to their respective authors; figures and policies are subject to the latest official information at the time you act.
