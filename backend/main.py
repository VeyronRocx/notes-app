import os
import json
from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel

# Define data models
class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class Note(NoteBase):
    id: int
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True

# Initialize FastAPI app
app = FastAPI(title="Notes API")

# Notes storage
class NoteStore:
    def __init__(self):
        self.notes = []
        self.file_path = "notes.json"
        self.load_notes()

    def load_notes(self):
        """Load notes from JSON file if it exists."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as file:
                    self.notes = json.load(file)
            except json.JSONDecodeError:
                self.notes = []
        else:
            self.notes = []

    def save_notes(self):
        """Save notes to JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump(self.notes, file, indent=4)

# Create note store instance
note_store = NoteStore()

# Routes
@app.get("/")
async def root():
    return {"message": "Welcome to Notes API"}

@app.get("/notes", response_model=List[Note])
async def get_all_notes():
    return note_store.notes

@app.get("/notes/{note_id}", response_model=Note)
async def get_note(note_id: int):
    for note in note_store.notes:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail=f"Note with ID {note_id} not found")

@app.post("/notes", response_model=Note)
async def create_note(note: NoteCreate):
    note_id = len(note_store.notes) + 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_note = {
        "id": note_id,
        "title": note.title,
        "content": note.content,
        "created_at": timestamp,
        "updated_at": timestamp
    }
    
    note_store.notes.append(new_note)
    note_store.save_notes()
    return new_note

@app.put("/notes/{note_id}", response_model=Note)
async def update_note(note_id: int, note_update: NoteUpdate):
    for note in note_store.notes:
        if note["id"] == note_id:
            if note_update.title is not None:
                note["title"] = note_update.title
            if note_update.content is not None:
                note["content"] = note_update.content
            note["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            note_store.save_notes()
            return note
    raise HTTPException(status_code=404, detail=f"Note with ID {note_id} not found")

@app.delete("/notes/{note_id}")
async def delete_note(note_id: int):
    for i, note in enumerate(note_store.notes):
        if note["id"] == note_id:
            note_store.notes.pop(i)
            note_store.save_notes()
            return {"message": f"Note with ID {note_id} deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Note with ID {note_id} not found")

@app.get("/notes/search/{query}")
async def search_notes(query: str):
    query = query.lower()
    results = []
    
    for note in note_store.notes:
        if query in note["title"].lower() or query in note["content"].lower():
            results.append(note)
    
    return results

# Run with: uvicorn main:app --reload
