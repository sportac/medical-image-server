import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.database import Base
from app.main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_user(test_db):
    user_data = {
        "email": "sergi@example.com",
        "password": "mypassword",
        "username": "sergi",
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json()["email"] == user_data["email"]
    assert response.json()["username"] == user_data["username"]
    assert "id" in response.json()


def test_create_user_with_existing_email(test_db):
    user_data = {
        "email": "sergi@example.com",
        "password": "mypassword",
        "username": "sergi",
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 400
    assert "Email already registered" in response.json()["detail"]


def test_read_users(test_db):
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_read_user(test_db):
    user_data = {
        "email": "dailabarret@example.com",
        "password": "mypassword",
        "username": "dailabarret",
    }
    response = client.post("/users/", json=user_data)
    user_id = response.json()["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["email"] == user_data["email"]
    assert response.json()["username"] == user_data["username"]
    assert response.json()["id"] == user_id


def test_read_user_not_found(test_db):
    response = client.get("/users/9999")
    assert response.status_code == 404
    assert "User not found" in response.json()["detail"]
