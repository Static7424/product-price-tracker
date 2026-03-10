from fastapi import APIRouter
from sqlalchemy import text

from src.database.database import DBSession


router = APIRouter(tags=["health"])


@router.get("/health", summary="Proves the process is alive and serving HTTP requests.")
def health():
    return {"status": "healthy"}


@router.get("/ready", summary="Checks for database connectivity.")
def ready(db: DBSession):
    db.execute(text("SELECT 1"))
    return {"status": "ready"}
