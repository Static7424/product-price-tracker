import os
import pytest

from fastapi.testclient import TestClient

from src.database.database import Reflected
from src.main import app


os.environ["ENVIRONMENT"] = "test"


@pytest.fixture
def client():
    with TestClient(app) as client:
        session = app.state.session_factory()
        try:
            for table in reversed(Reflected.metadata.sorted_tables):
                session.execute(table.delete())
            session.commit()
        finally:
            session.close()
        yield client
