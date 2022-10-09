

class MinHeap:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def _leftChild(self, index: int) -> int:
       return 2*index + 1

    def _rightChild(self, index: int) -> int:
        return 2 * index + 2

    def _parentIndex(self, index: int) -> int:
        return (index-1) // 2

    def _hasLeftChild(self, index: int) -> int:
        return self._leftChild(index) < self.size

    def _hasRightChild(self, index: int) -> int:
        return self._rightChild(index) < self.size

    def _hasParent(self, index: int) -> int:
        return self._parentIndex(index) >= 0

    def _leftItem(self, index):
        return self.data[self._leftChild(index)]

    def _rightItem(self, index):
        return self.data[self._rightChild(index)]

    def _parentItem(self, index) -> int:
        return self.data[self._parentIndex(index)]

    def _swap(self, indexOne: int, indexTwo: int):
        temp = self.data[indexOne]
        self.data[indexOne] = self.data[indexTwo]
        self.data[indexTwo] = temp

    def _ensureCapacity(self):
        if self.size == self.capacity:
            self.data += [None] * self.capacity * 2
            self.capacity *= 2

    ## Peek root/min node
    def peek(self):
        if self.size == 0:
            raise Exception("Empty")

        return self.data[0]

    # Return/pop root
    def poll(self):
        if self.size == 0:
            raise Exception("Empty")

        item = self.data[0]
        # replace top node with last node
        self.data[0] = self.data[self.size-1]
        self.size -= 1
        # heapify
        self._heapifyDown()

        return item

    def insert(self, value: int):
        self._ensureCapacity()
        # Add node to last
        self.data[self.size] = value
        self.size += 1
        self._heapifyUp()

    def _heapifyUp(self):
        index = self.size - 1

        import pdb; pdb.set_trace()
        #Walk it up
        while self._hasParent(index) and self._parentItem(index) > self.data[index]:
            # Swap with parent
            self._swap(self._parentIndex(index), index)
            index = self._parentIndex(index)

    def _heapifyDown(self):
        index = 0

        while self._hasLeftChild(index):
            smallerIndex = self._leftChild(index)
            value = self.data[index]
            # print("index %d %d" % (index, self.size))
            # print(self.data)
            # print(self._rightItem(index))
            if self._hasRightChild(index) and self._rightItem(index) < self._leftItem(index):
                smallerIndex = self._rightChild(index)

            # Walking down
            if value < self.data[smallerIndex]:
                break
            else:
                self._swap(index, smallerIndex)
            index = smallerIndex


heap = MinHeap(10)
heap.insert(25)
print(heap.data)
heap.insert(20)
print(heap.data)
heap.insert(17)
print(heap.data)
heap.insert(15)
print(heap.data)
heap.insert(10)

print(heap.data)
while heap.size > 0:
    print(heap.poll())
