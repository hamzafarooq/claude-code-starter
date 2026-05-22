---
name: youtube-deepdive
description: Takes one or more YouTube video URLs, visits each page using Brave MCP, extracts chapters/timestamps, key moments, and top comments, and produces a structured highlight report. Use when the user wants to find the best parts of a video without watching the whole thing.
---

## What this skill does

Given one or more YouTube video URLs, this skill visits each video page and extracts:
- Chapters and timestamps from the description
- Key moments (if YouTube shows them)
- The video description summary
- Notable comments that highlight key takeaways

It then produces a structured "highlight reel" report so the user can jump straight to the best parts.

---

## How to execute

For each video URL provided:

1. Navigate to the video URL — `mcp__brave-devtools__browser_navigate`
2. Take a snapshot — `mcp__brave-devtools__browser_snapshot`
3. Look for:
   - **Chapters/timestamps** in the description (lines starting with `0:00`, `1:23`, etc.)
   - **Key moments** panel YouTube sometimes renders on the page
   - **Description text** — first 3-5 sentences summarizing the content
   - **Top comments** — scroll or look for comment section in snapshot; extract 2-3 that mention specific tips or moments
4. If the description is collapsed, look for an "expand" or "more" button ref and click it — `mcp__brave-devtools__browser_click`
5. Repeat for each video
6. Close the browser when done — `mcp__brave-devtools__browser_close`

---

## Output format

Produce this write-up directly — no preamble:

### YouTube Deep Dive: [Video Title]
**Channel:** [channel name] | **URL:** [link] | **Duration:** [duration if visible]

#### What it's about
1-2 sentences from the description. Plain English.

#### Best parts to watch
| Timestamp | What happens | Why it matters |
|-----------|-------------|----------------|
| 0:00 | ... | ... |
| 2:15 | ... | ... |

*(If no timestamps are available, note that and summarize the key sections based on the description.)*

#### What viewers found valuable
2-3 highlights from top comments (quote briefly, note what they're reacting to).

#### Should you watch it?
One sentence verdict — who this is for and whether it's worth the full runtime.

---

*(Repeat the above block for each video.)*

---

## Rules

- Use plain English throughout — this is for PMs, not engineers
- Do not fabricate timestamps or quote comments you didn't read from the page
- If the video page is unavailable (private, deleted, region-blocked), say so and skip it
- If no chapters exist, do your best to infer structure from the description text
- After the write-up, ask: "Want me to save this to docs/youtube-deepdive.md?"
