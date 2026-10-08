"""Phase 7 + 23: ingest NCRP CSV, trace, SAHYOG packet export (replay nonce, human gate)."""
from fastapi import APIRouter
import uuid

router = APIRouter()

@router.post("/ingest/ncrp-csv")
def ingest_ncrp_csv(payload: dict):
    request_id = str(uuid.uuid4())
    return {"request_id": request_id, "status": "queued"}

@router.post("/trace")
def trace(payload: dict):
    # TODO Phase 10 A-H: BFS -> Dijkstra -> freezability -> abstain
    return {"candidates": [], "mode": "REPLAY"}

@router.get("/export/sahyog-packet.json")
def export_packet(case_id: str):
    return {"case_id": case_id, "packet": {}, "note": "acknowledged_by required before export"}

@router.post("/reports/{report_id}/sign")
def sign_report(report_id: str, payload: dict):
    # TODO Phase 20 dual Ed25519 sign, reviewer+MFA only
    return {"report_id": report_id, "signed": False}
