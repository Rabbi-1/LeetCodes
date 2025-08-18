# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    import heapq
    min_heap = []

    for node in lists:
        while node:
            heapq.heappush(min_heap, node.val)
            node = node.next
    dummy = ListNode(0)
    cur = dummy

    while min_heap:
        cur.next = ListNode(heapq.heappop(min_heap))
        cur = cur.next
    return dummy.next
# 23. Merge k Sorted Lists