---
name: skill-to-sdk
description: Turn an Anthropic Agent Skill into a runnable standalone Python app built on the Anthropic SDK. Use this whenever the user wants to "publish", "export", "package", or "turn into an app" a skill, or asks for the "SDK version" / "API version" / "standalone version" of a skill, or wants a script that loads a SKILL.md and runs it via the Claude API outside of Claude Code. Trigger whether the user provides an actual SKILL.md file OR just names/describes a skill in text — in the latter case, generate the SKILL.md first, then wrap it. Use this even if the user only says something like "make my X skill into a program" without saying "SDK" explicitly.
---

# Skill to SDK

Convert an Anthropic Agent Skill into a self-contained Python program that
loads the skill's instructions as a system prompt and runs them against the
Claude API. The output is a small command-line app the user runs with
`python app.py "their question"` (or interactively) that prints the answer to
the console.

## Why this exists

A skill normally lives inside Claude Code / Claude.ai and triggers when its
description matches. People often want to take a finished skill and run it as
an ordinary program — to share it, schedule it, embed it, or call it from
other code. This skill produces that program. The skill's instruction body
becomes the **system prompt**; the user's question becomes the user message;
the model's reply is printed to the console.

The wrapper is deliberately simple: one API call per turn, text in and text
out, no tools. That is exactly what an instruction-only skill needs — a skill
that just tells the model how to think, reason, format, or respond reproduces
faithfully this way (e.g. `market-sizing`, `okr-writer`, `exec-summary`).

## Input: two cases

The user will either hand you a SKILL.md or just describe a skill. Detect
which and proceed accordingly.

1. **They provide a SKILL.md** (a file, a path, or pasted text): use it
   directly. Strip the YAML frontmatter — only the markdown body becomes the
   system prompt. Keep the `name` from the frontmatter to name the output
   folder and files.

2. **They only give a name or description** (e.g. "a skill that summarizes
   legal contracts"): first write a short, well-formed SKILL.md for it
   yourself — frontmatter with `name` and `description`, then a clear
   instruction body in the imperative voice describing how the assistant
   should behave. Show it to the user briefly, then wrap it. Keep it focused;
   a single-purpose instruction set is better than a sprawling one.

If anything essential is ambiguous (what the skill should actually do, what
its name is), ask one concise question before generating. Otherwise proceed.

## What to generate

Create a folder named after the skill (kebab-case, from the skill's `name`),
containing exactly these files. Use the templates in `assets/` as the starting
point and fill in the skill-specific pieces.

```
<skill-name>-sdk/
├── skill/
│   └── SKILL.md          # the source skill (provided or generated)
├── app.py                # CLI: loads SKILL.md, calls the API, prints the reply
├── requirements.txt      # anthropic, python-dotenv
├── .env.example          # ANTHROPIC_API_KEY placeholder
└── README.md             # setup + run instructions, tailored to this skill
```

Copy `assets/app_template.py` to `app.py` **verbatim** — all the
skill-specific content lives in `skill/SKILL.md`, so the runner itself never
needs to change. Copy `assets/requirements.txt` and `assets/.env.example`
as-is. Only edit `app.py` if the user explicitly asks for behavior the
template doesn't cover (a different model, JSON output, or streaming).

### What app.py does

The template runner:

- Loads `skill/SKILL.md`, strips the frontmatter (everything up to the second
  `---`), and uses the remaining body as the `system` prompt.
- Handles input in three modes, in this order: (1) a command-line argument
  (`python app.py "question"`) runs one-shot; (2) if there's no argument but
  input is piped in and there's no interactive terminal
  (`sys.stdin.isatty()` is false), it reads all of stdin as a single question
  — this is what makes `echo "..." | python app.py` and CI/non-interactive
  shells work; (3) only when a real terminal is attached, it drops into an
  interactive loop that keeps conversation history. This ordering matters:
  never enter the `input()` loop without a TTY, or it exits immediately and no
  conversation happens. When there's no argument, no TTY, and no piped input,
  it prints clear usage rather than silently doing nothing.
- Calls `client.messages.create` with `model="claude-sonnet-4-6"`,
  `max_tokens=2000`, the system prompt, and the message history.
- Extracts the text blocks from the response and prints them to the console.
- Fails clearly if `ANTHROPIC_API_KEY` is missing, pointing the user to
  `.env.example`.

### README.md

Base it on `assets/README_template.md`, then customize the title and the
one-line description to match the specific skill, and add 2-3 realistic
example invocations relevant to what this skill does. Keep the "Notes & limits"
section — it sets correct expectations about what a text-only wrapper can do.

## Scope: instruction-only skills

This wrapper is a plain text-in / text-out API call. It cannot run bundled
scripts, read local files, or execute bash — so it reproduces **instruction-only**
skills, the ones that just guide how the model thinks, reasons, formats, or
responds. That covers the large majority of skills.

If the source skill genuinely needs to *act* — write files, read files, or run
shell commands as part of its core job — say so plainly. The text-only wrapper
will reproduce the skill's reasoning and describe the actions, but it won't
perform them; making those real would require adding tool use (function
calling) to `app.py`, which is out of scope here. Never silently imply a
file-producing skill will write files when it won't.

## Steps

1. Determine the input case (provided SKILL.md vs. name/description). If the
   latter, draft the SKILL.md and show it.
2. Note for the user whether the skill is fully instruction-only (reproduces
   faithfully) or relies on actions the text-only wrapper can't perform.
3. Create the folder structure from the `assets/` templates.
4. Write the source skill into `skill/SKILL.md`.
5. Tailor `README.md` (title, description, examples) to this skill.
6. If a file-creation/output mechanism is available, save everything to the
   outputs location, zip it, and present it for download. Otherwise show the
   files inline.
7. Give the user the run instructions: create and activate a virtual
   environment (`python -m venv .venv` then `source .venv/bin/activate`, or
   `.venv\Scripts\activate` on Windows), install deps, copy `.env.example` to
   `.env` and add their key, then `python app.py "a question"`.

## Quick sanity check before delivering

- Frontmatter stripping works (the system prompt should not start with `---`).
- The folder name and the skill `name` agree.
- `requirements.txt` lists `anthropic` and `python-dotenv`.
- The README's examples actually match what the skill does.
- You told the user whether the skill is fully instruction-only.
