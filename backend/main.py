from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # <-- Import CORS middleware
from pydantic import BaseModel

app = FastAPI()

# Add this CORS middleware block right after app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # Allow all origins for dev; restrict in prod
    allow_credentials=True,
    allow_methods=["*"],            # Allow all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],            # Allow all headers
)

todos = {}

class Todo(BaseModel):
    id: int
    task: str
    completed: bool = False

@app.post("/todos")
def add_todo(todo: Todo):
    if todo.id in todos:
        raise HTTPException(status_code=400, detail="Todo already exists")
    todos[todo.id] = todo
    return todo

@app.get("/todos")
def get_todos():
    return list(todos.values())

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    todos[todo_id] = todo
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
    return {"message": "Todo deleted"}
