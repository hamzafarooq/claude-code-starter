If a topic was not provided, ask the user:
1. What topic or question they want to research
2. How many videos they want (default: 5)
3. Any preferences — e.g. recent only, beginner-friendly, a specific channel

Then:
1. Use Brave MCP to navigate to YouTube search — `mcp__brave-devtools__browser_navigate` — using the URL format: `https://www.youtube.com/results?search_query=TOPIC` (replace spaces with `+`)
2. Take a snapshot to read the search results — `mcp__brave-devtools__browser_snapshot`
3. If results look thin or off-topic, refine the query and try once more
4. Close the browser when done — `mcp__brave-devtools__browser_close`

Produce the following write-up directly — no preamble:

### YouTube Research: [Topic]
**Search query used:** [exact query]

---

| # | Title | Channel | Views | Published | Link |
|---|-------|---------|-------|-----------|------|
| 1 | ... | ... | ... | ... | [Watch](...) |
| 2 | ... | ... | ... | ... | [Watch](...) |

---

#### Top pick
**[Video title]** — One sentence on why this is the best starting point for a PM or non-technical person.

#### What the results tell you
2-3 sentences on the overall landscape: Is this topic well-covered? Are results mostly technical or beginner-friendly? Any dominant voices or channels worth following?

#### Suggested follow-up searches
2-3 alternative queries to go deeper on subtopics.

---

Rules:
- Use plain English throughout
- Do not fabricate view counts or dates — only report what you read from the page
- If YouTube blocks the search or returns no results, tell the user clearly and stop
- After the write-up, ask: "Want me to save this to docs/youtube-research.md?"

$ARGUMENTS
