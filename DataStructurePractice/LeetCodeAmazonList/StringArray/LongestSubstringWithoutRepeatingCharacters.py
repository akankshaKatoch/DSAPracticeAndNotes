from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_char = defaultdict()
        #left
        char_set = set()
        maxLongSUbString = 0
        left = 0
        right = 0
        substring = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            maxLongSUbString = max(maxLongSUbString, right-left+1)
        return maxLongSUbString
    
s = "pwwkew"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))