from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0 
        right = len(nums) - 1
        operation = 0

        while left<right:
            currentsum = nums[left] + nums[right] 
            if currentsum== k:
                left += 1
                right -= 1
                operation += 1
            elif currentsum < k:
                left += 1
            else:
                right -= 1
        return operation
            
                
        