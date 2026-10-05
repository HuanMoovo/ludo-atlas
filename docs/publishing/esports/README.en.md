# Ludo Atlas · Esports & Competitive Design

> Competitive design, spectator systems, balance methodology, how to judge the tournament ecosystem, and the practical requirements for running events in China.
> Companions: Multiplayer & Backend (matchmaking and anti-cheat) · Live-Ops & Growth · Legal, Patents & Competition · Multi-platform Launch Playbook.
> One-sentence premise: esports amplifies a successful game, but it cannot make an unsuccessful game successful.

---

## 1. Separate Three Things First

"Doing esports" is actually three completely different jobs:

1. **Making a game with competitive play**: a design-level job, covered in §2 to §4 of this document.
2. **Running official tournaments**: a business and marketing-level job — a cost center or a marketing tool, not a revenue line (for the game company).
3. **Plugging into the third-party tournament ecosystem**: a community and licensing-level job, the lightest of the three, and the one that most depends on your game being popular in its own right.

The order of judgment is always: get the gameplay to stand up first → a competitive population forms naturally → only then consider tournaments. Skip the first two steps and force a tournament anyway, and loneliness is what you'll be running.

## 2. Competitive Design

The foundation of competitive games comes down to four words:

- **Fairness**: symmetric competition is the most stable (same characters, same rules); asymmetry (different characters with different abilities) has more personality, but balance difficulty rises multiplicatively — if you go that route, be ready for long-term tuning.
- **Depth**: the decision space must be "easy to learn, hard to master". Depth comes from interactions between systems, not from an execution barrier. Depth piled up out of raw speed shuts spectators and most players out together.
- **Clarity**: spectators can tell what is happening within 3 seconds. Information presentation (VFX, sound, UI) must let an outsider see "who's ahead, who's about to die, who's putting on a show". This is the first gate of watchability.
- **Suspense**: the existence of comeback potential. The harder the snowball rolls, the worse the watchability; leave the weaker side a counterplay path and people will watch the match.

Version stability is the implicit fifth word: esports players build muscle memory and tactical libraries version by version, and major mid-season overhauls are taboo. Concentrate adjustments in the window between the end of one season and the start of the next.

## 3. Spectator System: An Engineering Checklist

Spectating is not "just add another camera" — it is an entire product:

- **Observer camera**: free camera, player follow, first-person / tactical view switching, multi-feed picture-in-picture. Directors need "the ability to cut to any fight in progress at any moment".
- **Director system**: automated directing (picking focus by rules or algorithms) plus manual intervention. A must-have for large-scale tournaments, or the director can't keep up.
- **Spectator information layer**: the "spectator version" of health, economy, ability cooldowns, and win-rate curves. Information that players can't see must be visible to spectators — that is the value of a broadcast.
- **Replay system**: full replays, keyframe jumping, clip export. Replays are both a training tool and a content production tool (highlight reels, reviews, and tutorials are all grown out of them).
- **Data interfaces**: a real-time data stream output to broadcasters (scoreboards, charts). A requirement of professional broadcasts — reserve the API early.
- **Observer delay**: balancing anti-cheat (preventing screen-peeking) against stream delay; decide the approach in advance.
- **Technology choice affects replays**: frame sync (deterministic) makes replays easy; state sync relies on snapshots and input replay. **Replay capability must be reserved at the architecture stage — retrofitting it later costs enormously.**

## 4. Balance Methodology

- **Data-driven**: watch win rates, pick rates, ban rates, and rank distribution. Beware small samples (data from the first three days of a new version is basically noise) and survivorship bias (high-rank data does not represent the mass experience).
- **Balance philosophy**: absolute balance does not exist, and shouldn't be pursued. The goal is a "diverse meta": as many playstyles as possible should have a place. Show the pros a "boring but balanced" solution and they will teach you how to tear it apart.
- **Order of adjustments**: change numbers first, change feel with caution. Number changes can be rolled back; retraining the muscle memory of feel is costly, especially at the pro level.
- **Channels and transparency**: feedback channels for high-rank players and pros must exist; the reasoning behind changes must be written clearly in announcements. The feeling that "the designers are teaching you how to play" usually comes from changing without explaining.
- **Version freeze**: lock the version before a major tournament — a basic form of respect for the players and the event.

## 5. The Tournament Ecosystem

- **The ranked ladder is the foundation**: every tournament player grows out of ranked play (see the matchmaking and tier design in Multiplayer & Backend). If the ladder is unhealthy, the ecosystem is a castle in the air.
- **Official tournaments**: prize pools, formats (leagues / cups / invitationals), online and offline, venues, broadcast production. The whole pipeline is event operations plus the broadcast industry, and neither the money nor the people come cheap.
- **Third-party tournaments and licensing**: organizers need your authorization (a tournament content licensing agreement). How far to license is a strategic choice: fully open licensing (the ecosystem grows fast, quality varies) versus strict control (quality is controllable, growth is slow). Most companies take the middle route of "tiered licensing + applications through an official platform".
- **Clubs and players**: contracts, transfers, youth training, and salary structures carry many legal points (see Legal, Patents & Competition), and IP ownership of accounts and content is especially dispute-prone (ownership of a player's social media accounts is a high-frequency point of contention in the industry).
- **Broadcasting and platforms**: cooperation with streaming platforms is the main channel for reach; broadcast rights and derivative-work licensing terms should be settled in advance.

## 6. The Actual Situation in China (statements verified in 2026-10; before you act, the competent authorities' requirements prevail)

- **Status**: esports became an official competition event for the first time at the 2023 Hangzhou Asian Games, and the Chinese team finished with 4 gold medals (Xinhua News Agency report); the industry's public image and policy environment have turned positive overall.
- **Tournament regulation**: international esports tournaments hosted or co-hosted by the Sports Information Center of the General Administration of Sport of China must be submitted for approval through the prescribed process; approval/record-filing requirements for other tournaments **follow the rules of the sports authority of the host locality** (they vary from place to place — some cities require an application and approval, some only record-filing, and some have no special requirements); before running an event, always check the local requirements.
- **Performance and large-scale events**: offline tournaments have the nature of performances; the organizing entity usually needs qualifications such as a Commercial Performance License, and must obtain cultural, fire-protection, and public security permits as required locally; if the audience reaches the size standard for a large-scale event (e.g., a thousand people or more), a public security safety permit is also required.
- **Games used in tournaments**: games used in official matches in mainland China must be products that have obtained a game license number and can be operated legally; the operator qualifications for esports content (online publishing, ICP, etc.) fall under the same system as game operations (see the Multi-platform Launch Playbook).
- **Players and clubs**: tournaments under the sports system require players to be at least 18 years old; there is a registration system for clubs and players (registration is voluntary, but only registered parties may take part in tournaments approved by the sports system).
- **Streaming compliance**: the words and actions of players and streamers are bound by multiple layers — platform rules, industry norms (such as documents like the Code of Conduct for Esports Streamers), and the law.

## 7. When Not to Do Esports

- The daily active population can't support ranked matchmaking (if even a match takes five minutes to find, tournaments are out of the question).
- Poor watchability: spectators can't understand it, can't see it, or don't want to watch.
- The team has neither the capacity for event operations and broadcast production, nor the budget to outsource it.
- Treating esports as a lifeline: it only amplifies results, it cannot create them.

## 8. Common Pitfalls

1. Planning tournaments before the gameplay has taken hold.
2. The replay system was not reserved at the architecture stage, and it can't be retrofitted once you want to run tournaments.
3. Director tools are missing, so tournament broadcasts rely on people manually cutting between camera feeds.
4. Major version overhauls mid-season, and the players' collective morale explodes.
5. Balancing only by pro data, and the mass experience collapses.
6. A one-voice licensing policy, and the third-party tournament ecosystem never grows.
7. Offline-competition qualifications and permits not obtained, and the event gets shut down.
8. Sloppy player contracts, leaving landmines in account and content ownership.
9. Anti-cheat falls short, and the top of the ladder is all cheats (see Multiplayer & Backend).
10. Treating the tournament budget as loose change from the marketing budget, and putting on an event that is neither fish nor fowl.

## 9. Further Reading

- Matchmaking and anti-cheat: Multiplayer & Backend.
- Contract and IP essentials for tournaments and clubs: Legal, Patents & Competition.
- Large-scale event compliance: the relevant chapters of the Multi-platform Launch Playbook; for specific procedures, confirm with professional legal counsel.
