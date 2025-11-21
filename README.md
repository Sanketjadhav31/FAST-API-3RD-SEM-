# Task Manager API

A lightweight, efficient backend system for managing tasks, comments, and labels in collaborative workflows.

## Tech Stack
- **FastAPI** - Main framework
- **SQLModel/SQLAlchemy** - ORM + DB models
- **Pydantic** - Schema validation
- **SQLite/PostgreSQL** - Database
- **Uvicorn** - ASGI server
- **pytest** - Testing

## Project Structure
```
task-manager-api/
├── app/
│   ├── api/              # API routes
│   ├── models/           # Database models
│   ├── schemas/          # Pydantic schemas
│   ├── services/         # Business logic
│   ├── core/             # Config, database
│   └── utils/            # Helpers
├── tests/                # Test suite
├── scripts/              # Seed & utility scripts
└── .env                  # Environment variables
```

## Setup
```bash
pip install -r requirements.txt
python scripts/seed.py
uvicorn app.main:app --reload
```

## API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
