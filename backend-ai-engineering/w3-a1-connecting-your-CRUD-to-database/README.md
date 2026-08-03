# Week 3 Assignment: connecting your CRUD to database

This directory contains the Python/FastAPI implementation of the Week 3 assignment. Dependencies are managed with [`uv`](https://docs.astral.sh/uv/).

## Stack and prerequisites

- Python `>= 3.12`
- FastAPI with the standard dependencies
- Uvicorn, through the FastAPI CLI
- `uv`

## Installation and running

From this directory, create the environment and install the locked dependencies:

```bash
uv venv
uv sync
```

Activate the environment only if you want to run commands without `uv run`:

```bash
# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows Command Prompt
.venv\Scripts\activate.bat
```

Start the development server:

```bash
uv run fastapi dev
```

The API is available at `http://127.0.0.1:8000`. FastAPI also provides:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- OpenAPI schema: http://127.0.0.1:8000/openapi.json

## API endpoints

All application routes use the `/api/v1` prefix. The trailing slash shown for collection and root routes is the canonical route; FastAPI redirects the slashless form.

| Method | Endpoint                  | Description                              |
| ------ | ------------------------- | ---------------------------------------- |
| GET    | `/api/v1/`                | Return API name, version, and docs path. |
| GET    | `/api/v1/health`          | Return health status and process uptime. |
| GET    | `/api/v1/tasks/`          | List all tasks.                          |
| POST   | `/api/v1/tasks/`          | Create a task. Returns `201 Created`.    |
| GET    | `/api/v1/tasks/{task_id}` | Retrieve one task by integer ID.         |
| PUT    | `/api/v1/tasks/{task_id}` | Partially update `title` and/or `done`.  |
| DELETE | `/api/v1/tasks/{task_id}` | Delete a task. Returns `204 No Content`. |

## Request and response examples

Create a task:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Finish FlyRank Assignment"}'
```

```json
{
  "id": 4,
  "title": "Finish FlyRank Assignment",
  "done": false
}
```

List tasks and retrieve a specific task:

```bash
curl http://127.0.0.1:8000/api/v1/tasks/
curl http://127.0.0.1:8000/api/v1/tasks/1
```

Update or delete a task:

```bash
curl -X PUT http://127.0.0.1:8000/api/v1/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done":true}'

curl -i -X DELETE http://127.0.0.1:8000/api/v1/tasks/1
```

## Database Architecture (Week 3 — Stage 0 to 5)

### Why SQLite?

- **Zero-Configuration:** Stored directly as a single file on disk, making setup seamless across development environments.
- **ACID Compliant:** Offers full transactional integrity without needing an external database server running in a separate process.
- **Fast & Embedded:** Executes directly inside the Python runtime environment, minimizing local network latency during testing.
- **Easy to Migrate:** Can be easily swapped out for a more robust database solution like PostgreSQL or MySQL.

### Database File Location

The database is initialized as an embedded file stored at the project root:

### Database Schema

| Column Name | Data Type | Description |
| ----------- | --------- | ----------- |
| id          | INTEGER   | Primary key |
| title       | TEXT      | Task title  |
| done        | BOOLEAN   | Task status |

### Database Seeding

The database is seeded with 3 example tasks on startup. This is done to ensure the database is populated with data and can be used for testing.

### Database Viewer & Sample SQL

You can inspect and manipulate the underlying tasks.db file using DB Browser for SQLite or VS Code's SQLite extension.

Example SQL Queries Tested

```sql
-- 1. Fetch all tasks
SELECT \* FROM tasks;

-- 2. Fetch completed tasks only
SELECT id, title, done FROM tasks WHERE done = 1;

-- 3. Count total tasks in database
SELECT COUNT(\*) AS total_tasks FROM tasks;

-- 4. Mark all tasks as completed
UPDATE tasks SET done = 1;

-- 5. Delete completed tasks
DELETE FROM tasks WHERE done = 1;
```
