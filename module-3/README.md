# Module 3: Sub-Agents — Your Team of Specialists

Course: [Claude Code in Practice](https://maven.com/boring-bot/claude-code-in-practice)
Instructor: Hamza Farooq, Traversaal.ai

---

## Before you start

You need Claude Code installed and a project folder open. If you haven't done that yet, follow the [setup guide](../README.md) first.

This module builds on Module 2. If you haven't made a Skill yet, do Module 2 first — you'll use your `/write-prd` skill in Assignment 3c.

The key concept: **sub-agents are specialists you hire.** You write their job description once. Claude Code delegates automatically whenever you ask something that matches. They work in their own context window and hand you back a clean summary.

---

## What's in this folder

```
module-3/
├── README.md                   ← you are here (assignment guide)
└── .claude/
    └── agents/
        ├── research-agent.md   ← Assignment 3a
        ├── prd-reviewer.md     ← Assignment 3b
        ├── code-reviewer.md    ← Assignment 3d
        ├── data-analyst.md     ← Assignment 3e (optional)
        └── copy-writer.md      ← Assignment 3e (optional)
```

Mac tip: folders starting with `.` are hidden by default. Press `Cmd + Shift + .` in Finder to show them, or open the folder in VS Code where they're always visible.

---

## Assignment 3a: Build your research-agent

### What it does
Searches the web and returns a clean structured summary — competitors, market trends, background context. All the search noise stays in its own context window. Only the findings come back to you.

### Create the file

Open VS Code. Create a new file at `.claude/agents/research-agent.md` and paste this:

```markdown
---
name: research-agent
description: Research competitors, market trends, or background context.
  Use when asked to research, analyze competitors, or gather market
  information about a product, company, or industry.
model: claude-opus-4-6
tools:
  - WebSearch
  - WebFetch
  - Read
memory: .claude/memory/research-agent
---

You are a product research specialist.

When given a research task:
1. Search for the most recent information (prioritize sources from the last 12 months)
2. Cross-reference at least 2 independent sources
3. Return a structured summary in this exact format:

**Key Findings** (3–5 bullets)
- [finding 1]
- [finding 2]

**Sources**
- [URL 1] — [one-line description]
- [URL 2] — [one-line description]

**Gaps & Uncertainties**
- [anything you couldn't confirm or that needs deeper investigation]

Be concise. Return findings only. Do not explain your search process.
```

### Test it

Start a new Claude Code session in this folder and type:

```
Research the top 3 competitors for a clinical note automation tool for doctors.
```

Claude should automatically delegate to `research-agent`. You'll see it working in a separate context. When it finishes, a clean summary appears in your main session.

### How to know it's working

Claude will say something like: *"I'll have the research-agent look into this."* If it doesn't delegate automatically, check that the description field in your frontmatter starts with a clear trigger condition ("Use when asked to research...").

---

## Assignment 3b: Build your prd-reviewer

### What it does
Reads any PRD and returns 3 risks, 3 missing edge cases, and 1 scope creep flag — in that exact format, every time.

### Create the file

Create `.claude/agents/prd-reviewer.md`:

```markdown
---
name: prd-reviewer
description: Review a PRD and flag missing acceptance criteria, edge cases, and
  scope creep. Use when asked to review, critique, audit, or check any product
  requirement document or feature spec.
model: claude-sonnet-4-6
tools:
  - Read
---

You are a senior product manager reviewing a PRD for quality and completeness.

Read the PRD at the path provided. Then return this exact format:

**Risks** (rate each HIGH / MED / LOW)
1. [risk] — [severity]
2. [risk] — [severity]
3. [risk] — [severity]

**Missing Edge Cases**
1. [edge case not covered]
2. [edge case not covered]
3. [edge case not covered]

**Scope Creep Flag**
[One thing in the PRD that is out of scope for the stated goal]

One sentence per item. Findings only — no summaries, no praise.
```

### Test it

Point it at a real PRD file:

```
Review the PRD at docs/prd.md
```

Or, if you don't have a PRD yet, run `/write-prd` first (from your Module 2 skill), save it to `docs/prd.md`, then run the reviewer.

---

## Assignment 3c: Build a sub-agent pipeline

A pipeline is two or more agents working in sequence. Output from one becomes input to the next. No coordination layer needed — you're the handoff point.

### The pipeline: research → PRD

After completing 3a and 3b, run this in a single session:

```
Research the top 3 competitors for [your product idea].
Then use those findings to write a PRD for [your product].
Save the PRD to docs/prd.md.
Then review that PRD for risks and missing edge cases.
```

Claude will:
1. Delegate to `research-agent` (Opus, web access)
2. Use the findings to draft a PRD (your `/write-prd` skill if you have it, or directly)
3. Delegate to `prd-reviewer` (Sonnet, read-only) to audit it
4. Return the review

**That's a three-stage automated PM workflow — competitor research to reviewed spec — in one prompt.**

### What to notice

- Your main context stays clean the whole time
- Each agent runs independently; they never talk to each other
- The only "handoff" is you describing the sequence in your prompt
- Total time: 3–5 minutes depending on web search speed

---

## Assignment 3d: Add your code-reviewer

Even if you don't write code yourself, having a read-only code reviewer means you can check what Claude built before asking your engineer to look at it.

### Create the file

Create `.claude/agents/code-reviewer.md`:

```markdown
---
name: code-reviewer
description: Scan code changes and flag security issues, logic errors, and
  missing tests. Use when asked to review code, check a diff, look at a
  pull request, or audit any file before committing or deploying.
model: claude-sonnet-4-6
tools:
  - Read
  - Glob
  - Grep
---

You are a read-only code reviewer. You can read files but never modify them.

Review the code at the path(s) provided. Check for:
- Security vulnerabilities (injection, exposed secrets, missing auth)
- Logic errors (off-by-one, wrong conditionals, unhandled edge cases)
- Missing test coverage (untested paths, no error handling)

Return this exact format for each finding:

[CRITICAL/WARN/INFO] file.ts:42 — [what's wrong] → [how to fix it]

If no issues found, say: "No issues found in reviewed scope."

Never suggest refactors or style changes. Security and correctness only.
```

### Test it

After Claude builds something for you, say:

```
Review the code Claude just wrote for security issues and logic errors.
```

---

## Assignment 3e: Add the remaining agents (optional)

Two more agents to round out your library:

### data-analyst.md

```markdown
---
name: data-analyst
description: Analyze data exports and surface key stats, anomalies, and trends.
  Use when asked to analyze data, interpret metrics, or find patterns in a
  CSV, JSON, spreadsheet export, or any data file.
model: claude-sonnet-4-6
tools:
  - Read
  - Glob
memory: .claude/memory/data-analyst
---

You are a data analyst. Read the file(s) at the path provided.

Return this format:

**Key Stats** (3 numbers worth knowing)
- [stat 1]
- [stat 2]
- [stat 3]

**Anomaly Worth Investigating**
[One data point or pattern that looks unusual]

**Trend**
[One directional change over time visible in the data]

Use the data schema in memory if available. Update memory with any new schema
patterns or column names discovered. Do not return raw data rows.
```

### copy-writer.md

```markdown
---
name: copy-writer
description: Write in-app copy, email subject lines, onboarding tooltips,
  button labels, or microcopy. Use when asked to write copy, UI text, or
  any user-facing string for the product.
model: claude-haiku-4-5-20251001
tools:
  - Read
---

Write concise, clear copy for the product.

For each request, return 3 options labeled A, B, and C.
Tag each with its tone: [Direct] [Warm] [Bold]

Keep all copy under 12 words unless the format requires more.
Match the product voice: professional, plain English, no jargon.

Do not explain your choices. Return the options only.
```

Note the model: `claude-haiku-4-5-20251001` — this is intentional. Haiku is fast and cheap for high-volume, repetitive copy tasks. Save Opus for research, Sonnet for analysis, Haiku for copy.

---

## Assignment 3f (Bonus): Design your agent team blueprint

You don't need to build this — just design it. This is your Module 4 preparation.

For your own product, answer these 5 questions in writing:

1. **What task would actually require your agents to talk to each other?** (If no task comes to mind, you don't need a team yet — sub-agents are enough.)
2. **Name 3 specialists and their jobs.** (e.g., Backend, Frontend, QA — or Researcher, Analyst, Writer)
3. **Which model would each use and why?**
4. **Which files or directories does each teammate own exclusively?** (Two teammates editing the same file = overwrites and chaos.)
5. **What would you use as a `TaskCompleted` hook to enforce quality before work is accepted?**

Post your blueprint in the course Slack. You'll build it in Module 4.

---

## Your sub-agent library structure

When all five agents are in place:

```
.claude/
└── agents/
    ├── research-agent.md     # Opus — web research
    ├── prd-reviewer.md       # Sonnet — spec quality check
    ├── code-reviewer.md      # Sonnet — read-only code audit
    ├── data-analyst.md       # Sonnet — data interpretation
    └── copy-writer.md        # Haiku — fast, high-volume copy
```

These agents are available in any Claude Code session you open in this folder. You don't invoke them manually — Claude delegates automatically when your request matches the description field.

---

## Prompts worth saving

| What you want | What to type |
|---|---|
| Research a competitor | `"Research [company] — what do they charge, who's their target customer, and what do users complain about?"` |
| Review your PRD | `"Review the PRD at docs/prd.md for risks and missing edge cases"` |
| Run the full pipeline | `"Research [topic], write a PRD, and review it for gaps — save to docs/prd.md"` |
| Check code before review | `"Review the code in src/ for security issues"` |
| Write copy options | `"Write 3 options for the onboarding welcome message"` |
| Analyze your data | `"Analyze the export at data/users.csv and tell me what stands out"` |
| Check agent is wired up | `"What sub-agents do you have access to?"` |

---

## Troubleshooting

**Claude isn't delegating to my agent**
The most common cause: the description field is too vague. Instead of "Use for research", write "Use when asked to research competitors, market trends, or background context." The more specific the trigger, the more reliably Claude delegates.

**"I don't see the agent being called"**
Check that the file is at exactly `.claude/agents/<name>.md` (not `.claude/skills/` or anywhere else). The folder name must be `agents`, not `agent`.

**Agent returns too much noise**
Tighten the output format in the system prompt. Add: "Return findings only. Do not explain your process. Do not include raw search results."

**The memory field isn't working**
Create the memory directory first: `mkdir -p .claude/memory/research-agent`. The agent will create and update files there as it runs.

**Sub-agents vs skills: which do I use?**
Skills = you trigger it with `/command`. Sub-agents = Claude triggers it automatically when your request matches. Use skills for repeatable workflows you want to control. Use sub-agents for specialist tasks you want Claude to handle without a manual command.

---

*[Claude Code in Practice](https://maven.com/boring-bot/claude-code-in-practice) · Hamza Farooq · Traversaal.ai*
