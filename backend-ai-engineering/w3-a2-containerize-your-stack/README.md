# Week 3 Assignment: containerize your stack

This directory contains the Python/FastAPI implementation of the Week 3 assignment2. Dependencies are managed with [`uv`](https://docs.astral.sh/uv/).

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

## Architectural Proof: Swapping Databases (SQLite → PostgreSQL)

The core strength of this project's architecture is the **strict separation of concerns**:

- **Endpoints (`app/api/v1/endpoints/`)**: Handle HTTP routing, status codes, and request/response serialization.
- **Schemas (`app/schemas/`)**: Handle Pydantic data validation and contract enforcement.
- **Repository / CRUD (`app/crud/`)**: Encapsulates database-specific SQL logic.

### Database Migration

During Week 3, the backend repository was seamlessly migrated from an embedded **SQLite** database to a containerized **PostgreSQL** database running inside **Docker Compose**.

**Zero lines of code inside the routes, controllers, or Pydantic schemas needed to change.** Only the connection helper (`app/db/database.py`) and the CRUD SQL operations (`app/crud/crud_task.py`) were updated to handle PostgreSQL syntax (`%s` placeholders and `RETURNING` clauses).

---

## Stack Setup with Docker Compose

The complete infrastructure stack runs using **Docker Compose**, orchestrating three isolated services:

1. **`app`**: FastAPI web application running via Uvicorn.
2. **`db`**: PostgreSQL 15 database instance backed by a named Docker volume (`postgres_data`).
3. **`redis`**: Redis 7 cache server for background/caching tasks.

### Environment Configuration

Database credentials and connection parameters are loaded via environment variables defined in a `.env` file (gitignored for security). A template is provided in `.env.example`:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=taskdb
POSTGRES_HOST=db
POSTGRES_PORT=5432
DATABASE_URL=postgresql://postgres:postgres@db:5432/taskdb
REDIS_HOST=redis
REDIS_PORT=6379
```
