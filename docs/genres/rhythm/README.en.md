# Ludo Atlas · Genre Handbooks · Rhythm

> **Genre Handbooks · Volume 3**. Positioning: the genre that makes "actions landing precisely on a point in time" the first pleasure. Judgment is measured in milliseconds, calibration comes before everything, and the song library is the main content line.
> Companions: Game Design Handbook (core loops and feedback) · Programming Handbook (audio clocks and input latency) · Art & Audio Handbook (audio design and implementation) · Legal, Patents & Competition (music rights and contracts).
> This page carries no external links; examples are widely known works only, no specific tracks are named, and the figures are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: rhythm is the genre **that makes the precision of timing judgment the first pleasure**. Every input the player makes is converted into an offset from the beat, and the judgment result answers "how accurate are you"; hitting accurately is itself the content, not a means of getting somewhere.

The core loop, written as a verb cycle:

`listen → anticipate → press → receive the judgment → adjust your feel → combo or break`

This loop is measured in milliseconds. It holds on two preconditions only: judgment is trustworthy (§3.1) and calibration is in place (§3.3). Players are extremely sensitive about how they attribute failure in this genre — an offset of a few dozen milliseconds is reliably perceived; the moment judgment becomes "unreliable", players stop investing immediately.

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Action games | In action games rhythm shapes game feel; in rhythm games time is a hard rule and judgment is measured in milliseconds |
| Rhythm-action (runners, motion swinging) | The judgment carrier shifts from the input instant to a continuous motion; recognition uncertainty is higher, so the judgment window must be widened |
| Dance and fitness games | The goal leans from precision toward completion and exertion; scoring is lenient and continuous participation outranks judgment depth |
| Embedded rhythm minigames | A QTE-grade stretch of gameplay cannot carry a product; a rhythm game needs long-term investment in a judgment system, a song library and beatmap tools |

A self-check question: mute the music and leave only the notes — the game still plays (playing by sight works); replace "press on the beat" with "any press counts" and the game loses its meaning at once. If the second substitution breaks the game, what you are making is a rhythm game.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Trustworthiness**: the same input gets consistent judgment on any device, with the error distribution centered on zero. This is a life-or-death line, ahead of the thrill.
2. **Fluid thrill**: audio and picture in sync, hit feedback immediate, combos with weight — the illusion of performing comes from the three stacking together.
3. **Visible growth and a challenge ladder**: accuracy, grades and score curves quantify what practice earns; difficulty tiers cover newcomers and experts alike, and the song library's difficulty distribution is itself playable content.
4. **A sense of stage**: track presentation, interface atmosphere and leaderboards dress "playing it over and over" up as a performance.

Benchmark titles (play them yourself before breaking them down; judgment feel cannot be learned through video):

| Title | What to learn from it |
| --- | --- |
| osu! | The community beatmap ecosystem, one engine shared across modes, distribution and rating for user-made beatmaps |
| Taiko no Tatsujin | Minimal two-key input, the dual arcade-and-home design, the way its judgment tiers are named |
| Rhythm Heaven | The beat hidden inside a skit, teaching separated from testing; lenient judgment but extremely clear feedback |
| Muse Dash | The subtractive design of two keys plus touchscreen on mobile, visual packaging and a low barrier to entry |
| Beat Saber | The mapping from motion input to judgment, scoring swing amplitude and timing separately |
| Hatsune Miku: Project DIVA | Key-combination judgment, the binding of MV-grade staging to each track's art |
| Guitar Hero | The psychological contract of peripheral input, the ritual feel of the band fantasy |
| Friday Night Funkin' | The community song library and mod ecosystem, and the track-update cadence achievable at low art cost |

## 3. Design Essentials

### 3.1 The Judgment System: Windows, Attribution and Leniency

The judgment chain is four fixed steps: capture the input instant (a high-precision timestamp) → convert it to the audio clock → take the time difference against the nearest unjudged note on that lane → produce a result by tier. Four parameters decide the whole experience: window width, window symmetry, attribution rules, and the combo and score rules.

Common magnitudes for judgment tiers:

| Tier | Window (±) | Design intent |
| --- | --- | --- |
| Perfect | 20–40 ms | Separates experts; the main scoring zone for competition |
| Good | 60–100 ms | The everyday band for most players; the feedback should feel great, not humiliate |
| Pass | 100–160 ms | A floor of feedback, avoiding zero-reward frustration |
| Outside the window | Combo break | An offset large enough that the player can hear it themselves |

Three disciplines:

- **Choose leniency by audience, and put consistency before strictness**: casual and mobile titles widen the whole scale; competitive titles may tighten it, but must stay consistent. Strict is not the same as deep — leave difficulty to the beatmaps.
- **Tune windows against the offset histogram**: the debugger must output the offset distribution of every judgment, and a histogram is only tuned when it is centered on zero and not too wide; a global shift means adjusting the offset, a spread-out distribution means adjusting the window. Players often have systematic tendencies to hit early or late, and asymmetric windows are a legitimate tool.
- **Windows must not fight neighboring notes**: on one lane, adjacent notes' judgment windows may not overlap (a rule of thumb: keep the minimum spacing above twice the window's full width), or a single press qualifies for two notes and attribution becomes guesswork. For high-density runs, either cap the subdivision or handle them as a single judgment block.

Playing by ear and playing by sight need separate design: playing by ear means hitting with the music's beats, playing by sight means hitting with the scrolling notes. Low-density stretches should make the two agree (place notes on strong beats and give them visual emphasis); high-density stretches lean on sight, with a scroll lead-in commonly of 0.5–2 seconds and a player-adjustable speed. The two fail for different reasons (ear play fears latency, sight play fears dropped frames and scroll judder), so test them separately: once with the screen off, playing only by listening, and once with the sound off, playing only by the notes.

### 3.2 The Beatmap Design Process

The beatmap is this genre's level. The fixed process has six steps: mark the BPM and offset → divide into bars → lay the skeleton (main beats and phrase accents) → add flourishes (subdivisions, stacked notes, runs) → tier the difficulty → readability checks and test-play tuning. Build the low-difficulty beatmap first — it defines the skeleton; the high-difficulty beatmap is density and technique stacked onto that skeleton.

Memorize the BPM-to-subdivision conversions first (a quarter note counts as one beat; 1/4 beat means sixteenth notes):

| BPM | 1 beat | 1/2 beat | 1/3 beat | 1/4 beat |
| --- | --- | --- | --- | --- |
| 90 | 667 ms | 333 ms | 222 ms | 167 ms |
| 120 | 500 ms | 250 ms | 167 ms | 125 ms |
| 150 | 400 ms | 200 ms | 133 ms | 100 ms |
| 180 | 333 ms | 167 ms | 111 ms | 83 ms |

The relationship between density and judgment windows is the table's most important use: at 180 BPM the 1/4 beat spacing is 83 ms, smaller than the full width of a ±50 ms window (100 ms); such runs either move to slower stretches, narrow the window, or switch to special judgment. Also note that stretches alternating triplets (1/3 beat) with 1/4 beats are easily read as one density — check them separately in playtests.

Spread 3–5 difficulty tiers per track, with the tiers defined by structure rather than by deleting notes:

| Tier | Content structure | Target players |
| --- | --- | --- |
| Beginner | Main beats and held notes | First contact with the genre |
| Regular | Beats plus a little 1/2-beat work | Can play but does not chase scores |
| Advanced | Beats, 1/2 beats and scattered 1/4 beats | The everyday core crowd |
| Expert | 1/4-beat runs, stacked notes, cross-lane technique | Core players and leaderboard competition |

Calibrate difficulty ratings against testers' actual pass rates, not gut feel; within one tier, tracks must have similar completion rates across the target audience, or the tier loses credibility. The readability checklist: is the visual grouping clear, does the density breathe, are there physically unplayable combinations (same-hand cross-key conflicts, demands beyond one hand's movement speed), and do lane switches leave enough time. Store beatmaps in beats (musical time) with milliseconds as a derived value, so tempo-change tracks and BPM corrections never require re-charting the whole song; the editor's minimum spec is a waveform plus beat grid, note entry, instant audition and hot reload, with a validator (overlaps, out-of-bounds, same-lane spacing below the window) that raises a warning on save.

### 3.3 Audio Latency Calibration (Handling Device Differences)

Separate three accounts first, and do not smear one number over all of them: **beatmap offset** (where the track's beats actually start, marked by the author), **device latency** (the delay introduced by the player's device chain, the calibration value) and **visual latency** (the display chain, especially pronounced on TVs and projectors). The judgment baseline is "the time the player actually hears", and calibration measures the offset of that loop.

Design the calibration flow to finish within half a minute: use a steady metronome track, have the player tap along 8–16 times, drop the extremes and take the median (more resistant to slips than the mean), and after saving go straight into a short verification passage so the player can confirm judgment sits centered. Guide calibration on first launch, and keep a manual fine-tune slider and a "recalibrate" entry in the settings.

Common magnitudes of device difference:

| Chain | Extra latency magnitude | Handling |
| --- | --- | --- |
| Wired headphones | Minimal | The baseline case; default calibration is enough |
| Built-in speakers and ordinary speakers | A few to a few dozen milliseconds | Covered by calibration |
| Bluetooth and wireless headphones | Tens to hundreds of milliseconds, and it fluctuates | Prompt a switch to wired; allow calibration to cover it while disclosing the fluctuation |
| TVs and home theater | Tens to hundreds of milliseconds in the audio chain | Calibrate audio and picture separately |

Calibration values must follow the device: prompt a recalibration when the output device changes, and when offsets look abnormal suspect the environment first (Bluetooth, power-saving mode, system audio enhancements). Two disciplines: never fob everyone off with one global fixed offset — the device spread is wider than intuition suggests; and calibration only covers external latency — the code's own frame-alignment error must be fixed in the code first and never masked with the calibration value.

### 3.4 Gameplay Variants (Lane Counts, Key Layouts and Motion)

| Variant | Input | Judgment carrier | Best-fit scenario | Cost |
| --- | --- | --- | --- | --- |
| Lane-based falling notes (4–7 keys) | Keyboard, gamepad, arcade cabinet | Notes reaching the judgment line | Desktop and arcade; the strongest beatmap expressiveness | The more keys, the higher the reading load and practice cost |
| Multi-finger touchscreen | Thumbs and multi-touch | The judgment line or the touch instant | Mobile, in fragmented time | Finger occlusion and touch drift; a low density ceiling |
| Simplified, lane-free | Two keys (face and rim) | Drum-face zones | Arcade and home; the lowest barrier | A narrow expressive range, made up for by the song library and beatmap tricks |
| Free-pointing | Mouse or touchscreen | When icons appear and disappear | The PC community ecosystem | Judgment fairness and anti-cheat pressure |
| Motion and VR | Camera, controllers, headset | Motion trajectory and timing | Living rooms and showcase scenarios | Recognition latency and uncertainty; the judgment window must be widened |

Key counts come with physical constraints: keyboard play takes 4 keys as the baseline (both middle and index fingers), while 6- and 7-key layouts sit closer to a piano layout and cost more practice; mobile commonly runs 2–4 lanes (thumbs plus index fingers), and more runs into occlusion and hand-position conflicts. Motion projects split timing and amplitude into two scored items: motion repeats less precisely than fingers, so the judgment window widens accordingly, and staging position and camera guide the player's amplitude. One discipline: make one mode thoroughly good first. Multiple modes equal multiple beatmap systems, editor changes and testing costs — expand into them in a later phase, not at the design meeting.

## 4. Technical Essentials

**Clock and judgment**

- Use the audio clock as the master clock: input events carry high-precision timestamps, all converted to the audio playback position before judgment; never use frame time or system time as the judgment baseline.
- Hang judgment on input events (produce the result at the event's time), not on a per-frame scan; frame-rate jitter must never appear in judgment results.
- On many platforms the playback position query has an update granularity (per buffer block or render cycle); smooth and interpolate it — do not treat block-level jitter as the baseline.
- Low-latency playback is a means, not the goal: desktops use an exclusive or low-latency backend, mobile uses the low-latency audio path, and buffers commonly sit in the 10–30 ms magnitude; the fallback is still calibration and leniency — never make players tune the system buffer themselves.

**Input**

- Tune keyboards, gamepads and touchscreens per device with real measurements; touchscreens record touch-point timestamps and do multi-touch attribution; motion input gets its judgment window set from the device's measured latency; debounce and combo-protect input so one physical press yields exactly one judgment, and block system-level key repeat.

**Beatmaps and the toolchain**

- Store beatmap data in beats (musical time) with milliseconds as a derived value, and support BPM change points for tempo-variable tracks; ship the companion validator (overlaps, out-of-bounds, same-lane spacing below the window, unreachable combinations) that raises a warning on save.
- Replays and judgment logs: record input timestamps, judgment results and audio positions; window tuning and bug hunting both go by the log, not by memory.

**Performance and game feel**

- Pool note objects and batch their drawing, and render vertical scroll with subpixel or interpolated movement; avoid garbage-collection spikes and dropped frames — in this genre one lost frame is one judgment incident (playing by sight depends on smooth scrolling); set the frame-rate target by the lowest-spec target device, not by the dev machine.
- Hit feedback and hit sounds arrive on the same frame or the next; the timing relationship between hit sounds and the music needs deliberate design (aligned to accents or dotted on off-beats — never a smear).

**Multi-platform consistency**

- Reuse one calibration flow and data format across platforms; test on at least two real devices per platform before release.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for scope estimation; not a commitment.

| Project shape | Song library and beatmaps | Schedule magnitude | Notes |
| --- | --- | --- | --- |
| Judgment prototype | 1–2 tracks, 1 beatmap each | 2–4 weeks | No art; validates judgment, calibration and a minimal editor |
| Small complete title | 8–15 tracks, 2–3 difficulties each | 3–6 months | One visual theme; the library stays manageable |
| Typical indie title | 20–60 tracks, 3–5 difficulties each | 6 months to 2 years | The editor and beatmap pipeline dominate; library costs keep running |
| Live-ops form | 100+ tracks, continuously updated | 2+ years | Library updates are the content operation; licensing is a long race |

A single track's marginal cost has three parts: the licensing or commission fee, beatmap production (a first draft commonly takes half a day to two days, with testing and polish adding more than another 1×) and presentation art plus marketing assets. All three cost more than you expect, and "buy 50 tracks first" is the most expensive mistake.

The editor is a fixed investment: waveform, grid, note entry, audition, hot reload — commonly 2–6 weeks; without it, beatmap costs run out of control as the library grows. Spread the library's difficulty distribution across the target audience, keeping the beginner zone no lower than 30% of the total, or newcomers will not find a playable track in their first hour. Per-track art (cover, background, staging) quietly inflates easily — validate retention with a restrained approach first, then upgrade track by track. Schedule anchors: from zero to "trustworthy judgment, usable calibration, one playable track" usually takes 2–4 weeks; to a vertical slice (3–5 tracks, a working editor, handable to external testers) usually 2–3 months.

Song library and licensing (mandatory before greenlighting; for clause-by-clause checks see Legal, Patents & Competition):

- A track's rights usually split into two portions: the recording (master) and the composition (songwriting). The licence scope must cover at least worldwide, perpetual, any platform and editing rights, and spell out distribution rights for promotional materials, player livestreams and recorded gameplay.
- Settle the deliverables: master files, metadata (BPM, time signature, offset), whether stems are included, whether it is exclusive. Tracks missing metadata need manual annotation first — do not forget to count those hours.
- Write exit and renewal into the contract: licence expiry, takedown, renewal pricing and process, plus acceptance, revision counts and derivative-work limits for the three cooperation models — buyout, revenue share and commission; the item-by-item checklist is in Legal, Patents & Competition.

## 6. How to Start the First Prototype

The first prototype builds exactly one track, finished in 2–4 weeks, without touching the song library, story, store or accounts.

**Week 1: the judgment loop.** With a simple metronome track you recorded yourself or one with clean rights, implement falling-note judgment from 1 to 4 lanes; make the judgment window adjustable and the offset histogram visible; get the calibration screen working (tap along 8–16 times, take the median, verify). No art this week.

**Week 2: the minimal editor.** Waveform plus beat grid, note entry, instant audition, hot reload — produce the first beatmap you would hand to someone else to play; build the validator along the way, warning about same-lane spacing on save.

**Weeks 3–4: external testing and a calibration stress test.** Find 3–5 people (including 1–2 who have never played a rhythm game): watch whether the calibration flow can be completed without guidance, have each try once with different headphones and once on a different device, and record combo-break points and complaints. Only then chart a second and third beatmap, validating that the editor is not custom-built for one beatmap.

Success criteria (all observable):

- With all art and sound effects removed, testers still voluntarily play three or more tracks in a row.
- Calibration succeeds without guidance, testers can retell "what they were just doing", and they can rerun it themselves after switching devices.
- The judgment histogram is centered on zero with no obvious offset, and replaying the same passage under the same settings gives stable results.
- Testers can name the reason for failure ("I missed that beat") rather than "I don't know how it broke"; complaints of "I clearly hit it and it did not register" number zero per person.

If judgment and calibration miss the bar, stop and fix them inside the prototype; do not start laying out the song library and the art — rework on those two foundations is this genre's most expensive account.

## 7. Common Pitfalls

1. **Judging on frame time or system time**: game feel is good one moment and bad the next, with no findable cause. Judgment must hang on the audio clock (§4).
2. **No calibration, or no way to recalibrate**: shipping without calibration for wireless-headphone and home-theater setups means players blame the game for their device's latency — this genre's biggest source of bad reviews.
3. **Judgment windows conflicting with adjacent-note spacing**: one press qualifies for two notes and attribution is pure guesswork (§3.1).
4. **Treating the judgment window as a difficulty knob**: tightening the window manufactures anxiety, not depth; leave difficulty to the beatmaps.
5. **Judgment and feedback out of sync**: the hit registers visually but the sound lags, or hit sounds and judgments misalign, and the illusion of performing collapses on the spot.
6. **Buying the library first and settling gameplay later, or building the whole prototype around one track**: licensing and data formats both specialize in the wrong direction; prove "one track plays well" first, then talk volume.
7. **Gaps in licence scope**: trailers, store pages, player livestreams and recorded gameplay, and derivative edits each need their own rights coverage.
8. **Beatmaps that only pile on density**: an unreadable run means memorization, and "hard" is one line away from "unfair"; run the readability check before playtesting.
9. **Dropped frames and garbage-collection spikes**: in this genre one lost frame is one judgment incident; pooling and stable frame rates are hard requirements (§4).
10. **Only one difficulty**: newcomers cannot find a playable track in their first hour and experts hit the ceiling after two; the library's difficulty distribution is the retention structure itself.

## Further Reading

- Game Design Handbook: the general methods for core loops, feedback and scoring systems; corresponds to §3.
- Programming Handbook: audio clocks, input latency and performance engineering — the full expansion of §4.
- Art & Audio Handbook: audio design and implementation, loudness and loop-point specs — check its spec sheet before a track is delivered.
- Legal, Patents & Competition: music licensing, contracts and overseas compliance — read it through before greenlighting a song library.
- Level Design Handbook: difficulty curves and pacing design — the general methods for beatmaps as levels.
- Pitfalls & Anti-patterns: content-runaway and outsourcing pitfalls — read against §7.
- Homework: take a widely known rhythm game, run its latency calibration end to end, and record three things — how long the calibration flow took and how it measures (tap-along, or something else); play one round each with Bluetooth and wired headphones and note how far the judgment scores differ; pick one track's beginner and expert difficulties and write out the difference in their skeletons. Answer all three, then go build the judgment loop in §6.
