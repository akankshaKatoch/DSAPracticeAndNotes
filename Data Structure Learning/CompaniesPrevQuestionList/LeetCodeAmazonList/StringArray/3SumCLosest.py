from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        minDiff = 0

        for i in range(len(nums)):
            #if i>0 and nums[i] == nums[i-1]:
                #continue

            left = i+1
            right = len(nums)-1
            
            while left<right:
                curr_sum = nums[i] + nums[left] + nums [right]
                if curr_sum == target:
                    return curr_sum
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                if curr_sum < target:
                    left += 1
                else:
                    right -= 1


        return closest_sum


nums = [-1,2,1,-4]
target = 1
sol = Solution()
print(sol.threeSumClosest(nums, target))