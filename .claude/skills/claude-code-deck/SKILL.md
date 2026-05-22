---
name: claude-code-deck
description: Generate a complete, ready-to-share HTML presentation explaining Claude Code, Skills, Sub Agents, Hooks, and Multi-Agent Systems — designed for product managers. Outputs a single zero-dependency HTML file in Bold Signal style (dark, orange accents). Use when someone wants a polished explainer deck for Claude Code concepts.
---

# Claude Code Deck

Generate a production-ready, 11-slide HTML presentation on Claude Code's five core primitives — targeted at product managers and non-technical audiences.

## What This Skill Produces

A single `presentation.html` file featuring:
- **11 slides** covering Claude Code, Skills, Sub Agents, Hooks, Multi-Agent Systems, architecture, PM use cases, and next steps
- **Bold Signal style**: dark background (#080810), orange accents (#f5a623), geometric diagonal shapes, clean Helvetica typography
- **Zero dependencies**: fully self-contained, works offline
- **Navigation**: arrow keys, spacebar, click, swipe — progress bar, slide counter
- **Speaker notes**: press `N` to toggle per-slide notes

---

## Slide Outline

| # | Title | Core Insight |
|---|---|---|
| 1 | Title | Ship with Claude Code |
| 2 | What is Claude Code? | AI pair programmer in your terminal — reads, edits, runs, ships |
| 3 | The PM Superpower | Hours vs. engineering weeks |
| 4 | Concept 01 — Skills | Reusable workflows triggered by a slash command |
| 5 | Skills in Action | 6 real examples from the course |
| 6 | Concept 02 — Sub Agents | Delegate to specialist AI workers with isolated context |
| 7 | Concept 03 — Hooks | PreToolUse / PostToolUse / Stop / Notification |
| 8 | Concept 04 — Multi-Agent | Parallel fleets, scale beyond a single context window |
| 9 | How It All Fits | Layered architecture: Multi-Agent → Sub Agents → Skills → Hooks |
| 10 | What PMs Are Building | 4 real course builds with time-to-ship |
| 11 | Your Next 3 Steps | Install → run a skill → build a multi-agent workflow |

---

## Instructions

1. Copy the full HTML from `presentation.html` in the repo root (or regenerate it using the template below).
2. Save as `presentation.html` in the working directory.
3. Open with `open presentation.html` or deploy to Vercel:
   ```bash
   mkdir -p /tmp/claude-deck
   cp presentation.html /tmp/claude-deck/index.html
   cd /tmp/claude-deck && vercel deploy --yes
   ```
4. Share the Vercel URL. The deck is live in under 60 seconds.

---

## Regeneration Template

If the user wants to rebuild or customise the deck, use `frontend-slides` skill with these parameters:

- **Topic**: Claude Code — Skills, Sub Agents, Hooks, Multi-Agent Systems
- **Audience**: Product managers and non-engineers
- **Slides**: 11
- **Style**: Bold Signal (dark bg #080810, orange accent #f5a623, diagonal geometric shapes, Helvetica)
- **Vibe**: Impressed / Confident

Follow the slide outline above as the content structure. Every slide must:
- Have a **one-insight headline** (not a topic label)
- Fit entirely within `100vh` — no scrolling
- Use `clamp()` for all font sizes
- Include speaker notes in `data-notes` attribute

---

## Bold Signal Design Reference

```css
/* Core palette */
--bg:      #080810;
--accent:  #f5a623;
--accent2: #f04e23;
--text:    #ffffff;
--muted:   rgba(255,255,255,0.5);

/* Background shape (right diagonal) */
position: absolute; top: -25%; right: -8%; width: 52%; height: 140%;
background: linear-gradient(145deg, #f5a623, #f04e23);
clip-path: polygon(22% 0%, 100% 0%, 100% 100%, 0% 100%);
opacity: 0.09;

/* Typography */
h1: clamp(2.4rem, 5.5vw, 5.2rem) — weight 900 — tracking -0.035em
h2: clamp(1.6rem, 3vw, 2.8rem)   — weight 800 — tracking -0.025em
body: clamp(0.9rem, 1.5vw, 1.15rem) — weight 300 — muted white
kicker: clamp(0.55rem, 1vw, 0.75rem) — all-caps — letter-spacing 0.32em — orange
```

---

## Live Demo

Deployed at: **https://claude-deck.vercel.app**
