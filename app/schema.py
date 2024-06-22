from pydantic import BaseModel

# Pydantic model for request body validation
class NoteBase(BaseModel):
    title: str
    content: str


class NoteCreate(NoteBase):
    pass


class NoteUpdate(NoteBase):
    pass


class NoteInDB(NoteBase):
    id: int

    class Config:
        orm_mode = True
