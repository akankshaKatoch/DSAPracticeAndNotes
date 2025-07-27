"""from collections import defaultdict

class Solution:
    def maxDifference(self, s: str) -> int:
        chardict = defaultdict(int)
        
        for char in s:
            chardict[char] +=1
        
        maxOdd = 0
        maxeven = 0
        
        for count in chardict.values():
            if count % 2 == 0:
                if count > maxeven:
                    maxeven = count
            if count % 2 == 1:
                if count > maxOdd:
                    maxOdd = count
        
        return maxOdd - maxeven 
    """
from typing import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        maxOdd = max(x for x in c.values() if x % 2 == 1)
        minEven = min(x for x in c.values() if x % 2 == 0)
        return maxOdd - minEven
    
s = "abcabcab"
sol = Solution()
print(sol.maxDifference(s))

            
