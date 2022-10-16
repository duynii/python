
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def printList(head: ListNode, msg=''):
    node = head
    print('printList %s:' % msg, end=' ', sep=' ')
    while node:
        print(node.val, end=' ', sep=' ')
        node = node.next
    print()

#Sort linked list
class Soln:
    @staticmethod
    def getMiddleNode(head: ListNode) -> ListNode:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    @staticmethod
    def sortList(head: ListNode) -> ListNode:
        # Base condition
        if head is None or head.next is None:
            return head

        left = head
        right = Soln.getMiddleNode(head)
        # import pdb; pdb.set_trace()
        tmp = right.next
        right.next = None
        right = tmp
        printList(left, 'left')
        printList(right, 'right')

        left = Soln.sortList(left)
        right = Soln.sortList(right)

        def merge(left: ListNode, right: ListNode) -> ListNode:
            root = dummy = ListNode()
            while left is not None and right is not None:
                if left.val < right.val:
                    root.next = left
                    left = left.next
                else:
                    root.next = right
                    right = right.next
                root = root.next

            if left:
                root.next = left
            if right:
                root.next = right

            return dummy.next

        return merge(left, right)


n4 = ListNode(1, None)
n3 = ListNode(7, n4)
n2 = ListNode(4, n3)
tail = ListNode(9, n2)

# import pdb; pdb.set_trace()
right = Soln.getMiddleNode(n3)
sorted = Soln.sortList(tail)
printList(sorted, 'final')