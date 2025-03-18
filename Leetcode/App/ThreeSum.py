from typing import List


class ThreeSum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if val > 0: 
                break
            if i > 0 and val == nums[i - 1]:
                continue 

            #Set the pointers
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threesum = val + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                elif threesum == 0:
                    res.append([val, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                    
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        length = len(nums)
        for val in range(length - 2):
            if val > 0 and nums[val] == nums[val-1]:
                continue
            l = val + 1
            r = length - 1
            while l < r:
                temp = nums[val] + nums[l] + nums[r]
                if temp == 0:
                    res.add((nums[val], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif temp > 0:
                    r -= 1
                else:
                    l += 1
        return [list(triplet) for triplet in res]
