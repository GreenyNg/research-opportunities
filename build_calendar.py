import json
from datetime import datetime

def generate_ics(json_path="opportunities.json", output_path="research_calendar.ics"):
    with open(json_path, "r", encoding="utf-8") as f:
        items = json.load(f)

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

    print(f"Successfully generated {output_path} with {len(items)} events.")

if __name__ == "__main__":
    generate_ics()