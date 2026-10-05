# Ludo Atlas · Getting Started · Game Development at a Glance

> **Getting Started**. This page answers four questions: how games get made, what each kind of person on a team does, where the money comes from, and the six assumptions beginners most often get wrong. Read it before deciding which direction to go.

## 1. How a Game Gets Made

The process at a mature studio looks roughly like this. Indie development trims it down, but the order barely changes:

| Stage | What happens | Typical output | Time reference |
| --- | --- | --- | --- |
| Concept | Get clear on "who it's for, what you play, and why it's fun" | One-page kickoff doc, prototype goal list | Days to a few weeks |
| Prototype | Validate the core loop in the crudest possible way | A playable prototype that runs but looks bad | 1–4 weeks |
| Vertical slice | Bring "one short stretch of the full experience" to near-final quality | One complete, presentable level | 1–3 months |
| Production | Mass-produce levels, assets and systems | All of the game's content | 3+ months solo, 1+ year for a team |
| Polish | Game feel, balance, performance, bug fixes | A release-ready build | 1–3 months |
| Launch | Store page, marketing, platform review | A product live on storefronts | 1–2 months |
| Live-Ops | Updates, bug fixes, community management, post-launch content | Long-term revenue and reputation | Ongoing |

The details of each step are spread across the handbooks in this repository; this page only gives the map:

| What you want to get right | Where to look |
| --- | --- |
| Gameplay, systems, balance | [Game Design Handbook](../fundamentals/game-design/README.md) |
| Code, architecture, performance | [Programming Handbook](../fundamentals/programming/README.md) |
| Art and audio production | [Art & Audio Handbook](../fundamentals/art-audio/README.md) |
| Scheduling and scope control | [Production Handbook](../fundamentals/production/README.md) |
| Levels | [Level Design Handbook](../fundamentals/level-design/README.md) |
| After launch | [Live-Ops & Growth](../publishing/live-ops/README.md) |

## 2. Who's on the Team

Work in the game industry can be roughly split into eight tracks. For each role's full skill stack and entry path, see the [Roles & Skills Map](role-map.md); here is the one-line version:

| Track | Roles | One-line responsibility |
| --- | --- | --- |
| Programming | Gameplay / engine / tools / server | Turn design into working reality, and keep it smooth and crash-free |
| Design | Systems / balance / levels / narrative / combat | Decide "what you play" and "why it's fun" |
| Art | Concept / 2D / 3D / animation / VFX / UI / TA | Decide what the game looks like, and how everything you see moves |
| Audio | Sound design / composition / audio implementation | Decide how the game sounds; carries half the credit for game feel |
| Production | Producer / project manager | Get the right people doing the right things at the right time, and cut what isn't needed |
| Testing | QA | Find problems before players do, and hold the quality line |
| Publishing | Marketing / business development / platform relations | Make sure the target players know about the game and can buy it |
| Live-Ops | Community / data analysis / monetization | After launch, keep players around and playing longer |

Indie developers usually cover programming, design and some art on their own; small teams first fill in the "programming + art + design" trio.

## 3. Where the Money Comes From

| Business model | How it earns | Commonly seen in |
| --- | --- | --- |
| Premium | One-time purchase | PC, console, polished indie titles |
| In-app purchases (IAP) | Skins, items, gacha, battle passes | Mobile games, some PC online games |
| Ads | Rewarded video, interstitials | Mini-games, hypercasual |
| Hybrid | Premium + DLC / IAP + ads | Many commercial titles |
| Subscription | Membership-based content services | A few products and platform services |
| Crowdfunding / grants | Pre-orders or funding up front | The startup phase of indie projects |

Differences between platforms and form factors (PC, console, mobile, mini-games, web) directly shape the business model and development budget; see the [Multi-platform Launch Playbook](../../playbooks/platform-launch/README.md) and the [Legal, Patents & Competition](../publishing/legal/README.md) for details.

## 4. Three Scales, Three Approaches

| Scale | Headcount | Process traits | Biggest risk |
| --- | --- | --- | --- |
| Indie development | 1–2 people | No meetings, decide as you build; speed first, use ready-made assets | Scope out of control, project never ships |
| Small team | 3–10 people | Light process, weekly iterations; people wear several hats | Communication overhead, direction drift |
| Company | 10+ people | Dedicated roles, stage reviews; documentation and pipelines come first | High cost, slow decisions |

The larger the scale, the more it depends on process and documentation; the smaller the scale, the more it depends on picking the right scope. More on teams and collaboration keeps being added under Teams & Scale.

## 5. Extra Things to Watch for in Mainland China and Going Overseas

- Publishing in mainland China involves game licenses, anti-addiction rules, channel revenue splits and record-filing; see the [Legal, Patents & Competition](../publishing/legal/README.md) for details.
- Mini-games are a distinct engineering form (build size, performance and platform rules all differ); see the [Mini-Game Development](../publishing/minigame/README.md).
- Going overseas means Steam, consoles or overseas mobile stores, each with its own hurdles in testing, ratings and taxes; see the [Multi-platform Launch Playbook](../../playbooks/platform-launch/README.md).

## 6. Six Common Misconceptions

1. "Anyone who plays games can make games": playing is consumption, making is production. Between the two lie the engine, process, and ten thousand debugging passes.
2. "If you can't do art, you can't make games": art can be bought, collaborated on, or stylized. The real bottleneck is finishing.
3. "Pick the wrong engine and it's over": any mainstream engine can get a game finished. The cost of switching is far lower than the cost of never building anything.
4. "Indie development is free and easy": the freedom is real, the ease is not. It is high-intensity self-management.
5. "Coming up with a hit idea comes first": ideas are cheap; building it and pushing it out is what's valuable.
6. "AI is here, one person can make AAA": AI significantly speeds up coding and asset production, but it doesn't make your trade-offs for you. See the [AI Workflows](../ai/README.md).

## 7. Where You Are Now

| Where you are | Next stop |
| --- | --- |
| Wanting clarity on the industry and roles | [Roles & Skills Map](role-map.md) |
| Ready to start making something | [Engine Selection Guide](engine-choice.md) → [Your First Game](first-game.md) |
| Committing long term, planning years ahead | [Learning Paths](learning-path.md) |
| A project in hand, wanting to avoid pitfalls | [Pitfalls & Anti-patterns](../pitfalls/README.md) · [Indie Survival](../../playbooks/indie-survival/README.md) |

## Further Reading

- [Roles & Skills Map](role-map.md): full skill stacks and entry paths for the eight tracks.
- [Resources](../../resources/README.md): the full directory of engines, tools, courses and communities.
- [Case Studies](../postmortems/README.md): four-part breakdowns of successful and failed projects.
