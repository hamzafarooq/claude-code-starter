# Module 4: Ship It — Evaluate, Deploy, and Own the Full Loop

Course: [Claude Code in Practice](https://maven.com/boring-bot/claude-code-in-practice)
Instructor: Hamza Farooq, Traversaal.ai

---

## Before you start

You need Claude Code installed and the agents from Module 3 in place. If you haven't done Module 3 yet, do that first — you'll use your `research-agent` in Assignment 4c.

This module is the payoff. You'll write evals for what you built, deploy it to a live URL, and understand how to take your Claude Code skills into a production server environment.

---

## What's in this folder

```
module-4/
├── README.md                          ← you are here (assignment guide)
├── CLAUDE-template.md                 ← starter CLAUDE.md for a deploy-ready project
├── code-reference.md                  ← all code from the slides in one place
├── .claude/
│   └── skills/
│       ├── skill-evaluator/
│       │   └── SKILL.md              ← Assignment 4a: eval any Skill
│       └── deploy-checklist/
│           └── SKILL.md              ← Assignment 4b: pre-deploy checklist
└── meetingmemo/
    ├── README.md                      ← demo app from class
    ├── app/
    │   ├── page.tsx                   ← frontend (textarea + output)
    │   └── api/generate/route.ts      ← Claude API call
    └── package.json
```

Mac tip: folders starting with `.` are hidden by default. Press `Cmd + Shift + .` in Finder to show them, or open the folder in VS Code.

---

## Assignment 4a: Write evals for your Skill

Before you ship anything, you need to know it works. Evals are how you know.

### The concept

A Skill is deterministic — given the same input, it should always produce the same structure. That means you can write exact-match ground truth: "given this input, the output must look like this."

The eval loop is:
1. Write 10 input/output pairs (ground truth)
2. Run your Skill on each input
3. Score actual vs expected
4. Fix the Skill prompt, rerun
5. Repeat until 8/10 pass

### Install the skill-evaluator

The `/skill-evaluator` skill is in this folder at `.claude/skills/skill-evaluator/SKILL.md`. Copy the whole `.claude/` folder into your project folder, then test it:

```
/skill-evaluator
```

When prompted, paste in:
- Your Skill's system prompt (from its SKILL.md)
- One input you want to test
- The output you expected

The evaluator will score it 0–2 and tell you what to fix in the prompt.

### Build your ground truth table

Before running evals, write this in a file called `docs/eval-ground-truth.md`:

```markdown
| Input | Expected output | Pass criteria |
|-------|----------------|---------------|
| [real test case 1] | [what good looks like] | [how you'll score it] |
| [real test case 2] | [what good looks like] | [how you'll score it] |
```

Fill in at least 10 rows. Use real inputs from your work, not made-up examples. The quality of your ground truth determines the quality of your eval.

Then run:

```
/skill-evaluator

Evaluate my /prd-generator skill using the ground truth in docs/eval-ground-truth.md.
Run each input through the skill, score the output, and give me a final pass/fail count.
```

### What an 8/10 confidence score means

| Score | Action |
|-------|--------|
| 9–10 / 10 | Ship it |
| 7–8 / 10 | Fix the 2–3 failures, rerun |
| 5–6 / 10 | Find the failure pattern, rewrite the prompt |
| < 5 / 10 | Rethink the task definition |

---

## Assignment 4b: Deploy to Vercel

Get your product to a live URL. That's the only homework that counts.

### What to deploy

Take the app you built in Module 3 (or build MeetingMemo — see the `/meetingmemo` folder in this repo). The steps below work for any Next.js app.

### Deploy in 5 steps

```bash
# 1. Install Vercel CLI
npm i -g vercel

# 2. Link your project (run inside your project folder)
vercel link

# 3. Add your API key — do this BEFORE testing, or you'll get 401 errors
vercel env add ANTHROPIC_API_KEY

# 4. Preview deploy
vercel

# 5. Production deploy
vercel --prod
```

### Install the deploy-checklist skill

```
/deploy-checklist
```

Run this before every deploy. It catches the five things that break most first deploys.

### If you're using Python (FastAPI, Flask, Django)

Use Fly.io instead of Vercel — Vercel only runs Node/Next.js.

```bash
# 1. Install flyctl
brew install flyctl
fly auth login

# 2. Scaffold config (auto-generates fly.toml + Dockerfile)
fly launch

# 3. Set your API key
fly secrets set ANTHROPIC_API_KEY=sk-ant-...

# 4. Deploy
fly deploy
```

Ask Claude to write the Dockerfile and fly.toml for you:

```
Create a production Dockerfile and fly.toml for this [Python/FastAPI] project.
The app needs ANTHROPIC_API_KEY at runtime. Optimize for a small image size.
```

---

## Assignment 4c: Skills in Production

This is the question that comes up every cohort: *"I built a Skills pipeline in Claude Code — how do I run it on a server?"*

### The core concept

Claude Code doesn't run on your server. The intelligence runs on Anthropic's API. Claude Code is your local IDE — when you deploy, you call the same Anthropic API directly from your own code.

**The translation:**

| Claude Code (local) | Your server (Anthropic API) |
|---------------------|----------------------------|
| Skill prompt in SKILL.md | `system` field in your API call |
| MCP tools the Skill uses | `tools: [...]` array in your API call |
| One Skill calling another | Your code calls the next function, passes output as context |
| CLAUDE.md | System prompt |
| Sub-agent orchestration | A while loop in your own code |

### Convert a single Skill

```python
import anthropic

client = anthropic.Anthropic()

def run_skill(system_prompt: str, task: str, tools: list = []) -> str:
    messages = [{"role": "user", "content": task}]

    while True:
        response = client.messages.create(
            model="claude-opus-4-7",
            max_tokens=4096,
            system=system_prompt,
            tools=tools,
            messages=messages,
        )

        if response.stop_reason == "end_turn":
            return response.content[0].text

        # Handle tool calls
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                result = execute_tool(block.name, block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result,
                })

        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})
```

### Multi-skill pipeline (Skills calling Skills)

```python
# Define each skill as an agent
agents = {
    "market_research": {
        "system": "You are a market research specialist. Research the competitive landscape for the given product and return the top 3 competitors with their positioning in 3 bullets each.",
        "tools": [],  # add web_search_tool if you need live search
    },
    "copywriter": {
        "system": "You are a conversion copywriter. Given product research, write a headline, subheadline, and CTA for a landing page.",
        "tools": [],
    },
}

def run_pipeline(user_request: str) -> dict:
    # Step 1: research
    research = run_skill(
        agents["market_research"]["system"],
        user_request,
        agents["market_research"]["tools"],
    )

    # Step 2: copy — receives research as context
    copy = run_skill(
        agents["copywriter"]["system"],
        f"Product: {user_request}\n\nResearch: {research}",
        agents["copywriter"]["tools"],
    )

    return {"research": research, "copy": copy}
```

### Prompt to have Claude write this for you

```
I have a Claude Code Skills pipeline that does [describe what it does].
The skills involved are: [list your skill names and what each does].

Convert this into a Python API using the Anthropic SDK.
Each skill should become a function with its own system prompt.
Add prompt caching on the system prompts using cache_control.
Use claude-opus-4-7 as the default model.
Return a working FastAPI app with a single POST endpoint.
```

---

## The MeetingMemo Demo App

MeetingMemo was built live in class in 30 minutes. It converts raw meeting notes into a structured standup update.

The full app is in the `meetingmemo/` folder. Open it and run:

```bash
cd meetingmemo
npm install
# add ANTHROPIC_API_KEY to .env.local
npm run dev
```

Then open `http://localhost:3000`, paste in some meeting notes, and click Generate.

Study the code in `app/api/generate/route.ts` — this is the simplest possible example of a Claude API call in a Next.js app. Every AI feature you build will follow this same pattern.

---

## Prompts worth saving

| What you want | What to type |
|---|---|
| Eval a Skill | `/skill-evaluator` |
| Pre-deploy check | `/deploy-checklist` |
| Deploy to Vercel | `npm i -g vercel && vercel --prod` |
| Write a Dockerfile | `"Create a production Dockerfile and fly.toml for this project"` |
| Convert a Skill to API code | `"Convert my /skill-name Skill into a Python function using the Anthropic SDK"` |
| Convert a full pipeline | `"Convert this Claude Code Skills pipeline into a FastAPI app"` |
| Debug a 401 error | `"My Vercel app is returning 401 — check that ANTHROPIC_API_KEY is set in env vars"` |

---

## Troubleshooting

**Vercel deploy returns 401 on the AI routes**
You forgot to add the env var before deploying. Run `vercel env add ANTHROPIC_API_KEY` then `vercel --prod` again.

**"fly: command not found"**
Run `brew install flyctl` first. If you don't have Homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

**My eval scores are all 0**
The ground truth is probably too strict. Rewrite the "pass criteria" column to check structure and key fields rather than exact string match.

**The Skill-to-API conversion isn't handling tool calls**
Make sure your `run_skill` function loops until `stop_reason == "end_turn"`. A single API call won't work if the model needs to call a tool mid-response.

**Claude isn't picking up my system prompt in the API**
Pass it in the `system` parameter, not in the `messages` array. The system field is separate in the Anthropic SDK.

---

*[Claude Code in Practice](https://maven.com/boring-bot/claude-code-in-practice) · Hamza Farooq · Traversaal.ai*
