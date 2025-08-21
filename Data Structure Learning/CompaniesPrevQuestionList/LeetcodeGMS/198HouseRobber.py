from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        table = [0]*len(nums)
        

        def dp(i, memo = None):
            if memo == None:
                memo = {}
            if i in memo: return memo[i]

            if i> len(nums):
                return 0
            
            curr = nums[i] + dp(i+2)
            skip = dp(i+1)

            memo[i] = max(curr, skip)
            return memo[i]
        
        return dp(0)

