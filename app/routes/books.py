from fastapi import APIRouter, Depends
from app.db.database import get_session
from app.schemas.book import BookFind, BookCreate, BookPatch
from app.services.book_service import book_service

books_router = APIRouter(tags=["books"])


@books_router.get('/books')
def books(session=Depends(get_session)):
    return book_service.get_all(session)


@books_router.post('/books/{id}')
def find(payload: BookFind, session=Depends(get_session)):
    try:
        return book_service.find(payload.id, session)
    except ValueError:
        return {"message": "Книги с таким id не существует"}


@books_router.post('/books')
def create(payload: BookCreate, session=Depends(get_session)):
    book_service.create(payload, session)
    return {"message": "Книга успешно добавлена!"}


@books_router.patch('/books/{id}')
def patch(payload: BookPatch, session=Depends(get_session)):
    book_service.patch(payload, session)
    return {'message': 'ok'}


@books_router.delete('/books/{id}')
def delete(payload: BookFind, session=Depends(get_session)):
    try:
        book_service.delete(payload.id, session)
    except ValueError:
        return {"message": "Книги с таким id не существует"}
