from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height)-1
        maxCapacity =0
        while left<right:
            w = right-left
            if height[left]<height[right]:
                h = height[left]
                left +=1
            else:
                h = height[right]
                right -= 1
            capacity = h*w
            maxCapacity=max(capacity,maxCapacity)
        return maxCapacity





height = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.maxArea(height))
        