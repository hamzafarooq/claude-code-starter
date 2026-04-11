# Module 2: How the web works — and how to read code you didn't write

Course: [Claude Code in Practice](https://maven.com/boring-bot/claude-code-in-practice)
Instructor: Hamza Farooq, Traversaal.ai

---

## What you'll learn

- What frontend, backend, and AI backend actually mean (with a live demo)
- How to build your own Claude skill from scratch
- How to connect Claude Code to the web using Brave MCP
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

The skill file is already in this folder at:

```
module-2/.claude/skills/explain-me-a-repo/SKILL.md
```

Copy the `.claude/` folder into whichever project folder you're working in, or run Claude from the `module-2/` folder directly.

### Step 2: Read the skill file

Open [.claude/skills/explain-me-a-repo/SKILL.md](.claude/skills/explain-me-a-repo/SKILL.md) and read it. Notice:
- The `name:` field is what you type after `/`
- The `description:` tells Claude when to use it
- The body is the instruction set Claude follows

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

## Assignment 2b: Set up Brave MCP

MCP (Model Context Protocol) lets Claude use external tools — including a real browser. Once you set up Brave MCP, Claude can navigate to URLs, read pages, and browse repos live.

### Step 1: Install Brave Browser

Download from [brave.com](https://brave.com) if you don't already have it.

### Step 2: Install the Brave MCP server

Open your terminal and run:

```bash
npx @anthropic/mcp-server-brave-search
```

Or install it globally:

```bash
npm install -g @anthropic-ai/mcp-server-brave
```

### Step 3: Add MCP to Claude Code settings

Open (or create) your Claude Code settings file:

```
~/.claude/settings.json
```

Add the following (merge with any existing content):

```json
{
  "mcpServers": {
    "brave-devtools": {
      "command": "npx",
      "args": ["@browserbasehq/mcp-browserbase"],
      "env": {}
    }
  }
}
```

### Step 4: Restart Claude Code and verify

Stop Claude Code (`Ctrl+C`) and restart it:

```bash
claude
```

Type this to confirm MCP is connected:

```
List the MCP tools available to you.
```

You should see Brave browser tools listed (browser_navigate, browser_snapshot, etc.).

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

| What you want | What to type |
|---|---|
| Explain a GitHub repo | `/explain-me-a-repo` |
| Understand a file | `"Read [filename] and explain what it does in plain English"` |
| Find where something happens | `"Where in this codebase does [X] happen?"` |
| Prep questions for an engineer | `"What would an engineer need to know before building on top of this?"` |
| Turn repo into a PRD | `"Based on this repo, write a PRD for a web version"` |

---

## Troubleshooting

**Skill not triggering**
Check that `.claude/skills/explain-me-a-repo/SKILL.md` exists in your working folder and the `name:` field matches exactly.

**Brave MCP not connecting**
Restart Claude Code and check `~/.claude/settings.json` is valid JSON. Run `cat ~/.claude/settings.json` to inspect it.

**Claude can't access the URL**
The repo may be private. Test with a public repo first. If MCP isn't set up yet, Claude will use training knowledge instead — still useful, just not live.

**"command not found: npx"**
Install Node.js from [nodejs.org](https://nodejs.org) first.

---

*[Claude Code in Practice](https://maven.com/boring-bot/claude-code-in-practice) · Hamza Farooq · Traversaal.ai*
