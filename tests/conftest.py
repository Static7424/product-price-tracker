import os
import pytest

from fastapi.testclient import TestClient

from src.main import app


os.environ["ENVIRONMENT"] = "test"
os.environ["POSTGRES_VERSION"] = "17"
os.environ["POSTGRES_PORT"] = "5432"
os.environ["POSTGRES_DATABASE"] = "pricetracker"
os.environ["POSTGRES_USER"] = "user"
os.environ["POSTGRES_PASSWORD"] = "password"
os.environ["POSTGRES_URL"] = "localhost:5432"


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
