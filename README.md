# Claude Code in Practice

A course for product managers who want to ship real things without waiting on engineering.
[Enroll on Maven](https://maven.com/boring-bot/claude-code-in-practice)

Taught by Hamza Farooq, Founder at Traversaal.ai, UCLA Anderson, ex-Google.

---

## Get started

```bash
git clone https://github.com/hamzafarooq/claude-code-starter.git
cd claude-code-starter/module-1
```

Open [module-1/README.md](module-1/README.md) and follow the setup guide from there.

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
- [module-1/CLAUDE.md](module-1/CLAUDE.md) - starter template
- [module-1/.claude/skills/](module-1/.claude/skills/prd-generator/SKILL.md)

---

## Built with Claude Code

Apps built live in class. Fork them, break them, learn from them.

| Repo | What it does |
|------|-------------|
| [word-humanizer](https://github.com/hamzafarooq/word-humanizer/) | Rewrites AI-generated text to sound human |
| [seo-writer](https://github.com/hamzafarooq/seo-writer) | Generates SEO-optimized blog content |

More get added as the course runs.

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

Open your terminal and run:
```
npm install -g @anthropic/claude-code
```

No `npm`? Install Node.js from [nodejs.org](https://nodejs.org) (LTS version), then try again.

Check it worked:
```
claude --version
```

### API key setup

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Create an account, go to API Keys, create a key
3. Copy it (starts with `sk-ant-...`)

```
export ANTHROPIC_API_KEY=sk-ant-your-key-here
```

To make it stick across sessions:
```
echo 'export ANTHROPIC_API_KEY=sk-ant-your-key-here' >> ~/.zshrc
source ~/.zshrc
```

Don't commit this key to GitHub.

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
