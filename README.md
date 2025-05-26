# To-Do List Application

## 1. Project Overview
A simple full-stack To-Do List app that allows users to add, view, and delete tasks. Built using FastAPI for the backend and vanilla JavaScript for the frontend, with automated backend testing using Pytest and HTTPX.

## 2. Features
- Add tasks with unique IDs
- View all tasks
- Delete tasks by ID
- Automated backend tests
- Frontend communicates with backend using Fetch API
- CORS enabled for frontend-backend interaction

## 3. Technologies Used
- **Frontend:** HTML, CSS, JavaScript (Fetch API)
- **Backend:** Python, FastAPI, Pydantic
- **Testing:** Pytest, HTTPX
- **Server:** Uvicorn
- **Tools:** Python virtual environment (venv)

## 4. Setup Instructions

### Backend

1. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\activate


2. Install dependencies:
pip install fastapi uvicorn pytest httpx

3. Start the backend server:
uvicorn main:app --reload

### Frontend
Open frontend/index.html in a web browser.

## 5. API Endpoints
Method	 Endpoint	 Description
POST	 /todos	        Add a new todo
GET	     /todos	        List all todos
DELETE	 /todos/{id}	Delete a todo by ID

## 6. Running Test
pytest test_main.py

