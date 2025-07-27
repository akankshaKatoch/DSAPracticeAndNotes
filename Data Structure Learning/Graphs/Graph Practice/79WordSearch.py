from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        column = len(board[0])
        print('hello')
        for i in range(row):
            for j in range(column):
                if board[i][j] == word[0]:
                    stack = [(i,j,0, set())]
                    while stack:
                        x,y , index, visted = stack.pop()
                        print("x, y : ", x, y)
                        if index == len(word) - 1:
                            return True
                        #x,y = que.popleft()
                        if (x,y) in visted:
                            continue
                        
                        newvisited = set(visted)
                        newvisited.add((x,y))
                        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                            nx, ny = dx+x , dy+y
                            
                            if (0<=nx<row and 0<=ny<column and board[nx][ny]==word[index+1] and (nx, ny) not in newvisited ):
                                print(nx, ny, " -> board[nx][ny]: ", board[nx][ny] )
                                print( " newvisited : ", newvisited)
                                stack.append((nx, ny, index+1, newvisited))

        return False
    
#board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 

#word = "ABCCED"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
sol = Solution()
print(sol.exist(board, word))