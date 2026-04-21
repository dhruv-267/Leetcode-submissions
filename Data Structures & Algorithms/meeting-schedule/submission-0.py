"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)<=1:
            return True
        intervals.sort(key= lambda x:x.start)
        prevEnd = intervals[0].end
        for inter in intervals[1:]:
            if inter.start <prevEnd:
                return False
            prevEnd = inter.end
        return True

