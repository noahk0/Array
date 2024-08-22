def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    s = 0
    while s < len(intervals) and intervals[s][1] < newInterval[0]:
        s += 1

    e = s
    while e < len(intervals) and intervals[e][0] <= newInterval[1]:
        e += 1

    return intervals[:s] + [[min(newInterval[0], intervals[s][0]) if s < len(intervals) else newInterval[0], max(newInterval[1], intervals[e - 1][1]) if e else newInterval[1]]] + intervals[e:]
