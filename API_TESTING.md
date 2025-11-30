# 🧪 Complete API Testing Guide

**Live API**: https://task-management-api-q19j.onrender.com

### 1️⃣ Health & Root Endpoints

#### Test Root
```bash
curl https://task-management-api-q19j.onrender.com/
```
**Expected Response**:
```json
{
  "message": "Welcome to Task Management API",
  "version": "1.0.0",
  "docs": "/docs",
  "redoc": "/redoc"
}
```

#### Test Health Check
```bash
curl https://task-management-api-q19j.onrender.com/health
```
**Expected Response**:
```json
{
  "status": "healthy"
}
```

---

### 2️⃣ Tasks API

#### Create Task
```bash
curl -X POST https://task-management-api-q19j.onrender.com/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete Project Documentation",
    "description": "Write comprehensive API documentation",
    "status": "todo",
    "priority": "high"
  }'
```

#### Create Task with Labels
```bash
curl -X POST https://task-management-api-q19j.onrender.com/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Fix Authentication Bug",
    "description": "Users cannot login",
    "status": "in_progress",
    "priority": "high",
    "label_ids": [1, 2]
  }'
```

#### Get All Tasks
```bash
curl https://task-management-api-q19j.onrender.com/tasks
```

#### Get Single Task (with relations)
```bash
curl https://task-management-api-q19j.onrender.com/tasks/1
```

#### Filter Tasks by Status
```bash
curl "https://task-management-api-q19j.onrender.com/tasks?status=todo"
```

#### Filter Tasks by Priority
```bash
curl "https://task-management-api-q19j.onrender.com/tasks?priority=high"
```

#### Filter Tasks by Label
```bash
curl "https://task-management-api-q19j.onrender.com/tasks?label_id=1"
```

#### Sort Tasks
```bash
# Sort by priority (descending)
curl "https://task-management-api-q19j.onrender.com/tasks?sort_by=priority&sort_order=desc"

# Sort by created date (ascending)
curl "https://task-management-api-q19j.onrender.com/tasks?sort_by=created_at&sort_order=asc"
```

#### Pagination
```bash
# Get first 5 tasks
curl "https://task-management-api-q19j.onrender.com/tasks?skip=0&limit=5"

# Get next 5 tasks
curl "https://task-management-api-q19j.onrender.com/tasks?skip=5&limit=5"
```

#### Combined Filters
```bash
curl "https://task-management-api-q19j.onrender.com/tasks?status=in_progress&priority=high&sort_by=created_at&sort_order=desc&limit=10"
```

#### Update Task
```bash
curl -X PATCH https://task-management-api-q19j.onrender.com/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "done",
    "priority": "low"
  }'
```

#### Delete Task
```bash
curl -X DELETE https://task-management-api-q19j.onrender.com/tasks/1
```

---

### 3️⃣ Labels API

#### Create Label
```bash
curl -X POST https://task-management-api-q19j.onrender.com/labels \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Bug",
    "color": "#FF0000"
  }'
```

#### Create Multiple Labels
```bash
# Feature Label
curl -X POST https://task-management-api-q19j.onrender.com/labels \
  -H "Content-Type: application/json" \
  -d '{"name": "Feature", "color": "#00FF00"}'

# Enhancement Label
curl -X POST https://task-management-api-q19j.onrender.com/labels \
  -H "Content-Type: application/json" \
  -d '{"name": "Enhancement", "color": "#0000FF"}'

# Documentation Label
curl -X POST https://task-management-api-q19j.onrender.com/labels \
  -H "Content-Type: application/json" \
  -d '{"name": "Documentation", "color": "#FFA500"}'

# Urgent Label
curl -X POST https://task-management-api-q19j.onrender.com/labels \
  -H "Content-Type: application/json" \
  -d '{"name": "Urgent", "color": "#FF1493"}'
```

#### Get All Labels
```bash
curl https://task-management-api-q19j.onrender.com/labels
```

#### Get Single Label
```bash
curl https://task-management-api-q19j.onrender.com/labels/1
```

#### Update Label
```bash
curl -X PATCH https://task-management-api-q19j.onrender.com/labels/1 \
  -H "Content-Type: application/json" \
  -d '{
    "color": "#FF6600"
  }'
```

#### Delete Label
```bash
curl -X DELETE https://task-management-api-q19j.onrender.com/labels/1
```

---

### 4️⃣ Comments API

#### Create Comment
```bash
curl -X POST https://task-management-api-q19j.onrender.com/comments \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Started working on this task",
    "author": "John Doe",
    "task_id": 1
  }'
```

#### Create Multiple Comments
```bash
# Comment 1
curl -X POST https://task-management-api-q19j.onrender.com/comments \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Found the root cause of the issue",
    "author": "Jane Smith",
    "task_id": 1
  }'

# Comment 2
curl -X POST https://task-management-api-q19j.onrender.com/comments \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Will complete this by tomorrow",
    "author": "John Doe",
    "task_id": 1
  }'
```

#### Get All Comments
```bash
curl https://task-management-api-q19j.onrender.com/comments
```

#### Get Comments by Task
```bash
curl "https://task-management-api-q19j.onrender.com/comments?task_id=1"
```

#### Get Single Comment
```bash
curl https://task-management-api-q19j.onrender.com/comments/1
```

#### Update Comment
```bash
curl -X PATCH https://task-management-api-q19j.onrender.com/comments/1 \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Updated: Task completed successfully"
  }'
```

#### Delete Comment
```bash
curl -X DELETE https://task-management-api-q19j.onrender.com/comments/1
```

---

### 5️⃣ Activity Logs API

#### Get All Activity Logs
```bash
curl https://task-management-api-q19j.onrender.com/activity-logs
```

#### Get Activity Logs with Pagination
```bash
curl "https://task-management-api-q19j.onrender.com/activity-logs?skip=0&limit=10"
```

#### Get Activity Logs by Task
```bash
curl https://task-management-api-q19j.onrender.com/activity-logs/task/1
```

#### Filter Activity Logs by Action
```bash
curl "https://task-management-api-q19j.onrender.com/activity-logs?action=created"
```

#### Get Single Activity Log
```bash
curl https://task-management-api-q19j.onrender.com/activity-logs/1
```

---

## 🎯 Complete Test Workflow

### Step 1: Create Labels
```bash
curl -X POST https://task-management-api-q19j.onrender.com/labels \
  -H "Content-Type: application/json" \
  -d '{"name": "Bug", "color": "#FF0000"}'

curl -X POST https://task-management-api-q19j.onrender.com/labels \
  -H "Content-Type: application/json" \
  -d '{"name": "Feature", "color": "#00FF00"}'
```

### Step 2: Create Task with Labels
```bash
curl -X POST https://task-management-api-q19j.onrender.com/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Fix Login Bug",
    "description": "Users cannot login with correct credentials",
    "status": "in_progress",
    "priority": "high",
    "label_ids": [1, 2]
  }'
```

### Step 3: Add Comments
```bash
curl -X POST https://task-management-api-q19j.onrender.com/comments \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Investigating the issue",
    "author": "Developer",
    "task_id": 1
  }'
```

### Step 4: Update Task Status
```bash
curl -X PATCH https://task-management-api-q19j.onrender.com/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "done"}'
```

### Step 5: View Activity Logs
```bash
curl https://task-management-api-q19j.onrender.com/activity-logs/task/1
```

---

## 🔍 Advanced Testing

### Test Error Handling

#### 404 - Not Found
```bash
curl https://task-management-api-q19j.onrender.com/tasks/99999
```

#### 409 - Duplicate Label
```bash
# Create label
curl -X POST https://task-management-api-q19j.onrender.com/labels \
  -H "Content-Type: application/json" \
  -d '{"name": "Bug", "color": "#FF0000"}'

# Try to create same label again
curl -X POST https://task-management-api-q19j.onrender.com/labels \
  -H "Content-Type: application/json" \
  -d '{"name": "Bug", "color": "#00FF00"}'
```

#### 422 - Validation Error
```bash
# Invalid color format
curl -X POST https://task-management-api-q19j.onrender.com/labels \
  -H "Content-Type: application/json" \
  -d '{"name": "Test", "color": "red"}'

# Missing required field
curl -X POST https://task-management-api-q19j.onrender.com/tasks \
  -H "Content-Type: application/json" \
  -d '{"description": "No title provided"}'
```

---

## 📊 Test Results Checklist

### ✅ Basic Tests
- [ ] Root endpoint returns welcome message
- [ ] Health check returns healthy status
- [ ] Swagger UI loads at /docs
- [ ] ReDoc loads at /redoc

### ✅ Tasks
- [ ] Create task without labels
- [ ] Create task with labels
- [ ] Get all tasks
- [ ] Get single task with relations
- [ ] Filter by status
- [ ] Filter by priority
- [ ] Filter by label
- [ ] Sort tasks
- [ ] Paginate results
- [ ] Update task
- [ ] Delete task

### ✅ Labels
- [ ] Create label
- [ ] Get all labels
- [ ] Get single label
- [ ] Update label
- [ ] Delete label
- [ ] Duplicate name validation

### ✅ Comments
- [ ] Create comment
- [ ] Get all comments
- [ ] Filter by task
- [ ] Get single comment
- [ ] Update comment
- [ ] Delete comment

### ✅ Activity Logs
- [ ] Get all logs
- [ ] Get logs by task
- [ ] Filter by action
- [ ] Pagination works

### ✅ Error Handling
- [ ] 404 for non-existent resources
- [ ] 409 for duplicate labels
- [ ] 422 for validation errors

---

## 🎨 Using Swagger UI (Recommended)

1. **Open**: https://task-management-api-q19j.onrender.com/docs

2. **Test Tasks**:
   - Expand "Tasks" section
   - Click "POST /tasks"
   - Click "Try it out"
   - Fill in the request body
   - Click "Execute"
   - See response below

3. **Test All Endpoints**:
   - Repeat for each endpoint
   - See request/response examples
   - Test different parameters

---

## 📱 Using Postman

1. **Import Collection**:
   - Open Postman
   - Click "Import"
   - Select `postman_collection.json`
   - Collection imported!

2. **Set Base URL**:
   - Edit collection
   - Set variable: `baseUrl = https://task-management-api-q19j.onrender.com`

3. **Run Tests**:
   - Click any request
   - Click "Send"
   - View response

---

## 🐛 Troubleshooting

### API Not Responding?
```bash
# Check if service is up
curl https://task-management-api-q19j.onrender.com/health
```

### Getting 404 Errors?
- Check the URL is correct
- Ensure resource exists (create it first)

### Getting 422 Validation Errors?
- Check request body format
- Ensure all required fields are present
- Verify data types match schema

### Database Empty?
```bash
# Seed the database (if you have shell access)
python seed.py
```

---

## 📈 Performance Testing

### Test Response Times
```bash
# Using curl with timing
curl -w "\nTime: %{time_total}s\n" https://task-management-api-q19j.onrender.com/tasks
```

### Load Testing (Optional)
```bash
# Using Apache Bench (if installed)
ab -n 100 -c 10 https://task-management-api-q19j.onrender.com/tasks
```

---

## 🎉 Success Criteria

Your API is working correctly if:
- ✅ All health checks pass
- ✅ Can create, read, update, delete tasks
- ✅ Can create, read, update, delete labels
- ✅ Can create, read, update, delete comments
- ✅ Activity logs are created automatically
- ✅ Filtering and sorting work
- ✅ Pagination works
- ✅ Error handling works correctly
- ✅ Swagger UI is accessible

---

## 📞 Support

- **API Docs**: https://task-management-api-q19j.onrender.com/docs
- **ReDoc**: https://task-management-api-q19j.onrender.com/redoc
- **GitHub**: https://github.com/Sanketjadhav31/FAST-API-3RD-SEM-

---

**Happy Testing! 🚀**
