from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_dicom_patient():
    response = client.get("/dicom/patient")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert isinstance(data["name"], str)
