def lower_bound(a, x):
    """First idx >= x. O(log n)."""
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi)//2
        if a[mid] < x: lo = mid + 1
        else: hi = mid
    return lo

def upper_bound(a, x):
    """First idx > x. O(log n)."""
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi)//2
        if a[mid] <= x: lo = mid + 1
        else: hi = mid
    return lo
