from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        row, col = len(grid), len(grid[0])
        count = 0

        def dfs(r,c):

            #base condition when we are out of grid or when value = 0
            if r< 0 or r>=row or c<0 or c>=col or grid[r][c]=='0':
                return
            #make it zero so that we dont visit again. 
            grid[r][c] ='0'
            #do dfs for each side of this node recursively. this will remove all the attached nodes marked as 1 to 0. 
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count



# when we see 1 we srart new island count. change 0 to 1 so that dont revisit it. 

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

sol = Solution()
print(sol.numIslands(grid))