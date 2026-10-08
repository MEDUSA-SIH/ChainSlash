"""183 smoke on eval/cases.json 6 cases (spec P25/P26). Pass 5/6 + 0 High false is acceptance; here assert shape."""
import json
from pathlib import Path

def test_cases_shape():
    data = json.loads(Path("eval/cases.json").read_text())
    ids = {c["id"] for c in data["cases"]}
    assert {"direct", "one-hop", "multi-hop", "mixer", "bridge", "false-hub"} <= ids
    assert any(c["expected_band"] == "abstain" for c in data["cases"])
