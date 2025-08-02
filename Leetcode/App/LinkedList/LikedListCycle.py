from typing import Optional


class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    @staticmethod
    def hasCycle(head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
#141. Linked List Cycle