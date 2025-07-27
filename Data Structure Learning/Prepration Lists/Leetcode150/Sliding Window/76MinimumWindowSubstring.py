from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        print(t_count)
        char_dict = {}
        have = 0 
        need = len(t_count)
        left = 0
        res = [-1,-1]
        res_len = float("inf")
        for right in range(len(s)):
            char = s[right]

            char_dict[char] = char_dict.get(char, 0) + 1

            if char in t_count and char_dict[char] == t_count[char]:
                have +=1
            while have == need:
                if (right-left+1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                char_dict[s[left]] -= 1
                if s[left] in t_count and char_dict[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        left, right = res
        return s[left:right+1] if res_len!=float("inf") else ""
     

sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(sol.minWindow(s,t))