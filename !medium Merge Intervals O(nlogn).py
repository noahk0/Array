def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    new = [intervals[0]]

    for interval in intervals[1:]:
        if new[-1][1] < interval[0]:
            new.append(interval)
        else:
            new[-1][1] = max(new[-1][1], interval[1])

    return new
