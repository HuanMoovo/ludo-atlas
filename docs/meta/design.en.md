# Ludo Atlas · About This Repo

> Ludo Atlas (the Game Development Panorama Handbook) is a Chinese-first, structured, open-source knowledge base for game development: the whole path from getting started to shipping, with both international and Chinese resource lines.
> The name comes from Latin: ludo (I play) and atlas (a map collection) — the goal is to draw as complete a map as possible.
> This page is the repository overview: positioning, content map, quality standards, structure and how to take part.

---

## 01 What This Is

- **A learning and production path**: not a pile of tutorials, but an ordered route plus executable checklists (what counts as done).
- **Chinese-first**: Simplified Chinese is the primary language, with an English edition across the library; terminology is listed in [GLOSSARY.md](../../GLOSSARY.md).
- **Two resource lines**: every stage lists both international and Chinese tools, platforms and communities.
- **Continuously maintained**: content advances by versions; questions and suggestions go through Issues / PRs.

Who it is for:

- Newcomers: walk from Getting Started to your first playable game.
- Working developers: use the genre handbooks as checklists and fill the gaps.
- Indie developers and small teams: kickoff, scope control, launch and postmortem.
- Contributors: expand, proofread and translate along the shared templates.

Out of scope: news and hot takes, zero-to-one tutorials for a single engine, paid-course funnels.

## 02 Content Map

| Section | What you get | Entry |
| --- | --- | --- |
| Getting Started | The big picture, role map, engine choice, first game, learning paths | [Getting Started](../start/README.md) |
| Fundamentals | Game design, programming, art & audio, production, level design, engine internals, graphics | [Fundamentals](../fundamentals/README.md) |
| Genre Handbooks | Development handbooks for 81 game genres (four volumes) | [Genre Handbooks](../genres/README.md) |
| Engine Tracks | 12 engine and framework tracks | [Engine Tracks](../engines/README.md) |
| Pipelines & Workflows | Build & release, playtesting, version control, localization, telemetry, asset pipelines and more | [Pipelines & Workflows](../pipelines/README.md) |
| AI Workflows | Boundaries for using AI, agents, skills, and end-to-end workflows | [AI Workflows](../ai/README.md) |
| Teams & Scale | How solo devs, small teams and studios work | [Teams & Scale](../teams/README.md) |
| Publishing & Monetization | Launch, legal, live-ops, mini-games, consoles, VR/AR, esports | [Publishing & Monetization](../publishing/README.md) |
| Pitfalls & Postmortems | The anti-pattern collection and project postmortems | [Pitfalls](../pitfalls/README.md) · [Postmortems](../postmortems/README.md) |
| Playbooks | End-to-end processes: idea to demo, vertical slice, launch and more | [Playbooks](../../playbooks/README.md) |
| Templates | Ready-to-use templates: one-pager, GDD, tech design, milestones | [Templates](../../templates/README.md) |
| Examples | The example plan covering six engine tracks | [Examples](../../examples/README.md) |
| Resources | The full directory of engines, tools, assets, publishing and services (650+ entries) | [Resources](../../resources/README.md) |
| History & People | A brief history of games; indie developers and companies | [History](history/README.md) · [People](people/README.md) |

## 03 Quality Standards

- **Single source of truth**: reference existing content instead of copying it; cross-references use the form *Handbook §X*.
- **Verifiable**: links are checked one by one (method and records in Resources §11); figures and conclusions state their source or basis.
- **Writing conventions**: written in Simplified Chinese, consistent terminology (see GLOSSARY), no unverified promises.
- **AI use**: AI output must be human-verified; outward-facing assets are disclosed as platforms require, with a ledger (see the AI Workflows Handbook §8).
- **Link policy**: only entries that are reachable and genuinely useful for game development; one most-useful entry per category, no duplicates.
- **No empty talk**: no "empowerment" or "ecosystem" filler; every recommendation lands on an action.

## 04 Repository Layout

```text
gamedev-atlas/
├── docs/            # reading content: start / fundamentals / genres / engines / pipelines / AI / teams / publishing / pitfalls / postmortems / meta
├── playbooks/       # end-to-end playbooks
├── templates/       # ready-to-use templates
├── examples/        # the example plan
├── resources/       # the resource directory
├── site/            # reading-site build (Material for MkDocs)
├── scripts/         # maintenance scripts
└── .github/         # CI: lint / link check / site deploy
```

Current scale: 140+ Chinese documents · ~960k characters · 81 genre handbooks · 12 engine tracks · 650+ resource links.

## 05 Versions & Status

- Current version v2.6.2: full English coverage; the reading site is bilingual (Simplified Chinese / English).
- Milestones: v0.1 first 26 handbooks → v2.0 all tracks complete → v2.4 migration to Material for MkDocs → v2.6 full English coverage → v2.6.2 deduplication and trimming.
- Full log in [CHANGELOG.md](../../CHANGELOG.md); next directions in the [Content Roadmap](roadmap.md).

## 06 Licensing

- Documents and collected listings: see [LICENSE](../../LICENSE).
- Code and scripts: see [LICENSE-CODE](../../LICENSE-CODE).
- Third-party resources: each link belongs to its owner; inclusion is not a license.

## 07 Taking Part

- Questions and suggestions: GitHub Issues; content revisions: Pull Requests.
- Claim a topic or an expansion direction: the [Content Roadmap](roadmap.md).
- Contribution and conduct: [CONTRIBUTING.md](../../CONTRIBUTING.md) · [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md).

---

> Version log: [CHANGELOG.md](../../CHANGELOG.md) · Roadmap: [Content Roadmap](roadmap.md)
