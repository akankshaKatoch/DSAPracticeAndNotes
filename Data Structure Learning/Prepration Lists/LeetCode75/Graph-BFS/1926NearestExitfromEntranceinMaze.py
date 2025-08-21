from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque()
        queue.append((entrance[0], entrance[1], 0)) #tuple of (x , y and steps)

        directions = [(-1, 0), (1,0), (0, -1), (0,1)]

        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            r,c,steps = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if 0<= nr < rows and 0<= nc < cols:
                    if maze[nr][nc] == '.' and (nr, nc) not in visited:
                        if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                            return steps + 1
                        visited.add((nr, nc))
                        queue.append((nr, nc, steps+1))

        return -1
    
sol = Solution()
maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [1,2]
print(sol.nearestExit(maze, entrance))


maze = [[".","+"]]
entrance = [0,0]

print(sol.nearestExit(maze, entrance))




   