class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        hmap = {}
        for start , end in intervals:
            lenI = end - start + 1
            for i in range(start,end+1):
                hmap[i] = min(lenI,hmap.get(i,lenI))
        res = []
        for q in queries:
            if q in hmap:
                res.append(hmap[q])
            else:
                res.append(-1)
        return res 

        