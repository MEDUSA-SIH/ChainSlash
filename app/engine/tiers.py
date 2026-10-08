"""Phase 5 tiers: 1 verified, 2 high, 3 probable, 4 candidate. T3/4 never 'belongs to X'."""
def label_text(tier: int, vasp: str) -> str:
    if tier <= 2:
        return f"associated with {vasp} (tier {tier})"
    return f"candidate pattern consistent with {vasp}-like deposit (tier {tier}, unconfirmed)"
