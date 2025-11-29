import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from app.models import Label


def test_create_label(client: TestClient):
    """Test creating a new label"""
    response = client.post(
        "/labels",
        json={"name": "Bug", "color": "#FF0000"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Bug"
    assert data["color"] == "#FF0000"
    assert "id" in data


def test_create_duplicate_label(client: TestClient, session: Session):
    """Test creating a label with duplicate name"""
    label = Label(name="Bug", color="#FF0000")
    session.add(label)
    session.commit()
    
    response = client.post(
        "/labels",
        json={"name": "Bug", "color": "#00FF00"}
    )
    assert response.status_code == 409


def test_get_all_labels(client: TestClient, session: Session):
    """Test getting all labels"""
    label1 = Label(name="Bug", color="#FF0000")
    label2 = Label(name="Feature", color="#00FF00")
    session.add(label1)
    session.add(label2)
    session.commit()
    
    response = client.get("/labels")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


def test_get_single_label(client: TestClient, session: Session):
    """Test getting a single label"""
    label = Label(name="Bug", color="#FF0000")
    session.add(label)
    session.commit()
    
    response = client.get(f"/labels/{label.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Bug"
    assert data["color"] == "#FF0000"


def test_update_label(client: TestClient, session: Session):
    """Test updating a label"""
    label = Label(name="Bug", color="#FF0000")
    session.add(label)
    session.commit()
    
    response = client.patch(
        f"/labels/{label.id}",
        json={"color": "#0000FF"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["color"] == "#0000FF"
    assert data["name"] == "Bug"


def test_delete_label(client: TestClient, session: Session):
    """Test deleting a label"""
    label = Label(name="Bug", color="#FF0000")
    session.add(label)
    session.commit()
    label_id = label.id
    
    response = client.delete(f"/labels/{label_id}")
    assert response.status_code == 204
    
    # Verify label is deleted
    response = client.get(f"/labels/{label_id}")
    assert response.status_code == 404


def test_invalid_color_format(client: TestClient):
    """Test creating a label with invalid color format"""
    response = client.post(
        "/labels",
        json={"name": "Bug", "color": "red"}
    )
    assert response.status_code == 422
