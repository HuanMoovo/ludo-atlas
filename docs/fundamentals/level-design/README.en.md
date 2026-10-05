# Ludo Atlas · Level Design Handbook

> From "placing scenery" to "designing experience": building metrics, wordless guidance, pacing control, the whitebox workflow, and breakdowns of ten classic levels.
> Applies to both 2D and 3D. Companions: the Game Design Handbook (systems layer) · Programming Handbook · Art & Audio Handbook · Production Handbook.
> Deliberately link-free. Level design's feel comes from observation and practice; reading ten articles is worth less than whiteboxing one room.

---

## 1. What a Level Designer Does

A level designer is the person who turns systems into experience. Systems provide the actions — jump, shoot, build — and the level decides in what space, at what pace, and under what pressure those actions happen.

Three sets of interfaces with the people you work with:

- With designers: get the target experience (tense? exploratory? satisfying?) and the target duration, and translate them into paths and encounters.
- With artists: define the functional requirements of the space (sightlines, landmarks, readability); art then decides what it looks like.
- With programmers: confirm the boundaries of the mechanics (what can be changed, what's locked down), then start designing.

Documentation habit: one one-page spec per level, spelling out the target emotion, expected duration, new elements making their first appearance, checkpoint placement, and the list of asset dependencies. A level without that page will inevitably be half redone.

## 2. Metrics: Designing Space with Time and Steps

Beginners place platforms by feel; veterans place them by numbers. There is only one method: build a "unit table" for your project, then measure and calibrate it in the greybox.

The numbers you need to measure first:

| Metric | How to measure | Use |
| --- | --- | --- |
| Character movement speed | Meters/tiles traveled per second | Converts every distance |
| Horizontal jump distance | Farthest horizontal displacement from takeoff to landing | Grading platform gaps |
| Jump height | How high a full jump gets you | Vertical level heights |
| Air time | Seconds from takeoff to landing | Aerial moves and danger windows |
| Door and corridor width | Multiples of the character's body | Comfort of passage |
| Sightline distance | How far you can see on one screen | Range of guidance and foreshadowing |

The key conversion idea: **express distance as time**. The gap between two platforms equals jump air time times horizontal speed, so "can I make this jump?" becomes "how many air times does it take": 0.8 air times is a comfortable gap, 1× is a standard challenge, 1.2× is a limit play. A three-tier spacing system lets difficulty be tuned precisely, instead of by trial and error.

Three pacing scales also belong in the table: a small hit of stimulation every 3 seconds (a jump, a shot, a pickup), a medium event every 30 seconds (an encounter, a discovery, a twist), a major beat every 3 minutes (an area climax, a scene change). Too few hooks and players get bored; too many and they get tired.

## 3. Guidance: Teaching Without Words

Players don't read manuals; they read the environment. The available techniques for wordless guidance:

1. **Light and contrast**: players naturally walk toward what is brighter, more colorful, more animated. A warm lamp at the end of a corridor beats any arrow.
2. **Composition and sightlines**: use walls, cliffs and camera orientation to press the player's gaze onto the target. The first frame of entering a room decides where the player looks.
3. **Breadcrumbs**: small rewards or small events along the way to lead the player on.
4. **The broken bridge**: first let players see where they want to go, then collapse the direct route and force another path. A route players find themselves feels far better than one you laid out.
5. **Safe teaching**: rooms that teach a new mechanic carry no death penalty, so players can experiment freely.
6. **Telegraphing danger**: use color, dangling props and sound to signal "there's a trap here" ahead of time. Invisible deaths are a prime source of bad reviews.

The formula for a teaching sequence is "show, use, vary, combine": first let players see it (demonstrated once in a safe environment), then let them use it (a low-pressure scene), then vary it (change the conditions, e.g. add time pressure), and finally combine it (use it together with old mechanics). Teach only one new thing at a time.

Guidance checklist (run through it for every new room): where does the player look on entering? Is the objective in view? Can they notice a wrong turn within 5 seconds? Is anything hidden in a dead end? Is the cause of their first death understandable?

## 4. Pacing and Intensity Curves

Chart a level's tension as a line and you have an intensity curve (some teams call it a heartbeat chart). A healthy curve alternates peaks and troughs — tension, release, tension again — while climbing overall. A flat line (constantly tense, or constantly calm) is a disaster either way.

Three tools for managing the curve:

- **New-element rollout table**: list the room where each new mechanic first appears, keeping the spacing even and the introduction to one at a time.
- **Checkpoint map**: checkpoint spacing corresponds to "the run you repeat after a retry." Once the punishment run exceeds 20 seconds, frustration starts to outweigh the appetite for the challenge.
- **Difficulty sawtooth**: difficulty climbs overall, but needs local dips. After a long climb, always give an easy stretch — that's the breathing.

## 5. Spatial Language

Players need to read the meaning of a space within half a second: this is passable, that's a wall, this crate can be pushed, that cliff is a dead end.

- **Readability comes from contrast**: walkable areas vs. decoration, foreground vs. background, must differ in shape and color. Blurry art boundaries are the root of getting lost.
- **Alternate openness and pressure**: open spaces relax, narrow corridors tighten — a free pacing tool.
- **Looping structures**: one-way doors, elevators and unlocked shortcuts let the map grow a three-dimensional shape in the player's head. The "so this connects to there" surprise is the core pleasure of exploration games.
- **Landmark navigation**: place 1 to 2 landmarks visible from afar in a large area, with color-coded zones, so players can say where they are without checking a map.

## 6. The Level Workflow: From Whitebox to Final

There is only one correct order, and reversing it always blows up:

1. **Paper**: sketches and flowcharts. Objectives, paths, encounters, emotional peaks — think them through before you touch the tool.
2. **Greybox**: build all the space out of basic geometry only. Use placeholders to validate three things: can players get through (function), do they want to get through (desire), will they remember it (memorability). Being ugly at this stage is correct.
3. **Playtest iteration**: get people to play, observe, revise, play again. The author's intuition stops working by round three — bring in new people.
4. **Art pass**: art comes in; function first. After the art pass you must re-run the level to check that sightlines, guidance and performance haven't been blocked.
5. **Polish**: VFX, sound, camera, pacing fine-tuning. The final stage tunes 0.1-second-scale things: camera duration, hint delay, screen shake amplitude.

The most common greybox mistake is "decorating too early": afraid the team will lose confidence looking at something ugly, you apply textures ahead of schedule; then gameplay changes, the textures are all wasted, and you no longer dare to make major structural changes.

## 7. Genre Notes

| Genre | Spatial design core | Special notes |
| --- | --- | --- |
| Platformer | Jump-radius table and safety nets | Put punishment at pacing changes, not at pure-execution moments |
| Metroidvania | Ability gates: locks, keys, revisits | Every new ability needs a "reason to come back" |
| Shooter / arena | Cover, sightlines, entry/exit routes | Size the combat space before decorating it |
| Stealth | Patrol routes, vision cones, alert tiers | Leave routes that let the game go on after you're spotted |
| Puzzle | Restrained element count, teaching order | One core concept per room; don't stack concepts |
| Open world | Points-of-interest spacing and density | Chain the route with sightlines and landmarks, not a quest list |
| Horror | Resource pacing, safe rooms, audio cues | Scares come from setup and subverted expectations, not cheap jump scares |

## 8. Ten Classic Breakdowns

All of these are cases the industry has analyzed again and again; play each one yourself before reading the analysis.

1. **Super Mario Bros. World 1-1**: the textbook first level. It teaches movement, block bumping, mushrooms, pipes and hidden rewards in sequence, with zero text throughout. Transferable: put teaching objects on the route players must take.
2. **The Legend of Zelda: Ocarina of Time — Inside the Deku Tree**: the first 3D dungeon solved "how to give directions in three dimensions." Follow the camera, read the textures, try the interactions. Transferable: 3D guidance starts by constraining the camera.
3. **Portal — the first ten test chambers**: one rule taught per room, examined with the new rule immediately, then combined at the end. Transferable: the "teach, test, combine" three-part structure for puzzle levels.
4. **Half-Life 2 — Ravenholm**: a textbook intensity curve. High pressure throughout, with breathers woven in (safe houses, dialogue, lighting changes). Transferable: horror stretches need room to breathe, or players go numb.
5. **Dark Souls — Undead Burg and Undead Parish**: the model for three-dimensional looping. Elevators, shortcuts and one-way doors stitch three areas into one, and the death runback keeps getting shorter as shortcuts unlock. Transferable: shortcuts are the reward for players who retry.
6. **Celeste — Chapter 1**: punishment-free teaching plus strawberries (optional difficulty). The main path teaches the basics, strawberries serve challenge-seekers, and the A/B sides split the audience. Transferable: make difficulty an option, not a gate.
7. **The Witness — the starting area**: not a word of explanation; the puzzle sequence itself does all the teaching. Every panel teaches a new rule. Transferable: rule teaching can be handed entirely to the player's trial and error and the feedback.
8. **Inside — the opening**: a wordless opening that uses lighting, dogs and a chase to carve "running" into the player's muscle memory. Transferable: the opening 5 minutes decide whether players believe in your world.
9. **BioShock — the opening ("Welcome to Rapture")**: an extended scripted sequence as a world introduction; the player barely acts, yet the tension never lets up. Transferable: a controlled seizure-of-agency sequence buys deeper emotional investment, but you can only spend it once or twice in a lifetime.
10. **God of War (2018) — the opening fight with the Stranger**: teaching, narrative, emotion and spectacle in one. The combat teaching hides inside the story's conflict; by the end, players know the systems and remember the characters. Transferable: a tutorial doesn't have to be a briefing — make it part of the story.

## 9. Tools and Docs

- Whiteboxing tools: the engine's built-in geometry and modeling mode are enough; for focused work use dedicated tools (2D level editors like Tiled and LDtk — see Resources §2).
- One-page level doc template: number and name, target emotion, expected duration, first-appearance elements, checkpoints, a sketch of the emotion curve, an asset dependency table, and acceptance criteria (observable sentences like "the player should be able to learn the slide without dying").
- Playtest observation method: let the player play; you stay silent, don't hint, don't defend. Record three things: death points (where they get stuck), pause points (where they get confused), anomalous routes (where they took a long detour or fell back on an old habit). This beats a questionnaire ten times over.

## 10. Common Mistakes Checklist

1. Art before gameplay (wrong order; nothing can be changed later).
2. Testing only yourself (the author's filter will deceive you all the way to launch).
3. Big and empty: long corridors with no events, no decisions, no views.
4. Difficulty lurching between hard and easy, a roller-coaster curve.
5. Testing right after a single lesson, with no low-pressure practice stretch.
6. Symmetry and repetition across the whole map, stripping players of directional reference points.
7. Guidance that leans on text pop-ups and in-your-face arrows.
8. Checkpoints too far from the death point, turning retries into a cross-map run.
9. Invisible pits and deaths with no warning.
10. Camera blind spots: players can't see where the threat came from.
11. Important objectives occluded by decoration (a problem newly introduced during the art pass).
12. Ignoring performance during the greybox stage, then cutting content and tearing out structures late.

## 11. Exercises and Self-Test

Homework to set yourself, from easy to hard:

1. **Remake**: recreate Mario 1-1 or Portal's first test chamber using your own project's mechanics.
2. **Onion**: build easy/standard/very-hard versions of the same room, changing only layout and spacing, never values.
3. **Greybox sprint**: build a minimal level with "one lesson, one encounter, one reward" in 30 minutes.
4. **Observation homework**: play any game and chart 10 minutes of its intensity curve, plus every guidance technique it uses.

Self-test, ten questions: where does your gaze land on entering a room? Has the new thing been taught? What does failure cost? Does the pacing breathe? Can you find the landmarks? How many hooks are there in three minutes? Is there feedback when you go the wrong way? Can players find a route that works that you never designed (this is a good thing)?

## 12. Further Reading

- For the collected GDC level design talks, see Resources §3 (search the "level design" tag).
- For book recommendations, see the reading list section of Open Source Picks & Book Recommendations (Game Feel is the most practical on game feel and fine-tuning).
- Play more, break down more, whitebox more. The first two are input; the last is the only path that turns input into skill.
