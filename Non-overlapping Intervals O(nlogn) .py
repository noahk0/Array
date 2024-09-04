def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort()
    remove, end = 0, intervals[0][0]

    for interval in intervals:
        if interval[0] < end:
            remove += 1
            end = min(end, interval[1])
        else:
            end = interval[1]

    return remove
