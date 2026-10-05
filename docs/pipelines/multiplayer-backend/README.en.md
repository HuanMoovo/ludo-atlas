# Ludo Atlas · Multiplayer & Backend

> From "it can go online" to "it stays online, holds up under load, and resists attack": sync models, service layering, matchmaking, economy security, anti-cheat, and cost operations.
> Companions: Programming Handbook (networking fundamentals) · Live-Ops & Growth · Multi-platform Launch Playbook (the dedicated online-game licensing section) · Pitfalls & Anti-patterns.
> Premise: multiplayer is the technical choice with the largest "long-term operating cost". This document helps you pay less tuition on architecture; for the API details of specific frameworks, the official documentation is authoritative.

---

## 1. Start With Three Decisions

Architecture selection is essentially answering three questions:

1. **How many players share a session**: 2–8 (friend sessions), 8–100 (competitive matches), several hundred to a thousand (large worlds, siege battles) — the three tiers have completely different answers.
2. **Who is authoritative**: player machines (P2P, host authority) or servers (dedicated servers). For games involving economy, rankings or competitive fairness, the only possible answer is server authority.
3. **What it costs**: server costs rise linearly with CCU. Whether the business model (premium, IAP, ads) can carry that cost has to be calculated in advance.

| Scenario | Architecture | Technical points |
| --- | --- | --- |
| Friend co-op (2–8) | P2P or host authority + relay | Lowest cost; declare the cheating boundary up front |
| Competitive matches (5v5 and similar) | Dedicated servers, authoritative simulation | The trio of lag compensation, matchmaking and anti-cheat |
| Large scale (MMO/large worlds) | Partitioned servers + sharding | Zoning, mirrors, cross-server — the highest operational complexity |

## 2. Sync Models: Choose Right First, Optimize Later

- **State sync** (the mainstream): the server runs the authoritative simulation; clients send input and receive state. For game feel, clients predict (move locally first) and the server corrects the deviation. FPS, MOBA and action games essentially all take this route.
- **Lockstep (deterministic)**: only input commands are synced, and every client replays them through identical logic. RTS games, some fighting games and genres that need full replays use it. The engineering cost is that floating-point determinism (different hardware producing identical results) is extremely hard to guarantee, and reconnecting after a drop is hard too. Evaluate before choosing: does your gameplay really need it?
- **Rollback**: the fighting-game school (GGPO is the classic public implementation approach): save state snapshots, and roll back to recompute when a prediction is wrong. Excellent game feel and extremely high implementation complexity; suited to competitive games with a small state space.
- **Lag compensation stack**: client-side prediction, entity interpolation, server-side rewind checks (the source of the classic "killed after getting behind cover" phenomenon), input buffering. Each needs its own tuning; there is no silver bullet.
- **Two engineering iron rules**: decouple the logic frame from the render frame; layer the network apart from game logic. Violate either one and you will want to rewrite everything when tuning game feel later.
- **Network simulation is a development routine**: have built-in latency, jitter and packet-loss simulation toggles and flip them on while writing every multiplayer feature. Projects that only think about testing the network before launch always regret it.

## 3. Service Layering: A Checklist to Verify Against

A multiplayer game that can actually be operated splits roughly into these service layers (in the order you build them):

1. Accounts and authentication (platform accounts + your own account system, replay protection)
2. Sessions: lobby, rooms, parties, invites
3. Matchmaking (see §4)
4. Game servers: the authoritative simulation itself
5. Leaderboards and stats (server-verified)
6. Cloud saves (server as source of truth, client as cache)
7. Social: friends, recent players, chat/voice (a compliance minefield; see the Multi-platform Launch Playbook)
8. Economy and inventory (server-authoritative; see §6)
9. Anti-cheat and risk control (see §7)
10. Operations backend: bans, compensation, announcements, event toggles

Layering principle: deploy stateless and stateful services separately; decouple game servers from peripheral services (game servers only simulate; everything else goes through the periphery). Then scaling or restarting any single layer does not drag the whole system down.

## 4. Matchmaking

Matchmaking is a machine for trading off experience quality against wait time. Its elements:

- **Rating and ranks**: MMR/ELO-style rating systems; separating hidden rating from displayed rank is common practice.
- **Constraints**: region and latency caps (players above the latency threshold do not get matched together), party logic (separate pools for premades and solo queue).
- **Wait-time management**: progressively relax constraints as wait time grows (expand the search range in stages) — do not make skilled players wait ten minutes.
- **Pool discipline**: newbie pools, anti-cheat isolation pools and mode pools all need to exist, but do not over-segment — once the population is diluted, everyone is waiting.
- **Off-peak filling**: bots covering empty slots can save the experience, but manage expectations — do not let players feel deceived.
- **Implementation path**: small teams build a simplified "queue + rating function" first, and evaluate open-source matchmaking frameworks such as Open Match once it runs.

## 5. Backend Service Selection

| Option | Representative | Suited to | Watch out for |
| --- | --- | --- | --- |
| All-in-one open-source backend | Nakama | Small and midsize teams: accounts, matchmaking, leaderboards, storage and cloud functions in one stop | Self-hosted or a managed version |
| Room-based realtime framework | Colyseus | Room-based competitive and co-op gameplay | The state-sync model leans toward rooms |
| Game server orchestration | Agones + Open Match | Teams with K8s capability; dedicated server fleets | The ops bar is not low |
| Commercial BaaS | Photon, PlayFab and similar | A fast start without touching ops | Long-term cost and platform lock-in |
| Fully in-house | Build your own | Large teams, special requirements | Be cautious; exhaust off-the-shelf options first |

The realistic advice for small teams: **start from an all-in-one open-source solution** (Nakama or Colyseus and the like), prove out the gameplay first, and only then discuss building your own. Do not build the whole in-house stack in version one — that is solving the most uncertain problem in the most expensive way.

## 6. Leaderboards and Economy Security

- **Leaderboards**: scores must be server-verified (replaying the match for validation is the strongest tier) to prevent tampered uploads. Pagination, caching and seasonal resets all need design.
- **Economy system**: all currency and item changes are server-authoritative; random numbers are generated server-side; every transaction has an audit log; risk-control rules watch for "abnormal flow rates" (a year's worth farmed in one minute).
- **Saves**: checksums or signatures against tampering; decide the arbitration rule for cross-device conflicts in advance (server as source of truth is the default answer).
- **Mindset**: design version one of the economy on the assumption that it will be attacked. Adding security after launch is handing the holes to the black market first.

## 7. Anti-Cheat in Practice

A three-layer structure — missing any one layer leaves it incomplete:

1. **Client-side detection**: file integrity checks, memory scanning, driver-level solutions (the most invasive; be cautious). Its job is to keep amateur cheaters out.
2. **Server-side analysis**: behavioral statistics and anomaly detection (hit-rate distributions, input frequency, economy flow rates, movement patterns). Only this layer can handle professional cheaters.
3. **Reports and manual review**: player reports + supporting data + human judgement. Ban mechanisms should be tiered (observe, warn, ban), and an appeal channel for false bans is a must.

Principles and red lines:

- For anything the server can verify, never trust the client.
- Detection needs data backing; the reputational cost of a false ban is far higher than that of a missed one.
- Protocol encryption and version checks to prevent private servers; replay protection on the login channel.
- The reality in China: the cheat industry chain is mature, and the anti-cheat budget is a function of commercial scale — do not estimate it as a "moral issue"; legal measures (civil litigation) are a combination that has appeared in public reports.
- Publish the ban policy: only transparent rules keep order — and preserve your ability to defend your decisions.

## 8. Cost and Operations

- **Cost model**: peak CCU × per-match resource usage; bandwidth estimated from sync frequency and message size; build this table first, then talk business model.
- **Elastic scaling**: game servers are stateful services, so scaling down has to wait for matches to end — the plan must account for it.
- **Observability**: latency percentiles (P50/P95/P99), disconnect rate, matchmaking duration, error rate — these four metrics first; logs and tracing follow.
- **Hot-update capability**: being able to update the server without downtime is the lifeline of operations; design to that standard from version one.
- **Load testing**: bot swarms to stress matchmaking and game servers; run chaos drills before release (kill nodes, cut the network).

## 9. Pre-Launch Checklist

1. Measured latency: latency distributions on real devices and real networks in the target market.
2. Reconnection and crash-recovery paths all work end to end.
3. Matchmaking duration is acceptable in every time slot (including the bot strategy at off-peak).
4. Can leaderboard score validation be broken by attack testing (a security teammate simulating tampered packets)?
5. Economy audit logs complete; rollback tools available.
6. Ban and appeal backends available.
7. Server alerts and an on-call schedule in place.
8. A hot-update drill has been run.
9. Compliance: chat/voice content moderation, real-name registration and anti-addiction (mainland China; see the Multi-platform Launch Playbook).
10. Cost stress test: assume concurrent players triple — can the bill and the architecture take it?

## 10. Common Pitfalls

1. Client-authoritative economy or leaderboards: exploited by everyone from day one.
2. Network code coupled with logic: tuning game feel drives you to despair.
3. Testing only on the LAN: real-network behavior unknown.
4. No reconnection: mobile-network players all wiped out.
5. Over-segmented matchmaking pools: a diluted population leaves everyone waiting.
6. Anti-cheat only at the client layer: advanced cheaters walk all over you.
7. No appeals for false bans: community trust collapses.
8. Cost model pulled out of thin air: when the user base grows, you lose money instead of making it.
9. No server hotfixing: one typo in an announcement takes the service down for half an hour.
10. Saves stored only locally: save editors will humble you.
11. Replay/spectator support reserved too late: it cannot be added when you go esports.
12. Forgetting the anti-cheat pool: normal players and cheaters share one pool — a lose-lose.

## 11. Further Reading

- Nakama (open-source all-in-one backend): https://heroiclabs.com/
- Colyseus (room-based realtime framework): https://colyseus.io/
- Agones (K8s game server orchestration): https://agones.dev/
- Open Match (open-source matchmaking framework): https://github.com/googleforgames/open-match
- Photon: https://www.photonengine.com/
- PlayFab: https://playfab.com/

> More backend, analytics and anti-cheat entries are in Resources §2.5; for legal measures and compliance see Legal, Patents & Competition and the Multi-platform Launch Playbook.
