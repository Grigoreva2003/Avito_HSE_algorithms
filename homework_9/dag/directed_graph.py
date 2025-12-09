class DirectedGraph:
    def __init__(self):
        self.graph = {}  # adjacency list: node -> set of neighbors

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = set()

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].add(v)

    def find_cycle(self):
        """Returns any cycle found; otherwise None."""
        visited = set()
        stack = set()
        parent = {}

        def dfs(v):
            visited.add(v)
            stack.add(v)
            for neigh in self.graph[v]:
                if neigh not in visited:
                    parent[neigh] = v
                    if dfs(neigh):
                        return True
                elif neigh in stack:
                    # cycle detected — reconstruct
                    cycle = [neigh]
                    cur = v
                    while cur != neigh:
                        cycle.append(cur)
                        cur = parent[cur]
                    cycle.append(neigh)
                    cycle.reverse()
                    self._cycle = cycle
                    return True
            stack.remove(v)
            return False

        for v in self.graph:
            if v not in visited:
                parent[v] = None
                if dfs(v):
                    return self._cycle

        return None

    def topological_sort(self):
        """Kahn's algorithm. Returns list or raises ValueError if cycle exists."""
        # compute indegree
        indegree = {v: 0 for v in self.graph}
        for u in self.graph:
            for v in self.graph[u]:
                indegree[v] += 1

        queue = [v for v in indegree if indegree[v] == 0]
        order = []

        while queue:
            v = queue.pop()
            order.append(v)
            for neigh in self.graph[v]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)

        if len(order) != len(self.graph):
            raise ValueError("Topological sort impossible — graph has a cycle.")

        return order

    def analyse(self):
        cycle = self.find_cycle()

        if cycle is None:
            return "sort", self.topological_sort()
        return "cycle", cycle
