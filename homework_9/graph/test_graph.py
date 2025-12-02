# import pytest
# from graph import Graph


# graph = Graph()
# graph.from_dict({
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'D'],
#     'D': ['B', 'C'],
#     'E': []
# })
# print(graph)
# print(graph.get_components())

import pytest

from graph import Graph


def graph_dict(value):
    def decorator(func):
        return pytest.mark.parametrize("graph_dict", [value])(func)
    return decorator


def answer_components(value):
    def decorator(func):
        return pytest.mark.parametrize("answer_components", [value])(func)
    return decorator


def _normalize(components):
    return sorted(sorted(component) for component in components)


@graph_dict({})
@answer_components([])
def test_empty_graph(graph_dict, answer_components):
    graph = Graph()
    graph.from_dict(graph_dict)
    assert graph.get_components() == answer_components


@graph_dict({'A': []})
@answer_components([['A']])
def test__single_vertex(graph_dict, answer_components):
    graph = Graph()
    graph.from_dict(graph_dict)
    assert _normalize(graph.get_components()) == _normalize(answer_components)


@graph_dict({'A': [], 'B': []})
@answer_components([['A'], ['B']])
def test_mult_single_vertex(graph_dict, answer_components):
    graph = Graph()
    graph.from_dict(graph_dict)
    assert _normalize(graph.get_components()) == _normalize(answer_components)


@graph_dict({
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': ['E'],
    'E': ['D'],
    'F': [],
})
@answer_components([['A', 'B', 'C'], ['D', 'E'], ['F']])
def test_multiple_components_with_isolated_vertex(graph_dict, answer_components):
    graph = Graph()
    graph.from_dict(graph_dict)
    assert _normalize(graph.get_components()) == _normalize(answer_components)


@graph_dict({
    'X': ['Y'],
    'Y': ['X', 'Z'],
    'Z': ['Y'],
})
@answer_components([['X', 'Y', 'Z']])
def test_fully_connected_graph(graph_dict, answer_components):
    graph = Graph()
    graph.from_dict(graph_dict)
    assert _normalize(graph.get_components()) == _normalize(answer_components)
