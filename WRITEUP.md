# Write-up

## How I think about it
I applied the simple simple: **AI reads, code decides, a person approves.**

## 1. AI vs. rules
**AI:** reading each proposal and pull out the facts (price, weeks, installs, warranty years,
who holds the licence), and finding strange text, like a line that tells the tool what to do.

**Plain code:**  pass/fail checks, scoring maths, ranking, saving results.

I drew the line here because reading needs language skills, but a score should be a formula the
admin can see and change. If AI also did the scoring, a reviewer couldn't explain or justify it.

## 2. Consistency and explainability
- AI runs once per proposal at temperature 0 with a fixed model and prompt version. The facts are
  saved. Ranking again reads the saved facts, so **the same proposals give the same ranking**.
- The maths is a formula, so it never varies.
- Each fact comes with a quote from the proposal. The reviewer sees a table: criterion, fact found,
  quote, points. Code checks that each quote really exists in the text.
- Scores use **fixed targets** (the budget ceiling and the 16-week limit), not "best bidder". That
  way one bid being added or removed doesn't change everyone else's score.

My scoring for the sample and the admin could change them

| Criterion | How points are given |
|---|---|
| Experience (30) | installs ÷ 12, capped at 12 |
| Price (25) | full marks at 80% of budget, zero at the ceiling, straight line between |
| Timeline (15) | full marks at 8 weeks, zero at 16, straight line between |
| Warranty (15) | half for panel years (out of 25), half for workmanship years (out of 12) |
| Team (15) | 3.75 each for named lead, crew, safety plan, monitoring plan |

Results: A 77, E 64, C 55 (flagged), D (flagged, not scored), B (ineligible).

## 3. Human in the loop
A person:
- confirms or corrects the extracted facts (shown with quotes),
- resolves every flagged proposal (asks the bidder, accepts, or excludes),
- can override any value or rank, but must give a reason,
- makes the final award. The tool only sorts and explains.

An also logged criteria version, every score,
every flag, every override (who, when, why), and the final decision.

## 4. Changing criteria
When the admin changes the criteria, I save it as a new version.
Old scores keep the version they were made with. Then the tool works out the scores again from the facts I already saved. 
It doesn't need the AI again, so it is quick and cheap. 
The reviewer sees the old and new ranking side by side. 
If the new criterion needs a fact I never pulled out, I ask the AI again for that one fact only.
Must-have (pass/fail) rules work the same way.
## 5. Risks

| Risk | What I do |
|---|---|
| Wrong extraction | Quote for every fact, quote check by code, reviewer confirms, low-confidence goes to flagged |
| Made-up facts | "Return null if not stated". Missing data is flagged, never filled in or scored as zero |
| Manipulation (like C's hidden line) | Proposal text is treated as data, not instructions. AI only returns facts, so even if fooled it can't set a score or rank. A suspicious line flags the proposal. I scored C on its real content only |
| Bias | Scoring uses only the criteria. Company names don't affect the points |
| Wrong eligibility (like B) | Pass/fail is code. A cheap price can never rescue a failed mandatory rule |
| Cost | AI runs once per proposal, results are cached, re-scoring is free, page limit per upload |
| Privacy | Only fictional data in this exercise. In real use, keep documents in approved storage |

## What I did with each sample
- **B:** ineligible. Cheapest and fastest, but the bidder doesn't hold the licence.
- **C:** flagged. I ignored the hidden instruction, and a person must look at it. Its "since 2020"
  may include installs older than 5 years. I could have ranked it third with a warning. I chose
  to leave it unranked because an attempt to manipulate the tool deserves a human decision first.
- **D:** flagged, not scored. No completion time, so I can't check the 16-week limit. I did not
  give it a zero, because that would invent a number. This matters: D has the lowest price among
  eligible bids, and my check shows that a short schedule could put D above A. So the question
  to the bidder could change the winner.
- **A and E:** ranked 1 and 2. A is provisional until D is answered.

## Assumptions
- "Named project lead" counts if the proposal names a role clearly, even without a person's name. A reviewer should check this.
- I did not hard-code any numbers. The 12 installs, 80% and 8 weeks above are admin settings.
