# Ludo Atlas · Playbooks · Portfolio to Job

> **Playbook**. Positioning: turn "things you've made" into "evidence that gets you hired": how to assemble a portfolio and where to host it, how to write a resume and where to send it, how to tackle test tasks and interviews, and how to keep going when no one replies.
> Companions: Indie Developer Profiles (how others entered the industry and changed tracks) · Indie Developers & Companies (meet the people in the industry first) · Game History (background material for talking about industry context in interviews) · Pitfalls & Anti-patterns (a full-pipeline pitfall cross-check).

---

## 1. Applicability and Goals

Applies when:

- You have 1–3 runnable projects in hand and are preparing to enter the industry's job market (any track: programming, design, art, audio, production, QA, publishing, or live-ops).
- You are on the "Job Hunting" route of Learning Paths, switching from skills practice to the portfolio and application stage.
- You have sent out a batch of resumes but heard little back, and want to know which link is stuck.

Does not apply when: you haven't yet made something that runs — finish [Your First Game](../../docs/start/first-game.md) first; if the goal is independent publishing, turn to Indie Survival.

Goals (1–3 months):

1. Turn existing projects into job-hunting materials that a stranger can understand on their own and verify on the spot (portfolio, showcase channels, resume).
2. Complete at least two full application cycles: apply → test task → interview → feedback.
3. Get an offer, or get a list of "where the gaps are and what to fill next".

Three principles:

1. **Job hunting is a chain — fix the weakest link first**: portfolio, resume, applications, test tasks, interviews — if any link breaks, everything downstream goes to zero; when reviewing, first ask "which link got stuck this time".
2. **Evidence first; adjectives are void**: recruiters will only open the link, launch the build, and probe the details; an unverified "familiar with" or "expert in" counts as not written at all.
3. **Feedback loop**: every batch of applications gets a ledger and a review; silence is data too — use it to correct the next batch, not to beat yourself up.

Time budget: 2–4 hours a day, plus one focus day each week; applying itself is cheap — don't delay it with "just a little more prep".

## 2. The Full Process

The main loop, written as a verb chain:

`Break down target roles → Fill evidence gaps → Polish works → Apply → Test task → Interview → Write reviews → Patch weak spots`

Loop until you get an offer or confirm the gaps; normally two to four rounds.

| Stage | Output | Duration |
| --- | --- | --- |
| Direction and benchmarking | Target role list (tiered into stretch, match, and safety) + a high-frequency skills table distilled from 20 job descriptions | 1–2 weeks |
| Portfolio takes shape | The trio (complete, flashy, role-matched) + a one-page write-up per work | 2–6 weeks, rolling alongside applications |
| Showcase channels and resume in place | itch.io entries, tidied code repositories, a one-page resume, a landing point for the portfolio | 1–2 weeks |
| Applications and test tasks | Application ledger + test task delivery package | 2–4 weeks per batch |
| Interviews and reviews | Retrospective talking points, an answer log, a gap list | 1–3 weeks per round |
| Iteration | Rework works and skills against the gap list, then start the next batch | Continuous |

The full process, from starting to organize to getting a clear result, commonly takes 2–4 months. Most of the time goes into polishing works and waiting for feedback; the act of applying itself is only a small part.

## 3. Step-by-Step Execution

### 3.1 The Portfolio Trio

Each piece in the trio answers one question: can you finish things, where is your ceiling, and do you match the role. Quantity discipline: three polished works beat ten half-finished ones.

| Work | Question it answers | Passing bar (observable) |
| --- | --- | --- |
| Complete work | Can you finish things? | A stranger can get playing within 10 minutes on their own; it has a beginning and an end; it exists as a release (downloadable or playable in the browser) |
| Technical showpiece | Where is your ceiling? | One interactive demo plus a one-page technical write-up: the hard problems, the approach, the trade-offs, how it was verified |
| Role-matched piece | Do you match this role? | A recruiter holding the job description can find evidence in your work, line by line |

Fine-tune by role:

- Programming roles: pick a systems case in your target direction (gameplay, tools, rendering, server-side) as the role-matched piece; a code repository is mandatory.
- Design roles: use a "breakdown doc + a playable level or test work" as the role-matched piece, showing the whole path from judgment to execution.
- Art roles: the role-matched piece is a thematically consistent asset set (characters, environments, and UI in one style), with process drafts attached; for audio roles, use an audio implementation case where the implementation thinking is audible, not a pure collage of raw assets.
- Production, QA, and live-ops roles: use a schedule-management case, a test report, content planning, or a data retrospective as the role-matched piece.

Write-up baseline (one page per work): what it is, how to play or view it, which parts you were responsible for, what you used (tools and third-party assets), the development period, and known issues. If you followed a tutorial or borrowed assets, say so plainly and credit the source: saying it plainly only costs a few points; hiding it until someone digs it out resets you to zero. Every work must survive being talked about for 15 minutes — if you can't fill 15 minutes, either build up the write-up first or cut the work.

### 3.2 Showcase Channels: Trade-offs Among Three

| Channel | Strengths | Weaknesses | How to use it |
| --- | --- | --- | --- |
| itch.io | Free and instant to open; playable right in the browser; high recognition in indie circles | Recruiters don't often browse it on their own | The default entry point for every playable work; state the controls, session length, and how to play clearly on the page |
| Code repositories (hosting platforms like GitHub) | Shows code quality, commit history, and engineering habits | Art and design roles generally get no viewers; a messy repository is a minus | Essential for programming and technical roles; the README needs three things: what this is, how to run it, and which parts are yours |
| Personal site | One page that lets a recruiter see who you are, what you can do, and where your works are in 30 seconds | Upkeep cost; virtually no organic traffic | The one landing point on your resume; one click through to works and contact details |
| Process records (videos, logs) | Shows process and thinking; a must-have for art, animation, and VFX roles | Video alone can't show playability | Supplementary evidence; does not replace a playable build |

Trade-off principles:

- Startup priority: playable build → code repository (role-dependent) → one-page personal site → process records.
- You get only one chance when a recruiter opens your link: the first screen must be playable or immediately understandable; any entry point that requires signing up, downloading and unzipping, or paging through three screens of instructions should be replaced outright; click through all your links once a month — a dead link is a bigger minus than no link at all.
- Keep the personal site minimal: three paragraphs (who I am, what I can do, where my works are) plus 3–5 links, done in half a day; don't treat it as a work.
- Repository hygiene: a continuous commit history, clean naming, no build artifacts or keys pushed; when recruiters look at your commit history, they are reading your engineering habits.

### 3.3 Resume: Sentence Patterns and Quantification

One page; the top third decides your fate: name, target role, contact details, portfolio link.

Fix the sentence pattern as "verb first + object + method + result". Before-and-after examples:

| Weak phrasing | Strong phrasing |
| --- | --- |
| Responsible for optimizing game performance | Raised the main scene's frame rate from 32 to 60: traced it to excessive draw batches, fixed with atlas merging and occlusion culling |
| Participated in multiplayer module development | Independently implemented state sync for 4-player rooms: held character position error within half a character width under 200ms of poor network |
| Familiar with engines and common tools | Completed and shipped 3 full projects in an engine: 2 of them received playthrough feedback from strangers |

Quantification material:

- Performance and scale: frame rate, memory, load time, build size, draw calls; number of systems, levels, asset sets, and documentation pages.
- Verification and facts: number of testers, completion rate, count of feedback items, event shortlist records; it shipped, people are playing it, an event featured it, strangers picked up the source code.

When you have no numbers, use verifiable facts; don't invent numbers. Fill in the skills table honestly across three levels — "proficient", "have used", "know the basics" — and don't stack up "expert"; for every high-frequency word in the job description, there should be at least one use scenario you can talk through on the spot.

Customization: for every role you apply to, spend 10 minutes on keyword alignment (move the 5 words that keep appearing in the job description into prominent spots on your resume); blasting the same resume everywhere is the number-one killer of response rates.

Keep the cover letter to three sentences:

> Hello, I'm applying for the X role. My resume and portfolio links are below. Two things most relevant to this role: I doubled the performance of a certain system; I shipped a complete project with a level editor. Looking forward to talking further.

### 3.4 Application Strategy and Test Tasks

Application strategy:

- Build a tiered pool: stretch, match, and safety tiers at roughly one third each; the match tier means you cover 70% or more of the skills in the job description.
- 8–15 roles per batch, on a 2–4 week cycle; track everything in a ledger: role, channel, date applied, status, feedback. Start the first application round once your portfolio is at 80 points — where the remaining 20 points should go is something feedback will tell you, and preparing behind closed doors is never finished.
- Channel mix: recruitment platforms, companies' official channels, industry communities and referrals, development events and expos. Referrals work by putting your portfolio into one specific person's hands — save them until the portfolio is in place.

Handling test tasks:

- First clarify four things: the time budget, the delivery scope, which assets and tools are allowed, and whether you may make it public; then pick the smallest slice you can deliver completely: make sure it runs and has a write-up first, and only then talk about bonus points — write your time allocation into the write-up, because the trade-offs are exactly what the recruiter is looking at. Asking questions costs nothing; delivering something oversized costs points.
- The delivery package always has three items: a build that runs as-is, the source code, and a one-page write-up (your reading of the brief, your approach, the trade-offs, known issues, next steps).
- Do not publish or reuse test task content without permission; sync your progress proactively ahead of checkpoints. Keep a retrospective whether the result is good or bad: a test task is the industry's most honest skills calibration.

### 3.5 Interview Prep: Retrospective Talking Points and What to Do When You Can't Answer

The five-part project retrospective (one sentence per part, 3-minute version): background (who it was for, how big the scope), goal (what needed solving), approach (key decisions and trade-offs), results (numbers or verifiable facts), retrospective (what you would change if you redid it). Then prepare a 15-minute version, expanding each part into the "why".

Common follow-up questions and what to prepare:

| Follow-up | What to prepare |
| --- | --- |
| Why did you do it this way? | Two or three alternatives for each key choice, and the reasons you ruled them out |
| Which parts did you do? | Split the division of labor honestly; credit your teammates' contributions to them — two rounds of follow-ups will expose anything else |
| What would you change if you redid it? | Be specific — architecture, process, or scope; "nothing to change" is a minus |
| Where do the numbers come from? | The source and definition of the figures, ready to say off the cuff |

Three steps for when you can't answer:

1. Admit the boundary: I haven't done that, or I'm not sure.
2. Offer adjacent experience: something I've done comes from the same root; my reasoning is...
3. Offer an action plan: if I took this on, the first step I would take to verify.

Don't pretend to know, don't go silent, don't fabricate; what the interviewer is testing is how you work in the face of the unknown. For behavioral interviews, prepare three one-minute stories (team conflict, failure, crunch) set against real projects, with "I" as the subject rather than "we". For the part where you ask questions, prepare three: what stage the project is at, how the team divides work and validates it, and what you are expected to deliver in the first month on the job; the third question verifies the role's real requirements from the other side.

Write notes within 24 hours of every interview: the points you got probed on most, the answers you fumbled, and the points to patch for the next round. If the same question trips you up three times, it isn't a matter of luck.

### 3.6 Sustained Presence: Dev Logs and Community Signals

- Dev logs: one post a week or every two weeks covering "what I did, where I got stuck, how I solved it, and what's next"; post on your main channel and mirror it to the portfolio page. The lulls in your application cycle are exactly when to build signal; sanitized takeaways from each round of test tasks and interviews become your next log entry.
- Process is evidence: recruiters use search to verify the experience on your resume; projects with a public record carry more credibility and are more memorable. A record spanning eight or more weeks is itself a process portfolio.
- Community signals: leave a searchable, positive record in research or development communities (answering questions, joining development events, releasing test builds to collect feedback); a consistently present stranger is easier to remember and refer than a job seeker who suddenly appears.
- Discipline and time-boxing: don't boast, don't put others down, don't leak information about the company you interviewed with; assume every public account will be seen by a future interviewer. Put 2–4 hours a week into this — beyond that, you're eating into development time.

## 4. Acceptance Checklist

| Check item | Passing standard |
| --- | --- |
| The trio | All three in place, each filling a different role; every one has a clickable entry point |
| Write-ups | One page per work, with all four questions answered (what it is, how to play, what I did, what I used) |
| Showcase channels | Playable or understandable at first screen; no dead links; doesn't break when opened on a phone |
| Resume | One page; every experience follows "verb + method + result"; links resolve directly |
| Application ledger | 8–15 roles per batch; channel, date, status, and feedback all recorded |
| Test tasks | Delivered on time; build, source code, and one-page write-up all present |
| Interviews | Both the 3-minute and 15-minute retrospective versions; one story for each of the three behavioral types |
| Sustained presence | A public update within the last 8 weeks; searching your own name turns up a positive record |
| Review loop | A one-page gap list and next actions at the end of every round |

If the checklist is fully ticked and you still can't get interviews, the problem is most likely role matching or channels — go back to §3.2 and §3.4 and readjust, rather than piling on more works.

## 5. Common Pitfalls

1. **Tutorial re-creations only**: all three works are typed along with tutorials, and the moment you're asked "what did you decide yourself", it shows. Keep at least one work where you made every call from topic selection to release; the showpiece can be a re-creation variant, but you must be able to explain what you changed and why.
2. **Works with no write-up**: recruiters won't spend twenty minutes guessing at your project. Without a one-page write-up, a work effectively doesn't exist; write "how to play it, what I was responsible for" first, then patch in the technical details.
3. **Applying only to big studios**: the target pool is too narrow; processes are long and feedback is slow, so it's easy to stall out while waiting. Apply across all three tiers — stretch, match, safety — and get one cycle running first.
4. **Stopping when there's no feedback**: silence is the norm (long pipelines, cancelled roles, screening preferences); treat it as data, not a verdict; at the end of each batch, review three variables — works, resume, matching.
5. **A portfolio built purely on quantity**: ten half-finished works are worse than three you can talk through; a little knowledge of everything and nothing you can talk about for 15 minutes is the most common minus.
6. **A resume written as a job description**: "responsible for a module" carries no information; switch to verb, method, result — and to verifiable facts where you have no numbers.
7. **Turning the test task into a flashy big project**: going over time or delivering half-finished work is a negative score; do a small slice completely and write the trade-offs into the write-up.
8. **Works that don't match the role**: applying for server-side with nothing but small single-player projects, or for systems design with only art practice; build evidence line by line against the high-frequency words in the job description.
9. **Pretending to know in interviews**: a forced answer becomes an integrity problem the moment you're probed; handle it with the three steps — admit the boundary, offer adjacent experience, give an action plan.
10. **Letting your presence lapse**: you stop posting and disappear from communities during the job hunt, and a search shows your last update was six months ago; two hours a week maintaining your public signal is enough.

## Further Reading

- [Learning Paths](../../docs/start/learning-path.md): the upstream route for this document; this page is the follow-on for the "Job Hunting" route.
- [Roles & Skills Map](../../docs/start/role-map.md): pin down the role first, then decide how to configure the portfolio.
- [Indie Developer Profiles](../../docs/meta/people/indie/README.md): see how others entered the industry and made their transitions.
- [Open Source Picks & Book Recommendations](../../resources/books-and-repos.md): model repositories and further book lists.
- [Pitfalls & Anti-patterns](../../docs/pitfalls/README.md): pitfalls across the whole pipeline; check them off one by one before applying.
- [Multi-platform Launch Playbook](../platform-launch/README.md): when a work is going to be released publicly, use its checklist.
- [Indie Survival](../indie-survival/README.md): if you later turn to the indie route, read this one next.
