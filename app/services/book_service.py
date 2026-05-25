from sqlalchemy import select, update

from app.models.book import Book


class BookService:

    def get_all(self, session):
        return session.scalars(select(Book)).all()

    def create(self, payload, session):
        book = Book(**payload.model_dump())
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
        session.execute(
            update(Book).where(Book.id == payload.id).values(**payload.model_dump(exclude={'id'}, exclude_unset=True))
        )
        session.commit()

    def delete(self, id, session):
        book = self.find(id, session)
        session.delete(book)
        session.commit()


book_service = BookService()
