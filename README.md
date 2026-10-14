```markdown
# 🌍 AI & STEM Research Internship Deadlines & Master Tracker

A curated, automatically updating iCalendar (`.ics`) feed and opportunity repository tracking key application deadlines, requirements, and direct application links for top global research internships, pre-docs, residencies, and fellowships across Artificial Intelligence, Machine Learning, and Computer Science.

Designed especially for undergraduate and graduate researchers targeting tracks like **Data Management, Recommendation Systems, Machine Learning Systems, and AI Alignment**.

---

## 📅 Subscribe via Calendar (Live Sync)

Instead of manually importing static `.ics` files, subscribe using the raw calendar feed URL below. Any new deadline or correction pushed to this repository will automatically sync with your calendar application.

```text
[https://raw.githubusercontent.com/GreenyNg/research-opportunities/main/research_calendar_master.ics](https://raw.githubusercontent.com/GreenyNg/research-opportunities/main/research_calendar_master.ics)

```

### Quick Setup Instructions

| Platform | Instructions |
| --- | --- |
| **Google Calendar** | On the left sidebar, click **`+`** next to *Other calendars* → select **From URL** → paste the link → click **Add calendar**. |
| **Apple Calendar (Mac)** | Click **File** → **New Calendar Subscription...** → paste the URL → choose refresh frequency (e.g., daily/weekly). |
| **Apple Calendar (iOS)** | Open **Settings** → **Calendar** → **Accounts** → **Add Account** → **Other** → **Add Subscribed Calendar**. |
| **Microsoft Outlook** | Go to Calendar view → click **Add Calendar** → select **Subscribe from web** → paste link. |

---

## ✨ Features

* **Yearly Recurrence (`RRULE:FREQ=YEARLY`)**: All events recur annually so you can plan across your 200, 300, and 400 undergraduate levels and beyond.
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

## 🗺️ Career Roadmap: Data Management & Machine Learning

Target Track: **Data Management & ML | Focus: Recommendation Systems (RecSys)**

```
Phase 1: Orientation & Community (ML Collective Africa, Discord, Reading Groups)
   │
Phase 2: Math & Foundations (MIT OCW 18.06 Linear Algebra, Math for CS, Python ML Stack)
   │
Phase 3: Structured Research (CS197 Foundations Study Group, Lit Review, Capstone)
   │
Phase 4: Proof of Work (Kaggle Competition, GitHub Portfolio, Paper Reproduction)
   │
Phase 5: Focus Group & Artifact (3–5 Member RecSys Group, Workshop Paper Submission)
   │
Phase 6: Mentorship & External Programs (Google TRC, ETH SSRF, Summer @ EPFL, Max Planck)
   │
Phase 7: Career & Grad Push (MSc/PhD Applications, MT Scholarships, Residencies)

```

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

## 📜 License

This project is licensed under the [MIT License](https://www.google.com/search?q=LICENSE).

```

```