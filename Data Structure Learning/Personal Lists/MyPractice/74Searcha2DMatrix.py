from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m*n -1

        while left<=right:
            mid = (left+right) // 2
            row = mid // n
            col = mid%n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False



        """
        Instead of slowing row by row wise which will be inefficient solution we will treat whole matrix and find themid point. 
        """
        """for i in range(len(matrix)):
            print(i)
            right = len(matrix[i])
            left = 0
            while left<=right:
                mid = (right+left) // 2
                if matrix[i][mid] < target:
                    right = mid-1

                elif matrix[i][mid] > target:
                    left = mid+1

                else:
                    return True
        return False    """
            


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
sol = Solution()
print(sol.searchMatrix(matrix, target))      