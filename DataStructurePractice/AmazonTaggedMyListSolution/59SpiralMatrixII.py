from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # ia m give n 
        # nXn
        # define my matrix []*n
        # LIST [] *N
        # TOP = 0 TO N
        # FOR 

        top = 0
        bottom = n-1
        print('bottom', bottom)

        left = 0
        right = n-1
        print('right', right)

        """This intialisation is incorrect as: The issue in your code is related to how you're initializing the matrix. 
        When you create the matrix using matrix = [[0]*n]*n, you're actually creating a list with n references to the same inner list. 
        This means when you modify one row, all other rows get modified simultaneously because they're the same list in memory.
        #matrix =[[0]*n]*n"""

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        #print(matrix)
        no = 0

        while top<=bottom and left<=right:

            #populate top row
            for i in range(left, right+1):
                no += 1
                matrix[top][i] = no
                print('[top][i] ', top, i )
            print(matrix)
            top +=1

            #popualte right side of the column
            for i in range(top, bottom+1):
                no +=1
                matrix[i][right] = no
                print('[i][right] ', i, right )
            print(matrix)
            right -= 1

            # populate the bottom rows.
            if top<= bottom:
                for i in range(right, left-1, -1):
                    no += 1
                    matrix[bottom][i] = no
                    print('[bottom][i] ', bottom, i )
            print(matrix)
            bottom -= 1

            #populate the left side of the column
            if left<=right:
                for i in range(bottom, top-1, -1):
                    no += 1
                    matrix[i][left] = no
                    print('[i][left] ', i, left )
                print(matrix)
            left +=1
        
        print(matrix)



            


n = 3
sol = Solution()
print(sol.generateMatrix(n))
