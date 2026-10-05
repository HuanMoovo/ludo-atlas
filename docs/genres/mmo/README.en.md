# Ludo Atlas · Genre Handbooks · MMO

> **Genre Handbooks · Volume 3**. Positioning: turning "many people living in the same world for a long time" into a product. Gameplay is the entrance; community, economy and continuous operations are the body itself — as long as the servers are running, the world must keep giving people a reason to come back.
> Companions: Multiplayer & Backend · Live-Ops & Growth · Programming Handbook · Indie Survival.

---

## 1. Positioning and Core Loop

In one line: an MMO is a product form, not a gameplay genre. Turn-based, action and shooter gameplay can all fit inside the MMO shell; what decides success is not how combat is built but **whether a continuously running world can carry three long-term bills at once**: servers, operations and content.

**A word of discouragement first.** If any one of the three costs below is beyond you, do not start an MMO:

- **Servers**: running 24/7; bandwidth, databases, on-call shifts and customer support are billed by the month; a world whose servers are shut down is a negative asset — there is no "build it first and see" tier.
- **Operations**: events, announcements, community, anti-cheat and crisis communications are standing roles; most MMO incidents are operations incidents, not technology incidents.
- **Content**: players consume content several times faster than it is produced; the moment updates stop, the population starts to bleed away; the content pipeline is a perpetual construction project.

In one line: an MMO is building a city, not building a game project. Small teams drawn to the online world should read the alternatives in §5 first.

The core loop is measured per login session, and the long game in months and years:

`log in or return → do what today allows (quests, dungeons, gathering, socializing) → get stronger, get richer, be seen → spend and display (trading, guild events, cosmetics) → set a new goal → come back tomorrow`

Three interlocking systems sit inside this loop; with any one missing it degenerates into a single-player game plus an online lobby: progression handles "getting stronger", the economy handles "getting richer", and socializing handles "being seen".

Drawing boundaries against neighboring genres:

| Neighboring genre | The boundary |
| --- | --- |
| Single-player RPG | A single-player world's value does not depend on others being online; an MMO without live players is a dead world |
| Small-scale online (co-op, competitive, party) | Room-based and per-match, can end at any time; an MMO is a persistent world that keeps running while players are offline |
| MOBAs and battle royales | They also have seasons and account accumulation, but each match restarts among strangers, which does not amount to "living there" |
| Survival and sandbox multiplayer (self-hosted) | They also have persistent worlds, but the servers are built and run by players, at small scale, with no official live-ops commitment |

Self-check: does your design contain moments where "other people are on, so I have to be there now"? If not, what you should build is small-scale online (§5).

## 2. Player Experience Goals and Benchmark Titles

Experience goals (in priority order):

1. **Belonging**: a guild, a regular party, names you recognize; leaving makes you miss it, and someone will call you back.
2. **Accumulation**: months to years of progress visible at a glance; gear, titles and housing are all evidence of time.
3. **Presence**: people in the main city, voices in the channels, events in the world; an empty world is a veto against an MMO.
4. **Expression**: appearances, titles, mounts and housing are the social business card you show to others.
5. **Goal density**: at any hour you open the game there is something to do, and the portions are tiered (ten minutes, one hour, a whole evening).

Benchmark titles (widely known works only; play them yourself before breaking them down):

| Title | What to learn from it |
| --- | --- |
| World of Warcraft | The organizational shape of raids and guilds; the expansion-style version cadence |
| Final Fantasy XIV | Main-story-driven staging in large-scale raids; turning casual gameplay into a permanent content library |
| Fantasy Westward Journey | A long-term stable sample of a trading system and an official trading platform |
| JX Online 3 | A cosmetic economy and Chinese-style community operations; event beats coordinated with the version cadence |
| Sky: Children of the Light | The boundary of the lightweight social MMO: weak stats, strong expression, designs built on strangers' goodwill |

## 3. Design Essentials

### 3.1 World Shape: Decide "How Many People Live Together" First

The key number is live-player density, not map area. Three questions to answer first: how many people a single instance (a server or a channel) can carry, the probability that players encounter each other, and whether cross-server interaction is allowed.

| Shape | Approach | Cost |
| --- | --- | --- |
| Split servers | Players each choose a server; servers are isolated from one another | Socializing has a "neighbor" feel, but late-stage you face dead servers and server merges |
| Channels (mirrors) | One map runs several mirrored instances, and a full channel automatically diverts | Great for peaks; the cost is that people in the same place may not see each other |
| Single shared world | The whole server on one map, or seamless zoning | Strongest for competition and trade; highest engineering and governance complexity |
| Cross-server | Limited interaction for dungeons, battlegrounds or trading | Relieves late-stage dilution; the cost is more complex consistency and isolation rules |

Set population targets by phase: use channels to shave the launch peak, preserve encounter probability in the main city and strongholds during the steady phase, and keep the endgame alive with cross-server features, server merges or instance compression. Waiting until the server is empty to rescue it is the most expensive rescue there is.

### 3.2 The Social Skeleton: Guilds, Parties and Channels

Socializing is not a chat box; it is organization. The three pieces each answer one question:

| System | Question it answers | Common practice |
| --- | --- | --- |
| Friends and recent teammates | How to find people, and how to find them again | Friends lists, recent parties, following and blocking |
| Guilds | What reason keeps everyone bound together long term | Tiered permissions, guild channels, shared goals (dungeons, events, wars), contribution and distribution |
| Parties and dungeons | How things one person cannot do get done | Dual tracks of matchmaking and fixed groups; difficulty tiers that cover different group sizes |

The core of a guild is its distribution system: personal loot and point- or contribution-based distribution each have trade-offs, and the rules must be enforceable at the system level, not by moral suasion. Guild tools (announcements, event calendars, recruitment boards) decide organizing costs — the lower the cost, the higher the guild survival rate.

The negative side of socializing matters just as much: blocking, reporting, muting and support channels must all be complete; social friction accumulates on a monthly scale, and one mishandled incident will be remembered in trust terms for a long time (Live-Ops & Growth §8).

### 3.3 Trading and Markets: Keep Items Flowing

Settle three things first:

- **Binding rules**: account-bound, bind-on-equip or freely tradable; how tight or loose they are decides economic activity and the room for black markets — the freer the economy, the more security investment it needs (Multiplayer & Backend §6).
- **Channels**: face-to-face trading helps socializing but relies on manual matching; player stalls impose location and online requirements; the auction house is efficient but flattens price spreads and the value of place. The mix of the three is your economic shape.
- **Taxes and fees**: the auction tax is both a pricing tool and a currency sink; tune the rate to the economy's temperature (§3.4).

Monitor three metrics: median transaction price by category, listing volume and unsold rate, and holder concentration in large trades. Anomalies in price and concentration need automatic alerts, not a wait until players post screenshots and start shouting.

### 3.4 Economy and Inflation Control

An MMO is an open economy: both the faucet and the sink need an outlet, and the sink must grow in step with the faucet.

| Link | Common practice | Risk |
| --- | --- | --- |
| Faucet | Quests, drops and gathering, with daily output caps | Runaway output creates inflation directly |
| Sink | Repair fees, teleport fees, taxes, consumables, cosmetic spending | Insufficient sinks mean currency depreciation and soaring prices |
| Adjustment | Tune tax rates and shop buy-back prices by the metrics; run limited-time sink events | Make hard adjustments slowly; fast ones get you yelled at |

Three must-watch dashboards: currency held per player (look at the distribution, not a single point), a price index for core goods, and currency velocity (output and sinks per character per day). When inflation flares up, plug the faucet leaks first, then channel it with sinks and events; number tuning comes after every other tool.

The chronic disease is that newcomers cannot afford anything and veterans want for nothing: continually re-anchoring demand (new-version materials and cosmetics) is more workable than freezing the money supply. Black markets bleed the economy — real-money trading (RMT), gold-farming studios, stolen-account fencing — handle them with a combination of audits, risk controls and legal action (Multiplayer & Backend §6, §7).

### 3.5 Content Cadence: The Update Schedule of a Live Product

An MMO's launch is the starting line, not the finish. Updates usually come in three layers: major versions (expansions, measured in years), mid-size versions (dungeons and new systems, measured in quarters) and events (holidays, limited-time modes, crossovers, scheduled by month or by calendar beat). Stack the three and you have the live-ops calendar; for the method see Live-Ops & Growth §5.

- Content consumption always outpaces production; the structural condition is excess demand. Slow it down with repeatable content (dungeons, battlegrounds, collections), random affixes, alt-class replays and seasonal resets; speeding up production only takes more people and more money.
- Daily and weekly quests bring players back; long-term goals make them stay. Keep dailies few, short and backlog-friendly; bind players into clocking in for work and six months later the bill comes due all at once.
- Every major version is also an entry point for new players: new maps and new narrative are the reason to reintroduce the world.

### 3.6 Newcomers and Catch-Up: Let Late Arrivals In

The more old content there is, the more newcomers feel like they are climbing a mountain of legacy. Three layers of design:

- **Catch-up channel**: experience bonuses, level boosts and catch-up gear that put a newcomer's starting point next to the current version; catch-up speed must beat veterans' accumulation speed, or the entrance silts up until it is shut.
- **Veteran–newcomer incentives**: mentorship systems and comeback invites, turning veterans' leftover social warmth into newcomer retention.
- **Tiered access**: compress mandatory content to the shortest possible, convert old areas into optional collections, and keep newcomers from mistaking "catching up on homework" for the entire experience.

The goal: a newcomer hits the current version's core set pieces on their first evening, and meets at least one person willing to talk back.

## 4. Technical Essentials

The difficulty concentrates in four places: world services, economy security, live-ops tooling and cost. For sync models and architectural skeletons see Multiplayer & Backend and Programming Handbook §5; only the MMO-specific parts are listed here.

**World services**

- Server authority is the default answer: position, combat, drops and currency are all computed on the server, and the client only renders and predicts (Multiplayer & Backend §2).
- The standing capabilities of a stateful world: sharded data loading, cross-map migration, reconnection after disconnect, and crash rollbacks. Rollback granularity and compensation tooling must be designed in advance, not invented on the scene of the first incident.
- The on-screen budget is a hard constraint: main-city reward handouts, world events and siege battles are the most likely to blow the frame budget; shave the peaks with channels, mirrors, population caps and tiered effects.
- Login queues are more dignified than crashes: prepare capacity for launch day and update day at a multiple of the expected peak.

**Economy and security**

- Every increase or decrease of currency and items needs an audit log; random numbers are generated server-side; set risk-control rules for anomalous flow (per-account output, cross-account transfers) (Multiplayer & Backend §6).
- Trading and mail are the two main fencing channels; both need snapshot, trace-back and freeze tools.
- Deploy anti-cheat in three layers (client detection, server analysis, report review); economic crime and cheating are often the same people (Multiplayer & Backend §7).

**Live-ops tooling**

- The GM and live-ops console is the cockpit: bans, compensation, announcements, event switches, hot number tuning — it must exist in the first version, and all of it must be hot-updatable (Multiplayer & Backend §8).
- Four metric groups — concurrency, retention, payment and economy — go onto a real-time dashboard; sudden drops in concurrency and anomalous currency velocity need automatic alerts.

**Cost**

- Build a cost sheet from CCU and bandwidth before discussing scope (Multiplayer & Backend §8); for a world that never goes offline, the bill has no pause setting.
- Capacity planning must separate the daily waterline from version peaks; elastic scaling of stateful services must be designed before it is used.

## 5. Content Volume and Workload Reference

The following are common magnitudes for projects of this kind, for scope estimation — not a commitment.

| Shape | Content volume | Time frame | Team size |
| --- | --- | --- | --- |
| Small online world (community scale) | 1–2 maps plus one core loop | 3–6 months | 3–8 people |
| Small-scale MMO | 3–5 maps, dungeons and a basic economy | 1–2 years | 8–20 people |
| Commercial MMORPG | A continuously expanding world and version cycle | 3–5 years for the first release, then an annual cycle | 50+ people |

The content production ledger:

- **Text and quests**: a few minutes of story quest costs far more than a few minutes to make; at commercial scale, quest text totals in the hundreds of thousands of words (including dialogue, item and quest descriptions).
- **Art**: characters and monsters are industrialized as "reusable skeletons plus swapped parts"; the scenes and monsters of one raid can match the main-line scenes of a small single-player title in cost.
- **Classes**: every class or specialization is its own cost set of combat, animation, balance and testing; decide the number of classes by maintenance cost, not by fun.
- **Maps**: an MMO map must carry quests, drops, events, navigation and performance optimization; the combined cost per unit area is far higher than in single-player.

**The realistic alternative for small teams: small-scale online.** If what attracts you is the "online world" rather than "long-term cohabitation", swap out the small world:

| Dimension | MMO | Small-scale online |
| --- | --- | --- |
| World | Persistent, running 24/7 | Room-based or host-authoritative, opened and closed as needed |
| Population | Thousands concurrent on one server | 2–8 players per session, or matchmade |
| Cost | Servers and operations are long-term investments | Cost follows peak concurrent matches, and can be shut down |
| Social | Guilds, trading and relationship chains | Friends and recent players |
| Content driver | Update cadence | Per-match replayability |

The boundary: players do not need to "live inside it" — they only need to "play well and be able to meet up with friends". Co-op campaigns, party games, competitive games and online sandboxes all sit in this range; the skeleton still reuses the Multiplayer & Backend handbook, minus the heavy modules like guilds, auction houses and world chat. If you insist on a sense of world, compromise with a "small persistent world" (dozens of players) — but write the live-ops plan for the empty hours of low population in advance.

## 6. How to Start the First Prototype

The first prototype is not a "small MMO" but a small online slice that runs over a real network: one server, one small map, one loop (kill, loot, grow stronger), one social hook (party or chat). Six to eight weeks, starting from an off-the-shelf backend (Multiplayer & Backend §5) — do not build the whole stack in-house.

- **Weeks 1–2: the online skeleton.** Accounts, login, characters, movement sync, chat; server authority plus client prediction. Goal: two machines on different networks enter the same scene.
- **Weeks 3–4: one complete loop.** Kill drops, inventory, currency, shop, one progression step; numbers coarse first, fine later. Goal: 10 bot accounts grind for 1 hour without disconnects or crashes.
- **Weeks 5–6: the social hook and small-scale testing.** Parties with shared experience, or a guild prototype; get 10–20 real people to play together for three evenings, and watch the chat and the self-organization.
- **Weeks 7–8: live-ops drills and load testing.** Run one rehearsal each of announcements, compensation, bans and hotfixes; load-test at three times the expected peak.

Success criteria (all observable):

- In week two, people still log in voluntarily, and not because you reminded them; someone spontaneously waits for someone else to come online (forming a party, setting a time).
- The server runs continuously for 7 days (scheduled maintenance allowed); the disconnect and rollback procedures have been actually rehearsed at least once.
- Per-player currency growth stays controllable over 7 days, with no get-rich-overnight output exploit appearing.
- You can articulate "what content makes players come back the next day"; if you cannot, go back and fix it — do not add maps.

## 7. Common Pitfalls

1. **Starting at commercial MMO scale**: any one of the three bills — servers, operations, content — is enough to bankrupt a small team; read the alternatives in §5 first.
2. **Gameplay only, no social or economy**: players grind to cap and leave; the world becomes an empty lobby. Retention comes from organization and relationships, not from numbers.
3. **Faucets without sinks**: currency depreciates, prices take off, newcomers are driven out; sink design and faucet design must ship on the same day (§3.4).
4. **Client authority**: edited clients, edited saves and gold exploits break the economy overnight; put every economic settlement on the server (Multiplayer & Backend §6).
5. **Single-player update cadence**: players exhaust the game three months after launch; repeatable content and seasonal structures must enter the design early.
6. **Daily-quest bloat**: players are bound into clocking in for work, and freshness and word of mouth burn out together; keep dailies few and backlog-friendly.
7. **No server-split and merge plan**: launching without channels blows the peak; late-stage dead servers go unmerged, live-player density falls short, and the world exists in name only.
8. **The newcomer entrance silting shut**: catch-up mechanics are a standing system, not a one-off event (§3.6).
9. **No hotfixes or live-ops tools**: changing one number means half a day of downtime, and compensation goes out by hand; your operating radius is strangled by tooling (Multiplayer & Backend §8).
10. **Underestimating black markets and RMT**: gold-farming studios treat the economy as an ATM; audits, risk controls and legal action must be formed into a system (Pitfalls & Anti-patterns §8).
11. **Worshipping "player count"**: people brought in by paid acquisition are not a community — they scatter once the spending stops; resources spent on retention and organization pay better than resources spent on the entrance.

Gameplay decides why players come in; live operations and community decide why they stay. An MMO's pitch document should answer "how do we make people stay" first, and "how do we make people come in" second.

## Further Reading

- Multiplayer & Backend §2, §3, §6, §8: sync models, service layering, economy security and the cost ledger — the full expansion of section 4.
- Live-Ops & Growth §5, §6, §8: long-term operations, data metrics and community crisis management — the companion methods for section 3.5.
- Programming Handbook §5: networking and multiplayer fundamentals — the entry map before you start.
- Pitfalls & Anti-patterns §1, §8, §10: the high-frequency pitfalls on the kickoff, online and operations sides.
- Indie Survival: scope control and financial discipline — the working papers behind section 5's ledger.
- Exercise 1: write a one-page economy sheet for a fictional MMO — five items each for faucets, sinks and adjustments — and note the first response tool when each runs out of control.
- Exercise 2: go through the update logs of Final Fantasy XIV or World of Warcraft, chart the cadence between the last two major versions, and compare it against §3.5.
- Exercise 3: build a weekend prototype on an off-the-shelf backend — one map, ten players on screen, chat and drops — and measure the actual bill.
