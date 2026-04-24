---
name: boris-plan
description: Run Boris Cherny's plan-first workflow — write a complete plan, get explicit approval, then execute. Use at the start of any complex task to avoid wasted work and mid-session corrections. Named after Boris Cherny, creator of Claude Code.
---

This skill enforces the workflow Boris Cherny (creator of Claude Code) uses for every complex task: plan first, execute second, verify last. Credit: [Boris Cherny](https://github.com/bcherny) via [howborisusesclaudecode.com](https://howborisusesclaudecode.com/).

Ask the user: "Describe the task you want to accomplish."

Then produce a plan — do NOT write any code or make any changes yet:

---

## Plan: [Task Name]

### What I understand you want
One sentence restatement of the goal. Flag any ambiguity here before proceeding.

### Assumptions I'm making
List every assumption. If any are wrong, this is the time to correct them.

### What I will do (step by step)
Numbered list. Each step is specific enough that you can verify it happened.

1. [Step 1 — what file/thing will change and how]
2. [Step 2]
3. [Step 3]
...

### What I will NOT do
Explicitly name things that are out of scope — adjacent improvements, refactors, style changes — that you might expect but aren't in this plan.

### How we'll verify it worked
Specific check: a command to run, a behavior to observe, a test that should pass.

### Estimated scope
[Small: <30 min | Medium: 30–90 min | Large: >90 min] — and why

---

**Waiting for your approval before writing a single line.**

Reply "approved", suggest changes, or ask questions. Only after approval will execution begin.
