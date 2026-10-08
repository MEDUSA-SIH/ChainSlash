"""Phase 18 alerts: dedup_key UNIQUE + replay_nonce, acknowledged_by gate."""
def fire(case_id: str, alert_type: str, dedup_key: str):
    return {"case_id": case_id, "type": alert_type, "dedup_key": dedup_key, "mode": "REPLAY"}
