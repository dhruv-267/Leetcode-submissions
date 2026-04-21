class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''  GREEDY : O(n+k) 
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
        '''
        res , hmap = [],{}
        for start,end in intervals:
            hmap[start] = max(end,hmap.get(start,end))
        sortedmap = sorted(hmap)

        i =0
        while i <len(sortedmap):
            cur_start = sortedmap[i]
            cur_end = hmap[cur_start]
            j = i+1
            while j<len(sortedmap) and sortedmap[j] <= cur_end:
                cur_end = max(cur_end,hmap[sortedmap[j]])
                j+=1
            res.append([cur_start,cur_end])
            i = j
        return res





        
        