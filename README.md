# Claude Code in Practice

**A hands-on course for product managers who want to ship real things — without waiting on engineering.**

Build production apps, write PRDs with AI, and go from idea to deployed product using Claude Code. No coding background required.

[![Maven Course](https://img.shields.io/badge/Maven-Enroll%20Now-blue?style=for-the-badge)](https://maven.com/boring-bot/claude-code-in-practice)
[![Modules](https://img.shields.io/badge/Modules-3-brightgreen?style=for-the-badge)](#-course-modules)
[![Apps Built](https://img.shields.io/badge/Apps%20Built-3-orange?style=for-the-badge)](#-built-with-claude-code)
[![Status](https://img.shields.io/badge/Status-Active%20Cohorts-success?style=for-the-badge)](#)
[![Instructor](https://img.shields.io/badge/Instructor-Hamza%20Farooq-purple?style=for-the-badge)](https://maven.com/boring-bot/claude-code-in-practice)

> Taught by **Hamza Farooq** — Founder at Traversaal.ai · UCLA Anderson · ex-Google

[![Enroll in Claude Code in Practice on Maven](images/Screenshot%202026-04-16%20at%2002.26.25.png)](https://maven.com/boring-bot/claude-code-in-practice)

---

## 🚀 Get Started

**Three steps to your first session:**

```bash
# 1. Clone the repo
git clone https://github.com/hamzafarooq/claude-code-starter.git
cd claude-code-starter/module-1

# 2. Launch Claude Code
claude

# 3. Open your first assignment
# → See module-1/README.md
```

> First time? Follow the full [Installation guide](#-installation) below — takes about 10 minutes.

---

## 📦 What's in This Repo

All course code, templates, skills, and commands live here. Come back here whenever you need files from class.

| What | Where |
|------|-------|
| Module guides & assignments | `module-N/README.md` |
| CLAUDE.md starter templates | `module-N/CLAUDE-template.md` |
| Skills | `module-N/.claude/skills/<name>/SKILL.md` |
| Commands | `module-N/.claude/commands/<name>.md` |
| Community resources | [`docs/resources.md`](docs/resources.md) |

---

## 📚 Course Modules

### [Module 1: From Idea to Shipped Product](module-1/README.md)

Set up Claude Code, write a `CLAUDE.md` that gives Claude context about your project, install two skills, and ship something by the end of the module.

| Assignment | What you'll do |
|-----------|---------------|
| 1. Set up `CLAUDE.md` | Write your project context file so Claude knows your stack and goals |
| 2. Install skills | Add `/prd-generator` and `/user-story-writer` to your workflow |
| 3. Ship something | Go from idea → PRD → working MVP |

**Skills included:**
- `/prd-generator` — generates a structured PRD from a feature description
- `/user-story-writer` — converts rough ideas into user stories with acceptance criteria

**Files:**
- [module-1/README.md](module-1/README.md) — setup guide and assignments
- [module-1/CLAUDE-template.md](module-1/CLAUDE-template.md) — starter template
- [module-1/.claude/skills/](module-1/.claude/skills/prd-generator/SKILL.md) — skill files

---

### [Module 2: How the Web Works — and How to Read Code You Didn't Write](module-2/README.md)

Learn what frontend, backend, and AI backend actually mean, build a custom skill that reads GitHub repos, set up Brave MCP for live browsing, and use it all to understand a real codebase.

| Assignment | What you'll do |
|-----------|---------------|
| 1. Build `/explain-me-a-repo` | Write a skill that uses Brave MCP to read and summarize any GitHub repo |
| 2. Set up Brave MCP | Connect Claude Code to a live browser |
| 3. Use it on a real codebase | Run the skill on a repo you care about |

**Skills & commands included:**
- `/explain-me-a-repo` — navigates to a GitHub URL and produces a structured repo write-up
- `/youtube-deepdive` — visits YouTube URLs and produces a highlight report with timestamps and top comments

**Files:**
- [module-2/README.md](module-2/README.md) — assignment guide
- [module-2/CLAUDE-template.md](module-2/CLAUDE-template.md) — starter template
- [module-2/demo/index.html](module-2/demo/index.html) — frontend/backend/AI backend live demo
- [module-2/.claude/skills/explain-me-a-repo/SKILL.md](module-2/.claude/skills/explain-me-a-repo/SKILL.md)

---

### [Module 3: Sub-Agents — Your Team of Specialists](module-3/README.md)

Learn what sub-agents are, when to use them vs. skills, and build a library of 5 specialist agents. Culminates in a three-stage automated pipeline: competitor research → PRD → spec review — in one prompt.

| Assignment | What you'll do |
|-----------|---------------|
| 3a. Build `research-agent` | Web search specialist that returns clean structured findings |
| 3b. Build `prd-reviewer` | Reads any PRD and returns risks, edge cases, and scope creep flag |
| 3c. Build a pipeline | Chain research-agent → write PRD → prd-reviewer in a single prompt |
| 3d. Build `code-reviewer` | Read-only code audit for security and logic errors |
| 3e. Add `data-analyst` + `copy-writer` (optional) | Complete your specialist library |

**Agents included:**
- `research-agent` — Opus + web search, structured findings
- `prd-reviewer` — Sonnet, reads and audits any PRD
- `code-reviewer` — Sonnet, read-only security and logic review
- `data-analyst` — Sonnet, stats and anomaly detection from data files
- `copy-writer` — Haiku, fast in-app copy with 3 tone options
- `deck-builder` — Sonnet, researches a topic and produces a McKinsey-style deck for non-technical audiences

**Files:**
- [module-3/README.md](module-3/README.md) — assignment guide
- [module-3/.claude/agents/](module-3/.claude/agents/research-agent.md) — all 5 agent files

---

## 🧩 Skills Library

Skills are triggered with a `/command`. You install them once; Claude runs them on demand. All skills live in `.claude/skills/<name>/SKILL.md`.

| Skill | Command | What it does | Module |
|-------|---------|-------------|--------|
| PRD Generator | `/prd-generator` | Asks for a feature name, problem, target user, and constraints — then writes a full 9-section PRD with risks, acceptance criteria, and open questions | [Module 1](module-1/.claude/skills/prd-generator/SKILL.md) |
| User Story Writer | `/user-story-writer` | Turns a rough feature idea into prioritised user stories with Given/When/Then acceptance criteria, edge cases, and open questions | [Module 1](module-1/.claude/skills/user-story-writer/SKILL.md) |
| YouTube Deep Dive | `/youtube-deepdive` | Takes one or more YouTube URLs, visits each with Brave MCP, and returns a structured highlight report: timestamps, key moments, and top comments — so you skip to the best parts | [Module 2](module-2/.claude/skills/youtube-deepdive/SKILL.md) |
| YouTube Researcher | `/youtube-researcher` | Searches YouTube on any topic and returns a ranked table of videos with titles, channels, view counts, and a top-pick recommendation | [Module 2](module-2/.claude/skills/youtube-researcher/SKILL.md) |
| Explain Me a Repo | `/explain-me-a-repo` | Takes a GitHub URL, navigates to it with Brave MCP, and produces a structured repo write-up: what it does, how it's built, key files, and who it's for | [Module 2](module-2/.claude/commands/explain-me-a-repo.md) |

---

## 🤖 Sub-Agents Library

Sub-agents are specialists Claude delegates to automatically — no `/command` needed. When your request matches an agent's description, Claude hands it off, runs it in a separate context, and returns only the findings. All agents live in `.claude/agents/<name>.md`.

| Agent | Model | What it does | Module |
|-------|-------|-------------|--------|
| `research-agent` | Opus | Searches the web and returns structured findings: key facts, sources, and gaps. Triggers on any research, competitor analysis, or market context request | [Module 3](module-3/.claude/agents/research-agent.md) |
| `prd-reviewer` | Sonnet | Reads any PRD and returns exactly 3 risks (rated HIGH/MED/LOW), 3 missing edge cases, and 1 scope creep flag — no summaries, no praise | [Module 3](module-3/.claude/agents/prd-reviewer.md) |
| `code-reviewer` | Sonnet | Read-only audit of code files — flags security vulnerabilities, logic errors, and missing test coverage. Never modifies files | [Module 3](module-3/.claude/agents/code-reviewer.md) |
| `data-analyst` | Sonnet | Reads CSV, JSON, or data exports and returns 3 key stats, 1 anomaly worth investigating, and 1 directional trend | [Module 3](module-3/.claude/agents/data-analyst.md) |
| `copy-writer` | Haiku | Writes in-app copy, tooltips, button labels, and microcopy. Returns 3 options tagged [Direct], [Warm], or [Bold] — all under 12 words | [Module 3](module-3/.claude/agents/copy-writer.md) |
| `deck-builder` | Sonnet | Researches a topic using Brave MCP (Reddit, Medium, YouTube) and produces a McKinsey-style presentation deck with speaker notes — designed for non-technical audiences | [Module 3](module-3/.claude/agents/deck-builder.md) |

---

## 🧠 Skills vs Sub-Agents vs Agents — What's the Difference?

Three different ways to extend Claude Code. Here's when to use each one:

| | Skill | Sub-Agent | Agent |
|--|-------|-----------|-------|
| **What it is** | A prompt template you invoke with a `/command` | A specialist Claude spins up automatically and delegates to | A fully autonomous Claude instance with its own tools, model, and instructions |
| **How it's triggered** | You type `/skill-name` | Claude decides when to use it based on your request | Triggered by Claude or called explicitly via the Agent tool |
| **Who controls it** | You — you call it deliberately | Claude — it decides when to hand off | Claude or the system |
| **Memory/context** | Shares the main conversation context | Runs in a separate context, returns only results | Fully isolated context with its own tool access |
| **Best for** | Repeatable tasks you always want to run the same way (PRD generation, user stories) | Background specialists that shouldn't clutter your main thread (research, code review, data analysis) | Complex multi-step tasks that need dedicated focus or different model/tool access |
| **Lives in** | `.claude/skills/<name>/SKILL.md` | `.claude/agents/<name>.md` | `.claude/agents/<name>.md` (same file format as sub-agents) |
| **Example** | `/prd-generator` — you run it, Claude fills in a PRD | `research-agent` — Claude uses it when you ask for competitor research | A pipeline agent that runs research → writes PRD → reviews PRD autonomously |

**Simple rule of thumb:**
- Use a **skill** when you want to run the same prompt yourself, on demand.
- Use a **sub-agent** when you want Claude to automatically hand off specialist work (and you don't want the details in your main chat).
- An **agent** is the underlying mechanism — sub-agents *are* agents, just scoped to delegate-and-return behavior. You'll hear both terms used interchangeably.

---

## 🌐 Playwright vs MCP — What's the Difference?

Both let Claude interact with a browser. Here's when to use each:

| | Playwright | MCP (e.g. Brave MCP) |
|--|-----------|----------------------|
| **What it is** | A code library that automates browsers via scripts | A live browser Claude controls in real time through a protocol |
| **How it works** | You (or Claude) writes code that drives the browser — clicks, fills forms, scrapes pages | Claude connects to a running browser and takes actions directly, no code required |
| **Best for** | Repeatable, scheduled, or high-volume browser tasks (scraping, regression testing, form automation) | One-off research, reading live pages, visiting URLs during a conversation |
| **Requires coding?** | Yes — Python or JavaScript scripts | No — Claude drives it through natural language |
| **Speed** | Fast at scale, runs headless | Slower, real browser with a visible UI |
| **When you'd use it** | "Scrape 500 product pages every night" or "Run login tests on every deploy" | "Visit this GitHub repo and summarise it" or "Read the top 3 results for this search" |
| **In this course** | Not covered (engineering territory) | Used in Module 2 for `/explain-me-a-repo` and `/youtube-deepdive` |

**Simple rule of thumb:** Use MCP when you want Claude to browse something *now*, in conversation. Use Playwright when you need browser automation to run reliably at scale or on a schedule — that's usually an engineering task.

---

## 🛠️ Built with Claude Code

These are real, full-stack applications you can try out today — built live in class using Claude Code, with no engineering team. Fork them, break them, learn from them.

| App | What it does |
|-----|-------------|
| [word-humanizer](https://github.com/hamzafarooq/word-humanizer/) | Word add-in that rewrites AI-generated paragraphs to sound human — sits inside Word as a sidebar, rewrites one paragraph at a time, and shows exactly what patterns were removed |
| [seo-writer](https://github.com/hamzafarooq/seo-writer) | AI agent that researches a topic, finds images, and produces a finished SEO article in Markdown, HTML, and DOCX — learns from your existing articles to match your voice |
| [linkedin-growth](https://github.com/hamzafarooq/linkedin-growth) | Audits your LinkedIn profile against profiles you admire and produces a 90-day content plan — all from a single command in Claude Code |

More apps get added as the course runs.

---

## 🌐 Community Resources

Top GitHub repos for going deeper on skills, best practices, and memory management. Full write-ups in [docs/resources.md](docs/resources.md).

### Discover & Browse

| Repo | Stars | What it is |
|------|-------|-----------|
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | ⭐ 39k | The definitive curated list: skills, hooks, commands, agents, plugins |
| [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | ⭐ 33k | 1,400+ installable agentic skills for Claude Code and other AI CLIs |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | ⭐ 17k | 100+ specialized Claude Code subagents for development use cases |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | ⭐ 16k | 1,000+ agent skills from official teams and the community |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | ⭐ 11k | Curated Claude Skills list with workflow examples |

### Skills & Best Practices

| Repo | Stars | What it is |
|------|-------|-----------|
| [YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill) | ⭐ 256 | Reusable skill modules — good reference for structuring your own |
| [agamm/claude-code-owasp](https://github.com/agamm/claude-code-owasp) | ⭐ 128 | OWASP security best practices skill (Top 10:2025, ASVS 5.0) |
| [ThamJiaHe/claude-code-handbook](https://github.com/ThamJiaHe/claude-code-handbook) | ⭐ 104 | Guide for professional Claude prompts with MCP and Skills |

### Memory Management

| Repo | What it is |
|------|-----------|
| [lucasrosati/claude-code-memory-setup](https://github.com/lucasrosati/claude-code-memory-setup) | **Obsidian + Graphify** — up to 71.5x fewer tokens per session. Persistent memory and codebase knowledge graphs. |

---

## 🤔 What is Claude Code?

An AI assistant that runs inside your project folder and reads your actual files. Not a chatbot — a collaborator.

| Claude.ai / ChatGPT | Claude Code |
|---------------------|-------------|
| You paste text into a chat box | Claude reads your actual files |
| Starts fresh every conversation | Remembers your project through `CLAUDE.md` |
| You copy-paste results manually | Edits files directly |
| General-purpose | Configured for how your team works |

---

## ⚙️ Installation

Takes about 10 minutes. You'll do it once.

### Step 1 — Choose your access method

**Option A: Claude Max (recommended)**

Claude Max ($100/month) includes Claude Code with no usage limits and no per-token billing.

1. Go to [claude.ai/upgrade](https://claude.ai/upgrade) → subscribe to **Max**
2. Claude Code is included — no API key needed
3. Run `claude` and log in with your Claude account

**Option B: API Key (pay as you go)**

Better if you want to control costs or are already an API customer.

1. Go to [console.anthropic.com](https://console.anthropic.com) → create account → **API Keys** → **Create Key**

![Anthropic Console — API Keys page](https://developer.puter.com/assets/img/anthropic/api-key-page.webp)

2. Copy the key (starts with `sk-ant-...`) — you won't see it again
3. Set it in your terminal:

```bash
export ANTHROPIC_API_KEY=sk-ant-your-key-here

# Make it permanent:
echo 'export ANTHROPIC_API_KEY=sk-ant-your-key-here' >> ~/.zshrc
source ~/.zshrc
```

> Never commit your API key to GitHub.

### Step 2 — Install Claude Code

Requires [Node.js](https://nodejs.org) (LTS version).

```bash
npm install -g @anthropic/claude-code

# Verify:
claude --version
```

### Step 3 — Start Claude Code

```bash
cd claude-code-starter/module-1
claude
```

![Claude Code running in terminal](https://raw.githubusercontent.com/anthropics/claude-code/main/demo.gif)

You're in. Head to [module-1/README.md](module-1/README.md) for your first assignment.

---

## 💬 Prompts Worth Keeping

| What you want | What to type |
|---------------|-------------|
| Generate a PRD | `/prd-generator` |
| Write user stories | `/user-story-writer` |
| Find gaps in a spec | `"Review docs/prd.md and tell me what's missing"` |
| Write for execs | `"Rewrite this as 3 bullets for a VP with 10 seconds"` |
| Prep for engineering | `"What questions will engineers ask about this PRD?"` |
| Build a sprint plan | `"Turn the must-have stories into a 2-week sprint plan"` |
| Stress-test a flow | `"What edge cases am I missing here?"` |

---

## 🔧 Troubleshooting

**`command not found: claude`**
Run `npm install -g @anthropic/claude-code` again. Check Node.js is installed: `node --version`.

**API key error**
Run `export ANTHROPIC_API_KEY=your-key-here`. Make sure the key includes `sk-ant-`.

**Claude isn't reading my CLAUDE.md**
The file must be named exactly `CLAUDE.md` (all caps) in the folder where you ran `claude`.

**Skill not triggering**
Check the path is `.claude/skills/<name>/SKILL.md` and the `name:` field in the frontmatter matches what you typed after `/`.

---

[![Enroll in Claude Code in Practice on Maven](images/Screenshot%202026-04-16%20at%2002.26.25.png)](https://maven.com/boring-bot/claude-code-in-practice)

*[Claude Code in Practice](https://maven.com/boring-bot/claude-code-in-practice) · Hamza Farooq · Traversaal.ai*
