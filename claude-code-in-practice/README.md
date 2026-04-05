# Claude Code in Practice

**A hands-on course for product managers and builders.**
[Enroll on Maven →](https://maven.com/boring-bot/claude-code-in-practice)

Taught by **Hamza Farooq** — Founder at Traversaal.ai · UCLA Anderson · ex-Google

---

## What this repo is

This is the **official central repository** for [Claude Code in Practice](https://maven.com/boring-bot/claude-code-in-practice). All course code, templates, and resources live here. If you're a student, bookmark this page — come back here first whenever you need code from class.

Each module has its own folder or linked repo. Start here, then follow the links for each session.

---

## Course Modules

### Module 1 — From Idea to Shipped Product

Set up Claude Code, configure your workspace, and go from blank page to a full PRD without writing code.

**What you'll build:**
- Your `CLAUDE.md` — a standing briefing that makes Claude context-aware for your project
- Your first skills: `/prd-generator` and `/user-story-writer`
- A live PRD builder app that runs in your browser

**Resources in this repo:**
- [CLAUDE.md](CLAUDE.md) — template to customize for your project
- [prd-generator/index.html](prd-generator/index.html) — open in browser, no install needed
- [.claude/skills/prd-generator/](.claude/skills/prd-generator/SKILL.md) — PRD generator skill
- [.claude/skills/user-story-writer/](.claude/skills/user-story-writer/SKILL.md) — user story skill

**Assignment 1:**
1. Follow the [Quick Start](#quick-start) below to set up your `CLAUDE.md`
2. Open [prd-generator/index.html](prd-generator/index.html) in your browser and generate a PRD for a product idea of your own

**Code examples from class:**

See [Built with Claude Code](#built-with-claude-code) below for all repos showcased in this course.

---

## Built with Claude Code

These are real apps built using Claude Code — demoed live in class and available for you to explore, fork, and learn from.

| Repo | What it does | Built with |
|------|-------------|------------|
| [word-humanizer](https://github.com/hamzafarooq/word-humanizer/) | Rewrites AI-sounding text to sound human | Claude Code |
| [seo-writer](https://github.com/hamzafarooq/seo-writer) | SEO-optimized content generator | Claude Code |

> More repos will be added here as the course progresses.

---

## Quick Start

**1. Set up your workspace:**

Open Claude Code in this folder and run:
```
I'm a product manager. Help me create a CLAUDE.md file for my project. Ask me the questions you need to write a good one.
```

**2. Install your skills:**

Your skills are already in `.claude/skills/`. Test them:
```
/prd-generator
```
```
/user-story-writer
```

**3. Try the PRD builder app:**

Open [prd-generator/index.html](prd-generator/index.html) in your browser. Add your Anthropic API key (top right) and generate a full PRD from a form.

---

## Useful Prompts for PMs

| What you want | What to type |
|---|---|
| Generate a full PRD | `/prd-generator` |
| Write user stories | `/user-story-writer` |
| Find gaps in a spec | `"Review docs/prd.md and tell me what's missing"` |
| Write for execs | `"Rewrite this as 3 bullets for a VP with 10 seconds"` |
| Prep for engineering | `"What questions will engineers ask about this PRD?"` |
| Create a sprint plan | `"Turn the must-have stories into a 2-week sprint plan"` |
| Check for edge cases | `"What edge cases am I missing in this flow?"` |

---

## Troubleshooting

**Claude isn't reading my CLAUDE.md**
The file must be named exactly `CLAUDE.md` (all caps) and live in the folder where you ran `claude`.

**Skill not triggering**
Check that the path is `.claude/skills/<name>/SKILL.md` and the frontmatter `name:` matches what you typed after `/`.

**Claude responses are too long**
Add to your CLAUDE.md: `"Keep all responses under 200 words unless I ask for more."`

---

*[Claude Code in Practice](https://maven.com/boring-bot/claude-code-in-practice) · Taught by Hamza Farooq · Traversaal.ai*
