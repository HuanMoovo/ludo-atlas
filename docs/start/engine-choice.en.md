# Ludo Atlas · Getting Started · Engine Selection Guide

> **Getting Started**. This page helps you settle on an engine once, and never agonize over the choice again. Conclusion first: any mainstream engine can carry a game to completion, and the cost of switching engines is far lower than the cost of staying in selection mode forever.

## 1. Answer Four Questions First

1. **Target platform**: PC / console / mobile / mini-game / web? Desktop Steam and WeChat mini-games have completely different engineering requirements.
2. **2D or 3D**: Or a mix of both? This is the biggest divide.
3. **Your programming background**: Zero experience, a little scripting, or a seasoned programmer?
4. **Team and timeline**: One person for three months, or five people for a year?

## 2. The Decision Path

Walk this chain of checks in order:

1. Making a visual novel or pure text narrative → start with Ren'Py, don't overthink it.
2. Pixel art or small-scale 2D, wanting a fast ramp-up → Godot or GameMaker.
3. 2D with future mobile plans and a need for a large ecosystem → Unity or Godot.
4. Realistic 3D, large team, aiming for big-studio pipelines → Unreal.
5. Mid-scale 3D indie game → Unity or Godot (depending on art style).
6. Only small, browser-playable web games → Phaser / PixiJS; 3D showcase pieces → Three.js / Babylon.js.
7. Wanting to "hand-code everything" to learn the low level → raylib / LÖVE / Pygame and similar frameworks.
8. None of the above, or you have non-standard requirements → go back to item 1 and ask yourself again; a custom engine is the last resort.

## 3. Main Routes Compared

| Engine / Framework | Positioning | Primary language | Strengths | License and cost notes |
| --- | --- | --- | --- | --- |
| Godot | All-purpose open-source engine | GDScript / C# | Balanced 2D/3D, lightweight, fully open source | MIT; no revenue share, no royalties |
| Unity | Commercial all-purpose engine | C# | Largest ecosystem; mature mobile and 2D toolchains | A free personal tier exists; commercial terms per the official site |
| Unreal | AAA-grade engine | C++ / Blueprints | Top-tier visuals; film-grade pipeline | Free to download; revenue share above a revenue threshold |
| GameMaker | Rapid 2D development | GML | Fast prototyping; suited to pixel art and small-scale 2D | Free version is limited; commercial release requires a license |
| RPG Maker | RPG-specific | Scripting | Turn-based RPGs work out of the box | Paid software; watch asset licensing |
| Ren'Py | Visual novel-specific | Python family | Branching narrative; save and rollback out of the box | Free and open source |
| Web engines (Phaser / PixiJS / Three.js / Babylon.js) | Browser games | JavaScript / TypeScript | Zero-install distribution; web 3D | Open source; check each engine's own license |
| Lightweight frameworks (raylib / LÖVE / Pygame) | Code-first | C / Lua / Python | Learn the fundamentals; full control | Permissive open-source licenses |
| Bevy | Rust data-driven engine | Rust | ECS architecture; performance and safety | Open source; ecosystem still growing |
| Custom engine | Bespoke | Any | Full control | Very high cost; usually not the first choice |

## 4. Recommendations by Scenario

| Scenario | First choice | Alternative | Notes |
| --- | --- | --- | --- |
| First game (small-scale 2D) | Godot | GameMaker | Low complexity; plenty of community tutorials |
| Commercial mobile project | Unity | Godot | Mobile toolchain and plugin ecosystem |
| Realistic 3D | Unreal | Unity | Rendering and content pipeline advantages |
| Visual novel | Ren'Py | Godot + plugins | Purpose-built tools save half the work |
| WeChat / Douyin mini-games | Read [Mini-Game Development](../publishing/minigame/README.md) first | Depends on the platform plan | Unusual constraints on package size and performance |
| Playable in the browser | Phaser (2D) / Babylon.js (3D) | Three.js | Zero-install sharing |
| For learning programming | raylib / LÖVE | Pygame | Hand-write the loop; understand every pixel |

## 5. Common Dilemmas, Straight Answers

- **Unity or Godot**: For small personal 2D projects, choose Godot; if your goal is industry employment or a commercial mobile project, choose Unity. Knowing both is the ideal state.
- **Is Unity a waste for 2D**: No. The 2D toolchain is mature; the only downside is a slightly heavier startup.
- **Can Unreal do 2D**: Yes, but the ecosystem and tutorials lean toward 3D, and a 2D project has no need for it.
- **Can web engines ship commercial games**: Yes. Web distribution is a real channel for indie games; just set your performance expectations correctly.
- **Is a custom engine worth it**: Not unless the engine itself is your product, or your team is large enough to be constrained by commercial engine terms.

## 6. Discipline After You Choose

1. Choosing is committing: finish at least one complete, releasable work before you even consider switching.
2. During the learning phase, use tutorials from a single source only (official documentation first); no hopping between tutorials.
3. Put version control in place from the very beginning; follow the engine's official template for directory structure.
4. Treat "switching engines" as a migration, not relearning: the concepts (nodes, components, scenes, lifecycle) carry over across engines.

## Further Reading

- [Your First Game](first-game.md): with the engine chosen, make your first project in 30 days.
- [Resources](../../resources/README.md): official entry points, tutorials, and communities for each engine.
- [Programming Handbook](../fundamentals/programming/README.md): general engineering knowledge inside and outside the engine.
