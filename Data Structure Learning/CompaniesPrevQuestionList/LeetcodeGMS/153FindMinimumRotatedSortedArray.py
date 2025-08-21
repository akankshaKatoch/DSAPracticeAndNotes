from typing import List 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums)-1
        print(nums)
        while left<right:
            mid = (left+right)//2
            print(mid)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

        
#1,2,3,4,5,6 
#5,6,1,2,3,4
#3,4,5,6,1,2

sol = Solution()
nums = [3,4,5,1,2]
print(sol.findMin(nums))
nums = [11,13,15,17]
print(sol.findMin(nums))
nums = [2,3,4,5,6,1]
print(sol.findMin(nums))