"""Phase 7 + 23 (183): ingest NCRP CSV, trace, SAHYOG packet export (replay nonce, human gate)."""
from fastapi import APIRouter, HTTPException, Request
import re
import uuid

router = APIRouter()

ADDR_RE = re.compile(r"^(0x[0-9a-fA-F]{40}|T[A-Za-z1-9]{33}|bc1[0-9a-z]{25,60}|[13][a-km-zA-HJ-NP-Z1-9]{25,34}|[0-9a-zA-Z]{32,44})$")

def _version(req: Request) -> str:
    s = getattr(req.app.state, "settings", None)
    return getattr(s, "APP_VERSION", "0.1.0") if s else "0.1.0"

def _demo(req: Request) -> bool:
    s = getattr(req.app.state, "settings", None)
    return bool(getattr(s, "DEMO_MODE", True)) if s else True

@router.get("/health")
def health(req: Request):
    return {"status": "ok", "demo_mode": _demo(req), "version": _version(req)}

@router.get("/ready")
def ready(req: Request):
    # liveness ok; readiness checks DB/redis/neo4j when wired (S3). Stub returns degraded until then.
    return {"status": "degraded", "checks": {"postgres": "pending", "redis": "pending", "neo4j": "pending"}, "demo_mode": _demo(req)}

@router.post("/ingest/ncrp-csv")
def ingest_ncrp_csv(payload: dict):
    request_id = str(uuid.uuid4())
    return {"request_id": request_id, "status": "queued"}

@router.post("/trace")
def trace(payload: dict):
    addr = str(payload.get("address", ""))
    if not ADDR_RE.match(addr):
        raise HTTPException(status_code=422, detail="invalid address format")
    # TODO Phase 10 A-H: BFS -> Dijkstra -> freezability -> abstain
    return {"candidates": [], "mode": "REPLAY", "band": "abstain"}

@router.get("/export/sahyog-packet.json")
def export_packet(case_id: str, acknowledged_by: str | None = None):
    if not acknowledged_by:
        raise HTTPException(status_code=403, detail="acknowledged_by required before export")
    return {"case_id": case_id, "packet": {}, "request_id": str(uuid.uuid4())}

@router.post("/reports/{report_id}/sign")
def sign_report(report_id: str, payload: dict):
    # TODO Phase 20 dual Ed25519 sign, reviewer+MFA only
    return {"report_id": report_id, "signed": False}
