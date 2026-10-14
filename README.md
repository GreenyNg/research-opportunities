# 🌍 AI & STEM Research Internship Deadlines & Master Tracker

A curated, automatically updating iCalendar (`.ics`) feed and opportunity repository tracking key application deadlines, requirements, and direct application links for top global research internships, pre-docs, residencies, and fellowships across Artificial Intelligence, Machine Learning, and Computer Science.

Designed for undergraduate and graduate researchers targeting disciplines such as Data Management, Machine Learning Systems, Computer Vision, NLP, and AI Alignment.

---

## 📅 Subscribe via Calendar (Live Sync)

Instead of manually importing static `.ics` files, subscribe using the raw calendar feed URL below. Any new deadline or correction pushed to this repository will automatically sync with your calendar application.



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

* **Yearly Recurrence (`RRULE:FREQ=YEARLY`)**: All events recur annually so users can plan across continuous academic cycles.
* **Two-Stage Alarms**: Built-in alerts set for **14 days before** (preparation reminder) and **3 days before** (final submission check).
* **Rich Event Metadata**: Every calendar entry contains eligibility prerequisites, required documents (CV, transcripts, recommendations), and direct application links.
* **Floating Local Time**: Events are timed at 09:00 AM local time to prevent unwanted shifts across time zones.

---

## 🎯 Master Opportunities Directory

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

* `opportunities.json`: Structured source of truth for all program dates, eligibility rules, and portals.
* `build_calendar.py`: Python generator script that validates schema and builds the RFC 5545-compliant `.ics` file.
* `research_calendar_master.ics`: The compiled production calendar file.
* `.github/workflows/update_calendar.yml`: Automated CI workflow that rebuilds and pushes changes on commit.

---

## 🤝 Contributing

Contributions and updates are very welcome! If you know of an opportunity or notice a deadline shift:

1. Fork this repository.
2. Edit or add the opportunity details in `opportunities.json`.
3. Submit a Pull Request. The GitHub Action will automatically re-build and validate the `.ics` file.

---

## 🙏 Acknowledgements & Attribution

## 🙏 Acknowledgments & Credits

- Special thanks to the original compiler of the foundational [Research Internships 2026 Google Doc](https://docs.google.com/document/d/16odpvFaFm6ZKxdAPfZPCzk_D0bhnIQSk6-5rfCFBaNE/edit?tab=t.5zd9mj1gqbal), whose initial compilation inspired this automated calendar feed. 

We automated that foundational tracker into a structured `.ics` calendar and continuous pipeline so more researchers could access reminders directly in their workflow. Special thanks for laying the groundwork!

---

## 📜 License

This project is licensed under the [MIT License](https://www.google.com/search?q=LICENSE).

```

```
