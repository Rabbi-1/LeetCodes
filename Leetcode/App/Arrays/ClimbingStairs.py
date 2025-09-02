def climbStairs(n: int) -> int:
    one = 1
    two = 1
    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
    return one

#70. Climbing Stairs