from contextlib import asynccontextmanager
from importlib.metadata import version

from fastapi import FastAPI
from fastapi_pagination import add_pagination
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.config import settings
from src.database.database import Reflected
from src.routes import health, prices, products


@asynccontextmanager
async def lifespan(app: FastAPI):
    database_url = f"postgresql+psycopg://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_url}/{settings.postgres_database}"
    engine = create_engine(database_url)
    Reflected.prepare(engine)
    app.state.session_factory = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )
    yield
    engine.dispose()


app = FastAPI(
    title="Product Price Tracker",
    summary="Track grocery prices over time from supermarkets.",
    version=version("product-price-tracker"),
    lifespan=lifespan,
)

app.include_router(health.router)
app.include_router(prices.router)
app.include_router(products.router)

add_pagination(app)
