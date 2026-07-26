# Week 2 Assignment — FastAPI CRUD API (Python Track)

This directory contains the Python / FastAPI implementation of the Week 2 CRUD API assignment, managed using **`uv`** for fast dependency management.

---

## 🛠️ Stack & Prerequisites

- **Python:** `>= 3.12`
- **Framework:** FastAPI
- **Package/Env Manager:** [`uv`](https://github.com/astral-sh/uv)
- **ASGI Server:** Uvicorn

---

## 🚀 Installation & Running with `uv`

1. **Navigate to this folder:**
   ```bash
   cd backend-ai-engineering/w2-a1-build-your-first-CRUD-API/python-track
   ```
2. **Create a virtual environment:**
   ```bash
   uv venv
   ```
3. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   ```
4. **Install dependencies:**
   ```bash
   uv sync
   ```
5. **Start the development server:**
   ```bash
   uv run fastapi dev
   ```

## 📝 Notes

FastAPI generates automated OpenAPI documentation out of the box:

Swagger UI: http://127.0.0.1:8000/docs  
ReDoc: http://127.0.0.1:8000/redoc

---

## 📡 API Endpoints

### Summary

| Method | Endpoint | Description                                             |
| ------ | -------- | ------------------------------------------------------- |
| GET    | /        | Returns metadata about the API.                         |
| GET    | /health  | Returns a JSON object indicating the server is healthy. |
