from typing import List


class Solution:
'''
    Sort the array to handle duplicates and use two-pointer approach.
    For each element:
        - Skip duplicates.
        - Set left and right pointers.
        - While left < right:
            → If sum > 0 → move right pointer left.
            → If sum < 0 → move left pointer right.
            → If sum == 0 → add triplet to result, move both pointers, skip duplicates.
    Return all unique triplets.
'''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r-= 1
                elif threeSum < 0:
                    l+= 1
                else:
                    res.append([nums[i],nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res