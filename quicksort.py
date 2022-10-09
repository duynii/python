
class Solution:
    @staticmethod
    def quicksort(arr) -> list:
        low = 0
        end = len(arr) - 1

        def _sort(arr, left, right):
            if left >= right:
                return

            pivot = arr[ (left+right) // 2 ]
            index = Solution._partition(arr, left, right, pivot)
            # print("index %d" % index)
            _sort(arr, left, index-1)
            _sort(arr, index, right)

        _sort(arr, 0, end)

    @staticmethod
    def _swap(arr, a, b):
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

    @staticmethod
    def _partition(arr, left, right, pivot):
        # print("left right: %d %d %d %s" %(left, right, pivot, arr))
        while left <= right:
            while arr[left] < pivot:
                # print("left %d" % left)
                left += 1
            while arr[right] > pivot:
                # print("right %d" % right)
                right -= 1

            if left <= right:
                Solution._swap(arr, left, right)
                left += 1
                right -= 1

        return left


data = [5, 2, 7, 9, 10, 4]

Solution.quicksort(data)
print(data)