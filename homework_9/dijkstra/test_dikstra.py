import pytest
from dijkstra import WeightedGraph


# ----------------------------------------------------------
# БАЗОВЫЕ ТЕСТЫ
# ----------------------------------------------------------

def test_simple_graph():
    graph = WeightedGraph()
    graph.from_dict({
        'A': {'B': 1, 'C': 2},
        'B': {'A': 1, 'D': 3},
        'C': {'A': 2, 'D': 4},
        'D': {'B': 3, 'C': 4}
    })

    dist = graph.dijkstra('A')

    assert dist == {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 4
    }


# ----------------------------------------------------------
# ГРАФ ИЗ ОДНОЙ ВЕРШИНЫ
# ----------------------------------------------------------

def test_single_vertex():
    graph = WeightedGraph()
    graph.from_dict({'A': {}})

    dist = graph.dijkstra('A')

    assert dist == {'A': 0}


# ----------------------------------------------------------
# ОТСУТСТВУЮЩАЯ ВЕРШИНА
# ----------------------------------------------------------

def test_start_vertex_missing():
    graph = WeightedGraph()
    graph.from_dict({'A': {'B': 2}, 'B': {'A': 2}})

    with pytest.raises(KeyError):
        graph.dijkstra('Z')


# ----------------------------------------------------------
# ПЕТЛИ (A → A)
# ----------------------------------------------------------

def test_graph_with_self_loop():
    graph = WeightedGraph()
    graph.from_dict({
        'A': {'A': 10, 'B': 1},
        'B': {'A': 1}
    })

    dist = graph.dijkstra('A')

    # Дейкстра должна игнорировать петли — кратчайший путь A→A всегда 0
    assert dist['A'] == 0
    assert dist['B'] == 1


# ----------------------------------------------------------
# ТЕСТ С НЕСКОЛЬКИМИ ОДИНАКОВЫМИ КРАТЧАЙШИМИ ПУТЯМИ
# ----------------------------------------------------------

def test_multiple_shortest_paths():
    graph = WeightedGraph()
    graph.from_dict({
        'A': {'B': 2, 'C': 2},
        'B': {'D': 2},
        'C': {'D': 2},
        'D': {}
    })

    dist = graph.dijkstra('A')

    assert dist['D'] == 4
