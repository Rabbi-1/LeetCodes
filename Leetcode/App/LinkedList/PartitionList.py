class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode(0, head)
        after = ListNode(0, head)
        beforecurr, aftercurr = before, after
        while head:
            if head.val < x:
                beforecurr.next = head
                beforecurr = head
            else:
                aftercurr.next = head
                aftercurr = head
            head = head.next
        aftercurr.next = None
        beforecurr.next = after.next
        return before.next
#Leetcode 86