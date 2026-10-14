import json
import sys
from datetime import datetime

def generate_ics(json_path="opportunities.json", output_path="research_calendar_master.ics"):
    with open(json_path, "r", encoding="utf-8") as f:
        items = json.load(f)

    # --- 1. Schema & Data Validation ---
    if not isinstance(items, list):
        print("❌ Error: opportunities.json must be a JSON array [].")
        sys.exit(1)

    required_keys = {"id", "summary", "month", "day", "description"}
    seen_ids = set()

    for idx, item in enumerate(items):
        # Check required fields
        missing = required_keys - set(item.keys())
        if missing:
            print(f"❌ Error at item #{idx}: Missing fields {missing}")
            sys.exit(1)

        # Check unique id
        item_id = item["id"]
        if item_id in seen_ids:
            print(f"❌ Error: Duplicate ID '{item_id}' detected at item #{idx}.")
            sys.exit(1)
        seen_ids.add(item_id)

        # Check valid calendar dates
        try:
            m = int(item["month"])
            d = int(item["day"])
            datetime(year=2026, month=m, day=d)
        except (ValueError, TypeError) as e:
            print(f"❌ Error: Invalid date for '{item_id}' (month: {item.get('month')}, day: {item.get('day')}): {e}")
            sys.exit(1)

    print(f"✅ Schema validation passed for {len(items)} opportunities.")

    # --- 2. Build the ICS File ---
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//AI and CS Research Master Roadmap Calendar//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH"
    ]

    base_year = 2026

    for item in items:
        event_id = item["id"]
        summary = item["summary"]
        desc = item["description"]
        month = int(item["month"])
        day = int(item["day"])

        start_str = f"{base_year}{month:02d}{day:02d}T090000"
        end_str = f"{base_year}{month:02d}{day:02d}T100000"

        event = [
            "BEGIN:VEVENT",
            f"UID:recur-{event_id}@research",
            "DTSTAMP:20260101T000000Z",
            f"DTSTART:{start_str}",
            f"DTEND:{end_str}",
            "RRULE:FREQ=YEARLY",
            f"SUMMARY:{summary}",
            f"DESCRIPTION:{desc}",
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
            "END:VEVENT"
        ]
        lines.extend(event)

    lines.append("END:VCALENDAR")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\r\n".join(lines) + "\r\n")

    print(f"🚀 Successfully compiled {output_path} with {len(items)} events.")

if __name__ == "__main__":
    generate_ics()