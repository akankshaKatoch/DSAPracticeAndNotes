from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0]*n
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                elif i == 0:
                    dp[j] = dp[j-1] + grid[i][j]
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]
    

    def minPathSumTwo(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for j in range(1, n):
            grid[0][j] += grid[0][j-1]

        for i in range(1, m):
            grid[i][0] += grid[i-1][0]

        for i in range (1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[m-1][n-1]
     

        
