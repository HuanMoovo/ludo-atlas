# Ludo Atlas · Console Development

> Console development and release in practice: developer entry points, dev kits, porting work, certification, and publishing models.
> Companions: Multi-platform Launch Playbook (incl. mainland China console approval) · Programming Handbook · Legal, Patents & Competition · Production Handbook.
> **Honest disclosure**: most technical details of console platforms are protected by NDA — public channels will only ever carry a fraction of them. This page only covers public information and general processes; for specific terms, certification checklists and SDK details, the platform's official documentation and your contract are the authority.

---

## 1. How Consoles Differ from PC and Mobile

Consoles are closed platforms: development requires qualification review, release requires certification, the hardware is proprietary, and the terms are confidential. Four things are fundamentally different from other platforms:

| Dimension | Console | PC (Steam, etc.) |
| --- | --- | --- |
| Development qualifications | Platform review + signed agreement | Just register |
| Hardware | Official dev kit (loaned or purchased) | Any computer |
| Release | Certification-based; every update must be certified too | Upload freely |
| Commercial terms | Confidential contract; revenue split negotiated case by case | Standard platform revenue share |

Why still ship on consoles: the living-room setting and gamepad experience, exposure through platform subscription services (Game Pass, PS Plus), a quality endorsement, and one reality you can't dodge — for many genres, the mainstream audience is on consoles.

The costs have to be owned as well: application timelines, porting workload, certification costs, no freedom over updates. A console version is not "one more platform on the side" — it is a small project of its own.

## 2. Developer Entry Points for the Three Major Platforms

| Platform | Public entry point | Key steps | Notes |
| --- | --- | --- | --- |
| Xbox | ID@Xbox (developer.microsoft.com/en-us/games/) | Register → submit your project → sign an agreement → dev kit | Self-publishing flow is mature; a Game Pass exposure channel |
| PlayStation | PlayStation Partners (partners.playstation.net) | Register (as a legal entity; individuals accepted in some regions) → project brief → sign the GDPA → DevNet and SDK → dev kit (loaned, returned on schedule) | The official blog has a complete write-up of the "how to show your game to PlayStation" process |
| Nintendo | Nintendo Developer Portal (developer.nintendo.com) | Register (individuals allowed) → accept the NDA and terms → apply separately for Switch development qualification → dev kit | Self-publishing supported, with eShop release; expect the review cycle to take time |

Three general recommendations:

1. **Apply early.** Review, contracting and dev-kit logistics add up to months — don't wait until the game is nearly done to start.
2. **Make the project brief read like an elevator pitch.** Platforms look at "who is making it, what it is, when it ships, and why it deserves a slot" — not a complete design document.
3. **The NDA takes effect the day you register.** Don't discuss unreleased information in any public venue (social accounts included) — including what hardware you can get access to.

## 3. Dev Kits and the Engineering Environment

- Dev kits (devkit) and test kits (testkit) are two classes of hardware with different purposes: dev kits run debugging builds, test kits simulate the retail environment. Most platforms loan them to qualifying projects, on the condition that you return them on time and follow confidentiality procedures.
- The engineering environment must be set up to platform requirements: proprietary SDKs, encryption tools, certificate systems. Use a dedicated build machine and separate accounts for this — don't share them with your day-to-day dev machine.
- Engine support as it stands (public information): Unity and Unreal both have first-party support on all three platforms; Godot has no official console export and needs a third-party porting service or a publisher's help; in-house engines carry the highest porting cost. Factor this into your engine choice.
- Two disciplines for combining CI with consoles: build artifacts are confidential, so the pipeline and artifact repository must be isolated; and certification builds must be reproducible (same commit, same toolchain, same artifact).

## 4. Porting Essentials

When porting from PC to console, the real bulk of the work is the five areas below, ranked by how likely they are to trip you up:

1. **Input**: gamepad button mapping, dead-zone tuning, button-prompt icons switching with the device, motion sensing and vibration. Every game-feel parameter has to be re-tuned.
2. **Saves and user systems**: platform accounts, cloud saves, multi-user profile switching. Corrupted saves and cross-device conflicts are the biggest source of player complaints.
3. **Achievements and trophies**: a hard requirement — you must implement them, and the design can't be a perfunctory "complete Chapter 1".
4. **System behavior**: suspend/resume, network loss, account sign-out, controller disconnection. On PC you can ignore these scenarios; on console you won't pass certification, let alone launch, without handling them.
5. **Performance**: fixed hardware is both a blessing and a pressure. Frame-rate stability comes before absolute visual quality, and heat and power draw have to be considered too.

Extras: HDR, variable refresh rate, surround sound, accessibility options, parental controls. Console review demands far higher completeness on these than PC does.

## 5. Certification: the Entry Exam of the Console World

Each of the three platforms has its own name for the technical compliance checklist (Sony's TRC, Nintendo's Lotcheck, Microsoft's Xbox Requirements); the details are all confidential, but the public commonalities can be used to prepare:

**What certification generally tests** (a synthesis of public descriptions and practitioner consensus):

- System feature completeness: saves, achievements, friends, invitations, voice chat, store redirects.
- Parental controls and account boundaries: age ratings linked to content restrictions.
- Suspend/resume and abnormal scenarios: power loss, network loss, storage media plugged in and out.
- Performance baselines: load times, frame rate, crash rate.
- Text and icon standards: button prompts and the official wording of system terms.
- Network behavior: disconnect handling, reconnection, abnormal exits in multiplayer.

**Process**: submit a candidate build → platform certification testing → report issued (pass / conditional pass / fail) → fix and resubmit → book the release slot. Passing on the first submission (a "first cert pass") is a hard measure of a team's engineering capability; if you can't do it, budget for a couple more rounds.

**Preparation advice**: start running an internal checklist 2–3 months before certification; turn the pitfalls you've hit into a team checklist; every update has to go through certification the same way, so work that rhythm into your release plan.

## 6. Publishing Models

- **Self-publishing**: all three platforms support indie developers publishing on their own (the Xbox ecosystem is especially mature); you keep your IP and pricing control, and the platform's revenue share is set by contract (the industry rule of thumb is around 30%, but actual terms vary case by case and by tier).
- **Publishing through a publisher**: the publisher handles funding, certification coordination, physical editions and regionalization, at the cost of revenue share and some decision-making control. For selection criteria and negotiation points, see Legal, Patents & Competition §5.
- **Ratings**: releasing on console stores requires a content rating (ESRB, PEGI, CERO, etc.; digital releases mostly go through the IARC questionnaire process). Mainland China console models follow a separate approval system — see the Multi-platform Launch Playbook for details.
- **Subscription services**: Game Pass, PS Plus and the like have their own submission and business entry points; for indie teams they are both revenue and exposure, and you can apply on your own initiative.
- **Physical editions**: limited physical runs (models like Limited Run) are long-tail revenue and a marketing event in themselves — suited to titles that already have a fan base.

## 7. Launch Cadence

- Store page assets (screenshots, trailers, copy) are strictly regulated on every platform; format and content both have to be checked against the template.
- Once pre-orders and the release date are announced, you have committed to the platform and changes are costly — leave buffer in the schedule.
- Day-one patches must be certified too. So "ship first, fix later" doesn't work on consoles — accept that when you are packaging.
- Scheduling advice for a simultaneous multi-platform release: run the platform with the earliest and strictest certification first; the rest follow.

## 8. Common Pitfalls

1. Underestimating porting hours. Input, saves and achievements are three mountains — budget double your original plan.
2. No buffer in the certification schedule — missing the peak-season release date.
3. Forgetting that every update needs certification too; carrying hotfix habits onto consoles and getting bounced.
4. Dev-kit confidentiality procedures going wrong (showing off hardware, lending kits out, leaked screenshots).
5. Button-prompt icons not adapted per device — failing certification on the first round.
6. Suspend/resume scenarios not fully tested — a frequent certification failure item.
7. Lazy achievement design, drawing player backlash in reviews after launch.
8. Network failure scenarios left unhandled — a guaranteed certification failure for multiplayer games.
9. Tax and revenue-share structures not worked out properly — finding the shortfall only when the money arrives.
10. Treating consoles as "one more platform on the side", with no separate resourcing.

## 9. Official Entry Points

- ID@Xbox (Xbox developer portal): https://developer.microsoft.com/en-us/games/
- PlayStation Partners: https://partners.playstation.net/
- Sony's official write-up, "Showing your game to PlayStation": https://sonyinteractive.com/en/news/blog/showing-your-game-to-playstation/
- Nintendo Developer Portal: https://developer.nintendo.com/

> For a roundup of platform entry points, see Resources §2.7; for the full launch flow and mainland China approval, see the Multi-platform Launch Playbook.
