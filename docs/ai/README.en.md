# Ludo Atlas · AI Workflows

> Turning "how AI participates in game development" from an outline into an executable workflow set.
> The snapshot is October 2026. Tools like these change fast, so this page focuses on methods, checkpoints and red lines; for specific tool names and versions, go by the official sites (entry points in Resources §2.9).
> One premise up front: AI improves speed; judgment remains your responsibility. Whether output is usable, whether it needs disclosure, who is accountable when something goes wrong — none of those answers live with the model.
> This handbook also has two companion pages: **[AI Agents](agents/README.md)** (forms, orchestration, and rollout) and **[Skills for Game Development](skills/README.md)** (the skill checklist and how to set them up).

---

## 1. Use AI or Not: Pass a Decision Table First

To decide whether to hand a piece of work to AI, look at two variables: how easy the output is to verify, and how expensive a mistake would be.

| Task type | Verification cost | Cost of error | Recommendation |
| --- | --- | --- | --- |
| Boilerplate code, tool scripts, configuration | Low | Low | Use freely |
| Batch conversion (renaming, formats, data cleanup) | Low | Low | Use freely |
| Draft-type content (copy drafts, dialogue drafts) | Medium | Low | Use it, but give it a human pass |
| Retrieval and compilation (research summaries, comparison tables) | Medium | Medium | Use it, but verify every number and conclusion |
| First-draft translation | Medium | Medium | Use it — the glossary and sampled close reading can't be skipped |
| Ordinary business code | Medium | Medium | Use it, with tests and review |
| Core gameplay and game-feel code | High (only sensed by playing) | High | Use sparingly; write and tune it yourself |
| Architecture-level refactoring | High | High | Use with caution; write the plan before touching anything |
| Final public-facing copy | Medium | Medium | Let AI produce drafts only |
| Payments, accounts, security logic | High (needs auditing) | Extremely high | Written and reviewed by humans |

The one-line standard: can you verify this output within a few minutes? If you can, use AI more; if you can't, use it less — or not at all.

## 2. Coding Agent Workflows

### 2.1 The Tool Landscape (Short Table)

| Form | Representative | Good for |
| --- | --- | --- |
| Terminal agents | Claude Code, Codex CLI, Gemini CLI, opencode, aider | Large changes, multi-file tasks, scripting |
| Editor integrations | Cursor, Copilot, Cline, Continue | Inline completion, local edits |
| Cloud/async | various vendors' cloud coding agents | Queued tasks, parallel small changes |

Don't agonize over the choice: whichever one you already use, run the workflows on this page smoothly with it — the payoff is bigger than switching around.

### 2.2 First, Make the Agent Understand the Project (Context Engineering)

An agent's performance ceiling depends on the quality of the context you give it. A few files worth maintaining:

- **AGENTS.md (or an equivalent conventions file)**: build and test commands, a directory map, code conventions, no-go zones (files not to touch). This is the single highest-value document.
- **SPEC.md**: what to build, and the acceptance criteria.
- **ARCHITECTURE.md**: structural decisions and the reasoning (an ADR summary works).
- **Pitfall log**: write down where the agent broke something last time; next time it will steer around it.

Small trick: spell out "what we don't use" too (no new dependencies, not this pattern) — that prevents drift better than stating only "what we want".

### 2.3 The Work Loop (Six Steps)

1. **Define acceptance first**: write down the expected behavior or a test, even just one line of "pressing X should produce Y".
2. **Dispatch in small steps**: one feature point at a time; don't throw five requirements at it at once.
3. **Read the diff**: if you don't read the diff, you haven't really used the agent.
4. **Verify**: run the tests, or play it manually for three minutes.
5. **Commit**: one commit per passing small step, so a problem is easy to roll back.
6. **Capture**: write new conventions back into AGENTS.md so you explain them one time fewer.

Four anti-patterns: big-bang generation (hundreds of lines at once, no way to review them), trusting the diff blindly, skipping verification, and letting the agent "refactor everything while it's at it".

### 2.4 Common Pitfalls in Game Projects

- **Lifecycle misunderstandings**: generated code often makes mistakes like "initialize every frame" and "create objects inside events"; keep a standing item on the review checklist: where do initialization, update and destruction each happen?
- **Hallucinated APIs**: method names that don't match your engine version. Have the agent read the official docs for your version first, or paste the relevant API pages to it directly.
- **Performance blind spots**: per-frame allocation, string concatenation, enumerating GetComponent — all default agent habits; state requirements explicitly wherever performance matters.
- **Platform differences**: path case sensitivity, save directories, permission declarations — the agent doesn't know which platforms you ship on, so write it into the conventions.

### 2.5 What Not to Hand to the Agent

- Game-feel parameters (jump height, camera speed). These are played into shape and tuned, not generated.
- Refactors you don't intend to understand. Code you can't read is future debt, and the person who owes it is you.
- Payment, account, anti-cheat — logic that needs auditing.

## 3. Engine MCP: Let the Agent Drive the Editor Directly

How it works: an MCP server connects to an editor plugin, and the agent gains structured capabilities like reading the scene tree, editing nodes, running the game to take screenshots, and reading error logs. Instead of blind file edits, it operates against the real editor.

Current ecosystem (October 2026): Godot has several active community implementations covering scene editing, screenshots and input simulation, with tool counts ranging from a few dozen to over a hundred; Unity has an official built-in MCP service (in testing) plus a set of community implementations; Blender also has options for modeling assistance. Entry points in Resources §2.9.

**Three security principles** (none are optional):

1. Permissions start read-only; enable change-type tools one item at a time.
2. Let the agent act only on a working branch, and commit once before it starts.
3. Operations like deletion, export and executing arbitrary scripts get manual confirmation every single time.

Good fits: repetitive scene building, batch property changes, automated screenshot test runs. Bad fits: game-feel tuning, big refactors, anything you haven't thought through.

## 4. AI Art: From Concept to Assets

### 4.1 Maturity by Stage (a 2026 View)

- Concept art and references: mature; very cost-effective as reference.
- Finished 2D assets: usable, but they need a workflow and hand refinement — raw generations look bad.
- 3D models: usable for prototypes and placeholders; production assets still need retopology, UVs and decimation — don't skip them.
- Textures and materials: assistive level; batch generation of stylized materials works well.
- UI icons: generation plus a unified clean-up pass; a solid efficiency gain.

### 4.2 Consistency: The Biggest Hurdle

A set of assets growing less and less alike is the most common AI-art failure. The countermeasure is to fix "style" into an asset:

- **Style anchors**: pick 3–5 approved images as the baseline, and reference them for all later generation.
- **Technical means**: image-to-image from references sets the base tone; LoRA learns a style; ControlNet constrains poses and line art.
- **Process discipline**: cull half of every batch before discussing quality; what passes goes into the "baseline library", and don't settle for the ones that drift off-target.

### 4.3 The 2D Asset Pipeline

Generate → select → hand-refine → slice → import → log to the ledger.

Pixel art adds one step: pixelate the generated result first (restrict the palette, align to the pixel grid), then hand-fix keyframes. For any style, final quality rests with human hands; AI's job is to make the draft stage faster.

### 4.4 Turning ComfyUI into a Workflow

Turning "gacha pulls" into a pipeline is the dividing line for whether AI art can enter production:

- Workflows are saved as files and go into git, versioned like code.
- Parameterization: canvas size, style strength and seed all become inputs, which makes batch runs easy.
- Batch queueing: run a batch at a time, with scripts handling automatic naming and archiving.

Post-processing has to be scripted too: batch cropping, compression, naming and engine import as one chain. Opening each image by hand and saving it out is not a sustainable practice.

### 4.5 Records and Disclosure

Record four fields for every asset AI touched: tool, model, date, and degree of human modification. This is not just a compliance requirement (see §8) — it is also your own asset map: when a problem comes up, you can trace where it came from.

## 5. AI Audio

- **Music**: use generation for drafts or ambient beds, with humans picking sections and connecting loops. Any track that ships must get two things right: seamless loop points and consistent loudness (standards in Art & Audio Handbook §10). Check commercial-use terms vendor by vendor — terms change.
- **SFX**: a generate-then-trim pipeline is viable, and at batch scale it beats hunting for samples one by one. For lightweight cases, procedural SFX tools (like jsfxr) are faster and more reliable.
- **Voice-over**: TTS is fine for prototypes and internal builds; for an official release, mind three things: voice cloning must have written authorization from the person whose voice it is; platforms and the industry have disclosure requirements for AI voice acting; and audience acceptance of AI voices varies by genre.

## 6. AI Narrative and NPCs

### 6.1 Offline Generation (Do This First)

Uses: worldbuilding drafts, side-content copy, item descriptions, dialogue first drafts. Flow: write the setting documents (character bible, world rules) first, then generate, then rewrite by hand, and finally run a consistency check. The more specific the setting documents, the more the output reads like your game instead of someone else's.

### 6.2 Runtime LLMs (Experimental — Try at Small Scale First)

Architecturally, don't let the client connect straight to the model; add a gateway layer of your own to handle rate limiting, logging, content filtering and fallback. Three budgets to fix in advance:

- Cost: token spend per thousand conversations, estimated from player count and interaction frequency.
- Latency: responses over about one second break the feel of conversation; a small model plus caching is the common solution.
- Guardrails: output filtering, topic constraints, sensitive-content interception, and timeout fallbacks to pre-written lines. Steam requires you to describe your guardrails for runtime-generated content (§8) — this layer is the guardrails themselves.

### 6.3 Consistency

Character bible plus retrieval (RAG) is the mainstream approach: retrieve character settings and existing plot before generating, to avoid self-contradiction. Build a separate "already said" library — what players already know can't be walked back.

## 7. AI Testing and Localization

- **Smoke-test agents**: run the game in headless mode, simulate input, assert against logs. Good for automatically exercising the basic path after every build.
- **Visual regression**: screenshot comparison before and after, with humans reviewing the differences. The agent surfaces suspicious frames; you decide whether they're real problems.
- **Localization pipeline**: extract strings → glossary check → model translation (with character and scene context) → human LQA → backfill → font and line-break checks. The glossary and sampled close reading are the two steps you can't skip — skip them and the negative reviews will come.
- **Crash clustering**: group crash logs, have the agent write a first-pass assessment, and have a human review ticket severity.

## 8. Compliance and Disclosure (the Red-Line Zone)

- **Steam disclosure** (per the January 2026 revision; check the latest official docs before acting): internal tools used purely for efficiency don't need disclosure; content players can see or hear does, in two categories, pre-generated and runtime-generated; runtime generation requires describing your guardrails; false disclosure is a breach of contract, and copyright liability falls entirely on the developer.
- **Copyright**: the training sources of generative models are complicated; before output enters official assets, apply substantial human processing and keep complete records.
- **Team policy**: write down clearly where use is allowed, where it is forbidden, who checks, and how it is described externally. Key template points in the AI Workflows Handbook §8.
- **The ledger**: tool, model, date, degree of modification, license link. This table is a lifesaver in platform reviews and copyright disputes alike.

## 9. Eight End-to-End Workflows

| # | Scenario | Toolchain | Hard checkpoints |
| --- | --- | --- | --- |
| 1 | Weekend prototype | Engine + coding agent + image generation + generated music | Play it by hand for 5 minutes after each finished feature |
| 2 | Adding features to an existing project | Fill in AGENTS.md → small-step dispatch → regression tests | Full test run before each commit; don't touch public interfaces |
| 3 | Asset factory | Parameterized ComfyUI + naming and import scripts | Spot-check 10% of every batch; compare against the style anchors |
| 4 | Narrative pipeline | Setting docs → outline → dialogue-tree generation → human rewrite | Check the character-consistency table item by item |
| 5 | QA loop | Agent runs smoke tests → captures logs → files tickets | Human review of ticket severity |
| 6 | Localization | Extract → glossary → translation → LQA → backfill | Sampled close reading of 5% per language |
| 7 | Jam division of labor | Asset generation + coding agent + copy drafts | Reserve 2 hours before submission for a consistency check |
| 8 | Live-ops copy | Changelog drafts, community-reply drafts | Public-facing text must be fully human-edited before posting |

Once a workflow has run end to end, write it into the team documentation. A process you keep explaining is a process that should be formalized.

## 10. How to Build a Prompt Library

A prompt worth including has a fixed structure: purpose, applicable tools, template (variables as placeholders), example input, caveats, and review date.

Three maintenance principles: include only what you've used; delete what stops working — no souvenirs; when the tools move to a new generation, re-review old prompts so the library doesn't become a source of hallucination. In this repository it lands at `docs/ai/prompt-library/` (planned).

## 11. Common Mistakes

1. Treating AI as a search engine: what you get is outdated information and fabricated sources.
2. Shipping output without verifying it, turning a speed advantage into an incident advantage.
3. Using AI to write systems you don't understand — half a year later, no one can modify them.
4. Forgetting your disclosure obligations, and finding out at store submission that materials have to be supplied.
5. Chasing a "fully automated" workflow whose maintenance cost ends up exceeding the time it saved.
6. Letting AI decide the art direction: it delivers the average, and average means nothing memorable.
7. Collecting a pile of prompts without using them; the bigger the library, the more it feels like a bluff.
8. Posting AI-written public-facing copy as-is; readers are more sensitive than you think.
9. Not keeping a ledger — when something goes wrong, you have no way to account for it.
10. Mistaking "fast" for "good". Speed is a means; players judge by results alone.

---

> Companion reading: compliance details in the AI Workflows Handbook §8; official tool sites in Resources §2.9; related open-source projects in Open Source Picks & Book Recommendations §6; how this lands inside engines in Programming Handbook §6.
