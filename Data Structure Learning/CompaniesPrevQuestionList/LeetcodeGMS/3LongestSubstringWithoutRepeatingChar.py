class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        best = 0
        uniqueChar = {}

        for right, ch in enumerate(s):
            if ch in uniqueChar and uniqueChar[ch] >= left:
                left = uniqueChar[ch]+1

            uniqueChar[ch] = right
            best = max(best, right - left + 1)
        print(uniqueChar)
        return best
        
    
sol = Solution()
s = "abcabcbb"

print(sol.lengthOfLongestSubstring(s))

s = "pwwkew"

print(sol.lengthOfLongestSubstring(s))



