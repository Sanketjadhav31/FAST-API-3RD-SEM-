# API Testing Examples

Quick reference for testing all endpoints after running the seed script.

## Tasks API

### Create Task
```bash
POST http://localhost:8000/tasks
Content-Type: application/json

{
  "title": "Implement search feature",
  "description": "Add full-text search to tasks",
  "status": "todo",
  "priority": "high",
  "label_ids": [1, 2]
}
```

### Get All Tasks
```bash
GET http://localhost:8000/tasks
```

### Filter Tasks by Status
```bash
GET http://localhost:8000/tasks?status=in_progress
```

### Filter Tasks by Priority
```bash
GET http://localhost:8000/tasks?priority=high
```

### Filter Tasks by Label
```bash
GET http://localhost:8000/tasks?label_id=1
```

### Get Single Task with Relations
```bash
GET http://localhost:8000/tasks/1
```

### Update Task
```bash
PATCH http://localhost:8000/tasks/1
Content-Type: application/json

{
  "status": "done",
  "priority": "low"
}
```

### Update Task Labels
```bash
PATCH http://localhost:8000/tasks/1
Content-Type: application/json

{
  "label_ids": [2, 3]
}
```

### Delete Task
```bash
DELETE http://localhost:8000/tasks/1
```

---

## Comments API

### Create Comment
```bash
POST http://localhost:8000/comments
Content-Type: application/json

{
  "content": "This is a great task!",
  "author": "Jane Doe",
  "task_id": 1
}
```

### Get All Comments
```bash
GET http://localhost:8000/comments
```

### Get Comments for Specific Task
```bash
GET http://localhost:8000/comments?task_id=1
```

### Get Single Comment
```bash
GET http://localhost:8000/comments/1
```

### Update Comment
```bash
PATCH http://localhost:8000/comments/1
Content-Type: application/json

{
  "content": "Updated comment text"
}
```

### Delete Comment
```bash
DELETE http://localhost:8000/comments/1
```

---

## Labels API

### Create Label
```bash
POST http://localhost:8000/labels
Content-Type: application/json

{
  "name": "Critical",
  "color": "#FF0000"
}
```

### Get All Labels
```bash
GET http://localhost:8000/labels
```

### Get Single Label
```bash
GET http://localhost:8000/labels/1
```

### Update Label
```bash
PATCH http://localhost:8000/labels/1
Content-Type: application/json

{
  "name": "High Priority",
  "color": "#FF5733"
}
```

### Delete Label
```bash
DELETE http://localhost:8000/labels/1
```

---

## Sample Data After Seeding

### Tasks Created:
1. Fix login authentication bug (IN_PROGRESS, HIGH) - Labels: Bug, Urgent
2. Implement user profile page (TODO, MEDIUM) - Labels: Feature
3. Write API documentation (TODO, LOW) - Labels: Documentation
4. Optimize database queries (DONE, HIGH) - Labels: Enhancement
5. Add email notifications (TODO, MEDIUM) - Labels: Feature, Enhancement

### Labels Created:
1. Bug (#FF0000)
2. Feature (#00FF00)
3. Enhancement (#0000FF)
4. Documentation (#FFA500)
5. Urgent (#FF1493)

### Comments Created:
- 2 comments on Task 1 (login bug)
- 2 comments on Task 2 (profile page)
- 1 comment on Task 3 (documentation)
- 2 comments on Task 4 (optimization)

---

## Testing Relationships

### Get Task with All Comments and Labels
```bash
GET http://localhost:8000/tasks/1
```

Response includes:
- Task details
- All comments array
- All labels array

### Create Task with Multiple Labels
```bash
POST http://localhost:8000/tasks
Content-Type: application/json

{
  "title": "Multi-label task",
  "description": "Testing many-to-many relationship",
  "status": "todo",
  "priority": "medium",
  "label_ids": [1, 2, 3]
}
```

---

## Testing Filters

### Combine Multiple Filters
```bash
# Get high priority tasks that are in progress
GET http://localhost:8000/tasks?status=in_progress&priority=high

# Get all tasks with "Bug" label (label_id=1)
GET http://localhost:8000/tasks?label_id=1
```

---

## Error Cases to Test

### 404 Not Found
```bash
GET http://localhost:8000/tasks/999
```

### 409 Conflict (Duplicate Label Name)
```bash
POST http://localhost:8000/labels
Content-Type: application/json

{
  "name": "Bug",
  "color": "#FF0000"
}
```

### 422 Validation Error (Invalid Status)
```bash
POST http://localhost:8000/tasks
Content-Type: application/json

{
  "title": "Test",
  "status": "invalid_status"
}
```

### 422 Validation Error (Invalid Color)
```bash
POST http://localhost:8000/labels
Content-Type: application/json

{
  "name": "Test",
  "color": "not-a-hex-color"
}
```

---

## Using Swagger UI

1. Go to http://localhost:8000/docs
2. Click on any endpoint
3. Click "Try it out"
4. Fill in the parameters
5. Click "Execute"
6. See the response below

Much easier than using curl!
