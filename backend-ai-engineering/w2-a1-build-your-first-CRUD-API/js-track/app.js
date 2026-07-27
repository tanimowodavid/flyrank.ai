import express from "express";
import swaggerUi from "swagger-ui-express";
import fs from "fs";
const app = express();
const port = 3000;

app.use(express.json());

// Load Swagger/OpenAPI document
const swaggerDocument = JSON.parse(
  fs.readFileSync(new URL("./swagger.json", import.meta.url), "utf-8"),
);

// Serve Swagger UI at /api-docs
app.use("/docs", swaggerUi.serve, swaggerUi.setup(swaggerDocument));

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

// PUT /tasks/:id
app.put("/tasks/:id", (req, res) => {
  // Find the task by ID
  const task = tasks.find((t) => t.id == req.params.id);

  // Return 404 if task doesn't exist
  if (!task) {
    return res.status(404).json({ error: `Task ${req.params.id} not found` });
  }

  const { title, done } = req.body;

  // Reject empty request body (400 Bad Request)
  if (title === undefined && done === undefined) {
    return res.status(400).json({ error: "Request body cannot be empty" });
  }

  // Validate title if provided
  if (title !== undefined) {
    if (typeof title !== "string" || title.trim() === "") {
      return res.status(400).json({ error: "Title cannot be empty" });
    }
    task.title = title.trim();
  }

  // Update done status if provided (allows true or false)
  if (done !== undefined) {
    task.done = Boolean(done);
  }

  // Return 200 OK with the updated task
  return res.status(200).json(task);
});

// DELETE /tasks/:id
app.delete("/tasks/:id", (req, res) => {
  // Find task index
  const index = tasks.findIndex((t) => t.id == req.params.id);

  // Return 404 if not found (-1 means not found)
  if (index === -1) {
    return res.status(404).json({ error: `Task ${req.params.id} not found` });
  }

  // Remove 1 item at 'index'
  tasks.splice(index, 1);

  // Send 204 No Content with an empty body
  return res.status(204).send();
});

app.get("/health", (req, res) => {
  res.json({ status: "ok" });
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
