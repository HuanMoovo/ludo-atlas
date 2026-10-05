# Ludo Atlas · AI Workflows · AI Agents

> This page is a companion volume to the AI Workflows Handbook: it moves "get an agent to do the work for you" from one-off Q&A to a complete form that can be orchestrated, reviewed and rolled back.
> The snapshot is October 2026, consistent with the main volume: methods first; for tool names and versions, go by the official sites (entry points in Resources §2.9).
> One boundary up front: an agent can act on its own, but responsibility does not move with it. Every step it takes has to land somewhere you can review and roll back.

---

## 1. Where Agents Differ from Chat Q&A

| Capability | Chat Q&A | Agent |
| --- | --- | --- |
| Reading the codebase | You paste it in | Reads and searches on its own |
| Running commands | Can't | Runs commands and tests itself |
| Task span | One question at a time | Drives long tasks forward on its own |
| Output | Text | Landed changes: files, diffs, commits |

The difference comes down to one sentence: it can change things on its own. The benefit is fewer round trips; the new problems are overreach and going off track, and half of this page is about keeping those two in check.

## 2. Forms and Representatives (October 2026)

| Form | Representative | How it plugs in | Good for |
| --- | --- | --- | --- |
| Terminal agents | Claude Code, Codex CLI, Gemini CLI, opencode, aider | Runs in the repo, reading and writing files and commands directly | Large changes, cross-file tasks, scripted batches |
| Editor agents | Cursor, Copilot, Cline, Continue, Windsurf | Inline completion and chat inside the IDE | Editing as you go, local tasks |
| Cloud agents | various vendors' ticket-style coding agents | You dispatch tasks, they run queued and produce PRs | Parallel small tasks, without tying up local resources |
| Pipeline bots | agent scripts in CI (with GitHub Actions and the like) | Run fixed jobs in CI | Routine maintenance, test fixes, doc sync |

For tool choice, we keep the main volume's conclusion: getting one primary tool running smoothly pays off more than switching around. The point is not the form; it is the workflow.

## 3. What a Long Task Looks Like (Plan, Execute, Verify)

1. **Write the acceptance criteria**: the expected behavior first, or a test you can run.
2. **See the plan first**: have it produce a step list and spend a minute reading it. Discovering the wrong direction after three hours of running is a common incident.
3. **Limit the scope**: one feature point at a time; state which directories may be edited and leave everything else untouched.
4. **Set checkpoints**: commit once per node passed. Agents make mistakes, and checkpoints decide the cost of correction.
5. **Read the diff yourself**: not reading the diff does not count as done.
6. **Wrap up**: write new conventions back into AGENTS.md and clear out temporary scripts.

Four hard rules: one thing at a time; a clean commit before any work starts; on failure, roll back to the previous checkpoint; nothing passes until all tests are green.

## 4. Multi-Agent and Orchestration: When It Pays Off

- **Parallelizable work**: modules with no dependencies between them, batch migrations, multilingual translation, refactors split by directory.
- **Common pattern**: one lead agent writes the task list, several worker agents each take one piece, and acceptance runs against the list at the end.
- **When it is worth it**: the task can be decomposed, the interfaces are clear, and you can afford the review. Review cost is usually the bulk of it.
- **When it is not worth it**: coupled changes, vague requirements, small things you could finish in passing.
- **Conflict handling**: when several agents edit the same repo, assign file ownership first; leave merge conflicts to human judgment — don't let them patch each other.
- **A pragmatic reminder**: in most indie development situations, serial small steps plus frequent commits are enough. Orchestration is a tool, not an arms race.

## 5. Context Engineering, Advanced (an Expansion of the Main Volume's §2.2)

- **Layer the standing files**: AGENTS.md (commands, conventions, no-go zones) comes first; add SPEC, ARCHITECTURE and decision records as needed; keep appending to the pitfall log.
- **Spell out what not to use**: no new dependencies, don't enable this pattern. Preventing drift is cheaper than correcting it afterwards.
- **Memory lives in the repo**: facts that stay true long-term go into files, not session memory; they come along when you switch tools.
- **Turn repeated processes into skills**: when you explain the same steps for the third time, write it as a Skill — the method is in Skills for Game Development.
- **Anti-patterns**: stuffing the whole knowledge base into context; writing a large spec that never gets updated.

## 6. Permissions and Security

- **Least privilege**: start read-only; grant write access per directory; open the command allowlist item by item.
- **Credential management**: keep tokens in environment variables or the local credential store — not in the repo, not in prompts.
- **Actions that always get human confirmation**: deleting files, force-pushing branches, releasing, payments, changing CI secrets.
- **Auditing**: require commit messages to state what changed and why; when something goes wrong, you can replay it.
- **Sandboxing**: if it can run in a container or a VM, don't let it hold the host machine directly.

## 7. Cost Accounting

To decide whether an agent should do a piece of work, work out three numbers:

- the direct spend on tokens or subscriptions;
- your review time (reading, verifying, rework);
- incident cost (the probability of an error multiplied by its cost).

Signs it pays off: fast verification, high repetition, no contact with core game feel. Signs it doesn't: vague requirements, aesthetic decisions, fine-tuning where you know the details better than it does. The simple standard: if the time saved minus review and rework still leaves a surplus, use it; if not, do it yourself.

## 8. Task Checklist for Game Projects

| Task | Recommended form | Checkpoint |
| --- | --- | --- |
| Boilerplate code and tool scripts | Terminal agent | Run it once + read the diff yourself |
| Bulk conversion of data tables and configs | Terminal agent (scripted) | Row counts and samples match before and after |
| Bulk scene building and property changes | Engine MCP (main volume §3) | Screenshot comparison + commit on a branch |
| Smoke-test bot | Headless run + CI | All log assertions pass |
| Localization batches | Terminal agent + glossary | Sampled close reading per language |
| Crash log clustering | Terminal agent | Human review of the groupings |
| Docs and changelog drafts | Editor agent | Public-facing text finalized by a human |
| Store asset cleanup and naming | Editor agent | Human final check of sizes and specs |

## 9. Pitfalls Specific to Agents

1. A long task goes off track and never comes back. Set checkpoints; when it goes wrong, roll back — don't let it keep running while patching as it goes.
2. The fix list keeps growing. With no hard scope limit, it will refactor everything along the way.
3. Reports that don't match reality. The summary sounds great while the diff is full of something else: go by the diff alone.
4. Context rot. When one session accumulates change after change and piled-up requirements, a fresh task is cleaner than carrying on.
5. Incidents from excessive permissions. Gates like deletion, force-push and release must have human confirmation.
6. Treating orchestration as an achievement. Ten things running in parallel that you can't review equal ten things not done.
7. Hallucinated APIs. Paste the official docs to it, or require it to check the docs for its version before it starts.

## 10. A One-Day Onboarding Path

1. Pick one primary agent, install it, sign in, and get it running once in a test repo.
2. Write an AGENTS.md of ten lines or fewer: build command, test command, no-go zones.
3. Pick one low-risk repetitive job (bulk renaming, script generation) and run it through the §3 process once.
4. Write down this run's checkpoint list and reuse it for the next task.
5. Distill one repeated process into a Skill, and move on to the next topic.

---

> Companion reading: the main volume, the AI Workflows Handbook (decision table, work loop, red lines); the topic page Skills for Game Development (skill pack checklist and setup); Resources §2.9 (tool and ecosystem entry points); design doc §14.3 (engine MCP).
