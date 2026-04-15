# Module 2: How the web works — and how to read code you didn't write

Course: [Claude Code in Practice](https://maven.com/boring-bot/claude-code-in-practice)
Instructor: Hamza Farooq, Traversaal.ai

---

## What you'll learn

- What frontend, backend, and AI backend actually mean (with a live demo)
- How to build your own Claude skill from scratch
- How to connect Claude Code to the web using Playwright MCP
- How to understand any GitHub repo without reading every line of code

By the end of this module, you'll be able to hand Claude a GitHub link and get a full briefing on what it does.

---

## Before you start

Make sure Claude Code is installed and you've completed Module 1. If not, follow the [setup guide](../README.md#installation) first.

---

## The demo: Frontend · Backend · AI Backend

Before the assignments, open the demo in your browser to see the three layers in action.

```
module-2/demo/index.html
```

Open it by double-clicking the file, or drag it into your browser. Enter your API key in the top right and ask it a question.

**What you'll see:**

- **Frontend (Layer 1):** The form you type into. HTML, CSS, and JavaScript running in your browser.
- **Backend (Layer 2):** A simulated server log showing what happens when your request is received — validation, formatting, routing.
- **AI Backend (Layer 3):** A real call to Claude's API. The response comes back through the backend and renders in the frontend.

This is the same architecture behind every AI product you've used.

---

## Assignment 2a: Build your first custom skill

Skills are just text files Claude reads when you type `/skill-name`. In Module 1 you used skills someone else wrote. Now you'll build one yourself.

The skill: **`/explain-me-a-repo`** — paste a GitHub URL and Claude gives you a full write-up of what the repo does, how it works, and how to get started.

### Step 1: Copy the skill into your project

The command file is already in this folder at:

```
module-2/.claude/commands/explain-me-a-repo.md
```

> **Important:** Claude only loads `.claude/` from the folder it's launched in. Copy the entire `module-2/.claude/` folder into your project root, or launch Claude from inside `module-2/` directly.

### Step 2: Read the command file

Open [.claude/commands/explain-me-a-repo.md](.claude/commands/explain-me-a-repo.md) and read it. Notice:

- The filename is what you type after `/` (e.g. `explain-me-a-repo.md` → `/explain-me-a-repo`)
- The body is the instruction set Claude follows when you invoke it
- `$ARGUMENTS` at the bottom captures anything you type after the command name

### Step 3: Test it (without MCP first)

Run Claude from the `module-2/` folder and type:

```
/explain-me-a-repo
```

Give it this URL: `https://github.com/hamzafarooq/lennys-podcast-transcripts`

Claude will do its best using its training knowledge. In Assignment 2b you'll give it a real browser so it can actually visit the URL.

### Step 4: Customize it

Edit the SKILL.md to change the output format. For example:

- Add a "Red flags" section for things that would concern a PM
- Change the format to match your team's documentation style
- Make it shorter or more technical

---

## Assignment 2b: Set up Playwright MCP

MCP (Model Context Protocol) lets Claude use external tools — including a real browser. Once you set up Playwright MCP, Claude can navigate to URLs, read pages, and browse repos live.

### Step 1: Install the Playwright MCP server

Open your terminal and run:

```bash
npm install -g @playwright/mcp
```

### Step 2: Add MCP to Claude Code settings

Open (or create) your Claude Code settings file:

```
~/.claude/settings.json
```

Add the following (merge with any existing content):

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp"]
    }
  }
}
```

### Step 3: Restart Claude Code and verify

Stop Claude Code (`Ctrl+C`) and restart it:

```bash
claude
```

Type this to confirm MCP is connected:

```
List the MCP tools available to you.
```

You should see Playwright browser tools listed (browser_navigate, browser_snapshot, etc.).

---

## Live demo: Watch Playwright MCP run autonomously

This is the part to show in class. Once MCP is connected, Claude controls a real browser — no clicking required from you.

**What "autonomous" means here:** Claude decides on its own which pages to visit, when to take a snapshot, when to go deeper, and when it has enough information to answer. You give it one instruction; it drives.

### Try it yourself

Paste this prompt into Claude:

```
Navigate to https://github.com/hamzafarooq/lennys-podcast-transcripts,
explore the repo structure, open the episodes/ folder to see how transcripts
are organized, then tell me: how many episodes are there, what metadata is
stored per episode, and what topics are covered in the index?
```

**What you'll see Claude do automatically:**

1. Open the repo homepage in Brave
2. Take a snapshot to read the page layout and README
3. Navigate into `episodes/` to inspect the folder structure
4. Navigate into `index/` to read the topic files
5. Synthesize everything into a direct answer — without you doing anything

### Why this matters for PMs

Before MCP, Claude could only answer based on what it was trained on. With Playwright MCP, Claude can read live pages, follow links, and explore file trees — the same way you would, but faster. This is what makes `/explain-me-a-repo` work on repos Claude has never seen before.

### Try a second prompt to push it further

```
Now navigate to the index/product-management.md file in that repo and
summarize the top 5 most referenced product management topics across episodes.
```

Claude will navigate directly to that file path on GitHub and read the raw content.

### Another example: researching YouTube videos

Playwright MCP isn't limited to GitHub. Claude can navigate any public website — including YouTube. The `/youtube-researcher` skill (included in this module) uses Playwright to search YouTube and return a structured list of relevant videos on any topic.

Try it:

```
/youtube-researcher
```

When prompted, enter a topic like `"product-led growth"` or `"how to run a discovery sprint"`. Claude will navigate to YouTube, read the search results, and return a ranked list with titles, channels, view counts, and links — without you opening a browser tab.

The skill file is at:

```
module-2/.claude/skills/youtube-researcher/SKILL.md
```

Read it to see how it works, then customize the output format for your own use case.

---

## Assignment 2c: Use /explain-me-a-repo on a real repo

Now that Brave MCP is connected, Claude can actually browse GitHub instead of guessing.

Run:

```
/explain-me-a-repo
```

Give it this URL:

```
https://github.com/hamzafarooq/lennys-podcast-transcripts
```

Claude will:

1. Navigate to the repo in a browser
2. Read the README and browse the file structure
3. Return a structured write-up

When it's done, ask:

```
Save this to docs/repo-summary.md
```

Then ask:

```
Based on this repo, what would the product requirements be if we wanted to turn this into a web app?
```

### What to share

Post in the course Slack:

1. Your `docs/repo-summary.md`
2. One thing that surprised you about the repo

---

## Bonus: Clone and run the repo

If you want to go further, clone the repo and try running it locally.

```bash
git clone https://github.com/hamzafarooq/lennys-podcast-transcripts.git
cd lennys-podcast-transcripts
```

Then ask Claude:

```
I just cloned this repo. Read the files and tell me how to run it. Walk me through it step by step.
```

Claude will read the actual files and give you specific instructions for your machine.

---

## Prompts worth saving

| What you want                      | What to type                                                            |
| ---------------------------------- | ----------------------------------------------------------------------- |
| Explain a GitHub repo              | `/explain-me-a-repo`                                                    |
| Research YouTube videos on a topic | `/youtube-researcher`                                                   |
| Understand a file                  | `"Read [filename] and explain what it does in plain English"`           |
| Find where something happens       | `"Where in this codebase does [X] happen?"`                             |
| Prep questions for an engineer     | `"What would an engineer need to know before building on top of this?"` |
| Turn repo into a PRD               | `"Based on this repo, write a PRD for a web version"`                   |

---

## Troubleshooting

**Skill or command not triggering**
Skills and commands only work if the `.claude/` folder is in the **root directory where you launch Claude** — not a parent or sibling folder. If you're running Claude from your own project, copy the entire `module-2/.claude/` folder into that project's root. If you're running Claude from inside `module-2/`, you're already in the right place.

**Playwright MCP not connecting**
Restart Claude Code and check `~/.claude/settings.json` is valid JSON. Run `cat ~/.claude/settings.json` to inspect it.

**Claude can't access the URL**
The repo may be private. Test with a public repo first. If MCP isn't set up yet, Claude will use training knowledge instead — still useful, just not live.

**"command not found: npx"**
Install Node.js from [nodejs.org](https://nodejs.org) first.

---

_[Claude Code in Practice](https://maven.com/boring-bot/claude-code-in-practice) · Hamza Farooq · Traversaal.ai_
