---
name: verify-work
description: End-of-session code review — checks for unused imports, console.logs, missing error handling, hardcoded values, and edge cases before committing. Use when the user is done coding and wants a final pass before committing or shipping.
---

Review all recently modified files in the current session. Check for:

## Verify Work — Pre-Commit Review

### Cleanliness
- [ ] No `console.log`, `print`, or debug statements left in
- [ ] No commented-out code blocks
- [ ] No TODO comments that belong in the backlog, not the file
- [ ] No unused imports or variables

### Correctness
- [ ] Every function that can fail has error handling
- [ ] No hardcoded API keys, URLs, or credentials
- [ ] Environment variables are used for config values
- [ ] No hardcoded user IDs, test emails, or magic numbers without a constant name

### Edge cases
For each modified function, check:
- What happens if the input is null, empty, or the wrong type?
- What happens if an API call fails or times out?
- What happens on first run with no existing data?

### Security
- [ ] No user input is passed directly to a shell command, SQL query, or file path
- [ ] No sensitive data logged to console or written to files

---

**Report format:**

For each issue found:
> **File:** `path/to/file.ts` line [N]
> **Issue:** [what's wrong]
> **Fix:** [specific change to make]

If nothing is found: "All clear — no issues found in the reviewed files."

---

Fix issues directly if asked. Otherwise report only, don't change files.
