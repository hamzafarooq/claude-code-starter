---
name: sprint-planner
description: Turn a list of user stories or backlog items into a prioritized 2-week sprint plan with effort estimates and capacity check. Use when the user wants to plan a sprint, prioritize stories, or figure out what fits in two weeks.
---

Ask the user:
1. "Paste your list of user stories or backlog items."
2. "How many engineers are on the team, and are there any constraints this sprint (holidays, on-call, etc.)?"
3. "What's the sprint goal — what does 'done' look like in 2 weeks?"

Then produce:

## Sprint Plan — [Sprint Name or Number]

**Sprint goal:** [one sentence]
**Capacity:** [N engineers × 10 days = N story points / days available]

---

### Must Do (Sprint Committed)
| Story | Effort (S/M/L) | Owner hint | Notes |
|-------|---------------|------------|-------|
| [story] | [S=0.5d, M=1-2d, L=3-5d] | [FE/BE/Full] | [dependency or risk] |

**Committed total:** [X days] of [Y available]

### Should Do (if capacity allows)
Stories that are next in priority but can slip to next sprint without breaking the goal.

### Out of scope this sprint
Stories deliberately deferred — with one-line reason for each.

---

**Risks:**
- [dependency on another team, unclear requirement, etc.]

**Suggested check-ins:** [mid-sprint review suggestion]

---

Flag any story that is too vague to estimate — ask for clarification before committing it.
