def merge(intervals):
    """Merge overlapping intervals.
    Bug(s):
    - Sorts by end instead of start; merge condition wrong (uses < not <=).
    """
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[1])  # BUG: should sort by start
    res = [intervals[0]]
    for s, e in intervals[1:]:
        last_s, last_e = res[-1]
        if s < last_e:                  # BUG: should be s <= last_e to merge touching intervals if required
            res[-1][1] = max(last_e, e) # BUG: res[-1] is a list? intervals may be lists; but we unpacked tuple
        else:
            res.append([s, e])
    return res
