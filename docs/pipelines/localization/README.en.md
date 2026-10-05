# Ludo Atlas · Pipelines · Localization

> **Pipelines & Workflows**. Positioning: the complete workflow that carries a game from source-language-only to shippable in many languages, covering text extraction and key conventions, translation and backfill, translation memory and glossaries, fonts and typography, testing and acceptance, and platform and store language metadata.
> Companions: Programming Handbook · Production Handbook · Multi-platform Launch Playbook · Pitfalls & Anti-patterns.

---

## 1. Positioning and Applicability

Localization is not "translating the text once" — it is a pipeline that hangs off the project from kickoff to after launch. It governs five layers: UI and system text, narrative and dialogue text, fonts and typography, text embedded in textures, and store and platform language metadata. Miss any one layer and players of the corresponding language will notice immediately.

The level of investment is set by two variables: text volume determines cost, and context dependence sets the quality floor. The larger the text volume and the heavier the context dependence, the closer localization comes to a rewrite rather than a replacement.

| Project shape | Text volume | Localization strategy |
| --- | --- | --- |
| Light text (action, arcade, casual) | Thousands of characters | UI and the store page first; a language pack can cover it in one or two weeks |
| Medium (simulation, strategy, card games) | Tens of thousands of characters | Engine string system plus a translation platform; proceed in batches, language by language |
| Text-heavy (narrative, RPG, visual novel) | Hundreds of thousands of characters | The full pipeline: glossary, translation memory, outsourcing and LQA all in place |

If any one of these three preconditions fails to hold, hold off on adding languages:

- The source text is stable; keys and structure have been frozen through at least one round. Translating while writing suits incremental additions, not the primary launch languages.
- All text runs through the engine's string system; no hardcoding, no concatenated sentences.
- There is an explicit language priority and budget: which languages come first and what bar each is held to at acceptance, written into the schedule.

The language ladder (a common order): source language and English as the base, then ordered by store data — French, German, Spanish, Italian; Simplified and Traditional Chinese; Japanese and Korean; Portuguese, Russian, Polish. Each added language multiplies cost: translation, proofreading, LQA, fonts and image text each count once more.

Cost basis (for range estimates, not a quotation):

| Item | Billing basis | Order-of-magnitude intuition |
| --- | --- | --- |
| Translation | By source characters or words | Thousands of characters: hours; hundreds of thousands: months |
| Proofreading and LQA | By the hour, or as a share of translation volume | Commonly 30–60% of translation cost |
| Fonts | Licensed per language | Commercial CJK fonts are a fixed licensing fee |
| Image text | Per image | Every UI image and promo image containing text is billed separately |

## 2. Toolchain

Selection revolves around four actions: export, collaboration, backfill, validation. Choose tools by action, not by brand.

| Area | Tool category | Representative options | Selection points |
| --- | --- | --- | --- |
| Source text management | Engine string systems | Unity Localization, Unreal String Table, Godot translation resources, Ren'Py translate | Runtime language switching, plural and variable support, bulk export/import |
| Translation collaboration | Translation platforms | Crowdin, Lokalise, Weblate, Transifex, Phrase | Translation memory, glossary, context screenshots, review workflow, API |
| Exchange formats | Spreadsheets and standard formats | CSV, PO, XLIFF, JSON | Fixed column conventions, diffable, verifiable by scripts |
| MT assistance | MT engines and language models | General-purpose MT and mainstream LLMs | Terms can be preloaded, batchable; for boundaries see the AI Workflows Handbook |
| Fonts | Fonts and subsetting tools | Commercial and open-source CJK fonts, subsetting scripts | Commercial licensing, character coverage, fallback chain configuration |
| Validation | Pseudo-localization and static checks | Engine built-in flows, purpose-built scripts | Surface missing keys, placeholders and overlong text in one sweep |

Three disciplines:

- The single source of truth is the repository: source text lives in version control and the translation platform is only a collaboration copy; a version that was changed in the platform but is missing from the repository must never exist.
- Format priority: engine-native export first, standard formats only when it falls short; if you use a purpose-built format you must build your own validation scripts, or backfill turns into a manual accident.
- The first milestone is not "finished translating" but export, backfill and validation running automatically end to end.

## 3. Process and Conventions

The main line has six steps; the output of each is the input to the next:

1. Extraction: export a keyed batch of text from the engine.
2. Freeze: within a batch the keys are frozen — additions only, no edits; changes flag the affected segments.
3. Translation and proofreading: translators translate, proofreaders review, native speakers spot-check.
4. Backfill: translations are imported into the engine and language packs are generated per language.
5. Integration testing: all-language smoke runs, pseudo-localization and screenshot review.
6. Release and increments: ship with the version; new content goes through a new batch.

### 3.1 Text Extraction and Key Conventions

- Extraction is triggered by a content batch freeze, not by someone remembering to export. Every batch maps to a version number and is traceable end to end.
- One key-naming rule holds across the whole project; the recommended structure is `module.scene.number`, e.g. `ui.menu.start`, `dialogue.ch03.scene02.line07`.
- Keys must be stable: a published key is never renamed. A rename equals a delete plus an add, and the alignment of every language and the translation memory break together.
- Never use source text as a key: change the source and every translation loses its link.
- Minimum columns of the export sheet: key, source text, translation, context note, length limit, status, batch number. Notes spell out the speaker, the scene and the tone, plus the call made where one term has several senses.
- One key, one sentence: text with variables, plurals and gender is expressed with placeholders and the engine's plural system; do not split a sentence into fragment keys and stitch them together.
- Register text embedded in textures in the same pass: UI images, logos and tutorial images containing text go on an image-text list, complete as of the extraction stage.

### 3.2 Translation Decisions: Human, MT, Hybrid

The three modes can mix within one pipeline, but they must be layered by language and by content:

| Mode | Method | Quality | Cost | Where it fits |
| --- | --- | --- | --- | --- |
| Human translation | Translators translate, proofreaders review, LQA spot-checks | Highest | Highest | Primary launch languages, critical narrative |
| Hybrid | MT first draft plus human proofreading and polish | Upper-middle | Medium | Long-tail languages, system and UI text |
| Raw MT | Machine output straight into the build | Unstable | Lowest | Internal validation only, never as a shipping language |

- MT is positioned as a first-draft tool, not a finished product: terminology and tone must pass human review, and jokes, puns and cultural references never go through raw MT. For boundaries and the verification process, see the AI Workflows Handbook.
- Test-translate each language first: one terminology-dense passage, one colloquial passage, one variable-bearing passage and one length-constrained passage; scale up only after they pass acceptance.
- Three quality gates: translation and proofreading are separate roles, the project side runs consistency validation, and native-speaker LQA spot-checks the finished product.
- Languages can be tiered: human translation for primary launch languages, the hybrid mode for the long tail; put languages the data does not support on a watch list rather than padding the language count.
- Set the style guide before work starts: tone, forms of address, honorifics, punctuation and number formats. Rework caused by translators each doing their own thing is localization's most expensive hidden bill.

### 3.3 Translation Memory and Glossaries

- Translation memory (TM) is a repository of segment pairs: maintained per project and per language pair, it suggests translations for similar sentences automatically. The higher the reuse rate, the lower the cost and the better the consistency.
- Entry discipline: only proofread sentences are stored; MT drafts do not enter automatically, or the errors are inherited by every batch of translation that follows.
- The glossary governs three kinds of terms: proper nouns (names, places, move names, items), system terms (skills, stats, mechanics) and forbidden terms (platform-sensitive words and brand taboos).
- Minimum field set: source term, target translation, part of speech, capitalization rule, forbidden renderings, notes.
- Maintenance discipline: the glossary has exactly one owner; changing one term means re-checking translations across the whole project; new terms are registered before use.

| Asset | Contents | When maintained | Common failure |
| --- | --- | --- | --- |
| Glossary | Source terms, renderings, forbidden renderings, notes | At kickoff and with every new batch | One noun ends up with three names |
| Translation memory | Proofread segment pairs and metadata | Harvested from every batch | Unproofread MT enters the store and pollutes later batches |
| Style guide | Tone, forms of address, punctuation, number formats | Before work starts on each language | Translators' styles diverge; the result reads like a patchwork |

### 3.4 Backfill and Language Pack Versions

- Backfill only imports; it does not change structure: translations are imported key-aligned; any hand-editing of import files is lost with the next batch.
- Integrity checks: one pack per language, checked for missing keys, extra keys and stale keys (source text changed without re-translation).
- Missing-key fallback needs a strategy: showing the source-language text beats showing the key name; test the fallback path on every kind of UI control.
- Versions stay traceable: translation batches map to version tags; any release build can answer "which batch of translations went into this pack."
- Smoke-test right after backfill: boot, main menu, core loop, save/load and settings, once through per language.

### 3.5 Fonts and Typography

- The CJK font bill: glyphs number in the tens of thousands and font files are large; subset static text to the characters used, while player input and user-generated content must keep the full character set or a fallback chain.
- Licensing comes before purchase: confirm commercial licensing for every font, language by language, and archive the proof; check versions and terms even for open-source fonts.
- Fallback chain: fall back to a secondary font when the primary font lacks a glyph; sweep each language with a test string containing rare characters, special symbols and full-width punctuation.
- Typography rules: line height, letter spacing, punctuation prohibitions (no closing punctuation at the start of a line, etc.) and mixed CJK/Latin/numeric spacing go into the UI spec, not into tacit agreement.
- Truncation and adaptivity: reserve UI width for the longest language (start from a 30–60% margin over the source language); use auto-width or wrapping for buttons and labels; critical buttons must never truncate.
- Text overflow: dialogue and description text gets scrolling or pagination; pseudo-localization with 30–40% expansion is the baseline test condition.

### 3.6 Platform and Store Language Metadata

- Steam: the store language list splits into Interface, Subtitles and Full Audio; each must match what the game actually provides; whether the store description, achievements and cloud save names are covered is registered separately.
- Consoles: certification has checklist requirements for languages and regional content; prepare according to the platform's developer documentation; verify voice/subtitle separation clauses up front — do not discover a gap at the certification stage.
- Mobile and web stores: store listings, screenshots and update notes are all metadata; in-app language following the system language is a common expectation.
- Marketing material gets localized in the same pass: trailer subtitles, text embedded in promo art and event announcements go on the same list.
- Tick the store language list only for genuinely supported languages; changes must be scheduled into the release plan — backends take review time, and remembering on launch day will definitely cost you.

## 4. Automation and Acceptance

### 4.1 Automated Checks

| Check | What it looks for | Stage it serves |
| --- | --- | --- |
| Key consistency | Missing, extra and stale keys (source changed, not re-translated) | Backfill and integration |
| Placeholder consistency | Each language's placeholder set matches the source; rich-text tags are closed | Backfill |
| Length warnings | Keys with a declared length limit raise a warning when the translation exceeds it | Integration |
| Pseudo-localization build | A lengthened pseudo-localization pack generated on every commit | Day-to-day development |
| Terminology check | Forbidden renderings and translations that drift from the glossary | Before every batch delivery |

- Automation catches mechanical errors only; tone and quality are left to proofreaders and LQA; run the checks automatically after every language pack change, and send warnings to the bug tracker rather than leaving them unhandled in a log.

### 4.2 Testing Methods

- Pseudo-localization: replace source text with mock text expanded by 30–40% and salted with accents and special characters, exposing truncation, overflow and font problems early.
- Image-text sweep: run screenshots across the whole flow and check screen by screen whether text inside textures is on the list and translated.
- Language pack integrity: a full-playthrough smoke test per language, covering boot, tutorial, the core loop, saves, error prompts and settings.
- Native-speaker LQA: sample the main flow and critical text; record issues by category (mistranslation, tone, terminology, truncation, punctuation).
- Regression discipline: re-run the screenshot sweep after changing fonts, changing UI layout or adding text; truncation and overflow come back after every layout change.

### 4.3 Release Acceptance Checklist (per language)

- Key coverage at 100%, with the fallback strategy confirmed.
- All-language smoke tests pass; no blocking text defects.
- Pseudo-localization and test strings: no unrecorded truncation, overflow or missing glyphs.
- The image-text list is fully ticked off.
- Glossary and forbidden-term checks pass.
- Font licensing proof is archived.
- The store language list is verified item by item against actual in-game support.
- Open issues are on record, to be collected in a version update.

## 5. Common Pitfalls

1. **Hardcoded text**: strings baked into code and prefabs get missed by extraction and leak source text in some language. Avoid it: route all text through the string system and back it with static checks.
2. **String concatenation**: "You received" + number + "gold coins" assembled into a sentence comes out wrong in every language with a different word order. Avoid it: whole-sentence keys with placeholders; no fragment stitching.
3. **Missing context**: the same word means different things in different scenes, and the translator can only guess. Avoid it: exports always carry context notes and screenshots.
4. **Forgetting to test fonts and truncation**: the default font lacks glyphs and buttons overflow, so long languages collapse all at once. Avoid it: bring test strings, pseudo-localization and native-speaker testing together.
5. **Localizing at the finish line**: work starts a month before release while text is still moving, and every translation falls out of line. Avoid it: batch freezes and incremental translation — treat localization as a pipeline, not a final assembly step.
6. **Using source text as keys**: change the source and every language loses its link. Avoid it: stable key names; decouple keys from copy.
7. **Terminology drift**: one skill under three names. Avoid it: a glossary plus project-wide re-checks, and a mechanical scan before delivery.
8. **MT polluting the translation memory**: unproofread drafts enter the store and errors are inherited batch after batch. Avoid it: store proofread output only.
9. **Mistranslated placeholders**: a translator translates or deletes a variable name, causing runtime errors or text with missing arguments. Avoid it: automated validation plus a translator briefing.
10. **Missed image text**: text in promo images, tutorial images and textures never made it onto the list. Avoid it: build the list at the extraction stage and close the loop with the screenshot sweep.
11. **Random store language ticks**: the listing claims support the game lacks, earning bad reviews and complaints. Avoid it: verify item by item before release; fewer and true beats padded and false.
12. **Font copyright accidents**: unlicensed commercial fonts ship with the build. Avoid it: archive proof for each font and keep replaceable open-source options ready.

## Further Reading

- [Programming Handbook](../../fundamentals/programming/README.md): string systems, data-driven design and automation infrastructure — the source material for §2 and §4 of this page.
- [Production Handbook](../../fundamentals/production/README.md): outsourcing management, estimation and scheduling — the methodology behind language batch scheduling.
- [Multi-platform Launch Playbook](../../../playbooks/platform-launch/README.md): store submission and language metadata requirements; read alongside §3.6.
- [Pitfalls & Anti-patterns](../../pitfalls/README.md): text, UI and localization pitfalls; cross-reference with §5.
- [AI Workflows Handbook](../../ai/README.md): the boundaries of MT and AI assistance, and the human verification process.
- [Visual Novel Handbook](../../genres/visual-novel/README.md): localization prerequisites for text-heavy projects; see its §4.3.
