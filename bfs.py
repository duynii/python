from collections import defaultdict, deque

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def __bfs(self, v, visited, queue):
        if v in visited:
            return

        while len(queue) > 0:
            node = queue.popleft()
            print(node)
            visited.add(node)

            for v in self.graph[node]:
                if v not in visited:
                    queue.append(v)


    def BFS(self, root):
        visited = set()
        process_queue =  deque()
        process_queue.append(root)

        self.__bfs(root, visited, process_queue)


# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(2)