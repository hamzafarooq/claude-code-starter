# {{SKILL_TITLE}}

{{SKILL_DESCRIPTION}}

A standalone command-line app, built on the Anthropic SDK, that runs this
skill outside of Claude Code. It loads `skill/SKILL.md` as the system prompt
and answers your questions via the Claude API.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # Windows: .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your API key:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and paste your real key (from https://console.anthropic.com).

## Usage

One-shot:
```bash
python app.py "{{EXAMPLE_QUESTION}}"
```

Interactive (keeps conversation history):
```bash
python app.py
```

Examples:
{{EXAMPLES}}

## How it works

`skill/SKILL.md` → frontmatter stripped → passed as the `system` prompt on
every API call. The skill's instructions guide every response, the way they
would inside Claude Code.

## Notes & limits

- **Instruction-only skills work fully.** If this skill just tells the model
  how to think, format, or respond, the app reproduces it faithfully.
- **Skills that run scripts need more.** A plain API call only generates text
  — it can't execute bundled scripts, read local files, or run bash. If this
  skill relies on running its own tools, those steps won't run here;
  reproducing them requires adding tool use (function calling).
- Change the model or token limit at the top of `app.py` if needed.

## Deploying (optional)

To run this on a schedule or call it from other code, treat `app.py` as a
normal Python entry point. Set `ANTHROPIC_API_KEY` as an environment variable
in your hosting environment instead of using the `.env` file.
