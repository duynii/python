#Leetcode 34. Find First and Last Position of Element in Sorted Array
# search the index or left most index if values are equal
# Return index of where value should be inserted: Hence target+1
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def binarySearch(tgt: int) -> int:
            l, r = 0, len(nums)

            while l < r:
                mid = (l + r) // 2

                if nums[mid] < tgt:
                    l = mid + 1
                else:
                    r = mid

            return l

        index = binarySearch(target)
        if index == len(nums) or nums[index] != target:
            return [-1, -1]
        else:
            return [index, binarySearch(target + 1) - 1]