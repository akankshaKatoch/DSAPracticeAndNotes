from typing import List
import heapq 

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        A = sorted(zip(nums2, nums1), reverse= True)

        min_heap = []
        currentSum = 0

        ans = 0

        for num2, num1 in A:
            heapq.heappush(min_heap, num1)
            currentSum += num1
            if len(min_heap) > k:
                currentSum -=  heapq.heappop(min_heap)
            if len(min_heap) == k:
                ans = max(ans, currentSum* num2)

        return ans

sol = Solution()
nums1 = [1,3,3,2]
nums2 = [2,1,3,4]
k = 3
print(sol.maxScore(nums1, nums2, k))
