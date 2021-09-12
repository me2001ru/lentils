# empty, add tests here.
import sqlite3
import pytest
import init_db


# def test_hello(client):
#     response = client.get("/hello")
#     assert response.data == b"Hello, World!"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]
