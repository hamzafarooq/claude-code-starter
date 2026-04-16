# Claude Code in Practice

A course for product managers who want to ship real things without waiting on engineering.
[Enroll on Maven](https://maven.com/boring-bot/claude-code-in-practice)

Taught by Hamza Farooq, Founder at Traversaal.ai, UCLA Anderson, ex-Google.

---

## Get started

1. Follow the [Installation](#installation) section below to get Claude Code running
2. Clone this repo:
```bash
git clone https://github.com/hamzafarooq/claude-code-starter.git
cd claude-code-starter/module-1
claude
```
3. Open [module-1/README.md](module-1/README.md) for your first assignment

---

## What this repo is

All course code, templates, and skills live here. If you're taking the course, this is the place to come back to when you need files from class.

---

## Course modules

### [Module 1: From idea to shipped product](module-1/README.md)

You'll set up Claude Code, write a `CLAUDE.md` that gives Claude context about your project, install two skills, and ship something by the end.

Assignments:
1. Set up your `CLAUDE.md`
2. Install `/prd-generator` and `/user-story-writer`
3. Go from idea to PRD to MVP

Files:
- [module-1/README.md](module-1/README.md) - setup guide and assignments
- [module-1/CLAUDE-template.md](module-1/CLAUDE-template.md) - starter template
- [module-1/.claude/skills/](module-1/.claude/skills/prd-generator/SKILL.md)

---

### [Module 2: How the web works — and how to read code you didn't write](module-2/README.md)

You'll learn what frontend, backend, and AI backend mean (with a live demo), build a custom skill that reads GitHub repos, set up Brave MCP for live browsing, and use it all to understand a real codebase.

Assignments:
1. Build the `/explain-me-a-repo` skill
2. Set up Brave MCP
3. Use the skill on a live GitHub repo

Files:
- [module-2/README.md](module-2/README.md) - assignment guide
- [module-2/CLAUDE-template.md](module-2/CLAUDE-template.md) - starter template
- [module-2/demo/index.html](module-2/demo/index.html) - frontend/backend/AI backend live demo
- [module-2/.claude/skills/explain-me-a-repo/SKILL.md](module-2/.claude/skills/explain-me-a-repo/SKILL.md)

---

## Built with Claude Code

Apps built live in class. Fork them, break them, learn from them.

| Repo | What it does |
|------|-------------|
| [word-humanizer](https://github.com/hamzafarooq/word-humanizer/) | Rewrites AI-generated text to sound human |
| [seo-writer](https://github.com/hamzafarooq/seo-writer) | Generates SEO-optimized blog content |

More get added as the course runs.

---

## Community resources

Top GitHub repos for going deeper on skills, best practices, and memory management. Full descriptions in [docs/resources.md](docs/resources.md).

### Discover & browse

| Repo | Stars | What it is |
|------|-------|-----------|
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | ⭐ 39k | The definitive curated list: skills, hooks, commands, agents, plugins |
| [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | ⭐ 33k | 1,400+ installable agentic skills for Claude Code and other AI CLIs |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | ⭐ 17k | 100+ specialized Claude Code subagents for development use cases |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | ⭐ 16k | 1,000+ agent skills from official teams and the community |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | ⭐ 11k | Curated Claude Skills list with workflow examples |

### Skills & best practices

| Repo | Stars | What it is |
|------|-------|-----------|
| [YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill) | ⭐ 256 | Reusable skill modules — good reference for structuring your own |
| [agamm/claude-code-owasp](https://github.com/agamm/claude-code-owasp) | ⭐ 128 | OWASP security best practices skill (Top 10:2025, ASVS 5.0) |
| [ThamJiaHe/claude-code-handbook](https://github.com/ThamJiaHe/claude-code-handbook) | ⭐ 104 | Guide for professional Claude prompts with MCP and Skills |

### Memory management

| Repo | What it is |
|------|-----------|
| [lucasrosati/claude-code-memory-setup](https://github.com/lucasrosati/claude-code-memory-setup) | **Obsidian + Graphify** — up to 71.5x fewer tokens per session. Persistent memory and codebase knowledge graphs. |

---

## What is Claude Code?

It's an AI assistant that runs inside your project folder and reads your actual files. The difference from Claude.ai or ChatGPT:

| Claude.ai / ChatGPT | Claude Code |
|---|---|
| You paste text into a chat box | Claude reads your actual files |
| Starts fresh every conversation | Remembers your project through `CLAUDE.md` |
| You copy-paste results manually | Edits files for you directly |
| General-purpose | Configured for how your team works |

---

## Installation

This takes about 10 minutes. You'll do it once.

### Step 1: Choose how to access Claude Code

You have two options. Pick one:

**Option A — Claude Max subscription (recommended for most people)**

Claude Max ($100/month) gives you Claude Code with no usage limits and no API billing. Best if you're using Claude regularly throughout the day.

1. Go to [claude.ai/upgrade](https://claude.ai/upgrade) and subscribe to **Max**
2. Once subscribed, Claude Code is included — no API key needed
3. When you first run `claude`, it will walk you through logging in with your Claude account

**Option B — API key (pay as you go)**

Better if you want to control costs or are already an API customer.

1. Go to [console.anthropic.com](https://console.anthropic.com) and create an account

2. Click **API Keys** in the left sidebar, then **Create Key**

![Anthropic Console — API Keys page](https://developer.puter.com/assets/img/anthropic/api-key-page.webp)

3. Copy the key — it starts with `sk-ant-...`. You won't see it again.

4. Open your terminal and paste (replace with your actual key):
```
export ANTHROPIC_API_KEY=sk-ant-your-key-here
```

To make it stick across sessions:
```
echo 'export ANTHROPIC_API_KEY=sk-ant-your-key-here' >> ~/.zshrc
source ~/.zshrc
```

Never commit this key to GitHub.

### Step 2: Install Claude Code

If you don't have Node.js, install it from [nodejs.org](https://nodejs.org) (LTS version) first. Then open your terminal and run:

```
npm install -g @anthropic/claude-code
```

Check it worked:
```
claude --version
```

### Step 3: Start Claude Code

```
cd claude-code-starter/module-1
claude
```

![Claude Code running in terminal](https://raw.githubusercontent.com/anthropics/claude-code/main/demo.gif)

You're in. Head to [module-1/README.md](module-1/README.md) for your first assignment.

---

## Prompts worth keeping

| What you want | What to type |
|---|---|
| Generate a PRD | `/prd-generator` |
| Write user stories | `/user-story-writer` |
| Find gaps in a spec | `"Review docs/prd.md and tell me what's missing"` |
| Write for execs | `"Rewrite this as 3 bullets for a VP with 10 seconds"` |
| Prep for engineering | `"What questions will engineers ask about this PRD?"` |
| Build a sprint plan | `"Turn the must-have stories into a 2-week sprint plan"` |
| Stress-test a flow | `"What edge cases am I missing here?"` |

---

## Troubleshooting

**"command not found: claude"**
Run `npm install -g @anthropic/claude-code` again. Check Node.js is installed: `node --version`.

**API key error**
Run `export ANTHROPIC_API_KEY=your-key-here`. Make sure you copied the full key including `sk-ant-`.

**Claude isn't reading my CLAUDE.md**
The file must be named exactly `CLAUDE.md` (all caps) in the folder where you ran `claude`.

**Skill not triggering**
Check that the path is `.claude/skills/<name>/SKILL.md` and the `name:` in the frontmatter matches what you typed after `/`.

---

*[Claude Code in Practice](https://maven.com/boring-bot/claude-code-in-practice) · Hamza Farooq · Traversaal.ai*
