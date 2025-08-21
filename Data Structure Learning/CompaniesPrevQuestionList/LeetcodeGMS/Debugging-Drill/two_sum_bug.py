def two_sum(nums, target):
    """Return indices of two numbers adding to target; assume exactly one solution.
    Bug(s):
    - Overwrites index before checking pair (fails when same number repeated).
    - Returns indices in wrong order for some cases.
    """
    seen = {}
    for i, x in enumerate(nums):
        seen[x] = i                # BUG: storing before checking breaks duplicates like [3,3], target=6
        complement = target - x
        if complement in seen and seen[complement] != i:
            return [i, seen[complement]]  # order can be odd but acceptable; main bug is above
    return [-1, -1]
