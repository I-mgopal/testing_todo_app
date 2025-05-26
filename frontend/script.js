const API = "http://127.0.0.1:8000/todos";

async function addTask() {
  const taskInput = document.getElementById("taskInput");
  const task = taskInput.value;
  const id = Date.now();

  await fetch(API, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ id, task, completed: false })
  });

  taskInput.value = "";
  loadTasks();
}

async function deleteTask(id) {
  await fetch(`${API}/${id}`, {
    method: "DELETE"
  });
  loadTasks();
}

async function loadTasks() {
  const response = await fetch(API);
  const todos = await response.json();
  const list = document.getElementById("taskList");
  list.innerHTML = "";
  todos.forEach(todo => {
    const li = document.createElement("li");
    li.textContent = todo.task;

    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";
    deleteBtn.style.marginLeft = "10px";
    deleteBtn.onclick = () => deleteTask(todo.id);

    li.appendChild(deleteBtn);
    list.appendChild(li);
  });
}

window.onload = loadTasks;
