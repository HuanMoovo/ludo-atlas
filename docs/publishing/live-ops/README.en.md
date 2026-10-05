# Ludo Atlas · Live-Ops & Growth

> Positioning: a live-ops handbook for the road from "the game is launched" to "being played, being discussed, and lasting" — covering the growth funnel, the pre-launch/launch/post-launch cadence, data metrics, platform mechanics, community and crisis, monetization ethics, and overseas growth.
> Companions: Multi-platform Launch Playbook (launch flow) · Legal, Patents & Competition (competitive analysis) · Production Handbook · Resources (tools and data sites, §4, §8.3).
> Reminder: the marketing numbers (conversion rates / sales multiples) are all **industry experience ranges**, with enormous variance between genres — trust your own data dashboard over anything else.

---

## 1. Growth Funnel Overview (see the whole map first, then tighten each link)

```text
Exposure (platform recommendations / media / social / search)
  → Store page visits (decided by capsule click-through rate)
    → Wishlists / demo plays (decided by conversion)
      → Purchase (decided by pricing / word of mouth / timing)
        → Retention and spread (positive reviews / livestreams / word of mouth → feeding exposure back)
```

- Every link has an input and a conversion rate; **optimize only the leakiest link** (psst: for most indie games the bottom of the funnel is "exposure", not "pricing").
- On PC the core asset is the **wishlist**; on mobile it is **retention and LTV**; in mini-games it is the **share rate and ad eCPM**.

## 2. Pre-Launch Live-Ops (6-month countdown)

| Time | Action |
| --- | --- |
| T-6 months | Store page live (before everything else); settle the main capsule and trailer direction; set up community bases (pick one or two of Discord/QQ/Bilibili/Weibo) |
| T-4 months | Keep posting content (gif/short video/devlogs, every 1-2 weeks); collect media and creator lists (press kit ready) |
| T-2 months | Join platform festivals (Steam Next Fest etc.); demo release; pre-registration/wishlist push |
| T-2 weeks | Media and creator outreach (personalized emails with keys); confirm livestream schedules |
| T-1 week | Launch content ready (announcement/update notes/FAQ/support scripts); release-day checklist rehearsal |

- **Press kit template**: game description (three versions: 50/100/300 characters) · 3 selling points · team info · hi-res asset pack (logo/screenshots/gifs/trailer) · contact details. See the dopresskit style for reference (https://dopresskit.com/).
- **The capsule image is the single biggest lever**: A/B it side by side with competitors on the store page and in lists (assemble a comparison collage of 10 competitor capsules yourself); if it doesn't pass, redo it (the best money you'll spend).
- Marketing methodology to follow long-term: How To Market A Game (https://howtomarketagame.com/, first-hand experience from the Steam ecosystem).
- Three email principles: personalized (mention one specific thing of theirs) · short (under 5 lines) · one image, one link.

## 3. Launch Week Battle

- **The first week is the algorithm window**: from 24h before release, recommendation slots and chart weight are at their highest — concentrate all your ammunition in the first week.
- Launch discount (10-15% is standard) + launch announcement + synchronized media/creator push + community activities (giveaways/livestreams/challenges).
- Data monitoring sheet: wishlist conversion, refund rate, review velocity and average score, sales by region, abnormal crash rate (in coordination with the Programming Handbook).
- Support cadence: respond to frontline issues within 4-8 hours in the first week; major bugs go through the hotfix process (Multi-platform Launch Playbook §8).
- Mindset: **day one is not the endgame**: Steam's long tail is driven by festivals, discounts and word of mouth (see §5).

## 4. The 90 Days After Launch

| Phase | Focus |
| --- | --- |
| Weeks 1-2 | Hotfixes and stability (the rating defense); thanks and patch notes (patch notes are marketing content too) |
| Weeks 3-6 | Tease the first content update (keep exposure up); collect community feedback into the roadmap |
| Weeks 6-12 | First discount (follow the platform cadence and comparable titles); join platform festivals; community events |
| 90-day retrospective | Funnel retrospective (exposure/conversion/retention/word of mouth); set the long-term roadmap |

- **Review management**: never buy or fake reviews (platforms crack down hard); for negative reviews, reply once — concise, objective, no arguing; guide satisfied players to leave a review (a gentle in-game reminder, no inducement).
- Be aware of the rating tiers (Steam as the example): a positive rate around 80%+ is the "Very Positive" band, 95%+ is "Overwhelmingly Positive" (minimum review counts apply; the platform's rules are authoritative) — the tier affects recommendation weight and conversion.

## 5. Long-Term Live-Ops (6 months and beyond)

- **Update cadence**: promise only what is sustainable (a small update is still an update); 1-2 major versions a year + monthly small patches; every update = a small marketing window.
- **Content asset reuse**: update trailers/guides/replay compilations keep producing social media material; UGC (Workshop/challenges) is a free growth engine.
- **DLC/expansions**: do them once the base game's reputation has stabilized; the gold-mine assessment = base game sales × existing-player activity.
- **Cross-title planning**: sequels/new titles in the same universe convert existing players (cross-linked series pages, bundles).
- Mobile: season/event cadence (no pressure to pay), long-term numbers iterated with each version, soft launch through to scaling paid acquisition (see §7).

## 6. Metrics Handbook

### 6.1 Universal Funnel Metrics

| Link | Metric | Healthy signal (experience values) |
| --- | --- | --- |
| Exposure→visits | Store page visits | Fluctuates in step with exposure |
| Visits→wishlists | Wishlist conversion rate | Varies by genre; if under 1%, check capsule/tags |
| Wishlists→purchase | First-week conversion rate | Industry range around 10-25% (wide variance; benchmark within your genre) |
| Purchase→satisfaction | Average review score / refund rate | A refund rate clearly above comparable titles = a problem signal |

### 6.2 PC (Steam) Specifics

- Total wishlists and the **daily growth rate** (the rate in the 30 days before launch = a heat signal); Steam Next Fest performance (demo plays/wishlist gain).
- Sales conversion: review count, peak concurrent players, regional distribution (inputs to pricing and localization decisions).

### 6.3 Mobile Specifics (concept cheat sheet)

| Metric | Meaning | Use |
| --- | --- | --- |
| D1/D7/D30 retention | Share of players returning on day N | The core of product health (casual D1 experience range ~30-40%) |
| CPI | User acquisition cost | The denominator of paid-acquisition economics |
| LTV | User lifetime value | Must be > CPI to be sustainable |
| ROAS | Return on ad spend | The switch for scaling up or stopping media buys |
| ARPDAU | Average revenue per daily active user | Monetization efficiency |

- Paid acquisition 101: test creatives on a small budget first (3-5 sets) → watch CPI/ROAS → scale only once the numbers clear; for creative production see the tools in Resources §8.3.

## 7. Platform Mechanics and Algorithms (overview level)

- **Steam exposure mechanics (community consensus)**: wishlists and first-week conversion are the core signals; festivals/themed sales are the biggest free windows; tags decide who gets recommended (wrong tags = exposure to the wrong audience). Strategy: target tags at a niche audience, actively join official festivals, keep the update cadence.
- **Mobile stores**: charts and editorial features are influenced by retention/ratings/update activity; keep iterating ASO (title/subtitle/keywords/screenshots) (tools in Resources §4.4).
- **Mini-game platforms**: on WeChat, social traffic and share virality are king (share-incentive designs have platform red lines); on Douyin, short-video attachment is the core distribution (the creative is the ad spend); plan each platform's play separately.
- All "mechanics" can change; **follow the platforms' official announcements, don't trust folklore**.

## 8. Community and Crisis PR

- **Base strategy**: one main base (Discord or a QQ/WeChat group) + 1-2 content bases (Bilibili/Weibo/X/YouTube/Reddit); better few and well-kept than registered and abandoned.
- **Content cadence**: devlogs (weekly/biweekly) · behind-the-scenes · reshares of player creations · milestone celebrations — build trust through a sense of presence.
- **Crisis-handling SOP**:

  1. Stop: no emotional replies; 2. Check: establish the facts and scope; 3. Say: publicly, specifically, with a deadline ("we have located it; a patch within 48 hours"); 4. Do: keep the promise and follow up publicly; 5. Retro: write it into the process to prevent recurrence.

- Red-line list: don't argue with players, don't delete negative reviews (report rule-breaking ones instead), don't shift blame onto the platform/players, don't promise what you can't deliver (see Pitfalls & Anti-patterns).

## 9. Overseas and Localization Growth

- **Settle the markets first**: language-support priority = current sales regions × target-genre audience; Simplified/Traditional Chinese, English, Russian, Spanish, Portuguese, Japanese, Korean, French, German, Italian is a common reference order.
- **Localization is more than translation**: store page copy localization, festival localization (Lunar New Year/Christmas/local holidays), pricing by regional purchasing power (platform regional pricing suggestions ±).
- **Regional channels**: China (TapTap/WeGame/mini-games; compliance comes first, see Legal, Patents & Competition); Japan (media/CERO); Europe and North America (Reddit/Discord/creators); Latin America (Portuguese first). Regional differences are large — do a separate "release recap" per region.

## 10. Monetization Ethics and Sustainability

- **Principles**: monetization design should point the same way as the fun ("paying for love", not "paying for anxiety"); published gacha rates and transparent pity rules (a compliance floor, see Legal, Patents & Competition); ads must not interrupt the core experience (rewarded > forced).
- **Player trust = a long-term asset**: one predatory monetization move (trap UI / silently changing values / pressuring purchases) can drain ten years of accumulated goodwill.
- Financial sustainability: budget for live-ops costs (servers/updates/support); manage revenue-volatility expectations (the first month often accounts for a very high share — don't plan a full year of costs off the first-month line).

## 11. Retrospective and the Next Title

- 90-day post-launch retrospective template: funnel data (§6) → what content and live-ops got right → what was wasted → three improvements for the next title/version.
- Write each release's lessons into `docs/postmortems/`; compounding team knowledge is the independent developer's only stable "moat".
- The next loop: go back to the Game Design Handbook, and with data and experience in hand, take a more accurate next shot.

---

> **Full handbook index**: Resources (521 links) · Pitfalls & Anti-patterns · Legal, Patents & Competition · Multi-platform Launch Playbook · Game Design Handbook · Programming Handbook · Art & Audio Handbook · Production Handbook · Live-Ops & Growth — all collected in this repository.
