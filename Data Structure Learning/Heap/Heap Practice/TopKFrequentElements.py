from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        print(freq_map)

        heap = []

        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))
            if len(heap)>k:
                heapq.heappop(heap)

        return [num for freq, num in heap]


nums = [1,1,1,2,2,3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums, k))