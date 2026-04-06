# [Your Name]'s PM Workspace — Claude Code Guide

## Who I am
- Product Manager at [Company Name]
- Focus area: [e.g. "growth and monetization" / "core product" / "platform"]
- I'm comfortable with product thinking but not with code
- I work with [X] engineers and [X] designers

## What this project is
[One sentence describing your product — e.g. "NoteToTicket converts meeting recordings into structured Jira tickets using AI."]

- Current phase: [Discovery / Alpha / Beta / Launched]
- Key stakeholders: [PM, Eng, Design, Legal, Data, etc.]
- Primary users: [Who uses your product]

## How Claude should respond
- Keep answers concise — I don't need long explanations
- Use plain English, avoid technical jargon unless I ask for it
- When I ask you to write something, write it directly — don't explain what you're about to do first
- Flag risks and tradeoffs clearly, but don't over-explain
- When you edit a file, tell me what changed and why in one sentence
- If I ask a question and the answer is uncertain, say so — don't guess confidently

## Project conventions
- PRDs live in `docs/prd.md`
- User stories use the format: "As a [user], I want to [action] so that [outcome]"
- Acceptance criteria use Given/When/Then format
- Every PRD includes a "Risks and Assumptions" section
- Feature ideas go in `docs/prd.md` under the Backlog section

## What I use Claude Code for
- Draft and review PRDs from brief feature descriptions
- Write user stories and acceptance criteria
- Summarize long documents into executive-ready formats
- Flag gaps, edge cases, and missing requirements in specs
- Generate sprint plans from a list of user stories
- Rewrite content for different audiences (exec, engineer, customer)
- Answer "what did we decide about X?" by reading the docs

## Skills available
- `/prd-generator` — Generates a structured PRD from a feature description
- `/user-story-writer` — Converts rough feature ideas into user stories with acceptance criteria
