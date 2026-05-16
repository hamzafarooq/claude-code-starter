# Course Demo — Two Themes, One Workshop

Teaching demos for understanding LLM harness layers.

## Themes

### 🎯 Theme 1 — `research-agent/`
A Claude Code skill-based competitor research agent. Browse to understand the
"CC harness" pattern: skills, subagents, MCP servers, file-based memory.
Imported verbatim from
[maven-workshop-research-agent](https://github.com/aishwaryaashok14/maven-workshop-research-agent).

### 🎨 Theme 2 — `research-frontend/`
A Next.js teaching demo where students experience the **same domain** through
three harness layers, side-by-side:

| Tab | What it shows |
|---|---|
| **LLM** | The raw model — confidently hallucinated answers |
| **+ Tools** | RAG + web_search + Playwright — grounded, sourced answers |
| **+ Tools + Memory** | Above + CLAUDE.md persistent context + SKILL.md procedure |

Run `research-frontend/demo/` for the working version.
Work through `research-frontend/scaffold/` to build it yourself.
