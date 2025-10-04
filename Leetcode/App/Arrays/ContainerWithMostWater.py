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
