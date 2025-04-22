from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str

class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    id: int

    class Config:
        from_attributes = True