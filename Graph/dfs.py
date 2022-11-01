from collections import defaultdict

memoize_map = {}
def memoize(func):
    def inner(self, v, visited):
        # v = args[1]
        if v in memoize_map:
            print("Return from map")
            return memoize_map[v]
        else:
            result = func(self, v, visited)
            memoize_map[v] = result
            return result
    return inner

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    @memoize
    def _dfs(self, v, visited):

        if v in visited:
            return

        print(v)
        visited.add(v)

        for to_node in self.graph[v]:
            if to_node not in visited:
                self._dfs(to_node, visited)

    def DFS(self, v):
        visited = set()

        self._dfs(v, visited)

    # Must start from each node
    def DFS_disconnected_graph(self):
        visited = set()

        for v in self.graph.keys():
            if v not in visited:
                self._dfs(v, visited)


# Create a graph given
# in the above diagram
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is DFS from (starting from vertex 2)")
    # Function call
    g.DFS_disconnected_graph()