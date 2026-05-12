#!/usr/bin/env python3
"""
anthropic_watcher.py - Daily Anthropic brief

Pulls the last 30 days from RSS/Atom feeds, watches a few doc pages by
content hash, composes a categorized HTML email with an optional AI TL;DR,
and emails it via Gmail SMTP.

Behavior:
- FORCE_DAILY=1     -> always send the brief, even if nothing is new.
- otherwise         -> only send when new items are detected.

Required env vars:
    SMTP_USER, SMTP_PASS, EMAIL_TO

Optional env vars:
    SMTP_HOST (default smtp.gmail.com)
    SMTP_PORT (default 587)
    EMAIL_FROM (default SMTP_USER)
    ANTHROPIC_API_KEY (enables AI TL;DR)
    STATE_FILE (default scripts/.watcher_state.json)
    FORCE_DAILY (1 = always send)
    LOOKBACK_DAYS (default 30)
"""

import hashlib
import html
import json
import os
import re
import smtplib
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.message import EmailMessage
from email.utils import parsedate_to_datetime
from pathlib import Path
from zoneinfo import ZoneInfo

# ----- Sources -----

FEEDS = [
    ("News",          "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_news.xml"),
    ("Research",      "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_research.xml"),
    ("Engineering",   "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_engineering.xml"),
    ("Code Releases", "https://github.com/anthropics/claude-code/releases.atom"),
]

WATCH_PAGES = [
    ("Claude API Release Notes", "https://docs.claude.com/en/release-notes/api"),
    ("Claude App Release Notes", "https://docs.claude.com/en/release-notes/claude-apps"),
]

SECTION_ORDER = ["News", "Research", "Engineering", "Code Releases", "Docs"]
SECTION_COLORS = {
    "News":          "#0f62fe",
    "Research":      "#8a3ffc",
    "Engineering":   "#1192e8",
    "Code Releases": "#198038",
    "Docs":          "#6f6f6f",
}

LOOKBACK_DAYS = int(os.environ.get("LOOKBACK_DAYS", "30"))
STATE_FILE = Path(os.environ.get("STATE_FILE", "scripts/.watcher_state.json"))
USER_AGENT = "Mozilla/5.0 (anthropic-daily-brief)"
HTTP_TIMEOUT = 30

IMPORTANT_RE = re.compile(
    r"\b(launch(?:ed|es|ing)?|releas(?:ed|es|ing|e)?|"
    r"introduc(?:ed|es|ing|e)?|announc(?:ed|es|ing|e)?|"
    r"new model|claude (?:opus|sonnet|haiku)\s*\d|"
    r"pricing|sdk|new feature|partnership)\b",
    re.I,
)


# ----- HTTP / parsing -----

def fetch(url, timeout=HTTP_TIMEOUT):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def strip_ns(tag):
    return tag.split("}", 1)[-1] if "}" in tag else tag


def parse_dt(s):
    if not s:
        return None
    s = s.strip()
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        pass
    try:
        dt = parsedate_to_datetime(s)
        if dt and dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        return None


def extract_items(xml_bytes):
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return []
    items = []
    for it in root.iter():
        if strip_ns(it.tag) not in ("item", "entry"):
            continue
        data = {"id": "", "title": "", "link": "", "published": "", "summary": ""}
        for child in it:
            tag = strip_ns(child.tag)
            text = (child.text or "").strip()
            if tag == "title" and text:
                data["title"] = text
            elif tag == "link":
                href = child.attrib.get("href")
                if href:
                    data["link"] = href
                elif text:
                    data["link"] = text
            elif tag == "id" and text and not data["id"]:
                data["id"] = text
            elif tag == "guid" and text and not data["id"]:
                data["id"] = text
            elif tag in ("pubDate", "published", "updated") and text and not data["published"]:
                data["published"] = text
            elif tag in ("summary", "description", "content") and text and not data["summary"]:
                data["summary"] = text
        data["id"] = data["id"] or data["link"] or data["title"]
        data["dt"] = parse_dt(data["published"])
        items.append(data)
    return items


def normalize_html(html_str):
    text = re.sub(r"<(script|style|noscript)[^>]*>.*?</\1>", "", html_str, flags=re.DOTALL | re.I)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def clean_text(s, max_len=300):
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = re.sub(r"\s+", " ", s).strip()
    return s[:max_len]


def is_important(item):
    return bool(IMPORTANT_RE.search(f"{item.get('title','')} {clean_text(item.get('summary',''))}"))


# ----- State -----

def load_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except json.JSONDecodeError:
            pass
    return {"seen_entries": {}, "page_hashes": {}}


def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True))


# ----- Collection -----

def collect_feed_items(state):
    """Returns (items_in_lookback_window, newly_seen_items)."""
    seen = state.setdefault("seen_entries", {})
    cutoff = datetime.now(timezone.utc) - timedelta(days=LOOKBACK_DAYS)
    now_iso = datetime.now(timezone.utc).isoformat()
    window_items = []
    new_items = []
    for source, url in FEEDS:
        try:
            raw = fetch(url)
        except Exception as e:
            print(f"[warn] feed {source}: {e}", file=sys.stderr)
            continue
        for item in extract_items(raw):
            item["source"] = source
            in_window = bool(item["dt"] and item["dt"] >= cutoff)
            if in_window:
                window_items.append(item)
            if item["id"] and item["id"] not in seen and in_window:
                new_items.append(item)
            if item["id"]:
                seen.setdefault(item["id"], now_iso)
    return window_items, new_items


def collect_page_changes(state):
    """Returns list of changed-page items (treated as new docs updates)."""
    hashes = state.setdefault("page_hashes", {})
    out = []
    now = datetime.now(timezone.utc)
    for name, url in WATCH_PAGES:
        try:
            raw = fetch(url).decode("utf-8", errors="replace")
        except Exception as e:
            print(f"[warn] page {name}: {e}", file=sys.stderr)
            continue
        digest = hashlib.sha256(normalize_html(raw).encode("utf-8")).hexdigest()
        prev = hashes.get(url)
        if prev and prev != digest:
            out.append({
                "source":    "Docs",
                "title":     f"{name} updated",
                "link":      url,
                "published": now.isoformat(),
                "dt":        now,
                "summary":   "Page content changed since last check.",
                "id":        f"page::{url}::{digest}",
            })
        hashes[url] = digest
    return out


# ----- AI TL;DR -----

def generate_tldr(window_items, new_items):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return None
    sample = new_items if new_items else window_items
    if not sample:
        return None
    bullets = []
    for it in sorted(sample, key=lambda x: x.get("dt") or datetime.min.replace(tzinfo=timezone.utc), reverse=True)[:30]:
        date = it["dt"].strftime("%Y-%m-%d") if it.get("dt") else "?"
        bullets.append(f"- [{it['source']}] {date}: {clean_text(it.get('title',''), 140)}")
    audience_note = (
        "There are new items today." if new_items
        else "There are no new items today; summarize the last 30 days instead."
    )
    user_prompt = (
        f"{audience_note} Write a 2-3 sentence executive TL;DR for a product manager. "
        "Highlight new model releases, major partnerships, pricing or capability changes. "
        "Skip routine version bumps. Prose only, no headers, no bullet points.\n\n"
        + "\n".join(bullets)
    )
    payload = json.dumps({
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": 400,
        "messages": [{"role": "user", "content": user_prompt}],
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            res = json.loads(r.read())
            return res["content"][0]["text"].strip()
    except urllib.error.HTTPError as e:
        print(f"[warn] TL;DR HTTP {e.code}: {e.read()[:200]!r}", file=sys.stderr)
    except Exception as e:
        print(f"[warn] TL;DR failed: {e}", file=sys.stderr)
    return None


# ----- Rendering -----

def group_by_section(items):
    grouped = {s: [] for s in SECTION_ORDER}
    for it in items:
        src = it.get("source", "Docs")
        grouped.setdefault(src, []).append(it)
    for src in grouped:
        grouped[src].sort(
            key=lambda x: x.get("dt") or datetime.min.replace(tzinfo=timezone.utc),
            reverse=True,
        )
    return grouped


def esc(s):
    return html.escape(s or "", quote=True)


def render_html(date_str, window_items, new_items, tldr, force_daily):
    new_ids = {i["id"] for i in new_items}
    grouped = group_by_section(window_items + [i for i in new_items if i not in window_items])
    new_count = len(new_items)
    total = sum(len(v) for v in grouped.values())

    if new_count > 0:
        headline = f"{new_count} new update{'s' if new_count != 1 else ''} from Anthropic"
        headline_color = "#0f62fe"
    elif force_daily:
        headline = "Nothing new today"
        headline_color = "#6f6f6f"
    else:
        headline = f"{new_count} new updates"
        headline_color = "#6f6f6f"

    parts = [
        '<!DOCTYPE html><html><head><meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1">',
        "</head>",
        '<body style="margin:0;padding:24px;background:#f4f4f4;'
        'font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,Helvetica,Arial,sans-serif;'
        'color:#161616;">',
        '<div style="max-width:680px;margin:0 auto;background:#ffffff;border-radius:8px;'
        'padding:32px;box-shadow:0 1px 3px rgba(0,0,0,0.08);">',
        f'<div style="font-size:13px;color:#6f6f6f;margin-bottom:4px;">Anthropic Daily Brief &middot; {esc(date_str)}</div>',
        f'<h1 style="margin:0 0 8px 0;font-size:22px;color:{headline_color};">{esc(headline)}</h1>',
        f'<div style="font-size:13px;color:#6f6f6f;margin-bottom:24px;">'
        f'{total} item{"s" if total != 1 else ""} in the last {LOOKBACK_DAYS} days '
        f'&middot; {new_count} new since last check</div>',
    ]

    if tldr:
        parts.append(
            '<div style="background:#f4f4f4;border-left:3px solid #0f62fe;padding:14px 18px;'
            'border-radius:4px;margin-bottom:28px;font-size:14px;line-height:1.55;">'
            '<div style="font-weight:600;font-size:12px;text-transform:uppercase;letter-spacing:0.04em;'
            'color:#0f62fe;margin-bottom:6px;">TL;DR</div>'
            f'{esc(tldr)}'
            '</div>'
        )

    for section in SECTION_ORDER:
        items = grouped.get(section, [])
        if not items:
            continue
        color = SECTION_COLORS.get(section, "#161616")
        section_new = sum(1 for i in items if i["id"] in new_ids)
        new_badge = (
            f' <span style="background:{color};color:#fff;font-size:11px;padding:2px 7px;'
            f'border-radius:10px;margin-left:6px;vertical-align:middle;">'
            f'{section_new} new</span>'
            if section_new else ""
        )
        parts.append(
            f'<h2 style="font-size:15px;margin:24px 0 10px 0;color:{color};'
            'border-bottom:1px solid #e0e0e0;padding-bottom:6px;">'
            f'{esc(section)} <span style="color:#6f6f6f;font-weight:400;">({len(items)})</span>'
            f'{new_badge}</h2>'
            '<ul style="list-style:none;padding:0;margin:0;">'
        )
        for it in items:
            date = it["dt"].strftime("%b %d") if it.get("dt") else ""
            star = '<span title="important" style="color:#f1c21b;margin-right:4px;">&#9733;</span>' if is_important(it) else ""
            is_new = it["id"] in new_ids
            new_dot = '<span style="display:inline-block;width:6px;height:6px;background:#0f62fe;border-radius:50%;margin-right:8px;vertical-align:middle;"></span>' if is_new else '<span style="display:inline-block;width:6px;margin-right:8px;"></span>'
            link = esc(it.get("link", "#"))
            title = esc(it.get("title", "(untitled)"))
            summary = clean_text(it.get("summary", ""), 200)
            parts.append(
                f'<li style="padding:8px 0;border-bottom:1px solid #f4f4f4;">'
                f'{new_dot}{star}'
                f'<a href="{link}" style="color:#161616;text-decoration:none;font-weight:600;">{title}</a>'
                f'<div style="font-size:12px;color:#6f6f6f;margin:2px 0 0 14px;">{esc(date)}</div>'
            )
            if summary:
                parts.append(
                    f'<div style="font-size:13px;color:#525252;margin:4px 0 0 14px;line-height:1.45;">{esc(summary)}</div>'
                )
            parts.append("</li>")
        parts.append("</ul>")

    parts.append(
        '<div style="margin-top:28px;padding-top:16px;border-top:1px solid #e0e0e0;'
        'font-size:11px;color:#a8a8a8;text-align:center;">'
        '&#9733; flagged as important &middot; blue dot indicates new since last brief'
        '</div>'
    )
    parts.append("</div></body></html>")
    return "".join(parts)


def render_text(date_str, window_items, new_items, tldr, force_daily):
    grouped = group_by_section(window_items + [i for i in new_items if i not in window_items])
    new_ids = {i["id"] for i in new_items}
    lines = [f"Anthropic Daily Brief - {date_str}", ""]
    if new_items:
        lines.append(f"{len(new_items)} new update(s) since last check.")
    elif force_daily:
        lines.append("Nothing new today.")
    if tldr:
        lines += ["", "TL;DR", tldr]
    for section in SECTION_ORDER:
        items = grouped.get(section, [])
        if not items:
            continue
        lines += ["", f"== {section} ({len(items)}) =="]
        for it in items:
            date = it["dt"].strftime("%Y-%m-%d") if it.get("dt") else "?"
            marker = "NEW " if it["id"] in new_ids else "    "
            star = "* " if is_important(it) else "  "
            lines.append(f"{marker}{star}[{date}] {it.get('title','(untitled)')}")
            if it.get("link"):
                lines.append(f"        {it['link']}")
    return "\n".join(lines)


# ----- Email -----

def smtp_config():
    missing = [k for k in ("SMTP_USER", "SMTP_PASS", "EMAIL_TO") if not os.environ.get(k)]
    if missing:
        sys.exit(f"Missing required env vars: {', '.join(missing)}")
    return {
        "host":     os.environ.get("SMTP_HOST", "smtp.gmail.com"),
        "port":     int(os.environ.get("SMTP_PORT", "587")),
        "user":     os.environ["SMTP_USER"],
        "password": os.environ["SMTP_PASS"],
        "from":     os.environ.get("EMAIL_FROM", os.environ["SMTP_USER"]),
        "to":       os.environ["EMAIL_TO"],
    }


def send_email(cfg, subject, text_body, html_body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = cfg["from"]
    msg["To"] = cfg["to"]
    msg.set_content(text_body)
    msg.add_alternative(html_body, subtype="html")
    with smtplib.SMTP(cfg["host"], cfg["port"]) as s:
        s.starttls()
        s.login(cfg["user"], cfg["password"])
        s.send_message(msg)


# ----- Main -----

def main():
    state = load_state()
    first_run = not state.get("seen_entries") and not state.get("page_hashes")

    window_items, new_items = collect_feed_items(state)
    page_changes = collect_page_changes(state)
    new_items.extend(page_changes)
    save_state(state)

    force_daily = os.environ.get("FORCE_DAILY", "").lower() in ("1", "true", "yes")
    et_date = datetime.now(ZoneInfo("America/New_York")).strftime("%A, %b %d, %Y")

    if first_run and not force_daily:
        print(f"[init] Snapshotted {len(window_items)} items. No email (set FORCE_DAILY=1 to override).")
        return 0

    should_send = bool(new_items) or force_daily
    if not should_send:
        print(f"[ok] No new items. Skipping email. ({len(window_items)} items in window)")
        return 0

    tldr = generate_tldr(window_items, new_items)
    html_body = render_html(et_date, window_items, new_items, tldr, force_daily)
    text_body = render_text(et_date, window_items, new_items, tldr, force_daily)

    if new_items:
        subject = f"Anthropic Daily Brief - {len(new_items)} new update{'s' if len(new_items) != 1 else ''}"
    else:
        subject = "Anthropic Daily Brief - nothing new today"

    cfg = smtp_config()
    send_email(cfg, subject, text_body, html_body)
    print(f"[ok] Sent: {subject}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
