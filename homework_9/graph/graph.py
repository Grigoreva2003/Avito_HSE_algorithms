# Graph
# 
# Дан неориентированный граф.
# Необходимо, найти все компоненты связности графа и вывести их. 
# Подразумевается, что граф подается на вход в виде списка смежности (словарь со списками ребер). 
# Здесь очень важны краевые случаи. Тесты должны их покрыть. 

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
    
    def from_dict(self, dict_):
        for parent, children in dict_.items():
            self.add_vertex(parent)
            for child in children:
                self.add_edge(parent, child)

    def print_graph(self):
        for parent, children in self.graph.items():
            print(f"{parent}: {children}")

graph = Graph()
graph.from_dict({
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
})
graph.print_graph()