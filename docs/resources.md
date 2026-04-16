# Claude Code Community Resources

A curated list of GitHub repos worth knowing — organized by category. Use these to go deeper on skills, best practices, and memory management.

---

## Discover & Browse (Awesome Lists)

The fastest way to find skills, hooks, and commands the community has already built.

| Repo | Stars | What it is |
|------|-------|-----------|
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | ⭐ 39k | The definitive curated list: skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code |
| [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | ⭐ 33k | 1,400+ installable agentic skills for Claude Code, Cursor, Codex CLI — with a one-command install pipeline |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | ⭐ 17k | 100+ specialized Claude Code subagents covering a wide range of development use cases |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | ⭐ 16k | 1,000+ agent skills from official dev teams and the community — compatible with Claude Code, Codex, and Gemini CLI |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | ⭐ 11k | Curated list of Claude Skills, resources, and tools for customizing Claude AI workflows |

**Start here:** `hesreallyhim/awesome-claude-code` is the most comprehensive and actively maintained. Bookmark it.

---

## Skills & Best Practices

Specific skill repos worth installing or learning from.

| Repo | Stars | What it is |
|------|-------|-----------|
| [YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill) | ⭐ 256 | Reusable skill modules for Claude Code — code review, testing, documentation, and more. Good reference for how to structure your own skills |
| [agamm/claude-code-owasp](https://github.com/agamm/claude-code-owasp) | ⭐ 128 | Claude Code skill for OWASP security best practices (Top 10:2025, ASVS 5.0, Agentic AI security). Useful if you're building anything that handles user data |
| [ThamJiaHe/claude-code-handbook](https://github.com/ThamJiaHe/claude-code-handbook) | ⭐ 104 | Comprehensive guide for writing professional Claude prompts with MCP, Skills, and Superpowers integration |

---

## Memory Management

How to give Claude persistent memory across sessions so it doesn't start from scratch every time.

| Repo | What it is |
|------|-----------|
| [lucasrosati/claude-code-memory-setup](https://github.com/lucasrosati/claude-code-memory-setup) | **Obsidian + Graphify** memory system — claims up to 71.5x fewer tokens per session. Sets up persistent memory, codebase knowledge graphs, and a chat import pipeline. This is the most practical memory setup tutorial available for Claude Code. |

### What "memory management" means in Claude Code

By default, Claude starts fresh every session. If you want it to remember decisions, architecture choices, or prior conversations, you have two main options:

1. **CLAUDE.md** — The built-in approach. Everything in your `CLAUDE.md` file is loaded into every session. This is what we use in this course.
2. **External memory (like Graphify)** — Tools that build a knowledge graph of your codebase and conversations, then feed relevant chunks into context. More powerful, more setup required.

For PMs: start with `CLAUDE.md`. It handles 90% of what you need.

---

## Official Docs

- [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code) — Skills, hooks, MCP, CLAUDE.md reference
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) — Code examples for building with the Claude API

---

*Last updated: April 2026*
