---
name: md-to-pdf
description: Convert any markdown file to a clean PDF. Use when asked to make a PDF from a .md file, export a document, or convert markdown to PDF.
---

When the user asks to convert a markdown file to PDF, follow these steps exactly:

## Step 1 — Confirm the input file

Ask the user for the path to the `.md` file if not already provided. Confirm the output PDF path (default: same folder, same name, `.pdf` extension).

## Step 2 — Convert markdown to styled HTML

Run this command (replace INPUT and OUTPUT paths):

```bash
pandoc "INPUT.md" \
  -o "OUTPUT.html" \
  --standalone \
  --metadata title="Document" \
  --css=/dev/stdin <<'EOF'
body { font-family: "Helvetica Neue", Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 0 40px; font-size: 13px; line-height: 1.7; color: #1a1a1a; }
h1 { font-size: 26px; font-weight: 700; margin-bottom: 4px; }
h2 { font-size: 16px; font-weight: 700; margin-top: 32px; border-bottom: 1px solid #e0e0e0; padding-bottom: 6px; }
strong { font-weight: 600; }
table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 12px; }
th { background: #f5f5f5; padding: 8px; text-align: left; border: 1px solid #ddd; }
td { padding: 8px; border: 1px solid #ddd; }
hr { border: none; border-top: 1px solid #e0e0e0; margin: 24px 0; }
ul, ol { padding-left: 20px; }
li { margin-bottom: 6px; }
EOF
```

## Step 3 — Print HTML to PDF using Chrome

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --no-sandbox \
  --print-to-pdf="OUTPUT.pdf" \
  --print-to-pdf-no-header \
  --no-pdf-header-footer \
  "file://OUTPUT.html"
```

Note: encode spaces in the file path as `%20` in the `file://` URL.

## Step 4 — Clean up and confirm

Delete the intermediate HTML file:

```bash
rm "OUTPUT.html"
```

Tell the user the PDF is ready and give them the full path.

## Requirements

- `pandoc` must be installed (`which pandoc` to check)
- Google Chrome must be at `/Applications/Google Chrome.app/` (standard Mac install)
- Works on macOS only in this configuration

## Error handling

- If `pandoc` is not found: tell the user to run `brew install pandoc`
- If Chrome is not at the expected path: check with `ls /Applications/ | grep -i chrome` and adjust the path
- If the PDF is 0 bytes: the `file://` URL likely has unencoded spaces — encode them as `%20`
