class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n<2:
            return s
        bestl, bestr = 0, 0 
        def isPalindrome(l: int, r: int) -> bool:
            while l<=r:
                if s[l] != s[r]:
                    return False
                l +=1
                r -= 1
            return True
        bestLen = 1

        for l in range(n):
            if n-l <= bestLen:
                break 
            for r in range(n-1, l+ bestLen-1, -1):
                if isPalindrome(l, r):
                    bestl, bestr = l, r
                    bestLen = r - l + 1
                    break

        return s[bestl:bestr+1]

            


        

sol = Solution()
s = "babadab"
print(sol.longestPalindrome(s))
