---
name: slides-builder
description: Generate a complete HTML slide deck from a topic, bullet list, or document. McKinsey-style — one insight per slide, no filler. Use when the user wants to build a presentation, pitch deck, or teaching slide deck.
---

Ask the user:
1. "What's the topic and what's the goal of this deck? (e.g. pitch to investors, teach a concept, quarterly review)"
2. "Who is the audience and how much do they already know?"
3. "How many slides — and do you want speaker notes?"
4. "Paste any source material: bullets, doc, outline."

Then produce a complete single-file HTML presentation:

**Slide structure (McKinsey rules):**
- Every slide has exactly one headline that is a complete insight, not a topic label
  - Bad: "Market Opportunity"
  - Good: "The $4B SMB payroll market is 80% undigitized — and no one owns it"
- Body supports the headline — doesn't repeat it
- Max 5 bullets per slide, max 8 words per bullet
- No decorative transitions

**Required slides:**
1. Title slide — punchy, specific
2. Agenda / flow (for decks over 10 slides)
3. Content slides — one insight each
4. Summary / So what — what should the audience do or believe now?

**HTML requirements:**
- Full self-contained HTML (no external dependencies)
- Keyboard navigation: arrow keys advance/go back
- Clean, minimal design — dark background or white, your call
- Progress indicator
- Speaker notes in a hidden div (shown with `N` key if requested)

Output the complete HTML file ready to open in a browser.
