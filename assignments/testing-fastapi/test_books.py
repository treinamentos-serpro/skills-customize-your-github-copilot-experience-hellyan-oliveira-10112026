import pytest
from fastapi.testclient import TestClient

from main import app, reset_books

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_book_data():
    reset_books()
    yield
    reset_books()


def test_list_books_returns_all_books():
    response = client.get("/books")

    assert response.status_code == 200
    assert len(response.json()) == 2