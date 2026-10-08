"""Phase 7 BI + Phase 18: mempool watch defaults to REPLAY_MODE."""
MODE = "REPLAY"  # LIVE | POLL | REPLAY, badge always visible

def watch(addresses: list[str]):
    return {"mode": MODE, "watching": addresses}
