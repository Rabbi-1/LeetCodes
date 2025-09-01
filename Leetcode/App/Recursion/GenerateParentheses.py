from typing import List

def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def rec(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return
            if left < n:
                rec(left + 1, right, s + '(')
            if right < left:
                rec(left, right + 1, s + ')')
        rec(0, 0 , "")
        return res

#if left is less than n means we have room to add '(' to s
# if right less than left that means we can add ')' to s
# if s == n * 2: we reach a valid pair with valid combination (base case)
#append it to res

#22. Generate Parentheses