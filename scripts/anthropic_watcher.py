#!/usr/bin/env python3
"""
anthropic_watcher.py

Monitor Anthropic announcement sources and email a digest of new items.

Setup:
    pip install feedparser

Environment variables (required):
    SMTP_USER       SMTP username (e.g. your Gmail address)
    SMTP_PASS       SMTP password or app password
    EMAIL_TO        Where to send digests

Optional:
    SMTP_HOST       Default: smtp.gmail.com
    SMTP_PORT       Default: 587
    EMAIL_FROM      Default: SMTP_USER

Run:
    python anthropic_watcher.py

Schedule (cron, hourly):
    0 * * * * /usr/bin/python3 /path/to/anthropic_watcher.py >> /tmp/anthropic_watcher.log 2>&1

State is stored in ~/.anthropic_watcher_state.json. Delete it to start fresh.
The very first run records what currently exists and sends no email - only
items appearing AFTER that snapshot will trigger digests.
"""

import feedparser
import smtplib
import json
import os
import re
import sys
import hashlib
import urllib.request
from email.message import EmailMessage
from pathlib import Path
from datetime import datetime

# ----- Sources -----

# RSS / Atom feeds (preferred - structured, per-item)
FEEDS = [
    ("Anthropic News",
     "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_news.xml"),
    ("Anthropic Research",
     "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_research.xml"),
    ("Claude Code Releases",
     "https://github.com/anthropics/claude-code/releases.atom"),
    ("Claude Code Changelog",
     "https://claude-code-changelog-rss.stevenmenke.workers.dev/feed.xml"),
]

# Pages without feeds - monitored via content hash.
# If a URL 404s or moves, just update it here.
WATCH_PAGES = [
    ("Anthropic Engineering Blog", "https://www.anthropic.com/engineering"),
    ("Claude API Release Notes",   "https://docs.claude.com/en/release-notes/api"),
    ("Claude App Release Notes",   "https://docs.claude.com/en/release-notes/claude-apps"),
]

STATE_FILE = Path.home() / ".anthropic_watcher_state.json"
USER_AGENT = "Mozilla/5.0 (anthropic-watcher)"
HTTP_TIMEOUT = 30


# ----- SMTP config -----

def smtp_config():
    try:
        return {
            "host": os.environ.get("SMTP_HOST", "smtp.gmail.com"),
            "port": int(os.environ.get("SMTP_PORT", "587")),
            "user": os.environ["SMTP_USER"],
            "password": os.environ["SMTP_PASS"],
            "from": os.environ.get("EMAIL_FROM", os.environ["SMTP_USER"]),
            "to": os.environ["EMAIL_TO"],
        }
    except KeyError as e:
        sys.exit(f"Missing required env var: {e}. See script header for setup.")


# ----- State -----

def load_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except json.JSONDecodeError:
            pass
    return {"seen_entries": {}, "page_hashes": {}}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True))


# ----- Feed polling -----

def check_feeds(state):
    new_items = []
    seen = state.setdefault("seen_entries", {})
    for name, url in FEEDS:
        try:
            feed = feedparser.parse(url, request_headers={"User-Agent": USER_AGENT})
        except Exception as e:
            print(f"[warn] {name}: {e}")
            continue
        for entry in feed.entries:
            entry_id = entry.get("id") or entry.get("link")
            if not entry_id or entry_id in seen:
                continue
            seen[entry_id] = datetime.utcnow().isoformat()
            new_items.append({
                "source":    name,
                "title":     entry.get("title", "(untitled)"),
                "link":      entry.get("link", ""),
                "summary":   entry.get("summary", ""),
                "published": entry.get("published", ""),
            })
    return new_items


# ----- Page hash polling -----

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as r:
        return r.read().decode("utf-8", errors="replace")


def normalize_html(html):
    # Strip noisy bits, then collapse whitespace, so the hash is stable across
    # cache-busting tokens, timestamps, etc.
    text = re.sub(r"<(script|style|noscript)[^>]*>.*?</\1>", "", html, flags=re.DOTALL | re.I)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def check_pages(state):
    new_items = []
    hashes = state.setdefault("page_hashes", {})
    for name, url in WATCH_PAGES:
        try:
            html = fetch(url)
        except Exception as e:
            print(f"[warn] {name}: {e}")
            continue
        digest = hashlib.sha256(normalize_html(html).encode("utf-8")).hexdigest()
        previous = hashes.get(url)
        if previous and previous != digest:
            new_items.append({
                "source":    name,
                "title":     f"{name} updated",
                "link":      url,
                "summary":   "Page content changed since last check.",
                "published": "",
            })
        hashes[url] = digest
    return new_items


# ----- Email -----

def clean_text(s, max_len=400):
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = re.sub(r"\s+", " ", s).strip()
    return s[:max_len]


def render_email(items):
    lines = [f"{len(items)} new item(s) from Anthropic sources:\n"]
    for it in items:
        lines.append(f"- [{it['source']}] {it['title']}")
        if it.get("published"):
            lines.append(f"    {it['published']}")
        if it.get("link"):
            lines.append(f"    {it['link']}")
        summary = clean_text(it.get("summary", ""))
        if summary:
            lines.append(f"    {summary}")
        lines.append("")
    return "\n".join(lines)


def send_email(cfg, items):
    msg = EmailMessage()
    msg["Subject"] = f"Anthropic updates - {len(items)} new"
    msg["From"] = cfg["from"]
    msg["To"] = cfg["to"]
    msg.set_content(render_email(items))
    with smtplib.SMTP(cfg["host"], cfg["port"]) as s:
        s.starttls()
        s.login(cfg["user"], cfg["password"])
        s.send_message(msg)


# ----- Main -----

def main():
    state = load_state()
    first_run = not state.get("seen_entries") and not state.get("page_hashes")

    new_items = check_feeds(state) + check_pages(state)
    save_state(state)

    if first_run:
        print(f"[init] Snapshotted {len(new_items)} existing items. No email sent.")
        return

    if not new_items:
        print("[ok] No new items.")
        return

    cfg = smtp_config()
    send_email(cfg, new_items)
    print(f"[ok] Sent email with {len(new_items)} item(s).")


if __name__ == "__main__":
    main()
