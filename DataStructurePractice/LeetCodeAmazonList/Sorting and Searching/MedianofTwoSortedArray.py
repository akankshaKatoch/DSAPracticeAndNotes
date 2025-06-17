from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # you have to merge while combining the list. 
        #make sure len of num1 is small or num 1 is smallest array. 
        if len(nums1)>len(nums2):
            nums2, nums1 = nums1, nums2

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m
        totallen = m + n 

        #---- -----

        while(left<=right):
            partition1 = (left+right)//2
            partition2 = (totallen +1)//2 - partition1

            max_left_nums1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right_nums1 = float('inf') if partition1 == m else nums1[partition1]
            # from list nums2 max from part 2 and min from part 1
            max_left_nums2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right_nums2 = float('inf') if partition2 ==n else nums2[partition2]

            if max_left_nums1<= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                if totallen%2 == 0:
                    return((max(max_left_nums1, max_left_nums2)+min(min_right_nums1,min_right_nums2))/2)
                else:
                    return max(max_left_nums1, max_left_nums2)
            elif max_left_nums1 > min_right_nums2:
                right = partition1 - 1
            else:
                left = partition1 + 1


nums1 = [2,5]
nums2 = [1,3,6,7,8]
sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))







        
