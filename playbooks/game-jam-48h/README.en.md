# Ludo Atlas · Playbooks · 48-hour Game Jam

> **Playbook**. Positioning: a complete release rehearsal — trade the smallest deliverable scope for one small piece of work that is finished, playable, presentable and submittable.
> Companions: Game Design Handbook (one-line concept and core loop) · Production Handbook (scope and scheduling) · Pitfalls & Anti-patterns (the project management chapter) · Indie Survival (the path ladder).

---

## 1. Use Cases and Goals

The 48-hour game jam is a type of time-boxed development event: the organizers announce a theme, and participants build a runnable small piece within 48 hours and submit it before the deadline. Online jams and physical venues differ in form, but the core rules are the same; the differences concentrate in the deadline time zone, asset restrictions, AI usage terms and judging method.

**When it fits**:

- You want to walk the full "conceive, build, package, publish" pipeline once at minimum cost.
- You have built a prototype before and want to test your speed ceiling: what can 48 hours actually produce.
- You want a playable, showable small piece for a portfolio, or you want to meet future collaborators.
- You want to practice scope control: a jam is one of the few settings that drills "cut" into muscle memory.

**When it doesn't**:

- You want to learn a new engine or language along the way: the learning curve eats more than half the time (§5, item 2).
- You want long-term polish to commercial standards: jam output works as a prototype or portfolio piece, not as the start of long-term iteration.
- You can't assemble a continuous 48 hours: a fragmented "slow jam" is viable, but the cadence has to be designed separately.

**Goals (in priority order)**:

1. Submit on time: finish uploading before the deadline and get the submission receipt.
2. Finish: a complete small experience from title screen to ending screen, even with only 10 minutes of content.
3. Calibrate your speed: record the actual time each stage takes and correct your budget for the next jam.
4. Be legible: a stranger with the link can start playing without any explanation.

> **Time budget**: subtract sleep, meals and packaging from the 48 hours and roughly 30–36 hours of production time remain. Plan everything backwards from those 30 hours, not from 48.

## 2. Process at a Glance

The 48 hours run through four stages, with pre-jam preparation standing outside the timeline. Four gates sit between the stages: fail a gate and you may not enter the next stage — the first barrier against scope explosion.

| Stage | Output | Duration |
| --- | --- | --- |
| Pre-jam prep (one week before the jam) | Template project, asset library, publishing and submission accounts, rules checklist | 3–6 hours, spread out |
| Concept & scope cutting (hours 0–4) | One-line concept, scope contract, paper sketch, task board | 4 hours |
| Core playable (hours 4–24) | Greybox build: core loop closed, playable to failure and restart | 20 hours (including meals and 6 hours of sleep) |
| Content & polish (hours 24–40) | Content fill, audio, UI and feedback, playtest build | 16 hours |
| Submission & project page (hours 40–48) | Build package, platform page, submission receipt | 8 hours (first 4 to wrap up, last 4 as buffer) |

Pass criteria for the four gates:

1. **Hour 4**: you can state "what the player does and why it's fun" in one sentence, and the scope contract is frozen.
2. **Hour 24**: with no explanation and no hints, a tester can reach a full win or loss and wants to restart; the core loop is closed.
3. **Hour 40**: content freeze (feature freeze); every new wish goes onto the "next jam" list, and gameplay is no longer touched.
4. **Hour 44**: the build and the page have been uploaded at least once; the remaining time is for fixes and replacements only.

> **Set the internal deadline at hour 44**, not hour 48: uploading, transcoding, platform processing and network jitter all eat time — the remaining 4 hours are insurance, not development time.

## 3. Step by Step

### 3.1 Before the Jam: Toolchain and Template Project

- Use what's familiar, not what's new: engine, language and build tools all come from the set you have used continuously for the last three months — a jam is no place for learning.
- The template project should include at least: input mapping, character control and camera, scene transitions, pause and volume, a one-click packaging script; rehearse the shortest path from new project to build once.
- Before the jam, run the full "empty project to installer" flow once on the target platform; write the export settings and every pitfall you hit into the checklist.
- Version control: solo or small team, start from a local git repository and commit hourly; don't fiddle with branching models during a jam.
- Keep the task board to four columns: To do, Doing, Done, Next jam; at any moment, "Doing" holds exactly one item.

### 3.2 Before the Jam: Asset Library and Publishing Accounts

- Pre-stock the asset library with two sets of clearly licensed free assets (2D characters and environments, UI icons), one font set, 20–30 general sound effects and two loopable music tracks.
- Use assets as placeholders first and replace later; replace only assets confirmed to stay — never make art for content that will be cut.
- Register publishing and submission accounts ahead of time, verify email, complete author profiles; set up page drafts early wherever possible.
- Read the rules line by line and write them into a checklist: deadline time zone, submission materials, team-size cap, asset and AI clauses, whether pre-existing assets are allowed.
- Record asset sources and licenses on the day you acquire them; at submission you must be able to give provenance.

### 3.3 Reading the Theme: From Word to Verb

In the first hour after the theme is announced, diverge only — write no code.

1. **Split the words**: break the theme into three columns — nouns, verbs, adjectives — and associate 10 words per column, no judging.
2. **Verbalize**: ask "what is the action the player performs?". If the theme is a noun, find the verb it implies; if it's an adjective, find the action that matches it.
3. **Invert and change perspective**: turn the theme around, shrink it, enlarge it, swap the protagonist — one idea each; inversions often stand out more than the literal reading.
4. **Five-question filter**: can the gameplay be stated in one sentence; can a playable version be built in 48 hours; is there a moment that can be captured as a GIF; does the mechanic depend on heavy content; is it a repeat of the common interpretation.

Diverge for 60 minutes, converge for 30. After converging, keep exactly one concept and send the rest to the "next jam" list; pick the one that differentiates most easily, not the grandest.

### 3.4 Scope Discipline: Do One Thing

One-line concept template: **You are (a character), in (a setting), using (one mechanic), to achieve (one goal).** One word per blank; if you can't fill a blank in — or want to put in two — scope is already over budget.

Freeze the scope contract within the first 4 hours and pin it to the top of the task board:

| Do | Don't |
| --- | --- |
| One core mechanic, repeated throughout | A second system, skill trees, multiple characters |
| One scene, one theme | Multiple levels, multiple areas, branching story |
| One beginning and one ending | Save system, settings menu, achievements |
| Basic sound effects plus looping music | Custom art, original music, voice acting |
| Clean UI and feedback | Networking, leaderboards, multiplayer |

Cutting order: cut content volume first, then presentation — never the core loop. Every new idea goes straight onto the "next jam" list; no debate, no trial builds.

### 3.5 Team Split: Solo vs Small Team

| Dimension | Solo | 2–4 person team |
| --- | --- | --- |
| Typical setup | One person covering everything | Programmer, artist (doubling as design), audio (doubling as testing) |
| Strengths | Zero communication cost, fast decisions | Parallel output, complementary skills |
| Risks | Energy bottleneck, all-nighters out of control | Unclear interfaces, waiting on each other |
| Key discipline | Fixed sleep, cut scope by another third | Interfaces first, regular syncs |

Solo: set a fixed sleep window — for example, a full 6 hours of sleep between hours 20 and 26; write gameplay code when sharp, do low-brain work like asset swaps when flat; route around any problem you can't crack within 30 minutes.

Team of 2–4: settle three things within the first 2 hours — asset specs (sizes, naming, import paths), module boundaries (who writes what, how they connect), and sync cadence (a 10-minute stand-up every 4–6 hours, asking only what's done, where you're stuck, what to cut). Appoint one scope referee; when they say cut, it's cut — disagreements wait for the post-jam postmortem.

Five or more: split into three groups — gameplay, content, submission — each with one point of contact; the more people, the more expensive communication gets, so scope must shrink, not grow.

### 3.6 Timeline in Detail

**Hours 0–4: concept and scope cutting.** Finish the theme reading; settle the one-line concept and the scope contract; draw the loop diagram and UI sketch, and walk the core loop on paper; stand up the environment (template project, version control, task board). No production code in this block.

**Hours 4–24: core playable.** First 8 hours: reach minimum playable (the player can move, the core action can happen); hours 8–16: close the core loop (win and lose states, restart works); hours 16–24: internal playtest, fixes and sleep. Build "playable" before "pretty"; touch no decoration during the greybox phase.

**Hours 24–40: content and polish.** Content only as variations on existing mechanics (swap parameters, layouts, pacing); add no new mechanics; lay sound effects first, music after; fill in the title screen, win and lose screens, and the controls; have one person outside development playtest, and fix the first point where they get stuck.

**Hours 40–48: submission and page.** At hour 40, freeze content and package immediately, then verify in a clean environment; finish and upload the page assets in the same window (title, one-line pitch, screenshots, GIF, controls, asset credits); complete the first submission before hour 44, leaving margin for fixes and replacements.

### 3.7 Submission Checklist

| Category | Contents | Checkpoint |
| --- | --- | --- |
| Build package | Target-platform installer or web build | Runs in a clean environment; filename carries the version number |
| How to run | Controls, resolution, window mode | Needs no verbal explanation of any kind |
| Page assets | Title, one-line pitch, 3–5 screenshots, 1 GIF | The first screenshot shows the gameplay |
| Cover image | Made to platform-specified dimensions | Not blurry, not badly cropped, recognizable at a glance |
| Declarations | Asset credits and licenses, AI usage, team list | Checked item by item against the jam rules |
| Receipt | Screenshot and link of the completed submission | One copy stored locally, one in the cloud |

## 4. Acceptance Checklist

Walk every item before submitting; only a full pass counts as done.

**Gameplay & experience**:

- No more than three clicks from launch to playable; no black screens or deadlocks.
- A stranger can pick it up without explanation and makes their first correct action within 30 seconds.
- A complete win or loss within 10 minutes, and they want to restart.
- Start, end and restart paths are clear; both win and lose screens exist.
- The game still reads with the sound off; feedback doesn't rely on audio alone.

**Technical & distribution**:

- The full flow runs on a machine without the engine installed, or in a browser incognito window.
- 10 minutes of continuous play with no crash; repeated restarts don't corrupt state.
- Target resolutions and window modes behave; the web build loads within an acceptable time.
- Build filename, version number and how-to-run doc agree.
- Volume is adjustable, or at least there is no blown-out audio.

**Submission & compliance**:

- Page copy and screenshots reflect the actual gameplay; no placeholder text.
- Asset credits, licenses and AI declarations are complete.
- The submission receipt is archived; the link works while logged out.
- Official rules checked line by line: deadline, materials, team size, asset restrictions.

## 5. Common Pitfalls

1. **Scope explosion**: scope is frozen at hour 4; by hour 8 you want a second mechanic. Fix: a scope contract plus a scope referee; every new idea goes onto the "next jam" list.
2. **Learning a new tool at the jam**: treating the competition as a tutorial; the learning curve eats half the time and all that's left is a sample project. Fix: keep the main tools familiar; new tools are for a pre-jam practice project or the next jam.
3. **First build only near the deadline**: export, page and upload all crammed in before the cutoff; any step fails and there's no time left. Fix: rehearse the full pipeline before the jam; build at hour 40, submit before hour 44.
4. **Polish eats the content**: all the time goes into art while the gameplay is still greybox. Fix: make the loop fun first, replace assets in one pass after, and cap polish time.
5. **Trading all-nighters for progress**: the last 24 hours fall off a cliff, bug density doubles. Fix: a fixed sleep window; cut features before cutting sleep.
6. **No sound**: shipping muted by default leaves half the experience missing. Fix: pre-stock a sound-effect pack; laying in SFX is low-cost, high-return.
7. **Playtesting only with teammates**: a group blind spot — nobody notices that newcomers can't read the game. Fix: playtest with at least one person outside development.
8. **Theme as a skin**: the gameplay has nothing to do with the theme; judges see through it at a glance. Fix: apply the verbalize test (§3.3) and grow the theme into the mechanics.
9. **Not reading the rules**: time zone, asset restrictions, AI clauses, team-size cap — tripping any one can get you disqualified. Fix: read them line by line before the jam and write them into the checklist.
10. **No verification after submitting**: thinking it's over once the button is clicked. Fix: open the link logged out, download your own submitted build and run it once more, and confirm the receipt.

## Further Reading

- Game Design Handbook: the full method for core loops and one-line concepts — the source material for §3.3 and §3.4 here.
- Production Handbook: the phase model, scope control and postmortem process — follow it when scaling the 48 hours up to a full project.
- Pitfalls & Anti-patterns: the project management and release chapters — the expanded version of §5 here.
- Indie Survival: the walkthrough of rung 1 on the path ladder, and the decision rules for moving from a jam to the next size up.
