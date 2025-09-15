from db import Database
import pytest

@pytest.fixture
def db():
    """Creates a fresh instance of Database class and cleans up after the test."""
    database = Database()
    yield database # Provides the fixture instance
    database.data.clear() # Cleanup step (not needed for in-memory, but useful for real DBs)

def test_add_user(db):
    db.add_user(1, "Alice")
    assert db.get_user(1) == "Alice"

def test_add_duplicate_user(db):
    db.add_user(1, "Alice")
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user(1, "Bob")

def test_delete_user(db):
    db.add_user(2, "Bob")
    db.delete_user(2)
    assert db.get_user(2) is None