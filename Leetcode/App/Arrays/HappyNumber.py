def isHappy(n: int) -> bool:
    hset = set()
    while n != 1:
        if n in hset:
            return False
        hset.add(n)
        n = sum([int(i) ** 2 for i in str(n)])
    return True


class Solution:
    pass

#202. Happy Number