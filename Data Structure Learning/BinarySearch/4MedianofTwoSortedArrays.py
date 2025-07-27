from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        #Lets 1st solve using the brute force algorithm 

        #How to find the median of an two array. Merge the sorted array 1st. 
        """newarr = nums1+nums2
        newarr.sort()
        print(newarr)
        n = len(newarr)
        if n%2 == 0:
            return newarr[n//2]
        else:
            return (newarr[n//2]+newarr[n//2 -1])/2
        """
        #now binar search approch. What i Understood from the video. 
        #We will start checking from the mid of the total len. 
        #for example if nums1 half elements and remaining elements from num2
        # if end element of num1 < start element of num2 
        # if end element of num2 < start element of num1 
        # it will be a valid or sorted list. 

        # 1st step make shorted/ smallest array as num1 array.

        if len(nums1)>len(nums2):
            nums2, nums1 = nums1, nums2

        # 2nd step find the two list or partion between the lists. 

        m = len(nums1)
        n = len(nums2)
        left = 0 
        right = m
        total_len = m+n
        #partion needs to be at half

        while(left<=right):
            partitionI = (left+right)//2
            partitionII = (total_len +1)//2 - partitionI

            # from list nums1 max from part 1and min from part 2
            max_left_nums1 = float('-inf') if partitionI == 0 else nums1[partitionI - 1]
            min_right_nums1 = float('-inf') if partitionI == 0 else nums1[partitionI]
            # from list nums2 max from part 2 and min from part 1
            max_left_nums2 = float('-inf') if partitionII == 0 else nums2[partitionII - 1]
            min_right_nums2 = float('inf') if partitionII ==0 else nums2[partitionII]

            if max_left_nums1<= min_right_nums2 and max_left_nums2 <= min_right_nums2:
                if total_len%2 == 0:
                    return((max(max_left_nums1, max_left_nums2)+max(min_right_nums1,min_right_nums2))//2)
                else:
                    return max(max_left_nums1, max_left_nums2)
            elif max_left_nums1 > min_right_nums2:
                right = partitionI - 1
            else:
                left = partitionII + 1








nums1 = [1,3] 
nums2 = [2,2]
sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))
        
            




"""To implement this we either merge all and find the mid element.
        Is array provided are sorted? 
nums1 = [1,3], nums2 = [2] elements are 3 mid element 3 will be the median

nums1 = [1,2], nums2 = [3,4] element at 2 and 3 is median.


        #Step 1 choose the smallest array. 

        if len(nums2) < len(nums1):
            nums1 , nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        total_Len = m+n

        left = 0
        right = m 
        while left<right:
            partition1 = (left+right)//2
            partition2 = (total_len + 1) // 2 - partition1



        #of both no median will be at 

        

        total_len = len(nums1) + len(nums2) - 2
        med_at = 

        for i in range(total_len)

    """