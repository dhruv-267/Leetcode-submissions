class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        for i in range(1,len(intervals)):
            if intervals[i-1][1]< intervals[i][0]:
                res.append(intervals[i-1])
            else:
                intervals[i][0] = min(intervals[i][0],intervals[i-1][0])
                intervals[i][1] = max(intervals[i][1],intervals[i-1][1])
        res.append([intervals[-1][0],intervals[-1][1]])
        return res

