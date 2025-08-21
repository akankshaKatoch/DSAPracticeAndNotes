class Solution:
    def climbStairs(self, n: int) -> int:



        """
        def dp(k: int, memo = None):
            if memo == None:
                memo = {}
            if k in memo:
                return memo[k]
            if k<=1:
                return 1
            memo[k] = dp(k-1, memo) + dp(k-2, memo)
            return memo[k]
        
        return dp(n)
        """

            


        """
        def dp(k: int):
            if k<=1:
                return 1

            return dp(k-1) + dp(k-2)
        return dp(n)
        """


sol = Solution()
n = 2
print(sol.climbStairs(n))