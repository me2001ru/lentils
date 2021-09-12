# empty, add tests here.
import sqlite3
import pytest


# def test_hello(client):
#     response = client.get("/hello")
#     assert response.data == b"Hello, World!"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]


@pytest.fixture
def session():
    connection = sqlite3.connect(':memory:')
    db_session = connection.cursor()
    yield db_session
    connection.close()


@pytest.fixture
def cursor(conn):
    cursor = conn.cursor()
    yield cursor
    conn.rollback()
