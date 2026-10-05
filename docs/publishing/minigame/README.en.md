# Ludo Atlas · Mini-Game Development

> Hands-on practice for the mini-game ecosystem centered on WeChat and Douyin: engineering constraints, platform capabilities, monetization design, paid acquisition and review.
> Companions: Multi-platform Launch Playbook §6 (qualifications and process) · Live-Ops & Growth · Pitfalls & Anti-patterns.
> **Timeliness statement**: mini-game platform rules change frequently; the facts in this document were verified as of 2026-10. Check the platforms' latest official docs before you touch package-size limits, fee rates or payment policy (entry points in §10).

---

## 1. What Kind of Business Mini-Games Are

Mini-games are a "tap and play" game form that runs inside super-apps, with no install step. The core differences from app games:

| Dimension | Mini-game | App game |
| --- | --- | --- |
| User acquisition | Platform traffic pools (social/content recommendation) | App stores + paid acquisition |
| Package size | First package in the 4MB range, total package in the 20-30MB range | Hundreds of MB and up |
| Technical environment | JS/WASM runtime, capabilities limited by the platform | Native, close to unlimited |
| Monetization | Ads (IAA) first, in-app purchases (IAP) second | In-app purchases first |
| Lifecycle | Short and fast; day-one data decides its fate | Long-term live-ops first |

The essence of mini-games is a traffic business plus lightweight content. Teams used to App or PC development entering this space are most likely to underestimate two things: the hard constraint on package size, and the brutal cadence of "if day-one retention is low, you can never buy users again".

## 2. Platforms at a Glance

| Platform | Traffic source | Monetization | Entity and qualifications |
| --- | --- | --- | --- |
| WeChat mini-games | Social streams (sharing/groups), search, the mini-game center | IAA + virtual payments | Individual entities can publish free (ad-based) games; paid games require a corporate entity + a game license |
| Douyin mini-games | Content streams (short video, livestream attachment) | IAA + virtual payments | Corporate entity, software copyright; (virtual payments require) a game license |
| Kuaishou mini-games | Content streams; a user base that differs from Douyin's | Same as above | Same as above |
| Hardware channels (Xiaomi/OPPO/vivo and others, including the Quick Game Alliance) | Mini-game entries inside app stores | IAA + channel payments | Per-channel rules; most require software copyright |
| Overseas Web (Poki, CrazyGames, etc.) | The platforms' organic traffic | Ad revenue share | No mainland-China game-license requirement; see Multi-platform Launch Playbook §7 |

Work out first which kind of traffic suits your content: share-driven (WeChat), content-driven (Douyin/Kuaishou), or search- and editorial-driven (hardware channels). The same game needs a completely different distribution strategy on each platform.

## 3. Engineering Red Lines: Package Size and Performance

### 3.1 Package-size limits (verified as of 2026-10)

| Platform | Main package (first package) | Total package | Notes |
| --- | --- | --- | --- |
| WeChat mini-games | No more than 4MB | Main package + subpackages no more than 30MB in total | A single ordinary subpackage has no size limit; a single independent subpackage no more than 4MB |
| Douyin mini-games | No more than 4MB | No more than 20MB overall | A single subpackage no more than 20MB |
| Hardware channels (rpk standard) | No more than 4MB | No more than 30MB in total | The Quick Game Alliance standard; Cocos/Laya/Unity export supported |

The engineering implication is one sentence: **put only what startup needs in the first package; everything else goes through subpackages and the CDN**. First-package size directly determines cold-start download time, and every extra second of cold start produces visible drop-off.

### 3.2 Subpackaging and asset strategy

- Split subpackages by gameplay stage: startup package, core-gameplay package, late-game content package — downloaded while playing.
- Large assets (textures, audio) go through the CDN, with compression (gzip/brotli) and a caching strategy.
- Weak-network and first-download cases need progress display; cover the wait with a splash screen or a small looping animation.
- Do asset version management: a cache hit serving old-version assets is a common source of mini-game production incidents.

### 3.3 Performance and adaptation

- **Memory** is the mini-game's biggest enemy. On low-end Android devices, exceeding the memory limit crashes the app outright, and it is hard to reproduce. Watch the memory curve on a real device (not a simulator).
- **Rendering**: WebGL capabilities are limited; handle texture sizes and compression formats as the platform requires; budget DrawCalls and particle counts for low-end devices.
- **Adaptation**: screen ratios vary wildly; leave safe areas for notches and rounded corners; touch hot zones should be a size larger than the visuals; the game must recover when switching back from the background.
- **Audio**: autoplay policy restrictions are everywhere; the first sound effect needs unlocking after the player's first interaction.
- **Debugging**: WeChat DevTools and Douyin DevTools both support real-device preview and performance panels. Test on real devices, and on at least one low-end device.

### 3.4 Engine routes

| Engine | Route | Notes |
| --- | --- | --- |
| Cocos Creator | Native export support | The most mature option for the Chinese mini-game ecosystem; plenty of docs and case studies |
| LayaAir | Native export support | Also a Chinese engine, with deep accumulation in the mini-game direction |
| Unity / Tuanjie Engine | Conversion solution | Official conversion solution: `minigame-unity-webgl-transform` (WeChat); Tuanjie Engine supports Douyin mini-game export directly |
| Native JS/TS | Hand-written or a lightweight framework | Suited to ultra-light gameplay; the most controllable package size |

Assessment points for converting a Unity project to a mini-game: package size (WebGL build size), memory peak, third-party plugin compatibility (plugins containing native code are not usable). The conversion solution has an official compatibility-assessment process — assess before committing.

## 4. Platform Capability Integration

- **Login**: use the platform's account system for silent login; get guest mode running first, and guide binding when needed.
- **Sharing/forwarding**: WeChat's sharing chain is the core spread engine, but share designs should be gameplay-driven (showing off scores, asking for help, bragging) — don't abuse the "share to revive" pattern; it gets you penalized and hurts retention.
- **Leaderboards**: WeChat relationship-chain leaderboards are implemented through the open data domain; you can also build your own global leaderboard.
- **Cloud saves**: platform cloud capabilities (e.g. WeChat Cloud Development) or your own server-side; settle the save-conflict policy in advance.
- **Ad components** (the substance of IAA): rewarded video (the player opts in and gets a reward), interstitial (pops up in gaps), banner (a persistent small strip), native template. Rewarded video is the revenue mainstay; go easy on interstitials and banners — they are the main source of negative reviews.
- **Virtual payments (IAP)**: an important update is that the iOS channel is now open. At the end of 2025 Apple introduced the "Mini Apps Partner Program" and WeChat officially announced integration with iOS virtual payments — the history of "iOS can't do virtual payments, route users to external payments" is definitively over. Key points: virtual payments require a game license and a corporate entity; the fee structure (including Apple's share and the platform service fee) follows the latest official announcements; the various workaround schemes of the past are now non-compliant — stop using them.
- **Enabling capabilities**: on the WeChat side, enable them on demand through the "capability map" on the WeChat public platform; on the Douyin side, apply on the Open Platform. Don't leave it to the day before launch to discover a capability was never enabled.

## 5. Monetization Design

- **Rewarded-video cadence**: place it at "the moment the player just wants it" (revive, double, unlock, bonus top-up) — highest conversion, least damage to the experience. Frequency control matters more than placement: 2-3 times per session is the common safe line.
- **Hybrid monetization**: IAP for ad removal, packs and passes; IAA for day-to-day revenue. Keep a clear primary/secondary order, or the two value systems fight each other.
- **Data model**: watch day-1 and day-7 retention, average time per user, eCPM, LTV. If the numbers are poor, tune fast — mini-games offer no window for "slow work, fine craft".
- **Two classic routes**: the social-virality type (one big wave, betting on spread, like the Sheep a Sheep-style mass phenomenon) and the long-term IAA casual type (steady updates, rolling on paid and organic traffic). The two demand completely different capabilities — choose before you invest.

## 6. Review and Compliance

Consistent with Multi-platform Launch Playbook §6; here are the additions from the mini-game angle:

- **Qualifications**: software copyright is the baseline; enabling virtual payments requires a game license; on WeChat, free (pure-ad) games can be published by individual entities, while paid games require a corporate entity. Game-license processing is measured in months — schedule it into the development plan.
- **Anti-addiction and real-name verification**: companies enabling virtual payments must complete corporate registration and game binding in the real-name system and sync it with the platform (entry points in Multi-platform Launch Playbook §6.1).
- **Content review**: the category choice is made once and cannot be changed; name, icon, screenshots and gameplay description are all reviewed; lottery-style designs (undisclosed odds, cash-exchangeable structures) are a heavily policed no-go zone.
- **Privacy**: minimize user-data collection; integrate the privacy policy using the platform templates; don't take data you shouldn't.

## 7. Paid Acquisition and Live-Ops

- **Douyin side**: short-video creatives are the ammunition. Creative iteration speed sets the ceiling on media buying; prepare 10+ creative variants to A/B for the same gameplay. Livestream attachment suits gameplay with something to show. Judge the ad model by ROI — cut anything below the day-one break-even line.
- **WeChat side**: social virality (share-motivation design), WeChat Search keywords, mini-game center recommendation slots. Virality must be driven by real value (showing off scores, friends helping each other); forced sharing gets you penalized.
- **Version cadence**: weekly content or events to keep the motivation to come back. Mini-game users forget far faster than app users.
- **Data dashboard**: new users, retention (1/3/7-day), session time, eCPM, ARPU, LTV, share rate. Every metric should map to a lever you can pull; don't watch metrics with no corresponding action.

## 8. Launch Checklist

1. Qualification materials complete (software copyright/game license/entity info); real-name and anti-addiction integration done.
2. First-package size within limits; cold-start time measured and passing on real devices (low-end device).
3. All ad placements checked: frequency, occlusion, accidental-touch review.
4. Sharing chain verified end-to-end on real devices (Android + iOS).
5. Privacy policy and data-collection list checked.
6. Submission materials: name, icon, screenshots, gameplay description, qualification documents.
7. Run a gray release or trial build first, collecting crashes and blockers.
8. Daily dashboard patrol for the first week after launch.

## 9. Common Pitfalls

1. Estimating package size with app thinking; the first package goes over the limit and work has to be redone.
2. Testing only in the simulator; the crash rate on low-end devices explodes.
3. Old tutorials still teach you to "route around iOS payments" — following them is non-compliance.
4. Rewarded-video placements too dense; retention and ratings both tank.
5. Share design turns forced; the platform penalizes you.
6. The wrong category is picked, and after launch it cannot be changed.
7. The game license was never scheduled; everything is ready but the qualifications.
8. Not watching the real-device memory curve; mysterious crashes after launch.
9. Chaotic asset cache versions; users get old-version content.
10. The first-sound-effect unlock is forgotten; the game launches silent.

## 10. Official Entry Points and Docs

- WeChat mini-game development docs: https://developers.weixin.qq.com/minigame/dev/guide/
- WeChat mini-game subpackage loading (the official statement on package-size limits): https://developers.weixin.qq.com/minigame/dev/guide/base-ability/subPackage/useSubPackage.html
- WeChat iOS virtual payment docs: https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/virtual-payment/ios.html
- Unity WeChat mini-game conversion solution (official repository): https://github.com/wechat-miniprogram/minigame-unity-webgl-transform
- Cocos Creator publishing to Douyin mini-games: https://docs.cocos.com/creator/4.0/manual/zh/editor/publish/publish-bytedance-mini-game.html
- Douyin Open Platform (mini-games): https://developer.open-douyin.com/

> More Chinese channel entry points in Resources §2.7 (publishing platforms); the full qualifications and anti-addiction flow in Multi-platform Launch Playbook §6.
