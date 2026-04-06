# Course Primer — Claude Code in Practice

## What this course is

Claude Code in Practice teaches product managers to ship real products using Claude Code — without waiting on engineering, without writing code from scratch, and without switching between a dozen tools.

Each module is one session. By the end you've built something real.

Instructor: Hamza Farooq, Traversaal.ai (ex-Google, UCLA Anderson)
Platform: [Maven](https://maven.com/boring-bot/claude-code-in-practice)

---

## How the repo works

This repo is the single source of truth for all course materials. Each module lives in its own folder. When you're in a module folder and run `claude`, Claude reads the `CLAUDE.md` and `README.md` automatically and knows what you're working on.

```
clone the repo → cd into a module folder → run claude → follow the README
```

---

## Modules

### Module 1: From idea to shipped product
**What you'll do:** Set up Claude Code, write a `CLAUDE.md` for your project, install two skills, and take an idea from concept to working MVP.

**Key skills installed:**
- `/prd-generator` — generates a full PRD from a short description
- `/user-story-writer` — turns rough ideas into user stories with acceptance criteria

**Folder:** [module-1/](module-1/)
**Status:** Complete (tagged `v1.0`)

---

*(More modules added as the course runs. Check back after each cohort.)*

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
