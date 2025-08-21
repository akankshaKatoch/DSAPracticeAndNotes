from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        


        """
        my intuiton is to do 2d DP tabulation. 

        mat =  [[1,0,1],
                [1,1,0],
                [1,1,0]]

        mat =  [[1,0,1],
                [2,3,0],
                [3,7,0]]  1+1+2+3+3+6 => 16

                [[1, 0, 1], 
                [2, 3, 0], 
                [1, 5, 0]]
        
        """

        m = len(mat)
        n = len(mat[0])
        height = [0] * n
        #check = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                height[j] = height[j] + 1 if mat[i][j] == 1 else 0
                #check[j] = check[j] + mat[i][j] 
            #print(height)
            stack = []
            row_sum = 0
            for j in range(n):
                if height[j] == 0:
                    #no rectangle can end at j
                    stack.clear()
                    row_sum = 0
                    continue
                cnt = 1
                while stack and stack[-1][0] >= height[j]:
                    h, c = stack.pop()
                    row_sum -= h * c      # remove their contribution
                    cnt += c              # extend their spans with current column

                stack.append((height[j], cnt))
                row_sum += height[j] * cnt   # add contribution with new minimum
                ans += row_sum
        return ans



                
                
        print(height)
        print(check)
        return count
    

sol = Solution()
mat = [[1,0,1],[1,1,0],[1,1,0]]
print(sol.numSubmat(mat))

mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
print(sol.numSubmat(mat))