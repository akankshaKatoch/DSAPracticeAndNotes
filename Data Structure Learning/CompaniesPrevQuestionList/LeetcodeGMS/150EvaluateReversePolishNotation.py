from typing import List 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        total = 0

        for t in tokens:
            if t.lstrip('-').isdigit():
                stack.append(int(t))
            else: 
                a = stack.pop()
                b = stack.pop()
                if t == '+':
                    stack.append(b+a)
                elif t == "-":
                    stack.append(b-a)
                elif t == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(b/a))
            print(stack)
        return stack.pop()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

sol = Solution()

print(sol.evalRPN(tokens))
