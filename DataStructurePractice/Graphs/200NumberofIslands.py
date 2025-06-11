from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        print(grid)
        count = 0

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    count +=1 # this is the starting point for nodes not visited I think.
                    grid[i][j] = '0'
                    que = deque()
                    que.append((i,j))

                    while que:
                        x,y = que.popleft()
                        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                            nx, ny = dx+x, dy+y
                            if 0<= nx < rows and 0<= ny < columns and grid[nx][ny] =='1':
                                grid[nx][ny] = '0'
                                que.append((nx,ny))

        print(grid)
        return count





grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
sol = Solution()
print(sol.numIslands(grid))

"""
00, 01, 02, 03, 04
10, 11, 12, 13, 14
20, 21, 22, 23, 24
30, 31, 32, 33, 34

AdLs : 
0: 1, 

"""