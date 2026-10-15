#!/usr/bin/env python3
"""Build the research opportunities iCalendar feed from opportunities.json.

Usage:
    python build_calendar.py                 # validate, then write the .ics
    python build_calendar.py --check         # validate only, write nothing
    python build_calendar.py --input FILE --output FILE

Validation errors stop the build (exit code 1) and no calendar is written,
so a bad edit can never produce a broken feed. Warnings are printed but do
not stop the build.
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from urllib.parse import urlparse

# Events recur yearly, so this must be a NON-leap year. That is also what
# makes Feb 29 fail validation (clients often skip Feb 29 in other years).
BASE_YEAR = 2026

# Kept constant on purpose: a timestamp that changes on every run would make
# every build differ from the last one, even when the data has not changed.
DTSTAMP = "20260101T000000Z"

CALENDAR_NAME = "Research Opportunities"

# To add a field later (e.g. "source_url"), add it here and handle it below.
REQUIRED_FIELDS = {"id", "summary", "month", "day", "description"}
OPTIONAL_FIELDS = set()

ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
URL_PATTERN = re.compile(r"https?://\S+")
SHORTENER_DOMAINS = {"lnkd.in", "bit.ly", "tinyurl.com", "t.co", "goo.gl"}


# --------------------------------------------------------------------------
# Validation
# --------------------------------------------------------------------------

def _is_int(value) -> bool:
    # bool is a subclass of int in Python, so exclude it explicitly.
    return isinstance(value, int) and not isinstance(value, bool)


def validate(items) -> tuple[list[str], list[str]]:
    """Return (errors, warnings). Collects every problem instead of stopping at the first."""
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(items, list):
        return ["The top level of the file must be a list of opportunities."], warnings
    if not items:
        return ["The file contains no opportunities."], warnings

    seen_ids: dict[str, int] = {}

    for index, item in enumerate(items, start=1):
        label = f"entry #{index}"

        if not isinstance(item, dict):
            errors.append(f"{label}: must be an object, got {type(item).__name__}.")
            continue

        if isinstance(item.get("id"), str) and item["id"]:
            label = f"entry #{index} ({item['id']})"

        present = set(item)
        missing = REQUIRED_FIELDS - present
        unknown = present - REQUIRED_FIELDS - OPTIONAL_FIELDS
        if missing:
            errors.append(f"{label}: missing field(s): {', '.join(sorted(missing))}.")
        if unknown:
            allowed = ", ".join(sorted(REQUIRED_FIELDS | OPTIONAL_FIELDS))
            errors.append(
                f"{label}: unknown field(s): {', '.join(sorted(unknown))} (allowed: {allowed})."
            )

        # id: used to build each event's UID, so it must be unique and stable.
        if "id" in item:
            item_id = item["id"]
            if not isinstance(item_id, str) or not ID_PATTERN.match(item_id):
                errors.append(
                    f"{label}: 'id' must be lowercase letters and digits separated by "
                    f"single hyphens, e.g. 'eth-zurich' (got {item_id!r})."
                )
            elif item_id in seen_ids:
                errors.append(f"{label}: duplicate id (already used by entry #{seen_ids[item_id]}).")
            else:
                seen_ids[item_id] = index

        # summary: single line of text.
        if "summary" in item:
            summary = item["summary"]
            if not isinstance(summary, str) or not summary.strip():
                errors.append(f"{label}: 'summary' must be non-empty text.")
            elif "\n" in summary or "\r" in summary or "\\n" in summary:
                errors.append(f"{label}: 'summary' must be a single line (no line breaks).")

        # month / day: whole numbers forming a real calendar date.
        month, day = item.get("month"), item.get("day")
        for field in ("month", "day"):
            if field in item and not _is_int(item[field]):
                errors.append(f"{label}: '{field}' must be a whole number (got {item[field]!r}).")
        if _is_int(month) and _is_int(day):
            if not 1 <= month <= 12:
                errors.append(f"{label}: 'month' must be between 1 and 12 (got {month}).")
            else:
                try:
                    datetime.date(BASE_YEAR, month, day)
                except ValueError:
                    hint = (
                        " Feb 29 is not supported because events recur every year."
                        if (month, day) == (2, 29)
                        else ""
                    )
                    errors.append(f"{label}: {month}/{day} is not a valid calendar date.{hint}")

        # description: required text; links are checked as warnings.
        if "description" in item:
            description = item["description"]
            if not isinstance(description, str) or not description.strip():
                errors.append(f"{label}: 'description' must be non-empty text.")
            else:
                urls = URL_PATTERN.findall(description)
                if not urls:
                    warnings.append(f"{label}: description has no application link (http/https URL).")
                for url in urls:
                    host = (urlparse(url).hostname or "").lower()
                    if host in SHORTENER_DOMAINS:
                        warnings.append(
                            f"{label}: uses a link shortener ({host}); prefer the official application page."
                        )
                    if url.lower().startswith("http://"):
                        warnings.append(f"{label}: link uses http instead of https ({url}).")

    return errors, warnings


# --------------------------------------------------------------------------
# iCalendar (RFC 5545) output helpers
# --------------------------------------------------------------------------

def escape_text(value: str) -> str:
    """Escape a TEXT value for iCalendar.

    Line breaks can be written in opportunities.json either as a real newline
    or as the two characters backslash + n (the convention the existing data
    uses). Both become an iCalendar line break.
    """
    value = value.strip()
    value = value.replace("\\n", "\n")
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    value = value.replace("\\", "\\\\")
    value = value.replace(";", "\\;").replace(",", "\\,")
    return value.replace("\n", "\\n")


def fold_line(line: str) -> list[str]:
    """Fold a content line to at most 75 octets, never splitting a UTF-8 character."""
    if len(line.encode("utf-8")) <= 75:
        return [line]

    chunks: list[str] = []
    current = ""
    current_len = 0
    limit = 75  # continuation lines start with a space, which counts toward the limit
    for char in line:
        char_len = len(char.encode("utf-8"))
        if current_len + char_len > limit:
            chunks.append(current)
            current, current_len, limit = char, char_len, 74
        else:
            current += char
            current_len += char_len
    chunks.append(current)
    return [chunks[0]] + [" " + chunk for chunk in chunks[1:]]


def build_ics(items) -> str:
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//AI and CS Research Master Roadmap Calendar//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        # Not part of RFC 5545, but widely supported for naming a subscribed calendar.
        f"X-WR-CALNAME:{escape_text(CALENDAR_NAME)}",
    ]

    for item in sorted(items, key=lambda i: (i["month"], i["day"], i["id"])):
        summary = escape_text(item["summary"])
        description = escape_text(item["description"])
        start = f"{BASE_YEAR}{item['month']:02d}{item['day']:02d}T090000"
        end = f"{BASE_YEAR}{item['month']:02d}{item['day']:02d}T100000"

        lines += [
            "BEGIN:VEVENT",
            f"UID:recur-{item['id']}@research",
            f"DTSTAMP:{DTSTAMP}",
            f"DTSTART:{start}",
            f"DTEND:{end}",
            "RRULE:FREQ=YEARLY",
            f"SUMMARY:{summary}",
            f"DESCRIPTION:{description}",
            "BEGIN:VALARM",
            "TRIGGER:-P14D",
            "ACTION:DISPLAY",
            f"DESCRIPTION:Reminder: {summary} in 14 days",
            "END:VALARM",
            "BEGIN:VALARM",
            "TRIGGER:-P3D",
            "ACTION:DISPLAY",
            f"DESCRIPTION:Urgent: {summary} in 3 days",
            "END:VALARM",
            "END:VEVENT",
        ]

    lines.append("END:VCALENDAR")

    folded: list[str] = []
    for line in lines:
        folded.extend(fold_line(line))
    return "\r\n".join(folded) + "\r\n"


# --------------------------------------------------------------------------
# Command line
# --------------------------------------------------------------------------

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Validate opportunities.json and build the .ics feed.")
    parser.add_argument("--input", default="opportunities.json", help="path to the opportunities JSON file")
    parser.add_argument("--output", default="research_calendar_master.ics", help="path of the .ics file to write")
    parser.add_argument("--check", action="store_true", help="validate only; do not write the .ics file")
    args = parser.parse_args(argv)

    try:
        with open(args.input, "r", encoding="utf-8") as f:
            items = json.load(f)
    except FileNotFoundError:
        print(f"error: {args.input} not found.", file=sys.stderr)
        return 1
    except json.JSONDecodeError as exc:
        print(f"error: {args.input} is not valid JSON: {exc}", file=sys.stderr)
        return 1

    errors, warnings = validate(items)

    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)

    if errors:
        print(f"\n{len(errors)} validation error(s) in {args.input}:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        print("\nNo calendar was written.", file=sys.stderr)
        return 1

    if args.check:
        print(f"OK: {len(items)} entries validated ({len(warnings)} warning(s)).")
        return 0

    # newline="" stops Python from rewriting the CRLF line endings on Windows.
    with open(args.output, "w", encoding="utf-8", newline="") as f:
        f.write(build_ics(items))

    print(f"Successfully generated {args.output} with {len(items)} events ({len(warnings)} warning(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
