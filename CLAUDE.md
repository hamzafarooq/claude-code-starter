# Claude Code in Practice — Course Repo

## Who I am

- Yousuf, student of Claude Code in Practice for PM course
- Background: Solution Architect, Engineeing Practices Lead
- I am following course materials for PMs learning Claude Code
- I'm comfortable with APIs, backend and big picture thinking, not so deep on frontend

## What this repo is

Course materials for "Claude Code in Practice" (taught on Maven) — a course that teaches product managers to ship real things using Claude Code without relying on engineering.

- Current phase: Active (live cohorts running)
- Audience: Product managers with no coding background
- Maven course: https://maven.com/boring-bot/claude-code-in-practice

## Repo structure

```
/
├── CLAUDE.md               ← you are here (root context for Claude)
├── README.md               ← student-facing setup guide
├── primer.md               ← course overview and navigation guide
├── memory.md               ← persistent decisions and module status log
├── .gitignore
└── module-1/
    ├── README.md           ← assignment guide for Module 1
    ├── CLAUDE-template.md  ← starter CLAUDE.md template for students
    ├── prd-generator/      ← live demo app built in class
    └── .claude/
        └── skills/
            ├── prd-generator/SKILL.md
            └── user-story-writer/SKILL.md
```

## Conventions

- One folder per module: `module-1/`, `module-2/`, etc.
- Each module has its own `README.md` (student assignment guide) and `CLAUDE-template.md`
- Skills live in `module-N/.claude/skills/<name>/SKILL.md`
- Apps built live in class get their own GitHub repos (linked from root README)
- Version tags follow the pattern `v1.0`, `v2.0` per module completion
- `course-modules/` is gitignored (slide decks and raw HTML exports)

## How Claude should respond

- Be concise — I don't need long explanations
- When editing course content, match the tone of the existing files: plain English, instructional, PM-friendly
- When I ask you to write something, write it directly
- Flag anything that would confuse a non-technical student
- If something is unclear, ask rather than assume

## What I use Claude Code for in this repo

- Draft and update module README files and assignment guides
- Write and refine skill files (SKILL.md)
- Maintain the root README (setup guide, module list, app table)
- Update memory.md after key decisions or module completions
- Tag releases and manage version history
