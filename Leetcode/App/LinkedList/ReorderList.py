from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle of the list.
        # Reverse the second half of the list.
        # Merge the two halves.
        slow = head
        fast = head.next
        #Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        #Reverse
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        #Merge
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
    #143. Reorder List

