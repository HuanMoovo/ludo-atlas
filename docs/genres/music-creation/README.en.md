# Ludo Atlas · Genre Handbooks · Music Creation

> **Genre Handbooks · Volume 4**. Positioning: the genre that makes "piecing together a passage that sounds good" the first pleasure. Players do not read music theory or practice an instrument; they splice, layer and swap sound assets into a piece that loops as a finished work — being able to make it and being able to pass it on are this genre's two lifelines.
> Companions: Game Design Handbook (core loops and feedback) · Programming Handbook (audio systems and toolchains) · Art & Audio Handbook (audio design and delivery specs) · Legal, Patents & Competition (sampling and copyright boundaries).
> This page carries no external links; benchmark titles are widely known works only, and the figures are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: a music creation game is the genre **that makes "producing a piece of sound" itself the first pleasure**. Players do not perform scores written by someone else or chase a rating: they pick assets, place them, stack layers, until a passage of a few dozen seconds sounds "like what they had in mind"; there is no judgment, no failure, and all the tension comes from "I made this".

The core loop, written as a ring of verbs:

`pick assets → place them on the beat → layer and swap → listen back → fine-tune → export and share → see other people's work → come back and make another`

The loop rolls at three scales: a single placement is measured in seconds, a finished piece in 5–30 minutes, and an author in weeks and months. It stands on just two preconditions: sound comes out instantly (the very first click must sound good — see §3.2), and finished pieces travel easily (what you make must be sendable to others — see §3.4).

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Sandbox building | Both are creation genres: building outputs space and contraptions, creation outputs sound that flows over time; the two share isomorphic onboarding and sharing structures and can borrow from each other |
| Management and idle | Plenty of products wrap a management or idle shell around creation; once the core verb is no longer "make sound", greenlight it as the host genre and do not estimate it as this genre |
| Professional creation tools | Tools chase the ceiling of expression and take pride in "it can do anything"; this genre wants the opposite: constraints guarantee that "no matter how you play, it never sounds bad" — constraints are design, not compromise |

The boundary with Genre Handbooks · Rhythm in one line: a rhythm game's pleasure is verification — players prove they can hit the author's chart precisely; a music creation game's pleasure is production — players generate the sound themselves.

A self-check question: delete all scores, quests and levels, leaving only sound blocks looping on the beat — would players still want to layer on two more? If the answer is yes, what you are making is a music creation game; if players instantly lose their goal, it is another genre wearing a music skin.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Good sound in seconds**: with zero music theory, the very first click delivers a "this sounds good" result; every asset ships as a piece of a finished work, and any combination of them coexists. This is the life-or-death line, ahead of all depth.
2. **"I made this"**: ownership comes from the credit and the finished piece itself — cover art, title, a playable, shareable file. What players share is not the process of play but the work.
3. **Shallow and deep entrances**: the shallow tier turns out a track in three minutes, the deep tier can adjust volume, panning, arrangement and tone. One entrance cannot hold both kinds of people; lay both roads in parallel.
4. **Echo and relaxation**: plays, favorites and remixes give "make another one" its reason — a community with no echo does not survive a few weeks (§3.4); no failure and no time limit anywhere, with challenges and contests as optional pressure valves only.

Benchmark titles (all widely known; play them yourself before breaking them down):

| Title | What to learn from it |
| --- | --- |
| Incredibox | The textbook of loop splicing: parts as characters, a full stack turning into a song on its own; zero music-theory barrier, with recording and sharing built into one |
| Minecraft (note blocks) | Creation buried inside a sandbox world: redstone note blocks and a community score ecosystem, with UGC distribution forming a system of its own |
| Fuser | The sample-collage direction: stitching fragments of existing music into new works — a test of the gameplay ceiling of "recombining assets" |
| Sky: Children of the Light | The social scenario once instruments are handed to players: ensemble play and improvisation become ways of communicating, and sharing happens between people, not necessarily through files |

## 3. Design Essentials

### 3.1 The "Playing Music" Loop: Splicing, Layering and Swapping

There are only three core actions, each mapping to a product direction:

| Action | How it plays | Learning difficulty | Output form | Representative route |
| --- | --- | --- | --- | --- |
| Splicing (loop combining) | Each layer offers a few 1–4 bar loop blocks; selecting one plays it, and layers lock to the beat automatically | Lowest | A short, seamlessly looping track | Incredibox-style part splicing |
| Layering | One piece split into parts — drums, bass, harmony, melody, vocals — added and pulled out layer by layer | Low | A complete short song with section dynamics | Part toggles plus section arrangement |
| Sampling | Cutting licensed assets into beat-aligned chunks, then rearranging, time-stretching and pitch-shifting them into new passages | Medium | Remix-style works | Fuser-style asset recombination |

Reference values (typical magnitudes): 8–16 blocks to a sound pack; 2–4 variants per layer; 1–4 bars per block, with everything in one pack at the same tempo and key. The ceiling on total combinations is the product of the variant counts across layers — the most direct accounting of "combination space"; assets are content, so swapping in a new sound pack swaps the musical style, and the update cadence rides on packs rather than features (§5).

- **Mutual exclusion, complementarity and ceremony**: variants within a layer replace one another, while layers converse (melody and bass must leave each other room to breathe); the moment every part arrives is the pack's peak — stage it as one "ensemble" performance; pulling a layer out is also an action in its own right, and that is where the sense of sections comes from.
- **The discipline of sampling**: cut points land on the beat, durations are whole, pitch stays adjustable; keep the pleasure of "recognizing the source" while clearing the rights gate (§3.3).

### 3.2 Zero-Theory-Friendly Design: Hiding Music Theory in the System

For ordinary players, music theory is a threshold they have no wish to cross at all. This genre's design obligation is to make every theory decision for the player and leave only the choices:

| Device | Implementation | How players perceive it |
| --- | --- | --- |
| Quantization | Every placement snaps to the beat grid; nothing can be "off" | "However I place it, it's right" |
| Key constraint | All assets in a pack share one key, so any stack coexists | "Whatever I stack sounds good" |
| Harmony following | One track carries the chord progression and the rest follow automatically | "I think I can arrange now" |
| Starter templates | Official song skeletons, blank packs and other people's finished works all work as starting points | "I know where to begin" |
| Foolproofing feedback | There is no "wrong note": every click yields a usable sound | "I can click around boldly without ruining it" |

Two disciplines:

- **Choices first, depth later**: selecting, dragging and toggling are enough to complete a creation, with keyboard input and hand-written notation as advanced channels only; the advanced knobs (volume, panning, effects, part swapping, section arrangement) must exist but never on the beginner's first screen — the shallow tier never sees them, the deep tier can find them.
- **The acceptance bar**: test with people who cannot read music at all — a pass means producing a 30-second piece within 5 minutes, with no guidance throughout, and actively wanting to send it to someone (§6).

### 3.3 Sampling and Copyright Boundaries

Assets are this genre's provisions, and they come in through three routes with three sets of rights (verify clauses against Legal, Patents & Competition; this section lists actions only):

| Asset source | How it is obtained | Rights actions |
| --- | --- | --- |
| Self-made | Recorded or synthesized by you or collaborating musicians | The contract states the copyright assignment and credit; deliverables include source files and metadata (Legal, Patents & Competition §2) |
| Music libraries and royalty-free libraries | Buying or subscribing to ready-made assets | The license must cover in-game distribution, player exports and remixes, as well as promotional material and screen recordings |
| Commissioned custom work | Having musicians produce to a themed pack's spec | Spell out buyout or revenue share, revision counts and exclusivity scope; share one acceptance sheet with library content |

Two bottom lines:

- Sampling involves two sets of rights: the master recording and the composition are independent, and clearing only one is not enough; "re-recording a similar passage" can still infringe the composition.
- Player exports and remixes must be covered up front: posting a work to a short-video platform or having it taken and remixed are both acts of distribution and need a place in the license scope, with the boundary written into the terms of service; keep an asset ledger from the very first sound, filing sources, license proof and revision records item by item (Legal, Patents & Competition §2), with AI-generated assets booked separately.

### 3.4 Sharing and Community: Works Have to Get Out the Door

A work faces three gates on its way out: **export** (one click to a shareable file with cover art, credit and an asset-source list), **display** (being seen: the works library, a player, a share entry point) and **echo** (play counts, favorites and remixes — letting the author know someone listened). Miss one gate and the urge to create goes cold within weeks.

Three channels, ordered from low cost to high:

| Channel | Output | Cost | Fit |
| --- | --- | --- | --- |
| Screen recording and video export | A vertical short video with cover art and credit attached automatically | Low, a purely local feature | All products; short-video platforms are the largest discovery channel |
| Audio file export | Lossless and MP3/OGG tiers | Low | Playlists, voice messages, reediting |
| In-game works library | Browsing, previewing, favorites, remixing, charts | High: servers, moderation and recommendation slots are long-term bills | Products intended for long-term operations — see Modding & UGC for the full expansion |

The remix mechanic is this kind of community's healthiest loop: works may be taken apart and recombined, and lineage information preserves credit (the remix tree). Three companions: featured picks and theme-week events give creators goals; one-click previewing drives the cost of "give it a listen" to its floor; uploaded content goes through review (audio and text), reporting and takedown channels stay public, and community permissions for younger users are designed separately. The works library is an operations cost, not a feature toggle — write the headcount for moderation and recommendation slots into the budget at greenlight.

## 4. Technical Essentials

The engineering proposition in one line: **the arrival of sound must land on the beat, in sync with the player's hands; without that, the gameplay does not exist**. The difficulty concentrates in three places: the audio engine, the export pipeline and the works data.

**The audio engine**

- Beat authority and seamless looping: all loop blocks follow one audio clock and align to the sample on the same beat, or layering smears (playback position queries update at a coarse granularity and need interpolation and smoothing — Programming Handbook §2.7); loop points and head-to-tail trimming are standardized at import (for loudness and loop-point specs see Art & Audio Handbook §10.1), and preview and export read the same data, so that "great in preview, broken in the export" never happens.
- Triggering and load: click-to-sound latency stays in the tens of milliseconds; mobile and Bluetooth paths are naturally slower, so design UI feedback for the worst device; keep short blocks resident in memory and load by pack, cap the number of simultaneous voices and merge or truncate beyond it by priority — never let players stack their way into clipping and dropped frames.

**Export and rendering**

- Offline rendering: export replays the project to a file rather than running live playback, avoiding latency and noise in the capture; rendering and preview must match beat for beat (the same sound sources and effect parameters).
- Formats and duration: the lossless (WAV) and lossy (MP3/OGG) tiers serve different uses; video export runs through a recording or rendering pipeline, with cover art and credit templated; rendering runs on a background thread or a separate process, with progress and cancel.

**Works data and the backend**

- The project file is a reproducible format of "asset references plus timeline events": it carries a format version number and migration functions, and old works must still open after a game update; assets are referenced by ID rather than embedding the audio itself, which keeps work files small and makes dependency manifests and version checks feasible on the server.
- The works-library backend: uploads, a moderation queue, metadata, play counts and remix lineage; anti-abuse rules (chart manipulation, spam uploads) come first, and player works are treated as foreign data (size limits, reference validation, unknown fields rejected), with the boundary against code-level mods defined by Modding & UGC.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for scoping estimation; not a commitment.

| Project form | Content scale | Time reference | Notes |
| --- | --- | --- | --- |
| Prototype | 1 sound pack (8–16 blocks), no sharing | 2–4 weeks | Validates the pleasure of splicing and layering and the combinability of assets |
| Small complete work | 3–6 themed packs, export and sharing closed loop | 3–6 months | Solo or 2–3 people, with all assets original or fully licensed |
| Typical indie work | 10–20 themed packs, works library and remixing | 1–2 years | Community features and asset capacity are the two main threads |
| Long-term live-ops form | Continuously updated assets and events | 2+ years | Asset updates are content operations, and licensing and moderation are long-term bills |

Magnitudes for individual content units:

| Content unit | Unit cost | Notes |
| --- | --- | --- |
| One loop asset (1–4 bars) | 0.5–2 person-days | Recording or synthesis, beat cutting, loudness and loop-point standardization, metadata |
| One themed pack (8–16 mutually compatible blocks) | 2–6 weeks | Whole-pack design at one tempo and key plus per-block production; packs can be swapped and reused across one another |
| Commissioned custom work (compose first, then split into packs) | Per track; several person-days to several weeks | Includes licensing and metadata delivery; clauses in §3.3 |

Two scheduling anchors: from zero to "can make a 30-second piece and export it" usually takes 2–4 weeks; to a vertical slice (one themed pack plus a sharing loop, ready for outside testing) usually 2–3 months. Assets are the most flexible knob: freeze the loop and editing feel first, then expand packs according to capacity; cutting packs is safe, changing loops is dangerous.

## 6. How to Start the First Prototype

The first prototype makes one sound pack only, finished in 2–4 weeks, touching no accounts, no works library and no art.

1. **Week 1: the sound pack and "click to play".** Prepare 8–16 assets (start with licensed-clean or self-made loops, logging sources and licenses in the ledger first — Legal, Patents & Competition §2); at one tempo and key, with metadata (BPM, key, bar count) written into the files; one click plays, another click pulls the block out, all aligned to the audio clock.
2. **Weeks 2–3: layering, fine-tuning and a minimal export.** Stand up the layer structure (drums, bass, harmony, melody) and make quantization and the key constraint take effect; add a looping preview that plays while you edit, so changes are heard the moment they are made; then build the offline render — a 30-second piece with a title and credit, ugly UI or not, must run end to end, because it is where the sharing chain begins.
3. **Week 4: outside testing.** Find 5 people who cannot read music, give them no guidance at all and watch what they make in three minutes; record the stalls, the random clicking and the moments they give up, and collect who they "want to send it to".

Success criteria (all observable):

- At least 4 of the 5 testers produce a 30-second piece within 5 minutes with no guidance throughout; a passage assembled from 20 random clicks still lands inside "listenable" (the foolproofing check, §3.2).
- At least 3 people offer on their own to send the piece out or record it themselves; every asset's source and license proof is on the ledger, block by block (Legal, Patents & Competition §2), with no assets of unknown origin entering the prototype.

If splicing and layering do not pass, do not expand the assets and do not build the community yet: reworking the loop's game feel is the most expensive thing there is, and expanding assets is the cheapest.

## 7. Common Pitfalls

1. **Music theory up front**: force chords, notation and modes on players as tutorials and the mass audience leaves in the first hour; theory belongs hidden inside the system (§3.2).
2. **Assets at different tempos and keys**: combinations come out unlistenable and the foolproofing collapses on the spot; one tempo and one key per pack is an iron rule at the factory (§3.1).
3. **Parts but no sense of completion**: without the moment a "finished piece" crystallizes and a path to export, players drift away half done (§3.1, §3.4).
4. **Checkpoints on the sharing chain**: export requires registration, requires unlocking, uses nonstandard formats; distribution is free growth — do not tax it at the exit (§3.4).
5. **Vague rights**: assets of unknown origin, licenses that fail to cover player exports and remixes; clear Legal, Patents & Competition before launch and file every block (§3.3).
6. **Turning creation into a level grind**: adding time limits and scores turns inspiration into a chore; creation needs freedom and low pressure, and pressure valves may only be optional (§1).
7. **Audio latency and desync**: sound lands half a beat after the click, layers misalign, loop points click; without the audio clock and seamless looping, the gameplay simply collapses (§4).
8. **The community left exposed**: a works library with no moderation or reporting, where everything goes live on upload; UGC compliance and operations are long-term bills (§3.4, Modding & UGC).
9. **Depth and content that run out of steam**: players see everything on day one, with no advanced knobs and no asset updates (§3.2); assets pile up but stay mutually incompatible, so the combination space stands still — one world per pack, with packs swappable against one another (§3.1, §5).

## Further Reading

- [Game Design Handbook](../../fundamentals/game-design/README.md): the underlying draft for core loops, feedback and numeric methods, covering §1 and §3.
- [Programming Handbook](../../fundamentals/programming/README.md): audio systems (§2.7) and performance budgets, covering §4.
- [Art & Audio Handbook](../../fundamentals/art-audio/README.md): audio design and delivery specs (§7, §10) — check the spec sheet before assets go into the library.
- [Legal, Patents & Competition](../../publishing/legal/README.md): copyright, asset ledgers and contract clauses — read it through before greenlighting sampling or a music library.
- [Modding & UGC](../../pipelines/modding/README.md): the full expansion of the works library, moderation and community operations — the companion to §3.4.
- [Genre Handbooks · Rhythm](../rhythm/README.md): the mirror page for the judgment and chart direction; the same engine roots, the opposite product goal.
- [Pitfalls & Anti-patterns](../../pitfalls/README.md): the high-frequency pitfalls of creation and UGC genres, to read against §7.
- Homework: without writing code, first lay out a layering table for 8 assets in an existing music toy or on paper, hand-derive the constraints (tempo, key, register, breathing room) under which any combination coexists, and only then decide the sound pack's theme and licensing route.
