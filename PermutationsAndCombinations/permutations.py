# 46. Permutations
# https://leetcode.com/discuss/study-guide/1405817/Backtracking-algorithm-%2B-problems-to-practice
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def dfs(cur: list, used: set):
            if len(cur) == len(nums):
                res.append([x for x in cur])
                return

            for n in nums:
                if n not in used:
                    cur.append(n)
                    used.add(n)
                    dfs(cur, used)
                    cur.pop()
                    used.remove(n)

        dfs([], used)

        return res