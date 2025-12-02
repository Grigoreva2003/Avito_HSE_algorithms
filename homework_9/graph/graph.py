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

    def __repr__(self):
        output_list = []
        for parent, children in self.graph.items():
            output_list.append(f"{parent}: {children}")
        return "\n".join(output_list)

    def print_graph(self):
        for parent, children in self.graph.items():
            print

    def get_components(self):
        components = []
        visited = set()
        for vertex in self.graph:
            if vertex not in visited:
                component = []
                self.dfs(vertex, component, visited)
                components.append(component)
        return components

    def dfs(self, vertex, component, visited):
        visited.add(vertex)
        component.append(vertex)
        for child in self.graph[vertex]:
            if child not in visited:
                self.dfs(child, component, visited)

    def get_components(self):
        components = []
        visited = set()
        for vertex in self.graph:
            if vertex not in visited:
                component = []
                self.dfs(vertex, component, visited)
                components.append(component)
        return components

    def dfs(self, vertex, component, visited):
        visited.add(vertex)
        component.append(vertex)
        for child in self.graph[vertex]:
            if child not in visited:
                self.dfs(child, component, visited)
