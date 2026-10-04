# Ludo Atlas · Getting Started · Roles & Skills Map

> **Getting Started**. This page breaks game development roles down into eight tracks: what each track does, core skills, day-to-day output, and how to get started. It is for people considering entering the industry, forming a team, or figuring out "what should I practice right now."

## 1. Programming Track

Turns design and content into software that runs, runs smoothly, and doesn't crash.

| Role | What they do | Core skills | First steps |
| --- | --- | --- | --- |
| Gameplay programmer | Implement combat, abilities, interactions, level mechanics | One engine's scripting language, state machines, design patterns | Build three small gameplay prototypes in an engine |
| Engine/systems programmer | Rendering, physics, memory, toolchain | C++/Rust, data structures, graphics fundamentals | Read open-source code, write small engine modules |
| Tools programmer | Build editors and pipelines for designers and artists | Editor extensions, UI frameworks, automation | Write a level-editing plugin for an engine |
| Server programmer | Online sync, accounts, matchmaking, anti-cheat | Network protocols, concurrency, databases | Build the backend for a small online game |
| Graphics/technical artist | Rendering effects, performance optimization, art pipelines | Shaders, render pipelines, art tools | Recreate classic shader effects |

For deeper routes, see the [Programming Handbook](../fundamentals/programming/README.md) and [Engine Internals Path](../fundamentals/engine-internals/README.md).

## 2. Design Track

Decides "what you play" and "why it's fun". Design is not writing documents; it is making verifiable decisions, again and again.

| Role | What they do | Core skills |
| --- | --- | --- |
| Systems designer | Core loops, progression, economy systems | System breakdown, spreadsheets and balance modeling |
| Balance designer | Combat formulas, drop rates, economy balance | Math, Excel/Python modeling, probabilistic intuition |
| Level designer | Space, pacing, teaching, challenge | Level editors, pacing design, whitebox |
| Combat designer | Game feel, abilities, enemies and bosses | Action fundamentals, frame data, play/counterplay analysis |
| Narrative designer | Worldbuilding, story, dialogue, quests | Writing, branching structure, staging |

How to start: break down the core loops of three games you like and write them up; then build three small gameplay prototypes of your own. See the [Game Design Handbook](../fundamentals/game-design/README.md) and [Level Design Handbook](../fundamentals/level-design/README.md).

## 3. Art Track

Decides everything you see in the game.

| Role | What they do | Core skills |
| --- | --- | --- |
| Concept artist | Set the style, produce designs | Form, color, silhouette design |
| 2D artist | Characters, environments, UI, icons | Pixel/vector/painting pipelines, sprite atlas standards |
| 3D artist | Modeling, UVs, texturing, rigging | Modeling software, topology, PBR workflows |
| Animator | Character animation, effects animation | Keyframes, curves, animation principles |
| VFX artist | Hit effects, explosions, ambient effects | Particle systems, materials, timing |
| UI artist | Interface visuals and interaction mockups | Typography, component specs, motion design |
| Technical artist (TA) | The bridge between art and programming | Shaders, scripting, pipeline tools |

A portfolio matters more than a degree: 3–5 complete works, each of which you can explain clearly in terms of "goal, approach, result". For using AI-assisted tools, see the [AI Workflows Handbook](../ai/README.md).

## 4. Audio Track

| Role | What they do | Core skills |
| --- | --- | --- |
| Sound designer | Impact feel, ambience, Foley | Recording, synthesis, audio processing |
| Composer | Main themes, adaptive music | Music theory, harmony, emotional design |
| Audio implementer | Hook sound into the engine, control the mix | Middleware, script triggers, mixing buses |

Crossing over mid-career works: properly implementing and mixing free asset-library sounds is effective practice too. See the [Art & Audio Handbook](../fundamentals/art-audio/README.md).

## 5. Production Track

| Role | What they do | Core skills |
| --- | --- | --- |
| Producer | Set direction, manage risk, manage up and out | Judgment, communication, cutting requirements |
| Project manager | Scheduling, coordination, chasing blockers | Task breakdown, tools (kanban/docs), forecasting |

See the [Production Handbook](../fundamentals/production/README.md). Indie developers should set aside half a day each week for "producer time": check progress, cut scope, re-prioritize.

## 6. Testing Track (QA)

| Role | What they do | Core skills |
| --- | --- | --- |
| Functional testing | Verify features and regressions against test cases | Test-case design, boundary thinking |
| Compatibility testing | Device, resolution and performance matrices | Device management, performance tools |
| Automation testing | Scripted regression, record and replay | Scripting languages, CI integration |

QA is one of the fastest roles for understanding the product as a whole; people often move from it into design or production.

## 7. Publishing Track (Marketing & Business)

| Role | What they do | Core skills |
| --- | --- | --- |
| Marketing / promotion | Store pages, trailers, community, KOLs | Content planning, channel understanding, data postmortems |
| Business development | Platform relations, publishing deals, trade shows | Negotiation, networking, contract basics |
| Publishing ops | Wishlists, launch cadence, promotions | Platform backends, data metrics |

For indie developers, "publishing" is something you do yourself: see the [Multi-platform Launch Playbook](../../playbooks/platform-launch/README.md) for wishlist management and store-page polish.

## 8. Live-Ops Track

| Role | What they do | Core skills |
| --- | --- | --- |
| Community operations | Player communication, events, feedback loops | Content, empathy, crisis handling |
| Data analysis | Retention, conversion, spending analysis | SQL, metric systems, experiment design |
| Monetization | In-app purchase and event design | Psychological pricing, economy systems |

See the [Live-Ops Handbook](../publishing/live-ops/README.md).

## 9. How to Choose, How to Practice

Three self-check questions:

1. What can you do for several hours straight without getting bored? (Writing code / drawing / deconstructing rules / writing / organizing and coordinating)
2. Would you rather "create from nothing" or "polish what exists to its limit"?
3. How many hours can you consistently put in each week right now?

The matching ways to practice:

| Inclination | Main focus | First thing to do |
| --- | --- | --- |
| Logic and systems | Programming / balance | Build three mechanic prototypes in an engine |
| Aesthetics and expression | Art / narrative | Finish one set of pieces with a unified theme |
| Breakdown and empathy | Design / QA | Break down three games' full loops into documents |
| Organizing and driving | Production / publishing | Organize a game dev event or a release |

A common multi-hat combo for small teams: the programming + art + design triangle; sound and testing are often outsourced. For related experience, see [Indie Developer Profiles](../meta/people/indie/README.md) and the [Indie Survival Playbook](../../playbooks/indie-survival/README.md).

## Further Reading

- [Engine Selection Guide](engine-choice.md): once your craft is chosen, choose your tools.
- [Learning Paths](learning-path.md): stage plans for three routes.
- [Open Source & Book Picks](../../resources/books-and-repos.md): projects worth reading the source of, and book lists.
