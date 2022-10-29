import heapq


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Returns tuple of strength and index
        # Note with would be better to  use come kind of binary chop to count instead
        def countSoldiers(row: list, index: int) -> int:
            return (functools.reduce(lambda a, b: a + b, row), index)

        rows = list(
            map(countSoldiers, mat, range(len(mat)))
        )
        # print(rows)

        heapq.heapify(rows)
        # rows.sort()
        # print(rows)

        # return rows[:k]
        indices = []
        for _ in range(k):
            _, index = heapq.heappop(rows)
            indices.append(index)

        return indices