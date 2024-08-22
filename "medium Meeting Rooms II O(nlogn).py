def minMeetingRooms(self, intervals: List[Interval]) -> int:
    day, cur, meeting = 0, 0, []

    for interval in intervals:
        meeting.extend([(interval.start, 1), (interval.end, -1)])

    for _, meet in sorted(meeting):
        cur += meet
        day = max(day, cur)

    return day
