# Week 2 Assignment: FastAPI CRUD API (Python Track)

This directory contains the Python/FastAPI implementation of the Week 2 CRUD API assignment. Dependencies are managed with [`uv`](https://docs.astral.sh/uv/).

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

## Validation and behavior

- `title` is required when creating a task and must contain at least one character.
- `done` defaults to `false` when omitted.
- Updates are partial, so send only the fields that should change.
- Task titles must be unique, case-insensitively. A duplicate returns `400 Bad Request`.
- A missing task returns `404 Not Found`.
- Invalid request bodies return FastAPI's `422 Unprocessable Entity` response.
- Data is stored in memory, so all tasks reset whenever the server restarts. This implementation is intended for the assignment and is not persistent storage.

## Project structure

```text
app/
├── main.py                    # FastAPI application and /api/v1 registration
├── api/v1/endpoints/          # Health and task route handlers
├── crud/crud_task.py          # In-memory task operations
└── schemas/task.py            # Pydantic request and response models
```
