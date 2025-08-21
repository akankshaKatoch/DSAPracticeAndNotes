from collections import defaultdict
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        chardic = defaultdict(int)
        charset = set()

        freq = Counter(s)  
        print(freq) 

        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
        return -1

        for index, char in enumerate(s):
            if char in charset:
                if char in chardic:
                    del chardic[char]
            else:
                chardic[char] = index
                charset.add(char)
        print(chardic)
        return next(iter(chardic.values())) if chardic else -1



sol = Solution()

s = "leetcode"
print(sol.firstUniqChar(s))

s = "loveleetcode"
print(sol.firstUniqChar(s))

s = "aabb"
print(sol.firstUniqChar(s))

s = "aadadaad"
print(sol.firstUniqChar(s))

