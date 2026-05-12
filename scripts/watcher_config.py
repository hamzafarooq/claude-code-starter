"""
watcher_config.py - Customize the daily brief behavior.

Edit this file to mute sources, add saved-search keyword alerts, and tune
limits. Pure Python (no YAML dependency) so it's easy to edit and validate.
"""

# --- Per-source toggles ---
# Set any source to False to exclude it from the daily brief.
SOURCE_TOGGLES = {
    "News":          True,
    "Research":      True,
    "Engineering":   True,
    "Code Releases": True,
    "Docs":          True,
}

# --- Saved-search alerts ---
# Each tuple: (label, regex pattern). When a NEW item matches, you get an
# immediate dedicated email (independent of the daily brief), once per item.
# Patterns are case-insensitive. Examples:
#     ("Pricing changes",      r"\bpricing|price\b"),
#     ("Opus model news",      r"\bopus\b"),
#     ("New API features",     r"\bapi\b.*\b(new|release|launch)"),
SAVED_SEARCHES = [
    # Uncomment or add your own:
    # ("Pricing changes", r"\bpricing|price\b"),
    # ("Opus model news", r"\bopus\b"),
]

# --- LLM behavior ---
# Cap the number of items the deep-summary pass runs over (cost control).
DEEP_SUMMARY_LIMIT = 10

# Model used for TL;DR, magnitude tags, deep summaries, and weekly themes.
# Haiku is cheap and fast. Bump to claude-sonnet-4-6 if you want richer prose.
LLM_MODEL = "claude-haiku-4-5-20251001"

# --- Archive ---
# Where to write the searchable HTML archive of past briefs.
# Set ARCHIVE_DIR = None to disable archiving entirely.
ARCHIVE_DIR = "briefs"
