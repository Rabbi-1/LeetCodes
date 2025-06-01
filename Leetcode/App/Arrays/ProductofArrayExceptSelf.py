class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
# prefix = 1
# res = [1, 1, 2, 6]
# postfix = 4
# res = [1, 1, 2, 6]
# postfix = 12
# res = [1, 1, 8, 6]
# postfix = 12
# res = [1, 12, 8, 6]
# postfix = 24
# res = [24, 12, 8, 6]
# res = [1, 1, 2, 6]
# ris = [1, 4, 12, 24]
#LeetCode 238