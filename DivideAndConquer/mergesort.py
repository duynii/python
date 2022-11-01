
def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr

class Soln:

    @staticmethod
    def mergesort(nums: list[int]) -> list[int]:
        n = len(nums)
        if n == 1:
            return nums
        elif n == 2:
            return swap(nums, 0, 1) if nums[0] > nums[1] else nums

        mid = n // 2

        left = Soln.mergesort(nums[0:mid])
        right = Soln.mergesort(nums[mid:])

        def merge(left: list[int], right: list[int]) -> list[int]:
            print("merge %s and %s" % (left, right))
            i, j = 0, 0
            len_left, len_right = len(left), len(right)
            result = []
            while i < len_left and j < len_right:
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            if i < len_left-1:
                return result + left[i:]
            else:
                return result + right[j:]

        return merge(left, right)



data = [3, 6, 2, 3, 20, 7, 9, 2, 1]

print(Soln.mergesort(data))
