# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq


class HeapNode:
    def __init__(self, val=0, fr=None):
        self.val = val
        self.fr = fr

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeSort(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            # print(list1.val, list2.val, list1 != None, list2 != None)
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next

            # print(list1.val, list2.val, list1 != None, list2 != None)

        if list1:
            cur.next = list1
        else:
            cur.next = list2

        return dummy.next

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:

        # Attempt to use heap merge - or just call heapq.merge()
        # O(2nlog(k)) with only O(k) space in the heap, and O(n) in result
        def heapMerge(lists: list[list]) -> list:
            minheap = []
            heapq.heapify(minheap)
            dummy = ListNode()
            cur = dummy
            for ll in lists:
                if not ll:
                    continue
                heapq.heappush(minheap, HeapNode(ll.val, ll))

            while len(minheap) > 0:
                node = heapq.heappop(minheap)
                cur.next = node.fr
                cur = cur.next

                if node.fr.next:
                    heapq.heappush(minheap, HeapNode(node.fr.next.val, node.fr.next))

            return dummy.next

        # Divide and conquer using mergeSort, Time O(n log(k)) because of divide and conquer k lists
        def merge(lists) -> list:
            if not lists or len(lists) == 0:
                return None

            while len(lists) > 1:
                mergedLists = []
                for i in range(0, len(lists), 2):
                    l = lists[i]
                    r = lists[i + 1] if i + 1 < len(lists) else None

                    mergedLists.append(self.mergeSort(l, r))

                lists = mergedLists

            return lists[0]

        # return heapMerge(lists)
        return merge(lists)