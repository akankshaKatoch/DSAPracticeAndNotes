from typing import List

class Solution:
    def robRecursive(self, nums: List[int]) -> int:

        def rob(i):
            if i>=len(nums):
                return 0
            rob_current = nums[i] + rob(i+2)
            skip_current = rob(i+1)
            return max(rob_current, skip_current)
        return rob(0)


    def robMemoisation(self, nums: List[int]) -> int:
        
        def rob(i, memo = None):
            if memo == None:
                memo = {}
            if i>=len(nums):
                return 0
            if i in memo:
                return memo[i]
            rob_current = nums[i] + rob(i+2, memo)
            skip_current = rob(i+1, memo)
            memo[i] =  max(rob_current, skip_current)  
            return memo[i]   
        return rob(0)

    def robTabulation(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        

        table = [0]*(len(nums))
        table[0] = nums[0]
        table[1] = max(nums[0], nums[1])

        for i in range(2,len(table)):
            table[i] = max(nums[i-1], nums[i] + table[i-2])
        return table[-1]

sol = Solution()


nums = [1,2,3,5]
print(sol.robRecursive(nums))
print(sol.robMemoisation(nums))
print(sol.robTabulation(nums))
nums = [2,7,9,3,1]
print(sol.robRecursive(nums))
print(sol.robMemoisation(nums))
print(sol.robTabulation(nums))