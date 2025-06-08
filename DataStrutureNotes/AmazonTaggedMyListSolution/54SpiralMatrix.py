from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        toprow = 0
        bottomrow = len(matrix) -1

        leftcol = 0
        rightcol = len(matrix[0]) -1
        result = []

        while toprow<=bottomrow and leftcol<=rightcol:
            #travese from top to bottom
            for i in range(leftcol, rightcol+1):
                result.append(matrix[toprow][i])
            toprow +=1

            # traversal from 2nd row to bottom
            for i in range(toprow, bottomrow+1):
                result.append(matrix[i][rightcol])
            rightcol -= 1

            # traversal from right to left
            if toprow <= bottomrow: 
                for i in range(rightcol, leftcol -1, -1):
                    result.append(matrix[bottomrow][i])
                bottomrow -= 1
            
            if leftcol <= rightcol:
                for i in range(bottomrow, toprow-1, -1):
                    result.append(matrix[i][leftcol])
                leftcol += 1
            
        return result
        

matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
print(sol.spiralOrder(matrix))




