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
├── .claude/                ← Claude Code config (skills, commands, agents)
│   ├── skills/             ← all skill SKILL.md files (flat, one folder per skill)
│   ├── commands/           ← all slash command .md files
│   └── agents/             ← all sub-agent .md files
├── demos/                  ← all runnable demo apps
│   ├── meeting-notes-summarizer/
│   ├── prd-generator/
│   ├── youtube-demo/
│   ├── meetingmemo/
│   ├── skill-sub-multi-agent/
│   ├── research-agent/
│   ├── research-frontend/
│   ├── ai-agent-workshop/
│   └── royal-pop-website/
├── docs/                   ← reference resources
├── images/                 ← screenshots and GIFs
└── bin/                    ← npx installer CLI
```

## Conventions

- Flat by type: skills in `.claude/skills/`, agents in `.claude/agents/`, demos in `demos/`
- No module folders — content is organized by what it is, not which session it came from
- All skills and commands live at root `.claude/` — no module-scoped subdirectories
- Apps built live in class get their own GitHub repos (linked from root README)
- Version tags follow the pattern `v1.0`, `v2.0` per release

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
