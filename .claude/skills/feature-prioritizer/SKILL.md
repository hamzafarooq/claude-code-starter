---
name: feature-prioritizer
description: Score a feature list using RICE (Reach, Impact, Confidence, Effort) and return a ranked table with recommendation. Use when the user wants to prioritize features, decide what to build next, or cut scope.
---

Ask the user:
1. "Paste your list of features or initiatives."
2. "What's the timeframe — one quarter, one sprint, one year?"
3. "Any features that are already committed or non-negotiable? I'll mark them separately."

For each feature, estimate:
- **Reach** — how many users affected per period (1–10 scale or absolute number)
- **Impact** — how much does it move the needle per user (0.25 = minimal, 0.5 = low, 1 = medium, 2 = high, 3 = massive)
- **Confidence** — how sure are you about Reach and Impact? (percentage: 50%, 80%, 100%)
- **Effort** — person-months to build (use your best estimate; flag if unclear)

**RICE score = (Reach × Impact × Confidence) / Effort**

---

## Feature Prioritization — [Product / Quarter]

| Feature | Reach | Impact | Confidence | Effort | RICE Score | Priority |
|---------|-------|--------|------------|--------|------------|----------|
| [feature] | [#] | [#] | [%] | [months] | [score] | HIGH/MED/LOW |

### Recommended build order
Top 3 features with one-line rationale for each.

### Features to cut or defer
Which items scored low and why you should drop or delay them.

### What the scores can't tell you
Flag 1–2 strategic or political factors that aren't captured in RICE but matter for the decision.

---

State your assumptions clearly. Ask: "Want me to re-score with different estimates?"
