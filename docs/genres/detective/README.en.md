# Ludo Atlas · Genre Handbooks · Detective

> **Genre Handbooks · Volume 3**. Positioning: the genre that turns "who did it, how, and why" into the puzzle itself. Players collect clues, organize their deductions and accuse face to face inside cases written by the author; whether a deduction is right is decided by evidence, not by staging.
> Companions: Game Design Handbook (information structure and deduction loops) · Case Studies (finished works and failures) · Pitfalls & Anti-patterns (logic holes and dead-end traps) · Indie Survival (scope and scheduling for script volume).
> This page carries no external links; benchmark titles are well-known works only, and the numbers are common magnitudes — calibrate against your own project's measurements.

---

## 1. Positioning and Core Loop

One-sentence positioning: the detective genre is **the genre that breaks "solving a case" down into submittable deduction actions**. The player does not watch a detective solve a case; they play the detective themselves: read information, find contradictions, draw conclusions, then hand those conclusions to the game and accept the verdict on right or wrong. It does not test reflexes and rarely tests numbers — it tests whether you saw it all and connected it right. The core loop, written as a verb ring:

`take the case → investigate and question (gather clues) → organize the clues, find contradictions → form a hypothesis → submit your deduction (present evidence or accuse) → get verification → the truth lands or twists → the next case`

This loop is measured in minutes, and it rests on three premises: clues must be obtainable (the information you need is all in the game), conclusions must be derivable (every charge has a chain of evidence), and deductions must be submittable (the player hands the answer to the system in person). If any one of the three fails, the experience slides from "solving the case" toward "watching a show" or "guessing riddles." The loop at three scales:

| Scale | Loop | What the player gets |
| --- | --- | --- |
| One inference (1–10 minutes) | Spot a contradiction → pick out the evidence → submit → get confirmation or rejection | One verified deduction |
| One case (2–4 hours) | Take the case → investigate and question → integrate the clues → accuse → the truth is revealed | A complete truth, usually with one twist |
| One work or series (10+ hours) | A main-plot mystery planted between the standalone cases, advancing case by case | Character arcs and a final answer that runs through the whole work |

Drawing boundaries with neighboring genres:

| Neighboring genre | Boundary |
| --- | --- |
| Logic puzzle | The puzzle is abstract rules and the answer hides in the system; the detective's puzzle is people and causality, and the answer hides in the script |
| Escape room | An escape room uses information to open locks and the destination is the exit; a detective uses information to convict and the destination is a conclusion |
| Social deduction | Social deduction pits you against living players, with no guaranteed answer; in the detective genre the truth is already written, and the player is bringing it back |
| Visual novel | Visual novels are mainly about reading and choosing; the detective genre requires players to submit conclusions, and a wrong submission must have a cost |

A self-check question: if you removed the "submit your deduction" step, would the game still stand? If the answer is yes, you have made a visual novel or a narrative adventure; the foundation of the detective genre is that the player can answer wrong — and answer right with their own hands.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **The command of solving the case yourself**: every conclusion traces back to specific clues; solving the case is "something I did," not "something the staging told me."
2. **The moment of insight**: the "aha" when two pieces of known information connect in your head — the thrill currency of this genre.
3. **Being treated fairly**: the answer is fully derivable; a miss is your own failure to look closely, not the game hiding things.
4. **The truth paying off, and failure that is safe**: motive and twist converge at the moment of accusation; a failed accusation needs a step down, not humiliation.

Negative feelings (any one of these is a red flag): played for a fool (key information comes from somewhere the player could never have seen); done for (a character states the conclusion for the player in a scene); dead-ended (single-path clues — miss it and it is gone); worn down (brute-force elimination, repeated map traversal).

Benchmark titles (a well-known roster; play them yourself before breaking them down):

| Title | What to learn |
| --- | --- |
| Ace Attorney | The template for courtroom confrontation and evidence-presentation judgment: presenting the wrong thing has a cost, recantations have a rhythm, and contradictions in testimony are the puzzle |
| Danganronpa | Deduction blended with action minigames: cashing out story climaxes in playable segments |
| Return of the Obra Dinn | Deduction as "register and verify": answers confirmed in groups with crisp feedback, so players dare to commit to conclusions |
| Her Story | Database-search deduction: the information is fully open, and the puzzle is in "what to ask," not in "whether a clue exists" |
| Unheard | Reconstructing a case through audio playback: recordings from different viewpoints serve as each other's clues — a sample from a Chinese studio |

## 3. Design Essentials

### 3.1 Case Structure: the three acts — clues, deduction, accusation

Every case is a small play, and each of the three acts has its deliverable:

| Act | What the player is doing | Design task | Deliverable |
| --- | --- | --- | --- |
| Clues | Investigating, searching, questioning, collecting evidence | Control the order and density of information releases | A case file (clue and evidence tables) |
| Deduction | Finding contradictions, connecting clues, forming hypotheses | Provide organizing tools and a verification entry point | A set of submittable conclusions |
| Accusation | Submitting conclusions, confronting, bearing the outcome | Pay off the truth, land the emotion | A chain of evidence that holds up |

Four disciplines:

- One case tests one core puzzle: who did it, how, why — pick one as the headline and let the other two support it. Test all three at once and the player remembers none of them.
- Plant material for the twist in advance: midway, let the "smoothest explanation" be overturned once; the information used to overturn it must have appeared in the clues act, or it is deception (§3.2).
- Set the stakes of accusation early: whether a wrong accusation deducts trust, deducts turns, or is rejected for a retry — decide in the first case and hold it throughout; changing the rules mid-game forces players to relearn them.
- Arrange a difficulty curve across cases: clue count, location count and suspect count escalate case by case; make the first case a teaching case — small and direct, teaching the basic interactions of questioning and presenting evidence.

### 3.2 The Clue System: redundancy and fairness

Clues come in three classes, and their ratio is your first design decision:

| Class | Role | Allocation principle |
| --- | --- | --- |
| Key clues | Build the chain of evidence; none may be missing | Every conclusion backed by at least two independent clues |
| Redundant clues | A second path to the same conclusion; dead-end insurance | Cover every key conclusion |
| Distractor clues | Manufacture reasonable doubt; serve the deduction process | 2 to 5 per case, and every one must be refutable |

- Redundancy is the foundation against dead ends: every key conclusion must be reachable through two or more independent clues (different locations, different lines of questioning with different witnesses). Self-check: remove one clue at random — can the case still be solved? If not, add a path.
- False clues must be falsifiable: every distractor clue needs a clue that refutes it, and the refutation must be obtainable. Misdirection should come from characters' lies or the player's own assumptions, never from the narrator withholding from the player; information used by the twist must have been open to the player — this is the one red line of the genre.
- Tiered but quiet hints: stuck-point hints come in four levels — "point at the area → point at the object → point at the relationship → give the answer" — requested by the player, with a quiet entry point (the same discipline as the Puzzle page in the Genre Handbooks).

Two more cheap wins: the case file (clues auto-archived, annotatable, reviewable) is a baseline feature; "missed" is more dangerous than "stuck," so make key clues unmissable or revisitable, and never force players to reload a save. Checklist:

- Does the full path from opening to accusation hold up, and can every charge be traced back to a specific clue?
- At any given moment, does the player have something to investigate next (a location, an evidence item, or a person — one of the three)? Which clues are permanently missed if the player "sees but does not note" them? Change all of those.

### 3.3 Deduction Interactions: the trade-offs of presenting, confronting and assembling

The deduction phase has exactly one shared problem: the player has it right — how does the system know they really have it right? The common interactions each have their own temperament:

| Interaction | Player action | Strength | Risk |
| --- | --- | --- | --- |
| Presenting evidence | Pick out an evidence item or testimony at a designated moment | Clear scoring, strong drama | The answer and the timing must be unique; if it degenerates into "guess the designer's mind," it loses points |
| Confrontation | Mark the contradictory line in a chain of statements | Turns "find the contradiction" into a playable action; a natural stage for voiced reading | With too many statements it degenerates into checking every line one by one |
| Assembling | Drag clues into a relationship graph or conclusion slots | The player watches their deduction take shape | High interaction cost; slot hints that are too strong solve the puzzle for the player |
| Choosing and searching | Pick a conclusion, or type keywords to search a database | The first is cheapest, the second freest | Clearing the game by elimination and unguided search both dilute insight |

Judgment rules:

- Judgments should err on the lenient side, never the strict side: when the answer is "the butler," "the steward" and "the old butler" should all be accepted; when an evidence item is required, the question text must have a clear target, and penalties apply only to "wrong answers," not to "slow hands."
- Errors need feedback tiers and a step down: the most likely errors get a dedicated rebuttal (a purpose-written line), the rest fall through to a generic rejection; long multi-step judgments get checkpoints or an instant retry — don't let one slip of the hand wipe out half an hour.

The highest form of a finale is serial accusation: culprit, method and motive submitted one at a time, advancing only when all are correct (Return of the Obra Dinn stakes everything on this serial confirmation). It raises the bar from "guessed right once" to "actually understood," at the cost of bringing the hint system in earlier to prevent dead ends; and don't be greedy with interactions — one or two done deep is enough.

### 3.4 Script Volume and Branch Convergence

A detective script costs double: the text is counted in characters, the structure in "clue-and-conclusion graphs" — and the latter is more expensive to rework. For writing magnitudes see §5. Set up three tables before you write a word:

| Table | What it records | Purpose |
| --- | --- | --- |
| Timeline table | Each character's location and actions at every point in time | The draft for alibis and questioning; prevents continuity breaks |
| Clue table | Clue name, source, the conclusion it points to, which conclusions reference it | Redundancy checks and dead-end fallbacks |
| Evidence table | Appearance, origin, which dialogues it can be presented in | The data source for evidence-presentation judgments |

Discipline: the script may only reference registered clues; at wrap-up, reconcile in both directions and clear out both "written but unused" and "referenced but undefined" entries; every time you change a piece of canon, re-check the timeline and all related text. Most deduction scripts do not die of bad prose — they die of timeline breaks.

Branch convergence: the truth does not branch; the paths do.

- The convergence point is fixed at the truth: the player can take wrong paths and suspect the wrong people, but all paths return to the same truth; branches only flower in side endings and character relationships.
- Tier the cost of wrong accusations: generic rejection is cheapest, dedicated rebuttals are expensive but satisfying, a wrong ending is most expensive. The common practice is to give the two most likely errors their own lines, with generic copy for the rest.
- Register branches in a branch table: every branch records its entry, convergence point, affected state and owning writer; unregistered branches do not enter the script (same method as the Visual Novel page in the Genre Handbooks).
- Two blades for cutting text: trim a second statement of the same information to one line; merge or delete scenes that only pad atmosphere. Cutting 10% before the final draft is routine.

### 3.5 Designing the "Insight Moment"

Insight is the moment the player connects existing clues themselves and derives a new conclusion. It is not given by the staging; it happens inside the player's head. All design can do is prepare the conditions and then not interfere. Three preconditions — miss one and you get one fewer insight:

- Clues arrive before the question: present the evidence first, ask the question after — the question is the hook; reverse the order and players without all the answers can only guess.
- The leap must be short enough: keep the connection distance to one or two hops — clue to clue, then down to a conclusion; an "insight" that takes five clues to assemble is not insight, it is searching.
- There must be a verification entry point: the second after the player figures it out, they must be able to submit and get confirmation. Figuring it out with no way to submit throws cold water on the insight; submitting with vague feedback gives it away for nothing.

Placement and feedback:

- Schedule insight as a scarce resource: one planned major insight per case, usually in the middle-to-late stretch, plus one ending twist; keep small deductions confirmed roughly once every ten-odd minutes so the pacing can breathe.
- Verification must ring out: a correct submission gets clear system confirmation — sound, animation, clue highlight. This is the second when the player cashes "I get it" into "I got it right"; spend staging budget here first.
- Hints do not jump the gun, and the structure gets audited too: hints and dialogue never volunteer conclusions (tiered on request, see §3.2); characters may challenge the player, but never reason in the player's place; if testers brute-force their way to the end, verification is too sparse and the clue chain too long — go back and change the structure, not add hints.

## 4. Technical Essentials

**The case is data**

- Split a case into four pieces of data: scene and text tables, the clue table, the dialogue graph (including present-evidence branches) and the judgment table (which input maps to which conclusion); the engine only does playback and judgment. The content team changes the case by editing tables; changing the case never touches code.
- Freeze the data format before the first case (table exports or JSON, either works), and share one structure across all later cases: change the format constantly and content can never scale; put all text into string tables, organized for translation from day one, with a glossary of people, place and organization names built first.

**State and saves**

- One global detective state table: chapter progress, evidence items held, clues obtained, topics already asked, character trust values; clues are registered as booleans plus their source, and all UI and hints derive from this table.
- Decouple saves from story content (store state IDs, not text) so updating the script never breaks old saves; autosave covers every key clue and scene transition; backlog, skip-read and chapter select are expected as standard (checklist on the Visual Novel page in the Genre Handbooks).

**Judgments, tools and telemetry**

- A judgment input equals three things: the submission, the current context (question ID) and the allowed answer set; synonymous phrasings and near-miss options go into the judgment table, not hard-coded into scripts. Presenting is a first-class citizen of the dialogue system: every dialogue node supports "present an evidence item of type X → jump to the matching branch" — the skeleton of evidence-presentation gameplay.
- Tools start on day one of the prototype: debug commands (skip case, grant all clues, show the deduction graph, force a conclusion right or wrong) and telemetry (error rate and time at judgment points, dwell and abandonment points, hint requests) are both indispensable; the data is for finding "unfairly hard," not for ironing the difficulty curve flat.
- No real-time requirements and a low engineering bar: web, mobile and PC can all carry it; give voiced testimony subtitles and a skip; run through the evidence-presentation controls for touch and gamepad separately.

## 5. Content Volume and Workload Reference

The following are common magnitudes for projects of this kind, for scope estimation — not a promise.

| Form | Case count | Script body volume | Playtime to finish | Timeline magnitude (2–4 people) | Notes |
| --- | --- | --- | --- | --- | --- |
| Single-case prototype | 1 case | 5,000–15,000 characters | 30–60 minutes | 2–4 weeks | Validates only the clue chain and one accusation |
| Small complete work | 3–5 cases | 50,000–150,000 characters | 5–12 hours | 4–9 months | One main thread strings the standalone cases together |
| Typical indie commercial scope | 5–10 cases | 150,000–400,000 characters | 10–25 hours | 1.5–3 years | Character and location reuse; marginal cost declines |

Conversion conventions:

- Writing speed assumes 2,000–4,000 characters of first draft per day (an experienced writer, 6–8 effective hours), with revision and integration counted at 0.5–1× the draft; do not touch the script before the structure is frozen — one rework can void half a case's text, and structural review is counted separately: changing one clue means re-checking the whole case's timeline.
- Testing can only rely on strangers: for every case, blind-test with 3–5 people who have not read it, recording stuck points, wrong accusations and insight moments. The author is the worst tester — a case you have run ten times is always new to a player.

Art and staging magnitudes: scene backgrounds (crime scene, office, accusation stage) commonly run 5–10 per case; evidence close-ups are roughly one-to-one with the clue count and are an easily underestimated line item; portrait expression variants are counted per character who appears. Whitebox staging comes first; invest in detail art after the case is frozen. Scope control: the most common way a detective project dies is "the case file keeps growing"; build one complete case first — accusation staging and failure copy included — then scale up. Cutting a case is always safer than rushing one, and reusing characters and worldbuilding across a series significantly thins out art costs.

## 6. How to Start the First Prototype

Goal: 2–4 weeks, to answer one question — is this clue chain interesting? Don't touch art, voice acting or multiple endings.

1. **Paper case (days 1–2)**: write a single case with 5–7 clues — one incident, three suspects — and set down clearly, for every clue, whether it is true or false; draw a clue graph and work back from the conclusion along each chain of evidence. Ideas cut at the paper stage are the cheapest.
2. **Minimal implementation and guardrails (days 3–10)**: three scenes (crime scene, questioning, accusation), one case-file screen, one evidence-presentation judgment; auto-archiving in the case file, a tiered hint entry point, feedback copy for wrong accusations, debug commands for skipping cases and granting clues. Color blocks plus text are enough — ugly is expected.
3. **Blind test (days 11–14)**: find 3–5 people who have not read the case, watch silently throughout, and record four things: where they get stuck, how many times they accuse wrongly, whether an unprompted insight moment occurs, and whether they can retell the case and their reasoning afterward.

Success criteria (all observable):

- Testers can state the basis of their reasoning, rather than "I just picked"; at least two of them get through the whole case without hints.
- At least one unprompted insight reaction appears (slapping a knee, talking to oneself, "I've got it").
- Every stuck point can be attributed to a concrete design problem (clues not visible, chain too long, verification too sparse), not to "he just couldn't think of it."
- With all art and sound removed, the clue chain still holds and testers are still willing to read the case to the end.

## 7. Common Pitfalls

1. **The narrator withholding, and the unfalsifiable**: a twist that depends on information the player has never seen, or a red herring with no way to refute it, is cheating. Iron rule: information used by the twist is opened up in advance, and every misdirection gets a counter-proof.
2. **Single-path clues**: a key clue has only one route to obtain it; miss it and the player quits. Give every conclusion two paths (§3.2) and self-check by removing clues at random.
3. **Answers by guessing**: the judgment accepts only one phrasing and one timing, forcing players to brute-force. Accept synonymous phrasings; what needs tightening is the deduction chain, not the input box.
4. **Unbalanced punishment**: one wrong accusation means replaying half an hour, and from then on the player dares not think and only dares search for guides. Give key judgments checkpoints, and let error feedback explain the reason clearly.
5. **The detective reasoning for the player**: the protagonist states the whole conclusion in a scene and the player is left clicking OK. Characters may ask and challenge; conclusions must be submitted by the player.
6. **Clue hoarding**: twenty evidence items collected with no place to organize them, and information turns into noise. The case file and deduction board are baseline features, not bonus features.
7. **Timeline breaks**: one piece of canon changes and the dialogue and evidence are not updated to match; the player catches it every time. Go table-driven and reconcile at wrap-up (§3.4).
8. **Dry pacing**: hours of investigating and questioning with no emotional ups and downs — logically smooth, experientially exhausting. Character scenes, humor and suspense are the floor of a deduction game, not decoration.
9. **Scope out of control**: wanting to write a ten-case main plot from the start. Finish one complete case before talking about a series; within one case, build the main clue chain before expanding side branches.

## Further Reading

- Game Design Handbook: information design, core loops and validation methods — the source draft behind §1 and §3.
- Case Studies: methods for breaking down successes and failures — consult when greenlighting and postmorteming.
- Pitfalls & Anti-patterns: product and content pitfalls — read alongside §7.
- Indie Survival: scope control and scheduling discipline — complements §5.
- Genre Handbooks · Puzzle and Genre Handbooks · Escape Room: insight design, tiered hints, clue networks and anti-dead-end safeguards — cross-read with §3.2 and §3.5.
- Genre Handbooks · Visual Novel (Volume 1): branch governance, text engineering and staging rhythm — corresponds to §3.4 and §4.
- Genre Handbooks · Social Deduction (Volume 3): the same family from the opposite direction — deducing living people has no guaranteed answer; compare with the boundary table in §1.
- Homework: write a five-clue paper case, ask a friend to be the "player" while you host. Record where they stop, after which line their eyes light up, and whether they want to solve another case when it is over.

The detective genre ultimately tests only two things: whether the clues were given completely enough, and whether the game responds seriously at the moment the player figures it out.
