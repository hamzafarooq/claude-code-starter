# Day 0 — Your First 30 Minutes with Claude Code

**For product managers. No coding required.**

This folder is your starting point. Before you do anything else, read this guide.
It will show you the two things that make Claude Code dramatically more useful than a generic AI chat:

1. **CLAUDE.md** — a file that tells Claude who you are and how to work with you
2. **Skills** — reusable behaviors you can trigger with a single command

---

## Table of Contents

- [What is Claude Code?](#what-is-claude-code)
- [Step 1 — Install Claude Code](#step-1--install-claude-code)
- [Step 2 — Set up your API key](#step-2--set-up-your-api-key)
- [Step 3 — Open your project folder](#step-3--open-your-project-folder)
- [Step 4 — Create your CLAUDE.md file](#step-4--create-your-claudemd-file)
- [Step 5 — Add your first two skills](#step-5--add-your-first-two-skills)
- [Step 6 — Run your first session](#step-6--run-your-first-session)
- [Quick Reference — Prompts for PMs](#quick-reference--prompts-for-pms)
- [What to do next](#what-to-do-next)
- [Troubleshooting](#troubleshooting)

---

## What is Claude Code?

Claude Code is an AI assistant that lives inside your project folder and works directly with your files.

**The key difference from ChatGPT or Claude.ai:**

| Claude.ai / ChatGPT | Claude Code |
|---|---|
| You paste text into a chat box | Claude reads your actual files |
| Starts fresh every conversation | Remembers your project through `CLAUDE.md` |
| You copy-paste results manually | Edits files for you in real time |
| General-purpose | Configured for your team's way of working |
| No context about your product | Knows your PRDs, decisions, and conventions |

Think of it as a very capable colleague who has read every document in your project folder and follows a standing briefing you wrote once.

---

## Step 1 — Install Claude Code

Open your terminal (on Mac: press `Cmd + Space`, type "Terminal", hit Enter).

Run this command:

```
npm install -g @anthropic/claude-code
```

If you see an error about `npm` not being found, you need to install Node.js first:
1. Go to [nodejs.org](https://nodejs.org)
2. Download and install the "LTS" version
3. Re-run the command above

To confirm installation worked, run:
```
claude --version
```

You should see a version number printed. If you do, you're ready to move on.

---

## Step 2 — Set up your API key

Claude Code needs an Anthropic API key to work.

**Getting your key:**
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Create a free account (or log in)
3. Click **API Keys** in the left sidebar
4. Click **Create Key**, give it a name like "claude-code"
5. Copy the key — it starts with `sk-ant-...`

**Setting your key in the terminal:**

On Mac/Linux:
```
export ANTHROPIC_API_KEY=sk-ant-your-key-here
```

To make this permanent (so you don't have to set it every session):
```
echo 'export ANTHROPIC_API_KEY=sk-ant-your-key-here' >> ~/.zshrc
source ~/.zshrc
```

To verify it's set:
```
echo $ANTHROPIC_API_KEY
```

You should see your key printed back. Never share this key or commit it to GitHub.

---

## Step 3 — Open your project folder

Navigate to your project in the terminal. For this guide, that's the `day0` folder inside `claude-code-prototype`:

```
cd path/to/claude-code-prototype/day0
```

Then start Claude Code:
```
claude
```

You'll see a prompt appear. Claude is now running inside your folder.

> **Tip:** You can also open Claude Code from VS Code by installing the Claude Code extension, then pressing `Cmd+Shift+P` and searching "Open Claude Code."

---

## Step 4 — Create your CLAUDE.md file

This is the most important setup step. `CLAUDE.md` is a plain text file that Claude reads automatically every time you start a session. It tells Claude:

- What kind of work you do
- What your project is about
- How you want Claude to respond
- What shortcuts and conventions your team uses

**Think of it as a standing briefing memo you write once.**

### What makes a good CLAUDE.md

A good `CLAUDE.md` answers these four questions:

1. **Who am I?** — Your role, expertise, what you care about
2. **What is this project?** — Product context, goals, current phase
3. **How should Claude talk to me?** — Tone, format, level of technical detail
4. **What are our conventions?** — File locations, naming, workflows

### Template — copy and customize this

This folder includes a ready-to-use `CLAUDE.md` template at [CLAUDE.md](CLAUDE.md).

Here is what it contains and why each section matters:

```
# [Your Name]'s PM Workspace — Claude Code Guide
```
The title tells Claude who owns this workspace.

```
## Who I am
- Product Manager at [Company]
- Focus: [your product area, e.g. "growth and monetization"]
- I'm comfortable with product thinking but not with code
- I work with a team of 4 engineers and a designer
```
This shapes how Claude explains things. A PM gets plain English. An engineer gets code.

```
## What this project is
[One sentence description of your product]
Current phase: [Discovery / Alpha / Beta / Launched]
Key stakeholders: [PM, Eng, Design, Legal, etc.]
```
Without this, Claude treats every project the same. With it, Claude gives you context-specific answers.

```
## How Claude should respond
- Keep answers concise — I don't need long explanations
- Use plain English, no jargon
- When I ask you to write something, write it directly — don't explain what you're about to do first
- Flag risks and tradeoffs, but don't lecture
- When editing a file, tell me what changed and why in one sentence
```
This is the most overlooked section. These instructions save you from reformatting Claude's output every single time.

```
## Project conventions
- PRDs live in docs/prd.md
- User stories use the format: "As a [user], I want to [action] so that [outcome]"
- Acceptance criteria use Given/When/Then format
- We always include a "Risks and Assumptions" section in every PRD
```
Conventions make Claude's output drop directly into your existing workflow without editing.

```
## What I ask Claude Code to do
- Draft and review PRDs
- Write user stories and acceptance criteria
- Summarize long documents
- Flag gaps, edge cases, and missing requirements
- Generate sprint plans from a list of user stories
- Rewrite content for different audiences (exec, engineer, customer)
```
This primes Claude for what it's going to help with in this project specifically.

### How to create your CLAUDE.md

**Option A — Let Claude write it for you (recommended):**

Start Claude (`claude` in the terminal), then say:

> "I'm a product manager. Help me create a CLAUDE.md file for my project. Ask me the questions you need to write a good one."

Claude will ask you a few questions and generate the file for you.

**Option B — Copy and edit the template:**

1. Open the `CLAUDE.md` file in this folder
2. Replace each `[placeholder]` with your own information
3. Save the file

Either way, you can always come back and improve it. The file gets better over time.

---

## Step 5 — Add your first two skills

Skills are reusable behaviors stored in `.claude/skills/`. Each skill is a markdown file with instructions Claude follows when you trigger it with a `/skill-name` command.

**Why skills matter for PMs:**

Instead of typing the same long prompt every time ("Write a PRD with these sections: Problem, Users, Goals, User Stories, Acceptance Criteria, Risks..."), you type `/prd-generator` and Claude already knows exactly what format to use.

Skills turn repeated prompting into a one-word command.

### Skill 1: PRD Generator

This skill tells Claude how to generate a structured PRD from a brief description.

**How to create it:**

1. Create this folder path inside your project:
   ```
   .claude/skills/prd-generator/
   ```

2. Inside that folder, create a file called `SKILL.md`

3. Paste the following content (the full template is already in this folder at `.claude/skills/prd-generator/SKILL.md`):

```markdown
---
name: prd-generator
description: Generates a structured PRD from a feature description or brief. Use when asked to write, draft, or create a PRD.
---

## What this skill does
When triggered, ask the user for:
1. Feature name (one line)
2. Problem being solved (1-3 sentences)
3. Target user(s)
4. Any known constraints or context

Then generate a full PRD using this structure:

### PRD Structure
- **Problem Statement** — What pain are we solving and for whom?
- **Goals** — 3-5 measurable outcomes we want to achieve
- **Non-Goals** — What this feature explicitly will not do
- **Users & Use Cases** — Who uses this and how (include 2-3 scenarios)
- **User Stories** — Written as "As a [user], I want to [action] so that [outcome]"
- **Acceptance Criteria** — Written in Given/When/Then format
- **Risks & Assumptions** — What could go wrong; what are we assuming is true
- **Open Questions** — What needs to be decided before engineering starts
- **Success Metrics** — How will we know this worked?

## How to respond
- Write the full PRD directly — do not explain what you're about to write
- Use plain English — no jargon
- Flag any section where you made an assumption with "[ASSUMPTION]"
- End with: "Review and fill in the [ASSUMPTION] sections before sharing with engineering."
```

**How to use it:**

In a Claude Code session, type:
```
/prd-generator
```

Claude will prompt you for the details and generate a complete, structured PRD.

---

### Skill 2: User Story Writer

This skill takes a rough feature idea — even a single bullet point — and turns it into well-formatted user stories with acceptance criteria.

**How to create it:**

1. Create this folder:
   ```
   .claude/skills/user-story-writer/
   ```

2. Create `SKILL.md` inside it (template already in this folder):

```markdown
---
name: user-story-writer
description: Converts feature ideas or bullets into user stories with acceptance criteria. Use when asked to write user stories or break down a feature.
---

## What this skill does
Take a feature description (can be rough — even a bullet point) and produce:

1. **Primary user story** — one main story capturing the core value
2. **Supporting user stories** — 2-4 sub-stories for the key flows
3. **Acceptance criteria** for each story in Given/When/Then format
4. **Edge cases to consider** — 3-5 scenarios the team should discuss

## Format for each user story
```
**Story:** As a [user type], I want to [do something] so that [I get this value].

**Acceptance Criteria:**
- Given [context], when [action], then [result]
- Given [context], when [action], then [result]
- Given [context], when [action], then [result]

**Priority:** Must-have / Should-have / Nice-to-have
**Estimated effort:** Small / Medium / Large
```

## How to respond
- Write the stories directly without preamble
- Keep language simple enough for a non-technical stakeholder to understand
- Mark stories with unclear scope as "[NEEDS CLARIFICATION]"
- After all stories, add a "Questions for the team" section with 2-3 open questions
```

**How to use it:**

```
/user-story-writer
```

Then describe the feature — even informally. Example:
> "Users need a way to export their meeting notes to Jira"

Claude will produce properly formatted stories ready to paste into your sprint board.

---

### How skills are stored

Your project folder structure should now look like this:

```
your-project/
├── CLAUDE.md                          ← Your standing instructions for Claude
├── docs/
│   └── prd.md
└── .claude/
    └── skills/
        ├── prd-generator/
        │   └── SKILL.md               ← Skill 1: generates PRDs
        └── user-story-writer/
            └── SKILL.md               ← Skill 2: writes user stories
```

> **Note:** The `.claude/` folder is hidden by default on Mac (folders starting with `.` are hidden). You can view it in Finder by pressing `Cmd + Shift + .` to show hidden files.

---

## Step 6 — Run your first session

With your `CLAUDE.md` created and two skills installed, here is your first real session:

**Start Claude:**
```
claude
```

**Try these prompts in order:**

**1. Orient Claude to your project:**
> "What do you know about this project based on what you've read?"

Claude should summarize your project accurately based on `CLAUDE.md`.

**2. Test your PRD generator skill:**
> "/prd-generator"

Follow the prompts. Give Claude a real feature idea from your current work.

**3. Test your user story skill:**
> "/user-story-writer"

Describe a feature informally. See how Claude structures it.

**4. Edit and refine:**
> "The acceptance criteria in story 2 are too vague. Rewrite them to be more specific and testable."

**5. Save your output:**
> "Save this PRD to docs/prd.md"

Claude will write the file directly to your project.

---

## Quick Reference — Prompts for PMs

| What you want to do | What to type |
|---|---|
| Generate a full PRD | `/prd-generator` |
| Write user stories | `/user-story-writer` |
| Summarize a document | "Summarize docs/prd.md for me" |
| Find gaps in a PRD | "Review docs/prd.md and tell me what's missing" |
| Write for execs | "Rewrite this as 3 bullets for a VP with 10 seconds" |
| Prep for engineering | "What questions will engineers ask about this PRD?" |
| Create a sprint plan | "Turn the must-have stories into a 2-week sprint plan" |
| Write release notes | "Write release notes for this feature in plain English" |
| Check for edge cases | "What edge cases am I missing in flow 2?" |
| Turn bullets into prose | "Turn these bullets into a well-written problem statement" |

---

## What to do next

Once you've completed Day 0, move to the main course materials:

1. Open [START_HERE.md](../START_HERE.md) for the full 7-step walkthrough
2. Explore [docs/prd.md](../docs/prd.md) — a sample PRD to practice on
3. Open [project/index.html](../project/index.html) in your browser — a live PRD builder app

**Suggested Day 1 exercise:**

Pick a real feature your team is currently working on or planning. Use Claude Code to:
1. Draft the PRD with `/prd-generator`
2. Break it into user stories with `/user-story-writer`
3. Ask Claude: "What are the three riskiest assumptions in this PRD?"
4. Save the final document and share it with your team

---

## Troubleshooting

**"command not found: claude"**
Run `npm install -g @anthropic/claude-code` again. If it still fails, check that Node.js is installed (`node --version`).

**"API key not set" or authentication error**
Run `export ANTHROPIC_API_KEY=your-key-here` in your terminal. Make sure you copied the full key including `sk-ant-`.

**Claude isn't reading my CLAUDE.md**
Make sure the file is named exactly `CLAUDE.md` (all caps) and is in the same folder where you ran `claude`. Claude reads it automatically from the current directory.

**Skill not working / "I don't know that command"**
Check that:
- The skill folder is at `.claude/skills/skill-name/SKILL.md`
- The file is named `SKILL.md` exactly
- The frontmatter at the top has `name:` matching what you typed after `/`

**Claude's responses are too long / too short**
Update the "How Claude should respond" section in your `CLAUDE.md`. For example, add: "Keep all responses under 200 words unless I ask for more."

**I want to reset and start fresh**
In Claude Code, type `/clear` to clear the conversation context. Your files stay untouched.

---

*This workspace is part of [Agentic AI System Design for PMs](https://maven.com/boring-bot/ml-system-design) — taught by Hamza Farooq.*
