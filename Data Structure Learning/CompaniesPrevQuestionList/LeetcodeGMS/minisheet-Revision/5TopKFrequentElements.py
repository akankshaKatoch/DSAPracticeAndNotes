import heapq
from collections import Counter

def top_k_frequent(nums, k):
    """Min-heap of size k. O(n log k)."""
    cnt = Counter(nums)
    heap = []
    for val, f in cnt.items():
        if len(heap) < k:
            heapq.heappush(heap, (f, val))
        else:
            if f > heap[0][0]:
                heapq.heapreplace(heap, (f, val))
    return [v for _, v in heap]
