# Ludo Atlas · Legal, Patents & Competition

> Positioning: a practical map for game developers across six areas — copyright, trademarks, patents, contracts, overseas compliance and market competition.
> **Disclaimer**: this is an informational summary and **does not constitute legal advice**; for major matters such as disputes, contract signing or litigation, consult a licensed attorney. Laws, regulations and platform policies change continuously — before you act, rely on the latest official texts (the full texts of laws and regulations can be looked up in the databases at the end of this document).
> Companions: Pitfalls & Anti-patterns · Multi-platform Launch Playbook · Resources (including a directory of tools and sites).

---

## 1. Map of Legal Areas in Games

| Area | When you'll run into it | Key actions |
| --- | --- | --- |
| Copyright | Throughout: ownership of and infringement in code/art/music/writing | Put ownership in writing, asset ledger, open-source compliance (§2) |
| Trademarks | Naming at kickoff, before promotion, merchandise development | Search + registration (§3) |
| Patents | Referencing mechanics, being told you infringe, protecting mechanic innovations | Search + design-around + documenting evidence (§4) |
| Contract law | Publishing agreements, outsourcing, partnerships, platform agreements | Review of key clauses (§5) |
| Data & privacy | Collecting user data, analytics SDKs, child users | Policy + consent + minimization (§6) |
| Content & publishing regulation | Mainland China launch, game licenses, anti-addiction, gacha disclosure | Compliance up front (§6.3, Multi-platform Launch Playbook §7) |
| Tax law | When you receive overseas platform revenue | W-8BEN/VAT/withholding tax (§6.4) |

## 2. Copyright in Practice

### 2.1 What Is Protected — and What Isn't

- **Protected**: code, art (however simple), music, sound effects, writing and story, UI expression, character likenesses — all of these are "expression".
- **Generally not protected**: gameplay rules, mechanics, balance concepts (the "idea" layer); but **specific expression** (a distinctive level layout, a combination of art styles, written text) is protected.
- **Conclusion**: copying gameplay is generally legal (the industry broadly does it); copying expression (art/code/writing) is illegal. When referencing, keep the process documentation of your "redesign from the mechanic".

### 2.2 Ownership: Paperwork Matters More Than Anything Else

| Scenario | Risk | What you must do |
| --- | --- | --- |
| Outsourced art/music/code | Without a written agreement, copyright may still belong to the creator | State "**copyright assignment**" in the contract (full transfer of economic rights) + deliverables list + source files |
| Employee creations | Ownership of works created in the course of employment must be made clear under law and contract | Set out ownership and attribution of works created in the course of employment in the employment contract or a supplementary agreement |
| Co-founders developing together | Disputes over code/art ownership after a falling-out | The partnership agreement states contributions, rights allocation and exit mechanisms |
| Crowdfunding / commissioned fan creations | An unclear chain of title blocks commercialization | A "submission grants a license" clause (with a clear scope) |

### 2.3 Common Infringement Landmines

- Copying or tracing others' art (even recolored) → high risk of a substantial-similarity finding.
- Misusing asset-store licenses ("free" ≠ commercial use; asset licenses are tiered).
- Music "covers/remixes" without a license; commercial BGM licenses whose scope excludes games.
- Using third-party IP in screenshots or likenesses (fan assets making it into the shipping build).
- Embedding font files in the game package (fonts are independent works; commercial use requires a license).

### 2.4 Open-Source License Compliance (required reading for programmers)

| License | Copyleft | Notes for games |
| --- | --- | --- |
| MIT / BSD / Apache-2.0 | None | Closed-source commercial use allowed; Apache requires keeping NOTICE and includes a patent grant |
| MPL | Weak (file-level) | Modified MPL files must be open-sourced |
| LGPL | Weak (library-level) | Dynamic linking is generally fine; modifying the library itself requires open-sourcing |
| GPL | Strong | Linking GPL code usually requires open-sourcing the whole game |
| AGPL | Strong + network clause | **Server-side use also triggers the open-source obligation** (a key audit item for online games) |
| UE/Unity and other engines | Special license | Governed by the engine's commercial terms (revenue share/revenue threshold), not an open-source license |

- Practice: maintain a dependency list (SBOM) → scan licenses with tools → verify compatibility one by one; engine plugins need the same checks.
- The cost of getting it wrong: a closed-source game bundling a GPL library gets forced to open-source or rewrite; using an AGPL backend component without open-sourcing gets you held liable.

### 2.5 Fonts and Music (high-incident areas)

- **Fonts**: a hotspot for enforcement in mainland China. Use only fonts from "free for commercial use" lists (see Resources §5.6), and keep font license documentation on file.
- **Music**: three models: custom buyout (the cleanest rights), royalty-free libraries (check the scope: worldwide/perpetual/commercial/video platforms), CC (check the terms clause by clause). Write into the contract: commercial use, worldwide, perpetual, adaptation allowed, promotional use included.

## 3. Trademarks

- **Why**: the game name is your biggest intangible asset; if someone registers it first, you may be forced to rename (extremely high sunk cost); app stores, WeChat and console platforms may all require a trademark or proof of authorization.
- **Class strategy**: Class **9** (computer software/game programs), Class **41** (entertainment services/online games), Class **42** (software development); add Classes **16/25** (merchandise) and **35** (promotion) if budget allows.
- **Timing**: after the name is settled at kickoff and before any public promotion — search first, then register; file in your key markets (China + target overseas countries) in parallel.
- **Search**: China Trademark Office https://sbj.cnipa.gov.cn/ (trademark search portal https://sbj.cnipa.gov.cn/trademark-query); overseas, use the local trademark office or the WIPO Madrid System.
- **If someone registers it first**: evidence of prior use (promotion, sales records) → opposition/declaration of invalidity/non-use cancellation; the earlier you act, the more complete your evidence.
- **Note**: search for similar marks (sound/meaning/visual) before registering — don't just check for an identical name.

## 4. Patents (key section)

### 4.1 Can Games Be Patented?

- **Yes**: interaction mechanics, system designs and technical solutions (such as rendering/matching/anti-cheat technology) can obtain patents in most jurisdictions worldwide; the patentability of software-related inventions varies by country (China requires a "technical solution"; the US, after case law, requires "significantly more than an abstract idea").
- **Term**: an invention patent typically lasts **20 years** (from the filing date).
- **The reality for indie developers**: being sued over a game patent is a low-probability, high-damage event; **defense rests on the "search + design-around + evidence" trio**, not on fear.

### 4.2 Notable Game Patent Cases (public reports)

| Case | Summary | Takeaway |
| --- | --- | --- |
| Loading-screen mini-game (Namco, 1990s → expired 2015) | The mechanic of playing a mini-game while loading was once covered by a patent; the industry broadly steered clear until it expired | Mechanic patents really exist; after expiry it became a public resource |
| Arrow navigation (Sega's Crazy Taxi, 1998 → expired 2018) | A display mechanic that uses arrows to guide players to a target point | Mind this in street-navigation-style gameplay design |
| Rhythm-game note judgment (Konami, 2000s) | Patents related to falling-note judgment once affected similar music games | Search before borrowing music-game mechanics |
| Middle-earth Nemesis system (Warner Bros., granted 2021) | The procedural "nemesis" character-relationship system was granted a patent, sparking industry discussion | Complex system designs can also be covered by patents |
| Nintendo v. Palworld (filed 2024, ongoing) | A patent-portfolio lawsuit involving capture and other mechanics (as reported); no final ruling yet | Patent risk is concentrated in hot mechanics (creature capture/pet battles); watch the patent pools of leading studios |

> The above is compiled from public reports; for patent status and litigation progress, defer to official announcements.

### 4.3 Defense Strategies (executable by indie developers)

1. **FTO mindset**: before referencing a hot mechanic, spend 30 minutes searching for related patents (whether one exists, whether it is in force, and where).
2. **Design around**: don't copy the specific implementation (input method, judgment logic, UI presentation); reach a similar experience a different way.
3. **Document your independent development process**: design-doc timelines, commit history (git log), sketches — if you're accused of infringement, these are key evidence of "independent creation".
4. **Mind the patent clauses of open-source licenses**: Apache-2.0 includes a patent grant (reassuring to use); GPLv3 has patent-retaliation terms; MIT has no patent clause (note that).
5. **If you receive a warning letter (cease & desist)**: stay calm — don't reply, don't admit anything, don't delete evidence; **find a lawyer immediately**; assess prior-art invalidation and design-around room. Most game patent warnings can be resolved with a design-around.
6. **Don't be so afraid you can't build**: the vast majority of indie games never touch a patent dispute; the real risk is concentrated in "copying the signature mechanics of a leading studio".

### 4.4 Patent Search Toolbox

| Tool | Coverage | Use |
| --- | --- | --- |
| Google Patents | Global (with translations) | https://patents.google.com/ keyword + CPC classification search |
| China National Intellectual Property Administration (CNIPA) | China | https://www.cnipa.gov.cn/ patent search and status lookup |
| USPTO Patent Public Search | United States | https://ppubs.uspto.gov/pubwebapp/ |
| Espacenet | Europe/global | https://worldwide.espacenet.com/ |
| WIPO PATENTSCOPE | International applications | https://patentscope.wipo.int/ |

- Search tips: game-related patents mostly fall under **CPC class A63F** (including A63F13, video games); search in both Chinese and English keywords (game mechanic / 交互方法); focus on the **claims**, not the title.

### 4.5 Should You File Patents Yourself?

- **When it's worth it**: "signature mechanics" a competitor could also use, technology-barrier innovations (networking/rendering/anti-cheat); when a company is building a long-term IP asset portfolio.
- **Process overview**: draft the application → file it (you can file a provisional/priority application first) → substantive examination → grant (typically 2–4 years).
- **Cost scale**: agent fees + official fees, from a few thousand to tens of thousands of yuan per filing (depending on jurisdiction and complexity).
- **Personal advice**: indie developers should put their energy into the product and the trademark first; patents are worth investing in only when "a copied mechanic would make the game lose its competitiveness".

## 5. Contract Practice

### 5.1 Publishing Contracts: Eight Must-Check Clauses

| Clause | What to check | Typical trap |
| --- | --- | --- |
| Revenue-share base | The definition of "net revenue" (which costs are deducted) | A vague net-revenue definition dilutes your share without limit |
| Advance | Whether it's recoupable (recoup) and the recoupment order | The "advance" is really an interest-free loan; you see no money until it's recouped |
| IP ownership | Whether the game IP transfers to the publisher | After signing, the IP is no longer yours and sequels are constrained |
| Sequels / right of first negotiation | The scope of the publisher's priority rights over sequels | You get tied to your next title |
| Exclusivity and term | The scope and duration of platform/territory exclusivity | Perpetual all-platform exclusivity locks up future revenue |
| Termination conditions | Termination and IP-recovery mechanisms if performance falls short | No termination right — a bad publisher locks up your product |
| Audit rights | Whether you can inspect the books | You can't verify that revenue shares are real |
| Delivery obligations | Milestones and payment schedule, acceptance criteria | Vague acceptance criteria leave the final payment dangling |

### 5.2 Outsourcing and Freelancing

- Must-haves: a deliverables list (format/spec/source files), milestones and payment percentages, a **copyright assignment clause**, confidentiality terms, caps on delays and revision rounds.
- Attachments: reference images/spec sheets (to prevent "this isn't what I wanted" disputes).

### 5.3 Partnerships and Equity

- Equity allocation: fixed in writing by contribution (labor/capital/IP); a **vesting** mechanism (4 years with a 1-year cliff is common) stops early members from taking shares and walking away.
- Make the decision mechanism (who has the final say) and the exit mechanism (buyback price formula) explicit.

### 5.4 NDAs and Non-Competes

- You can sign an NDA before talks with a publisher/platform; check whether NDAs you've signed restrict similar projects later.
- Non-compete restrictions require consideration (compensation); from the player's perspective, most "job-hopping" cases don't apply — but mind the boundary around taking code/assets with you.

## 6. Going Overseas and Compliance

### 6.1 Privacy and Data

| Regulation | Applies to | Key points |
| --- | --- | --- |
| GDPR (EU) | EU-facing users | Legal basis, notice, right to erasure, cross-border data transfer |
| CCPA/CPRA (California) | California users | Sale/sharing notice and opt-out mechanisms |
| COPPA (US) | Child-directed (<13) | Collecting children's data requires parental consent (https://www.ftc.gov/legal-library/browse/rules/childrens-online-privacy-protection-rule-coppa) |
| PIPL (China) | Chinese users | Consent, minimization, special protection of children's personal information |
| Platform rules | All platforms | Privacy labels (App Store)/data safety forms (Google Play) must match reality |

### 6.2 Age Ratings

- IARC (one submission, ratings for multiple regions) https://www.globalratings.com/; ESRB (North America), PEGI (Europe), CERO (Japan) and others per target market; rating questionnaires must be answered truthfully (including IAP, gacha, social features and violence).

### 6.3 Content and Consumer-Compliance Trends

- **Gacha/loot boxes**: probability and pity-guarantee disclosure is already a hard requirement in mainland China; Belgium, the Netherlands and elsewhere have strict rulings on loot boxes — check market by market when going overseas.
- **Advertising**: no false claims ("the most fun in the world" and similar phrasing is risky); "limited-time" and "free" promises must be true.
- **Terms of service/privacy policy**: an essential document package before launch (see the Multi-platform Launch Playbook §2).

### 6.4 Tax and Payouts (brief)

- US platform revenue: file **W-8BEN** (individuals) to declare non-US taxpayer status and avoid 30% withholding.
- Europe: some platforms remit VAT for you (per platform policy); selling on your own means handling local VAT.
- Payouts: mind the payment methods and fees each platform supports; consult an accountant when your revenue structure is complex.

## 7. Competitive Analysis (market and competitors)

### 7.1 Competitor Teardown Framework (the one-page table method)

For each direct competitor, fill in a six-dimension table: **core loop** (what players do in the first 30 minutes) → **selling points** (what the store-page art/trailer is shouting) → **content volume** (playtime/level count) → **price and discount history** → **review analysis** (positive/negative review keywords, reviews from the last 30 days) → **estimated sales range**. Output: a positioning chart (price × complexity / audience × selling points).

### 7.2 Data Tools (all estimates — cross-verify)

| Tool | Dimensions |
| --- | --- |
| SteamDB | Concurrent players, tags, upcoming releases chart (check competitors and release windows) |
| Gamalytic / VG Insights | Sales and revenue estimates, competitor comparisons |
| SteamSpy | Sales range estimates |
| Qimai / Diandian Data | Mobile charts, download and revenue estimates |
| Sensor Tower / Newzoo | Market-level reports (paid) |
| Community signals | Wishlist data (developer backend), Reddit/Discord discussion volume |

- Rule of thumb (use with caution): Steam review count × 30–50 ≈ order of magnitude of sales; the relationship between wishlist conversion and first-week sales varies widely by genre — benchmark within your genre.

### 7.3 Judging the Market Space

- Look at **saturation**: the number of similar new releases in the last 12 months and top-end concentration (the top 5 eating most of the revenue → be cautious).
- Look at **long-tail opportunities**: whether a niche audience (a theme/a gameplay combination) is served; which unsolved problems negative reviews cluster around (your opening).
- Look at the **price band**: the common price range for similar quality; anchor pricing to "competitors + your level of completion".

### 7.4 Differentiation Strategy Toolbox

1. **Combinatorial innovation**: X meets Y (e.g. "farming + cards", "roguelike + rhythm game"), but make sure the two systems genuinely interlock.
2. **Depth for breadth**: fewer but better (one mechanic taken to the extreme > ten half-finished mechanics).
3. **Audience niche**: serve overlooked groups (language/culture/accessibility/platform).
4. **Presentation moat**: distinctive art style, strong narrative, strong music — the most realistic perceivable differentiation for an indie team.
5. **Timing strategy**: release in the gaps between similar big titles; first-mover advantage (especially for lightweight gameplay).

### 7.5 Facing Competition and Being Copied

- Copying (at the legal-gameplay level): faster iteration and community bonds are the best defense (speed + brand + player relationships).
- Infringement (at the expression level): preserve evidence → demand letter → platform complaint (DMCA/store infringement channels) → litigation; see §2.
- Big studios following your genre: don't fight head-on; change lanes / strengthen your vertical community / build the deep experience "the big studios can't be bothered to make".

## 8. Public Case Index (Further Reading)

| Case | Theme | In a nutshell |
| --- | --- | --- |
| No Man's Sky | Promise management | A complete case of overpromising + sincere late-stage recovery |
| Cyberpunk 2077 | Launch quality and console certification | The textbook case of shipping below platform quality standards → delisting + refunds |
| Anthem | Vision drift and management | A "development without direction" case exposed by public press investigations |
| Nintendo v. Palworld | Patent risk | A patent lawsuit in a hot-mechanics field, still in progress |
| Namco loading patent / Nemesis patent | Patent boundaries | Two archetypes of mechanic and system patents: expired into the public domain vs newly granted and contested |
| Loot box rulings around the world | Consumer compliance | A bellwether of tightening gacha regulation globally |

> Only cases with ample public reporting and clear boundaries are listed above; read the original reports and official announcements — don't trust second-hand retellings.

## 9. Legal Action Checklist (by stage)

| Stage | Must-dos |
| --- | --- |
| Kickoff | Trademark search (name); confirm the gameplay doesn't copy patented implementations; asset sourcing plan (free-for-commercial-use lists) |
| Development | Outsourcing contracts (copyright assignment); open-source dependency audit (SBOM); archive music/font license files; asset ledger (including AI records) |
| Pre-launch | Terms of service + privacy policy; age-rating questionnaire; platform compliance checks; game licenses/anti-addiction (mainland China online games); submit the trademark application |
| Live | Infringement monitoring (asset theft/name imitation); compliance updates (policy changes); revenue tax handling; shutdown contingencies |

> One more reminder: this handbook is a map of "when to call a lawyer and what to look at when you do" — not the lawyer itself. When real money is at stake in a contract, always pay for professional advice.
