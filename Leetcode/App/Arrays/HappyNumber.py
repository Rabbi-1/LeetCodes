def isHappy(n: int) -> bool:
    hset = set()
    while n != 1:
        if n in hset:
            return False
        hset.add(n)
        n = sum([int(i) ** 2 for i in str(n)])
    return True

def isHappy(self, n: int) -> bool:
    def nxt(x: int) -> int:
        return sum((int(i) ** 2 for i in str(x)))
    slow = n
    fast = nxt(n)
    while fast != 1 and slow != 1 and slow != fast:
        slow = nxt(slow)
        fast = nxt(nxt(fast))

    return fast == 1 or slow == 1

#202. Happy Number