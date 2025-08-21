from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        
             
        left = 0
        right = len(height) - 1
 
        leftmax, rightmax = 0, 0
        water = 0 

        while left<right:
            if height[left]<height[right]:
                if height[left]>= leftmax:
                    leftmax = height[left]
                else:
                    water += leftmax - height[left]
                left += 1
            else:
                if height[right] >= rightmax:
                    rightmax = height[right]
                else:
                    water += rightmax - height[right]
                right -= 1


        return water


