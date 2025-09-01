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


#22. Generate Parentheses