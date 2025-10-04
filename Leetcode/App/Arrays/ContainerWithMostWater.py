#Brute Force
from typing import List

#Searching through all possible pairs of values takes O(n^2) time,
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_water = 0
        for i in range(n):
            for j in range(i+1, n):
                water = min(height[i], height[j]) * (j - i)
                max_water = max(max_water, water)

        return max_water


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        water_max = 0
        while left < right:

            water = min(height[left], height[right]) * (right - left)
            water_max = max(water_max, water)
            if height[right] < height[left]:
                right -= 1
            elif height[right] > height[left]:
                left += 1
            else:
                left += 1
                right -= 1
        return water_max


'''
Time complexlty: The time complexity of largest_container is O(n) because we perform approximately n iterations using the two-pointer technique.
Space complexity: We only allocated a constant number of variables, so the space complexity is
0(1)
'''