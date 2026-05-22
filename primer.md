# Course Primer — Claude Code in Practice

## What this course is

Claude Code in Practice teaches product managers to ship real products using Claude Code — without waiting on engineering, without writing code from scratch, and without switching between a dozen tools.

Each module is one session. By the end you've built something real.

Instructor: Hamza Farooq, Traversaal.ai (ex-Google, UCLA Anderson)
Platform: [Maven](https://maven.com/boring-bot/claude-code-in-practice)

---

## How the repo works

This repo is the single source of truth for all course materials. Everything is organized by type — not by module. When you run `claude` from the repo root, Claude reads `CLAUDE.md` automatically.

```
clone the repo → run claude from root → explore skills, agents, and demos
```

**Three things to know:**
- **Skills** → `.claude/skills/` — trigger with `/skill-name`
- **Agents** → `.claude/agents/` — Claude delegates automatically
- **Demos** → `demos/` — runnable apps built in class

---

## What's covered

### Skills
Run `/prd-generator`, `/user-story-writer`, `/sprint-planner`, `/competitor-research`, and 30+ more PM-focused skills — all in `.claude/skills/`.

### Sub-Agents
Specialist agents Claude delegates to automatically: `research-agent`, `prd-reviewer`, `code-reviewer`, `data-analyst`, `copy-writer`, `deck-builder` — all in `.claude/agents/`.

### Demo Apps
Working apps built live in class — in `demos/`. Includes `meeting-notes-summarizer`, `meetingmemo`, `skill-sub-multi-agent`, `research-agent`, `research-frontend`, and more.

---

*(Content grows as the course runs. Check back after each cohort.)*

---

## Core concepts

### CLAUDE.md
A plain text file Claude reads at the start of every session. It tells Claude who you are, what your project is, and how you want to work. Without it, Claude treats every session the same. Think of it as a one-time briefing you write once and update as your project evolves.

### Skills
Reusable instruction sets stored in `.claude/skills/<name>/SKILL.md`. You trigger them with `/skill-name`. Instead of typing the same long prompt every session, you type one word. Skills are editable — open the file and change how Claude responds.

### Memory
This repo uses a `memory.md` file to track key decisions, module status, and anything that isn't obvious from the code. Claude reads it to stay up to date across sessions.

---

## Apps built in class

Live demos shipped during course sessions. Fork them, break them, learn from them.

| App | What it does | Repo |
|-----|-------------|------|
| word-humanizer | Rewrites AI text to sound human | [github.com/hamzafarooq/word-humanizer](https://github.com/hamzafarooq/word-humanizer/) |
| seo-writer | Generates SEO blog content | [github.com/hamzafarooq/seo-writer](https://github.com/hamzafarooq/seo-writer) |

---

## Useful prompts

| Goal | Prompt |
|------|--------|
| Generate a PRD | `/prd-generator` |
| Write user stories | `/user-story-writer` |
| Find gaps in a spec | `Review docs/prd.md and tell me what's missing` |
| Prep for engineering | `What questions will engineers ask about this PRD?` |
| Write for execs | `Rewrite this as 3 bullets for a VP with 10 seconds` |
| Build a sprint plan | `Turn the must-have stories into a 2-week sprint plan` |
| Stress-test a flow | `What edge cases am I missing here?` |

---

## Version history

| Tag | What it marks |
|-----|--------------|
| `v1.0` | Module 1 complete |

To restore any version: `git checkout v1.0`
To see all tags: `git tag`
