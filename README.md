# MATACS-TH-2026-02: AI Proposal Triage Design

- **Name:** [Mansoor Hussain]
- **Reference:** MATACS-TH-2026-02
- **Time actually spent:** [1 hr 20 min]

## Files
- [WRITEUP.md](WRITEUP.md): answers to the five questions
- [diagram/flow.png](diagram/flow.png): process flow from upload to ranked output
- [PROMPTS.md](PROMPTS.md): the extraction prompt
- [ranking.json](ranking.json): my expected ranking of A to E
- [prototype/score.py](prototype/score.py): optional, a small script that checks my scoring maths (no API, no keys)

## How I used AI
I used Claude to help me spot the problems in the sample proposals and to draft the write-up, prompt, diagram and scoring script. I compared two AI drafts and kept the parts I agreed with.

I corrected one thing: both drafts scored price and timeline against the best bidder, so adding or removing one bid would change everyone else's score. I changed it to fixed targets (the $260,000 budget ceiling and the 16-week limit), so scores stay the same and are easier to explain.

I also corrected the team score. One draft gave credit for "team and approach" too loosely and missed that C has no safety or monitoring plan and D has no crew or monitoring plan. I changed it to a four-item checklist (named lead, crew, safety plan, monitoring plan), so missing items lose points.

I also disagreed with one draft that gave proposal D a missing timeline a score of 0, because that invents a number the bidder never gave. I left that proposal unscored and flagged it instead.
