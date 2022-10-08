from collections import defaultdict

memoize_map = {}
def memoize(func):
    def inner(self, v, visited, depth):
        # v = args[1]
        if v in memoize_map:
            print("Return from map")
            return memoize_map[v]
        else:
            result = func(self, v, visited, depth)
            memoize_map[v] = result
            return result
    return inner

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # @memoize
    def _dfs(self, v, visited, depth):
        print(v)
        visited.add(v)

        if len(self.graph[v]) == 0:
            return depth + 1

        max_depth = depth + 1
        for to_node in self.graph[v]:
            if to_node not in visited:
                new_depth = self._dfs(to_node, visited, depth+1)
                print("Node %d new depth is %d" % (to_node, new_depth))
                max_depth = max(new_depth, max_depth)

        return max_depth

    def DFS(self, v):
        visited = set()

        self._dfs(v, visited)

    # Must start from each node
    def DFS_disconnected_graph(self):
        visited = set()

        max_depth = 0
        for v in self.graph.keys():
            if v not in visited:
                depth = self._dfs(v, visited, max_depth)
                max_depth = max(depth, max_depth)

        print("Max depth is %d" % max_depth)
        for key, value in memoize_map.items():
            print("Node %d depth is %d" % (key, value))



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