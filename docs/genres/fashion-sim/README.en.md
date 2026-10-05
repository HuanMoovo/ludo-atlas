# Ludo Atlas · Genre Handbooks · Fashion Sim

> **Genre Handbooks · Volume 4**. Positioning: the genre that makes "styling" its core verb. The theme sets the question, the wardrobe supplies the material, and the scoring grades the paper — wound together into a loop of "read the question, pick pieces, swap one piece and retry"; long-term drive comes from collecting, story and display. This page covers outfit scoring, wardrobe content and art costs, narrative integration, social display and monetization compliance.
> Companions: Game Design Handbook (core loops and scoring balance) · Art & Audio Handbook (clothing assets and outsourcing management) · Live-Ops & Growth (seasons, monetization and long-term cadence) · Legal, Patents & Competition (probability disclosure and content compliance).
> This page carries no external links; benchmarks are widely known works only, and the figures are common magnitudes — calibrate them against measurements in your own project.

---

## 1. Positioning and Core Loop

Fashion sim (in the Chinese market it is commonly called the "dress-up game") is one of the pillar genres of the female-oriented market: it started from the dress-up play of browser and early mobile titles, and the Nikki series (Nikki UP2U: World Traveller, Love Nikki and Shining Nikki, from 2013 onward) turned "collect clothes, style to clear stages" into a mobile top seller; on the handheld side there is the clothing-store and stock-selection play of the Style Savvy line, and the dress-up systems inside life sims are cousins from the same root. If you can dress yourself, you can play — there is almost no barrier to entry.

In one line: fashion sim is the genre that **makes styling the first-order pleasure**. Players use clothing as vocabulary and outfits as sentences, answering one question after another — "what do I wear to this occasion?"; the scoring system grades the paper, and the wardrobe supplies the vocabulary. Success rests on two things: scoring must be explainable (§3.1), and individual pieces must keep arriving (§3.2, §3.5); if either link drags, players shift from "I want to build one more outfit" to "I'll go look up a guide".

The core loop, written as a verb chain:

`read the brief (occasion and style) → browse the wardrobe → select and style → submit for scoring → change one piece per the feedback and retry → claim rewards and new pieces`

All three scales of the loop need payoff points: one styling session is measured in minutes, scored the moment you submit; one chapter is measured in hours, settled by a run of levels plus story progression; one season and one compendium are measured in weeks and months, closed out by collecting, contests and the season settlement.

Drawing boundaries against adjacent genres:

| Adjacent genre | Boundary |
| --- | --- |
| Life sim | There, dressing up is part of self-expression, with no scoring or levels; in fashion sim every outfit must pass a grading system |
| Dating sim | There, the main loop is advancing a relationship and clothing is only an item that moves affinity; fashion sim makes the clothing itself the main course |
| Management sim | Running a clothing store is about stock, pricing and foot traffic; fashion sim is about "does this outfit answer the question" — the business side is at most a side dish |
| Collect-and-raise games | There, collecting is compendium completion itself; in fashion sim every piece must be wearable, scorable and displayable — collecting is a means, not the end |

A self-check question: swap the clothing for furniture, pets or weapons — does the gameplay still hold? If the answer is "it still holds", what you are making is probably a collection-management game; if the answer is "it doesn't", what you are making is fashion sim.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Expression delivered**: satisfy "looks the way I imagined" first, "scores high" second; players will take a second look at their own finished outfit — that moment is the core appeal of the whole genre.
2. **Judgment you can explain**: a score must trace back to specific reasons (style mismatch, missing pieces, outfit completeness); change one piece along the feedback and the score moves — only then is scoring not a lottery.
3. **Wardrobe growth**: the collecting itch comes from "one more piece to go" and from "the new arrival unlocks a new solution"; the supply cadence on the free path decides long-term retention.
4. **A stage for display**: outfits must be seen; photo albums, contests and peer review give expression an epilogue — without display, collecting motivation halves.
5. **The pull of story**: occasions and motives come from the narrative (an interview, a banquet, a stage) — that is what makes scoring criteria meaningful and keeps levels from being pure score farming.

Benchmark titles (play them yourself before breaking them down; watch especially how scoring feedback explains itself and what players do when stuck):

| Title | What to learn |
| --- | --- |
| Shining Nikki | The engineering and staging spec of 3D dress-up; outfits as narrative units; the long-term structure of contests and seasons |
| Love Nikki | The scoring system and chapter progression of 2D dress-up levels; light text plus high-density clothing updates |
| Style Savvy | Turning "read the customer's needs" into core gameplay: the small loop of selecting, matching and presenting |
| The Sims 4 | Proof that dress-up works as self-expression: it holds without level scoring, and display and sharing can drive on their own |
| Animal Crossing: New Horizons | A lightweight model for clothing design and sharing: custom patterns and the gifting loop |

## 3. Design Essentials

### 3.1 Outfit Scoring Mechanics

The scoring system has to do two jobs at once: judge right from wrong, and teach the method. Its structure starts from three accounts:

`total score = base score (rarity) + fit score (tags times weights) + combo bonus (sets and series)`

- The base score lays a floor by rarity and returns the value of "owning";
- The fit score is the main account: each piece carries 2–4 style tags and values (6–10 master styles across the whole catalog), a level supplies a set of weights, and the two are multiplied and added;
- The combo bonus rewards "dressing completely": full sets, matching color families and matching series score lightly, encouraging a coordinated outfit rather than stacking one piece.

Design discipline: the fit score must take 60–80% of the total, so that "the right low-rarity piece" reliably beats "an expensive random pile"; fail that, and scoring degrades into a power comparison, with free players frustrated the whole way (§3.5).

The four-piece kit for a level's question: the occasion (write the scene in narrative language, as in "a class reunion — comfortable yet presentable"), the weights (multipliers for primary and secondary styles, as in simple ×3, fresh ×1.5, gorgeous ×0.5), the thresholds (clear / excellent / perfect, three tiers), and the feedback (an explanation beyond the score, as in "missing a clean top").

Three acceptance criteria:

1. **Feedback speaks plainly**: "An interview calls for dignity; this looks too casual" beats "elegance value insufficient"; number-minded players can optimize against the thresholds, and intuition players can guess the right direction from reading the question.
2. **No one-size-fits-all**: scan the wardrobe with a script across all levels; the top-scoring outfit in any two levels should overlap by no more than two or three pieces; when one outfit beats everything, adjust the weights or rotate the themes.
3. **Thresholds calibrated against the free-to-obtain wardrobe**: work the clear line backwards from the best free-path solution, leaving one or two tenths of headroom; paying buys faster and more complete, never the "only solution" (§3.5).

### 3.2 Wardrobe Content and Art

The wardrobe starts with slot taxonomy before output volume: head (hairstyle, makeup, headwear, earrings), torso (tops, bottoms, dresses, outerwear), limbs (socks, shoes, handwear, handhelds), atmosphere (backgrounds, effects, poses); start with 8–10 core slots, then add by production capacity — finer slots mean more combinations and higher cost.

The books on the 2D and 3D routes:

| Route | Per-piece content | Cost magnitude | The price |
| --- | --- | --- | --- |
| 2D variations | Each piece drawn as a layer over a uniform pose, sharing a base body | Half a day to two days per piece | Low freedom of motion and camera; change the pose and the whole set is redrawn |
| 3D models | Modeling, pattern-making, materials, rig fitting | Several days to two weeks per piece | The highest cost; clipping across layered cloth is long-term maintenance debt |
| Hybrid | The main body follows one route; staging and effects get separate layered treatment | Between the two | Freeze the spec as early as possible, or you rework on both ends |

Production discipline (for pipelines and outsourcing management see the Art & Audio Handbook):

- **New clothes must mix with the old**: run a mix-and-match spot check as each new piece enters the pipeline (sampling the combination matrix against catalog pieces); a one-off that only works within its own set was made for nothing.
- **Deliver in series**: each version or chapter produces one themed series as a batch, with a unified style and a matching copy set, so outsourced acceptance has a reference pack and samples.
- **Don't miss the by-products**: icon, compendium card, thumbnail, acquisition copy and try-on data — every piece comes with this whole set; miss one and you rework.
- **Establish the clothing chapter of the Art Bible first**: era, silhouette, palette, materials and subject boundaries written clearly, or the outsourced pieces will assemble like a sampler platter.

### 3.3 Narrative Integration

The fashion subject comes with scripts built in: a designer's rise, the road to top model, reviving a family brand, climbing a competition ladder — all suit a chapter structure of "one occasion per scene"; the flow is fixed as:

`story intro → 1 to 3 styling levels → story reaction (relationship progress and rewards) → new pieces and new hooks`

- **Level motivation comes from the story**: "you have an interview tomorrow" lets players understand the scoring criteria better than "level five"; the occasion description directly shapes how players read the question.
- **Scoring criteria and story demands must agree**: if the story says "plain and understated", scoring cannot hand high marks to the gorgeous — this is the most frequent spot where narrative and gameplay undercut each other (§7).
- **Clothing can be a relationship prop**: events where you save a friend in a pinch or pick clothes for a partner wire the wardrobe into social and romance lines (build the romance line to the standards of the matching genre handbook).
- **Budget text and staging separately**: dialogue, branches, portrait variants and voice are all additive costs; estimate them at visual-novel magnitudes before writing (estimation methods in the Production Handbook).
- **Long-term serialization**: the story serializes by version, with chapter themes aligned to outfit themes; one batch of clothes tells one story, and the story teases the next batch.

### 3.4 Social Features and Display

Display comes in four layers: for yourself (photo album, photo mode, one-tap output with frames and watermarks); peer review (themed contests, pairwise voting — anonymous, vote-limited, tier-matched); competition (leaderboards and seasons, with tiered rewards but no shaming of the losers); playing together (borrowing clothes from friends, co-op events and mini-games).

- **Keep rewards light**: a guaranteed participation prize, ranks split into tiers only — low-scoring outfits are treated kindly, so the urge to express does not turn into social pressure.
- **Fairness comes from mechanics**: anonymous entries, anti-vote-farming (vote limits plus server-side tallying), tier-matched pairing — newcomers never share a stage with veterans who own full wardrobes.
- **Scope UGC first**: custom dyeing, patterns and stickers lead; free drawing comes later; design and naming bring in moderation, copyright and minor-protection issues.
- **Sharing is growth**: share images carry watermarks and event tags — the cheapest organic traffic in this genre; build composition templates into photo mode; don't expect players to crop their own.

### 3.5 Monetization Structure and Compliance Boundaries

Monetization has four layers (for operating cadence and spend see Live-Ops & Growth); only the structure is given here — calibrate the numbers against your own retention and choke points:

- **Direct purchase**: individual pieces, full sets and bundles at clearly listed prices — the genre's word-of-mouth bedrock;
- **Monthly cards and battle passes**: daily resources plus wardrobe perks, carrying steady revenue and daily return visits;
- **Limited draws**: seasonal themed sets obtained by probability draw, structurally identical to the card pools of gacha RPGs: probability disclosure, pity and draw records follow the same standards (Legal, Patents & Competition; Live-Ops & Growth), and this page does not repeat them;
- **Stamina and tickets**: level consumption and recovery cadence regulate how fast content is consumed — set the parameters before setting the outputs.

One red line: main-line clear thresholds must be calibrated against the free-to-obtain wardrobe (§3.1); paying buys "more choices and a faster pace", never the "only solution"; if a paid-exclusive piece is the only solution, the scoring system becomes a toll booth (§7).

Compliance boundaries — walk through them at greenlight (each expanded in Legal, Patents & Competition and the Multi-platform Launch Playbook): probability-draw disclosure, pity and records; minor spending limits, real-name verification and playtime controls; marketing copy may not use absolute terms, and claims about looks or originality need substantiation; real brand marks, celebrity likenesses and fashion photography can all be protected subject matter — art reference is not usable material; UGC content must pass review, with minor-protection measures built alongside.

Ledger discipline: multiply per-piece pricing by content volume first; confirm it "sells back its cost" before opening a production line; the standards for this ledger and for operating metrics follow Live-Ops & Growth.

## 4. Technical Essentials

The engineering difficulty concentrates in three places: dress-up rendering, testable data and scoring, and wardrobe search plus saves; for general architecture see the Programming Handbook.

**Dress-up rendering**

- 2D route: anchor points and layer order need a written spec (each slot's texture origin goes into the asset spec; display order rules like "outerwear over the hem" go into a table); misalignment between combined pieces is 2D dress-up's most common accident; recolor via palettes and shaders, not redraws. Previews must open in a snap: preprocess thumbnails and atlases — never render the full outfit live at runtime.
- 3D route: skinning and cloth simulation, multi-body fitting, and a cloth toggle on mobile; build clipping detection into a tool (bounding-box spot checks plus a visual-inspection matrix of critical combinations) — fixing one piece and breaking three is the norm, and the detection pipeline is worth more than after-the-fact patches.

**Data-driven design and testable scoring**

- One row per piece: slot, tag vector, rarity, source, icon, compendium copy, live status; one row per level: weights, thresholds, copy, rewards; code only reads tables, and formulas live apart from tables. A sold asset cannot be deleted; retiring it only affects its acquisition entry point.
- The batch scoring script is the core tool: all levels × all wardrobe search, producing each level's top solution and distribution, rerun on every new release to keep new pieces from breaking old levels (§3.1); unit tests cover empty slots, duplicate pieces, extreme weights and borderline thresholds.

**Wardrobe UX and saves**

- Search experience at the thousand-piece scale is retention: filter by slot and tag, sort by color and recency, favorites, outfit presets, and a one-tap "generate a draft from the current level's weights" button.
- Save fields: ownership, favorites, presets, level progress and season data all serialized in full, with a version number and migration functions; for live-service titles, add server-side records of purchases and draws, server-side contest tallying, and share-image rendering specs.

## 5. Content Volume and Workload Reference

The following are common magnitudes for comparable projects, for scoping estimates; they are not a commitment.

| Project form | Clothing volume | Timeline magnitude | Notes |
| --- | --- | --- | --- |
| Mechanics prototype | 30–60 placeholder pieces | 2–4 weeks | Color blocks instead of art; validates scoring and the loop only |
| Small complete title | 200–400 pieces, with levels matched to chapters | 6–12 months | Art takes the lion's share; the story is produced in parallel |
| Long-running mobile product | 600+ pieces at launch, 60–120 per version | 1 year and up, with ongoing investment | Output capacity is locked to the operating cadence |
| High-spec 3D product | Thousands of pieces in total | Multiple years for a team | Clothing and staging are the cost body |

Per-piece costs and magnitude conclusions (rough measures; calibrate against your own): a 2D variation takes half a day to two days (drawing, layer separation, try-on, icon); a 3D piece takes several days to two weeks (modeling, materials, rig fitting, mix-and-match clipping tests); one styling level (weights, copy, thresholds, scan verification) takes half a day to two days; one story chapter (5–10 levels plus dialogue and staging) takes weeks. Clothing assets are usually the largest slice of the whole project's art budget (a common measure is over half; for pipelines see the Art & Audio Handbook) — work out capacity first (pieces per person per month), then set the content plan and update promises; capacity failing to match consumption is this genre's main accident, because players can burn through a month's output in a week; the cutting priority, first to last: reuse clothing (recolors of the same design, edits of the same model) > reduce staging specs > reduce story branches > shrink the compendium — clothing is the main course, so the knife goes there last.

## 6. How to Start the First Prototype

Goal: spend 2–4 weeks answering one question — can the loop of "pick clothes, score points" make someone voluntarily build another outfit; use color-block placeholders throughout, and draw no art.

1. **Week 1: the clothing skeleton**. 8–10 slots, 30–60 placeholder pieces (color block plus tags plus values), and one acquisition entry point (level rewards or a shop) so new clothes can reach the player.
2. **Week 2: scoring and levels**. One scoring formula (base score plus fit score), 5–8 levels (each with weights and three-tier thresholds), and explainable feedback copy; write a scan script alongside to check that the top solution is not the same outfit across levels.
3. **Week 3: close the loop and add a story shell**. Acquire → style → score → reward → acquire again; add 3–5 screens of dialogue to the first chapter to make the "occasion" clear, and watch whether players read the question.
4. **Week 4: playtest and tune**. Find 5 people who have never played; record only, prompt never: do they read the question, can they explain the score, do they swap one piece and retry after failing; note the spots where "stuck means quit".

Success criteria (all observable):

- Testers can explain the score in their own words ("this scene calls for elegance, and I dressed too casually") rather than "no idea why".
- With art and audio stripped out, testers will replay levels for the next piece of clothing, 30+ minutes in one sitting.
- Any two levels have different top configurations, and the scan script can verify this within 10 minutes.
- At least 3 of the 5 testers adjust their outfit on their own and retry after failing, and can say why.

Not during the prototype: 3D, cloth, social systems, gacha, real currency, localization; verify "is styling fun" first, then do the launch engineering.

## 7. Common Pitfalls

1. **Scoring is unexplainable**: players cannot tell where the score gap comes from, and gameplay degrades into guide-reading. How to avoid: feedback specific to tags and pieces, in the language of the occasion (§3.1).
2. **A single optimal solution**: one universal outfit beats every level, and collecting and styling lose their meaning at once. How to avoid: weight rotation plus solution-space scanning (§3.1).
3. **Rarity crushes styling**: high-rarity pieces dominate on raw numbers, scoring becomes a power comparison, and free players are frustrated. How to avoid: let the fit score take the lion's share; calibrate thresholds against the free wardrobe (§3.1, §3.5).
4. **Wardrobe search out of control**: past a thousand pieces, clothes can no longer be found. How to avoid: filters, favorites, one-tap drafts (§4).
5. **Clothing output collapse**: updates cannot keep up with consumption, and promised sets go missing. How to avoid: compute capacity before making promises; amortize costs with reuse and recolors (§5).
6. **Clothes with no stage**: no levels, story or display to use them in — the clothes have nowhere to go. How to avoid: give each batch of clothing a batch of uses; every release is an event (§3.3, §3.4).
7. **Clipping and fitting debt**: 3D clothing clips as soon as layers pile up. How to avoid: put detection tooling and combination-matrix spot checks into the pipeline (§4).
8. **A paywall in the way**: the main line's only solution is purchasable. How to avoid: "the free path can clear the game" is the red line; paying sells choices and pace (§3.5).
9. **Draw standards and social pressure**: undisclosed pity rates and public punishment for low scores both push well-disposed players away. How to avoid: the same disclosure rules as card pools; tiered rewards, anonymous peer review, and a prize for taking part (§3.4).

## Further Reading

- Game Design Handbook: core loops, number tables and feedback design — the drafting paper for §1 and §3.1.
- Art & Audio Handbook: clothing asset specs, outsourcing management and style acceptance — the full expansion of §3.2 and §5.
- Live-Ops & Growth: seasons, events and monetization cadence — the companion to §3.5; for probability disclosure standards see Legal, Patents & Competition; for the content-side pitfalls against §7 see Pitfalls & Anti-patterns.
- The Dating Sim and Life Sim pages in the Genre Handbooks: the boundaries and meeting points with adjacent genres; read before greenlight.
- Play, don't read: clear one chapter of Shining Nikki or Love Nikki and note how the scoring feedback explains itself and what your first reaction is when stuck; then feel out how Style Savvy turns "reading the customer" into gameplay.
- Homework: build a scoring model on a paper spreadsheet (10 pieces × 6 tags × 3 levels), compute each level's top outfit by hand, and check whether one set steamrolls them all; if so, fix the weights before writing code.
