from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, Float


class Book(Base):

    __tablename__ = 'book'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150))
    author: Mapped[str] = mapped_column(String(50))
    genre: Mapped[str] = mapped_column(String(50))
    year: Mapped[int] = mapped_column(Integer)
    publisher: Mapped[str] = mapped_column(String(50))
    rating: Mapped[float] = mapped_column(Float)
    award: Mapped[str | None] = mapped_column(String(50))
    isbn: Mapped[str] = mapped_column(String(17))
    description: Mapped[str] = mapped_column(String(1000))
