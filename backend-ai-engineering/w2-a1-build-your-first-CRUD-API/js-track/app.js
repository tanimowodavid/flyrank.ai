const express = require("express");
const app = express();
const port = 3000;

app.use(express.json());

let tasks = [
  { id: 1, title: "Task 1", done: false },
  { id: 2, title: "Task 2", done: false },
  { id: 3, title: "Task 3", done: true },
];

// Base endpoint
app.get("/", (req, res) => {
  res.json({ name: "Task API", version: "1.0", endpoints: ["/tasks"] });
});

// GET all tasks
app.get("/tasks", (req, res) => {
  res.json({ tasks }); // Shortened from { tasks: tasks }
});

// GET task by ID
app.get("/tasks/:id", (req, res) => {
  const task = tasks.find((t) => t.id == req.params.id);

  if (!task) {
    return res.status(404).json({ error: `Task ${req.params.id} not found` });
  }

  return res.json(task);
});

// POST new task
app.post("/tasks", (req, res) => {
  const { title } = req.body;

  // Validate input: check if title is missing or empty
  if (!title || title.trim() === "") {
    return res.status(400).json({
      error: "Title is required and cannot be empty",
    });
  }

  // Generate next free ID (find highest existing ID and add 1)
  const nextId = tasks.length > 0 ? Math.max(...tasks.map((t) => t.id)) + 1 : 1;

  // Create new task object
  const newTask = {
    id: nextId,
    title: title.trim(),
    done: false,
  };

  // Add to list and return 201 Created
  tasks.push(newTask);
  return res.status(201).json(newTask);
});

app.get("/health", (req, res) => {
  res.json({ status: "ok" });
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
