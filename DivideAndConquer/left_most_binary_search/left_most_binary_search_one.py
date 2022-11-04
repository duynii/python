# Leetcode 35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def search(tgt: int) -> int:
            l, r = 0, len(nums)

            while l < r:
                m = (l + r) // 2

                if nums[m] < tgt:
                    l = m + 1
                else:
                    r = m
            return l

        return search(target)
