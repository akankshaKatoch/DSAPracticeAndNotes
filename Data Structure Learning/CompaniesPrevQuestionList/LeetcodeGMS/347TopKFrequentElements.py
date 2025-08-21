import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #freqdict = dict(Counter(nums)) -- counter already gives dict of num and frequency
        counts = Counter(nums)
    
        heap = []
        for num, freq in counts.items():
            if len(heap)<k:
                heapq.heappush(heap, (freq, num))
            else:
                # ** remember this condition check for heap top element 
                if freq > heap[0][0]:
                    heapq.heapreplace(heap, (freq, num))
        
        return [num for _, num in heap]
    
    


sol = Solution()
nums = [1,1,1,2,2,3]
k = 2

print(sol.topKFrequent(nums, k))