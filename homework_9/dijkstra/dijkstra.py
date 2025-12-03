# Реализовать алгоритм Дейкстры для взвешенного графа.
# Тесты.
import heapq

class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].setdefault(vertex2, 0)
            self.graph[vertex1][vertex2] = weight
            self.graph[vertex2].setdefault(vertex1, 0)
            self.graph[vertex2][vertex1] = weight

    def from_dict(self, dict_):
        for vertex1, vertexes in dict_.items():
            for vertex2, weight in vertexes.items():
                self.add_vertex(vertex1)
                self.add_vertex(vertex2)
                self.add_edge(vertex1, vertex2, weight)

    def __repr__(self):
        output_list = []
        for vertex1, vertexes in self.graph.items():
            for vertex2, weights in vertexes.items():
                output_list.append(f"{vertex1} - {vertex2}: {weights}")
        return "\n".join(output_list)

    def dijkstra(self, start_vertex):
        distances = {vertex: float('inf') for vertex in self.graph.keys()}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.graph[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
