from sqlalchemy import select, update

from app.models.book import Book


class BookService:

    def get_all(self, session):
        return session.scalars(select(Book)).all()

    def create(self, name, author, genre, year, publisher, rating, award, isbn, description, session):
        book = Book(
            name=name,
            author=author,
            genre=genre,
            year=year,
            publisher=publisher,
            rating=rating,
            award=award,
            isbn=isbn,
            description=description,
        )
        session.add(book)
        session.commit()
        session.refresh(book)
        return book

    def find(self, id, session):
        book = session.get(Book, id)
        if book is None:
            return ValueError("Книга не найдена")
        return book

    def patch(self, payload, session):
        session.execute(update(Book).where(Book.id == payload.id).values(**payload))
        session.commit()

    def delete(self, id, session):
        book = self.find(id, session)
        session.delete(book)
        session.commit()


book_service = BookService()
