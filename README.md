# 🌍 AI & STEM Research Internship Deadlines & Master Tracker

A curated iCalendar (`.ics`) feed and opportunity repository tracking key application deadlines, requirements, and application links for top global research internships, pre-docs, residencies, and fellowships across Artificial Intelligence, Machine Learning, and Computer Science.

Designed for undergraduate and graduate researchers targeting disciplines such as Data Management, Machine Learning Systems, Computer Vision, NLP, and AI Alignment.

> **⚠️ Always verify on the official page.** Dates, eligibility, and funding details are compiled from public sources and change from year to year. Treat each calendar entry as a reminder to check the program's own page, not as a guarantee. If you spot an error, please open an issue or a pull request.

---

## 📅 Subscribe via Calendar (Live Sync)

Instead of manually importing static `.ics` files, subscribe using the raw calendar feed URL below. Any new deadline or correction pushed to this repository will appear in your calendar the next time your calendar app refreshes the feed (this can take several hours or longer, depending on the app).

<p align="center">
  <!-- 1-Click for Google Calendar Web -->
  <a href="https://calendar.google.com/calendar/render?cid=https%3A%2F%2Fraw.githubusercontent.com%2FGreenyNg%2Fresearch-opportunities%2Fmain%2Fresearch_calendar_master.ics" target="_blank">
    <img src="https://img.shields.io/badge/📅_Add_to_Google_Calendar-4285F4?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Add to Google Calendar" />
  </a>
</p>

<p align="center">
  <b>Calendar Feed URL (Copy for Apple Calendar / Outlook):</b><br/>
  <code>https://raw.githubusercontent.com/GreenyNg/research-opportunities/main/research_calendar_master.ics</code>
</p>

### 📱 Quick Setup Instructions

| Platform | How to Subscribe |
| :--- | :--- |
| **Google Calendar** | Click the **Add to Google Calendar** button above (or paste the feed URL into *Other calendars &rarr; From URL*). |
| **Apple Calendar (Mac)** | Press `Option + Cmd + S` (or **File &rarr; New Calendar Subscription...**), paste the feed URL, and click **Subscribe**. |
| **Apple Calendar (iOS)** | Go to **Settings &rarr; Calendar &rarr; Accounts &rarr; Add Account &rarr; Other &rarr; Add Subscribed Calendar**, paste the URL, and save. |
| **Microsoft Outlook** | Go to Calendar view &rarr; **Add Calendar &rarr; Subscribe from web**, paste the URL, and save. |

---

## ✨ Features

* **Yearly Recurrence (`RRULE:FREQ=YEARLY`)**: Events repeat each year as a prompt to re-check the program page. Some programs are one-off postings or change their dates, so always confirm the current cycle.
* **Two-Stage Alarms**: Built-in alerts set for **14 days before** (preparation reminder) and **3 days before** (final submission check).
* **Event Details**: Most entries include the focus area, eligibility notes, required documents, and an application link. The level of detail varies by program.
* **Floating Local Time**: Events are timed at 09:00 AM local time to prevent unwanted shifts across time zones.

---

## 🎯 Master Opportunities Directory

Eligibility varies widely. Some programs are limited to a particular year of study, nationality, gender, or to graduate students, so check the requirements before you apply.

### Global Research Fellowships & Internships

* **Max Planck Institutes** (CaCTüS Internship & CIS Research Internships) — *Germany*
* **ETH Zurich Student Summer Research Fellowship (SSRF)** — *Switzerland*
* **Summer @ EPFL Research Fellowship** — *Switzerland*
* **INSAIT SURF (ETH / EPFL Partner)** — *Bulgaria*
* **OIST Research Internship Program** — *Japan*
* **Aalto Science Institute (AScI) International Summer Research** — *Finland*
* **ISTA ISTernship Program** — *Austria*
* **CERN OpenLab & Summer Student Programme** — *Switzerland*
* **DESY Summer Student Programme** — *Germany*
* **Vector Institute Research Internships (Winter / Spring / Fall)** — *Canada*
* **Kempner AI Fellows Program (Harvard)** — *USA*
* **Caltech SURF** & **IPAM RIPS (UCLA / Singapore)** — *USA / Singapore*
* **UCL Gatsby Computational Neuroscience & Machine Learning Unit** — *UK*
* **Google Research Africa Student Researcher** — *Africa Locations*
* **MBZUAI UGRIP (Undergraduate Research Internship)** — *UAE*
* **Mak-AI Undergraduate Internship Program** — *Uganda*
* **RENEU Program (University of Chicago)** — *USA / Nigeria*
* **EDGE Summer Program** (Mathematical Sciences) — *USA*
* **CMU LTI Language Technologies Internship** — *USA*

### AI Safety, Alignment & Independent Labs

* **MATS (Machine Learning Alignment Theory & Scholars)**
* **PIBBSS Summer Research Fellowship**
* **Cambridge ERA:AI Summer Fellowship**
* **SPAR (Supervised Program for Alignment Research)**
* **Black in AI Safety & Ethics (BASE) Fellowship**
* **LASR Labs Summer Fellowship**
* **Big Theta Research Mentorship**

### Graduate Funding & Long-Term Residencies

* **OpenAI Residency Program** (6-month research transition)
* **Michael Taiwo (MT) Scholarships** (GRE/IELTS & Grad application fees funding)
* **Knight-Hennessy Scholars (Stanford University)**
* **Lateef Jakande Leadership Academy (LJLA)**

---

## 🛠️ Repository Architecture

* `opportunities.json`: Structured source of truth for program dates, details, and application links.
* `build_calendar.py`: Python script that validates `opportunities.json` and generates the `.ics` file. If validation fails, nothing is written. Run `python build_calendar.py --check` to validate without writing anything.
* `research_calendar_master.ics`: The compiled production calendar file.
* `.github/workflows/update_calendar.yml`: Automated CI workflow that rebuilds and pushes the calendar on commit.

### Data Format

Each opportunity in `opportunities.json` looks like this (placeholder values shown):

```json
{
  "id": "example-program",
  "summary": "DEADLINE: Example Research Internship",
  "month": 1,
  "day": 15,
  "description": "Focus: Machine Learning.\\nEligibility: Undergraduates.\\nRequirements: CV, transcript.\\nPortal: https://example.org/apply"
}
```

* `id`: a unique, lowercase, hyphenated identifier.
* `month` / `day`: the deadline as numbers. The year is handled by the yearly recurrence.
* `description`: write line breaks as `\\n`, as in the example above (the standard JSON `\n` also works). Commas and semicolons are escaped for you.

---

## 🤝 Contributing

Contributions and updates are very welcome! If you know of an opportunity or notice a deadline shift:

1. Fork this repository.
2. Edit or add the opportunity in `opportunities.json`, following the format above.
3. Include a link to the **official** application page, and double-check the date against it.
4. Run `python build_calendar.py --check` to validate your changes locally. It reports every problem it finds, such as a bad date or a duplicate `id`.
5. Submit a Pull Request. Once it is merged, the GitHub Action rebuilds the `.ics` file.

---

## 🙏 Acknowledgments & Credits

This project began from the [Research Internships 2026 Google Doc](https://docs.google.com/document/d/16odpvFaFm6ZKxdAPfZPCzk_D0bhnIQSk6-5rfCFBaNE/edit?tab=t.5zd9mj1gqbal), and its initial dataset is based on that document. Special thanks to its original compiler for laying the groundwork.

We turned that static tracker into a structured `.ics` calendar and an automated pipeline so more researchers can get reminders directly in their own calendar.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
