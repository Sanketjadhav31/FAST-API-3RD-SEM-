# Task Management API

A production-ready RESTful API for task management built with FastAPI, SQLModel, and Pydantic.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-green.svg)](https://fastapi.tiangolo.com/)
[![Tests](https://img.shields.io/badge/Tests-23%20passed-success.svg)](tests/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📐 Architecture Diagrams

### High-Level Design (HLD)
![High-Level Design](docs/HLD_dig.png)

### Request-Response Flow
![Request-Response Flow](docs/REQ_RES.png)

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

## 🔧 Installation & Setup

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Git

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/Sanketjadhav31/FAST-API-3RD-SEM-.git
cd FAST-API-3RD-SEM-
```

2. **Create virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
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

### Docker Setup (Alternative)

```bash
# Using Docker Compose
docker-compose up

# Or build and run manually
docker build -t task-api .
docker run -p 8000:8000 task-api
```

## 📚 API Documentation

Once the server is running:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🎯 API Endpoints

### Tasks
- `POST /tasks` - Create task with optional labels
- `GET /tasks` - List all tasks (supports filters, sorting, pagination)
- `GET /tasks/{id}` - Get task with comments and labels
- `PATCH /tasks/{id}` - Update task
- `DELETE /tasks/{id}` - Delete task

**Filters**: `?status=in_progress&priority=high&label_id=1`
**Sorting**: `?sort_by=created_at&sort_order=desc`
**Pagination**: `?skip=0&limit=10`

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

### Activity Logs
- `GET /activity-logs` - List all activity logs (with filters)
- `GET /activity-logs/{id}` - Get single activity log
- `GET /activity-logs/task/{task_id}` - Get logs for specific task

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

## 🎯 Project Status

### ✅ Completed Features
- [x] Complete CRUD operations (Tasks, Comments, Labels)
- [x] Database models with relationships
- [x] Pydantic schemas with validation
- [x] Advanced filtering and sorting
- [x] Pagination support
- [x] Activity logging system
- [x] Many-to-many relationships
- [x] Database seed script
- [x] Comprehensive test suite (23 tests)
- [x] API documentation (Swagger/ReDoc)
- [x] Docker support
- [x] Production-ready code

### 🚀 Future Enhancements
- [ ] JWT Authentication & Authorization
- [ ] User management system
- [ ] WebSocket for real-time updates
- [ ] File attachments for tasks
- [ ] Email notifications
- [ ] Task assignments to users
- [ ] PostgreSQL support
- [ ] CI/CD pipeline

## 🧪 Testing

### Automated Tests
Run the test suite with pytest:
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=app --cov-report=html
```

**Test Coverage**: 23 tests covering all CRUD operations, filtering, validation, and error handling.

### Test Results
```
======================== 23 passed in <2s ==========================
```

### Manual Testing
Access the interactive API documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

Use the "Try it out" feature to test all endpoints directly from your browser.

## 🚀 Deployment

### Deploy to Render (Recommended)

**Free tier available!** Complete guide: [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md)

**Quick Deploy**:
1. Push code to GitHub ✓ (already done)
2. Sign up at [render.com](https://render.com)
3. Connect your repository
4. Configure and deploy (2-5 minutes)
5. Your API is live! 🎉

**Live URL**: `https://your-app-name.onrender.com`

### Setup PostgreSQL (Recommended for Production)

**Quick Guide**: [QUICK_POSTGRESQL.md](QUICK_POSTGRESQL.md) - 3 steps, 5 minutes

1. Create PostgreSQL database on Render (Free)
2. Copy Internal Database URL
3. Update DATABASE_URL in your web service
4. Auto-redeploys with PostgreSQL! ✅

### Environment Variables
Create a `.env` file for local development:
```env
DATABASE_URL=sqlite:///./task_management.db
# For PostgreSQL: postgresql://user:password@localhost/dbname
ENVIRONMENT=development
LOG_LEVEL=INFO
```

### Production Deployment (Self-Hosted)
```bash
# Install production dependencies
pip install -r requirements.txt

# Run with production server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Docker Deployment
```bash
docker-compose up -d
```

For detailed deployment guides, see [DEPLOYMENT.md](DEPLOYMENT.md)

## 📊 API Performance

- Response time: < 100ms for simple queries
- Supports pagination for large datasets
- Optimized database queries with proper indexes
- CORS enabled for cross-origin requests

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Sanket Jadhav**
- GitHub: [@Sanketjadhav31](https://github.com/Sanketjadhav31)
- Project: [Task Management API](https://github.com/Sanketjadhav31/FAST-API-3RD-SEM-)

## 🙏 Acknowledgments

- FastAPI framework and documentation
- SQLModel for seamless ORM integration
- The Python community
- Project mentors and reviewers

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: [GitHub Profile](https://github.com/Sanketjadhav31)

---

**Made with ❤️ using FastAPI**
