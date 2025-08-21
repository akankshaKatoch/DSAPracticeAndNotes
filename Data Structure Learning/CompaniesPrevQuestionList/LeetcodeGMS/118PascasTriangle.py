from typing import List 

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = []

        for i in range(numRows):
            row = [1]*(i+1)
            for j in range(1,i):
                row[j] = pascalTriangle[i-1][j-1]+ pascalTriangle[i-1][j]
                #for j[2][1] = i [1,0] + i[1,1]
            pascalTriangle.append(row)

        return pascalTriangle


sol = Solution()
numRows = 5
print(sol.generate(numRows))
         