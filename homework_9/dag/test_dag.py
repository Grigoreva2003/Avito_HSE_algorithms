import pytest
from directed_graph import DirectedGraph


def test_add_vertices_and_edges():
    g = DirectedGraph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")

    assert "A" in g.graph
    assert "B" in g.graph
    assert "C" in g.graph

    assert "B" in g.graph["A"]
    assert "C" in g.graph["B"]


def test_find_cycle_none():
    g = DirectedGraph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")

    assert g.find_cycle() is None


def test_find_cycle_detects():
    g = DirectedGraph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "A")  # cycle

    cycle = g.find_cycle()

    assert cycle is not None
    assert cycle[0] == cycle[-1]
    assert set(cycle[:-1]) == {"A", "B", "C"}


def test_topological_sort_simple():
    g = DirectedGraph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")

    order = g.topological_sort()
    assert order == ["A", "B", "C"]


def test_topological_sort_branching():
    g = DirectedGraph()
    g.add_edge("A", "C")
    g.add_edge("B", "C")

    order = g.topological_sort()

    # A and B can be in any order, but C must be last
    assert order[-1] == "C"
    assert set(order[:2]) == {"A", "B"}


def test_topological_sort_cycle_error():
    g = DirectedGraph()
    g.add_edge(1, 2)
    g.add_edge(2, 1)

    with pytest.raises(ValueError):
        g.topological_sort()
