If a GitHub repo URL was not provided, ask the user for one now.

Then:
1. Use Brave MCP to navigate to the repo URL — `mcp__brave-devtools__browser_navigate`
2. Take a snapshot to read the page — `mcp__brave-devtools__browser_snapshot`
3. Navigate to the raw README if visible — look for README.md link and navigate to it
4. Explore key folders by navigating to subdirectories as needed (src/, app/, main files, config)
5. Close the browser when done — `mcp__brave-devtools__browser_close`

Produce the following write-up directly — no preamble:

### [Repo Name]
**URL:** [GitHub URL]
**Language(s):** [Primary languages used]

---

#### What it does
One paragraph. Plain English. What problem does this repo solve? Who would use it?

#### How it works (high level)
2-4 bullet points explaining the architecture or flow. No code. Focus on concepts.

#### Key files and folders
A short table:
| Path | What it does |
|------|-------------|
| ... | ... |

#### Who it's for
One sentence. Developer? PM? Data scientist? End user?

#### How to get started
Copy the "Quick Start" or "Installation" steps from the README verbatim, or summarize if there is none. Maximum 5 steps.

#### Interesting things to note
2-3 observations: unusual design choices, dependencies worth knowing about, anything a PM should flag.

---

Rules:
- Use plain English throughout — no code unless quoting directly from the repo
- If the README is missing or thin, say so and work from what you can find in the file structure
- If you cannot access the repo (private, 404, etc.), tell the user clearly and stop
- After the write-up, ask: "Want me to save this to docs/repo-summary.md?"

$ARGUMENTS
