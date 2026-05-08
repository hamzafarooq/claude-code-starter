If one or more YouTube video URLs were not provided, ask the user:
1. Which YouTube video(s) they want to deep dive (paste the URL(s))
2. Whether they want to focus on a specific aspect (e.g. "just the tips", "only the first half")

Then for each video URL:
1. Use Brave MCP to navigate to the video page — `mcp__brave-devtools__browser_navigate`
2. Take a snapshot to read the page — `mcp__brave-devtools__browser_snapshot`
3. Look for chapters/timestamps in the description (lines like `0:00 Intro`, `3:45 Key concept`)
4. If the description is collapsed, click the expand button to reveal it
5. Extract top comments that mention specific tips, moments, or timestamps
6. Repeat for each video, then close the browser — `mcp__brave-devtools__browser_close`

Produce the following write-up directly — no preamble:

### YouTube Deep Dive: [Video Title]
**Channel:** [channel name] | **URL:** [link] | **Duration:** [duration if visible]

#### What it's about
1-2 sentences from the description. Plain English.

#### Best parts to watch
| Timestamp | What happens | Why it matters |
|-----------|-------------|----------------|
| 0:00 | ... | ... |
| 2:15 | ... | ... |

*(If no timestamps are found, summarize key sections based on the description.)*

#### What viewers found valuable
2-3 highlights from top comments — brief quotes, noting what they're reacting to.

#### Should you watch it?
One sentence verdict — who this is for and whether it's worth the full runtime.

---

*(Repeat the block above for each video provided.)*

---

Rules:
- Use plain English throughout — written for PMs, not engineers
- Do not fabricate timestamps or comments — only report what you read from the page
- If a video is private, deleted, or inaccessible, say so clearly and skip it
- If no chapters exist, infer structure from the description text
- After the write-up, ask: "Want me to save this to docs/youtube-deepdive.md?"

$ARGUMENTS
