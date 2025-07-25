from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        """
        nums = [1,0,-1,0,-2,2]
        after sorting = [-2, -1, 0, 0, 1, 2]
        # duplication isnot allowed

        """
        for i in range(len(nums)- 3):
            if i > 0 and nums[i]==nums[i-1]:
                continue

            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j]==nums[j-1]:
                    continue

                left = j + 1
                right = len(nums) - 1

                while left < right:
                    total = nums[i] + nums[j]+ nums[left] + nums[right]

                    if total < target:
                        left +=1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[i] , nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1

        return result            



nums = [1,0,-1,0,-2,2]
target = 0
sol = Solution()
print(sol.fourSum(nums, target))