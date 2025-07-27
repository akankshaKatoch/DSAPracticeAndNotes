class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
       # memoisation
       def lcs(i,j, memo = None):
            key = (i,j)
            if memo is None:
                memo = {}
            if i == len(text1) or j == len(text2):
                return 0
            if key in memo:
                return memo[key]
            if text1[i] == text2[j]:
                memo[key] = 1 + lcs(i+1, j+1, memo)
            else:
                memo[key] = max(lcs(i+1, j, memo), lcs(i, j+1, memo))
            return memo[key]
           
       return lcs(0,0)
       # recursive
       def lcs(i,j):
           if i == len(text1) or j == len(text2):
               return 0
           if text1[i] == text2[j]:
               return 1 + lcs(i+1, j+1)
           else:
               return max(lcs(i+1, j), lcs(i, j+1))
           
       return lcs(0,0)