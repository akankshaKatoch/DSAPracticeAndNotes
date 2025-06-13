from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        """temp = [0]*len(cells)
        for _ in range(n):
            for i in range(len(cells)):
                
                # take care of border conditions. 
                if i ==0 or i == len(cells)-1:
                    #cells[i] = 0
                    temp[i] = 0
                #check for the adjacent cells
                # If a cell has two adjacent neighbors that are both occupied or both vacant, 
                # then the cell becomes occupied
                elif (cells[i-1] == 1 and cells[i+1] == 1) or (cells[i-1] == 0 and cells[i+1] == 0):
                    #cells[i] = 1
                    temp[i] = 1
                else:
                    #cells[i] = 0
                    temp[i] = 0
            #print('for :', _,  temp)
            #print('cells : ', cells, '->  temp : ', temp)
            cells = temp.copy()
            print(_, 'cells ',  cells)
            
            
        print("final : ", temp)
        return temp
        """

cells = [0,1,0,1,1,0,0,1] 
n = 7
sol = Solution()
print(sol.prisonAfterNDays(cells, n))