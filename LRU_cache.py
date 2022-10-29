class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.value = val
        self.prev = self.next = None
import sys
# Needs debugging
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.head = self.tail = None
        self.summy = -sys.maxint

    def promote(self, key):
        node = self.head.next
        while node.key != key:
            node = node.next

        print('promote ', node.key)
        if key == self.tail.key:
            self.tail = self.tail.prev
        # extract
        node.prev.next = node.next
        node.next = self.head
        self.head.prev = node
        self.head = node

    def get(self, key: int) -> int:
        print('get ', key)
        if key not in self.data:
            return -1
        elif self.head.key == key:
            return self.head.value
        # elif self.tail.key == key:
        #     self.tail.prev.next = None
        #     self.tail.next = self.head
        #     tmp = self.tail.prev
        #     self.head = self.tail
        else:
            self.promote(key)

        print('get head', self.head.key)
        print('get tail', self.tail.key)

        return self.head.value

    def put(self, key: int, value: int) -> None:
        print('put', key)
        if not self.head:
            self.data[key] = value
            self.head = Node(key, value)
            self.tail = self.head
        else:
            self.data[key] = value
            node = Node(key, value)
            node.next = self.head
            self.head.prev = node
            self.head = node

        print('put head', self.head.key)
        print('put tail', self.tail.key)

        if len(self.data) > self.capacity:
            print('trim ', self.tail.key)
            node = self.tail
            # if self.tail == self.head:
            #     head = None
            print('head', self.head.key)
            print('tail', self.tail.key)
            self.tail = self.tail.prev

            self.data.pop(key)
