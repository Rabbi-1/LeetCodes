def maxSubArray(self, nums: List[int]) -> int:
    maxSum = 10 ** 4 * -1
    currentSum = 0

    for num in nums:
        currentSum += num

        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return maxSum
#53. Maximum Subarray