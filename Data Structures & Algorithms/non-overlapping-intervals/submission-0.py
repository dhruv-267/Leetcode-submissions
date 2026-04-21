class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)==1:
            return 0
        intervals.sort(key = lambda x : x[0])
        res = 0
        i = 1
        while i < len(intervals):
            if intervals[i-1][1] <= intervals[i][0]:
                i += 1
            else:
                res += 1
                if intervals[i-1][1] > intervals[i][1]:
                    intervals.pop(i-1)
                else:
                    intervals.pop(i)
        return res
