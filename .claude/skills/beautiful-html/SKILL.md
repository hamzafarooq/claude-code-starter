---
name: beautiful-html
description: Turn any document, proposal, report, or outline into a stunning single-file HTML presentation using 34 pre-built professional templates. Use when the user wants to convert a markdown file, proposal, or written content into a beautiful visual HTML document ready to share or convert to PDF.
---

# Beautiful HTML

Convert any written content into a polished, single-file HTML presentation using templates from the [beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates) library.

## Template Library

34 templates available. Key ones by use case:

| Use Case | Template | Style | Raw URL |
|---|---|---|---|
| B2B proposals, consulting, investor updates | `blue-professional` | Light / Cobalt Blue | https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/templates/blue-professional/template.html |
| Investor decks, board presentations | `signal` | Mixed / Navy & Gold | https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/templates/signal/template.html |
| White papers, research, policy briefs | `monochrome` | Light / Black & White | https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/templates/monochrome/template.html |
| Investment theses, research reports | `cartesian` | Light / Neutral Warm | https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/templates/cartesian/template.html |
| Leadership presentations, strategy | `emerald-editorial` | Mixed / Emerald-Navy | https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/templates/emerald-editorial/template.html |
| Research findings, white papers | `vellum` | Dark / Navy & Gold | https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/templates/vellum/template.html |
| Design reports, studio annuals | `cobalt-grid` | Light / Cobalt Blue | https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/templates/cobalt-grid/template.html |
| Startup pitches, founder presentations | `raw-grid` | Light / Multi | https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/templates/raw-grid/template.html |
| Quarterly reviews, studio updates | `editorial-forest` | Mixed / Forest Green | https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/templates/editorial-forest/template.html |
| Design studios, creative agencies | `studio` | Dark / Electric Yellow | https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/templates/studio/template.html |

Full list of all 34 templates at: https://github.com/zarazhangrui/beautiful-html-templates

---

## Workflow

### Phase 1 — Gather Content

Ask the user:
1. "What's the content? (paste text, share a .md file path, or describe what to build)"
2. "What's the purpose? (proposal, report, pitch, research, internal update)"
3. "Who's the audience?"

If a file path is provided, read it. If it's a markdown proposal, parse it into sections.

---

### Phase 2 — Template Selection

Based on the purpose and audience, recommend 3 templates from the library above with a one-line reason for each. Show them as options (A, B, C).

For professional B2B proposals → default recommend `blue-professional`, `signal`, `cartesian`.
For research/reports → default recommend `monochrome`, `vellum`, `cartesian`.
For creative/agency → default recommend `studio`, `editorial-forest`, `cobalt-grid`.

Wait for the user to pick one — or auto-select if they say "you choose."

---

### Phase 3 — Fetch Template

Use WebFetch to retrieve the raw HTML template from GitHub:

```
WebFetch: https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/templates/<template-name>/template.html
```

Read the template structure carefully:
- Identify all slide layout types available (cover, content, metrics, quote, split, timeline, etc.)
- Note the CSS variable names for colors and fonts
- Identify placeholder text patterns to replace

---

### Phase 4 — Populate Content

Map the user's content onto the template's slide layouts:

**Mapping rules:**
- Cover slide → title, subtitle, date, submitted by
- Agenda slide → top-level sections as bullet list
- Content slides → one section per slide, headline = the key insight (not the topic label)
- Metrics slide → any numbers, KPIs, success metrics
- Quote slide → testimonials, key statements, pull quotes
- Split slide → before/after, problem/solution, two-column comparisons
- Timeline slide → roadmaps, horizons, phased plans
- Table slide → pricing, commercials, structured breakdowns

**Content rules:**
- Every slide headline = one complete insight
  - Bad: "Section 3"
  - Good: "90% of the team will have a live AI agent in production by month six"
- Never dump raw sections — rewrite as slide-friendly statements
- Keep bullets to 4–5 max per slide
- Numbers and metrics get their own slide

Replace all placeholder text in the template HTML with the user's actual content. Preserve all CSS, JS, navigation, and structure — only change the text content and optionally adjust CSS color variables if needed to better match the client's brand.

---

### Phase 5 — Save and Open

Save the populated HTML file with a descriptive filename (e.g. `sb-ai-proposal.html`).

Offer to:
- **Convert to PDF** using Playwright:
  ```bash
  npx playwright install chromium --with-deps
  node -e "
  const { chromium } = require('playwright');
  (async () => {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    await page.setViewportSize({ width: 1280, height: 720 });
    await page.goto('file://' + require('path').resolve('<filename>.html'));
    const slideCount = await page.evaluate(() => document.querySelectorAll('.slide').length);
    await page.pdf({
      path: '<filename>.pdf',
      width: '1280px',
      height: '720px',
      printBackground: true,
      pageRanges: '1-' + slideCount
    });
    await browser.close();
    console.log('Saved: <filename>.pdf');
  })();
  "
  ```
- **Deploy to Vercel** for a shareable link

---

## Source

Templates from [beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates) by Zara Zhang Rui. MIT licensed.
