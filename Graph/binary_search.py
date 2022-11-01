

def binary_search(array: list, target: int) -> int:
    low = 0
    end = len(array) - 1

    while low <= end:
        mid = (low + end) // 2
        # print("mid %d" % mid)
        value = array[mid]
        if value == target:
            return mid
        elif target > value:
            low = mid + 1
        else:
            end = mid - 1

    return -1

data = [ 2, 3, 6, 8]

print(binary_search(data, 8))

print(binary_search([], 4))
print(binary_search(data + [11], 3))
print(binary_search(data + [11], 11))
print(binary_search(data + [11], 12))
print(binary_search(data + [11], 2))
