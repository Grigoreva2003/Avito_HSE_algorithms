from dijkstra import WeightedGraph

graph = WeightedGraph()
graph.from_dict({
    'A': {'B': 1, 'C': 2},
    'B': {'A': 1, 'D': 3},
    'C': {'A': 2, 'D': 4},
    'D': {'B': 3, 'C': 4}
})
print(graph)
print(graph.dijkstra('A'))
