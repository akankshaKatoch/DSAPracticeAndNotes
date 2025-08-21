from typing import List 
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diag1 = set()
        diag2 = set()
        pos = [-1] * n      # pos[r] = column index of the queen in row r
        ans: List[List[str]] = []
        def backtrack(r:int):
            if r == n:
                print("line 11 pos", pos)
                board = ['.' * pos[i] + 'Q' + '.' * (n - pos[i] - 1) for i in range(n)]
                ans.append(board)
                return 
            for c in range(n):
                print("line 16: C: ", c, "and r: ", r)
                if c in col or r-c in diag1 or r+c in diag2:
                    continue
                pos[r] = c
                col.add(c); diag1.add(r-c); diag2.add(r+c)
                #print("line 21: col: ", col, " diag1: ", diag1, " diag2: ", diag2)
                backtrack(r+1)
                #print("line 23: col: ", col, " diag1: ", diag1, " diag2: ", diag2)
                col.remove(c); diag1.remove(r-c); diag2.remove(r+c)
                pos[r] = -1
        backtrack(0)
        return ans
    
sol = Solution()
n = 4
print(sol.solveNQueens(n))