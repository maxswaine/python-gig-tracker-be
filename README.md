# Python Gig Tracker (Backend)

A lightweight backend API for tracking live music experiences — gigs, festivals, and artists — built with **FastAPI** and **SQLAlchemy**. This backend forms the foundation of a personal music memory tracker where users can log gigs and festivals they've attended, see all artists they've seen live, and share moments with friends.

---

## 🎯 Features

- **Track Gigs & Festivals**  
  Record details of gigs (venue, date, location, artists) and multi-day festivals (with per-day lineups).  

- **Artists Database**  
  Centralised artist management to avoid duplicates and keep a history of all performances you've seen.  

- **User Accounts**  
  Supports user accounts with relationships to gigs, festivals, and friends (friend features coming soon).  

- **REST API**  
  Clean and modern API built with FastAPI for easy integration with frontend or mobile apps.  

- **Testing Suite**  
  Includes Pytest-based tests for robust development and CI/CD readiness.

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **FastAPI** – modern, fast (high-performance) web framework  
- **SQLAlchemy ORM** – relational data modeling  
- **SQLite** (dev) / Postgres ready (prod)  
- **Alembic** – database migrations  
- **Pytest** – test-driven development  
- **Pydantic** – data validation and serialization  

---

## 🚀 Getting Started

### Clone the repository
```bash
git clone https://github.com/your-username/python-gig-tracker-be.git
cd python-gig-tracker-be
```

### Install Dependencies
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run the API
```bash
uvicorn app.main:app --reload
```
The API will be available at http://127.0.0.1:8000


Go to http://127.0.0.1:8000/docs for full API documentation

### Run tests
```bash
pytest
```

## 🌱 Upcoming features
- OAuth2/JWT authentication & authorization
-	Friend requests and social features
-	Artist metadata enrichment via Spotify API / MusicBrainz API
-	Frontend integration (React/Next.js planned)
-	Deployment on Docker/Kubernetes
