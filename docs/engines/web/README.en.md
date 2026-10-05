# Ludo Atlas · Engine Tracks · Web Games

> **Engine Tracks**. Positioning: a game development route that uses the browser as its runtime — its core promise is "share a link and it plays," pushing distribution and installation costs close to zero.
> Companions: Multi-platform Launch Playbook · Programming Handbook · Art & Audio Handbook · Mini-Game Development.

---

## 1. Positioning and Choice

In one line: Web games are the route where **the link is the unit of distribution**. Players click and play, no install, and you do not queue for store review; the price is that performance ceilings, memory and device variance are dictated by the browser and the user's hardware.

Where it fits and where it does not:

| Dimension | Fits | Does not fit |
| --- | --- | --- |
| Project shape | Short-session gameplay, casual and puzzle, prototypes and demos, 3D showcases, teaching demos | Large bundles of heavy 3D; long-immersion large-scale works |
| Business shape | Virality and demo conversion, embedded products, ad monetization, portfolios | Scenarios that rely on store discovery and premium purchases |
| Technical expectations | 2D and light 3D; accept "good on mid-range phones" rather than "maximum fidelity" | Competitive and photoreal projects with hard framerate and fidelity promises |

The first filter is the three-way split of tools:

| Category | Example | What it is | Fits | Does not fit |
| --- | --- | --- | --- | --- |
| Game framework | Phaser | Batteries-included 2D framework: scenes, sprites, physics, input, audio | Complete small 2D games, game jams, fast prototypes | Deeply custom render pipelines |
| 2D rendering library | PixiJS | Solves high-performance 2D rendering only; the rest is yours | Self-built game frameworks; UI-dense 2D products | Wanting ready-made gameplay and flow modules |
| 3D engine | Three.js / Babylon.js | 3D rendering and scene capabilities in the browser | 3D showcases, light 3D gameplay, data visualization | Heavy 3D worlds and film-grade pipelines |

Three.js vs Babylon.js: the former is closer to a "rendering library" — high freedom, a big ecosystem, a pipeline you assemble; the latter is closer to a "complete engine" — modules and tools included, less assembly to start. Pick one by team habit; do not learn both at once.

Selection order: first ask whether you need 3D — if yes, go to a 3D engine; if no, ask whether you want ready-made gameplay modules — if yes, a game framework; if no, a rendering library. Also note: native engines like Godot and Unity can also export browser builds, but that is the "an existing project ships a Web version on the side" route; new Web-first projects start from Web-native tools, with a smaller bundle and fewer compatibility burdens.

## 2. Ecosystem and Project Structure

A Web game is essentially a single-page frontend application; the toolchain shares its lineage with the front end. Three things must be right:

- **Package management and version locking**: start with npm; commit the lockfile; one Node version across the team and build machines, to avoid "it runs on mine."
- **Bundler**: a local dev server with hot reload (start with Vite) for development; the production build emits static files. Dev and build behavior can differ — verify the built artifact separately.
- **TypeScript strongly recommended**: gameplay state, asset keys and event names get caught at compile time; starting in plain JS and migrating mid-way costs a lot.

Lay out directories by "entry, scenes, systems, entities, UI, assets" — stable as you scale:

```text
src/
├── main.ts        # Entry: initialization and wiring
├── scenes/        # Scenes and states: title, level, results
├── systems/       # Input, audio, saves, asset loading
├── entities/      # Game objects, named by domain rather than file type
├── ui/            # UI and HUD
└── assets/        # Assets and the asset manifest
```

Two disciplines: register asset references centrally in a manifest file — loading and releasing are checked against the manifest; before adding any dependency, ask what it adds to the bundle — runaway frontend dependency trees are a common accident unique to the Web route.

## 3. Core Workflows

**Development loop**: a hot-reloading local server, browser DevTools for debugging, real-device verification (a phone on the same network opening the dev address), then back to desktop iteration. Move real-device verification to day one — do not see your game on a phone for the first time at release.

**Build and deployment**: the bundler combines entry, scripts and assets into static output; before deploying, verify under the real target path (subdirectory deploys, case sensitivity, cache hits), and accept one update by the standard "existing users receive the new version."

**Release channels**:

| Channel | How | Fits | Notes |
| --- | --- | --- | --- |
| itch.io Web | Upload a zip with an entry page; the platform hosts it and runs it embedded on the project page | Indie games, game jams, demos | Verify fullscreen, pointer lock and audio unlock behavior under embedded play, item by item |
| Self-hosting | Static hosting platforms or your own server for the build artifact | Own branding, long-term operation, embedded products | Configure encrypted access and compression; plan cache and version-update strategy |
| As a demo | Ship the full game on stores; the Web version covers only the opening stretch | Store-page acquisition, wishlist conversion | Actively control content scope and performance expectations; do not let the demo take the full game's bad reviews |
| Mini-game platforms | Distribution via WeChat, Douyin and similar (China) | Chinese channels and paid acquisition | A different set of engineering constraints from pure Web — see Mini-Game Development |

Pre-release checklist:

- Seconds from open to "playable" on the first screen, and real behavior on weak and mobile networks.
- The touch flow works end to end; virtual buttons do not misalign on mainstream devices.
- Audio plays after the first user gesture; the mute toggle works.
- Background and return: the screen recovers, timing does not scramble, audio reconnects.
- Shared title, description and share image are correct.

## 4. Idioms for Key Systems

### 4.1 Game loop and time steps

- Rendering hangs off the browser's per-frame callback; logic and rendering are layered. Define every speed "per second," multiply motion by delta time — never "fixed pixels per frame."
- Physics and consistency-critical logic run on a fixed step (commonly 60Hz): slice real time into fixed pieces before updating, interpolate on the render side. Ordinary screens, high-refresh screens and thermally throttled low-end devices then behave the same.
- Screen refresh rate is not a constant — background throttling and device throttling change it. Show framerate and time step on screen while debugging; do not trust feel.

### 4.2 Input and touch

- Separate physical input from logical actions: keyboard, mouse and touch map to the same action names, so rebinding and devices never touch gameplay code.
- Route touch through Pointer Events uniformly — one event path covering mouse, finger and stylus.
- Position touch layouts by screen ratio; hit areas no smaller than the conventional minimum (about 44–48 px); design for multi-finger presses — movement and jump often go together.
- Suppress browser default gestures (page scroll, double-tap zoom, long-press selection); the mobile address bar expanding and collapsing changes the visual height — adapt layouts to dynamic viewport and safe areas.
- Phone browsers may also have keyboards, mice or gamepads attached — do not hard-wire a single device in the input layer.

### 4.3 Asset loading and lifecycle

- Loaders and progress feedback are standard: the first screen loads only the minimum "playable" set; the rest lazy-loads per level or scene.
- Textures go in atlases; manage asset handles centrally, following the manifest discipline of §2.
- Release discipline: GPU resources such as textures and render targets are outside browser garbage collection — destroy them explicitly when done; check item by item against the manifest on scene switches.

### 4.4 Audio and autoplay restrictions

- Browsers block audio without user interaction by default: bind audio initialization and unlocking to a real user gesture — the "Start" button on the title screen is the most common spot.
- When the page goes to the background, audio and timers get paused or throttled; on return, restore state and resync timing.
- Mobile devices cap concurrent voices and decoding memory: control audio count and size, stream long audio, and provide master volume and mute toggles.

### 4.5 Saves and state

- Small data (settings, progress pointers) in local key-value storage; structured data in IndexedDB; private browsing may restrict both — have fallbacks and messaging.
- Saves store state and a version number, never object references; write migrations when the structure changes, and support export and import.
- Refreshing the page equals a cold start: do not keep critical progress only in memory.

## 5. Performance and Optimization

**Target and measurement**: a stable 60 fps on mid-range phones is the common floor; if you cannot reach it, lock to 30 for stability rather than jittering in between. Use the browser DevTools performance and memory panels to watch frame times and allocation curves; trust real devices — desktop browser data lies.

**Rendering**:

- Draw calls are the main line: atlases and batching, fewer texture and material switches, cached static text (text drawing is expensive).
- Resolution control: render resolution equals layout size times device pixel ratio (DPR); multiplying fully on high-DPI screens multiplies the pixel count several times over. Common practice: cap the DPR (e.g. at 2) or scale dynamically by performance tier.
- Overdraw: large translucent areas and dense particles cost a lot on mobile; control layer counts.

**Memory**:

- Textures dominate: large resident images, unreleased scene textures, and canvases and render targets created and destroyed frequently are all accident sources.
- The big three JS-side leaks: event listeners, timers, closures holding references; unregister and clean up on scene switches.

**Per-frame allocation and GC**: create no objects, arrays, strings or closures inside loops; reuse temporary vectors; route bullets and effects through object pools. GC pauses present as periodic frame drops.

**Load size**: minimal first screen, code splitting, asset compression (enable server-side compression), modern image formats with size limits, audio loaded on demand. "Dozens of seconds of white screen" is fatal — it kills retention outright.

**Mobile specifics**: sustained full framerate drains battery and heats the device — drop frame rates in menus and static scenes actively; the WebGL context may be reclaimed by the system or reset by drivers — have logic to rebuild resources and recover; tier devices and downgrade quality automatically on low-end hardware.

## 6. Learning Path

| Stage | Content | Bar to clear |
| --- | --- | --- |
| 1. Language and browser basics | JavaScript and TypeScript, DOM and events, DevTools debugging | Independently locate an error and a frame drop |
| 2. First framework game | Build a complete small game with Phaser: start, play, results, restart | Published on itch.io; anyone with the link can play |
| 3. Engineering | npm, bundlers, TypeScript throughout, asset manifests, build and deploy | One command produces a deployable artifact; playable on a phone |
| 4. Rendering depth | Add PixiJS (self-built framework) or Three.js / Babylon.js (3D) per goal | Explain your project's draw-call makeup and bottleneck |
| 5. Performance and devices | Real-device matrix, memory and load optimization, mobile specifics | Stable on mid-range phones; survives backgrounding |

Learning discipline:

- Official docs and official examples first; follow one tutorial source only — no hopping between islands.
- One tool per stage; running three libraries at once means mastering none.
- Every stage emits a link "someone else can open"; practice without a release does not count.
- When dissecting competitors, watch load time and mobile behavior — that is where the Web route is won or lost.

## 7. Common Pitfalls

1. **Texture and GPU resource leaks**: scene switches drop references without destroying textures; GPU memory only grows, and the game freezes after a few levels. Release checked item by item against the asset manifest (§4.3).
2. **Uncapped high-DPI rendering**: device pixel ratio multiplied straight into render resolution multiplies mobile pixel counts, bringing frame drops and heat together. Cap the DPR or scale by performance tier (§5).
3. **Runaway first-screen load**: everything in the initial bundle, dozens of seconds of white screen. Minimal first screen, code splitting, compression on (§5).
4. **Per-frame temporary allocations**: objects and closures created casually in loops, GC pausing periodically. Reuse and object pools (§5).
5. **Playing audio before unlocking**: no sound on first entry and players think the game is broken. Bind unlocking to a user gesture (§4.4).
6. **Logic written per fixed frame**: fixed per-frame steps behave differently on high-refresh screens and low-end devices. Delta-time driven with fixed-step physics (§4.1).
7. **Ignoring background transitions**: switching tabs away and back causes time jumps — clipping through geometry, exploding timers. Handle page visibility changes and clamp time.
8. **Conflicting touch gestures**: page scroll, double-tap zoom and long-press selection steal input; hit areas too small to tap. Both need deliberate design (§4.2).
9. **Testing desktop browsers only**: everything is fine on desktop Chrome, and audio, fullscreen, memory and rendering all change on iOS and Android devices. A real-device matrix belongs in the process.
10. **Runaway dependencies**: a single-page game dragging in an entire frontend framework and dozens of dependencies explodes both bundle and upgrade costs. Minimal dependencies, locked versions (§2).
11. **Running full framerate all the time**: menus and static screens render at full rate too, draining mobile batteries and ruining the experience. Frame-rate drops and quality tiers (§5).
12. **Deployment path and cache issues**: hard-coded subdirectory paths fail, case sensitivity bites, and existing users do not get the new version after updates. Accept the built artifact under the real deployment path (§3).

## Further Reading

- [Engine Tracks overview](../README.md): how the 12 tracks divide the landscape, and where the Web route sits.
- [Engine Selection Guide](../../start/engine-choice.md): the full comparison between Web-native tools and the engine routes.
- [Multi-platform Launch Playbook](../../../playbooks/platform-launch/README.md): release channels and compliance — section 3 here expanded.
- [Programming Handbook](../../fundamentals/programming/README.md): the general groundwork for performance engineering and engineering infrastructure.
- [Art & Audio Handbook](../../fundamentals/art-audio/README.md): asset specs and audio practice.
- [Mini-Game Development](../../publishing/minigame/README.md): the WeChat and Douyin mini-game route, and where constraints differ from pure Web.
- [Resources](../../../resources/README.md): official engine entry points, tutorials and courses.
