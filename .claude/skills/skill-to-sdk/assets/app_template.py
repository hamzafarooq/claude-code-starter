"""
Standalone runner for an Anthropic Agent Skill.

Loads skill/SKILL.md as the system prompt and runs it against the Claude API.
Usage:
    python app.py "your question here"      # one-shot (argument)
    echo "your question" | python app.py    # one-shot (piped / non-interactive)
    python app.py                            # interactive loop (real terminal only)
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key:
    raise SystemExit(
        "Missing ANTHROPIC_API_KEY.\n"
        "Copy .env.example to .env and add your key, "
        "or export ANTHROPIC_API_KEY in your shell."
    )

client = Anthropic(api_key=api_key)

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 2000

# Load the skill body as the system prompt, stripping YAML frontmatter.
raw = Path(__file__).parent.joinpath("skill", "SKILL.md").read_text(encoding="utf-8")
if raw.startswith("---"):
    raw = raw.split("---", 2)[-1]  # drop the frontmatter block
SYSTEM_PROMPT = raw.strip()


def ask(history):
    """Send the current history to Claude and return the assistant's text."""
    msg = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=SYSTEM_PROMPT,
        messages=history,
    )
    return "".join(b.text for b in msg.content if b.type == "text")


def one_shot(question):
    history = [{"role": "user", "content": question}]
    print(ask(history))


def interactive():
    print("Interactive mode. Type your question and press Enter. "
          "Ctrl-C or empty line to quit.\n")
    history = []
    while True:
        try:
            question = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not question:
            break
        history.append({"role": "user", "content": question})
        try:
            answer = ask(history)
        except Exception as e:
            history.pop()
            print(f"Error: {e}\n")
            continue
        history.append({"role": "assistant", "content": answer})
        print(f"\n{answer}\n")


def main():
    # 1. Question passed as a command-line argument -> one-shot.
    if len(sys.argv) > 1:
        one_shot(" ".join(sys.argv[1:]))
        return

    # 2. No argument, but input is piped in (no real terminal) -> read stdin
    #    as a single question. Covers `echo "..." | python app.py` and CI.
    if not sys.stdin.isatty():
        piped = sys.stdin.read().strip()
        if piped:
            one_shot(piped)
        else:
            print(
                "No question provided. Pass one as an argument:\n"
                '    python app.py "your question here"\n'
                "or pipe it in:\n"
                '    echo "your question here" | python app.py'
            )
        return

    # 3. A real interactive terminal -> conversation loop.
    interactive()


if __name__ == "__main__":
    main()
