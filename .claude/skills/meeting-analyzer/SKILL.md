---
name: meeting-analyzer
description: Extract action items, decisions, risks, and open questions from raw meeting notes or transcripts. Use when the user pastes meeting notes or asks what came out of a meeting.
---

Ask the user to paste their meeting notes or transcript.

Then return:

## Meeting Analysis

**Meeting type:** [standup / planning / design review / 1:1 / exec review / other]
**Date:** [if mentioned]
**Attendees:** [if mentioned]

---

### Decisions Made
Bullet list of things that were agreed or resolved. Flag HIGH CONFIDENCE vs TENTATIVE.

### Action Items
| Owner | Task | Due date |
|-------|------|----------|
| [name or "unassigned"] | [specific action] | [date or "not set"] |

### Open Questions
Things raised but not resolved. These need a follow-up owner.

### Risks & Blockers
Anything that could slow progress. One sentence each.

### What Was Left Unsaid
One observation about what the notes suggest but no one said directly — a tension, an assumption, or a decision that needs to be made but wasn't.

---

Keep the action items actionable: verb + object + owner. If the notes are vague, flag it rather than fabricate specificity.
