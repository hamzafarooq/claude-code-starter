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

## Wall of Love (built 2026-05-31)

Scrapes all Maven reviews for maven.com/boring-bot and renders a filterable HTML page.

### Files
| File | Purpose |
|------|---------|
| `scrape_reviews.py` | Hits Maven's public API (`api.maven.com/courses/{id}/reviews`) — no browser needed. Saves `reviews.json`. |
| `build_wall.py` | Reads `reviews.json`, generates `wall-of-love.html` with all reviews embedded. |
| `reviews.json` | 239 scraped reviews (gitignore candidate — regenerate with scraper). |
| `wall-of-love.html` | Self-contained wall of love page. White theme, Inter font, course filter tabs, real profile photos. |

### Course IDs (Maven API)
| Course | ID | Reviews |
|--------|-----|---------|
| Claude Code in Practice | 19374 | 34 |
| Agentic AI for Product Managers | 3847 | 110 |
| Agent Engineering Bootcamp | 10144 | 82 |
| Workshop | 11426 | 13 |

### Usage
```bash
# Full refresh — scrape all reviews then rebuild page
python3 build_wall.py --run-scraper

# Rebuild from existing reviews.json (faster)
python3 build_wall.py
```

### How it works
- Maven's review API is public (no auth): `GET https://api.maven.com/courses/{id}/reviews?page=N&limit=50`
- Response includes `metadata.total`, `metadata.pages` for pagination
- Reviews with null `preferred_name` are filtered out (~46 anonymous reviews)
- Profile photos come from `user.attrs.bio.profile_image_url`, proxied through Maven's Next.js image endpoint

### Next steps
- [ ] Add `reviews.json` to `.gitignore` (large, regeneratable)
- [ ] Embed wall-of-love in course landing page or Substack
- [ ] Run scraper periodically to pick up new cohort reviews

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
