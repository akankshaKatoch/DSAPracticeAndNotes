from typing import List 

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        result = 0
        streak = 0

        for x in nums:
            if x==0:
                streak += 1
                result += streak # it goes like this - 1 + 1 , 2 + 2, 4 + 3, 7+ 1, 8+ 1
            else:
                streak = 0
        return result



sol = Solution()
nums = [1,3,0,0,2,0,0,4]
print(sol.zeroFilledSubarray(nums))
nums = [0,0,0,2,0,0]
print(sol.zeroFilledSubarray(nums))