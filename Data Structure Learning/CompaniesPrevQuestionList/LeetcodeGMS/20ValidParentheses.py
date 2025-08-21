class Solution:
    def isValid(self, s: str) -> bool:

        paraDict = {"}":"{", "]":"[", ")":"("}

        stack = []
        for p in s:
            if p in paraDict:
                if stack:
                    open = stack.pop()
                    if paraDict[p] != open:
                        return False
                else:
                    return False
                
            else:
                stack.append(p)
                
                
        return True if not stack else False

        

sol = Solution()
s = "(())[]"
print(sol.isValid(s))
