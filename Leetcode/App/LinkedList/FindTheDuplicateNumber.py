from typing import List, Optional, Any


class Solution:
    def findDuplicate(self, nums: List[int]) -> Optional[Any]:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow
        return None
#287. Find the Duplicate Number