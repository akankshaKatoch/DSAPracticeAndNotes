from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        minLen = float('inf')
        result = []
        total = 0

        for right in range(n):
            total += nums[right]

            while total >= target:
                if right - left + 1 < minLen:
                    minLen = right  - left + 1
                    result = nums[left : right+1]
                # if it just need the length then dont do above If condition 
                # just run below code and get the minleng and return that
                # minLen = min(min_len, right-left + 1)
                total -= nums[left]
                left +=1
        return result

sol = Solution()            
target = 7
nums = [2,3,1,2,4,3]
print(sol.minSubArrayLen(target, nums))
target = 7
nums = [2,3,2,2,4,3]
print(sol.minSubArrayLen(target, nums))
target = 4
nums = [1,4,4]
print(sol.minSubArrayLen(target, nums))
target = 11
nums = [1,1,1,1,1,1,1,1]
print(sol.minSubArrayLen(target, nums))

