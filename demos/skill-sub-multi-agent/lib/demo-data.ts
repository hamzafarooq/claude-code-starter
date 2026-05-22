// Coordinates are within the 720×440 fixed canvas — see SimulationView.tsx.
// NODE_W = 170, NODE_H = 78

export type AgentStatus = 'idle' | 'thinking' | 'done';

export interface AgentDef {
  id: string;
  name: string;
  role: 'human' | 'single' | 'main' | 'sub' | 'orch' | 'merge';
  x: number;
  y: number;
  sublabel?: string;
  brief: string;
  detail?: string;
}

export interface Connection {
  from: string;
  to: string;
}

export interface SimStep {
  agentId: string;
  status: 'thinking' | 'done';
  output?: string;
  delay: number;
}

export interface LevelDef {
  id: number;
  name: string;
  tagline: string;
  description: string;
  analogy: string;
  explanation: string;
  code: string;
  agents: AgentDef[];
  connections: Connection[];
  steps: SimStep[];
}

export const LEVELS: LevelDef[] = [
  /* ──────────────────────────── LEVEL 1 ──────────────────────────── */
  {
    id: 1,
    name: 'Single Skill',
    tagline: 'A skill is a reusable prompt',
    description:
      'A skill is a reusable prompt — a named, repeatable instruction you save once and invoke by name. One developer handles the entire website: design, frontend, backend, and deployment. One prompt, one answer.',
    analogy: 'Like hiring one developer and asking them to be the designer, frontend engineer, backend engineer, and QA — all at once.',
    explanation:
      'A skill is nothing more than a reusable prompt. No tools, no memory, no file access, no web search. Everything the model knows has to come from its training or from what you put in the prompt. That is the constraint. It is also why skills are fast, cheap, and predictable — there is nothing else to go wrong.',
    code: `# A skill is just a .md file — a saved, reusable prompt.
#
# skills/full-stack-developer.md
# ───────────────────────────────
# You are a full-stack web developer. Given
# a project brief, produce a complete plan:
# tech stack, file structure, and key code.

import anthropic

client = anthropic.Anthropic()

# In code: load the .md file as the system prompt
with open("skills/full-stack-developer.md") as f:
    skill_prompt = f.read()

response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    system=skill_prompt,
    messages=[{
        "role": "user",
        "content": "Build a full-stack task manager app "
                   "with React frontend and FastAPI backend."
    }]
)

result = response.content[0].text`,
    agents: [
      {
        id: 'fullstack',
        name: 'Full-Stack Dev',
        role: 'single',
        x: 275,
        y: 181,
        brief:
          'Gets one project brief and handles everything alone — design decisions, frontend, backend, and deployment plan. No helpers, no hand-offs. Fast, but the scope is wide.',
        detail: `## This is a Skill

A skill is a reusable prompt — nothing more. In practice it is a \`.md\` file with a system prompt and a task. That is the entire definition.

\`\`\`
skills/full-stack-developer.md
───────────────────────────────
You are a full-stack web developer. Given a
project brief, produce a complete plan.
\`\`\`

### Skills have no tools
A skill cannot search the web, read a file, run code, or remember anything from a previous session. Everything has to come from the model's training or from what you put in the prompt.

Use a skill when the task is bounded and the model already knows enough to answer it.`,
      },
    ],
    connections: [],
    steps: [
      { agentId: 'fullstack', status: 'thinking', delay: 300 },
      {
        agentId: 'fullstack',
        status: 'done',
        delay: 2400,
        output:
          'Full-stack task manager plan\n' +
          '─────────────────────────────\n' +
          'Stack\n' +
          '  Frontend  React 18 + TypeScript\n' +
          '  Backend   FastAPI + PostgreSQL\n' +
          '  Hosting   Vercel (FE) + Fly.io (BE)\n' +
          '\n' +
          'File structure (excerpt)\n' +
          '  /frontend\n' +
          '    TaskList.tsx  TaskCard.tsx  api.ts\n' +
          '  /backend\n' +
          '    main.py  models/task.py  routes/\n' +
          '\n' +
          'Steps\n' +
          '  1  Scaffold monorepo\n' +
          '  2  FastAPI + SQLModel setup\n' +
          '  3  CRUD endpoints\n' +
          '  4  React components\n' +
          '  5  Wire frontend to API\n' +
          '  6  Deploy',
      },
    ],
  },

  /* ──────────────────────────── LEVEL 2 ──────────────────────────── */
  {
    id: 2,
    name: 'Sub-Agent',
    tagline: 'Skill vs Sub-Agent — side by side',
    description:
      'You hand a goal to the Planner Agent. It decides how to split the work: formatting goes to the Formatter Skill (just a prompt, no tools), research goes to the Research Agent (has tools, isolated context). The Planner sees only the results — never the work in progress.',
    analogy:
      'Like a project manager who knows which tasks need a template and which need someone to go research first. They hand off both, wait, and assemble the result.',
    explanation:
      'The Skill and the Sub-Agent look similar — both receive a task and return a result. The difference is capability. The Skill has no tools; it only knows what the model was trained on. The Sub-Agent can use tools: web search, file access, code execution. That is why the Planner routes research to the Sub-Agent and formatting to the Skill.',
    code: `import anthropic

client = anthropic.Anthropic()

# Sub-agent: research runs in its own isolated context window
# It can use tools — the Planner never sees its reasoning, only the result
research_resp = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=512,
    system="You are a tech researcher with web search access.",
    messages=[{
        "role": "user",
        "content": "Best stack for a task manager app in 2025?"
    }]
)
stack_research = research_resp.content[0].text

# Skill: just a reusable prompt — no tools, no isolated context
# In practice this is a .md file loaded as the system prompt
format_resp = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=256,
    system="You are a sprint formatter. Convert any plan into "
           "a clean sprint card structure.",
    messages=[{
        "role": "user",
        "content": "Format spec: 2 sprints, 5 days each, "
                   "with owner and status fields."
    }]
)
format_spec = format_resp.content[0].text

# Main agent: sees only the two results — not the reasoning behind them
plan_resp = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    system="You are a project planner.",
    messages=[{
        "role": "user",
        "content": f"Build a task manager sprint plan.\\n"
                   f"Stack research:\\n{stack_research}\\n"
                   f"Format spec:\\n{format_spec}"
    }]
)`,
    agents: [
      {
        id: 'human',
        name: 'You',
        role: 'human',
        x: 275,
        y: 25,
        sublabel: 'human',
        brief: 'Starts the process with a plain-English goal. No technical knowledge required.',
        detail: `## Human

You type a goal. That is the entire input. The Planner Agent handles everything from here — deciding what needs research, what needs formatting, and how to assemble the result.

### What you provide
- A plain-English goal
- Nothing else

### What you get back
- A finished sprint plan grounded in current stack research and formatted cleanly`,
      },
      {
        id: 'planner',
        name: 'Planner Agent',
        role: 'main',
        x: 275,
        y: 181,
        brief:
          'Receives your goal and decides how to split the work. Routes formatting to the Skill (fast, no tools) and research to the Sub-Agent (has tools). Assembles both results into the final plan.',
        detail: `## Main Agent

The Planner Agent receives your goal and makes two routing decisions:
1. Send the format spec task to the Formatter Skill — it is templated and the model already knows how to do it
2. Send the research task to the Research Agent — it needs to look things up, so it needs tools

### The Planner does not do this work itself
It delegates, waits for both results, then synthesises. It never sees the reasoning inside either call — only what comes back.

### Not an orchestrator yet
An orchestrator (Level 3) delegates everything and does no work itself. The Planner here still assembles the final output — it is a main agent, not a pure router.`,
      },
      {
        id: 'skill',
        name: 'Formatter',
        role: 'single',
        x: 80,
        y: 330,
        sublabel: 'skill · no tools',
        brief:
          'A reusable prompt. Converts a raw plan into a clean sprint format. Fast — no tools needed, the model already knows how to format.',
        detail: `## Skill

A skill is a saved, reusable prompt — nothing more. No tools, no memory, no file access.

\`\`\`
skills/sprint-formatter.md
───────────────────────────
You are a sprint formatter. Convert any plan
into a clean sprint card structure with owner,
status, and dependency fields.
\`\`\`

### Why use a skill here?
Formatting is a templated task. The model already knows how to structure sprint cards — there is nothing to look up, no file to read. A skill is faster and cheaper than a full agent call.

### The constraint
If the task ever requires current information (e.g. "what format does Linear use today?"), a skill cannot answer it. That is when you reach for a sub-agent with tools.`,
      },
      {
        id: 'research',
        name: 'Research Agent',
        role: 'sub',
        x: 470,
        y: 330,
        sublabel: 'agent · has tools',
        brief:
          'Searches the web for current stack options. Returns grounded recommendations the Planner uses to build the plan. Runs in its own isolated context — the Planner only sees the result.',
        detail: `## Sub-Agent

The Research Agent runs in complete isolation — its own system prompt, its own context window. The Planner never sees its tool calls or reasoning. It only receives the final recommendations.

### What tools unlock
\`\`\`
name: research-agent
tools:
  - WebSearch   ← look up current stack trends
  - Read        ← read existing project files
  - Write       ← save findings to disk
\`\`\`

A skill can only use what the model was trained on. A sub-agent with tools can go and get what it needs right now — current library versions, recent benchmarks, live documentation.

### Isolation is the point
The Planner gets one clean result. It never sees the search queries, intermediate findings, or dead ends. That boundary keeps the main agent's context clean.`,
      },
    ],
    connections: [
      { from: 'human', to: 'planner' },
      { from: 'planner', to: 'skill' },
      { from: 'planner', to: 'research' },
      { from: 'skill', to: 'planner' },
      { from: 'research', to: 'planner' },
    ],
    steps: [
      { agentId: 'human', status: 'thinking', delay: 300 },
      {
        agentId: 'human',
        status: 'done',
        delay: 700,
        output: 'Build me a task manager app.\nModern stack, full sprint plan.',
      },
      { agentId: 'planner', status: 'thinking', delay: 500 },
      { agentId: 'skill', status: 'thinking', delay: 900 },
      { agentId: 'research', status: 'thinking', delay: 100 },
      {
        agentId: 'skill',
        status: 'done',
        delay: 1200,
        output:
          'Sprint format spec\n' +
          '──────────────────\n' +
          'Sections   Goal · Stack · Sprint 1 · Sprint 2\n' +
          'Cards      Title · owner · days · deps\n' +
          'Status     Todo / In Progress / Done\n' +
          'Notes      Inline, max 1 line per card',
      },
      {
        agentId: 'research',
        status: 'done',
        delay: 1400,
        output:
          'Stack research (web)\n' +
          '────────────────────\n' +
          'Frontend  React 18 — dominant, Vite for speed\n' +
          'Backend   FastAPI rising, Express still default\n' +
          'DB        PostgreSQL + Prisma ORM popular pairing\n' +
          'Host      Vercel (FE) · Railway (BE) — lowest friction\n' +
          'Auth      Clerk gaining vs NextAuth\n' +
          'Trend     tRPC + React Query replacing REST+Axios',
      },
      {
        agentId: 'planner',
        status: 'done',
        delay: 900,
        output:
          'Task manager — sprint plan\n' +
          '──────────────────────────\n' +
          'Stack   React 18 · FastAPI · PostgreSQL · Prisma\n' +
          'Host    Vercel (FE) · Railway (BE)\n' +
          '──────────────────────────────────────────────────\n' +
          'Sprint 1 — Core (5 days)\n' +
          '  D1  DB schema + Prisma migration\n' +
          '  D2  FastAPI CRUD routes\n' +
          '  D3  React board + TaskCard\n' +
          '  D4  Wire API with React Query\n' +
          '  D5  Drag-and-drop (dnd-kit)\n' +
          'Sprint 2 — Ship (4 days)\n' +
          '  D1  Auth (Clerk)\n' +
          '  D2  Priority badges + assignees\n' +
          '  D3  Deploy: Vercel + Railway\n' +
          '  D4  QA + polish',
      },
    ],
  },
  /* ──────────────────────────── LEVEL 3 ──────────────────────────── */
  {
    id: 3,
    name: 'Orchestrator',
    tagline: 'The agent decides the team',
    description:
      'The Project Lead reads the goal and decides who is needed — you do not hardcode that in your script. Same code, different goal → different specialists dispatched. The topology is dynamic.',
    analogy:
      'Like a project lead who reads the brief and figures out who to call. A landing page? Just designer + frontend. A full app? The whole team. The decision lives in the agent, not in your code.',
    explanation:
      'If you hardcoded asyncio.gather(designer, frontend, backend) in your script, the team is fixed forever — change the project, rewrite the code. Here, the Project Lead reads the goal and decides the team at runtime. Change the goal from "full app" to "landing page" and it dispatches only two specialists. You change the prompt, not the code. The topology is dynamic.',
    code: `# Level 3 — project lead plans, team executes, tech lead integrates.
import asyncio
import anthropic

aclient = anthropic.AsyncAnthropic()

async def run(system: str, prompt: str) -> str:
    r = await aclient.messages.create(
        model="claude-opus-4-5", max_tokens=512,
        system=system,
        messages=[{"role": "user", "content": prompt}]
    )
    return r.content[0].text

goal = "Build a full-stack task manager with React, FastAPI, and PostgreSQL."

# Step 1: Project lead scopes the work
brief = await run(
    "You are a project lead. Break the goal into "
    "specialist briefs for your team. Return JSON.",
    goal
)

# Step 2: All specialists work in parallel
design, frontend, backend, qa = await asyncio.gather(
    run("UI Designer",        f"Brief: {brief}"),
    run("Frontend Developer", f"Brief: {brief}"),
    run("Backend Developer",  f"Brief: {brief}"),
    run("QA Engineer",        f"Brief: {brief}"),
)

# Step 3: Tech lead integrates into the final build plan
final = await run(
    "Tech Lead",
    f"Integrate into one build plan:\\n"
    f"Design: {design}\\nFrontend: {frontend}\\n"
    f"Backend: {backend}\\nQA: {qa}"
)`,
    agents: [
      {
        id: 'orch',
        name: 'Project Lead',
        role: 'orch',
        x: 275,
        y: 30,
        sublabel: 'plan + dispatch',
        brief:
          'Reads the project goal and decides who handles what. Does not write any specs — its only job is to scope the work and send the team off.',
        detail: `## Orchestrator — dynamic topology

The difference from a hardcoded script: **you do not write the team into your code**.

If you wrote \`asyncio.gather(designer, frontend, backend)\`, that team is fixed forever. Here, the project lead reads the goal and **decides the team at runtime**:

\`\`\`python
# Same code for any goal
brief = await run(
    "You are a project lead. Decide which specialists "
    "are needed and write each one a brief. Return JSON.",
    goal   # ← this is the only thing that changes
)
\`\`\`

Full app → dispatches designer + frontend + backend + QA.
Landing page → maybe just designer + frontend.
API only → backend + QA, no designer.

**You change the goal. The agent changes the team.**

### Why this matters for scale
Adding a new capability (security review, accessibility audit) means adding a specialist skill file — not editing the orchestrator or any existing prompt. The topology grows without the code growing.`,
      },
      {
        id: 'designer',
        name: 'UI Designer',
        role: 'sub',
        x: 20,
        y: 200,
        brief:
          'Produces the design system: component structure, style guide, and interaction patterns. Dispatched by the project lead with a scoped brief.',
        detail: `## Specialist Sub-Agent

Dispatched by the project lead with a specific brief.

This agent does not know about the other three specialists running in parallel. Its context is clean: one role, one question, one output.

### Dispatched, not chained
In a chained workflow, each step runs after the previous finishes. Here, the project lead dispatches all four specialists at once — this one runs in parallel with the frontend dev, backend dev, and QA engineer.

### The brief determines the quality
The project lead's scoping brief is the most important input this agent receives. A vague brief produces a vague design. A tight brief produces something the tech lead can integrate directly.`,
      },
      {
        id: 'frontend',
        name: 'Frontend Dev',
        role: 'sub',
        x: 190,
        y: 200,
        brief:
          'Specs the React component tree, state management, and data-fetching strategy. Runs in parallel — no awareness of what the designer or backend dev are producing.',
        detail: `## Specialist Sub-Agent

Scopes the React component tree, state management, and data-fetching strategy. Returns a frontend spec the tech lead can use directly.

Runs in parallel with three other specialists. Its output goes directly to the tech lead — the project lead never sees its raw work.

### Scoped to one domain
The tighter the scope from the project lead's brief, the more useful this agent's output. A frontend spec that bleeds into backend design produces something neither specialist nor integrator can use cleanly.`,
      },
      {
        id: 'backend',
        name: 'Backend Dev',
        role: 'sub',
        x: 360,
        y: 200,
        brief:
          'Designs the data models, REST API endpoints, and database schema. Isolated from the frontend and design specs — they meet at the tech lead.',
        detail: `## Specialist Sub-Agent

Designs the data models, API endpoints, and DB schema. Returns a backend spec the tech lead can integrate with the frontend and design outputs.

Isolated context, narrow focus. The tech lead slots this spec into the build plan alongside the design system and frontend component tree.

### Each specialist sees only its brief
This agent does not see what the UI designer or frontend dev produced. That isolation is deliberate — it prevents anchoring and keeps each output independent. The tech lead is the only place where all specs meet.`,
      },
      {
        id: 'qa',
        name: 'QA Engineer',
        role: 'sub',
        x: 530,
        y: 200,
        brief:
          'Writes the test plan and acceptance criteria before a line of code exists. Works from the project brief alone.',
        detail: `## Specialist Sub-Agent

Writes the test plan and acceptance criteria in parallel with the other three specialists — before any code exists.

This is possible because the project lead's brief carries enough context. The QA engineer does not need to see the component tree or API design to define what "done" looks like.

### Skills-as-workers pattern
Each specialist here is a skill file with a focused role:
\`\`\`
skills/qa-engineer.md
──────────────────────
You are a QA engineer. Given a project brief,
produce a test plan: unit tests, integration
tests, E2E scenarios, and acceptance criteria.
\`\`\`

The orchestrator pattern works because every worker is interchangeable — a skill file you can swap, tune, or replace without touching anything else.`,
      },
      {
        id: 'synth',
        name: 'Tech Lead',
        role: 'merge',
        x: 275,
        y: 362,
        sublabel: 'integrate',
        brief:
          'The only agent that sees all four specialist outputs at once. Turns them into one coherent build plan — stack, sprints, testing strategy, deployment.',
        detail: `## Synthesiser

The final agent. Receives outputs from all four specialists and composes the finished build plan.

This is the only agent in the pipeline that sees everything at once. It is also the only one whose output the team actually ships from.

### Context discipline
The tech lead never sees raw reasoning — only distilled specs. Four full context windows of thinking get compressed into four tight outputs before they arrive here. That keeps the tech lead's context tight and its plan coherent.

### Still just a skill
\`\`\`
skills/tech-lead.md
────────────────────
You are a tech lead. Given specialist specs
from design, frontend, backend, and QA,
produce an integrated build plan with stack
decisions, sprint breakdown, and test strategy.
\`\`\`

The complexity is in the architecture — the pipeline that feeds this agent. The agent itself is a plain skill file.`,
      },
    ],
    connections: [
      { from: 'orch', to: 'designer' },
      { from: 'orch', to: 'frontend' },
      { from: 'orch', to: 'backend' },
      { from: 'orch', to: 'qa' },
      { from: 'designer', to: 'synth' },
      { from: 'frontend', to: 'synth' },
      { from: 'backend', to: 'synth' },
      { from: 'qa', to: 'synth' },
    ],
    steps: [
      { agentId: 'orch', status: 'thinking', delay: 300 },
      {
        agentId: 'orch',
        status: 'done',
        delay: 1600,
        output:
          'Team briefs\n' +
          '─────────────\n' +
          '1. Designer  · Kanban UI · style guide · drag-drop\n' +
          '2. Frontend  · React component tree · state mgmt\n' +
          '3. Backend   · REST API · data models · DB schema\n' +
          '4. QA        · test plan · acceptance criteria\n' +
          'Dispatching all four in parallel.',
      },
      { agentId: 'designer', status: 'thinking', delay: 700 },
      { agentId: 'frontend', status: 'thinking', delay: 0 },
      { agentId: 'backend', status: 'thinking', delay: 0 },
      { agentId: 'qa', status: 'thinking', delay: 0 },
      {
        agentId: 'designer',
        status: 'done',
        delay: 2000,
        output:
          'Design system\n' +
          '───────────────\n' +
          'Board   3-col Kanban · drag placeholder\n' +
          'Card    title · assignee avatar · priority badge\n' +
          'Colors  #1a1a1a · #f5f5f0 · terracotta accent\n' +
          'Motion  200ms ease · 0.85 drag ghost opacity',
      },
      {
        agentId: 'frontend',
        status: 'done',
        delay: 600,
        output:
          'Frontend spec\n' +
          '───────────────\n' +
          '<Board> <Column> <TaskCard> <TaskModal>\n' +
          'State   Zustand · React Query\n' +
          'Router  Next.js App Router\n' +
          'DnD     dnd-kit for drag-to-reorder',
      },
      {
        agentId: 'backend',
        status: 'done',
        delay: 700,
        output:
          'API + data model\n' +
          '──────────────────\n' +
          'Task    id · title · status · priority\n' +
          '        assignee_id · due_date\n' +
          'Routes  CRUD /tasks · PATCH /:id/status\n' +
          'Auth    JWT · POST /auth/login\n' +
          'DB      PostgreSQL + SQLModel',
      },
      {
        agentId: 'qa',
        status: 'done',
        delay: 900,
        output:
          'Test plan\n' +
          '───────────\n' +
          'Unit   TaskCard renders priority badge\n' +
          '       PATCH /tasks/:id returns updated task\n' +
          'E2E    Create → drag to Done → verify DB\n' +
          'Perf   Drag operations < 100ms\n' +
          'Done   all columns render · auth flow works',
      },
      { agentId: 'synth', status: 'thinking', delay: 800 },
      {
        agentId: 'synth',
        status: 'done',
        delay: 2800,
        output:
          'Full-stack build plan — final\n' +
          '═══════════════════════════════════════════\n' +
          'Stack    Next.js · FastAPI · PostgreSQL\n' +
          'Design   Kanban · Inter · dnd-kit drag-drop\n' +
          'Auth     NextAuth + JWT\n' +
          '\n' +
          'Sprint 1  Foundation\n' +
          '  D1  Monorepo setup + DB schema + migrations\n' +
          '  D2  FastAPI CRUD endpoints + auth\n' +
          '  D3  <Board> <Column> <TaskCard>\n' +
          '  D4  React Query ↔ API integration\n' +
          'Sprint 2  UX + Quality\n' +
          '  D1  Drag-to-reorder + optimistic updates\n' +
          '  D2  TaskModal + priority badges\n' +
          '  D3  Unit + E2E tests (pytest + Playwright)\n' +
          'Sprint 3  Ship\n' +
          '  D1  Vercel (FE) + Fly.io (BE) deploy\n' +
          '  D2  CI/CD GitHub Actions\n' +
          '  D3  Error tracking + monitoring',
      },
    ],
  },
];
