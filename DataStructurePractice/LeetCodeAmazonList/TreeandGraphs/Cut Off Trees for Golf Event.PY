from typing import List
from collections import deque
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
    # 1st try to get the sorted values for forest. 
    
        tree = []

        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] > 1:
                    tree.append((forest[i][j], i, j))

        tree.sort()
        print(tree)

        total_steps = 0
        x, y = 0, 0

        def bfs(forest, startx, starty, endx, endy):
            que = deque([(startx, starty, 0)])
            visited = set()
            visited.add((startx, starty))

            while que:
                x, y, steps = que.popleft()
                if x == endx and y == endy:
                    return steps
                for dx, dy in [(1,0), (-1,0), (0, 1), (0,-1)]:
                    nx, ny =  dx+x, dy+y
                    if 0 <= nx < len(forest) and 0 <= ny < len(forest[0]) and forest[nx][ny] != 0 and (nx, ny) not in visited:
                        visited.add((nx,ny))
                        que.append((nx, ny, steps+1))
            return -1
        
        for height, next_x, next_y in tree:
            steps = bfs(forest, x, y, next_x, next_y)
            if steps == -1:
                return -1
            total_steps += steps
            x, y = next_x, next_y  # Move to the next tree

        return total_steps

        

      
      
      
      # my solution is totally wrong/ 
    """ self.count = 0
        totalcells = len(forest) * len(forest[0]) 
        def dfs(forest, x, y):
            if x <0 or x>= len(forest) or y < 0 or y>= len(forest[0]) or forest[x][y] == 0:
                return 
            self.count += 1
            dfs(forest, x-1, y)
            dfs(forest, x+1, y)
            dfs(forest, x, y-1)
            dfs(forest, x, y)
        dfs(forest, x=0, y=0)
        return totalcells - self.count
            """
            
            



forest1 = [[1,2,3],
           [0,0,4],
           [7,6,5]]
forest = [[1,2,3],[0,0,0],[7,6,5]]

sol = Solution()
print = sol.cutOffTree(forest1)