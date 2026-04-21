"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res, count = 0,0
        start = [ inter.start for inter in intervals ]
        end  = [ inter.end for inter in intervals ]
        start.sort()
        end.sort()
        i ,j = 0,0
        while i<len(start):
            if start[i]<end[j]:
                i+=1
                count+=1
            else:
                j+=1
                count-=1
            res = max(res,count)
        return res