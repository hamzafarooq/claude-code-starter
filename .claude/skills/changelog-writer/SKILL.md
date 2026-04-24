---
name: changelog-writer
description: Read the git log and write a user-facing changelog entry in Keep a Changelog format. Use when the user wants to document what changed in a release, write release notes, or update their CHANGELOG.md.
---

Run `git log --oneline` to get the recent commits. Ask the user: "What version number is this release, and what date?"

Then produce a changelog entry:

## [Version] — [Date]

### Added
New features visible to users. One bullet per feature. Start each bullet with a verb (e.g. "Added ability to…", "New export option for…").

### Changed
Behavior that changed for existing users. Flag anything that changes how something works, even if it's an improvement.

### Fixed
Bugs that were resolved. Be specific — "Fixed crash when uploading files larger than 10MB" not "Fixed bugs."

### Removed
Features or settings that are gone. If something was deprecated, this is where it moves to.

### Security
Security fixes always get their own section, even if minor.

---

**Rules:**
- Write for users, not engineers — no commit hashes, branch names, or internal ticket IDs
- If a commit message is too technical to translate, ask what the user-facing impact was
- One bullet per change — don't merge multiple changes into one line
- Present tense: "Adds…" or past tense: "Added…" — pick one and be consistent

Append the entry to `CHANGELOG.md` if it exists. Create it if it doesn't.
