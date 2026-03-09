from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.config import settings
from src.database.database import Reflected
from src.routes import prices, products


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_engine(settings.database_url)
    Reflected.prepare(engine)
    app.state.session_factory = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )
    yield
    engine.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(prices.router)
app.include_router(products.router)
