from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            check = numbers[left] + numbers[right]
            if check == target:
                return [left + 1, right + 1]
            elif check >= target:
                right -= 1
            else:
                left += 1
        return None

#167. Two Sum II - Input Array Is Sorted
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]

        return []
