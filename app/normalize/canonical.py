"""Phase 9 canonical: 7 core + asset/fee/status + provenance + chain_metadata (never flattened)."""
CORE = ["chain", "block_height", "timestamp", "tx_hash", "sender", "recipient", "amount"]

def to_canonical(raw: dict) -> dict:
    return {k: raw.get(k) for k in CORE} | {
        "asset": raw.get("asset"),
        "provenance": raw.get("provenance", {}),
        "chain_specific_metadata": raw.get("chain_specific_metadata", {}),
    }
