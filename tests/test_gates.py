"""183 export + sign gates: acknowledged_by required, sign defaults unsigned."""
from fastapi.testclient import TestClient
from app.main import create_app

def test_export_gate():
    c = TestClient(create_app())
    r = c.get("/export/sahyog-packet.json", params={"case_id": "c1"})
    assert r.status_code == 403
    r2 = c.get("/export/sahyog-packet.json", params={"case_id": "c1", "acknowledged_by": "inv1"})
    assert r2.status_code == 200 and "request_id" in r2.json()

def test_trace_rejects_bad_address():
    c = TestClient(create_app())
    r = c.post("/trace", json={"address": "not-an-address"})
    assert r.status_code == 422
