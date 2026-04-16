# Claude Code in Practice

**A hands-on course for product managers who want to ship real things — without waiting on engineering.**

Build production apps, write PRDs with AI, and go from idea to deployed product using Claude Code. No coding background required.

[![Maven Course](https://img.shields.io/badge/Maven-Enroll%20Now-blue?style=for-the-badge)](https://maven.com/boring-bot/claude-code-in-practice)
[![Modules](https://img.shields.io/badge/Modules-2-brightgreen?style=for-the-badge)](#-course-modules)
[![Apps Built](https://img.shields.io/badge/Apps%20Built-3-orange?style=for-the-badge)](#-built-with-claude-code)
[![Status](https://img.shields.io/badge/Status-Active%20Cohorts-success?style=for-the-badge)](#)
[![Instructor](https://img.shields.io/badge/Instructor-Hamza%20Farooq-purple?style=for-the-badge)](https://maven.com/boring-bot/claude-code-in-practice)

> Taught by **Hamza Farooq** — Founder at Traversaal.ai · UCLA Anderson · ex-Google

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

## 🛠️ Built with Claude Code

Full-stack apps built live in class. Fork them, break them, learn from them.

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

*[Claude Code in Practice](https://maven.com/boring-bot/claude-code-in-practice) · Hamza Farooq · Traversaal.ai*
