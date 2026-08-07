# Week 4 Assignment 1: Supabase Authentication Practice

This repository is mainly a practice project for learning and implementing authentication flows with Supabase in a FastAPI application. It focuses on basic auth concepts such as sign up, login, and protecting routes with a bearer token.

Dependencies are managed with [`uv`](https://docs.astral.sh/uv/).

## Stack and prerequisites

- Python `>= 3.12`
- FastAPI with the standard dependencies
- Uvicorn, through the FastAPI CLI
- `uv`
- Supabase Python client

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

## Available endpoints

### Health

- `GET /health` — returns service health and uptime information

### Public

- `GET /public/info` — returns a public message

### Protected

- `GET /protected/profile` — requires an `Authorization: Bearer <token>` header

### Authentication (Supabase)

- `POST /auth/signup` — creates a new user in Supabase Auth
- `POST /auth/login` — signs in a user and returns access/refresh tokens
