# TIMEVAULT — Personal Life Decision Intelligence System

> **Tagline:** *"Decide today. Learn tomorrow."*

TimeVault is an open-source, production-grade decision intelligence platform designed to help people convert ambiguous, high-stakes life dilemmas into structured multi-criteria evaluations, commit decisions with confidence tracking, and conduct retrospective **Decision Replay** audits when real-world outcomes unfold.

---

## Key Features

1. **Structured Multi-Step Decision Engine**:
   - **Options**: Compare any number of competing paths (e.g. Job Offer A vs Job Offer B vs Staying).
   - **Evaluation Criteria**: Define personalized criteria (e.g. Compensation, Work-Life Balance, Growth, Culture) and assign weights from 1 to 10.
   - **Scoring Matrix**: Score each option against each factor on a standardized 1–10 scale.
   - **Mathematical Synthesis**: Computes weighted scores and normalized percentages:
     $$\text{Weighted Score} = \sum (\text{Factor Weight} \times \text{Option Score})$$
     $$\text{Normalized \%} = \frac{\sum (\text{Factor Weight} \times \text{Option Score})}{\sum (\text{Factor Weight} \times 10)} \times 100$$
   - **Intuitive Divergence Tracking**: Allows users to pick any option (even if it differs from the mathematical #1) while documenting their conviction and confidence percentage (1–100%).

2. **Longitudinal Outcome Tracking & Comparison**:
   - Record actual real-world consequences, satisfaction ratings (1–10), financial impacts, and unexpected surprises after months or years.

3. **Signature Feature — Decision Replay**:
   - Side-by-side retrospective view comparing:
     - **At Decision Time**: Original options, factor weights, candidate rankings, selected path, confidence %, and reasoning.
     - **After Outcome**: Actual reality, satisfaction rating, what went right, what went wrong, and actionable future wisdom.
     - **Prediction Calibration**: Algorithmic assessment of confidence vs actual satisfaction (identifies overconfidence, accurate risk foresight, and alignment).

4. **Event Timeline & History**:
   - Immutable audit trail tracking milestones: creation, option changes, scoring updates, final selection, and outcome logging.

5. **Decision Intelligence Insights**:
   - Empirical aggregate statistics: domain/category success rates (Career, Finance, Personal, etc.), mean confidence calibration, and gut-vs-model divergence audits.

6. **Enterprise Security & Isolation**:
   - Session-based authentication with strict per-user data isolation: users can never inspect or alter another user's records.
   - CSRF protection across all forms and server-side validation.

---

## Tech Stack

- **Backend**: Python 3.11 + Django 5.0 (MVT Architecture)
- **Database**: SQLite with Django ORM
- **Frontend**: Django Templates, Clean High-Contrast CSS3 Design System, Vanilla JavaScript for dynamic live preview
- **Zero External UI Bloat**: No React, Vue, npm, or heavy frontend toolchains. Fast, responsive, and maintainable.

---

## Project Architecture

```text
TIMEVAULT/
│
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3
│
├── config/                     # Django project configuration
│   ├── settings.py             # Settings, apps, auth redirects, static & template paths
│   ├── urls.py                 # Root URL configuration
│   ├── wsgi.py
│   └── asgi.py
│
├── decisions/                  # Core Decision Intelligence Application
│   ├── models.py               # Relational schema (Decision, Option, Factor, Score, ProsCons, Outcome, Event)
│   ├── services.py             # Pure Python MCDA scoring engine and replay analytics
│   ├── forms.py                # Server-validated Django ModelForms
│   ├── views.py                # MVT view controllers with user data isolation
│   ├── urls.py                 # Endpoint routing
│   ├── admin.py                # Comprehensive Django Admin portal
│   ├── tests.py                # Comprehensive test suite
│   └── management/
│       └── commands/
│           └── seed_demo.py    # Demo data generator
│
├── templates/                  # Django templates
│   ├── base.html               # Main layout shell with sidebar
│   ├── 404.html                # Custom error page
│   ├── registration/
│   │   ├── login.html          # Authentication login
│   │   └── register.html       # New user registration
│   └── decisions/
│       ├── dashboard.html      # Intelligence dashboard with KPIs
│       ├── decision_list.html  # Search & multi-parameter filtering
│       ├── decision_form.html  # Basic info & metadata form
│       ├── decision_wizard.html# Multi-step options, factors, matrix, and final choice
│       ├── decision_detail.html# Full analytical overview & timeline
│       ├── outcome_form.html   # Real-world outcome recording
│       ├── decision_replay.html# Signature retrospective Replay
│       ├── insights.html       # Meta-patterns & historical analytics
│       └── decision_confirm_delete.html
│
└── static/
    ├── css/
    │   └── style.css           # Modern SaaS high-contrast CSS design system
    └── js/
        └── scoring.js          # Dynamic client-side calculation preview
```

---

## Installation & Setup Guide

### 1. Clone & Set Up Environment
```bash
git clone https://github.com/Bhola-11/timevalue.git
cd timevalue

python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Database Migrations
```bash
python manage.py migrate
```

### 4. (Optional) Seed Demo Data
Populates realistic demo decisions across Career, Personal, and Business domains:
```bash
python manage.py seed_demo
```
*Default Demo Credentials:*
- **Username:** `demo_user`
- **Password:** `demopass123`

### 5. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6. Start the Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## Running Automated Tests

Run the complete test suite verifying models, MCDA scoring math, user isolation, edge cases, and view workflows:

```bash
python manage.py test
```

Expected output:
```text
Creating test database for alias 'default'...
Found 9 test(s).
System check identified no issues (0 silenced).
.........
----------------------------------------------------------------------
Ran 9 tests in ~11s

OK
Destroying test database for alias 'default'...
```

---

## License
MIT License. Built for high-judgment personal decision making.
