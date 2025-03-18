class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            temp = ""
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    temp += s[i]
                    i += 1
                stack.append(int(temp))
                continue
            elif s[i] == '[':
                stack.append('[')
            elif s[i] == ']':
                substring = ""
                while stack and stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()
                repeat_count = stack.pop()
                stack.append(repeat_count * substring)
            else:
                stack.append(s[i])
            i += 1

        return ''.join(stack)
