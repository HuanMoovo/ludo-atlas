# Ludo Atlas · Multi-platform Launch Playbook (incl. online-game specifics)

> Positioning: a complete process map from "the game is done" to "launched on every platform", covering international PC/console/mobile, mainland China channels, mini-games, and the **online-game specifics** (game license, anti-addiction, real-name verification, operating qualifications).
> **Timeliness statement**: platform policies and regulatory rules keep changing; the facts in this document were verified as of **2026-10**. Before acting, go by the latest official documentation. For regulatory matters, use a licensed publishing agency or legal channel.
> Companions: Pitfalls & Anti-patterns · Legal, Patents & Competition · Resources (which includes official links for every platform).

---

## 1. Launch Landscape at a Glance

| Platform | Access & fees | Hard qualification requirements | Review characteristics | Best for |
| --- | --- | --- | --- | --- |
| Steam | Steamworks registration, $100 per title (returned once sales reach $1,000) | No game-license requirement (international platform) | Two reviews: store page + build | PC mainstay, worldwide |
| Epic Games Store | Apply to join | No game-license requirement | Manual review, moderate bar | PC, 88/12 revenue share |
| GOG | Apply for review | No game-license requirement | Higher quality bar, DRM-free | Polished PC titles |
| itch.io | Free and instant | None | No review, publish freely | Prototypes / early testing / jams |
| Xbox / PlayStation / Switch | Platform-holder approval to join | No China game-license requirement | Concept review + strict certification (cert) process | Consoles |
| App Store (China region) | $99/year | **Games require a game license** | Guidelines strictly enforced | iOS |
| Google Play | $25 one-time | No game-license requirement (overseas) | New individual accounts must pass closed testing first (§5.2) | Overseas Android |
| TapTap | Developer onboarding | Software copyright + game license (for formal mainland China release) | Platform quality review | Mainland China Android/PC |
| Haoyou Kuaibao | Developer platform | Software copyright + game license | Focus on testing and pre-registration operations | Mainland China mobile games |
| WeGame / Steam China | Apply to join | Game license | Platform review | Mainland China PC |
| WeChat / Douyin / Kuaishou mini-games | Entity registration | Software copyright + (a game license to enable virtual payments) | Category + content + qualification review | Mini-games |
| 4399 and similar browser-game/mini-game channels | Open-platform registration | Software copyright + game license | Standard review | Mini-games / browser games |
| Web platforms such as CrazyGames / Poki | Free registration | None (overseas) | Quality and performance review | HTML5 web games |

> Universal iron rule: **every formal commercial channel in mainland China (app stores, mini-game virtual payments, mainland China PC platforms) requires a game license**; overseas platforms such as international Steam do not require a China game license, but you must comply with the target market's regulations (Legal, Patents & Competition §6).

## 2. Common Preparation Pack (assemble it all before launch)

| Category | Checklist | Notes |
| --- | --- | --- |
| Legal documents | Terms of service, privacy policy, age-rating questionnaire, trademark (recommended) | The privacy policy must match the real data flows (including third-party SDKs) |
| Qualification documents | Software copyright certificate, game-license documents (mainland China), ICP filing/license (online-game operation) | For software copyright registration see Resources §9.1 (Copyright Protection Center of China) |
| Store assets | Capsule/key art, screenshots (multiple platforms and resolutions), trailer, store copy (multiple languages) | Specs differ per platform; prepare asset masters and export scripts in advance |
| Technical capabilities | Achievements, cloud saves, gamepad support, pause/save failure handling, crash reporting | Tick off each item against each platform's "required feature list" |
| Accounts & payment | Developer accounts, payout accounts, tax forms (W-8BEN etc.) | Keep the payout entity identical to the developer entity to reduce review friction |
| Version management | Version-number conventions, build pipeline, rollback-capable release packages | See pipelines/build-release |

## 3. PC Platforms

### 3.1 Steam (ten-step process)

1. Register a Steamworks developer account and pay the $100 app fee per title (returned once sales reach $1,000).
2. Complete tax and bank information (W-8BEN etc.) → decide the payout entity.
3. Create the app → build the **store page** (capsule, screenshots, trailer, tags, description) → submit the store page for review (make it public as early as possible to accumulate wishlists).
4. Integrate the Steamworks SDK: achievements, cloud saves, leaderboards, Workshop (optional), Steam Input.
5. Upload builds with steamcmd (manage branches with depots: default/beta).
6. Submit the **Build Review**; if problems come back, fix per the feedback and resubmit.
7. Set the release date (changeable at any time); start curator/press outreach two weeks before release.
8. Configure regional pricing and the launch discount (see the pricing tools in Resources and the pricing bands of comparable titles).
9. Release: check every language page, system requirements (including the Steam Deck compatibility rating) and refund-policy notices.
10. After release: validate hotfixes on the beta branch → promote to default; use Steamworks data to watch conversion and regional performance.

> Note: AI content disclosure happens in the Steamworks content survey (two categories: pre-generated and runtime-generated; see design doc §14.9); the sooner you get store-page asset specs and a "Coming Soon" page up, the better.

### 3.2 Epic Games Store

- Apply to join through the official form → sign the digital distribution agreement (88/12 revenue share) → submit the store page and build for review; you can also apply for EOS (Epic Online Services), a free multiplayer service.
- Official entry points: https://store.epicgames.com/ (developers: https://dev.epicgames.com/).

### 3.3 GOG

- Submit an application on the official site (manual curation; DRM-free and well-finished titles preferred) → negotiate commercial terms → launch; suits polished indie and classic games.

### 3.4 itch.io

- Publish the moment you register: upload a build, customize the page and pricing (you can set your own price), Pay-What-You-Want supported; best suited to prototypes, jams, early testing and community management.

### 3.5 Web Game Platforms (HTML5)

- **CrazyGames**: developer portal https://developer.crazygames.com/, with review focused on playability and performance, and an ad revenue-share model.
- **Poki**: developer platform https://developers.poki.com/, with strict review and a focus on mobile adaptation and load performance.
- Suits lightweight gameplay; before launching, always test mobile-browser compatibility and optimize loading.

### 3.6 Mainland China PC (WeGame / Steam China)

- Both require a **game license** and complete compliance materials; WeGame (https://www.wegame.com.cn/) also involves communication around platform-exclusivity policy; Steam China (https://store.steamchina.com/) is the mainland-compliant edition of Steam.

## 4. Console Platforms (the shared process)

1. **Apply to join**: ID@Xbox (https://www.xbox.com/en-US/developers), PlayStation Partners (https://partners.playstation.net/), Nintendo Developer Portal (https://developer.nintendo.com/).
2. **Concept review / incubation**: submit a pitch and a playable demo; on approval, sign the NDA and development agreement.
3. **Dev kits and certification**: obtain the development kits; develop against the platform's technical requirements (TRC/TCR etc.).
4. **Certification**: submit a candidate build for review; key checks: error handling (network unplug / power loss / full save storage), UI standards, multiple languages, achievements, parental controls.
5. **Release**: store page, age ratings, regions and pricing → launch.

> Certification is the biggest schedule variable in console launches: budget **2–6 weeks** (longer for a first one); a failed certification means fixing everything and re-queuing, so leave buffer in the release date.

## 5. Mobile Platforms

### 5.1 App Store

- Process: Apple developer account ($99/year) → create the app record in App Store Connect → metadata and screenshots → TestFlight beta → submit for review → release (manual/automatic).
- **China region**: games **must provide a game license** to launch (no license, no launch; overseas releases are not subject to this).
- Common rejection reasons: 4.3 (duplicates/reskins), 2.1 (insufficient completeness), 3.1 (circumventing IAP), 5.1 (privacy labels / ATT mismatch), infringing assets.
- Review guidelines: https://developer.apple.com/app-store/review/guidelines/

### 5.2 Google Play

- Process: developer account ($25 one-time) → create the app → Data safety form, content rating (IARC), target API compliance → test tracks (internal/closed/open) → production release.
- **New individual developer accounts**: before applying for production release you must first complete **closed testing (at least 12 testers for 14 consecutive days)**. The policy is revised over time (in some periods and statements it was 20 testers); go by the latest statement in Play Console: https://support.google.com/googleplay/android-developer/answer/14151465
- Common rejection reasons: the Data safety form not matching reality, permission abuse, infringing store assets.

### 5.3 Mainland China Android Channels (TapTap / Tencent MyApp / Huawei / Xiaomi / OPPO / vivo / Haoyou Kuaibao)

- In common: **a corporate entity + software copyright + a game license** (for formal commercialization); each channel has its own developer console and launch-materials process.
- Process outline: register a channel developer account → submit qualifications (business license / software copyright / game license) → upload the package (channels may require hardening/signing) → channel review → first-launch / joint-operation setup.
- TapTap (https://developer.taptap.cn/): includes PC distribution and community management; Haoyou Kuaibao (https://open.3839.com/): focused on testing and pre-registration.

## 6. Mini-Game Platforms

### 6.1 WeChat Mini-Games (the most granular rules; the official docs are authoritative)

- Entity: individual entities can publish **free** mini-games (ad monetization); **paid games require a corporate entity**.
- Qualifications: **enabling virtual payments (IAP) requires submitting a game license (the online game publication number issuance document) + software copyright + a letter of authorization**; free games that don't enable payments don't need a game license (the platform helps integrate the real-name system in a unified way).
- Anti-addiction integration: companies that enable virtual payments must complete corporate registration, add the game and bind channels in the Publicity Department (National Press and Publication Administration) real-name verification system (https://wlc.nppa.gov.cn/fcm_company/index.html), and sync the information to the WeChat platform (guide: https://developers.weixin.qq.com/minigame/introduction/guide/zzsh-iap.html).
- Review focus: category choice (a game category cannot be changed), content compliance, no circumventing virtual payments (no directing users to external payment).
- Release flow: upload via the developer tools → submit for review → publish; beta and trial builds are supported as separate tracks.

### 6.2 Douyin Mini-Games

- Register on the ByteDance Open Platform (https://developer.open-douyin.com/) → mini-game category qualifications → integrate real-name and anti-addiction → submit for review and publish; distribution relies on short-video + livestream attachment, and the operating playbook differs from WeChat's.

### 6.3 Kuaishou / Huawei / OPPO / vivo / Xiaomi / Baidu

- All follow: open-platform registration → qualification submission → review and release; qualification requirements are similar to WeChat's (software copyright as the baseline; payment features need a game license); traffic characteristics differ per platform, so focus operations on "1 primary + 1 secondary".

## 7. Online-Game Specifics (mainland China; the key section)

### 7.1 Online Games vs. Standalone: Launch-Compliance Differences

| Item | Standalone (mainland channels) | Online games / with in-app purchases |
| --- | --- | --- |
| Software copyright | Required | Required |
| Game license (ISBN) | Required for formal mainland channels | **Required, and mandatory for paid operation** |
| ICP filing / license | Ordinary website filing | The operating entity needs an ICP license (one of the game-license application materials) |
| Anti-addiction / real-name | Required as soon as it's online | **Mandatory** (integration with the NPPA system) |
| Probability disclosure | If gacha is included | **Mandatory disclosure of probabilities and pity guarantees** |
| Content self-review | Self-policed | Requires a self-review system and self-inspection reports |

### 7.2 The Full Game-License Application Process (online game publication number)

**Prerequisites**:

1. Copyright: software copyright registration certificate (or copyright documents that meet the requirements); **the copyright owner must be a Chinese citizen or a domestically funded enterprise**.
2. Operating entity: business license + **ICP license** (Telecommunications and Information Services Business Operating License); the publishing unit must hold online-publishing qualifications (usually you file through a qualified publisher/agency).
3. Sufficient completeness: a runnable build, stable servers, complete content.
4. Content compliance: no prohibited content (the red lines: politics / religion / pornography / gambling, etc.); prepare the **full Chinese script text + a banned-word library**.

**Application flow**: prepare materials → submit to the **provincial publishing administration** → after provincial review and approval, report to the **National Press and Publication Administration** → approval → the approval document and game license are issued. (Imported games follow a separate "foreign copyright owner authorization" channel, with materials including the National Copyright Administration's approval of copyright contract registration, etc.)

**Main materials checklist** (subject to the latest official requirements): provincial request document, publishing application / application form, review report, copyright proof, business license + ICP license, game screenshots (≥10, including the main interface), full Chinese script text and banned-word library, anti-addiction system configuration description, review test accounts (high/mid/low level), demo video (including the healthy-game advice, combat demonstration, etc.), client/installer, etc.

**Timelines and cadence**: the statutory approval time is **80 working days** from acceptance (the provincial stage adds its own review time); in practice, from preparation to getting the number is measured in months (approval results are published monthly: https://www.nppa.gov.cn/bsfw/jggs/yxspjg/). **Plan the game license 6–12 months ahead**.

**Notes**: one application per game; major version changes require a change application; after launch, report operating information to the local authorities within the prescribed time.

### 7.3 Anti-Addiction and Real-Name Verification (mandatory)

- **System integration**: the **online-game anti-addiction real-name verification system** of the Publicity Department (National Press and Publication Administration): https://wlc.nppa.gov.cn/fcm_company/index.html. The flow: corporate registration → add the game (name / approval document number / ISBN) → channel binding → in-game real-name integration and data reporting.
- **Minor-protection rules** (adults are not restricted): play is allowed for 1 hour only on **Fridays, Saturdays, Sundays and statutory public holidays, 20:00–21:00**; **top-up limits**: under 8, no top-ups; ages 8–16, ≤50 yuan per transaction and ≤200 yuan per month; ages 16–18, ≤100 yuan per transaction and ≤400 yuan per month; guest mode must not offer payments or top-ups.
- Paid operation without a game license or without system integration is a clear violation (see Pitfalls & Anti-patterns §8).

### 7.4 Other Operating Qualifications

- **ICP filing/license**: file the website and server domains; paid operation requires an ICP license (one of the game-license materials).
- **Cybersecurity classified protection (MLPS 2.0)**: for systems with user data and networked services, complete classification filing and assessment as local requirements demand (especially for larger-scale products).
- **Network Culture Business License (wenwangwen)**: game-related approvals have gone through reforms; **whether you need to apply depends on the latest position of the local culture and tourism authority**.
- **Payment compliance**: in-app purchases go through WeChat Pay / Alipay / store IAP; do not circumvent the platform payment system (explicitly required for mini-games).

### 7.5 What You Can Do Before You Have a Game License

- Allowed: free testing (with no payments of any kind), pre-registration / wishlist operations, events / press exposure, paid-acquisition pre-testing (per platform rules).
- Not allowed: charging in any form (virtual payments / item sales / memberships); mini-game virtual payments require a game license; "selling test activation keys" also carries compliance risk (go by the regulator's position).
- The safe strategy: in mainland China go "free testing → monetize after the number is granted", while also evaluating **going overseas first** (overseas platforms do not require a China game license).

### 7.6 Overseas Release Flow

- The full overseas-platform flow is in §3–§5 of this playbook; no China game license is required, but you do need: age ratings for the target market (IARC/ESRB/PEGI), privacy compliance (GDPR/CCPA/COPPA), tax (W-8BEN/VAT), and store localization.

## 8. After Launch: Updates, Hotfixes and Service Shutdown

| Item | Key points |
| --- | --- |
| PC updates | Steam publishes instantly (pre-validate on the beta branch); Epic/GOG each have their own backends |
| Console patches | Every patch goes through certification (budget 1–3 weeks) |
| Mobile updates | Every update is reviewed again (budget 1–7 days); for hot updates, mind the platforms' prohibitive terms |
| Mini-game updates | Platform review (usually 1–3 days) |
| Shutdown plan | An advance notice period (some overseas jurisdictions have case-law requirements; in mainland China follow platform rules) + a compensation scheme + player data export options |

## 9. Common Review Rejections and Countermeasures

| Platform | Typical rejection reasons | Countermeasures |
| --- | --- | --- |
| App Store | 4.3 reskins/duplicates, 2.1 completeness, 3.1 circumventing IAP, 5.1 privacy | Provide a differentiation statement; submit only once completeness is up to standard; route all payments through IAP |
| Google Play | Data safety form mismatches, target API too low, permissions | Refill the form to match the data flows; upgrade the target API |
| Steam | Missing content survey (AI), asset specs | Answer truthfully; produce assets to spec |
| WeChat mini-games | Category/qualification mismatches, circumventing virtual payments | Have software copyright/game license ready; route payments only through virtual payments |
| General | Infringing assets (fonts/music/icons) | An asset ledger + licensing proof (Legal, Patents & Competition §2) |

## 10. Launch Checklist (final version)

- **Qualifications**: software copyright ✓ game license (mainland China) ✓ ICP (online games) ✓ trademark (recommended) ✓ rating questionnaire ✓
- **Documents**: terms of service ✓ privacy policy ✓ (matching the SDK data flows) content self-review report (mainland China) ✓
- **Store**: capsule/screenshots/trailer/all-language copy ✓ pricing and discounts ✓ release-date buffer ✓
- **Technical**: achievements/cloud saves/gamepad ✓ crash monitoring ✓ hotfix-process drills ✓ device-matrix testing ✓
- **Anti-addiction**: real-name system integration ✓ minor restrictions ✓ probability disclosure (if applicable) ✓
- **Emergency**: day-one hotfix plan ✓ support channel ✓ community announcement templates ✓
