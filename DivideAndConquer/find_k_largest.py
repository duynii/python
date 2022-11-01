
def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

class Soln:

    # Target index = len(nums) - k
    @staticmethod
    def findKthLargest(nums: list[int], k: int) -> int:

        targetIndex = len(nums) - k

        def quickselect(left: int, right: int):
            pivot, p = nums[right], left

            if left > right:
                return -1

            for index in range(left, right):
                if nums[index] > pivot:
                    swap(nums, index, p)
                    p += 1

            swap(nums, p, right)

            if p > targetIndex:
                return quickselect(left, p-1)
            elif p < targetIndex:
                return quickselect(p+1, right)
            else:
                return nums[p]

        return quickselect(0, len(nums)-1)


data = [5, 4, 3, 2, 1, 7, 6, 8, 9]

print(Soln.findKthLargest(data, 2))
print(Soln.findKthLargest(data, 8))
print(Soln.findKthLargest(data, 11))
