# backend/test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_todo():
    response = client.post("/todos", json={"id": 1, "task": "Test task", "completed": False})
    assert response.status_code == 200

def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_todo():
    client.post("/todos", json={"id": 2, "task": "Update me", "completed": False})
    response = client.put("/todos/2", json={"id": 2, "task": "Updated", "completed": True})
    assert response.status_code == 200
    assert response.json()["completed"] == True

def test_delete_todo():
    client.post("/todos", json={"id": 3, "task": "Delete me", "completed": False})
    response = client.delete("/todos/3")
    assert response.status_code == 200
