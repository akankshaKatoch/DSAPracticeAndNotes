class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        uniqueChar = set()
        #count = 0
        maxCount = 0

        for right in range(len(s)):
            while s[right] in uniqueChar:
                uniqueChar.remove(s[left])
                left +=1
            uniqueChar.add(s[right])
            maxCount = max(maxCount, right- left + 1)
        return maxCount


sol = Solution()
s = "abcabcbb"
print(sol.lengthOfLongestSubstring(s))

s = "bbbbb"
print(sol.lengthOfLongestSubstring(s))

s = "pwwkew"
print(sol.lengthOfLongestSubstring(s))
            

