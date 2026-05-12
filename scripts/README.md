# scripts/

Utility scripts that support the course but aren't tied to a specific module.

## anthropic_watcher.py — Anthropic Daily Brief

Pulls the last 30 days of Anthropic announcements, research, blog posts, Claude Code releases, and doc-page updates, then emails you a styled HTML digest. Runs automatically every morning at **7 AM ET** via GitHub Actions, plus any time during the day when new items appear.

### What you get in each email

- **Headline:** "N new updates" or "Nothing new today"
- **TL;DR:** 2-3 sentence AI summary (requires `ANTHROPIC_API_KEY`)
- **Categorized sections:** News, Research, Engineering, Code Releases, Docs
- **Per-item flags:**
  - Blue dot = new since last brief
  - Gold star = matched an importance keyword (launch / release / new model / pricing / partnership / SDK / etc.)

### Sources

| Source | URL | Type |
|---|---|---|
| Anthropic News | RSS via `Olshansk/rss-feeds` | feed |
| Anthropic Research | RSS via `Olshansk/rss-feeds` | feed |
| Anthropic Engineering Blog | RSS via `Olshansk/rss-feeds` | feed |
| Claude Code Releases | `github.com/anthropics/claude-code/releases.atom` | feed |
| Claude API Release Notes | `docs.claude.com/en/release-notes/api` | hash-watched page |
| Claude App Release Notes | `docs.claude.com/en/release-notes/claude-apps` | hash-watched page |

The Claude App Release Notes page sits behind Cloudflare and may 403 from cloud runners. The script logs a warning and keeps going — the other five sources always work.

---

## Setup: GitHub Actions (recommended)

### 1. Create a Gmail App Password

Gmail blocks regular passwords from scripts. Generate an App Password:

1. Go to https://myaccount.google.com/apppasswords
2. Sign in if prompted. App Passwords require 2FA to be on.
3. Name it "Anthropic Watcher" and click **Create**.
4. Copy the 16-character password (spaces don't matter).

### 2. Add GitHub repo secrets

In this repo, go to **Settings -> Secrets and variables -> Actions -> New repository secret** and add:

| Secret name | Value |
|---|---|
| `SMTP_USER` | your Gmail address (e.g. `you@gmail.com`) |
| `SMTP_PASS` | the 16-char App Password from step 1 |
| `EMAIL_TO` | where the brief should arrive |
| `EMAIL_FROM` | usually same as `SMTP_USER` (optional) |
| `ANTHROPIC_API_KEY` | from https://console.anthropic.com/ (optional, enables TL;DR) |

### 3. Enable the workflow

The workflow file is at `.github/workflows/anthropic-daily-brief.yml`. After merging this branch:

- **Hourly cron** runs at the top of every hour (UTC).
- **7 AM ET hour** forces a full brief, even if nothing is new.
- **Other hours** only send when new items are detected.
- When new items are detected, the state file `scripts/.watcher_state.json` is committed back to the repo — that's why you may see chore commits from `github-actions[bot]`.

### 4. Test it manually

Go to **Actions -> Anthropic Daily Brief -> Run workflow** in GitHub. Leave "Force-send" checked and click **Run workflow**. You should get an email within a minute or two.

---

## Setup: local run (optional)

Useful for debugging or running off your laptop.

```bash
cp scripts/.env.example scripts/.env
# Fill in real values, especially SMTP_PASS
set -a; source scripts/.env; set +a
python3 scripts/anthropic_watcher.py
```

The first run snapshots existing items and sends nothing. Set `FORCE_DAILY=1` to send anyway:

```bash
FORCE_DAILY=1 python3 scripts/anthropic_watcher.py
```

State lives in `scripts/.watcher_state.json` (or wherever `STATE_FILE` points). Delete it to reset.

---

## Schedule notes

The cron expression `0 * * * *` runs every hour in UTC. Python inside the job converts to America/New_York and only force-sends during the 7 AM ET hour. This means:

- DST is handled automatically — no need to edit cron when clocks change.
- GitHub Actions cron has 5-15 min jitter under load, so "7 AM" can mean 7:05 - 7:15.
- Hourly polling makes near-real-time alerts cheap — the watcher is fast (~5s).

---

## Customizing sources

Edit `FEEDS` and `WATCH_PAGES` at the top of `anthropic_watcher.py`. The script is tolerant of dead URLs — they log a warning and the rest of the brief still goes out.

---

## Troubleshooting

**No email arrived from the 7 AM run**
Check **Actions** tab for a red X. Most common: a typo in a secret name, or your Gmail App Password expired.

**"403 Forbidden" warning in the log**
That's the Cloudflare-gated Claude App Release Notes page. Expected from cloud runners; doesn't break the brief.

**"Missing required env vars" error**
The script needs `SMTP_USER`, `SMTP_PASS`, and `EMAIL_TO` set. For GitHub Actions, these are repo secrets (see step 2 above).

**TL;DR is missing from the email**
You haven't set `ANTHROPIC_API_KEY`, or the call failed. Check the workflow log for `[warn] TL;DR ...`.

**State file commits are noisy**
That's by design — each commit records that the watcher saw something new from Anthropic. If you want fewer commits, change cron to `0 7,12,18 * * *` (three times a day instead of hourly).
