from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

# Create FastAPI app
app = FastAPI()

# Serve static files (React build output)
frontend_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'frontend/build')
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/")
def read_index():
    # Serve the index.html from React build
    with open(os.path.join(frontend_path, "index.html")) as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.get("/api/notes")
def get_notes():
    # Replace with your database logic
    return {"notes": ["Note 1", "Note 2"]}

@app.post("/api/notes")
def create_note(note: str):
    # Replace with database logic to save the note
    return {"message": "Note created", "note": note}

