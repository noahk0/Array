def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
    intervals.sort()
    i, heap, size = 0, [], {}

    for query in sorted(set(queries)):
        while i < len(intervals) and intervals[i][0] <= query:
            heappush(heap, (intervals[i][1] - intervals[i][0], intervals[i][1]))
            i += 1

        while heap and heap[0][1] < query:
            heappop(heap)

        if heap:
            size[query] = heap[0][0] + 1

    return [size.get(query, -1) for query in queries]
