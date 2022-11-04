# 47. Permutations II
from collections import Counter

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        hmap = Counter(nums)
        res = []

        def dfs(cur: list, hmap: Counter):
            if len(cur) == len(nums):
                res.append([*cur])
                return

            for num, freq in hmap.items():
                if freq == 0: continue

                hmap[num] -= 1
                cur.append(num)
                dfs(cur, hmap)
                cur.pop()
                hmap[num] += 1

        dfs([], hmap)

        return res