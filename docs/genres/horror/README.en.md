# Ludo Atlas · Genre Handbooks · Horror

> **Genre Handbooks · Volume 3**. Positioning: the genre that makes "fear" itself the core experience. The three raw materials — the unknown, loss of control and scarcity — are fed to the player's imagination by recipe; by the time the monster appears, fear is usually already in its settlement phase, and the real engineering all happens before it shows up.
> Companions: Game Design Handbook (core loop and pacing) · Art & Audio Handbook (atmosphere and sound) · Level Design Handbook (spatial pressure and breathers) · Case Studies (breakdowns of finished and failed projects).
> This page carries no external links; benchmarks are widely known works only, and the figures are common magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

One-line positioning: horror is the genre that **turns "unease" into a sustained experience**. What it sells is not the monster but the fear players manufacture in their own heads; the designer's job is to lay out the three raw materials — the unknown, loss of control and scarcity — and then leave the space to the player's imagination. The same "chase plus resources" skeleton can make action horror (you can fight back), survival horror (there is never enough ammo) or psychological horror (the threat is in your head) — but the emotional goal is the same.

The core loop, written as a verb loop (the three sub-genres share the skeleton):

`sense danger → assess resources and escape routes → hide, detour or confront → escape at a cost → brief recovery → a new threat begins to accumulate`

The loop is measured in minutes and holds on three premises: resources are always insufficient (§3.1), safety always has an expiry (§3.5), and information is always incomplete (§3.1). With all three in place, players will perform the fear for you.

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Survival crafting | Survival pressure can ultimately be solved by growing stronger and building; horror requires players to stay weak, and growth must be restrained |
| Action shooter | The ceiling on firepower sets the floor on fear: with plenty of bullets, monsters degrade into targets |
| Escape room | Horror can wear the escape room's shell but does not depend on it; take away the threat and the escape room still stands — the reverse does not hold |
| Narrative exploration | Both use walking and sound; the horror walking branch hands pacing to the threat, while narrative exploration refuses punishment |

A self-check question: swap the monster model for a placeholder cube — is the game still scary? If the answer is "not scary", what you are relying on is art, not design.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (ranked by priority):

1. **Insecurity**: any corner may hide something, and even the save point may not be absolutely trustworthy; the world can revoke the sense of safety at any time.
2. **Fair deception**: the scare's setup must land first, so that afterwards players concede "I was outplayed by design", not "I got played".
3. **Choices under scarcity**: every bullet and every medkit has to be weighed for its use — the decision itself generates tension.
4. **Tension and breathers**: tightness and release alternate; fear is sustained by a sawtooth curve, not by holding maximum pressure throughout.
5. **Survivor narrative**: fleeing, scrambling and sheer luck are the story in themselves, and the ending must tally the cost of the road taken.

Benchmark titles (a widely known list; play them yourself before breaking them down — this genre feeds especially on the first encounter, so complete one full playthrough yourself first and keep a spoiler-free record of that experience):

| Title | What to learn from it |
| --- | --- |
| Resident Evil (including the remakes) | The baseline of resource-management fear; map revisits, ammunition scarcity and stalker-type pressure |
| Silent Hill 2 | The paradigm of psychological horror: fog turns a rendering constraint into an atmosphere asset, and monsters are psychological projections |
| Outlast | The complete vocabulary of unarmed escape: chases, detours, hiding in lockers and battery management |
| Layers of Fear | Spatial storytelling in psychological horror: the house's structure itself deforms — the scenery is the scare |
| Dead Space | A sci-fi shell with the interface fused in: resource suppression plus no-HUD immersion |
| Phasmophobia | A different answer for online horror: teammate reactions, information gathering and procedural haunting |
| Half-Life 2 (the Ravenholm section) | A textbook intensity curve with breathers: safe houses, dialogue and lighting changes interleaved |
| Paper Bride | Chinese folk horror and short-chapter mobile pacing; a release structure that starts free |

## 3. Design Essentials

### 3.1 The Fear Resource Model: Unknown, Loss of Control, Scarcity

Fear is not a single knob but a recipe of three raw materials:

| Raw material | Corresponding mechanic | Common devices | Failure direction |
| --- | --- | --- | --- |
| The unknown | Information gaps | Darkness and fog, sound before image, showing only parts of the threat, false information | The full picture revealed too early; fear drops to zero |
| Loss of control | Stripped power | Unarmed or weak firepower, speed limits and a restricted camera, no winning head-on | Deprivation taken too far — the player becomes a powerless spectator |
| Scarcity | Resource constraints | Ammo, batteries, medicine, inventory slots and save slots | So scarce that players reload saves repeatedly; fear turns into irritation |

Recipe discipline: open at least two raw materials at once; the unknown alone is an atmosphere stroll, scarcity alone is survival torture, loss of control alone is a cutscene.

- Fear habituates: when the same threat or the same trick appears three times in a row, the fourth time pays close to zero. The counter is to rotate fear sources, alternating between threats of different forms so players cannot build up immunity.
- Scarcity is an emotional lever, and the floor is that an affordable way out must always exist: when you are short on bullets, hiding and running must always remain viable; the single remaining vial, the low-battery warning chime, generate more screams than any monster model (for numeric-curve methods see Game Design Handbook §4).

### 3.2 Atmosphere and Jump Scares: Division of Labor and Restraint

Atmosphere is **baseline pressure**; the jump scare is **peak pressure**. The two are not an either/or but a division of labor.

| Dimension | Atmospheric horror | Jump scare |
| --- | --- | --- |
| Time scale | Minutes to hours, continuously in effect | A one-second impact, then fast decay |
| The fear it supplies | Anticipated fear (will it appear) | Event fear (it appeared) |
| Main tools | Lighting, sound layers, spatial pressure, narrative hints | Timing, silence, a sudden audio-visual event |
| Cost structure | Continuous art and audio investment | Single-point choreography; low implementation cost |
| Main risk | Setup so long that players desensitize | Overuse cries wolf; players go from afraid to annoyed |

Execute the jump scare's proportion item by item, and remember one sentence first: its essence is expectation management — first make players expect A, then deliver a modified A; the greater and more justified the violated expectation, the stronger the effect.

- **Setup first**: give 3–10 seconds of foreshadowing before every scare — a change in sound, a light flicker, ambience suddenly falling silent all count; draining out the music and the ambience is a zero-cost, maximally effective warning that tenses players up instantly. A loud bang with no foreshadowing is not scaring — it is offensive.
- **Controlled density**: major scares laid out on a 10–20 minute scale; small jolts (a door closing by itself, a distant noise) can come more densely and carry the everyday pressure; before a trick's third appearance, its form must change.
- **Real and fake mixed**: leave some pre-warnings that never pay off, so the telegraphs cannot be predicted 100%; but do not fool players often, or the setup loses its credibility.
- **Leave an afterglow after the scare**: give a dozen or so seconds of recovery after the peak; players need to breathe, savor it and re-assess the environment before the next one begins.
- **Opening credibility**: within the first 15 minutes, deliver one small but credible scare to prove "things really do go wrong here"; but do not spend your biggest scare early.

The way to build atmosphere is "making the normal feel wrong": lighting, fog and visibility, sound layers (§3.4), traces of objects out of place (bloodstains, drag marks, an overturned chair). The sign that atmosphere has landed is this: nothing has happened, and players already do not dare walk fast.

### 3.3 Chase and Hiding Mechanics Design

Chase sections are horror's peak set piece — and the sections most easily done badly. Design item by item:

- **Opening signal**: give "you are hunted" one consistent, unmistakable signal used throughout (a music switch, a scream, a camera change); players must instantly understand that the state has changed, and only reuse of the signal turns it into a conditioned reflex.
- **Routes must read**: mid-chase, players have no spare attention for wayfinding. Teach chase routes during calm stretches, and avoid introducing un-walked space inside chase sections; when new space is unavoidable, guide it on the fly with light sources and flow.
- **Speed and price**: a chaser's speed commonly runs 0.9–1.1× the player's — slower tests endurance and route memory, faster forces players to break contact using terrain and hiding; the goal is "almost caught" tension, not instant death or never being caught; follow each chase with a breather section (§3.5) to land the adrenaline, and raise the frequency across the game while leaving ample recovery between two chases.
- **Hiding spots**: lockers, under beds, under desks, closing doors. Getting in is not the end but the second act: footsteps approaching and receding, a heartbeat, a peephole gap; it must be interruptible and exitable early, and players must get clear feedback of "I gambled and won" or "that was close".
- **Rules readable and consistent**: hiding safety is decided by inferable rules (line of sight, dwell time, sound), not dice rolls; the chaser's patrol, hearing, search and give-up rules stay consistent throughout — players may fear it, but they must be able to reason about it, and every "I just can't shake it" must trace back to rules, not to AI cheating.

| Chaser type | Behavior | Player's counter | Notes |
| --- | --- | --- | --- |
| Zone guard | Guards a main-route chokepoint; chases only when you enter its sight | Detours, decoys, slipping past during patrol gaps | Cheapest to implement; build this first in the prototype |
| Full-route stalker | Respawns on a timer, closes in slowly and applies constant pressure | Reroute, use terrain and hiding spots | The strongest pressure; at high frequency it becomes annoying |
| Scripted event chaser | A single scripted chase set piece | Memorize the route and follow the guidance | High staging cost, low replay value |
| Perception hunter | Relies on smell, hearing or other special senses | Erase your traces (don't run, don't light fires) | Rules must be taught, or it feels unsolvable |

### 3.4 Sound Design: Half the Genre

Vision only works when players "look at it"; sound works in all 360 degrees — and it is the strongest amplifier of "the unknown". Horror projects' audio budget share is typically significantly higher than other genres (for specs and implementation details see Art & Audio Handbook §7–§9).

- Three layers: **ambience** (a continuous environmental bed, representing "normal"), **event sounds** (footsteps, doors, breathing — breaking the normal) and **music** (emotional instructions, used with restraint).
- Silence is an asset: the most expensive scares are spent on silence. Drain the sound away first, then place one sound; do not carpet the whole runtime with music — most of the time should be left to ambience.
- Sound before image: let a threat be heard before it rounds the corner, and leave the rest to the player's imagination; what is heard lasts longer than what is seen.
- The sound field is an information layer: reverb differences between corridors, basements and open ground let players know what space they are in even with their eyes closed — the sound tiers of opening doors, through walls and across floors must be done seriously; anomalies all signal "something is over there", so guiding sounds and deceptive sounds must use the same volume level, or players learn which sounds to believe and the suspense drops to zero.
- The player's own sounds (breathing, heartbeat, footsteps) are a free tension generator; footsteps while running are psychological pressure by themselves.
- Test method: turn the screen off and play by sound alone for one minute — can you say where the threat is and which way to go? If not, the audio layer is not doing its guidance job.

### 3.5 Pacing: Tension and Release, Safe Rooms and Breathers

- The intensity curve is a sawtooth, not a straight line: fear, release, fear again. Sustained high pressure equals numbness, and players start explaining everything with "that's just how this game is".
- A safe room has three functions: recovery (health and resources), organization (information and routes), and anchor (the memory of "home" makes every departure an adventure).
- Safe-room trust boundaries require trade-offs: absolute safety (save points, shops) lowers death pressure but gives players the courage to restart; relative safety (can be invaded) is more oppressive and must come with warnings and counterplay, or it is plain frustration.
- Breather toolbox: safe rooms, saves, dialogue and radio, reloading and organizing time, music passages ending, door-opening transitions, and transition containers like elevators and cable cars.
- Lay it out with a "scare calendar": put scares, chases and breathers on one timeline and check the intervals and intensities; when homogeneous sections line up, change the method or insert a breather.
- Opening mix and session discipline: the first 15–30 minutes lean on unfamiliarity and small jolts; put the first real threat and first chase in the middle; a comfortable single session is roughly 1–2 hours, with chapters and levels as natural stopping points — don't force players to burn through a state of high tension nonstop.

## 4. Technical Essentials

The engineering difficulty concentrates in four blocks: atmosphere rendering, chase AI, the sound system, and saves and state. Engine choice has no special threshold — Unity, Godot and Unreal all have stock templates to start from.

**Atmosphere rendering**

- Horror is one of the few genres that encourages "not seeing clearly": visibility is a design variable, not tech debt. Fog, volumetric light and post-processing (grain, vignette, chromatic aberration) all need restraint — overdone post-processing reads as cheapness and causes motion sickness; 2D horror takes a different route (light cones, face-close silhouettes, noise) at one tier lower cost than 3D.
- Lighting budget: dynamic shadows are expensive; the common approach is to statically bake the scene and give the player one dynamic light source in hand (flashlight, lighter, phone), moving the performance budget onto "the beam the player is staring at".
- Shadows must not crush to black: keep a very low ambient brightness for silhouettes, or players get lost before they get scared; a brightness slider in the settings page is basic infrastructure for this kind of game.

**Chase AI**

- The chaser is a state machine: patrol, sense, chase, search, give up; put the five states' parameters (view angle, hearing radius, search duration, give-up distance) into the numbers table, and make parameter edits apply live — the game feel of a chase is tuned, not written. Test the edge cases first: doors, stairs, destructible obstacles, corner snags; a chase AI that locks up hurts immersion more than one that cannot catch you.
- Perception in three layers: sight (vision cone plus occlusion checks), hearing (event-driven propagation radius) and contact; each layer must give players readable feedback (it stopped; it is heading toward the sound).
- AI may cheat, but needs a credible explanation: e.g. "it can smell blood". Unexplained pinpoint tracking gets quickly identified as cheap behavior.

**Sound system**

- Build a sound tree with audio middleware (FMOD, Wwise and the like) or the engine's mixer, and make mix states follow gameplay states (one configuration each for exploration, tension, chase and hiding), switching with crossfades and no hard cuts; the approach of attaching sound-effect files ad hoc will inevitably break down on "the same corridor reused three times" (details in Art & Audio Handbook §9).
- Separate scare audio from logic: split one jump scare into three parts — trigger component, audio event and camera event — driven by configuration, which makes timing and intensity easy to tune and lets strong and weak become an accessibility option.
- Build the debug commands first: trigger any scare, jump into a chase section, mute one audio layer in isolation. Horror test sections are short and dense; without these tools, every test pass means walking the same ten minutes again.

**Saves and state**

- Choose the save scheme first: save-point style (typewriters, cassette tapes) amplifies resource and death risk and suits survival horror; save-anywhere lowers risk and suits narrative and lighter horror. When unsure, ask one question: is the stretch players replay after dying a punishment or a review? Align death penalties with pacing: dying in a chase restarts from the start of the section, with the replay held to 30 seconds to a minute; dying while exploring returns you to the safe room.
- Keep state registered in one place: whether a scare has already fired, whether an item has been picked up, whether a door is locked or open — all registered centrally (the same state-table discipline as the Escape Room page); reloading a save must not produce the break in illusion where a scare duds out.
- Randomization trade-offs: procedural haunt events suit online play and replay; scripted choreography suits narrative; start with scripted in the prototype — randomization is late-stage work.

## 5. Content Volume and Workload Reference

The following are common magnitudes for projects of this kind, for scoping estimates — not a commitment.

| Form | Content volume | Completion time | Timeline scale | Notes |
| --- | --- | --- | --- | --- |
| Prototype | One corridor, one chase, one atmosphere stretch | 15 to 30 minutes | 3 to 6 weeks | Validates atmosphere, chase and sound |
| Short chapters | 3 to 5 chapters | 2 to 5 hours | 4 to 9 months | One scare beat per chapter, one set of themed art |
| Common indie release scope | 6 to 8 hours of play | 6 to 8 hours | 1 to 2 years | Animation and audio are the bulk of the cost |
| Larger scope | 12 hours or more | 12 hours or more | Multiple years | Needs mechanical variety to counter emotional fatigue |

- Cost is not in level count but in density: behind a ten-minute horror stretch usually sit dozens of lighting, sound and trigger events; whiteboxing is fast and atmosphere detailing is slow, with a three-to-five-fold blow-up factor being common; environment reuse is the strongest lever — the same corridor recombined through lighting, props and sound into three or four states, and the "re-dress" pipeline is worth investing in first.
- Animation is the most expensive single asset: a chaser's full set of actions (entrance, chase, attack, search, give up) usually eats the bulk of the animation budget — in design, prefer forms that can still perform with few animations.
- Reserve audio investment in advance: sound is half of fear (§3.4), so don't let modeling eat the combined budget for mixing, spatial audio and music; bring audio work in early and leave only polish for the late stages (audio specs in Art & Audio Handbook §10).
- Duration discipline: horror is sensitive to length, and 8–12 hours is the common comfortable ceiling for premium titles; beyond that, emotional density has to be traded against mechanical variety (for scope calibration see Case Studies and Indie Survival).

## 6. How to Start the First Prototype

Goal: in 2 to 4 weeks, build a 15–30 minute "one corridor plus one chase" that validates three things: does the atmosphere hold up, does the chase run, and can the sound scare people. Don't touch production art or story.

| Milestone | What to build | Acceptance (watch behavior, not questionnaires) | Reference time |
| --- | --- | --- | --- |
| M1 Atmosphere space | A whitebox corridor and two rooms, flashlight or light cone | With all enemies off, testers still don't dare walk fast | 3 to 5 days |
| M2 The sound trio | Ambience, anomalous sounds, chaser footsteps | Testers can say where the threat is with their eyes closed | 3 to 4 days |
| M3 Chase section | Chase trigger, chaser AI, one hiding spot | Someone gets chased through a full section; anyone caught can explain why | 5 to 7 days |
| M4 One real scare | A main scare built on a 3–10 second setup | Half the testers are scared, and afterwards accept the setup | 3 to 4 days |
| M5 Wrap-up and testing | Breathers, saves, 3 to 5 playtesters | Testers want a second run unprompted, not a polite smile | 3 to 5 days |

Three rules:

1. All art stays placeholder: the source of fear is mechanics and choreography, not textures; push the urge to embellish until after the gameplay passes testing.
2. Do sound for real, early: in this genre sound is not late-stage decoration — M2's audio sources should already use the final approach, because placeholder sound gives you wrong test conclusions.
3. Ask only three questions per test round: where does he stop, and why? Where does he look while being chased? When it is over, does he want more?

Success criteria (all observable):

- At least 3 of 4 testers complete the whole course without prompts, and nobody gets hard-stuck or lost for long.
- At least half the testers are scared by "atmosphere or choreography" (not just a loud bang) and can restate the chaser's behavior rules; with all music and art removed, the chase and the sound guidance still hold.

## 7. Common Pitfalls

1. **Nothing but jump scares**: no foreshadowing and loud bangs in a row, until players go from afraid to annoyed and then learn to predict them. Scares must be sparse, set up and given an afterglow (§3.2).
2. **Outsourcing fear to the art**: however expensive the monster model, it is a sculpture if the mechanics pose no threat; make players afraid of the rules first, then talk about the monster's face.
3. **The resource curve out of control at both ends**: mid-game ammo overflows and players find no reason to fear anything; or everything must be saved and dead ends abound, so players reload saves repeatedly and fear settles into irritation. Always keep one affordable way out (§3.1).
4. **Chases with no solution**: too fast, too few hiding spots, unreadable rules — caught ten times and still no idea why. A chase is an exam, and the questions must have been taught (§3.3).
5. **Safe rooms out of balance**: either so safe that the pressure drains away, or invaded so often there is no breather. Trust boundaries must be designed, not set on a whim (§3.5).
6. **Visibility and comfort out of control**: too dark to see the path, or first-person motion sickness with no options — both shut some players out at the door; the object of fear should be the threat, not the navigation.
7. **Sound abuse**: music carpeted from end to end and loud bangs used casually — the auditory channel fatigues early. Sound is this genre's scarcest asset; spend it where it cuts (§3.4).
8. **Every scare leaked in the trailer**: marketing gives away the best monster and the hardest moments, leaving only repeats for the release build. The part never shown is the product.
9. **Save design mismatched to the genre**: save-anywhere makes death cost nothing, while sparse save points make death too expensive — both ruin the payoff of tension.
10. **Length dilutes intensity**: fear intensity is highly sensitive to duration, and after ten hours most players have only fatigue left. Better short and sharp than long and blunt.

## Further Reading

- Game Design Handbook: general methods for core loops, difficulty and pacing; fear's numeric curves are done inside its §4 growth and resource curves.
- Art & Audio Handbook: §7 audio design and §9 audio implementation — the full expansion of §3.4 here and the sound section of §4.
- Level Design Handbook: level-design approaches to spatial pressure, guidance and safe rooms, to cross-read with §3.3 and §3.5; the "Ravenholm" breakdown is in its §8.
- Case Studies: breakdown methods for successful and failed projects; pair with Indie Survival and Pitfalls & Anti-patterns when calibrating scope.
- Homework: write a "30-second scare script" (the player's route, what they hear, what they see, how they escape, how they recover afterwards), implement it as whitebox plus sound, and test it with 3 people; then break down the first 30 minutes of a benchmark title, draw its intensity curve, and mark every breather and the setup length of every scare.

Horror ultimately tests only two things: whether the setup plays fair enough, and whether the payoff hits hard enough. When both hold, players will gladly let themselves be scared.
