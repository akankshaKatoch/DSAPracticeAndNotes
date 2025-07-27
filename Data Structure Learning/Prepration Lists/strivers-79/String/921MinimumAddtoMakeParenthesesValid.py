class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        parenthesesDic = {')':'(',
                          '}':'{',
                          ']':'['
                          }
        minAdd = 0
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            elif char in parenthesesDic:
                if stack[-1] == parenthesesDic[char]:
                    stack.pop()
                else: stack.append(char)
            else :
                stack.append(char)
        return len(stack)





s = "((((())"
sol = Solution()
print(sol.minAddToMakeValid(s))