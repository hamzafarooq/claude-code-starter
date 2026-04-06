---
name: prd-generator
description: Generates a structured PRD from a feature description or brief. Use when asked to write, draft, or create a PRD.
---

## What this skill does

When triggered, ask the user for:
1. Feature name (one line)
2. Problem being solved (1-3 sentences)
3. Target user(s)
4. Any known constraints or context (timeline, technical limits, compliance, etc.)

Then generate a full PRD using the structure below.

---

## PRD Structure

### 1. Problem Statement
What pain are we solving and for whom? Why does this matter now?

### 2. Goals
3-5 measurable outcomes we want to achieve with this feature.
Format: "Increase [metric] by [amount] within [timeframe]"

### 3. Non-Goals
What this feature explicitly will NOT do. Be specific.
This section prevents scope creep.

### 4. Users & Use Cases
Who uses this feature and in what context?
Include 2-3 concrete scenarios (short narrative, not bullets).

### 5. User Stories
Written as: "As a [user type], I want to [action] so that [outcome]."
Group into: Must-have / Should-have / Nice-to-have

### 6. Acceptance Criteria
Written in Given/When/Then format for each must-have story.
Should be specific enough that a QA engineer can write a test.

### 7. Risks & Assumptions
Two columns:
- **Risks** — What could go wrong? What dependencies exist?
- **Assumptions** — What are we treating as true that we haven't confirmed?

### 8. Open Questions
What must be decided before engineering starts?
Format as questions, not statements. Assign an owner if known.

### 9. Success Metrics
How will we measure whether this feature succeeded?
Include leading indicators (early signals) and lagging indicators (final outcomes).

---

## How to respond

- Write the full PRD directly — do not explain what you're about to write
- Use plain English — avoid technical jargon
- Mark any section where you made an assumption with `[ASSUMPTION]`
- Mark anything that needs the PM's input with `[NEEDS INPUT]`
- End with: "Review the [ASSUMPTION] and [NEEDS INPUT] sections before sharing with engineering."
- Ask the user if they want to save it to `docs/prd.md`
