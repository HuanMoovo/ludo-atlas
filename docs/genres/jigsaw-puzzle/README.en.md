# Ludo Atlas · Genre Handbooks · Jigsaw Puzzle

> **Genre Handbooks · Volume 4**. Positioning: the digital form of a tabletop category whose first pleasure is "restoring pieces into a whole picture". Players sort pieces using two kinds of clues, shape and pattern; there is no failure, no time limit, and you can stop at any moment; the image library and the feel of the pieces are the entire asset base. This page covers jigsaw feel, image-library production and licensing, difficulty and accessibility features, the relaxation positioning and mobile monetization structure, plus collaborative and daily variants.
> Companions: Game Design Handbook (core loops and difficulty tiers) · Art & Audio Handbook (image-library production and outsourcing management) · Live-Ops & Growth (ads, IAP and long-term content cadence) · Legal, Patents & Competition (image licensing and user-content compliance).
> This page carries no external links; the figures are typical magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

In Chinese, the word meaning "puzzle" does double duty: broadly it names the whole puzzle family, narrowly it refers to the jigsaw (assembling pieces back into a whole), and this page covers only the latter; for puzzle design, defer to the Puzzle page (Volume 1). The jigsaw began as an eighteenth-century European teaching tool (cut-up maps for geography lessons) and later evolved into a tabletop and casual product; the digital form keeps every action — finding pieces, placing them, restoring the picture — and adds conveniences the tabletop version lacks: deterministic snapping, automatic grouping, save anytime and a nearly unlimited image library.

In one line: the jigsaw puzzle is a genre **whose first pleasure is "restoration"**. Every piece has exactly one correct position, and every placement makes the picture one step more complete; the design work revolves around three things: snap feel (§3.1), the image library (§3.2), and the balance of difficulty and assistance (§3.3).

The core loop, written as a verb chain: `pick a picture and a tier → spread out the pieces → sort the edges → gather by region → snap into groups → fill in the rest → settle and collect`. It comes in three scales:

| Scale | The loop | What the player gets |
| --- | --- | --- |
| A single placement (1–3 seconds) | Find a piece → drag it close → it snaps if correct | One definite "that's it" |
| One puzzle (10 minutes to hours) | Sort edges → split into regions → gather → fill in | Visible progress as the picture is restored |
| One image library (weeks to months) | Finish a puzzle → settle and collect → pick the next | A growing collection and renewed freshness |

Three preconditions for the loop to hold: snapping must be deterministic (right is right, wrong never sticks, no gray zone); the cost of finding pieces must stay under control (most of the time goes into searching, and the tools decide the share); and progress must survive being saved at any moment (sessions in this category are interrupted constantly, and coming back must resume exactly where you left off). Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Puzzle | In puzzle games progress comes from reasoning; jigsaw does no reasoning — the answer is fully given up front — and progress comes from recognition and matching |
| Hidden-object | Both are visual casual games: hidden-object tests "finding", jigsaw tests "placing"; the former leans on scanning, the latter on comparing |
| Match-3 | Match-3 has a move budget and failure; jigsaw has no failure, and a time limit exists at most as an optional mode |
| Merge games | The pleasure of merging is combination and numeric growth; jigsaw's combination is restoration — no numbers, only completeness |

A self-check question: if you replaced the picture with a flat color, leaving only the shapes, would the game still hold up? If it holds but the fun drops a tier, then both pattern and shape are your content; now take away the certainty of snapping (nothing sticks wherever you drag, no response when placed correctly) and the gameplay collapses instantly — proof that the feel is the vital organ.

Team framing: light engineering, heavy content, with a shallow tech stack (drag-and-drop, snapping, saving, image-library management) and no physics, AI or networking (except for the online-multiplayer variant); premium and small-scale releases are common, the long-running mobile form is sustained by its update cadence, and the scarce skill is aesthetic judgment in, and procurement of, the image library. One-line conclusion: jigsaw does not sell gameplay — it sells the image library and comfort.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Definite progress**: a correct placement gives a clear receipt, players always know "I got it right", and no rules lecture is needed.
2. **Relaxation**: no failure, no time limit, stop anytime; its opponent is not difficulty but pressure — jigsaw is one of the rare categories you can play while listening to a podcast (§3.4).
3. **Tactile game feel**: the magnetic pull of a snap, its sound and its settle are the core currency of satisfaction, polished until players "cannot resist placing one more piece" (§3.1).
4. **Progress visible to the naked eye**: edges finished, regions connected, the endgame closing in — the picture itself is the progress bar.
5. **Low-cost assistance**: there is a way out when stuck, and using help carries no penalty and no shame (§3.3).

Negative feelings (any one of these is a red flag): unable to find a piece and unable to find a way out; dragging into place with no response, or snapping crooked for no reason; quitting mid-way and losing all progress; a repetitive, monotonous library. Benchmarks and product forms (no names needed — break down one sample per form, methods in Case Studies):

| Form | What to learn |
| --- | --- |
| Classic PC/web jigsaw (premium collection) | The image library and piece-count tiers are the content itself; one image serves several difficulty tiers; the interface is templated so cost concentrates in the library |
| Mobile relaxation-focused jigsaw | One-handed play, an auto-grouping tray, quiet audiovisual presentation; session design built around "close it and reopen it anytime" |
| Daily jigsaw (same puzzle for everyone) | A daily ritual traded for return visits: light content at a fixed time, streaks and sharing; for share design, cross-read with the Word Game page (Volume 3) |
| Collaborative multiplayer jigsaw | Moving the household activity of a family around one table onto screens: dividing regions, same-screen or online sync, merging progress |
| Instant-play jigsaw on mini-game platforms | Low-friction distribution with ad-based returns; library rotation and loading strategy set the ceiling of the experience |

Three shared traits: the core asset is the library, not the mechanics (there is little room to vary mechanics; freshness comes from images); difficulty is modularized through piece count (the same image runs from 12 pieces to 1,000); and long-term return visits depend on content cadence (daily and seasonal packs) — without it, there is no reason to come back.

## 3. Design Essentials

### 3.1 Jigsaw Feel: Snapping, Rotation, Grouping, Edges First

| Component | Approach | Design stance |
| --- | --- | --- |
| Snapping | Drag near the correct adjacent slot and the piece settles automatically | Snap only on "correct adjacency", never bond in wrong positions; this eliminates the most expensive mistake of physical jigsaws: a whole region assembled wrongly has to be broken apart and rebuilt |
| Rotation | Pieces carry an angle and only snap once turned upright | Off by default, offered as a difficulty option; when enabled, add angle snapping (a near-correct angle auto-corrects), keep the interaction to single gestures like tapping to rotate by a fixed step, and provide one-button snap-to-upright as a fallback |
| Grouping | Two correctly adjacent pieces bond into one unit that drags as a whole, and groups keep snapping together and merging | The biggest game-feel dividend of digital over physical jigsaws; it is mandatory and must be smooth: lift the whole group, snap the whole group, settle with a single sound |
| Edges first | Sorting edge pieces or a one-tap edge picker | People naturally do the edges first — the smoothest opening path, and a wordless tutorial (for teaching discipline, cross-read the Puzzle page (Volume 1)) |

- Grab, drag and tray: on pickup, scale up slightly and add shadow and a sense of lift; while dragging, keep the piece's center a little above the touch point; when released without a snap, leave it where it is — never bounce it back to the tray; snap tolerance is measured as a fraction of the piece's edge length, wider on touchscreens than with a mouse, and goes into the config table for calibration per tier and device; the loose-piece tray sorts by color and shape, while "show me where a piece is" belongs to the hint layer (§3.3) and is counted separately from the basic tools.
- The snap-feedback trio: a magnetic pull animation of a few dozen milliseconds, a settle sound (its timbre varying by region or progress), and small particles or a highlight — all three on the same beat; a late or missing snap response makes the feel go floaty instantly.

Game-feel acceptance: have 5 people each assemble puzzles of 24 to 100 pieces, and log the counts of "dragging lagged behind", "placed correctly but nothing happened" and "the snap could not be felt" — all should be near zero; then look at the share of session time spent finding pieces — over half means the loose-piece management tools are not up to the job.

### 3.2 Image-Library Content and Licensing

- The library is the content itself: on a jigsaw product's asset sheet, the library is the first line; serving one image at several piece-count tiers is the core lever for spreading cost, and library size determines the reserve of "one puzzle after another" freshness. Subject matrix (common mix): travel landscapes, animals and nature, city architecture, famous paintings, illustrated picture books, flowers and still life, seasons and holidays, abstract gradients; calibrate each subject's share to your audience — for a long-running platform, breadth first, and never bet heavily on a single subject.
- Four routes for image sources, ordered from lowest to highest rights pressure:
  - Commissioned work and in-house art (the cleanest rights, the highest per-image cost), plus open assets and the public domain (famous paintings, public-domain photography, openly licensed libraries — check the terms for every image; a "painting" and a photograph of it may each carry separate rights);
  - Stock-library purchases: the terms often impose extra restrictions on "redistributing images as a product's core content" — never assume that buying means you can use it;
  - User-uploaded photos: a common feature of custom jigsaws with the heaviest privacy and moderation burden; run the agreement and storage past Legal, Patents & Competition first.
- Licensing ledger and red lines: one record per image (source, rights holder, licensing scope and term, attribution requirements, path to supporting documents); never use material whose source cannot be found; stay away from film, anime, game characters, celebrity photos and brand marks — fan works are equally off-limits — and for material containing people, mind likeness rights.
- Art acceptance specific to jigsaw: detail density must be even across the picture — large flat areas (sky, water) offer no clues, while over-dense regions offer no entry point; the acceptance move is to shrink the image to target size, point at five random spots, and confirm each has recognizable pattern clues.

### 3.3 Difficulty System and Assistance Features

There are only four difficulty knobs: piece count, shape (standard grid or irregular), rotation on/off, and time limit on/off; change only one at a time.

| Tier | Piece count (typical) | Default assistance | Aimed at |
| --- | --- | --- | --- |
| Starter | 12–48 | Ghost image and edge sorting fully on | New and younger players |
| Regular | 100–192 | Reference image always visible, ghost optional | Mainstream relaxation |
| Challenge | 300–500 | Reference image optional, ghost optional | Experienced players |
| Hardcore | 500–1,000 and up | No preview, no ghost; voluntary extra hardship allowed | Core players |

- Piece count and time magnitudes: common tiers double each step (12/24/48/96/192) or use round, memorable numbers (100/300/500/1000), and serving 3 to 6 tiers for one image is normal; including searching and hesitating, a piece averages tens of seconds, so 100 pieces commonly runs half an hour to an hour, and 1,000 pieces is a multi-hour project at minimum (§5).
- Assistance feature list (all basic items are free, and using them deducts no points, no stars and leaves no record):
  - Reference image and ghost image: the original can be shown persistently and zoomed, and the board can faintly display the picture's outline — the latter is a lifesaver at large tiers and in flat-color regions;
  - Region and loose-piece tools: partition the picture into zones and focus one at a time; sort loose pieces by color or shape, pick out edges with one tap, page through the tray;
  - Tiered hints: tier A points out a piece's rough destination region, tier B places it directly in its correct position; a limited number are free, and beyond that they are topped up with rewarded video or IAP (§3.4) — the entry point is a pressure valve, not a fine notice;
  - Accessibility: two-step tapping as an alternative to dragging (motor impairments), piece-edge outlines and a high-contrast mode (low vision and color-vision differences), and text and button sizes that meet standards.
- Time limits and timers: if you want pressure for experienced players, build a separate mode with leaderboards — do not let it intrude on the main line; making the default experience timed turns a relaxation category into an exam.

### 3.4 The Relaxation Positioning and Mobile Monetization Structure

The relaxation positioning starts with hard constraints: no failure, no punishment, no forced time limit, and sessions that can be interrupted at any moment and resumed seamlessly; monetization for a long-running mobile product is made of four layers, whose proportions and order vary by product — calibrate the numbers against your own retention and friction data (methods in Live-Ops & Growth):

- Library payments: themed packs (landscapes, holidays, collaborations), subscription membership (unlimited library), and single-image purchases; the free path must guarantee there is always something to play, while paying buys faster updates and subject matter better suited to taste.
- Ads: rewarded video in exchange for hints, previews and the day's new image; interstitials go after the completion summary; one red line — never interrupt while the player is assembling; the moment of completion and serialized jigsaws are the most valuable attention in the whole category.
- Hint and assistance IAP: hint packs, auto-finishing the endgame, ad removal; the free path must have substitutes (limited hints, wait-to-restore), and paying buys faster, easier play.
- Custom photos: importing your own photo to generate a jigsaw, usually a premium feature; privacy, storage and content-moderation duties come with it (§3.2; Legal, Patents & Competition).
- Premium comparison and discipline: on PC and web, premium collections or DLC packs are common, and the difference lies in the update promise — subscriptions and serialized content need production capacity behind them; watch single-puzzle completion rate and next-puzzle start rate in the data; pressure-based monetization (time pressure, progress wipes, shaming assistance) shatters the positioning and the word of mouth — the rule is "pay for love, not for anxiety".

### 3.5 Variants

| Variant | Core change | Engineering and design points | Where it fits |
| --- | --- | --- | --- |
| Daily jigsaw | Same puzzle for all players, fixed time window (typically one day), shareable on completion | A very light server side (the puzzle and the results), share-image generation, streaks and a history page | Return visits and light social play |
| Collaborative jigsaw (same screen) | One device, assembled together or in turns | Multi-pointer drag conflicts (two people grabbing the same piece), merging progress | Families and offline gatherings |
| Collaborative jigsaw (online) | Several players dividing the work or assembling together on one picture | Authoritative state, piece locking with timeout release, reconnection; engineering rises to the level of a small online game | Friends and social play |
| Jigsaw plus long-term goals | Puzzles produce resources that drive decoration, collection or story | Modeled on the match-3-plus-decoration loop; content accounting schedules two pipelines | Long-running mobile products |

Discipline: the main line keeps only one thing — "quietly finishing a picture" — and variants are supplements to the reason for returning; collaboration and daily are the two most common add-ons, and neither is engineering-heavy except online collaboration; manage the daily puzzle bank and the library schedule together, stock seasonal images one cycle ahead, and a single missed day breaks every streak.

## 4. Technical Essentials

The tech stack is shallow, with no physics and no AI; the difficulty concentrates in four things — piece data, drag-and-drop interaction, saving and the image pipeline — and everything below is engine-agnostic.

- **Pieces and snapping**: each piece carries a data record (image-source ID, row and column index, position and angle, owning group ID); "correct" is decided by row/column adjacency, never by pixel comparison; rendering takes a sub-region of the full image plus a piece-shaped mask, so there is no need to pre-cut thumbnails; the snap test looks at "the dragged piece against the edge slots of existing pieces or groups", grouping uses union-find, and group snapping, group dragging and the completion test of "only one set remains" all fall out of the same structure.
- **Drag-and-drop and interaction**: calibrate touchscreen, mouse and gamepad separately (wider tolerance and grab radius on touch), and keep drag-follow latency to one or two frames; the pick-up, drag, drop three-phase state machine must be clean, and a lost touch counts as "dropped without snapping"; a two-step tap path (select a piece, then tap the target) must exist; when the board overflows the screen, offer zoom and pan — and piece dragging takes priority over panning the view.
- **Saving and recovery**: save on every snap (position, angle, owning group and assistance toggles all go into the file); the OS can kill a session at any moment, so save granularity is the experience's floor; pieces are bound to the image-source ID, so old saves can upgrade as long as the image is unchanged; cloud saves (if you build them) work by "taking the union of placed pieces and merging groups through union-find" — never by overwriting whole files.
- **Library pipeline and loading**: make the library catalog data-driven (each image carries subject tags, a licensing-record ID, available tiers and unlock conditions, so operations can add images without code changes); previews, the board and pieces pull different resolutions per tier, and image sources must cover the highest tier; cut templates (standard grid, irregular edges, fully irregular) are shape-difficulty assets.
- **Testability**: the minimal telemetry set is per-puzzle completion rate and time, quit points, assistance and hint usage counts, and next-puzzle start rate; a developer test tier must be able to jump in one tap to "N pieces left" and to a fully loaded loose-piece state, or the endgame experience and performance cannot be tested at all.

## 5. Content Volume and Workload Reference

The following are typical magnitudes, for estimating scope; not a commitment.

| Project form | Content volume | Time reference | Notes |
| --- | --- | --- | --- |
| Mechanics prototype | 5–10 images (open assets) | 2–4 weeks | Validates only snapping, grouping and saving |
| Small premium title | 50–150 images with multiple tiers | 3–6 months | Library procurement is the main cost |
| Long-running mobile product | 100+ images at launch, continuously updated | Ongoing investment | Library capacity and update cadence are bound together |
| Online collaborative product | Library needs halve, engineering doubles | Mid-size project tier | Online play is the bulk of the engineering |

Conversion rates:

- The library account is the main account: estimated at the typical magnitude of a few hundred to a few thousand yuan per commissioned illustration, or a few dozen to a few hundred yuan per stock-library license, a 100-image starter library is a procurement in the tens of thousands of yuan; serving 3 to 6 tiers per image spreads the cost, large tiers demand higher-resolution sources, and you should pick images by the highest tier when buying.
- Scheduling and scope discipline: mechanics and tools take 2–6 weeks, and launch timing is decided linearly by "how many images per week" your capacity adds — the bottleneck is procurement and curation, not code; subject breadth can start narrow, but clean licensing is non-negotiable — one infringing image can get your product taken down.

## 6. How to Start the First Prototype

Goal: answer one question in 2–4 weeks — when a finger drags a piece close to its correct position, can that one snap make someone want to place a second piece? Use open assets; buy no library.

1. **Week 1: drag-and-drop and snapping.** One board and one image of 12–24 pieces; implement pickup, dragging, correct-adjacency snapping and settle feedback. It is supposed to be ugly.
2. **Week 2: grouping and loose-piece management.** Two pieces bonding into a group, groups dragging and snapping together, one-tap edge picking, a sortable loose-piece tray; make saving happen on every operation, and verify recovery by killing the process over and over.
3. **Week 3: assistance and difficulty tiers.** Reference image, ghost image, region focus; add two difficulty tiers (24 and 96) for comparison testing.
4. **Week 4: blind testing and wrap-up.** Have 3 to 5 people each assemble two puzzles; record and stay silent: completion time, share of time spent searching, when they want to give up, and whether they ask for the next puzzle on their own; then add the completion presentation and the hand-off to "the next puzzle".

Success criteria (all observable):

- Testers start dragging the first piece without being taught, and most pick the edges first on their own.
- No one gives up because of "drag not responding" or "snapping not working"; completion times fall within the magnitudes of §3.3.
- At least half the testers ask for the next puzzle after finishing; killing the process and reopening loses no progress; changing one snap-tolerance parameter can be verified on a real device within 5 minutes.

If the prototype fails acceptance, do not buy a library: the library is this genre's single most expensive purchase, and if the feel does not hold, no number of images can save it.

## 7. Common Pitfalls

1. **Snapping judged by pixels**: pieces snap crooked in same-color regions, or fail to snap when they should; let row/column adjacency decide correctness instead (§4).
2. **Half-finished grouping**: groups drag but fall apart when released, and group snapping waterfalls piece by piece; this is the core dividend over physical jigsaws, and doing it poorly wastes the whole effort (§3.1).
3. **Progress not saved**: an incoming call or a killed process wipes it; sessions in this category are interrupted constantly, so saving is not a feature but a floor (§4).
4. **Shaming the assistance**: hints cost stars, cost money or demand long ads; under a relaxation positioning, punishing assistance manufactures frustration (§3.3).
5. **Vague licensing**: shipping commercially with "images found online" is infringement; every image needs a licensing ledger entry (§3.2; Legal, Patents & Competition).
6. **Monotonous subjects**: a hundred landscapes in the same style wear thin by the tenth puzzle; subject breadth is a long-running product's source of freshness (§3.2).
7. **Starting tiers too large**: defaulting to 1,000 pieces shuts mainstream users out; start at 12 pieces (§3.3).
8. **Time limits intruding on the main line**: timed by default with timeout penalties turns a relaxation category into an exam (§3.4).
9. **Image and source not matching the game**: large flat areas, over-dense detail, edges the same color as the background, or resolution that cannot support large tiers; give commissioned work "jigsaw legibility" acceptance criteria (§3.2, §4).
10. **Daily puzzle gaps**: you promise a puzzle every day, one missed day breaks streaks and hurts word of mouth; stock up images before the holidays (§3.5).

## Further Reading

- Game Design Handbook: core loops, difficulty tiers and feedback design — the base document for §3.1 and §3.3.
- Art & Audio Handbook: image-library production, outsourcing management and acceptance workflows — the full expansion of §3.2.
- Live-Ops & Growth: the framing for ads, IAP and long-term content cadence — the companion to §3.4 and §5.
- Legal, Patents & Competition: compliance framing for image licensing, user content and likeness rights — the complete expansion of §3.2.
- Genre Handbooks · Puzzle (Volume 1): the sister page; jigsaw does no reasoning and leans on recognition and matching — for boundary comparison see §1.
- Genre Handbooks · Word Game (Volume 3): a comparison sample for daily puzzles and share design — see §3.5.
- Exercise: take an existing photo, cut it into 24 pieces in your engine, and build only four things — drag-and-drop, snapping, grouping and saving — then assemble it once yourself and once with family; when it can keep someone seated to the end, talk about buying a library.
