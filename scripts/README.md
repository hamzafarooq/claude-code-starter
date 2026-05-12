# scripts/

Utility scripts that support the course but aren't tied to a specific module.

## anthropic_watcher.py

Monitors Anthropic announcement sources (news, research, Claude Code releases, docs release notes, engineering blog) and emails you a digest whenever something new appears.

### How it works

- **RSS/Atom feeds** are checked per-entry. Each entry id is tracked in a local state file so you only get notified once.
- **Pages without feeds** (the engineering blog, the API and Claude apps release notes pages) are monitored by hashing their normalized HTML content. When the hash changes, you get a "page updated" notification with a link.
- The **first run** snapshots what exists today and sends no email. Only items appearing after that first snapshot trigger digests.

State is stored in `~/.anthropic_watcher_state.json`. Delete that file to reset.

### Setup

```bash
pip install feedparser
cp scripts/.env.example scripts/.env   # then fill in real values
```

If you're using Gmail, `SMTP_PASS` must be an [App Password](https://myaccount.google.com/apppasswords), not your regular account password.

Load the env file before running (or export the vars in your shell):

```bash
set -a; source scripts/.env; set +a
python scripts/anthropic_watcher.py
```

### Schedule it (cron, hourly)

```cron
0 * * * * set -a; . /path/to/claude-code-starter/scripts/.env; set +a; \
  /usr/bin/python3 /path/to/claude-code-starter/scripts/anthropic_watcher.py \
  >> /tmp/anthropic_watcher.log 2>&1
```

### Customizing sources

Edit the `FEEDS` and `WATCH_PAGES` lists at the top of `anthropic_watcher.py`. If a URL 404s or moves, just update it in place - no other changes needed.
