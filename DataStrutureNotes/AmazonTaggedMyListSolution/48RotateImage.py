from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #print(matrix)
        for i in range(len(matrix)):
            #k = len(matrix) - 1
            for j in range (i, len(matrix)):
                matrix[i][j], matrix[j][i]=  matrix[j][i], matrix[i][j]
        #print(matrix)
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        







matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
print(sol.rotate(matrix))