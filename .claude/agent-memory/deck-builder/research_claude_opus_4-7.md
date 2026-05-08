---
name: Claude Opus 4.7 vs 4.6 Research
description: Research notes from April 2026 deck build — benchmarks, pricing, use cases, developer sentiment, key sources
type: reference
---

## Release Facts
- Released April 16, 2026 by Anthropic
- Positioned as the most capable publicly available Claude model
- Anthropic explicitly concedes it trails their unreleased internal model "Mythos" on safety grounds

## Pricing
- Same rate card as Opus 4.6: $5 / 1M input tokens, $25 / 1M output tokens
- Hidden cost trap: new tokenizer produces 1.0–1.35x MORE tokens for the same input text
- Real bills can rise up to 35% even though the price-per-token is unchanged
- Prompt caching saves up to 90%; batch processing saves 50%

## Context Window
- 1M input tokens / 128K output tokens (same as 4.6)

## Key Benchmark Improvements
- SWE-bench Verified: 80.8% → 87.6% (+6.8 points)
- SWE-bench Pro: 53.4% → 64.3% (+10.9 points)
- CursorBench (real IDE tasks): 58% → 70% (+12 points)
- MCP-Atlas (agentic tool use): +14.6 point jump (largest single improvement)
- Visual navigation (no tools): 57.7% → 79.5%
- Computer vision (penetration testing partner): 54.5% → 98.5%
- Beats GPT-5.4 and Gemini 3.1 Pro on coding, tool use, and computer use benchmarks

## Key Capability Changes
1. Vision resolution: 3x higher (up to 2,576px long edge / ~3.75 MP)
2. Self-verification: model writes tests, runs sanity checks, inspects its own output before declaring complete
3. Instruction following: more literal than 4.6 — a behavioral shift, not just performance
4. New effort level "xhigh" added (levels: low / medium / high / xhigh / max)
5. Agentic autonomy: better at long-horizon tasks without needing human check-ins

## Behavioral Shift Warning
- Opus 4.7 is MORE literal in following instructions — prompts tuned for 4.6's loose interpretation may break
- This is the #1 migration risk for teams upgrading

## Developer Sentiment
- Positive for agentic coding and complex multi-step tasks
- Teams can "hand off their hardest coding work with confidence"
- Not a clean win for every use case — general Q&A, light writing tasks: smaller gains
- Tokenizer change is the top complaint

## Best Sources Found
- Anthropic official: https://www.anthropic.com/news/claude-opus-4-7
- Benchmark deep dive: https://www.vellum.ai/blog/claude-opus-4-7-benchmarks-explained
- Pricing cost trap: https://www.finout.io/blog/claude-opus-4.7-pricing-the-real-cost-story-behind-the-unchanged-price-tag
- PM/builder review: https://karozieminski.substack.com/p/claude-opus-4-7-review-tutorial-builders
- vs 4.6 comparison: https://llm-stats.com/blog/research/claude-opus-4-7-vs-opus-4-6
- CNBC coverage: https://www.cnbc.com/2026/04/16/anthropic-claude-opus-4-7-model-mythos.html

## Analogies That Work for PM Audiences
- Vision upgrade = "hiring a team member who can now read the whiteboard from the back of the room"
- Self-verification = "a contractor who double-checks their own work before showing you the invoice"
- Literal instruction following = "if you say 'paint the door red,' don't expect them to also paint the trim"
- Tokenizer cost trap = "same price per mile, but the car gets fewer miles per gallon"
