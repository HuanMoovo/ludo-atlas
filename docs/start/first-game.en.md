# Ludo Atlas · Getting Started · Your First Game

> **Getting Started**. The goal is not to make a good game, but to **make a game that is finished**. The ability to "finish" is worth more than any single technical point. This page gives a complete 30-day plan at 2-3 hours a day.

## 1. Set the Rules First

- Scope: small enough for one person to finish in 2-6 weeks. Write the ceiling onto a single page: 1 core mechanic, 3-5 levels, 15-30 minutes total playtime.
- Assets: your first game is allowed to use free assets throughout (see [Resources](../../resources/README.md)).
- Bar: playable, completable, has sound effects, a title screen, an ending screen, and can be shared with friends.
- Bans: no multiplayer, no open world, no personal dream project (that is for your second game).

## 2. Pick a Project

Choose one from the list below; do not invent a new one:

| Project | Difficulty | What You Will Practice |
| --- | --- | --- |
| Breakout / Space Invaders | ★ | Input, collision, loops |
| Platformer (3 levels) | ★★ | Game feel, level pacing |
| Top-down shooter (wave survival) | ★★ | Enemy spawning, balance |
| Sokoban-style puzzle (10 levels) | ★★ | Mechanic design, undo |
| Endless runner | ★★ | Procedural generation, difficulty curve |
| Small-scale tower defense (5 waves) | ★★★ | Balance, UI, state machines |

## 3. The 30-Day Calendar

**Week 1: Minimum Playable**

| Day | Task |
| --- | --- |
| 1 | Install the engine, complete the official getting-started tutorial, set up a repository |
| 2 | Character can move + one core action (jump / shoot / push) |
| 3 | First enemy or obstacle + win and lose conditions |
| 4 | Complete main loop: start, play, die, restart |
| 5-7 | Tune the core mechanic until "you are willing to replay it yourself" |

**Week 2: Content and Pacing**

| Day | Task |
| --- | --- |
| 8-10 | Build 3-5 levels/waves with rising difficulty |
| 11-12 | Clear conditions, scoring, progress saving |
| 13-14 | First playtest with someone else; log every sticking point and confusion |

**Week 3: Presentation and Polish**

| Day | Task |
| --- | --- |
| 15-16 | Sound effects and music (assets will do); fill in feedback (hits, scoring) |
| 17-18 | Screen adaptation, title screen, pause menu |
| 19-20 | Fix issues from playtest feedback; performance checks (play on the target device) |
| 21 | Freeze content; fix bugs only |

**Week 4: Release**

| Day | Task |
| --- | --- |
| 22-23 | itch.io page: name, description, 3 screenshots, 1 GIF |
| 24-25 | Package a Windows build (add a web build if you have energy left); write the controls documentation |
| 26-27 | Share at a small scale, collect feedback, fix the last batch of issues |
| 28-30 | Release; write a postmortem (use the [Postmortem Template](../../templates/postmortem.md)); start thinking about the next one |

## 4. The "Finished" Acceptance Checklist

- A new player can learn the controls within 5 minutes (without you explaining beside them).
- From launch to completion, there are no freezes or crashes anywhere.
- There is a title screen and an ending screen; it is clear whether you "won / lost".
- There is sound, and it can be turned off.
- It runs on someone else's computer (not just your development environment).
- There is a shareable link or file.
- You wrote a postmortem for it.

Tick all of the above and the first game counts as finished. If one or two items are missing, go fill them in; do not start a new project.

## 5. Common Failure Modes and Countermeasures

| Failure mode | Symptom | Countermeasure |
| --- | --- | --- |
| Scope explosion | "Let's add multiplayer too" | Log every idea in the "next game" list |
| Tutorial hell | 3 hours of tutorials, 5 minutes of coding | Write code for 1 hour each day before you allow yourself tutorials |
| Engine-switching addiction | Still choosing an engine in week 3 | Go back and read the last section of the [Engine Selection Guide](engine-choice.md) |
| Perfectionism | Redrawing the protagonist over and over | Asset freeze day: day 15 |
| Not shipping | "A bit more polish" | Put the release date in the calendar; as non-negotiable as a promise to a friend |
| Giving up when nobody bites | The first project gets no attention | The goal of a first project is to "learn to finish", not to "succeed" |

## 6. After Release

1. Write a postmortem (data + feelings + adjustments for next time) and save it in the [postmortems section](../postmortems/README.md).
2. Take the three things you most want to change from the postmortem as practice goals for your second game.
3. Keep the second project within double the scope. Progress step by step until you can handle your dream project.

## Further Reading

- [Learning Paths](learning-path.md): fit "making games" into your long-term plans.
- [Production Handbook](../fundamentals/production/README.md): the proper way to do scope control.
- [Multi-platform Launch](../../playbooks/platform-launch/README.md): for when you want to push your work out through more formal channels.
