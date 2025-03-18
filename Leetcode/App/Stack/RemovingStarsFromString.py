class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i == '*':
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)


# s = "leet**cod*e"
# s = lee*cod*e -> lecod*e -> lecoe
