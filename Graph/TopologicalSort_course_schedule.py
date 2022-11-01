# Leetcode 210. Course Schedule II
# DFS, cyclic detection, recursion, topological search
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = {c: [] for c in range(numCourses)}
        # print(adj)

        for pre in prerequisites:
            adj[pre[0]].append(pre[1])

        visited, path = set(), set()
        result = []

        # Post order dfs
        # False for cyclic graph found
        def dfs(node: int) -> bool:
            if node in path:
                return False  # cyclic

            if node in visited:
                return True

            path.add(node)
            for pre in adj[node]:

                if dfs(pre) == False:
                    return False

            visited.add(node)
            path.remove(node)
            result.append(node)
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []

        return result

