# Course Memory

Running log of decisions, module status, and context that isn't obvious from the code.
Update this file after major changes or decisions.

---

## Repo decisions

| Decision | Reason | Date |
|----------|--------|------|
| `course-modules/` is gitignored | Contains slide decks and raw HTML exports — too large and not useful to students | 2026-04-05 |
| `module-1/CLAUDE.md` renamed to `CLAUDE-template.md` | Prevents confusion — students should create their own CLAUDE.md, not use the repo's | 2026-04-05 |
| Root `CLAUDE.md` is for instructor use | Gives Claude context when Hamza is working on course content from the root folder | 2026-04-05 |
| Version tags follow `vN.0` per module | Easy to restore course state after each module; visible in GitHub under Tags | 2026-04-05 |

---

## Module status

| Module | Status | Git tag | Notes |
|--------|--------|---------|-------|
| Module 1 | Complete | `v1.0` | Assignments 1a, 1b, 1c. Skills: prd-generator, user-story-writer |
| Module 2 | In progress | — | Assignments 2a (explain-me-a-repo skill), 2b (Brave MCP setup), 2c (apply to lennys-podcast-transcripts repo). Demo: frontend/backend/AI backend |

---

## Skills inventory

| Skill | Trigger | Location | Status |
|-------|---------|----------|--------|
| prd-generator | `/prd-generator` | `module-1/.claude/skills/prd-generator/SKILL.md` | Live |
| user-story-writer | `/user-story-writer` | `module-1/.claude/skills/user-story-writer/SKILL.md` | Live |
| explain-me-a-repo | `/explain-me-a-repo` | `module-2/.claude/skills/explain-me-a-repo/SKILL.md` | Live — requires Brave MCP for live browsing |

---

## Apps built in class

| App | Repo | Built in |
|-----|------|---------|
| word-humanizer | https://github.com/hamzafarooq/word-humanizer/ | Module 1 |
| seo-writer | https://github.com/hamzafarooq/seo-writer | Module 1 |

---

## Open items

- [x] Add Module 2 folder and materials
- [ ] Review Module 2 against the deck and refine after next cohort session
- [ ] Update version tag to `v2.0` when Module 2 is complete
- [ ] Consider adding a `docs/` folder at root for cross-module reference material

---

## How to update this file

After any of the following, add a row or update the relevant section:
- A module is completed or tagged
- A new skill is added or changed
- A repo-level decision is made
- An app is built in class
