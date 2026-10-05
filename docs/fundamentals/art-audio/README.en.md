# Ludo Atlas · Art & Audio Handbook

> Positioning: a production handbook about making the visuals "watchable" and the sound "punchy", covering art direction and specs, 2D/3D/UI pipelines, technical art basics, audio design and implementation, and delivery specs.
> Companions: Game Design Handbook (game feel and feedback) · Production Handbook (outsourcing process) · Resources (tools and asset sites, §2.2-2.6, §5) · Pitfalls & Anti-patterns (art/audio chapters).
> Audience: developers who did not come from art but want to ship a complete game, and art leads on small teams; this does not replace a systematic art course — the emphasis is on pipelines and specs.

---

## 1. Art Direction and the Art Bible (do this before production starts)

- **Mood board**: collect 8–15 references (color/composition/brushwork/lighting) and mark "what we want / what we don't"; produce 1–2 "target mockups" (hire an artist, or paint them yourself until they are presentable).
- **Art Bible minimum set**: palette (primary/secondary/semantic colors) · line and brushwork rules · lighting and value hierarchy · resolution and spec sheets · naming conventions · reference gallery (including a "counter-examples" section).
- **Style = a combination of constraints**: a limited palette, consistent outlines, one light direction. "Restraint" reads as more professional than "piling on detail".
- **Feasibility check**: for every style decision, ask "how long does one asset take? And 100 of them?", because the style must be mass-producible (see the art workload pitfall in Pitfalls & Anti-patterns).

## 2. 2D Pipeline

### 2.1 Three 2D Styles and Their Specs

| Style | Key specs | Tools | Watch out |
| --- | --- | --- | --- |
| Pixel art | Fixed internal resolution (e.g. 320×180); unified PPU (pixels per unit); palette limits; pixel-perfect camera | Aseprite/Pixelorama/LibreSprite | Non-integer scaling blurs; rotate/scale in integer steps where possible |
| Hand-drawn/cartoon | Consistent outlines and brushes; layering (line art / base color / shadow / effects) | Krita/Photoshop/Procreate | Layer conventions and export (PSD → layered import into the engine) |
| Vector/flat | SVG/assets built from shapes and color; consistent strokes | Inkscape/Affinity/Illustrator | Engines usually rasterize on import; fix your resolution tiers in advance |

### 2.2 2D Animation

- **Frame animation**: frame-count conventions (8/12/24 fps are common), loop and non-loop animations separated, squash & stretch keyframes.
- **Skeletal animation**: Spine/DragonBones (→ Resources §2.4); re-skinning and part swaps are cheap, which suits producing characters at volume; lock down the skeleton import pipeline into the engine.
- **Procedural assistance**: tweened parameter animation (translation/scale/skew) replaces a large share of hand-drawn inbetweens — cheaper and tunable.
- Animation acceptance: check **both** frame-by-frame playback and in-game playback on the target build (sprite sheets mask problems).

### 2.3 Sprite Slicing and Import

- Atlas planning: group by scene/function, reserve suffix conventions (`_n` normal, `_e` emissive); guard transparent edges against bleed (2–4px padding prevents sampling fringes).
- Naming example: `char_hero_idle_01.png` (category_subject_action_index); script the import settings (filtering/compression/anchor).

## 3. 3D Pipeline

### 3.1 Modeling Conventions (programmer-friendly hard constraints)

| Item | Example spec | Why |
| --- | --- | --- |
| Units and facing | 1 unit = 1 meter; face +Z (per engine convention) | Physics and animation compatibility |
| Poly budget | Characters 5k–30k tris (tiered by platform); modular scenes | Performance budget (Programming Handbook §3.1) |
| UVs | No overlap, margins kept, consistent orientation | Baking and texture reuse |
| Naming | SM_/SK_/M_/T_ prefixes (static mesh/skeletal/material/texture) | Batch processing and automated lookup |
| Pivot | Bottom center (characters/props) | Spawn and placement efficiency |

### 3.2 Textures and Materials (PBR minimum concepts)

- PBR maps: Albedo (no lighting information) · Roughness · Metallic · Normal · AO (optional).
- Texture specs: power-of-two sizes (512/1024/2048); compress per platform (desktop BC/ASTC, mobile ASTC/ETC2); texture atlases and channel packing (e.g. Metallic-Smoothness combined).
- Material count control: fewer material types are easier to optimize; use a parameterized Master Material plus instances.

### 3.3 Animation and Retargeting

- 3D animation basics: keyframe animation (for a small number of actions) vs skeletal animation; Mixamo for fast prototyping (→ Resources §2.3).
- Retargeting: conventions for sharing animations across different skeletons (naming conventions, T-pose, proportions) — settle the skeleton first, then mass-produce animations.
- Align the animation state machine (engine side) with the art deliverables: an action list (Idle/Walk/Run/Turn/Jump/Fall/Attack×N/Hit/Death…) plus loop/event points (footstep points/hit frames).

### 3.4 Level/Environment Art

- **Modular kits**: standard meshes (walls/floors/corner pieces) combine into scenes; the 45° texture orientation trick for reuse.
- **Lighting and atmosphere**: lightmap vs real-time GI trade-offs; fog/skybox/post-processing (bloom/tonemapping) to unify the look.
- **Performance**: occlusion culling, LOD chains (LOD0-3), distant impostors.

## 4. UI and Graphic Design

- **9-slice**: export buttons/panels by stretch regions; cover all four states (normal/hover/pressed/disabled).
- **Icon system**: one shared grid (e.g. 24/32/48), pick either line or filled style; export SVG plus multi-scale bitmaps.
- **Fonts and typography**: distinct fonts for headings/body/numerals; CJK–Latin mixed typesetting, line height, outline and shadow contrast rules; minimum readable size (mobile: ≥ 12sp for regular text).
- **Resolution strategy**: anchors (edge elements pinned to the edges, dialogs centered) + proportional scaling (core area scaled uniformly) + an adaptation checklist for ultrawide/narrow screens; keep the UI consistent with the 3D world's feel (color tone/corner radius/materials).

## 5. Technical Art Primer (the Bridge Between Programming and Art)

- **Shader mental model**: vertex shader (position/deformation) → rasterization → fragment shader (color/lighting); learn to "tune parameters" (material instances) first, then to "write logic".
- **Common effects**: particle systems (emission/lifetime/curves), flipbook effects, trails, dissolve/rim light (common shader prefabs).
- **Effect performance**: overdraw ranking (full-screen post-processing > large particles > translucent UI); effect tiers (disable post-processing and lower particle density on low-end devices).
- **Asset convention enforcement**: import validation scripts (oversized textures/wrong naming/wrong material types → CI warnings); a TA's output is not the effects themselves, it is "the pipeline that keeps art mass-production from going off the rails".

## 6. Art Outsourcing and Asset Usage (process)

1. **Requirements package**: reference images + spec sheet (size/format/layers/naming) + delivery format + acceptance criteria (quantifiable: e.g. "three-view proportions consistent, palette matches the Art Bible").
2. **Paid test**: order one test piece first (paid); go to batch production only once style and communication pass.
3. **Milestones and acceptance**: staggered delivery (draft → line art → coloring → final), confirm each stage before continuing; source files (PSD/Blender) must be handed over.
4. **Archiving**: an asset ledger (source/author/license/modification record), including AI-generation records (see the Legal, Patents & Competition Handbook / Pitfalls & Anti-patterns).

- Using asset sites (Kenney/Aigei, etc.) → Resources §5; **check the license of every asset and keep the proof**.

## 7. Audio Design (from the sound designer's perspective)

- **Feedback layers** (layer first, then design the sounds):

  | Layer | Examples | Principle |
  | --- | --- | --- |
  | Core feedback | Jump/hit/pickup/taking damage | Must be clear, distinct and low-latency; top priority |
  | Status cues | Low health/ability ready/countdown | Loopable but restrained; avoid fatigue |
  | Ambience | Wind/water/crowds/machines | Builds space and mood; the lowest volume layer |
  | UI sounds | Click/confirm/error | Short, light, one unified timbre family |
  | Music | BGM/dynamic music | The emotional carrier (§8) |

- **Dynamic mixing**: bus structure (Master→Music/SFX/Voice/UI); sidechain/ducking (music automatically ducks under dialogue); priority and concurrency caps (Programming Handbook §2.7).
- **Spatialization**: 2D games simplify it (left-right panning); 3D uses distance attenuation + reverb zones (switching between indoor/cave).

## 8. Music Design

- **Structure**: loops (seamless head-to-tail) · transition stingers (event-triggered) · layers (base/tension/combat, stacked).
- **Three modes of adaptive music**: vertical layering (stacking within the same track), horizontal re-sequencing (switching section order), transition bridges (in/out points); build the simplest layering first, and complicate it only after validating.
- **Tied to gameplay**: music intensity follows combat/exploration state (parameterized, not hard cuts); reserve "phase transition" sections in boss music.
- **Production options compared**: custom composition (best quality and fit) · royalty-free libraries (fast, cheap, prone to duplicate tracks) · AI generation (fast; mind licensing and disclosure, see the Legal, Patents & Competition Handbook). **The license must cover: worldwide/perpetual/commercial/editable**.

## 9. Audio Implementation (the interface between programming and audio)

- **Event-driven playback**: game code emits semantic events (`footstep_grass`, `ui_confirm`), and the audio side decides the concrete samples and randomization — decoupled, and it lets audio iterate independently.
- **Middleware concepts** (FMOD/Wwise, see Resources §2.6): events · parameters (intensity/environment) · snapshots (state switching) · buses.
- **Implementation checklist**: audio pool and concurrency caps, streaming (long music), pause/scene-transition handling, music that persists across scenes, settings (master volume/category volumes/mute toggle defaults).
- **Performance notes**: decode cost (CPU for decoding compressed formats), memory (audio caches), background audio behavior on mobile.

## 10. Delivery Specs and Checklists

### 10.1 Spec Sheet (agree with art/audio before work starts)

| Asset type | Spec items | Example standard |
| --- | --- | --- |
| 2D art | Size/format/PPU/naming | PNG, 2x art @PPU 100, `ui_icon_sword@2x.png` |
| 3D models | Units/poly count/UVs/naming/pivot | Metric, characters ≤15k tris, SM_ prefix |
| Textures | Size/channels/compression | 1024 power-of-two, Albedo+Normal+RMA packed |
| Audio | Format/loudness/sample rate/looping | OGG (music)/WAV (short SFX), unified target loudness (LUFS standard), seamless loop points |
| Fonts | License/subsetting/fallback | Keep records of free commercial licenses; subset by language to reduce size |

### 10.2 Pre-launch Checklist

- [ ] Spot-check all assets for Art Bible consistency (palette/style/size)
- [ ] All assets follow naming and directory conventions (scannable by script)
- [ ] Atlas/material/audio category budgets not exceeded (Programming Handbook §3.1)
- [ ] Audio loudness unified, loops seamless, settings items work
- [ ] Asset and AI-asset ledger complete (license proof + modification record)
- [ ] Low-end/mobile fallback paths verified (effects/post-processing/texture tiers)
- [ ] UI tested at all resolutions + multilingual overflow tested

> Further reading: art learning resources (Saint11 pixel art tutorials, Gnomon, ArtStation, etc.) are listed in Resources §3 and the standalone art resources list.
