import math


class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        pre_op = "+"
        s += '+'
        stack = []

        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
            elif i == ' ':
                continue
            else:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    operant = stack.pop()
                    stack.append(operant * num)
                elif pre_op == '/':
                    operant = stack.pop()
                    stack.append(math.trunc(operant/num))
                num = 0
                pre_op = i
        return sum(stack)

    def calculate(self, s: str) -> int:
        i = 0
        cur = 0
        prev = 0
        res = 0
        cur_operation = "+"

        while i < len(s):
            cur_char = s[i]
            if cur_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])  # 332 '3' '3' '2'
                    i += 1
                i -= 1

                if cur_operation == "+":
                    res += cur
                    prev = cur
                elif cur_operation == "-":
                    res -= cur
                    prev = -cur
                elif cur_operation == "*":
                    res -= prev
                    res += prev * cur
                    prev = prev * cur
                else:
                    res -= prev
                    res += int(prev/cur)
                    prev = int(prev/cur)
                cur = 0
            elif cur_char != " ":
                cur_operation = cur_char
            i += 1
        return res
