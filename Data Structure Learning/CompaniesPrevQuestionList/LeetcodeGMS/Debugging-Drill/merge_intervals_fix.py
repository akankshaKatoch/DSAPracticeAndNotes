def merge(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    res = []
    cur_s, cur_e = intervals[0]
    for s, e in intervals[1:]:
        if s <= cur_e:
            cur_e = max(cur_e, e)
        else:
            res.append([cur_s, cur_e])
            cur_s, cur_e = s, e
    res.append([cur_s, cur_e])
    return res
