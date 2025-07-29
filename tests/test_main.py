from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def teste_stats_valid():
    response = client.post("/stats", json={"numbers": [1, 2, 2, 3]})
    assert response.status_code == 200
    data = response.json()
    assert data["mean"] == 2.0
    assert data["median"] == 2.0
    assert data["mode"] == 2

def test_stats_no_unique_mode():
    response = client.post("/stats", json={"numbers": [1, 2, 3]})
    assert response.status_code == 400
    assert response.json()["detail"] == "No unique mode found"