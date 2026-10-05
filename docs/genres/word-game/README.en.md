# Ludo Atlas · Genre Handbooks · Word Game

> **Genre Handbooks · Volume 3**. Positioning: the genre that makes language itself its primary material. Players spell in grids, chain on links and fill from clues, trading a word list and validation rules for one "I thought of it" after another; this page covers word-list engineering, daily puzzles, hints and difficulty curves, spoiler-free score sharing and multilingual word lists.
> Companions: Game Design Handbook (core loops and feedback) · Programming Handbook (word-list pipelines and validation implementation) · Live-Ops & Growth (daily cadence and retention) · Case Studies (daily-puzzle product breakdowns).
> This page carries no external links; benchmarks list widely known works and traditional formats only, and figures such as word-list scale are common magnitudes — defer to measurements in your own project.

---

## 1. Positioning and Core Loop

In one line: the word game is the genre **that makes letters and words its primary material**. Players deal in spelling, letter selection, chaining, grid-filling and the rules of language, and the pleasure comes from "I thought of that word"; visuals and narrative are the shell, while the word list and the validation are the substance.

The core loop, written as a verb chain: `read the prompt (grid / clue / chain head) → search and associate → enter a candidate → validation and feedback → eliminate or confirm → enter again`

This loop is measured in seconds to minutes: a single answer takes a dozen seconds or so, one round runs a few to a dozen minutes, and the daily mode stretches it into a once-a-day ritual. It holds on just two preconditions: the word list must be clean (§3.1), and every entry must eliminate (feedback has to narrow the answer space, not just return "wrong", §3.3).

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Logic puzzle | A logic puzzle's rules have nothing to do with language; a word game's rules grow inside the language, and the answer is drawn from the word list (§3.1) |
| Trivia / quiz | Trivia tests whether you know a fact, and the answer sits in the question bank; a word game has you spell, guess, chain and fill inside language material, testing construction and retrieval |
| Interactive Fiction | In interactive fiction, text is a narrative medium and input advances the story; in a word game, text is gameplay material, and input only cashes out into validation and score |
| Grid logic (the sudoku kind) | Also grid-filling deduction, but with numbers or shapes as the material; a word game swaps in letters and words, so difficulty comes from language and reasoning at once |

A self-check question: swap the material for meaningless symbols — does the game still hold? If it stops holding, what you are making is a word game.

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **The moment it clicks**: the instant an entry is judged correct is the main pleasure. The observation point for acceptance is a player saying "I knew it was that one", not "a lucky guess".
2. **Fair and explainable**: every rejection has a reason, and answers stay within common usage; the only way to lose is failing to think of the word, never being tripped up by the word list.
3. **Ritual and showing off**: a fixed hour, one shared puzzle, once a day; streaks and score cards turn scarcity into progress you can show off, and sharing is part of the design (§3.2, §3.4).
4. **Zero barrier**: if you can read, you can play — the rules fit in one sentence, and the input method is no barrier at all.

Negative feelings (any one of these is a red light): being tripped up (obscure or ambiguous answers), being played (validation that is inconsistent from one moment to the next), left waiting (only one puzzle a day, with nothing to do but wait), or spoiled (the answer leaks before you even start).

Benchmark titles (all widely known works and traditional formats; play them yourself before breaking them down):

| Title or format | What to learn from it |
| --- | --- |
| Wordle | One puzzle a day, spoiler-free score sharing, the information design of three-state feedback, minimal rules |
| Crossword | The calibration of clue wording, the double retrieval of language and knowledge, the prototype of the daily ritual |
| Scrabble | Tile distribution and letter values, the strategic space from word to board, the tradition of arbitrating word-list disputes |
| Chengyu chain | A chain game from Chinese oral tradition: the tail-character constraint, chengyu data, social play for groups |
| Lantern riddles and character riddles | Character-shape and meaning play unique to Chinese: the measure of a riddle's wording, the ceremony of the reveal |
| Picture-guess-idiom mobile games | A picture gives the semantic clue and a chengyu is the answer; a mobile form built for fragmented time |

## 3. Design Essentials

### 3.1 Word Lists and Language Data: The Chinese-Specific Ledger

The word list is the substance. Separate the three layers first, then talk about scale:

| Layer | Content | Standard |
| --- | --- | --- |
| Answer pool | Common, unambiguous words everyone recognizes | On the order of a few thousand entries; better small and clean |
| Guess pool | Entries that can be judged valid | Several times the answer pool; uncommon words accepted |
| Blocklist | Slurs, offensive terms, brands and personal names | Maintained separately, updated regularly |

- Word segmentation: Chinese has no spaces, so word boundaries have to be defined by hand — whether "diannao" (computer) is one word or two directly decides whether it can enter the answer pool; the answer pool must be a hand-revised word list, never raw corpus mechanically split to pad the count.
- Pinyin: homophones are extremely common, and the collision rate is far higher than in English. For pinyin word-guessing gameplay, settle rules for multi-reading characters and tones in advance; for Chinese-character input gameplay, visually similar characters and IME candidates are new pitfalls.
- Chengyu: mostly four characters but not always; misspellings, variant forms and simplified–traditional mapping each get their own list; a chengyu's allusions and its praise-or-blame tone decide whether it is fit to be an answer.
- Character sets and cleaning: define the range with an authoritative character table such as the Table of General Standard Chinese Characters (8,105 characters in the full table, with the 3,500 characters of the Level 1 table as the common set), and keep obscure characters out of the answer pool; write deduplication, variant-form normalization, blocklist filtering and frequency tiering as re-runnable scripts, with every entry carrying source and tier fields; tier on frequency data, not on author preference — a hand-maintained five-thousand-entry list will not survive two versions.

### 3.2 The Daily Puzzle Mode: Built to Spread

The goal of the daily mode is not to restrict but to build one event everyone lives through at the same time: every player faces the same answer at the same hour, once a day, refreshing at a fixed time.

- The number of attempts commonly sits around 6: few enough that every entry carries weight, enough that deduction can converge; if you change it, retune word length and frequency tier alongside — do not turn this one knob alone.
- One shared puzzle and refresh time: discussion and sharing need a common coordinate, and an unsynchronized puzzle throws the social value away; anchor the reset to local midnight or a single global time, write the choice into the spec and never change it.
- Streaks and forgiveness: consecutive days are the retention engine, so the missed-day rule needs leniency (keep the personal best); besides the daily mode, leave a practice mode or an archive of past puzzles, but give practice its own separate word pool and no streak credit, so the sense of scarcity is not diluted.
- Scheduling and spoiler discipline: schedule a full year of puzzles in one pass and freeze them, flagging holiday easter eggs in advance; official channels post no answers before the day rolls over, and if the product has chat and comments, the day's answer goes on the blocklist.

### 3.3 Hints and the Difficulty Curve

There are only four difficulty knobs, all controllable:

| Knob | Toward easy | Toward hard |
| --- | --- | --- |
| Word length and form | Two-character words, common four-character chengyu | Long words, near-synonym decoy answers |
| Word frequency | High-frequency, everyday | Mid-frequency, still within "you know it" range |
| Clues | Direct definitions | Character decomposition, homophones, lantern-riddle phrasing |
| Feedback | Plenty of constraints from the start | Require convergence from nothing |

- Feedback is a hint: every judgment must give usable elimination information, with three-state results readable at a glance; show color plus symbols as two channels, never relying on color vision.
- Curve discipline: the day-one puzzle must be easy — the first impression decides retention; for level-based modes, order levels by "frequency tier plus clue type", giving only direct clues for the first several levels before gradually switching to more taxing phrasing; obscure words remain easter eggs forever.
- A way out when stuck: the daily mode usually leaves only one exit, "give up and see the answer"; level-based modes hint in tiers, from range to structure (first character or first pinyin letter) to outright reveal, with used hints recorded and displayed separately from unaided scores; hint copy passes no judgment — a condescending tone pushes players away.

### 3.4 The Share Mechanic: A Spoiler-Free Score Card

Score sharing is part of the design, not a feature patched in on release day. Its duties: let those who played show off, make those who did not curious, and ruin nobody's day-of experience.

A passing score card:

```text
Puzzle 128 · 4/6 · Streak 12
●○○·○
·●●○○
●○●●○
●●●●●
```

Legend (explained on the page): ● right position, ○ wrong position, · not present; each row is one guess, and the card itself contains no characters from any entry.

- Red line number one: no characters from the answer or the guesses appear on the card; the block matrix conveys only the shape of the process — a good result looks good as a shape, not as leaked content.
- One line of text, copied as plain text, pasteable into any chat app; generated from the local match record, no network required; date or puzzle number plus attempt count and streak, so that same-day players can signal each other.
- The share rate is designed, not hoped for: the copy button sits on the results flow, and the card can be regenerated at any time; freeze the format once shipped — a redesign breaks the match with veterans' historical cards.

### 3.5 Localization and Multilingual Word Lists

Multilingual support is not translation; it is a separate "language pack" per language, and all four pieces have to come as a set:

| Module | What each language needs |
| --- | --- |
| Word list | Answer pool and guess pool each cleaned, tiered and filtered |
| Validation | Character-set rules, case and diacritics, repeated-character handling |
| Input | Keyboard layout, IME and candidate behavior, touchscreen adaptation |
| Content | Puzzle generation, clue copy, share-card format |

- Chinese simplified–traditional mapping, multi-reading characters and chengyu data do not apply to an English version, and English letter distribution and word-length structure do not apply to a Chinese version; a word list is a language asset and can only be reviewed by native speakers — machine translation drags "words that do not exist" into the answer pool. Mechanics can be shared; assets cannot be transplanted.
- Difficulty alignment and production order: word length and character sets differ by language, so re-tier with each language's own frequency data; finish one language's complete experience before starting the second — rolling out five languages at once usually means all five come out dirty.

## 4. Technical Essentials

The engineering bar is low, and the difficulty concentrates in data and validation; web, mobile and desktop can all carry it, and everything below is engine-agnostic.

**Word-List Pipeline**

- Word-list files go into version control, with fields frozen on day one (entry, pinyin, frequency tier, length, tags, source, status); change words through scripts — hand-editing the list does not last; word-list releases and game releases move on separate rhythms, and changing a word touches no code.
- The validator is the first tool to write: fields complete, all answers in the same pool, no duplicates, blocklist in effect, tier distribution reasonable.

**Validation**

- Write the validation rules as an explicit spec with test cases. The most common mistake is repeated characters: first check position by position for right-place hits, then judge wrong-place hits by remaining occurrence counts (a two-pass scan); cover cases of the "two identical characters, only one hits" kind.
- Chinese input has to handle IME composition events: do not steal keys while a candidate is uncommitted, and validate uniformly once it is committed; test the custom-keyboard and system-IME approaches separately.
- Write the accepted range of answers into the validation table: whether aliases, simplified–traditional variants and common misspellings count is decided entry by entry and kept in the log, not hard-coded into code branches.

**The Daily Puzzle and Time**

- The date-to-puzzle mapping must be deterministic: the puzzle number plus a word-list index generates the seed, so one date means one puzzle worldwide; the schedule ships with the version and is frozen.
- Answer delivery is a trade-off: a word list shipped with the client will always be unpacked, so the common practices are to obfuscate or encrypt it before use, or to serve the day's answer from the server; it cannot be fully prevented, and the goal is to lower the payoff of digging. Write the reset time and metric definitions in stone: anchor to device-local midnight or server time; store streaks locally first, and add accounts only for cross-device sync.

**Share Cards and Telemetry**

- Share cards are generated from the local record, with one automated check attached: the generated text contains no character from that day's answer. Telemetry watches five numbers: start rate, completion rate, give-up rate, share rate and the distribution of guess counts — the last is the master data for difficulty calibration, deciding which frequency band the word pool should shift toward.

## 5. Content Volume and Workload Reference

The following are typical magnitudes for projects of this kind, for estimation and for cutting requirements; not a commitment.

| Tier | Content scale | Timeline scale | Notes |
| --- | --- | --- | --- |
| Prototype | A few hundred words, one mode | 1 to 2 weeks | Validates the loop and the validation; word list picked by hand |
| Small complete title | A few thousand words, two to four modes | 1 to 3 months | Word-list cleaning is the bulk of the work |
| Daily-operations product | Thousands of scheduled puzzles plus a maintenance line | Ongoing investment | Scheduling and word-list upkeep are a monthly bill |

Conversion standards:

- One language's clean answer pool typically runs a few thousand entries; cleaning, tiering and the blocklist take one to two weeks; drawing a year's schedule with scripts plus human review typically takes a few days, after which you keep a fixed weekly maintenance window.
- Modes, hints and share cards are light work, but the word-list fields have to be reserved up front (source, tier, status); each new language equals roughly half a new project, with the word list and input adaptation as the main costs (§3.5).
- Scope discipline: get one language and one mode right first. This genre does not die from being unfinished; it dies from laying out modes before the word list is clean.

## 6. How to Start the First Prototype

Goal: one to two weeks to answer one question — is this loop annoying? Do not touch art, accounts or servers.

1. **Days 1–2: a small, clean word list.** Hand-pick 200 to 500 common words and mark each as answer pool or guess pool; skip the cleaning pipeline and run one pass by hand first.
2. **Days 3–5: validation and feedback.** One Chinese input approach, three-state feedback that delivers elimination information; write the repeated-character rules as test cases. Ugly is expected.
3. **Days 6–9: the daily skeleton.** Puzzle number equals the date, one puzzle a day, 6 attempts; record streaks and the guess-count distribution locally; add a plain-text share card.
4. **Days 10–14: two rounds of blind testing.** Get 5 people to play three days in a row, and record the day-two return rate, the average number of attempts, and whether anyone shares their card unprompted; in the second round, fix only the word list and the validation.

Acceptance criteria (all observable):

- At least three of five testers come back on their own the next day; the engine of the daily mode is return visits, not a single completion.
- No "that is not even a word" disputes anywhere along the way; any disputes that did occur are on record and enter the cleaning list.
- At least one person shares their score card unprompted and the card contains no characters from the answer; those who fail explain the result as "I did not think of it" rather than "this game judges at random".

## 7. Common Pitfalls

1. **A dirty answer pool**: obscure words, variant forms, offensive terms and nicknames leak into the shared puzzle, and one crash-and-burn costs you a batch of players (§3.1).
2. **Validation rules left unclear**: repeated characters, aliases, simplified–traditional variants and misspellings are handled inconsistently, and what players remember is the grievance of "I entered it and it did not count" (§4).
3. **Leaks and spoilers**: the share card carries guess characters, or the client stores the whole year's answers in plaintext — once unpacked, same-day spoilers are only a matter of time (§3.4, §4).
4. **Streaks and dead waiting**: missing a day resets the streak with no remedy, turning ritual into guilt; with nothing playable besides the daily mode, players finish the day's puzzle and have nothing to do (§3.2).
5. **Difficulty by obscurity**: using technical terms, dialect words and rarely seen characters as the difficulty knob is a trick, not a challenge (§3.3).
6. **Failing the hint dilemma**: either there is no exit and stuck players churn, or one button hands over the answer and wipes the challenge to zero (§3.3).
7. **Localization as translation only**: mechanics ported straight over while character sets, word lengths and input methods all mismatch; rolling out several languages at once leaves every one of them dirty (§3.5).
8. **Copying another product's word list and schedule**: unclear provenance and licensing, with no buffer at all when trouble hits (§3.1).
9. **Changing a puzzle mid-flight**: editing the day's answer after launch so the same puzzle has two versions (§3.2).

## Further Reading

- Game Design Handbook: the base document for core loops, feedback and difficulty curves — the draft under §1 and §3 of this page.
- Programming Handbook: the details of data pipelines, validation implementation and local storage, corresponding to §4.
- Live-Ops & Growth: the operations ledger of daily cadence, retention and spread — cross-read with §3.2 and §3.4.
- Case Studies: breakdown methods for daily-puzzle products — consult when choosing a direction and during retrospectives.
- Indie Survival: scope control and scheduling for small-scope projects, complementary to §5.
- Exercise: hand-write a 200-word answer pool, have a friend play for three days, and record three things: the day-two return, the average number of attempts, and whether anyone shares unprompted. Those three records are this handbook's acceptance sheet.
