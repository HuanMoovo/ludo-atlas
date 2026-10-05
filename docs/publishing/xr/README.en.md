# Ludo Atlas · VR/AR Development

> XR development and shipping in practice: platform landscape, store requirements, interaction design, comfort, performance budgets.
> Companions: Multi-platform Launch Playbook · Console Development · Programming Handbook · Art & Audio Handbook · AI Workflows Handbook.
> **Freshness note**: XR hardware and platform rules update extremely fast; this document was verified in 2026-10. Before you act, defer to the platforms' official documentation.

---

## 1. First, Know the XR Segments and the Landscape

XR is an umbrella term; inside it sit completely different businesses:

- **VR (fully virtual)**: immersive but cut off from reality. The mainstream is the Meta Quest ecosystem, plus PICO, PSVR2 and PCVR (SteamVR).
- **MR (mixed reality)**: virtual content overlaid on the real environment. Quest 3/3S and Vision Pro fall into this category.
- **AR (augmented reality)**: two tracks — phone AR and glasses. Phone AR has a low barrier and a large user base; AR glasses remain an early market.

The common path for teams entering: Quest first (largest installed base, most mature toolchain); once successful, port to PICO and PCVR; then evaluate Vision Pro and phone AR.

One practical question to think through: XR's games audience is still far smaller than PC and mobile. For projects under real survival pressure, XR suits a second platform or a short-cycle experiment — not your only bet.

## 2. The Four Major Platforms and Their Launch Requirements

| Platform | Submission portal | Key requirements | Notes |
| --- | --- | --- | --- |
| Meta Quest | Meta Horizon Store (submit via the developer dashboard) | Pass the VRC checks; review is split into technical, content and distribution parts; submit at least two weeks in advance (recommended); store metadata includes a comfort rating | App Lab has been merged into the main store; there is an Early Access badge channel; saturated categories may have review terminated on the first violation |
| PICO | PICO Developer Platform | Self-service onboarding and publishing, paid apps supported; individual developers can handle everything online | Two portals: international and China (developer-cn) |
| PSVR2 | PlayStation Partners (same process as consoles) | Follows the console partnership process; details in the Console Development | Requires console developer qualification |
| Apple Vision Pro | App Store Connect | visionOS apps are built and submitted separately; existing iPad/iPhone apps can opt into compatible release (auto-published, editable) | Gaze and gesture interaction; accessibility and privacy disclosure are review priorities |

Meta Quest's review details deserve their own note: the VRC (Virtual Reality Checks) is the platform's whole technical compliance checklist, covering both performance and functionality; review splits into technical, content and distribution parts; go through the VRC item by item before submitting — most rejections are for items spelled out in the list. Also, Meta officially asks for a review window of at least two weeks before submission, so don't cut your launch date too fine.

## 3. Interaction Design: Start from "the Player Has a Controller"

- **Controller-first**: controllers (ray + buttons) are still the mainstream interaction for commercial Quest titles — reliable, precise, no learning curve.
- **Hand tracking**: suits social, casual and demo-style experiences. Hand tracking's tap precision is lower than controllers': make buttons bigger, tolerate jitter, give gestures clear feedback.
- **Gaze and pinch**: the Vision Pro paradigm — eyes aim, fingers confirm. Design points: gaze precision is limited (about 1–2 degrees of deviation); targets must be large enough; and gaze data has privacy boundaries (apps only receive hover events, not raw eye-tracking data — privacy disclosure is a review priority).
- **Put UI in 3D space**: design text by visual angle, not pixels. Distant signage must be large enough to read from the front row; don't paste prompts right in front of the face (near-field focus strains the eyes).
- **Direct grabbing and physicality**: things you can hold in your hands are more immersive than menus; hands-on manipulation within interaction distance is VR's sweet spot.
- **Feedback must be multi-layered**: haptics (vibration), audio (spatial sound) and visuals (highlights and deformation) — all three together; miss one and it feels "floaty".

## 4. Comfort: the Lifeline of a VR Product

Users driven away by motion sickness won't give you a second chance. The order of control is:

1. **Frame rate first**. Dropped frames are the number-one source of motion sickness; the performance budget always protects frame rate first. (Meta's hard floor is in the next section.)
2. **Never take away camera control**. Any camera movement the player did not initiate (cutscenes, head-bobbing, forced turning) is high-risk; avoid it if you can.
3. **Offer locomotion options**: teleport is the default low-risk choice; smooth locomotion plus tunnel vision (vignette masking) can soften it; abrupt stops and turns are the disaster zone.
4. **Use snap turning**: snap turn is far more comfortable than smooth turning.
5. **Seated mode**: prepared for players who sit for long periods or have limited mobility.
6. **The first minute is the most dangerous**: avoid intense motion in the opening; let players "steady themselves" in a static scene first.
7. **Comfort rating is a store requirement**: the Meta store requires a comfort level — this is not a formality, it's expectation management for users.

Testing discipline: don't test only yourself and your colleagues (all VR veterans). Test newcomers, motion-sensitive people, and different heights and eyesight. Watch for discomfort signals: sweating, taking off the headset, closing eyes, weight shifting. Rather cut one thrill than keep one reason to quit.

## 5. Performance Budget: Double Pressure on Mobile Chips

Standalone headsets like Quest and PICO are essentially mobile chips doing dual-screen rendering, and the performance budget is tighter than mobile games':

- **Frame-rate floor**: Meta's VRC requires a render rate no lower than 60fps (the standard after the August 2024 revision; with application spacewarp it can drop to half the refresh rate), a refresh rate of at least 72Hz, with mainstream tiers at 90Hz and above. Target stable 72fps first, then push for 90.
- **Fill rate is king**: large semi-transparent effects, full-screen particles and overly dense scene depth all collapse on fill rate. Budget your overdraw.
- **Use the official techniques well**: multisample anti-aliasing (MSAA) beats post-process sharpening; fixed foveated rendering (FFR) is free compute; baked lighting beats real-time.
- **Thermal throttling**: chips throttle after 20 minutes of continuous play — holding frame rate then is the real test. Test over long sessions; don't test only a cold device.
- **Toolchain**: Meta has performance-capture tools like OVR Metrics; Meta XR Simulator lets you iterate without deploying to a device. In 2026 Meta also introduced MCP-compatible AI agent tools such as XR Operator, which can drive an app running in the simulator to run build, test and verify loops (for the approach, see the AI Workflows Handbook).

## 6. Engineering Stack

- **Engines**: Unity has first-party support (the Meta XR package family is the most complete); Unreal's official support is mature; Godot goes the OpenXR module plus community route, suited to lightweight projects; native OpenXR suits in-house engines.
- **OpenXR is the cross-platform common denominator**: sink as low as possible into the OpenXR layer and use platform-proprietary SDKs only for differentiated features — this keeps multi-platform porting costs lowest.
- **Test matrix**: cover device models (the gap between older Quests and newer models), controllers/hand tracking, seated/standing, and room size. The Android foundation means you can sideload for debugging.
- **One legacy reminder**: many tutorials online are still stuck in the Oculus era (Oculus SDK, Quest 1/2 wording); check the date of the docs before copying code.

## 7. Audio and Presence

In XR, sound is not a supporting player — it's half of spatial perception: footsteps, echoes and sounds overhead all directly affect immersion and comfort. Spatial audio is a must; sound is also an important guidance tool (someone behind you, a door on your left). Keep volume and low frequencies in check — bass bombardment worsens discomfort.

## 8. Cadence from Prototype to Launch

1. Build a prototype that "validates one interaction only" (grabbing, say, or locomotion) — no art talk yet.
2. Get 10 newcomers to test comfort and approachability.
3. Expand content only after the core loop works; track the performance budget from day one.
4. Store materials: video (essential — XR users decide based on video), screenshots, comfort rating, privacy notes.
5. Submit for review: schedule backwards from each platform's lead time in §2; leave at least two weeks for Meta.

## 9. Common Pitfalls

1. Testing only with VR veterans; newcomers all get driven away by motion sickness.
2. Missing the frame-rate target; review stuck on the VRC performance items.
3. UI pasted in front of the face or sized in pixels — users can't see it clearly and their eyes hurt.
4. Cutscene animations forcing camera movement; players are put off right at the opening.
5. Only testing short sessions on a cold device; everything collapses after thermal throttling.
6. Hand-tracking hit areas too small to hit.
7. Ignoring accessibility and privacy disclosure; review sends it back.
8. A perfunctory store video; an extremely low conversion rate.
9. Carrying mobile-game performance habits into XR; textures and particles over budget.
10. Forgetting to reserve review time; missing your release window.
11. Shipping Quest-only with no OpenXR abstraction; a rewrite for the second platform.
12. Mismatched expectations: a small XR installed base, but the revenue model assumes the full PC audience.

## 10. Official Entry Points

- Meta Quest submission and resources (VRC, review): https://developers.meta.com/horizon/resources/publish-submit
- Meta VRC performance items (rendering and refresh-rate wording): https://developers.meta.com/horizon/resources/vrc-quest-performance-1
- PICO Developer Platform (international): https://developer.picoxr.com/
- PICO Developer Platform (China): https://developer-cn.picoxr.com/
- Apple visionOS submission guide: https://developer.apple.com/visionos/submit
- OpenXR standard (Khronos): https://www.khronos.org/openxr/

> For more XR platform entry points, see Resources §2.7 and the Multi-platform Launch Playbook §7.
