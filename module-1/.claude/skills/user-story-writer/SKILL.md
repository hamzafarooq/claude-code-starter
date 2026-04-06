---
name: user-story-writer
description: Converts feature ideas or rough bullets into user stories with acceptance criteria. Use when asked to write user stories or break down a feature.
---

## What this skill does

Take a feature description — it can be rough, even a single bullet point — and produce:

1. **Primary user story** — the one main story that captures the core value
2. **Supporting user stories** — 2-4 sub-stories for the key flows
3. **Acceptance criteria** for each story in Given/When/Then format
4. **Edge cases to consider** — 3-5 scenarios the team should discuss before building
5. **Open questions** — what needs to be answered before sprint planning

---

## Story format

Use this exact format for each story:

```
**Story [N]:** As a [user type], I want to [do something] so that [I get this value].

**Acceptance Criteria:**
- Given [starting context], when [user takes this action], then [this result happens]
- Given [starting context], when [user takes this action], then [this result happens]
- Given [starting context], when [user takes this action], then [this result happens]

**Priority:** Must-have / Should-have / Nice-to-have
**Effort:** Small (< 1 day) / Medium (2-3 days) / Large (1 week+)
```

---

## Edge cases section

After the stories, add:

```
## Edge Cases to Discuss
- [Scenario 1: e.g. "What happens if the user has no data yet?"]
- [Scenario 2: e.g. "What if the export fails mid-way?"]
- [Scenario 3: e.g. "How does this behave on mobile?"]
```

---

## Open questions section

End with:

```
## Questions for the Team
1. [Question about scope, ownership, or a missing decision]
2. [Question about a dependency or integration]
3. [Question about edge cases that need a product decision]
```

---

## How to respond

- Write the stories directly without preamble or explanation
- Keep language simple enough for a non-technical stakeholder to read
- Mark stories with unclear scope as `[NEEDS CLARIFICATION]`
- If the feature seems too large for one sprint, say so and suggest how to split it
- After delivering the stories, ask: "Want me to add these to docs/prd.md?"
