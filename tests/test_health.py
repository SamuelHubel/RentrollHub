from fastapi.testclient import TestClient

from hub.api import app


def test_health_pings_database():
    resp = TestClient(app).get("/api/v1/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok", "database": "ok"}
