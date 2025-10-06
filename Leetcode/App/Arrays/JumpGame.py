from typing import List


def canJump(self, nums: List[int]) -> bool:
    gas = 0
    for n in nums:
        if gas < 0: #run out of gas
            return False
        elif n > gas:
            gas = n
        gas -= 1
    return True
#55. JumpGame
#we go through the array each iteration takes one gas if next index gas is greater replace gas
#now we do this proccess till we reach the end(true) or we run out(false)