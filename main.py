from fastapi import FastAPI
from app.routes.books import books_router
from app.routes.frontend import frontend_router

app = FastAPI()
app.include_router(books_router)
app.include_router(frontend_router)
