"""183 health contract: /health liveness + /ready degraded stub."""
from fastapi.testclient import TestClient
from app.main import create_app

def test_health():
    c = TestClient(create_app())
    r = c.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert "demo_mode" in body and "version" in body

def test_ready():
    c = TestClient(create_app())
    r = c.get("/ready")
    assert r.status_code == 200
    assert r.json()["status"] in ("ok", "degraded")
