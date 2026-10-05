# Ludo Atlas · Renderer from Scratch

> A project-based route into advanced graphics: software rasterization → real-time rendering APIs → ray tracing / modern APIs — three stages, acceptance criteria and resources.
> Companion reading: Programming Handbook · Engine Internals Path · Open Source Picks & Book Recommendations (the graphics book list).
> Who it's for: developers with programming fundamentals who want to genuinely "write" graphics. The full route runs about 9–12 months at 4–6 hours a week.

---

## 1. Why Write a Renderer

Understanding a graphics article and being able to write a renderer are separated by a river. Writing a renderer is one of the few projects that trains three things at once:

- **Math made concrete**: linear algebra goes from "I studied it" to "I've used it".
- **Systems skills**: resource management, state machines, performance analysis — the whole set, walked through once.
- **Portfolio piece and talking point**: hard currency for interviews in graphics, engine and TA roles; one renderer with real substance beats any number of adjectives.

## 2. Route Overview

| Stage | Content | Reference duration | Acceptance |
| --- | --- | --- | --- |
| One | Software rasterizer | 4–8 weeks | Render a classic model with textures, lighting and shadows |
| Two | Real-time rendering API (pick one of three) | 3–5 months | A self-built small scene running at 60fps |
| Three | Advanced direction (pick one) | As needed | Ray tracer / modern-API rewrite / feature specialization |

Do not reverse the order. Software before hardware is the consensus of everyone who has been through it: Stage One lets you see every concept clearly, with no API magic in the way; Stage Two is where you learn how an API expresses them.

## 3. Stage One: Software Rasterizer

**Route**: start from tinyrenderer's approach, begin by drawing a line, and write your way, line by line, up to a complete renderer.

Course content, in order:

1. Drawing lines (Bresenham's algorithm) and wireframe models.
2. Triangle rasterization and barycentric interpolation.
3. z-buffer depth testing: solving occlusion.
4. Texture mapping and perspective-correct interpolation.
5. Lighting: Gouraud to Phong, normals and diffuse reflection.
6. Shadow mapping (software-rendered) and simple post effects.

**Language is up to you**: C++ is smoothest, Rust works too, and you can even start in Python (never mind performance; concepts matter most). **Acceptance criteria**: render the classic head model (textures, lighting and shadows all in place), and be able to derive every algorithm by hand on a whiteboard.

Resource: the tinyrenderer tutorial and code (https://github.com/ssloy/tinyrenderer).

## 4. Stage Two: Real-Time Rendering APIs

Pick one of three routes, according to your goal:

| Route | Representative tutorial | Best for | Notes |
| --- | --- | --- | --- |
| OpenGL | LearnOpenGL | First choice; the most complete conceptual system | Abundant material in the Chinese-language community; the widest concept coverage, and interview concepts mostly come from here |
| WebGPU / WebGL | WebGPU Fundamentals / WebGL Fundamentals | A front-end background, wanting to run in the browser | Modern API design; convenient cross-platform demos |
| Vulkan | Vulkan Tutorial | Aiming for an industry engine role | Explicit memory and synchronization; the highest barrier — best attempted after a foundation in one of the first two |

Lesson-by-lesson checklist (the OpenGL route as reference): window and context → first triangle → shaders → textures → camera → lighting (basic / materials / light maps) → model loading → depth testing and stencil → blending → framebuffers → shadow mapping → normal mapping → PBR → post-processing (bloom, etc.).

**Acceptance criteria**: one small self-built scene: floor plus a model, sunlight plus shadows, one post-processing effect, a stable 60fps. Record a video of the result — this is portfolio material.

## 5. Stage Three: Advanced Directions (Pick One to Go Deep)

- **Ray tracing**: start with the Ray Tracing in One Weekend series (https://raytracing.github.io/), and relearn how light propagates from a per-pixel point of view. Extension project: a CPU ray tracer plus denoising.
- **Modern-API rewrite**: rebuild the Stage Two scene in Vulkan or WebGPU, and get a feel for what "explicit control" buys you.
- **Feature specialization**: pick one graphics feature and dig to the bottom of it (global illumination, shadow techniques, volumetric fog, procedural skies); build a demo and write a technical article.
- **GPGPU**: play with particles, fluids and cloth in compute shaders, and open the door to "a graphics card does more than draw pictures".

## 6. How to Learn

- **Run it, then change it**: after every lesson, do three things without fail — change a parameter, add a small feature, deliberately break it and then fix it.
- **Write notes**: at least three posts per stage (concept understanding, pitfalls log, work showcase). Writing is the check that presses "I feel I've got it" back down into "I've actually got it".
- **Build performance habits from day one**: log frame times, learn to read GPU profiler data; performance intuition is a core asset for anyone in graphics.
- **Patch up the math when you meet it**: fill in linear algebra as the course progresses (the 3Blue1Brown series; for 3D Math Primer for Graphics and Game Development, see Open Source Picks & Book Recommendations). Don't study math for three months before you start building — that's procrastination in its most advanced form.

## 7. Common Pitfalls

1. Watching without writing — bingeing the videos and believing you've learned it.
2. Skipping Stage One and going straight at Vulkan, then getting scared off by synchronization and memory management.
3. Taking no notes; three months later, everything is back to zero.
4. Over-tinkering with the toolchain (swapping window libraries and build systems in and out), with zero progress on the core content.
5. Expecting quick mastery, and giving up when no "big work" appears after two months.
6. Grinding on without patching up the math, dying over and over at matrix transforms.
7. Not documenting your work, so there is nothing to show in an interview.
8. Forever copying tutorials, never adding changes of your own (an interviewer sees through it at a glance).
9. Chasing visual effects only, unable to analyze performance (a guaranteed fail item for graphics roles).
10. Pushing ahead on a single thread before really absorbing it; the unpaid debt compounds with interest.

## 8. Resource Entry Points

- tinyrenderer (software rasterization): https://github.com/ssloy/tinyrenderer
- LearnOpenGL: https://learnopengl.com/
- WebGL Fundamentals: https://webglfundamentals.org/
- WebGPU Fundamentals: https://webgpufundamentals.org/
- Vulkan Tutorial: https://vulkan-tutorial.com/
- Ray Tracing in One Weekend: https://raytracing.github.io/

> For books and more open-source projects, see Open Source Picks & Book Recommendations; for reading engine source code alongside this route, see the Engine Internals Path.
