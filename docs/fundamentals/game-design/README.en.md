# Ludo Atlas · Game Design Handbook

> Positioning: a design methodology and hands-on handbook that goes from "having an idea" to "proving it's fun," covering the design process, core loops, systems, balance, levels, game feel, UX, narrative and validation methods.
> Companions: the Production Handbook (scheduling and slices) · Pitfalls & Anti-patterns · Resources (tools and courses) · `docs/genres/` (design essentials for each of the 112 genre playbooks).
> This document is a methodology roundup: frameworks are crutches, not scripture — the final standard is "your players measured it as fun."

---

## 1. The Design Process: From Idea to Playable

| Stage | Output | Core question | Bar to clear |
| --- | --- | --- | --- |
| Concept phase | One-line concept (high concept) + one-pager | "What is this game? Who plays it? Why is it fun?" | Makes someone's eyes light up within 10 seconds; explainable in 3 sentences |
| Paper prototype | Sketches of the rules/loop (paper, cards, spreadsheets) | Does the core loop hold up? | After 3 rounds on paper, you want to keep going |
| Digital prototype (toy) | Whitebox demo: core gameplay only, no art | Is the "fun" coming from the gameplay itself? | You never tire of replaying it yourself; test it on 3 people and 1 wants to keep going |
| Vertical slice | A short stretch of experience at final quality | Quality benchmark and effort estimate | Quality at shippable level; used to calibrate scheduling (see the Production Handbook) |
| Production | All the content | Hold quality, control scope | See the Production Handbook |

**Design document tiers (pick by scale; templates in `templates/`)**:

- **One-pager** (any project): concept, player fantasy, core loop, target platforms, competitors and differentiation, risks.
- **Mini GDD** (jams/small projects): + controls, systems list, level list, art/audio direction.
- **Full GDD** (production projects): + detailed system designs, balance baselines, content plan, technical constraints. **Note: the GDD is a "living document," not a contract**: update it every two weeks as validation results come in; delete stale sections outright.

**Iteration loop (runs through the whole project)**: hypothesis → minimal prototype → player test → decision (keep / adjust / cut). Iron rule: **an untested hypothesis doesn't count**; "I think it's fun" has no evidentiary value.

## 2. Core Loops and Experience Goals

### 2.1 The Core Loop

- How to draw it: chain verbs into a loop: `explore → fight → loot → level up → explore (deeper)`. If you can't write the verb loop, you don't have a game yet.
- **Nested loops**: second-scale (input feedback: jump-land), minute-scale (challenge-reward), hour-scale (level-growth), long-term (weeks/seasons: seasons, goals). Every layer needs a "hook" (the pull of the layer above it).
- Check: does the start of each loop make you want another round? Are the loop's rewards paid out as soon as possible (especially at the minute scale)?

### 2.2 Experience Goals and Pillars

- Write 2-4 **experience pillars** (e.g. "tense but fair," "absurd fun," "solitary exploration"); every decision (mechanics/art/music) must be able to answer "which pillar does this serve?"
- Design backwards from the experience (experience-first): first write "what the player should feel right now," then design the rules that produce that feeling.

### 2.3 The MDA Framework (quick version)

**Mechanics (the rules) → Dynamics (gameplay emergence) → Aesthetics (the felt experience)**. When tuning, act at the M end, observe at the D end, sign off at the A end; when player feedback says "boring" or "frustrating," trace it back to the M end to find the cause.

## 3. System and Mechanic Design

- **The three elements of a mechanic**: rules (what you can do) · feedback (what happens when you do it) · cost/trade-off (what you give up to do it). A mechanic without a "cost" is fun handed out for free.
- **Interlocking systems**: make two systems each other's resource (e.g. "exploration yields materials → materials strengthen exploration"), and emergent stories and strategies grow out of it.
- **Complexity budget**: treat the player's learning bandwidth as a budget: teach one new mechanic at a time; use a "cognitive load checklist" to check that new concepts per level stay ≤2.
- **Design pattern library (common paradigms)**:

  | Pattern | Mechanic template | Fits |
  | --- | --- | --- |
  | Risk/reward | Bigger payoff demands bigger risk (extract or dive deeper) | Roguelites, extraction shooters |
  | Resource conversion | A→B→C crafting chains | Building, survival |
  | Set collection | Collect, then a completion reward | Compendiums, pets |
  | Time pressure | Timed tasks shift decision weights | Rhythm, arcade |
  | Dueling resources | Two resource pools hold each other in check (health/heat, light/dark) | Stealth, puzzle |
  | Visible progress | The progress bar is the motivation (XP, achievements) | Everywhere |

- **Control mapping**: a 1:1 verb-to-input mapping comes first; button combos, long presses and double taps are "advanced grammar," introduced only once the player is fluent.

## 4. Numbers and Balance

### 4.1 Balance Table Methodology

- **Tables before code**: every tunable value goes into a CSV/spreadsheet (columns: parameter / initial value / unit / notes / test log), and the code only reads the table.
- Suggested structure: gameplay values, growth curves, enemy stats, drop tables and economy pricing each get a separate sheet.

### 4.2 Growth Curves

| Curve | Shape | Used for | Watch out for |
| --- | --- | --- | --- |
| Linear | Constant rate | Fallbacks, short-term values | Loses the sense of progress over the long run |
| Exponential | Rises faster and faster | Power, level requirements | Prone to blowing up; pair it with a "soft cap / decay" |
| Logarithmic / square root | Fast, then slow | Stat returns | Fits "stacking with diminishing returns" design |
| S-curve | Slow-fast-slow | Mastery, gathering efficiency | Naturally staged feedback |
| Stepped | Discrete jumps | Gear tiers, realm stages | Each tier needs a perceptible leap in quality |

### 4.3 Damage and Formulas (example approach)

- Mixing multiplicative and additive terms needs a reason: damage = base × attack/defense modifier × crit × skill. **For armor mitigation, use a curve like `damage × (1 - armor/(armor+K))`** to avoid negative damage and infinite mitigation.
- Before changing a formula, ask: could it produce an "invincible build"? What happens at extreme values (everything stacked into one stat)?

### 4.4 The Economy

- **Faucets and sinks**: every currency needs production and consumption of comparable scale; draw a "currency flow diagram" marking every faucet, sink and rate.
- Inflation control: add sink consumption as versions progress (cosmetics / consumables / taxes) + limit infinite generation.
- Currency tiers: primary currency (general use) / premium currency (purpose-limited) / social currency; keep the layers few and clear.

### 4.5 Balance Methodology

1. **Anchoring**: define a baseline unit (1 point of damage = how many seconds = how many gold), and express every value relative to the anchor.
2. **Relative balance**: don't chase absolute balance; make "each option optimal in a specific situation" (the cost of rock-paper-scissors).
3. **Data and feel, double-checked**: reason on paper → measure in game → tune → test again; log every change to prevent flip-flopping.
4. **Metagame check**: work out whether the three strongest strategies are the same build; leave counterplay against "routine traps."

### 4.6 Randomness Design

- Variance and experience: high randomness is exciting but frustration-prone; low randomness is steady but flat. Choose by pillar.
- Techniques: pseudo-random distribution (prevents bad-luck streaks), pity systems (gacha/drops), weight tables, dynamic weights (compensation for unpopular picks).

## 5. Level Design

- **Elements**: space (paths / sightlines / cover) · guidance (visual / audio / lighting) · pacing (swings in intensity) · reward (payoff for exploration).
- **Tutorial levels (wordless teaching)**: safe environment → introduce danger (nothing lethal) → combined application; shape player expectations with the "the environment cannot lie" principle (everything you can see is reachable).
- **Pacing curve**: tension and release alternate (a taut encounter → a safe zone / narrative treat); always put a "breathing point" before a boss or climax.
- **Metrics**: define in-game units (e.g. "a jump = 1 unit") and express all jump distances / platform gaps in those units, with tolerance built in (a ×1.2 design margin on what a normal jump can reach).
- **Iteration workflow**: paper layout → playable whitebox → guidance testing (watch where players get lost) → art pass → polish. **After every change, observe again instead of asking again.**
- **Structural tools**: gates / paths / landmarks (teasing distant areas), one-way doors, looping shortcuts; in open spaces, use "points-of-interest density" to distribute pacing.

## 6. Difficulty, Game Feel and Accessibility

### 6.1 Difficulty

- Difficulty curve: an overall climb plus periodic "mini-climaxes"; leave room for dynamic fine-tuning of "falling behind / pulling ahead" (use forced DDA sparingly, keep it transparent or toggleable).
- Give different players options: difficulty tiers, assist modes, official "cheat" toggles (at a cost: achievements disabled, etc.) — more modern than forcing one shared experience.

### 6.2 Game Feel Checklist

| Item | Method | Notes |
| --- | --- | --- |
| Input buffering | Queue inputs made within 100-200ms | Landing jumps/attacks don't drop commands |
| Coyote time | Still able to jump for 80-150ms after leaving a ledge | The grace window cuts "but I pressed it" frustration |
| Speed curves | Separate parameters for acceleration / deceleration / air control | The three big knobs of feel tuning |
| Screen feedback | Screen shake, hitstop, zoom pulses | The hit-impact trio; must be toggleable |
| Audio reinforcement | Action sounds / hit sounds / layered sounds | Audio is half of game feel (see the Art & Audio Handbook) |
| Particles and trails | Trails, hit sparks, dust | Low cost, high perceived value |

### 6.3 Accessibility

- Basics: key remapping, subtitles (size / background / speaker), colorblind modes, UI scaling, brightness/contrast, no-QTE alternatives, camera shake toggle.
- References: Game Accessibility Guidelines (https://gameaccessibilityguidelines.com/) and platform accessibility guidelines; console platforms each have their own accessibility tag system — check against it before submission.
- Business value: accessibility design benefits all players at once (subtitles and remapping especially).

## 7. UX and Onboarding

- **First-minute experience (FTUE)**: the first 60 seconds must contain "one moment of delight + one decision"; the first 10 minutes must teach the core loop.
- **Information hierarchy**: the HUD shows only "the information needed for the decision right now"; it can expand or be hidden.
- **Three rules of feedback**: timely (from the same frame to within 200ms) · clear (what changed) · proportionate (doesn't block the view or fatigue the player).
- **Tutorial approaches compared**: contextual teaching (learning by doing) > forced pop-ups; when a pop-up is unavoidable, one concept per screen.
- **Defaults are tutorials**: sensible defaults (auto-pathfinding on, assists off) + explanatory copy for each setting.

## 8. Narrative Design

- **Choosing a structure**: linear (low cost, controllable experience) · branching (a sense of choice; cost grows exponentially with branch count) · sandbox/emergent (systems produce stories) · hybrid (linear main line + branching side content).
- **Managing branch cost**: converge branches at "merge points"; put heavy content (animation/VO) on the trunk and light content (text/variants) on branches; "selective perception" (choices shape attitudes and NPC lines rather than the global state).
- **Layers of worldbuilding**: environmental storytelling (scene props / layout) → collectibles (fragmentary text) → dialogue (the most common, and the easiest to skip); put what matters in the earlier layers.
- **Dialogue design**: one "voice sheet" per character (word choice / sentence length / taboos); in choices, avoid fake choices where "all three options lead to the same result" (if you're going to do it, do a real branch; if not, cut it).
- **Gameplay as metaphor**: mechanics resonating with the theme (e.g. "inventory management = the burden of memory") — that's the biggest narrative advantage indie games have.

## 9. Gameplay Validation and Design Review

### 9.1 Testing Methods

| Method | When | Key points |
| --- | --- | --- |
| Self-testing | Throughout | Log the moments you get stuck or want to skip — they're all signals |
| Internal cross-testing | After the prototype | Observers keep quiet and only take notes (no hints) |
| External playtests | After the slice | 5+ target players; watch behavior, not questionnaires |
| Analytics | Once you have volume | Pass rates / session length / drop-off points; keep it lightweight during prototyping |

**Three iron rules**: don't ask "do you think it's fun?" (stated preference is an unreliable answer); ask "what were you trying to do just now / what was the most boring part"; observed behavior > spoken feedback.

### 9.2 Design Review Checklist (run through it before every major change)

- Aligned with the experience pillars? Is the core loop clearer or more complicated? Is the added cost (learning + production) worth it?
- Is the balance table updated? Have the knock-on effects on economy/balance been assessed? What gets cut to pay for it?
- What's the player validation plan? (who, when, how)

## 10. Toolbox and Where to Go Next

- **System modeling**: Machinations (https://machinations.io/, visual simulation of economies and loops).
- **Templates**: one-pager / GDD / playtest plan → `templates/` (see Design Documents §9).
- **Design essentials by genre**: `docs/genres/` (112 genres, each with its own `design.md`).
- **Theory reading**: the MDA paper, flow theory, Jesse Schell's The Art of Game Design, Raph Koster's A Theory of Fun for Game Design. Full bibliography in Resources §3.
- **Where to go next in design**: break down a game you love (write out its verb loop and economy diagram) → validate a new mechanic with a paper prototype → move on to the Production Handbook and build your first vertical slice.
