"""Phase 20-21 WORM + hash chain report->candidate->evidence->tx->api_response."""
import hashlib, json

def manifest_hash(record: dict) -> str:
    return hashlib.sha256(json.dumps(record, sort_keys=True).encode()).hexdigest()
