from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # pointers 
        #left max value and right max value 
        #Water can be stored in between of these max values. 
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        """for example from left side the min is = no water can be stored. and no boundary 
        at 2nd index it have the 1 which is max between left 
        """
        left = 0 
        right = len(height)-1
        max_left = height[left]
        max_right = height[right]
        water_unit = 0
        while left<right:
            if height[left]<height[right]:
                left +=1
                max_left = max(max_left, height[left])
                water_unit += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                water_unit += max_right - height[right]

        return water_unit

height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trap(height))
