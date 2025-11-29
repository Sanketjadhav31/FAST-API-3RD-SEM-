import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from app.models import Task, Label, TaskLabel
from app.models.task import TaskStatus, TaskPriority


def test_create_task(client: TestClient):
    """Test creating a new task"""
    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "description": "Test Description",
            "status": "todo",
            "priority": "high"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test Description"
    assert data["status"] == "todo"
    assert data["priority"] == "high"
    assert "id" in data


def test_create_task_with_labels(client: TestClient, session: Session):
    """Test creating a task with labels"""
    # Create labels first
    label1 = Label(name="Bug", color="#FF0000")
    label2 = Label(name="Feature", color="#00FF00")
    session.add(label1)
    session.add(label2)
    session.commit()
    
    response = client.post(
        "/tasks",
        json={
            "title": "Task with Labels",
            "description": "Test",
            "label_ids": [label1.id, label2.id]
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Task with Labels"


def test_get_all_tasks(client: TestClient, session: Session):
    """Test getting all tasks"""
    # Create test tasks
    task1 = Task(title="Task 1", status=TaskStatus.TODO)
    task2 = Task(title="Task 2", status=TaskStatus.IN_PROGRESS)
    session.add(task1)
    session.add(task2)
    session.commit()
    
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


def test_filter_tasks_by_status(client: TestClient, session: Session):
    """Test filtering tasks by status"""
    task1 = Task(title="Task 1", status=TaskStatus.TODO)
    task2 = Task(title="Task 2", status=TaskStatus.DONE)
    session.add(task1)
    session.add(task2)
    session.commit()
    
    response = client.get("/tasks?status=todo")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["status"] == "todo"


def test_filter_tasks_by_priority(client: TestClient, session: Session):
    """Test filtering tasks by priority"""
    task1 = Task(title="Task 1", priority=TaskPriority.HIGH)
    task2 = Task(title="Task 2", priority=TaskPriority.LOW)
    session.add(task1)
    session.add(task2)
    session.commit()
    
    response = client.get("/tasks?priority=high")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["priority"] == "high"


def test_filter_tasks_by_label(client: TestClient, session: Session):
    """Test filtering tasks by label"""
    label = Label(name="Bug", color="#FF0000")
    session.add(label)
    session.commit()
    
    task1 = Task(title="Task 1")
    task2 = Task(title="Task 2")
    session.add(task1)
    session.add(task2)
    session.commit()
    
    # Assign label to task1 only
    task_label = TaskLabel(task_id=task1.id, label_id=label.id)
    session.add(task_label)
    session.commit()
    
    response = client.get(f"/tasks?label_id={label.id}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Task 1"


def test_get_task_with_relations(client: TestClient, session: Session):
    """Test getting a task with comments and labels"""
    task = Task(title="Task with Relations")
    session.add(task)
    session.commit()
    
    response = client.get(f"/tasks/{task.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Task with Relations"
    assert "comments" in data
    assert "labels" in data


def test_update_task(client: TestClient, session: Session):
    """Test updating a task"""
    task = Task(title="Original Title", status=TaskStatus.TODO)
    session.add(task)
    session.commit()
    
    response = client.patch(
        f"/tasks/{task.id}",
        json={"title": "Updated Title", "status": "done"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["status"] == "done"


def test_delete_task(client: TestClient, session: Session):
    """Test deleting a task"""
    task = Task(title="Task to Delete")
    session.add(task)
    session.commit()
    task_id = task.id
    
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204
    
    # Verify task is deleted
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404


def test_get_nonexistent_task(client: TestClient):
    """Test getting a task that doesn't exist"""
    response = client.get("/tasks/99999")
    assert response.status_code == 404
