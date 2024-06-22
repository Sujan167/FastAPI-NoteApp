# app/main.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from pydantic import BaseModel
from schema import NoteCreate, NoteInDB, NoteUpdate  # Import Pydantic models

from models import Note

# Create tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Pydantic model for request body validation
class NoteCreate(BaseModel):
    title: str
    content: str

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/note/")
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    new_note = Note(title=note.title, content=note.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


@app.get("/note/{note_id}", response_model=NoteInDB)
def read_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.get("/notes/", response_model=list[NoteInDB])
def read_notes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Note).offset(skip).limit(limit).all()


@app.put("/note/{note_id}", response_model=NoteInDB)
def update_note(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    db_note.title = note.title
    db_note.content = note.content
    db.commit()
    db.refresh(db_note)
    return db_note


@app.delete("/note/{note_id}", response_model=NoteInDB)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return note