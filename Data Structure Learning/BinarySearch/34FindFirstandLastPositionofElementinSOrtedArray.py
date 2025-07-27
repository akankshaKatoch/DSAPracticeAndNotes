from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findFirst(nums, target):
            first = -1
            left = 0
            right = len(nums) - 1

            #should i search for the left and then for the right?
            while left<= right:
                mid = (left+right)//2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    first = mid 
                    right = mid -1
            return first
        
        def findLast(nums, target):
            last = -1
            left = 0
            right = len(nums) - 1

            #should i search for the left and then for the right?
            while left<= right:
                mid = (left+right)//2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    last = mid 
                    left = mid + 1
            return last
        first = findFirst(nums, target)
        last = findLast(nums, target)

        return [first, last]
        
sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))  # Output: [3, 4]
print(sol.searchRange([5,7,7,8,8,10], 6))  # Output: [-1, -1]
print(sol.searchRange([], 0))  # Output: [-1, -1]
print(sol.searchRange([1,1,1,1], 1)) 






        