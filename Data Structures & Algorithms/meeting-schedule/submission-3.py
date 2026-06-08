"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda time: time.end)

        end_first = intervals[0].end if intervals else 0

        for i in range(1, len(intervals)):
            start_next = intervals[i].start
            if end_first > start_next:
                return False
            else:
                end_first = intervals[i].end
        
        return True
