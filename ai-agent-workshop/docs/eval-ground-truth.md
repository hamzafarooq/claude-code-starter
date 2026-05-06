# Ground truth: `competitor-research` skill

10 test cases for evaluating the `competitor-research` skill. Each row follows the
workshop's three-column structure: **Input · Golden Output · Pass Criteria**.

> **The rule:** *If you can't write the Golden Output column, you don't know what
> the AI is supposed to do. Defining ground truth IS the spec.*

## Three ground truth types in this dataset

| Type | What it tests | Cases |
| --- | --- | --- |
| **Exact match** — deterministic | Format, structure, refusal behavior, scoping protocol. Golden Output is specific text or a boolean (skill triggered / didn't). | 1–5 |
| **Rubric** — scored against criteria | Research quality. Golden Output describes *required properties*; pass is judged on dimensions like source recency, anti-fabrication, gap falsifiability. | 6–10 |
| **Comparative** — human preference | Not used in this initial set. Add later when you have two skill versions to compare. | — |

## Honest caveat

The workshop says *"start with 10 real examples from actual use — not synthetic
ones you invented."* These 10 cases are **scenario-based**, not yet drawn from
real production runs. As real usage accumulates, replace them with logged
inputs that surfaced actual failure modes. Synthetic evals catch the failure
modes you anticipated; real evals catch the ones you didn't.

---

## Test cases

| # | Type | Input | Golden Output | Pass Criteria |
| --- | --- | --- | --- | --- |
| 1 | Exact | *"Run competitor research on Notion for solo creators"* | One-line scope confirmation; then 3–5 competitor cards (exactly 6 bullets each); then Gap Analysis section with 3 bullets; closing question is the final line. | All sections present in order. Every card has exactly 6 bullets. Closing question is verbatim *"Based on this, which gap are you trying to own?"* and is the last line. |
| 2 | Exact | *"Run competitor research on Stripe"* | Asks one scoping question: *"What product or feature are you researching? Who is it for?"* (or close paraphrase). No research output yet. | Exactly one scoping question asked. No competitor cards generated. No fabricated competitor list. |
| 3 | Exact | *"Do some competitor research"* | Same scoping question as #2. Does not proceed. | Scoping question asked. No research performed. No fabricated product or audience inferred. |
| 4 | Exact | *"Should I switch from Slack to Teams?"* | Skill does **not** trigger. Claude responds normally that this is a personal switching decision, not a competitive landscape. | `/competitor-research` not invoked. No 6-bullet cards produced. |
| 5 | Exact | *"Compare Postgres vs MySQL"* | Skill does **not** trigger. Head-to-head comparison is a different job. | `/competitor-research` not invoked. |
| 6 | Rubric | *"Research voice dictation apps for Mac"* | 3–5 cards covering current top players. All sources observed within last 12 months. Every non-trivial claim cites ≥2 independent sources. | **Source recency**: ≥80% of sources ≤12 months old. **Cross-referencing**: every pricing tier and differentiator has ≥2 source URLs. **Format**: 6-bullet cap honored. |
| 7 | Rubric | *"Research alternatives to Salesforce CRM"* | 3–5 cards; competitors with gated enterprise tiers explicitly write *"Contact sales"*. No invented enterprise prices. | **Anti-fabrication**: zero invented $ figures for hidden tiers. **Honesty**: *"Contact sales"* or *"Not public"* appears where appropriate. |
| 8 | Rubric | *"Where's the gap in AI note-taking apps?"* | 3–5 cards followed by Gap Analysis with 3 bullets. Each gap is **falsifiable** — a specific, verifiable claim. | Exactly 3 gap bullets. Each is testable (e.g., *"no per-seat tier under $10/mo"*). Vague gaps like *"better UX"* or *"more polished"* are failures. |
| 9 | Rubric | *"Research alternatives to Linear for engineering teams"* | Weakness bullets carry `(N+ sources)` or `(N reviews on M platforms)` qualifiers, proving review-miner subagent ran. | Each weakness has a confirming-voice count. Patterns drawn from ≥2 platforms (e.g., Reddit + HN; not just one G2 thread). Single-source complaints absent. |
| 10 | Rubric | *"Research alternatives to Postgres"* | Open-source / self-hosted pricing model handled correctly. Cards don't force a $/mo number where none exists. | Pricing field accepts non-monetary models (*"Free, open-source (BSD)"*, *"Self-hosted free / Cloud from $X"*). Sources include GitHub repos or official docs. |

---

## How to run this eval

1. **Capture outputs.** Run the `competitor-research` skill on each input above.
   Save each output verbatim to `runs/<date>/case-NN-<slug>.md`.
2. **Score.** Invoke the `skill-evaluator` skill, pointing it at this file and
   the captured outputs. It returns a per-case 0/1/2 score and an aggregate
   confidence rating.
3. **Iterate.** Use the evaluator's *"Fix to make"* output to update
   [SKILL.md](../.claude/skills/competitor-research/SKILL.md). Re-run the eval.
   Don't ship until confidence ≥ 9/10 *and* zero exact-match failures.

## Failure-mode patterns to watch for

When multiple test cases fail together, it usually points at a single root cause.
Common patterns for this skill:

| If these fail together... | Likely root cause |
| --- | --- |
| Cases 1 + 8 (format violations + missing closing question) | Skill not enforcing the hard caps; loosen ≠ improve |
| Cases 2 + 3 (scoping question skipped) | Skill jumping to research without scoping — Step 1 of SKILL.md being ignored |
| Cases 4 + 5 (skill triggers when it shouldn't) | Skill description too broad; trigger phrases over-matching |
| Cases 6 + 9 (no `(N+ sources)` qualifiers) | Subagent delegation step skipped; orchestrator doing review work inline |
| Case 7 alone (invented enterprise pricing) | Anti-fabrication rule not loaded into context — likely SKILL.md too long, getting truncated |
