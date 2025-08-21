import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            heapq.heappush(heap, n)

            if len(heap)> k:
                heapq.heappop(heap)

        return heapq.heappop(heap)
    

    def findKthLargestHeapify(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for n in nums[k:]:

            if n>heap[0]:
                heapq.heapreplace(heap, n)

        return heap[0]

