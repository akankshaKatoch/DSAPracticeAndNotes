from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # key point to consider list is not sorted
        # nums = [1,2,3,1]
        # here array is not sorted but we can still use binary search as element will rise and then eventually drop right?

        left = 0
        right = len(nums) - 1

        while left<right:
            mid = (left + right)//2
            if nums[mid]<nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return left


nums = [1,2,1,3,5,6,4]
sl = Solution()
print(sl.findPeakElement(nums))

