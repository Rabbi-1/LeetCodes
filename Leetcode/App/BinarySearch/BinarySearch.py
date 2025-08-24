from typing import List


def search(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

class Solution:
    def binarySearch(self, l: int, r: int, nums: List[int], target:int) -> int:
        if l > r:
            return -1
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            return self.binarySearch(m+1, r, nums, target)
        else:
            return self.binarySearch(l, m-1, nums, target)

    def search1(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums) - 1, nums, target)
#704. Binary Search