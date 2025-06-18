class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        n = len(nums)
        for i in range(n):
            goal = target - nums[i]
            if goal in res:
                return [res[goal], i]
            res[nums[i]] = i
        return []
