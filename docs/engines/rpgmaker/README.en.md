# Ludo Atlas · Engine Tracks · RPG Maker

> **Engine Tracks**. Positioning: a paid, purpose-built RPG production tool — its map editor and event system press the barrier of entry for traditional 2D RPGs to the floor; suited to prototypes and small-scope works, and not the place to start anything that is not an RPG.
> Companions: Game Design Handbook · Art & Audio Handbook · Multi-platform Launch Playbook · Indie Survival.

---

## 1. Positioning and Choice

In one line: RPG Maker is a **paid production tool tailor-made for traditional 2D RPGs**. It pre-builds the genre's common systems and exposes their parameters and logic: the map editor handles "it draws", the event system handles "it runs" — turn-based combat, the database, saves and menus are all out of the box; without writing a line of code you can build something playable to the ending.

The tool's core is two things:

- The map editor: assemble maps tile by tile; passability, layers and region markers set directly in the editor;
- The event system: dialogue, treasure chests, locked doors, teleports, cutscenes and quest logic unified as "events on tiles", strung into complete flows with conditions and commands.

### Who it fits

- People who want a playable RPG prototype or small-scope work fast: from install to a playable flow, an order of magnitude faster than general engines;
- Solo developers who write no code at all, or do not want to touch programming yet: the mainline stays code-free, extensions come as plugins when needed;
- Projects in the classic JRPG shape: parties, equipment, skills, turn-based combat, towns and dungeons are all default capabilities;
- People validating narrative and level design quickly: change the map, the events, the dialogue — and run it immediately.

### Who it does not fit

- Non-RPG projects: action, platforming, shooters, management sims all fight the tool — a general engine saves more effort;
- Deep combat customization: tactics, ARPGs and card-style combat must move the default framework itself — plugins can patch it, at a high long-term maintenance cost;
- 3D or high-fidelity visual routes: the capability does not exist;
- Large teams and industrial pipelines: project organization and collaboration mechanisms are thin — past small-team scale it strains;
- Engineering-minded teams wanting full control: the editor wraps things deep — the scripting layer can change runtime behavior, but not the editor and toolchain.

When unsure, run the four self-check questions in the [Engine Selection Guide](../../start/engine-choice.md) once more.

## 2. Ecosystem and Project Structure

An RPG Maker project is an ordinary folder: data, assets, scripts and plugins stored in zones, with no compile step — releasing is packaging that folder for each platform. The simple structure is an advantage, and it also means project discipline is entirely yours to set.

### 2.1 Directories and division of labor

| Location | What goes here |
| --- | --- |
| `data/` | Game data: maps, the database, common events |
| `img/` | Tiles, character sheets, faces, enemies, battlebacks and interface assets |
| `audio/` | Four audio classes: BGM, ambience, situational effects and regular sound effects |
| `js/` | Core scripts and the plugin directory (recent generations use JavaScript as the scripting layer) |
| `fonts/`, `movies/` | Fonts and video assets |
| Project root | The entry page and project identity files — no content |

### 2.2 Data and version control

- Recent generations store maps and the database in text formats with readable diffs — good for version control;
- Exclude the test save folder and release artifacts; large assets go through Git LFS to keep the repository from ballooning;
- The project itself is the whole asset: avoid version operations while the editor is running, and commit after each batch of content changes;
- Introducing plugins and assets is a high-risk moment: snapshot before and after, so problems can be rolled back wholesale (see §7).

### 2.3 Plugin ecosystem and the scripting boundary

- Plugins are the officially open extension mechanism: a single script file dropped into the project, ordered, toggled and parameterized in the plugin manager — new systems without writing code;
- The ecosystem covers combat, menus and interfaces, saves and quests, messages and staging, performance tools and more — free and paid works side by side, with uneven quality and maintenance;
- Three checks before adopting a plugin: maintenance status, its binding to engine versions, license terms; a plugin that stopped years ago is evaluated as a "permanent dependency" and never the single pillar on a critical path;
- Know the scripting boundary: plugins can override and extend runtime behavior, but not the editor and toolchain; edits made straight to core scripts get wiped by engine upgrades;
- Deep customization (a brand-new combat system, a brand-new scene structure) enters the maintenance territory of JavaScript and the engine's script architecture — you are evaluating long-term maintenance cost, not one-time development cost.

### 2.4 Bundled assets and licensing

- Assets that ship with the program (commonly known as the RTP) are not public assets: the license binds to "the version you hold", and the permitted scope shifts as the official terms are updated;
- The relatively stable floor: usable only in games you create; never extracted separately, resold, redistributed or packaged into an asset library, and never claimed as your own;
- Questions like "may I reuse it elsewhere" defer to the official terms and the license text of your version — not to second-hand conclusions in old community posts;
- DLC asset packs in the official store and third-party packs each carry their own terms (commercial scope, attribution, whether editing is allowed) — check pack by pack and keep records;
- The bundled sample game's assets are usually restricted separately: the sample project is for studying structure, not for lifting as an asset library.

## 3. Core Workflows

### 3.1 From zero to running

1. Create the project: settle resolution and the default battle template; keep the project path short and in English, away from cloud-sync folders;
2. Draw the map: use default tiles to lay out "one town, one dungeon" first, marking regions along the way;
3. Enter the database: stand up a minimal set of actors, skills, enemies and items — just enough for one battle;
4. Write events: dialogue, chests, locked doors, teleports and quest triggers all become events; build switch and variable registers before starting (see §4.3);
5. Test: the editor has built-in test play — change a piece, test a piece; do not save up a big batch and hunt problems later;
6. Add plugins: introduce needed systems one at a time, running a regression over affected scenes after each addition (see §4.6);
7. Wrap up: replace default assets, finish the text, clean unused resources, then move to export.

### 3.2 Export and release platforms

| Target | Route | Notes |
| --- | --- | --- |
| Windows, macOS | Official deployment produces desktop programs directly | The mainstream shipping form; signing and distribution follow your channel (details in the Multi-platform Launch Playbook) |
| Web browsers | Deploy as a web page; upload to hosting and it plays | Verify locally through a local server; audio needs one prior user interaction |
| Mobile | Run the browser build first, or follow a separate packaging flow | Touch controls, performance and audio strategy need dedicated adaptation |
| Consoles | No universal one-click export | Console releases need a separate porting and publishing route |

Pre-release checklist: default assets replaced, unused assets cleaned, the full chain from boot to loading a save verified on target devices, and store assets and copy prepared.

## 4. Idioms for Key Systems

This section is RPG Maker's way of thinking: it abstracts the game into "events on maps" plus "global switches and variables." Following that abstraction works twice as well; fighting it chafes everywhere.

### 4.1 Maps: tiles are both canvas and data

- Maps are assembled from tiles, and tile passability is maintained in the database's tilesets; set drawing, passability and regions in the editor once and well;
- Region markers are not decoration: encounter zones, event checks and plugin logic all rely on them — decide what each ID means while planning;
- Keep map sizes restrained: several small maps with rhythm beat one big map; split event-dense areas for both performance and readability (see §5).

### 4.2 Events: one tile is one state machine

- Events hang on tiles and consist of several event pages; each page = a set of appearance conditions (switches, variables, self switches, items) + a trigger mode + a list of commands;
- The engine evaluates conditions back to front, and pages with higher numbers win: put "more special states" on later pages — chests and locked doors are state machines by nature;
- Choosing trigger modes:

| Trigger | Typical use | Notes |
| --- | --- | --- |
| Action button | Dialogue, chests, signs | The default; lowest cost |
| Player touch, event touch | Traps, teleports, follow scenes | Frequent firing — exit early on conditions |
| Autorun | Cutscenes, mandatory sequences | Locks the player in place; switch it off the moment the scene ends |
| Parallel process | Persistent listeners, ambient staging | Runs every frame — strictly cap the count (see §5.1) |

- Self switches (each event's own A, B, C) handle one-time states: chests and one-off NPC scenes use them, saving global switch IDs.

### 4.3 Switches and variables: global state needs registers

- Switches are global booleans, variables are global numbers: quest progress, story flags, zone unlocks and economy counters are all their combinations;
- Discipline one: one switch expresses one thing; name, purpose, who writes and who reads all go into the register — no naming on the spot;
- Discipline two: number variables in system blocks (one block for quests, one for economy, one for systems); append within a block, never squeeze in;
- Discipline three: variables can serve as counters, coordinates and temporaries, but temporaries shared across systems are breeding grounds for accidents — clear them when done;
- The register is the team interface: in multi-person work, update the table before touching anything; without it, half a year later you cannot read your own game.

### 4.4 Common events: reuse and throttling

- Common events are command sets callable from anywhere: recurring staging, checks and system logic live here — change one place, apply globally;
- They can also be triggered by switches as "autorun" or "parallel", for global listeners; parallel processing must be throttled, or it is a full check every frame (see §5.1);
- Reuse discipline: extract a command set into a common event on its third appearance; logic used exactly once should not be extracted "for beauty" — jump chains get out of control all the same.

### 4.5 The database and numbering: append-only after release

- The database (actors, classes, skills, items, enemies, troops, states, animations, etc.) is number-keyed, and events, drops and plugin parameters all reference each other by number;
- After release, numbers are part of save compatibility: new content always appends to the end — never reorder, delete or reuse a number;
- Numbers are free to change; structural changes (renumbering, re-referencing) go through save-compatibility verification;
- Plan on paper before entering data (what exists, for whom, what values, dropped from where), then type it in; designing numbers while typing guarantees rework.

### 4.6 Plugins and scripts: order is logic

- The order in the plugin manager is the order of execution and override; multiple plugins for one system will fight — keep exactly one set per system;
- Adoption discipline: add one at a time, then immediately run a regression over affected scenes (combat, menus, saves each once), then proceed;
- Configuration first: whatever a plugin parameter can solve, do not fix by editing plugin source; source edits get wiped on plugin upgrades and lose community support;
- Leave traces of changes: plugin name, version, order and changed parameters go into the project maintenance list — version-control commit messages count too;
- For script-level development, separate "can write it" from "can maintain it long-term" before committing effort.

## 5. Performance and Optimization

RPG Maker framerate problems mostly come from "too much running persistently" and excessive assets — not from the renderer first; optimize by cutting persistence first, then talk about the rest.

### 5.1 Events are the performance main variable

- Parallel events (including parallel common events) run every frame: be alert past single digits in count; anything a switch or touch trigger can handle must not poll;
- Large recurring checks (a whole-map chest audit, say) become event-driven; do not scan every frame;
- The more page conditions and the more frequent page switching, the higher the cost; do not carry purely decorative changes on whole-page conditions;
- Cap the total resident events per map, and erase or switch off events that are done.

### 5.2 Maps and assets

- Budget each map's size and event count; split when over: one town per map and one room per interior are common grains;
- Assets you do not use do not enter the project; clean again before release — bundle size and load time benefit directly;
- Make tiles and character assets at the engine's specified sizes; do not shrink oversized images for use — memory and rendering both suffer;
- Follow the engine's default audio division of labor: long music streamed, sound effects resident; do not stuff large files in by the batch.

### 5.3 Target-device verification

- Performance conclusions stand on target devices: low-end Android phones and older laptop browsers are common floors — smooth on the dev machine proves nothing;
- Web and mobile carry extra constraints: browser audio needs one prior user interaction; mobile memory budgets are tight and touch controls need dedicated design;
- Before release, run the chain "boot, load save, battle, save, quit" end to end on every class of target device.

## 6. Learning Path

A straight line accepted by "something playable":

1. Built-in help and official tutorials: walk the three blocks — maps, events, database — once each; open the sample project to study structure, and do not repurpose its assets (see §2.4).
2. First short work: one town, one dungeon, one boss — the whole flow from new project to export, walked completely once.
3. Events and switches, advanced: chests, locked doors, quest chains and NPC state changes, all built from "event pages plus switches and variables"; when reading community tutorials, focus on numbering discipline.
4. Database planning: turn enemies, skills, states, troops and drops into a table before entering data — practice "design first, type second".
5. Plugins: start from the official plugin docs and each plugin's own readme, adopting the minimum by need; when deep customization is confirmed, learn JavaScript and the script structure systematically.
6. Release: schedule deployment, target-device testing, asset replacement and store preparation as part of the project — not as closing chores.

## 7. Common Pitfalls

1. **Default-asset dependence**: shipping with bundled assets throughout makes the game read as a "sample project" at a glance, and replacement later means redoing staging and tiles. Set the asset plan at kickoff and budget the pre-release replacement.
2. **Plugin conflicts**: multiple plugins for one system and carelessly ordered, combat and menus glitch randomly. One system, one plugin set; add one at a time and regression-test immediately.
3. **Unplanned data structures**: switches and variables coined on the fly, database numbers changed at will — by the midpoint the logic fights itself. Build the registers first (§4.3, §4.5).
4. **Infrequent project backups**: without versioning or backups, one crash or mis-delete takes everything. Version control plus periodic full backups, with snapshots before high-risk operations.
5. **Renumbering the database after release**: old saves mismatch and player progress scrambles. Append-only after release; no reordering, no reused numbers.
6. **Parallel-event abuse**: treating "parallel process" as a background thread wears the framerate away. If it can be event-driven, do not poll (§5.1).
7. **Event logic as spaghetti**: one event with hundreds of commands, copied across maps — fix one place, miss nine. Extract a common event on the third repetition (§4.4).
8. **Forcing non-RPG gameplay into events**: action combat, tactics and complex systems heaped out of events — the shape is there, the soul is not. Decide first whether to switch plugins or tools (§1).
9. **Verifying only on the dev machine**: smooth on desktop is not smooth in browsers and on phones. Run the full chain on target devices.
10. **Surgery on core scripts**: editing core scripts directly or overhauling plugin source invalidates everything on upgrade. Prefer the plugin mechanism and keep an upgrade path.

## Further Reading

- [Engine Tracks index](../README.md): the overview and plan for all 12 tracks — this page is the "RPG Maker" one.
- [Game Design Handbook](../../fundamentals/game-design/README.md): design methodology for core loops, combat and progression — echo of §4 here.
- [Art & Audio Handbook](../../fundamentals/art-audio/README.md): specs and volumes for tiles, character art and audio — consult when planning asset replacement.
- [Multi-platform Launch Playbook](../../../playbooks/platform-launch/README.md): qualifications and flows for desktop and Web releases — §3.2 expanded.
- [Indie Survival](../../../playbooks/indie-survival/README.md): scope control and scheduling, complementing the small-scope positioning.
- [Pitfalls & Anti-patterns](../../pitfalls/README.md): high-frequency pitfalls across the whole pipeline — read against section 7 here.
- [Legal, Patents & Competition](../../publishing/legal/README.md): the systematic treatment of assets and licensing — the deep version of §2.4.
- [The JRPG page in the Genre Handbooks](../../genres/jrpg/README.md): this page's best partner — design points for combat, progression and content scope.
