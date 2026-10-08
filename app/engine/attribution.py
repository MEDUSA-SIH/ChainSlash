"""Phase 10 A-H + Phase 3 scores. Rank/conf/freezability never blended."""
import math

def freezability(i_token: float, r_vasp: float, t_hours: float, amt_usdt: float) -> float:
    return i_token * r_vasp * math.exp(-t_hours / 48) * min(1, amt_usdt / 1000)

def rank_candidates(candidates: list[dict]):
    # sort by freezability-adjusted proximity; show all three numbers
    return sorted(candidates, key=lambda c: (c.get("proximity", 999), -c.get("freezability", 0)))

def explain(path: dict) -> dict:
    return {"hops": path.get("hops"), "tier": path.get("tier"), "why_lower": "see evidence rows"}
