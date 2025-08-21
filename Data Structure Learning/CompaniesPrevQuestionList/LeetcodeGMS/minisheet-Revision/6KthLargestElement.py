import heapq

def kth_largest(nums, k):
    """Min-heap of size k. O(n log k)."""
    heap = []
    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)
    return heap[0]
