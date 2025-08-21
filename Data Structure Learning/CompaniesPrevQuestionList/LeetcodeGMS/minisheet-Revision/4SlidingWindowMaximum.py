from collections import deque

def max_sliding_window(nums, k):
    """Deque keeps indices; front is max. O(n)."""
    dq, out = deque(), []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k: dq.popleft()
        if i >= k-1:
            out.append(nums[dq[0]])
    return out
