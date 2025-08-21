def subarray_sum(nums, k):
    """Count subarrays summing to k.
    Bug(s):
    - Resets prefix map on encountering zero / negative (shouldn't).
    - Off-by-one initializing prefix counts.
    """
    count = 0
    prefix = 0
    freq = {}   # BUG: should start with {0:1}
    for x in nums:
        prefix += x
        need = prefix - k
        if need in freq:
            count += freq[need]
        if x == 0:
            freq = {}              # BUG: don't reset map on zero
        freq[prefix] = freq.get(prefix, 0) + 1
    return count
