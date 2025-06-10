from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1

        while left<right:
            mid = (left+right)//2

            if mid % 2 == 1:
                mid -= 1

            #Now      1 1 2 3 3 4 4 8 8
            #index    0 1 2 3 4 5 6 7 8
            #Now      1 1 3 3 4 4 5 5 7 7 8  9  9
            #index    0 1 2 3 4 5 6 7 8 9 10 11 12
            if nums[mid]==nums[mid+1]:
                left = mid +2 
            else: 
                right = mid

        return nums[left]


            
        """This is brute force wont work much.
            if nums[mid-1] != nums[mid] or nums[mid] != nums[mid+1]:
                return nums[mid]"""
            

nums = [1,1,2,3,3,4,4,8,8]
nums2 = [3,3,7,7,10,11,11]
s1 = Solution()
print(s1.singleNonDuplicate(nums))
print(s1.singleNonDuplicate(nums2))