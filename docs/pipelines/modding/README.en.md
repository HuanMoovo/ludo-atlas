# Ludo Atlas · Modding & UGC

> The complete decision and execution guide for adding mod support and user-generated content (UGC) to a game: support tiers, architecture principles, Steam Workshop and mod.io integration, community operations, and legal compliance.
> Companions: Programming Handbook · Live-Ops & Growth · Legal, Patents & Competition · Pitfalls & Anti-patterns.
> The one-line conclusion up front: mod support is a strategic issue that requires architecture decisions a year ahead — it is not a feature you add after launch.

---

## 1. First, Decide Whether Your Game Should Support Mods

Whether it is worth doing comes down to three signals:

- **Content consumption rate**: if players consume the content and leave (short narrative games), mods will not save you; if players replay and want to build things (simulation, building, survival, sandbox, roguelike), mods are the long-tail engine.
- **System openness**: the systems themselves are the source of fun (stats, combinations, automation), and players feel the urge to say "I want to try something else."
- **Community traits**: players are already asking "can you mod this?" and pulling apart your data files — that is the signal.

Reference data (mod.io's own official pitch): games that have been on mod.io for more than two years keep average daily active users at roughly half their peak; on console, fewer than 2% of games support UGC, which leaves room to differentiate.

The costs should be made clear up front too: compatibility maintenance, moderation headcount, legal terms, and added performance and anti-cheat complexity all grow along with the mod ecosystem.

## 2. Support Tiers: From L0 to L3

It is not a matter of two options, "full mod support" or "no support." There are four tiers of increasing investment:

| Tier | What you do | Team investment | Best for |
| --- | --- | --- | --- |
| L0 Open data | Parameters, stats and skins live in external data files (JSON/spreadsheets) that players may edit | Minimal | Every game; costs almost nothing |
| L1 Official API/SDK | Expose scripting interfaces and a toolchain so players can make gameplay-level changes | Medium | Systems-driven games |
| L2 Platform distribution | Integrate the Workshop or mod.io: subscription, versioning and moderation end to end | Medium | Once you have a community base |
| L3 Full editor | Official level/gameplay editor; players build content | Large | Platform-scale long-term products |

The right route for the vast majority of teams: do L0 now, reserve room for L1 in the architecture design, watch the community for L2, and keep L3 for platform ambitions only.

## 3. Architecture Principles: Mod Support Is Won or Lost Before Any Code

1. **Data-driven**: separate content (items, levels, rules) from logic. Players change data without touching logic, and most of your stability is preserved.
2. **Stable interfaces with version numbers**: version the mod-facing API from day one; breaking changes require an announcement and a transition period.
3. **Sandboxing and permissions**: mods from L1 upward mean executing player code. Choose a language with a restricted environment for the scripting layer (Lua is a common choice), and grant filesystem and network access on a least-privilege basis.
4. **Conflict handling**: several mods editing the same data is the norm. Design load order, override rules and conflict warnings — do not make players guess.
5. **Save compatibility**: saves that use mods must record their dependencies; when a mod is missing, the save should still load, warn the player, and not crash.
6. **Anti-cheat boundaries**: in multiplayer, match modded and unmodded players in separate pools; server-authoritative rules must not be rewritable by client-side mods.

## 4. Steam Workshop Integration

Steam has a complete official solution (the Steamworks Workshop):

- **Technical side**: implement upload, subscription and download through the ISteamUGC API; listen for the item-installed callback (ItemInstalled) and read data from the install directory; the official SpaceWar example covers the most common call paths.
- **Content validation**: the official recommendation is to accept only formats the game client can load, and to provide official tools that limit what can be changed. "Give players and yourself the same set of tools" is the least-effort moderation strategy.
- **The official answer to version hell**: the Workshop supports item versioning, so mods can declare the range of game versions they support; paired with game branch management (a beta branch), you can have mod authors adapt on the beta branch before an update ships, which sharply reduces incidents where an update breaks mods. This is a high-value feature — enable it when you adopt the Workshop.
- **Legal and branding**: Workshop content requires platform-side agreement coverage, and there is guidance documentation for brand asset usage — follow the official docs.

## 5. mod.io: A Cross-Platform UGC Solution

The biggest obstacle to mod support on console is platform restrictions; mod.io is currently the most industrialized cross-platform solution:

- Covers PC, console, mobile and VR; provides Unity and Unreal plug-ins plus a C++ SDK and a REST API.
- Includes moderation and content-management tools (critical for console compliance), analytics, and optional monetization and white-label integration.
- Real cases: Baldur's Gate 3's console and cross-platform mod support is built on mod.io's white-label solution; SnowRunner used cross-platform mods to extend its lifespan.
- The special discipline of console mods: all content is reviewed before release, runtime behavior is restricted, and memory and size budgets are stricter than on PC — the solution itself accounts for these constraints.

Bottom-line recommendation: on PC, prefer the Workshop first (the user base and habits are there); to cover console and mobile, evaluate mod.io directly or use it as a complement.

## 6. Toolchain & Ecosystem Notes

- **Nexus Mods** is a major hub of the PC mod community; even if you do not officially support mods, players may publish them there. Rather than fight it, design your formats so that they can.
- **The reality for Unity projects**: the player community has mature injection-based mod frameworks (BepInEx, MelonLoader and the like) and you cannot stop them. The smart move is to embrace it: give them data formats, interfaces and documentation.
- **Your official tools are the mod tools**: clean up the in-house level/stats editing tools and ship them to the community (Steam's official docs recommend this too) — cheaper and more stable than building a separate set.
- **Example mods are the best documentation**: publish two or three source-level examples (one that changes stats, one that adds content, one that changes gameplay) and the rate at which mod authors get started will multiply.

## 7. Community Operations

- **Creator incentives**: featured placements, early-access invitations, official reposts. Be cautious with paid revenue shares (see §9), but you can give recognition, beta access and thanks.
- **Compatibility announcement discipline**: announce breaking updates in advance, provide a beta branch and an adaptation window. Mod authors work for free — you owe them transparency.
- **Moderation and governance**: make the handling process for malicious and infringing content public (takedown standards, appeals channel). On console platforms the publisher is responsible for content moderation, so staff up in advance.
- **Data dashboards**: subscription counts, active mod counts, the share of players who depend on mods — these numbers decide how many resources the mod ecosystem deserves.

## 8. Legal and Compliance Essentials

- **Write the EULA clearly**: what is allowed (non-commercial mods, attribution), what is prohibited (stolen assets, commercialization, malicious code), and IP ownership (mods belong to their authors, but they run on top of your IP).
- **Lessons from paid mods**: Steam's 2015 paid-mod experiment on the Workshop was withdrawn within days after fierce community backlash; subscription-style attempts such as Creation Club came later. Conclusion: community acceptance of paid mods is scarce and fragile — before doing it, decide who pays, who takes a share, and who provides support.
- **DMCA process**: have a takedown response process ready for infringement, while also protecting your own content from being misappropriated.
- **UGC compliance for operating in China**: when operating in mainland China, user-generated content carries statutory review and management duties, and the platform side has corresponding requirements. Build the review mechanism, reporting channel and handling process before launch (for the key regulations see the Legal, Patents & Competition and Multi-platform Launch Playbook handbooks).

## 9. Case Sketches

- **Minecraft**: the extreme case of full openness from data to code, with the mod ecosystem becoming part of the product's lifespan.
- **The Elder Scrolls V: Skyrim**: the evergreen of single-player mod ecosystems, showing the lasting power of the "tools + formats + community" trio.
- **Terraria**: taking the community mod loader (tModLoader) in as official free DLC — a benchmark move of embracing the community.
- **Stardew Valley**: a solo developer staying open to mods, and the SMAPI ecosystem in turn extended the product's life.
- **Baldur's Gate 3**: a major studio used an industrial-grade UGC solution (mod.io) to bring mod support to console, proving console mods are viable.
- **Factorio**: an official mod portal plus a strict version mechanism — one of the best-managed answers to the "update breaks mods" problem.

## 10. Common Pitfalls

1. The architecture leaves no interfaces, and adding mod support after launch means rebuilding the data layer.
2. No versioning mechanism: one update breaks the whole community's mods and ratings plunge.
3. Mods are given arbitrary code execution, and one security incident takes your reputation down with it.
4. Console tries to copy the PC mod approach, ignoring the platform constraint that content is reviewed before release.
5. Official tools are kept hidden, reverse engineering costs the community too much, and the ecosystem never grows.
6. Updates ship without announcements, and mod authors walk away en masse.
7. A carelessly designed paid-mod scheme ignites community sentiment.
8. The EULA is unclear, leaving no basis when an IP dispute arises.
9. Only one distribution channel is supported, shutting out console and mobile players.
10. Treating UGC moderation as trivial, and taking hits on both mainland China compliance and console compliance.

## 11. Further Reading

- Steam Workshop overview (Steamworks, Chinese): https://partner.steamgames.com/doc/features/workshop?l=schinese
- Steam Workshop implementation guide (ISteamUGC API): https://partner.steamgames.com/doc/features/workshop/implementation?l=schinese
- Steam Workshop item versioning (solving update compatibility): https://partner.steamgames.com/doc/features/workshop/itemversioning?l=schinese
- mod.io documentation (cross-platform UGC solution): https://docs.mod.io/
- mod.io website: https://mod.io/

> Also: see github.com/BepInEx/BepInEx for BepInEx (the Unity community mod framework), and nexusmods.com for Nexus Mods. Common infrastructure of the PC mod ecosystem — worth knowing.
