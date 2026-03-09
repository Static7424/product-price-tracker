import os
import pytest

from fastapi.testclient import TestClient

from src.main import app


os.environ["ENVIRONMENT"] = "test"


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
