"""183 freezability + tiers (spec P3/P5)."""
from app.engine.attribution import freezability
from app.engine.tiers import label_text

def test_freezability_formula():
    s = freezability(1.0, 0.90, 0.0, 1000.0)
    assert abs(s - 0.90) < 1e-6

def test_tier_hedging():
    assert "belongs" not in label_text(4, "Demo").lower() or "unconfirmed" in label_text(4, "Demo").lower()
