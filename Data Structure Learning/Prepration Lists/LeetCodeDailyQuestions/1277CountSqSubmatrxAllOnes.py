from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        [
         [0,1,1,1],
         [1,1,1,1],
         [0,1,1,1]
        ]
        1X1
        2X2
        3X3
        4X4
        """
        
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0]* n for _ in range(m)]
        
        count = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    count += dp[i][j]
        return count 
    
sol = Solution()
matrix =[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

print(sol.countSquares(matrix))

