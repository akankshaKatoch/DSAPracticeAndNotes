from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)
        #imp points
        def calEatingSpeed(k):
            thours = 0
            for pile in piles:
                thours = (pile+k-1)//k
            return thours<=h
        result = right
        if left <= right:
            #imp point
            mid = (left + right)// 2
            if calEatingSpeed(mid):
                result = mid
                right -= 1
            else: 
                left += 1

        return result
                
            
sol = Solution()
piles = [3,6,7,11] 
h = 8
print(sol.minEatingSpeed(piles, h))
        