#!/usr/bin/env python3
"""
anthropic_watcher.py - Daily Anthropic brief

Pulls the last 30 days of Anthropic announcements, research, blog posts,
and Claude Code releases. Sends:
  - Saved-search alerts at any time (one email per matched new item).
  - Full daily brief when FORCE_DAILY=1 (the workflow sets this at 7 AM ET).
  - Weekly themes email when FORCE_WEEKLY=1 (workflow: Friday 7 AM ET).

Daily brief includes: AI TL;DR, categorized sections, per-item magnitude
tags (major/minor/routine), deep-summary paragraphs for new items, and a
star for keyword-matched items.

Each brief is also saved as briefs/YYYY-MM-DD.html with an index page so
you can host an archive on GitHub Pages.

Required env vars:
    SMTP_USER, SMTP_PASS, EMAIL_TO

Optional env vars:
    SMTP_HOST (default smtp.gmail.com), SMTP_PORT (default 587),
    EMAIL_FROM (default SMTP_USER), ANTHROPIC_API_KEY (enables LLM features),
    STATE_FILE (default scripts/.watcher_state.json),
    FORCE_DAILY=1, FORCE_WEEKLY=1, LOOKBACK_DAYS (default 30).
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

sys.path.insert(0, str(Path(__file__).parent))
import watcher_config as cfg  # noqa: E402

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
MAGNITUDE_BADGE = {
    "major":   ("#da1e28", "MAJOR"),
    "minor":   ("#0f62fe", "MINOR"),
    "routine": ("#a8a8a8", "ROUTINE"),
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
    return {"seen_entries": {}, "page_hashes": {}, "alerted_entries": {}}


def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True))


# ----- Collection -----

def collect_feed_items(state):
    """Returns (items_in_lookback_window, newly_seen_items)."""
    seen = state.setdefault("seen_entries", {})
    cutoff = datetime.now(timezone.utc) - timedelta(days=LOOKBACK_DAYS)
    now_iso = datetime.now(timezone.utc).isoformat()
    window_items, new_items = [], []
    for source, url in FEEDS:
        if not cfg.SOURCE_TOGGLES.get(source, True):
            continue
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
    if not cfg.SOURCE_TOGGLES.get("Docs", True):
        return []
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


# ----- LLM helpers -----

def llm_call(prompt, max_tokens=1200, system=None):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return None
    body = {
        "model": cfg.LLM_MODEL,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }
    if system:
        body["system"] = system
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps(body).encode("utf-8"),
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            res = json.loads(r.read())
            return res["content"][0]["text"].strip()
    except urllib.error.HTTPError as e:
        print(f"[warn] LLM HTTP {e.code}: {e.read()[:200]!r}", file=sys.stderr)
    except Exception as e:
        print(f"[warn] LLM call failed: {e}", file=sys.stderr)
    return None


def _items_to_bullets(items, limit=30):
    rows = []
    for it in sorted(items, key=lambda x: x.get("dt") or datetime.min.replace(tzinfo=timezone.utc), reverse=True)[:limit]:
        date = it["dt"].strftime("%Y-%m-%d") if it.get("dt") else "?"
        summary = clean_text(it.get("summary", ""), 220)
        rows.append(f"id={it['id']} | [{it['source']}] {date} | {clean_text(it.get('title',''),140)} | {summary}")
    return "\n".join(rows)


def _extract_json(text):
    if not text:
        return None
    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError:
        return None


def analyze_items(window_items, new_items):
    """Single LLM call returning TL;DR + per-item magnitude + deep summaries.

    Returns dict: {"tldr": str, "items": {item_id: {"magnitude": str, "deep_summary": str}}}
    """
    sample = new_items if new_items else window_items
    if not sample:
        return {"tldr": None, "items": {}}
    deep_targets = sample[:cfg.DEEP_SUMMARY_LIMIT]
    deep_ids = {it["id"] for it in deep_targets}
    audience = (
        "There ARE new items today."
        if new_items
        else "There are NO new items today; summarize the last 30 days instead."
    )
    prompt = (
        f"{audience} Below are recent Anthropic items.\n\n"
        "Return strict JSON, no prose outside the JSON, with this exact shape:\n"
        '{"tldr": "2-3 sentence executive summary",\n'
        ' "items": [{"id": "...", "magnitude": "major|minor|routine", '
        '"deep_summary": "1-2 sentences explaining why this matters to a product manager"}]}\n\n'
        f"Provide magnitude for every item below. Provide deep_summary ONLY for these ids "
        f"(others can omit the field): {sorted(deep_ids)}\n\n"
        "Magnitude rubric:\n"
        " - major: new model, major product launch, pricing change, strategic partnership, policy shift.\n"
        " - minor: feature additions, blog research findings, minor product updates.\n"
        " - routine: version bumps, doc edits, small UX tweaks.\n\n"
        "Items:\n" + _items_to_bullets(sample, limit=40)
    )
    raw = llm_call(prompt, max_tokens=2000)
    parsed = _extract_json(raw)
    if not parsed:
        return {"tldr": None, "items": {}}
    out = {"tldr": parsed.get("tldr"), "items": {}}
    for entry in parsed.get("items", []):
        if not isinstance(entry, dict) or "id" not in entry:
            continue
        out["items"][entry["id"]] = {
            "magnitude": entry.get("magnitude", "routine"),
            "deep_summary": entry.get("deep_summary", ""),
        }
    return out


def weekly_themes(items_7d):
    if not items_7d:
        return None
    prompt = (
        "Cluster the items below into 3-5 themes for a weekly recap email. "
        "Return strict JSON only:\n"
        '{"themes": [{"name": "short title", "summary": "2-3 sentences", "item_ids": [list of ids]}]}\n\n'
        "Items:\n" + _items_to_bullets(items_7d, limit=80)
    )
    return _extract_json(llm_call(prompt, max_tokens=1800))


# ----- Saved-search alerts -----

def saved_search_matches(new_items, state):
    """Returns list of (label, item) for new items matching saved searches that
    haven't been alerted yet. Marks them in state."""
    if not cfg.SAVED_SEARCHES:
        return []
    alerted = state.setdefault("alerted_entries", {})
    out = []
    now_iso = datetime.now(timezone.utc).isoformat()
    for item in new_items:
        if item["id"] in alerted:
            continue
        blob = f"{item.get('title','')} {clean_text(item.get('summary',''))}"
        for label, pattern in cfg.SAVED_SEARCHES:
            try:
                if re.search(pattern, blob, flags=re.I):
                    out.append((label, item))
                    alerted[item["id"]] = now_iso
                    break
            except re.error as e:
                print(f"[warn] bad regex for '{label}': {e}", file=sys.stderr)
    return out


# ----- Rendering -----

def group_by_section(items):
    grouped = {s: [] for s in SECTION_ORDER}
    for it in items:
        grouped.setdefault(it.get("source", "Docs"), []).append(it)
    for src in grouped:
        grouped[src].sort(
            key=lambda x: x.get("dt") or datetime.min.replace(tzinfo=timezone.utc),
            reverse=True,
        )
    return grouped


def esc(s):
    return html.escape(s or "", quote=True)


def render_daily_html(date_str, window_items, new_items, analysis, force_daily):
    new_ids = {i["id"] for i in new_items}
    by_id = {it["id"]: it for it in window_items + new_items}
    combined = list(by_id.values())
    grouped = group_by_section(combined)
    item_meta = (analysis or {}).get("items", {})
    tldr = (analysis or {}).get("tldr")
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

    p = ['<!DOCTYPE html><html><head><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         f'<title>Anthropic Daily Brief - {esc(date_str)}</title></head>',
         '<body style="margin:0;padding:24px;background:#f4f4f4;'
         'font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,Helvetica,Arial,sans-serif;color:#161616;">',
         '<div style="max-width:680px;margin:0 auto;background:#ffffff;border-radius:8px;'
         'padding:32px;box-shadow:0 1px 3px rgba(0,0,0,0.08);">',
         f'<div style="font-size:13px;color:#6f6f6f;margin-bottom:4px;">Anthropic Daily Brief &middot; {esc(date_str)}</div>',
         f'<h1 style="margin:0 0 8px 0;font-size:22px;color:{headline_color};">{esc(headline)}</h1>',
         f'<div style="font-size:13px;color:#6f6f6f;margin-bottom:24px;">'
         f'{total} item{"s" if total != 1 else ""} in the last {LOOKBACK_DAYS} days '
         f'&middot; {new_count} new since last check</div>']

    if tldr:
        p.append(
            '<div style="background:#f4f4f4;border-left:3px solid #0f62fe;padding:14px 18px;'
            'border-radius:4px;margin-bottom:28px;font-size:14px;line-height:1.55;">'
            '<div style="font-weight:600;font-size:12px;text-transform:uppercase;letter-spacing:0.04em;'
            f'color:#0f62fe;margin-bottom:6px;">TL;DR</div>{esc(tldr)}</div>'
        )

    for section in SECTION_ORDER:
        items = grouped.get(section, [])
        if not items:
            continue
        color = SECTION_COLORS.get(section, "#161616")
        section_new = sum(1 for i in items if i["id"] in new_ids)
        new_badge = (
            f' <span style="background:{color};color:#fff;font-size:11px;padding:2px 7px;'
            f'border-radius:10px;margin-left:6px;vertical-align:middle;">{section_new} new</span>'
            if section_new else ""
        )
        p.append(
            f'<h2 style="font-size:15px;margin:24px 0 10px 0;color:{color};'
            f'border-bottom:1px solid #e0e0e0;padding-bottom:6px;">'
            f'{esc(section)} <span style="color:#6f6f6f;font-weight:400;">({len(items)})</span>{new_badge}</h2>'
            '<ul style="list-style:none;padding:0;margin:0;">'
        )
        for it in items:
            date = it["dt"].strftime("%b %d") if it.get("dt") else ""
            meta = item_meta.get(it["id"], {})
            mag = meta.get("magnitude", "")
            mag_badge = ""
            if mag in MAGNITUDE_BADGE:
                bg, label = MAGNITUDE_BADGE[mag]
                mag_badge = (
                    f'<span style="background:{bg};color:#fff;font-size:10px;font-weight:600;'
                    f'padding:2px 6px;border-radius:3px;margin-left:6px;letter-spacing:0.04em;">{label}</span>'
                )
            star = '<span title="important" style="color:#f1c21b;margin-right:4px;">&#9733;</span>' if is_important(it) else ""
            is_new = it["id"] in new_ids
            new_dot = (
                '<span style="display:inline-block;width:6px;height:6px;background:#0f62fe;'
                'border-radius:50%;margin-right:8px;vertical-align:middle;"></span>'
                if is_new else
                '<span style="display:inline-block;width:6px;margin-right:8px;"></span>'
            )
            link = esc(it.get("link", "#"))
            title = esc(it.get("title", "(untitled)"))
            summary = clean_text(it.get("summary", ""), 200)
            deep = meta.get("deep_summary", "")
            p.append(
                f'<li style="padding:8px 0;border-bottom:1px solid #f4f4f4;">'
                f'{new_dot}{star}<a href="{link}" style="color:#161616;text-decoration:none;font-weight:600;">{title}</a>'
                f'{mag_badge}'
                f'<div style="font-size:12px;color:#6f6f6f;margin:2px 0 0 14px;">{esc(date)}</div>'
            )
            if deep:
                p.append(
                    f'<div style="font-size:13px;color:#161616;background:#fafafa;border-left:2px solid #0f62fe;'
                    f'padding:8px 10px;margin:6px 0 0 14px;line-height:1.5;">'
                    f'<strong style="font-size:11px;color:#0f62fe;text-transform:uppercase;letter-spacing:0.04em;">'
                    f'Why it matters</strong><br>{esc(deep)}</div>'
                )
            elif summary:
                p.append(
                    f'<div style="font-size:13px;color:#525252;margin:4px 0 0 14px;line-height:1.45;">{esc(summary)}</div>'
                )
            p.append("</li>")
        p.append("</ul>")

    p.append(
        '<div style="margin-top:28px;padding-top:16px;border-top:1px solid #e0e0e0;'
        'font-size:11px;color:#a8a8a8;text-align:center;">'
        '&#9733; flagged as important &middot; blue dot indicates new since last brief &middot; '
        'magnitude tags via LLM</div>'
    )
    p.append("</div></body></html>")
    return "".join(p)


def render_daily_text(date_str, window_items, new_items, analysis, force_daily):
    grouped = group_by_section(window_items + [i for i in new_items if i["id"] not in {x["id"] for x in window_items}])
    new_ids = {i["id"] for i in new_items}
    item_meta = (analysis or {}).get("items", {})
    tldr = (analysis or {}).get("tldr")
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
            mag = item_meta.get(it["id"], {}).get("magnitude", "")
            mag_tag = f"[{mag.upper()}] " if mag else ""
            lines.append(f"{marker}{star}{mag_tag}[{date}] {it.get('title','(untitled)')}")
            if it.get("link"):
                lines.append(f"        {it['link']}")
            deep = item_meta.get(it["id"], {}).get("deep_summary", "")
            if deep:
                lines.append(f"        > {deep}")
    return "\n".join(lines)


def render_weekly_html(date_str, themes, window_items):
    by_id = {it["id"]: it for it in window_items}
    p = ['<!DOCTYPE html><html><head><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1"></head>',
         '<body style="margin:0;padding:24px;background:#f4f4f4;'
         'font-family:-apple-system,BlinkMacSystemFont,Helvetica,Arial,sans-serif;color:#161616;">',
         '<div style="max-width:680px;margin:0 auto;background:#fff;border-radius:8px;padding:32px;">',
         f'<div style="font-size:13px;color:#6f6f6f;margin-bottom:4px;">Weekly Themes &middot; {esc(date_str)}</div>',
         f'<h1 style="margin:0 0 24px 0;font-size:22px;color:#8a3ffc;">This week in Anthropic</h1>']
    if not themes or not themes.get("themes"):
        p.append('<p>No themes identified this week.</p>')
    else:
        for theme in themes["themes"]:
            p.append(f'<h2 style="font-size:16px;color:#8a3ffc;margin:20px 0 8px;">{esc(theme.get("name",""))}</h2>')
            p.append(f'<p style="font-size:14px;line-height:1.55;margin:0 0 10px;">{esc(theme.get("summary",""))}</p>')
            ids = theme.get("item_ids", [])
            if ids:
                p.append('<ul style="font-size:13px;margin:0;padding-left:20px;">')
                for iid in ids:
                    it = by_id.get(iid)
                    if not it:
                        continue
                    date = it["dt"].strftime("%b %d") if it.get("dt") else ""
                    p.append(
                        f'<li style="margin-bottom:4px;">'
                        f'<a href="{esc(it.get("link","#"))}" style="color:#161616;">{esc(it.get("title","(untitled)"))}</a>'
                        f' <span style="color:#6f6f6f;">- {esc(date)}</span></li>'
                    )
                p.append('</ul>')
    p.append('</div></body></html>')
    return "".join(p)


def render_alert_html(matches, date_str):
    p = ['<!DOCTYPE html><html><head><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1"></head>',
         '<body style="margin:0;padding:24px;background:#f4f4f4;'
         'font-family:-apple-system,BlinkMacSystemFont,Helvetica,Arial,sans-serif;color:#161616;">',
         '<div style="max-width:680px;margin:0 auto;background:#fff;border-radius:8px;padding:28px;">',
         f'<div style="font-size:13px;color:#6f6f6f;margin-bottom:4px;">Saved-search alert &middot; {esc(date_str)}</div>',
         f'<h1 style="margin:0 0 18px 0;font-size:20px;color:#da1e28;">{len(matches)} match{"es" if len(matches)!=1 else ""} from your saved searches</h1>']
    for label, it in matches:
        date = it["dt"].strftime("%b %d") if it.get("dt") else ""
        p.append(
            '<div style="border:1px solid #e0e0e0;border-radius:6px;padding:14px;margin-bottom:12px;">'
            f'<div style="font-size:11px;font-weight:700;color:#da1e28;text-transform:uppercase;letter-spacing:0.04em;margin-bottom:6px;">{esc(label)}</div>'
            f'<a href="{esc(it.get("link","#"))}" style="color:#161616;text-decoration:none;font-weight:600;font-size:15px;">{esc(it.get("title","(untitled)"))}</a>'
            f'<div style="font-size:12px;color:#6f6f6f;margin-top:4px;">[{esc(it.get("source",""))}] {esc(date)}</div>'
            f'<div style="font-size:13px;color:#525252;margin-top:8px;line-height:1.45;">{esc(clean_text(it.get("summary",""), 320))}</div>'
            '</div>'
        )
    p.append('</div></body></html>')
    return "".join(p)


# ----- Archive -----

def write_archive(date_str, html_body):
    if not cfg.ARCHIVE_DIR:
        return
    archive_dir = Path(cfg.ARCHIVE_DIR)
    archive_dir.mkdir(parents=True, exist_ok=True)
    iso_date = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d")
    (archive_dir / f"{iso_date}.html").write_text(html_body, encoding="utf-8")

    entries = sorted(
        (p for p in archive_dir.glob("*.html") if p.name != "index.html"),
        reverse=True,
    )
    index = ['<!DOCTYPE html><html><head><meta charset="utf-8">',
             '<title>Anthropic Daily Brief - Archive</title>',
             '<meta name="viewport" content="width=device-width,initial-scale=1">',
             '<style>body{font-family:-apple-system,sans-serif;max-width:680px;margin:40px auto;padding:24px;color:#161616}',
             'h1{font-size:24px;margin:0 0 4px}.sub{color:#6f6f6f;margin-bottom:24px}',
             'ul{list-style:none;padding:0}li{padding:10px 0;border-bottom:1px solid #f4f4f4}',
             'a{color:#0f62fe;text-decoration:none;font-weight:600}a:hover{text-decoration:underline}',
             '.date{color:#6f6f6f;font-weight:400;font-size:13px;margin-left:8px}</style></head><body>',
             '<h1>Anthropic Daily Brief</h1>',
             f'<div class="sub">{len(entries)} archived brief{"s" if len(entries)!=1 else ""}</div>',
             '<ul>']
    for entry in entries:
        d = entry.stem
        try:
            pretty = datetime.strptime(d, "%Y-%m-%d").strftime("%A, %b %d, %Y")
        except ValueError:
            pretty = d
        index.append(f'<li><a href="{entry.name}">{pretty}</a><span class="date">{d}</span></li>')
    index.append('</ul></body></html>')
    (archive_dir / "index.html").write_text("".join(index), encoding="utf-8")


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


def send_email(cfg_, subject, text_body, html_body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = cfg_["from"]
    msg["To"] = cfg_["to"]
    msg.set_content(text_body)
    msg.add_alternative(html_body, subtype="html")
    with smtplib.SMTP(cfg_["host"], cfg_["port"]) as s:
        s.starttls()
        s.login(cfg_["user"], cfg_["password"])
        s.send_message(msg)


# ----- Main -----

def main():
    state = load_state()
    first_run = not state.get("seen_entries") and not state.get("page_hashes")

    window_items, new_items = collect_feed_items(state)
    new_items.extend(collect_page_changes(state))

    force_daily = os.environ.get("FORCE_DAILY", "").lower() in ("1", "true", "yes")
    force_weekly = os.environ.get("FORCE_WEEKLY", "").lower() in ("1", "true", "yes")
    et_now = datetime.now(ZoneInfo("America/New_York"))
    et_date = et_now.strftime("%A, %b %d, %Y")

    if first_run and not force_daily:
        save_state(state)
        print(f"[init] Snapshotted {len(window_items)} items. No email (set FORCE_DAILY=1 to override).")
        return 0

    # --- Saved-search alerts (always evaluated for new items) ---
    matches = saved_search_matches(new_items, state)
    if matches:
        matched_ids = [it["id"] for _, it in matches]
        try:
            cfg_smtp = smtp_config()
            subject = f"[Alert] {len(matches)} new match{'es' if len(matches)!=1 else ''} from saved searches"
            html_body = render_alert_html(matches, et_date)
            text_body = "Saved-search matches:\n\n" + "\n".join(
                f"- [{label}] {it.get('title','(untitled)')}\n  {it.get('link','')}"
                for label, it in matches
            )
            send_email(cfg_smtp, subject, text_body, html_body)
            print(f"[ok] Sent saved-search alert with {len(matches)} match(es).")
        except Exception as e:
            # Roll back so we retry next hour
            for iid in matched_ids:
                state.get("alerted_entries", {}).pop(iid, None)
            print(f"[error] saved-search alert failed: {e}", file=sys.stderr)

    # --- Daily brief ---
    if force_daily or new_items:
        analysis = analyze_items(window_items, new_items)
        html_body = render_daily_html(et_date, window_items, new_items, analysis, force_daily)
        text_body = render_daily_text(et_date, window_items, new_items, analysis, force_daily)
        write_archive(et_date, html_body)
        if new_items:
            subject = f"Anthropic Daily Brief - {len(new_items)} new update{'s' if len(new_items) != 1 else ''}"
        else:
            subject = "Anthropic Daily Brief - nothing new today"
        cfg_smtp = smtp_config()
        send_email(cfg_smtp, subject, text_body, html_body)
        print(f"[ok] Sent daily brief: {subject}")
    else:
        print(f"[ok] No new items, not 7 AM ET window. Skipping daily email.")

    # --- Weekly themes ---
    if force_weekly:
        cutoff_7d = datetime.now(timezone.utc) - timedelta(days=7)
        items_7d = [it for it in window_items if it.get("dt") and it["dt"] >= cutoff_7d]
        themes = weekly_themes(items_7d)
        if themes and themes.get("themes"):
            html_body = render_weekly_html(et_date, themes, items_7d)
            text_body = "Weekly themes:\n\n" + "\n\n".join(
                f"## {t.get('name','')}\n{t.get('summary','')}"
                for t in themes["themes"]
            )
            cfg_smtp = smtp_config()
            send_email(cfg_smtp, f"Anthropic Weekly Themes - {et_date}", text_body, html_body)
            print(f"[ok] Sent weekly themes email.")
        else:
            print("[ok] Weekly themes requested but no themes returned (likely no API key or empty week).")

    save_state(state)
    return 0


if __name__ == "__main__":
    sys.exit(main())
