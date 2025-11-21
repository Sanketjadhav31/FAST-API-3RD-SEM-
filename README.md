# Task Management API

A modern, RESTful API for task management built with FastAPI, SQLModel, and Pydantic. This API provides comprehensive task tracking with comments, labels, and activity logging capabilities.

---

## 🚀 Features

- **Task Management**: Create, read, update, and delete tasks with status tracking
- **Priority System**: Organize tasks by priority (Low, Medium, High)
- **Status Workflow**: Track task progress (TODO, In Progress, Done)
- **Comments**: Add threaded discussions to tasks
- **Labels**: Categorize tasks with customizable color-coded labels
- **Activity Logging**: Automatic tracking of all task-related actions
- **Due Dates**: Set and track task deadlines

---

## 📋 Tech Stack

- **Framework**: FastAPI
- **ORM**: SQLModel (SQLAlchemy + Pydantic)
- **Validation**: Pydantic v2
- **Database**: SQLite/PostgreSQL (configurable)
- **Python**: 3.10+

---

## 📁 Project Structure

```
task-management-api/
├── app/
│   ├── models/              # SQLModel database models
│   │   ├── __init__.py
│   │   ├── task.py          # Task model with enums
│   │   ├── comment.py       # Comment model
│   │   ├── label.py         # Label & TaskLabel models
│   │   └── activity_log.py  # Activity log model
│   │
│   └── schemas/             # Pydantic schemas for validation
│       ├── __init__.py
│       ├── task.py          # Task CRUD schemas
│       ├── comment.py       # Comment CRUD schemas
│       ├── label.py         # Label CRUD schemas
│       └── activity_log.py  # Activity log read schema
│
├── SCHEMAS_README.md        # Detailed schema documentation
├── DAYWISE_TASKS.md         # Development task breakdown
└── README.md                # This file
```

---

## 🗄️ Database Schema

### Core Models

#### Task
- **Fields**: id, title, description, status, priority, due_date, created_at, updated_at
- **Relationships**: comments, labels (many-to-many), activity_logs
- **Enums**: TaskStatus (TODO, IN_PROGRESS, DONE), TaskPriority (LOW, MEDIUM, HIGH)

#### Comment
- **Fields**: id, content, author, task_id, created_at, updated_at
- **Relationships**: task (many-to-one)

#### Label
- **Fields**: id, name, color
- **Relationships**: tasks (many-to-many via TaskLabel)

#### TaskLabel (Junction Table)
- **Fields**: task_id, label_id
- **Purpose**: Many-to-many relationship between tasks and labels

#### ActivityLog
- **Fields**: id, task_id, action, description, performed_by, created_at
- **Relationships**: task (many-to-one)
- **Purpose**: Audit trail for task changes

---

## 📝 API Schemas

### Task Schemas
- `TaskCreate`: Create new tasks with optional label assignments
- `TaskUpdate`: Partial updates to existing tasks
- `TaskRead`: Basic task response
- `TaskReadWithRelations`: Task with comments and labels included

### Comment Schemas
- `CommentCreate`: Add comments to tasks
- `CommentUpdate`: Edit comment content
- `CommentRead`: Comment response with metadata

### Label Schemas
- `LabelCreate`: Create color-coded labels
- `LabelUpdate`: Modify label name or color
- `LabelRead`: Label response

### Activity Log Schema
- `ActivityLogRead`: Read-only activity log entries

For detailed schema documentation, see [SCHEMAS_README.md](SCHEMAS_README.md)

---

## 🔧 Installation

### Prerequisites
- Python 3.10 or higher
- pip or poetry for package management

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd task-management-api
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install fastapi sqlmodel pydantic uvicorn
```

4. **Run the application**
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

---

## 📚 API Documentation

Once the server is running, access:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 🎯 Usage Examples

### Create a Task
```python
POST /tasks
{
  "title": "Implement authentication",
  "description": "Add JWT-based authentication",
  "status": "todo",
  "priority": "high",
  "due_date": "2025-12-31T23:59:59",
  "label_ids": [1, 2]
}
```

### Add a Comment
```python
POST /comments
{
  "content": "Started working on this task",
  "author": "John Doe",
  "task_id": 1
}
```

### Create a Label
```python
POST /labels
{
  "name": "Bug",
  "color": "#FF0000"
}
```

### Update Task Status
```python
PATCH /tasks/1
{
  "status": "in_progress"
}
```

---

## 🔐 Validation Rules

### Task
- Title: 1-200 characters (required)
- Status: Must be one of: todo, in_progress, done
- Priority: Must be one of: low, medium, high

### Comment
- Content: 1-1000 characters (required)
- Author: 1-100 characters (required)

### Label
- Name: 1-50 characters (required, unique)
- Color: Valid hex color code (e.g., #FF5733)

---

## 🏗️ Development Status

### ✅ Completed
- [x] Database models (SQLModel)
- [x] Pydantic schemas with validation
- [x] Model relationships and foreign keys
- [x] Enum definitions for status and priority
- [x] Activity logging structure

### 🚧 In Progress
- [ ] API endpoints (CRUD operations)
- [ ] Database initialization and migrations
- [ ] Business logic and services layer

### 📅 Planned
- [ ] Authentication & authorization
- [ ] API rate limiting
- [ ] Pagination and filtering
- [ ] Search functionality
- [ ] Unit and integration tests
- [ ] Docker containerization
- [ ] CI/CD pipeline

---

## 📖 Documentation

- **[SCHEMAS_README.md](SCHEMAS_README.md)**: Complete schema documentation with examples
- **[DAYWISE_TASKS.md](DAYWISE_TASKS.md)**: 2-day development plan for schema completion

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👥 Authors

Your Name - Initial work

---

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- SQLModel for seamless ORM integration
- Pydantic for robust data validation

---

## 📞 Support

For questions or issues, please open an issue on GitHub.

---

**Built with ❤️ using FastAPI and SQLModel**
