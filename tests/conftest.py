import pytest
from fastapi.testclient import TestClient

from app import app, database


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def clear_database():
    database.clear()
    yield
    database.clear()
