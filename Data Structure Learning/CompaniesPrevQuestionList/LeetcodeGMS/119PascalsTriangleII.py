from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascalTriangle = []

        for i in range(rowIndex+1):
            row = [1]*(i+1)
            for j in range(1,i):
                row[j] = pascalTriangle[i-1][j-1]+ pascalTriangle[i-1][j]
                #for j[2][1] = i [1,0] + i[1,1]
            #print(row)
            pascalTriangle.append(row)

        return pascalTriangle[rowIndex]
    

    
sol = Solution()
rowIndex = 5
print(sol.getRow(rowIndex))
        