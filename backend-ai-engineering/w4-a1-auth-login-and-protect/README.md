# Week 4 Assignment 1: Authentication and login

This directory contains the Python/FastAPI implementation of the Week 4 assignment. Dependencies are managed with [`uv`](https://docs.astral.sh/uv/).

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
