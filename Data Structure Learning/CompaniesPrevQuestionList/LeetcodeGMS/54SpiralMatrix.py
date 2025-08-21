from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        toprow = 0
        bottomrow = len(matrix)-1

        leftcol = 0
        rightcol = len(matrix[0])-1

        res = []
        while toprow<=bottomrow and leftcol<=rightcol:
            for j in range(leftcol, rightcol+1):
                res.append(matrix[toprow][j])
            toprow+=1
            for i in range(toprow, bottomrow+1):
                res.append(matrix[i][rightcol])
            rightcol -= 1
            
            if toprow<= bottomrow:
                for j in range(rightcol, leftcol-1, -1):
                    res.append(matrix[bottomrow][j])
                bottomrow -= 1
            if leftcol <= rightcol:
                for i in range(bottomrow, toprow-1, -1):
                    res.append(matrix[i][leftcol])
                leftcol += 1

        return res



        


sol = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(sol.spiralOrder(matrix))