from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        #find peak element

        while left<right:
            mid = (left+right)//2

            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[left]
                


nums1 = [4,5,6,7,0,1,2]
nums2 = [3,4,5,1,2]
nums3 = [11,13,15,17]
sl = Solution()

print(sl.findMin(nums1))
print(sl.findMin(nums2))
print(sl.findMin(nums3))
        