from typing import DefaultDict
from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = 0 
        charDict = DefaultDict(int)
        #char_count = OrderedDict()

        for char in s:
            charDict[char] += 1
            # char_count[char] = char_count.get(char, 0) + 1
        
        for index, key in enumerate(s):
            if charDict[key]==1:
                return index

        return -1
        

s = "leetcodel"
sol = Solution()
print(sol.firstUniqChar(s))