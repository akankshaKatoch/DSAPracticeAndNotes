from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # o/p index of target
        # rotated array. peak and then if will fall. 
        # I can divide this problem in two parts. 
        # If I get element before the highest value. 5 
        # find peak and then search for no? 

        left = 0 
        right = len(nums) - 1

        while left<=right:
            mid = (left+right)//2
            print(mid)
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]:
                if nums[left]<= target< nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid]<target <=nums[right]:
                    left = mid+1
                else:
                    right = mid -1
            
        return -1 





nums = [4,5,6,7,0,1,2]
target = 0
sl = Solution()
print(sl.search(nums, target))
        