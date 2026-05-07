class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if (first-second)!= 0:
                heapq.heappush(stones,first-second)
            
        return abs(stones[0]) if stones else 0
            
"""
#bucket sort optimised algo : O(n+w); w = max weight of stone
# this algo is only efficient for small w values while heap solution works good for even larger w sizes 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        maxw = max(stones)
        freq = [0] * (maxw+1)
        for s in stones:
            freq[s]+=1
        first = second = maxw
        while first > 0:
            if freq[first]%2==0:
                #freq[first] = 0
                first -=1
                continue

            second = min(first-1,second)
            while second>0 and freq[second]==0:
                second-=1
            if second == 0:
                return first
            
            #collision
            #freq[first]=0
            freq[second]-=1
            freq[first-second]+=1
            first = max(first-second,second)
        return first
"""