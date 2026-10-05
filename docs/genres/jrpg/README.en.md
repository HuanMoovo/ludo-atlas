# Ludo Atlas · Genre Handbooks · JRPG

> **Genre Handbooks · Volume 2**. Positioning: a party RPG pulled forward by story and framed by command-based combat, where victory and defeat turn on decisions about resources, counters and turn order — and content volume is this genre's largest cost.
> Companions: Game Design Handbook (combat and progression systems) · Programming Handbook (data pipelines and saves) · Level Design Handbook (town and dungeon spaces) · Case Studies (breakdown and retrospective methods).

---

## 1. Positioning and Core Loop

One-line positioning: a JRPG is a **narrative-driven party RPG**. Combat resolves through commands (turn-based or semi-real-time), and victory and defeat are decided mainly by decisions — resource management, elemental counters, turn order — rather than execution precision. The boundary test is direct: strip out all real-time input, and the combat still stands, with the cause of any loss reviewable in a menu — that is a JRPG.

The core loop, written as a verb chain: `push through the map → trigger combat → play out the command duel → resolve rewards → reinforce through growth → unlock new areas and new story`

The loop has four layers:

| Layer | Loop | What holds players |
| --- | --- | --- |
| Second-to-second | Issue a command → resolve the feedback | Damage numbers, hit sounds, action staging |
| Battle | Encounter → decisions → win or lose | The retrospective satisfaction of winning from behind; the tension of resources draining away |
| Chapter | Town resupply → dungeon exploration → story beats | The pull of "I want to know what happens next" |
| Playthrough | Clear the game → collection and hidden content | New Game Plus, compendiums, hidden bosses |

Drawing boundaries against neighboring genres:

| Neighboring genre | Boundary |
| --- | --- |
| Action RPG (ARPG) | Combat runs on real-time execution and hit feel; the JRPG settles victory in menus |
| Tactical RPG (SRPG) | SRPGs spread combat across grids and positioning; the JRPG's spatial layer lives in towns and dungeons |
| Monster collection games | Collection and raising are the spine; the JRPG runs on a fixed party and story |
| Visual novel | Progress comes from reading and choices; in a JRPG the story only advances through combat and exploration |
| Western RPG (CRPG) | Character-build freedom and branching endings carry more weight; the JRPG stays closer to a single main line plus optional side quests |

A self-check question: turn off all battle animations and leave only text resolution — is the combat still fun? If the answer is "yes", your decision layer stands on its own; if it is "no", what you have built is not combat but staging.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Visible growth**: the payoff from a level-up, a new skill or new gear is felt immediately — numbers and abilities strengthen together.
2. **Winning by strategy**: you win because you thought it through (counters, order, resources), and a loss can be reviewed; the way out of frustration is "I'll play it differently next time".
3. **Narrative pull**: every stage ends with a reason to want the next chapter.
4. **Party development and exploration rewards**: characters have personality and signature abilities; treasure chests, side quests and hidden bosses give real rewards to players willing to take the long way around.

Benchmark titles (a widely known list; play them yourself before breaking them down):

| Title | What to learn from it |
| --- | --- |
| Dragon Quest series | Minimal commands, classic pacing; any player can see what to do next |
| Final Fantasy series | A history of combat-system iteration: Active Time Battle, jobs, growth grids and the boundaries of escalating presentation |
| Pokémon series | A loop driven by collection and raising, a counter matrix, zero-friction onboarding |
| Persona 5 | The calendar and daily rhythm, the double loop of daily life and dungeon runs, the benchmark for stylized presentation |
| Octopath Traveler | A pixel JRPG at modern scale: the Break mechanic and a multi-character party structure |
| Chrono Trigger | The golden sample of no random encounters, multiple endings and pacing control |

The genre's baseline expectations (missing any of these earns negative reviews outright): suspend saves available at any time, skippable or speed-up battle animations, clear objective guidance, and failure penalties that are not too heavy. Modern titles treat auto-battle, encounter toggles and fast travel as standard equipment — leave room for them from the prototype stage.

## 3. Design Essentials

### 3.1 Combat System: Turn Order, Resources and Decision Space

Combat is the JRPG's skeleton; settle three things first: how turn order is arranged, what the resources are, and how many worthwhile paths each turn offers.

The four mainstream turn-order models:

| Model | Method | Representatives | Cost |
| --- | --- | --- | --- |
| Fixed turn-based | Reorder by speed each round; everyone acts once | Dragon Quest, Pokémon | No time pressure; all tension rests on resources and counters |
| Active Time Battle (ATB) | Action timing follows gauge fill speed; the menu can pause it | Final Fantasy series | Complex UI and pause rules; beginners panic easily |
| Predictable order | The turn order is fully displayed; skills can push actions later or earlier | A common modern turn-based approach | Needs order-manipulation skills to support it |
| Semi-real-time hybrid | A turn-based skeleton with real-time elements (follow-up actions, combos) | The follow-up actions of the Persona series | Rules cost more to explain; the teaching load rises |

Three disciplines for turn-order design:

- Speed is a hidden power stat (first strike, action count, healing timing): either compress the speed range and cap it, or turn "winning the speed race" into a skill effect rather than pure stat stacking.
- Tie-breaking rules must be deterministic and visible: a fixed priority order or a fixed random rule, written down and never wavering.
- Turn order must be visible, so players can work out whether they can take one more hit and still heal in time; then keep a set of delay and haste skills as pacing valves, so that order itself becomes gameplay.

Resource model: resources are combat's currency; the mainstream structure is HP plus one resource pool (MP, SP and the like) plus consumables.

- Variants: skill charges (usable every N rounds), cost-type resources (spending HP or items), and per-battle resources (limited by time or turn count).
- Three design questions: what is scarcest in this battle? Which skills are worth paying for with it? What options remain once resources bottom out? There is only one acceptance criterion: resources must create the dilemma of "use the ultimate or not" — an answer that is always yes, or always no, means it was never designed.

Elemental counters and duration budgets:

- Keep the number of elements to 4–8; common multipliers are 1.5–2× when strong against, 0.5× when weak against, 0× when immune (the Pokémon style uses two tiers, 2× and 0.5×); counters must be visible — no hidden multipliers that only guide sites know about.
- Duration references: standard fights 3–5 rounds (about 30–90 seconds), elite fights 5–8 rounds, boss fights 10–20 rounds across 2–3 phases. Staging serves this budget — when more than half of a battle is spent watching animations, players start dodging fights.

### 3.2 Party and Progression: Jobs, Skill Trees and Curves

- Active party size is commonly 3–4; benched members receive partial experience (commonly around 50%) so that a benchwarmer is never permanently locked out of the party.
- The job system comes in three routes; see the costs clearly before choosing:

| Route | Method | Strengths | Cost |
| --- | --- | --- | --- |
| Fixed roles | Signature skills bound to each character's identity | High character recognition; mechanics and narrative are one | Low freedom in party building |
| Job switching | A shared job pool with free class changes (a series tradition in Final Fantasy and Dragon Quest) | Build freedom and replayability | Characters homogenize; the balance surface multiplies |
| Hybrid | A character-specific base plus learnable sub-jobs | Balances identity and builds (the Octopath Traveler way) | Unlock and tutorial flows get more complex |

- Skill-tree granularity: 15–30 skills per character (passives included), with 4–8 usable on one screen (a menu constraint); group them by function: damage (single-target and area), recovery, buffs and debuffs, control, passives.
- Level-up rewards must rotate in qualitative nodes: new skills, new commands, combo unlocks. Several consecutive levels of stat growth alone make players lose interest along the way.
- Level caps commonly run 50–99; leave 2–4 levels of growth room per map and write "expected level = map index × coefficient" into the tables. Be careful with free stat allocation — players will build a save-breaking character; either offer cheap respecs or replace it with fixed growth plus a skill tree.
- Attack and HP must grow at the same rate for battle length to stay stable: stacking only attack turns fights into mutual one-shots, and stacking only HP drags them out.
- Keep equipment simple: three slots — weapon, armor, accessory — are enough. Equipment's job is reward pacing (chests, shops, boss drops) and a little role definition, not a dumping ground for stat stacking.

### 3.3 World Structure and Narrative Pacing: Towns, Dungeons and Story Beats

The structural unit is fixed as a formula: `town → field encounters → dungeon → boss → story beat → new area`. Each unit has its own job:

| Unit | Function | Design points |
| --- | --- | --- |
| Town | Resupply, information, shops, story progress | Every town gives at least one new piece of information; dialogue updates on return visits |
| Field | Encounters, resources, small events | Offer detour routes; not every square has to force a fight |
| Dungeon | Exploration, chests, puzzles, bosses | First clear 15–40 minutes, with a save point every 10–15 minutes; value lies in density, not floor area — design the space following the Level Design Handbook |
| Story beat | Advances the main line and character arcs | 1–2 per area; the moment a beat ends, say where to go next |

Pacing goals (tunable per project, but all four need watching):

- The objective is always clear: at any moment the player can say where to go next, and why.
- Three tracks in rotation: exploration (containing 2–4 fights), an event or a new skill, a dungeon, a story beat — cycled to avoid long stretches of a single activity.
- Hook cadence: every area ends on a cliffhanger, and the gap between main-line beats never runs past an hour or two; the first 30 minutes must contain one battle victory and one hook — no long walls of text explaining the world.
- Side quests are pacing buffers: place them in the main line's troughs, aim rewards at growth and companion stories, and never let them be pure filler.

### 3.4 Text and Staging Volume: Accounting for the Biggest Cost

- Estimation method: take net reading time as 20–30% of total playtime and reading speed as 200–300 characters per minute, which yields roughly 2,500–5,500 characters of main-line text per hour; multiply by 1.5–2.5× to get the total volume including side quests, menus and compendiums.
- Extrapolated by this method:

| Playtime | Main-line story text (by this method) | Total volume (side quests and menus included) |
| --- | --- | --- |
| 1 hour | 3,000–6,000 characters | around 10,000 characters |
| 5 hours | 15,000–30,000 characters | 30,000–60,000 characters |
| 10 hours | 30,000–50,000 characters | 60,000–120,000 characters |
| 20 hours | 60,000–110,000 characters | 150,000–250,000 characters |
| 30+ hours | 100,000–160,000 characters | 250,000+ characters |

- Staging is allocated in tiers: tier S (fully animated cutscenes or major CG), tier A (camera movement plus character staging), tier B (dialogue boxes plus expression changes). Tier S is capped at "single digits across the whole game" and reserved for main-line milestones; tier B carries 90% of the information. A staging budget without caps will inevitably run away.
- Voice acting is usually the largest single audio cost, and the common compromise is voicing key scenes only; for BGM, 20–60 tracks is a typical magnitude. Skill descriptions, item descriptions, compendiums, tutorials and UI copy all have to be written, proofed and translated — forgetting to budget this block is the norm.

### 3.5 Combat Balance and the Number-Tuning Process

A five-step process; do not skip the order:

1. **Paper math**: turn the damage formula, growth curve and skill multipliers into a calculable sheet; first use expected values to work out by hand how many rounds a standard fight lasts.
2. **Scripted simulation**: move the formulas into a spreadsheet or Python, run 1,000–10,000 battles in batch, and tally win rates, average rounds and resource consumption. Change one variable, run it again, and a set of conclusions takes minutes.
3. **In-game logging**: record each battle's inputs, random seeds and resolution; on a loss, show a review panel (who died to which skill, and by how much).
4. **Human playtests**: watch skill usage rates, potion consumption, death points and quit points; when data and intuition conflict, trust the data, then look for the reason.
5. **Freeze and regression**: after the numbers are frozen, log every change and rerun the baseline battle set (the same fixed party fighting the same 5 battles), so that fixing one thing does not break ten.

Acceptance metrics (observable):

- No single dominant skill that shows up in more than half of battles; skills below 5% long-term usage go on the prune-or-rework list.
- Standard fights average 3–5 rounds and boss fights 10–20; three party setups (balanced, burst, defensive) can all clear the main line in the simulation script.
- Testers can explain the cause of their most recent loss, and it matches the design intent.

## 4. Technical Essentials

### 4.1 Data-Driven Design and Formulas

- All numbers go into tables: level curves, enemies, skills, equipment, drops; keep only formula functions in code, manage the tables as CSV or JSON, generate game assets with export scripts, and never hand-edit the generated output.
- Reference integrity goes into CI: skill IDs, drop tables and localization keys reference each other — run validation scripts. Once tables pass a thousand rows, typos are the largest source of bugs. Keep combat formulas in one module with comments, so every change is traceable.

### 4.2 Layering Resolution and Staging

- Resolve a round into a list of events first (who acted on whom, what they did, how much damage, whether anyone fell), then play animations from that list; skipping and speed-ups affect only the player, never the resolution. This is the single most important architectural decision in a battle system.
- Decouple the battle state machine from the map scene: enter → gather commands → resolve in order → play events → judge victory → return. With clean states, saves and debug tools can hook in.
- Use a seedable, deterministic RNG: crits, hit checks and drops all run through one seed manager, so a bugged battle can be reproduced.

### 4.3 Saves and Debug Tools

- Put world state into a single table: story progress, chests, NPC states and side-quest flags; a save = party data + world state + version number.
- Build save version migration from day one: post-launch updates are routine, and a save that will not open is the most damaging kind of amateur accident.
- Autosaves and suspend saves: fixed trigger points (entering a town, entering a dungeon, before a boss, after a story beat); the suspend save is the floor for handheld play and fragmented play sessions.
- The development panel is mandatory: level skipping, money and item grants, forced and disabled encounters, one-hit kills, battle skip, story skip, and playback of any staged sequence; battle replays record the seed plus the input sequence, so a problematic fight reproduces in one click; check menu and compendium responsiveness frame by frame too — confirm, page-turn and scroll must all be immediate.

### 4.4 Text and Localization

- Give every string an ID and ban hardcoding; establish a glossary for character names, place names and skill names before writing the body text.
- Organize for translation from day one: export the translation table → translate → import back → validate terminology; every added language runs the whole pipeline once, checking line breaks and fonts.
- Confirm the commercial license for each CJK font individually; reserve 30% extra UI width for the longest target language.

## 5. Content Volume and Workload Reference

| Tier | Scale | Time reference | Notes |
| --- | --- | --- | --- |
| Prototype (vertical slice) | 1 town + 1 dungeon + 3 standard fights + 1 boss + opening story | 3–6 weeks | Validates only the combat and growth loop |
| Small finished title | 4–6 areas, 8–12 enemy types, 6–10 hours of play | 8–12 months (solo) | One combat system plus one main line |
| Mid-size title | 10–15 areas, 30–50 enemy types, 15–25 hours of play | 2–3 years (small team) | Content production and polish split the time evenly |
| Large title | 30+ areas, 100+ enemy types, 30+ hours of play | Multiple years with a team | Only a series pays the cost back |

Cost breakdown (each content block gets its own budget line):

| Content block | Magnitude anchor | Cost profile |
| --- | --- | --- |
| Combat content | 30–80 enemy types, 100–300 skills | Every enemy equals a whole set of numbers, skills, animations and encounter setup |
| Text and narrative | See the method table in §3.4 | The largest single item, and it does not compress |
| Maps and scenes | 5–10 scene blocks per area | Town and dungeon art specs run in parallel |
| Staging and audio | Tier-S staging priced by the minute | The highest unit cost; rationed by cap |
| Interface and systems | Menus, compendiums, saves, battle UI | The most easily underestimated; schedule it as its own line |

These magnitudes are for scope estimation and are not a commitment. Scheduling anchors: combat prototype 2–4 weeks; vertical slice 2–4 months; after that, extrapolate from content volume, scheduling later content conservatively at a 0.6–0.8 output factor. Scope running away is this genre's most common cause of death — cutting areas is always safer than cutting combat depth.

## 6. How to Start the First Prototype

Goal: in 3–4 weeks, build the minimal loop — "can fight, can grow, can save, has one short story stretch" — without touching art, side quests, a world map or crafting systems. Two engine routes: RPG Maker provides a complete combat and map framework and is the fastest way to start; for a deeply customized combat system, go with Godot or Unity, using data tables plus a self-built battle state machine.

- Week 1: combat loop. A 3-person party against 1 enemy type, 4 skills (single-target damage, area attack, healing, buff), speed-sorted turn order, experience on victory.
- Week 2: growth loop. Level-ups unlocking new skills, save and load, map encounters and the battle transition, and one town with nothing but a healing point and a placeholder shop.
- Week 3: miniature content. A whitebox dungeon (10 minutes to cross) plus 3 standard fights plus 1 boss, with a 5-minute opening story.
- Week 4: playtest and judgment. Get 5 people through the whole flow, recording battle duration, skill usage, stuck points and willingness to retry.

Success criteria (all observable):

- With zero art and zero audio, testers are willing to finish the boss and want the next stretch.
- Standard fights average no more than 3 rounds; the boss fight runs 5–10 minutes, with one or two losses allowed.
- Testers can explain the cause of a loss, matching the design intent; changing one number (boss attack ±10%) has its impact quantified within 10 minutes — provided the simulation script and logs are in place.

Decision gate: if the combat loop does not pass the playtest, do not start mass-producing content. Replace the combat system first, then talk about piling on content; reversing the order means paying tuition for foundation rework.

## 7. Common Pitfalls

1. **Stacking too many combat systems**: combos, fusion skills, terrain and summons all built at once, none polished to the point of fun. Avoidance: make one core system plus one variation stand first; everything else goes on the backlog.
2. **Unskippable animations and no speed-up**: players start dodging fights from hour three. Avoidance: build skip, speed-up and auto-battle during the prototype — the cost is tiny and the payoff is huge.
3. **Balancing by feel, testing one setup**: without simulation and logs, a boss is either unwinnable or unloseable, and balance covers only the default party. Avoidance: follow the five-step process in §3.5; run three party setups through the simulation script.
4. **Dead skills and one dominant answer**: half the menu goes unused, or one skill beats everything. Avoidance: prune with usage data, and change mechanics before changing numbers.
5. **Underestimating content volume**: estimating text, maps, battle setup and staging all at feature-development speed is a guaranteed crash. Avoidance: build the budget lines from §5 at greenlight, and ID-ify text from day one.
6. **Encounter torture**: a high encounter rate with unskippable battles and escape animations. Avoidance: visible encounters or an adjustable encounter rate, and lower encounter density in late-game maps.
7. **Story drought or story dump**: 30 minutes of pure exposition up front, or hours without a story beat. Avoidance: deliver one victory and one hook within the first half hour; 1–2 beats per area.
8. **Growth you cannot feel**: level-ups only add percentages, with no qualitative change. Avoidance: make new skills, new commands and combo attacks the bulk of level-up rewards.
9. **Missing save expectations**: no autosave, no save point before a boss, no suspend save. Avoidance: treat saves as experience design and implement the trigger-point checklist item by item.
10. **Dungeons that chase size**: 40-minute straight corridors with no landmarks, rewards or rhythm. Avoidance: follow the metrics and landmark methods in the Level Design Handbook.

## Further Reading

- [Game Design Handbook](../../fundamentals/game-design/README.md): the base document for core loops, combat systems and number methods.
- [Programming Handbook](../../fundamentals/programming/README.md): implementation details for data-driven design, saves and debug tooling.
- [Level Design Handbook](../../fundamentals/level-design/README.md): spatial design for towns and dungeons, and the whitebox workflow.
- [Case Studies](../../postmortems/README.md): retrospective methods for success and failure cases — consult when choosing or dissecting a project.
- [Pitfalls & Anti-patterns](../../pitfalls/README.md): pitfalls around greenlighting and content production; read against §7 on this page.
- [Indie Survival](../../../playbooks/indie-survival/README.md): scope control and scheduling, complementing §5.
