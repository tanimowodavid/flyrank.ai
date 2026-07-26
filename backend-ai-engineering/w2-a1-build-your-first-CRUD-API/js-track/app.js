const express = require("express");
const app = express();
const port = 3000;

let tasks = [
  { id: 1, name: "Task 1", done: false },
  { id: 2, name: "Task 2", done: false },
  { id: 3, name: "Task 3", done: true },
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

app.get("/health", (req, res) => {
  res.json({ status: "ok" });
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
