# Ludo Atlas · Genre Handbooks · Interactive Fiction

> **Genre Handbooks · Volume 2**. Positioning: a development handbook for a genre whose primary medium is text, turning "read, think, decide, see the consequences" into the whole experience; it covers the two main schools, parser-based and choice-based, from state tracking and text budgets all the way to endings and replay.
> Companions: Game Design Handbook (narrative and branching costs) · Case Studies (breaking down works) · Pitfalls & Anti-patterns (design and content production) · Indie Survival (scope and scheduling).

---

## 1. Positioning and Core Loop

In one line: interactive fiction (also called text adventure, or IF) **treats text as its engine**. Scenes are built out of sentences, actions are expressed as commands or choices, and every change in the world is written back into the text; interface, images and sound are supporting players, not the skeleton.

Get the two schools straight first:

| Dimension | Parser-based | Choice-based |
| --- | --- | --- |
| Player input | Free-text commands (look, take lamp) | Picking one of several options |
| World model | Built into the tool: rooms, objects, verbs, rules | Maintained by the author: passages, flags, variables |
| Learning curve | High — you must learn command syntax and vocabulary | Low — if you can read, you can play |
| Writing focus | Scene description and rule responses | Passage structure and variation text |
| Representative tools | Inform 7, TADS | Twine, Ink, ChoiceScript |
| Representative works | Zork, Colossal Cave Adventure | 80 Days, the Choice of Games series |

The core loop, written as a verb chain:

- Choice-based: `read a passage → make a choice → state changes → the text calls back to the decision just made → keep reading`
- Parser-based: `read the scene → type a command → parse and resolve → the change is written back into the description → type again`

Both loops stick for the same reason: text builds the world, and state makes the world remember the player. The difference lies in how decisions are expressed, and in who carries the cost of maintaining the world model — the tool handles it for parser-based games, while in choice-based games it rests entirely with the author.

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Visual novel | The visual novel presents through character art, staging and voice acting; in interactive fiction the text itself is the presentation layer, and interaction is only commands and choices |
| Point-and-click adventure | The point-and-click adventure advances through mouse input and item puzzles, with graphics as the star; in interactive fiction both description and interaction are carried by text |
| MUDs and text worlds | Multiplayer, always online, centered on social play and long-term accumulation; interactive fiction is a single-player work with a clear ending |
| Idle text games | Idle games put numeric progression at the core and use text as skin; in interactive fiction the text is the content, and numbers are only a notation for state |

A self-check question: if you replaced all the text with dry synonyms, would the game still hold up? If the answer is still "yes", what you want to build may be systems design, not interactive fiction.

## 2. Player Experience Goals and Benchmark Titles

The experience goals are the promises the text must keep:

| Experience goal | The player's inner voice | Where design pushes |
| --- | --- | --- |
| Immersion and agency | "I call the shots" | Choices have real costs; the world calls back to what the player has done |
| Curiosity and discovery | "What else can I do here?" | World rules open to experimentation, secret spaces, verb experiments |
| The weight of choice | "I need to think about this" | Trade-offs under incomplete information; visible costs |
| The pleasure of the prose itself | "That line was well written" | Description density and voice; the read-aloud test as the gate |
| A believable world | "It makes sense" | The same action gets a sensible response in every situation |
| Comfort and autonomy | "I can stop whenever I want" | Save anywhere, roll back, text size, skip already-read text |

Benchmark works (widely known titles only; play them yourself before breaking them down):

| Title | One-line background | What to borrow |
| --- | --- | --- |
| Colossal Cave Adventure | 1977, the starting point of interactive fiction | Prototype methods for modeling space with text: rooms, objects, puzzles |
| Zork | Infocom's parser-based gold standard | The completeness of its world model and its comic voice; even error messages are content |
| The Hitchhiker's Guide to the Galaxy | Infocom's licensed adaptation | Bringing the source material's tone into command responses — a model for adaptation writing |
| 80 Days | inkle's around-the-world narrative | Choice-based play plus resource pressure; highly reused branches, a model of writing efficiency |
| The Choice of Games series | Pipeline productions of the ChoiceScript platform | Industrialized variable tracking and multiple endings, with per-playthrough variations |
| Lifeline | Mobile choice-based | Real-time waiting and notifications turn "waiting" into a narrative device |
| AI Dungeon | Generative interactive fiction | The stability of generated text and the problem of the absent author — a public specimen of the lessons |

Play a parser-based work yourself for at least two hours; the tolerance and frustration of a command interface cannot be felt through videos.

## 3. Design Essentials

### 3.1 Choose the School First

Selection starts with four questions:

| Question | Leaning parser-based | Leaning choice-based |
| --- | --- | --- |
| Where players play | Keyboard, willing to sit still, willing to learn | Touchscreen, fragmented time, zero learning |
| Who maintains the world | Accepting tool-managed rules | Willing to register every piece of state by hand |
| Writing habits | Strong at description and rule responses | Strong at passage and branching structure |
| Release form | Classic interpreters and enthusiast communities | Web, mobile, mainstream platforms |

For a first project, choose choice-based: lower barrier, faster feedback, and a work you can actually finish. Parser-based is the higher-barrier traditionalist path — and also a unique entry point to verb experiments and simulated worlds.

Two hybrid routes worth knowing: command buttons (turning common verbs into clickable buttons, sidestepping text input and IME issues); and choices plus state (maintaining a world model behind the options, the route 80 Days takes). Building parser-based games for Chinese-language players needs extra input design: verb panels, clickable noun highlighting, synonym tolerance — all assembled by hand.

### 3.2 State and Variables: A World-Model Mindset

The writer needs a "world model" in their head: what states exist, which actions change them, and which texts change along with them. Many flags do not make a world feel alive; only write-backs the player can actually read count.

Register variables by category — enough to work, without bloat:

| Category | What it records | Examples | How it writes back |
| --- | --- | --- | --- |
| World state | Doors, mechanisms, item positions | The gate is unlocked | One line of description changes when you pass again |
| Character state | The player's condition and situation | Injured, wanted | Narration and NPC reactions change |
| Relationships and attitudes | Where NPCs stand toward the player | Trust level, debt | Different forms of address and dialogue variations |
| Knowledge | Who knows what | The player knows the killer | Unlocks new options, steers away from wrong words |
| Meta-progress | Records across playthroughs | Endings seen | Chapter select, narration hints |

Five disciplines:

- Register before writing: the variable table spells out name, type, initial value, read/write points and affected passages; no variable may be referenced until it is registered.
- Few and deep beats a pile of flags: ten dimensions that can combine with each other make a more living world than a hundred boolean flags.
- Variations first: if changing one line solves it, do not open a new branch; reserve big branches for key decisions.
- Perceptible write-backs: when state changes, the player must be able to read it (descriptions, forms of address, options appearing and disappearing). A change no one can read was never made.
- Reconcile at project close: use a script to check three things — references to undefined variables, variables defined but never triggered, and variables triggered but never read.

### 3.3 Text Budget and Writing Workflow

Do the math before you write. Estimate by "the total cost per thousand characters, including variations, testing and revision" — do not count only the first draft; text in this genre is inherently costlier than plain prose, because behind every line there are state and branching accounts.

Run the writing workflow in order:

1. One-page skeleton: what the story is, what the player does, how many endings there are.
2. Structure diagram: choice-based starts with a passage map (nodes, divergences, convergence points); parser-based starts with a room map and a verb list. No structure may appear in the prose that is not on the diagram.
3. First draft: write one complete route in one go; first make the story stand up.
4. State and variation backfill: fill in the write-back points against the variable table — the step most often missed, and the most damaging to the experience.
5. Revision: cut 10%–20% before finalizing, cutting hardest at the opening; a slow opening is this genre's number-one source of bad reviews.
6. Read-aloud test: read it out loud once and fix any sentence that trips the tongue; have someone else read it and watch where they pause and where they re-read.
7. Integration and full playthrough testing: run the text in the tool, going item by item against the prompts and assets.

Toolchain habits: separate prose from logic, keeping the prose in standalone files or spreadsheets; turn word counts into visible progress numbers — long projects survive on them.

### 3.4 Endings and Replay

Endings come first: define the set of endings and their conditions (an ending matrix sheet) before writing the paths that lead to them. Endings are the work's attitude; their number is not.

| Design item | Approach |
| --- | --- |
| First playthrough | Must be self-contained: most players finish the game only once, so put the best content on the mandatory path |
| Ending matrix | One ending per row: name, conditions, emotional tone, first-playthrough reachability |
| Replay hooks | New-perspective passages, narration variations, state payoffs, an ending list and achievements |
| Smooth replay | Skip already-read text, chapter select, playthrough carry-over — never force players to re-walk three miles |
| A closing scene | Offer one look back: let players see the sum of their choices |

## 4. Technical Essentials

### 4.1 Tooling Routes (Conceptual Level)

The choice-based family:

- Twine: passages joined by links form a story graph, exported to HTML for release; the first choice for prototypes and small scope, with adequate variables and macros, though it starts to chafe once the structure gets complex.
- Ink: a narrative scripting language with a clean separation of text and logic, embeddable in Unity / Godot; inkle's own narrative works come from this lineage.
- ChoiceScript: built around the Choice of Games platform, with variable tracking, multiple playthroughs and statistics built in; consider it when your release target is tied to that platform ecosystem.
- Ren'Py: when you need character art, staging and voice acting, choice-based text can be built directly into a visual novel structure.

The parser-based family:

- Inform 7: describes rooms, objects and verbs in near-natural-language rules, with the world model built in and the output run by a unified interpreter; the default answer for parser-based work.
- TADS: a veteran parser-based system whose scripting is closer to a traditional programming language; the other mature route alongside Inform.
- One takeaway to carry forward: the core of a parser-based tool is "a world model plus a rule system" — parsing is only the outermost step; understand that, and your choice-based state design will be much cleaner too.

A general-purpose engine plus a narrative plugin (Unity / Godot with Ink) suits teams that already have an engine stack; building your own is only worth considering when the interaction model outgrows off-the-shelf tools — never for a first project. Tools here are introduced conceptually only; for concrete routes, defer to each tool's official documentation.

### 4.2 Engineering Implementation Essentials

- Externalized text: keep the prose in standalone files or spreadsheets and have code only read it; changing one line of dialogue should never touch logic.
- State serialization: saves store every variable and position, and the variable table carries a version number and migration functions; players sink the most time into a text world, so a corrupted save is the number-one crime in bad reviews.
- Autosave points: autosave at every divergence point and chapter opening; slots must allow stepping back a few moves.
- Debug tools: a jump command (straight to any passage or room), a variable viewer, state injection (set variables and run straight to an ending), and passage coverage checks (which branches were never reached).
- Input and vocabulary (parser-based): synonym tables, adjective handling, pronoun resolution and disambiguation are double work — design plus implementation — and need their own budget line.
- Localization: the text volume is large, so the glossary comes first; for Chinese full-width punctuation, mixed Chinese-English typesetting and line breaking, do a manual pass after integration.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimating scope; not a commitment:

| Project form | Text volume | Playtime | Time reference | Notes |
| --- | --- | --- | --- | --- |
| Prototype | 5,000–20,000 characters | 15–40 minutes | 2–4 weeks | One route plus two endings; validates the text and state loop |
| Jam entry | 5,000–15,000 characters | 15–30 minutes | One weekend to 2 weeks | Single scene, few variables; schedule in hours |
| Short work | 30,000–80,000 characters | 1–3 hours | 2–6 months | The lower edge of sellable scope; one person can finish it |
| Mid-size work | 100,000–250,000 characters | 4–10 hours | 6–18 months | Multiple routes and endings; writing and testing split the time evenly |
| Large work | 300,000+ characters | 15+ hours | 2+ years | A team or years of solo investment; usually with platform and tooling support |

Conversion rates:

- Playtime is estimated at 200–300 characters per minute, including thinking and clicking; excluding replay and being stuck.
- Writing speed: a practiced writer produces 1,500–3,000 characters of publishable-quality incremental text per day; state and branching design count separately.
- Revision and testing multiplier: 0.5–1× the first draft; one full playthrough test pass takes half a day to two days.

Two magnitude conclusions about cost structure:

- Choice-based incremental cost is roughly linear; opening a new branch also pays for its convergence points. Using variations instead of new branches is the main cost-control lever.
- Parser-based room costs follow the verbs: how many verbs a room supports and how many layers of response each verb gets — set the ceiling early (say, only nurture 20 common verbs) and lock it down; do not loosen it midway.

## 6. How to Start the First Prototype

Build the first prototype in two weeks and deliver a minimal work that "reads through completely, has working state, and can save and load" — not one illustration required.

1. Days 1–2: pick the school and install the tool. Twine for choice-based, Inform 7 for parser-based; get the "change text → see the result" loop running first and touch nothing else.
2. Days 3–5: write a complete short story of 3,000–5,000 characters: one scene, one NPC, two or three state variables, two endings. Finish it in a text editor first, then move it into the tool.
3. Days 6–7: complete the state. Put the variable table on paper (names, initial values, read/write points) and give every variable at least one perceptible write-back.
4. Days 8–9: add comfort features: save and load anywhere, roll back, restart, text size; for parser-based, add a verb list and error messages.
5. Days 10–11: tune pacing and hints: split long passages; build a rough three-tier hint system (three sentences will do).
6. Days 12–14: test with 3–5 people. Watch only three things: where they stall, which choice gets discussed, and whether anyone restarts voluntarily after finishing.

Acceptance criteria (all observable):

- Testers finish one route in 15–20 minutes with no hints and can say what one of their decisions changed.
- At least one person restarts voluntarily to try another route.
- After the test, at least two people can retell the story and their choices, not just recall clicking.
- You can locate and fix a tester's stuck point within 5 minutes.

Counter-example: stacking the variable table to a hundred lines, building a toolbox first, writing a ten-chapter outline first. Not one word of prose on the page means all of it is zero.

## 7. Common Pitfalls

1. **Fake choices**: options produce no perceptible variation, and once players see through it they never take it seriously again. Avoidance: every option changes at least one piece of state or text; if it can't, cut the option.
2. **Branch explosion**: tree-shaped branching with no convergence points doubles the writing and testing load. Avoidance: mark convergence points and a depth cap first (key branches three layers at most), then write.
3. **Variable yarn ball**: flags pile up and no one knows which are still alive. Avoidance: add the three end-of-project checks to the variable table (references, triggers, read points).
4. **Dead ends with no hints**: guessing verbs in parser-based games, clicking blindly in choice-based ones — stuck means quit. Avoidance: synonym tables, verb lists, three-tier hints; write error messages as informative sentences.
5. **Under-informed options**: players don't know what they are choosing, and choice becomes a dice roll. Avoidance: keep option text short and concrete, stating the stance and the stakes.
6. **Estimating text volume from the first draft**: variation backfill, revision and testing left uncounted. Avoidance: budget at 1.5–2× the first draft.
7. **Slow opening**: still laying out the setting twenty minutes in. Avoidance: give one choice, one consequence and one hook in the first chapter.
8. **Missing comfort features**: no save, no skip, eye-searing text size — reviews will say so outright. Avoidance: put saving, rollback, text size and skip-already-read on the release floor checklist.
9. **Forced replay**: rewalking a whole chapter just to try one option. Avoidance: skip already-read text, chapter select, playthrough shortcuts.
10. **Generated text as filler**: stuffing branches with generative text; style drift and broken logic destroy the sense that "the author is present". Avoidance: use generation only for drafts and variations; finalize core text by hand.
11. **Tools first**: writing an engine, building tools, months with no prose. Avoidance: text first, tools only serve the text, and use off-the-shelf tools for a first project.

## Further Reading

- Game Design Handbook §8, narrative design: branching cost management, dialogue and option design — the base document for §3 of this page.
- Case Studies: methods for breaking down narrative works; before dissecting, build a text ledger for the work you plan to break down.
- Indie Survival: scope control and scheduling, to be used together with the accounts in §5; scope creep in text projects is the most insidious kind.
- Pitfalls & Anti-patterns §2 and §3: common pitfalls in design and content production; cross-read with §7 of this page.
- Genre Handbooks · Visual Novel and Genre Handbooks · Point & Click Adventure: the division of labor between text and staging, and the item-puzzle route; boundaries in §1.
- Exercise: play a classic parser-based work for two hours and log every command that gets you stuck; then break one 80 Days route into a three-column table of "choice → state change → text call-back".

Interactive fiction's code can be very small, but its text accounts must be very large. Write one route all the way to the end and watch the state to death before you talk about scope and release.
