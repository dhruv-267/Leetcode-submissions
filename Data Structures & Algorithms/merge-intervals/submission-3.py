class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        hashmap = {}
        minstart = math.inf
        maxend = 0
        for start,end in intervals:
            hashmap[start] = max(end,hashmap.get(start,end))
            minstart = min(minstart,start)
            maxend = max(maxend,end)
        i = minstart
        while i <= maxend:
            if i in hashmap:
                j = i
                while j <= hashmap[i]:
                    if j in hashmap:
                        hashmap[i] = max(hashmap[i],hashmap[j])
                    j+=1 
                res.append([i,hashmap[i]])
                i = 1 + hashmap[i]
            else:
                i+=1
        return res
                    
                

        
        