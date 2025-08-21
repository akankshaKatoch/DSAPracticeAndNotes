from typing import List
from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        dailPadMap = { "2":"abc", "3":"def", "4":"ghi", "5":"jkl","6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        queue =deque([""])
        # what should happen if my digit have 0 1 in it?
        for digit in digits:
            for _ in range(len(queue)):
                base = queue.popleft()
                for ch in dailPadMap[digit]:
                    print(base)
                    queue.append(base+ch)


        return list(queue)
            
sol = Solution()
digits = "236"
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(sol.letterCombinations(digits))



        
        
