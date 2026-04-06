# Module 1: From idea to shipped product

Course: [Claude Code in Practice](https://maven.com/boring-bot/claude-code-in-practice)
Instructor: Hamza Farooq, Traversaal.ai

---

## Setup

### Clone the repo

```bash
git clone https://github.com/hamzafarooq/claude-code-starter.git
cd claude-code-starter/module-1
```

### Install Claude Code

```bash
npm install -g @anthropic/claude-code
```

No Node.js? Download the LTS version from [nodejs.org](https://nodejs.org), then run the command above.

Check it worked:
```bash
claude --version
```

### Set up your API key

1. Go to [console.anthropic.com](https://console.anthropic.com), create an account
2. Go to API Keys and create a new key
3. Copy it (starts with `sk-ant-...`)

```bash
export ANTHROPIC_API_KEY=sk-ant-your-key-here
```

To make it permanent:
```bash
echo 'export ANTHROPIC_API_KEY=sk-ant-your-key-here' >> ~/.zshrc
source ~/.zshrc
```

Don't commit this key to GitHub.

### Start Claude Code

From inside the `module-1` folder:
```bash
claude
```

You're ready. Work through the three assignments below.

---

## Assignment 1: Set up your CLAUDE.md

`CLAUDE.md` is a plain text file Claude reads at the start of every session. It tells Claude who you are, what your project is, and how to work with you. Without it, Claude treats every project the same. With it, you stop repeating yourself.

Write it once, improve it over time.

### What to put in it

A good `CLAUDE.md` answers four questions:
1. Who are you? Your role, what you care about, what you don't need explained
2. What's the project? One sentence, current stage, key stakeholders
3. How should Claude respond? Tone, length, format
4. What are your conventions? Where files live, how you write user stories, required PRD sections

### How to create it

Open Claude Code in this folder and type:

```
I'm a product manager. Help me create a CLAUDE.md file for my project. Ask me the questions you need to write a good one.
```

Claude will ask a few questions and generate the file. A starter template is also in this folder at [CLAUDE.md](CLAUDE.md) if you'd rather edit directly.

### Check that it's working

Start a new session and ask:

```
What do you know about this project based on what you've read?
```

Claude should describe your project and role accurately. If it doesn't, open `CLAUDE.md` and fill in the blank sections.

---

## Assignment 2: Install your skills

Skills are reusable instructions stored in `.claude/skills/`. You trigger them with a `/skill-name` command. Instead of typing the same long prompt every session, you type one word.

Two skills are already in this folder:
- `/prd-generator` - generates a structured PRD from a brief description
- `/user-story-writer` - converts rough feature ideas into user stories with acceptance criteria

### What to do

Test the PRD generator:
```
/prd-generator
```
Give it a real feature idea, something your team is actually working on.

Test the user story writer:
```
/user-story-writer
```
Describe the same feature informally and see how Claude structures it.

Then open [.claude/skills/prd-generator/SKILL.md](.claude/skills/prd-generator/SKILL.md) and read it. This is exactly what Claude follows when you run the command. You can edit it to match your team's format.

### Where the files live

```
module-1/
├── CLAUDE.md
└── .claude/
    └── skills/
        ├── prd-generator/
        │   └── SKILL.md
        └── user-story-writer/
            └── SKILL.md
```

Mac tip: folders starting with `.` are hidden by default. Press `Cmd + Shift + .` in Finder to show them.

---

## Assignment 3: From idea to PRD to MVP

Take a real product idea through the full workflow: rough concept to structured PRD to working prototype.

### Part A: Pick your idea

Choose something small enough to ship in a week. It should be a real problem, not a made-up exercise. Examples from class:
- A tool that rewrites AI-generated text to sound more human
- An SEO content generator for blog posts
- A converter that turns meeting notes into Jira tickets

### Part B: Generate the PRD

Run `/prd-generator` and answer the questions for your idea.

When Claude finishes, ask:
```
Save this PRD to docs/prd.md
```

Then ask:
```
What are the three riskiest assumptions in this PRD?
```

### Part C: Break it into stories

Run `/user-story-writer` with the must-have features from your PRD.

Ask Claude to prioritize:
```
Which of these stories should be in the first sprint?
```

### Part D: Build the MVP

Tell Claude what you want:
```
Based on this PRD, help me build the simplest version of this product. Ask me what tools and constraints I'm working with.
```

Claude will ask a few clarifying questions, then start building with you. You don't need to write any code.

### What to share

Post in the course Slack channel:
1. Your `docs/prd.md`
2. The working MVP (a URL, file, or screenshot)

---

## Prompts worth saving

| What you want | What to type |
|---|---|
| Generate a PRD | `/prd-generator` |
| Write user stories | `/user-story-writer` |
| Find gaps in a spec | `"Review docs/prd.md and tell me what's missing"` |
| Prep for engineering | `"What questions will engineers ask about this PRD?"` |
| Build a sprint plan | `"Turn the must-have stories into a 2-week sprint plan"` |
| Write for execs | `"Rewrite this as 3 bullets for a VP with 10 seconds"` |
| Stress-test a flow | `"What edge cases am I missing here?"` |

---

## Troubleshooting

**"command not found: claude"**
Run `npm install -g @anthropic/claude-code` again. Check Node.js is installed: `node --version`.

**Claude isn't reading my CLAUDE.md**
The file must be named exactly `CLAUDE.md` (all caps) in the same folder where you ran `claude`.

**Skill not triggering**
Check that the path is `.claude/skills/<name>/SKILL.md` and the `name:` in the frontmatter matches what you typed after `/`.

**Responses are too long**
Add this to your CLAUDE.md: `Keep all responses under 200 words unless I ask for more.`

---

*[Claude Code in Practice](https://maven.com/boring-bot/claude-code-in-practice) · Hamza Farooq · Traversaal.ai*
