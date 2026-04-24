> This is a starter template for a deploy-ready project. Copy it into your project folder, rename it to `CLAUDE.md`, and fill in the bracketed sections.

# [Your Name]'s Project — Deploy-Ready Workspace

## Who I am
- [Your role — e.g. "Product Manager at [Company]" or "Founder of [Startup]"]
- I'm comfortable with product thinking; I can read code but don't write it from scratch
- I build and ship AI-powered tools using Claude Code

## What this project is
[One sentence — e.g. "MeetingMemo converts raw meeting notes into structured standup updates using Claude."]

- Current phase: [Building / Evaluating / Deployed]
- Stack: [e.g. Next.js + Anthropic API + Vercel]
- Live URL: [your Vercel or Fly.io URL once deployed]

## How Claude should respond
- Be concise — I don't need long explanations
- When I ask you to build something, build it directly
- Flag anything that would break in production (missing env vars, no error handling)
- If a change touches deployment config (Dockerfile, fly.toml, vercel.json), warn me before making it

## Project structure
```
/
├── CLAUDE.md               ← context for Claude (you are here)
├── app/
│   ├── page.tsx            ← frontend
│   └── api/
│       └── generate/
│           └── route.ts    ← Claude API call lives here
├── docs/
│   ├── prd.md              ← product spec
│   └── eval-ground-truth.md ← eval test cases
├── .env.local              ← API keys (never commit this)
└── package.json
```

## Conventions
- API keys go in `.env.local` — never hardcoded, never committed
- Ground truth for evals lives in `docs/eval-ground-truth.md`
- PRD lives in `docs/prd.md`
- Every AI feature goes through `/skill-evaluator` before shipping

## Eval status
- [ ] Ground truth written (10 examples minimum)
- [ ] `/skill-evaluator` run — current score: [X / 10]
- [ ] `/deploy-checklist` run — all green

## Skills available
- `/skill-evaluator` — Score a Skill's output against ground truth, identify failure patterns
- `/deploy-checklist` — Run pre-deploy checks before pushing to Vercel or Fly.io
