from fastapi import APIRouter
from fastapi.responses import FileResponse
from app import config

frontend_router = APIRouter()


@frontend_router.get("/")
def index():
    pass
    # return FileResponse(config.frontend_dir / "index.html")
