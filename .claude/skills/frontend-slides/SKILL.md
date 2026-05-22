---
name: frontend-slides
description: Create stunning, animation-rich single-file HTML presentations from scratch or by converting a PowerPoint (.pptx) file. Use when the user wants to build a presentation, convert a PPT to web format, or create slides for a talk, pitch, or demo. Shows 3 visual style previews before building the full deck — no design experience needed.
---

# Frontend Slides

Create zero-dependency, animation-rich HTML presentations that run entirely in the browser.

## Core Principles

1. **Zero Dependencies** — Single HTML files with inline CSS/JS. No npm, no build tools.
2. **Show, Don't Tell** — Generate 3 visual previews before building. People discover what they want by seeing options, not describing them.
3. **Distinctive Design** — No generic slides. Every presentation must feel custom-crafted.
4. **Viewport Fitting (NON-NEGOTIABLE)** — Every slide MUST fit exactly within 100vh. No scrolling within slides ever. Content overflows? Split into multiple slides.

---

## Workflow

### Phase 1 — Gather Content

Ask the user:
1. "What's the topic and goal? (e.g. investor pitch, product demo, teaching a concept)"
2. "Who is the audience?"
3. "How many slides roughly?"
4. "Paste your content, bullets, or outline — OR share a .pptx file path to convert."

If a `.pptx` file is provided → jump to **Phase 4 (PowerPoint Conversion)** first, then return here.

---

### Phase 2 — Style Selection (Always Do This)

Ask the user their vibe (multiselect, max 2):
- Impressed / Confident
- Excited / Energized
- Calm / Focused
- Inspired / Moved

Map their vibe to 3 distinct presets from this list and generate one single-slide HTML preview for each:

| Preset | Feel |
|---|---|
| Bold Signal | Dark, high-contrast, confident |
| Electric Studio | Vibrant neon on dark, energized |
| Dark Botanical | Dark with organic texture, calm authority |
| Notebook Tabs | Light, handwritten-feel, approachable |
| Pastel Geometry | Soft colors, geometric shapes, friendly |
| Neon Cyber | Cyberpunk grid, glowing text, futuristic |
| Creative Voltage | Bold gradients, dynamic diagonals |
| Split Pastel | Two-tone split layout, modern editorial |
| Paper & Ink | Cream background, serif type, classic |
| Swiss Modern | Brutalist grid, red + black, no-nonsense |
| Vintage Editorial | Magazine-style, muted tones, typographic |
| Minimal Zen | White space, single accent color, clean |

Save 3 preview files to `.claude-design/slide-previews/` as `style-a.html`, `style-b.html`, `style-c.html` and open them.

Wait for the user to pick one (A, B, or C) — or ask to mix elements from two.

---

### Phase 3 — Build the Full Deck

Using the chosen style, generate the complete single-file HTML presentation.

**Slide structure rules:**
- Every slide headline = one complete insight, not a topic label
  - Bad: "Market Opportunity"
  - Good: "The $4B SMB payroll market is 80% undigitized"
- Body supports the headline — never repeats it
- Max bullets/content per slide type:

| Slide Type | Maximum Content |
|---|---|
| Title | 1 heading + 1 subtitle + optional tagline |
| Content | 1 heading + 4–6 bullets OR 2 paragraphs |
| Feature grid | 1 heading + 6 cards max (2×3 or 3×2) |
| Code | 1 heading + 8–10 lines of code |
| Quote | 1 quote (max 3 lines) + attribution |
| Image | 1 heading + 1 image (max 60vh) |

**Required slides:**
1. Title slide
2. Agenda (for decks over 8 slides)
3. Content slides
4. Summary / So what

**HTML requirements:**
- Fully self-contained — no external CDN, no imports
- Keyboard navigation: arrow keys + spacebar
- Progress indicator
- Speaker notes in hidden `<div>` (toggle with `N` key)
- `prefers-reduced-motion` support

**Viewport fitting (mandatory):**
- Every `.slide`: `height: 100vh; height: 100dvh; overflow: hidden;`
- All font sizes: `clamp(min, preferred, max)` — never fixed px/rem
- Images: `max-height: min(50vh, 400px)`
- Media breakpoints at 700px, 600px, 500px height
- Never negate CSS functions directly — use `calc(-1 * clamp(...))`

Output the complete HTML file. Default filename: `presentation.html`.

---

### Phase 4 — PowerPoint Conversion (if .pptx provided)

1. Run the extractor (auto-installs `python-pptx` if needed):
   ```bash
   pip install python-pptx -q
   python -c "
   from pptx import Presentation
   import json, sys
   prs = Presentation(sys.argv[1])
   slides = []
   for i, slide in enumerate(prs.slides):
       texts = [shape.text for shape in slide.shapes if shape.has_text_frame]
       slides.append({'slide': i+1, 'content': texts})
   print(json.dumps(slides, indent=2))
   " <path_to_pptx>
   ```
2. Confirm extracted slide titles, content summaries, and image counts with the user.
3. Proceed to Phase 2 for style selection.
4. Generate HTML preserving all text, slide order, and speaker notes (as HTML comments).

---

## Optional Post-Build

**Deploy to Vercel** (requires Node + Vercel CLI):
```bash
vercel deploy ./presentation.html
```

**Export to PDF** (requires Node + Playwright):
```bash
npx playwright install chromium --with-deps
node -e "
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + require('path').resolve('presentation.html'));
  await page.pdf({ path: 'presentation.pdf', printBackground: true });
  await browser.close();
  console.log('Saved: presentation.pdf');
})();
"
```

---

## Source

Based on [frontend-slides](https://github.com/zarazhangrui/frontend-slides) by Zara Zhang Rui.
