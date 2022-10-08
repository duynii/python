

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value: int):
        if value < self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value) -> bool:
        if value == self.data:
            return True
        elif value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def printInOrder(self):
        if self.left is not None:
            self.left.printInOrder()

        print(self.data)

        if self.right is not None:
            self.right.printInOrder()