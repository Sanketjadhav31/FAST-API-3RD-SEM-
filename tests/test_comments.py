import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from app.models import Task, Comment


def test_create_comment(client: TestClient, session: Session):
    """Test creating a comment"""
    task = Task(title="Test Task")
    session.add(task)
    session.commit()
    
    response = client.post(
        "/comments",
        json={
            "content": "Test comment",
            "author": "John Doe",
            "task_id": task.id
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["content"] == "Test comment"
    assert data["author"] == "John Doe"
    assert data["task_id"] == task.id


def test_create_comment_invalid_task(client: TestClient):
    """Test creating a comment with invalid task_id"""
    response = client.post(
        "/comments",
        json={
            "content": "Test comment",
            "author": "John Doe",
            "task_id": 99999
        }
    )
    assert response.status_code == 404


def test_get_all_comments(client: TestClient, session: Session):
    """Test getting all comments"""
    task = Task(title="Test Task")
    session.add(task)
    session.commit()
    
    comment1 = Comment(content="Comment 1", author="User 1", task_id=task.id)
    comment2 = Comment(content="Comment 2", author="User 2", task_id=task.id)
    session.add(comment1)
    session.add(comment2)
    session.commit()
    
    response = client.get("/comments")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


def test_filter_comments_by_task(client: TestClient, session: Session):
    """Test filtering comments by task_id"""
    task1 = Task(title="Task 1")
    task2 = Task(title="Task 2")
    session.add(task1)
    session.add(task2)
    session.commit()
    
    comment1 = Comment(content="Comment 1", author="User", task_id=task1.id)
    comment2 = Comment(content="Comment 2", author="User", task_id=task2.id)
    session.add(comment1)
    session.add(comment2)
    session.commit()
    
    response = client.get(f"/comments?task_id={task1.id}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["task_id"] == task1.id


def test_update_comment(client: TestClient, session: Session):
    """Test updating a comment"""
    task = Task(title="Test Task")
    session.add(task)
    session.commit()
    
    comment = Comment(content="Original", author="User", task_id=task.id)
    session.add(comment)
    session.commit()
    
    response = client.patch(
        f"/comments/{comment.id}",
        json={"content": "Updated content"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["content"] == "Updated content"


def test_delete_comment(client: TestClient, session: Session):
    """Test deleting a comment"""
    task = Task(title="Test Task")
    session.add(task)
    session.commit()
    
    comment = Comment(content="Test", author="User", task_id=task.id)
    session.add(comment)
    session.commit()
    comment_id = comment.id
    
    response = client.delete(f"/comments/{comment_id}")
    assert response.status_code == 204
    
    # Verify comment is deleted
    response = client.get(f"/comments/{comment_id}")
    assert response.status_code == 404
