# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head == None:
            return False

        def findMid(head: ListNode) -> ListNode:
            start = head
            end = head
            while end and end.next:
                start = start.next
                end = end.next.next

            return start

        # Returns end node
        def reverse(head: ListNode) -> ListNode:
            prev = None
            slow = head
            while slow:
                tmp = slow.next
                slow.next = prev
                prev = slow
                slow = tmp

            return prev

        mid = findMid(head)

        reverseHead = reverse(mid)

        while reverseHead:
            if head.val != reverseHead.val:
                return False

            head = head.next
            reverseHead = reverseHead.next

        return True
