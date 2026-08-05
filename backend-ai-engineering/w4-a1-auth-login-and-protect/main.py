from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Server running and connected to Supabase"}
