from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        low = 0
        #Left side must contain these many elelemts. 
        leftsize = (m+n+1)//2
        high = m

        while low<=high:
            i = (low+high)//2
            j = leftsize - i

            nums1_left = nums1[i-1] if i > 0 else '-inf' 
            nums1_right = nums1[i] if i<m else 'inf'
            nums2_left = nums2[j-1] if j >0 else '-inf'
            nums2_right = nums2[j] if j < n else 'inf'

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m+n)%2:
                    return max(nums1_left, nums2_left)
                else:
                    return(max(nums1_left, nums2_left)+ min(nums1_right, nums2_right))/2.0
            elif nums1_left>nums2_right:
                high = i-1
            else:
                low = i+1

sol = Solution()
nums1 = [1, 5, 9, 10, 11, 15]
nums2 = [2, 3, 6, 7, 12, 14]

print(sol.findMedianSortedArrays(nums1, nums2))




        
