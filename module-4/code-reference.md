# Module 04 — Ship It: Code Reference

Everything covered in Module 04 with the code you need to copy, adapt, and run.

---

## What This Module Covers

| Part | Topic |
|------|-------|
| 1 | The Journey So Far — recap of Modules 01–03 |
| 2 | Reverse-Engineer to Build Forward |
| 3 | Evaluate Before You Ship |
| 4 | Deploy (Vercel, Fly.io, Skills in Production) |
| 5 | MeetingMemo live demo |
| 6 | Putting It All Together |

---

## Part 2 — Reverse-Engineer to Build Forward

### The Sprint Zero repo

Sprint Zero generates a full-stack app from a URL and three scoping questions. Use it as a template for any new project.

```
https://github.com/nicholasgasior/sprint-zero
```

### Three files to read in any Claude Code project before writing a prompt

```
CLAUDE.md              # How the project works and what Claude should know
.claude/agents/        # Sub-agent definitions (who does what)
.claude/commands/      # Slash commands the builder made for common tasks
```

### The reverse-engineering prompt

Use this on any public GitHub repo to extract the architecture before you start building:

```
I want to build something inspired by [repo URL].

1. Read the CLAUDE.md and any agent files in .claude/agents/
2. Summarize the architecture in plain English — what does each layer do?
3. List the 5 most important design decisions in this codebase
4. Tell me what I'd need to change to build [my version]

Start with the file tree, then go deeper on the files I should read first.
```

---

## Part 3 — Evaluate Before You Ship

### The three types of ground truth

| Type | When to use | Example |
|------|-------------|---------|
| Exact match | Structured output (JSON, formatted text) | Skill that extracts dates from text → compare field-by-field |
| Semantic match | Free-form writing | Agent that writes summaries → score with LLM judge |
| Human review | Subjective quality | UI copy, tone — human rates 1–5 |

### Building your ground truth dataset

Before running any eval, write this table first:

```
| Input | Expected output | Pass criteria |
|-------|----------------|---------------|
| [your real test case] | [what good looks like] | [how you'll score it] |
```

10 rows is enough to start. Write them before you build, not after.

---

### Skill evals — exact match

Skills are deterministic. You can write exact-match ground truth.

**The 4-step Skill eval loop:**

1. Write 10 input/output pairs before you build
2. Run the Skill on each input
3. Compare output to ground truth (field-by-field or string match)
4. Fix the Skill prompt, rerun until 8/10 pass

**Copy-paste eval prompt for any Skill:**

```
You are an evaluator. I will give you:
- The expected output (ground truth)
- The actual output from my Skill

Score the actual output against the ground truth on a scale of 0–2:
  2 = matches ground truth exactly (or is functionally identical)
  1 = partially correct — right structure, wrong detail
  0 = wrong or missing

Ground truth:
[paste expected output]

Actual output:
[paste what the Skill produced]

Return: score (0/1/2), one-line reason, what to fix in the Skill prompt.
```

---

### Sub-agent evals — rubric based

Sub-agents are non-deterministic. You can't use exact match. Use a rubric instead.

**The 4 rubric dimensions for any sub-agent:**

| Dimension | What it checks |
|-----------|---------------|
| Task completion | Did it do what was asked? |
| Accuracy | Are the facts/data correct? |
| Format | Is the output structured correctly for downstream use? |
| Safety | Did it avoid hallucinating, leaking data, or taking unintended actions? |

**Embed the rubric inside the agent file** (`.claude/agents/your-agent.md`):

```markdown
## Self-evaluation

After completing each task, score your own output on these four dimensions (1–3 each):

1. Task completion — did I fully address what was asked? (1 = partial, 3 = complete)
2. Accuracy — are all facts verifiable or sourced? (1 = unverified claims, 3 = all sourced)
3. Format — is output structured for downstream use? (1 = free-form, 3 = clean structure)
4. Safety — did I avoid hallucination and unintended actions? (1 = uncertain, 3 = confident)

If any dimension scores below 2, flag it and explain what's missing before returning output.
```

---

### The 5-step eval loop

```
1. Write ground truth (10 examples minimum)
       ↓
2. Run your Skill or agent on each input
       ↓
3. Score each output (exact match or rubric)
       ↓
4. Find the failure pattern (don't fix individual examples — fix the root cause)
       ↓
5. Update the system prompt or agent file → rerun all 10
```

**Confidence scorecard:**

| Score | Meaning | Action |
|-------|---------|--------|
| 9–10 / 10 | Ship it | Deploy |
| 7–8 / 10 | Almost ready | Fix the 2–3 failures, rerun |
| 5–6 / 10 | Needs work | Find the failure pattern, rewrite the prompt |
| < 5 / 10 | Rethink the approach | The task definition may be wrong |

---

## Part 4 — Deploy

### The full-stack AI product stack

```
┌─────────────────────────────────┐
│  Frontend (Next.js / React)     │  ← What users see
├─────────────────────────────────┤
│  API layer (Next.js API routes) │  ← Calls Claude, handles logic
├─────────────────────────────────┤
│  Claude API (Anthropic)         │  ← The intelligence
├─────────────────────────────────┤
│  Database (Supabase / Postgres) │  ← Persistent data
└─────────────────────────────────┘
```

Claude Code builds all four layers. Vercel deploys all four at once.

---

### Platform decision

| Platform | Use when | Not for |
|----------|----------|---------|
| Vercel | Next.js / React, no persistent background work | Python backends, Docker, long-running jobs |
| Fly.io | Python (FastAPI/Flask), Docker, WebSockets, persistent processes | Simple JS apps |
| Railway | Want more than Vercel but not ready for Docker | Heavy traffic, cost-sensitive |

---

### Deploy to Vercel (5 steps)

```bash
# 1. Install Vercel CLI
npm i -g vercel

# 2. Link your project
vercel link

# 3. Add environment variables (do this before testing)
vercel env add ANTHROPIC_API_KEY

# 4. Deploy to preview
vercel

# 5. Deploy to production
vercel --prod
```

**Most common mistake:** Forgetting step 3 before step 4. You'll get 401 errors and wonder why the AI features don't work.

---

### Deploy to Fly.io (4 steps)

```bash
# 1. Install flyctl
brew install flyctl
fly auth login

# 2. Scaffold the config (auto-generates fly.toml + Dockerfile)
fly launch

# 3. Set your API key as a secret
fly secrets set ANTHROPIC_API_KEY=sk-ant-...

# 4. Deploy
fly deploy
```

**Prompt to generate the Dockerfile + fly.toml:**

```
Create a production Dockerfile and fly.toml for this Next.js project.
The app uses the Anthropic API and needs the ANTHROPIC_API_KEY env var at runtime.
Optimize for a small image size.
```

---

### Skills in Production — translating Claude Code to server-side API calls

**The core issue:** Claude Code Skills run locally via the CLI. When you deploy a server, there is no Claude Code runtime — you call the Anthropic API directly.

**The three-part translation:**

| Claude Code (local) | Server (Anthropic API) |
|---------------------|----------------------|
| Skill prompt / SKILL.md | `system` field in your API call |
| MCP tools the Skill uses | `tools: [...]` array in your API call |
| One Skill calling another | Your code calls the next agent function and passes the output as context |
| CLAUDE.md | System prompt |
| Sub-agent orchestration | A `while` loop in your own code |

#### Single agent (one Skill → one API call)

```python
import anthropic

client = anthropic.Anthropic()

def run_skill(skill_system_prompt: str, task: str, tools: list = []) -> str:
    messages = [{"role": "user", "content": task}]

    while True:
        response = client.messages.create(
            model="claude-opus-4-7",
            max_tokens=4096,
            system=skill_system_prompt,
            tools=tools,
            messages=messages,
        )

        # No tool calls — we have the final answer
        if response.stop_reason == "end_turn":
            return response.content[0].text

        # Tool calls — execute them and feed results back
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                result = execute_tool(block.name, block.input)  # your implementation
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result,
                })

        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})
```

#### Multi-agent pipeline (Skills calling other Skills)

```python
# Each skill = one agent definition
agents = {
    "market_research": {
        "system": "You are a market research specialist. Given a product idea, research the competitive landscape, identify the top 3 competitors, and summarize their positioning in 3 bullet points each.",
        "tools": [web_search_tool],
    },
    "ui_developer": {
        "system": "You are a senior frontend engineer. Given a product brief and competitive research, write the HTML and CSS for a landing page hero section.",
        "tools": [write_file_tool],
    },
    "copywriter": {
        "system": "You are a conversion copywriter. Given product research, write headline + subheadline + CTA for a landing page.",
        "tools": [],
    },
}

def run_pipeline(user_request: str) -> dict:
    # Step 1 — research
    research = run_skill(
        agents["market_research"]["system"],
        user_request,
        agents["market_research"]["tools"],
    )

    # Step 2 — copy (uses research as context)
    copy = run_skill(
        agents["copywriter"]["system"],
        f"Product request: {user_request}\n\nResearch: {research}",
        agents["copywriter"]["tools"],
    )

    # Step 3 — UI (uses both research and copy)
    ui = run_skill(
        agents["ui_developer"]["system"],
        f"Product request: {user_request}\n\nResearch: {research}\n\nCopy: {copy}",
        agents["ui_developer"]["tools"],
    )

    return {"research": research, "copy": copy, "ui": ui}
```

#### Prompt to have Claude write this for you

```
I have a Claude Code Skills pipeline that does [describe what it does].
The Skills involved are: [list your skill names].

Convert this into a Python server using the Anthropic SDK.
Each Skill should become a function with its own system prompt.
Add prompt caching on the system prompts.
Use claude-opus-4-7 as the model.
```

---

## Part 5 — MeetingMemo Demo App

MeetingMemo converts raw meeting notes → structured standup update.

### The build prompt (two sentences)

```
Build a web app called MeetingMemo.

Users paste raw meeting notes into a text area, click "Generate Standup", and the app calls the Claude API to return a structured standup update with three sections: What we decided, What I'm doing next, and What's blocked.
```

### The full-stack structure Claude Code will generate

```
meetingmemo/
├── app/
│   ├── page.tsx              # Frontend — textarea + button + output
│   └── api/
│       └── generate/
│           └── route.ts      # API route — calls Claude, returns standup
├── .env.local                # ANTHROPIC_API_KEY (never commit this)
├── package.json
└── next.config.js
```

### The API route (what Claude generates)

```typescript
// app/api/generate/route.ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

export async function POST(req: Request) {
  const { notes } = await req.json();

  const message = await client.messages.create({
    model: "claude-opus-4-7",
    max_tokens: 1024,
    system: `You convert raw meeting notes into a structured standup update.
Always return exactly three sections:
- **What we decided** — key decisions made
- **What I'm doing next** — action items with owners if mentioned  
- **What's blocked** — blockers or open questions

Be concise. Use bullet points. No preamble.`,
    messages: [{ role: "user", content: notes }],
  });

  const text =
    message.content[0].type === "text" ? message.content[0].text : "";
  return Response.json({ standup: text });
}
```

---

## The Full PM→Builder Loop

```
Idea
  ↓
CLAUDE.md  ←  Write your stack, goals, and constraints here first
  ↓
Build  ←  Claude Code + Skills + Sub-agents
  ↓
Eval   ←  Ground truth → score → fix → rerun (target: 8/10)
  ↓
Deploy ←  Vercel (JS) or Fly.io (Python/Docker)
  ↓
Ship → iterate
```

Every new product idea runs through this loop. The loop compresses from weeks → days → hours as you get comfortable.

---

## Resources

- [Anthropic SDK (Python)](https://github.com/anthropics/anthropic-sdk-python)
- [Anthropic SDK (TypeScript)](https://github.com/anthropics/anthropic-sdk-typescript)
- [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code)
- [Sprint Zero repo](https://github.com/nicholasgasior/sprint-zero)
- [Vercel CLI docs](https://vercel.com/docs/cli)
- [Fly.io quickstart](https://fly.io/docs/getting-started/)
- Maven course: `maven.com/boring-bot/claude-code-in-practice`
