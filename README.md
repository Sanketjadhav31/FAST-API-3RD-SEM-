# Task Management API

A modern RESTful API for task management built with FastAPI, SQLModel, and Pydantic.

## 🚀 Features

- **Task Management**: Complete CRUD operations with status tracking
- **Priority System**: Organize tasks by priority (Low, Medium, High)
- **Status Workflow**: Track progress (TODO, In Progress, Done)
- **Comments**: Add discussions to tasks
- **Labels**: Categorize tasks with color-coded labels
- **Activity Logging**: Automatic tracking of all operations
- **Filtering**: Filter tasks by status, priority, and labels

## 📋 Tech Stack

- **Framework**: FastAPI
- **ORM**: SQLModel (SQLAlchemy + Pydantic)
- **Database**: SQLite (easily switchable to PostgreSQL)
- **Validation**: Pydantic v2
- **Python**: 3.11+

## 🗄️ Database Schema

### Models

- **Task**: Main task entity with status, priority, due dates
- **Comment**: Comments linked to tasks
- **Label**: Reusable labels with colors
- **TaskLabel**: Junction table for many-to-many relationship
- **ActivityLog**: Audit trail for all operations

### Relationships

- Task → Comments (one-to-many)
- Task ↔ Labels (many-to-many)
- Task → ActivityLogs (one-to-many)

## 🔧 Installation

### Prerequisites
- Python 3.11 or higher
- pip

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/Sanketjadhav31/FAST-API-3RD-SEM-.git
cd FAST-API-3RD-SEM-
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install fastapi sqlmodel uvicorn[standard] python-dotenv
```

4. **Seed the database**
```bash
python seed.py
```

5. **Run the application**
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

Once the server is running:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🎯 API Endpoints

### Tasks
- `POST /tasks` - Create task with optional labels
- `GET /tasks` - List all tasks (supports filters)
- `GET /tasks/{id}` - Get task with comments and labels
- `PATCH /tasks/{id}` - Update task
- `DELETE /tasks/{id}` - Delete task

**Filters**: `?status=in_progress&priority=high&label_id=1`

### Comments
- `POST /comments` - Add comment to task
- `GET /comments` - List all comments (filter by task_id)
- `GET /comments/{id}` - Get single comment
- `PATCH /comments/{id}` - Update comment
- `DELETE /comments/{id}` - Delete comment

### Labels
- `POST /labels` - Create label with color
- `GET /labels` - List all labels
- `GET /labels/{id}` - Get single label
- `PATCH /labels/{id}` - Update label
- `DELETE /labels/{id}` - Delete label

## 📝 Usage Examples

### Create a Task
```bash
curl -X POST "http://localhost:8000/tasks" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Implement authentication",
    "description": "Add JWT-based auth",
    "status": "todo",
    "priority": "high",
    "label_ids": [1, 2]
  }'
```

### Filter Tasks
```bash
# Get all high priority tasks
curl "http://localhost:8000/tasks?priority=high"

# Get tasks with specific label
curl "http://localhost:8000/tasks?label_id=1"

# Get in-progress tasks
curl "http://localhost:8000/tasks?status=in_progress"
```

### Add Comment
```bash
curl -X POST "http://localhost:8000/comments" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Started working on this",
    "author": "John Doe",
    "task_id": 1
  }'
```

## 🌱 Sample Data

Run the seed script to populate the database:
```bash
python seed.py
```

This creates:
- 5 sample tasks with different statuses
- 5 labels (Bug, Feature, Enhancement, Documentation, Urgent)
- 7 comments across tasks
- 5 activity logs

## 📁 Project Structure

```
FAST-API-3RD-SEM-/
├── app/
│   ├── models/              # SQLModel database models
│   │   ├── task.py
│   │   ├── comment.py
│   │   ├── label.py
│   │   └── activity_log.py
│   ├── schemas/             # Pydantic validation schemas
│   │   ├── task.py
│   │   ├── comment.py
│   │   ├── label.py
│   │   └── activity_log.py
│   ├── routers/             # API endpoints
│   │   ├── tasks.py
│   │   ├── comments.py
│   │   └── labels.py
│   ├── database.py          # Database configuration
│   └── main.py              # FastAPI application
├── seed.py                  # Database seed script
└── README.md                # This file
```

## 🔐 Validation Rules

### Task
- Title: 1-200 characters (required)
- Status: todo | in_progress | done
- Priority: low | medium | high

### Comment
- Content: 1-1000 characters (required)
- Author: 1-100 characters (required)

### Label
- Name: 1-50 characters (required, unique)
- Color: Valid hex color (#RRGGBB)

## 🎯 Development Status

### ✅ Completed (W1 & W2)
- [x] Database models with relationships
- [x] Pydantic schemas with validation
- [x] Task CRUD with filtering
- [x] Comment CRUD with activity logging
- [x] Label CRUD with validation
- [x] Many-to-many relationships
- [x] Database seed script
- [x] API documentation (Swagger)

### 📅 Planned (W3 & W4)
- [ ] Unit and integration tests (pytest)
- [ ] Advanced filtering and sorting
- [ ] Pagination
- [ ] Authentication & authorization
- [ ] Docker containerization

## 🧪 Testing

Access the interactive API documentation:
```
http://localhost:8000/docs
```

Use the "Try it out" feature to test all endpoints directly from your browser.

## 🤝 Contributing

This is a student project for learning purposes.

## 📄 License

This project is for educational purposes.

## 👤 Author

**Sanket Jadhav**
- GitHub: [@Sanketjadhav31](https://github.com/Sanketjadhav31)

## 🙏 Acknowledgments

- FastAPI documentation
- SQLModel documentation
- Project mentor and reviewers
