"""Phase 18 mempool REPLAY_MODE canned 500-line log at 5tx/s."""
MODE = "REPLAY"
def replay(log_path: str = "eval/canned/canned_mempool.log"):
    return {"mode": MODE, "log": log_path}
