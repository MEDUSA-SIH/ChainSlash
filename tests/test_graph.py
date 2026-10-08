"""NetworkX unit-test helper only, never persisted (spec lock)."""
import networkx as nx
def test_graph_helper():
    g = nx.DiGraph()
    g.add_edge("a", "b")
    assert g.has_edge("a", "b")
