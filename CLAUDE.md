# Claude Code in Practice — Course Repo

## What this repo is

Course materials for **Claude Code in Practice** (taught on Maven) — a hands-on course that teaches product managers to ship real things using Claude Code without relying on engineering.

- Audience: Product managers and non-engineers learning to build with Claude Code
- Status: Active (live cohorts running)
- Instructor: Hamza Farooq (Traversaal.ai, UCLA Anderson, ex-Google)
- Co-instructor: Aishwarya Ashok
- Maven course: https://maven.com/boring-bot/claude-code-in-practice

## Repo structure

```
/
├── CLAUDE.md               ← root context for Claude
├── README.md               ← student-facing setup guide
├── primer.md               ← course overview and navigation guide
├── memory.md               ← decisions and module status log
├── LICENSE                 ← MIT
├── .claude/                ← shared skills, commands, agents (all modules)
│   ├── skills/
│   ├── commands/
│   └── agents/
├── module-1/               ← PRDs, user stories, first app
├── module-2/               ← Web app demo, repo & video research commands
├── module-3/               ← (in progress)
├── module-4/               ← MeetingMemo app, code reference
└── ai-agent-workshop/      ← Capstone-style competitor research module
```

## Conventions

- One folder per module: `module-1/`, `module-2/`, etc.
- Each module has its own `README.md` (assignment guide) and `CLAUDE-template.md` (starter context for students)
- Module-scoped skills/commands live in `module-N/.claude/skills/` and `module-N/.claude/commands/`
- Repo-wide skills/commands/agents live in `/.claude/`
- Apps built live in class get their own GitHub repos (linked from root README)
- Version tags follow the pattern `v1.0`, `v2.0` per module completion

## How Claude should respond in this repo

- Be concise — short answers, no long preambles
- Match the tone of existing course content: plain English, instructional, PM-friendly
- When asked to write something, write it directly
- Flag anything that would confuse a non-technical student
- If something is unclear, ask rather than assume

## What Claude is used for here

- Drafting and updating module README files and assignment guides
- Writing and refining skill files (`SKILL.md`)
- Maintaining the root README (setup guide, module list, app table)
- Updating `memory.md` after key decisions or module completions
- Tagging releases and managing version history
