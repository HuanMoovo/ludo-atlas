# Ludo Atlas · AI Workflows · Skills for Game Development

> This page answers one question: for agents to genuinely take part in game development, which Skills you need to prepare, and how.
> The conclusion up front: a Skill is not a mystical prompt; it is a three-part set of instructions, scripts and checks, written so it can be reused, reviewed and handed over.
> The snapshot is October 2026. Skills and tool ecosystems change fast, so for mechanism details go by each vendor's official docs (entry points in Resources §2.9).

---

## 1. First, Get Three Terms Straight

| Term | What it is | Analogy |
| --- | --- | --- |
| Skill (skill pack) | A reusable description of how to do one class of work: trigger conditions, steps, scripts, acceptance | A role's operations manual |
| MCP (tool interface) | The protocol layer through which agents connect to external tools (editors, Blender, browsers) | Hands and eyes |
| Rule files | Project-level conventions such as AGENTS.md: commands, standards, no-go zones | Factory rules |

The relationship in one sentence: MCP gives it hands; a Skill teaches it how to use those hands for one class of work; rule files draw the line on what it must not do.

## 2. The Skill Checklist for Game Development

A survey by stage. The "checkpoint" column is a veto item: miss it and the skill does not count as usable.

| Stage | Skills needed | Output | Checkpoint |
| --- | --- | --- | --- |
| Design & documentation | Design-doc drafting and health checks, competitor teardowns | An executable spec | Verify every number and conclusion item by item |
| Numbers & balance | Balance-table generation, change regression reports | A balance report | Verify by replaying real data |
| Code & tools | Scaffolding, refactoring, test generation | Changes that pass tests | Read the diff + all tests green |
| Engine operation | Scene building, bulk properties, screenshot smoke tests (via MCP) | In-editor changes | Screenshot comparison + commit on a branch |
| Levels & data | Map-data validation, batch level scripts | Level drafts | Take a few levels into the game and actually play them |
| Art pipeline | Concept art, asset generation, style-anchor maintenance, pixelation and slicing | Assets ready for the pipeline | Compare against anchors + hand refinement |
| Audio | Generation, trimming, loop-point and loudness checks | Usable clips | Ear-check loops and loudness |
| Narrative | Setting-library maintenance, dialogue-tree generation, consistency checks | Dialogue first drafts | Walk the consistency table item by item |
| Localization | Glossary maintenance, batch translation, LQA checklists | Translated drafts | Sampled close reading per language |
| QA | Smoke bots, visual regression, crash clustering | Tickets | Human review of ticket severity |
| Build & release | CI orchestration, release notes, store assets | A shippable build | Real-device acceptance |
| Live-ops | Changelogs, community-reply drafts | Drafts | Public-facing text finalized by a human |
| Team infrastructure | Context-file maintenance, prompt library, AI usage ledger | Long-term assets | Regular review |

You don't have to fill in this table all at once. Start with the two or three stages you repeat most; expand once those run smoothly.

## 3. Two Examples: What a Written Skill Looks Like

### 3.1 The Screenshot Smoke-Test Skill

- **Trigger**: after every build, or on the phrase "run the smoke tests".
- **Inputs**: the build artifact path, the levels and routes to cover.
- **Steps**: launch headless → simulate input from the script → screenshot at key points → compare against baseline → output the difference list.
- **Tools and permissions**: engine CLI, screenshot tools; read-only permissions, with writes allowed only to the screenshot directory.
- **Acceptance**: all screenshots are compared, differing frames are listed, and the call on which are real problems is left to a human.

### 3.2 The Style-Anchor Skill

- **Trigger**: before generating any new asset.
- **Steps**: load the anchor set → generate → compare against the nearest anchor → redo if it fails → log to the ledger on a pass.
- **Acceptance**: the output matches the anchors in style; all four ledger fields (tool, model, date, degree of human modification) are filled.

What the two examples share: the steps can be followed, the acceptance can be executed, and permissions name concrete paths. That is the difference between a Skill and "a paragraph of prompt text".

## 4. How to Get These Skills: Three Routes

1. **Use what exists**: search the agent's own skill ecosystem, plugin and MCP marketplaces first. Engine operation, Blender and browser automation all have ready-made implementations.
2. **Configure the rules**: AGENTS.md plus a prompt library (main volume §10); lowest cost — do these two first.
3. **Build your own skill packs**: once the same process has repeated three times or more, it is worth writing as a Skill.

Suggested order: set up the rules first, then try the existing ecosystem, and leave building your own for last. Installing a pile of plugins before the rules are in place only automates the chaos.

## 5. How to Write a Skill of Your Own

A skill pack answers at least seven questions, and the recommended carrier is an instruction file with a fixed structure:

```markdown
# Skill Name
## Purpose                     One line: what job it does, when to use it
## Trigger                     What phrase, at what moment, it fires
## Prerequisites               Which files, permissions and tools are needed
## Steps                       Numbered steps, with commands written out in full
## Acceptance Criteria         What can be checked automatically becomes a check; what cannot, state the manual item explicitly
## Permissions and Red Lines   Which paths may be written; which actions require manual confirmation
## Maintenance Log             Last review date, applicable engine and model versions
```

Three disciplines: the steps must be followable to the end (with real commands); acceptance must be a runnable action; red lines must name concrete paths and actions, not empty phrases like "be careful".

Where to keep them: alongside the project is the most stable option. Put them in the repo (a `tools/skills/` directory, for instance), versioned with the code and shared across the team.

## 6. Maintenance and Governance

- **Version binding**: after engines or models move to a new generation, re-review the affected Skills one by one; mark the ones you can't update as disabled for now.
- **Review**: trial a new Skill at small scale first; promote it only after it passes.
- **Regression**: changes to a Skill go through review. One bad skill affects a whole batch of output — more expensive than having no skill at all.
- **Retirement**: delete or explicitly mark outdated ones; don't keep a pile of zombie skills that still run but nobody uses.

## 7. The Human Part

A capable tool does not mean the human can stay ignorant. Three things cannot be delegated: acceptance criteria (you have to know how to write them), aesthetic judgment (game feel, style, pacing), and responsibility (disclosure and compliance).

The minimum skill list: read a diff, run the tests, spot anomalies in the data, and write a requirement as one verifiable sentence.

One reminder: a Skill is leverage; judgment is the capital. Without enough capital, leverage only magnifies the losses.

---

> Companion reading: the main volume, the AI Workflows Handbook (prompt library and red lines); the topic page AI Agents (permissions, orchestration and cost); Resources §2.9 (tool and skill ecosystem entry points); design doc §14.
