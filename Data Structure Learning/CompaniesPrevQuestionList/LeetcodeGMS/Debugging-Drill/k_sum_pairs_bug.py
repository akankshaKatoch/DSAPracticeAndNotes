def max_operations(nums, k):
    """Max number of disjoint pairs summing to k.
    Bug(s):
    - Two-pointer assumes sorted but forgot to sort.
    - On equal sum, moves only left or right incorrectly.
    """
    i, j = 0, len(nums) - 1
    ops = 0
    # BUG: forgot to sort
    while i < j:
        s = nums[i] + nums[j]
        if s == k:
            ops += 1
            i += 1            # BUG: should move both pointers
        elif s < k:
            i += 1
        else:
            j -= 1
    return ops
