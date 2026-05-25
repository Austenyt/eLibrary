from pydantic import BaseModel
from typing import Optional


class BookFind(BaseModel):
    id: int


class BookCreate(BaseModel):
    name: str
    author: str
    genre: str
    year: int
    publisher: str
    rating: float
    award: str
    isbn: str
    description: str


class BookPatch(BaseModel):
    id: int
    name: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    year: Optional[int] = None
    publisher: Optional[str] = None
    rating: Optional[float] = None
    award: Optional[str] = None
    isbn: Optional[str] = None
    description: Optional[str] = None
