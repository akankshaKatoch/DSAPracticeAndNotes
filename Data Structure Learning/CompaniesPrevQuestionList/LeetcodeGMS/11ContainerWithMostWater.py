from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxWater = 0
        while left<right:
            #print(height[left]," - ", height[right])
            current_water = min(height[left], height[right])*(right-left)
            maxWater = max(maxWater, current_water)
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1

        return maxWater


            
        
sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))