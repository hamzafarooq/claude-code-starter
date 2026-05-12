# scripts/

Utility scripts that support the course but aren't tied to a specific module.

## anthropic_watcher.py — Anthropic Daily Brief

Pulls the last 30 days of Anthropic announcements, research, blog posts, Claude Code releases, and doc-page updates, then emails you a styled HTML digest. Runs every hour via GitHub Actions:

- **7 AM ET, daily** — always sends a full brief, even if nothing is new.
- **7 AM ET, Friday** — also sends a separate weekly themes email.
- **Any hour with a saved-search match** — sends a focused alert email.
- **Any hour with new items** — sends the daily brief immediately, not waiting for the morning.

Each brief is also archived to `docs/briefs/<date>.html` with an index page, so you can host it on GitHub Pages and search past briefs.

---

### What you get in each daily email

- **Headline:** "N new updates" or "Nothing new today"
- **AI TL;DR:** 2-3 sentence summary (requires `ANTHROPIC_API_KEY`)
- **Categorized sections:** News, Research, Engineering, Code Releases, Docs
- **Per-item flags:**
  - Blue dot = new since last brief
  - Gold star = keyword match (launch / release / pricing / etc.)
  - `MAJOR` / `MINOR` / `ROUTINE` badge = LLM-judged magnitude
  - "Why it matters" deep summary on new items (capped at 10 per brief)

### What you get in saved-search alerts

- One email per hour where a new item matched. Subject: `[Alert] N new matches from saved searches`.
- Body shows label, title, source, date, summary, and link for each match.
- Each item alerts only once (tracked in state).

### What you get in the weekly themes email

- Friday 7 AM ET, in addition to the daily brief.
- 3-5 LLM-clustered themes from the past 7 days, each with a 2-3 sentence summary and the list of items in that theme.

---

### Sources

| Source | URL | Type |
|---|---|---|
| Anthropic News | RSS via `Olshansk/rss-feeds` | feed |
| Anthropic Research | RSS via `Olshansk/rss-feeds` | feed |
| Anthropic Engineering Blog | RSS via `Olshansk/rss-feeds` | feed |
| Claude Code Releases | `github.com/anthropics/claude-code/releases.atom` | feed |
| Claude API Release Notes | `docs.claude.com/en/release-notes/api` | hash-watched page |
| Claude App Release Notes | `docs.claude.com/en/release-notes/claude-apps` | hash-watched page |

The Claude App Release Notes page sits behind Cloudflare and may 403 from cloud runners. The script logs a warning and keeps going.

---

## Setup: GitHub Actions (recommended)

### 1. Create a Gmail App Password

1. https://myaccount.google.com/apppasswords (requires 2FA)
2. Name it "Anthropic Watcher" → **Create**
3. Copy the 16-character password.

### 2. Add GitHub repo secrets

**Settings → Secrets and variables → Actions → New repository secret:**

| Secret | Value |
|---|---|
| `SMTP_USER` | your Gmail address |
| `SMTP_PASS` | the 16-char app password |
| `EMAIL_TO` | where the brief should arrive |
| `EMAIL_FROM` | usually same as `SMTP_USER` (optional) |
| `ANTHROPIC_API_KEY` | from console.anthropic.com (optional but enables TL;DR, magnitude tags, deep summaries, weekly themes) |

### 3. Test it manually

**Actions → Anthropic Daily Brief → Run workflow.** Leave "force daily" checked. Email should arrive within ~1 minute.

### 4. (Optional) Enable GitHub Pages for the archive

**Settings → Pages → Source: Deploy from a branch → Branch: `main`, Folder: `/docs`.** Your archive index will be live at `https://<your-org>.github.io/<repo>/briefs/`.

---

## Setup: local run

```bash
cp scripts/.env.example scripts/.env
# fill in real values
set -a; source scripts/.env; set +a
FORCE_DAILY=1 python3 scripts/anthropic_watcher.py
```

State lives in `scripts/.watcher_state.json`. Delete to reset.

---

## Customization

### Mute sources or add saved searches

Edit `scripts/watcher_config.py`:

```python
SOURCE_TOGGLES = {
    "News":          True,
    "Research":      True,
    "Engineering":   False,   # mute the engineering blog
    "Code Releases": True,
    "Docs":          True,
}

SAVED_SEARCHES = [
    ("Pricing changes",  r"\bpricing|price\b"),
    ("Opus model news",  r"\bopus\b"),
]
```

Patterns are case-insensitive regex. Each matched new item triggers one alert email; alerts are deduplicated via the state file.

### Change the model or limits

Also in `watcher_config.py`:

```python
DEEP_SUMMARY_LIMIT = 10                       # cap on per-brief deep summaries
LLM_MODEL          = "claude-haiku-4-5-20251001"  # bump to sonnet for richer prose
ARCHIVE_DIR        = "docs/briefs"            # set None to disable archive
```

### Change schedule frequency

Cron is hourly by default. To run less often, edit `.github/workflows/anthropic-daily-brief.yml`:

```yaml
- cron: "0 7,12,18 * * *"   # three times a day instead of hourly
```

---

## Troubleshooting

**No email arrived from the 7 AM run**
Check the **Actions** tab. Common: typo in a secret, expired Gmail App Password, or `EMAIL_TO` is wrong.

**"403 Forbidden" warning in the log**
Expected for the Cloudflare-gated Claude App Release Notes page. Doesn't break the brief.

**TL;DR / magnitude / deep summaries are missing**
`ANTHROPIC_API_KEY` is not set, or the API call failed. Check the workflow log for `[warn] LLM ...`. The brief still sends without LLM enrichment.

**State / archive commits are noisy**
Each hour where anything changes produces one commit. To reduce, change cron to fewer hours or move the archive to a `gh-pages` orphan branch.

**Saved-search alert didn't fire**
Verify the pattern matches title or summary text (not the URL). Test the regex with `python3 -c "import re; print(re.search(r'YOUR_PATTERN', 'sample title', re.I))"`. Each item alerts only once — to retest, delete the item's id from `alerted_entries` in the state file.
