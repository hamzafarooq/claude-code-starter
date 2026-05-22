---
name: youtube-researcher
description: Uses Brave MCP to search YouTube and find relevant videos on a topic. Use when asked to find, research, or recommend YouTube videos about a subject.
---

## What this skill does

When triggered, ask the user:
1. What topic or question they want to research
2. How many videos they want (default: 5)
3. Any preferences — e.g. recent only, beginner-friendly, a specific channel

Then use Brave MCP to navigate YouTube, search for the topic, and return a structured list of relevant videos.

---

## How to execute

1. Navigate to `https://www.youtube.com/results?search_query=TOPIC` — replace TOPIC with the user's input (URL-encode spaces as `+`)
2. Take a snapshot to read the search results page
3. Collect the top results — for each video note: title, channel name, view count, publish date, and URL
4. If results look off-topic or thin, refine the search and try once more
5. Close the browser when done

---

## Output format

Produce this write-up directly — no preamble:

### YouTube Research: [Topic]
**Search query used:** [exact query]

---

| # | Title | Channel | Views | Published | Link |
|---|-------|---------|-------|-----------|------|
| 1 | ... | ... | ... | ... | [Watch](...) |
| 2 | ... | ... | ... | ... | [Watch](...) |
| ... | | | | | |

---

#### Top pick
**[Video title]** — One sentence on why this is the best starting point for a PM or non-technical person.

#### What the results tell you
2-3 sentences on the overall landscape: Is this topic well-covered? Are results mostly technical or beginner-friendly? Any dominant voices or channels worth following?

#### Suggested follow-up searches
2-3 alternative queries to go deeper on subtopics.

---

## Rules

- Use plain English throughout
- If YouTube blocks the search or results are empty, tell the user and suggest they try the query manually
- Do not fabricate view counts or dates — only report what you read from the page
- After the write-up, ask: "Want me to save this to docs/youtube-research.md?"
